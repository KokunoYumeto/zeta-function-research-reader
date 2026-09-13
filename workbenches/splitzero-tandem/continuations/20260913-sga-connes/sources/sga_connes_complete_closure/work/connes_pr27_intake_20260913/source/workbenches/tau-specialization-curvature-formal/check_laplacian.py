#!/usr/bin/env python3
"""Exact symbolic source regressions, not sampled zeta zeros or analytic estimates."""
from __future__ import annotations
import argparse
import json
import re
import sys
import unittest
from pathlib import Path
import sympy as s
from check_specialization import equal, fixture, require

NAMES='adjoint_defect energy_identity symmetric_of_zero_defect constituent jet_expansion intertwining_power injective_power nilpotent_image_zero shifted_nilpotent_image_zero'.split()
EXPECTED={'SplitZero.LaplacianControl.'+n for n in NAMES}
ALLOWED={'propext','Classical.choice','Quot.sound'}

def audit(text: str) -> dict:
    found={}
    for name,raw in re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]",text):
        require(name not in found,'duplicate audit target')
        axioms={x.strip() for x in raw.split(',') if x.strip()}
        require(axioms<=ALLOWED,'forbidden transitive axiom')
        found[name]=sorted(axioms)
    require(set(found)==EXPECTED,'missing or extra audit targets')
    require('error:' not in text.lower(),'Lean error in audit')
    return found

