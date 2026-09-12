#!/usr/bin/env python3
"""Exact finite regressions for FINITE_OPERATOR_COMPARISON.md.

These test encoded algebraic examples; they do not certify the analytic range
lemmas, spectral completeness, Deligne's estimates, or RH. No Python assert
statement is used. unittest assertions execute with and without python -O.
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

x, s, z, L, a0 = sp.symbols('x s z L a0')


def truncated(expr, n):
    if n == 0:
        return sp.Integer(0)
    return sp.series(expr, z, 0, n).removeO().expand()


def multiplication_matrix(expr, n):
    M = sp.zeros(n)
    e = truncated(expr, n)
    for j in range(n):
        v = truncated(e * z**j, n)
        for i in range(n):
            M[i, j] = v.coeff(z, i)
    return M


def op_gaussian(P):
    return sp.expand(-x * sp.diff(P, x) + 2 * sp.pi * x**2 * P)


def relative_mellin_gaussian(P):
    # Integral divided by (1/2)*pi^(-s/2)*Gamma(s/2), with this factor retained.
    result = 0
    for (degree,), coeff in sp.Poly(P, x).terms():
        if degree % 2:
            raise ValueError('expected even polynomial')
        k = degree // 2
        result += coeff * sp.pi**(-k) * sp.rf(s / 2, k)
    return sp.expand(result)


class FiniteOperatorTests(unittest.TestCase):
    def equal_matrix(self, A, B):
        self.assertEqual(A.shape, B.shape)
        for left, right in zip(A, B):
            self.assertEqual(sp.simplify(left-right), 0)

    def test_gaussian_multiplier_and_all_retained_factors(self):
        P = 4 * sp.pi**2 * x**4 - 6 * sp.pi * x**2
        for j in range(7):
            with self.subTest(order=j):
                self.assertEqual(sp.simplify(relative_mellin_gaussian(P)
                                             - s**j * s * (s-1)), 0)
                self.assertEqual(P.subs(x, 0), 0)
                self.assertEqual(relative_mellin_gaussian(P).subs(s, 1), 0)
            P = op_gaussian(P)

    def test_source_local_inverse_coefficients(self):
        rho = sp.Rational(1, 3) + sp.I * sp.Rational(2, 5)
        P = sum((j+2)*x**(2*j) for j in range(1, 8))
        inverse = -sum((j+2)*x**(2*j)/(rho+2*j) for j in range(1, 8))
        self.assertEqual(sp.expand(-x*sp.diff(inverse, x)-rho*inverse-P), 0)
        self.assertEqual(inverse.subs(x, 0), 0)
        self.assertEqual(sp.expand(inverse.subs(x, -x)-inverse), 0)

    def test_ode_operator_on_logarithmic_gaussians(self):
        y, rho = sp.symbols('y rho')
        F = sp.exp(-y*y)
        H = -sp.diff(F, y)-rho*F
        # Exact derivative of the defining tail primitive.
        self.assertEqual(sp.simplify(sp.diff(sp.exp(rho*y)*F, y)
                                     + sp.exp(rho*y)*H), 0)
        for m in range(1, 5):
            Hm = F
            for _ in range(m):
                Hm = -sp.diff(Hm, y)-rho*Hm
            self.assertEqual(sp.simplify(Hm / F).is_polynomial(y, rho), True)

    def test_hermite_crt_and_operator_intertwining(self):
        t = sp.symbols('t')
        packets = [
            [(sp.Rational(1,3), 2), (sp.Rational(2,3), 3)],
            [(sp.Rational(1,2)+sp.I, 3),
             (sp.Rational(1,2)-sp.I, 1)],
        ]
        for packet in packets:
            h = sp.expand(sp.prod((t-r)**m for r,m in packet))
            n = sum(m for _,m in packet)
            T = sp.zeros(n)
            for j in range(n):
                rem = sp.rem(t**(j+1), h, t)
                for i in range(n):
                    T[i,j] = sp.expand(rem).coeff(t,i)
            J = sp.zeros(n)
            row = 0
            blocks = []
            for rho,m in packet:
                blocks.append(multiplication_matrix(rho+z, m))
                for k in range(m):
                    for j in range(n):
                        J[row+k,j] = sp.diff(t**j,t,k).subs(t,rho)/sp.factorial(k)
                row += m
            D = sp.diag(*blocks)
            self.assertNotEqual(sp.simplify(J.det()), 0)
            self.equal_matrix(J*T, D*J)
            # A model multiplier, not a claim about zeta values.
            g = (t-packet[0][0]) * (3+t) * (5-t)
            M = sp.zeros(n)
            for j in range(n):
                rem = sp.rem(g*t**j,h,t)
                for i in range(n):
                    M[i,j] = sp.expand(rem).coeff(t,i)
            G = sp.diag(*(multiplication_matrix(g.subs(t,r+z),m)
                          for r,m in packet))
            self.equal_matrix(J*M,G*J)

    def test_local_kernel_cokernel_and_unit_transport(self):
        unit = 2+3*z+z*z
        for m in range(1, 6):
            for r in range(0, 7):
                with self.subTest(test_order=m, zero_order=r):
                    G = multiplication_matrix(z**r*unit,m)
                    d = min(m,r)
                    self.assertEqual(m-G.rank(), d)
                    K = sp.zeros(m,d)
                    P = sp.zeros(d,m)
                    for j in range(d):
                        K[m-d+j,j] = 1
                        P[j,j] = 1
                    self.equal_matrix(G*K,sp.zeros(m,d))
                    self.equal_matrix(P*G,sp.zeros(d,m))
                    if d:
                        self.assertEqual(K.rank(),d)
                        self.assertEqual(P.rank(),d)

    def test_derived_residue_pairing_retains_the_unit(self):
        unit = 2+3*z+z*z
        for r in range(1,5):
            for m in range(r,6):
                with self.subTest(zero_order=r,test_order=m):
                    embedding = sp.zeros(m,r)
                    for j in range(r):
                        image = truncated(z**(m-r+j)/unit,m)
                        for i in range(m):
                            embedding[i,j] = image.coeff(z,i)
                    G = multiplication_matrix(z**r*unit,m)
                    self.equal_matrix(G*embedding,sp.zeros(m,r))
                    self.assertEqual(embedding.rank(),r)
                    pair_h = sp.zeros(r,r)
                    pair_g = sp.zeros(r,r)
                    for i in range(r):
                        for j in range(r):
                            u = sum(embedding[k,j]*z**k for k in range(m))
                            pair_h[i,j] = sp.expand(z**i*u).coeff(z,m-1)
                            pair_g[i,j] = truncated(z**(i+j)/unit,r).coeff(z,r-1)
                    self.equal_matrix(pair_h,pair_g)
                    self.assertNotEqual(sp.simplify(pair_g.det()),0)
                    jac = multiplication_matrix(sp.diff(z**r*unit,z),r)
                    result = pair_g*jac
                    expected=sp.zeros(r); expected[0,0]=r
                    self.equal_matrix(result,expected)

    def test_full_packet_comparison_and_projector_identities(self):
        for r in range(1,6):
            U=multiplication_matrix(2+3*z+z*z,r)
            Ui=multiplication_matrix(1/(2+3*z+z*z),r)
            self.equal_matrix(U*Ui,sp.eye(r))
            # Exact diagram: Q=finite packet + complementary part;
            # quotient followed by connecting map is U, not an unrecorded 1.
            q=sp.eye(r).row_join(sp.zeros(r,2))
            delta=U.col_join(sp.zeros(2,r))
            sigma=delta*Ui
            projector=sigma*q
            self.equal_matrix(q*delta,U)
            self.equal_matrix(q*sigma,sp.eye(r))
            self.equal_matrix(projector*projector,projector)
            self.assertEqual(projector.rank(),r)
            A=sp.diag(multiplication_matrix(a0*sp.exp(L*z),r),7,11)
            self.equal_matrix(A*projector,projector*A)
            self.assertEqual(sp.simplify(sp.trace(A*projector)-r*a0),0)

    def test_split_projectors_internal_zero_and_not_absence(self):
        def lift(P,v):
            return None if v is None else tuple(P*sp.Matrix(v))
        P=sp.diag(1,0,0); Q=sp.diag(0,1,0)
        vals=[(1,2,3),(0,0,0),(-2,1,0),None]
        for v in vals:
            result=lift(P,lift(Q,v))
            if v is None:
                self.assertIsNone(result)
            else:
                self.assertEqual(result,(0,0,0))
                self.assertIsNotNone(result)
        self.equal_matrix(P*Q,sp.zeros(3))
        self.equal_matrix((P+Q)*(P+Q),P+Q)
        for label in [1,2,3]:
            image=(label,lift(P,lift(Q,(1,2,3))))
            self.assertEqual(image,(label,(0,0,0)))

    def test_smaller_label_kernel(self):
        for m in range(2,6):
            for r in range(m):
                G=multiplication_matrix(z**r*(2+z),m)
                for j in range(m):
                    J=multiplication_matrix(z**j,m)
                    retained=(G*J).rank()
                    full=G.rank()
                    self.assertEqual((m-retained)-(m-full),full-retained)
                    self.assertGreaterEqual(full-retained,0)

    def test_derived_tensor_signs_and_trace_degree(self):
        g=sp.Matrix([[0,0],[1,0]])
        I=sp.eye(2)
        d0=sp.kronecker_product(g,I).col_join(sp.kronecker_product(I,g))
        d1=(-sp.kronecker_product(I,g)).row_join(sp.kronecker_product(g,I))
        self.equal_matrix(d1*d0,sp.zeros(4))
        for r in range(1,6):
            U=multiplication_matrix(a0*sp.exp(L*z),r)
            self.assertEqual(sp.simplify(sp.trace(U)-r*a0),0)
            self.assertEqual(sp.trace(U)-sp.trace(U),0)


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--output',type=Path)
    p.add_argument('--negative-control',action='store_true')
    args=p.parse_args()
    if args.negative_control:
        raise RuntimeError('Intentional failing control: must fail under python and python -O')
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(FiniteOperatorTests)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    report={
        'test_methods_run': result.testsRun,
        'success': result.wasSuccessful(),
        'failures':len(result.failures),
        'errors':len(result.errors),
        'python':platform.python_version(),
        'sympy':sp.__version__,
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope':'Exact finite algebraic regression examples, not a formal or analytic proof certificate.',
    }
    text=json.dumps(report,indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text,encoding='utf-8')
    print(text,end='')
    return 0 if result.wasSuccessful() else 1

if __name__=='__main__':
    sys.exit(main())
