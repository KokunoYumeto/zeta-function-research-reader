#!/usr/bin/env python3
"""Independent checks of explicit formulas in the 25 September continuations (note 12_):
OZD3.3, OZD5.3/5.8, SPF8.2/GSP1.5-1.6, WHR2.4, WHR3.2, WHR8.2.
claude-ab, model claude-opus-5-5 (Opus 5.5, max effort), 25 September 2026.
"""
import sympy as sp
import mpmath as mp
mp.mp.dps = 30
out = []
def say(s):
    print(s); out.append(s)

# OZD3.3: Laplacian of h(x) exp(2t(x^2 - y^2))
x, y, t = sp.symbols('x y t', real=True)
h = sp.Function('h')(x)
phi = h * sp.exp(2 * t * (x ** 2 - y ** 2))
lap = sp.diff(phi, x, 2) + sp.diff(phi, y, 2)
claim = sp.exp(2 * t * (x ** 2 - y ** 2)) * (sp.diff(h, x, 2) + 8 * t * x * sp.diff(h, x) + 16 * t ** 2 * (x ** 2 + y ** 2) * h)
say("OZD3.3 Laplacian identity holds: %s" % (sp.simplify(lap - claim) == 0))

# OZD5.8: phi_+(1), phi_-(1) with phi = eta(x) q_r(x) e^{2t(x^2-y^2)}, eta = 1 near [0,1], R(x,y) = (1-x, y)
r = sp.symbols('r', positive=True)
q = lambda X: (r ** X - r ** (1 - X)) ** 2
ph = lambda X, Y: q(X) * sp.exp(2 * t * (X ** 2 - Y ** 2))
php = sp.simplify((ph(1, 0) + ph(0, 0)) / 2); phm = sp.simplify((ph(1, 0) - ph(0, 0)) / 2)
say("OZD5.8 phi_+(1) = (r-1)^2 (e^{2t}+1)/2: %s ; phi_-(1) = (r-1)^2 (e^{2t}-1)/2: %s" % (
    sp.simplify(php - (r - 1) ** 2 * (sp.exp(2 * t) + 1) / 2) == 0, sp.simplify(phm - (r - 1) ** 2 * (sp.exp(2 * t) - 1) / 2) == 0))

# OZD5.3: log|zeta(s)| - log|zeta(1 - conj s)| = log|chi(s)|, chi(s) = pi^{s-1/2} Gamma((1-s)/2)/Gamma(s/2)
chi = lambda s: mp.pi ** (s - mp.mpf(1) / 2) * mp.gamma((1 - s) / 2) / mp.gamma(s / 2)
worst = 0
for s in [mp.mpc(0.3, 7.1), mp.mpc(0.8, 21.4), mp.mpc(-0.4, 3.3), mp.mpc(1.2, 40.0)]:
    lhs = mp.log(abs(mp.zeta(s))) - mp.log(abs(mp.zeta(1 - mp.conj(s))))
    worst = max(worst, abs(lhs - mp.log(abs(chi(s)))))
say("OZD5.3 odd part = (1/2) log|chi| (i.e. log|zeta(s)| - log|zeta(Rs)| = log|chi|): max error %s" % mp.nstr(worst, 3))

# SPF8.2 / GSP1.5-1.6: Mellin of f0 and exceptional values of F0 = xi/4
f0 = lambda v: mp.pi / 2 * v ** 2 * (2 * mp.pi * v ** 2 - 3) * mp.exp(-mp.pi * v ** 2)
F0 = lambda s: s * (s - 1) / 8 * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)
s = mp.mpc(2.3, 1.1)
I = mp.quad(lambda v: f0(v) * v ** (s - 1), [0, 1, mp.inf])
say("SPF8.2 int f0(v) v^{s-1} dv = s(s-1)/8 pi^{-s/2} Gamma(s/2): error %s" % mp.nstr(abs(I - s * (s - 1) / 8 * mp.pi ** (-s / 2) * mp.gamma(s / 2)), 3))
say("SPF8.4/GSP1.6 F0(0)=F0(1)=1/8: %s %s ; F0(-1)=F0(2)=pi/24: %s %s" % (
    mp.nstr(mp.limit(F0, 0), 12), mp.nstr(mp.limit(F0, 1), 12), mp.nstr(F0(-1), 12), mp.nstr(F0(2), 12)))
say("   pi/24 = %s ; F0(-4) = %s, F0(5) = %s (functional equation F0(s) = F0(1-s))" % (
    mp.nstr(mp.pi / 24, 12), mp.nstr(mp.limit(F0, -4), 12), mp.nstr(F0(5), 12)))

# WHR2.4: int |x|^{2j} (1+x^2)^{-delta} dx = Gamma(j+1/2) Gamma(delta-j-1/2)/Gamma(delta)
for j, d in [(0, 1.0), (1, 2.3), (2, 4.1)]:
    num = mp.quad(lambda X: abs(X) ** (2 * j) * (1 + X ** 2) ** (-d), [-mp.inf, 0, mp.inf])
    say("WHR2.4 j=%d delta=%.1f: integral %s, Beta formula %s" % (j, d, mp.nstr(num, 12),
        mp.nstr(mp.gamma(j + 0.5) * mp.gamma(d - j - 0.5) / mp.gamma(d), 12)))

# WHR3.2: Mellin of h0(v) = (log v - 2)/(8 sqrt(pi)) exp(-(log v)^2/4) equals (s-1)/2 e^{s^2}
h0 = lambda v: (mp.log(v) - 2) / (8 * mp.sqrt(mp.pi)) * mp.exp(-mp.log(v) ** 2 / 4)
for s in [mp.mpc(0.5, 1.0), mp.mpc(-0.7, 0.4)]:
    I = mp.quad(lambda X: h0(mp.e ** X) * mp.e ** (s * X), [-mp.inf, 0, mp.inf])
    say("WHR3.2 s=%s: Mellin %s ; (s-1)/2 e^{s^2} = %s" % (mp.nstr(s, 3), mp.nstr(I, 12), mp.nstr((s - 1) / 2 * mp.e ** (s ** 2), 12)))
say("WHR3.2 int_R h0 = 2 M_S h0(1) = 0: %s" % mp.nstr(2 * mp.quad(lambda X: h0(mp.e ** X) * mp.e ** X, [-mp.inf, 0, mp.inf]), 3))

# WHR8.2: sup_y (1+(y+t)^2)/(1+y^2) = (t^2+2+|t| sqrt(t^2+4))/2
for tt in [0.3, 1.0, 2.7, -4.2]:
    f = lambda Y: -(1 + (Y + tt) ** 2) / (1 + Y ** 2)
    best = max(-f(Y) for Y in [k / 1000.0 for k in range(-20000, 20001)])
    say("WHR8.2 t=%.1f: grid sup %.9f ; Lambda_+(t) = %.9f" % (tt, best, (tt ** 2 + 2 + abs(tt) * (tt ** 2 + 4) ** 0.5) / 2))
