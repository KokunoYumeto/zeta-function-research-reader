# Validation of ym_blocks.py: representation properties, known norms (8, 27, 16/48, 8/24 sqrt 3),
# completeness of the block decomposition, and the Gamma identity for B(W_r, X) by finite differences.
import numpy as np, itertools
from fractions import Fraction as Fr
from ym_blocks import *

rng = np.random.default_rng(7)
def rU(): return su2(rng.normal(size=4))
ok = True
def check(name, cond, extra=''):
    global ok; ok &= bool(cond); print(('PASS ' if cond else 'FAIL ') + name + ('  ' + str(extra) if extra else ''))

# (a) D^s is a unitary representation, for s = 1/2, 1, 3/2, 2
for s in (HALF, Fr(1), Fr(3, 2), Fr(2)):
    U1, U2 = rU(), rU()
    check(f"D^{s} homomorphism and unitary", np.allclose(D(s, U1 @ U2), D(s, U1) @ D(s, U2)) and np.allclose(D(s, U1) @ D(s, U1).conj().T, np.eye(dim(s))))
# (b) intertwiners for several coupling paths
for path in ([HALF, Fr(0)], [HALF, Fr(1)], [HALF, Fr(1), HALF], [HALF, Fr(0), HALF], [HALF, Fr(1), Fr(3, 2)], [HALF, Fr(1), Fr(3, 2), Fr(1)], [HALF, Fr(1), HALF, Fr(1)]):
    J = intertwiner(path); k = J.ndim - 1; s = path[-1]
    Jm = J.reshape(2**k, dim(s)); U = rU()
    Uk = functools.reduce(np.kron, [U] * k)
    check(f"intertwiner {[str(x) for x in path]}: isometry and U^k J = J D^s(U)",
          np.allclose(Jm.T @ Jm, np.eye(dim(s))) and np.allclose(Uk @ Jm, Jm @ D(s, U)))

# random configuration on a window
def rand_conf(R=3):
    conf = {}
    for n in itertools.product(range(-R, R + 1), repeat=3):
        for i in range(3): conf[(n, i)] = rU()
    return conf
conf = rand_conf()
p = plaquette((0, 0, 0), 0, 1)
# (c) single plaquette
sp, A = block_coefficient([p], {e: ([(0, pos)], [HALF]) for pos, (e, s) in enumerate(p[1])})
check("||W_p||_X = 8", abs(trace_norm(A) - 8) < 1e-10, trace_norm(A))
check("W_p block evaluates to tr(word)", abs(eval_block(sp, A, conf) - eval_word(p, conf)) < 1e-10)
# (d) W_p^2
tot = 0; norms = {}
for ss in itertools.product((Fr(0), Fr(1)), repeat=4):
    coup = {e: ([(0, pos), (1, pos)], [HALF, ss[pos]]) for pos, (e, s) in enumerate(p[1])}
    sp, A = block_coefficient([p, p], coup)
    tot += eval_block(sp, A, conf); norms[ss] = trace_norm(A)
nz = {k: v for k, v in norms.items() if v > 1e-9}
check("W_p^2 has only the blocks (0000) and (1111), norms 1 and 27", set(nz) == {(0, 0, 0, 0), (1, 1, 1, 1)} and abs(nz[(1, 1, 1, 1)] - 27) < 1e-9 and abs(nz[(0, 0, 0, 0)] - 1) < 1e-12, nz)
check("blocks of W_p^2 sum to W_p^2", abs(tot - eval_word(p, conf)**2) < 1e-9)
# (e) adjacent pairs: coplanar and bent, both orientations
def pair_blocks(p, q):
    lp, lq = links_of(p), links_of(q); e = next(iter(lp & lq))
    out = {}
    for s in (Fr(0), Fr(1)):
        coup = {}
        for pos, (f, _) in enumerate(p[1]):
            coup[f] = ([(0, pos)], [HALF])
        for pos, (f, _) in enumerate(q[1]):
            if f == e:
                posp = [k for k, (g, _) in enumerate(p[1]) if g == e][0]
                coup[f] = ([(0, posp), (1, pos)], [HALF, s])
            else:
                coup[f] = ([(1, pos)], [HALF])
        out[s] = block_coefficient([p, q], coup)
    return out
