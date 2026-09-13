#!/usr/bin/env python3
"""Bounded exact checks for spectral-sum descent. Not an analytic or RH certificate."""
import argparse
from itertools import product, combinations_with_replacement
import json
from pathlib import Path
import sys
import unittest
import sympy as s

x,y,S,r,z,t=s.symbols('x y S r z t')

def equal(a,b):
    return s.expand(a-b)==0

def parts(h):
    hp=s.expand(h.subs(t,(S+r)/2)); hm=s.expand(h.subs(t,(S-r)/2))
    def even(P):
        out=0
        for (a,b),c in s.Poly(s.cancel(P),S,r).terms():
            if b%2: raise ValueError('odd term in even polynomial')
            out+=c*S**a*z**(b//2)
        return s.expand(out)
    return even((hp+hm)/2),even((hp-hm)/(2*r))

def local(ms):
    basis=list(product(*(range(m) for m in ms)))
    index={a:i for i,a in enumerate(basis)}; n=len(basis); D=sum(m-1 for m in ms)
    N=s.zeros(n); F=s.zeros(n); H=s.zeros(n); G=s.zeros(n)
    for a,j in index.items():
        H[j,j]=2*sum(a)-D
        G[j,j]=s.prod(s.factorial(q)*s.factorial(m-1)/s.factorial(m-1-q) for q,m in zip(a,ms))
        for i,m in enumerate(ms):
            if a[i]+1<m:
                b=list(a);b[i]+=1;N[index[tuple(b)],j]+=1
            if a[i]>0:
                b=list(a);b[i]-=1;F[index[tuple(b)],j]+=a[i]*(m-a[i])
    return basis,N,F,H,G

class Core(unittest.TestCase):
    def mat(self,a,b):
        self.assertEqual(s.Matrix(a-b).applyfunc(s.simplify),s.zeros(*a.shape))

    def test_1_invariant_generators(self):
        for h in [t-2,(t-s.Rational(1,2))**2,t**3-2*t+7,t**4+t+1]:
            E,O=parts(h)
            self.assertTrue(equal(E.subs(z,r*r)+r*O.subs(z,r*r),h.subs(t,(S+r)/2)))
            self.assertTrue(equal(E.subs(z,r*r)-r*O.subs(z,r*r),h.subs(t,(S-r)/2)))
        for d in range(1,9):
            p=sum(t**(i+j) for i,j in combinations_with_replacement(range(d),2))
            self.assertTrue(equal(p*(1-t)*(1-t*t),(1-t**d)*(1-t**(d+1))))

    def test_2_original_primitive_signs(self):
        h=t**3-2*t+1;E,O=parts(h);a=S*S+3*z+1;b=S-2
        p1=(a.subs(z,r*r)+r*b)/2;p2=(a.subs(z,r*r)-r*b)/2
        original=h.subs(t,(S+r)/2)*p1-h.subs(t,(S-r)/2)*(-p2)
        self.assertTrue(equal(original,(E*a+z*O*b).subs(z,r*r)))

    def test_3_gaussian_fibre_mass_and_signs(self):
        M=s.Matrix(3,3,lambda a,b:(-1)**(a+b)*2**(a+b)*s.factorial2(2*(a+b)-1))
        self.mat(M,s.Matrix([[1,-2,12],[-2,12,-120],[12,-120,1680]]))
        T=s.Matrix([[1,2,12],[0,1,12],[0,0,1]])
        self.mat(T.T*M*T,s.diag(1,8,384))
        self.assertEqual(abs(s.Matrix([[s.Rational(1,2),s.Rational(1,2)],[s.Rational(1,2),-s.Rational(1,2)]]).det()),s.Rational(1,2))
        self.assertEqual(s.sqrt(s.pi)*2*s.sqrt(s.pi),2*s.pi)

    def test_4_raising_lowering_and_all_ordered_lengths(self):
        for ms in [(2,2),(2,3),(3,3),(2,2,2),(3,2,2)]:
            b,N,F,H,G=local(ms);D=sum(m-1 for m in ms)
            self.mat(N*F-F*N,H);self.mat(H*N-N*H,2*N);self.mat(N.T*G,G*F)
            c=[sum(sum(a)==j for a in b) for j in range(D+1)]
            ranks=[(N**j).rank() for j in range(D+3)]
            actual={j:ranks[j-1]-2*ranks[j]+ranks[j+1] for j in range(1,D+2) if ranks[j-1]-2*ranks[j]+ranks[j+1]}
            expected={D-2*j+1:c[j]-(c[j-1] if j else 0) for j in range(D//2+1) if c[j]-(c[j-1] if j else 0)}
            self.assertEqual(actual,expected)

    def test_5_symmetric_order_three_jets(self):
        b,N,F,H,G=local((3,3));orbits=list(combinations_with_replacement(range(3),2))
        I=s.zeros(9,6)
        for i,a in enumerate(b):I[i,orbits.index(tuple(sorted(a)))]=1
        L=(I.T*I).inv()*I.T;A=L*N*I
        self.mat(N*I,I*A)
        self.assertEqual([(A**j).rank() for j in range(6)],[6,4,3,2,1,0])
        p=s.Matrix([1 if a in [(2,0),(0,2)] else -1 if a==(1,1) else 0 for a in b])
        self.mat(N*p,s.zeros(9,1))
        self.assertNotEqual(p,s.zeros(9,1))

    def test_6_free_resolution(self):
        A=s.Matrix([[s.Rational(1,3),1],[0,s.Rational(1,3)]])
        cs=[s.Matrix([j+1,2-j]) for j in range(5)]
        f=sum((S**j*cs[j] for j in range(5)),s.zeros(2,1))
        val=sum((A**j*cs[j] for j in range(5)),s.zeros(2,1))
        q=sum((sum((S**(j-1-i)*A**i*cs[j] for i in range(j)),s.zeros(2,1)) for j in range(1,5)),s.zeros(2,1))
        self.mat(f-val,(S*s.eye(2)-A)*q)

    def test_7_resolvent_duality_and_trace(self):
        rho=s.Rational(2,7);A=s.Matrix([[rho,1],[0,rho]])
        R=(S*s.eye(2)-A).inv();chi=(S*s.eye(2)-A).det()
        self.assertEqual(s.cancel(s.trace(R)-s.diff(chi,S)/chi),0)
        row=s.Matrix([[S*S+1,2*S]]);v=s.Matrix([1,3])
        actual=s.residue((row*R*v)[0],S,rho)
        expected=(s.Matrix([[1,0]])*v+s.Matrix([[0,2]])*A*v+s.Matrix([[1,0]])*A*A*v)[0]
        self.assertEqual(s.simplify(actual-expected),0)
        self.assertEqual(s.cancel(R[0,1]-1/(S-rho)**2),0)

    def test_8_external_and_supported_zero(self):
        # None is tau; a tuple is a supported coefficient vector, including zero.
        def q(a):return None if a is None else a[:2]
        self.assertIsNone(q(None));self.assertEqual(q((0,0,1)),(0,0))
        self.assertNotEqual(q((0,0,1)),None)
        self.assertNotEqual((0,0,1),(0,0,0))

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--json',type=Path);p.add_argument('--self-test-failure',action='store_true');a=p.parse_args()
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(Core)
    if a.self_test_failure:
        class Failure(unittest.TestCase):
            def runTest(self):self.assertEqual(1,0,'deliberately false guard')
        suite.addTest(Failure())
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    rec={'tests_run':result.testsRun,'success':result.wasSuccessful(),'failures':len(result.failures),'errors':len(result.errors),'sympy':s.__version__,'scope':'bounded exact finite regressions; no analytic or Lean certificate'}
    if a.json:a.json.write_text(json.dumps(rec,indent=2)+'\n')
    print(json.dumps(rec,sort_keys=True));return 0 if result.wasSuccessful() else 1
if __name__=='__main__':sys.exit(main())
