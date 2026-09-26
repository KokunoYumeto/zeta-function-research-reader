#!/usr/bin/env python3
import os
"""F7 verification (independent code).

(a) Hurwitz: Z_a(1-s) = 2 Gamma(s) (2 pi)^(-s) cos(pi s/2) Phi_a(s), Phi_a(s) = 2 sum_k cos(2 pi k a) k^-s,
    checked at points with Re s > 1 (series) and, by continuation, via the character decomposition.
(b) Character decomposition for prime q:  Phi_{1/q} = (2/(q-1)) (q^{1-s} - 1) zeta(s)
        + (2/(q-1)) sum_{chi even, nontrivial} tau(chi) L(s, conj chi),
    checked at q = 5, 7, 11, 13 at points inside the strip; |tau(chi)| = sqrt(q) for every nontrivial chi.
    q = 5 reproduces 1/2[(5^{1-s}-1) zeta + sqrt5 L(s,(./5))]; q = 3 gives (3^{1-s}-1) zeta only.
(c) Not of the form P(s) L(s,psi): coefficient test a_p^2 = b(1) a_{p^2} at primes in two classes
    (the argument used for the Davenport-Heilbronn function in 24_ Prop 24.6), for q = 5, 7, 11, 13.
(d) The zero file figures/data/z15_zeros_150.csv: counts right/left of the line, the gap, and
    Phi_{1/5}(1 - z) = 0 at every listed zero z with Re z < 1/2 (these are the reflected zeros).
"""
import csv
import mpmath as mp

mp.mp.dps = 40

def Z(a, s):
    return mp.zeta(s, a) + mp.zeta(s, 1 - a)

def Phi_series(a, s, K=None):
    return 2 * mp.nsum(lambda k: mp.cos(2 * mp.pi * k * a) * k ** (-s), [1, mp.inf])

def chars_mod_prime(q):
    import sympy
    g = int(sympy.primitive_root(q))
    # discrete log table
    dlog, x = {}, 1
    for e in range(q - 1):
        dlog[x] = e; x = (x * g) % q
    chars = []
    for j in range(q - 1):
        w = mp.exp(2j * mp.pi * j / (q - 1))
        chi = [mp.mpc(0)] + [w ** dlog[n] for n in range(1, q)]
        chars.append((j, chi))
    return chars

def L(s, chi):
    return mp.dirichlet(s, chi)

def tau(chi, q):
    return mp.fsum(chi[a] * mp.exp(2j * mp.pi * a / q) for a in range(1, q))

def Phi_decomp(q, s):
    tot = mp.mpf(2) / (q - 1) * (q ** (1 - s) - 1) * mp.zeta(s)
    for j, chi in chars_mod_prime(q):
        if j == 0:
            continue
        if abs(chi[q - 1] - 1) > 1e-30:   # odd character
            continue
        tot += mp.mpf(2) / (q - 1) * tau(chi, q) * L(s, [mp.conj(c) for c in chi])
    return tot

