# Referee library (written independently of the reader's and the previous referee's code):
# Fourier-block decomposition of products of SU(2) plaquette traces on the cubic lattice,
# with exact link orientations, and trace norms of the block coefficient matrices.
#
# A function f(U) = sum_{a,b} F[a_1..a_K, b_1..b_K] prod_k U_{l_k}[a_k, b_k] over K "occurrences" (links l_k,
# possibly repeated) is stored as (links, F).  Writing f = Tr(A X) with X = (x)_k U_{l_k}, A[(b),(a)] = F[a,b].
# For a link with n occurrences, U^{(x)n} = sum_{j,c} J_{jc} D^j(U) J_{jc}^+ with isometric intertwiners J_{jc}
# sharing the same D^j across the multiplicity copies c; the Fourier coefficient of spin tuple (j_l) is
# A_(j) = sum_c (x_l J)^+ A (x_l J), and its trace norm is the SVD sum.
import numpy as np, itertools
from functools import lru_cache

C2 = np.array([[0., 1.], [-1., 0.]])          # U^{-1} = C U^T C^{-1} on SU(2)
C2inv = np.linalg.inv(C2)

def plaquette(n, i, j):
    """links (as (vertex tuple, direction)) and orientation signs of W_p = tr(U_i(n) U_j(n+e_i) U_i(n+e_j)^-1 U_j(n)^-1), i<j"""
    ei = tuple(1 if k == i else 0 for k in range(3)); ej = tuple(1 if k == j else 0 for k in range(3))
    add = lambda a, b: tuple(x + y for x, y in zip(a, b))
    return [((tuple(n), i), +1), ((add(n, ei), j), +1), ((add(n, ej), i), -1), ((tuple(n), j), -1)]

def trace_word_tensor(word):
    """word: list of (link, sign). Returns (links, F) with F of shape (2,)*(2K): axes a_1..a_K, b_1..b_K."""
    K = len(word)
    # factor k: U^s[r_k, r_{k+1}] = sum_{a,b} T_s[r_k, r_{k+1}, a, b] U[a,b]
    Tp = np.zeros((2, 2, 2, 2)); Tm = np.zeros((2, 2, 2, 2))
    for r in range(2):
        for c in range(2):
            Tp[r, c, r, c] = 1.0
            for a in range(2):
                for b in range(2):
                    Tm[r, c, a, b] = C2[r, b] * C2inv[a, c]
    # contract the cyclic r indices
    F = None
    for k, (link, s) in enumerate(word):
        T = Tp if s > 0 else Tm
        if F is None:
            F = T  # r1, r2, a1, b1
        else:
            # F: r1, r_k, (a,b)...;  T: r_k, r_{k+1}, a_k, b_k
            F = np.tensordot(F, T, axes=([1], [0]))       # r1, (ab)..., r_{k+1}, a_k, b_k
            F = np.moveaxis(F, -3, 1)                      # r1, r_{k+1}, (ab)..., a_k, b_k
    F = np.trace(F, axis1=0, axis2=1)                      # (a1 b1 a2 b2 ...)
    # reorder to a_1..a_K, b_1..b_K
    perm = [2 * k for k in range(K)] + [2 * k + 1 for k in range(K)]
    F = np.transpose(F, perm)
    return [w[0] for w in word], F

def product(f, g):
    (lf, Ff), (lg, Fg) = f, g
    Kf, Kg = len(lf), len(lg)
    P = np.multiply.outer(Ff, Fg)          # a^f b^f a^g b^g
    perm = list(range(Kf)) + list(range(2 * Kf, 2 * Kf + Kg)) + list(range(Kf, 2 * Kf)) + list(range(2 * Kf + Kg, 2 * Kf + 2 * Kg))
    return lf + lg, np.transpose(P, perm)

# ---- intertwiners for U^{(x)n}, n = 1, 2, 3 ----
def _spin_ops(n):
    sx = np.array([[0, 1], [1, 0]]) / 2; sy = np.array([[0, -1j], [1j, 0]]) / 2; sz = np.array([[1, 0], [0, -1]]) / 2
    ops = []
    for s in (sx, sy, sz):
        tot = np.zeros((2**n, 2**n), dtype=complex)
        for k in range(n):
            mats = [np.eye(2)] * n; mats = list(mats); mats[k] = s
            M = mats[0]
            for mm in mats[1:]: M = np.kron(M, mm)
            tot += M
        ops.append(tot)
    return ops

