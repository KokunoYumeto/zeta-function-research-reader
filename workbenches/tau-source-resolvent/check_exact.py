#!/usr/bin/env python3
"""Exact finite calibrations. No arithmetic zero locations or moments are assumed."""
from __future__ import annotations
from fractions import Fraction as F
import argparse
import json
import sys
import unittest
import sympy as s

X=s.Symbol('x', real=True)
S=s.Symbol('S')
HALF=s.Rational(1,2)

def need(ok, label):
    if not bool(ok):
        raise AssertionError(label)

def clean(M):
    return M.applyfunc(s.cancel)

def equal(A,B):
    return clean(A-B)==s.zeros(A.rows,A.cols)

def moment(n):
    return 0 if n%2 else 7*s.factorial2(n-1) if n else s.Integer(7)

def integrate(p):
    return s.expand(sum(c*moment(a[0]) for a,c in s.Poly(s.expand(p),X).terms()))

def gram(N, weight):
    z=HALF+s.I*X
    return s.Matrix(N+1,N+1,lambda a,b:integrate(s.conjugate(z)**a*z**b*weight))

def presentation(N, chi):
    q=s.degree(chi,S)
    C=s.zeros(N+1,q)
    for i in range(q): C[i,i]=1
    B=s.zeros(N+1,N+1-q)
    for j in range(N+1-q):
        p=s.Poly(s.expand(chi*S**j),S)
        for i in range(N+1): B[i,j]=p.nth(i)
    return B,C

def canonical(M,B,C):
    H=(B.H*M*B).inv() if B.cols else s.zeros(0,0)
    Z=clean(H*B.H*M*C)
    R=clean(C-B*Z)
    return H,Z,R,clean(R.H*M*R)

def data(N=3, chi=(S-HALF)**2+1):
    B,C=presentation(N,s.expand(chi))
    M0=gram(N,1)
    M1=gram(N,1+X**2)
    M2=gram(N,1+2*X**2+X**4)
    return B,C,[M0,M1,M2],[canonical(M,B,C) for M in [M0,M1,M2]]

def frac(x):
    x=s.Rational(x)
    return F(int(x.p),int(x.q))

def log_bounds(x: F, N=100):
    if x<=0: raise ValueError('positive argument required')
    power=0
    while x>2: x/=2;power+=1
    while x<1: x*=2;power-=1
    def local(z):
        y=(z-1)/(z+1)
        val=2*sum((y**(2*j+1)/F(2*j+1) for j in range(N)),F(0))
        tail=2*abs(y)**(2*N+1)/(F(2*N+1)*(1-y*y))
        return val-tail,val+tail
    a,b=local(x);c,d=local(F(2))
    return (a+power*c,b+power*d) if power>=0 else (a+power*d,b+power*c)

def enclose_moments(mom,p,err=F(1,10**18)):
    # A deliberately non-exact midpoint; interval proofs must absorb its error.
    lo={n:mom[n]-err for n in range(1,2*p+1)}
    hi={n:mom[n]+2*err for n in range(1,2*p+1)}
    if hi[p]>=1: raise ValueError('uncertified stopping denominator')
    lower=sum((lo[n]/n for n in range(1,p+1)),F(0))
    prefix=sum((hi[n]/n for n in range(1,p+1)),F(0))
    tail=sum((hi[n]/n for n in range(p+1,2*p+1)),F(0))
    return lower,prefix+tail/(1-hi[p])

def matrix_interval(H):
    # Computing the certificate uses exact matrix powers, not eigenvectors.
    p=1
    while frac(s.trace(H**p))>=F(1,2):
        p*=2
        if p>1024: raise RuntimeError('fixture stopping limit')
    T=s.eye(H.rows);mom={}
    for n in range(1,2*p+1):
        T=clean(T*H)
        mom[n]=frac(s.re(s.trace(T)))
    return enclose_moments(mom,p),p

