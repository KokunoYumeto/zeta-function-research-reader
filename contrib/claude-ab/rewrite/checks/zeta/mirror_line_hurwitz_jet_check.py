#!/usr/bin/env python3
"""Checks for note 17_ (the mirror line Re s = -1/2, the Hurwitz jets, and the two centres of reflection).

claude-ab lane, model claude-opus-5-5 (Opus 5.5, maximum reasoning effort), 25 September 2026.

Parts
 1. Hurwitz first jet: d/dt zeta(s, 1+t) at t = 0 equals -s zeta(s+1)  (finite differences, several s).
    s*zeta(1+s) -> 1 as s -> 0  (the pole at 1, carried to 0 by the shift, becomes the value 1).
    At s = rho - 1 (rho a zeta zero) the first jet vanishes while zeta(s) itself is nonzero.
 2. The two reflections A(s) = -conj(s) (centre 0) and B(s) = 1 - conj(s) (centre 1/2):
    B o A = translation by 1; A(rho) = rho - 1 exactly when Re rho = 1/2.
 3. Hopf / Clifford-torus picture: [s : s-1] lies on |w| = 1 iff Re s = 1/2; [s : s+1] iff Re s = -1/2.
    The normalized pairs trace the two halves of Gamma = {(e^{i psi}, -e^{-i psi})/sqrt 2}.
 4. Explicit formula with Gaussian test functions: the pairing centred at 1/2 (Weil's g*) gives a real sum;
    the pairing centred at 0 gives a non-real sum.  Zero side and prime side are computed independently.
"""
import math, cmath
import mpmath as mp

mp.mp.dps = 30
out = []
def say(s=""):
    print(s); out.append(s)

say("claude-ab mirror/Hurwitz checks; mpmath %s, dps = %d" % (mp.__version__, mp.mp.dps))
gam = [mp.im(mp.zetazero(k)) for k in range(1, 11)]
say("first zero heights: " + ", ".join(mp.nstr(g, 12) for g in gam[:4]) + ", ...")

# ---------- 1. Hurwitz first jet ----------
say("\n1. Hurwitz first jet  d/dt zeta(s,1+t)|_{t=0} = -s zeta(s+1)")
for s in [mp.mpc(2.3, 1.1), mp.mpc(0.5, 14.134725), mp.mpc(-0.5, 3.0), mp.mpc(0.25, -7.5)]:
    h = mp.mpf("1e-12")
    fd = (mp.zeta(s, 1 + h) - mp.zeta(s, 1 - h)) / (2 * h)
    rhs = -s * mp.zeta(s + 1)
    say("   s = %-28s  central difference = %-40s  -s zeta(s+1) = %-40s |diff| = %s"
        % (mp.nstr(s, 8), mp.nstr(fd, 15), mp.nstr(rhs, 15), mp.nstr(abs(fd - rhs), 3)))
for e in ["1e-5", "1e-10", "1e-20"]:
    with mp.workdps(80):
        s = mp.mpf(e)
        v = s * mp.zeta(1 + s)
    say("   s = %-6s  s*zeta(1+s) = %s   (1 + euler*s = %s)" % (e, mp.nstr(v, 25), mp.nstr(1 + mp.euler * mp.mpf(e), 25)))
say("   Zero velocity under the Hurwitz shift: rho'(0) = rho zeta(rho+1)/zeta'(rho)  (read on Re s = 3/2)")
for k in range(3):
    rho = mp.mpc(0.5, gam[k])
    v = rho * mp.zeta(rho + 1) / mp.zeta(rho, derivative=1)
    tt = mp.mpf("1e-8")
    r_p = mp.findroot(lambda s: mp.zeta(s, 1 + tt), rho)
    r_m = mp.findroot(lambda s: mp.zeta(s, 1 - tt), rho)
    say("   k=%d  formula = %-34s  (root(t) - root(-t))/2t = %s" % (k + 1, mp.nstr(v, 12), mp.nstr((r_p - r_m) / (2 * tt), 12)))
say("   At the mirror points s = rho_k - 1:")
for k in range(3):
    rho = mp.mpc(0.5, gam[k])
    s = rho - 1
    jet = -s * mp.zeta(s + 1)
    say("   k=%d  s = %-26s |zeta(s)| = %-12s |first jet| = %s"
        % (k + 1, mp.nstr(s, 12), mp.nstr(abs(mp.zeta(s)), 8), mp.nstr(abs(jet), 3)))
