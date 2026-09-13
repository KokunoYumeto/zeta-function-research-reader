#!/usr/bin/env python3
"""Exact source regressions; Gaussian polynomial fixtures are not zeta packets."""
from __future__ import annotations
import argparse
import json
import re
import sys
import unittest
from pathlib import Path
import sympy as s

ALLOWED={'propext','Classical.choice','Quot.sound'}
TARGETS={
 'RelationCurve':'observation gram canonical_gram constituent control'.split(),
 'SpecializationChart':'local_injective local_exact boundary_surjective specialization_square fibre_kernel fibre_exact chart_inverse transported_action pole_iff_invariant'.split(),
 'ActionHull':'contains stable least idempotent eq_self_iff'.split(),
 'CurvatureRestriction':'radialMass_deriv density_deriv density_change jet_as_difference recover_moment curvature_certificate stopping cost_operator return_cost matrix_curvature_certificate'.split(),
}
EXPECTED={'SplitZero.'+ns+'.'+n for ns,names in TARGETS.items() for n in names}

def require(ok, message):
    if not ok: raise AssertionError(message)

def audit(text):
    found={}
    for name,values in re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]",text):
        require(name not in found,'duplicate audit target')
        vals=[x.strip() for x in values.split(',') if x.strip()]
        require(set(vals)<=ALLOWED,'forbidden transitive axiom')
        found[name]=sorted(vals)
    require(set(found)==EXPECTED,'missing or extra audit targets')
    require('error:' not in text.lower(),'Lean error in audit')
    return found

def equal(a,b):
    if isinstance(a,s.MatrixBase) or isinstance(b,s.MatrixBase):
        return all(s.simplify(v)==0 for v in a-b)
    return s.simplify(a-b)==0

def fixture(psi,degree,mass=7):
    u=s.Symbol('u'); q=s.degree(psi,u)
    pol=[s.Integer(1),u]
    for n in range(1,degree): pol.append(s.expand(u*pol[-1]-n*pol[-2]))
    cols=[]
    for n in range(degree+1):
        rem=s.Poly(s.rem(s.I**n*pol[n],psi,u),u)
        cols.append(s.Matrix([rem.nth(a) for a in range(q)]))
    B=s.Matrix.hstack(*cols); O=s.diag(*[mass*s.factorial(n) for n in range(degree+1)])
    K=B*O.inv()*B.conjugate().T; G=K.inv(); R=O.inv()*B.conjugate().T*G
    T=s.Matrix.hstack(*[s.Matrix([s.Poly(s.rem(u**(a+1),psi,u),u).nth(b) for b in range(q)]) for a in range(q)])
    return dict(B=B,O=O,K=K,G=G,R=R,A=s.eye(q)+s.I*T,q=q,degree=degree,mass=mass)

def pair(psi,i,j,mass=7):
    lo,hi=fixture(psi,i,mass),fixture(psi,j,mass)
    X=lo['R'].col_join(s.zeros(j-i,lo['q'])); D=X-hi['R']; G=hi['G']
    ker=D.nullspace()
    if ker:
        Q=s.Matrix.hstack(*ker); P0=Q*(Q.conjugate().T*G*Q).inv()*Q.conjugate().T*G
    else: P0=s.zeros(lo['q'])
    return lo,hi,X,D,P0,s.eye(lo['q'])-P0

