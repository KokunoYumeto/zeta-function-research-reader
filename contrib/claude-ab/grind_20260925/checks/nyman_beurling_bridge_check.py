# claude-ab: the Nyman-Beurling functions rho_a(x) = {1/(a x)} (a > 1) are values of the programme's summation map
# Sigma h(u) = 2 sum_{n>=1} h(n u) on even step functions h with the programme's moment condition int h = 0:
#   if sum_k c_k / a_k = 0 then sum_k c_k rho_{a_k}(x) = -(1/2) Sigma(h)(x),  h = sum_k c_k 1_{[-1/a_k, 1/a_k]},
# and Sigma(h) vanishes for x > 1.  Also checks Titchmarsh's identity int_0^oo {1/x} x^{s-1} dx = -zeta(s)/s (0<Re s<1).
import mpmath as mp
from fractions import Fraction as Fr
import math, random
random.seed(1)
ok = True
def frac(y): return y - math.floor(y)
def Sigma_h(x, cs, as_):       # 2 * sum_n h(n x), h = sum_k c_k 1_{[-1/a_k, 1/a_k]}  (finite: n <= 1/(a_k x))
    return 2*sum(c*math.floor(1/(a*x) + 1e-15) for c, a in zip(cs, as_))
for trial in range(5):
    as_ = [1 + random.random()*4 for _ in range(3)]
    c12 = [random.uniform(-1, 1) for _ in range(2)]
    c3 = -as_[2]*(c12[0]/as_[0] + c12[1]/as_[1])      # enforce sum c_k/a_k = 0  (<=> int h = 0)
    cs = c12 + [c3]
    ok &= abs(sum(c/a for c, a in zip(cs, as_))) < 1e-12
    for x in [0.013, 0.07, 0.19, 0.33, 0.5, 0.91, 1.3, 2.7]:
        lhs = sum(c*frac(1/(a*x)) for c, a in zip(cs, as_))
        rhs = -0.5*Sigma_h(x, cs, as_)
        ok &= abs(lhs - rhs) < 1e-9
        if x > 1: ok &= abs(rhs) < 1e-12
print("step-function identity and support in (0,1]:", ok)
import numpy as np
mp.mp.dps = 20
for s in (complex(0.5, 3.0), complex(0.25, -1.5), complex(0.75, 0.0)):
    # int_0^oo {y} y^{-s-1} dy = int_0^1 y^{-s} dy + sum_{n=1}^{M-1} int_n^{n+1} (y-n) y^{-s-1} dy + tail,
    # each unit interval integrated exactly; tail over [M, oo) = M^{-s}/(2s) - M^{-s-1}/12 + O(M^{-Re s - 2}).
    M = 2_000_000
    n = np.arange(1, M, dtype=np.float64)
    pieces = ((n+1)**(1-s) - n**(1-s))/(1-s) - n*(n**(-s) - (n+1)**(-s))/s
    val = 1/(1-s) + pieces.sum() + M**(-s)/(2*s) - M**(-s-1)/12   # Euler-Maclaurin tail: mean 1/2 plus the B_2 correction
    ref = complex(-mp.zeta(s)/s)
    ok &= abs(val - ref) < 1e-10   # float64 summation of 2e6 terms limits the agreement
    print("s =", s, " integral =", val, " -zeta(s)/s =", ref, " diff = %.1e" % abs(val-ref))
print("ALL PASS" if ok else "FAIL")
