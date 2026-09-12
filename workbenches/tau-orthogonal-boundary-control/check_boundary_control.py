#!/usr/bin/env python3
"""Exact finite regressions for the orthogonal-theta-boundary derivations.

These tests verify finite algebraic identities, not the analytic theta range,
actual zeta zeros, polynomial density, or a Lean build. No Python assert is used.
"""
from __future__ import annotations
import argparse
import hashlib
from functools import lru_cache
import itertools
import json
import platform
import sys
import unittest
from pathlib import Path
import sympy as sp


def simp(M: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix(M).applyfunc(sp.simplify)


def equal(A, B) -> bool:
    if isinstance(A, sp.MatrixBase) or isinstance(B, sp.MatrixBase):
        return simp(sp.Matrix(A)-sp.Matrix(B)) == sp.zeros(*sp.Matrix(A).shape)
    return sp.simplify(A-B) == 0


@lru_cache(maxsize=None)
def model(d: int, m: int):
    """Normal finite ambient calibration, NOT the infinite theta quotient."""
    ambient = 8
    D = sp.diag(*[sp.Rational(1, 2)+sp.I*j for j in range(-3,5)])
    if d == 1:
        vals = [sp.Rational(1,2)+sp.I/2]
    elif d == 2:
        vals = [sp.Rational(1,4), sp.Rational(3,4)]
    elif d == 3:
        vals = [sp.Rational(1,4), sp.Rational(3,4),sp.Rational(1,2)+sp.I/2]
    else:
        raise ValueError('d must be 1, 2 or 3')
    A=sp.diag(*vals)
    f=sp.ones(ambient,1)
    R=sp.Matrix(ambient,d,lambda i,j:1/(D[i,i]-A[j,j]))
    F=sp.Matrix.hstack(*[(D**j)*f for j in range(m+1)])
    H=simp(F.H*F); C=simp(F.H*R); B=simp(-H.inv()*C)
    Rm=simp(R+F*B); G=simp(Rm.H*Rm)
    fn=(D**(m+1))*f
    z=simp(Rm.H*fn); b=B[m,:]
    W=simp(A.H*G+G*A-G)
    return D,A,f,R,F,H,C,B,Rm,G,fn,z,b,W


class ExactChecks(unittest.TestCase):
    def eq(self,A,B):
        self.assertTrue(equal(A,B),msg=f'Identity failed: {A!s} versus {B!s}')

    def test_full_two_equation_homotopy_classification(self):
        # R=F_p, V=R, B=R^2, Theta(v)=(v,0), F multiplication by f.
        # Exhaust ALL 2x2 linear H matrices, not only the stated examples.
        for p in (2,3,5):
            for f in range(1,p):
                inv=pow(f,-1,p)
                for k in range(p):
                    observed=set()
                    for a,b,c,d in itertools.product(range(p),repeat=4):
                        # H [[a,b],[c,d]], d_chart [[1,-f],[0,0]].
                        cond1=((a-f*c)%p==0 and (b-f*d-k)%p==0)
                        cond2=(a%p==0 and c%p==0)
                        if cond1 and cond2: observed.add((a,b,c,d))
                    expected={(0,(k+alpha)%p,0,inv*alpha%p) for alpha in range(p)}
                    self.assertEqual(observed,expected)

    def test_original_split_homotopy_lift(self):
        # Internal arithmetic modulo 5, four supports represented by bit masks.
        p=5
        def add(x,y):
            if x is None:return y
            if y is None:return x
            return (x[0]|y[0],tuple((a+b)%p for a,b in zip(x[1],y[1])))
        def scale(r,x):
            if r is None or x is None:return None
            return (x[0],tuple(r*a%p for a in x[1]))
        for alpha in range(p):
            def H(x):
                if x is None:return None
                # kappa(b0,b1)=2*b1, quotient coordinate b1, F=2.
                q=x[1][1]
                return (3,((2+alpha)*q%p,3*alpha*q%p))
            xs=[None]+[(mask,(a,b)) for mask in (1,2,3) for a,b in itertools.product(range(p),repeat=2)]
            for x in xs:
                for r in (None,0,1,2,4): self.assertEqual(H(scale(r,x)),scale(r,H(x)))
                self.assertEqual(H(add(x,x)),add(H(x),H(x)))
            for x,y in zip(xs, reversed(xs)): self.assertEqual(H(add(x,y)),add(H(x),H(y)))
            self.assertEqual(H((1,(1,0))),(3,(0,0)))
            self.assertIsNone(H(None))

    def test_source_equation_and_minimum(self):
        for d,m in ((1,0),(2,0),(2,1),(3,1)):
            D,A,f,R,F,H,C,B,Rm,G,fn,z,b,W=model(d,m)
            self.eq(D*R-R*A,f*sp.ones(1,d))
            self.eq(F.H*Rm,sp.zeros(m+1,d))
            self.eq(G,R.H*R-C.H*H.inv()*C)
            T=sp.Matrix(m+1,d,lambda i,j:sp.Rational(i+j+1,3))
            self.eq((R+F*T).H*(R+F*T),G+(T-B).H*H*(T-B))
            self.assertTrue(all(sp.simplify(G[:i,:i].det())>0 for i in range(1,d+1)))

    def test_rank_two_boundary_control(self):
        for d,m in ((1,1),(2,0),(2,1),(3,0),(3,1)):
            D,A,f,R,F,H,C,B,Rm,G,fn,z,b,W=model(d,m)
            ext=sp.Matrix.hstack(F,fn)
            I=sp.eye(m+2)[:,:m+1]; S=sp.zeros(m+2,m+1)
            for j in range(m+1):S[j+1,j]=1
            ell=sp.ones(1,d); e0=sp.eye(m+2)[:,0]
            K=e0*ell+S*B-I*B*A
            self.eq(D*Rm-Rm*A,ext*K)
            self.eq(W,-z*b-b.H*z.H)
            self.assertLessEqual(W.rank(),2)
            self.eq(sp.trace(G.inv()*W),2*sp.re(sp.trace(A))-d)

    def test_scalar_certificate_polynomial(self):
        cases=[(sp.diag(2,3,4),sp.Matrix([1,sp.I,2]),sp.Matrix([[sp.I,2,-1]])),
               (sp.Matrix([[3,1],[1,2]]),sp.Matrix([1+sp.I,2]),sp.Matrix([[2,1-sp.I]])),
               (sp.Matrix([[5]]),sp.Matrix([1+sp.I]),sp.Matrix([[2-sp.I]]))]
        lam=sp.symbols('lam')
        for G,z,b in cases:
            W=-z*b-b.H*z.H
            u=(z.H*G.inv()*z)[0];v=(b*G.inv()*b.H)[0];c=sp.simplify((b*G.inv()*z)[0])
            # Two-column factorization compares nonzero spectra even in d=1.
            T=-sp.Matrix([[c,v],[u,sp.conjugate(c)]])
            self.eq(T.charpoly(lam).as_expr(),lam**2+2*sp.re(c)*lam+sp.Abs(c)**2-u*v)
            self.eq(sp.trace(G.inv()*W),-2*sp.re(c))
            self.eq(sp.trace((G.inv()*W)**2),sp.trace(T**2))
            self.assertTrue(sp.simplify(u*v-sp.im(c)**2)>=0)

    def test_rank_one_next_level_update(self):
        for d,m in ((1,0),(2,0),(2,1),(3,0)):
            D,A,f,R,F,H,C,B,Rm,G,fn,z,b,W=model(d,m)
            P=simp(F*H.inv()*F.H)
            a=simp((sp.eye(D.rows)-P)*fn); eta=sp.simplify((a.H*a)[0])
            nxt=model(d,m+1)
            self.assertTrue(eta>0)
            self.eq(nxt[8],Rm-a*z.H/eta)
            self.eq(nxt[9],G-z*z.H/eta)
            self.eq(nxt[13]-W,-(A.H*(z*z.H)+(z*z.H)*A-z*z.H)/eta)

    def test_full_quotient_metric_transport(self):
        D,A,f,R,F,H,C,B,Rm,G,fn,z,b,W=model(2,1)
        P=simp(F*H.inv()*F.H)
        a=simp((sp.eye(D.rows)-P)*fn);eta=(a.H*a)[0]
        Pnext=P+a*a.H/eta
        x=sp.Matrix([sp.Rational(j+1,3)+sp.I for j in range(D.rows)])
        y=sp.Matrix([sp.Rational(j*j+1,7) for j in range(D.rows)])
        oldx=(sp.eye(D.rows)-P)*x;newx=(sp.eye(D.rows)-Pnext)*x
        oldy=(sp.eye(D.rows)-P)*y;newy=(sp.eye(D.rows)-Pnext)*y
        self.eq(oldx,newx+a*(a.H*x)[0]/eta)
        self.eq((oldx.H*oldy)[0],(newx.H*newy)[0]+sp.conjugate((a.H*x)[0])*(a.H*y)[0]/eta)

    def test_admitted_representative_gauge(self):
        D,A,f,R,F,H,C,B,Rm,G,fn,z,b,W=model(2,1)
        T=sp.Matrix([[sp.Rational(1,7),sp.I],[2,3]])
        Rp=R+F*T; Cp=F.H*Rp; Bp=-H.inv()*Cp
        self.eq(Rp+F*Bp,Rm)
        self.eq(Bp,B-T)

    def test_theta_polynomial_recursion(self):
        x=sp.symbols('x',positive=True)
        P=4*sp.pi**2*x**4-6*sp.pi*x**2
        for j in range(6):
            expr=P*sp.exp(-sp.pi*x*x)
            new=sp.expand(2*sp.pi*x*x*P-x*sp.diff(P,x))
            self.eq(-x*sp.diff(expr,x),new*sp.exp(-sp.pi*x*x))
            self.eq(P.subs(x,-x),P)
            self.eq(P.subs(x,0),0)
            P=new

    def test_exterior_moment_reflection_coefficients(self):
        t=sp.symbols('t')
        for j in range(8):
            self.eq(sum((-1)**k*sp.binomial(j,k)*t**k for k in range(j+1)),(1-t)**j)
        # Derivative/incomplete-gamma identity, independent of floating evaluation.
        c=sp.symbols('c',positive=True);x=sp.symbols('x',positive=True)
        for k in range(5):
            primitive=-sp.uppergamma(k+sp.Rational(1,2),c*x*x)/(2*c**(k+sp.Rational(1,2)))
            self.eq(sp.diff(primitive,x),x**(2*k)*sp.exp(-c*x*x))

    def test_support_transport_preserves_internal_zero(self):
        # Original split scalar, modulo 5; never represent tau as numeric zero.
        p=5
        def add(a,b):
            if a is None:return b
            if b is None:return a
            return (a+b)%p
        def mul(a,b):
            if a is None or b is None:return None
            return a*b%p
        def sync(v):
            a,b=v;return(add(a,mul(0,b)),add(b,mul(0,a)))
        carrier=[None]+list(range(p))
        for x in itertools.product(carrier,repeat=2):
            self.assertEqual(sync(sync(x)),sync(x))
            self.assertEqual(tuple(0 if a is None else a for a in sync(x)),tuple(0 if a is None else a for a in x))
        self.assertEqual(sync((1,None)),(1,0))
        self.assertNotEqual(sync((1,None)),(1,None))
        self.assertEqual(sync((None,None)),(None,None))

    def test_duality_and_tensor_control(self):
        A=sp.diag(sp.Rational(1,4),sp.Rational(3,4));S=sp.Matrix([[0,1],[-1,0]])
        G=sp.Matrix([[3,1+sp.I],[1-sp.I,4]]);W=A.H*G+G*A-G
        Gd=S.H*G.inv()*S;Wd=A.H*Gd+Gd*A-Gd
        self.eq(A.H*S+S*A,S)
        self.eq(Wd,-S.H*G.inv()*W*G.inv()*S)
        An=sp.kronecker_product(A,sp.eye(2))+sp.kronecker_product(sp.eye(2),A)
        Gn=sp.kronecker_product(G,G)
        self.eq(An.H*Gn+Gn*An-2*Gn,sp.kronecker_product(W,G)+sp.kronecker_product(G,W))

    def test_eigenline_defect_not_removed_by_projection(self):
        for m in range(3):
            D,A,f,R,F,H,C,B,Rm,G,fn,z,b,W=model(2,m)
            for j in range(2):
                self.eq(W[j,j]/G[j,j],2*sp.re(A[j,j])-1)
        for m in range(2):
            self.eq(model(1,m)[13],sp.zeros(1))


class DeliberateFailure(unittest.TestCase):
    def runTest(self):
        self.fail('intentional negative control; must fail even under python -O')


class RecordingResult(unittest.TextTestResult):
    def __init__(self,*a,**kw):
        super().__init__(*a,**kw);self.passed=[]
    def addSuccess(self,test):
        self.passed.append(test.id());super().addSuccess(test)


def main()->int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--json',type=Path)
    ap.add_argument('--deliberate-failure',action='store_true')
    args=ap.parse_args()
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(ExactChecks)
    if args.deliberate_failure:suite.addTest(DeliberateFailure())
    res=unittest.TextTestRunner(verbosity=2,resultclass=RecordingResult).run(suite)
    out={'scope':'finite algebraic regressions, not Lean or analytic certificates',
         'python':platform.python_version(),'sympy':sp.__version__,
         'tests_run':res.testsRun,'success':res.wasSuccessful(),
         'passed':res.passed,'failures':[t.id() for t,_ in res.failures],
         'errors':[t.id() for t,_ in res.errors],
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if args.json:args.json.write_text(json.dumps(out,indent=2)+'\n')
    return 0 if res.wasSuccessful() else 1

if __name__=='__main__':sys.exit(main())