@lru_cache(maxsize=None)
def intertwiners(n):
    """dict spin (float) -> list of isometries J_c (2^n x (2j+1)) intertwining U^{(x)n} J_c = J_c D^j(U) with a common D^j."""
    if n == 1:
        return {0.5: [np.eye(2, dtype=complex)]}
    Sx, Sy, Sz = _spin_ops(n)
    Splus = Sx + 1j * Sy; Sminus = Sx - 1j * Sy
    Csq = Sx @ Sx + Sy @ Sy + Sz @ Sz
    out = {}
    w, V = np.linalg.eigh(Csq)
    spins = sorted(set(np.round((-1 + np.sqrt(1 + 4 * w)) / 2 * 2) / 2))
    for j in spins:
        cols = V[:, np.abs((-1 + np.sqrt(1 + 4 * w)) / 2 - j) < 1e-6]
        # highest-weight vectors: Sz = j within this isotypic space
        Pz = cols.conj().T @ Sz @ cols
        wz, Vz = np.linalg.eigh(Pz)
        hw = cols @ Vz[:, np.abs(wz - j) < 1e-6]            # orthonormal basis of the highest-weight space (mult)
        Js = []
        for c in range(hw.shape[1]):
            vecs = [hw[:, c]]
            m = j
            while m > -j + 1e-9:
                v = Sminus @ vecs[-1]
                v = v / np.sqrt(j * (j + 1) - m * (m - 1))   # standard lowering normalisation
                vecs.append(v); m -= 1
            Js.append(np.array(vecs).T)                        # columns |j, j>, |j, j-1>, ...
        out[float(j)] = Js
    return out

def blocks(f):
    """Fourier blocks of f = (links, F).  Returns dict: tuple of (link, spin) sorted by link -> coefficient matrix A_(j)."""
    links, F = f
    K = len(links)
    uniq = sorted(set(links))
    occ = {l: [k for k in range(K) if links[k] == l] for l in uniq}
    order = [k for l in uniq for k in occ[l]]
    perm = order + [K + k for k in order]
    Fp = np.transpose(F, perm)
    dim = 2**K
    A = Fp.reshape(dim, dim).T      # A[(b),(a)] = F[a,b]  (rows b, cols a)
    per_link = [intertwiners(len(occ[l])) for l in uniq]
    res = {}
    for choice in itertools.product(*[sorted(pl.keys()) for pl in per_link]):
        Ablk = None
        for cs in itertools.product(*[range(len(per_link[t][choice[t]])) for t in range(len(uniq))]):
            J = np.array([[1.0 + 0j]])
            for t in range(len(uniq)):
                J = np.kron(J, per_link[t][choice[t]][cs[t]])
            term = J.conj().T @ A @ J
            Ablk = term if Ablk is None else Ablk + term
        if np.abs(Ablk).max() > 1e-12:
            res[tuple(zip(uniq, choice))] = Ablk
    return res

def tnorm(M):
    return float(np.linalg.svd(M, compute_uv=False).sum())

def casimir(key):
    return sum(j * (j + 1) for (_, j) in key)

def evaluate(f, U):
    links, F = f
    val = F
    K = len(links)
    # contract a_k, b_k with U_{l_k}[a_k, b_k]: after each contraction the next a/b axes shift
    for k in range(K):
        Uk = U[links[k]]
        # current axes: a_k..a_K, b_1'..: we contract a_k (axis 0) and b_k (axis K-k)
        val = np.tensordot(val, Uk, axes=([0, K - k], [0, 1]))
    return val

def evaluate_blocks(bl, U):
    tot = 0
    for key, A in bl.items():
        # Tr(A (x)_l D^{j_l}(U_l)) with D^j defined by the intertwiners J_{j,0}: D^j(U) = J^+ U^{(x)n} J
        D = np.array([[1.0 + 0j]])
        for (l, j) in key:
            # recover n = number of occurrences from A's size is ambiguous; D^j via n = 2j is enough (J_{j,0} of n=2j)
            n = int(round(2 * j))
            if n == 0:
                Dj = np.array([[1.0 + 0j]])
            else:
                Jj = intertwiners(n)[j][0] if n > 1 else np.eye(2, dtype=complex)
                Un = U[l]
                for _ in range(n - 1): Un = np.kron(Un, U[l])
                Dj = Jj.conj().T @ Un @ Jj
            D = np.kron(D, Dj)
        tot += np.trace(A @ D)
    return tot

def random_su2(rng):
    q = rng.normal(size=4); q /= np.linalg.norm(q)
    a, b = q[0] + 1j * q[1], q[2] + 1j * q[3]
    return np.array([[a, b], [-np.conj(b), np.conj(a)]])
