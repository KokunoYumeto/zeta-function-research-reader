#!/usr/bin/env python3
"""Exact finite calibrations; no zeta-zero or arithmetic-integral assertions."""
from __future__ import annotations
import argparse
import json
import sympy as S

x = S.Symbol('x')
I = S.I

def need(value: bool, reason: str) -> None:
    if not value:
        raise AssertionError(reason)

def zero(M: S.Matrix) -> bool:
    return all(S.simplify(a) == 0 for a in M)

def fixture():
    R = S.Matrix([[1,I,1,0],[0,2,1,I],[0,0,1,1],[1,0,0,2]])
    G = R.H * R + S.diag(1,2,3,4)
    K = G.inv()
    L = S.Matrix([[1,0,1,I],[0,1,I,1]])
    Q = (L*K*L.H).inv()
    section = K*L.H*Q
    fixed = L.H*(L*L.H).inv()
    inc = S.Matrix.hstack(*L.nullspace())
    kap = S.Matrix.hstack(inc, fixed).inv()[:inc.cols,:]
    X = S.Matrix([[1,2],[I,1],[2,1-I],[1+I,3]])
    lam = L*X
    residual = X-section*lam
    return G,K,L,Q,section,fixed,inc,kap,X,lam,residual

def metric_section():
    G,K,L,Q,A,_,_,_,_,_,_ = fixture()
    need(zero(L*A-S.eye(2)), 'section observation')
    need(zero(A.H*G-Q*L), 'source dual')
    need(zero(A.H*G*A-Q), 'section Gram')
    need(zero(G*K-S.eye(4)), 'original inverse')

def mixed_residual():
    G,_,L,Q,A,_,_,_,X,lam,r = fixture()
    need(zero(L*r), 'kernel membership')
    need(zero(r.H*G*A), 'kernel-section orthogonality')
    E = X.H*G*X-lam.H*Q*lam
    need(zero(r.H*G*r-E), 'complete residual Gram')
    need(S.simplify(E[0,1]) != 0, 'fixture must have mixed covariance')

def section_correction():
    G,_,L,_,A,T,J,kap,X,lam,r = fixture()
    need(zero(J*kap-(S.eye(4)-T*L)), 'fixed splitting')
    v = kap*X-kap*A*lam
    need(zero(J*v-r), 'OPR section correction')
    need(zero(v.H*(J.H*G*J)*v-r.H*G*r), 'original kernel Gram')
    need(not zero(J*kap*X-r), 'uncorrected section must differ')

def ordered_factors():
    G,_,_,Q,_,_,_,_,X,lam,r = fixture()
    t = S.simplify((X.H*G*X)[0,0])
    xi = S.simplify((lam.H*Q*lam)[0,0])
    a = S.simplify((r.H*G*r)[0,0])
    need(xi > 0 and a > 0 and t == xi+a, 'positive retained costs')
    need(S.simplify((1+xi)*(1+a/(1+xi))-(1+t)) == 0, 'ordered factors')

def mass_scaling():
    G,K,L,Q,A,_,_,_,_,_,_ = fixture()
    scale = S.Rational(7)
    K2 = (scale*G).inv()
    Q2 = (L*K2*L.H).inv()
    need(zero(Q2-scale*Q), 'quotient mass')
    need(zero(K2*L.H*Q2-A), 'section mass invariance')

def empty_boundary():
    G = S.Matrix([[3,1],[1,2]])
    L = S.zeros(0,2)
    Q = S.zeros(0,0)
    A = G.inv()*L.H*Q
    X = S.eye(2)
    r = X-A*L*X
    need(A.shape == (2,0) and zero(r-X), 'empty section convention')
    need(zero(r.H*G*r-G), 'empty boundary leaves whole kernel')

