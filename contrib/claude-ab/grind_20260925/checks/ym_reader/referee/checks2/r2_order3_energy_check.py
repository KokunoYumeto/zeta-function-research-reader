# Cross-check of the v_2, v_3 machinery against the record's energy coefficient e4 = 5M/216 - 2J/1053
# (quartic cube reader, E2/E8): needs  int v2 K v2 = M/648 + 2J/1053  and  2 sum_r <W_r, v3> = -2M/81,
# i.e. W_r-coefficient of v3[{r,r,r}] = -1/81 and of v3[{p,p,r}] = 0 (p ~ r).
import sys, numpy as np, itertools
sys.path.insert(0, '.')
from r2_order3 import *
r = ((0, 0, 0), 0, 1); p = ((0, 0, 0), 0, 2)
Wr = W(r); keyW = tuple(sorted((l, 0.5) for l in links_of(r)))
AW = blocks_fast(Wr)[keyW]
def wcoef(bl):
    M = bl.get(keyW)
    if M is None: return 0.0
    return float(np.sum(M * AW) / np.sum(AW * AW))
print("W_r coefficient in v3[{r,r,r}] :", wcoef(v3_cluster((r, r, r))), " expected -1/81 =", -1 / 81)
print("W_r coefficient in v3[{p,p,r}] :", wcoef(v3_cluster(tuple(sorted((p, p, r))))), " expected 0")
# int v2 K v2 per label: sum_b x_b^2 c_b ||A_b||_HS^2 / d_b
def l2K(S):
    tot = 0.0
    for (x, cb, g) in X2(S):
        for key, M in blocks_fast(g).items():
            if casimir(key) != cb: continue
            d = np.prod([2 * j + 1 for _, j in key])
            tot += x * x * cb * np.sum(M * M) / d
    return tot
print("int v2[{p,p}] K v2[{p,p}] =", l2K((r, r)), " expected 1/648 =", 1 / 648)
print("int v2[{p,q}] K v2[{p,q}] =", l2K(tuple(sorted((p, r)))), " expected 2/1053 =", 2 / 1053)
q2 = ((0, 0, 0), 1, 2); q3 = ((1, 0, 0), 1, 2)
for q in (q2, q3, ((0, -1, 0), 0, 1)):
    print("   other adjacent pair", q, l2K(tuple(sorted((r, q)))))
