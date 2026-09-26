#!/usr/bin/env python3
"""Independent recomputation of the second-order coefficient bounds (m_2, t_2) of YM-01 / YM-05.

Source values (FIFTH_REFERENCE.md F26; also 17 Sep reader R29 via (3/2)m2-6t2 = 1136/13):
    m_2 = 5834/39,  t_2 = 137/6.
Nothing from the workbench is imported. Method:
  * v_1 = (1/3) sum_p W_p; v_2 = B(v_1, v_1) = (1/9) sum_{p,q} B(W_p, W_q), B = K^{-1} Q_H Gamma.
  * Character algebra (hand-derived, also checked numerically below):
      B(W_p, W_p) = -(1/8) chi_1(U_p)            [block: spin 1 on the 4 edges of p, Casimir 8]
      p != q sharing edge e:  B(W_p,W_q) = (1/6) P0(W_p W_q) - (1/26) P1(W_p W_q)
      where P_lambda projects onto spin lambda on e (Casimirs 9/2 and 13/2 of the output blocks).
  * Fourier-algebra norm ||f||_X = sum_j ||A_j(f)||_1 computed from explicit SU(2) coefficient
    tensors (inverse links written with sigma_2 conjugation), projected with the exact
    Sym^2 / Lambda^2 projectors on the two occurrences of the shared link.
  * Norms of F6: ||v||_loc = sup_a sum_{S ni a} c_j ||A||_1, m = sup_a sum_{S ni a} (sum_e j_e)||A||_1,
    t = sup_e sum_{S ni e} j_e ||A||_1, with label S = union of the input plaquettes' edges,
    anchor a = the x-link at the origin of the infinite cubic lattice (all links equivalent under
    translations and axis permutations, which preserve link orientation).
"""
import itertools, numpy as np
from fractions import Fraction as F

s2 = np.array([[0, -1j], [1j, 0]])
def occ_tensor(sign):
    # M[x,y,c,d] with (U^sign)_{xy} = sum_{cd} M[x,y,c,d] U_{cd}
    M = np.zeros((2, 2, 2, 2), dtype=complex)
    for x, y, c, d in itertools.product(range(2), repeat=4):
        M[x, y, c, d] = (x == c and y == d) if sign > 0 else s2[y, c] * s2[d, x]
    return M

def word_matrix(signs):
    """T[(c),(d)] for the closed word tr(prod_k U_k^{s_k}), all links distinct, as a 2^l x 2^l matrix."""
    l = len(signs); Ms = [occ_tensor(s) for s in signs]
    T = np.zeros((2,) * (2 * l), dtype=complex)
    for r in itertools.product(range(2), repeat=l):
        term = None
        for k in range(l):
            f = Ms[k][r[k], r[(k + 1) % l]]  # 2x2 over (c_k, d_k)
            term = f if term is None else np.multiply.outer(term, f)
        # term axes: c0,d0,c1,d1,... -> reorder to c0..c_{l-1}, d0..d_{l-1}
        T += np.transpose(term, [2 * k for k in range(l)] + [2 * k + 1 for k in range(l)])
    return T.reshape(2**l, 2**l)

def tn(M): return float(np.linalg.svd(M, compute_uv=False).sum())

# projectors on V (x) V
I4 = np.eye(4); SW = np.zeros((4, 4))
for a, b in itertools.product(range(2), repeat=2): SW[2 * b + a, 2 * a + b] = 1
Psym, Panti = (I4 + SW) / 2, (I4 - SW) / 2

def slot_projector(P, n_slots, k1, k2):
    """P acting on tensor slots k1,k2 of (C^2)^{n_slots}, identity elsewhere."""
    dim = 2**n_slots
    Pt = P.reshape(2, 2, 2, 2)
    out = np.zeros((2,) * (2 * n_slots))
    for idx in itertools.product(range(2), repeat=n_slots):
        for a2, b2 in itertools.product(range(2), repeat=2):
            v = Pt[a2, b2, idx[k1], idx[k2]]
            if v == 0: continue
            jdx = list(idx); jdx[k1] = a2; jdx[k2] = b2
            out[tuple(jdx) + idx] += v
    return out.reshape(dim, dim)

# ---- lattice
E = [np.array(v) for v in ((1, 0, 0), (0, 1, 0), (0, 0, 1))]
def plaq(n, i, j):
    n = np.array(n)
    return [(tuple(n), i, +1), (tuple(n + E[i]), j, +1), (tuple(n + E[j]), i, -1), (tuple(n), j, -1)]
R = 3
plaqs = [(n, i, j) for n in itertools.product(range(-R, R + 1), repeat=3) for i in range(3) for j in range(i + 1, 3)]
P_occ = {p: plaq(*p) for p in plaqs}
P_edges = {p: {(o[0], o[1]) for o in P_occ[p]} for p in plaqs}
anchor = ((0, 0, 0), 0)

report = []
def rep(name, ok, val=None):
    report.append(ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}" + ("" if val is None else f": {val}"))

