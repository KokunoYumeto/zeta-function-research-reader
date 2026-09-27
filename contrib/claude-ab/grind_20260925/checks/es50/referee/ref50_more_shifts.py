#!/usr/bin/env python3
"""ref50_more_shifts.py -- referee search for further quadratic-residue conditions of the kind of Theorem 50.4.

Three certificate types whose shell R is a multiple of a prime q dividing a shifted value S(p):
  M_s : u = s,     S = p + 4s,  needs s | a^2          (R | u + a  <=>  R | p + 4s)
  E_t : u = a/t,   S = p + t,   needs t | a            (R | 4u + 1 <=>  R | p + t)
  F_t : u = t a,   S = t p + 1, needs t | a            (R | 4u + 1 <=>  R | t p + 1)
For a prime q | S with (p/q) = -1 one takes R = q r, where r is a product of the small primes 3, 9, 5, 7 whose
divisibility of S the class of p modulo 10080 forces, chosen so that R = 3 (mod 4) and the divisibility
condition on a = (p+R)/4 holds.  (p/q) = (-s/q), (-t/q), (-t/q) respectively.  A (type, parameter, class) is
QR-GOOD when every class of q modulo 10080 with (p/q) = -1 admits such an r: then a counterexample in that class
is a quadratic residue modulo every prime factor of S (other than 2 and the forced small primes).

Theorem 50.4 contains E_1 (p+1), M_1 (p+4), E_2 (p+2), M_2 (p+8), F_2 (2p+1), which are QR-good on all 72
hard classes modulo 10080.  This script lists every further QR-good (type, parameter) on hard classes, for
{2,3,5,7}-smooth parameters, verifies all certificates exactly for all primes p = 1 (mod 24) below X, and counts
how many of the survivors of Table 'survivors' (31 below 10^7) the new conditions remove.
"""
import sys, time
from math import gcd, isqrt, prod
from itertools import product
import numpy as np

X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**7
T0 = time.time()
L = 10080
S840 = {1, 121, 169, 289, 361, 529}
HC = [c for c in range(1, L, 24) if c % 840 in S840]
assert len(HC) == 72

# primes up to 3X via smallest-prime-factor sieve
LIM = 3 * X + 100
spf = np.zeros(LIM + 1, dtype=np.int32)
for i in range(2, isqrt(LIM) + 1):
    if spf[i] == 0:
        blk = spf[i*i::i]; blk[blk == 0] = i; spf[i*i::i] = blk
z = np.nonzero(spf == 0)[0]; spf[z] = z; spf[0] = 0; spf[1] = 1
spf = spf.tolist()
from sympy import factorint as _factorint
def fac(n):
    if n > LIM: return dict(_factorint(n))
    f = {}
    while n > 1:
        q = spf[n]; f[q] = f.get(q, 0) + 1; n //= q
    return f
