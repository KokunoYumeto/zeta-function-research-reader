#!/usr/bin/env python3
"""Referee v2, script r04.  Lemma 5.5 (integer positivity), the Z/3 and Z/2 examples.

Z/3 with characters 1, tau, tau^2 (tau(g) = omega^g).  A genuine rho = a + b tau + c tau^2 (a,b,c >= 0 integers).
 1. The multiplicities of rho*conj(rho), computed by inner products on the group, are
    [.:1] = a^2+b^2+c^2 and [.:tau] = [.:tau^2] = ab+bc+ca.
 2. nu(1) = 1, nu(tau) = nu(tau^2) = -x: nu(rho conj rho) >= 0 for all genuine rho (a,b,c <= 12) iff x <= 1/2
    (violation at (1,1,1) as soon as x > 1/2); the real-valued bound sum d_tau(-nu(tau)) = 2x <= 1 is sharp at 1/2,
    where two non-quadratic characters are negative (the integer dichotomy fails for real nu).
 3. Z/2: nu(sgn) = -1 satisfies every hypothesis: nu((a + b sgn) conj) = (a - b)^2 >= 0.
"""
from fractions import Fraction as Fr
import cmath, itertools
ok_all = True
def rep(name, cond, info=""):
    global ok_all
    ok_all &= bool(cond); print(("[PASS] " if cond else "[FAIL] ") + name + ("" if not info else ": " + str(info)))
om = cmath.exp(2j * cmath.pi / 3)
chars = [lambda g: 1, lambda g: om**g, lambda g: om**(2 * g)]
def mult(a, b, c):
    f = [abs(a + b * om**g + c * om**(2 * g))**2 for g in range(3)]      # rho(g) conj(rho(g)) as a class function
    return [round((sum(f[g] * chars[j](g).conjugate() for g in range(3)) / 3).real, 9) for j in range(3)]
bad = 0
for a, b, c in itertools.product(range(6), repeat=3):
    m = mult(a, b, c)
    if abs(m[0] - (a*a + b*b + c*c)) > 1e-7 or abs(m[1] - (a*b + b*c + c*a)) > 1e-7 or abs(m[2] - (a*b + b*c + c*a)) > 1e-7:
        bad += 1
rep("1  multiplicities of rho conj(rho) on Z/3", bad == 0, "216 genuine rho checked")

def positive(x, B=12):
    for a, b, c in itertools.product(range(B + 1), repeat=3):
        if a*a + b*b + c*c - 2 * x * (a*b + b*c + c*a) < 0:
            return False, (a, b, c)
    return True, None
res = {str(x): positive(x) for x in (Fr(0), Fr(1, 4), Fr(1, 2), Fr(1, 2) + Fr(1, 10**9), Fr(3, 5))}
rep("2  positivity holds iff x <= 1/2 (exhaustive a,b,c <= 12, exact rationals)",
    res['0'][0] and res['1/4'][0] and res['1/2'][0] and not res[str(Fr(1, 2) + Fr(1, 10**9))][0] and not res['3/5'][0],
    {k: (v[0], v[1]) for k, v in res.items()})
rep("2' at x = 1/2: sum_{tau != 1} d_tau(-nu(tau)) = 2x = 1 (sharp), two negative characters, tau^2 != 1 (not quadratic)",
    2 * Fr(1, 2) == 1 and abs(om**2 - 1) > 0.5)
rep("3  Z/2: nu(sgn) = -1 gives nu((a+b sgn)(a+b sgn)) = a^2 + b^2 - 2ab = (a-b)^2 >= 0",
    all(a*a + b*b - 2*a*b >= 0 for a in range(30) for b in range(30)))
print("ALL CHECKS PASS" if ok_all else "SOME CHECKS FAILED")
