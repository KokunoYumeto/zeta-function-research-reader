#!/usr/bin/env python3
"""Exact rational calibrations, not arithmetic zero or analytic certificates."""
from __future__ import annotations
import argparse
import itertools as it
import json
import math
import unittest
from fractions import Fraction as Q
from pathlib import Path


def matrix(rows):
    return [[Q(x) for x in row] for row in rows]

def eye(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]

def zero(n, m=None):
    return [[Q(0) for _ in range(n if m is None else m)] for _ in range(n)]

def tr(a):
    return sum(a[i][i] for i in range(len(a)))

def tp(a):
    return [list(x) for x in zip(*a)]

def add(a, b):
    return [[x+y for x,y in zip(ar,br)] for ar,br in zip(a,b)]

def scale(c, a):
    return [[Q(c)*x for x in row] for row in a]

def sub(a,b):
    return add(a,scale(-1,b))

def mul(a,b):
    if len(a[0]) != len(b):
        raise ValueError('incompatible matrix shapes')
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]

def inv(a):
    n=len(a)
    x=[ar[:] + er for ar,er in zip(a,eye(n))]
    for j in range(n):
        k=next((k for k in range(j,n) if x[k][j]), None)
        if k is None:
            raise ValueError('singular matrix')
        x[j],x[k]=x[k],x[j]
        p=x[j][j]
        x[j]=[v/p for v in x[j]]
        for k in range(n):
            if k != j:
                c=x[k][j]
                x[k]=[u-c*v for u,v in zip(x[k],x[j])]
    return [row[n:] for row in x]

def det(a):
    n=len(a)
    if n == 0:
        return Q(1)
    return sum(((-1)**j)*a[0][j]*det([r[:j]+r[j+1:] for r in a[1:]]) for j in range(n))

def sign(p):
    return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))

def hs(a):
    return tr(mul(tp(a),a))

def control(a,g,w):
    return sub(add(mul(tp(a),g),mul(g,a)),scale(w,g))

