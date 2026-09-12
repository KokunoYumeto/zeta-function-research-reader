"""Exact algebra calibrations of the proved kernel formulas.

The arithmetic weight is NOT numerically evaluated here.  The calibration
measure is the explicitly different Gaussian probability measure on t.
This checks the implementation, including repeated-root jets and signs.
"""
import json
from pathlib import Path
import sympy as S

s, t = S.symbols("s t", real=True)
line = S.Rational(1, 2) + S.I * t
checks = []

def expect(name, value):
    if not bool(value):
        raise AssertionError(name)
    checks.append(name)

def zero(matrix):
    return all(S.simplify(x) == 0 for x in matrix)

def inner(p, q):
    poly = S.Poly(S.expand(S.conjugate(p.subs(s, line)) * q.subs(s, line)), t)
    value = 0
    for (power,), coefficient in poly.terms():
        if power % 2 == 0:
            moment = 1 if power == 0 else S.factorial2(power - 1)
            value += coefficient * moment
    return S.simplify(value)

def coefficients(p, size):
    poly = S.Poly(S.expand(p), s)
    return S.Matrix([poly.nth(i) for i in range(size)])

for label, polynomial in [
    ("off_line_pair", (s-S.Rational(1,4))*(s-S.Rational(3,4))),
    ("full_double_jet", (s-S.Rational(1,2))**2),
]:
    polynomial = S.expand(polynomial)
    d = S.degree(polynomial, s)
    remainder = lambda p: S.rem(p, polynomial, s)
    A = S.Matrix.hstack(*[coefficients(remainder(s**(j+1)), d) for j in range(d)])
    U = S.eye(d) + 2*A
    expect(label+":unit", U.det() != 0)
    qs, norms = [], []
    for n in range(d+4):
        q = s**n
        for old, norm in zip(qs, norms):
            q -= old*inner(old,s**n)/norm
        qs.append(S.expand(q))
        norms.append(inner(q,q))
        expect(label+f":positive_norm_{n}", norms[-1] > 0)
    for m in range(3):
        N = d+m
        H = S.Matrix(N+1,N+1,lambda i,j:inner(s**i,s**j))
        C = S.Matrix.hstack(*[coefficients(remainder(s**j),d) for j in range(N+1)])
        K = S.simplify(C*H.inv()*C.adjoint())
        vs = [coefficients(remainder(q),d) for q in qs]
        Ksum = sum((vs[n]*vs[n].adjoint()/norms[n] for n in range(N+1)),S.zeros(d))
        expect(label+f":kernel_sum_{m}", zero(K-Ksum))
        L = A*K+K*A.adjoint()-K
        edge = (vs[N+1]*vs[N].adjoint()+vs[N]*vs[N+1].adjoint())/norms[N]
        expect(label+f":vertical_plus_edge_{m}",zero(L-edge))
        P = H.inv()*C.adjoint()*K.inv()*U
        expect(label+f":actual_constraint_{m}",zero(C*P-U))
        T = S.Matrix.hstack(*[coefficients(polynomial*s**j,N+1) for j in range(m+1)])
        expect(label+f":source_orthogonality_{m}",zero(T.adjoint()*H*P))
        R = S.zeros(N+1,d)
        R[:d,:] = U
        Hsource = T.adjoint()*H*T
        B = -Hsource.inv()*T.adjoint()*H*R
        expect(label+f":same_source_minimum_{m}",zero(P-(R+T*B)))
        G = U.adjoint()*K.inv()*U
        expect(label+f":same_gram_{m}",zero(P.adjoint()*H*P-G))
        W = A.adjoint()*G+G*A-G
        expect(label+f":weight_congruence_{m}",zero(W-U.adjoint()*K.inv()*L*K.inv()*U))
        w, k = vs[N+1],norms[N+1]
        nextK = K+w*w.adjoint()/k
        theta = (w.adjoint()*K.inv()*w)[0]
        nextG = U.adjoint()*nextK.inv()*U
        update = G-U.adjoint()*K.inv()*w*w.adjoint()*K.inv()*U/(k+theta)
        expect(label+f":inverse_update_{m}",zero(nextG-update))
        expect(label+f":det_update_{m}",S.simplify(nextG.det()/G.det()-k/(k+theta))==0)

record = {
    "passed": len(checks),
    "all_passed": True,
    "measure": "explicit Gaussian probability calibration on t; not zeta quadrature",
    "packet_models": ["off-line rational pair", "full double jet"],
    "checks": checks,
}
Path(__file__).with_suffix(".json").write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:v for k,v in record.items() if k!="checks"}))
