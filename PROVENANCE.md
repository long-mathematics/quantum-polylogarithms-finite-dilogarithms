# Source and version provenance

## Release history and current revision

The initial GitHub release is dated **October 1, 2026**. Earlier dates in the research history are drafting dates, not claims of public availability or priority. Both public manuscripts name Christopher D. Long as author.

The functional manuscript is based on the September 22, 2026, sole-author version 2 of *Rational-Exponential Iterated Integrals and Quantum Polylogarithms*. It includes the absolute fixed-parameter coefficient-field extension. The alternate titles *Quantum Polylogarithms: Residue Modules, Iterated Integrals, and Pentagon Operators* and *Quantum Fourier Letters and Iterated Integrals* refer to earlier formulations, not additional papers in this release.

The finite-equation manuscript is based on the September 21, 2026 working note *Finite quantum dilogarithms: normalization exceptions, infinitesimal rigidity, and effective degree bounds*. The initial `v0.1.0` release made its general infinitesimal criterion explicitly conditional, retained the unconditional low-order certificates and degree bounds, and updated the current-source comparison. The subsequent October 1 main-branch revision discharges that hypothesis by a universal normalized-ring argument and intrinsic reconstruction over dual numbers. The earlier tag and release assets are not rewritten.

## Primary references checked for the release

- Danylo Radchenko and Campbell Wheeler, *Real quadratic fields and finite quantum dilogarithms I*, [arXiv:2609.21892](https://arxiv.org/abs/2609.21892). Version 1 was submitted September 18, 2026; version 2 September 29, 2026. Current Theorem 5 is for order greater than four; Remark 3 explicitly records exceptional raw-equation solutions at small orders and the additional normalization convention. The finite paper retains explicit historical version-1 references where its raw equation and earlier proof are being discussed. Equation numbering must not be transferred silently between versions or renderings.
- Marcus Appleby, Steven T. Flammia, and Gene S. Kopp, *The twisted convolution identity and ghost r-SICs from finite quantum dilogarithms*, [arXiv:2609.39192v1](https://arxiv.org/abs/2609.39192v1), September 30, 2026. The all-admissible-rank twisted convolution identity and cocycle dictionary are background, not claimed as results of either manuscript here.
- Alexander B. Goncharov, *Quantum polylogarithms*, [arXiv:2601.00472v1](https://arxiv.org/abs/2601.00472v1), January 1, 2026. The Fourier integrals, modular difference equations, and existing shuffle structure originate in this work.
- Alexander B. Goncharov, *The pentagon relation for the quantum dilogarithm and quantized M0,5*, [arXiv:0706.4054](https://arxiv.org/abs/0706.4054). The operator appendix specifies the version and imported common-domain/covariance results.
- Pavel Etingof, Dmitri Nikshych, and Viktor Ostrik, *On fusion categories*, [arXiv:math/0203060](https://arxiv.org/abs/math/0203060), Annals of Mathematics 162 (2005), 581–642. The finite-paper infinitesimal argument uses Theorem 2.27 and the first-order interpretation in Section 7.1, not merely finiteness of equivalence classes.

The bibliographies also credit the classical iterated-integral, shuffle, difference-algebra, and categorical ingredients. This focused source check does not establish literature-wide novelty. In particular, algebraicity and finiteness were already goals/results of RW v1; they should not be described as results of this project lost only when v2 appeared.

## Computational provenance

The original exact finite verifier and the recovered functional verification scripts are included with their scope disclaimers. All three functional runs (exact, mixed-contour, and earlier contour/Laplace comparisons) and the finite verifier were executed again for this release. Reports in `verification/` describe the actual checks and software environment; no earlier numerical exploration is promoted to a certificate without a reproducible script.

## Focused audit incorporated in the rigidity revision

The source check used RW **v2**, Sections 5.4–5.5 and Appendix B, together with ENO Theorem 2.27 and Section 7.1. The displayed completeness calculation on printed page 30 of the RW v2 PDF has coefficient `N(N+d)/d^2`; the generator formulas instead give `N/d^2 + N/d = 1`. The revised manuscript derives the correction and the correlation identity over the actual normalized coordinate ring, without passing to its radical. HTML and PDF equation numbers differ, so the reference is to the section and printed page, not an unqualified equation number.

The reconstruction argument uses a generator of the free distinguished line, canonical normalization on `Hom(1,rho^2)`, common-unit cancellation, and explicit associator/tensorator transport. It does not identify arbitrary basis-dependent coefficients as categorical invariants. The [audit record](audits/2026-10-01-hypothesis-3-1.md) and `scripts/verify_rigidity_identities.py` record these checks and their limitations. No independent review, formalization, new release timestamp, or literature-wide priority claim is implied by this revision.

## Concurrent-literature revision

The citation revision is based on the merged proof commit `d3cb0989d12988b507c6126e03488e0c2ebb2f78` (PR #3). It preserves the finite-paper mathematical core and both papers’ theorem/proof environments exactly. It adds contextual discussion and bibliography entries for Huang, Gannon–Schopieray–Yadav, earlier AFK, Kopp, Seki, and Blümlein–Gavrilik–Mykhailiv–Schneider, and explicitly credits Evans–Gannon’s algebraic precedent. The complete version and scope record is [CITATION_AUDIT.md](CITATION_AUDIT.md).

In particular, GSY Theorem A.3 is already a commutative-ring identity; the discussion does not incorrectly describe all of GSY as field-only. Its HI equations are not identified with the raw near-group scheme in this project. The original release remains unchanged.
