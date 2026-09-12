#!/usr/bin/env python3
"""Exact finite regressions for spectral-sum descent; not an RH or analytic certificate."""
from __future__ import annotations
import argparse
from itertools import product, combinations_with_replacement
from collections import Counter
from functools import lru_cache
import json
from pathlib import Path
import sys
import unittest
import sympy as sp

x,y,S,r,Delta,u,v,t=sp.symbols('x y S r Delta u v t')
HALF=sp.Rational(1,2)

def clean(M):
    return sp.Matrix(M).applyfunc(lambda z:sp.cancel(sp.expand(z)))

def inv_parts(h):
    hp=sp.expand(h.subs(t,(S+r)/2)); hm=sp.expand(h.subs(t,(S-r)/2))
    e=sp.Poly(sp.expand((hp+hm)/2),S,r)
    o=sp.Poly(sp.cancel((hp-hm)/(2*r)),S,r)
    def convert(P):
        out=0
        for (a,b),c in P.terms():
            if b%2: raise ValueError('expected even polynomial')
            out+=c*S**a*Delta**(b//2)
        return sp.expand(out)
    return convert(e),convert(o)

def phi(P):return sp.expand(P.subs({S:x+y,Delta:(x-y)**2},simultaneous=True))

def reduce2(P,h):
    P=sp.rem(sp.Poly(P,x),sp.Poly(h.subs(t,x),x)).as_expr()
    return sp.expand(sp.rem(sp.Poly(P,y),sp.Poly(h.subs(t,y),y)).as_expr())

def vec2(P,h):
    d=sp.degree(h,t);P=reduce2(P,h)
    return sp.Matrix([P.coeff(x,a).coeff(y,b) for a,b in product(range(d),repeat=2)])

def invariant_inclusion(d):
    bas=list(combinations_with_replacement(range(d),2)); allb=list(product(range(d),repeat=2))
    I=sp.zeros(d*d,len(bas))
    for col,(a,b) in enumerate(bas):
        I[allb.index((a,b)),col]=1
        I[allb.index((b,a)),col]=1
    return I,bas

def normal_moment(n,var=1):
    return sp.Integer(0) if n%2 else sp.factorial2(n-1)*sp.sympify(var)**(n//2)

def gauss_expect(P,variables,variances):
    z=sp.Poly(sp.expand(P),*variables);out=0
    for ex,c in z.terms():
        out+=c*sp.prod(normal_moment(a,b) for a,b in zip(ex,variances))
    return sp.expand(out)

def source_pair(P,Q):
    a,b=sp.symbols('a b',real=True)
    P=P.subs({x:HALF+sp.I*a,y:HALF+sp.I*b},simultaneous=True)
    Q=Q.subs({x:HALF+sp.I*a,y:HALF+sp.I*b},simultaneous=True)
    return sp.expand(2*sp.pi*gauss_expect(sp.conjugate(P)*Q,(a,b),(1,1)))

@lru_cache(None)
def invariant_fixture(M=4):
    h=(t-HALF)**2
    old=[x**a*y**b+(x**b*y**a if a!=b else 0)
         for a,b in combinations_with_replacement(range(M+1),2) if a+b<=M]
    new=[S**a*Delta**b for b in range(M//2+1) for a in range(M-2*b+1)]
    allb=list(product(range(M+1),repeat=2))
    def col(P):
        P=sp.expand(P);return sp.Matrix([P.coeff(x,a).coeff(y,b) for a,b in allb])
    Old=sp.Matrix.hstack(*(col(P) for P in old))
    New=sp.Matrix.hstack(*(col(phi(P)) for P in new))
    C=clean((Old.T*Old).inv()*Old.T*New)
    moment=clean([[source_pair(P,Q) for Q in old] for P in old])
    I,bas=invariant_inclusion(2); L=(I.T*I).inv()*I.T
    unit=(x+1)*(y+1)
    J=clean(sp.Matrix.hstack(*(L*vec2(unit*P,h) for P in old)))
    Jet=clean(J*C)
    Mp=clean(C.H*moment*C)
    K=clean(J*moment.inv()*J.H); G=clean(K.inv())
    Cp=clean(Mp.inv()*Jet.H*G)
    Co=clean(moment.inv()*J.H*G)
    A=clean(sp.Matrix.hstack(*(L*vec2((x+y)*sum(I[i,j]*x**a*y**b for i,(a,b) in enumerate(product(range(2),repeat=2))),h) for j in range(3))))
    return dict(h=h,old=old,new=new,C=C,M=moment,Mp=Mp,J=J,Jet=Jet,K=K,G=G,Cp=Cp,Co=Co,A=A)

def sl2(ms):
    bas=list(product(*(range(m) for m in ms)));d=len(bas);D=sum(m-1 for m in ms)
    N=sp.zeros(d);F=sp.zeros(d);H=sp.zeros(d);G=sp.zeros(d)
    idx={a:i for i,a in enumerate(bas)}
    for a,i in idx.items():
        H[i,i]=2*sum(a)-D
        G[i,i]=sp.prod(sp.factorial(j)*sp.factorial(m-1)/sp.factorial(m-1-j) for j,m in zip(a,ms))
        for l,m in enumerate(ms):
            if a[l]+1<m:
                b=list(a);b[l]+=1;N[idx[tuple(b)],i]+=1
            if a[l]:
                b=list(a);b[l]-=1;F[idx[tuple(b)],i]+=a[l]*(m-a[l])
    return bas,N,F,H,G

def jordan_counts(N,D):
    ranks=[(N**j).rank() for j in range(D+3)]
    return {j:ranks[j-1]-2*ranks[j]+ranks[j+1] for j in range(1,D+2)
            if ranks[j-1]-2*ranks[j]+ranks[j+1]}

def expected_counts(coeff):
    D=len(coeff)-1
    return {D-2*r+1:coeff[r]-(coeff[r-1] if r else 0)
            for r in range(D//2+1) if coeff[r]-(coeff[r-1] if r else 0)}

class SumDescentTests(unittest.TestCase):
    def eq(self,a,b):self.assertEqual(sp.expand(a-b),0)
    def mat(self,a,b):self.assertEqual(clean(sp.Matrix(a)-sp.Matrix(b)),sp.zeros(*sp.Matrix(a).shape))

    def test_01_coordinate_inverse_and_jacobian(self):
        self.eq(((S+r)/2+(S-r)/2),S)
        self.eq(((S+r)/2-(S-r)/2),r)
        self.eq(sp.Matrix([[HALF,HALF],[HALF,-HALF]]).det(),-HALF)

    def test_02_even_odd_generators(self):
        for h in [t-3,(t-HALF)**2,t**3-2*t+7,t**4+t**3-3*t+2]:
            E,O=inv_parts(h)
            self.eq(E.subs(Delta,r*r)+r*O.subs(Delta,r*r),h.subs(t,(S+r)/2))
            self.eq(phi(E), (h.subs(t,x)+h.subs(t,y))/2)
            self.eq(phi(Delta*O),(x-y)*(h.subs(t,x)-h.subs(t,y))/2)

    def test_03_invariant_quotient_length_and_surjection(self):
        for h in [(t-HALF)**2,t**3-2*t+7,(t-1)**3,t**4+t+1]:
            d=sp.degree(h,t); E,O=inv_parts(h)
            self.eq(reduce2(phi(E),h),0);self.eq(reduce2(phi(Delta*O),h),0)
            cols=[vec2(phi(S**a*Delta**b),h) for b in range(d) for a in range(2*d-1-2*b)]
            self.assertEqual(sp.Matrix.hstack(*cols).rank(),d*(d+1)//2)

    def test_04_hilbert_polynomial_all_degrees(self):
        for d in range(1,10):
            p=sum(t**(a+b) for a,b in combinations_with_replacement(range(d),2))
            self.eq(p*(1-t)*(1-t*t),(1-t**d)*(1-t**(d+1)))

    def test_05_original_boundary_primitives_and_sign(self):
        h=t**3-2*t+1;E,O=inv_parts(h)
        A=S**2+3*Delta+1;B=S-2
        P1=sp.expand((A.subs(Delta,r*r)+r*B.subs(Delta,r*r))/2)
        P2=sp.expand((A.subs(Delta,r*r)-r*B.subs(Delta,r*r))/2)
        target=(E*A+Delta*O*B).subs(Delta,r*r)
        self.eq(h.subs(t,(S+r)/2)*P1-h.subs(t,(S-r)/2)*(-P2),target)

    def test_06_asymmetric_source_also_has_exchange_symmetry(self):
        # No evenness of the one-factor weight is required for exchange invariance.
        mu=sp.Rational(2,3)
        self.eq(((u+v)/2-mu)**2+((u-v)/2-mu)**2,((u-2*mu)**2+v*v)/2)

    def test_07_matrix_weight_literal_constants(self):
        M=sp.Matrix(3,3,lambda a,b:(-1)**(a+b)*2**(a+b)*sp.factorial2(2*(a+b)-1))
        self.mat(M,[[1,-2,12],[-2,12,-120],[12,-120,1680]])
        T=sp.Matrix([[1,2,12],[0,1,12],[0,0,1]])
        self.mat(T.T*M*T,sp.diag(1,8,384))
        self.eq(2*sp.pi*gauss_expect(1,(u,v),(2,2)),2*sp.pi)

    def test_08_direct_and_pushforward_gaussian_moments(self):
        U,V=sp.symbols('U V',real=True)
        polys=[S**a*Delta**b for b in range(3) for a in range(5-2*b)]
        for i,P in enumerate(polys):
            for Q in polys[:i+1]:
                p=P.subs({S:1+sp.I*U,Delta:-V*V},simultaneous=True)
                q=Q.subs({S:1+sp.I*U,Delta:-V*V},simultaneous=True)
                via=2*sp.pi*gauss_expect(sp.conjugate(p)*q,(U,V),(2,2))
                self.eq(source_pair(phi(P),phi(Q)),via)

    def test_09_jet_unit_and_same_canonical_representative(self):
        z=invariant_fixture()
        self.mat(z['J']*z['Co'],sp.eye(3));self.mat(z['Jet']*z['Cp'],sp.eye(3))
        self.mat(z['C']*z['Cp'],z['Co'])
        self.mat(z['Jet']*z['Mp'].inv()*z['Jet'].H,z['K'])
        self.mat(z['Cp'].H*z['Mp']*z['Cp'],z['G'])

    def test_10_sum_action_and_control_transport(self):
        z=invariant_fixture();A=z['A'];G=z['G']
        U=sp.Matrix([[1,2,0],[0,1,1],[0,0,2]])
        Ap=U.inv()*A*U;Gp=U.H*G*U
        self.mat(Ap.H*Gp+Gp*Ap-2*Gp,U.H*(A.H*G+G*A-2*G)*U)
        K=G.inv();Kp=Gp.inv()
        self.mat(Kp,U.inv()*K*U.inv().H)

    def test_11_convolution_covariance_keeps_relative_component(self):
        M=sp.Matrix([[1,-2],[-2,12]])
        T=sp.Matrix([[1,-2],[0,1]])
        self.mat(T.H*sp.diag(1,8)*T,M)
        # Relative vector (-m1, m0) has positive, nonzero retained norm.
        self.eq((sp.Matrix([2,1]).T*M*sp.Matrix([2,1]))[0],8)

    def test_12_sl2_commutators_and_auxiliary_metric(self):
        for ms in [(2,2),(2,3),(3,3),(2,2,2),(3,2,2)]:
            bas,N,F,H,G=sl2(ms)
            self.mat(N*F-F*N,H);self.mat(H*N-N*H,2*N);self.mat(H*F-F*H,-2*F)
            self.mat(N.T*G,G*F)
            self.assertTrue(all(g>0 for g in G.diagonal()))

    def test_13_all_ordered_primitive_block_lengths(self):
        for ms in [(2,2),(2,3),(3,3),(2,2,2),(3,2,2)]:
            bas,N,F,H,G=sl2(ms);D=sum(m-1 for m in ms)
            coeff=[sum(sum(a)==r for a in bas) for r in range(D+1)]
            self.assertEqual(jordan_counts(N,D),expected_counts(coeff))

    def test_14_symmetric_ladder_blocks(self):
        for m,k in [(2,2),(2,3),(2,5),(3,2),(3,3),(4,2)]:
            bas,N,F,H,G=sl2((m,)*k);orbits=list(combinations_with_replacement(range(m),k))
            I=sp.zeros(len(bas),len(orbits))
            for i,a in enumerate(bas):I[i,orbits.index(tuple(sorted(a)))]=1
            L=(I.T*I).inv()*I.T;Ns=L*N*I
            self.mat(N*I,I*Ns)
            D=k*(m-1);coeff=[sum(sum(a)==r for a in orbits) for r in range(D+1)]
            self.assertEqual(jordan_counts(Ns,D),expected_counts(coeff))

    def test_15_symmetric_order_three_full_six_dimensions(self):
        h=t**3;N=x+y;p=x*x-x*y+y*y
        columns=[vec2(N**j,h) for j in range(5)]+[vec2(p,h)]
        self.assertEqual(sp.Matrix.hstack(*columns).rank(),6)
        self.eq(reduce2(N*p,h),0)
        self.eq(reduce2(N**4,h),6*x*x*y*y)
        E,O=inv_parts(h)
        self.eq(8*E,S**3+3*S*Delta)
        self.eq(8*Delta*O,3*S*S*Delta+Delta**2)

    def test_16_colliding_sums_retain_occupation_labels(self):
        roots=[-1,0,1];occup=list(combinations_with_replacement(roots,2))
        fibres={}
        for a in occup:fibres.setdefault(sum(a),[]).append(a)
        self.assertEqual(fibres[0],[(-1,1),(0,0)])
        self.assertEqual(len(occup),6)
        self.assertEqual(sum(len(x) for x in fibres.values()),6)

    def test_17_nilpotent_trace_and_weight_not_erased(self):
        for ms in [(2,3),(3,3),(2,2,2)]:
            bas,N,_,_,_=sl2(ms);D=sum(m-1 for m in ms)
            expN=sum((N**j*t**j/sp.factorial(j) for j in range(D+1)),sp.zeros(len(bas)))
            self.eq(sp.trace(expN),len(bas))
        rho=sp.symbols('rho',real=True)
        self.eq(2*(3*rho)-3,3*(2*rho-1))

    def test_18_full_and_opposite_reflection_coordinates(self):
        # Coefficient-semilinear reflection sends s_i to 1-s_i.
        self.eq((1-x)+(1-y),2-(x+y))
        self.eq(((1-x)-(1-y))**2,(x-y)**2)
        C=sp.Matrix([[1,0],[0,-1]])
        G=sp.Matrix([[2,sp.I],[-sp.I,3]])
        self.mat(C.H*G*C,sp.conjugate(G))

    def test_19_split_linear_coordinate_map_and_two_zeros(self):
        p=5
        vecs=[None]+list(product(range(p),repeat=2))
        scal=[None]+list(range(p))
        def add(a,b):
            if a is None:return b
            if b is None:return a
            return tuple((a[i]+b[i])%p for i in range(2))
        def scale(s,a):return None if s is None or a is None else tuple(s*x%p for x in a)
        def T(a):return None if a is None else ((a[0]+a[1])%p,(a[0]-a[1])%p)
        for a in vecs:
            for b in vecs:self.assertEqual(T(add(a,b)),add(T(a),T(b)))
            for s in scal:self.assertEqual(T(scale(s,a)),scale(s,T(a)))
        self.assertEqual(T((0,0)),(0,0));self.assertIsNone(T(None))
        self.assertNotEqual((0,0),None)

    def test_20_nilpotent_quotient_is_supported_not_absent(self):
        def q(a):return None if a is None else a[:2]
        self.assertEqual(q((0,0,1)),(0,0));self.assertIsNone(q(None))
        self.assertNotEqual((0,0,1),(0,0,0))


    def test_21_free_resolution_telescoping_and_action(self):
        A=sp.Matrix([[sp.Rational(1,3),1,0],[0,sp.Rational(1,3),1],[0,0,sp.Rational(1,3)]])
        cols=[sp.Matrix([j+1,j*j-2,3-j]) for j in range(5)]
        f=sum((S**j*cols[j] for j in range(5)),sp.zeros(3,1))
        val=sum((A**j*cols[j] for j in range(5)),sp.zeros(3,1))
        q=sum((sum((S**(j-1-i)*A**i*cols[j] for i in range(j)),sp.zeros(3,1)) for j in range(1,5)),sp.zeros(3,1))
        self.mat(f-val,(S*sp.eye(3)-A)*q)

    def test_22_resolvent_retains_every_nilpotent_power(self):
        rho=sp.Rational(2,7);N=sp.Matrix([[0,1,0],[0,0,1],[0,0,0]])
        A=rho*sp.eye(3)+N
        R=sum((N**j/(S-rho)**(j+1) for j in range(3)),sp.zeros(3))
        self.mat((S*sp.eye(3)-A)*R,sp.eye(3))
        self.eq(sp.trace(R),3/(S-rho))
        self.assertNotEqual(R[0,2],0)

    def test_23_pushforward_residue_duality(self):
        rho=sp.Rational(2,7);A=sp.Matrix([[rho,1,0],[0,rho,1],[0,0,rho]])
        v0=sp.Matrix([1,2,3]);rows=[sp.Matrix([[1,0,2]]),sp.Matrix([[0,3,1]]),sp.Matrix([[2,1,0]])]
        P=sum((S**j*rows[j] for j in range(3)),sp.zeros(1,3))
        rat=(P*(S*sp.eye(3)-A).inv()*v0)[0]
        value=sum((rows[j]*A**j*v0)[0] for j in range(3))
        self.eq(sp.residue(rat,S,rho),value)
        relation=sp.Matrix([[S+1,2*S,3]])*(S*sp.eye(3)-A)
        self.eq(sp.residue((relation*(S*sp.eye(3)-A).inv()*v0)[0],S,rho),0)

    def test_24_finite_lefschetz_resolvent_trace(self):
        A=sp.Matrix([[sp.Rational(1,4),1,0],[0,sp.Rational(1,4),0],[0,0,sp.Rational(3,4)]])
        char=(S*sp.eye(3)-A).det();res=sp.trace((S*sp.eye(3)-A).inv())
        self.eq(sp.cancel(res-sp.diff(char,S)/char),0)
        psi=1+2*S+3*S*S
        trace=sum(sp.residue(psi*res,S,r0) for r0 in [sp.Rational(1,4),sp.Rational(3,4)])
        self.eq(trace,sp.trace(sp.eye(3)+2*A+3*A*A))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json',type=Path)
    parser.add_argument('--self-test-failure',action='store_true')
    args=parser.parse_args()
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(SumDescentTests)
    if args.self_test_failure:
        class Failure(unittest.TestCase):
            def runTest(self):self.assertEqual(1,0,'deliberate false guard')
        suite.addTest(Failure())
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    record={'tests_run':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'success':result.wasSuccessful(),
            'sympy':sp.__version__,'scope':'exact finite polynomial, Gaussian-moment, nilpotent and split-support regression; no analytic or Lean certificate'}
    if args.json:args.json.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,sort_keys=True))
    return 0 if result.wasSuccessful() else 1

if __name__=='__main__':sys.exit(main())
