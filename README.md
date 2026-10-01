# Quantum Polylogarithms and Finite Quantum Dilogarithms

Christopher D. Long · [galizur@gmail.com](mailto:galizur@gmail.com)

Two research manuscripts on functional relations, iterated integrals, finite quantum-dilogarithm equations, and arithmetic rigidity. Initial public research-draft release: **October 1, 2026**.

## Manuscripts

### 1. Rational-Exponential Iterated Integrals and Quantum Polylogarithms

*Absolute fixed-parameter completeness and a pentagon crossed product*

[PDF](papers/quantum_polylogarithms.pdf) · [LaTeX source](papers/quantum_polylogarithms.tex)

For a fixed positive irrational parameter and finitely many fixed offsets, the paper presents the translated Fourier-letter space by a two-variable localization modulo Laurent polynomials. Residue detection gives meromorphic de Rham injectivity. A controlled Laplace–Chen transform and a word-independence argument give shuffle completeness along a common translation variable. An additive-difference and pole-orbit argument presents the nonlinear weight-zero differential field, yielding an absolute functional presentation over `C(x)`. A separate appendix proves a faithful pentagon crossed-product normal form.

Here **absolute** means that the functional coefficient field is explicitly presented. It does not mean a numerical period theorem, arithmetic specialization, moving-parameter completeness, or a scalar action of quantum-cluster mutations.

### 2. Finite Quantum Dilogarithms

*Normalization Exceptions, Effective Degree Bounds, and an Infinitesimal Rigidity Criterion*

[PDF](papers/finite_quantum_dilogarithms.pdf) · [LaTeX source](papers/finite_quantum_dilogarithms.tex)

The paper studies the **raw** finite equations, including small-order points excluded by an additional normalization convention. It gives exact exceptional solutions, complete saturated calculations for two low-order metrics, Fourier–Weil eigenspace degree bounds, and an elementary recovery of a known elementary-abelian two-group obstruction.

**The general finite-étale theorem is conditional on Hypothesis 3.1**, a specified realization and reconstruction statement over dual numbers. The small-order certificates and degree bounds do not depend on that hypothesis. No general reducedness, Stark reciprocity, or unitary Galois-conjugate theorem is announced unconditionally.

## Status and attribution

These manuscripts were developed with AI assistance and checked internally. They have not been independently refereed or formally verified. Exact computations certify the finite statements specified in the scripts; numerical comparisons are sanity checks, not proofs or interval enclosures.

Radchenko–Wheeler's finite pentagon, algebraicity, and finiteness results, and Appleby–Flammia–Kopp's all-rank twisted-convolution result and modular-cocycle dictionary, are cited background. The small-order normalization exceptions are acknowledged in Radchenko–Wheeler v2, Remark 3; this release makes no priority claim for noticing them.

See [research status](RESEARCH_STATUS.md) and [source/version provenance](PROVENANCE.md) for exact boundaries.

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
python scripts/checks_absolute.py --mode exact --output verification/quantum_exact.json
python scripts/checks_absolute.py --mode numeric --output verification/quantum_numeric.json
python scripts/checks_v1.py --output verification/quantum_contours.json
```

`checks_v1.py` retains its historical filename; its contour and normalization tests remain applicable to the current functional manuscript. The tracked [verification reports](verification/) record the initial release runs. Both compiled PDFs are intentionally tracked. Build artifacts such as `.aux` and `.log` files are ignored.

## Contents

- `papers/`: the two standalone LaTeX sources and their PDFs.
- `scripts/`: exact finite certificates and supplementary analytic checks.
- `verification/`: outputs and environment information from the release checks.
- `.github/workflows/verification.yml`: repeatable verification and PDF builds.
- `CITATION.cff`: citation metadata for the repository collection.

## License

[MIT](LICENSE), as selected when the repository was created. Third-party papers are cited, not redistributed in this repository.
