# Source and version provenance

## This release

The initial GitHub release is dated **October 1, 2026**. Earlier dates in the research history are drafting dates, not claims of public availability or priority. Both public manuscripts name Christopher D. Long as author.

The functional manuscript is based on the September 22, 2026, sole-author version 2 of *Rational-Exponential Iterated Integrals and Quantum Polylogarithms*. It includes the absolute fixed-parameter coefficient-field extension. The alternate titles *Quantum Polylogarithms: Residue Modules, Iterated Integrals, and Pentagon Operators* and *Quantum Fourier Letters and Iterated Integrals* refer to earlier formulations, not additional papers in this release.

The finite-equation manuscript is based on the September 21, 2026 working note *Finite quantum dilogarithms: normalization exceptions, infinitesimal rigidity, and effective degree bounds*. The release makes its general infinitesimal criterion explicitly conditional, retains the unconditional low-order certificates and degree bounds, and updates the current-source comparison.

## Primary references checked for the release

- Danylo Radchenko and Campbell Wheeler, *Real quadratic fields and finite quantum dilogarithms I*, [arXiv:2609.21892](https://arxiv.org/abs/2609.21892). Version 1 was submitted September 18, 2026; version 2 September 29, 2026. Current Theorem 5 is for order greater than four; Remark 3 explicitly records exceptional raw-equation solutions at small orders and the additional normalization convention. The finite paper retains explicit historical version-1 references where its raw equation and earlier proof are being discussed. Equation numbering must not be transferred silently between versions or renderings.
- Marcus Appleby, Steven T. Flammia, and Gene S. Kopp, *The twisted convolution identity and ghost r-SICs from finite quantum dilogarithms*, [arXiv:2609.39192v1](https://arxiv.org/abs/2609.39192v1), September 30, 2026. The all-admissible-rank twisted convolution identity and cocycle dictionary are background, not claimed as results of either manuscript here.
- Alexander B. Goncharov, *Quantum polylogarithms*, [arXiv:2601.00472v1](https://arxiv.org/abs/2601.00472v1), January 1, 2026. The Fourier integrals, modular difference equations, and existing shuffle structure originate in this work.
- Alexander B. Goncharov, *The pentagon relation for the quantum dilogarithm and quantized M0,5*, [arXiv:0706.4054](https://arxiv.org/abs/0706.4054). The operator appendix specifies the version and imported common-domain/covariance results.
- Pavel Etingof, Dmitri Nikshych, and Viktor Ostrik, *On fusion categories*, [arXiv:math/0203060](https://arxiv.org/abs/math/0203060), Annals of Mathematics 162 (2005), 581–642. The finite-paper conditional argument uses first-order rigidity, not merely finiteness of equivalence classes.

The bibliographies also credit the classical iterated-integral, shuffle, difference-algebra, and categorical ingredients. This focused source check does not establish literature-wide novelty. In particular, algebraicity and finiteness were already goals/results of RW v1; they should not be described as results of this project lost only when v2 appeared.

## Computational provenance

The original exact finite verifier and the recovered functional verification scripts are included with their scope disclaimers. All three functional runs (exact, mixed-contour, and earlier contour/Laplace comparisons) and the finite verifier were executed again for this release. Reports in `verification/` describe the actual checks and software environment; no earlier numerical exploration is promoted to a certificate without a reproducible script.