# sanity: single plaquette norm 8 and chi_1 norm 27
p0 = ((0, 0, 0), 0, 1)
Tp = word_matrix([o[2] for o in P_occ[p0]])
rep("||W_p||_X = 8 (F12 with l=4, k=1, d=2)", abs(tn(Tp) - 8) < 1e-9, round(tn(Tp), 9))
Tpp = np.kron(Tp, Tp)  # 8 slots: p occurrences 0..3, copy 4..7
Pall = np.eye(256)
for k in range(4): Pall = Pall @ slot_projector(Psym, 8, k, 4 + k)
chi1 = Pall @ Tpp @ Pall
rep("||chi_1(U_p)||_X = 27 (spin-1 part of W_p^2)", abs(tn(chi1) - 27) < 1e-8, round(tn(chi1), 9))

def pair_norms(p, q):
    shared = P_edges[p] & P_edges[q]; assert len(shared) == 1; e = next(iter(shared))
    k1 = next(k for k, o in enumerate(P_occ[p]) if (o[0], o[1]) == e)
    k2 = next(k for k, o in enumerate(P_occ[q]) if (o[0], o[1]) == e)
    T = np.kron(word_matrix([o[2] for o in P_occ[p]]), word_matrix([o[2] for o in P_occ[q]]))
    P0 = slot_projector(Panti, 8, k1, 4 + k2); P1 = slot_projector(Psym, 8, k1, 4 + k2)
    return e, tn(P0 @ T @ P0), tn(P1 @ T @ P1), tn(T)

cache = {}
m2 = t2 = loc2 = 0.0
# diagonal pieces: p contains the anchor
for p in plaqs:
    if anchor in P_edges[p]:
        coef = 27 / 72  # (1/9)(1/8)*27
        m2 += coef * 4; t2 += coef * 1; loc2 += coef * 8
# off-diagonal pieces: unordered adjacent pairs with anchor in the union label
pairs = set()
for p in plaqs:
    if anchor not in P_edges[p]: continue
    for q in plaqs:
        if q != p and len(P_edges[p] & P_edges[q]) == 1:
            pairs.add(frozenset((p, q)))
rep("number of adjacent pairs whose union label contains the anchor = 42", len(pairs) == 42, len(pairs))
shapes = {}
for pr in pairs:
    p, q = sorted(pr)
    e, n0, n1, nT = pair_norms(p, q)
    key = (round(n0, 6), round(n1, 6)); shapes[key] = shapes.get(key, 0) + 1
    w = 2 / 9  # ordered pairs (p,q),(q,p) times 1/9
    m2 += w * ((1 / 6) * 3 * n0 + (1 / 26) * 4 * n1)
    ja0 = 0 if e == anchor else 0.5; ja1 = 1 if e == anchor else 0.5
    t2 += w * ((1 / 6) * ja0 * n0 + (1 / 26) * ja1 * n1)
    loc2 += w * ((1 / 6) * 4.5 * n0 + (1 / 26) * 6.5 * n1)
print("INFO (||P0 part||_1, ||P1 part||_1) -> number of pairs:", shapes)
rep("exact m(v_2) <= source bound 5834/39 (source is a valid upper bound)", m2 <= 5834 / 39 + 1e-9, f"exact {m2:.10f} vs source {5834/39:.10f}")
rep("exact t(v_2) <= source bound 137/6 (source is a valid upper bound)", t2 <= 137 / 6 + 1e-9, f"exact {t2:.10f} vs source {137/6:.10f}")
# Reconstruction of the source's bookkeeping: every pair bounded by the reflection maximum (16, 48);
# for t, the shared-edge spin-1 channel bounded by the full product norm ||W_p||*||W_q|| = 64 (source L3).
m_src = F(6) + 42 * F(2, 9) * (F(1, 6) * 3 * 16 + F(1, 26) * 4 * 48)
loc_src = F(12) + 42 * F(2, 9) * (F(1, 6) * F(9, 2) * 16 + F(1, 26) * F(13, 2) * 48)
t_src = F(3, 2) + 6 * (F(2, 9) * F(1, 26) * 64) + 36 * (F(2, 9) * (F(1, 6) * F(1, 2) * 16 + F(1, 26) * F(1, 2) * 48))
rep("reflection-maximum bookkeeping reproduces m_2 = 5834/39 exactly", m_src == F(5834, 39), m_src)
rep("reflection-maximum bookkeeping reproduces ||v_2||_loc = 236 exactly (17 Sep reader md L479)", loc_src == 236, loc_src)
rep("source formula 3/2 + 6*(64/117) + 36*(176/351) = 137/6", t_src == F(137, 6) and F(2, 9) * F(1, 26) * 64 == F(64, 117), t_src)
print(f"INFO ||v_2||_loc (anchor sum) = {loc2:.10f}  (as a fraction ~ {F(loc2).limit_denominator(2000)})")
rep("(3/2)m_2 - 6t_2 = 1136/13 (17 Sep R29 coefficient)", F(3, 2) * F(5834, 39) - 6 * F(137, 6) == F(1136, 13))
print("ALL PASS" if all(report) else "SOME FAIL")
