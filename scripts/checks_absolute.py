#!/usr/bin/env python3
"""Supplementary convention checks for Paper B, version 2.

Exact symbolic checks validate formulas used in the coefficient-field argument.
Numerical quadratures check selected contour instances only. Neither finite
calculations nor quadrature constitute proofs of algebraic independence.
"""
from __future__ import annotations
import argparse
import json
from functools import lru_cache
from pathlib import Path
from typing import Any
import sympy as sp
import mpmath as mp


def exact_checks() -> dict[str, Any]:
    x, rho, h, alpha, V, t = sp.symbols('x rho h alpha V t', nonzero=True)
    ipi = sp.I*sp.pi
    out: dict[str, Any] = {}
    # Closed one-frequency polynomial, independently constructed from recursion.
    z = sp.symbols('z')
    axis = sp.Integer(1)
    for b in range(1, 8):
        if b > 1:
            axis = sp.expand((z+ipi*(b-2))/(2*ipi*(b-1))*axis.subs(z,z-ipi))
        closed = sp.prod(z+ipi*(b-2-2*k) for k in range(b-1))/((2*ipi)**(b-1)*sp.factorial(b-1))
        assert sp.simplify(axis-closed)==0, ('axis',b)
        A = sp.prod(x+rho+ipi+ipi*h*(2*l-1) for l in range(1,b))/(h*(2*ipi*h)**(b-1)*sp.factorial(b-1))
        normalized = closed.subs(z,(x+rho+ipi)/h+ipi*(b-1))/h
        assert sp.simplify(normalized-A)==0, ('increment',b)
        assert sp.Poly(A,x).degree()==b-1
        expected_lc=1/(h*(2*ipi*h)**(b-1)*sp.factorial(b-1))
        assert sp.simplify(sp.Poly(A,x).LC()-expected_lc)==0
    out['axis_and_increment_polynomials']='exact for b=1,...,7'

    # Check the leading V-principal part for a polynomial coefficient.
    # A generic polynomial is sufficient to test the derivation convention;
    # the manuscript proves the formula for every polynomial and every j.
    A=x**3+rho*x+2
    f=-A*V/(V-alpha)
    for j in range(6):
        if j:
            f=sp.cancel(sp.diff(f,x)+V/h*sp.diff(f,V))
        coefficient=sp.limit((V-alpha)**(j+1)*f,V,alpha)
        expected=(-1)**(j+1)*sp.factorial(j)*alpha**(j+1)/h**j*A
        assert sp.simplify(coefficient-expected)==0, ('pole',j)
    out['highest_pole_coefficient']='exact for derivative orders j=0,...,5'

    # Verify lowering/multiplication elimination without assuming the result.
    a,b=sp.symbols('a b', positive=True, integer=True)
    l, lm, ls = sp.symbols('L Lminus Lsum')
    # At z+pi*i, L_{a+1,b}(z+2pi*i)=L_{a+1,b}(z)+L_{a,b}(z+pi*i).
    derived=sp.solve(sp.Eq((z+ipi)*l, ipi*a*(2*lm+l)+ipi*h*b*ls),lm)[0]
    expected=(z-ipi*(a-1))/(2*ipi*a)*l-h*b/(2*a)*ls
    assert sp.simplify(derived-expected)==0
    out['first_index_reduction']='exact symbolic elimination'

    # A finite rational coboundary has two orbit endpoints (illustration only).
    q=sp.Rational(2)
    g=1/(V-alpha)+x/(V-q*alpha)
    sg=g.subs({x:x+1,V:q*V}, simultaneous=True)
    diff=sp.cancel(sg-g)
    assert sp.simplify(sp.limit((V-alpha/q)*diff,V,alpha/q))!=0
    assert sp.simplify(sp.limit((V-q*alpha)*diff,V,q*alpha))!=0
    out['orbit_endpoint_example']='two uncancelled endpoints verified exactly'
    out['scope_guardrails']={
        'rational_h':'h=1 gives identical mixed and one-frequency kernels L_11=L_20',
        'duplicate_rho':'rho and rho+2*pi*i have the same q-orbit and differ by an elementary increment',
        'constants':'proof uses sigma-constants C(U), not differential constants C',
    }
    return out


