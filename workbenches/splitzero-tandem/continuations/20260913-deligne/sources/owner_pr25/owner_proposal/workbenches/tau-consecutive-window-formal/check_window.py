#!/usr/bin/env python3
"""Finite algebra checks; not zeta data or an analytic norm certificate."""
import argparse
from fractions import Fraction as F
from functools import reduce
from operator import mul
from pathlib import Path
import re
import unittest

NAMES = ('exact_step', 'radius_step', 'exact_product', 'product_bound',
         'lower_bound_propagates', 'first_radius_step',
         'norm_bound_forces_volume', 'log_volume_forcing', 'doubling_from_envelope',
         'canonical_norm_volume')
ALLOWED = {'propext', 'Classical.choice', 'Quot.sound'}

def audit(text):
    found = {}
    pattern = r"'([^']+)' (?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)"
    for match in re.finditer(pattern, text, re.S):
        name = match.group(1)
        if name in found:
            raise ValueError('duplicate report')
        axioms = {s.strip() for s in (match.group(2) or '').split(',') if s.strip()}
        if not axioms <= ALLOWED:
            raise ValueError('unexpected axiom: ' + repr(axioms))
        found[name] = sorted(axioms)
    expected = {'SplitZero.ConsecutiveWindow.' + n for n in NAMES}
    if set(found) != expected:
        raise ValueError('wrong target set: ' + repr(set(found) ^ expected))
    return found

def product(xs):
    return reduce(mul, xs, F(1))

class Tests(unittest.TestCase):
    def test_exact_product(self):
        for r in range(1, 13):
            d = [F(j+1, j+3) for j in range(r+1)]
            w = [F((j+2)**3, 7) for j in range(r+1)]
            v = [F(13)]
            for j in range(r):
                v.append(v[-1] * d[j+1])
            f = [(w[j+1]/w[j])*(1-d[j])*(1/d[j+1]-1) for j in range(r)]
            rhs = (w[-1]/w[0])*(v[0]/v[-1])*(1-d[0])*(1-d[-1])
            rhs *= product(1-x for x in d[1:-1])**2
            self.assertEqual(product(f), rhs)
            self.assertLessEqual(product(f), (w[-1]/w[0])*(v[0]/v[-1]))
    def test_mass(self):
        for q in range(1, 6):
            for c in (F(1,7), F(3), F(11)):
                self.assertEqual((F(29)/5)*(F(7)/2), (c*29/(c*5))*(c**q*7/(c**q*2)))
    def test_first_degree(self):
        w, wn, nu, v = F(7), F(14), F(42), F(9)
        vn = v*wn/nu
        e2 = (nu-wn)/w
        self.assertLessEqual(e2*w/v, wn/vn)
    def test_four_threshold(self):
        for q in range(2, 12):
            t = F(3)
            v = lambda j: t**(-2*j)
            r0 = v(q-1)/v(2*q-1)
            r1 = v(q)/v(2*q)
            self.assertEqual(r0, t**(2*q))
            self.assertEqual(r1, t**(2*q))
            self.assertEqual(r0*r1, t**(4*q))
    def test_doubling_identity(self):
        for n in range(1, 10):
            lo, up = F(2,7), F(5,3)
            self.assertEqual((up*2*n)**(4*n), (4*up**2/lo*n)**(2*n)*(lo*n)**(2*n))
    def test_zero_eigenvalue_multiplicity(self):
        # Mass-one Gaussian calibration, not an arithmetic zero packet.
        # Modulo psi=u^3+u, Q3,Q4,Q5 have columns (0,-4,0),(3,0,-7),(0,26,0).
        columns = [[F(0), F(-4), F(0)], [F(3), F(0), F(-7)], [F(0), F(26), F(0)]]
        gram = [[F(1), F(0), F(1)], [F(0), F(1), F(0)], [F(1), F(0), F(3)]]
        omega = [F(6), F(24), F(120)]
        a = [[sum(columns[i][r]*gram[r][s]*columns[j][s]
                  for r in range(3) for s in range(3)) for j in range(3)] for i in range(3)]
        det = lambda m: (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
                         -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
                         +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))
        eigenvalues = [F(0), F(19,4), F(83,10)]
        self.assertEqual(len(eigenvalues), 3)
        self.assertEqual(sum(v == 0 for v in eigenvalues), 1)
        for value in eigenvalues:
            self.assertEqual(det([[a[i][j]-(value*omega[i] if i == j else 0)
                                   for j in range(3)] for i in range(3)]), 0)
        self.assertEqual([sum(columns[j][i]*[13,0,2][j] for j in range(3))
                          for i in range(3)], [0,0,0])
        volume_ratio = det([[F(i == j)+a[i][j]/omega[i] for j in range(3)] for i in range(3)])
        self.assertEqual(volume_ratio, product(1+v for v in eigenvalues))
        self.assertEqual(volume_ratio, F(2139,40))
        self.assertLessEqual(volume_ratio, (1+sum(eigenvalues)/3)**3)
        for k in range(4, 20, 2):
            for multiplicity in range(1, 5):
                q = (1+k*(multiplicity-1))*(k+1)**2
                self.assertEqual(q % 2, 1)
                self.assertEqual((q+1)//2-((q-1)//2), 1)
    def test_audit_valid(self):
        text = '\n'.join("'SplitZero.ConsecutiveWindow.%s' depends on axioms: [propext, Classical.choice, Quot.sound]" % n for n in NAMES)
        self.assertEqual(len(audit(text)), len(NAMES))
    def test_audit_bad(self):
        with self.assertRaises(ValueError):
            audit('')
        text = '\n'.join("'SplitZero.ConsecutiveWindow.%s' depends on axioms: [sorryAx]" % n for n in NAMES)
        with self.assertRaises(ValueError):
            audit(text)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--audit')
    parser.add_argument('--negative', action='store_true')
    args = parser.parse_args()
    if args.negative:
        raise SystemExit('intentional negative control')
    if args.audit:
        reports = audit(Path(args.audit).read_text())
        print('Accepted transitive reports:', len(reports))
    else:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        raise SystemExit(0 if result.wasSuccessful() else 1)