say("   Direct t-derivative (mpmath diff of t -> zeta(s,1+t)) at the mirror points s = rho_k - 1:")
for k in range(3):
    s = mp.mpc(0.5, gam[k]) - 1
    fdk = mp.diff(lambda t: mp.zeta(s, 1 + t), 0)          # adaptive numerical derivative in t
    ref = mp.diff(lambda t: mp.zeta(s + mp.mpf("0.3"), 1 + t), 0)
    say("   k=%d  |d/dt zeta(s,1+t)| at t = 0: %s   (for comparison, at s + 0.3: %s)" % (k + 1, mp.nstr(abs(fdk), 3), mp.nstr(abs(ref), 6)))
s1 = mp.mpc(-0.6, 8.3)
for m in (2, 3):
    fd = mp.diff(lambda t: mp.zeta(s1, 1 + t), 0, m)
    rhs = (-1) ** m * mp.rf(s1, m) * mp.zeta(s1 + m)
    say("   m=%d jet formula at s = -0.6+8.3i (Re s < 1): mp.diff = %s, formula = %s" % (m, mp.nstr(fd, 12), mp.nstr(rhs, 12)))
say("   m-th jet: (-1)^m (s)_m zeta(s+m) vanishes at s = rho_1 - m:")
for m in [2, 3]:
    s = mp.mpc(0.5, gam[0]) - m
    jet = (-1) ** m * mp.rf(s, m) * mp.zeta(s + m)
    h = mp.mpf("1e-4")
    # finite-difference m-th t-derivative (central) for comparison of the formula at a generic point
    s0 = mp.mpc(1.7, 0.9)
    fd = mp.diff(lambda t: mp.zeta(s0, 1 + t), 0, m)
    rhs = (-1) ** m * mp.rf(s0, m) * mp.zeta(s0 + m)
    say("   m=%d  |jet(rho_1 - m)| = %-10s   generic s0=1.7+0.9i: mp.diff = %s, formula = %s"
        % (m, mp.nstr(abs(jet), 3), mp.nstr(fd, 12), mp.nstr(rhs, 12)))

# ---------- 2. the two reflections ----------
say("\n2. A(s) = -conj(s), B(s) = 1 - conj(s)")
A = lambda s: -mp.conj(s)
B = lambda s: 1 - mp.conj(s)
for s in [mp.mpc(0.3, 2.0), mp.mpc(0.5, 14.1), mp.mpc(-1.2, -0.7)]:
    say("   s = %-16s  B(A(s)) - s = %-10s  A(s) - (s-1) = %s  (zero iff Re s = 1/2)"
        % (mp.nstr(s, 6), mp.nstr(B(A(s)) - s, 5), mp.nstr(A(s) - (s - 1), 6)))

# ---------- 3. Hopf / equator ----------
say("\n3. Equator test |w| = |s - c| / |s| for the shift pairing [s : s - c]")
for c, sig in [(1, 0.5), (1, 0.3), (-1, -0.5), (-1, -0.3)]:
    vals = [abs((mp.mpc(sig, t) - c) / mp.mpc(sig, t)) for t in [0.1, 1, 14.1347, 1000]]
    say("   c = %+d, Re s = %+.1f: |w| at t = 0.1, 1, 14.13, 1000: %s"
        % (c, sig, ", ".join(mp.nstr(v, 10) for v in vals)))
say("   Normalized pairs versus Gamma(psi) = (e^{i psi}, -e^{-i psi})/sqrt2:")
worst = 0
for t in [-50, -3, -0.2, 0, 0.7, 14.134725, 200]:
    s = mp.mpc(0.5, t)                      # critical line, pair (s, s-1)
    z = (s / abs(s), (s - 1) / abs(s - 1))
    phi = mp.atan(2 * t)
    g = (mp.expj(phi), -mp.expj(-phi))
    worst = max(worst, abs(z[0] - g[0]), abs(z[1] - g[1]))
    s2 = mp.mpc(-0.5, t)                    # mirror line, pair (s, s+1)
    z2 = (s2 / abs(s2), (s2 + 1) / abs(s2 + 1))
    psi = mp.pi - phi
    g2 = (mp.expj(psi), -mp.expj(-psi))
    worst = max(worst, abs(z2[0] - g2[0]), abs(z2[1] - g2[1]))
say("   max deviation over sample points (both halves) = %s" % mp.nstr(worst, 3))
say("   critical half: psi = atan(2t) in (-pi/2, pi/2); mirror half: psi = pi - atan(2t) in (pi/2, 3pi/2)")