class TraceModels(unittest.TestCase):
    def test_01_projection_overlap_and_slack(self):
        p=scale(Q(1,25),matrix([[9,12,0],[12,16,0],[0,0,0]]))
        f=matrix([[1,0,0],[0,0,0],[0,0,0]])
        g=matrix([[0,0,0],[0,0,0],[0,0,1]])
        self.assertEqual(mul(p,p),p)
        for e in [Q(1),Q(3,2),Q(7)]:
            h=scale(e,sub(f,g))
            val=tr(mul(p,h))
            self.assertGreaterEqual(val,-e)
            self.assertLessEqual(val,e)
            self.assertEqual(val,e*(1-hs(mul(f,sub(eye(3),p)))-hs(mul(g,p))))
        self.assertEqual(tr(mul(p,f)),hs(mul(f,p)))

    def test_02_oblique_spectral_projection(self):
        t=matrix([[1,0,1],[0,1,2],[0,0,1]])
        ti=inv(t)
        a=mul(mul(t,matrix([[2,0,0],[0,-1,0],[0,0,Q(1,2)]])),ti)
        p=matrix([[1,0,0],[0,1,0],[0,0,0]])
        q=mul(mul(t,p),ti)
        self.assertNotEqual(p,q)
        self.assertNotEqual(mul(p,a),mul(a,p))
        self.assertEqual(mul(a,q),mul(q,a))
        self.assertEqual(mul(q,p),p)
        self.assertEqual(mul(p,q),q)
        self.assertEqual(mul(sub(p,q),sub(p,q)),zero(3))
        self.assertEqual(tr(mul(p,a)),tr(mul(q,a)))
        self.assertEqual(tr(mul(p,a)),1)

    def test_03_constructed_control_projections(self):
        u=matrix([[1,0],[0,1],[0,0]])
        v=matrix([[0,2,0],[2,0,0]])
        h=mul(u,v); c=mul(v,u); e=Q(2)
        self.assertEqual(tr(c),0)
        self.assertEqual(det(c),-e*e)
        self.assertEqual(mul(mul(h,h),h),scale(e*e,h))
        self.assertEqual(tr(mul(h,h)),2*e*e)
        fp=scale(1/(2*e*e),add(mul(h,h),scale(e,h)))
        fm=scale(1/(2*e*e),sub(mul(h,h),scale(e,h)))
        for f in [fp,fm]:
            self.assertEqual(mul(f,f),f)
            self.assertEqual(tp(f),f)
            self.assertEqual(tr(f),1)
        self.assertEqual(mul(fp,fm),zero(3))
        self.assertEqual(scale(e,sub(fp,fm)),h)

    def test_04_original_gram_and_inclusion(self):
        t=matrix([[2,1,0],[0,3,1],[0,0,Q(1,2)]])
        ti=inv(t); g=mul(tp(t),t)
        a0=matrix([[Q(3,2),0,0],[0,Q(1,2),0],[0,0,Q(-1,2)]])
        h0=control(a0,eye(3),1)
        a=mul(mul(ti,a0),t); h=mul(mul(ti,h0),t)
        b0=matrix([[1,0],[0,1],[0,0]])
        l0=tp(b0); b=mul(ti,b0); l=mul(l0,t); p=mul(b,l)
        self.assertEqual(mul(l,b),eye(2))
        self.assertEqual(mul(tp(p),g),mul(g,p))
        self.assertEqual(mul(g,h),control(a,g,1))
        self.assertEqual(tr(mul(p,h)),2)
        self.assertEqual(mul(mul(tp(ti),control(a,g,1)),ti),h0)
        self.assertEqual(mul(mul(tp(b),g),b),eye(2))
        self.assertEqual(tr(mul(p,h)),2*tr(mul(mul(l,a),b))-2)

    def test_05_zero_control_does_not_remove_jordan_action(self):
        h=zero(3)
        self.assertEqual(hs(h),0)
        a=matrix([[Q(1,2),2,0],[0,Q(1,2),0],[0,0,Q(1,2)]])
        c=control(a,eye(3),1)
        self.assertEqual(c,matrix([[0,2,0],[2,0,0],[0,0,0]]))
        p=matrix([[1,0,0],[0,0,0],[0,0,0]])
        self.assertEqual(tr(mul(p,c)),0)
        self.assertNotEqual(c,h)
        nonhermitian=matrix([[0,1],[0,0]])
        self.assertEqual(tr(mul(nonhermitian,nonhermitian)),0)
        self.assertNotEqual(nonhermitian,zero(2))
        self.assertNotEqual(tp(nonhermitian),nonhermitian)

    def test_06_exterior_factorial_original_gram(self):
        t=matrix([[2,1,0],[0,1,1],[0,0,3]])
        g=mul(tp(t),t)
        for p in [1,2,3]:
            wedges=list(it.combinations(range(3),p))
            tensors=list(it.product(range(3),repeat=p))
            alt=zero(len(tensors),len(wedges)); rows={a:i for i,a in enumerate(tensors)}
            for j,w in enumerate(wedges):
                for perm in it.permutations(range(p)):
                    alt[rows[tuple(w[i] for i in perm)]][j]+=sign(perm)
            gt=[[math.prod(g[a[i]][b[i]] for i in range(p)) for b in tensors] for a in tensors]
            gw=[[det([[g[i][j] for j in wj] for i in wi]) for wj in wedges] for wi in wedges]
            self.assertEqual(mul(mul(tp(alt),gt),alt),scale(math.factorial(p),gw))

    def test_07_exterior_allowance_and_both_signs(self):
        e=Q(5,3)
        for n in range(2,9):
            vals=[e]+[Q(0)]*(n-2)+[-e]
            for p in range(n+1):
                sums=[sum(vals[j] for j in comb) for comb in it.combinations(range(n),p)]
                self.assertTrue(all(-e<=v<=e for v in sums))
                if p == n:
                    self.assertEqual(sums,[0])
        for k in range(1,7):
            for p in range(1,6):
                for perm in it.permutations(range(p)):
                    s=sign(perm)
                    self.assertEqual(s**(k+1)*s**k,s)
                for j in range(p):
                    self.assertEqual((-1)**(k*j)*(-1)**(k*j),1)

    def test_08_full_jet_monodromy_filtration(self):
        for ell in range(1,10):
            weights=[ell-1-2*a for a in range(ell)]
            for j in range(-ell-1,ell+2):
                for a,w in enumerate(weights):
                    if w<=j and a+1<ell:
                        self.assertLessEqual(weights[a+1],j-2)
            for j in range(ell+2):
                src=[a for a,w in enumerate(weights) if w==j]
                dst=[a for a,w in enumerate(weights) if w==-j]
                self.assertEqual([a+j for a in src],dst)
            for a in range(ell):
                self.assertEqual(weights[a]+weights[ell-1-a],0)
                self.assertEqual(a+ell-1-a,ell-1)

    def test_09_quartet_multiplicity_and_scale(self):
        for k in range(1,21):
            possible=set()
            for a in range(k+1):
                for b in range(k+1):
                    t=max(0,a+b-k)
                    occ=[t,a-t,b-t,k-a-b+t]
                    self.assertTrue(all(v>=0 for v in occ))
                    self.assertEqual(sum(occ),k)
                    possible.add((2*a-k,2*b-k))
            self.assertEqual(len(possible),(k+1)**2)
            for m in range(1,5):
                ell=1+k*(m-1); d=ell*(k+1)**2
                excess=2*ell*sum(a for a,b in possible if a>0)
                self.assertEqual(excess,2*ell*(k+1)*((k+1)**2//4))
                self.assertGreaterEqual(excess,Q(k*d,2))

    def test_10_filtration_gram_schur_product(self):
        t=matrix([[2,1,3],[0,3,2],[0,0,5]])
        g=mul(tp(t),t)
        # Successive induced quotient metrics, not restrictions to a chosen complement.
        pivot=g[0][0]
        s=[[g[i][j]-g[i][0]*g[0][j]/pivot for j in [1,2]] for i in [1,2]]
        final=s[1][1]-s[1][0]*s[0][1]/s[0][0]
        self.assertGreater(pivot,0); self.assertGreater(s[0][0],0); self.assertGreater(final,0)
        self.assertEqual(det(g),pivot*s[0][0]*final)

class NegativeControl(unittest.TestCase):
    def runTest(self):
        self.assertEqual(1,2,'intentional negative control')

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--json',type=Path)
    p.add_argument('--self-test-failure',action='store_true')
    args=p.parse_args()
    suite=unittest.TestSuite([NegativeControl()]) if args.self_test_failure else unittest.defaultTestLoader.loadTestsFromTestCase(TraceModels)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    receipt={'tests_run':result.testsRun,'success':result.wasSuccessful(),
             'failures':len(result.failures),'errors':len(result.errors),
             'scope':'Exact rational finite calibration; no actual zero input or analytic estimate.'}
    text=json.dumps(receipt,sort_keys=True)+'\n'
    if args.json:
        args.json.write_text(text,encoding='utf-8')
    print(text,end='')
    raise SystemExit(0 if result.wasSuccessful() else 1)

if __name__=='__main__':
    main()
