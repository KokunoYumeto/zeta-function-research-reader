# Referee check: independent recomputation of the order-2 inputs m(v2), t(v2), ||v2||_loc of the
# Yang-Mills workbench (F6 norms), from explicit SU(2) coefficient tensors.  No workbench code is used.
#   v1 = S/3,  v2 = B(v1,v1) = (1/9) sum_{p,q} B(W_p,W_q),
#   B(W_p,W_p) = -chi_1(V_p)/8,   B(W_p,W_q) = (1/6) P0(W_p W_q) - (1/26) P1(W_p W_q)  (p != q adjacent),
# (from 2 Gamma(f,h) = (Kf)h + f(Kh) - K(fh)), where P_s projects the shared link onto spin s.
# The Fourier-algebra norm of a block is the trace norm of its coefficient matrix A_j with f = Tr(A_j pi_j(U)).
import itertools, numpy as np
from fractions import Fraction as Fr

eps = np.array([[0., 1.], [-1., 0.]]); epsinv = np.linalg.inv(eps)

def plaquette_word(n, i, j):
    ei = tuple(1 if k == i else 0 for k in range(3)); ej = tuple(1 if k == j else 0 for k in range(3))
    add = lambda a, b: tuple(x + y for x, y in zip(a, b))
    return [((n, i), +1), ((add(n, ei), j), +1), ((add(n, ej), i), -1), ((n, j), -1)]

def word_tensor(word):
    """T[alpha_1..alpha_l, beta_1..beta_l] with tr(word) = sum T prod U_{e_i}[alpha_i, beta_i] (fundamental)."""
    l = len(word)
    T = np.zeros((2,) * (2 * l))
    for r in itertools.product(range(2), repeat=l):
        # each letter: s=+1 -> delta(alpha, r_i) delta(beta, r_{i+1});
        #              s=-1 -> (U^{-1})[r_i, r_{i+1}] = sum eps[r_i, beta] U[alpha, beta] epsinv[alpha, r_{i+1}]
        facs = []
        for k, (_, s) in enumerate(word):
            ri, rn = r[k], r[(k + 1) % l]
            if s == +1:
                facs.append([((ri, rn), 1.0)])
            else:
                facs.append([((al, be), eps[ri, be] * epsinv[al, rn]) for al in range(2) for be in range(2)
                             if eps[ri, be] * epsinv[al, rn] != 0])
        for combo in itertools.product(*facs):
            c = 1.0; idx_a = []; idx_b = []
            for (al, be), w in combo:
                c *= w; idx_a.append(al); idx_b.append(be)
            T[tuple(idx_a) + tuple(idx_b)] += c
    return T

def coeff_matrix(T, l):
    """A with f = Tr(A (x)U): A[beta, alpha] = T[alpha, beta]."""
    return T.reshape(2**l, 2**l).T

def trace_norm(A): return np.linalg.svd(A, compute_uv=False).sum()

# singlet/triplet change of basis on C^2 (x) C^2
V = np.zeros((4, 4))
s2 = 1 / np.sqrt(2)
V[0] = [0, s2, -s2, 0]          # singlet
V[1] = [1, 0, 0, 0]             # triplet m=+1
V[2] = [0, s2, s2, 0]           # triplet m=0
V[3] = [0, 0, 0, 1]             # triplet m=-1
assert np.allclose(V @ V.T, np.eye(4))
# sanity: V (U(x)U) V^T is block diagonal for a random SU(2) U
rng = np.random.default_rng(1)
def rand_su2():
    q = rng.normal(size=4); q /= np.linalg.norm(q)
    return np.array([[q[0] + 1j * q[3], q[2] + 1j * q[1]], [-q[2] + 1j * q[1], q[0] - 1j * q[3]]])
U = rand_su2(); B = V @ np.kron(U, U) @ V.T
assert abs(B[0, 0] - 1) < 1e-12 and np.allclose(B[0, 1:], 0) and np.allclose(B[1:, 0], 0)

