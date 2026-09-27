# Referee check for Lemma 3.2 (the girth form of the gauge-invariance Casimir inequality).
# (1) the count of nonzero spin assignments with vertex singlets and all j_e <= 1 on the cube graph Q3;
# (2) the per-link optimum  opt_e = min Sum_f j_f / j_e  over real weights with the vertex inequalities,
#     compared with the formula  min( l_e , 1 + (c_u + c_w)/2 ),  where l_e is the shortest cycle through e
#     and c_x the shortest closed non-backtracking walk at x avoiding e (a 'lollipop': cycle + 2*stem).
import itertools, networkx as nx
from fractions import Fraction as Fr
from scipy.optimize import linprog
import numpy as np

def admissible(G, spins):
    for v in G.nodes:
        inc = [spins[e] for e in G.edges(v, keys=True)] if G.is_multigraph() else [spins[tuple(sorted(e))] for e in G.edges(v)]
        s = sum(inc)
        if s.denominator != 1: return False
        if any(2 * x > s for x in inc): return False
    return True

Q3 = nx.hypercube_graph(3)
Q3 = nx.convert_node_labels_to_integers(Q3)
edges = [tuple(sorted(e)) for e in Q3.edges]
vals = [Fr(0), Fr(1, 2), Fr(1)]
count = 0; minratio = None
for assign in itertools.product(vals, repeat=len(edges)):
    if not any(assign): continue
    spins = dict(zip(edges, assign))
    if admissible(Q3, spins):
        count += 1
        tot = sum(assign)
        r = min(tot / x for x in assign if x > 0)
        minratio = r if minratio is None else min(minratio, r)
print("Q3: nonzero admissible assignments with j_e in {0,1/2,1}:", count, " min Sum j / j_e over them:", minratio)

def lp_opt(G, e):
    """min Sum_f j_f subject to j_e = 1, j >= 0, vertex inequalities j_f <= Sum_{f' at v, f' != f} j_f'."""
    E = list(G.edges(keys=True)) if G.is_multigraph() else [tuple(sorted(x)) for x in G.edges]
    idx = {f: k for k, f in enumerate(E)}
    A_ub, b_ub = [], []
    for v in G.nodes:
        inc = [f for f in E if v in f[:2]]
        for f in inc:
            row = np.zeros(len(E))
            # a loop would count twice; there are none
            row[idx[f]] += 1
            for f2 in inc:
                if f2 != f: row[idx[f2]] -= 1
            A_ub.append(row); b_ub.append(0)
    A_eq = [np.eye(len(E))[idx[e]]]; b_eq = [1]
    res = linprog(np.ones(len(E)), A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=[(0, None)] * len(E), method='highs')
    return res.fun if res.status == 0 else float('inf')

def formula(G, e):
    u, w = e[0], e[1]
    H = G.copy(); H.remove_edge(*e)
    # shortest cycle through e: 1 + dist_{G-e}(u, w)
    try: le = 1 + nx.shortest_path_length(H, u, w)
    except nx.NetworkXNoPath: le = float('inf')
    # shortest closed non-backtracking walk at x avoiding e: min over cycles Z of G-e of |Z| + 2 dist(x, Z)
    cycles = [c for c in nx.simple_cycles(H.to_directed()) if len(c) >= 3]
    def cx(x):
        best = float('inf')
        for c in cycles:
            try: dist = min(nx.shortest_path_length(H, x, y) for y in c)
            except nx.NetworkXNoPath: continue
            best = min(best, len(c) + 2 * dist)
        return best
    return min(le, 1 + (cx(u) + cx(w)) / 2)

tests = {}
# bridge between two triangles
B = nx.Graph([(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 5), (5, 3)]); tests['two triangles + bridge'] = B
# lollipop: triangle with a path of length 2 to an edge, then another triangle
L2 = nx.Graph([(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 5), (5, 6), (6, 4)]); tests['triangles joined by a 2-path'] = L2
# a square with a pendant triangle sharing a vertex (girth 3; square edges have l_e = 4)
S = nx.Graph([(0, 1), (1, 2), (2, 3), (3, 0), (0, 4), (4, 5), (5, 0)]); tests['square + triangle at a vertex'] = S
# a hexagon with a chord making two squares... and a triangle far away
Hh = nx.Graph([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0), (0, 6), (6, 7), (7, 8), (8, 6)]); tests['hexagon + triangle on a stem'] = Hh
tests['Petersen'] = nx.petersen_graph()
tests['cube Q3'] = Q3
for name, G in tests.items():
    G = nx.Graph(G)
    worst = 0; rows = []
    for e in G.edges:
        e = tuple(sorted(e))
        o = lp_opt(nx.Graph(G), e); f = formula(G, e)
        worst = max(worst, abs(o - f) if f < float('inf') else (0 if o == float('inf') else 99))
        rows.append((e, round(o, 6), f))
    girth = min((len(c) for c in nx.cycle_basis(G)), default=None)
    print(f"{name}: girth {nx.girth(G)}, min_e opt_e = {min(r[1] for r in rows)}, max |LP - formula| = {worst}")
    if name in ('two triangles + bridge', 'triangles joined by a 2-path', 'square + triangle at a vertex', 'hexagon + triangle on a stem'):
        print("   per-link (edge, LP optimum, formula):", rows)
