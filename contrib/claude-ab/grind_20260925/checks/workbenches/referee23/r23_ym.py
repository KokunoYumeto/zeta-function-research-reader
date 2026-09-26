#!/usr/bin/env python3
"""Referee 23: independent checks of the Yang-Mills passages (Section 4).
F26 rationals transcribed from the source (CUMULATIVE_RESEARCH.md, F26 at fa79faf); everything else from the definitions."""
import sys, math, itertools, random, time
from fractions import Fraction as F
import sympy as sp
import mpmath as mp
mp.mp.dps = 50
t0 = time.time()
def say(tag, ok, msg=""):
    print(("[PASS] " if ok else "[FAIL] ") + tag + (": " + msg if msg else "")); sys.stdout.flush()

m = {1: F(64, 3), 2: F(5834, 39), 3: F(336572872, 208845), 4: F(17270702970768271, 341697152160), 5: F(1638684)}
t = {1: F(16, 3), 2: F(137, 6), 3: F(225985217, 1253070), 4: F(110695177857394584026401, 18025447358750832000), 5: F(190128)}
x = sp.symbols('x')
def polys(N, mm=m, tt=t):
    ell = sum(sp.Rational((mm[i] + 4 * tt[i]).numerator, (mm[i] + 4 * tt[i]).denominator) * x**i for i in range(1, N + 1))
    dl = sum(sp.Rational((3 * (mm[i] * tt[j] + mm[j] * tt[i])).numerator, (3 * (mm[i] * tt[j] + mm[j] * tt[i])).denominator) * x**(i + j)
             for i in range(1, N + 1) for j in range(1, N + 1) if i + j >= N + 1)
    D = sp.expand((1 - ell)**2 - sp.Rational(8, 3) * dl)
    lin = sum(sp.Rational((F(3, 2) * mm[i] - 6 * tt[i]).numerator, (F(3, 2) * mm[i] - 6 * tt[i]).denominator) * x**i for i in range(1, N + 1))
    return ell, dl, D, lin
def first_pos_root(D):
    P = sp.Poly(D, x)
    roots = [r for r in P.real_roots() if r > 0]
    r = min(roots, key=lambda r: sp.N(r, 60))
    return sp.N(r, 40)
res = {}
for N in range(1, 6):
    ell, dl, D, lin = polys(N)
    a = first_pos_root(D)
    dN = lambda xi, D=D, lin=lin: mp.mpf(1.5) * (1 + mp.sqrt(max(mp.mpf(0), mp.mpf(str(sp.N(D.subs(x, xi), 50)))))) + mp.mpf(str(sp.N(lin.subs(x, xi), 50)))
    thr = 1 / (2 * mp.sqrt(mp.mpf(str(a))))
    res[N] = (a, thr, dN)
    # ell < 1 on [0, alpha]
    ellmax = sp.N(ell.subs(x, a), 20)
    # monotonicity on a grid
    grid = [mp.mpf(str(a)) * k / 400 for k in range(401)]
    vals = [dN(sp.Rational(str(g)) if False else sp.nsimplify(str(g))) for g in grid[:0]]
    print(f"   N={N}: alpha_N = {mp.nstr(mp.mpf(str(a)), 18)}, threshold g^2 >= {mp.nstr(thr, 15)}, ell_N(alpha_N) = {ellmax}, d_N(alpha_N) = {mp.nstr(dN(a), 10)}")
# closed form N=1
ell1, dl1, D1, lin1 = polys(1)
say("Cor 4.5(a): D_1 = 1 - 256 xi/3 exactly, (3/2)m_1 - 6t_1 = 0, alpha_1 = 3/256, threshold 8/sqrt3", sp.simplify(D1 - (1 - sp.Rational(256, 3) * x)) == 0 and lin1 == 0
    and abs(res[1][0] - sp.Rational(3, 256)) < 1e-30 and abs(res[1][1] - 8 / mp.sqrt(3)) < mp.mpf(10)**-30, f"threshold {mp.nstr(res[1][1], 12)}")
def d_at_g2(N, g2):
    xi = sp.Rational(1, 4) / sp.nsimplify(g2)**2
    return res[N][2](xi)
v = {('1', 5): d_at_g2(1, 5), ('1', 10): d_at_g2(1, 10), ('2', 4.1): d_at_g2(2, sp.Rational(41, 10)), ('2', 5): d_at_g2(2, 5)}
say("Cor 4.5(a) values 2.0745 (g^2=5), 2.8304 (g^2=10)", mp.nstr(v[('1', 5)], 5) == '2.0745' and mp.nstr(v[('1', 10)], 5) == '2.8304', f"{mp.nstr(v[('1',5)],8)}, {mp.nstr(v[('1',10)],8)}")
say("Cor 4.5(b): alpha_2 = 0.0154800849822..., g^2 >= 4.0186791538833..., d_2(alpha_2) = 1.52094, 1.7665 (4.1), 2.3033 (5)",
    mp.nstr(mp.mpf(str(res[2][0])), 12) == '0.0154800849822' and mp.nstr(res[2][1], 14) == '4.0186791538833' and mp.nstr(res[2][2](res[2][0]), 6) == '1.52094'
    and mp.nstr(v[('2', 4.1)], 5) == '1.7665' and mp.nstr(v[('2', 5)], 5) == '2.3033',
    f"{mp.nstr(mp.mpf(str(res[2][0])),15)}, {mp.nstr(res[2][1],15)}, {mp.nstr(res[2][2](res[2][0]),8)}, {mp.nstr(v[('2',4.1)],8)}, {mp.nstr(v[('2',5)],8)}")
