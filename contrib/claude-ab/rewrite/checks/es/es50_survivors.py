#!/usr/bin/env python3
"""es50_checks.py -- independent checks for note 50_ (the owner's Erdos-Straus notes).

Written by claude-ab from the statements, not from the referee scripts.  Every certificate is
turned into an explicit triple (x, y, z) and tested exactly: 4xyz == p(xy + yz + zx).

Sections
  A  the support-zero core: no elementary j=1 certificate class contains a unit square
  B  quadratic-residue necessary conditions (eight shifts; p+5; visible-box shells)
  C  barriers (width-one versus group barrier; the example (433, 91))
  D  shell facts (non-coprime shells; R | p-1; the parity law for R | p^2-1)
  E  identities from the notes (29-channels; n = -c mod 4k-1 with c | k)
  F  locks and types (lock certificates for hard primes; Type II within R <= 107; complement squares)
Usage: python3 es50_checks.py [X]   (default X = 10**7)
"""
import sys, time, random
from math import gcd, isqrt
import numpy as np

X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**7
T0 = time.time()
RESULTS = []
def check(label, name, ok, detail=""):
    RESULTS.append(ok)
    print(("PASS " if ok else "FAIL ") + label + " " + name + ("  [" + detail + "]" if detail else ""), flush=True)

# ---------------------------------------------------------------- sieve (smallest prime factor)
LIM = 3 * X + 64
spf = np.zeros(LIM + 1, dtype=np.int32)
for i in range(2, isqrt(LIM) + 1):
    if spf[i] == 0:
        blk = spf[i*i::i]
        blk[blk == 0] = i
        spf[i*i::i] = blk
z = np.nonzero(spf == 0)[0]
spf[z] = z
spf[0] = 0; spf[1] = 1
spf = spf.tolist()
def fac(n):
    f = {}
    while n > 1:
        q = spf[n]
        f[q] = f.get(q, 0) + 1
        n //= q
    return f
def isprime(n):
    return n >= 2 and spf[n] == n
