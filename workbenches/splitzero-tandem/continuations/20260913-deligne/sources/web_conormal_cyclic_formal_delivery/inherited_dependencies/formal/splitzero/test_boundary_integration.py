#!/usr/bin/env python3
"""Exact finite regression models and negative audit-harness controls.

These tests are not arithmetic theta evaluations and are not Lean certificates.
All numerical fixtures use Fraction or integer arithmetic.
"""
from __future__ import annotations
from fractions import Fraction as Q
import itertools
import json
from pathlib import Path
import tempfile
import unittest

from check_boundary_integration import preflight
from check_derived import audit


def transpose(a):
    return [list(x) for x in zip(*a)]


def mm(a, b):
    bt = transpose(b)
    return [[sum(x*y for x, y in zip(row, col)) for col in bt] for row in a]


def minus(a, b):
    return [[x-y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def gram(a):
    return mm(transpose(a), a)


class BoundaryTests(unittest.TestCase):
    def test_rank_two_from_actual_vectors(self):
        # A single old relation and one new, deliberately unnormalised, vector.
        R = [[0, 0, 0], [1, 2, -1], [2, -1, 3], [1, 4, 2]]
        old = [[2, -3, 1], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        u = [0, 2, 0, 0]
        h = Q(4)
        r = [Q(3), Q(-2), Q(5)]
        s = [Q(x, 2) for x in R[1]]
        boundary = [[old[i][j]-u[i]*r[j] for j in range(3)] for i in range(4)]
        actual = minus([[0]*3 for _ in range(3)],
                       [[x+y for x, y in zip(ar, br)]
                        for ar, br in zip(mm(transpose(R), boundary), mm(transpose(boundary), R))])
        expected = [[h*(s[i]*r[j]+r[i]*s[j]) for j in range(3)] for i in range(3)]
        self.assertEqual(actual, expected)
        cols = [[h*s[i], h*r[i]] for i in range(3)]
        self.assertEqual(mm(cols, [r, s]), expected)
        nxt = [[R[i][j]-u[i]*s[j] for j in range(3)] for i in range(4)]
        self.assertEqual(minus(gram(R), gram(nxt)),
                         [[h*s[i]*s[j] for j in range(3)] for i in range(3)])
        self.assertEqual(mm([u], nxt), [[0, 0, 0]])

    def test_orthogonal_minimum_is_not_arbitrary_metric(self):
        R = [[Q(3), Q(2)], [Q(1), Q(-1)], [Q(2), Q(4)]]
        for a, b in itertools.product(range(-2, 3), repeat=2):
            changed = [[R[0][0]+a, R[0][1]+b], R[1], R[2]]
            residual = [[Q(0), Q(0)], R[1], R[2]]
            removed = [[R[0][0]+a, R[0][1]+b], [Q(0), Q(0)], [Q(0), Q(0)]]
            self.assertEqual(minus(gram(changed), gram(residual)), gram(removed))

    def test_original_layer_coordinate(self):
        # U=<e0>, W=<e0,e1>, same ambient 3-space throughout.
        for a, b, c in itertools.product(range(-2, 3), repeat=3):
            qU = (Q(b), Q(c))
            qW = (Q(c),)
            layer = Q(b)
            self.assertEqual((layer, qW[0]), qU)
            self.assertEqual(qW == (0,), c == 0)
            self.assertEqual(qU == (0, 0), b == 0 and c == 0)
        self.assertNotEqual((Q(1), Q(0)), (Q(0), Q(0)))
        transport = lambda x: (x[1],)
        self.assertEqual(transport((Q(1), Q(0))), (Q(0),))

    def test_full_four_mask_lift(self):
        p = 3
        active = [(0, (0, 0))] + [(m, b) for m in (1, 2, 3)
                                  for b in itertools.product(range(p), repeat=2)]
        def add(x, y):
            return (x[0] | y[0], tuple((a+b) % p for a, b in zip(x[1], y[1])))
        def scale(c, x):
            return (0, (0, 0)) if c is None else (x[0], tuple(c*a % p for a in x[1]))
        def lift(x, alpha):
            if x[0] == 0:
                return (0, (0, 0))
            b = x[1][1]
            # theta(v)=(v,0), Fourier=2 with inverse 2 modulo 3.
            return (3, ((1+alpha)*b % p, 2*alpha*b % p))
        for alpha in range(p):
            for x in active:
                for c in [None, 0, 1, 2]:
                    self.assertEqual(lift(scale(c, x), alpha), scale(c, lift(x, alpha)))
                for y in active:
                    self.assertEqual(lift(add(x, y), alpha), add(lift(x, alpha), lift(y, alpha)))
            self.assertEqual(lift((1, (0, 0)), alpha), (3, (0, 0)))
            self.assertNotEqual(lift((1, (0, 0)), alpha), lift((0, (0, 0)), alpha))
            for b in itertools.product(range(p), repeat=2):
                h = lift((1, b), alpha)[1]
                self.assertEqual((h[0]-2*h[1]) % p, b[1])
            for x in range(p):
                self.assertEqual(lift((3, (x, 0)), alpha), (3, (0, 0)))

    def test_compressed_characteristic_polynomial(self):
        # Exact real and imaginary parts, including degeneracies.
        for a, b, x, y, t in itertools.product(range(3), repeat=5):
            if x*x+y*y > a*b:
                continue
            self.assertEqual((x-t)**2+y*y-a*b, (t-x)**2-(a*b-y*y))
            self.assertGreaterEqual(a*b-y*y, 0)

    def test_audit_accept_and_reject(self):
        name = 'SplitZero.BoundaryIntegration.projector_commutator'
        valid = f"'{name}' depends on axioms: [propext, Quot.sound]\n"
        self.assertEqual(set(audit(valid, [name])[name]), {'propext', 'Quot.sound'})
        for bad in ['', valid+valid, valid.replace('Quot.sound', 'sorryAx'),
                    valid.replace(name, 'SplitZero.Wrong')]:
            with self.assertRaises(ValueError):
                audit(bad, [name])

    def test_manifest_negative_controls(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            spec = {'SplitZeroProbe': ['SplitZero.Probe.test']}
            # The preserved library's manifest must never be consumed or overwritten.
            legacy = root/'BOUNDARY_TARGETS.json'
            legacy.write_text('not the integration manifest')
            (root/'BOUNDARY_INTEGRATION_TARGETS.json').write_text(json.dumps(spec))
            with self.assertRaises(FileNotFoundError):
                preflight(root)
            file = root/'SplitZeroProbe.lean'
            file.write_text('theorem test : True := by trivial\n', encoding='utf-8', newline='\n')
            self.assertEqual(preflight(root)[1], ['SplitZero.Probe.test'])
            self.assertEqual(legacy.read_text(), 'not the integration manifest')
            file.write_text('theorem test : True := by sorry\n', encoding='utf-8', newline='\n')
            with self.assertRaises(ValueError):
                preflight(root)
            file.write_text('/- sorry only inside a comment -/\ntheorem test : True := by trivial\n',
                            encoding='utf-8', newline='\n')
            preflight(root)
            spec['SplitZeroProbe'].append('SplitZero.Probe.test')
            (root/'BOUNDARY_INTEGRATION_TARGETS.json').write_text(json.dumps(spec))
            with self.assertRaises(ValueError):
                preflight(root)

if __name__ == '__main__':
    unittest.main()
