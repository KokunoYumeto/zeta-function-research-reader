#!/usr/bin/env python3
"""Exact finite regression checks for the tau-source frontier calculation.

The fixtures are declared Gaussian moment models and polynomial quotient algebras.
They are not zeta-zero data. A specified scalar mass is retained, not set to one
inside any theorem. Analytic arithmetic inputs are outside this checker's scope.
"""
from __future__ import annotations
import argparse
import itertools
import json
import math
import sys
import unittest
from functools import lru_cache
from pathlib import Path
import sympy as sp

s = sp.Symbol('s')
I = sp.I

def comp(n: int, k: int):
    if k == 1:
        yield (n,)
    else:
        for a in range(n + 1):
            for b in comp(n-a, k-1):
                yield (a,) + b

def kron(items):
    items = list(items)
    if len(items) == 1:
        return items[0]
    return sp.kronecker_product(*items)

def zero(m):
    return all(sp.simplify(x) == 0 for x in m)

def equal(a, b):
    if not zero(a-b):
        raise AssertionError(f'exact matrix disagreement:\n{sp.simplify(a-b)}')

def polycoords(p, h):
    d = int(sp.degree(h, s))
    r = sp.Poly(sp.rem(p, h, s), s)
    return sp.Matrix([r.nth(i) for i in range(d)])

class Model:
    """Positive Gaussian measure on Re(s)=1/2, with supplied mass and mean."""
    def __init__(self, h, unit=1, mass=sp.Integer(7), mean=sp.Rational(1,3), variance=sp.Rational(2,1)):
        self.h=sp.Poly(h,s).as_expr()
        self.unit=sp.sympify(unit)
        self.mass=sp.sympify(mass)
        self.mean=sp.sympify(mean)
        self.variance=sp.sympify(variance)
        self.d=int(sp.degree(h,s))
        if self.d < 1 or sp.degree(sp.gcd(self.h,self.unit),s)>0:
            raise ValueError('positive quotient degree and invertible unit required')
        self.beta=sp.Rational(1,2)+I*self.mean
        self.A=sp.Matrix.hstack(*(polycoords(s*s**j,self.h) for j in range(self.d)))
    @lru_cache(None)
    def p(self,n):
        if n==0:return sp.Integer(1)
        if n==1:return s-self.beta
        return sp.expand((s-self.beta)*self.p(n-1)+(n-1)*self.variance*self.p(n-2))
    def w(self,n):return self.mass*sp.factorial(n)*self.variance**n
    def a(self,n):return n*self.variance
    @lru_cache(None)
    def z1(self,n):return polycoords(self.unit*self.p(n),self.h)
    def z(self,alpha):return kron(self.z1(j) for j in alpha)
    def weight(self,alpha):return sp.prod(self.w(j) for j in alpha)
    def action(self,k):
        return sum((kron(self.A if j==l else sp.eye(self.d) for j in range(k)) for l in range(k)),sp.zeros(self.d**k))
    @lru_cache(None)
    def kernel(self,k,M):
        return sp.simplify(sum((self.z(a)*self.z(a).H/self.weight(a) for m in range(M+1) for a in comp(m,k)),sp.zeros(self.d**k)))
    def frontier(self,k,M):
        high=list(comp(M+1,k)); F=sp.Matrix.hstack(*(self.z(b) for b in high))
        Ecols=[]
        for b in high:
            u=sp.zeros(self.d**k,1)
            for j in range(k):
                if b[j]:
                    pre=list(b);pre[j]-=1
                    u+=self.a(b[j])*self.z(tuple(pre))
            Ecols.append(u)
        E=sp.Matrix.hstack(*Ecols)
        Om=sp.diag(*(self.weight(b) for b in high))
        return high,F,E,Om
    def symmetric_embedding(self,k):
        tuples=list(itertools.product(range(self.d),repeat=k))
        orbits=sorted(set(tuple(sorted(a)) for a in tuples))
        B=sp.zeros(self.d**k,len(orbits))
        for j,b in enumerate(orbits):
            for i,a in enumerate(tuples):
                if tuple(sorted(a))==b:B[i,j]=1
        return orbits,B
    def symmetric_kernel(self,k,M):
        _,B=self.symmetric_embedding(k);left=(B.T*B).inv()*B.T
        C=sp.zeros(B.cols)
        for deg in range(M+1):
            orbits=sorted(set(tuple(sorted(a)) for a in comp(deg,k)))
            for rep in orbits:
                orbit=set(itertools.permutations(rep)); n=len(orbit)
                zz=sum((left*self.z(a) for a in orbit),sp.zeros(B.cols,1))
                C+=zz*zz.H/(n*self.weight(rep))
        return sp.simplify(C)

class FrontierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        x=s-sp.Rational(1,2)
        cls.repeated=Model(x*x,1+I*x,mean=sp.Rational(1,3))
        cls.off=Model((s-sp.Rational(1,4))*(s-sp.Rational(3,4)),1+s,mean=0,variance=1)
        cls.gauss=Model(x*x,mass=1,mean=0,variance=1)
    def test_recurrence_retains_imaginary_diagonal(self):
        m=self.repeated
        for n in range(1,7):
            self.assertEqual(sp.expand(s*m.p(n)-m.p(n+1)-m.beta*m.p(n)+m.a(n)*m.p(n-1)),0)
        self.assertEqual(sp.re(m.beta),sp.Rational(1,2));self.assertNotEqual(sp.im(m.beta),0)
    def test_full_jets_and_nonconstant_unit(self):
        m=self.repeated
        for n in range(5): equal(polycoords(m.unit*m.p(n),m.h),m.z1(n))
        self.assertNotEqual(m.z1(0)[1],0)
    def test_raw_and_orthogonal_moment_kernel(self):
        m=self.repeated;N=4
        # Column T maps the p_j basis to powers of s. The prescribed actual
        # Gram in power coordinates is T^{-*} diag(w_j) T^{-1}.
        T=sp.Matrix([[sp.Poly(m.p(j),s).nth(i) for j in range(N+1)] for i in range(N+1)])
        Om=sp.diag(*(m.w(j) for j in range(N+1)))
        M=T.inv().H*Om*T.inv()
        J=sp.Matrix.hstack(*(polycoords(m.unit*s**j,m.h) for j in range(N+1)))
        equal(J*M.inv()*J.H,m.kernel(1,N))
    def test_tensor_displacement(self):
        for m,k,M in [(self.repeated,1,3),(self.repeated,2,2),(self.off,2,3),(self.gauss,3,3)]:
            K=m.kernel(k,M);A=m.action(k);_,F,E,Om=m.frontier(k,M)
            equal(A*K+K*A.H-k*K,F*Om.inv()*E.H+E*Om.inv()*F.H)
    def test_exact_kernel_increment(self):
        for k,M in [(1,2),(2,2),(3,3)]:
            m=self.gauss;_,F,E,Om=m.frontier(k,M)
            equal(m.kernel(k,M+1)-m.kernel(k,M),F*Om.inv()*F.H)
    def test_woodbury_with_relation_gram(self):
        m=self.off;k=2;M=2;K=m.kernel(k,M);G=K.inv();_,F,E,Om=m.frontier(k,M)
        H=Om+F.H*G*F
        equal(m.kernel(k,M+1).inv(),G-G*F*H.inv()*F.H*G)
    def test_actual_relation_layer_map(self):
        m=self.gauss;k=2;M=2;low=[a for deg in range(M+1) for a in comp(deg,k)]
        high,F,E,Oh=m.frontier(k,M)
        Z=sp.Matrix.hstack(*(m.z(a) for a in low));Ol=sp.diag(*(m.weight(a) for a in low))
        G=m.kernel(k,M).inv();R=Ol.inv()*Z.H*G
        RR=R.col_join(sp.zeros(len(high),m.d**k))
        Htot=sp.diag(Ol,Oh)
        b=(-R*F).col_join(sp.eye(len(high)))
        J=Z.row_join(F)
        equal(J*b,sp.zeros(J.rows,b.cols))
        equal(b.H*Htot*b,Oh+F.H*G*F)
        equal(b.H*Htot*RR,-F.H*G)
        eta=(Oh+F.H*G*F).inv()
        Y=-b*eta*F.H*G
        C=b*Oh.inv()*E.H*G
        W=m.action(k).H*G+G*m.action(k)-k*G
        equal(-(Y.H*Htot*C+C.H*Htot*Y),W)
        equal(RR-Y,Htot.inv()*J.H*m.kernel(k,M+1).inv())
    def test_relative_inequality_congruence(self):
        m=self.off;k=2;M=3;K=m.kernel(k,M);G=K.inv();A=m.action(k)
        Z=A*K+K*A.H-k*K;W=A.H*G+G*A-k*G
        e=sp.Rational(7,3)
        equal(G*(e*K-Z)*G,e*G-W)
        equal(G*(e*K+Z)*G,e*G+W)
    def test_border_nonzero_spectrum(self):
        m=self.gauss;k=1;M=2;K=m.kernel(k,M);G=K.inv();_,F,E,Om=m.frontier(k,M)
        B=F.row_join(E);J=sp.BlockMatrix([[sp.zeros(F.cols),Om.inv()],[Om.inv(),sp.zeros(F.cols)]]).as_explicit()
        Z=B*J*B.H
        self.assertEqual((G*Z).charpoly().as_expr(),(J*B.H*G*B).charpoly().as_expr())
    def test_lowering_incidence_bound(self):
        k=3;M=3;m=self.gauss;low=list(comp(M,k));high=list(comp(M+1,k))
        L=sp.zeros(len(low),len(high))
        for bidx,b in enumerate(high):
            for j in range(k):
                if b[j]:
                    pre=list(b);pre[j]-=1;L[low.index(tuple(pre)),bidx]+=m.a(b[j])
        Ol=sp.diag(*(m.weight(a) for a in low));Oh=sp.diag(*(m.weight(b) for b in high))
        Q=Ol*L*Oh.inv()*L.T
        equal(Q*sp.ones(len(low),1),k*(M+1)*sp.ones(len(low),1))
    def test_symmetric_metric_compression(self):
        for m,k,M in [(self.repeated,2,3),(self.gauss,3,3)]:
            _,B=m.symmetric_embedding(k);K=m.kernel(k,M);G=K.inv();Ks=m.symmetric_kernel(k,M)
            equal(Ks.inv(),B.T*G*B)
            left=(B.T*B).inv()*B.T
            equal(Ks,left*K*left.T)
    def test_orbit_factors_not_discarded(self):
        _,B=self.gauss.symmetric_embedding(3)
        equal(B.T*B,sp.diag(1,3,3,1))
        self.assertEqual(B.cols,sp.binomial(4,1))
    def test_symmetric_generator(self):
        m=self.gauss;k=2;_,B=m.symmetric_embedding(k)
        C=sp.Matrix([[1,-sp.Rational(1,2)],[0,1]])
        B=kron([C,C])*B;left=(B.T*B).inv()*B.T
        As=left*m.action(k)*B
        equal(m.action(k)*B,B*As)
        equal(As,sp.Matrix([[1,0,0],[1,1,0],[0,2,1]]))
    def test_joint_metric_calibration(self):
        m=self.gauss;_,B=m.symmetric_embedding(2)
        C=sp.Matrix([[1,-sp.Rational(1,2)],[0,1]]);B=kron([C,C])*B
        G=m.kernel(2,4).inv();W=m.action(2).H*G+G*m.action(2)-2*G
        Gs=B.T*G*B;Ws=B.T*W*B
        equal(Gs,sp.diag(sp.Rational(1,3),sp.Rational(2,3),sp.Rational(1,4)))
        equal(Ws,sp.Matrix([[0,sp.Rational(2,3),0],[sp.Rational(2,3),0,sp.Rational(1,2)],[0,sp.Rational(1,2),0]]))
        z=sp.Symbol('z');self.assertEqual(sp.factor((z*Gs-Ws).det()/Gs.det()),z*(2*z*z-7)/2)
    def test_rectangular_comparison(self):
        m=self.gauss;_,B=m.symmetric_embedding(2);G1=m.kernel(1,2).inv();G=kron([G1,G1]);A=m.action(2);W=A.H*G+G*A-2*G
        z=sp.Symbol('z');Gs=B.T*G*B;Ws=B.T*W*B
        self.assertEqual(sp.factor((z*Gs-Ws).det()/Gs.det()),z*(z*z-6))
    def test_mass_retained(self):
        m=Model((s-sp.Rational(1,2))**2,mass=7,mean=0,variance=1)
        equal(m.kernel(2,3),self.gauss.kernel(2,3)/49)
        equal(m.kernel(2,3).inv(),49*self.gauss.kernel(2,3).inv())
    def test_alternating_chain_projector_sign(self):
        # C^0=<v>, C^1=<b,c>, d(v)=b; direct basis enumerated by degree.
        symbols=[(0,0),(1,0),(1,1)];tuples=list(itertools.product(symbols,repeat=2))
        bydeg={j:[a for a in tuples if sum(x[0] for x in a)==j] for j in range(3)}
        differentials={}
        swaps={}
        for deg in range(3):
            B=bydeg[deg];P=sp.zeros(len(B))
            for j,(a,b) in enumerate(B):P[B.index((b,a)),j]=(-1)**(a[0]*b[0])
            swaps[deg]=P
            if deg<2:
                T=bydeg[deg+1];d=sp.zeros(len(T),len(B))
                for j,b in enumerate(B):
                    for pos in range(2):
                        if b[pos][0]==0:
                            out=list(b);out[pos]=(1,0)
                            d[T.index(tuple(out)),j]+=(-1)**sum(t[0] for t in b[:pos])
                differentials[deg]=d
        for deg in range(2):equal(differentials[deg]*swaps[deg],swaps[deg+1]*differentials[deg])
        for deg in range(3):
            p=(sp.eye(swaps[deg].rows)-swaps[deg])/2;equal(p*p,p)
        ordinary= -swaps[2]
        equal((sp.eye(4)-swaps[2])/2,(sp.eye(4)+ordinary)/2)
        # Repeated odd tensor c tensor c survives the sign-isotypic projector.
        v=sp.zeros(4,1);v[-1]=1
        equal((sp.eye(4)-swaps[2])*v/2,v)
    def test_supported_projector_keeps_zero_active(self):
        # A total reconstruction with identity transports; orbit closure on labels.
        # The amplitude projection is (a,b)->((a+b)/2,(a+b)/2).
        def p(mask,v):
            if not mask:return (frozenset(),(0,0))
            a,b=v;t=sp.Rational(1,2)*(a+b)
            return (frozenset({0,1}),(t,t))
        for mask in [frozenset(),frozenset({0}),frozenset({1}),frozenset({0,1})]:
            for a,b in itertools.product(range(-1,2),repeat=2):
                out=p(mask,(a,b));self.assertEqual(p(*out),out)
        self.assertEqual(p(frozenset({0}),(1,-1)),(frozenset({0,1}),(0,0)))
    def test_full_trace_retained_by_complement(self):
        m=self.gauss;k=3;_,B=m.symmetric_embedding(k);proj=B*(B.T*B).inv()*B.T
        U=sp.Matrix([[2,1],[0,3]]);Uk=kron([U]*k)
        actual=sp.trace(proj*Uk);pred=2**3+2**2*3+2*3**2+3**3
        self.assertEqual(actual,pred)
        self.assertEqual(sp.trace(proj*Uk)+sp.trace((sp.eye(8)-proj)*Uk),sp.trace(Uk))
    def test_actual_coarse_bound_fixture(self):
        m=self.gauss;k=2;M=2;K=m.kernel(k,M);G=K.inv();A=m.action(k)
        _,F,E,Om=m.frontier(k,M);Delta=F*Om.inv()*F.H
        self.assertEqual(set((G*Delta).eigenvals()),{sp.Integer(0),sp.Integer(2)})
        Z=A*K+K*A.H-k*K
        # Gamma=6 and lambda=2 give 4 sqrt(3)<7. Check the rational certificate.
        for sign in [-1,1]:
            H=7*K+sign*Z
            for n in range(1,H.rows+1):
                for ids in itertools.combinations(range(H.rows),n):
                    self.assertGreaterEqual(H.extract(ids,ids).det(),0)
    def test_symmetric_eigenline_survives(self):
        m=self.off
        v=(m.A-sp.Rational(1,4)*sp.eye(2)).nullspace()[0]
        for k in range(1,4):
            vv=kron([v]*k);_,B=m.symmetric_embedding(k);P=B*(B.T*B).inv()*B.T
            equal(P*vv,vv)
            K=m.kernel(k,k);G=K.inv();A=m.action(k);W=A.H*G+G*A-k*G
            self.assertEqual(sp.simplify((vv.H*W*vv)[0]/(vv.H*G*vv)[0]),-sp.Rational(k,2))
    def test_partition_shell_dimensions(self):
        for k in range(1,5):
            for M in range(6):
                shell=set(tuple(sorted(a)) for a in comp(M+1,k))
                low=set(tuple(sorted(a)) for r in range(M+1) for a in comp(r,k))
                high=set(tuple(sorted(a)) for r in range(M+2) for a in comp(r,k))
                self.assertEqual(len(high)-len(low),len(shell))


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--json',type=Path);parser.add_argument('--negative-control',action='store_true')
    args=parser.parse_args()
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(FrontierTests)
    if args.negative_control:
        def fail(): raise AssertionError('intentional false control')
        suite.addTest(unittest.FunctionTestCase(fail))
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    rec={'tests_run':result.testsRun,'successful':result.wasSuccessful(),'failures':len(result.failures),'errors':len(result.errors),'fixture_scope':'exact finite Gaussian moment calibrations; not arithmetic certificates','sympy':sp.__version__}
    if args.json:args.json.write_text(json.dumps(rec,indent=2)+'\n')
    return 0 if result.wasSuccessful() else 1
if __name__=='__main__':sys.exit(main())
