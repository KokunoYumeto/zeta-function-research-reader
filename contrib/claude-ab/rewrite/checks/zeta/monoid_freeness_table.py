# claude-ab: for q = 1..12, the one-sided sheet monoid M_q = {n >= 1: n = 1 mod q} (zeta(s,1/q) = q^s D_{M_q}) and the
# even-sheet monoid S_q = {n >= 1: n = +-1 mod q} (zeta(s,1/q)+zeta(s,1-1/q) = q^s D_{S_q}):
# first non-unique factorization and first negative coefficient of the formal logarithm (exact rationals, n <= N).
from fractions import Fraction as Fr
from math import gcd
N = 4000
def analyse(inset):
    elems = [n for n in range(2, N+1) if inset(n)]
    S = set(elems)
    irr = [n for n in elems if not any(n % a == 0 and (n//a) in S for a in elems if a < n and a*a <= n)]
    # factorization counts up to N by dynamic programming over irreducibles (multisets)
    cnt = [0]*(N+1); cnt[1] = 1
    for p in irr:
        for n in range(p, N+1):
            if n % p == 0 and cnt[n//p]: pass
        # multiset DP: process each irreducible once, allowing repetition
        for n in range(p, N+1):
            if n % p == 0: cnt[n] += cnt[n//p]
    nonuniq = next((n for n in elems if cnt[n] > 1), None)
    # formal log of D = sum_{n in S or n=1} n^{-s}
    d = [Fr(0)]*(N+1); d[1] = Fr(1)
    for n in elems: d[n] = Fr(1)
    E = d[:]; E[1] = Fr(0); logc = [Fr(0)]*(N+1); P = E[:]; k = 1
    while any(P):
        for n in range(N+1): logc[n] += Fr((-1)**(k+1), k)*P[n]
        Q = [Fr(0)]*(N+1)
        for i in range(2, N+1):
            if P[i]:
                for j in range(2, N//i+1):
                    if E[j]: Q[i*j] += P[i]*E[j]
        P = Q; k += 1
    neg = next((n for n in range(2, N+1) if logc[n] < 0), None)
    return nonuniq, neg, (str(logc[neg]) if neg else None)
print(" q | one-sided M_q={n=1 mod q}: first non-unique, first negative log coeff | even S_q={n=+-1 mod q}: same | phi(q)")
for q in range(1, 13):
    m1 = analyse(lambda n, q=q: n % q == 1 % q)
    m2 = analyse(lambda n, q=q: n % q in {1 % q, (q-1) % q})
    phi = sum(1 for k in range(1, q+1) if gcd(k, q) == 1)
    print("%2d | %s | %s | %d" % (q, m1, m2, phi))
