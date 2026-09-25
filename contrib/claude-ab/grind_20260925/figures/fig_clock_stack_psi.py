#!/usr/bin/env python3
"""Checks and figure for note 15_ (the clock stack of PMS, 24-25 September 2026).

1. M6.2: log L_N - log L_{N-1} = Lambda(N), with L_N = lcm(1..N)  (exact integer check, N <= 20000).
2. M3.2: p has exact multiplicative order d modulo p^d - 1  (p <= 50, d <= 30).
3. M4.2: the joint state set of the clocks Z/1, ..., Z/N has exactly L_N elements (brute force, N <= 12).
4. Figure: psi(N) - N = log lcm(1..N) - N for N <= 10^6, with the RH band +-sqrt(N) log^2 N / (8 pi)
   (Schoenfeld's explicit form of von Koch's bound, valid under RH for N >= 73.2; drawn for orientation only).
claude-ab, model claude-opus-5-5 (Opus 5.5, maximum reasoning effort), 25 September 2026.
"""
import os, math
from math import gcd, log
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
out = []
def say(s):
    print(s); out.append(s)

def mangoldt(n):
    if n < 2:
        return 0.0
    for p in range(2, int(n ** 0.5) + 1):
        if n % p == 0:
            m = n
            while m % p == 0:
                m //= p
            return math.log(p) if m == 1 else 0.0
    return math.log(n)

# 1. exact: L_N / L_{N-1} = p if N = p^a else 1
L = 1
bad = 0
for N in range(2, 20001):
    Lnew = L * N // gcd(L, N)
    r = Lnew // L
    # r must be p (if N = p^a) or 1
    lam = mangoldt(N)
    ok = (r == 1 and lam == 0.0) or (r > 1 and abs(math.log(r) - lam) < 1e-12)
    bad += (not ok)
    L = Lnew
say("M6.2: L_N/L_{N-1} = e^{Lambda(N)} for 2 <= N <= 20000: failures = %d" % bad)

# 2. exact order of p modulo p^d - 1
bad = 0
for p in [q for q in range(2, 51) if all(q % r for r in range(2, int(q ** 0.5) + 1))]:
    for d in range(2, 31):
        m = p ** d - 1
        order = next(k for k in range(1, d + 1) if pow(p, k, m) == 1)
        bad += (order != d)
say("M3.2: ord of p mod p^d - 1 equals d (primes p <= 50, 2 <= d <= 30): failures = %d" % bad)

# 3. joint clock states
for N in range(1, 13):
    Ln = 1
    for d in range(1, N + 1):
        Ln = Ln * d // gcd(Ln, d)
    states = {tuple(n % d for d in range(1, N + 1)) for n in range(0, 2 * Ln + 5)}
    say("M4.2: N=%2d  distinct joint states of Z/1..Z/N = %6d   lcm(1..N) = %6d" % (N, len(states), Ln))

# 4. psi(N) - N via sieve of prime powers
NMAX = 1_000_000
lam = np.zeros(NMAX + 1)
sieve = np.ones(NMAX + 1, dtype=bool); sieve[:2] = False
for p in range(2, int(NMAX ** 0.5) + 1):
    if sieve[p]:
        sieve[p * p::p] = False
primes = np.nonzero(sieve)[0]
for p in primes:
    pk = p
    while pk <= NMAX:
        lam[pk] = math.log(p)
        pk *= p
psi = np.cumsum(lam)
n = np.arange(NMAX + 1)
dev = psi - n
xs = n[2:]
band = np.sqrt(xs) * np.log(xs) ** 2 / (8 * math.pi)
ratio = np.abs(dev[74:]) / (np.sqrt(n[74:]) * np.log(n[74:]) ** 2 / (8 * math.pi))
say("psi(10^6) = %.6f ; psi(10^6) - 10^6 = %.6f" % (psi[NMAX], dev[NMAX]))
say("max over 74 <= N <= 10^6 of |psi(N) - N| / (sqrt(N) log^2 N / (8 pi)) = %.4f" % ratio.max())
say("max over N <= 10^6 of |psi(N) - N| / sqrt(N) = %.4f" % (np.abs(dev[2:]) / np.sqrt(xs)).max())

plt.rcParams.update({"font.size": 10, "font.family": "DejaVu Sans"})
fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 4.8), gridspec_kw={"width_ratios": [1, 1.4], "wspace": 0.22})
# left: the clock stack, first steps
Ls, Ns = [], list(range(1, 31))
Lc = 1
for N in Ns:
    Lc = Lc * N // gcd(Lc, N); Ls.append(Lc)
a1.step(Ns, np.log(Ls), where="post", color="#2b6cb0", lw=2, label="log lcm(1..N) = ψ(N)")
a1.plot(Ns, Ns, color="0.5", lw=1, ls="--", label="N")
for N in Ns[1:]:
    if mangoldt(N) > 0:
        a1.annotate(str(N), (N, math.log(Ls[N - 1])), xytext=(0, 6), textcoords="offset points",
                    fontsize=7, ha="center", color="#c53030")
a1.set_xlabel("N (clocks of periods 1, …, N)"); a1.set_ylabel("log (number of joint clock states)")
a1.set_title("The clock stack grows by Λ(N) at each prime power N (red)", fontsize=10)
a1.legend(fontsize=8.5, loc="upper left")
# right: normalized deviation
step = 20
a2.plot(n[2::step], dev[2::step] / np.sqrt(n[2::step]), color="#2b6cb0", lw=0.5, label="(ψ(N) − N)/√N", rasterized=True)
a2.fill_between(xs[::step], -band[::step] / np.sqrt(xs[::step]), band[::step] / np.sqrt(xs[::step]),
                color="#fed7d7", alpha=0.7, label="±log²N / (8π)  (Schoenfeld's bound under RH, N ≥ 73.2)", rasterized=True)
a2.axhline(1, color="0.4", lw=0.8, ls=":"); a2.axhline(-1, color="0.4", lw=0.8, ls=":", label="±1")
a2.set_xscale("log"); a2.set_xlim(10, NMAX); a2.set_ylim(-3, 3)
a2.set_xlabel("N"); a2.set_ylabel("(ψ(N) − N) / √N")
a2.set_title("log lcm(1..N) − N, divided by √N, up to 10⁶:\nthe zeros' oscillation around the pole's average N", fontsize=10)
a2.legend(fontsize=8.5, loc="lower left")
fig.text(0.01, -0.02, "claude-ab (Opus 5.5, max effort) · exact prime-power sieve · figures/fig_clock_stack_psi.py",
         fontsize=7, color="0.4")
for ext in ("png", "svg"):
    fig.savefig(os.path.join(HERE, "fig_clock_stack_psi." + ext), dpi=160, bbox_inches="tight")
say("saved")
