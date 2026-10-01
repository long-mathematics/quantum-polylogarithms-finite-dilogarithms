#!/usr/bin/env python3
"""Supplementary checks for the Paper B research draft.

These calculations check conventions and selected numerical instances. They are
not proofs or rigorous numerical enclosures. Run with Python 3.10 or later and
numpy, sympy, and mpmath installed. The JSON report is written next to this file
unless --output is supplied.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import mpmath as mp
import numpy as np
import sympy as sp
from numpy.polynomial.legendre import leggauss


def symbolic_checks() -> dict[str, Any]:
    """Check axis-sector normalization identities by exact symbolic reduction."""
    u = sp.symbols("u")
    l1 = -sp.exp(u) / (1 + sp.exp(u))
    l2 = u / (2 * sp.pi * sp.I) * sp.exp(u) / (1 - sp.exp(u))
    l3 = (u**2 + sp.pi**2) / (2 * (2 * sp.pi * sp.I)**2) * l1

    def shift(f: sp.Expr, v: sp.Expr) -> sp.Expr:
        return sp.simplify(f.subs(u, u + v))

    ipi = sp.I * sp.pi
    identities = {
        "terminal_lowering": shift(l1, ipi) - shift(l1, -ipi),
        "lowering_a2": shift(l2, ipi) - shift(l2, -ipi) - l1,
        "multiplication_a1": u*l1 - ipi*(shift(l2, ipi) + shift(l2, -ipi)),
        "multiplication_a2": u*l2 - 2*ipi*(shift(l3, ipi) + shift(l3, -ipi)),
        "reflection_a1": l1 + l1.subs(u, -u) + 1,
    }
    report: dict[str, Any] = {}
    for name, expression in identities.items():
        remainder = sp.simplify(expression)
        if remainder != 0:
            raise AssertionError(f"{name}: nonzero symbolic remainder {remainder}")
        report[name] = "exact symbolic identity"
    return report


def kernel(p: Any, a: int, b: int, h: Any) -> Any:
    return 1 / ((2*mp.sinh(mp.pi*p))**a * (2*mp.sinh(mp.pi*h*p))**b)


def letter_line(w: Any, a: int, b: int, h: Any, eta: Any) -> Any:
    """Integrate on a fixed horizontal line strictly above the origin."""
    return -mp.j * mp.quad(
        lambda t: mp.exp(-mp.j*(t+mp.j*eta)*w)*kernel(t+mp.j*eta, a, b, h),
        [-mp.inf, -2, 0, 2, mp.inf],
    )


def letter_tails(w: Any, a: int, b: int, h: Any, rho: Any, terms: int) -> Any:
    """Truncate both normally convergent tail series, retaining the detour."""
    if terms < 1 or not (0 < rho < min(1, 1/h)):
        raise ValueError("Invalid truncation size or detour radius")

    def arc_integrand(theta: Any) -> Any:
        p = rho*mp.exp(mp.j*theta)
        return mp.exp(-mp.j*p*w)*kernel(p, a, b, h)*mp.j*p

    # The upper semicircle runs clockwise from -rho to +rho.
    total = -mp.j*mp.quad(arc_integrand, [mp.pi, 0])
    for m in range(terms):
        cm = mp.binomial(a+m-1, m) if a else int(m == 0)
        for n in range(terms):
            cn = mp.binomial(b+n-1, n) if b else int(n == 0)
            if not cm*cn:
                continue
            A = mp.pi*(a+2*m+h*(b+2*n))
            total += -mp.j*cm*cn*(
                mp.exp(-rho*(A+mp.j*w))/(A+mp.j*w)
                + (-1)**(a+b)*mp.exp(-rho*(A-mp.j*w))/(A-mp.j*w)
            )
    return total


def tail_checks() -> dict[str, Any]:
    h, w = mp.sqrt(2), mp.mpf("-0.7")
    eta, rho, terms = mp.mpf(".23"), mp.mpf(".3"), 60
    report: dict[str, Any] = {}
    for a, b in [(1, 1), (2, 1)]:
        direct = letter_line(w, a, b, h, eta)
        expanded = letter_tails(w, a, b, h, rho, terms)
        error = abs(direct-expanded)
        if error >= mp.mpf("1e-30"):
            raise AssertionError(f"Mixed-tail comparison failed: {(a,b)}, {error}")
        report[f"tail_a{a}_b{b}"] = {
            "error": mp.nstr(error, 8),
            "line_value": mp.nstr(direct, 25),
            "h": "sqrt(2)", "argument": str(w),
            "height": str(eta), "radius": str(rho), "terms_per_index": terms,
        }
    return report


def laplace_checks() -> dict[str, Any]:
    """Compare 2D momentum quadrature with 1D Chen integrals in the axis sector.

    The b=0 sector allows an independent elementary/polylogarithmic inner
    primitive. Increasing Gauss-Legendre node counts checks numerical stability;
    the reported differences are not certified error bounds.
    """
    x, d1, d2 = mp.mpf("-.7"), mp.mpf(".3"), mp.mpf("0")
    report: dict[str, Any] = {}

    def logistic(t: Any) -> Any:
        return -mp.exp(t)/(1+mp.exp(t))

    for n1, n2 in [(1, 1), (1, 2), (2, 1)]:
        if n1 == 1:
            def inner(t: Any) -> Any:
                return -mp.log(1+mp.exp(t+d1))
        else:
            def inner(t: Any) -> Any:
                return mp.polylog(2, -mp.exp(t+d1))

        chen = mp.quad(
            lambda t: inner(t)*logistic(t+d2)*(x-t)**(n2-1)/mp.factorial(n2-1),
            [-mp.inf, x],
        )
        entries = []
        cutoff, height = 10.0, 0.35
        for nodes in [200, 400, 700]:
            v, qw = leggauss(nodes)
            p, qw = cutoff*v+1j*height, cutoff*qw
            k1 = np.exp(-1j*p*float(x+d1))/(2*np.sinh(np.pi*p))
            k2 = np.exp(-1j*p*float(x+d2))/(2*np.sinh(np.pi*p))
            value = (1j)**(n1+n2-2)*np.sum(
                (qw*k1/(p**n1))[:, None]*(qw*k2)[None, :]
                / ((p[:, None]+p[None, :])**n2)
            )
            error = abs(complex(chen)-value)
            entries.append({"nodes": nodes, "error": float(error),
                            "real": float(value.real), "imag": float(value.imag)})
        if entries[-1]["error"] >= 2e-11:
            raise AssertionError(f"Depth-two Laplace comparison failed: {entries}")
        report[f"laplace_depth2_{n1}{n2}"] = {
            "chen": mp.nstr(chen, 25), "momentum_checks": entries,
            "real_cutoff": cutoff, "height": height,
            "arguments": [str(x+d1), str(x+d2)], "kernel_pairs": [[1, 0], [1, 0]],
        }
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().with_name("checks_results.json"))
    args = parser.parse_args()
    mp.mp.dps = 40
    results: dict[str, Any] = {
        "disclaimer": "Sanity checks only; not proofs or rigorous numerical enclosures.",
        "versions": {"numpy": np.__version__, "sympy": sp.__version__,
                     "mpmath": mp.__version__},
        "decimal_precision": mp.mp.dps,
    }
    results.update(symbolic_checks())
    results.update(tail_checks())
    results.update(laplace_checks())
    payload = json.dumps(results, indent=2) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")
    print(f"All checks completed; report: {args.output}")


if __name__ == "__main__":
    main()
