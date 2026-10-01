#!/usr/bin/env python3
"""Exact checks accompanying the Radchenko--Wheeler research note.

Requires Python 3.10+ and SymPy. Run:
    python verify_rw_extensions.py

Checks Definition 4 / equation (29), NOT the differently printed equation (7).
Certifies the two normalization exceptions, their tangent ranks, and complete
small-order saturated ideals. It does not certify the general categorical
infinitesimal-rigidity proof.
"""
from __future__ import annotations

import itertools
import sys
from collections.abc import Callable, Sequence

import sympy as sp


def equations(q: Sequence[sp.Expr], xs: Sequence[sp.Expr], c: sp.Expr,
              add: Callable[[int, int], int], neg: Callable[[int], int],
              root_n: sp.Expr) -> list[sp.Expr]:
    """Return sqrt(N) times the residual for every unordered pair (x,y)."""
    n = len(q)
    if len(xs) != n or sp.simplify(root_n**2 - n) != 0:
        raise ValueError("Incompatible group data or square root.")
    q = [sp.sympify(v) for v in q]
    return [sp.expand(root_n * (q[add(x,y)] / (q[x]*q[y]) * xs[x]*xs[y] - c)
                      - sum(q[z]*xs[add(x,neg(z))]*xs[z]*xs[add(y,neg(z))]
                            for z in range(n)))
            for x in range(n) for y in range(x,n)]


def check_metric(q: Sequence[sp.Expr], add: Callable[[int, int], int],
                 neg: Callable[[int], int]) -> None:
    n = len(q)
    q = [sp.sympify(v) for v in q]
    b = lambda x,y: sp.simplify(q[add(x,y)] / (q[x]*q[y]))
    assert q[0] == 1
    for x in range(n):
        assert sp.simplify(q[x] - q[neg(x)]) == 0
        for y in range(n):
            for z in range(n):
                assert sp.simplify(b(x,add(y,z))-b(x,y)*b(x,z)) == 0
        assert sp.simplify(sum(b(x,y) for y in range(n)) - (n if x == 0 else 0)) == 0


def rank_minor(residuals: list[sp.Expr], variables: list[sp.Symbol],
               values: dict[sp.Symbol, sp.Expr]) -> tuple[tuple[int, ...], sp.Expr]:
    mat = sp.Matrix(residuals).jacobian(variables).subs(values).applyfunc(sp.simplify)
    for rows in itertools.combinations(range(mat.rows), len(variables)):
        det = sp.simplify(mat[list(rows), :].det())
        if det != 0:
            return rows, det
    raise AssertionError("No full-rank Jacobian minor found.")


