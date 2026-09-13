#!/usr/bin/env python3
"""Exact declared fixtures. Not arithmetic zero data, quadrature, or a Lean proof.

The adaptive certificate computes traces of matrix powers; no eigenvalue
solver, matrix logarithm, floating-point norm, or supplied spectral gap is used.
"""
from __future__ import annotations
import argparse
import json
import math
import re
import sys
import unittest
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import sympy as sp

R = sp.Rational
S, z = sp.symbols('S z')
CHIS = ((S-1)**2, (S-1)**2+1, (S-1)**3)
ALLOWED = {'propext', 'Classical.choice', 'Quot.sound'}
TARGETS = {
    **{n:'SplitZero.Restriction.' for n in (
        'metric_adjoint','return_comp','return_inverse','action_defect','deficit_comp',
        'determinant_transport','retained_gram','representative_section',
        'representative_adjoint','representative_gram','source_restriction',
        'relation_decomposition','relation_observations','relation_gram','relation_cocycle')},
    **{n:'SplitZero.RestrictionLog.' for n in (
        'hasSum_remainder','remainder_nonneg','double_remainder_le','sharp_remainder_le',
        'adaptive_scalar','prefix_as_moments','prefix_lower','sharp_trace_upper',
        'adaptive_trace_upper','powerTrace_tendsto_zero','exists_stopping_degree')}
}

def audit(text: str) -> dict:
    found = {}
    pattern = r"'([^']+)' (?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)"
    for match in re.finditer(pattern, text, re.S):
        name=match.group(1)
        if name in found:
            raise ValueError('duplicate axiom report: '+name)
        axioms={a.strip() for a in (match.group(2) or '').split(',') if a.strip()}
        if not axioms <= ALLOWED:
            raise ValueError('unapproved transitive axiom: '+repr(axioms))
        found[name]=sorted(axioms)
    expected={prefix+n for n,prefix in TARGETS.items()}
    if set(found) != expected:
        raise ValueError('unexpected target set: '+repr(set(found)^expected))
    return found

def exact(a,b) -> bool:
    if isinstance(a,sp.MatrixBase) or isinstance(b,sp.MatrixBase):
        return all(sp.simplify(v)==0 for v in sp.Matrix(a)-sp.Matrix(b))
    return sp.simplify(a-b)==0

@lru_cache(None)
def frame(chi, N: int, mass=7):
    q=sp.degree(chi,S)
    if q < 1 or N < q-1:
        raise ValueError('nonempty quotient and admitted source degree required')
    ps=[sp.S.One]
    if N:
        ps.append(S-1)
    for n in range(1,N):
        ps.append(sp.expand((S-1)*ps[-1]+n*ps[-2]))
    def column(p):
        rem=sp.Poly(sp.rem(p,chi,S),S)
        return sp.Matrix([rem.nth(j) for j in range(q)])
    B=sp.Matrix.hstack(*(column(p) for p in ps))
    O=sp.diag(*(sp.Integer(mass)*math.factorial(n) for n in range(N+1)))
    K=B*O.inv()*B.H
    G=K.inv()
    Rep=O.inv()*B.H*G
    A=sp.Matrix.hstack(*(column(S**(j+1)) for j in range(q)))
    return B,O,K,G,Rep,A

def pad(X,rows):
    return X.col_join(sp.zeros(rows-X.rows,X.cols))

def log_interval(t,cutoff=100):
    t=R(t)
    if t<1:
        lo,hi=log_interval(1/t,cutoff)
        return -hi,-lo
    y=(t-1)/(t+1)
    lo=2*sum(y**(2*j+1)/R(2*j+1) for j in range(cutoff))
    tail=2*y**(2*cutoff+1)/(R(2*cutoff+1)*(1-y*y))
    return lo,lo+tail

def adaptive(H,p):
    if p<1 or H.rows!=H.cols:
        raise ValueError('positive degree and square loss matrix required')
    power=sp.eye(H.rows); moments=[]
    for n in range(1,2*p+1):
        power=power*H
        moments.append(sp.trace(power))
    s=moments[p-1]
    if not (0<=s<1):
        raise ValueError('trace-moment stopping condition not certified')
    low=sum(moments[n-1]/n for n in range(1,p+1))
    block=sum(moments[n-1]/n for n in range(p+1,2*p+1))
    return sp.factor(low),sp.factor(low+block/(1-s))

