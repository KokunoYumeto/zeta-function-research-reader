# Validation of ym_fast.py against direct evaluation and finite-difference Gamma.
import numpy as np, itertools, time
from fractions import Fraction as Fr
from scipy.linalg import expm
from ym_blocks import plaquette, links_of, su2, eval_word, trace_norm, HALF
from ym_fast import *
rng = np.random.default_rng(11)
ok = True
def check(name, cond, extra=''):
    global ok; ok &= bool(cond); print(('PASS ' if cond else 'FAIL ') + name + ('  ' + str(extra) if extra else ''), flush=True)
conf = {}
for n in itertools.product(range(-3, 4), repeat=3):
    for i in range(3): conf[(n, i)] = su2(rng.normal(size=4))
p = plaquette((0, 0, 0), 0, 1)
Wp = plaquette_block(p)
check("W_p block: norm 8 and value tr(word)", abs(trace_norm(Wp.matrix()) - 8) < 1e-12 and abs(Wp.evaluate(conf) - eval_word(p, conf)) < 1e-12)
bl = list(product_blocks(Wp, Wp))
nz = [(b.key(), trace_norm(b.matrix())) for b, sh in bl if trace_norm(b.matrix()) > 1e-9]
check("W_p^2: nonzero blocks are the constant (norm 1) and chi_1 (norm 27)", sorted(round(x[1], 9) for x in nz) == [1.0, 27.0], [round(x[1], 9) for x in nz])
check("W_p^2 blocks sum to W_p^2", abs(sum(b.evaluate(conf) for b, sh in bl) - eval_word(p, conf)**2) < 1e-10)
for q in (plaquette((1, 0, 0), 0, 1), plaquette((0, 0, 0), 0, 2), plaquette((0, 0, -1), 0, 2), plaquette((0, 0, 0), 1, 2)):
    bl = list(product_blocks(Wp, plaquette_block(q)))
    val = sum(b.evaluate(conf) for b, sh in bl)
    nr = {tuple(sh.values())[0][2]: round(trace_norm(b.matrix()), 6) for b, sh in bl}
    check(f"pair {q[0]}: blocks sum to W_p W_q; norms by shared spin {nr}", abs(val - eval_word(p, conf) * eval_word(q, conf)) < 1e-10)
# Gamma identity with finite differences
Ta = [-0.5j * np.array([[0, 1], [1, 0]]), -0.5j * np.array([[0, -1j], [1j, 0]]), -0.5j * np.array([[1, 0], [0, -1]])]
H = 1e-5; EXP = [(expm(H * T), expm(-H * T)) for T in Ta]
def Xd(func, e, a):
    c1 = dict(conf); c2 = dict(conf); c1[e] = EXP[a][0] @ conf[e]; c2[e] = EXP[a][1] @ conf[e]
    return (func(c1) - func(c2)) / (2 * H)
def Gamma(f, g, links): return sum(Xd(f, e, a) * Xd(g, e, a) for e in links for a in range(3))
def chi1(pp):
    for b, sh in product_blocks(plaquette_block(pp), plaquette_block(pp)):
        if all(v[2] == 1 for v in sh.values()): return b
def pairP(pp, qq, s):
    for b, sh in product_blocks(plaquette_block(pp), plaquette_block(qq)):
        if list(sh.values())[0][2] == s: return b
Xs = [('chi1', chi1(p))] + [(f'P{s}', pairP(p, q, Fr(s))) for q in (plaquette((1, 0, 0), 0, 1), plaquette((0, 0, 0), 0, 2)) for s in (0, 1)]
check("chi_1(V_p) = W_p^2 - 1", abs(Xs[0][1].evaluate(conf) - (eval_word(p, conf)**2 - 1)) < 1e-10)
t0 = time.time()
for name, X in Xs:
    for r in (p, plaquette((1, 0, 0), 0, 1), plaquette((0, 0, 0), 0, 2), plaquette((0, 0, 0), 1, 2), plaquette((1, 0, 0), 1, 2), plaquette((0, 1, 0), 0, 2), plaquette((0, 0, -1), 0, 2), plaquette((0, -1, 0), 0, 1)):
        shared = links_of(r) & set(X.links)
        if not shared: continue
        lhs = Gamma(lambda c: eval_word(r, c), X.evaluate, shared)
        res = B_of(plaquette_block(r), X)
        rhs = sum(float(g) * b.evaluate(conf) for b, g, c in res)
        tot = sum(b.evaluate(conf) for b, g, c in res)
        check(f"Gamma(W_r, {name}) r={r[0]}: finite difference = block formula; blocks sum to W_r X",
              abs(lhs - rhs) < 1e-6 and abs(tot - eval_word(r, conf) * X.evaluate(conf)) < 1e-10, (round(lhs.real, 7), round(rhs.real, 7)))
print(f"{time.time() - t0:.1f}s", "ALL PASS" if ok else "SOME FAILED")
