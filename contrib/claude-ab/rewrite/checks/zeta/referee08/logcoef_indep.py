# Referee: independent formal log of D_5 via the derivation d(n^{-s}) = Omega(n) n^{-s}:
# Omega(n) r_n = d_n Omega(n) - sum_{m|n, 1<m<n} Omega(m) r_m d_{n/m}.
from fractions import Fraction as Fr
from sympy import factorint
N = 3000
d = [0]*(N+1)
for n in range(1, N+1): d[n] = 1 if n % 5 in (1, 4) else 0
Om = [0]*(N+1)
for n in range(2, N+1): Om[n] = sum(factorint(n).values())
divs = [[] for _ in range(N+1)]
for m in range(2, N+1):
    for n in range(2*m, N+1, m): divs[n].append(m)
r = [Fr(0)]*(N+1)
for n in range(2, N+1):
    s = Fr(d[n]*Om[n]) - sum(Om[m]*r[m]*d[n//m] for m in divs[n] if d[n//m])
    r[n] = s / Om[n]
neg = [n for n in range(2, N+1) if r[n] < 0]
print("r_36 =", r[36], "; first negatives:", neg[:6], "; count n<=3000 with r_n<0:", len(neg))
# primes of S_5 up to 60 via this: irreducible = element >1 of S not product of two elements >1 of S
S = [n for n in range(2, 61) if d[n]]
irr = [n for n in S if not any(n % a == 0 and d[n//a] and 1 < a < n for a in S)]
print("irreducibles up to 60:", irr)