tests = [(plaquette((0, 0, 0), 0, 1), plaquette((1, 0, 0), 0, 1)),       # coplanar
         (plaquette((0, 0, 0), 0, 1), plaquette((0, 0, 0), 0, 2)),       # bent, both at n
         (plaquette((0, 0, 0), 0, 1), plaquette((0, 0, -1), 0, 2)),      # bent, other side
         (plaquette((0, 0, 0), 1, 2), plaquette((0, 0, 0), 0, 2))]
for p1, q1 in tests:
    bl = pair_blocks(p1, q1)
    n0, n1 = trace_norm(bl[Fr(0)][1]), trace_norm(bl[Fr(1)][1])
    f = sum(eval_block(*bl[s], conf) for s in bl)
    check(f"pair {p1[0]} {q1[0]}: blocks sum to W_p W_q; (||P0||,||P1||) = ({n0:.6f}, {n1:.6f})",
          abs(f - eval_word(p1, conf) * eval_word(q1, conf)) < 1e-9)

# (f) Gamma(W_r, X) = sum_j gamma_j (W_r X)_j, by finite differences, for X = chi_1(V_p) and X = P_s(W_p W_q)
Ta = [-0.5j * np.array([[0, 1], [1, 0]]), -0.5j * np.array([[0, -1j], [1j, 0]]), -0.5j * np.array([[1, 0], [0, -1]])]
from scipy.linalg import expm
H = 1e-5
EXP = [(expm(H * T), expm(-H * T)) for T in Ta]
def Xderiv(func, conf, e, a):
    c1 = dict(conf); c2 = dict(conf)
    c1[e] = EXP[a][0] @ conf[e]; c2[e] = EXP[a][1] @ conf[e]
    return (func(c1) - func(c2)) / (2 * H)
def Gamma(f, g, conf, links):
    return sum(Xderiv(f, conf, e, a) * Xderiv(g, conf, e, a) for e in links for a in range(3))
import ym_order3 as Y3
def term_fn(X):
    sp, A = block_coefficient(X['plaqs'], X['coup'])
    return lambda c: eval_block(sp, A, c)
chi1_p = term_fn(Y3.chi1_term(p))
check("chi_1(V_p) = W_p^2 - 1 pointwise", abs(chi1_p(conf) - (eval_word(p, conf)**2 - 1)) < 1e-9)
print("Gamma checks:")
for r in (plaquette((0, 0, 0), 0, 1), plaquette((0, 0, 0), 0, 2), plaquette((0, -1, 0), 0, 1)):
    X = Y3.chi1_term(p); fX = term_fn(X)
    shared = links_of(r) & Y3.active_links(X)
    lhs = Gamma(lambda c: eval_word(r, c), fX, conf, shared)
    blocks = Y3.B_blocks(r, X)
    rhs = sum(float(g) * eval_block(sp, A, conf) for (sp, A, g, cj) in blocks)
    full = sum(eval_block(sp, A, conf) for (sp, A, g, cj) in blocks)
    check(f"  Gamma(W_r, chi_1(V_p)) for r = {r[0]}; blocks sum to W_r X", abs(lhs - rhs) < 1e-6 and abs(full - eval_word(r, conf) * fX(conf)) < 1e-9, (round(lhs.real, 8), round(rhs.real, 8)))
q = plaquette((1, 0, 0), 0, 1)
qb = plaquette((0, 0, 0), 0, 2)
for (pp, qq) in ((p, q), (p, qb)):
    for s in (Fr(0), Fr(1)):
        X = Y3.pair_term(pp, qq, s); fX = term_fn(X)
        for r in (pp, qq, plaquette((0, 0, 0), 1, 2), plaquette((1, 0, 0), 1, 2), plaquette((0, 1, 0), 0, 2), plaquette((0, 0, -1), 0, 2)):
            shared = links_of(r) & Y3.active_links(X)
            if not shared: continue
            lhs = Gamma(lambda c: eval_word(r, c), fX, conf, shared)
            blocks = Y3.B_blocks(r, X)
            rhs = sum(float(g) * eval_block(sp, A, conf) for (sp, A, g, cj) in blocks)
            full = sum(eval_block(sp, A, conf) for (sp, A, g, cj) in blocks)
            check(f"  Gamma(W_r, P_{s}(W_p W_q)) p={pp[0]} q={qq[0]} r={r[0]}; blocks sum to W_r X",
                  abs(lhs - rhs) < 1e-6 and abs(full - eval_word(r, conf) * fX(conf)) < 1e-9, (round(lhs.real, 8), round(rhs.real, 8)))
print("ALL PASS" if ok else "SOME FAILED")
