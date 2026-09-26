#!/usr/bin/env python3
"""Extra referee checks: Collatz template count (Thm 44.5 claim), 817 negative results 3 and 4."""
import time, itertools
T0 = time.time()
def out(*a): print(*a, flush=True)

def v2(n): return (n & -n).bit_length() - 1
def T(n):
    m = 3*n + 1; a = v2(m); return m >> a, a
def word(n, L):
    w = []
    for _ in range(L):
        n, a = T(n); w.append(a)
    return n, w

# ---- Collatz: which odd n < 400000 are the larger member of a template (any e, b, sigma, a' >= a_min)?
LIM = 400000
members = {}
for e in range(2, 40, 2):
    he = (2**e + 2)//3
    for b in range(1, 13):
        if 3**b > LIM: break
        for sig in (0, 1):
            amin = 1
            while 2**(amin + e + 2*b - sig) >= 3**(amin + b): amin += 1
            J = 2**(e + 2*b - sig); d, r = (4, 3) if sig == 0 else (32, 27)
            for ap in range(amin, 60):
                Q = 3**(ap + b)
                if Q > 50*LIM*d: break
                x = (-he * 3**b * pow(J, -1, Q)) % Q
                n = next((x + k*Q for k in range(d) if (x + k*Q) % d == r), None)
                while n is not None and n < LIM:
                    if n > 1:
                        num = 2**ap * J * n + 2**ap * he * 3**b
                        m = num // Q - 1
                        lw = [1] if sig == 0 else [1, 2, 1]
                        rw = [1]*ap + [e] + [2]*(b - 1) + ([3] if sig == 0 else [1, 1, 3])
                        yn, wn = word(n, len(lw)); ym, wm = word(m, len(rw))
                        if wn == lw and wm == rw and yn == ym and 0 < m < n:
                            members.setdefault(n, set()).add(e)
                    n += d*Q
out(f"odd n in (1, {LIM}) that are the larger member of some template: {len(members)} (note: 367); max e: {max(max(s) for s in members.values())}")

# ---- 817 negative result 3: B={2,7}, q=11, k=3: modular 3-AP exists, but base-11 lifts are 3-AP-free (lengths 1..4)
def H(A):
    S = {0}
    for a in A: S |= {s + a for s in S}
    return S
B = [2, 7]; HB = sorted(H(B)); q = 11
modap = any(all((x + j*dd) % q in {h % q for h in HB} for j in range(3)) for x in range(q) for dd in range(1, q))
def has_int_ap(S, k):
    S = sorted(S); Ss = set(S)
    for i, x in enumerate(S):
        for y in S[i+1:]:
            dd = y - x
            if all(x + j*dd in Ss for j in range(2, k)): return True
    return False
lift_free = []
for L in range(1, 5):
    lang = {sum(dg * q**i for i, dg in enumerate(digs)) for digs in itertools.product(HB, repeat=L)}
    lift_free.append(not has_int_ap(lang, 3))
out("B={2,7}, q=11, k=3: modular 3-AP present:", modap, "; base-11 digit languages 3-AP-free for lengths 1..4:", lift_free)

# ---- 817 negative result 4: for B* every base q in 71..96 fails at k=5 (a 5-AP in the 2- or 3-digit language)
Bs = [1, 4, 5, 17, 21, 22]; HBs = sorted(H(Bs))
def first_fail(qq, k, maxlen=3):
    for L in range(1, maxlen + 1):
        lang = {sum(dg * qq**i for i, dg in enumerate(digs)) for digs in itertools.product(HBs, repeat=L)}
        if has_int_ap(lang, k): return L
    return None
f5 = {qq: first_fail(qq, 5) for qq in range(71, 98)}
f6 = {qq: first_fail(qq, 6) for qq in range(71, 94)}
out("B*, k=5: bases 71..96 with an integer 5-AP within 3 digits:", all(f5[qq] for qq in range(71, 97)), "; base 97:", f5[97])
out("B*, k=6: bases 71..92 with an integer 6-AP within 3 digits:", all(f6[qq] for qq in range(71, 93)), "; base 93:", f6[93])
out(f"total {time.time()-T0:.1f}s")
