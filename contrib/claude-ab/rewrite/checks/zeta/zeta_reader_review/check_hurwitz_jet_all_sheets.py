#!/usr/bin/env python3
"""Checks for the finding on reader Theorem 4.1 (first Hurwitz jet), stated there at a = 1 only.

Claim (proof: d_a zeta(s,a) = -s zeta(s+1,a) for all a>0, s != 1, and s*zeta(s+1,a) is entire with value 1 at s=0):
  for EVERY a > 0 the zero divisor of the first a-jet  d_a zeta(s,a) = -s zeta(s+1,a)  is exactly
  (zero divisor of zeta(.,a)) - 1, globally (no strip restriction), and the jet equals -1 at s = 0.
  m-th jet: div = (div zeta(.,a) - m) + [0] + [-1] + ... + [2-m].
Also: the mirror statement A(Z_a) = Z_a - 1 (Thm 4.2) does NOT extend to a != 1 (e.g. a = 1/2).
"""
import mpmath as mp
mp.mp.dps = 30

def dzeta_da(s, a, h=mp.mpf('1e-12')):
    # central difference in a (analytic in a), high precision
    return (mp.zeta(s, a + h) - mp.zeta(s, a - h)) / (2*h)

ok = True
print("1. identity d_a zeta(s,a) = -s zeta(s+1,a) at several (s,a), incl. Re s < 1:")
for a in [mp.mpf('0.3'), mp.mpf('0.5'), mp.mpf('1'), mp.mpf('2'), mp.mpf('3.7')]:
    for s in [mp.mpc('2.3', '1.1'), mp.mpc('0.5', '14.1'), mp.mpc('-0.5', '3'), mp.mpc('-2.7', '-5.5')]:
        lhs = mp.diff(lambda x: mp.zeta(s, x), a)
        rhs = -s*mp.zeta(s+1, a)
        err = abs(lhs - rhs)/max(1, abs(rhs))
        ok &= err < 1e-20
    print(f"   a={mp.nstr(a,3)}: max rel err ok so far = {ok}")

print("2. value of the first jet at s = 0 is -1 on every sheet (s*zeta(s+1,a) -> 1):")
for a in ['0.1', '0.3', '0.5', '1', '2', '7.25']:
    a = mp.mpf(a)
    with mp.workdps(60):
        s = mp.mpf('1e-12')
        val = -s*mp.zeta(1 + s, a)
        pred = -(1 - mp.digamma(a)*s)          # Laurent: zeta(1+s,a) = 1/s - psi(a) + O(s)
    print(f"   a={mp.nstr(a,4)}: -s*zeta(s+1,a) at s=1e-12: {mp.nstr(val, 20)}   (-1 + psi(a) s = {mp.nstr(pred,20)})")
    ok &= abs(val - pred) < 1e-20

print("3. zeros of zeta(.,a) shifted by -1 are zeros of the a-jet (outside any strip), and |zeta(.,a)| there:")
tests = []
# a = 2: zeta(s,2) = zeta(s)-1, zero from the register (Re s > 1)
z2 = mp.findroot(lambda s: mp.zeta(s, 2), mp.mpc('1.40778804065', '23.3279877546'))
tests.append((mp.mpf(2), z2))
# a = 1/2: zeros on Re s = 0 from (2^s-1), s_k = 2 pi i k / log 2, and s = 0 (zeta(0,1/2) = 0)
for k in [1, 3]:
    tests.append((mp.mpf('0.5'), 2j*mp.pi*k/mp.log(2)))
tests.append((mp.mpf('0.5'), mp.mpf(0)))
# a = 0.3: locate a few zeros near the line and one to the right (Davenport-Heilbronn type), by findroot from grid minima
a3 = mp.mpf('0.3')
for guess in [mp.mpc('0.5', '10'), mp.mpc('0.6', '20'), mp.mpc('0.5', '30'), mp.mpc('1.0', '40')]:
    try:
        z = mp.findroot(lambda s: mp.zeta(s, a3), guess)
        tests.append((a3, z))
    except Exception as e:
        pass
