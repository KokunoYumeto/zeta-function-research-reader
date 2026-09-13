#!/usr/bin/env python3
"""Exact finite calibrations; not arithmetic-zero samples and not a Lean certificate."""
from __future__ import annotations
from fractions import Fraction as Q
from itertools import product
import argparse
import io
import json
import sys
import unittest


def poly(p):
    p = list(map(Q, p))
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def pmul(p, q):
    out = [Q(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return poly(out)


def mon(n):
    return [Q(0)]*n + [Q(1)]


def rem(p, h):
    h, p = poly(h), poly(p)
    if h[-1] != 1:
        raise ValueError('modulus must be monic')
    while len(p) >= len(h) and any(p):
        n, a = len(p)-len(h), p[-1]
        for i, b in enumerate(h):
            p[n+i] -= a*b
        p = poly(p)
    return p + [Q(0)]*(len(h)-1-len(p))


def tr(a):
    return [list(c) for c in zip(*a)]


def eye(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def zero(n, m):
    return [[Q(0) for _ in range(m)] for _ in range(n)]


def mm(a, b):
    if not a or not b or len(a[0]) != len(b):
        raise ValueError('nonempty compatible matrix dimensions required')
    return [[sum((x*y for x, y in zip(row, col)), Q(0)) for col in tr(b)] for row in a]


def scale(c, a):
    return [[c*x for x in row] for row in a]


def plus(a, b):
    return [[x+y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def minus(a, b):
    return plus(a, scale(-1, b))


def inv(a):
    n = len(a)
    if any(len(r) != n for r in a):
        raise ValueError('square matrix required')
    b = [list(map(Q, r))+e for r, e in zip(a, eye(n))]
    for j in range(n):
        pivot = next((i for i in range(j, n) if b[i][j]), None)
        if pivot is None:
            raise ValueError('singular matrix')
        b[j], b[pivot] = b[pivot], b[j]
        b[j] = [x/b[j][j] for x in b[j]]
        for i in range(n):
            if i != j:
                c = b[i][j]
                b[i] = [x-c*y for x, y in zip(b[i], b[j])]
    return [r[n:] for r in b]


def det(a):
    b = [list(map(Q, r)) for r in a]
    v = Q(1)
    for j in range(len(b)):
        pivot = next((i for i in range(j, len(b)) if b[i][j]), None)
        if pivot is None:
            return Q(0)
        if pivot != j:
            b[j], b[pivot] = b[pivot], b[j]
            v = -v
        c = b[j][j]
        v *= c
        for i in range(j+1, len(b)):
            d = b[i][j]/c
            b[i] = [x-d*y for x, y in zip(b[i], b[j])]
    return v


def rank(a):
    b = [list(map(Q, r)) for r in a]
    row = 0
    for col in range(len(b[0])):
        p = next((i for i in range(row, len(b)) if b[i][col]), None)
        if p is None:
            continue
        b[row], b[p] = b[p], b[row]
        d = b[row][col]
        b[row] = [x/d for x in b[row]]
        for i in range(row+1, len(b)):
            d = b[i][col]
            b[i] = [x-d*y for x, y in zip(b[i], b[row])]
        row += 1
        if row == len(b):
            break
    return row


def trace(a):
    return sum((a[i][i] for i in range(len(a))), Q(0))


POLYS = [[0, 1], [0, 0, 1], [1, 0, 1], [-1, 3, -3, 1],
         [4, 0, 5, 0, 1], [0, 0, 0, 0, 0, 1]]


def residue_gram(h):
    q = len(h)-1
    return [[rem(mon(i+j), h)[q-1] for j in range(q)] for i in range(q)]


def companion(h):
    q = len(h)-1
    return tr([rem(mon(j+1), h) for j in range(q)])


def moment(n, weights):
    nodes = list(range(-3, 4))
    return [[sum((Q(w)*Q(x)**(i+j) for x, w in zip(nodes, weights)), Q(0))
             for j in range(n+1)] for i in range(n+1)]


def metric_data(n, s=Q(0)):
    m0 = moment(n, [1]*7)
    m1 = moment(n, [Q(3,2), Q(2,3), Q(5,4), 1, Q(5,4), Q(2,3), Q(3,2)])
    dm = minus(m1, m0)
    m = plus(m0, scale(s, dm))
    j = tr([rem(mon(a), [1, 0, 1]) for a in range(n+1)])
    p = inv(m)
    kernel = mm(mm(j, p), tr(j))
    g = inv(kernel)
    r = mm(mm(p, tr(j)), g)
    return m, dm, j, p, g, r


def log_interval(x, order=160):
    if x <= 0:
        raise ValueError('positive argument required')
    y = (x-1)/(x+1)
    value = 2*sum((y**(2*n+1)/Q(2*n+1) for n in range(order)), Q(0))
    error = 2*abs(y)**(2*order+1)/(Q(2*order+1)*(1-y*y))
    return value-error, value+error


def slope_and_volume(n, s):
    _, dm, _, _, g, r = metric_data(n, s)
    return trace(mm(inv(g), mm(mm(tr(r), dm), r))), det(g)


class ResidueTests(unittest.TestCase):
    def test_perfect_original_remainder_pairing(self):
        for h in POLYS:
            q = len(h)-1
            self.assertEqual(det(residue_gram(h)), (-1)**(q*(q-1)//2))

    def test_bounded_constructive_detection(self):
        for h in POLYS:
            q = len(h)-1
            for v in product((-1, 0, 1), repeat=q):
                if not any(v):
                    continue
                d = max(i for i, x in enumerate(v) if x)
                n = q-1-d
                self.assertTrue(0 <= n < q)
                self.assertEqual(rem(pmul(mon(n), v), h)[q-1], v[d])

    def test_actual_dual_inverse(self):
        for h in POLYS:
            a = residue_gram(h)
            self.assertEqual(mm(inv(a), a), eye(len(h)-1))

    def test_repeated_constituent_transverse_rank_and_kernel(self):
        for d, e in [([0, 0, 1], [0, 0, 0, 1]), ([-1, 1], [1, 2, 1]),
                     ([1, 2, 1], [-1, 1]), ([1, 0, 1], [1, 0, 1])]:
            h = pmul(d, e)
            q, p = len(h)-1, len(e)-1
            inc = tr([rem(pmul(d, mon(j)), h) for j in range(p)])
            a = companion(h)
            self.assertEqual(rank([x+y for x, y in zip(inc, mm(a, inc))]), p)
            ins = zero(q, q)
            ins[0][-1] = Q(1)
            quotient = tr([rem(mon(j), d) for j in range(q)])
            response = mm(mm(quotient, ins), inc)
            self.assertEqual(rank(response), 1)
            self.assertEqual(p-rank(response), p-1)
            self.assertEqual(response[0], inc[-1])
            self.assertTrue(all(not any(row) for row in response[1:]))

    def test_joint_operator_algebra_retains_every_direction(self):
        for h in POLYS:
            q = len(h)-1
            a = companion(h)
            ins = zero(q, q)
            ins[0][-1] = Q(1)
            powers = [eye(q)]
            for _ in range(q-1):
                powers.append(mm(powers[-1], a))
            columns = [sum(mm(mm(x, ins), y), []) for x in powers for y in powers]
            self.assertEqual(rank(tr(columns)), q*q)

    def test_canonical_sections_preserve_full_remainder(self):
        for n in range(1, 5):
            for s in (Q(0), Q(1,3), Q(1)):
                m, _, j, _, g, r = metric_data(n, s)
                self.assertEqual(mm(j, r), eye(2))
                self.assertEqual(mm(mm(tr(r), m), r), g)
                self.assertGreater(det(m), 0)
                self.assertGreater(det(g), 0)

    def test_source_derivative_is_original_relation(self):
        for n in range(1, 5):
            m, dm, j, p, g, r = metric_data(n, Q(1,3))
            pd = scale(-1, mm(mm(p, dm), p))
            kd = mm(mm(j, pd), tr(j))
            gd = scale(-1, mm(mm(g, kd), g))
            rd = plus(mm(mm(pd, tr(j)), g), mm(mm(p, tr(j)), gd))
            self.assertEqual(mm(j, rd), zero(2, 2))
            if n == 1:
                self.assertEqual(rd, zero(n+1, 2))
            else:
                b = tr([pmul([1,0,1], mon(a)) + [Q(0)]*(n-2-a) for a in range(n-1)])
                hb = inv(mm(mm(tr(b), m), b))
                expected = scale(-1, mm(mm(mm(mm(b, hb), tr(b)), dm), r))
                self.assertEqual(rd, expected)

    def test_gram_first_and_second_derivatives(self):
        for n in range(1, 5):
            m, dm, j, p, g, r = metric_data(n, Q(2,5))
            pd = scale(-1, mm(mm(p, dm), p))
            pdd = scale(2, mm(mm(mm(mm(p, dm), p), dm), p))
            kd = mm(mm(j, pd), tr(j))
            kdd = mm(mm(j, pdd), tr(j))
            gd = scale(-1, mm(mm(g, kd), g))
            gdd = minus(scale(2, mm(mm(mm(mm(g,kd),g),kd),g)), mm(mm(g,kdd),g))
            self.assertEqual(gd, mm(mm(tr(r), dm), r))
            if n == 1:
                self.assertEqual(gdd, zero(2,2))
            else:
                b = tr([pmul([1,0,1], mon(a)) + [Q(0)]*(n-2-a) for a in range(n-1)])
                hb = inv(mm(mm(tr(b), m), b))
                z = mm(mm(tr(b), dm), r)
                self.assertEqual(gdd, scale(-2, mm(mm(tr(z), hb), z)))
            self.assertLessEqual(gdd[0][0], 0)
            self.assertLessEqual(gdd[1][1], 0)
            self.assertGreaterEqual(det(gdd), 0)

    def test_two_sided_endpoint_slope_certificate(self):
        for n in range(1, 5):
            d0, v0 = slope_and_volume(n, Q(0))
            d1, v1 = slope_and_volume(n, Q(1))
            low, high = log_interval(v1/v0)
            self.assertLessEqual(d1, low)
            self.assertLessEqual(high, d0)

    def test_signed_four_endpoint_sides(self):
        rows = [slope_and_volume(n, s) for n in range(1, 5) for s in (Q(0), Q(1))]
        d0 = [rows[2*n][0] for n in range(4)]
        d1 = [rows[2*n+1][0] for n in range(4)]
        ratios = [rows[2*n+1][1]/rows[2*n][1] for n in range(4)]
        low, high = log_interval(ratios[0]*ratios[1]/ratios[2]/ratios[3])
        self.assertLessEqual(d1[0]+d1[1]-d0[2]-d0[3], low)
        self.assertLessEqual(high, d0[0]+d0[1]-d1[2]-d1[3])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--negative', choices=('rank', 'source-sign'))
    args = parser.parse_args()
    if args.negative == 'rank':
        if rank([[Q(0),Q(1)],[Q(0),Q(0)]]) != 0:
            raise ValueError('deliberate false rank-zero formula rejected')
        raise RuntimeError('bad rank formula accepted')
    if args.negative == 'source-sign':
        _, dm, _, _, _, r = metric_data(2)
        form = mm(mm(tr(r),dm),r)
        if form != scale(-1,form):
            raise ValueError('deliberate false source-derivative sign rejected')
        raise RuntimeError('bad source sign accepted')
    stream = io.StringIO()
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(ResidueTests))
    if not result.wasSuccessful():
        sys.stderr.write(stream.getvalue())
        sys.exit(1)
    print(json.dumps({'status':'passed', 'exact_test_methods':result.testsRun,
                      'scope':'declared rational polynomial and finite source-moment fixtures',
                      'arithmetic_zero_certificate':False}, sort_keys=True))


if __name__ == '__main__':
    main()
