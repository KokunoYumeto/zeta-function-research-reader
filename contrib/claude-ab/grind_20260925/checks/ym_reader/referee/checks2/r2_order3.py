# Referee check: exact local norms of the third vacuum coefficient v_3 = 2 B(v_1, v_2) of the YM workbench,
# computed independently (explicit SU(2) coefficient tensors, real Clebsch-Gordan intertwiners, trace norms by SVD).
#   v_1 = (1/3) sum_r W_r,  v_2 = sum_S X_S,  X_S = sum_b x^S_b P_b(prod_{p in S} W_p),
#   B(f,h) = sum_{b' != 0} (c_f + c_h - c_b')/(2 c_b') P_b'(f h)   for Casimir eigenfunctions f, h (F17).
# Norms at the anchor link (0,0,0)->(1,0,0) on the infinite lattice with positive link orientations:
#   m(v) = sum_{L ∋ a} sum_b (sum_e j_e) ||A_{L,b}||_1,  t(v) = sum_{L ∋ a} sum_b j_a ||A_{L,b}||_1,
#   ||v||_loc = sum_{L ∋ a} sum_b c_b ||A_{L,b}||_1.
# Symmetries used (norm-preserving for real functions): translations, axis permutations, point inversion.
import numpy as np, itertools, time, sys, json
from functools import lru_cache

# ---------------- real SU(2) machinery ----------------
C2 = np.array([[0., 1.], [-1., 0.]]); C2inv = np.linalg.inv(C2)
def _ops(n):
    sz = np.diag([0.5, -0.5]); sm = np.array([[0., 0.], [1., 0.]])   # S_- |up> = |down>, basis (up, down)
    sp = sm.T
    def tot(s):
        T = np.zeros((2**n, 2**n))
        for k in range(n):
            M = np.array([[1.]])
            for q in range(n): M = np.kron(M, s if q == k else np.eye(2))
            T += M
        return T
    Sz, Sm, Sp = tot(sz), tot(sm), tot(sp)
    Csq = Sz @ Sz + (Sp @ Sm + Sm @ Sp) / 2
    return Sz, Sm, Csq
@lru_cache(maxsize=None)
def intertwiners(n):
    if n == 1: return {0.5: [np.eye(2)]}
    Sz, Sm, Csq = _ops(n)
    w, V = np.linalg.eigh(Csq)
    jj = (-1 + np.sqrt(1 + 4 * np.maximum(w, 0))) / 2
    out = {}
    for j in sorted(set(np.round(jj * 2) / 2)):
        cols = V[:, np.abs(jj - j) < 1e-6]
        wz, Vz = np.linalg.eigh(cols.T @ Sz @ cols)
        hw = cols @ Vz[:, np.abs(wz - j) < 1e-6]
        Js = []
        for c in range(hw.shape[1]):
            vecs = [hw[:, c]]; m = j
            while m > -j + 1e-9:
                v = Sm @ vecs[-1] / np.sqrt(j * (j + 1) - m * (m - 1)); vecs.append(v); m -= 1
            Js.append(np.array(vecs).T)
        out[float(j)] = Js
    return out
def projector(n, j):
    return sum(J @ J.T for J in intertwiners(n)[j])

def plaquette(n, i, j):
    ei = tuple(1 if k == i else 0 for k in range(3)); ej = tuple(1 if k == j else 0 for k in range(3))
    add = lambda a, b: tuple(x + y for x, y in zip(a, b))
    return [((tuple(n), i), +1), ((add(n, ei), j), +1), ((add(n, ej), i), -1), ((tuple(n), j), -1)]
def links_of(p): return [l for (l, s) in plaquette(*p)]

@lru_cache(maxsize=None)
def _word_T():
    Tp = np.zeros((2, 2, 2, 2)); Tm = np.zeros((2, 2, 2, 2))
    for r in range(2):
        for c in range(2):
            Tp[r, c, r, c] = 1.0
            for a in range(2):
                for b in range(2): Tm[r, c, a, b] = C2[r, b] * C2inv[a, c]
    return Tp, Tm
