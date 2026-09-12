#!/usr/bin/env python3
"""Exact rational calibration of KR identities, with genuine confluent/resonant inputs.

Finite positive measures are used to check finite algebra and Schur signs.
They are not the arithmetic measure, not proofs of analytic convergence,
and not evidence of locations or multiplicities of zeta zeros.
No assert statements: normal and optimized Python execute identical checks.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
import sympy as sp

s = sp.Symbol("s")
I = sp.I
half = sp.Rational(1, 2)
checks: list[dict] = []


def scalar_zero(x):
    return sp.cancel(sp.expand(x)) == 0


def matrix_zero(x):
    return all(scalar_zero(v) for v in x)


def check(name, result, scope="exact finite algebra"):
    ok = bool(result)
    checks.append({"name": name, "passed": ok, "scope": scope})
    if not ok:
        raise RuntimeError(name)


def fixture(ts, weights):
    nodes = [half + I * sp.Rational(t) for t in ts]
    ww = [sp.Rational(w) for w in weights]

    def integral(p):
        return sp.expand(sum(w * p.subs(s, z) for z, w in zip(nodes, ww)))

    def pair(p, q):
        return sp.expand(sum(w * sp.conjugate(p.subs(s, z)) * q.subs(s, z)
                             for z, w in zip(nodes, ww)))

    q = []
    norms = []
    for k in range(len(nodes)):
        p = s**k
        for qj, norm in zip(q, norms):
            p = sp.expand(p - qj * pair(qj, p) / norm)
        q.append(p)
        norms.append(sp.cancel(pair(p, p)))
    q.append(sp.expand(sp.prod(s-z for z in nodes)))
    return nodes, ww, integral, pair, q, norms


def jacobi(q, norms, pair, size):
    J = sp.zeros(size)
    for k in range(size):
        J[k, k] = sp.cancel(pair(q[k], s*q[k])/norms[k])
        if k + 1 < size:
            J[k+1, k] = 1
            J[k, k+1] = -norms[k+1]/norms[k]
    return J


def quotient(h):
    d = sp.degree(h, s)

    def rem(p):
        r = sp.Poly(sp.rem(p, h, s), s)
        return sp.Matrix([r.nth(k) for k in range(d)])

    A = sp.Matrix.hstack(*[rem(s**(k+1)) for k in range(d)])
    return A, rem(1+0*s), rem


def poly_matrix(p, A):
    pol = sp.Poly(p, s)
    answer = sp.zeros(A.rows)
    for k in range(pol.degree()+1):
        answer += pol.nth(k) * A**k
    return sp.simplify(answer)


nodes, weights, integral, pair, q, norms = fixture(
    [-4, -2, -1, 0, 1, 3, 6], [1, 2, 1, 3, 2, 1, 2])
full = len(nodes)
Jall = jacobi(q, norms, pair, full)
H = sp.diag(*norms)
check("actual vertical adjoint identity", matrix_zero(Jall.conjugate().T*H + H*Jall-H))
z = sp.Rational(7, 6) + I*sp.Rational(2, 3)
true_m = sp.cancel(sum(w/(z-lam) for w, lam in zip(weights, nodes)))
for n in [1, 2, 3, 4]:
    Jn = Jall[:n, :n]
    Rn = (z*sp.eye(n)-Jn).inv()
    mn = norms[0]*Rn[0, 0]
    Fn = Rn[n-1, n-1]
    check(f"terminal ratio n={n}", scalar_zero(Fn-q[n-1].subs(s,z)/q[n].subs(s,z)))
    check(f"characteristic value n={n}", scalar_zero((z*sp.eye(n)-Jn).det()-q[n].subs(s,z)))
    tail = Jall[n:, n:]
    tail_resolvent = (z*sp.eye(full-n)-tail).inv()
    zz = tail_resolvent[0,0]
    an = norms[n]/norms[n-1]
    obs = sp.cancel(sum(w*sp.conjugate(q[n].subs(s,lam))*q[n].subs(s,lam)/(z-lam)
                         for w,lam in zip(weights,nodes))/norms[n])
    check(f"dressed true tail n={n}", scalar_zero(obs-zz/(1+an*Fn*zz)))
    predicted = (-1)**n*norms[n]*zz/(q[n].subs(s,z)**2*(1+an*Fn*zz))
    check(f"signed Schur remainder n={n}", scalar_zero(true_m-mn-predicted))
    check(f"orthogonal remainder n={n}", scalar_zero(true_m-mn-(-1)**n*norms[n]*obs/q[n].subs(s,z)**2))
    endpoint_product = (-1)**(n-1)*norms[n-1]/norms[0]/q[n].subs(s,z)**2
    check(f"endpoint cofactor product n={n}", scalar_zero(Rn[0,n-1]*Rn[n-1,0]-endpoint_product))
    check(f"negative sign control n={n}", not scalar_zero(true_m-mn+predicted), "deliberately reversed remainder sign is rejected")

# Complete discrete quadrature fixes its nodes exactly.  Degree-n annihilator
# is used only for finite quadrature/kernel identities, never as positive kappa_n.
nodes, weights, integral, pair, q, norms = fixture(
    [-3,-1,0,2,5], [1,2,3,4,5])
n = len(nodes)
sigma = [sp.cancel(w*sp.conjugate(q[n-1].subs(s,lam))*q[n-1].subs(s,lam)/norms[n-1])
         for w,lam in zip(weights,nodes)]
check("terminal weights positive", all(v.is_positive is True for v in sigma))
check("terminal weights sum one", scalar_zero(sum(sigma)-1))
L = [sp.div(q[n],s-lam,s)[0]/sp.diff(q[n],s).subs(s,lam) for lam in nodes]
for j in range(n):
    check(f"endpoint weights bridge j={j}", scalar_zero(sigma[j]-norms[n-1]/(weights[j]*abs(sp.diff(q[n],s).subs(s,nodes[j]))**2)))

for label,h in [
    ("off_line_double_pair", (s-(sp.Rational(1,4)+I))**2*(s-(sp.Rational(3,4)+I))**2),
    ("critical_resonance_with_double_jet", (s-nodes[2])**2*(s-(sp.Rational(3,4)+I))),
]:
    h = sp.expand(h)
    A,c,rem = quotient(h)
    d = A.rows
    K = sp.zeros(d)
    for k in range(n):
        vv = rem(q[k])
        K += vv*vv.conjugate().T/norms[k]
    K_quad = sp.zeros(d)
    for j in range(n):
        vv = rem(L[j])
        K_quad += vv*vv.conjugate().T/weights[j]
    check(f"{label}: full polynomial quadrature kernel", matrix_zero(K-K_quad))
    check(f"{label}: complete rank", K.det().is_positive is True)
    Q = poly_matrix(q[n],A)
    check(f"{label}: quotient polynomial exact", matrix_zero(poly_matrix(h,A)))
    if label.startswith("off"):
        S = sp.zeros(d)
        rr = sp.zeros(d,1)
        for sig,lam in zip(sigma,nodes):
            X = (A-lam*sp.eye(d)).inv()*c
            S += sig*X*X.conjugate().T
            rr += sig*X
        check("off-line complete-jet metric congruence", matrix_zero(K-Q*S*Q.conjugate().T/norms[n-1]))
        check("off-line exact rational weight defect", matrix_zero(A*S+S*A.conjugate().T-S-c*rr.conjugate().T-rr*c.conjugate().T))
        check("off-line terminal functional calculus", matrix_zero(rr-poly_matrix(q[n-1],A)*Q.inv()*c))
        check("off-line negative defect sign control", not matrix_zero(A*S+S*A.conjugate().T-S+c*rr.conjugate().T+rr*c.conjugate().T), "deliberately reversed weight defect is rejected")
    else:
        check("resonant rational inverse correctly unavailable", Q.det()==0)
        check("resonant complete kernel remains invertible", K.det()!=0)

base = Path(__file__).resolve().parents[1]
sources = [base/"tex"/"kernel_resolvent.tex"]
receipt = {
    "script": str(Path(__file__).resolve()),
    "scope": "Exact rational finite positive-measure calibrations; no actual zeta evaluations, no analytic theorem certificate, no RH claim.",
    "passed": len(checks), "failed": 0,
    "source_sha256": {str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
    "checks": checks,
}
target = Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_suffix(".json")
target.write_text(json.dumps(receipt,indent=2),encoding="utf-8")
print(json.dumps({"passed":len(checks),"failed":0,"receipt":str(target)}))
