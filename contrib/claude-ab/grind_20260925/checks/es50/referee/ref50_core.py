#!/usr/bin/env python3
"""ref50_core.py -- referee check of Theorem 50.1(a) / reader Theorem termcore(a) and Lemma j1square.

Independent of es50_support_core.py and of the author's scripts:
  * the 32 visible shells and the 4951 survivors are recomputed by brute force over explicit certificates
    (R, m, u) with m | 2*3*5*7*11*19*23, u | m^2, class conditions checked directly on the integer n = CRT class;
  * the 'only if' direction is checked CONSTRUCTIVELY: for every base class that is not a square mod 11, 19, 23
    we exhibit an explicit P-smooth R = 3^a 5^b 7^c 11^d 19^e 23^f (exponents <= 3), an explicit certificate
    (R, m, u), an explicit lift n0 modulo lcm(M, R) in the class that satisfies n0 = -R (mod 4m) and n0 = -4u (mod R),
    and (for a sample) an actual PRIME in that lift whose solution 4/p = 1/x+1/y+1/z is verified exactly;
  * the 'if' direction (Lemma j1square) is checked on all certificates used, by computing the Jacobi symbol formula;
  * the semigroup sizes 45,139 and 22,074 of the source note are recomputed by a different method
    (products 3^a..23^f taken modulo M, exponents up to the multiplicative orders).
"""
import time, random
from math import gcd, prod
from itertools import product
from sympy import isprime, jacobi_symbol, factorint

T0 = time.time()
M = 840 * 11 * 19 * 23
S840 = [1, 121, 169, 289, 361, 529]
BASEP = [2, 3, 5, 7, 11, 19, 23]
P = [3, 5, 7, 11, 19, 23]

