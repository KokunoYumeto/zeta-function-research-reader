# Referee computation: exact local norms of the order-2 and order-3 vacuum-source coefficients
#   m(v_n) = sup_a sum_{S ni a} sum_j (sum_e j_e) ||A_{S,j}||_1,  t(v_n) = sup_e sum_{S ni e} sum_j j_e ||A_{S,j}||_1,
#   ||v_n||_loc = sup_a sum_{S ni a} sum_j c_j ||A_{S,j}||_1        (F6, with edge-set labels S),
# for v1 = S/3, v2 = B(v1, v1), v3 = 2 B(v1, v2), B = K^{-1} Q_H Gamma, on the infinite cubic lattice
# (every box uses a subset of the labels).  All anchors are equivalent under translations and axis
# permutations, which preserve link orientations and hence the Fourier-algebra norms.
import itertools, time, sys, json
import numpy as np
from fractions import Fraction as Fr
from ym_blocks import plaquette, links_of, trace_norm, HALF
from ym_fast import Block, plaquette_block, product_blocks, B_of, casimir

def all_plaquettes(R):
    P = []
    for n in itertools.product(range(-R, R + 1), repeat=3):
        for i in range(3):
            for j in range(i + 1, 3):
                P.append(plaquette(n, i, j))
    return P

def v2_terms(P):
    """(coefficient, Block, label) for v2 = -(1/72) sum chi_1(V_p) + sum_{p~q} [(1/27) P0 - (1/117) P1]."""
    PB = {p[0]: plaquette_block(p) for p in P}
    L = {p[0]: links_of(p) for p in P}
    terms = []
    for p in P:
        for b, sh in product_blocks(PB[p[0]], PB[p[0]]):
            if all(v[2] == 1 for v in sh.values()):
                terms.append((Fr(-1, 72), b, L[p[0]]))
    for p, q in itertools.combinations(P, 2):
        if len(L[p[0]] & L[q[0]]) == 1:
            for b, sh in product_blocks(PB[p[0]], PB[q[0]]):
                s = list(sh.values())[0][2]
                terms.append((Fr(1, 27) if s == 0 else Fr(-1, 117), b, L[p[0]] | L[q[0]]))
    return terms

def accumulate_order2(anchor, R=2):
    P = all_plaquettes(R); PB = {p[0]: plaquette_block(p) for p in P}; L = {p[0]: links_of(p) for p in P}
    acc = {}
    for p in P:
        for q in P:
            if not (L[p[0]] & L[q[0]]): continue
            label = L[p[0]] | L[q[0]]
            if anchor not in label: continue
            for blk, gamma, cj in B_of(PB[q[0]], PB[p[0]]):
                if gamma == 0 or cj == 0: continue
                key = (label, blk.key()); c = float(Fr(1, 9) * gamma / cj)
                acc[key] = acc.get(key, 0) + c * blk.A
    return acc

def order3_by_label(anchor, R=2):
    """Group all contributions (coef, X, r) of v3 = (2/3) sum_r sum_X coef_X B(W_r, X) by edge label containing the anchor."""
    P = all_plaquettes(R); PB = {p[0]: plaquette_block(p) for p in P}; L = {p[0]: links_of(p) for p in P}
    terms = v2_terms(P)
    groups = {}
    for coefX, X, labX in terms:
        act = set(X.links)
        for r in P:
            if not (L[r[0]] & act): continue
            label = L[r[0]] | labX
            if anchor not in label: continue
            groups.setdefault(label, []).append((coefX, X, PB[r[0]]))
    return groups

def norms_order3(anchor, R=2, keep_per_label=False):
    groups = order3_by_label(anchor, R)
    m = t = loc = 0.0; nlab = 0; nprod = 0; per_label = {}; sizes = {}
    for label, contribs in groups.items():
        acc = {}
        for coefX, X, rb in contribs:
            for blk, gamma, cj in B_of(rb, X):
                nprod += 1
                if gamma == 0: continue
                c = float(Fr(2, 3) * coefX * gamma / cj)
                k = blk.key(); acc[k] = acc.get(k, 0) + c * blk.A
        mm = tt = ll = 0.0
        for k, A in acc.items():
            d = int(round(np.sqrt(A.size))); nrm = trace_norm(A.reshape(d, d))
            if nrm < 1e-11: continue
            sumj = float(sum(s for e, s in k)); cj = float(sum(s * (s + 1) for e, s in k))
            ja = float(sum(s for e, s in k if e == anchor))
            mm += sumj * nrm; ll += cj * nrm; tt += ja * nrm
        if ll > 0:
            nlab += 1; sizes[len(label)] = sizes.get(len(label), 0) + 1
            if keep_per_label: per_label[label] = (mm, tt, ll)
        m += mm; t += tt; loc += ll
        del acc
    return m, t, loc, nlab, nprod, sizes, per_label

def norms(acc, anchor):
    m = t = loc = 0.0; labels = set(); per_label = {}
    for (label, key), A in acc.items():
        d = int(round(np.sqrt(A.size)))
        nrm = trace_norm(A.reshape(d, d))
        if nrm < 1e-11: continue
        labels.add(label)
        sumj = float(sum(s for e, s in key)); cj = float(sum(s * (s + 1) for e, s in key))
        ja = float(sum(s for e, s in key if e == anchor))
        m += sumj * nrm; loc += cj * nrm; t += ja * nrm
        per_label[label] = per_label.get(label, 0.0) + cj * nrm
    return m, t, loc, labels, per_label

if __name__ == '__main__':
    anchor = ((0, 0, 0), 0)
    R = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    t0 = time.time()
    m2, t2, l2, lab2, _ = norms(accumulate_order2(anchor, R), anchor)
    print(f"[R={R}] order 2: m(v2) = {m2:.10f}  t(v2) = {t2:.10f}  ||v2||_loc = {l2:.10f}  anchored labels {len(lab2)}  ({time.time()-t0:.1f}s)", flush=True)
    t0 = time.time()
    m3, t3, l3, nlab, nprod, sizes, _ = norms_order3(anchor, R)
    print(f"[R={R}] order 3: m(v3) = {m3:.10f}  t(v3) = {t3:.10f}  ||v3||_loc = {l3:.10f}  anchored labels {nlab} by link count {dict(sorted(sizes.items()))}, {nprod} block products  ({time.time()-t0:.1f}s)")
    print(f"workbench (F26): m3 = {336572872/208845:.6f}, t3 = {225985217/1253070:.6f};  C23: ||v3||_loc <= 944984/351 = {944984/351:.6f}")
    json.dump({'R': R, 'm2': m2, 't2': t2, 'loc2': l2, 'm3': m3, 't3': t3, 'loc3': l3, 'labels3': nlab},
              open(f'ym_order3_R{R}.json', 'w'), indent=1)
