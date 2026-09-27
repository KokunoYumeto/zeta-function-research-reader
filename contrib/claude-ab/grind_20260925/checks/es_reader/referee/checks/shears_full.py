from math import gcd
from sympy import primerange, divisors
import sys
LIM = int(sys.argv[1])
def W(p, a):
    R = 4*a - p
    D = divisors(p*a)
    return {(m, n) for m in D for n in D if gcd(m, n) == 1 and (m + n) % R == 0}
first_len = {}
maxdeg_ok = True
comp_paths = True
for p in primerange(3, LIM):
    lo = p//4 + 1
    Ws = {a: W(p, a) for a in range(lo, p)}
    succ = {}; indeg = {}
    for a in range(lo, p - 1):
        for (m, n) in Ws[a]:
            for t in ((m + n, n), (m, m + n)):
                if t in Ws[a + 1]:
                    succ.setdefault((a, m, n), []).append((a + 1,) + t)
                    indeg[(a + 1,) + t] = indeg.get((a + 1,) + t, 0) + 1
    if any(len(v) > 1 for v in succ.values()) or any(v > 1 for v in indeg.values()): maxdeg_ok = False
    # longest path (DAG: a increases)
    memo = {}
    def longest(v):
        if v in memo: return memo[v]
        r = 0
        for w in succ.get(v, []): r = max(r, 1 + longest(w))
        memo[v] = r; return r
    Lmax = max([longest(v) for v in succ] + [0])
    for k in range(1, Lmax + 1):
        first_len.setdefault(k, p)
    if Lmax >= 2 and p % 3 != 2: print("VIOLATION at", p)
print("in/out-degree <= 1 everywhere:", maxdeg_ok)
print("least prime with a directed path of length k (full graph, p <", LIM, "):", first_len)
