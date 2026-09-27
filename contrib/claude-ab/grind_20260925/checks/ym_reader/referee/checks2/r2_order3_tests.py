# Tests for r2_order3.py: block reconstruction vs direct evaluation; symmetry invariance of block norms.
import numpy as np, sys, itertools, time
sys.path.insert(0, '.')
from r2_order3 import *
rng = np.random.default_rng(3)
def rsu2():
    q = rng.normal(size=4); q /= np.linalg.norm(q); a, b = q[0] + 1j * q[1], q[2] + 1j * q[3]
    return np.array([[a, b], [-np.conj(b), np.conj(a)]])
def evaluate(f, U):
    links, F = f; K = len(links); val = F.astype(complex)
    for k in range(K):
        val = np.tensordot(val, U[links[k]], axes=([0, K - k], [0, 1]))
    return val
def Dj(U, j):
    n = int(round(2 * j))
    if n == 0: return np.array([[1.0 + 0j]])
    J = intertwiners(n)[j][0]
    Un = U
    for _ in range(n - 1): Un = np.kron(Un, U)
    return J.T @ Un @ J
def eval_blocks(bl, U):
    tot = 0
    for key, M in bl.items():
        D = np.array([[1.0 + 0j]])
        for (l, j) in key: D = np.kron(D, Dj(U[l], j))
        # M is (alpha, beta) = A^T where f_block = Tr(A D) with A rows beta cols alpha -> Tr(M^T D)
        tot += np.trace(M.T @ D)
    return tot
p = ((0, 0, 0), 0, 1); q = ((0, 0, 0), 0, 2); r = ((0, 0, 0), 1, 2); s = ((0, -1, 0), 0, 1)
tests = {"path p,q,(1,0,0)x": [p, q, ((1, 0, 0), 1, 2)], "corner": [p, q, r], "common-edge": [p, q, s], "p,p,q": [p, p, q], "p,p,p": [p, p, p]}
for name, L in tests.items():
    t0 = time.time()
    f = W(L[0])
    for x in L[1:]: f = product(f, W(x))
    bl = blocks_fast(f)
    U = {l: rsu2() for l in set(f[0])}
    d = abs(evaluate(f, U) - eval_blocks(bl, U))
    print(f"{name}: {len(bl)} blocks, reconstruction error {d:.2e}, norms {sorted(round(tnorm(M), 6) for M in bl.values())}, {time.time()-t0:.1f}s", flush=True)
# symmetry invariance of block norms of W_p W_q W_r for a corner and a path
for L in ([p, q, r], [p, q, ((1, 0, 0), 1, 2)], [p, s, ((0, 0, 0), 0, 2)]):
    f = W(L[0])
    for x in L[1:]: f = product(f, W(x))
    base = sorted(round(tnorm(M), 8) for M in blocks_fast(f).values())
    ok = True
    for g in G:
        L2 = [g_plaq(g, x) for x in L]
        f2 = W(L2[0])
        for x in L2[1:]: f2 = product(f2, W(x))
        ok &= (sorted(round(tnorm(M), 8) for M in blocks_fast(f2).values()) == base)
    print("block norms invariant under the 12 point maps:", ok, base)
# a non-symmetry (single-axis reflection) changes norms, as expected (partial transposition)
L = [p, q, ((1, 0, 0), 1, 2)]
def refl_x_plaq(p_):
    ls = links_of(p_); im = []
    for (n, i) in ls:
        n2 = (-n[0], n[1], n[2])
        if i == 0: n2 = (n2[0] - 1, n2[1], n2[2])
        im.append((n2, i))
    dirs = sorted(set(l[1] for l in im)); base = tuple(min(l[0][k] for l in im) for k in range(3))
    return (base, dirs[0], dirs[1])
L2 = [refl_x_plaq(x) for x in L]
f = W(L[0]); f2 = W(L2[0])
for x in L[1:]: f = product(f, W(x))
for x in L2[1:]: f2 = product(f2, W(x))
print("x-reflection (not a norm symmetry):", sorted(round(tnorm(M), 6) for M in blocks_fast(f).values()), "->", sorted(round(tnorm(M), 6) for M in blocks_fast(f2).values()))