def algebra(chi, rows):
    chi = S.Poly(chi, x, domain=S.QQ).monic()
    q = chi.degree()
    def vector(p):
        r = S.rem(S.Poly(p, x, domain=S.QQ), chi)
        return S.Matrix([r.nth(j) for j in range(q)])
    A = S.Matrix.hstack(*(vector(x**(j+1)) for j in range(q)))
    L = S.zeros(len(rows),q)
    for k,a in enumerate(rows):
        for j in range(q):
            L[k,j] = vector(a*x**j)[q-1]
    O = S.Matrix.vstack(*(L*A**j for j in range(q)))
    d = chi
    for a in rows:
        d = S.gcd(d, S.Poly(a,x,domain=S.QQ))
    d = d.monic()
    need(O.rank() == q-d.degree(), 'residue gcd rank')
    if d.degree():
        p = S.exquo(chi,d).as_expr()
        Z = S.Matrix.hstack(*(vector(p*x**j) for j in range(d.degree())))
    else:
        Z = S.zeros(q,0)
    need(zero(O*Z), 'explicit invisible ideal')
    need(Z.rank() == q-O.rank(), 'entire invisible kernel')
    need(zero(O*A*Z), 'invariance of retained kernel')
    return chi,A,L,O,Z

def residue_rank_cases():
    chi = (x-S.Rational(3,4))**3*(x-S.Rational(1,4))**2
    for rows in [[1],[x-S.Rational(3,4)],
                 [(x-S.Rational(3,4))**2,(x-S.Rational(3,4))*(x-S.Rational(1,4))],[]]:
        algebra(chi,rows)
    algebra((x-1)**4,[(x-1)**2])

def original_shift():
    chi,A,L,O,_ = algebra((x-1)**3*(x+2)**2,[1,x-1])
    q,r = A.rows,L.rows
    T = S.zeros(q*r,q*r)
    for j in range(q-1):
        T[j*r:(j+1)*r,(j+1)*r:(j+2)*r] = S.eye(r)
    for j in range(q):
        T[(q-1)*r:q*r,j*r:(j+1)*r] = -chi.nth(j)*S.eye(r)
    need(zero(O*A-T*O),'original coefficient shift')
    need(zero(O[:r,:]-L),'first component is original observation')

def transient_kernel():
    _,A,L,O,_ = algebra(x**4,[1])
    z = S.Matrix([1,0,0,0])
    need(zero(L*z) and not zero(O*z), 'one-step zero remains observable later')
    need(not zero(L*A**3*z), 'full nilpotent iterate is retained')
    _,_,_,O2,Z2 = algebra(x**4,[x])
    need(O2.rank() == 3 and Z2.cols == 1, 'socle failure is not silently removed')

TESTS = [metric_section,mixed_residual,section_correction,ordered_factors,
         mass_scaling,empty_boundary,residue_rank_cases,original_shift,transient_kernel]

def negative():
    G,_,L,Q,A,_,J,kap,X,lam,r = fixture()
    gram = r.H*G*r
    t = S.simplify((X.H*G*X)[0,0]); xi = S.simplify((lam.H*Q*lam)[0,0])
    _,N,obs,O,_ = algebra(x**4,[1])
    _,_,_,O2,_ = algebra(x**4,[x])
    wrong = {
      'omit-section-correction': zero(r-J*kap*X),
      'diagonal-only': zero(gram-S.diag(*gram.diagonal())),
      'omit-denominator': S.simplify((1+xi)*(1+t-xi)-(1+t)) == 0,
      'one-step-closed': zero(obs*N**3*S.Matrix([1,0,0,0])),
      'always-faithful': O2.rank() == 4,
    }
    for name,value in wrong.items():
        print(json.dumps({'control':name,'false_claim_accepted':bool(value)},sort_keys=True))
    return 1 if all(not value for value in wrong.values()) else 0

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--negative',action='store_true')
    args=parser.parse_args()
    if args.negative:
        raise SystemExit(negative())
    for test in TESTS:
        test()
    print(json.dumps({'status':'pass','methods':len(TESTS),
      'tests':[t.__name__ for t in TESTS],
      'scope':'Exact declared polynomial and matrix fixtures; no arithmetic zero or integral certificate.'},sort_keys=True))

if __name__ == '__main__':
    main()
