#!/usr/bin/env python3
"""Exact finite source calibrations; no arithmetic moments or zero packets are certified."""
from __future__ import annotations
import argparse
import json
import sys
import unittest
from functools import lru_cache
import sympy as s


def clean(A: s.Matrix) -> s.Matrix:
    return A.applyfunc(s.simplify)


def same(A, B) -> bool:
    if isinstance(A, s.MatrixBase):
        return clean(A-B) == s.zeros(*A.shape)
    return s.simplify(A-B) == 0


def center(A: s.Matrix) -> s.Matrix:
    return clean(A-s.trace(A)*s.eye(A.rows)/A.rows)


@lru_cache(None)
def fixture(q: int = 2, x=s.Rational(1, 3), mass: int = 1):
    n = 2*q+1
    z = s.Symbol('S')
    chi = (z-s.Rational(3, 4))**q  # declared repeated-root polynomial, not a zeta packet
    U = s.eye(n)
    U[0, 1] = s.I/2
    U[1, 2] = s.Rational(1, 3)
    U[0, n-1] += s.Rational(1, 5)
    weights = [mass*(i+2) for i in range(n)]
    b = [s.Rational(1, 2)+s.Rational(3*i, 2*(n-1)) for i in range(n)]
    M0 = clean(U.H*s.diag(*weights)*U)
    M1 = clean(U.H*s.diag(*(w*t for w,t in zip(weights,b)))*U)
    M = clean((1-x)*M0+x*M1)
    X = clean(M.inv()*(M1-M0))
    D = clean(M0.inv()*M1)
    lam = [1-x+x*t for t in b]
    a = (lam[0]+lam[-1])/2
    H = clean(s.eye(n)-((1-x)*s.eye(n)+x*D)/a)
    T = clean((D-s.eye(n))/a)
    C = s.eye(n)[:, :q]
    reps, grams, projectors, relations = [], [], [], []
    for N in (q-1,q,2*q-1,2*q):
        B = s.zeros(n,max(0,N-q+1))
        for j in range(B.cols):
            p = s.Poly(chi*z**j,z)
            for i in range(n): B[i,j] = p.nth(i)
        rho = C if B.cols == 0 else clean(C-B*(B.H*M*B).inv()*B.H*M*C)
        G = clean(rho.H*M*rho)
        P = clean(rho*G.inv()*rho.H*M)
        relations.append(B); reps.append(rho); grams.append(G); projectors.append(P)
    Q = clean(projectors[0]+projectors[1]-projectors[2]-projectors[3])
    return dict(n=n,b=b,lam=lam,a=a,M=M,M0=M0,M1=M1,X=X,H=H,T=T,
                Q=Q,P=projectors,R=reps,G=grams,B=relations)


def residual(f, L: int):
    Y = clean(sum((f['H']**r for r in range(L+1)),s.zeros(f['n']))*f['T'])
    R = clean(f['X']-Y)
    return Y,R,center(R)


