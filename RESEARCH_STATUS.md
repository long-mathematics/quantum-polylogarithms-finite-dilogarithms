# Research status — initial public draft

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
| General finite étaleness of the raw defining scheme | **Conditional** on the normalized categorical realization and reconstruction over dual numbers (Hypothesis 3.1). |
| Flatness and rigidity implication | The draft proves flatness of the relevant Hom spaces and the deduction from first-order categorical rigidity, once the realization hypothesis is supplied. |
| General good reduction / nilpotent lifting conclusions | Conditional when deduced from the general criterion; unconditional for the explicitly computed reduced schemes. |
| Elementary-abelian two-group obstruction | Already known categorically. The draft gives an elementary recovery, not a new existence/nonexistence theorem. |

The general finite-étale assertion in the earlier working note is **not released as an unconditional theorem**. Passing from identities over fields to identities over nonreduced rings requires a ring-level argument. The exact small-order verifier does not supply that argument for every metric group.

## Outstanding interfaces

The principal unresolved release obligation for the finite paper is a complete ring-level verification of the specified RW Leavitt realization, split fusion/duality identities, and invariant scalar reconstruction over dual numbers. A functional-to-arithmetic specialization functor with an independently identified kernel is a different problem, as are Stark/Artin reciprocity and the required unitary Galois conjugates. None is inferred from functional independence, finiteness of a complex solution set, or the existence of a Galois action on algebraic points.

The unitarity reduction discussed during research exploration is not included as a theorem or as a certified numerical result in this release.