def W(p):
    word = plaquette(*p); Tp, Tm = _word_T(); F = None
    for (link, s) in word:
        T = Tp if s > 0 else Tm
        if F is None: F = T
        else:
            F = np.tensordot(F, T, axes=([1], [0])); F = np.moveaxis(F, -3, 1)
    F = np.trace(F, axis1=0, axis2=1)
    K = 4
    F = np.transpose(F, [2 * k for k in range(K)] + [2 * k + 1 for k in range(K)])
    return ([w[0] for w in word], F)
def product(f, g):
    (lf, Ff), (lg, Fg) = f, g; Kf, Kg = len(lf), len(lg)
    P = np.multiply.outer(Ff, Fg)
    perm = list(range(Kf)) + list(range(2 * Kf, 2 * Kf + Kg)) + list(range(Kf, 2 * Kf)) + list(range(2 * Kf + Kg, 2 * Kf + 2 * Kg))
    return (lf + lg, np.ascontiguousarray(np.transpose(P, perm)))
def project(f, link, j):
    links, F = f; K = len(links); occ = [k for k in range(K) if links[k] == link]; n = len(occ)
    Pm = projector(n, j)
    # contract a-axes of this link with Pm (F'[a,b] = sum_a' F[a',b] Pm[a',a])
    F2 = np.moveaxis(F, occ, list(range(n)))
    sh = F2.shape
    F2 = np.tensordot(Pm.reshape([2] * (2 * n)), F2, axes=(list(range(n)), list(range(n))))  # new a (n axes) first
    F2 = np.moveaxis(F2, list(range(n)), occ)
    return (links, F2)

def blocks_fast(f):
    """dict: tuple((link, spin) sorted by link) -> real block matrix (alpha, beta) (trace norm = Fourier block norm)"""
    links, F = f; K = len(links)
    uniq = sorted(set(links)); occ = {l: [k for k in range(K) if links[k] == l] for l in uniq}
    # bring axes to order: for each link in uniq: its a-axes then its b-axes
    order = []
    for l in uniq: order += occ[l] + [K + k for k in occ[l]]
    T0 = np.transpose(F, order)
    # partial results: list of (key_list, tensor with remaining axes); process links sequentially from the front
    parts = [([], T0)]
    for l in uniq:
        n = len(occ[l]); new = []
        for key, T in parts:
            # T axes: [processed dims ... (2 per processed link: alpha,beta)] + [n a-axes, n b-axes of l] + rest
            npre = 2 * len(key)
            sh = T.shape
            T = T.reshape(sh[:npre] + (2**n, 2**n) + sh[npre + 2 * n:])
            if n == 1:
                new.append((key + [(l, 0.5)], T))
                continue
            for j, Js in intertwiners(n).items():
                acc = None
                for J in Js:
                    X = np.tensordot(T, J, axes=([npre], [0]))          # a-group -> alpha (moved to end)
                    X = np.tensordot(X, J, axes=([npre], [0]))          # b-group -> beta  (moved to end)
                    X = np.moveaxis(X, [-2, -1], [npre, npre + 1])
                    acc = X if acc is None else acc + X
                if np.abs(acc).max() > 1e-13:
                    new.append((key + [(l, j)], acc))
        parts = new
    res = {}
    for key, T in parts:
        nl = len(key)
        # axes: alpha_1, beta_1, alpha_2, beta_2, ... -> matrix (alphas) x (betas)
        T = np.transpose(T, [2 * i for i in range(nl)] + [2 * i + 1 for i in range(nl)])
        da = int(np.prod(T.shape[:nl])); M = T.reshape(da, -1)
        res[tuple(key)] = M
    return res
def tnorm(M): return float(np.linalg.svd(M, compute_uv=False).sum())
def casimir(key): return sum(j * (j + 1) for (_, j) in key)

# ---------------- lattice symmetries (12 point maps) ----------------
def e(i): return tuple(1 if k == i else 0 for k in range(3))
def perm_vertex(pi, n): out = [0, 0, 0]; [out.__setitem__(pi[k], n[k]) for k in range(3)]; return tuple(out)
def g_link(g, l):
    pi, inv = g; (n, i) = l
    n2 = perm_vertex(pi, n); i2 = pi[i]
    if inv:
        n2 = tuple(-x - y for x, y in zip(n2, e(i2)))
    return (n2, i2)
