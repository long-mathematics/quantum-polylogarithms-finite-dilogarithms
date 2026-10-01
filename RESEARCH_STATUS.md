# Research status — audited infinitesimal-rigidity revision

**Date:** October 1, 2026. This is a claim/dependency ledger, not an independent referee report or a certificate of literature-wide novelty.

## Functional manuscript

| Claim | Scope and dependencies |
|---|---|
| Fourier-letter presentation by a direct sum of `S/R` | Fixed positive irrational parameter, fixed finite offset set, finite constant-linear combinations. Proof uses both residue tails and exact terminal lowering identities. |
| Meromorphic exactness obstruction | A nonzero specified letter combination has a nonzero finite residue; no globally single-valued meromorphic primitive exists. This does not compute the entire meromorphic de Rham quotient. |
| Laplace–simplex / Chen identity | Positive integral weights and nontrivial kernels. Uses positive contour heights, positive cumulative imaginary parts, and an explicit Fubini majorant. |
| Relative shuffle completeness | One common translation variable over the actual weight-zero differential field. Classical word-independence and shuffle/Lyndon machinery are credited. |
| Nonlinear coefficient-field presentation | The normalized mixed towers and all their derivatives are algebraically independent over `C(x,exp(x),exp(x/h))`. The additive-dependence lemma uses the correct difference constants `C(exp(x))`. |
| Absolute functional completeness | Combines the explicitly presented coefficient field and its shuffle extension. Not numerical specialization or an arithmetic period theorem. |
| Pentagon crossed-product normal form | Separate operator statement on Goncharov's common invariant domain, with his covariance and order-five theorem as inputs. No analytic inversion of arbitrary difference operators. |

The October 1 cleanup retains the stronger September 22 version-2 coefficient-field theorem rather than reverting to the earlier relative-only manuscript. Symbolic and contour checks have been rerun; they do not prove the universal independence statements.

## Finite-equation manuscript

| Claim | Status |
|---|---|
| Raw-equation normalization alternatives | Proved in the draft using the finite Fourier relations and explicit low-order calculations. The current RW small-order convention is distinguished explicitly. |
| Cyclic order-three scheme | Exactly five reduced geometric points for the specified metric, certified by the saturated Gröbner calculation and squarefree primitive polynomial. |
| Anisotropic four-point scheme | Exactly one reduced rational point, certified by a saturated Gröbner basis. |
| Eigenspace degree bounds | Uses the existing finiteness theorem; does not depend on the general finite-étale criterion. Cubic Bézout bound in general and quadratic bound in prime order. |
| Universal normalized realization | Proved by identities in the normalized coordinate ring without taking its radical. Includes the corrected RW completeness coefficient, correlation and dual pentagon, split fusion, and snake identities. |
| General finite étaleness of the raw defining scheme | **Proved in the revised draft (Theorem 3.1).** Uses universal realization, flatness, normalized reconstruction, and ENO first-order rigidity; exceptional points use exact Jacobian certificates. |
| Flatness and normalized reconstruction | Free Hom modules are proved over the dual numbers. The distinguished line requires a generator, the normalized U_g force common rescaling, and explicit associator/tensorator coherence proves invariance. |
| General good reduction / nilpotent lifting conclusions | Follow from finite étaleness; no extra realization hypothesis. Explicit low-order models retain their separate exact certificates. |
| Elementary-abelian two-group obstruction | Already known categorically. The draft gives an elementary recovery, not a new existence/nonexistence theorem. |

The historical `v0.1.0` release stated the general theorem conditionally. The current revision discharges that hypothesis with a ring-level proof and normalized categorical reconstruction; it does not infer nonreduced-base validity from complex-point identities. The [audit record](audits/2026-10-01-hypothesis-3-1.md) documents the corrected completeness coefficient and the gauge-normalization details. The new exact regression script does not replace the arbitrary-group proof. This remains an internally audited research draft, not independent peer review or formal verification.

## Outstanding interfaces

The initial finite-paper realization obligation is discharged in the revised draft. A functional-to-arithmetic specialization functor with an independently identified kernel remains a different, unresolved problem, as do Stark/Artin reciprocity and the required unitary Galois conjugates. None is inferred from functional independence, finiteness of a complex solution set, or the existence of a Galois action on algebraic points.

The unitarity reduction discussed during research exploration is not included as a theorem or as a certified numerical result in this release.

## Related-work scope and revision integrity

The [citation audit](CITATION_AUDIT.md) distinguishes concurrent HI constructions, the general finite-QD theory, Stark/cocycle motivation, and distinct q-iterated-integral theories. None of these contextual citations is presented as a proof of our generic-to-arithmetic specialization problem. The citation revision preserves the merged proof and both papers’ theorem/proof environments; its exact preservation check is recorded in `verification/CITATION_REVISION_CHECKS.json`.
