#!/usr/bin/env python3
"""Finite exact regressions for the tau-base chain-descent research note.

These are algebraic model tests, not numerical tests of zeta zeros, not Lean
certificates, and not an independent verification of PR #8's analytic lemmas.
All checks use unittest methods, which remain active with python -O.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import platform
import sys
import unittest

import sympy as sp

t = sp.Symbol('t')


def rem(p: sp.Expr, h: sp.Expr) -> sp.Expr:
    return sp.rem(sp.expand(p), sp.expand(h), t)


def col(p: sp.Expr, n: int) -> sp.Matrix:
    p = sp.Poly(sp.expand(p), t)
    return sp.Matrix([p.nth(i) for i in range(n)])


def mul_matrix(p: sp.Expr, h: sp.Expr) -> sp.Matrix:
    n = sp.degree(h, t)
    return sp.Matrix.hstack(*(col(rem(p*t**j, h), n) for j in range(n)))


def poly_matrix(p: sp.Expr, matrix: sp.Matrix) -> sp.Matrix:
    out = sp.zeros(matrix.rows)
    for (degree,), value in sp.Poly(p, t).terms():
        out += value * matrix**degree
    return sp.simplify(out)


class Model:
    """Exact finite model: V=A/(h), B=A/(h^2), theta=multiplication by h.

    Arithmetic observation J is multiplication by v then reduction modulo h.
    This models the extension and chain identities, not the analytic spaces.
    """
    def __init__(self, h: sp.Expr, v: sp.Expr):
        self.h, self.v = sp.expand(h), sp.expand(v)
        self.d = int(sp.degree(h, t))
        self.c = sp.invert(v, h, t)
        d = self.d
        self.theta = sp.Matrix.hstack(*(col(h*t**j, 2*d) for j in range(d)))
        self.J = sp.Matrix.hstack(*(col(rem(v*t**j,h), d) for j in range(2*d)))
        self.S = sp.Matrix.hstack(*(col(self.r(t**j),2*d) for j in range(d)))
        self.P = self.S*self.J
        self.Dv = mul_matrix(t,h)
        self.Db = mul_matrix(t,sp.expand(h*h))
        self.K = sp.Matrix.hstack(*(col(self.q(t,t**j),d) for j in range(d)))
        self.delta = sp.zeros(3*d)
        self.delta[d:,:d] = self.theta
        self.projector = sp.diag(sp.zeros(d),self.P)
        self.action = sp.diag(self.Dv,self.Db)
        self.homotopy = sp.zeros(3*d)
        self.homotopy[:d,d:] = self.K*self.J
        self.parity = sp.diag(sp.eye(d),-sp.eye(2*d))

    def r(self,u: sp.Expr) -> sp.Expr:
        return rem(self.c*u,self.h)

    def q(self,p: sp.Expr,u: sp.Expr) -> sp.Expr:
        numerator = sp.expand(p*self.r(u)-self.r(rem(p*u,self.h)))
        quotient, remainder = sp.div(numerator,self.h,t)
        if sp.expand(remainder) != 0:
            raise ArithmeticError('The actual polynomial numerator was not divisible by h')
        return sp.expand(quotient)


CASES = [
    (t-sp.Rational(1,3),2+t),
    ((t-sp.Rational(1,3))**2,2+t+t*t),
    ((t-sp.Rational(1,4))*(t-sp.Rational(3,4)),2+t*(1-t)),
    ((t-sp.Rational(1,4))**2*(t-sp.Rational(3,4))**2,2+t*(1-t)),
]


class ExactChecks(unittest.TestCase):
    def eqm(self,a: sp.Matrix,b: sp.Matrix) -> None:
        self.assertEqual(a.shape,b.shape)
        self.assertEqual(sp.simplify(a-b),sp.zeros(*a.shape))

    def test_01_actual_extension_and_section(self):
        for h,v in CASES:
            with self.subTest(h=h,v=v):
                m=Model(h,v); d=m.d
                self.eqm(m.J*m.theta,sp.zeros(d,d))
                self.eqm(m.J*m.S,sp.eye(d))
                self.eqm(m.P*m.P,m.P)
                self.assertEqual(m.theta.rank(),d)
                self.assertEqual(m.J.rank(),d)
                self.eqm(m.Db*m.theta,m.theta*m.Dv)
                self.eqm(m.J*m.Db,m.Dv*m.J)

    def test_02_rank_one_and_ext_class(self):
        for h,v in CASES:
            with self.subTest(h=h,v=v):
                m=Model(h,v); d=m.d
                self.eqm(m.Db*m.S-m.S*m.Dv,m.theta*m.K)
                self.assertEqual(m.K.rank(),1)
                for j in range(d):
                    self.assertEqual(m.q(t,t**j),sp.Poly(m.r(t**j),t).nth(d-1))
                self.eqm(poly_matrix(m.h,m.Db)*m.S,
                         m.theta*mul_matrix(m.c,m.h))
                self.assertEqual(rem(m.c*m.v,m.h),1)
                self.assertNotEqual(rem(m.c,m.h),0)

    def test_03_polynomial_composition_cocycle(self):
        p=t*t+2; q=t*t*t+t+1
        for h,v in CASES:
            m=Model(h,v)
            for j in range(m.d):
                u=t**j
                with self.subTest(h=h,j=j):
                    difference=m.q(p*q,u)-p*m.q(q,u)-m.q(p,rem(q*u,h))
                    self.assertEqual(sp.expand(difference),0)

    def test_04_chain_projector_and_homotopy(self):
        for h,v in CASES:
            with self.subTest(h=h):
                m=Model(h,v); d=m.d
                self.eqm(m.delta**2,sp.zeros(3*d))
                self.eqm(m.delta*m.projector,m.projector*m.delta)
                self.eqm(m.projector**2,m.projector)
                self.eqm(m.action*m.projector-m.projector*m.action,
                         m.delta*m.homotopy+m.homotopy*m.delta)
                self.assertEqual(m.delta.rank(),d)

    def test_05_dilation_cocycle_with_log_parameters(self):
        x,y,a,b=sp.symbols('x y a b')
        for order in [1,2]:
            m=Model(t**order,2+3*t+t*t); d=order
            Nv=mul_matrix(t,t**d); Nb=mul_matrix(t,t**(2*d))
            def exponential(N,z,scalar):
                return scalar*sum((z**j/sp.factorial(j)*N**j for j in range(N.rows)),sp.zeros(N.rows))
            def k(z,scalar):
                Db=exponential(Nb,z,scalar)
                De=exponential(Nv,z,scalar)
                defect=sp.simplify(Db*m.S-m.S*De)
                self.eqm(defect[:d,:],sp.zeros(d))
                return defect[d:,:]
            ka,kb,kab=k(x,a),k(y,b),k(x+y,a*b)
            self.eqm(kab,exponential(Nv,x,a)*kb+ka*exponential(Nv,y,b))

    def test_06_finite_chain_lefschetz_trace(self):
        for h,v in CASES:
            m=Model(h,v)
            for p in [1,t,2+t+t**3]:
                action=sp.diag(poly_matrix(p,m.Dv),poly_matrix(p,m.Db))
                chain_trace=sp.trace(m.parity*m.projector*action)
                packet_trace=sp.trace(poly_matrix(p,m.Dv))
                self.assertEqual(sp.simplify(chain_trace+packet_trace),0)

    def test_07_reflection_is_strict_with_odd_and_even_degree(self):
        reflection_cases=[
            (t-sp.Rational(1,2)-sp.I,sp.I),
            ((t-sp.Rational(1,4))*(t-sp.Rational(3,4)),2+t*(1-t)),
        ]
        for h,v in reflection_cases:
            m=Model(h,v); d=m.d
            def star(p):
                return sp.expand(sp.conjugate(p).subs(sp.conjugate(t),1-t))
            self.assertEqual(sp.expand(star(h)-(-1)**d*h),0)
            self.assertEqual(sp.expand(star(h*v)-h*v),0)
            for j in range(d):
                u=t**j+sp.I
                self.assertEqual(sp.expand(m.r(star(u))-(-1)**d*star(m.r(u))),0)
                # In this algebra model the Mellin map is multiplication by v.
                # Its induced anti-linear B action is (-1)^d times reflection.
                lhs=rem((-1)**d*star(m.r(u)),sp.expand(h*h))
                rhs=m.r(star(u))
                self.assertEqual(sp.expand(lhs-rhs),0)

    def test_08_ext_unit_residue_jacobian_trace(self):
        cases=[
            ((t-sp.Rational(1,4))*(t-sp.Rational(3,4)),2+t*(1-t),
             [(sp.Rational(1,4),1),(sp.Rational(3,4),1)]),
            ((t-sp.Rational(1,4))**2*(t-sp.Rational(3,4))**2,2+t*(1-t),
             [(sp.Rational(1,4),2),(sp.Rational(3,4),2)]),
        ]
        z=sp.Symbol('z')
        for h,v,roots in cases:
            m=Model(h,v); g=sp.expand(h*v)
            f=1+sp.I*t; u=2+t+t*t
            fs=sp.expand(sp.conjugate(f).subs(sp.conjugate(t),1-t))
            def residue_at(expr,r):
                return sp.residue(expr,t,r)
            # Ext coefficient converts h-residue to actual g-residue.
            lhs=sum(residue_at(fs*m.c*u/h,r) for r,_ in roots)
            rhs=sum(residue_at(fs*u/g,r) for r,_ in roots)
            self.assertEqual(sp.simplify(lhs-rhs),0)
            contracted=sum(residue_at(fs*m.c*sp.diff(g,t)*u/h,r) for r,_ in roots)
            target=sum(order*fs.subs(t,r)*u.subs(t,r) for r,order in roots)
            self.assertEqual(sp.simplify(contracted-target),0)
            self.assertEqual(sp.simplify(sp.trace(mul_matrix(fs*u,h))-target),0)

    def test_09_support_homotopy_mismatch_and_synchronization(self):
        # Finite model of two source legs; Fourier is the identity here.
        # V=k, B=k^2, theta(v)=(v,0), packet quotient is second coordinate.
        theta=sp.Matrix([1,0]); J=sp.Matrix([[0,1]])
        S=sp.Matrix([0,1]); P=S*J
        U=sp.Matrix([[2,7],[0,3]])
        K=sp.Matrix([[7]])
        self.eqm(U*S-S*sp.Matrix([[3]]),theta*K)
        left=sp.Matrix.vstack(K*J,sp.zeros(1,2))
        right=sp.Matrix.vstack(sp.zeros(1,2),-K*J)
        jointd=sp.Matrix.hstack(theta,-theta)
        self.eqm(jointd*left,U*P-P*U)
        self.eqm(jointd*right,U*P-P*U)
        self.assertNotEqual(left,right)
        self.eqm(jointd*(left-right),sp.zeros(2,2))
        self.assertEqual((left-right).rank(),1)
        self.eqm(J*jointd,sp.zeros(1,2))

    def test_10_original_split_synchronization_masks(self):
        p=5
        # None is tau; integer zero is the supported zero.
        def add(a,b):
            return b if a is None else a if b is None else (a+b)%p
        def mul(a,b):
            return None if a is None or b is None else a*b%p
        def support(x):
            return tuple(v is not None for v in x)
        def sync(x):
            a,b=x
            return (add(a,mul(0,b)),add(b,mul(0,a)))
        vals=[None,*range(p)]
        images={}
        for a in vals:
            for b in vals:
                x=(a,b); y=sync(x)
                self.assertEqual(sync(y),y)
                self.assertEqual(tuple(0 if v is None else v for v in x),
                                 tuple(0 if v is None else v for v in y))
                key=(support(x),y)
                self.assertNotIn(key,images)
                images[key]=x
                if any(support(x)):
                    self.assertEqual(support(y),(True,True))
        self.assertNotEqual(sync((None,None)),sync((0,None)))

    def test_11_tensor_homotopy_and_koszul_signs(self):
        m=Model(t-sp.Rational(1,3),2+t)
        delta,parity=m.delta,m.parity
        left=m.action*m.projector
        right=m.projector*m.action
        H=m.homotopy
        for n in [2,3]:
            def tensor(ms):
                out=sp.Matrix([[1]])
                for mat in ms:out=sp.kronecker_product(out,mat)
                return out
            size=3**n
            dn=sp.zeros(size)
            hn=sp.zeros(size)
            for j in range(n):
                dn+=tensor([parity]*j+[delta]+[sp.eye(3)]*(n-j-1))
                # The degree-minus-one factor crosses the preceding inputs.
                hn+=tensor([right*parity]*j+[H]+[left]*(n-j-1))
            self.eqm(dn**2,sp.zeros(size))
            self.eqm(tensor([left]*n)-tensor([right]*n),dn*hn+hn*dn)
            total_parity=tensor([parity]*n)
            trace=sp.trace(total_parity*tensor([left]*n))
            expected=(-1)**n*sp.trace(m.Dv)**n
            self.assertEqual(sp.simplify(trace-expected),0)

    def test_12_degree_one_and_joint_degree_zero(self):
        for h,v in CASES[:3]:
            m=Model(h,v); d=m.d
            # Joint theta uses identity Fourier in this finite model.
            jointd=sp.Matrix.hstack(m.theta,-m.theta)
            self.assertEqual(jointd.cols-jointd.rank(),d)
            self.assertEqual(jointd.rows-jointd.rank(),d)
            cycle=sp.Matrix.vstack(sp.eye(d),sp.eye(d))
            self.eqm(jointd*cycle,sp.zeros(2*d,d))
            self.assertEqual(cycle.rank(),d)
            # Single-leg source has no H0; same E appears as H1.
            self.assertEqual(m.theta.cols-m.theta.rank(),0)
            self.assertEqual(m.theta.rows-m.theta.rank(),d)


class RecordingResult(unittest.TextTestResult):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.passed=[]
    def addSuccess(self,test):
        self.passed.append(test.id())
        super().addSuccess(test)


class DeliberateFailure(unittest.TestCase):
    def runTest(self):
        self.fail('intentional negative control: this must fail under normal and optimized Python')


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json',type=Path)
    parser.add_argument('--deliberate-failure',action='store_true')
    args=parser.parse_args()
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(ExactChecks)
    if args.deliberate_failure:suite.addTest(DeliberateFailure())
    result=unittest.TextTestRunner(verbosity=2,resultclass=RecordingResult).run(suite)
    report={
        'scope':'finite exact algebraic regressions; no analytic or Lean certification',
        'python':platform.python_version(),'sympy':sp.__version__,
        'tests_run':result.testsRun,'success':result.wasSuccessful(),
        'passed':result.passed,
        'failures':[name.id() for name,_ in result.failures],
        'errors':[name.id() for name,_ in result.errors],
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    if args.json:args.json.write_text(json.dumps(report,indent=2)+'\n')
    return 0 if result.wasSuccessful() else 1


if __name__=='__main__':
    raise SystemExit(main())
