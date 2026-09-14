#!/usr/bin/env python3
"""Exact finite calibrations for the conormal/cyclic depth formulas.

The general theorems are not proved by these tests. No zero location, analytic
integral, floating-point value or external private file is used.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from itertools import product
import json
from math import factorial
from pathlib import Path
import unittest


def survivors(m, r):
    if not m or r < 1 or min(m) < 1:
        raise ValueError('positive multiplicities, degree and depth are required')
    return [a for a in product(*(range(r*v) for v in m))
            if sum(x//v for x,v in zip(a,m)) < r]


def multiply_sum(p, m, r):
    out = {}
    for a,c in p.items():
        for i in range(len(m)):
            b = list(a); b[i] += 1; b = tuple(b)
            if sum(x//v for x,v in zip(b,m)) < r:
                out[b] = out.get(b,0) + c
    return {a:c for a,c in out.items() if c}


def actual_order(m, r):
    p = {tuple(0 for _ in m):1}
    n = 0
    limit = sum(r*v for v in m) + 1
    while p:
        p = multiply_sum(p,m,r)
        n += 1
        if n > limit:
            raise RuntimeError('nilpotency did not terminate')
    return n


def predicted_order(m, r):
    return 1 + sum(v-1 for v in m) + (r-1)*max(m)


def orders(packet, k, r):
    out = {}
    for tup in product(packet,repeat=k):
        value = sum(a for a,_ in tup)
        ell = predicted_order(tuple(m for _,m in tup),r)
        out[value] = max(out.get(value,0),ell)
    return out


def trim(p):
    p = list(p)
    while len(p)>1 and p[-1]==0: p.pop()
    return p


def pmul(p,q):
    out=[Fraction(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): out[i+j] += a*b
    return trim(out)


def annihilator(packet,k,r):
    p=[Fraction(1)]
    for root,ell in sorted(orders(packet,k,r).items()):
        for _ in range(ell): p=pmul(p,[-Fraction(root),Fraction(1)])
    return p


def derivative(p):
    return trim([Fraction(i)*p[i] for i in range(1,len(p))] or [Fraction(0)])


def remainder(p,q):
    p=trim([Fraction(x) for x in p]); q=trim(q)
    if q==[0]: raise ZeroDivisionError('zero polynomial')
    while len(p)>=len(q) and p!=[0]:
        shift=len(p)-len(q); a=p[-1]/q[-1]
        for i,b in enumerate(q): p[i+shift] -= a*b
        p=trim(p)
    return p


class ExactDepth(unittest.TestCase):
    def test_01_degree_bound_and_attainment(self):
        for k in range(1,4):
            for m in product(range(1,4),repeat=k):
                for r in range(1,4):
                    basis=survivors(m,r)
                    self.assertEqual(max(map(sum,basis)),predicted_order(m,r)-1)

    def test_02_actual_nilpotent_sum(self):
        for k in range(1,4):
            for m in product(range(1,4),repeat=k):
                for r in range(1,4):
                    self.assertEqual(actual_order(m,r),predicted_order(m,r))

    def test_03_top_coefficient_is_retained(self):
        for m in [(1,1),(2,2),(2,3),(3,1,2)]:
            for r in range(1,4):
                j=m.index(max(m))
                a=tuple(v-1+(r-1)*v*(i==j) for i,v in enumerate(m))
                p={tuple(0 for _ in m):1}
                for _ in range(sum(a)): p=multiply_sum(p,m,r)
                coef=factorial(sum(a))
                for v in a: coef//=factorial(v)
                self.assertEqual(p[a],coef)
                self.assertGreater(coef,0)

    def test_04_collided_maximum_can_change_tuple(self):
        packet=[(0,5),(1,4),(2,1)]
        self.assertEqual([orders(packet,2,r)[2] for r in range(1,6)], [7,11,15,20,25])

    def test_05_not_the_power_of_first_relation(self):
        packet=[(0,2)]
        for r in range(1,5):
            self.assertEqual(orders(packet,2,r)[0],2*r+1)
            self.assertLessEqual(2*r+1,3*r)
            if r>1: self.assertNotEqual(2*r+1,3*r)

    def test_06_derivative_and_transition_divisibility(self):
        for packet in [[(0,2)],[(0,1),(1,2)],[(0,2),(1,1),(2,2)]]:
            for k in [1,2,3]:
                for r in [1,2,3]:
                    p=annihilator(packet,k,r)
                    q=annihilator(packet,k,r+1)
                    self.assertEqual(remainder(q,p),[0])
                    self.assertEqual(remainder(derivative(q),p),[0])

    def test_07_empty_packet_is_the_zero_arithmetic_quotient(self):
        for k in [1,2,3]:
            for r in [1,2,3]:
                self.assertEqual(annihilator([],k,r),[1])
                self.assertEqual(remainder([1,2,3],[1]),[0])
        tau=object()
        def split_zero(x): return tau if x is tau else ('supported',0)
        self.assertIs(split_zero(tau),tau)
        self.assertEqual(split_zero(('supported',17)),('supported',0))
        self.assertIsNot(split_zero(('supported',17)),tau)

    def test_08_dimension_of_local_power_quotient(self):
        for m in [(1,),(2,),(2,3),(2,1,3)]:
            for r in [1,2,3,4]:
                k=len(m); d=1
                for v in m: d*=v
                expected=d*factorial(k+r-1)//(factorial(k)*factorial(r-1))
                self.assertEqual(len(survivors(m,r)),expected)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json',type=Path)
    parser.add_argument('--self-test-failure',action='store_true')
    args=parser.parse_args()
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(ExactDepth)
    if args.self_test_failure:
        class DeliberateFailure(unittest.TestCase):
            def runTest(self): self.assertEqual(1,2,'intentional negative control')
        suite.addTest(DeliberateFailure())
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    record={'tests_run':result.testsRun,'errors':len(result.errors),'failures':len(result.failures),
            'success':result.wasSuccessful(),'scope':'Exact finite local monomial and polynomial calibrations, not an analytic certificate'}
    if args.json: args.json.write_text(json.dumps(record,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(record,sort_keys=True))
    return 0 if result.wasSuccessful() else 1

if __name__=='__main__':
    raise SystemExit(main())
