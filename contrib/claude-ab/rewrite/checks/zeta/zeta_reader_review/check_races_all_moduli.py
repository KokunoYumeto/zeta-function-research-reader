#!/usr/bin/env python3
"""Check for the finding on reader Prop 4.10 (second line and prime races), stated there for mod 4.

For any q and classes a != b coprime to q, the two-line theta race differs from the one-line race by
   sum_{p<=x, p=a} log p/p - sum_{p<=x, p=b} log p/p
   = phi(q)^{-1} sum_{chi != chi0} (conj chi(a) - conj chi(b)) sum_{p<=x} chi(p) log p / p,
a convergent series (PNT in progressions); the principal character cancels.  Same for the counting race
with weights 1/p.  So the conclusion of Prop 4.10 holds for every modulus and every pair (or r-tuple) of classes.
"""
import numpy as np
X = 10**7
sieve = np.ones(X + 1, bool); sieve[:2] = False
for p in range(2, int(X**0.5) + 1):
    if sieve[p]:
        sieve[p*p::p] = False
P = np.nonzero(sieve)[0].astype(np.int64)
lp = np.log(P.astype(float))
ok = True
checkpoints = [10**3, 10**4, 10**5, 10**6, 10**7]
for q, pairs in [(5, [(2, 1), (4, 1), (3, 2)]), (8, [(3, 1), (5, 1), (7, 1)]), (3, [(2, 1)]), (12, [(11, 1), (5, 7)])]:
    print(f"modulus q = {q}")
    for a, b in pairs:
        wa = np.where(P % q == a, lp/P, 0.0) - np.where(P % q == b, lp/P, 0.0)     # theta race correction
        ca = np.where(P % q == a, 1.0/P, 0.0) - np.where(P % q == b, 1.0/P, 0.0)   # counting race correction
        cw, cc = np.cumsum(wa), np.cumsum(ca)
        th = np.cumsum(np.where(P % q == a, lp, 0.0) - np.where(P % q == b, lp, 0.0))
        vals = []; valc = []; norm = []
        for x in checkpoints:
            i = np.searchsorted(P, x, side='right') - 1
            vals.append(cw[i]); valc.append(cc[i]); norm.append(abs(cw[i])/np.sqrt(x))
        print(f"   ({a},{b}): sum log p/p diff at 1e3..1e7: " + ", ".join(f"{v:.4f}" for v in vals)
              + " | sum 1/p diff: " + ", ".join(f"{v:.5f}" for v in valc)
              + f" | correction/sqrt(x) at 1e7: {norm[-1]:.2e}")
        ok &= abs(vals[-1] - vals[-2]) < 0.02 and abs(valc[-1] - valc[-2]) < 0.002
print("\nALL CHECKS PASS" if ok else "\nSOME CHECK FAILED")
