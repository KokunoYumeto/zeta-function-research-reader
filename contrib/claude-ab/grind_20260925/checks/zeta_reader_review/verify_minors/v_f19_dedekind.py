#!/usr/bin/env python3
"""F19 verification (independent code): the separator inputs for Dedekind zeta functions.

Fields (abelian, so zeta_K is a product of Dirichlet L-functions):
  Q(i):            d = -4,  (r1,r2) = (0,1), n = 2, zeta_K = zeta L(s, chi_-4)
  Q(sqrt5):        d = 5,   (r1,r2) = (2,0), n = 2, zeta_K = zeta L(s, (./5))
  cubic, cond. 7:  d = 49,  (r1,r2) = (3,0), n = 3, zeta_K = zeta L(s,chi) L(s,conj chi), chi cubic mod 7
  Q(zeta_5):       d = 125, (r1,r2) = (0,2), n = 4, zeta_K = zeta L(chi) L(chi^2) L(chi^3), chi mod 5 of order 4
Checks:
 (a) Gamma_R(1-s)Gamma_R(1+s) = 1/cos(pi s/2), Gamma_C(1-s)Gamma_C(1+s) = s/(pi sin pi s)   (Gamma_C = 2(2pi)^{-s}Gamma(s))
 (b) Lambda_K(s) = Lambda_K(1-s)
 (c) matched rates for G_K(s) = xi_K(s) xi_K(s+1), xi_K = s(s-1)Lambda_K: the local polynomial order
     [log R(80) - log R(40)]/log 2 of R(t) = |G_K(x+it)| e^{alpha t} on x in {-1.5,-1,-0.5,0,0.5,1,1.5} stays bounded
     for alpha = n pi/2, while alpha = n pi/2 -+ pi/2 gives slopes of order -+ (pi/2)*40/log 2 = -+ 90.6;
     and log R(t) on x = 0 is bounded below on [2, 80] (no zero, polynomial lower bound) for alpha = n pi/2.
 (d) the 3-4-1 inequality zeta_K(sigma)^3 |zeta_K(sigma+it)|^4 |zeta_K(sigma+2it)| >= 1 on a grid (sigma > 1).
"""
import mpmath as mp

mp.mp.dps = 30

def GR(s): return mp.pi ** (-s / 2) * mp.gamma(s / 2)
def GC(s): return 2 * (2 * mp.pi) ** (-s) * mp.gamma(s)

def chars(q, order_gen):
    # characters mod prime q from a primitive root
    import sympy
    g = int(sympy.primitive_root(q))
    dlog, x = {}, 1
    for e in range(q - 1):
        dlog[x] = e; x = (x * g) % q
    def chi(j):
        w = mp.exp(2j * mp.pi * j / (q - 1))
        return [0] + [w ** dlog[n] for n in range(1, q)]
    return chi

chi5 = chars(5, 4); chi7 = chars(7, 6)
FIELDS = {
    'Q(i)':       dict(d=4, r1=0, r2=1, Ls=[[0, 1, 0, -1]]),
    'Q(sqrt5)':   dict(d=5, r1=2, r2=0, Ls=[[0, 1, -1, -1, 1]]),
    'cubic7':     dict(d=49, r1=3, r2=0, Ls=[chi7(2), chi7(4)]),          # order-3 characters (even)
    'Q(zeta5)':   dict(d=125, r1=0, r2=2, Ls=[chi5(1), chi5(2), chi5(3)]),
}

def zetaK(F, s):
    v = mp.zeta(s)
    for c in F['Ls']:
        v *= mp.dirichlet(s, c)
    return v

def LamK(F, s):
    return mp.mpf(F['d']) ** (s / 2) * GR(s) ** F['r1'] * GC(s) ** F['r2'] * zetaK(F, s)

def xiK(F, s):
    return s * (s - 1) * LamK(F, s)

def GK(F, s):
    return xiK(F, s) * xiK(F, s + 1)

def main():
    print("(a) Gamma reflection products")
    for s in (mp.mpc(0.3, 2.0), mp.mpc(-1.2, 7.5), mp.mpc(0.9, -13.0)):
        e1 = abs(GR(1 - s) * GR(1 + s) * mp.cos(mp.pi * s / 2) - 1)
        e2 = abs(GC(1 - s) * GC(1 + s) - s / (mp.pi * mp.sin(mp.pi * s))) / abs(s / (mp.pi * mp.sin(mp.pi * s)))
        print("  s=%s: |G_R(1-s)G_R(1+s)cos(pi s/2) - 1| = %.1e ; rel err Gamma_C identity %.1e" % (mp.nstr(s, 4), float(e1), float(e2)))
        assert e1 < 1e-25 and e2 < 1e-25
    print("(b) functional equations")
    for name, F in FIELDS.items():
        # sanity: the even/odd parity of the L-factors matches the signature (all even for totally real)
        err = max(abs(LamK(F, s) - LamK(F, 1 - s)) / abs(LamK(F, s)) for s in (mp.mpc(0.2, 3.3), mp.mpc(0.71, 8.9), mp.mpc(-0.5, 1.7)))
        print("  %-9s Lambda_K(s) = Lambda_K(1-s): max rel err %.1e" % (name, float(err)))
        assert err < 1e-20
    print("(c) matched rates for G_K = xi_K(s) xi_K(s+1)")
    for name, F in FIELDS.items():
        n = F['r1'] + 2 * F['r2']
        alpha = n * mp.pi / 2
        slopes = {}
        for dal in (-mp.pi / 2, 0, mp.pi / 2):
            sl = []
            for x in (-1.5, -1, -0.5, 0, 0.5, 1, 1.5):
                R = lambda t: mp.log(abs(GK(F, mp.mpc(x, t)))) + (alpha + dal) * t
                sl.append((R(80) - R(40)) / mp.log(2))
            slopes[float(dal)] = (min(sl), max(sl))
        lowest = min(mp.log(abs(GK(F, mp.mpc(0, t)))) + alpha * t for t in mp.linspace(2, 80, 79))
        print("  %-9s n=%d alpha=n pi/2: local order in [%.2f, %.2f]; with alpha - pi/2: [%.1f, %.1f]; with alpha + pi/2: [%.1f, %.1f]; min_{2<=t<=80} log(|G_K(it)|e^{alpha t}) = %s"
              % (name, n, slopes[0.0][0], slopes[0.0][1], slopes[float(-mp.pi / 2)][0], slopes[float(-mp.pi / 2)][1],
                 slopes[float(mp.pi / 2)][0], slopes[float(mp.pi / 2)][1], mp.nstr(lowest, 5)))
        assert -2 < slopes[0.0][0] and slopes[0.0][1] < 25
        assert slopes[float(mp.pi / 2)][0] > 60 and slopes[float(-mp.pi / 2)][1] < -60
    print("(d) 3-4-1 inequality for zeta_K on a grid")
    for name, F in FIELDS.items():
        mn = mp.inf
        for sig in (1.02, 1.1, 1.5):
            for t in mp.linspace(0.5, 60, 60):
                v = abs(zetaK(F, mp.mpf(sig))) ** 3 * abs(zetaK(F, mp.mpc(sig, t))) ** 4 * abs(zetaK(F, mp.mpc(sig, 2 * t)))
                mn = min(mn, v)
        print("  %-9s min over grid = %s (>= 1)" % (name, mp.nstr(mn, 5)))
        assert mn >= 1
    print("ALL F19 CHECKS PASS")

if __name__ == "__main__":
    main()