class ExactSourceTests(unittest.TestCase):
    def test_original_canonical_frames(self):
        for q in (1,2):
            f = fixture(q)
            for B,R,G,P in zip(f['B'],f['R'],f['G'],f['P']):
                self.assertTrue(same(P*P,P))
                self.assertTrue(same(P.H*f['M'],f['M']*P))
                self.assertEqual(s.simplify(s.trace(P)),q)
                self.assertTrue(same(R.H*f['M']*R,G))
                self.assertTrue(same(B.H*f['M']*R,s.zeros(B.cols,q)))

    def test_last_power_and_constant_term(self):
        f = fixture()
        self.assertTrue(same((s.eye(f['n'])-f['H'])*f['X'],f['T']))
        for L in (0,1,3):
            _,R,_ = residual(f,L)
            self.assertTrue(same(R,f['H']**(L+1)*f['X']))

    def test_exact_centered_spectrum(self):
        f = fixture()
        for L in (0,1,3):
            _,R,E = residual(f,L)
            delta = [(1-l/f['a'])**(L+1)*(b-1)/l for b,l in zip(f['b'],f['lam'])]
            var = sum(d*d for d in delta)-sum(delta)**2/f['n']
            self.assertTrue(same(s.trace(R),sum(delta)))
            self.assertTrue(same(s.trace(E*E),var))
            self.assertTrue(same(s.trace(E),0))

    def test_signed_interval_and_full_cross_term(self):
        f = fixture(); Q = f['Q']; P = f['P']
        self.assertTrue(same(s.trace(Q),0))
        Z = s.simplify(s.trace(Q*Q))
        A0,A1 = P[0]-P[2],P[1]-P[3]
        self.assertTrue(same(Z,s.trace(A0*A0)+s.trace(A1*A1)+2*s.trace(A0*A1)))
        self.assertFalse(same(s.trace(A0*A1),0))
        for L in (0,1,3):
            Y,R,E = residual(f,L)
            error = s.simplify(s.trace(R*Q))
            self.assertTrue(same(error,s.trace(E*Q)))
            gap = s.simplify(s.trace(E*E)*Z-error**2)
            self.assertGreaterEqual(gap,0)
            self.assertTrue(same(s.trace(f['X']*Q),s.trace(Y*Q)+error))

    def test_fixed_pair_geometric_bound(self):
        f = fixture(); theta = (f['b'][-1]-f['b'][0])/(f['b'][-1]+f['b'][0])
        K = sum((abs(b-1)/min(1,b))**2 for b in f['b'])
        self.assertGreater(theta,0); self.assertLess(theta,1)
        for L in (0,1,3):
            _,_,E = residual(f,L)
            self.assertGreaterEqual(s.simplify(theta**(2*L+2)*K-s.trace(E*E)),0)

    def test_mass_kept_and_common_scale_cancels(self):
        f,g = fixture(),fixture(mass=7)
        self.assertTrue(same(g['M'],7*f['M']))
        self.assertTrue(same(g['X'],f['X']))
        self.assertTrue(same(g['Q'],f['Q']))
        for G,F in zip(g['G'],f['G']): self.assertTrue(same(G,7*F))

    def test_affine_contraction_including_endpoints(self):
        for x in (s.S(0),s.Rational(1,7),s.Rational(1,2),s.S(1)):
            b = [s.Rational(1,2),s.Rational(5,4),s.S(2)]
            lam = [1-x+x*t for t in b]
            a = (lam[0]+lam[-1])/2
            theta = (b[-1]-b[0])/(b[-1]+b[0])
            for t,l in zip(b,lam):
                self.assertLessEqual(abs(1-l/a),theta)
                self.assertLessEqual(abs((t-1)/l),abs(t-1)/min(1,t))

    def test_scalar_pair_exactness(self):
        n=3; c=s.Rational(7,3); x=s.Rational(2,5)
        D=c*s.eye(n); a=1-x+x*c
        H=s.eye(n)-((1-x)*s.eye(n)+x*D)/a
        self.assertEqual(H,s.zeros(n))
        Q=fixture(1)['Q']
        self.assertTrue(same(s.trace((D-s.eye(n))*Q/a),0))

    def test_proper_boundary_and_signed_coordinates(self):
        theta=s.Matrix([[1,0],[0,1],[0,0]])
        W=s.Matrix([1,0]); v=s.Matrix([0,1]); small=theta*W; full=theta
        self.assertEqual(full.row_join(theta*v).rank(),full.rank())
        self.assertGreater(small.row_join(theta*v).rank(),small.rank())
        q=s.Matrix([[0,1,0],[0,0,1]])  # quotient by the original small boundary
        self.assertNotEqual(q*theta*v,s.zeros(2,1))
        self.assertEqual(s.Matrix([[0,0,1]])*theta*v,s.zeros(1,1))
        injection=s.Matrix([[1,0],[0,1],[0,0],[0,0]])
        signed=s.Matrix([[0,-1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,-1]])
        local=s.Matrix([[0,-1],[1,0]])
        self.assertEqual(signed*injection,injection*local)

    def test_empty_inner_face_retains_outer_label(self):
        present=('source-W',frozenset(),0)
        absent=(None,frozenset(),0)
        self.assertNotEqual(present,absent)


def negative(name: str) -> int:
    f=fixture(); Y,R,E=residual(f,1); Q=f['Q']; P=f['P']
    claims={
      'wrong-power': same(R,f['H']*f['X']),
      'uncentered': same(s.trace(E*E),s.trace(R*R)),
      'diagonal-only': same(s.trace(Q*Q),s.trace((P[0]-P[2])**2)+s.trace((P[1]-P[3])**2)),
      'unweighted': same(P[0].H,P[0]),
      'proper-zero': s.Matrix([[1,0,0]]).T.row_join(s.Matrix([0,1,0])).rank()==1,
    }
    selected = claims if name == 'all' else {name: claims[name]}
    for control, accepted in selected.items():
        print(json.dumps({'control':control,'false_claim_accepted':bool(accepted)},sort_keys=True))
    return 0 if any(selected.values()) else 1


def main() -> int:
    parser=argparse.ArgumentParser()
    parser.add_argument('--negative',choices=['all','wrong-power','uncentered','diagonal-only','unweighted','proper-zero'])
    args=parser.parse_args()
    if args.negative: return negative(args.negative)
    result=unittest.TextTestRunner(stream=sys.stderr).run(unittest.defaultTestLoader.loadTestsFromTestCase(ExactSourceTests))
    print(json.dumps({'success':result.wasSuccessful(),'methods':result.testsRun,
      'scope':'Exact declared finite polynomial/matrix calibrations; not arithmetic moments, zero packets, or path integrals.'},sort_keys=True))
    return 0 if result.wasSuccessful() else 1

if __name__=='__main__': raise SystemExit(main())