def g_plaq(g, p):
    ls = links_of(p); im = [g_link(g, l) for l in ls]
    dirs = sorted(set(l[1] for l in im)); i, j = dirs
    base = tuple(min(l[0][k] for l in im) for k in range(3))
    q = (base, i, j)
    assert sorted(links_of(q)) == sorted(im), (p, g)
    return q
G = [(pi, inv) for pi in itertools.permutations(range(3)) for inv in (False, True)]
def canon(L):
    best = None
    for g in G:
        im = [g_plaq(g, p) for p in L]
        t = tuple(min(q[0][k] for q in im) for k in range(3))
        im = tuple(sorted((tuple(x - y for x, y in zip(q[0], t)), q[1], q[2]) for q in im))
        if best is None or im < best[0]: best = (im, g, t)
    return best

# ---------------- v_2 data and v_3 cluster functions ----------------
@lru_cache(maxsize=None)
def X2(S):
    """v_2 cluster function for label S (sorted tuple of 2 plaquettes): list of (coefficient, casimir, projected function)"""
    p, q = S
    if p != q and not (set(links_of(p)) & set(links_of(q))): return []
    f = product(W(p), W(q)); mult = 1 if p == q else 2
    out = []
    for key, _ in blocks_fast(f).items():
        cb = casimir(key)
        if cb == 0: continue
        g = f
        for (l, j) in key:
            if sum(1 for x in f[0] if x == l) > 1: g = project(g, l, j)
        out.append((mult / 9.0 * (6 - cb) / (2 * cb), cb, g))
    return out

def v3_cluster(L):
    """block matrices of the v_3 cluster function with label L (sorted tuple of 3 plaquettes)"""
    tot = {}
    seen = set()
    for idx in range(3):
        r = L[idx]; S = tuple(sorted(L[:idx] + L[idx + 1:]))
        if (r, S) in seen: continue
        seen.add((r, S))
        for (x, cb, g) in X2(S):
            prod = product(g, W(r))
            for key, M in blocks_fast(prod).items():
                cbp = casimir(key)
                if cbp == 0: continue
                coef = (2.0 / 3.0) * x * (3 + cb - cbp) / (2 * cbp)
                if abs(coef) < 1e-15: continue
                tot[key] = tot.get(key, 0) + coef * M
    return tot

