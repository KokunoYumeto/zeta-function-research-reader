# Referee computation: the exact order-3 source norms m(v3), t(v3), ||v3||_loc (F6 norms, edge labels)
# of the workbench's vacuum source, from v1 = S/3 and the exact v2, with v3 = 2B(v1, v2).
# Uses only ym_blocks.py (independent of all workbench code).
import itertools, time, sys
import numpy as np
from fractions import Fraction as Fr
from ym_blocks import *

def chi1_term(p):
    """chi_1(V_p) = the all-spin-1 block of W_p W_p."""
    return {'plaqs': [p, p], 'coup': {e: ([(0, pos), (1, pos)], [HALF, Fr(1)]) for pos, (e, s) in enumerate(p[1])},
            'label': links_of(p)}

def pair_term(p, q, s):
    """P_s(W_p W_q): the shared link of the adjacent faces p, q projected on spin s (other links spin 1/2)."""
    lp, lq = links_of(p), links_of(q); e = next(iter(lp & lq))
    coup = {}
    for pos, (f, _) in enumerate(p[1]): coup[f] = ([(0, pos)], [HALF])
    posp = [k for k, (g, _) in enumerate(p[1]) if g == e][0]
    for pos, (f, _) in enumerate(q[1]):
        coup[f] = ([(0, posp), (1, pos)], [HALF, Fr(s)]) if f == e else ([(1, pos)], [HALF])
    return {'plaqs': [p, q], 'coup': coup, 'label': lp | lq}

def active_links(X): return frozenset(e for e, (occ, path) in X['coup'].items() if path[-1] != 0)

def eval_term(X, conf):
    sp, A = block_coefficient(X['plaqs'], X['coup'])
    return eval_block(sp, A, conf)

def B_blocks(r, X):
    """Blocks of W_r X, each with (spins, A_j, gamma_j, c_j), where Gamma(W_r, X) = sum gamma_j (W_r X)_j
    and B(W_r, X) = K^{-1} Q_H Gamma(W_r, X) = sum (gamma_j / c_j) (W_r X)_j."""
    ir = len(X['plaqs'])
    shared = [(pos, e) for pos, (e, s) in enumerate(r[1]) if e in X['coup']]
    options = []
    for pos, e in shared:
        sig = X['coup'][e][1][-1]
        options.append([sig + HALF] if sig == 0 else [sig + HALF, sig - HALF])
    out = []
    for choice in itertools.product(*options):
        coup = {e: (list(occ), list(path)) for e, (occ, path) in X['coup'].items()}
        gamma = Fr(0)
        for (pos, e), s2 in zip(shared, choice):
            occ, path = coup[e]; sig = path[-1]
            coup[e] = (occ + [(ir, pos)], path + [s2])
            if sig > 0:
                gamma += (-sig if s2 == sig + HALF else sig + 1) / 2
        for pos, (e, s) in enumerate(r[1]):
            if e not in X['coup']:
                coup[e] = ([(ir, pos)], [HALF])
        cj = sum(path[-1] * (path[-1] + 1) for occ, path in coup.values())
        sp, A = block_coefficient(X['plaqs'] + [r], coup)
        out.append((sp, A, gamma, cj))
    return out

def all_plaquettes(R):
    P = []
    for n in itertools.product(range(-R, R + 1), repeat=3):
        for i in range(3):
            for j in range(i + 1, 3):
                P.append(plaquette(n, i, j))
    return P

def v2_terms(P):
    terms = []
    for p in P: terms.append((Fr(-1, 72), chi1_term(p)))
    L = {p[0]: links_of(p) for p in P}
    for a_, b_ in itertools.combinations(P, 2):
        if len(L[a_[0]] & L[b_[0]]) == 1:
            terms.append((Fr(1, 27), pair_term(a_, b_, 0)))
            terms.append((Fr(-1, 117), pair_term(a_, b_, 1)))
    return terms

def v3_anchored(anchor, R=2, verbose=True):
    """All labelled blocks of v3 whose edge label contains the anchor link."""
    P = all_plaquettes(R)
    L = {p[0]: links_of(p) for p in P}
    terms = v2_terms(P)
    acc = {}
    t0 = time.time(); ncalls = 0
    for coefX, X in terms:
        act = active_links(X)
        for r in P:
            lr = L[r[0]]
            if not (lr & act): continue
            label = lr | X['label']
            if anchor not in label: continue
            for sp, A, gamma, cj in B_blocks(r, X):
                ncalls += 1
                if gamma == 0: continue
                c = Fr(2, 3) * coefX * gamma / cj
                key = (label, tuple(sp))
                acc[key] = acc.get(key, 0) + float(c) * A
    if verbose: print(f"  {ncalls} block evaluations, {len(acc)} labelled blocks, {time.time() - t0:.1f}s")
    return acc

def norms(acc, anchor):
    m = t = loc = 0.0
    labels = set()
    for (label, sp), A in acc.items():
        nrm = trace_norm(A)
        if nrm < 1e-12: continue
        labels.add(label)
        sumj = sum(float(s) for e, s in sp)
        cj = sum(float(s * (s + 1)) for e, s in sp)
        ja = sum(float(s) for e, s in sp if e == anchor)
        m += sumj * nrm; loc += cj * nrm; t += ja * nrm
    return m, t, loc, len(labels)

if __name__ == '__main__':
    anchor = ((0, 0, 0), 0)
    # order-2 reproduction through the same pipeline: v2 = (1/9) sum_{p,q} B(W_p, W_q)
    P = all_plaquettes(2); Lk = {p[0]: links_of(p) for p in P}
    acc2 = {}
    for p in P:
        Xp = {'plaqs': [p], 'coup': {e: ([(0, pos)], [HALF]) for pos, (e, s) in enumerate(p[1])}, 'label': Lk[p[0]]}
        for q in P:
            if not (Lk[q[0]] & Lk[p[0]]): continue
            label = Lk[p[0]] | Lk[q[0]]
            if anchor not in label: continue
            for sp, A, gamma, cj in B_blocks(q, Xp):
                if gamma == 0 or cj == 0: continue
                key = (label, tuple(sp)); acc2[key] = acc2.get(key, 0) + float(Fr(1, 9) * gamma / cj) * A
    m2, t2, loc2, nl2 = norms(acc2, anchor)
    print(f"order 2 through the pipeline: m = {m2:.10f}, t = {t2:.10f}, loc = {loc2:.10f}, labels = {nl2}")
    acc3 = v3_anchored(anchor, R=2)
    m3, t3, loc3, nl3 = norms(acc3, anchor)
    print(f"order 3: m(v3) = {m3:.10f}, t(v3) = {t3:.10f}, ||v3||_loc = {loc3:.10f}, anchored edge labels = {nl3}")
    print(f"workbench bounds: m3 = {336572872/208845:.6f}, t3 = {225985217/1253070:.6f}, ||v3||_loc <= 944984/351 = {944984/351:.6f}")
    # robustness: window radius 3 must give the same numbers
    if len(sys.argv) > 1 and sys.argv[1] == '--R3':
        acc3b = v3_anchored(anchor, R=3)
        print("R=3:", norms(acc3b, anchor))