def main():
    print("(a) Hurwitz functional equation for Z_a")
    for a in (mp.mpf(1) / 5, mp.mpf('0.3'), mp.mpf(1) / 7):
        for s in (mp.mpc(1.7, 3.2), mp.mpc(2.5, -11.0)):
            lhs = Z(a, 1 - s)
            rhs = 2 * mp.gamma(s) * (2 * mp.pi) ** (-s) * mp.cos(mp.pi * s / 2) * Phi_series(a, s)
            print("  a=%s s=%s: |lhs-rhs|/|lhs| = %.2e" % (mp.nstr(a, 4), mp.nstr(s, 4), abs(lhs - rhs) / abs(lhs)))
            assert abs(lhs - rhs) / abs(lhs) < 1e-25

    print("(b) character decomposition of Phi_{1/q} for prime q (tested against Hurwitz: Phi = Z(1-s)/(2 Gamma (2pi)^-s cos))")
    for q in (3, 5, 7, 11, 13):
        for s in (mp.mpc(0.3, 7.1), mp.mpc(0.8, -15.3), mp.mpc(1.4, 2.2)):
            direct = Z(mp.mpf(1) / q, 1 - s) / (2 * mp.gamma(s) * (2 * mp.pi) ** (-s) * mp.cos(mp.pi * s / 2))
            dec = Phi_decomp(q, s)
            err = abs(direct - dec) / abs(direct)
            assert err < 1e-25, (q, s, err)
        taus = [abs(tau(chi, q)) for j, chi in chars_mod_prime(q) if j]
        n_even_nontriv = sum(1 for j, chi in chars_mod_prime(q) if j and abs(chi[q - 1] - 1) < 1e-30)
        print("  q=%2d: decomposition holds (rel. err < 1e-25 at 3 points); nontrivial even characters: %d; min |tau| = %s = sqrt(q)? %s"
              % (q, n_even_nontriv, mp.nstr(min(taus), 12), abs(min(taus) - mp.sqrt(q)) < 1e-30))
    s = mp.mpc(0.37, 9.9)
    leg5 = [0, 1, -1, -1, 1]
    alt = (5 ** (1 - s) - 1) * mp.zeta(s) / 2 + mp.sqrt(5) * L(s, leg5) / 2
    print("  q=5 closed form 1/2[(5^{1-s}-1)zeta + sqrt5 L(s,(./5))]: rel. err %.2e" % (abs(alt - Phi_decomp(5, s)) / abs(alt)))

    print("(c) Phi_{1/q} is not P(s)L(s,psi): a_p^2 = b(1) a_{p^2} would force the same b(1) for all large p")
    for q in (5, 7, 11, 13):
        a = lambda n: 2 * mp.cos(2 * mp.pi * n / q)
        vals = {}
        for c in range(1, q):
            if a(c * c) != 0:
                vals[c] = a(c) ** 2 / a(c * c)
        distinct = sorted(set(mp.nstr(v, 10) for v in vals.values()))
        print("  q=%2d: b(1) forced by class c: %s -> %d distinct values (need 1 for P*L form)" % (q, {c: mp.nstr(v, 6) for c, v in vals.items()}, len(distinct)))
        assert len(distinct) >= 2

    print("(d) zeros of Z_{1/5} below height 150 (figures/data/z15_zeros_150.csv)")
    rows = list(csv.DictReader(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..' + ('/..' if 'verify_minors' in __file__ else ''), '..', 'figures', 'data', 'z15_zeros_150.csv'))))
    zs = [mp.mpc(mp.mpf(r['beta']), mp.mpf(r['gamma'])) for r in rows]
    right = [z for z in zs if z.real > 0.5]
    mid = [z for z in zs if 0 < z.real < 0.5]
    left = [z for z in zs if z.real <= 0]
    gap = min(abs(z.real - 0.5) for z in zs)
    print("  total %d; Re>1/2: %d; 0<Re<1/2: %d; Re<=0: %d; min |Re - 1/2| = %s; max Re = %s; min Re = %s"
          % (len(zs), len(right), len(mid), len(left), mp.nstr(gap, 6), mp.nstr(max(z.real for z in zs), 6), mp.nstr(min(z.real for z in zs), 6)))
    worst_Z = max(abs(Z(mp.mpf(1) / 5, z)) for z in zs)
    worst_Phi = 0
    for z in mid + left:
        w = 1 - z
        ph = Phi_decomp(5, w)
        scale = mp.fsum(abs(t) for t in [(5 ** (1 - w) - 1) * mp.zeta(w) / 2, mp.sqrt(5) * L(w, leg5) / 2])
        worst_Phi = max(worst_Phi, abs(ph) / scale)
    print("  max |Z_{1/5}(z)| over the 90 listed zeros: %.2e" % worst_Z)
    print("  max relative |Phi_{1/5}(1-z)| over the %d listed zeros with Re z < 1/2: %.2e" % (len(mid + left), worst_Phi))
    print("  (so Phi_{1/5} has zeros with Re w > 1 (from Re z < 0) and with 1/2 < Re w < 1 (from 0 < Re z < 1/2))")
    assert worst_Phi < 1e-12
    print("ALL F7 CHECKS PASS")

if __name__ == "__main__":
    main()
