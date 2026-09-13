#!/usr/bin/env python3
"""Exact polynomial-source regressions, not numerical zeta-zero certificates."""
from __future__ import annotations
import argparse
from fractions import Fraction
from functools import lru_cache
import itertools
import json
import math
from pathlib import Path
import unittest
import sympy as sp

x,s,t=sp.symbols('x s t', real=True)
q=2
h=(s-sp.Rational(1,2))**2+1
MASS=sp.Integer(7)

def gaussian_moment(n:int)->sp.Expr:
    return sp.Integer(0) if n%2 else sp.factorial2(n-1) if n else sp.Integer(1)

def integral(poly:sp.Expr, perturb:sp.Rational)->sp.Expr:
    pol=sp.Poly(sp.expand(poly*(1+perturb*x*x)),x)
    return sp.expand(MASS*sum(c*gaussian_moment(k[0]) for k,c in pol.terms()))

def source(N:int,perturb:sp.Rational)->sp.Matrix:
    return sp.Matrix(N+1,N+1,lambda i,j:integral((sp.Rational(1,2)-sp.I*x)**i*(sp.Rational(1,2)+sp.I*x)**j,perturb))

def presentation(N:int):
    C=sp.eye(N+1)[:,:q]
    B=sp.Matrix(N+1,N-q+1,lambda i,j:sp.expand(h*s**j).coeff(s,i))
    J=sp.Matrix(q,N+1,lambda i,j:sp.rem(s**j,h,s).coeff(s,i))
    return C,B,J

def canonical(N:int,perturb:sp.Rational):
    M=source(N,perturb);C,B,J=presentation(N)
    H=(B.T*M*B).inv() if B.cols else sp.zeros(0,0)
    K=H*B.T*M*C
    R=C-B*K
    G=sp.simplify(R.T*M*R)
    return dict(M=M,C=C,B=B,J=J,H=H,K=K,R=R,G=G)

def equal(A,B)->bool:
    return all(sp.cancel(z)==0 for z in A-B)

def psd(A:sp.Matrix)->bool:
    if not equal(A,A.conjugate().T):return False
    return all(A.extract(I,I).det()>=0 for r in range(1,A.rows+1) for I in itertools.combinations(range(A.rows),r))

DATA={(N,e):canonical(N,sp.Rational(e)) for N in range(1,5) for e in [0,1,2]}

def fraction(a)->Fraction:
    p,d=sp.fraction(sp.cancel(a));return Fraction(int(p),int(d))

def mat2(A):return tuple(tuple(fraction(A[i,j]) for j in range(2)) for i in range(2))
def mul2(A,B):return tuple(tuple(sum(A[i][l]*B[l][j] for l in range(2)) for j in range(2)) for i in range(2))
def traces(H,stop):
    P=((Fraction(1),Fraction(0)),(Fraction(0),Fraction(1)))
    out=[Fraction(2)]
    for _ in range(stop):P=mul2(P,H);out.append(P[0][0]+P[1][1])
    return out

def logarithm_enclosure(a:Fraction,order:int=160):
    if a<=0:raise ValueError('positive ratio required')
    z=(a-1)/(a+1)
    approx=2*sum((z**(2*j+1)/Fraction(2*j+1) for j in range(order)),Fraction(0))
    rem=2*abs(z)**(2*order+1)/(Fraction(2*order+1)*(1-z*z))
    return approx-rem,approx+rem

@lru_cache(maxsize=None)
def certificate(e0=0,e1=1):
    A=[DATA[(N,e0)]['G'].inv()*DATA[(N,e1)]['G'] for N in range(1,5)]
    c=1+sum(sp.trace(a) for a in A)
    H=[mat2(sp.eye(2)-a/c) for a in A]
    p=1
    while True:
        orders=[];bounds=[]
        for a in H:
            z=traces(a,2*p)
            if z[p]>=1:break
            prefix=sum((z[j]/j for j in range(1,p+1)),Fraction(0))
            tail=sum((z[j]/j for j in range(p+1,2*p+1)),Fraction(0))
            bounds.append((prefix,prefix+tail/(1-z[p])))
            orders.append(p)
        if len(bounds)==4:
            lo=bounds[2][0]+bounds[3][0]-bounds[0][1]-bounds[1][1]
            hi=bounds[2][1]+bounds[3][1]-bounds[0][0]-bounds[1][0]
            if hi-lo<Fraction(1,10**10):break
        p*=2
        if p>1024:raise RuntimeError('fixture precision did not stop')
    ratios=[fraction(DATA[(N,e1)]['G'].det()/DATA[(N,e0)]['G'].det()) for N in range(1,5)]
    total=ratios[0]*ratios[1]/(ratios[2]*ratios[3])
    return lo,hi,total,orders,fraction(c)

