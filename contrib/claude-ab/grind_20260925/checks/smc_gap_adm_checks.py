#!/usr/bin/env python3
"""Checks for note 18_ (content map of SMC, GAP and ADM, 25 September 2026 continuations).

 SMC7.2  int |Theta a(1/2+it)|^2 dt = (pi/2) int_0^oo |a(u)|^2 du, Theta a(s) = (1/2) int a(u) u^s du/u.
 GAP3.2  Theta a_{t,1} = g_t, a_{t,1}(u) = e^{t/4}/sqrt(pi t) u^{-1/2} exp(-(log u - t)^2/(4t)), g_t(s) = e^{t s^2}.
 GAP3.4  Theta(a *_M b) = 2 Theta a Theta b, (a *_M b)(u) = int a(u/v) b(v) dv/v.
 GAP7.1  g_t(1-s) = e^{t(1-2s)} g_t(s).
 ADM2.7  |1 + rho#| >= (1+|Im rho|)/sqrt2 for 0 < Re rho < 1 (sampled), and ADM3.3 |d_r(rho)| <= r - 1.
 ADM6    the separator's divisor G(s) = F0(s) F0(s+1) vanishes on Z and on Z - 1 and not at s = 0, -1.
claude-ab, model claude-opus-5-5 (Opus 5.5, maximum reasoning effort), 25 September 2026.
"""
import os
import mpmath as mp
mp.mp.dps = 25
out = []
def say(s=""):
    print(s); out.append(s)

def Theta(a, s):
    return mp.quad(lambda x: a(mp.e ** x) * mp.e ** (s * x), [-mp.inf, -5, 0, 5, mp.inf]) / 2

a = lambda u: mp.e ** (-(mp.log(u)) ** 2)                 # a(e^x) = e^{-x^2}: in A, with Theta a(s) = (sqrt(pi)/2) e^{s^2/4}
b = lambda u: mp.e ** (-(mp.log(u) - 1) ** 2 / 2)        # b(e^x) = e^{-(x-1)^2/2}: Theta b(s) = (sqrt(2 pi)/2) e^{s + s^2/2}
# SMC7.2 (outer integral over |t| <= 30; the integrand is (pi/4) e^{(1/4 - t^2)/2}, below e^{-449} beyond)
lhs = mp.quad(lambda t: abs(Theta(a, mp.mpc(0.5, t))) ** 2, [-30, -10, 0, 10, 30])
rhs = mp.pi / 2 * mp.quad(lambda x: abs(a(mp.e ** x)) ** 2 * mp.e ** x, [-mp.inf, 0, mp.inf])
say("SMC7.2: int|Theta a(1/2+it)|^2 dt = %s ; (pi/2) int |a|^2 du = %s ; closed form (pi/2) sqrt(pi/2) e^{1/8} = %s"
    % (mp.nstr(lhs, 15), mp.nstr(rhs, 15), mp.nstr(mp.pi / 2 * mp.sqrt(mp.pi / 2) * mp.e ** (mp.mpf(1) / 8), 15)))
# GAP3.2
t = mp.mpf("0.7")
at = lambda u: mp.e ** (t / 4) / mp.sqrt(mp.pi * t) * u ** mp.mpf(-0.5) * mp.e ** (-(mp.log(u) - t) ** 2 / (4 * t))
for s in [mp.mpc(0.5, 2), mp.mpc(-0.3, 5), mp.mpc(1.2, -1)]:
    say("GAP3.2 at s = %-12s Theta a_{t,1} = %-38s g_t(s) = %s" % (mp.nstr(s, 4), mp.nstr(Theta(at, s), 14), mp.nstr(mp.e ** (t * s ** 2), 14)))
# GAP3.4: the multiplicative convolution of a and b is c(e^x) = sqrt(2 pi/3) e^{-(x-1)^2/3} (Gaussian convolution, completed square)
cfun = lambda u: mp.sqrt(2 * mp.pi / 3) * mp.e ** (-(mp.log(u) - 1) ** 2 / 3)
x0 = mp.mpf("0.37")
say("GAP3.4: convolution at x = 0.37 by quadrature = %s ; closed form = %s"
    % (mp.nstr(mp.quad(lambda y: a(mp.e ** (x0 - y)) * b(mp.e ** y), [-mp.inf, 0, mp.inf]), 15), mp.nstr(cfun(mp.e ** x0), 15)))
for s in [mp.mpc(0.4, 1.3), mp.mpc(-0.8, 2.1)]:
    say("GAP3.4 at s = %-10s Theta(a*b) = %-36s 2 Theta a Theta b = %s" % (mp.nstr(s, 3), mp.nstr(Theta(cfun, s), 13), mp.nstr(2 * Theta(a, s) * Theta(b, s), 13)))
# GAP7.1
for s in [mp.mpc(0.2, 3), mp.mpc(2, -1)]:
    say("GAP7.1 at s = %-8s g_t(1-s) - e^{t(1-2s)} g_t(s) = %s" % (mp.nstr(s, 3), mp.nstr(mp.e ** (t * (1 - s) ** 2) - mp.e ** (t * (1 - 2 * s)) * mp.e ** (t * s ** 2), 3)))
# ADM2.7 and ADM3.3 on a grid of 0 < Re rho < 1
worst = mp.inf; worst_d = 0; r = mp.mpf(3)
for i in range(1, 50):
    for gg in [0, 0.5, 3, 14.13, 100, 1e4]:
        rho = mp.mpc(i / 50, gg)
        ratio = abs(1 + (1 - mp.conj(rho))) / ((1 + abs(mp.im(rho))) / mp.sqrt(2))
        worst = min(worst, ratio)
        d = abs(mp.e ** (-1j * mp.im(rho) * mp.log(r)) * (r ** mp.re(rho) - r ** (1 - mp.re(rho))))
        worst_d = max(worst_d, d)
say("ADM2.7: min over grid of |1+rho#| / ((1+|Im rho|)/sqrt2) = %s (must be >= 1)" % mp.nstr(worst, 6))
say("ADM3.3: max over grid of |d_r(rho)| at r = 3: %s (bound r - 1 = 2)" % mp.nstr(worst_d, 6))
# ADM6 divisor
F0 = lambda s: s * (s - 1) / 8 * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)
G = lambda s: F0(s) * F0(s + 1)
rho1 = mp.zetazero(1)
say("ADM6: |G(rho_1)| = %s, |G(rho_1 - 1)| = %s, G(0) = F0(0) F0(1) = %s (= 1/64), G(-1) = F0(-1) F0(0) = %s (= pi/192 = %s)"
    % (mp.nstr(abs(G(rho1)), 3), mp.nstr(abs(G(rho1 - 1)), 3), mp.nstr(mp.limit(G, 0), 12), mp.nstr(mp.limit(G, -1), 12), mp.nstr(mp.pi / 192, 12)))
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "smc_gap_adm_checks_OUTPUT.txt"), "w") as fh:
    fh.write("\n".join(out) + "\n")
