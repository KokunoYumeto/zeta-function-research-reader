#!/usr/bin/env python3
"""F18 verification (independent code).

For q in {3, 5, 7, 8, 12} and every pair of distinct reduced classes a, b: the two-line minus one-line difference
    theta-race:   sum_{p<=x} (1_{p=a} - 1_{p=b}) log p / p
    counting race: sum_{p<=x} (1_{p=a} - 1_{p=b}) / p
at x = 1e3, 1e4, 1e5, 1e6, 1e7 (primes by numpy sieve).  The principal character cancels in the difference, so
each is phi(q)^{-1} sum_{chi != chi0} (conj chi(a) - conj chi(b)) sum_{p<=x} chi(p) log p/p (resp. chi(p)/p):
both converge by the PNT in progressions.  Report the spread of the last three values (should shrink) and the
maximum over pairs of the value at 1e7 divided by sqrt(1e7) (theta) and by sqrt(1e7)/log(1e7) (counting).
Also the r-way normalisation phi(q) sum_{p=a} 1/p - sum_p 1/p (principal part converges to -sum_{p|q} 1/p).
"""
import numpy as np
from math import gcd, log, sqrt

X = 10 ** 7
sieve = np.ones(X + 1, dtype=bool); sieve[:2] = False
for i in range(2, int(X ** 0.5) + 1):
    if sieve[i]:
        sieve[i * i::i] = False
P = np.nonzero(sieve)[0]
logp_over_p = np.log(P) / P
inv_p = 1.0 / P
checkpoints = [10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7]
cut = [np.searchsorted(P, x, side='right') for x in checkpoints]

def partial(mask, w):
    c = np.cumsum(np.where(mask, w, 0.0))
    return [c[k - 1] for k in cut]

worst_theta, worst_count, worst_spread_theta, worst_spread_count = 0, 0, 0, 0
for q in (3, 5, 7, 8, 12):
    classes = [a for a in range(1, q) if gcd(a, q) == 1]
    res = P % q
    for i, a in enumerate(classes):
        for b in classes[i + 1:]:
            m = (res == a).astype(float) - (res == b).astype(float)
            th = partial(m != 0, m * logp_over_p)
            ct = partial(m != 0, m * inv_p)
            sp_th = max(th[2:]) - min(th[2:]); sp_ct = max(ct[2:]) - min(ct[2:])
            worst_spread_theta = max(worst_spread_theta, sp_th); worst_spread_count = max(worst_spread_count, sp_ct)
            worst_theta = max(worst_theta, abs(th[-1]) / sqrt(X)); worst_count = max(worst_count, abs(ct[-1]) * log(X) / sqrt(X))
            if (q, a, b) in [(5, 1, 2), (8, 1, 3), (12, 5, 11), (7, 3, 6), (3, 1, 2)]:
                print("  q=%2d (%d,%d): theta-diff %s | count-diff %s" % (q, a, b,
                      " ".join("%.4f" % v for v in th), " ".join("%.5f" % v for v in ct)))
    # r-way principal part: phi(q) sum_{p=a} 1/p - sum_p 1/p = sum_{chi != chi0} conj chi(a) sum chi(p)/p - sum_{p|q} 1/p
    phi = len(classes)
    for a in classes[:2]:
        v = partial(res == a, inv_p)
        allp = partial(np.ones_like(res, dtype=bool), inv_p)
        rway = [phi * v[k] - allp[k] for k in range(len(cut))]
        print("  q=%2d r-way term phi(q) S_a - S (a=%d): %s" % (q, a, " ".join("%.4f" % r for r in rway)))
print("max spread over x in {1e5,1e6,1e7}, all pairs: theta %.4f, counting %.5f" % (worst_spread_theta, worst_spread_count))
print("max |theta-diff(1e7)|/sqrt(1e7) = %.2e ; max |count-diff(1e7)| log(1e7)/sqrt(1e7) = %.2e" % (worst_theta, worst_count))
assert worst_spread_theta < 0.05 and worst_spread_count < 0.002 and worst_theta < 1e-3 and worst_count < 1e-2   # normalised values decay like 1/sqrt(x) resp. log x/sqrt(x)
print("ALL F18 CHECKS PASS")