def numerical_checks() -> dict[str, Any]:
    mp.mp.dps=45
    h=mp.sqrt(2); eta=mp.mpf('.23'); ipi=mp.j*mp.pi
    @lru_cache(maxsize=None)
    def L(a: int,b: int,z: Any) -> Any:
        if abs(mp.im(z))>=mp.pi*(a+h*b):
            raise ValueError('This numerical helper only uses the defining strip')
        def integrand(t: Any) -> Any:
            p=t+mp.j*eta
            return mp.exp(-mp.j*p*z)/( (2*mp.sinh(mp.pi*p))**a*(2*mp.sinh(mp.pi*h*p))**b )
        return -mp.j*mp.quad(integrand,[-mp.inf,-3,-1,0,1,3,mp.inf])
    report:dict[str,Any]={}
    def record(name:str,left:Any,right:Any)->None:
        err=abs(left-right)/(1+abs(left)+abs(right))
        if err>mp.mpf('1e-30'):
            raise AssertionError(f'{name}: normalized error {err}')
        report[name]={'normalized_error':mp.nstr(err,10),
                      'left':mp.nstr(left,28),'right':mp.nstr(right,28)}
    # A negative imaginary part puts every term of the first sigma increment
    # in a strict common strip; normalized b-shifts align the elementary pole.
    x=mp.mpc('-.7',str(-mp.pi)); rho=mp.mpc('.13','.07')
    for b in range(1,4):
        z=x+rho+ipi*h*(b-1)
        lhs=L(1,b,z+2*ipi)-L(1,b,z)
        A=mp.fprod(x+rho+ipi+ipi*h*(2*l-1) for l in range(1,b))/(h*(2*ipi*h)**(b-1)*mp.factorial(b-1))
        a_rho=mp.exp((rho+ipi)/h)
        rhs=A*(-a_rho*mp.exp(x/h)/(1+a_rho*mp.exp(x/h)))
        record(f'normalized_sigma_increment_b{b}',lhs,rhs)
    z=mp.mpc('-.6','.17')
    for a,b in [(1,1),(2,1),(1,2)]:
        lhs=L(a+1,b,z)
        rhs=(z-ipi*(a-1))/(2*ipi*a)*L(a,b,z+ipi)-h*b/(2*a)*(L(a,b+1,z+ipi+ipi*h)+L(a,b+1,z+ipi-ipi*h))
        record(f'first_index_reduction_a{a}_b{b}',lhs,rhs)
    # Choose a common strip also for J_{b-1} and both tau-shifted arguments.
    x=mp.mpc('-.9','.1'); rho=mp.mpc('.08','-.13')
    for b in [2,3]:
        z=x+rho+ipi*h*(b-1)
        lhs=L(1,b,z-2*ipi*h)
        rhs=L(1,b,z)-L(1,b-1,x+rho+ipi*h*(b-2))
        record(f'backward_tau_b{b}',lhs,rhs)
    return report


def main()->None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--mode',choices=['all','exact','numeric'],default='all')
    p.add_argument('--output',type=Path,default=Path(__file__).with_name('checks_absolute_results.json'))
    a=p.parse_args()
    data:dict[str,Any]={'disclaimer':'Supplementary checks, not independence proofs or interval enclosures.',
                        'mode':a.mode,'sympy':sp.__version__,'mpmath':mp.__version__}
    if a.mode in ('all','exact'):data['exact']=exact_checks()
    if a.mode in ('all','numeric'):data['numerical']=numerical_checks()
    a.output.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))
if __name__=='__main__':main()