class Tests(unittest.TestCase):
    def test_01_actual_weighted_minimum(self):
        for chi in CHIS:
            for N in range(int(sp.degree(chi,S))-1,7):
                B,O,K,G,Q,_=frame(chi,N)
                self.assertTrue(exact(B*Q,sp.eye(G.rows)))
                self.assertTrue(exact(Q.H*O*Q,G))
                self.assertTrue(exact(Q.H*O,G*B))
    def test_02_reverse_adjoint_composition(self):
        for chi in CHIS:
            i=int(sp.degree(chi,S))-1; j=i+2; l=j+2
            *_,=()
            Bi,Oi,Ki,Gi,Qi,A=frame(chi,i)
            Bj,Oj,Kj,Gj,Qj,_=frame(chi,j)
            Bl,Ol,Kl,Gl,Ql,_=frame(chi,l)
            Tij=Ki*Gj; Tjl=Kj*Gl
            self.assertTrue(exact(Gi*Tij,Gj))
            self.assertTrue(exact(Tij*Tjl,Ki*Gl))
            self.assertTrue(exact(Tij*(Kj*Gi),sp.eye(Gi.rows)))
    def test_03_source_restriction(self):
        for chi in CHIS:
            i=int(sp.degree(chi,S))-1; j=i+3
            Bi,Oi,Ki,Gi,Qi,A=frame(chi,i)
            Bj,Oj,Kj,Gj,Qj,_=frame(chi,j)
            P=sp.diag(*([1]*(i+1)+[0]*(j-i)))
            X=pad(Qi,j+1); T=Ki*Gj
            self.assertTrue(exact(P*Qj,X*T))
            self.assertTrue(exact(X-Qj,X*(sp.eye(Gi.rows)-T)-(sp.eye(j+1)-P)*Qj))
    def test_04_relation_and_energy(self):
        for chi in CHIS:
            i=int(sp.degree(chi,S))-1; j=i+3
            Bi,Oi,Ki,Gi,Qi,A=frame(chi,i)
            Bj,Oj,Kj,Gj,Qj,_=frame(chi,j)
            d=pad(Qi,j+1)-Qj
            self.assertTrue(exact(Bj*d,sp.zeros(Gi.rows)))
            self.assertTrue(exact(d.H*Oj*d,Gi-Gj))
            self.assertTrue(exact(Qj.H*Oj*d,sp.zeros(Gi.rows)))
    def test_05_action_defect(self):
        for chi in CHIS:
            i=int(sp.degree(chi,S))-1; j=i+3
            Bi,Oi,Ki,Gi,Qi,A=frame(chi,i)
            Bj,Oj,Kj,Gj,Qj,_=frame(chi,j)
            T=Ki*Gj
            Hi=Ki*A.H*Gi+A-2*sp.eye(A.rows)
            Hj=Kj*A.H*Gj+A-2*sp.eye(A.rows)
            self.assertTrue(exact(A*T-T*A,Hi*T-T*Hj))
        self.assertNotEqual(A*T-T*A,sp.zeros(A.rows))
    def test_06_retained_low_energy(self):
        Bi,Oi,Ki,Gi,Qi,A=frame(CHIS[0],1)
        Bj,Oj,Kj,Gj,Qj,_=frame(CHIS[0],3)
        T=Ki*Gj; P=sp.diag(1,1,0,0)
        self.assertTrue(exact((P*Qj).H*Oj*(P*Qj),Gj*Ki*Gj))
        self.assertTrue(exact(T.H*Gi*T,Gj*Ki*Gj))
    def test_07_nonnormal_coordinate_covariance(self):
        _,_,Ki,Gi,_,_=frame(CHIS[0],1)
        _,_,Kj,Gj,_,_=frame(CHIS[0],4)
        U=sp.Matrix([[1,1+sp.I],[0,2]])
        Gip=U.H*Gi*U; Gjp=U.H*Gj*U
        Tp=Gip.inv()*Gjp
        self.assertTrue(exact(Tp,U.inv()*(Ki*Gj)*U))
        self.assertTrue(exact(Tp.det(),(Ki*Gj).det()))
        self.assertTrue(exact(sp.trace((sp.eye(2)-Tp)**3),sp.trace((sp.eye(2)-Ki*Gj)**3)))
    def test_08_noncommuting_return_matrices(self):
        B=sp.Matrix([[1,0,1,2,1],[0,1,sp.I,1,2+sp.I]])
        O=sp.diag(7,14,21,28,35)
        def kg(n):
            C=B[:,:n]; D=O[:n,:n]
            K=C*D.inv()*C.H
            return K,K.inv()
        Ki,Gi=kg(2); Kj,Gj=kg(3); Kl,Gl=kg(5)
        T=Ki*Gj; U=Kj*Gl
        self.assertTrue(exact(T*U,Ki*Gl))
        self.assertFalse(exact(T*U,U*T))
        self.assertTrue(exact(sp.eye(2)-T*U,(sp.eye(2)-T)+T*(sp.eye(2)-U)))
    def test_09_cauchy_binet_and_degree_marker(self):
        B,O,K,G,Rep,A=frame(CHIS[0],4)
        i=1; Ki=frame(CHIS[0],i)[2]
        terms=0
        for D in combinations(range(B.cols),B.rows):
            minor=B[:,list(D)].det()
            weight=minor*sp.conjugate(minor)/sp.prod(O[d,d] for d in D)
            terms+=weight*z**sum(d>i for d in D)
        self.assertTrue(exact(terms,(Ki+z*(K-Ki)).det()))
        T=Ki*G
        self.assertTrue(exact(terms/K.det(),(T+z*(sp.eye(2)-T)).det()))
    def test_10_exact_return_spectra(self):
        for i,j,values in [(1,3,[R(2,3),R(2,5)]),(2,4,[R(4,5),R(2,5)])]:
            Ki=frame(CHIS[0],i)[2]; Gj=frame(CHIS[0],j)[3]
            self.assertEqual(sorted((Ki*Gj).eigenvals().keys()),sorted(values))
            self.assertTrue(exact((Ki*Gj).det(),sp.prod(values)))
    def test_11_adaptive_rational_upper(self):
        lows=[]; highs=[]
        for i,j in [(1,3),(2,4)]:
            Ki=frame(CHIS[0],i)[2]; Gj=frame(CHIS[0],j)[3]
            T=Ki*Gj; H=sp.eye(2)-T
            actual_low,actual_high=log_interval(1/T.det(),160)
            low,high=adaptive(H,32)
            self.assertLessEqual(low,actual_low)
            self.assertGreaterEqual(high,actual_high)
            self.assertLess(high-low,R(1,10**8))
            lows.append(low); highs.append(high)
        actual_low,actual_high=log_interval(R(375,32),500)
        self.assertLessEqual(sum(lows),actual_low)
        self.assertGreaterEqual(sum(highs),actual_high)
    def test_12_adaptive_failure_is_not_silently_accepted(self):
        H=sp.diag(R(9,10),R(9,10))
        with self.assertRaises(ValueError): adaptive(H,1)
        low,high=adaptive(H,32)
        lo,hi=log_interval(100,1500)
        self.assertLessEqual(low,lo); self.assertGreaterEqual(high,hi)
        self.assertEqual(adaptive(sp.zeros(2),2),(0,0))
    def test_13_source_sharp_certificate(self):
        xsets=[[R(1,3),R(3,5)],[R(1,5),R(3,5)]]
        r=R(3,5); p=2; bound=0
        loglo,loghi=log_interval(R(5,2),200)
        cp=(loghi-sum(r**m/m for m in range(1,p+1)))/r**(p+1)
        for xs in xsets:
            s=lambda m:sum(x**m for x in xs)
            bound+=sum(s(m)/m for m in range(1,p+1))+cp*s(p+1)
        actual_low,actual_high=log_interval(R(375,32),500)
        self.assertGreater(bound,actual_high)
        self.assertLess(bound,R(2469887624578038,10**15))
    def test_14_original_mass_is_retained(self):
        for N in (1,3,4):
            B,O,K,G,Q,A=frame(CHIS[0],N,7)
            B2,O2,K2,G2,Q2,A2=frame(CHIS[0],N,35)
            self.assertTrue(exact(O2,5*O)); self.assertTrue(exact(K2,K/5))
            self.assertTrue(exact(G2,5*G)); self.assertTrue(exact(Q2,Q))
            self.assertEqual(O[0,0],7)
    def test_15_factor_four_block_strengthening(self):
        for q in range(1,8):
            for t in (R(2),R(5)):
                g=[1/t**2]*q
                self.assertEqual(sp.prod(g),t**(-2*q))
                self.assertLessEqual(min(g),1/t**2)
                self.assertEqual(sp.prod(g)**2,t**(-4*q))
    def test_16_audit_fail_closed(self):
        valid='\n'.join("'%s%s' depends on axioms: [propext, Classical.choice, Quot.sound]"%(v,n) for n,v in TARGETS.items())
        self.assertEqual(len(audit(valid)),len(TARGETS))
        for bad in ('',valid+'\n'+valid,valid.replace('Quot.sound','sorryAx'),valid.split('\n',1)[1]):
            with self.assertRaises(ValueError): audit(bad)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--negative',action='store_true')
    parser.add_argument('--audit')
    args=parser.parse_args()
    if args.negative:
        raise SystemExit('intentional restriction-certificate negative control')
    if args.audit:
        print(json.dumps({'status':'PASS','reports':audit(Path(args.audit).read_text())},sort_keys=True))
        return 0
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    names=[t.id().split('.')[-1] for t in suite]
    result=unittest.TestResult(); suite.run(result)
    payload={'status':'PASS' if result.wasSuccessful() else 'FAIL','methods':result.testsRun,
        'tests':names,'failures':[{'test':str(t),'traceback':msg} for t,msg in result.failures],
        'errors':[{'test':str(t),'traceback':msg} for t,msg in result.errors],
        'scope':'exact finite source matrices and rational log enclosures; not arithmetic quadrature'}
    print(json.dumps(payload,indent=2,sort_keys=True))
    return 0 if result.wasSuccessful() else 1

if __name__=='__main__':
    sys.exit(main())
