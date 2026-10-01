# Citation and related-work audit

Checked October 1, 2026 against the specified primary-source versions. “Posted” dates below are arXiv submission dates, not claims of journal publication, independent verification, or priority. Older foundational references already in the manuscripts are retained. Each added bibliography item is cited in the body, with its role distinguished from a proof dependency.

## Finite quantum dilogarithms and categorical background

| Source and version | Verified role and placement |
|---|---|
| Danylo Radchenko and Campbell Wheeler, *Real quadratic fields and finite quantum dilogarithms I*, [v1](https://arxiv.org/abs/2609.21892v1), September 18, 2026; [v2](https://arxiv.org/abs/2609.21892v2), September 29, 2026 | Both papers. The primary source for finite QDs, finite pentagon relations, special values, and algebraicity/finiteness. Paper 2 uses v2 Theorem 5 and Remark 3 for normalization scope, Sections 5.4–5.5 and Appendix B for realization and reconstruction. Historical v1 references explicitly identify the raw equation and earlier normalization argument. |
| Marcus Appleby, Steven T. Flammia, and Gene S. Kopp, *The twisted convolution identity and ghost r-SICs from finite quantum dilogarithms*, [v1](https://arxiv.org/abs/2609.39192v1), September 30, 2026 | Both papers, explicitly citing Theorem 1.3 and Proposition 2.1 for the ghost-r-SIC/all-rank TCI endpoint and convention dictionary. Cited background, not an output of this project. The Stark/Galois step is not inferred from the finite endpoint. |
| Tzu-Chen Huang, *Cyclic Haagerup–Izumi fusion categories at every odd order*, [v1](https://arxiv.org/abs/2609.15986v1), September 14, 2026 | Both related-work passages, principally Paper 2. An independent cyclic HI construction with double-sine, Fourier, and categorical ingredients. Its HI fusion rules are not identified with the near-group/raw-QD scheme treated here. |
| Terry Gannon, Andrew Schopieray, and Harshit Yadav, *On Haagerup–Izumi fusion categories*, [v1](https://arxiv.org/abs/2609.25185v1), September 21, 2026 | Both related-work passages; explicit methodological discussion in Paper 2. Theorem 2.5 and Theorem B.20 concern reconstruction over algebraically closed fields in arbitrary characteristic. Theorem A.3 also gives a commutative-ring identity. It would be inaccurate to describe the entire paper as restricted to fields. These precedents do not automatically establish our normalized dual-number reconstruction or reducedness of our raw scheme. |
| David E. Evans and Terry Gannon, *Non-unitary fusion categories and their doubles via endomorphisms*, Advances in Mathematics **310** (2017), 1–43; [arXiv:1506.03546](https://arxiv.org/abs/1506.03546) | Paper 2 explicitly credits the algebraic endomorphism/Leavitt approach without a positivity or C*-assumption. Journal metadata checked against the author's publication list as well as the cited paper. |
| Pavel Etingof, Dmitri Nikshych, and Viktor Ostrik, *On fusion categories*, Annals of Mathematics **162** (2005), 581–642; [DOI](https://doi.org/10.4007/annals.2005.162.581) | Paper 2's essential rigidity input: Theorem 2.27, with the first-order H^3 interpretation and twist argument in Sections 7.1 and 7.3. Finiteness of equivalence classes alone does not establish the required tangent-space conclusion. |

## Arithmetic motivation

| Source and version | Verified role and placement |
|---|---|
| Marcus Appleby, Steven T. Flammia, and Gene S. Kopp, *A Constructive Approach to Zauner's Conjecture via the Stark Conjectures*, [v2](https://arxiv.org/abs/2501.03970v2), March 17, 2025 (first posted January 7, 2025) | Both papers. The earlier conditional Stark/SIC and twisted-convolution framework. Not cited as an unconditional Stark reciprocity theorem. |
| Gene S. Kopp, *The Shintani–Faddeev modular cocycle: Stark units from q-Pochhammer ratios*, [v3](https://arxiv.org/abs/2411.06763v3), May 3, 2025 (first posted November 11, 2024) | Both papers. Foundational cocycle and real-multiplication/Stark context. This contextual relation does not supply a generic-to-arithmetic specialization morphism for our functional algebra. |

## Other deformations of iterated integrals

| Source and version | Verified role and placement |
|---|---|
| Shin-ichiro Seki, *A proof of Hirose's duality conjecture*, [v1](https://arxiv.org/abs/2609.40213v1), September 30, 2026 | Paper 1. Related word relations for a q-discretization on the four-punctured projective line with word-dependent shifts. Not identified with Goncharov's Fourier kernels or claimed to prove our completeness theorem. |
| J. Blümlein, A. M. Gavrilik, O. Mykhailiv, and C. Schneider, *The q-extension of iterated integrals and nested sums in quantum field theory*, [v1](https://arxiv.org/abs/2608.02702v1), August 3, 2026 | Paper 1. A different q-iterated-integral/nested-sum construction. All four authors are included; the abstract-page display's abbreviated author count is not used. |

## Attribution and version safeguards

The chronology is not reduced to “RW, then AFK”: Huang and GSY are explicitly acknowledged as concurrent categorical developments. Algebraicity/finiteness, the finite pentagon, all-rank TCI, and the cocycle dictionary are not claimed as new here. The new finite-paper argument concerns the actual nonreduced defining scheme and normalized infinitesimal reconstruction; its degree bounds use previously established finiteness. No exhaustive literature-wide novelty claim is made.

RW's HTML and PDF equation numbers are not always identical. The correction in the proof is pinned to **v2, Appendix B.1, printed PDF page 30**; the generator formulas and Appendix B proof are cited by section. The original PDF display was checked visually. No equation-number comparison alone is treated as evidence of a mathematical error.

The bibliography-key and cross-reference checker is a reproducible bookkeeping check. It cannot verify a citation's mathematical applicability, publication history, or completeness; those are supplied by this source audit and the manuscript's explicit scope statements.

## Reconciliation with the proof revision

The separate proof revision was merged as PR #3, commit `d3cb0989d12988b507c6126e03488e0c2ebb2f78`, while this citation audit was being prepared. The citation revision is based on that commit and preserves its proof bodies, generator formulas, rigidity regression script, and audit record. It adds related-work passages and bibliographic entries rather than replacing the newly merged proof. The initial `v0.1.0` tag and assets remain unchanged.