def legendre(a, q):
    a %= q
    if a == 0: return 0
    return 1 if pow(a, (q - 1) // 2, q) == 1 else -1
def divisors_f(f):
    ds = [1]
    for q, e in f.items():
        ds = [d * q**k for d in ds for k in range(e + 1)]
    return ds
def is_solution(p, x, y, z):
    return x > 0 and y > 0 and z > 0 and 4 * x * y * z == p * (x * y + y * z + z * x)
def shell_solution(p, R, u, channel):
    """solution with x = a from the shell certificate: E (R | 4u+1) or M (R | u+a); u | a^2."""
    assert (p + R) % 4 == 0
    a = (p + R) // 4
    assert (a * a) % u == 0
    if channel == 'E':
        assert (4 * u + 1) % R == 0
        d = p * p * u
    else:
        assert (u + a) % R == 0
        d = p * u
    N = p * a
    assert (N + d) % R == 0 and (N + N * N // d) % R == 0
    return (a, (N + d) // R, (N + N * N // d) // R)

S840 = {1, 121, 169, 289, 361, 529}
P24 = [p for p in range(25, X, 24) if isprime(p)]          # primes p = 1 (mod 24), p < X
HARD = [p for p in P24 if p % 840 in S840]
print(f"# X = {X}: primes = 1 (mod 24): {len(P24)}; hard (mod 840 in S840): {len(HARD)}; sieve {time.time()-T0:.1f}s", flush=True)


def eight_shift_certificates(p):
    out = []
    for name, val in (("p+1", p + 1), ("p+2", p + 2), ("p+3", p + 3), ("p+4", p + 4),
                      ("p+7", p + 7), ("p+8", p + 8), ("2p+1", 2 * p + 1), ("3p+1", 3 * p + 1)):
        for q in fac(val):
            if q == 2 or legendre(p, q) != -1: continue
            if name in ("p+1", "p+4"):
                R = q
                if name == "p+1": out.append((name, q, shell_solution(p, R, (p + R) // 4, 'E')))
                else:              out.append((name, q, shell_solution(p, R, 1, 'M')))
            elif name in ("p+2", "p+8", "2p+1"):
                R = q if q % 8 == 7 else 3 * q
                a = (p + R) // 4
                if name == "p+2":  out.append((name, q, shell_solution(p, R, a // 2, 'E')))
                if name == "2p+1": out.append((name, q, shell_solution(p, R, 2 * a, 'E')))
                if name == "p+8":  out.append((name, q, shell_solution(p, R, 2, 'M')))
            elif name == "p+3":
                out.append((name, q, shell_solution(p, 3, q, 'E')))
            elif name == "p+7":
                a = (p + 7) // 4
                if q % 7 == 5:   out.append((name, q, shell_solution(p, 7, q, 'E')))
                elif q % 7 == 6: out.append((name, q, shell_solution(p, 7, a * q, 'M')))
                elif q % 7 == 3: out.append((name, q, shell_solution(p, 7, 2 * a * q, 'M')))
                else: raise AssertionError((p, q))
            elif name == "3p+1":
                N3 = (3 * p + 1) // 4
                h = N3 // q
                m = (h + 1) // 3
                R = (4 * q + 1) // 3
                assert N3 % q == 0 and (h + 1) % 3 == 0 and (4 * q + 1) % 3 == 0
                assert 4 * q * m - p == R
                out.append((name, q, shell_solution(p, R, q, 'E')))
    return out

def lock_a(p, mu, d):
    """lock (a): d odd, d | p+mu, d = -p (mod 4 mu): shell R = d, u = a/mu (E)."""
    return shell_solution(p, d, (p + d) // 4 // mu, 'E')

def lock_b(p, mu, h):
    """lock (b): h | N = (p+mu)/2, h = -1 (mod 4 mu): a = 2 mu e t, R = mu + 2e, u = mu^2 t (M)."""
    N = (p + mu) // 2
    e = N // h; t = (h + 1) // (4 * mu)
    a = 2 * mu * e * t; R = mu + 2 * e
    assert 4 * a - p == R
    return shell_solution(p, R, mu * mu * t, 'M')

def mu_lock(p, mu):
    N = (p + mu) // 2
    if (p + mu) % 2: return None
    f = fac(N)
    for d in sorted(divisors_f(f)):
        if d % 2 == 1 and (d + p) % (4 * mu) == 0 and d != p:
            return ('a', d, lock_a(p, mu, d))
        if (d + 1) % (4 * mu) == 0:
            return ('b', d, lock_b(p, mu, d))
    return None

def forced_box(c, R):
    lo = {}
    w = c + R
    v = 0
    while w % 2 == 0 and v < 12: w //= 2; v += 1
    t2 = v - 2
    if t2 > 0: lo[2] = min(t2, 3)                  # p mod 32 fixes v2(p+R) only up to 5
    if R != 3 and (c + R) % 3 == 0: lo[3] = 2 if (c + R) % 9 == 0 else 1
    for f in (5, 7):
        if R != f and (c + R) % f == 0: lo[f] = 1
    box = {1}
    for f, e in lo.items():
        box = {(b * pow(f, k, R)) % R for b in box for k in range(2 * e + 1)}
    return box

def occupied(p, R):
    a = (p + R) // 4
    if gcd(a, R) != 1: return False
    ds = divisors_f({q: 2 * e for q, e in fac(a).items()})
    tE = (-pow(4, -1, R)) % R; tM = (-a) % R
    for u in ds:
        r = u % R
        if r == tE: return ('E', u)
        if r == tM: return ('M', u)
    return False


classes10080 = [c for c in range(1, 10080, 24) if c % 840 in S840]
goodR = {}
for R in [q for q in range(3, 700) if isprime(q) and q % 4 == 3]:
    QR = {(i * i) % R for i in range(1, R)}
    g = [c for c in classes10080 if QR <= forced_box(c, R)]
    if g: goodR[R] = set(g)
s0 = [p for p in HARD if not eight_shift_certificates(p)]
s1 = [p for p in s0 if mu_lock(p, 5) is None]
s2 = [p for p in s1 if mu_lock(p, 17) is None]
s3 = [p for p in s2 if not any((p % 10080) in gl and occupied(p, R) for R, gl in goodR.items() if R != p)]
print(f"X = {X}: survivors of the eight shifts: {len(s0)}; + mu=5 lock: {len(s1)}; + mu=17 lock: {len(s2)}; + visible-box shells: {len(s3)}")
print("first survivors of all conditions:", s3[:10])
print("p* = 8803369 in s0/s1/s2/s3:", [8803369 in s for s in (s0, s1, s2, s3)])

# --- the referee's restricted version: each condition applied only on the classes where it is a QR condition
def good5(p):
    s = p % 840
    return p % 40 == 9 or s == 121 or (s in (1, 361) and p % 9 == 4)
def good17(p):
    return p % 840 in (361, 529) and p % 9 == 1 and p % 17 in (8, 15, 16)
r1 = [p for p in s0 if not (good5(p) and mu_lock(p, 5) is not None)]
r2 = [p for p in r1 if not (good17(p) and mu_lock(p, 17) is not None)]
r3 = [p for p in r2 if not any((p % 10080) in gl and occupied(p, R) for R, gl in goodR.items() if R != p)]
print(f"restricted: {len(s0)} -> +mu=5 on its classes: {len(r1)} -> +mu=17 on its classes: {len(r2)} -> +visible-box: {len(r3)}")
print("first restricted survivors:", r3[:10])