class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        u=s.Symbol('u'); cls.data=pair(u**3+u,2,5)

    def test_01_original_source_and_difference(self):
        lo,hi,X,D,P0,P1=self.data; B,O,R,G=(hi[n] for n in ['B','O','R','G'])
        self.assertTrue(equal(B*R,s.eye(3))); self.assertTrue(equal(B*D,s.zeros(3)))
        self.assertTrue(equal(R.conjugate().T*O*D,s.zeros(3)))
        self.assertTrue(equal(D.conjugate().T*O*D,lo['G']-G)); self.assertEqual(O[0,0],7)

    def test_02_affine_curve_and_original_action(self):
        lo,hi,X,D,P0,P1=self.data
        for z in [s.Integer(0),s.Integer(1),s.I,s.Rational(2,3)+s.I/2]:
            R=hi['R']+z*D; G=hi['G']+s.conjugate(z)*z*(lo['G']-hi['G'])
            self.assertTrue(equal(hi['B']*R,s.eye(3)))
            self.assertTrue(equal(R.conjugate().T*hi['O']*R,G))
            A=hi['A']; W=lambda g:A.conjugate().T*g+g*A-2*g
            self.assertTrue(equal(W(G),W(hi['G'])+s.conjugate(z)*z*(W(lo['G'])-W(hi['G']))))

    def test_03_compactified_source_injective(self):
        lo,hi,X,D,P0,P1=self.data
        for w in [0,1,s.I,s.Rational(3,5)]:
            Psi=hi['R']*P0+w*hi['R']*P1+D*P1
            self.assertEqual(Psi.rank(),3)
            self.assertTrue(equal(hi['B']*Psi,P0+w*P1))
        self.assertEqual(P0.rank(),1); self.assertEqual(P1.rank(),2)
        self.assertTrue(equal(D*P0,s.zeros(6,3)))

    def test_04_two_charts_and_exceptional_kernel(self):
        lo,hi,X,D,P0,P1=self.data; w=s.Rational(2,3)
        self.assertTrue(equal((hi['R']+D/w)*(P0+w*P1),hi['R']*P0+w*hi['R']*P1+D*P1))
        self.assertTrue(equal((P0+w*P1)*(P0+P1/w),s.eye(3)))
        self.assertTrue(equal(P0*P1,s.zeros(3))); self.assertEqual(len(P0.nullspace()),P1.rank())

    def test_05_local_polynomial_sequence(self):
        w=s.Symbol('w')
        for v in [0,w,w+w**3,3*w-2*w**2]:
            q,rem=s.div(v,w,w); self.assertEqual(rem,0); self.assertTrue(equal(w*q,v))
        self.assertNotEqual(s.rem(1+w,w,w),0)
        self.assertEqual(s.diag(1,w,w).det(),w**2); self.assertEqual(s.diag(1,0,0).rank(),1)

    def test_06_action_pole_not_discarded(self):
        lo,hi,X,D,P0,P1=self.data; A=hi['A']; w=s.Symbol('w',nonzero=True)
        full=(P0+P1/w)*A*(P0+w*P1)
        blocks=P0*A*P0+w*P0*A*P1+P1*A*P0/w+P1*A*P1
        self.assertTrue(equal(full,blocks)); self.assertNotEqual(P1*A*P0,s.zeros(3))

    def test_07_minimal_hull_and_cyclic_gcd(self):
        lo,hi,X,D,P0,P1=self.data; A=hi['A']; E0=s.Matrix.hstack(*D.nullspace())
        self.assertEqual(s.Matrix.hstack(*[A**n*E0 for n in range(3)]).rank(),3)
        u=s.Symbol('u'); pol=sum(E0[a,0]*u**a for a in range(3))
        self.assertEqual(s.degree(s.gcd(u**3+u,pol),u),0)
        chi=(u-1)**3*(u+2)**2; generators=[(u-1)**2*(u+2),(u-1)**2*(u+2)**2]
        d=s.Poly(s.gcd(chi,s.gcd(*generators)),u).monic().as_expr()
        self.assertEqual(s.degree(d,u),3); self.assertEqual(s.degree(chi,u)-s.degree(d,u),2)

    def test_08_metric_pole_keeps_boundary_degree(self):
        lo,hi,X,D,P0,P1=self.data; w=s.Symbol('w',positive=True)
        Q0=s.Matrix.hstack(*D.nullspace()); Q1=s.Matrix.hstack(*P1.columnspace())
        Psi=(hi['R']*Q0).row_join(w*hi['R']*Q1+D*Q1)
        GM=Psi.conjugate().T*hi['O']*Psi; inclusion=s.diag(1,w,w)
        GA=inclusion.inv().conjugate().T*GM*inclusion.inv()
        self.assertTrue(equal(GA.det(),GM.det()/w**4))
        self.assertEqual(2-(3-1),0); self.assertNotEqual(s.simplify(GM.det().subs(w,0)),0)

    def test_09_return_cost_identification(self):
        lo,hi,X,D,P0,P1=self.data
        Z=hi['K']*(lo['G']-hi['G']); T=lo['K']*hi['G']; H=s.eye(3)-T
        self.assertTrue(equal(Z,(hi['K']-lo['K'])*lo['G']))
        self.assertTrue(equal(s.eye(3)+Z,T.inv())); self.assertTrue(equal(Z*T,H))
        self.assertEqual(Z.eigenvals(),{0:1,s.Rational(19,4):1,s.Rational(83,10):1})
        self.assertEqual(T.eigenvals(),{1:1,s.Rational(4,23):1,s.Rational(10,93):1})

    def test_10_second_fundamental_map_and_observation(self):
        lo,hi,X,D,P0,P1=self.data; O=hi['O']; C=lo['G']-hi['G']; z=s.Rational(2,3)+s.I/4
        R=hi['R']+z*D; G=hi['G']+s.conjugate(z)*z*C
        P=R*G.inv()*R.conjugate().T*O; N=(s.eye(6)-P)*D
        self.assertTrue(equal(P*P,P))
        self.assertTrue(equal(N.conjugate().T*O*N,C-s.conjugate(z)*z*C*G.inv()*C))
        self.assertTrue(equal(hi['B']*P*D,s.conjugate(z)*G.inv()*C))
        self.assertTrue(equal(hi['B']*N,-s.conjugate(z)*G.inv()*C))
        self.assertNotEqual(hi['B']*N,s.zeros(3))

    def test_11_curvature_and_radial_antiderivative(self):
        lo,hi,X,D,P0,P1=self.data; Z=hi['K']*(lo['G']-hi['G']); t=s.Symbol('t',nonnegative=True)
        vals=[s.Integer(0),s.Rational(19,4),s.Rational(83,10)]
        kap=sum(l/(1+t*l)**2 for l in vals); M=sum(t*l/(1+t*l) for l in vals)
        self.assertTrue(equal(s.diff(M,t),kap)); self.assertEqual(s.limit(M,t,s.oo),2)
        self.assertTrue(equal(s.trace(Z*(s.eye(3)+t*Z).inv()**2),kap))
        self.assertTrue(equal(s.prod(1+l for l in vals),lo['G'].det()/hi['G'].det()))

    def test_12_curvature_jets_recover_trace_moments(self):
        vals=[s.Rational(19,4),s.Rational(83,10),s.Integer(0)]; t=s.Symbol('t')
        x=[l/(1+l) for l in vals]; moment=lambda n:sum(a**n for a in x)
        require(not any(a.has(s.Float) for a in x),'inexact spectrum in exact fixture')
        kap=sum(l/(1+t*l)**2 for l in vals)
        for n in range(7):
            self.assertTrue(equal(s.diff(kap,t,n).subs(t,0),(-1)**n*s.factorial(n+1)*sum(l**(n+1) for l in vals)))
            self.assertTrue(equal((-1)**n*s.diff(kap,t,n).subs(t,1)/s.factorial(n+1),moment(n+1)-moment(n+2)))
        for m in range(1,8):
            rec=moment(1)-sum((-1)**n*s.diff(kap,t,n).subs(t,1)/s.factorial(n+1) for n in range(m-1))
            self.assertTrue(equal(rec,moment(m)))

    def test_13_constituent_source_map(self):
        lo,hi,X,D,P0,P1=self.data; eig=hi['A'].eigenvects()[0][2][0]
        for z in [0,1,s.I]: self.assertTrue(equal((hi['R']+z*D)*eig,hi['R']*eig+z*D*eig))
        self.assertEqual(s.Matrix.hstack(eig,hi['A']*eig).rank(),1)

    def test_14_dual_boundary_pairing(self):
        w=s.Symbol('w',nonzero=True); alpha=s.diag(1,w,w); dual=alpha.inv().T
        self.assertTrue(equal(alpha.T*dual,s.eye(3)))
        self.assertEqual(alpha.det(),w**2); self.assertEqual(dual.det(),w**(-2))

    def test_15_fixed_degree_does_not_bound_logarithmic_moment(self):
        t=s.Symbol('t',nonnegative=True)
        for L in [1,4,100]:
            M=2*t*L/(1+t*L); self.assertEqual(s.limit(M,t,s.oo),2)
            self.assertEqual(M.subs(t,s.Rational(1,L)),1)
            self.assertEqual((s.eye(2)+L*s.eye(2)).det(),(1+L)**2)

    def test_16_audit_accepts_exact_reports(self):
        text='\n'.join("'"+n+"' depends on axioms: [propext, Classical.choice, Quot.sound]" for n in sorted(EXPECTED))
        self.assertEqual(len(audit(text)),29)

    def test_17_audit_rejects_missing_or_forbidden(self):
        with self.assertRaises(AssertionError): audit('')
        text='\n'.join("'"+n+"' depends on axioms: [sorryAx]" for n in sorted(EXPECTED))
        with self.assertRaises(AssertionError): audit(text)

def main():
    p=argparse.ArgumentParser(); p.add_argument('--audit',type=Path); p.add_argument('--negative',action='store_true')
    args=p.parse_args()
    if args.negative: require(False,'intentional specialization negative control')
    if args.audit:
        print(json.dumps({'status':'PASS','reports':audit(args.audit.read_text())},sort_keys=True)); return 0
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(Tests); names=[t._testMethodName for t in suite]
    result=unittest.TestResult(); suite.run(result)
    print(json.dumps({'status':'PASS' if result.wasSuccessful() else 'FAIL','methods':result.testsRun,'tests':names,
        'failures':[(str(t),e) for t,e in result.failures],'errors':[(str(t),e) for t,e in result.errors],
        'scope':'exact polynomial sources; no arithmetic zero sampling, sheaf or integral certificate'},indent=2,sort_keys=True))
    return 0 if result.wasSuccessful() else 1
if __name__=='__main__': sys.exit(main())
