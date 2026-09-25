#!/usr/bin/env python3
# Written by the referee subagent of the sixth referee pass (claude-opus-5-5, Opus 5.5), 25 September 2026, for notes 19-20;
# copied into checks/ with these two header lines added. Output: referee_theorem_c_independent_checks_OUTPUT.txt
"""Referee's independent checks for notes 19-20 (not derived from the authors' scripts).

b(n) is built as the Dirichlet convolution sum_{d|n} mu(n/d)/d (coefficients of zeta(s+1)/zeta(s)),
not from the closed product formula; lambda(n) from Omega(n) computed by repeated division sieve.
"""
import math, time
import numpy as np
import mpmath as mp

N = 10_000_000
t0 = time.time()
# Moebius via linear sieve
mu = np.ones(N + 1, dtype=np.int8)
is_comp = np.zeros(N + 1, dtype=bool)
Omega = np.zeros(N + 1, dtype=np.int8)
primes = []
# simple Eratosthenes for primes
sieve = np.ones(N + 1, dtype=bool); sieve[:2] = False
for i in range(2, int(N ** 0.5) + 1):
    if sieve[i]:
        sieve[i * i::i] = False
primes = np.nonzero(sieve)[0]
mu[:] = 1
for p in primes:
    mu[p::p] *= -1
    pp = p * p
    if pp <= N:
        mu[pp::pp] = 0
    # Omega: add number of times p divides n
    q = p
    while q <= N:
        Omega[q::q] += 1
        q *= p
mu[0] = 0
lam = np.where(Omega % 2 == 0, 1, -1).astype(np.int8)
print("sieve done %.1fs" % (time.time() - t0))

# b = mu * (1/n) Dirichlet convolution: b(n) = sum_{d|n} (1/d) mu(n/d)
b = np.zeros(N + 1)
inv = 1.0 / np.arange(1, N + 1)
for d in range(1, N + 1):
    # add (1/d) * mu(m) to b(d*m) for m = 1..N//d
    M = N // d
    if M == 0:
        break
    b[d:d * M + 1:d] += inv[d - 1] * mu[1:M + 1]
print("convolution done %.1fs" % (time.time() - t0))
# spot check against closed form b(n) = n^{-1} prod_{p|n}(1-p)
def bclosed(n):
    r = 1.0; m = n; p = 2
    while p * p <= m:
        if m % p == 0:
            r *= (1 - p)
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        r *= (1 - m)
    return r / n
mx = max(abs(b[n] - bclosed(n)) for n in [1, 2, 3, 4, 6, 12, 30, 97, 360, 9973, 65536, 999999, 9699690])
print("max |b_conv - b_closed| on spot values = %.2e" % mx)

bl = b * lam
cs = np.cumsum(bl[1:])
for x in [10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7]:
    print("sum_{n<=%d} b(n)lambda(n)/x = %.6f" % (x, cs[x - 1] / x))

n = np.arange(2, N + 1, dtype=float); ln = np.log(n)
for D in [0.5, 0.35, 0.3]:
    w = n ** -0.5 * np.exp(-D * D * ln ** 2 / 2) / ln
    V6 = np.sum(bl[2:10 ** 6 + 1] * w[:10 ** 6 - 1])
    V7 = np.sum(bl[2:] * w)
    tau = math.pi * D * D
    Vt6 = np.sum(bl[2:10 ** 6 + 1] * w[:10 ** 6 - 1] * np.exp(-1j * tau * ln[:10 ** 6 - 1]))
    Vt7 = np.sum(bl[2:] * w * np.exp(-1j * tau * ln))
    # main term integral (2/5) int_{log2}^inf e^{u/2 - D^2 u^2/2} du/u
    main = mp.mpf(2) / 5 * mp.quad(lambda u: mp.e ** (u / 2 - D * D * u * u / 2) / u, [math.log(2), 1 / (2 * D * D), mp.inf])
    lb = 0.8 * D * math.exp(1 / (8 * D * D) - 0.5)
    print("D=%.2f: V(n<=1e6)=%.4f V(n<=1e7)=%.4f | ImV_tau(1e6)=%.4f ImV_tau(1e7)=%.4f | main term=%.4f claimed lower bound=%.4f | u0-1/D=%.3f vs log2=%.3f"
          % (D, V6, V7, Vt6.imag, Vt7.imag, float(main), lb, 1 / (2 * D * D) - 1 / D, math.log(2)))

b2 = b[2:] ** 2 / (n * ln ** 2)
S6 = np.sum(b2[:10 ** 6 - 1]); S7 = np.sum(b2)
mean6 = np.mean(b[1:10 ** 6 + 1] ** 2); mean7 = np.mean(b[1:] ** 2)
# exact mean value of b(n)^2: prod_p (1-1/p)(1 + (p-1)^2/(p^3-1))
Mexact = mp.mpf(1)
for p in primes[:200000]:
    p = mp.mpf(int(p))
    Mexact *= (1 - 1 / p) * (1 + (p - 1) ** 2 / (p ** 3 - 1))
print("sum_{2<=n<=1e6} b^2/(n log^2 n) = %.5f ; to 1e7 = %.5f" % (S6, S7))
print("mean b^2: to 1e6 = %.5f, to 1e7 = %.5f, Euler product (primes < %d) = %.5f" % (mean6, mean7, primes[199999], float(Mexact)))
for (S, NN) in [(S6, 1e6), (S7, 1e7)]:
    tot = S + float(Mexact) / math.log(NN)
    print("N=%.0e: total ~ %.5f ; 7/(12 pi^2) * total = %.5f" % (NN, tot, tot * 7 / (12 * math.pi ** 2)))
print("done %.1fs" % (time.time() - t0))
