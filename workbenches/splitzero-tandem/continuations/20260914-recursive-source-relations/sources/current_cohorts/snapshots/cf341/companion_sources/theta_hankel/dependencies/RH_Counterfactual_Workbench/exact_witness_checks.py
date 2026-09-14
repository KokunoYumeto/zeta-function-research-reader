#!/usr/bin/env python3
"""Exact finite checks and a rational interval witness evaluator.

The interval evaluator trusts its supplied coefficient enclosures.
It does not certify the analytic quadrature that produced an enclosure.
"""
from fractions import Fraction as Q
import json
import unittest

def logarithmic_coefficients(a, count):
    if len(a)<count+1 or not a[0]:
        raise ValueError('Need a nonzero constant and count+1 coefficients')
    b=[]
    for n in range(count):
        b.append((-(n+1)*a[n+1]-sum(a[j]*b[n-j] for j in range(1,n+1)))/a[0])
    return b

def quadratic(b,c,shift=0):
    return sum(c[i]*c[j]*b[i+j+shift] for i in range(len(c)) for j in range(len(c)))

def enclose_quadratic(intervals,c,shift=0):
    """Exact enclosure of sum c_i c_j b_(i+j+shift), c_i rational."""
    if not c or len(intervals)<2*len(c)-1+shift:
        raise ValueError('Not enough moment intervals')
    lower=upper=Q(0)
    for i,x in enumerate(c):
        for j,y in enumerate(c):
            lo,hi=map(Q,intervals[i+j+shift])
            if lo>hi:
                raise ValueError('Reversed interval')
            factor=Q(x)*Q(y)
            terms=(factor*lo,factor*hi)
            lower+=min(terms); upper+=max(terms)
    return {'lower':str(lower),'upper':str(upper),
            'strict_negative_given_valid_input_enclosures':upper<0}

class ExactChecks(unittest.TestCase):
    def test_logarithmic_recurrence(self):
        # 7(1-w/2)(1-w/3); literal mass seven retained.
        a=[Q(7),-Q(35,6),Q(7,6),Q(0),Q(0),Q(0)]
        b=logarithmic_coefficients(a,5)
        self.assertEqual(b,[Q(1,2)**(n+1)+Q(1,3)**(n+1) for n in range(5)])
    def test_positive_nodes(self):
        b=[Q(1,2)**(n+1)+Q(1,3)**(n+1) for n in range(5)]
        c=[Q(2),Q(-3)]
        expected=Q(1,2)*(2-Q(3,2))**2+Q(1,3)*(2-1)**2
        self.assertEqual(quadratic(b,c),expected)
        self.assertGreater(expected,0)
    def test_nonreal_pair_negative(self):
        # beta=(240+128*i)/289 and its conjugate: NOT actual zeta zeros.
        br=Q(240,289); bi=Q(128,289)
        norm=br*br+bi*bi
        a=[Q(7),-14*br,7*norm,Q(0)]
        b=logarithmic_coefficients(a,3)
        value=quadratic(b,[Q(-1),Q(1)])
        self.assertEqual(value,-Q(3500576,24137569))
        self.assertLess(value,0)
        self.assertEqual(b[0]*b[2]-b[1]*b[1],-4*norm*bi*bi)
    def test_interval_negative_witness(self):
        # Derive all three coefficients by exact formal division.
        a=[Q(7),-Q(3360,289),Q(1792,289),Q(0)]
        b=logarithmic_coefficients(a,3)
        eps=Q(1,10**8)
        result=enclose_quadratic([(v-eps,v+eps) for v in b],[Q(-1),Q(1)])
        self.assertTrue(result['strict_negative_given_valid_input_enclosures'])
        self.assertLess(Q(result['upper']),0)
    def test_inconclusive_is_not_negative(self):
        result=enclose_quadratic([(Q(-1),Q(1))],[Q(1)])
        self.assertFalse(result['strict_negative_given_valid_input_enclosures'])
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            enclose_quadratic([(Q(2),Q(1))],[Q(1)])
        with self.assertRaises(ValueError):
            logarithmic_coefficients([Q(0),Q(1)],1)

if __name__=='__main__':
    unittest.main(verbosity=2)
