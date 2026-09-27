# Kinetic row of H14: entries mu Gamma(W_p, W_q).  Gamma(W_p,W_q) = sum_b (6 - c_b)/2 P_b(W_p W_q) (F17 with c = 3).
import sys, itertools, numpy as np
sys.path.insert(0, '.')
from r2_order3 import *
p = ((0, 0, 0), 0, 1)
P = [(n, i, j) for n in itertools.product(range(-2, 3), repeat=3) for i in range(3) for j in range(i + 1, 3)]
nbrs = [q for q in P if q != p and set(links_of(p)) & set(links_of(q))]
def gamma_norm(p, q):
    f = product(W(p), W(q)); tot = 0.0; const = 0.0
    for key, M in blocks_fast(f).items():
        cb = casimir(key); nr = tnorm(M)
        if cb == 0: const += 3 * nr
        else: tot += abs((6 - cb) / 2) * nr
    return const, tot
c0, d0 = gamma_norm(p, p)
print("diagonal: ||Gamma(W_p,W_p)|| = constant part", c0, "+ nonconstant", d0, "=", c0 + d0, "(workbench: 30)")
vals = [gamma_norm(p, q)[1] for q in nbrs]
print("number of adjacent faces:", len(nbrs), " off-diagonal norms:", sorted(round(v, 6) for v in vals), "(workbench bound: 48 each)")
row = c0 + d0 + sum(vals)
print("exact row sum of Fourier norms:", row, " = 30 + 8*24 + 4*(6 + 6 sqrt3) =", 30 + 8 * 24 + 4 * (6 + 6 * np.sqrt(3)), " (workbench: 606)")
chi = 11 / 24
print("with the sharper mean bound |mu F| <= |P_H F| + chi ||Q_H F||: row <= 3 + chi*(27 + off) =", 3 + chi * (27 + sum(vals)))
