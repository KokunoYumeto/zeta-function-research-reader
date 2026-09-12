#!/usr/bin/env python3
"""Exact finite regression models for the authored global theta retraction note.

These do not certify any analytic convergence or Fourier uncertainty theorem.
All checks use unittest, so they remain active under python -O.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
import unittest
from pathlib import Path
from typing import Iterable

import sympy as sp

Q = sp.Rational


def kron(*factors: sp.MatrixBase) -> sp.MatrixBase:
    return sp.kronecker_product(*factors) if factors else sp.Matrix([[1]])


def collapse(matrix: sp.MatrixBase) -> sp.MatrixBase:
    return matrix.applyfunc(sp.simplify)


class SplitScalar:
    """None is tau. Zero with present=True is e. Rational amplitudes only."""

    def __init__(self, value: sp.Expr | int | None):
        self.value = None if value is None else sp.sympify(value)

    def __add__(self, other: 'SplitScalar') -> 'SplitScalar':
        if self.value is None:
            return other
        if other.value is None:
            return self
        return SplitScalar(self.value + other.value)

    def __mul__(self, other: 'SplitScalar') -> 'SplitScalar':
        if self.value is None or other.value is None:
            return SplitScalar(None)
        return SplitScalar(self.value * other.value)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, SplitScalar) and self.value == other.value

    def __repr__(self) -> str:
        return 'tau' if self.value is None else f'{self.value}^bullet'


def mixed_mul(x: tuple[SplitScalar, SplitScalar],
              y: tuple[SplitScalar, SplitScalar]) -> tuple[SplitScalar, SplitScalar]:
    a, b = x
    c, d = y
    return a*c + SplitScalar(-1)*b*d, a*d + b*c


def support(x: tuple[SplitScalar, SplitScalar]) -> tuple[bool, bool]:
    return tuple(c.value is not None for c in x)  # type: ignore[return-value]


def model(seed: int = 1):
    """An exact non-orthogonal split injection, not an analytic theta model."""
    B = sp.Matrix([[seed, 1], [-1, seed + 1]])
    theta = sp.eye(4)[:, :2]
    section = sp.Matrix.vstack(B, sp.eye(2))
    left = sp.Matrix.hstack(sp.eye(2), -B)
    quotient = sp.eye(4)[2:, :]
    return theta, left, quotient, section


class ExactChecks(unittest.TestCase):
    def eq(self, a, b):
        if isinstance(a, sp.MatrixBase) or isinstance(b, sp.MatrixBase):
            self.assertEqual(collapse(a - b), sp.zeros(a.rows, a.cols))
        else:
            self.assertEqual(sp.simplify(a - b), 0)

    def test_01_full_mobius_inverse(self):
        for n in range(1, 24):
            theta = sp.zeros(n)
            mobius = sp.zeros(n)
            for i in range(1, n + 1):
                for j in range(i, n + 1, i):
                    theta[i-1, j-1] = 2
                    mobius[i-1, j-1] = Q(1, 2)*sp.mobius(j//i)
            self.eq(mobius*theta, sp.eye(n))
            self.eq(theta*mobius, sp.eye(n))
            for k in range(2, n + 1):
                value = SplitScalar(0)
                for d in sp.divisors(k):
                    value = value + SplitScalar(sp.mobius(d))
                self.assertEqual(value, SplitScalar(0))
                self.assertNotEqual(value, SplitScalar(None))

    def test_02_euler_derivative_coefficients(self):
        x = sp.symbols('x', positive=True)
        f = x**7 + 2*x**3 + x**-4
        for order in range(7):
            actual = f
            for k in range(order):
                actual = -x*sp.diff(actual, x) + k*actual
            self.eq((-1)**order*actual, x**order*sp.diff(f, x, order))

    def test_03_cutoff_parametrix_finite_unitary(self):
        U = sp.Matrix([[1,1,1,1],[1,-1,1,-1],
                       [1,1,-1,-1],[1,-1,-1,1]])/2
        self.eq(U.T*U, sp.eye(4))
        for a, b in [(Q(1,3), Q(1,4)), (Q(2,5), Q(1,7)), (0,0)]:
            A = sp.diag(1,a,0,0)
            B = U.T*sp.diag(1,0,b,0)*U
            T = A*B
            positivity = sp.eye(4)-T.T*T
            for k in range(1,5):
                self.assertGreater(positivity[:k,:k].det(), 0)
            rhs = sp.eye(4)-A+A*(sp.eye(4)-B)
            self.eq(rhs, sp.eye(4)-T)
            self.eq((sp.eye(4)-T).inv()*rhs, sp.eye(4))

    def test_04_moment_projection(self):
        x = sp.symbols('x', real=True)
        g0 = sp.exp(-sp.pi*x*x)
        g2 = 2*sp.pi*x*x*g0
        for g, v0, integral in [(g0,1,1),(g2,0,1)]:
            self.eq(g.subs(x,0), v0)
            self.eq(sp.integrate(g,(x,-sp.oo,sp.oo)), integral)
        # Independent exact finite moment map with a non-coordinate section.
        moments = sp.Matrix([[1,0,2,0],[1,1,0,3]])
        section = sp.Matrix([[1,0],[-1,1],[0,0],[0,0]])
        self.eq(moments*section, sp.eye(2))
        P = sp.eye(4)-section*moments
        self.eq(P*P,P)
        self.eq(moments*P,sp.zeros(2,4))

    def test_05_global_splitting_and_dual(self):
        for seed in [-2,0,1,3]:
            th, L, q, s = model(seed)
            K = sp.eye(4)-th*L
            self.eq(L*th,sp.eye(2))
            self.eq(q*s,sp.eye(2))
            self.eq(L*s,sp.zeros(2))
            self.eq(K,s*q)
            self.eq(K*K,K)
            self.eq(sp.Matrix.hstack(th,s)*sp.Matrix.vstack(L,q),sp.eye(4))
            self.eq(th.T*L.T,sp.eye(2))
            self.eq(L.T*th.T+q.T*s.T,sp.eye(4))

    def test_06_two_leg_contractions(self):
        th,L,q,s = model(2)
        Fourier = sp.Matrix([[0,1],[1,0]])
        d = sp.Matrix.hstack(th,-th*Fourier)
        i0 = sp.Matrix.vstack(Fourier,sp.eye(2))
        pL = sp.Matrix.hstack(sp.zeros(2),sp.eye(2))
        pR = sp.Matrix.hstack(Fourier,sp.zeros(2))
        HL = sp.Matrix.vstack(L,sp.zeros(2,4))
        HR = sp.Matrix.vstack(sp.zeros(2,4),-Fourier*L)
        for p,H in [(pL,HL),(pR,HR)]:
            self.eq(p*i0,sp.eye(2))
            self.eq(H*d,sp.eye(4)-i0*p)
            self.eq(d*H,sp.eye(4)-s*q)
        self.eq(d*(HL-HR),sp.zeros(4))
        self.assertNotEqual(HL,HR)

    def test_07_original_synchronization_and_recovery(self):
        tau,e,one=SplitScalar(None),SplitScalar(0),SplitScalar(1)
        E=(one,e)
        cases=[tau,e,one,SplitScalar(-1),SplitScalar(2)]
        observed={}
        for a in cases:
            for b in cases:
                x=(a,b)
                r=mixed_mul(E,x)
                self.assertEqual(mixed_mul(E,r),r)
                self.assertEqual(tuple(0 if v.value is None else v.value for v in x),
                                 tuple(0 if v.value is None else v.value for v in r))
                key=(support(x),repr(r))
                if key in observed:self.assertEqual(observed[key],x)
                observed[key]=x
                if support(x)!=(False,False):self.assertEqual(support(r),(True,True))
        self.assertEqual(mixed_mul(E,(tau,tau)),(tau,tau))
        self.assertEqual(mixed_mul(E,(one,tau)),(one,e))

    def test_08_global_cocycle(self):
        th,L,q,s = model(1)
        change=sp.Matrix.hstack(th,s)
        A1=sp.Matrix([[1,1],[0,1]]); C1=sp.Matrix([[2,0],[0,3]])
        A2=sp.Matrix([[1,0],[1,1]]); C2=sp.Matrix([[1,1],[0,1]])
        B1=sp.Matrix([[1,2],[3,1]]); B2=sp.Matrix([[0,-1],[2,1]])
        def action(a,b,c):
            return change*sp.Matrix.vstack(sp.Matrix.hstack(a,b),
                         sp.Matrix.hstack(sp.zeros(2),c))*change.inv()
        U1=action(A1,B1,C1); U2=action(A2,B2,C2)
        k1=L*U1*s; k2=L*U2*s
        self.eq(U1*s-s*C1,th*k1)
        self.eq(L*U1*U2*s,A1*k2+k1*C2)
        b=sp.Matrix([[2,-1],[1,3]])
        snew=s+th*b; Lnew=L-b*q
        self.eq(Lnew*snew,sp.zeros(2))
        self.eq(Lnew*U1*snew,k1+A1*b-b*C1)

    def test_09_finite_extension_class_unchanged(self):
        t=sp.symbols('t')
        for h in [(t-2)*(t+1), (t-2)**3, (t-2)**2*(t+1)]:
            old=3+t+t*t
            b=2-t+t**3
            new=old-h*b
            self.eq(sp.rem(new,h,t),sp.rem(old,h,t))
            self.eq(new+ h*b,old)

    def test_10_projector_change_trace(self):
        th,L,q,s=model(2)
        old_s=s+th*sp.Matrix([[1,2],[0,-1]])
        P=old_s*q; Pnew=s*q
        b=L*old_s
        self.eq(Pnew-P,-th*b*q)
        self.eq(q*th,sp.zeros(2))
        C=sp.Matrix([[3,1],[0,4]])
        self.eq(sp.trace(old_s*C*q),sp.trace(s*C*q))
        self.eq(sp.trace(s*C*q),sp.trace(C))

    def test_11_completed_tensor_contraction_algebra(self):
        # Basis (source degree 0, boundary degree 1, quotient degree 1).
        d=sp.zeros(3);d[1,0]=1
        h=sp.zeros(3);h[0,1]=1
        P=sp.diag(0,0,1); parity=sp.diag(1,-1,-1); I=sp.eye(3)
        for n in range(1,5):
            dn=sp.zeros(3**n);hn=sp.zeros(3**n)
            for j in range(n):
                dn += kron(*([parity]*j+[d]+[I]*(n-j-1)))
                hn += kron(*([P*parity]*j+[h]+[I]*(n-j-1)))
            self.eq(dn*dn,sp.zeros(3**n))
            self.eq(dn*hn+hn*dn,sp.eye(3**n)-kron(*([P]*n)))

    def test_12_exact_metric_boundary_defect(self):
        th,L,q,s=model(2)
        A=sp.Matrix([[0,1],[1,0]]); C=sp.diag(1,-1)
        U=2*sp.diag(A,C); action=2*C
        self.eq(U.T*U,4*sp.eye(4))
        k=L*U*s; B=th*k
        gram=s.T*s
        left=action.T*gram*action-4*gram
        right=-(U*s).T*B-B.T*(U*s)+B.T*B
        self.eq(left,right)
        self.assertNotEqual(left,sp.zeros(2))


class DeliberateFailure(unittest.TestCase):
    def runTest(self):
        self.fail('intentional failure control; normal and -O must both fail')


class RecordingResult(unittest.TextTestResult):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.passed=[]
    def addSuccess(self,test):
        self.passed.append(test.id())
        super().addSuccess(test)


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json',type=Path)
    parser.add_argument('--deliberate-failure',action='store_true')
    args=parser.parse_args()
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(ExactChecks)
    if args.deliberate_failure:suite.addTest(DeliberateFailure())
    result=unittest.TextTestRunner(verbosity=2,resultclass=RecordingResult).run(suite)
    report={
        'scope':'exact finite regression models, not analytic or Lean certification',
        'python':platform.python_version(),'sympy':sp.__version__,
        'tests_run':result.testsRun,'success':result.wasSuccessful(),
        'passed':result.passed,
        'failures':[t.id() for t,_ in result.failures],
        'errors':[t.id() for t,_ in result.errors],
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    if args.json:args.json.write_text(json.dumps(report,indent=2)+'\n')
    return 0 if result.wasSuccessful() else 1


if __name__=='__main__':
    raise SystemExit(main())
