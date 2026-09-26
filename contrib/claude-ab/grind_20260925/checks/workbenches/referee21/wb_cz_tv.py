# Referee 21 (wbreader): Theorem 2.2 numerical TV values at N = 2^20 (starts 1,3,...,2^21-1, i.e. b = 0),
# m = floor(L/2 + c sqrt(L)), L = 20; TV(P, G_m) = 1 - sum_w min(P(w), 2^-A(w)).
import math
from collections import Counter
N = 2**20; L = 20
cs = [-1, -0.5, 0, 0.5, 1]
ms = [math.floor(L/2 + c*math.sqrt(L)) for c in cs]
M = max(ms)
words = []
for k in range(N):
    n = 2*k+1; w = []
    for _ in range(M):
        x = 3*n+1; a = (x & -x).bit_length()-1; n = x >> a; w.append(a)
    words.append(tuple(w))
Phi = lambda z: 0.5*(1+math.erf(z/math.sqrt(2)))
for c, m in zip(cs, ms):
    cnt = Counter(w[:m] for w in words)
    s = sum(min(v/N, 2.0**(-sum(w))) for w, v in cnt.items())
    print(f"c={c:5}: m={m:2d}  TV={1-s:.3f}  Phi(2c)={Phi(2*c):.3f}")
