#!/usr/bin/env python3
"""Exact algebraic checks for the actual-test-function origin ladder.
The factorization proof for 2 xi is analytic and written in the companion note.
Polynomial g examples below test the universal CRT identities, not RH.
"""
import json
from collections import Counter
import sympy as sp

x, s, z = sp.symbols('x s z')
p = sp.Symbol('pi', positive=True)
counts = Counter()

def verify(suite, expression):
    counts[suite] += 1
    if sp.cancel(sp.expand(expression)) != 0:
        raise ArithmeticError((suite, expression))

def D(P):
    return sp.expand(2*p*x**2*P - x*sp.diff(P,x))

def mellin_gaussian_polynomial(P):
    ans = 0
    for (power,), coefficient in sp.Poly(P, x).terms():
        if power % 2:
            raise ArithmeticError('input must be even')
        k = power // 2
        ans += coefficient*p**(-k)*sp.rf(s/2,k)
    return sp.expand(ans)

P0 = 4*p**2*x**4 - 6*p*x**2
P = P0
for j in range(9):
    verify('actual_D_ladder', mellin_gaussian_polynomial(P)-s**j*s*(s-1))
    verify('actual_D_ladder', P.subs(x,0))
    verify('actual_D_ladder', sp.Poly(P,x).LC()-4*p**2*(2*p)**j)
    P = D(P)
P = P0
for j in range(7):
    verify('actual_symmetric_ladder', mellin_gaussian_polynomial(P)-(s*(1-s))**j*s*(s-1))
    verify('actual_symmetric_ladder', ((s*(1-s))**j).subs(s,1-s)-(s*(1-s))**j)
    P = sp.expand(D(P)-D(D(P)))

g = 1+3*s*(1-s)+2*(s*(1-s))**2
for m in range(1,7):
    a = sp.series(1/g,s,0,m).removeO()
    b, rem = sp.div(1-a*g,s**m,s)
    verify('origin_CRT', rem)
    verify('origin_CRT', a*g+b*s**m-1)
    for u,v in [(1+s,s**(m-1)),(s**2+2,1+s**m)]:
        inverse = b*s**m*u+a*g*v
        verify('origin_CRT', sp.rem(inverse-u,g,s))
        verify('origin_CRT', sp.rem(inverse-v,s**m,s))
    poly = (s*(1-s))**m
    a2 = sp.invert(g,poly,s)
    b2,rem2 = sp.div(1-a2*g,poly,s)
    verify('two_endpoint_CRT', rem2)
    verify('two_endpoint_CRT', a2*g+b2*poly-1)
    verify('two_endpoint_CRT', poly.subs(s,1+z)-(-1)**m*z**m*(1+z)**m)
    aa = sum((j+1+sp.I/(j+2))*z**j for j in range(m))
    dag = sp.conjugate(aa.subs(z,-sp.conjugate(z)))
    dag2 = sp.conjugate(dag.subs(z,-sp.conjugate(z)))
    verify('endpoint_involution', dag2-aa)

print(json.dumps({'status':'passed','checks':dict(counts),'total':sum(counts.values()),
 'scope':'Exact Gaussian Mellin-polynomial recursions and universal polynomial CRT tests; no numerical zeta-root assertion.'},indent=2,sort_keys=True))
