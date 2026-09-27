#!/usr/bin/env python3
"""Non-vacuous test of the finite clock identity used in the Tao clock preprint:
 sum_{n<=X, Cmin(n)>K} 1/n = sum_{a>=0} 2^-a sum_{m<=X/2^a, m odd, Smin(m)>K} 1/m.
For 3x+1 both sides vanish on every verified range, so the same (map-independent) mechanism is
tested on the 3x-1 map, whose nontrivial cycles (min 5 and min 17) make both sides nonzero."""
from fractions import Fraction
def v2(x): return (x & -x).bit_length()-1
def Tm(n): x=3*n-1; return x>>v2(x)
def full_orbit_min(n):
    seen=set(); best=n; x=n
    while x not in seen:
        seen.add(x); best=min(best,x)
        x = x//2 if x%2==0 else 3*x-1
    return best
def odd_orbit_min(m):
    seen=set(); best=m; x=m
    while x not in seen:
        seen.add(x); best=min(best,x); x=Tm(x)
    return best
for X,K in ((50000,4),(50000,16),(120000,4)):
    lhs=sum(Fraction(1,n) for n in range(1,X+1) if full_orbit_min(n)>K)
    rhs=Fraction(0); a=0
    while X>>a:
        rhs+=Fraction(1,2**a)*sum(Fraction(1,m) for m in range(1,X//2**a+1,2) if odd_orbit_min(m)>K); a+=1
    assert lhs==rhs and lhs>0
    print('3x-1 map, X=%d, K=%d: both sides equal exactly = %.6f (nonzero): PASS'%(X,K,float(lhs)))
