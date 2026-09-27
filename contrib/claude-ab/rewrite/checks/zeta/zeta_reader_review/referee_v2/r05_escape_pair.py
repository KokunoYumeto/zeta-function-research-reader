#!/usr/bin/env python3
"""Referee v2, script r05.  Lemma 6.4 (escape under ramification) for real a > 1.

 1. a = 3/2, rho = 0.55 + i: Z = {rho, rho#, a rho, a rho#, (a rho)#, (a rho#)#} (x# = 1 - conj x) lies in
    0 < Re < 1, is #-closed, and contains a*rho and a*rho#: a reflected pair returns together (exact rationals).
 2. For a >= 2 no reflected pair returns: Re rho < 1/a and 1 - Re rho < 1/a are incompatible (grid check);
    for 1 < a < 2 exactly the band 1 - 1/a < Re rho < 1/a allows it.
 3. Collision a rho = a' rho' with real a, a': rho/rho' = a'/a > 0 need not be rational
    (a = 2 sqrt 2, a' = 2, rho = 0.3 + 0.3i, rho' = sqrt 2 rho, both in the strip); on the critical line
    (1/2 + i g)/(1/2 + i g') is real only if g = g'.
 4. Finite return sets: {k >= 0 : a^k rho in strip} is finite for every a > 1 (Re grows geometrically).
"""
from fractions import Fraction as Fr
import math, random
ok_all = True
def rep(name, cond, info=""):
    global ok_all
    ok_all &= bool(cond); print(("[PASS] " if cond else "[FAIL] ") + name + ("" if not info else ": " + str(info)))
def sharp(z): return (1 - z[0], z[1])                  # z = (Re, Im) exact; x# = 1 - conj(x): (1 - Re, Im)
def mul(a, z): return (a * z[0], a * z[1])
a = Fr(3, 2); rho = (Fr(55, 100), Fr(1)); rs = sharp(rho)
Z = {rho, rs, mul(a, rho), mul(a, rs), sharp(mul(a, rho)), sharp(mul(a, rs))}
rep("1  a = 3/2, rho = 0.55+i: Z in the strip, #-closed, contains a rho and a rho#",
    all(0 < z[0] < 1 for z in Z) and all(sharp(z) in Z for z in Z) and mul(a, rho) in Z and mul(a, rs) in Z and len(Z) == 6,
    sorted((float(z[0]), float(z[1])) for z in Z))
ok2 = True
for a2 in (2.0, 2.5, 3.0, 7.0):
    for i in range(1, 1000):
        b = i / 1000
        if b < 1 / a2 and 1 - b < 1 / a2: ok2 = False
band_ok = all(((1 - 1 / aa < b < 1 / aa) == (b < 1 / aa and 1 - b < 1 / aa)) for aa in (1.2, 1.5, 1.9) for b in [i / 997 for i in range(1, 997)])
rep("2  a >= 2: no pair can return together; 1 < a < 2: exactly the band 1 - 1/a < Re < 1/a", ok2 and band_ok)
aa, ap = 2 * math.sqrt(2), 2.0
r = complex(0.3, 0.3); rp = math.sqrt(2) * r
rep("3a real a, a': collision a rho = a' rho' with irrational ratio rho/rho' = 1/sqrt 2",
    abs(aa * r - ap * rp) < 1e-12 and 0 < r.real < 1 and 0 < rp.real < 1 and abs((r / rp).imag) < 1e-15 and abs((r / rp).real - 1 / math.sqrt(2)) < 1e-15)
random.seed(1)
okc = True
for _ in range(20000):
    g, gp = random.uniform(-100, 100), random.uniform(-100, 100)
    q = complex(0.5, g) / complex(0.5, gp)
    if abs(q.imag) < 1e-9 and abs(g - gp) > 1e-6: okc = False
rep("3b on the critical line the ratio is real only when the ordinates agree (20000 random pairs)", okc)
okf = True
for aa in (1.01, 1.5, 2.0, 3.7):
    for b in (0.001, 0.2, 0.9):
        ks = [k for k in range(0, 2000) if k * math.log(aa) + math.log(b) < 0]
        okf &= len(ks) < 2000 and ks == list(range(len(ks)))
rep("4  {k >= 0 : a^k Re rho < 1} is a finite initial segment for every a > 1", okf)
print("ALL CHECKS PASS" if ok_all else "SOME CHECKS FAILED")
