#!/usr/bin/env python3
"""Checks for note 20_ (independent re-proof of Theorem C, parts 1-2, of copy-newresults).

 (1) Euler factor of b(n) lambda(n): (1 + p^{-s})/(1 + p^{-1-s}); B(s) = zeta(2s+2)/(zeta(2s) zeta(s+1)); B(1) = 2/5.
 (2) sum_{n<=x} b(n) lambda(n) / x for x up to 10^6.
 (3) V(Delta) = sum b(n) lambda(n) n^{-1/2} e^{-Delta^2 log^2 n / 2}/log n against the lower bound (4/5) Delta e^{1/(8 Delta^2) - 1/2}.
 (4) the T-linear part of the Gaussian-window transform: h1hat(xi) contains -(T/2pi) ghat(xi) e^{-i T xi}/xi (sympy).
 (5) sum_{n>=2} b(n)^2/(n log^2 n) and the constant 7/(12 pi^2) times it.
 (6) Kronecker illustration: max over sampled T of Re D_Delta(T) against V(Delta), Delta = 0.5.
claude-ab, model claude-opus-5-5 (Opus 5.5, maximum reasoning effort), 25 September 2026.
"""
import os, math
import numpy as np
import sympy as sp
out = []
def say(s=""):
    print(s); out.append(s)

# (1) Euler factors, symbolic in X = p^{-s}, P = p
X, P = sp.symbols('X P', positive=True)
k = sp.symbols('k', integer=True, nonnegative=True)
# b(p^k) lambda(p^k) p^{-ks} = (1 - P) (-1)^k (X/P)^k for k >= 1, and 1 for k = 0
geo = (-X / P) / (1 + X / P)          # sum_{k>=1} (-X/P)^k, |X/P| < 1
series = 1 + (1 - P) * geo
target = (1 + X) / (1 + X / P)
say("(1) Euler factor: simplify(series - (1+p^-s)/(1+p^{-1-s})) = %s" % sp.simplify(series - target))
# zeta(s) B(s) Euler factor: (1-X)^{-1} (1-X^2)(1-X/P)/(1-X^2/P^2)
zb = (1 - X ** 2) * (1 - X / P) / ((1 - X ** 2 / P ** 2) * (1 - X))
say("(1) zeta(s) B(s) Euler factor minus target: %s ; B(1) = zeta(4)/zeta(2)^2 = %s" % (sp.simplify(zb - target), sp.nsimplify(sp.zeta(4) / sp.zeta(2) ** 2)))

# (2)-(3), (5)-(6): arithmetic functions by sieve
N = 1_000_000
spf = np.zeros(N + 1, dtype=np.int64)
for i in range(2, N + 1):
    if spf[i] == 0:
        spf[i::i][spf[i::i] == 0] = i
b = np.zeros(N + 1); lam = np.zeros(N + 1, dtype=np.int64)
b[1] = 1.0; lam[1] = 1
for n in range(2, N + 1):
    p = spf[n]; m = n // p
    lam[n] = -lam[m]
    # b(n) = n^{-1} prod_{p|n} (1-p): multiplicative in the radical
    if m % p == 0:
        b[n] = b[m] / p
    else:
        b[n] = b[m] * (1 - p) / p
cs = np.cumsum(b[1:] * lam[1:])
for x in [10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6]:
    say("(2) sum_{n<=%d} b(n) lambda(n) / x = %.6f" % (x, cs[x - 1] / x))
n = np.arange(2, N + 1, dtype=float)
ln = np.log(n)
for D in [0.5, 0.35, 0.3]:
    V = np.sum(b[2:] * lam[2:] * n ** -0.5 * np.exp(-D ** 2 * ln ** 2 / 2) / ln)
    tail = np.exp(-D ** 2 * math.log(N) ** 2 / 2) * N ** 0.5      # size of the omitted tail terms (crude)
    say("(3) Delta = %.2f: V(Delta) = %.4f (n <= 10^6; tail factor %.1e) ; lower bound (4/5) Delta e^{1/(8 Delta^2) - 1/2} = %.4f"
        % (D, V, tail, 0.8 * D * math.exp(1 / (8 * D * D) - 0.5)))
for D in [0.5, 0.35, 0.3]:
    tau = math.pi * D * D
    Vt = np.sum(b[2:] * lam[2:] * n ** (-0.5) * np.exp(-1j * tau * ln) * np.exp(-D ** 2 * ln ** 2 / 2) / ln)
    main = 0.4 * (-1j) * 2 * math.sqrt(2 * math.pi) * D * math.exp(1 / (8 * D * D))
    say("(3') Delta = %.2f, tau = pi Delta^2: V_tau(Delta) = %s ; leading term (2/5)(-i) 2 sqrt(2 pi) Delta e^{1/(8 Delta^2)} = %s"
        % (D, np.round(Vt, 4), np.round(main, 4)))
S2 = np.sum(b[2:] ** 2 / (n * ln ** 2))
say("(5) sum_{2<=n<=10^6} b(n)^2/(n log^2 n) = %.4f ; times 7/(12 pi^2) = %.5f" % (S2, S2 * 7 / (12 * math.pi ** 2)))
# (4) T-linear part of hat h_1 for h = 1_[T1,T] * g_Delta: only the e^{-iT xi} part of hat h depends on T
xi, T, Dl = sp.symbols('xi T Delta', real=True)
ghat = sp.exp(-Dl ** 2 * xi ** 2 / 2)
hT = -ghat * sp.exp(-sp.I * T * xi) / (sp.I * xi)
h1T = (sp.Rational(1, 2) * hT - sp.diff(hT, xi)) / (2 * sp.pi)
coef = sp.simplify(sp.diff(sp.expand(h1T * sp.exp(sp.I * T * xi)), T))
say("(4) coefficient of T in the T-part of h1hat, times e^{iT xi}: %s ; minus (-ghat/(2 pi xi)) = %s"
    % (coef, sp.simplify(coef + ghat / (2 * sp.pi * xi))))
mean_b2 = float(np.mean(b[1:] ** 2))
say("(5) mean of b(n)^2 over n <= 10^6 = %.4f ; tail estimate sum_{n>10^6} ~ mean/log(10^6) = %.4f ; total ~ %.4f ; constant ~ %.5f"
    % (mean_b2, mean_b2 / math.log(N), S2 + mean_b2 / math.log(N), (S2 + mean_b2 / math.log(N)) * 7 / (12 * math.pi ** 2)))
# (6) Kronecker illustration
D = 0.5
nn = np.arange(2, 20001, dtype=float); lnn = np.log(nn)
cn = b[2:20001] * nn ** -0.5 * np.exp(-D ** 2 * lnn ** 2 / 2) / lnn
V = np.sum(cn[:400] * lam[2:402])
Ts = np.linspace(0, 2.0e5, 400001)
best = -1e9; arg = None
for chunk in np.array_split(Ts, 200):
    vals = (np.exp(-1j * np.outer(chunk, lnn[:400])) @ cn[:400]).real + 0.0
    j = np.argmax(vals)
    if vals[j] > best:
        best = vals[j]; arg = chunk[j]
say("(6) Delta = 0.5, first 400 terms: V = %.4f ; max of Re D_Delta(T) over T in [0, 2e5], step 0.5: %.4f at T = %.1f ; sup_T Re D_Delta >= V(Delta) by Kronecker"
    % (V, best, arg))
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "theorem_c_reproof_checks_OUTPUT.txt"), "w") as fh:
    fh.write("\n".join(out) + "\n")
