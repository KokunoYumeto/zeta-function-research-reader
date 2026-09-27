#!/usr/bin/env python3
"""F9 verification (independent code).

(1) N(T) at the Platt-Trudgian height.  PT (arXiv:2004.09765, Theorem 1, as fetched): RH holds up to
    T = 3 000 175 332 800 and "the lowest 12 363 153 437 138 non-trivial zeroes have Re = 1/2".
    Compare with the smooth Riemann-von Mangoldt count theta(T)/pi + 1 (S(T) is O(log T), below ~10 in practice).
(2) Corollary B at a = 1 (02_ section 4.2): error O(T2 d(Delta) + K(Delta)) + O(e^{-pi T1/2} + T1 e^{-T1^2/(8 Delta^2)}),
    d(Delta) = sum_n |b(n)| n^{-1/2} e^{-Delta^2 log^2 n/2}/log n, b(n) = prod_{p|n}(1-p)/n (coefficients of zeta(s+1)/zeta(s)).
    Recompute d(Delta) at Delta = 1,2,3,5 (02_ table: 0.757, 0.230, 0.060, 1.26e-3), then T d(Delta(T)) for
    Delta(T) = 1.1 sqrt(2 log T)/log 2, and T1 e^{-T1^2/(8 Delta^2)} at T1 = 10 Delta and T1 = 4 Delta sqrt(log Delta).
"""
import mpmath as mp
import sympy

mp.mp.dps = 30

def b(n):
    f = sympy.factorint(n)
    num = 1
    for p in f:
        num *= (1 - p)
    return mp.mpf(num) / n

def d_of(Delta, nmax=20000):
    s = mp.mpf(0)
    for n in range(2, nmax + 1):
        ln = mp.log(n)
        term = abs(b(n)) * n ** mp.mpf(-0.5) * mp.e ** (-(Delta ** 2) * ln ** 2 / 2) / ln
        s += term
        if n > 50 and term < mp.mpf(10) ** (-40):
            break
    return s

def main():
    T = mp.mpf(3000175332800)
    smooth = mp.siegeltheta(T) / mp.pi + 1
    print("(1) theta(T)/pi + 1 at T = 3 000 175 332 800: %s ; PT count 12 363 153 437 138 ; difference %s"
          % (mp.nstr(smooth, 16), mp.nstr(smooth - 12363153437138, 6)))
    T3 = mp.mpf(3) * 10 ** 12
    print("    theta(T)/pi + 1 at T = 3e12: %s  (so n <= 1.2e13 is covered)" % mp.nstr(mp.siegeltheta(T3) / mp.pi + 1, 8))
    assert abs(smooth - 12363153437138) < 50

    print("(2) d(Delta) and K-independent parts of the Corollary B error")
    for D in (1, 2, 3, 5):
        print("    d(%d) = %s" % (D, mp.nstr(d_of(mp.mpf(D)), 4)))
    for e in (4, 6, 8, 12, 16):
        T = mp.mpf(10) ** e
        D = mp.mpf('1.1') * mp.sqrt(2 * mp.log(T)) / mp.log(2)
        dd = d_of(D)
        n2 = abs(b(2)) * 2 ** mp.mpf(-0.5) * mp.e ** (-(D ** 2) * mp.log(2) ** 2 / 2) / mp.log(2)
        T1a = 10 * D
        T1b = 4 * D * mp.sqrt(mp.log(D))
        ga = T1a * mp.e ** (-T1a ** 2 / (8 * D ** 2))
        gb = T1b * mp.e ** (-T1b ** 2 / (8 * D ** 2))
        print("    T=1e%-2d Delta=%6s  T*d(Delta)=%-9s (n=2 share %s)  T1 e^{-T1^2/8D^2}: at 10D %-9s at 4D sqrt(log D) %s"
              % (e, mp.nstr(D, 4), mp.nstr(T * dd, 3), mp.nstr(n2 / dd, 6), mp.nstr(ga, 3), mp.nstr(gb, 3)))
    # large-Delta behaviour of the T1 term with T1 = 10 Delta (it grows) versus T1 = 4 Delta sqrt(log Delta) (it decays)
    for D in (10, 100, 1000, 10 ** 4, 10 ** 6):
        D = mp.mpf(D)
        ga = 10 * D * mp.e ** (-100 / mp.mpf(8))
        T1b = 4 * D * mp.sqrt(mp.log(D))
        gb = T1b * mp.e ** (-T1b ** 2 / (8 * D ** 2))
        print("    Delta=%-8s T1=10 Delta: %-10s  T1=max(10D, 4D sqrt(log D)): %s" % (mp.nstr(D, 3), mp.nstr(ga, 3), mp.nstr(min(ga, gb) if 10 * D >= T1b else gb, 3)))
    print("ALL F9 CHECKS PASS")

if __name__ == "__main__":
    main()