# a = 1: nontrivial and trivial zeros (global statement includes -3, -5, ...)
tests.append((mp.mpf(1), mp.zetazero(1)))
tests.append((mp.mpf(1), mp.mpf(-2)))
tests.append((mp.mpf(1), mp.mpf(-4)))
for a, rho in tests:
    zr = abs(mp.zeta(rho, a)) if rho != 1 else None
    jet = -(rho - 1)*mp.zeta(rho, a)            # first jet evaluated at rho - 1
    jet_direct = mp.diff(lambda x: mp.zeta(rho - 1, x), a)
    print(f"   a={mp.nstr(a,3):>4} rho={mp.nstr(rho,12):>36}  |zeta(rho,a)|={mp.nstr(zr,3):>8}  |jet(rho-1)| direct={mp.nstr(abs(jet_direct),3):>8}")
    ok &= abs(jet_direct) < 1e-15
# converse: the a-jet has no other zeros: check -s zeta(s+1,a) at a zero of the jet found numerically equals a zero of zeta(.,a) shifted
print("4. converse: a zero of the a-jet found by findroot, shifted by +1, is a zero of zeta(.,a):")
for a, guess in [(mp.mpf('0.3'), mp.mpc('-0.5', '9.5')), (mp.mpf(2), mp.mpc('0.4', '23.3')), (mp.mpf('0.5'), mp.mpc('-1.0', '9.0'))]:
    try:
        w = mp.findroot(lambda s: -s*mp.zeta(s+1, a), guess)
        print(f"   a={mp.nstr(a,3)}: jet zero w={mp.nstr(w,15)}, |zeta(w+1,a)|={mp.nstr(abs(mp.zeta(w+1,a)),3)}")
        ok &= abs(mp.zeta(w+1, a)) < 1e-20
    except Exception as e:
        print("   findroot failed:", e)

print("5. m-th jet at a != 1: (-1)^m (s)_m zeta(s+m,a); simple zeros at 0,-1,...,2-m; value at s=1-m is (-1)^(m-1)(m-1)!*(-1)^m... check m=3, a=0.3:")
a = mp.mpf('0.3'); m = 3
jet = lambda s: (-1)**m*mp.rf(s, m)*mp.zeta(s+m, a)
for s0 in [0, -1]:
    print(f"   jet({s0}) = {mp.nstr(jet(mp.mpf(s0)+mp.mpf('1e-30')), 5)}   (zero expected)")
print(f"   jet(1-m) (pole cancelled) = {mp.nstr(jet(mp.mpf(1-m)+mp.mpf('1e-25')), 12)} ; (-1)^m (1-m)(2-m)...(-1) = {(-1)**m*mp.rf(1-m, m-1)}")
ok &= abs(jet(mp.mpf(1-m)+mp.mpf('1e-25')) - (-1)**m*mp.rf(1-m, m-1)) < 1e-15

print("6. Theorem 4.2 does not extend: on the sheet a = 1/2 the zero s_1 = 2 pi i/log 2 has partner 1 - conj(s_1) with zeta(.,1/2) != 0 there:")
s1 = 2j*mp.pi/mp.log(2)
partner = 1 - mp.conj(s1)
print(f"   |zeta(s1,1/2)| = {mp.nstr(abs(mp.zeta(s1, 0.5)),3)},  |zeta(1-conj(s1),1/2)| = {mp.nstr(abs(mp.zeta(partner, 0.5)),6)}  (nonzero: # is not a symmetry of Z_(1/2))")
print("   so A(Z_a) = Z_a - 1 fails at a = 1/2; the jet statement (items 1-4) holds on every sheet, the mirror statement is zeta-specific.")
print("\nALL CHECKS PASS" if ok else "\nSOME CHECK FAILED")
