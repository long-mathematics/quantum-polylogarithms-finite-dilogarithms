#!/usr/bin/env python3
"""Exact regression checks for the audited infinitesimal-rigidity revision.

These checks do not prove the arbitrary-group realization, Hom-space flatness,
ENO rigidity, or monoidal coherence. Those arguments are in the manuscript.
The Leavitt checks use formal coefficients, not sampled complex solutions.
"""
from __future__ import annotations

import itertools
import math
from collections.abc import Sequence

import sympy as sp

# A letter is (S-or-T, group index, primed). Only the contraction relations
# S'_g S_h = T'_g T_h = delta(g,h), S'_g T_h = T'_g S_h = 0 are needed here.
Letter = tuple[str, int, bool]
Word = tuple[Letter, ...]


def contract(word: Word) -> Word | None:
    stack: list[Letter] = []
    for letter in word:
        if stack and stack[-1][2] and not letter[2]:
            previous = stack.pop()
            if previous[:2] != letter[:2]:
                return None
        else:
            stack.append(letter)
    return tuple(stack)


def group_data(moduli: Sequence[int]) -> tuple[list[tuple[int, ...]], dict[tuple[int, ...], int]]:
    if not moduli or any(m < 2 for m in moduli):
        raise ValueError("Expected a nonempty tuple of moduli >= 2.")
    elements = list(itertools.product(*(range(m) for m in moduli)))
    return elements, {g: i for i, g in enumerate(elements)}


def check_projector(moduli: Sequence[int]) -> int:
    elements, _ = group_data(moduli)
    order = math.lcm(*moduli)
    z = sp.Symbol("z")
    cyclotomic = sp.Poly(sp.cyclotomic_poly(order, z), z, domain=sp.QQ)
    for h in elements:
        poly = sum(z ** ((-sum((order // m) * a * b
                              for m, a, b in zip(moduli, g, h))) % order)
                   for g in elements)
        expected = len(elements) if all(x == 0 for x in h) else 0
        assert sp.rem(sp.Poly(poly - expected, z, domain=sp.QQ), cyclotomic).is_zero
    return len(elements)


def check_reconstruction(moduli: Sequence[int]) -> int:
    elements, index = group_data(moduli)
    n = len(elements)
    s, nu, lam = sp.symbols("s nu lambda", nonzero=True)
    E = sp.symbols(f"E0:{n}")
    q = [sp.S.One] + list(sp.symbols(f"q1:{n}", nonzero=True))

    def add(g: int, h: int) -> int:
        return index[tuple((a + b) % m for m, a, b in zip(moduli, elements[g], elements[h]))]

    def neg(g: int) -> int:
        return index[tuple((-a) % m for m, a in zip(moduli, elements[g]))]

    def chi(g: int, h: int) -> sp.Expr:
        return sp.S.One if g == 0 or h == 0 else sp.Symbol(f"chi_{g}_{h}", nonzero=True)

    def S(g: int, prime: bool = False) -> Letter:
        return ("S", g, prime)

    def T(g: int, prime: bool = False) -> Letter:
        return ("T", g, prime)

    for g in range(n):
        terms: list[tuple[sp.Expr, Word]] = []
        for h, k in itertools.product(range(n), repeat=2):
            terms.append((lam * chi(add(h, neg(g)), k) / (nu * s), (S(h), T(k, True))))
            terms.append((1 / (lam * q[g] * s * chi(add(g, h), k)), (T(k), S(h), S(h, True))))
            terms.append((q[h] * E[add(h, g)] / (s * chi(g, k)), (T(add(h, k)), T(neg(h)), T(k, True))))
        reduced: dict[Word, sp.Expr] = {}
        for coefficient, word in terms:
            result = contract((T(0, True), T(0, True)) + word + (T(0),))
            if result is not None:
                reduced[result] = reduced.get(result, sp.S.Zero) + coefficient
        assert set(reduced) == {()}
        assert sp.cancel(reduced[()] - E[g] / s) == 0
    return n


def main() -> None:
    N, d, e, s = sp.symbols("N d e s", nonzero=True)
    relation = d**2 - N * (d + 1)
    numerator = sp.cancel((N / d**2 + N / d - 1) * d**2)
    assert sp.rem(numerator, relation, d) == 0
    wrong = sp.rem(sp.expand(N * (N + d) - d**2), relation, d)
    assert sp.expand(wrong - N * (N - 1)) == 0
    assert sp.expand((2 * e - s)**2 - (s**2 + 4) - 4 * (e**2 - s * e - 1)) == 0
    print("Correct completeness coefficient: N/d^2 + N/d = 1 modulo d^2-N(d+1).")
    print("Printed coefficient residual: N(N-1)/d^2 (not zero for N > 2).")
    print("Scalar-normalization discriminant identity: exact.")

    eps, b0, bg = sp.symbols("epsilon b0 bg")
    u, u0, ug = sp.symbols("u u0 ug", nonzero=True)
    assert sp.cancel(u**(-1) * u**(-1) * u * u) == 1
    factor = sp.cancel(u0**(-1) * u0**(-1) * ug * u0)
    assert factor == ug / u0
    linear = sp.series(factor.subs({u0: 1 + eps * b0, ug: 1 + eps * bg}), eps, 0, 2).removeO()
    assert sp.expand(linear - 1 - eps * (bg - b0)) == 0
    print("Normalized common-unit invariance and independent-unit obstruction: exact.")

    groups = [(3,), (4,), (5,), (2, 2), (2, 3), (3, 3)]
    counts = [check_projector(group) for group in groups]
    print(f"Character projectors: {sum(counts)} diagonal entries over exact cyclotomic fields; groups={groups}.")
    groups = [(3,), (4,), (5,), (2, 2)]
    counts = [check_reconstruction(group) for group in groups]
    print(f"Formal Leavitt reconstruction: {sum(counts)} coordinates equal E_g/s; groups={groups}.")
    print("PASS. Finite regression scope only; not a certification of the general categorical proof.")


if __name__ == "__main__":
    main()
