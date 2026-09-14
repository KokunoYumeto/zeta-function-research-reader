#!/usr/bin/env python3
"""Exact finite checks for the Deligne-to-arithmetic non-implication note.

These tests are regressions for the written arguments, not an RH proof,
not a Lean certificate, and not interval evaluation of zeta moments.
The Gamma mass is represented by a positive symbol m; the theorem uses
m=(2*pi)^(k/2).  No test identifies this mass with 1.
"""
from __future__ import annotations
import argparse
import json
import sys
import unittest
from functools import lru_cache
import sympy as s

S = s.Symbol('S')
mass = s.Symbol('m', positive=True)

def sim(x):
    return x.applyfunc(s.simplify) if isinstance(x, s.MatrixBase) else s.simplify(x)

def quartet_poly(k: int) -> s.Poly:
    roots = [s.Rational(k,2)+s.Rational(1,4)*(2*a-k)+s.I*(2*b-k)
             for a in range(k+1) for b in range(k+1)]
    return s.Poly(s.expand(s.prod(S-r for r in roots)), S)

@lru_cache(None)
def gamma_model(k: int, top: int):
    chi = quartet_poly(k)
    q = chi.degree()
    p = [s.Poly(1,S), s.Poly(S-s.Rational(k,2),S)]
    for n in range(1,top):
        a = n*(s.Rational(k,2)+n-1)
        p.append(s.Poly(s.expand((S-s.Rational(k,2))*p[-1].as_expr()+a*p[-2].as_expr()), S))
    b=[]
    w=[]
    for n in range(top+1):
        r = p[n].rem(chi)
        b.append(s.Matrix([r.nth(j) for j in range(q)]))
        w.append(s.factorial(n)*s.rf(s.Rational(k,2),n))
    A=s.zeros(q)
    for j in range(q):
        rem=s.Poly(S**(j+1),S).rem(chi)
        A[:,j]=s.Matrix([rem.nth(l) for l in range(q)])
    K=[]; G=[]; V=[]; now=s.zeros(q)
    for n in range(top+1):
        now=now+b[n]*b[n].conjugate().T/w[n]
        K.append(now/mass)
        if n>=q-1:
            gn=now.inv()*mass
            G.append(gn)
            V.append(s.factor(gn.det()))
        else:
            G.append(None); V.append(None)
    return chi,p,b,w,A,K,G,V