# ---------- 4. explicit formula, two centres ----------
say("\n4. Explicit formula with h = g * g^(centre), g(x) = exp(-(log x)^2/(2w) + i b log x)")
say("   Weil/Bombieri form: sum_rho H(rho) = H(0) + H(1) - sum_n Lambda(n)[h(n) + h(1/n)/n]")
say("                       - (log 4pi + gamma) h(1) - int_1^oo [h(x) + h(1/x)/x - 2h(1)/x] dx/(x - 1/x)")
w = mp.mpf(1)
b = mp.mpf("0.5") - gam[0]
NMAX = 200000
# von Mangoldt by sieve
lam = [0.0] * (NMAX + 1)
sieve = bytearray([1]) * (NMAX + 1); sieve[0] = sieve[1] = 0
for p in range(2, NMAX + 1):
    if sieve[p]:
        for q in range(p * p, NMAX + 1, p):
            sieve[q] = 0
        pk = p
        while pk <= NMAX:
            lam[pk] = math.log(p); pk *= p

def run(centre, w=w, b=b):
    # Mellin: g^(s) = sqrt(2 pi w) exp(w (s + i b)^2 / 2)
    if centre == "half":      # g*(x) = x^{-1} conj g(1/x);  H(s) = g^(s) conj g^(1 - conj s)
        H = lambda s: 2 * mp.pi * w * mp.e ** (w / 4) * mp.e ** (w * (s + 1j * b - mp.mpf(1) / 2) ** 2)
        h = lambda x: mp.sqrt(mp.pi * w) * mp.e ** (w / 4) * x ** (-mp.mpf(1) / 2) * mp.e ** (-(mp.log(x)) ** 2 / (4 * w) + 1j * b * mp.log(x))
    else:                     # g^flat(x) = conj g(1/x);   H(s) = g^(s) conj g^(-conj s)
        H = lambda s: 2 * mp.pi * w * mp.e ** (w * (s + 1j * b) ** 2)
        h = lambda x: mp.sqrt(mp.pi * w) * mp.e ** (-(mp.log(x)) ** 2 / (4 * w) + 1j * b * mp.log(x))
    # check the Mellin pair numerically at one point
    s_test = mp.mpc(0.3, 0.2)
    mel = mp.quad(lambda y: h(mp.e ** y) * mp.e ** (s_test * y), [-mp.inf, 0, mp.inf])
    zero_side = mp.mpf(0)
    for g_ in gam:
        for rho in (mp.mpc(0.5, g_), mp.mpc(0.5, -g_)):
            zero_side += H(rho)
    prime = mp.mpf(0)
    for n in range(2, NMAX + 1):
        if lam[n]:
            prime += lam[n] * (h(mp.mpf(n)) + h(1 / mp.mpf(n)) / n)
    arch_int = mp.quad(lambda y: (h(mp.e ** y) + mp.e ** (-y) * h(mp.e ** (-y)) - 2 * mp.e ** (-y) * h(1)) * mp.e ** y / (2 * mp.sinh(y)), [0, 1, 5, 40])
    rhs = H(0) + H(1) - prime - (mp.log(4 * mp.pi) + mp.euler) * h(1) - arch_int
    return mel, H(s_test), zero_side, rhs

for centre in ["half", "zero"]:
    mel, Ht, zs, rhs = run(centre)
    say("   centre %-4s: Mellin check |int h x^(s-1) - H(s)| at s = 0.3+0.2i: %s" % (centre, mp.nstr(abs(mel - Ht), 3)))
    say("              zero side (first 10 zeros and conjugates) = %s" % mp.nstr(zs, 15))
    say("              prime + archimedean side                  = %s" % mp.nstr(rhs, 15))
    say("              |difference| = %s ; imaginary part of the sum = %s" % (mp.nstr(abs(zs - rhs), 3), mp.nstr(mp.im(rhs), 10)))
say("   expected, centre zero: 2 pi e^{i/2} = %s (one zero dominates; w = 1, b = 1/2 - gamma_1)" % mp.nstr(2 * mp.pi * mp.expj(mp.mpf(1) / 2), 15))
say("   Second test, several zeros contributing: w = 0.1, b = -25")
for centre in ["half", "zero"]:
    mel, Ht, zs, rhs = run(centre, w=mp.mpf("0.1"), b=mp.mpf(-25))
    say("   centre %-4s: zero side = %s ; prime + archimedean side = %s ; |difference| = %s"
        % (centre, mp.nstr(zs, 15), mp.nstr(rhs, 15), mp.nstr(abs(zs - rhs), 3)))

import os
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "mirror_line_hurwitz_jet_check_OUTPUT.txt"), "w") as f:
    f.write("\n".join(out) + "\n")