def pair_norms(wp, wq):
    word = wp + wq
    l = len(word)
    shared = [k for k in range(l) if any(word[k][0] == word[m][0] for m in range(l) if m != k)]
    assert len(shared) == 2
    # tr(w_p) tr(w_q): tensor product of the two word tensors
    Tp = word_tensor(wp); Tq = word_tensor(wq)
    lp = len(wp)
    T = np.einsum(Tp, list(range(2 * lp)), Tq, list(range(2 * lp, 2 * l)), )
    # reorder axes to (alpha_1..alpha_l, beta_1..beta_l) of the concatenated word
    order = list(range(lp)) + list(range(2 * lp, 2 * lp + (l - lp))) + list(range(lp, 2 * lp)) + list(range(2 * lp + (l - lp), 2 * l))
    T = np.transpose(T, order)
    # move the two shared occurrences to the last two positions (for both alpha and beta)
    o1, o2 = shared
    rest = [k for k in range(l) if k not in shared]
    perm = rest + [o1, o2]
    T = np.transpose(T, perm + [l + k for k in perm])
    A = T.reshape(2**l, 2**l).T            # A[beta, alpha]
    Vbig = np.kron(np.eye(2**(l - 2)), V)
    Ap = Vbig @ A @ Vbig.T
    sing = [k for k in range(2**l) if k % 4 == 0]
    trip = [k for k in range(2**l) if k % 4 != 0]
    n0 = trace_norm(Ap[np.ix_(sing, sing)]); n1 = trace_norm(Ap[np.ix_(trip, trip)])
    # off-diagonal blocks must not contribute to the function; the diagonal blocks reconstruct it:
    return n0, n1, (o1, o2), word

# checks on single plaquettes
wp = plaquette_word((0, 0, 0), 0, 1)
A = coeff_matrix(word_tensor(wp), 4)
print("||W_p||_X =", round(trace_norm(A), 10), "(expected 8)")
# numerical identity check tr(word) == Tr(A (x)U)
Us = {}
def Ufor(e):
    if e not in Us: Us[e] = rand_su2()
    return Us[e]
def eval_word(word):
    M = np.eye(2, dtype=complex)
    for e, s in word: M = M @ (Ufor(e) if s == 1 else np.linalg.inv(Ufor(e)))
    return np.trace(M)
X = np.array([[1.0]])
for e, s in wp: X = np.kron(X, Ufor(e))
print("tr(word) == Tr(A (x)U):", np.allclose(eval_word(wp), np.trace(A @ X)))
# chi_1 of the plaquette holonomy: adjoint rep is real orthogonal, pi(U^-1) = pi(U)^T
l = 4; T3 = np.zeros((3,) * 8)
for r in itertools.product(range(3), repeat=4):
    ia, ib = [], []
    for k, (_, s) in enumerate(wp):
        ri, rn = r[k], r[(k + 1) % 4]
        if s == 1: ia.append(ri); ib.append(rn)
        else: ia.append(rn); ib.append(ri)
    T3[tuple(ia) + tuple(ib)] += 1
print("||chi_1(V_p)||_X =", round(trace_norm(T3.reshape(81, 81).T), 10), "(expected 27)")

# enumerate the anchored pairs around the anchor a = ((0,0,0), x)
a = ((0, 0, 0), 0)
def plaqs_near(R=2):
    out = []
    for n in itertools.product(range(-R, R + 1), repeat=3):
        for i in range(3):
            for j in range(i + 1, 3):
                out.append((n, i, j))
    return out
P = plaqs_near()
links = {p: set(e for e, _ in plaquette_word(*p)) for p in P}
containing = [p for p in P if a in links[p]]
assert len(containing) == 4
pairs = set()
for p in P:
    for q in P:
        if p < q and len(links[p] & links[q]) == 1 and (a in links[p] or a in links[q]):
            pairs.add((p, q))
print("anchored adjacent pairs:", len(pairs), "(expected 42)")

m = Fr(0); mfl = 6.0; tfl = 1.5; locfl = 12.0     # single-plaquette blocks: m 4*(3/2), t 4*(3/8), loc 4*3
hist = {}
for p, q in sorted(pairs):
    n0, n1, _, word = pair_norms(plaquette_word(*p), plaquette_word(*q))
    shared_link = (links[p] & links[q]).pop()
    key = (round(n0, 6), round(n1, 6)); hist[key] = hist.get(key, 0) + 1
    mfl += n0 / 9 + 4 * n1 / 117
    locfl += n0 / 6 + n1 / 18
    if a == shared_link:
        tfl += n1 / 117
    else:
        tfl += 0.5 * (n0 / 27 + n1 / 117)
print("norm pairs (||P0||, ||P1||) and counts:", hist, " 24*sqrt(3) =", 24 * np.sqrt(3))
print(f"m(v2) = {mfl:.10f}   (workbench bound 5834/39 = {5834/39:.10f})")
print(f"t(v2) = {tfl:.10f}   (workbench bound 137/6 = {137/6:.10f})")
print(f"||v2||_loc = {locfl:.10f}   (single-norm bound 236)")