def crt(pairs):
    x, m = 0, 1
    for r, q in pairs:
        g = gcd(m, q)
        assert (r - x) % g == 0
        l = m // g * q
        t = ((r - x) // g * pow(m // g, -1, q // g)) % (q // g)
        x = (x + m * t) % l; m = l
    return x, m

classes = [crt([(s, 840), (x, 11), (y, 19), (z, 23)])[0]
           for s in S840 for x in range(1, 11) for y in range(1, 19) for z in range(1, 23)]
assert len(classes) == 23760 and len(set(classes)) == 23760
def issq(c, q): return pow(c % q, (q - 1) // 2, q) == 1
square = {c for c in classes if issq(c, 11) and issq(c, 19) and issq(c, 23)}
print(f"base classes {len(classes)}, square classes {len(square)} (= 6*5*9*11 = {6*5*9*11})")

def available(R, n):
    """primes l of BASEP not dividing R with n = -R (mod 4l) (mod 8 for l = 2); n is the class mod M."""
    out = []
    for l in BASEP:
        if R % l == 0: continue
        mod = 8 if l == 2 else 4 * l
        if (n + R) % mod == 0: out.append(l)
    return out

def certs(R, n):
    """all (m, u) with m = product of available primes (squarefree), u | m^2, and the residue -4u mod g,
    g = gcd(M, R).  Returns dict residue(mod g) -> (m, u)."""
    A = available(R, n)
    g = gcd(M, R)
    out = {}
    for exps in product((0, 1, 2), repeat=len(A)):
        u = prod(l**e for l, e in zip(A, exps))
        m = prod(l for l, e in zip(A, exps) if e > 0)
        r = (-4 * u) % g
        if r not in out: out[r] = (m, u)
    return out

# (1) visible shells: R | M, R = 3 mod 4 (odd divisors of M)
odd_divs = sorted(prod(q for q, b in zip(P, bits) if b) for bits in product((0, 1), repeat=6))
visible = [R for R in odd_divs if R % 4 == 3]
alive = set(classes)
for R in visible:
    kill = set()
    for n in alive:
        c = certs(R, n)
        if n % R in c:          # R | M, so the class determines n mod R: a covering statement
            kill.add(n)
    alive -= kill
print(f"(1) visible shells {len(visible)}; survivors {len(alive)} (claim 4951); square core inside survivors: {square <= alive}")

# (2) constructive 'only if': explicit P-smooth shells with exponents <= 3
shells = sorted(R for R in (prod(q**e for q, e in zip(P, ex)) for ex in product(range(4), repeat=6)) if R % 4 == 3)
print(f"    P-smooth shells R = 3 mod 4 with exponents <= 3: {len(shells)}")
witness = {}
todo = [n for n in classes if n not in square]
random.seed(1)
for R in shells:
    if not todo: break
    g = gcd(M, R)
    rest = []
    for n in todo:
        c = certs(R, n)
        if n % g in c:
            witness[n] = (R, c[n % g])
        else:
            rest.append(n)
    todo = rest
print(f"    non-square classes {len([n for n in classes if n not in square])}; without an explicit witness at exponents <= 3: {len(todo)}")
# second round for the remainder: exponents up to 11 (every P-smooth residue state modulo M is reached with
# exponents below the multiplicative orders, which divide 1980; 12 per prime suffices in practice)
if todo:
    shells2 = sorted(R for R in (prod(q**e for q, e in zip(P, ex)) for ex in product(range(12), repeat=6)) if R % 4 == 3)
    for R in shells2:
        if not todo: break
        g = gcd(M, R)
        rest = []
        for n in todo:
            c = certs(R, n)
            if n % g in c:
                witness[n] = (R, c[n % g])
            else:
                rest.append(n)
        todo = rest
    print(f"    second round (exponents <= 11, {len(shells2)} shells): without an explicit witness: {len(todo)}")
if todo:
    # third round: BFS over residue states modulo M, remembering an exponent vector for each state
    from collections import deque
    state_exp = {1: (0,) * 6}
    dq = deque([1])
    while dq:
        r = dq.popleft()
        for i, q in enumerate(P):
            s = (r * q) % M
            if s not in state_exp:
                e = list(state_exp[r]); e[i] += 1
                state_exp[s] = tuple(e); dq.append(s)
    print(f"    third round: {len(state_exp)} residue states modulo M (BFS)")
    for rho, ex in sorted(state_exp.items(), key=lambda t: sum(t[1])):
        if rho % 4 != 3 or not todo: continue
        R = prod(q**e for q, e in zip(P, ex))
        g = gcd(M, R)
        rest = []
        for n in todo:
            c = certs(R, n)
            if n % g in c:
                witness[n] = (R, c[n % g])
                print(f"      class {n}: witness R = {'*'.join(f'{q}^{e}' for q, e in zip(P, ex) if e)} with (m, u) = {c[n % g]}")
            else:
                rest.append(n)
        todo = rest
    print(f"    third round: without an explicit witness: {len(todo)}")
# verify each witness: build the lift n0 mod lcm(M, R): n0 = n (mod M), n0 = -4u (mod R); check class conditions
bad = 0; jacobi_bad = 0; maxR = 0
for n, (R, (m, u)) in witness.items():
    n0, L = crt([(n, M), ((-4 * u) % R, R)])
    maxR = max(maxR, R)
    ok = (m * m) % u == 0 and (n0 + R) % (4 * m) == 0 and (n0 + 4 * u) % R == 0 and gcd(n0, R) == 1 and R % 4 == 3
    if not ok: bad += 1
    # Lemma j1square formula: (n/R) = - prod_{l | u} eps_l(n)^{v_l(u)}
    rhs = -1
    for l, e in factorint(u).items():
        eps = (1 if n0 % 8 == 1 else -1) if l == 2 else jacobi_symbol(n0 % l, l)
        rhs *= eps**e
    if jacobi_symbol(n0 % R, R) != rhs: jacobi_bad += 1
print(f"    witnesses verified: {len(witness)}; bad class conditions {bad}; Lemma j1square formula failures {jacobi_bad}; largest R used {maxR}")
# sample: an actual prime in the lift, with an explicit solution verified exactly
def solve_from_cert(p, R, u):
    a = (p + R) // 4; N = p * a; d = p * u               # middle channel M_a: d = p u
    assert (a * a) % u == 0 and (u + a) % R == 0 and gcd(R, p * a) == 1
    y = (N + d) // R; z = (N + N * N // d) // R
    assert (N + d) % R == 0 and (N + N * N // d) % R == 0
    return a, y, z
sample = random.sample(sorted(witness), 400)
nsol = 0
for n in sample:
    R, (m, u) = witness[n]
    n0, L = crt([(n, M), ((-4 * u) % R, R)])
    p = n0
    while not isprime(p): p += L
    a, y, z = solve_from_cert(p, R, u)
    assert 4 * a * y * z == p * (a * y + y * z + z * a)
    nsol += 1
print(f"    sampled lifts with an explicit prime solution verified: {nsol}")
# (2b) the 'if' direction on the same shells: no certificate (any u from available primes) hits a square class
hitsq = 0
for R in shells[:400]:
    g = gcd(M, R)
    for n in random.sample(sorted(square), 300):
        if n % g in certs(R, n): hitsq += 1
print(f"    'if' direction spot check: square classes hit by the first 400 shells: {hitsq}")

# (3) semigroup sizes, by the exponent-vector description: an element of <3,5,7,11,19,23> (with 1) modulo M is
#     determined by (e_q >= 1 ? 0 : unit part) at each odd prime of M and by its value mod 8.  We enumerate
#     exponent vectors e_q in [0, K) with K large enough (all orders divide 1980), reducing on the fly.
import numpy as np
S = np.array([1], dtype=np.int64)
for q in P:
    pw = [1]
    cur = 1
    for _ in range(1, 2000):
        cur = (cur * q) % M
        pw.append(cur)
    pw = np.unique(np.array(pw, dtype=np.int64))
    S = np.unique((S[:, None] * pw[None, :]) % M)
print(f"(3) products of powers of 3,5,7,11,19,23 modulo M (with 1): {len(S)} (claim 45,139); = 3 mod 4: {int((S % 4 == 3).sum())} (claim 22,074)")
print(f"time {time.time() - T0:.1f}s")
