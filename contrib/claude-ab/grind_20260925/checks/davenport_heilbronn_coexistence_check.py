#!/usr/bin/env python3
"""Check for note 17_, section 10: coexistence of a function with its translate does not force zeros onto a line.

The Davenport-Heilbronn function (Titchmarsh, The Theory of the Riemann Zeta-Function, 2nd ed., section 10.25):
  f(s) = ((1 - i k)/2) L(s, chi) + ((1 + i k)/2) L(s, conj chi),  chi mod 5 with chi(2) = i,
  k = (sqrt(10 - 2 sqrt5) - 2)/(sqrt5 - 1).
It satisfies a functional equation of the same shape as zeta's, f(s) = X(s) f(1 - s), with
  X(s) = 5^{1/2 - s} 2 (2 pi)^{s-1} Gamma(1 - s) cos(pi s / 2),
and it has zeros off Re s = 1/2 (Spira, Math. Comp. 63 (1994) 747-748, reports 0.808517 + 85.699348 i among others).
Its translate f(s+1) 'coexists' with it exactly as zeta(s+1) coexists with zeta(s).

claude-ab, model claude-opus-5-5 (Opus 5.5, maximum reasoning effort), 25 September 2026.
"""
import os
import mpmath as mp
mp.mp.dps = 30
out = []
def say(s=""):
    print(s); out.append(s)

chi = [0, 1, 1j, -1j, -1]                 # chi(n) for n mod 5: chi(2) = i, chi(3) = -i, chi(4) = -1
chib = [mp.conj(c) for c in chi]
k = (mp.sqrt(10 - 2 * mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1)
def f(s):
    return (1 - 1j * k) / 2 * mp.dirichlet(s, chi) + (1 + 1j * k) / 2 * mp.dirichlet(s, chib)
def X(s):
    return 5 ** (mp.mpf(1) / 2 - s) * 2 * (2 * mp.pi) ** (s - 1) * mp.gamma(1 - s) * mp.cos(mp.pi * s / 2)

say("kappa = %s" % mp.nstr(k, 20))
for s in [mp.mpc(0.3, 7.1), mp.mpc(0.8, 20.5), mp.mpc(-0.4, 3.3)]:
    say("functional equation at s = %-14s |f(s) - X(s) f(1-s)| / |f(s)| = %s" % (mp.nstr(s, 5), mp.nstr(abs(f(s) - X(s) * f(1 - s)) / abs(f(s)), 3)))
z0 = mp.findroot(f, mp.mpc(0.808517, 85.699348))
say("zero found near 0.808517 + 85.699348i: %s   |f| = %s" % (mp.nstr(z0, 15), mp.nstr(abs(f(z0)), 3)))
say("its real part differs from 1/2 by %s; its reflection 1 - conj(z0) = %s is also a zero: |f| = %s"
    % (mp.nstr(mp.re(z0) - mp.mpf(1) / 2, 10), mp.nstr(1 - mp.conj(z0), 12), mp.nstr(abs(f(1 - mp.conj(z0))), 3)))
g = lambda s: f(s + 1)
say("the translate g(s) = f(s+1) vanishes at z0 - 1 = %s: |g| = %s  (off Re s = -1/2 by %s)"
    % (mp.nstr(z0 - 1, 12), mp.nstr(abs(g(z0 - 1)), 3), mp.nstr(mp.re(z0 - 1) + mp.mpf(1) / 2, 10)))
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "davenport_heilbronn_coexistence_check_OUTPUT.txt"), "w") as fh:
    fh.write("\n".join(out) + "\n")