def main() -> None:
    a,b,d,e,c,t = sp.symbols("a b d e c t")
    s = sp.sqrt(3)
    r = (-1 + sp.I*s)/2
    field = sp.QQ.algebraic_field(s, sp.I)

    q3 = [sp.S.One, r, r]
    add3 = lambda x,y: (x+y)%3
    neg3 = lambda x: (-x)%3
    check_metric(q3, add3, neg3)
    f3 = equations(q3, [a,b,d], c, add3, neg3, s)
    exc3 = {a:(s-sp.I)/2, b:-(s+sp.I)/2, d:-(s+sp.I)/2, c:r**2}
    assert all(sp.simplify(f.subs(exc3)) == 0 for f in f3)
    assert sp.simplify((a*a-s*a-1).subs(exc3)) == -2
    rows, det = rank_minor(f3, [a,b,d,c], exc3)
    print("C3 exceptional solution: all 9 ordered equations hold exactly.")
    print("Normalization residual: -2")
    print("Full-rank Jacobian minor:", rows, sp.expand_complex(det).simplify())

    # t*c-1 implements C != 0; placing b last gives a primitive-element form.
    gb3 = sp.groebner(f3+[t*c-1], t,c,d,a,b,
                     extension=[s,sp.I], order="lex")
    assert len(gb3.polys) == 5
    p = sp.Poly(gb3.polys[-1].as_expr(), b, domain=field)
    assert p.degree() == 5 and p.LC() == 1
    assert sp.gcd(p,p.diff()).degree() == 0
    disc = sp.simplify(p.discriminant().as_expr())
    assert sp.simplify(disc + 147*r**2) == 0
    q = sp.div(p, sp.Poly(b+(s+sp.I)/2,b,domain=field))[0]
    assert q.degree() == 4
    assert sp.simplify(q.discriminant().as_expr()+147) == 0
    assert sp.simplify(q.eval(-(s+sp.I)/2).as_expr()-r) == 0

    recovery: dict[sp.Symbol, sp.Expr] = {}
    for variable, polynomial in zip([t,c,d,a], gb3.polys[:-1]):
        expr = polynomial.as_expr()
        assert sp.diff(expr,variable) == 1
        recovery[variable] = sp.expand(variable-expr)
        assert recovery[variable].free_symbols <= {b}
    def mod_q(expr: sp.Expr) -> sp.Expr:
        return sp.Poly(sp.expand(expr.subs(recovery, simultaneous=True)),
                       b,domain=field).rem(q).as_expr()
    lam = (s-sp.I)/2
    normalized_checks = [a*a-s*a-1, b*d-r**-1, c+lam*a]
    for u in range(3):
        hat = sum([a,b,d][v]*q3[(v-u)%3]/(q3[v]*q3[(-u)%3])
                  for v in range(3))/s
        normalized_checks.append(hat-lam*q3[u]*[a,b,d][u])
    assert all(mod_q(expr) == 0 for expr in normalized_checks)
    print("\nC3 saturated Groebner basis:")
    for polynomial in gb3.polys:
        print(" ", polynomial.as_expr())
    print("Primitive polynomial factorization:")
    print(" ", sp.factor(p.as_expr(),extension=[s,sp.I]))
    print("Discriminant:", disc, "= -147*r^2")
    print("Exactly five reduced geometric points: one exceptional, four normalized.")

    q4 = [sp.S.One,-sp.S.One,-sp.S.One,-sp.S.One]
    add4 = lambda x,y: x^y
    neg4 = lambda x: x
    check_metric(q4, add4, neg4)
    f4 = equations(q4, [a,b,d,e], c, add4, neg4, sp.Integer(2))
    exc4 = {a:1,b:-1,d:-1,e:-1,c:-1}
    assert all(sp.expand(f.subs(exc4)) == 0 for f in f4)
    assert (a*a-2*a-1).subs(exc4) == -2
    rows4, det4 = rank_minor(f4,[a,b,d,e,c],exc4)
    gb4 = sp.groebner(f4+[t*c-1], t,c,e,d,b,a,order="lex")
    assert [f.as_expr() for f in gb4.polys] == [t+1,c+1,e+1,d+1,b+1,a-1]
    print("\nC2 x C2 anisotropic metric: all 16 ordered equations hold exactly.")
    print("Normalization residual: -2")
    print("Full-rank Jacobian minor:",rows4,det4)
    print("Saturated Groebner basis:",gb4)
    print("The solution scheme for this metric is one reduced rational point.")

    # The last step of the elementary rank >= 3 obstruction: N = 32.
    z = sp.Symbol("z")
    modulus = sp.Poly(z**4+1,z,domain=sp.QQ)
    print("\nN=32 coefficient-norm obstruction (root powers 1,3,5,7):")
    norms = []
    for j in (1,3,5,7):
        for sign in (1,-1):
            sqrt2 = z-z**3
            expr = (4*sqrt2*z**j-1)*(2*sqrt2+sign*3)
            poly = sp.Poly(expr,z,domain=sp.QQ).rem(modulus)
            norm = sum(abs(poly.nth(k)) for k in range(4))
            assert norm > 31
            norms.append(int(norm))
            print(f"  lambda=z^{j}, sign={sign:+d}: {poly.as_expr()}, coefficient norm={norm}")
    assert min(norms) == 37
    print("\nAll exact checks passed.")


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, ValueError) as error:
        print(f"VERIFICATION FAILED: {error}", file=sys.stderr)
        raise
