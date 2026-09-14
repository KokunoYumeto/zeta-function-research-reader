#!/usr/bin/env python3
"""Exact finite checks for the original-source two-moment determinant bound.
No numerical arithmetic-zero input and no Lean certificate are supplied here.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from math import isqrt
from pathlib import Path
import json
import sys
import unittest
import sympy as s

S = s.symbols('S')

def require(p: bool, message: str) -> None:
    if not p:
        raise AssertionError(message)

def eq(a, b) -> bool:
    if isinstance(a, s.MatrixBase) or isinstance(b, s.MatrixBase):
        return (a-b).applyfunc(s.simplify) == s.zeros(*a.shape)
    return s.simplify(a-b) == 0

def frac(x) -> F:
    x=s.Rational(x)
    return F(int(x.p), int(x.q))

class Interval:
    def __init__(self, lo, hi=None):
        self.lo=F(lo); self.hi=F(lo if hi is None else hi)
        require(self.lo<=self.hi, 'reversed interval')
    @staticmethod
    def cast(x): return x if isinstance(x,Interval) else Interval(x)
    def __add__(self,y):
        y=self.cast(y); return Interval(self.lo+y.lo,self.hi+y.hi)
    __radd__=__add__
    def __neg__(self): return Interval(-self.hi,-self.lo)
    def __sub__(self,y): return self+-self.cast(y)
    def __rsub__(self,y): return self.cast(y)+-self
    def __mul__(self,y):
        y=self.cast(y); v=[a*b for a in (self.lo,self.hi) for b in (y.lo,y.hi)]
        return Interval(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,y):
        y=self.cast(y);require(not y.lo<=0<=y.hi,'division across zero')
        return self*Interval(1/y.hi,1/y.lo)
    def __rtruediv__(self,y):return self.cast(y)/self
    def power(self,n:int):
        require(n>=0,'negative power');out=Interval(1)
        for _ in range(n):out=out*self
        return out
    def json(self):
        scale=1<<180
        lo=F((self.lo.numerator*scale)//self.lo.denominator,scale)
        hi=F(-((-self.hi.numerator*scale)//self.hi.denominator),scale)
        return {'lower':str(lo),'upper':str(hi),'outward_dyadic_bits':180}

def log_fraction(x:F,terms:int=42)->Interval:
    x=F(x);require(x>0,'nonpositive logarithm')
    if x<1:return -log_fraction(1/x,terms)
    e=0;y=x
    while y>=2:y/=2;e+=1
    def series(y):
        z=(y-1)/(y+1);p=z;v=F(0)
        for n in range(terms):v+=2*p/(2*n+1);p*=z*z
        err=2*p/((2*terms+1)*(1-z*z))
        return Interval(v,v+err)
    return series(y)+e*series(F(2))

def log_interval(x:Interval)->Interval:
    return Interval(log_fraction(x.lo).lo,log_fraction(x.hi).hi)

def sqrt_fraction(x:F,bits:int=90)->Interval:
    x=F(x);require(x>=0,'negative square root')
    scale=1<<bits;n=isqrt((x.numerator*scale*scale)//x.denominator)
    lo=F(n,scale)
    if lo*lo==x:return Interval(lo)
    return Interval(lo,F(n+1,scale))

def two_moment_parameters(q:int,t1,t2):
    require(q>=2,'parameters require q>=2')
    d=s.sqrt((q*t2-t1*t1)/s.Integer(q-1))
    return s.simplify((t1+(q-1)*d)/q),s.simplify((t1-d)/q)

def sharp_upper_interval(q:int,t1:F,t2:F)->Interval:
    d=sqrt_fraction((q*t2-t1*t1)/F(q-1))
    a=(Interval(t1)+(q-1)*d)/q;b=(Interval(t1)-d)/q
    return log_interval(1+a)+(q-1)*log_interval(1+b)

def hermite_certificate(q:int,t1:Interval,t2:Interval,cap:F,tangent:F)->Interval:
    require(F(0)<=tangent<cap,'invalid nodes')
    require(cap>=t1.hi,'cap not established by trace upper bound')
    la=log_fraction(1+cap);lb=log_fraction(1+tangent)
    c=(la-lb-(cap-tangent)/(1+tangent))/((cap-tangent)**2)
    return q*lb+(t1-q*tangent)/(1+tangent)+c*(t2-2*tangent*t1+q*tangent*tangent)

@lru_cache(None)
def fixture(q:int,last:int,c=s.Integer(1),mass=s.Integer(7)):
    chi=(S-c)**q;p=[s.Integer(1)]
    if last:p.append(S-c)
    for n in range(1,last):p.append(s.expand((S-c)*p[-1]+n*p[-2]))
    cols=[]
    for v in p:
        rem=s.Poly(s.rem(v,chi,S),S)
        cols.append(s.Matrix([rem.nth(a) for a in range(q)]))
    def at(n):
        B=s.Matrix.hstack(*cols[:n+1]);O=s.diag(*[mass*s.factorial(a) for a in range(n+1)])
        K=B*O.inv()*B.H;G=K.inv();R=O.inv()*B.H*G
        return B,O,K,G,R
    acols=[]
    for a in range(q):
        v=s.Poly(s.rem(S**(a+1),chi,S),S);acols.append(s.Matrix([v.nth(r) for r in range(q)]))
    A=s.Matrix.hstack(*acols)
    return p,cols,at,A

def block(q:int,i:int,j:int):
    p,cols,at,A=fixture(q,j)
    Bi,Oi,Ki,Gi,Ri=at(i);Bj,Oj,Kj,Gj,Rj=at(j)
    Fc=s.Matrix.hstack(*cols[i+1:j+1]) if j>i else s.zeros(q,0)
    Om=s.diag(*[7*s.factorial(n) for n in range(i+1,j+1)]) if j>i else s.zeros(0)
    D=Kj-Ki;Z=D*Gi;T=Ki*Gj
    t1=s.trace(Z);t2=s.trace(Z*Z);e2=s.factor((t1*t1-t2)/2)
    return locals()

class Tests(unittest.TestCase):
    def test_01_inverse_restriction_source(self):
        b=block(3,3,6);I=s.eye(3)
        self.assertTrue(eq(b['Z'],b['T'].inv()-I))
        self.assertTrue(eq(b['Gi']*b['Z'],b['Z'].H*b['Gi']))
        L=s.zeros(7,4);L[:4,:4]=s.eye(4);P=L*L.T
        self.assertTrue(eq(L*b['Ri']*b['T'],P*b['Rj']))
    def test_02_actual_source_adjoint(self):
        b=block(3,3,6);Fd=b['Om'].inv()*b['Fc'].H*b['Gi']
        self.assertTrue(eq(b['Z'],b['Fc']*Fd))
        self.assertTrue(eq((b['Ri']*b['Fc']).H*b['Oi']*(b['Ri']*b['Fc']),b['Fc'].H*b['Gi']*b['Fc']))
    def test_03_trace_cross_pairings(self):
        b=block(3,3,6);F0=b['Fc'];G=b['Gi'];weights=list(b['Om'].diagonal())
        t1=sum((F0[:,a].H*G*F0[:,a])[0]/weights[a] for a in range(F0.cols))
        t2=sum((F0[:,a].H*G*F0[:,c])[0]*s.conjugate((F0[:,a].H*G*F0[:,c])[0])/(weights[a]*weights[c]) for a in range(F0.cols) for c in range(F0.cols))
        self.assertTrue(eq(t1,b['t1']));self.assertTrue(eq(t2,b['t2']))
    def test_04_exterior_area(self):
        b=block(3,3,6);Gram=b['Fc'].H*b['Gi']*b['Fc'];weights=list(b['Om'].diagonal())
        e2=sum(Gram.extract([a,c],[a,c]).det()/(weights[a]*weights[c]) for a,c in combinations(range(Gram.rows),2))
        self.assertTrue(eq(e2,b['e2']));self.assertEqual(e2,s.Rational(507,64))
    def test_05_original_relation(self):
        b=block(3,3,6);L=s.zeros(7,4);L[:4,:4]=s.eye(4)
        new=s.zeros(7,3);new[4:7,:]=s.eye(3)
        rel=new-L*b['Ri']*b['Fc']
        self.assertTrue(eq(b['Bj']*rel,s.zeros(3)))
        self.assertTrue(eq(rel.H*b['Oj']*rel,b['Om']+b['Fc'].H*b['Gi']*b['Fc']))
    def test_06_action_defect(self):
        b=block(3,3,6);A=b['A'];I=s.eye(3)
        H1=b['Ki']*(A.H*b['Gi']+b['Gi']*A-2*b['Gi'])
        H2=b['Kj']*(A.H*b['Gj']+b['Gj']*A-2*b['Gj'])
        self.assertTrue(eq(A*b['Z']-b['Z']*A,H2*(I+b['Z'])-(I+b['Z'])*H1))
    def test_07_coordinate_transport(self):
        b=block(3,3,6);C=s.Matrix([[1,s.I,0],[0,2,1],[1,0,1]])
        self.assertNotEqual(C.det(),0)
        F1=C*b['Fc'];G1=C.inv().H*b['Gi']*C.inv()
        Z1=F1*b['Om'].inv()*F1.H*G1
        self.assertTrue(eq(Z1,C*b['Z']*C.inv()))
        self.assertTrue(eq(s.trace(Z1**2),b['t2']))
    def test_08_literal_mass(self):
        b=block(3,3,6);mass=s.Rational(11,7)
        Z1=b['Fc']*(mass*b['Om']).inv()*b['Fc'].H*(mass*b['Gi'])
        self.assertTrue(eq(Z1,b['Z']))
    def test_09_dimension_two_exact(self):
        totals=s.Integer(1)
        for i,j in [(1,3),(2,4)]:
            b=block(2,i,j);a,c=two_moment_parameters(2,b['t1'],b['t2'])
            det=(s.eye(2)+b['Z']).det();self.assertTrue(eq(det,(1+a)*(1+c)));totals*=det
        self.assertEqual(totals,s.Rational(375,32))
    def test_10_exact_extremizers(self):
        for q,a,b in [(4,9,2),(5,20,1),(3,7,0),(4,2,2)]:
            vals=[s.Integer(a)]+[s.Integer(b)]*(q-1)
            t1=sum(vals);t2=sum(x*x for x in vals);aa,bb=two_moment_parameters(q,t1,t2)
            self.assertTrue(eq(aa,a));self.assertTrue(eq(bb,b))
            self.assertTrue(eq(s.prod(1+x for x in vals),(1+aa)*(1+bb)**(q-1)))
    def test_11_rational_area_upper(self):
        for vals in [(0,1,2),(1,3,6),(1,2,3,4),(0,0,9,12),(1,1,1,5,100)]:
            q=len(vals);t1=s.Integer(sum(vals));t2=s.Integer(sum(x*x for x in vals));e2=(t1*t1-t2)/2
            upper=(1+t1)*(1+2*e2/((q-1)*t1))**(q-1)
            self.assertGreaterEqual(upper,s.prod(1+x for x in vals))
    def test_12_scalar_remainder_identity(self):
        x,b,a,t=s.symbols('x b a t');g=lambda y:1/(t+y)
        c=(g(a)-g(b)+(a-b)/(t+b)**2)/(a-b)**2
        interp=g(b)-(x-b)/(t+b)**2+c*(x-b)**2
        exact=(a-x)*(x-b)**2/((t+x)*(t+b)**2*(t+a))
        # Reciprocal minus its interpolant has the same nonnegative sign.
        self.assertTrue(eq(g(x)-interp,exact))
    def test_13_third_remainder_positive(self):
        b0=block(3,2,5);Z=b0['Z'];a,b=two_moment_parameters(3,b0['t1'],b0['t2'])
        C3=s.trace((a*s.eye(3)-Z)*(Z-b*s.eye(3))**2)
        self.assertGreater(C3,0)
        self.assertTrue(eq(C3,-s.trace(Z**3)+(a+2*b)*b0['t2']-(2*a*b+b*b)*b0['t1']+3*a*b*b))
    def test_14_sharp_interval_fixture(self):
        b0=block(3,3,6);U=sharp_upper_interval(3,frac(b0['t1']),frac(b0['t2']))
        actual=log_fraction(frac((s.eye(3)+b0['Z']).det()))
        self.assertLess(actual.hi,U.lo)
        self.assertLess(U.hi,F(30634,10000))
        coarse=3*log_fraction(1+frac(b0['t1'])/3)
        self.assertLess(U.hi,coarse.lo)
    def test_15_error_aware_certificate(self):
        b0=block(3,3,6);e=F(1,10**10)
        U=hermite_certificate(3,Interval(F(11)-e,F(11)+e),Interval(F(3365,32)-e,F(3365,32)+e),F(11)+e,F(29,40))
        exact=log_fraction(F(5145,256))
        self.assertLess(exact.hi,U.lo)
        self.assertLess(U.hi,F(33,10))
    def test_16_log_interval_arithmetic(self):
        for a,b in [(F(7),F(3,8)),(F(1,99),F(27)),(F(15,4),F(25,8))]:
            x=log_fraction(a)+log_fraction(b);y=log_fraction(a*b)
            self.assertLessEqual(max(x.lo,y.lo),min(x.hi,y.hi))
        self.assertEqual(log_fraction(F(1)).lo,0)
    def test_17_cap_from_moments(self):
        for vals in [(0,1,2),(1,2,3,4),(1,1,1,5,100)]:
            q=len(vals);t1=s.Integer(sum(vals));t2=s.Integer(sum(x*x for x in vals));a,b=two_moment_parameters(q,t1,t2)
            self.assertTrue(bool(a>=max(vals)));self.assertTrue(bool(b>=0))
            self.assertTrue(eq(a+(q-1)*b,t1));self.assertTrue(eq(a*a+(q-1)*b*b,t2))
    def test_18_rank_one_source(self):
        G=s.Matrix([[2,1],[1,3]]);F0=s.Matrix([[1,2],[1,2]]);O=s.diag(7,11)
        Z=F0*O.inv()*F0.H*G;t=s.trace(Z)
        self.assertEqual(Z.rank(),1);self.assertTrue(eq(s.trace(Z**2),t*t))
        self.assertTrue(eq((s.eye(2)+Z).det(),1+t))
    def test_19_supported_relation_and_area(self):
        tau=('absent',None)
        def lift(fn,x):return tau if x[0]=='absent' else (x[0],fn(x[1]))
        rel=('degree-j',s.Poly((S-1)**2,S))
        image=lift(lambda x:s.rem(x.as_expr(),(S-1)**2,S),rel)
        self.assertEqual(image,('degree-j',0));self.assertNotEqual(image,tau)
        self.assertEqual(lift(lambda x:0,tau),tau)
        admitted=('pair-(0,2)',s.det(s.Matrix([[1,2],[0,0]])))
        self.assertEqual(admitted[1],0);self.assertNotEqual(admitted,tau)
    def test_20_two_trace_gap(self):
        q=4;a=s.Integer(9);b=s.Integer(2);J=s.diag(a,b,b,b)
        T=(s.eye(q)+J).inv();self.assertEqual(min(T.diagonal()),1/(1+a))
    def test_21_zero_cases(self):
        Z=s.zeros(3);self.assertEqual(s.trace(Z),0);self.assertEqual((s.eye(3)+Z).det(),1)
        self.assertEqual(s.zeros(0).det(),1)
        a=s.Rational(7,3);self.assertEqual((s.eye(1)+s.Matrix([[a]])).det(),1+a)
    def test_22_extremal_formula_majorant(self):
        # Rational nodes give an exact bound on every diagonal spectrum here.
        vals=[s.Rational(0),s.Rational(9,4),s.Rational(9,2)]
        q=3;t1=sum(vals);t2=sum(x*x for x in vals)
        a,b=two_moment_parameters(q,t1,t2)
        if a.is_Rational and b.is_Rational:
            self.assertGreaterEqual((1+a)*(1+b)**(q-1),s.prod(1+x for x in vals))
        else:
            ui=sharp_upper_interval(q,frac(t1),frac(t2))
            li=log_fraction(frac(s.prod(1+x for x in vals)))
            self.assertLessEqual(li.hi,ui.lo)

def run_negative():
    G=s.eye(2);F0=s.Matrix([[1,1],[0,1]])
    Z=F0*F0.H*G
    exact=(s.trace(Z)**2-s.trace(Z**2))/2
    omitted=(F0[:,0].H*G*F0[:,0])[0]*(F0[:,1].H*G*F0[:,1])[0]
    require(eq(exact,omitted),'negative control rejected: omitted cross-pairing changes exterior area')

def calibration():
    records=[]
    for q,i,j in [(2,1,3),(2,2,4),(3,2,5),(3,3,6)]:
        b0=block(q,i,j);a,b=two_moment_parameters(q,b0['t1'],b0['t2'])
        det=s.factor((s.eye(q)+b0['Z']).det())
        records.append({'q':q,'i':i,'j':j,'t1':str(b0['t1']),'t2':str(b0['t2']),'e2':str(b0['e2']),
          'determinant_ratio':str(det),'a':str(a),'b':str(b),
          'actual_log_interval':log_fraction(frac(det)).json(),
          'two_moment_log_interval':sharp_upper_interval(q,frac(b0['t1']),frac(b0['t2'])).json()})
    return {'scope':'exact Gaussian polynomial fixtures; no actual zeta-zero certificate','records':records}

def main():
    p=argparse.ArgumentParser();p.add_argument('--json');p.add_argument('--calibration');p.add_argument('--negative-control',action='store_true');args=p.parse_args()
    if args.negative_control:
        try:run_negative()
        except AssertionError as e:print(str(e),file=sys.stderr);return 1
        return 0
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    names=[t.id().split('.')[-1] for t in suite]
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    data={'passed':result.wasSuccessful(),'test_methods':result.testsRun,'names':names,
          'failures':len(result.failures),'errors':len(result.errors),
          'scope':'finite exact matrix, polynomial, scalar, and rational-enclosure checks; not Lean or arithmetic quadrature'}
    if args.json:Path(args.json).write_text(json.dumps(data,indent=2)+'\n')
    if args.calibration:Path(args.calibration).write_text(json.dumps(calibration(),indent=2)+'\n')
    return 0 if result.wasSuccessful() else 1
if __name__=='__main__':raise SystemExit(main())
