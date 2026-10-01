#!/usr/bin/env python3
"""Check local citation/label consistency and revision-specific references.

This validates manuscript bookkeeping, not the truth of cited theorems or
mathematical arguments. Source verification is recorded in CITATION_AUDIT.md.
"""
from __future__ import annotations

import argparse
import collections
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
COMMON = {"Huang2026", "GSY2026", "AFK2025", "Kopp2024"}


def check(path: Path) -> dict[str, object]:
    text = path.read_text()
    bad_controls = sorted({ord(c) for c in text if ord(c) < 32 and c not in "\n\r\t"})
    if bad_controls:
        raise AssertionError(f"{path.name}: unexpected control characters: {bad_controls}")
    body = re.sub(r"(?<!\\)%[^\n]*", "", text)
    bib = re.findall(r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}", body)
    labels = re.findall(r"\\label\{([^}]+)\}", body)
    for kind, values in (("bibliography key", bib), ("label", labels)):
        duplicates = [k for k, n in collections.Counter(values).items() if n > 1]
        if duplicates:
            raise AssertionError(f"{path.name}: duplicate {kind}: {duplicates}")
    cited = set()
    for entry in re.findall(r"\\cite\w*(?:\[[^\]]*\])*\{([^}]+)\}", body):
        cited.update(k.strip() for k in entry.split(","))
    referenced = set()
    for entry in re.findall(r"\\(?:[cC]ref|eqref|ref)\*?\{([^}]+)\}", body):
        referenced.update(k.strip() for k in entry.split(","))
    if cited - set(bib):
        raise AssertionError(f"{path.name}: missing bibliography entries: {cited-set(bib)}")
    if referenced - set(labels):
        raise AssertionError(f"{path.name}: undefined labels: {referenced-set(labels)}")
    required = COMMON | ({"Seki2026", "BGMS2026"} if "polylogarithms" in path.name
                         else {"EvansGannon2017"})
    if required - cited:
        raise AssertionError(f"{path.name}: uncited required literature: {required-cited}")
    if "hyp:realization" in body or r"\begin{hypothesis}" in body:
        raise AssertionError(f"{path.name}: obsolete realization hypothesis remains")
    if "an Infinitesimal Rigidity Criterion" in body:
        raise AssertionError(f"{path.name}: obsolete companion title remains")
    return {"file": path.relative_to(ROOT).as_posix(), "status": "passed",
            "bibliography_entries": len(bib), "cited_keys": len(cited),
            "labels": len(labels), "unused_bibliography_keys": sorted(set(bib)-cited)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = {"status": "passed", "papers": [check(p) for p in sorted((ROOT/'papers').glob('*.tex'))],
              "scope": "Citation and label bookkeeping, not mathematical or external-source verification."}
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