d4a = res[4][2](sp.Rational(1, 64)); d4b = res[4][2](sp.Rational(4, 225))
say("Cor 4.5(c): alpha_4 = 0.0181049722316..., g^2 >= 3.7159603625..., d_4(1/64) = 1.898118, d_4(4/225) = 1.658436",
    mp.nstr(mp.mpf(str(res[4][0])), 12) == '0.0181049722316' and mp.nstr(res[4][1], 11) == '3.7159603625' and mp.nstr(d4a, 7) == '1.898118' and mp.nstr(d4b, 7) == '1.658436',
    f"{mp.nstr(mp.mpf(str(res[4][0])),15)}, {mp.nstr(res[4][1],13)}, {mp.nstr(d4a,9)}, {mp.nstr(d4b,9)}")
d5a = res[5][2](sp.Rational(1, 64)); d5b = res[5][2](sp.Rational(4, 225)); d5e = res[5][2](res[5][0]); d50 = res[5][2](0)
say("Thm 4.1: alpha_5 = 0.0184249535761176166818..., threshold 3.6835519839857273..., d_5(1/64)=1.9068301567, d_5(alpha_5)=1.5453, d_5(0)=3; d_5(4/225) > 1.6993",
    mp.nstr(mp.mpf(str(res[5][0])), 25).startswith('0.0184249535761176166818') and mp.nstr(res[5][1], 17) == '3.6835519839857273' and mp.nstr(d5a, 11) == '1.9068301567'
    and mp.nstr(d5e, 5) == '1.5453' and d50 == 3 and d5b > mp.mpf('1.6993'),
    f"{mp.nstr(mp.mpf(str(res[5][0])),22)}, {mp.nstr(res[5][1],18)}, {mp.nstr(d5a,12)}, {mp.nstr(d5e,8)}, {mp.nstr(d5b,8)}")
say("4/225 <= alpha_4 (so YM-05 is inside Cor 4.5(c)'s range) and g^2 = 15/4 <-> xi = 4/225", F(4, 225) < F(str(sp.N(res[4][0], 30))) and F(1, 4) / (F(15, 4)**2) == F(4, 225))
# sign of every linear coefficient (3/2)m_i - 6t_i  -> d_N >= 3/2 for every N
coefs = {i: F(3, 2) * m[i] - 6 * t[i] for i in range(1, 6)}
say("(3/2)m_i - 6t_i >= 0 for every i <= 5, so d_N >= 3/2 on [0, alpha_N] for EVERY N", all(c >= 0 for c in coefs.values()), str({i: float(c) for i, c in coefs.items()}))
say("(3/2)m_2 - 6t_2 = 3408/39", coefs[2] == F(3408, 39))
# monotonicity of d_N: derivative identity w' sqrt(D) = delta' + ell' w  (symbolic) and grid check
ok = True
for N in range(1, 6):
    ell, dl, D, lin = polys(N)
    w = sp.Rational(3, 4) * (1 - ell - sp.sqrt(D))
    ident = sp.simplify(sp.diff(w, x) * sp.sqrt(D) - (sp.diff(dl, x) + sp.diff(ell, x) * w))
    if ident != 0: ok = False
    a = res[N][0]
    prev = None
    for k in range(0, 401):
        xi = sp.Rational(k, 400) * sp.nsimplify(str(sp.N(a, 40)))
        val = res[N][2](xi)
        if prev is not None and val > prev + mp.mpf(10)**-20: ok = False
        prev = val
say("d_N decreasing on [0, alpha_N]: identity w_*' sqrt(D) = delta' + ell' w_* (symbolic) and a 401-point grid, N = 1..5", ok)
# sensitivity claim: m5,t5 doubled
m2 = dict(m); t2 = dict(t); m2[5] *= 2; t2[5] *= 2
ell, dl, D, lin = polys(5, m2, t2)
a = first_pos_root(D)
thr = 1 / (2 * mp.sqrt(mp.mpf(str(a))))
dd = mp.mpf(1.5) * (1 + mp.sqrt(mp.mpf(str(sp.N(D.subs(x, sp.Rational(1, 64)), 50))))) + mp.mpf(str(sp.N(lin.subs(x, sp.Rational(1, 64)), 50)))
say("sensitivity: m5,t5 doubled -> threshold ~3.737, d_5(1/64) ~ 1.8946", mp.nstr(thr, 4) == '3.737' and mp.nstr(dd, 5) == '1.8946', f"{mp.nstr(thr,8)}, {mp.nstr(dd,8)}")
# ---------------------------------------------------------------- Neumann radii and M_L
def plaquettes(L):
    V = [(i, j, k) for i in range(-L, L + 1) for j in range(-L, L + 1) for k in range(-L, L + 1)]
    S = set(V); cnt = 0
    for v in V:
        for (a, b) in ((0, 1), (0, 2), (1, 2)):
            ea = [0, 0, 0]; ea[a] = 1; eb = [0, 0, 0]; eb[b] = 1
            w1 = tuple(v[c] + ea[c] for c in range(3)); w2 = tuple(v[c] + eb[c] for c in range(3)); w3 = tuple(v[c] + ea[c] + eb[c] for c in range(3))
            if w1 in S and w2 in S and w3 in S: cnt += 1
    return cnt