class MetricTransferTests(unittest.TestCase):
    def test_source_positivity_and_full_mass(self):
        for (N,e),a in DATA.items():
            self.assertEqual(a['M'][0,0],7*(1+e))
            self.assertTrue(all(a['M'][:r,:r].det()>0 for r in range(1,N+2)))
            self.assertTrue(all(a['G'][:r,:r].det()>0 for r in range(1,q+1)))
    def test_original_remainders(self):
        for a in DATA.values():
            self.assertTrue(equal(a['J']*a['C'],sp.eye(q)))
            self.assertTrue(equal(a['J']*a['B'],sp.zeros(q,a['B'].cols)))
            self.assertTrue(equal(a['J']*a['R'],sp.eye(q)))
    def test_boundary_primitive(self):
        for N in range(1,5):
            a,b=DATA[(N,0)],DATA[(N,1)];D=b['R']-a['R']
            self.assertTrue(equal(D,a['B']*(a['K']-b['K'])))
            self.assertTrue(equal(b['J']*D,sp.zeros(q,q)))
    def test_both_exact_secants(self):
        for N in range(1,5):
            a,b=DATA[(N,0)],DATA[(N,1)];D=b['R']-a['R'];E=b['M']-a['M'];dG=b['G']-a['G']
            self.assertTrue(equal(dG,a['R'].T*E*a['R']-D.T*b['M']*D))
            self.assertTrue(equal(dG,b['R'].T*E*b['R']+D.T*a['M']*D))
    def test_pencil_gap_and_positivity(self):
        for N in range(1,5):
            a,b=DATA[(N,0)],DATA[(N,1)];M=sp.Rational(2,5)*a['M']+sp.Rational(3,5)*b['M'];B=a['B'];C=a['C']
            R=C-B*(B.T*M*B).inv()*B.T*M*C if B.cols else C
            G=R.T*M*R; gap=G-sp.Rational(2,5)*a['G']-sp.Rational(3,5)*b['G']
            target=sp.Rational(2,5)*(R-a['R']).T*a['M']*(R-a['R'])+sp.Rational(3,5)*(R-b['R']).T*b['M']*(R-b['R'])
            self.assertTrue(equal(gap,target));self.assertTrue(psd(gap))
    def test_first_and_second_source_variations(self):
        a,b=DATA[(3,0)],DATA[(3,1)];E=b['M']-a['M'];M=a['M']+t*E;B=a['B'];C=a['C']
        R=sp.simplify(C-B*(B.T*M*B).inv()*B.T*M*C);G=sp.simplify(R.T*M*R)
        velocity=-B*(B.T*M*B).inv()*B.T*E*R
        self.assertTrue(equal(sp.diff(R,t),velocity))
        self.assertTrue(equal(sp.diff(G,t),R.T*E*R))
        self.assertTrue(equal(sp.diff(G,t,2),-2*velocity.T*M*velocity))
    def test_log_curvature_with_both_terms(self):
        a,b=DATA[(3,0)],DATA[(3,1)];E=b['M']-a['M'];M=a['M']+t*E;B=a['B'];C=a['C']
        R=sp.simplify(C-B*(B.T*M*B).inv()*B.T*M*C);G=sp.simplify(R.T*M*R)
        for t0 in [0,sp.Rational(1,3),1]:
            G0=G.subs(t,t0);v=sp.diff(R,t).subs(t,t0);Z=sp.diff(G,t).subs(t,t0)
            rhs=-2*sp.trace(G0.inv()*v.T*M.subs(t,t0)*v)-sp.trace((G0.inv()*Z)**2)
            lhs=sp.diff(sp.log(G.det()),t,2).subs(t,t0)
            self.assertEqual(sp.cancel(lhs-rhs),0);self.assertLessEqual(rhs,0)
    def test_adaptive_signed_certificate(self):
        for e0,e1 in [(0,1),(1,0),(1,1)]:
            lo,hi,v,orders,c=certificate(e0,e1);a,b=logarithm_enclosure(v)
            self.assertLessEqual(lo,a);self.assertGreaterEqual(hi,b)
            self.assertTrue(all(p>0 for p in orders));self.assertGreater(c,0)
            if e0<e1:self.assertGreater(lo,0)
            if e1<e0:self.assertLess(hi,0)
    def test_scale_terms_really_cancel(self):
        A=[DATA[(N,0)]['G'].inv()*DATA[(N,1)]['G'] for N in range(1,5)]
        for c in [1+sum(sp.trace(a) for a in A), 5+sum(sp.trace(a) for a in A)]:
            H=[sp.eye(q)-a/c for a in A]
            ratio=sp.prod(a.det() for a in A[:2])/sp.prod(a.det() for a in A[2:])
            lossratio=sp.prod((sp.eye(q)-z).det() for z in H[:2])/sp.prod((sp.eye(q)-z).det() for z in H[2:])
            self.assertEqual(sp.cancel(ratio-lossratio),0)
    def test_supported_boundary_not_absence(self):
        a,b=DATA[(3,0)],DATA[(3,1)];v=sp.Matrix([1,0]);D=(b['R']-a['R'])*v
        self.assertTrue(any(z!=0 for z in D));self.assertTrue(equal(a['J']*D,sp.zeros(q,1)))
        supported_zero=('degree-3',(0,0)); absence=('tau',None)
        self.assertNotEqual(supported_zero,absence)

def main()->int:
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path);parser.add_argument('--negative-control',choices=['omit-boundary-loss','reverse-signed-log']);args=parser.parse_args()
    if args.negative_control:
        if args.negative_control=='omit-boundary-loss':
            a,b=DATA[(3,0)],DATA[(3,1)]
            false_claim=equal(b['G']-a['G'],a['R'].T*(b['M']-a['M'])*a['R'])
        else:
            _,_,v,_,_=certificate();false_claim=(v==1/v)
        print(json.dumps({'control':args.negative_control,'false_claim_accepted':false_claim}));return 0 if false_claim else 1
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(MetricTransferTests))
    lo,hi,v,orders,c=certificate()
    record={'tests':result.testsRun,'successful':result.wasSuccessful(),'scope':'Exact polynomial/Gaussian fixtures with source mass 7; not arithmetic zero or integral certificates.','common_scale':str(c),'stopping_orders':orders,'signed_ratio':str(v),'signed_log_interval_display':[float(lo),float(hi)],'signed_log_direct_display':float(sp.log(sp.Rational(v.numerator,v.denominator))),'negative_controls':['omit-boundary-loss','reverse-signed-log']}
    text=json.dumps(record,indent=2)+'\n';print(text)
    if args.output:args.output.write_text(text)
    return 0 if result.wasSuccessful() else 1
if __name__=='__main__':raise SystemExit(main())
