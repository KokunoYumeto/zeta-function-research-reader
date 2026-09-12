#!/usr/bin/env python3
"""Exact rational source/quotient and scalar checks; not an arithmetic interval certificate."""
from __future__ import annotations
import argparse
import importlib.util
import itertools
import json
import math
import unittest
from fractions import Fraction as Q
from pathlib import Path

p = Path(__file__).resolve().parents[1] / 'tau-exterior-trace-formal' / 'check_trace_models.py'
spec = importlib.util.spec_from_file_location('retained_trace_models', p)
if spec is None or spec.loader is None:
    raise RuntimeError('inherited exact matrix checker is missing')
t = importlib.util.module_from_spec(spec)
spec.loader.exec_module(t)

def energy(a, prev, mid, nxt, phase):
    return a*(1-mid/prev)*(mid/nxt-1)-phase**2

class VolumeModels(unittest.TestCase):
    def test_01_two_losses(self):
        for a,p,m,q,z in itertools.product([Q(0),Q(2),Q(7,3)], [Q(1),Q(3)], [Q(-1),Q(1,2),Q(2)], [Q(1,3),Q(2)], [Q(0),Q(2,5)]):
            rhs=a*(p-q)**2/(4*p*q)-a*(2*m-p-q)**2/(4*p*q)-z*z
            self.assertEqual(energy(a,p,m,q,z),rhs)
            self.assertLessEqual(rhs,a*(p-q)**2/(4*p*q))

    def test_02_equality_conditions(self):
        for p,q in itertools.product([Q(2),Q(5)], [Q(1),Q(3,2)]):
            m=(p+q)/2
            up=3*(p-q)**2/(4*p*q)
            self.assertEqual(energy(Q(3),p,m,q,Q(0)),up)
            self.assertLess(energy(Q(3),p,m,q,Q(1,10)),up)
            self.assertLess(energy(Q(3),p,m+Q(1,10),q,Q(0)),up)

    def test_03_mass_scaling(self):
        for c in [Q(1,10),Q(7),Q(100)]:
            self.assertEqual(energy(Q(5),6*c,4*c,2*c,Q(1,3)),energy(Q(5),Q(6),Q(4),Q(2),Q(1,3)))

    def test_04_trace_forces_volume(self):
        # Exact nonnormal rank-two example: eigenvalue excess 2, allowance 3.
        a=t.matrix([[Q(3,2),Q(5,2)],[0,Q(-1,2)]])
        h=t.control(a,t.eye(2),1)
        self.assertEqual(t.tr(h),0)
        self.assertEqual(t.det(h),-Q(41,4))
        L=Q(2)
        e2=-t.det(h)
        prev,mid,nxt=Q(9),Q(5),Q(1)
        alpha=e2*prev*nxt/((prev-mid)*(mid-nxt))
        self.assertEqual(energy(alpha,prev,mid,nxt,Q(0)),e2)
        self.assertLessEqual(4*prev*nxt*L*L,alpha*(prev-nxt)**2)

    def test_05_constructed_residual_gram(self):
        b=t.matrix([[1,0],[0,1],[1,2],[2,-1]])
        c=t.matrix([[1,2],[3,-1],[2,1],[-1,4]])
        hb=t.mul(t.tp(b),b); invhb=t.inv(hb)
        residual=t.sub(c,t.mul(b,t.mul(invhb,t.mul(t.tp(b),c))))
        self.assertEqual(t.mul(t.tp(b),residual),t.zero(2))
        gram=t.mul(t.tp(residual),residual)
        raw=t.mul(t.tp(c),c)
        schur=t.sub(raw,t.mul(t.mul(t.mul(t.tp(c),b),invhb),t.mul(t.tp(b),c)))
        self.assertEqual(gram,schur)
        full=[cr+br for cr,br in zip(c,b)]
        self.assertEqual(t.det(t.mul(t.tp(full),full)),t.det(hb)*t.det(gram))
        self.assertGreater(t.det(gram),0)

    def test_06_original_observation(self):
        b=t.matrix([[1],[2],[3]])
        c=t.matrix([[2,1],[0,1],[1,4]])
        j=t.matrix([[-2,1,0],[-3,0,1]])
        self.assertEqual(t.mul(j,b),t.zero(2,1))
        r=t.sub(c,t.mul(b,t.mul(t.inv(t.mul(t.tp(b),b)),t.mul(t.tp(b),c))))
        self.assertEqual(t.mul(j,r),t.mul(j,c))

    def test_07_ratio_telescope(self):
        volumes=[Q(1,j+1) for j in range(30)]
        for r in range(1,12):
            product=Q(1)
            for j in range(r):
                product*=volumes[2*j]/volumes[2*j+2]
            self.assertEqual(product,volumes[0]/volumes[2*r])

    def test_08_quartet_dimension_scale(self):
        for k,m in itertools.product(range(1,20),range(1,5)):
            ell=1+k*(m-1); dimension=ell*(k+1)**2
            lower=2*ell*(k+1)*((k+1)**2//4)
            self.assertGreaterEqual(Q(lower,dimension),Q(k,2))
            self.assertEqual(lower,2*ell*(k+1)*sum(2*a-k for a in range(k//2+1,k+1)))

    def test_09_hankel_toda_small_orders(self):
        # The actual scalar Hankel identity on declared finite moment measures.
        atoms=[Q(-2),Q(0),Q(1),Q(3)]
        masses=[Q(2),Q(1),Q(3),Q(5)]
        mu=[sum(w*x**j for x,w in zip(atoms,masses)) for j in range(10)]
        d1=mu[0]; d1p=mu[1]; d1pp=mu[2]
        d2=mu[0]*mu[2]-mu[1]**2
        self.assertEqual(d1*d1pp-d1p*d1p,d2)
        d2p=mu[0]*mu[3]-mu[1]*mu[2]
        d2pp=mu[0]*mu[4]-mu[2]**2
        d3=t.det([[mu[i+j] for j in range(3)] for i in range(3)])
        self.assertEqual(d2*d2pp-d2p*d2p,d3*d1)

    def test_10_empty_relation_dimension(self):
        self.assertEqual(t.det([]),1)
        # h=1: the arithmetic quotient is zero, not the analytic source.
        source=t.matrix([[2,1],[1,3]])
        self.assertEqual(t.det(source)/t.det(source),1)
        self.assertNotEqual(t.det(source),0)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json',type=Path)
    parser.add_argument('--self-test-failure',action='store_true')
    args=parser.parse_args()
    if args.self_test_failure:
        class Negative(unittest.TestCase):
            def runTest(self): self.assertEqual(1,2,'intentional negative control')
        suite=unittest.TestSuite([Negative()])
    else:
        suite=unittest.defaultTestLoader.loadTestsFromTestCase(VolumeModels)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    data={'tests_run':result.testsRun,'success':result.wasSuccessful(),'failures':len(result.failures),'errors':len(result.errors),'scope':'Exact rational finite identities, not analytic or arithmetic interval certification'}
    text=json.dumps(data,sort_keys=True)+'\n'
    if args.json: args.json.write_text(text,encoding='utf-8')
    print(text,end='')
    raise SystemExit(0 if result.wasSuccessful() else 1)
if __name__=='__main__': main()
