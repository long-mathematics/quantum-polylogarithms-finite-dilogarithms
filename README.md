# Quantum Polylogarithms and Finite Quantum Dilogarithms

Christopher D. Long · [galizur@gmail.com](mailto:galizur@gmail.com)

Two research manuscripts on functional relations, iterated integrals, finite quantum-dilogarithm equations, and arithmetic rigidity. Initial public research-draft release: **October 1, 2026**. The current main-branch revision incorporates the audited infinitesimal-rigidity proof; the historical `v0.1.0` release remains unchanged.

## Manuscripts

### 1. Rational-Exponential Iterated Integrals and Quantum Polylogarithms

*Absolute fixed-parameter completeness and a pentagon crossed product*

[PDF](papers/quantum_polylogarithms.pdf) · [LaTeX source](papers/quantum_polylogarithms.tex)

For a fixed positive irrational parameter and finitely many fixed offsets, the paper presents the translated Fourier-letter space by a two-variable localization modulo Laurent polynomials. Residue detection gives meromorphic de Rham injectivity. A controlled Laplace–Chen transform and a word-independence argument give shuffle completeness along a common translation variable. An additive-difference and pole-orbit argument presents the nonlinear weight-zero differential field, yielding an absolute functional presentation over `C(x)`. A separate appendix proves a faithful pentagon crossed-product normal form.

Here **absolute** means that the functional coefficient field is explicitly presented. It does not mean a numerical period theorem, arithmetic specialization, moving-parameter completeness, or a scalar action of quantum-cluster mutations.

### 2. Finite Quantum Dilogarithms

*Normalization Exceptions, Infinitesimal Rigidity, and Effective Degree Bounds*

[PDF](papers/finite_quantum_dilogarithms.pdf) · [LaTeX source](papers/finite_quantum_dilogarithms.tex)

The paper studies the **raw** finite equations, including small-order points excluded by an additional normalization convention. It gives exact exceptional solutions, complete saturated calculations for two low-order metrics, Fourier–Weil eigenspace degree bounds, and an elementary recovery of a known elementary-abelian two-group obstruction.

**Theorem 3.1 proves finite étaleness of the actual raw solution scheme**, including reducedness of the localized defining ideal. The proof discharges the initial release’s Hypothesis 3.1 by a universal-ring Leavitt realization, a flat split skeleton, and normalized scalar reconstruction invariant under strong monoidal equivalences. It records the corrected completeness coefficient in RW v2 and includes the associator/tensorator argument. The exact low-order certificates and degree bounds remain logically independent of this proof. No Stark reciprocity or unitary Galois-conjugate theorem is asserted.

## Status and attribution

These manuscripts were developed with AI assistance and checked internally. They have not been independently refereed or formally verified. Exact computations certify the finite statements specified in the scripts; numerical comparisons are sanity checks, not proofs or interval enclosures.

Radchenko–Wheeler's finite pentagon, algebraicity, and finiteness results, and Appleby–Flammia–Kopp's all-rank twisted-convolution result and modular-cocycle dictionary, are cited background. The small-order normalization exceptions are acknowledged in Radchenko–Wheeler v2, Remark 3; this release makes no priority claim for noticing them.

See [research status](RESEARCH_STATUS.md), [source/version provenance](PROVENANCE.md), and the [focused realization/reconstruction audit](audits/2026-10-01-hypothesis-3-1.md) for exact boundaries.

## Reproducible checks

Use Python 3.11 or later and a TeX Live installation with pdfLaTeX and `latexmk`. Python 3.13 is used by CI.

```sh
python -m pip install -r requirements.txt
make verify
make papers
```

The individual checks are:

```sh
python scripts/verify_rw_extensions.py
python scripts/verify_rigidity_identities.py
python scripts/checks_absolute.py --mode exact --output verification/quantum_exact.json
python scripts/checks_absolute.py --mode numeric --output verification/quantum_numeric.json
python scripts/checks_v1.py --output verification/quantum_contours.json
```

`checks_v1.py` retains its historical filename; its contour and normalization tests remain applicable to the current functional manuscript. The tracked [verification reports](verification/) include the current regression runs; `RELEASE_CHECKS.json` remains the historical initial-release record. The new rigidity checks cover scalar identities, representative character projectors, and formal reconstruction contractions. They do not certify the arbitrary-group categorical proof. Both compiled PDFs are intentionally tracked. Build artifacts such as `.aux` and `.log` files are ignored.

## Contents

- `papers/`: the two standalone LaTeX sources and their PDFs.
- `scripts/`: exact finite certificates, rigidity regression checks, and supplementary analytic checks.
- `audits/`: the focused ring-level and monoidal-gauge audit.
- `verification/`: outputs and environment information from the release checks.
- `.github/workflows/verification.yml`: repeatable verification and PDF builds.
- `CITATION.cff`: citation metadata for the repository collection.

## License

[MIT](LICENSE), as selected when the repository was created. Third-party papers are cited, not redistributed in this repository.