class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        u=s.Symbol('u'); cls.source=fixture(u**3+u,5)

    def test_01_original_gaussian_is_laplacian_image(self):
        x=s.Symbol('x',positive=True); g=s.exp(-s.pi*x*x); D=lambda f:-x*s.diff(f,x)
        self.assertTrue(equal(D(D(g))-D(g),(4*s.pi**2*x**4-6*s.pi*x*x)*g))

    def test_02_retained_mellin_half_coefficient(self):
        z=s.Symbol('z'); mellin=s.Rational(1,2)*s.pi**(-z/2)*s.gamma(z/2); phi=z*(z-1)*mellin
        self.assertTrue(equal(phi.subs(z,s.Rational(1,2)),-s.pi**(-s.Rational(1,4))*s.gamma(s.Rational(1,4))/8))
        xi=s.Rational(1,2)*z*(z-1)*s.pi**(-z/2)*s.gamma(z/2)*s.Symbol('zeta')
        self.assertTrue(equal(2*s.Symbol('zeta')*phi,2*xi))

    def test_03_original_metric_laplacian_defects(self):
        A,G=(self.source[n] for n in ['A','G']); W=A.conjugate().T*G+G*A-2*G; L=A*A-2*A
        self.assertTrue(equal(L.conjugate().T*G-G*L,A.conjugate().T*W-W*A))
        self.assertTrue(equal(G*L,W*A-A.conjugate().T*G*A)); self.assertLessEqual(W.rank(),2)

    def test_04_centered_energy_keeps_cross_term(self):
        A,G=(self.source[n] for n in ['A','G']); B=A-s.eye(3)
        W=A.conjugate().T*G+G*A-2*G; L=A*A-2*A
        self.assertTrue(equal(G*L,W*B-B.conjugate().T*G*B-G)); self.assertNotEqual(W*B,s.zeros(3))

    def test_05_full_jordan_laplacian(self):
        N=s.Matrix([[0,1,0],[0,0,1],[0,0,0]]); rho=s.Rational(1,2)+2*s.I
        A=rho*s.eye(3)+N; L=A*A-A; scalar=rho*(rho-1)
        self.assertTrue(equal(L,scalar*s.eye(3)+(2*rho-1)*N+N*N))
        self.assertEqual((L-scalar*s.eye(3)).rank(),2)
        self.assertTrue(equal((L-scalar*s.eye(3))**3,s.zeros(3)))

    def test_06_finite_comparison_kernel_and_action(self):
        z,e=s.symbols('z e'); rc=s.Rational(1,2)+2*s.I; ro=s.Rational(2,3)+3*s.I
        h=s.expand((z-rc)**2*(z-ro)**3)
        A=s.Matrix.hstack(*[s.Matrix([s.Poly(s.rem(z**(j+1),h,z),z).nth(i) for i in range(5)]) for j in range(5)])
        J=s.Matrix([[s.expand((rc+e)**j).coeff(e,i) for j in range(5)] for i in range(2)])
        B=s.Matrix([[rc,0],[1,rc]])
        self.assertTrue(equal(J*A,B*J)); self.assertEqual(5-J.rank(),3)
        K=s.Matrix.hstack(*[s.Matrix([s.expand((z-rc)**2*z**j).coeff(z,i) for i in range(5)]) for j in range(3)])
        self.assertEqual(K.rank(),3); self.assertTrue(equal(J*K,s.zeros(2,3)))
        LK=(A*A-A)*K; F=K[:3,:].inv()*LK[:3,:]
        self.assertTrue(equal(LK,K*F))

    def test_07_critical_jet_phase_and_factorial(self):
        z,t=s.symbols('z t'); gamma=s.Integer(2); rho=s.Rational(1,2)+s.I*gamma; f=3+2*z-z**3+s.I*z**5
        for j in range(5):
            lhs=s.I**(-j)*s.diff(f.subs(z,s.Rational(1,2)+s.I*t),t,j).subs(t,gamma)/s.factorial(j)
            self.assertTrue(equal(lhs,s.diff(f,z,j).subs(z,rho)/s.factorial(j)))

    def test_08_zero_mode_renormalized_transfer(self):
        L=s.Symbol('L',positive=True); a=s.Symbol('a'); h=a/s.sqrt(L)
        for n in [2,3,7]:
            self.assertTrue(equal(s.sqrt(n)*h.subs(L,n*L),h)); self.assertTrue(equal(s.sqrt(L)*h,a))
        self.assertTrue(equal(s.diff(h,L),-a/(2*L**s.Rational(3,2))))

    def test_09_exact_audit_acceptance(self):
        text='\n'.join("'%s' depends on axioms: [propext, Classical.choice, Quot.sound]"%n for n in sorted(EXPECTED))
        self.assertEqual(set(audit(text)),EXPECTED)

    def test_10_audit_rejects_mutations(self):
        lines=["'%s' depends on axioms: [propext]"%n for n in sorted(EXPECTED)]
        for text in ['\n'.join(lines[:-1]),'\n'.join(lines+[lines[0]]),'\n'.join(lines).replace('[propext]','[sorryAx]',1),'\n'.join(lines).replace('[propext]','[Lean.ofReduceBool]',1)]:
            with self.assertRaises(AssertionError): audit(text)

def main() -> None:
    parser=argparse.ArgumentParser(); parser.add_argument('--audit',type=Path); parser.add_argument('--negative',action='store_true'); args=parser.parse_args()
    if args.negative: require(False,'intentional Laplacian negative control')
    if args.audit:
        reports=audit(args.audit.read_text(encoding='utf-8')); print(json.dumps({'status':'PASS','targets':len(reports),'reports':reports},sort_keys=True,indent=2)); return
    names=unittest.defaultTestLoader.getTestCaseNames(Tests); result=unittest.TestResult(); unittest.defaultTestLoader.loadTestsFromTestCase(Tests).run(result)
    out={'status':'PASS' if result.wasSuccessful() else 'FAIL','methods':result.testsRun,'tests':names,'failures':[(str(t),x) for t,x in result.failures],'errors':[(str(t),x) for t,x in result.errors],'scope':'exact symbolic source and finite jet identities; no Schwartz closure, heat limit or RH certificate'}
    print(json.dumps(out,sort_keys=True,indent=2)); sys.exit(0 if result.wasSuccessful() else 1)

if __name__=='__main__': main()