say("M_L = 12 L^2 (2L+1) for L = 2..5", all(plaquettes(L) == 12 * L * L * (2 * L + 1) for L in range(2, 6)))
M2 = 12 * 4 * 5
say("radii at L=2: 3/(16 M_2) = 1/1280, 3/(4 M_2) = 1/320; 1/alpha_5 = 54.27", F(3, 16 * M2) == F(1, 1280) and F(3, 4 * M2) == F(1, 320), f"1/alpha_5 = {mp.nstr(1/mp.mpf(str(res[5][0])), 6)}")
# optimality over contours: for x in (0,c), max(1/x, 1/(c-x)) >= 2/c
ok = all(max(1 / xx, 1 / (0.75 - xx)) >= 8 / 3 - 1e-12 for xx in [0.75 * k / 1000 for k in range(1, 1000)])
say("max(1/x, 1/(3/4-x)) >= 8/3 on (0,3/4)", ok)

# ---------------------------------------------------------------- girth lemma: LP over real weights with the vertex inequalities only
from scipy.optimize import linprog
import networkx as nx
def lp_constant(edges, n):
    """edges: list of (u,v) (parallel allowed, no loops). returns list of min sum_f j_f subject to j_e = 1 and vertex inequalities."""
    E = len(edges); inc = {v: [] for v in range(n)}
    for i, (u, v) in enumerate(edges): inc[u].append(i); inc[v].append(i)
    A_ub = []; b_ub = []
    for v in range(n):
        for f in inc[v]:
            row = [0.0] * E
            row[f] += 1.0
            for g in inc[v]:
                if g != f: row[g] -= 1.0
            A_ub.append(row); b_ub.append(0.0)
    out = []
    for e in range(E):
        A_eq = [[1.0 if i == e else 0.0 for i in range(E)]]
        r = linprog([1.0] * E, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=[1.0], bounds=[(0, None)] * E, method='highs')
        out.append(r.fun if r.status == 0 else math.inf)
    return out
def girth_multigraph(edges, n):
    # shortest cycle length, counting 2-cycles from parallel links
    from collections import Counter
    c = Counter(tuple(sorted(e)) for e in edges)
    if any(v >= 2 for v in c.values()): return 2
    G = nx.Graph(); G.add_nodes_from(range(n)); G.add_edges_from(edges)
    try:
        return nx.girth(G)
    except Exception:
        return math.inf
tests = []
G = nx.petersen_graph(); tests.append(("Petersen", list(G.edges()), G.number_of_nodes()))
G = nx.hypercube_graph(4); G = nx.convert_node_labels_to_integers(G); tests.append(("Q4", list(G.edges()), G.number_of_nodes()))
G = nx.grid_graph(dim=[3, 3, 3]); G = nx.convert_node_labels_to_integers(G); tests.append(("box {-1,0,1}^3", list(G.edges()), G.number_of_nodes()))
G = nx.heawood_graph(); tests.append(("Heawood", list(G.edges()), G.number_of_nodes()))
G = nx.circulant_graph(9, [1, 3]); tests.append(("circulant C9(1,3)", list(G.edges()), 9))
tests.append(("theta with parallel links", [(0, 1), (0, 1), (1, 2), (2, 0)], 3))
tests.append(("two triangles joined by a path of 2 links", [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 5), (5, 6), (6, 4)], 7))
tests.append(("5-cycle with a chord and a pendant path", [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (0, 2), (4, 5), (5, 6)], 7))
random.seed(7)
for r in range(6):
    G = nx.gnm_random_graph(10, 16, seed=r)
    tests.append((f"random G(10,16) #{r}", list(G.edges()), 10))
ok = True; lines = []
for name, edges, n in tests:
    g = girth_multigraph(edges, n)
    vals = lp_constant(edges, n)
    finite = [v for v in vals if v < math.inf]
    mn = min(vals)
    lines.append(f"{name}: girth {g}, min over links {mn:.4f}, max {max(finite) if finite else None}")
    if mn < g - 1e-7: ok = False
    # sharpness: min over links equals girth when the graph has a cycle
    if g < math.inf and abs(mn - g) > 1e-7: ok = False
say("girth lemma by LP (real weights, vertex inequalities only): min over links of sum_f j_f / j_e equals the girth", ok, "; ".join(lines))
print(f"elapsed {time.time()-t0:.1f}s")
