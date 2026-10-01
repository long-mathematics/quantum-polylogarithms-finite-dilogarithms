"""One-shot citation edit, pinned to the merged proof revision; removed after use."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

BASE = 'd3cb0989d12988b507c6126e03488e0c2ebb2f78'
ROOT = Path('.')
EXPECTED = {
    'papers/finite_quantum_dilogarithms.tex': 'd8178591db8f8e605588ef248aa3e5bccd7c12f2',
    'papers/quantum_polylogarithms.tex': '61522a63ac35e59200cff6185d4175ab4f7b4e7b',
}

def once(text, old, new):
    assert text.count(old) == 1, (old[:100], text.count(old))
    return text.replace(old, new, 1)

before = {}
for name, expected in EXPECTED.items():
    data = (ROOT/name).read_bytes()
    actual = hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    assert actual == expected, (name, actual, expected)
    before[name] = data.decode()

common = r'''
\bibitem{Huang2026}
T.-C.~Huang,
\emph{Cyclic Haagerup--Izumi fusion categories at every odd order},
\href{https://arxiv.org/abs/2609.15986v1}{arXiv:2609.15986v1}, September 14, 2026.

\bibitem{GSY2026}
T.~Gannon, A.~Schopieray, and H.~Yadav,
\emph{On Haagerup--Izumi fusion categories},
\href{https://arxiv.org/abs/2609.25185v1}{arXiv:2609.25185v1}, September 21, 2026.

\bibitem{AFK2025}
M.~Appleby, S.~T.~Flammia, and G.~S.~Kopp,
\emph{A Constructive Approach to Zauner's Conjecture via the Stark Conjectures},
\href{https://arxiv.org/abs/2501.03970v2}{arXiv:2501.03970v2}, March 17, 2025.
First version: January 7, 2025.

\bibitem{Kopp2024}
G.~S.~Kopp,
\emph{The Shintani--Faddeev modular cocycle: Stark units from $q$-Pochhammer ratios},
\href{https://arxiv.org/abs/2411.06763v3}{arXiv:2411.06763v3}, May 3, 2025.
First version: November 11, 2024.
'''

p = ROOT/'papers/finite_quantum_dilogarithms.tex'
s = before[p.as_posix()]
s = once(s, 'Research draft, audited infinitesimal-rigidity revision',
         'Research draft, audited proof and revised references')
intro = r'''\paragraph{Concurrent and related developments.}
Huang \cite{Huang2026} and Gannon--Schopieray--Yadav \cite{GSY2026}
construct cyclic Haagerup--Izumi categories by double-sine/Fourier identities
and categorical reconstruction. Their HI fusion rules are different from
the near-group rules used here; they are not simply alternative
presentations of our raw finite-QD scheme. Gannon--Schopieray--Yadav also
give a Leavitt reconstruction over algebraically closed fields in arbitrary
characteristic \cite[Theorems~2.5 and~B.20]{GSY2026}, and some auxiliary
identities already hold over commutative rings \cite[Theorem~A.3]{GSY2026}.
This is closely related algebraic precedent. Our additional task is to
control the normalized RW equations over a nonreduced base, their flat
category deformation, and the scalar invariant under its trivializing gauge.
The earlier algebraic endomorphism method is due to Evans--Gannon
\cite{EvansGannon2017}; we use the specific realization of \cite{RW2}.

Kopp's cocycle interpretation \cite{Kopp2024} and the conditional Stark/SIC
framework of Appleby--Flammia--Kopp \cite{AFK2025} supply earlier arithmetic
context. The later AFK paper proves the all-admissible-rank twisted
convolution identity and ghost $r$-SIC construction, and gives the
RW/Shintani--Faddeev convention dictionary \cite[Theorem~1.3 and
Proposition~2.1]{AFK}. The scheme-theoretic rigidity and effective bounds
studied here do not identify a Stark reciprocity law or produce the required
unitary Galois conjugates.

'''
s = once(s, r'The companion functional paper \cite{LongQuantum}',
         intro+r'The companion functional paper \cite{LongQuantum}')
s = once(s, r'\bibitem{LongQuantum}', common+r'''
\bibitem{EvansGannon2017}
D.~E.~Evans and T.~Gannon,
\emph{Non-unitary fusion categories and their doubles via endomorphisms},
Advances in Mathematics \textbf{310} (2017), 1--43;
\href{https://arxiv.org/abs/1506.03546}{arXiv:1506.03546}.

\bibitem{LongQuantum}''')
p.write_text(s)

p = ROOT/'papers/quantum_polylogarithms.tex'
s = before[p.as_posix()]
s, n = re.subn(r'Research draft,[^}\n]*', 'Research draft, revised references', s, count=1)
assert n == 1
intro = r'''\subsection{Concurrent and related developments}

Other $q$-deformations of iterated integrals address related but different
questions. Seki proves Hirose's duality conjecture for a $q$-discretization
on the four-punctured projective line, with word-dependent parameter shifts,
using a terminating basic-hypergeometric connector \cite{Seki2026}.
Bl\"umlein--Gavrilik--Mykhailiv--Schneider construct $q$-extensions of
iterated-integral alphabets and nested sums motivated by quantum field
theory \cite{BGMS2026}. We cite these as distinct deformation theories;
we neither identify their functions with Goncharov's Fourier integrals
nor use their word identities to obtain the completeness theorem here.

The contemporaneous double-sine constructions of cyclic Haagerup--Izumi
categories by Huang \cite{Huang2026} and Gannon--Schopieray--Yadav
\cite{GSY2026} belong to the finite categorical side of this subject.
They provide important context for the arithmetic direction, not inputs
to the fixed-parameter residue, coefficient-field, or shuffle proofs below.
The relation to RW and the Stark/SIC literature is specified in the
arithmetic-motivation subsection.

'''
s = once(s, r'\subsection{The functions and the common translation variable}',
         intro+r'\subsection{The functions and the common translation variable}')
s = once(s, r'''Appleby--Flammia--Kopp extend the rank-one twisted convolution identity to all
admissible ranks and give a dictionary with the Shintani--Faddeev modular
cocycle \cite{ApplebyFlammiaKopp2026}. These finite identities and their
arithmetic applications are background here, not conclusions of this paper.''', r'''Kopp interprets real-quadratic Stark class invariants using the
Shintani--Faddeev modular cocycle \cite{Kopp2024}.
Appleby--Flammia--Kopp's earlier work gives the conditional Stark/ghost-SIC
and rank-$r$ framework \cite{AFK2025}; their later paper proves the
all-admissible-rank twisted convolution identity and supplies the
RW/Shintani--Faddeev dictionary \cite[Theorem~1.3 and
Proposition~2.1]{ApplebyFlammiaKopp2026}. These finite identities and their
arithmetic applications are background, not conclusions of this paper.''')
s = once(s, r'\bibitem{LongFinite2026}', common+r'''
\bibitem{Seki2026}
S.-i.~Seki,
\emph{A proof of Hirose's duality conjecture},
\href{https://arxiv.org/abs/2609.40213v1}{arXiv:2609.40213v1}, September 30, 2026.

\bibitem{BGMS2026}
J.~Bl\"umlein, A.~M.~Gavrilik, O.~Mykhailiv, and C.~Schneider,
\emph{The $q$-extension of iterated integrals and nested sums in quantum field theory},
\href{https://arxiv.org/abs/2608.02702v1}{arXiv:2608.02702v1}, August 3, 2026.

\bibitem{LongFinite2026}''')
p.write_text(s)

# Preserve the recently merged mathematical statements and proof bodies exactly.
pattern = r'\\begin\{(theorem|lemma|proposition|corollary|proof)\}.*?\\end\{\1\}'
checks = []
for name, old in before.items():
    new = (ROOT/name).read_text()
    old_blocks = [m.group(0) for m in re.finditer(pattern, old, re.S)]
    new_blocks = [m.group(0) for m in re.finditer(pattern, new, re.S)]
    assert old_blocks and old_blocks == new_blocks, name
    if 'finite_' in name:
        core = lambda t: t[t.index(r'\section{The raw solution scheme}'):t.index(r'\begin{thebibliography}')]
        assert core(old) == core(new), 'finite mathematical core changed'
    checks.append({'file': name, 'unchanged_mathematical_environments': len(old_blocks),
                   'sha256': hashlib.sha256(new.encode()).hexdigest()})

p = ROOT/'README.md'; s = p.read_text()
s = once(s, 'See [research status](RESEARCH_STATUS.md),',
    'The related-work discussion also distinguishes Huang and Gannon–Schopieray–Yadav on HI categories, the earlier AFK Stark/SIC framework, Kopp’s Shintani–Faddeev cocycle, and the different q-iterated-integral theories of Seki and Blümlein–Gavrilik–Mykhailiv–Schneider. The [citation audit](CITATION_AUDIT.md) records versions, theorem pointers, and the distinction between proof dependencies and contextual references. In particular, GSY already has commutative-ring identities as well as field-based reconstruction statements.\n\nSee [research status](RESEARCH_STATUS.md),')
s = once(s, 'python scripts/verify_rigidity_identities.py\n',
    'python scripts/verify_rigidity_identities.py\npython scripts/check_manuscript_integrity.py --output verification/manuscript_integrity.json\n')
s = once(s, 'Both compiled PDFs are intentionally tracked.',
    'The manuscript-integrity check validates bibliography keys, labels, required related-work citations, and accidental control characters; it is not a mathematical or exhaustive literature check. Both compiled PDFs are intentionally tracked.')
p.write_text(s)

p = ROOT/'Makefile'; s = p.read_text()
s = once(s, '$(PYTHON) scripts/verify_rw_extensions.py > verification/finite_exact.txt',
    '$(PYTHON) scripts/verify_rw_extensions.py > verification/finite_exact.txt\n\t$(PYTHON) scripts/check_manuscript_integrity.py --output verification/manuscript_integrity.json')
p.write_text(s)

p = ROOT/'PROVENANCE.md'; s = p.read_text()
s += '\n## Concurrent-literature revision\n\nThe citation revision is based on the merged proof commit `d3cb0989d12988b507c6126e03488e0c2ebb2f78` (PR #3). It preserves the finite-paper mathematical core and both papers’ theorem/proof environments exactly. It adds contextual discussion and bibliography entries for Huang, Gannon–Schopieray–Yadav, earlier AFK, Kopp, Seki, and Blümlein–Gavrilik–Mykhailiv–Schneider, and explicitly credits Evans–Gannon’s algebraic precedent. The complete version and scope record is [CITATION_AUDIT.md](CITATION_AUDIT.md).\n\nIn particular, GSY Theorem A.3 is already a commutative-ring identity; the discussion does not incorrectly describe all of GSY as field-only. Its HI equations are not identified with the raw near-group scheme in this project. The original release remains unchanged.\n'
p.write_text(s)
p = ROOT/'RESEARCH_STATUS.md'; s = p.read_text()
s += '\n## Related-work scope and revision integrity\n\nThe [citation audit](CITATION_AUDIT.md) distinguishes concurrent HI constructions, the general finite-QD theory, Stark/cocycle motivation, and distinct q-iterated-integral theories. None of these contextual citations is presented as a proof of our generic-to-arithmetic specialization problem. The citation revision preserves the merged proof and both papers’ theorem/proof environments; its exact preservation check is recorded in `verification/CITATION_REVISION_CHECKS.json`.\n'
p.write_text(s)
p = ROOT/'RELEASE_NOTES.md'; s = p.read_text()
s = '# Unreleased — citation and provenance audit (October 1, 2026)\n\nExpand both manuscripts with concurrent and related developments. Add Huang, Gannon–Schopieray–Yadav, earlier AFK, Kopp, Seki, and Blümlein–Gavrilik–Mykhailiv–Schneider, and explicitly credit Evans–Gannon in the finite paper. Preserve the audited proof merged in PR #3, including all generator formulas and regression checks. The citation discussion distinguishes GSY’s commutative-ring identities from its field-based reconstruction, and avoids identifying different fusion rules or different q-deformations.\n\nSynchronize the README, provenance, research status, and citation guidance; add the source/version audit and reproducible bibliography/cross-reference checks. Both PDFs and verification outputs are rebuilt. No release tag or historical asset is rewritten.\n\n---\n\n'+s
p.write_text(s)
p = ROOT/'CITATION.cff'; s = p.read_text()
s = once(s, 'use this entry for the repository collection.',
    'use this entry for the repository collection and specify the commit or release consulted. Source/version details are recorded in CITATION_AUDIT.md.')
p.write_text(s)

report = {'base_commit': BASE, 'scope': 'Citation-only revision on the merged rigidity proof; not independent mathematical verification.',
          'status': 'passed', 'manuscripts': checks, 'finite_mathematical_core_unchanged': True,
          'historical_release_unchanged': True}
(ROOT/'verification/CITATION_REVISION_CHECKS.json').write_text(json.dumps(report, indent=2, sort_keys=True)+'\n')
print(json.dumps(report, indent=2))
