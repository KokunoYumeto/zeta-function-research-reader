# Referee check: exact local norms of the second vacuum coefficient v_2 = B(v_1, v_1), v_1 = S/3,
# on the infinite cubic lattice with all links positively oriented, at the anchor link (0,0,0)->(1,0,0).
# B(f,h) on an output block b of fh (f, h Casimir eigenfunctions): (c_f + c_h - c_b)/(2 c_b) (fh)_b  (from F17).
import numpy as np, itertools, sys
sys.path.insert(0, '.')
from r2_su2_blocks import *

rng = np.random.default_rng(7)

def plaqs_near(R=2):
    P = []
    for n in itertools.product(range(-R, R + 1), repeat=3):
        for i in range(3):
            for j in range(i + 1, 3):
                P.append((n, i, j))
    return P

def links_of(p):
    return [l for (l, s) in plaquette(*p)]

def W(p):
    return trace_word_tensor(plaquette(*p))

# ---- sanity checks ----
p0 = ((0, 0, 0), 0, 1)
bl = blocks(W(p0))
print("W_p blocks:", [(tuple(j for _, j in k), round(tnorm(A), 10)) for k, A in bl.items()])
U = {l: random_su2(rng) for l in links_of(p0)}
print("W_p evaluate vs blocks:", abs(evaluate(W(p0), U) - evaluate_blocks(bl, U)) < 1e-10)
sq = product(W(p0), W(p0)); bsq = blocks(sq)
print("W_p^2 blocks:", sorted((tuple(j for _, j in k), round(tnorm(A), 8)) for k, A in bsq.items()))
print("W_p^2 evaluate vs blocks:", abs(evaluate(sq, U) - evaluate_blocks(bsq, U)) < 1e-10)

def v2_norms(anchor, R=2):
    P = plaqs_near(R)
    Pset = {p: set(links_of(p)) for p in P}
    labels = []
    for p in P:
        if anchor in Pset[p]:
            labels.append(((p, p), 1.0 / 9.0))          # B(W_p,W_p) once in sum_{p,q}
    for p, q in itertools.combinations(P, 2):
        if Pset[p] & Pset[q] and (anchor in Pset[p] or anchor in Pset[q]):
            labels.append(((p, q), 2.0 / 9.0))          # (p,q) and (q,p)
    m = t = loc = 0.0
    kinds = {}
    for (p, q), pref in labels:
        prod = product(W(p), W(q))
        for key, A in blocks(prod).items():
            cb = casimir(key)
            if cb == 0: continue
            coef = pref * (6 - cb) / (2 * cb)
            nrm = tnorm(A)
            sj = sum(j for _, j in key)
            ja = dict(key).get(anchor, 0.0)
            m += abs(coef) * sj * nrm; t += abs(coef) * ja * nrm; loc += abs(coef) * cb * nrm
            if p != q:
                kinds.setdefault(round(nrm, 6), 0); kinds[round(nrm, 6)] += 1
    return m, t, loc, len(labels), kinds

anchor = ((0, 0, 0), 0)
m, t, loc, nl, kinds = v2_norms(anchor)
print(f"anchor x-link: m(v2) = {m:.10f}, t(v2) = {t:.10f}, ||v2||_loc = {loc:.10f}, labels = {nl}")
print("   block norms of pair products (norm: count):", kinds)
print("   closed forms: m = 6 + 11200/117 + 14(8/9 + 32 sqrt3/39) =", 6 + 11200 / 117 + 14 * (8 / 9 + 32 * np.sqrt(3) / 39))
for anc in (((0, 0, 0), 1), ((0, 0, 0), 2), ((1, -1, 0), 0)):
    mm, tt, ll, nl2, _ = v2_norms(anc)
    print(f"anchor {anc}: m = {mm:.10f}, t = {tt:.10f}, loc = {ll:.10f}, labels = {nl2}")