if __name__ == "__main__":
    t0 = time.time()
    anchor = ((0, 0, 0), 0)
    R = 3
    P = [(n, i, j) for n in itertools.product(range(-R, R + 1), repeat=3) for i in range(3) for j in range(i + 1, 3)]
    Ls = {p: set(links_of(p)) for p in P}
    adj = {p: [q for q in P if q != p and Ls[p] & Ls[q]] for p in P if abs(p[0][0]) <= 2 and abs(p[0][1]) <= 2 and abs(p[0][2]) <= 2}
    A0 = [p for p in P if anchor in Ls[p]]
    # order-2 sanity: 46 labels, m(v2) = 134.067...
    labels2 = set()
    for a in A0:
        labels2.add((a, a))
        for q in adj[a]: labels2.add(tuple(sorted((a, q))))
    for a in A0:
        for q in adj[a]:
            pass
    # all order-2 labels containing the anchor: {p,q} adjacent with anchor in p or q
    labels2 = set([(a, a) for a in A0] + [tuple(sorted((a, q))) for a in A0 for q in adj[a]])
    m2 = t2 = l2 = 0.0
    for S in labels2:
        for (x, cb, g) in X2(S):
            for key, M in blocks_fast(g).items():
                if casimir(key) != cb: continue
                nr = tnorm(M); m2 += abs(x) * sum(j for _, j in key) * nr; t2 += abs(x) * dict(key).get(anchor, 0) * nr; l2 += abs(x) * cb * nr
    print(f"order 2 (sanity): labels {len(labels2)}, m = {m2:.10f}, t = {t2:.10f}, loc = {l2:.10f}", flush=True)
    # order-3 labels containing the anchor
    labels3 = set()
    for a in A0:
        Y = [a] + adj[a]
        for y in Y:
            Z = set([a, y] + adj[a] + adj.get(y, []))
            for z in Z:
                labels3.add(tuple(sorted((a, y, z))))
    # keep connected multisets
    def connected(L):
        U = list(L); comp = {0}; changed = True
        while changed:
            changed = False
            for i in range(3):
                if i in comp: continue
                if any(U[i] == U[k] or (Ls[U[i]] & Ls[U[k]]) for k in comp): comp.add(i); changed = True
        return len(comp) == 3
    labels3 = [L for L in labels3 if connected(L)]
    print("order-3 anchored labels:", len(labels3), flush=True)
    classes = {}
    for L in labels3:
        c, g, t = canon(L)
        classes.setdefault(c, []).append(L)
    print("symmetry classes:", len(classes), flush=True)
    only = sys.argv[1] if len(sys.argv) > 1 else None
    results = {}
    for ci, (c, members) in enumerate(sorted(classes.items())):
        rep = members[0]
        t1 = time.time()
        bl = v3_cluster(rep)
        data = []
        for key, M in bl.items():
            nr = tnorm(M)
            if nr < 1e-12: continue
            data.append((key, nr))
        results[c] = (rep, data)
        kinds = "".join(sorted("s" if rep.count(p) == 3 else ("r" if rep.count(p) == 2 else "d") for p in set(rep)))
        print(f"class {ci+1}/{len(classes)} ({kinds}, {len(members)} anchored members, {len(data)} blocks): {time.time()-t1:.1f}s", flush=True)
    # anchored sums: for member L = h(rep) we need the block data transported; use norms keyed by link of L
    m3 = t3 = l3 = 0.0
    per_type = {}
    for c, members in classes.items():
        rep, data = results[c]
        Mv = sum(sum(j for _, j in key) * nr for key, nr in data)
        Lv = sum(casimir(key) * nr for key, nr in data)
        for L in members:
            # find a symmetry h mapping rep -> L (as multisets), then anchor's preimage link
            found = None
            for g in G:
                im = [g_plaq(g, p) for p in rep]
                for p0 in [L[0]]:
                    # translation: match sorted lists
                    ims = sorted(im)
                    Ls_ = sorted(L)
                    tvec = tuple(Ls_[0][0][k] - ims[0][0][k] for k in range(3))
                    im2 = sorted((tuple(x + y for x, y in zip(q[0], tvec)), q[1], q[2]) for q in im)
                    if im2 == Ls_:
                        found = (g, tvec); break
                if found: break
            if not found:
                # try all translations aligning any image plaquette with L[0]
                for g in G:
                    im = [g_plaq(g, p) for p in rep]
                    for q0 in im:
                        tvec = tuple(L[0][0][k] - q0[0][k] for k in range(3))
                        im2 = sorted((tuple(x + y for x, y in zip(q[0], tvec)), q[1], q[2]) for q in im)
                        if im2 == sorted(L): found = (g, tvec); break
                    if found: break
            assert found, L
            g, tvec = found
            def mapl(l):
                n2, i2 = g_link(g, l); return (tuple(x + y for x, y in zip(n2, tvec)), i2)
            Tv = sum(dict((mapl(l), j) for (l, j) in key).get(anchor, 0) * nr for key, nr in data)
            m3 += Mv; t3 += Tv; l3 += Lv
            kinds = "".join(sorted("s" if rep.count(p) == 3 else ("r" if rep.count(p) == 2 else "d") for p in set(rep)))
            pt = per_type.setdefault(kinds, [0, 0.0, 0.0]); pt[0] += 1; pt[1] += Lv
    print(f"\norder 3 at the anchor: m(v3) = {m3:.10f}, t(v3) = {t3:.10f}, ||v3||_loc = {l3:.10f}")
    print("F26 bounds: m3 = 336572872/208845 =", 336572872 / 208845, " t3 = 225985217/1253070 =", 225985217 / 1253070, "  C23: 944984/351 =", 944984 / 351)
    print("per label type (count, loc sum):", per_type)
    print(f"total time {time.time()-t0:.1f}s")