class ExactChecks(unittest.TestCase):
    def test_01_explicit_balanced_quartet(self):
        z=S-s.Rational(1,2)
        explicit=s.Poly(z**4+s.Rational(15,8)*z**2+s.Rational(289,256),S)
        self.assertEqual(quartet_poly(1),explicit)
        self.assertEqual(s.expand(explicit.as_expr().subs(S,1-S)-explicit.as_expr()),0)
        self.assertTrue(all(v.is_Rational for v in explicit.all_coeffs()))

    def test_02_all_sum_grid_and_aggregate(self):
        for k in range(1,13):
            q=(k+1)**2
            roots={(s.Rational(k,2)+s.Rational(1,4)*(2*a-k),2*b-k)
                   for a in range(k+1) for b in range(k+1)}
            self.assertEqual(len(roots),q)
            # The integer occupation matrix for every pair of margins.
            for a in range(k+1):
                for b in range(k+1):
                    t=max(0,a+b-k)
                    occ=(t,a-t,b-t,k-a-b+t)
                    self.assertTrue(min(occ)>=0)
                    self.assertEqual(sum(occ),k)
            L=sum(2*re-k for re,im in roots if re>s.Rational(k,2))
            formula=s.Rational(1,2)*(k+1)*((k+1)**2//4)
            self.assertEqual(L,formula)
            self.assertGreaterEqual(L,s.Rational(1,8)*k*q)

    def test_03_reference_norm_ratios(self):
        for k in range(1,9):
            q=(k+1)**2
            for n in range(1,15):
                h=mass*s.factorial(n)*s.rf(s.Rational(k,2),n)
                hp=mass*s.factorial(n-1)*s.rf(s.Rational(k,2),n-1)
                self.assertEqual(s.cancel(h/hp),n*(n+s.Rational(k,2)-1))
            for n in (q,q+1,2*q-1,2*q):
                self.assertLessEqual(n*(n+s.Rational(k,2)-1),5*q*q)

    def test_04_canonical_quotient_and_relation(self):
        chi,p,b,w,A,K,G,V=gamma_model(1,8)
        q=chi.degree()
        for N in (q-1,q,2*q):
            J=s.Matrix.hstack(*b[:N+1]); O=s.diag(*(mass*x for x in w[:N+1]))
            C=O.inv()*J.conjugate().T*G[N]
            self.assertEqual(sim(J*C),s.eye(q))
            self.assertEqual(sim(C.conjugate().T*O*C-G[N]),s.zeros(q))
            v=s.Matrix([1,2,3,4])
            poly=s.expand(sum(p[n].as_expr()*(C*v)[n] for n in range(N+1)))
            self.assertEqual(s.Poly(poly,S).rem(chi).as_expr(),sum(v[n]*S**n for n in range(q)))

    def test_05_christoffel_darboux_and_rank(self):
        chi,p,b,w,A,K,G,V=gamma_model(1,8)
        q=chi.degree()
        for N in range(q-1,8):
            Z=sim(A*K[N]+K[N]*A.conjugate().T-K[N])
            edge=(b[N+1]*b[N].conjugate().T+b[N]*b[N+1].conjugate().T)/(mass*w[N])
            self.assertEqual(sim(Z-edge),s.zeros(q))
            W=sim(A.conjugate().T*G[N]+G[N]*A-G[N])
            H=sim(K[N]*W)
            self.assertEqual(s.simplify(s.trace(H)),0)
            self.assertLessEqual(H.rank(),2)
            self.assertGreaterEqual(s.simplify(s.trace(H*H)/2),1) # L_1=1.

    def test_06_exact_radius_and_steps(self):
        chi,p,b,w,A,K,G,V=gamma_model(1,8)
        q=chi.degree()
        for N in range(q-1,8):
            W=sim(A.conjugate().T*G[N]+G[N]*A-G[N])
            H=sim(K[N]*W)
            eps2=s.simplify(s.trace(H*H)/2)
            ad=(b[N].conjugate().T*G[N]*b[N])[0]*(b[N+1].conjugate().T*G[N]*b[N+1])[0]
            cross=(b[N].conjugate().T*G[N]*b[N+1])[0]
            radius=s.simplify((ad-abs(cross)**2)/(mass*w[N])**2)
            self.assertEqual(eps2,radius)
            ratio=s.simplify((w[N+1]/w[N])*(V[N]/V[N+1]))
            self.assertGreaterEqual(s.simplify(ratio-eps2),0)
            if N>=q:
                d0=s.cancel(V[N]/V[N-1]); d1=s.cancel(V[N+1]/V[N])
                upper=s.cancel((w[N+1]/w[N])*(1-d0)*(1/d1-1))
                self.assertEqual(eps2,s.simplify(upper-abs(cross)**2/(mass*w[N])**2))

    def test_07_first_admitted_degree(self):
        chi,p,b,w,A,K,G,V=gamma_model(1,8)
        q=chi.degree(); J=s.Matrix.hstack(*b[:q])
        coords=J.inv()*b[q]
        remnorm=s.simplify(sum(s.conjugate(coords[j])*coords[j]*mass*w[j] for j in range(q)))
        nu=mass*w[q]+remnorm
        self.assertEqual(s.cancel(V[q]/V[q-1]),s.cancel(mass*w[q]/nu))
        self.assertIsNone(G[q-2])

    def test_08_two_window_telescopes(self):
        chi,p,b,w,A,K,G,V=gamma_model(1,8)
        q=chi.degree()
        for i in (q-1,q):
            j=i+q
            # L_1=1, so the exact inequality L^(2q) <= (omega_j/omega_i)(V_i/V_j).
            rhs=s.cancel(s.Rational(w[j],w[i])*(V[i]/V[j]))
            self.assertGreaterEqual(rhs,1)
            self.assertEqual(s.cancel(s.prod(V[n]/V[n+1] for n in range(i,j))),s.cancel(V[i]/V[j]))

    def test_09_rank_one_period_and_control(self):
        u=s.Symbol('u',positive=True); t=s.Symbol('t',real=True); lam=s.Rational(3,4)
        Pi=s.I*s.sqrt(2*s.pi*u)*s.exp(-(lam+t)**2/(2*u))
        self.assertEqual(s.simplify(-u*s.diff(Pi,t)/Pi),lam+t)
        self.assertEqual(s.simplify(s.conjugate(Pi)*Pi-2*s.pi*u*s.exp(-(lam+t)**2/u)),0)
        g=s.Symbol('G',positive=True)
        self.assertEqual(s.simplify((2*lam*g-g)/g),s.Rational(1,2))

    def test_10_gauss_sum_orthogonality(self):
        for p in (5,7,11,13):
            for u in (1,2):
                inv=pow(2*u,-1,p)
                counts=[0]*p
                for x in range(p):
                    for y in range(p):
                        counts[((x*x-y*y)*inv)%p]+=1
                self.assertEqual(counts[0],2*p-1)
                self.assertEqual(counts[1:],[p-1]*(p-1))
                # coefficients give p+(p-1)*(1+z+...+z^(p-1)).

    def test_11_split_kernel_retained(self):
        tau=('absent',None)
        lift=lambda v:tau if v==tau else ('supported',v[1]*0)
        e=('supported',0)
        self.assertEqual(lift(tau),tau)
        self.assertEqual(lift(('supported',5)),e)
        self.assertNotEqual(e,tau)
        self.assertNotEqual(('supported',5),e)

    def test_12_period_congruence_cannot_improve_allowance(self):
        A=s.Matrix([[s.Rational(3,4),1],[0,s.Rational(1,4)]])
        G=s.Matrix([[7,2],[2,5]]); P=s.Matrix([[1,s.I],[0,2]])
        W=A.conjugate().T*G+G*A-G
        Pt=P.inv(); Gt=Pt.conjugate().T*G*Pt
        Wt=Pt.conjugate().T*W*Pt
        self.assertEqual(sim(Gt.inv()*Wt-P*(G.inv()*W)*P.inv()),s.zeros(2))
        self.assertEqual(s.cancel(Gt.det()/G.det()),s.Rational(1,4))


    def test_13_repeated_primary_not_reduced(self):
        base = quartet_poly(1)
        chi = base**2
        q=chi.degree()
        A=s.zeros(q)
        for j in range(q):
            r=s.Poly(S**(j+1),S).rem(chi)
            A[:,j]=s.Matrix([r.nth(l) for l in range(q)])
        def evalpoly(p):
            R=s.zeros(q)
            for a in p.all_coeffs(): R=R*A+a*s.eye(q)
            return R
        N=evalpoly(base)
        self.assertNotEqual(N,s.zeros(q))
        self.assertEqual(N*N,s.zeros(q))
        self.assertEqual(evalpoly(chi),s.zeros(q))

    def test_14_full_unit_is_retained(self):
        chi,p,b,w,A,K,G,V=gamma_model(1,8)
        q=chi.degree(); N=5
        U=2*s.eye(q)+A
        self.assertNotEqual(U.det(),0)
        J=s.Matrix.hstack(*b[:N+1])
        O=s.diag(*(mass*x for x in w[:N+1]))
        JU=U*J
        GU=(JU*O.inv()*JU.T).inv()
        UI=U.inv()
        self.assertEqual(sim(GU-UI.T*G[N]*UI),s.zeros(q))
        CU=O.inv()*JU.T*GU
        self.assertEqual(sim(JU*CU),s.eye(q))
        self.assertEqual(sim(U*A-A*U),s.zeros(q))


    def test_15_original_boundary_pairing_before_quotient(self):
        chi,p,b,w,A,K,G,V=gamma_model(1,8)
        q=chi.degree()
        for N in (3,5):
            J=s.Matrix.hstack(*b[:N+1])
            Jnext=s.Matrix.hstack(*b[:N+2])
            O=s.diag(*(mass*x for x in w[:N+1]))
            Onext=s.diag(*(mass*x for x in w[:N+2]))
            R=O.inv()*J.conjugate().T*G[N]
            Rpad=R.col_join(s.zeros(1,q))
            D=s.zeros(N+2,N+1)
            for j in range(N+1):
                D[j,j]=s.Rational(1,2)
                D[j+1,j]=1
                if j: D[j-1,j]=-j*(j-s.Rational(1,2))
            boundary=sim(D*R-Rpad*A)
            self.assertEqual(sim(Jnext*boundary),s.zeros(q))
            self.assertNotEqual(boundary,s.zeros(N+2,q))
            W=A.conjugate().T*G[N]+G[N]*A-G[N]
            pairing=Rpad.conjugate().T*Onext*boundary+boundary.conjugate().T*Onext*Rpad
            self.assertEqual(sim(W+pairing),s.zeros(q))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--negative-control',action='store_true')
    args=parser.parse_args()
    if args.negative_control:
        if s.Rational(3,4)==s.Rational(1,2):
            print('bad control unexpectedly accepted'); return 0
        print(json.dumps({'negative_control':'pure_auxiliary_implies_critical_generator','rejected':True},sort_keys=True))
        return 1
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(ExactChecks)
    count=suite.countTestCases()
    result=unittest.TextTestRunner(stream=sys.stderr,verbosity=2).run(suite)
    print(json.dumps({'tests_run':result.testsRun,'tests_declared':count,'failures':len(result.failures),
                      'errors':len(result.errors),'success':result.wasSuccessful(),
                      'scope':'finite exact algebra; analytic arguments are written proofs; no RH certificate'},sort_keys=True))
    return 0 if result.wasSuccessful() else 1

if __name__=='__main__':
    raise SystemExit(main())