class Tests(unittest.TestCase):
    def test_source_resolvent(self):
        for N in [1,2,3,4]:
            B,C,Ms,ds=data(N)
            H0,Z0,R0,G0=ds[0];H1,Z1,R1,G1=ds[1]
            cross=clean(B.H*(Ms[1]-Ms[0])*R0)
            U=clean(H1*cross)
            need(equal(U,Z1-Z0),'primitive')
            need(equal(R1,R0-B*U),'section resolvent')
            need(equal(G1,G0+R0.H*(Ms[1]-Ms[0])*R0-cross.H*H1*cross),'quotient resolvent')
            need(equal(cross.H*H1*cross,(B*U).H*Ms[1]*(B*U)),'retained loss Gram')
    def test_complex_noncommuting_blocks(self):
        B,C,Ms,ds=data(4)
        H0,Z0,R0,G0=ds[0];H1,Z1,R1,G1=ds[1]
        need(not equal(G0*G1,G1*G0),'fixture must not commute')
        # Even densities have real Grams despite the complex S coordinate.
        # This separate strictly positive asymmetric density has nonreal entries.
        complexM=gram(2,1+(X+1)**2)
        need(any(v.has(s.I) for v in complexM),'nonreal original-coordinate Gram')
        Bc,Cc=presentation(2,s.expand((S-HALF)**2+1))
        Mc=gram(2,1+(X-2)**2)
        h0,z0,r0,g0=canonical(complexM,Bc,Cc)
        h1,z1,r1,g1=canonical(Mc,Bc,Cc)
        cross=clean(Bc.H*(Mc-complexM)*r0)
        need(equal(g1,g0+r0.H*(Mc-complexM)*r0-cross.H*h1*cross),'nonreal resolvent')
    def test_primitive_cocycle(self):
        B,C,Ms,ds=data()
        def prim(i,j):return clean(ds[j][0]*B.H*(Ms[j]-Ms[i])*ds[i][2])
        need(equal(prim(0,2),prim(0,1)+prim(1,2)),'exact path composition')
    def test_generator_defect(self):
        B,C,Ms,ds=data()
        R0=ds[0][2];R1=ds[1][2]
        D=s.Matrix(4,4,lambda i,j:i-2*j+int(i==j))
        A=s.Matrix([[0,-s.Rational(5,4)],[1,1]])
        U=clean(ds[1][0]*B.H*(Ms[1]-Ms[0])*R0)
        need(equal((D*R1-R1*A)-(D*R0-R0*A),-D*B*U+B*U*A),'full defect')
    def test_repeated_root_and_first_degree(self):
        for N in [1,3]:
            B,C,Ms,ds=data(N,(S-HALF)**2)
            R0=ds[0][2];R1=ds[1][2]
            for j in range(2):
                poly=sum((R1[i,j]-R0[i,j])*S**i for i in range(N+1))
                need(s.rem(poly,(S-HALF)**2,S)==0,'complete repeated relation')
    def test_unchanged_section_case(self):
        B,C,Ms,ds=data()
        H1,Z1,R1,G1=canonical(3*Ms[0],B,C)
        need(equal(R1,ds[0][2]),'same representatives under a common source scale')
        need(equal(B.H*(2*Ms[0])*ds[0][2],s.zeros(B.cols,C.cols)),'cross vanishes')
        need(equal(G1,3*ds[0][3]),'mass not lost')
    def test_trace_interval_and_zero_mode(self):
        diag=s.diag(0,s.Rational(1,4),s.Rational(3,5))
        U=s.Matrix([[1,2,0],[0,1,3],[0,0,1]])
        H=U*diag*U.inv()
        interval,p=matrix_interval(H)
        value=frac((s.eye(3)-H).det())
        l,u=log_bounds(value)
        need(interval[0]<=-u<=-l<=interval[1],'trace-data interval')
        need(p>0,'positive stopping degree')
    def test_signed_four_source_metrics(self):
        As=[]
        for N in [1,2,3,4]:
            B,C,Ms,ds=data(N)
            As.append(clean(ds[0][3].inv()*ds[1][3]))
        c=1+sum(s.trace(A) for A in As)
        intervals=[]
        for A in As:
            I,p=matrix_interval(clean(s.eye(2)-A/c))
            intervals.append(I)
        low=intervals[2][0]+intervals[3][0]-intervals[0][1]-intervals[1][1]
        high=intervals[2][1]+intervals[3][1]-intervals[0][0]-intervals[1][0]
        ratio=frac(As[0].det()*As[1].det()/(As[2].det()*As[3].det()))
        l,u=log_bounds(ratio)
        need(low<=l<=u<=high,'signed endpoint enclosure')
    def test_input_error_and_stopping_guard(self):
        exact=F(17,32);mid=exact+F(1,1000);err=F(1,500)
        need(mid-err<=exact<=mid+err,'absolute error propagation')
        try:enclose_moments({1:F(999,1000),2:F(1,2)},1,F(1,100))
        except ValueError:return
        raise AssertionError('uncertified positive denominator accepted')


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--negative',choices=['omit-loss','subtract-upper-prefixes'])
    args=ap.parse_args()
    if args.negative:
        if args.negative=='omit-loss':
            B,C,Ms,ds=data()
            claimed=equal(ds[1][3],ds[0][3]+ds[0][2].H*(Ms[1]-Ms[0])*ds[0][2])
        else:
            # True prefixes 1 and 2; both upper estimates are valid, their difference is not.
            claimed=(F(2)-F(100)>=F(2)-F(1))
        print(json.dumps({'negative_control':args.negative,'false_claim_accepted':bool(claimed)},sort_keys=True))
        sys.exit(0 if claimed else 1)
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    result=unittest.TextTestRunner(verbosity=1,stream=sys.stderr).run(suite)
    record={'methods':result.testsRun,'success':result.wasSuccessful(),
            'arithmetic_zero_certificate':False,'mass':7,'coordinate':'S=1/2+i*x',
            'scope':'Exact finite source resolvents, original polynomial relations, and certified trace errors.'}
    print(json.dumps(record,indent=2,sort_keys=True))
    if not result.wasSuccessful():sys.exit(1)

if __name__=='__main__':main()