def isprime(n): return n >= 2 and spf[n] == n
def leg(a, q):
    a %= q
    return 0 if a == 0 else (1 if pow(a, (q - 1) // 2, q) == 1 else -1)
def divisors_f(f):
    ds = [1]
    for q, e in f.items(): ds = [d * q**k for d in ds for k in range(e + 1)]
    return ds

# a representative prime for every unit class modulo L (used to evaluate the characters (-s/q))
rep = {}
for n in range(11, LIM):
    if isprime(n) and n % L not in rep and gcd(n, L) == 1:
        rep[n % L] = n
    if len(rep) == 2304: break
assert len(rep) == 2304          # phi(10080) = 2304

def v(n, l):
    k = 0
    while n % l == 0: n //= l; k += 1
    return k

def shift(typ, par, p): return p + 4 * par if typ == 'M' else (p + par if typ == 'E' else par * p + 1)
def need_ok(typ, par, a_mod):
    """a_mod: dict of (a mod 2^k etc.) given as the integer (p+R)/4 reduced mod L/4?  We pass valuations."""
    raise NotImplementedError

def cond_ok(typ, par, c, R):
    """divisibility condition on a = (p+R)/4 for p = c (mod L), R given mod L (as residue); uses only the
    valuations of p+R at 2 (up to 5), 3 (up to 2), 5, 7 (up to 1), which the classes mod L fix."""
    w = (c + R) % L
    e2 = min(v(w, 2), 5) - 2 if w else 3
    if w % 32 == 0: e2 = None                     # v2(p+R) >= 5 : a has v2 >= 3 but exact value unknown
    va = {2: (3 if e2 is None else e2), 3: min(v(w, 3), 2) if w % 9 else 2, 5: 1 if w % 5 == 0 else 0, 7: 1 if w % 7 == 0 else 0}
    if (c + R) % 4: return False
    if typ == 'M':      # s | a^2
        for l, e in ((2, v(par, 2)), (3, v(par, 3)), (5, v(par, 5)), (7, v(par, 7))):
            if e and 2 * va[l] < e: return False
        return True
    else:               # t | a
        for l, e in ((2, v(par, 2)), (3, v(par, 3)), (5, v(par, 5)), (7, v(par, 7))):
            if e and va[l] < e: return False
        return True

def forced_mults(typ, par, c):
    Sm = shift(typ, par, c) % L
    fs = []
    if Sm % 3 == 0: fs.append([1, 3, 9] if Sm % 9 == 0 else [1, 3])
    if Sm % 5 == 0: fs.append([1, 5])
    if Sm % 7 == 0: fs.append([1, 7])
    return sorted({prod(t) for t in product(*fs)}) if fs else [1]

def chi(typ, par, qrep):
    t = -4 * par if typ == 'M' else -par
    return leg(t, qrep)

def qr_good(typ, par, c):
    mults = forced_mults(typ, par, c)
    for qc, qrep in rep.items():
        if qrep in (3, 5, 7) or par % qrep == 0: continue
        if chi(typ, par, qrep) != -1: continue
        if not any(((qc * r) % 4 == 3) and cond_ok(typ, par, c, (qc * r) % L) for r in mults):
            return False
    return True

# complete finite parameter sets for this mechanism: the class mod 10080 fixes v2(a) only up to 3, v3(a) up to 2,
# v5(a), v7(a) up to 1; so s | a^2 needs s | 2^6 3^4 5^2 7^2 and t | a needs t | 2^3 3^2 5 7
paramsM = sorted({2**a * 3**b * 5**cc * 7**d for a in range(7) for b in range(5) for cc in range(3) for d in range(3)})
paramsE = sorted({2**a * 3**b * 5**cc * 7**d for a in range(4) for b in range(3) for cc in range(2) for d in range(2)})
good = {}
for typ in ('M', 'E', 'F'):
    for par in (paramsM if typ == 'M' else paramsE):
        if typ == 'F' and par == 1: continue
        gl = [c for c in HC if qr_good(typ, par, c)]
        if gl: good[(typ, par)] = gl
name = lambda typ, par: (f"p+{4*par}" if typ == 'M' else (f"p+{par}" if typ == 'E' else f"{par}p+1"))
print(f"# QR-good (type, parameter): number of good hard classes mod {L} (of 72); complete over {len(paramsM)} M-parameters and {len(paramsE)} E/F-parameters")
for (typ, par), gl in sorted(good.items(), key=lambda t: (-len(t[1]), t[0])):
    cls840 = sorted({c % 840 for c in gl})
    print(f"  {typ}_{par:<3d} shift {name(typ, par):7s}: {len(gl):2d} classes; classes mod 840 met: {cls840}")

# ------------------------------------------------------------------ exact verification on primes
def cert(typ, par, p, q, mults):
    """build the certificate for prime q | S with (p/q) = -1; return (R, u, channel) or None"""
    for r in mults:
        R = q * r
        if R % 4 != 3 or (p + R) % 4: continue
        a = (p + R) // 4
        if gcd(R, p * a) != 1: continue
        if typ == 'M':
            if (a * a) % par: continue
            u, ch = par, 'M'
        elif typ == 'E':
            if a % par: continue
            u, ch = a // par, 'E'
        else:
            if a % par: continue
            u, ch = par * a, 'E'
        if ch == 'M' and (u + a) % R: continue
        if ch == 'E' and (4 * u + 1) % R: continue
        return R, u, ch
    return None
def solution(p, R, u, ch):
    a = (p + R) // 4; N = p * a; d = p * p * u if ch == 'E' else p * u
    y = (N + d) // R; z = (N + N * N // d) // R
    assert (N + d) % R == 0 and (N + N * N // d) % R == 0
    assert 4 * a * y * z == p * (a * y + y * z + z * a)
    return a, y, z

P24 = [p for p in range(25, X, 24) if isprime(p)]
HARD = [p for p in P24 if p % 840 in S840]
new_keys = [k for k in good if k not in {('E', 1), ('M', 1), ('E', 2), ('M', 2), ('F', 2)}]
nver = 0; nfail = 0
certified_by = {}
for p in HARD:
    c = p % L
    for key in new_keys:
        if c not in good[key]: continue
        typ, par = key
        S = shift(typ, par, p)
        mults = [m for m in forced_mults(typ, par, c)]
        for q in fac(S):
            if q in (2, 3, 5, 7) or par % q == 0: continue
            if leg(p, q) != -1: continue
            cr = cert(typ, par, p, q, mults)
            if cr is None:
                nfail += 1
                if nfail < 5: print("  FAIL", key, p, q)
                continue
            solution(p, *cr); nver += 1
            certified_by.setdefault(p, set()).add(key)
print(f"# exact verification, hard primes below {X}: {nver} certificates from the new conditions, {nfail} failures")

# ------------------------------------------------------------------ effect on the survivors (restricted version)
def eight(p):
    for S in (p + 1, p + 2, p + 3, p + 4, p + 7, p + 8, 2 * p + 1, 3 * p + 1):
        for q in fac(S):
            if q != 2 and leg(p, q) == -1: return True
    return False
def good5(p):
    s = p % 840
    return p % 40 == 9 or s == 121 or (s in (1, 361) and p % 9 == 4)
def good17(p): return p % 840 in (361, 529) and p % 9 == 1 and p % 17 in (8, 15, 16)
def nr_factor(p, S, skip=(2,)):
    return any(q not in skip and leg(p, q) == -1 for q in fac(S))
# visible-box good classes (recomputed as in Theorem 50.6)
def forced_box(c, R):
    lo = {}
    w = (c + R) % L
    t2 = min(v(w, 2), 5) - 2 if w % 32 else 3
    if t2 > 0: lo[2] = min(t2, 3)
    if R != 3 and w % 3 == 0: lo[3] = 2 if w % 9 == 0 else 1
    for f in (5, 7):
        if R != f and w % f == 0: lo[f] = 1
    box = {1}
    for f, e in lo.items(): box = {(b * pow(f, k, R)) % R for b in box for k in range(2 * e + 1)}
    return box
goodR = {}
for R in [q for q in range(3, 700) if isprime(q) and q % 4 == 3]:
    Q = {(i * i) % R for i in range(1, R)}
    g = {c for c in HC if Q <= forced_box(c, R)}
    if g: goodR[R] = g
surv = []
for p in HARD:
    if eight(p): continue
    if good5(p) and nr_factor(p, p + 5, (2, 5)): continue
    if good17(p) and nr_factor(p, p + 17, (2, 17)): continue
    if any((p % L) in g and p != R and nr_factor(p, p + R, (2, R)) for R, g in goodR.items()): continue
    surv.append(p)
print(f"# survivors of all conditions of §3 (restricted), p < {X}: {len(surv)} (claim 31 for 10^7)")
newsurv = [p for p in surv if p not in certified_by]
print(f"# of these, removed by the new conditions: {len(surv) - len(newsurv)}; remaining: {len(newsurv)}")
print("  removed:", [(p, sorted(name(*k) for k in certified_by[p])) for p in surv if p in certified_by][:40])
print("  remaining:", newsurv[:40])
print(f"time {time.time() - T0:.1f}s")
