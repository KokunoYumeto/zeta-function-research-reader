#!/usr/bin/env python3
"""Exact checks of adaptive source variation; generic finite-moment calibrations only."""
from fractions import Fraction as Q
import io
import json
import sys
import unittest
from check_exact import metric_data, slope_and_volume, log_interval, mm, tr, inv, trace


def brackets(n, r):
    slopes = [slope_and_volume(n, Q(j,r))[0] for j in range(r+1)]
    return sum(slopes[1:],Q(0))/r, sum(slopes[:-1],Q(0))/r, slopes


class AdaptiveTests(unittest.TestCase):
    def test_partition_enclosure_and_exact_width(self):
        for n in range(1,5):
            _, v0 = slope_and_volume(n,Q(0))
            _, v1 = slope_and_volume(n,Q(1))
            lo, hi = log_interval(v1/v0)
            for r in (1,2,4,8):
                lower, upper, slopes = brackets(n,r)
                self.assertTrue(all(x >= y for x,y in zip(slopes,slopes[1:])))
                self.assertLessEqual(lower,lo)
                self.assertLessEqual(hi,upper)
                self.assertEqual(upper-lower,(slopes[0]-slopes[-1])/r)

    def test_signed_partition_certificate(self):
        ratios = [slope_and_volume(n,Q(1))[1]/slope_and_volume(n,Q(0))[1]
                  for n in range(1,5)]
        lo, hi = log_interval(ratios[0]*ratios[1]/ratios[2]/ratios[3])
        for r in (1,2,4,8):
            rows = [brackets(n,r) for n in range(1,5)]
            lower = rows[0][0]+rows[1][0]-rows[2][1]-rows[3][1]
            upper = rows[0][1]+rows[1][1]-rows[2][0]-rows[3][0]
            self.assertLessEqual(lower,lo)
            self.assertLessEqual(hi,upper)
            self.assertEqual(upper-lower,sum((b-a for a,b,_ in rows),Q(0)))

    def test_quotient_dual_coupling_derivative(self):
        # F is the specified second coordinate. This metric identity needs no
        # invariance assumption; the separate Lean theorem handles invariant F.
        for n in range(1,5):
            for s in (Q(0),Q(1,3),Q(1)):
                _, dm, _, _, g, r = metric_data(n,s)
                gd = mm(mm(tr(r),dm),r)
                vq = [[Q(1)],[-g[1][0]/g[1][1]]]
                vf = [[Q(0)],[1/g[1][1]]]
                def ray(v):
                    return mm(mm(tr(v),gd),v)[0][0]/mm(mm(tr(v),g),v)[0][0]
                expected = trace(mm(inv(g),gd))-2*gd[1][1]/g[1][1]
                self.assertEqual(ray(vq)-ray(vf),expected)


def main():
    stream=io.StringIO()
    result=unittest.TextTestRunner(stream=stream,verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(AdaptiveTests))
    if not result.wasSuccessful():
        sys.stderr.write(stream.getvalue())
        sys.exit(1)
    print(json.dumps({'status':'passed','exact_test_methods':result.testsRun,
                      'scope':'finite source-metric partition and residue-coupling identities',
                      'arithmetic_zero_certificate':False},sort_keys=True))


if __name__=='__main__':
    main()
