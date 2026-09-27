# Lemma 3.2 checks: (i) Q3 count of nonzero half-integer assignments j_e in {0,1/2,1} with vertex singlets;
# (ii) LP optimum of sum_f j_f / j_e with vertex inequalities only, per link, vs girth and vs the exact per-link
#      constant gamma_e = min(g_e, 1 + (l_u + l_w)/2) (g_e: shortest cycle through e; l_x: shortest closed walk at x
#      in G - e with no immediate backtracking).
import itertools, networkx as nx, numpy as np
from fractions import Fraction as Fr
from scipy.optimize import linprog
Q3 = nx.hypercube_graph(3); E = list(Q3.edges())
def singlet(spins):
    s = sum(spins)
    return s.denominator == 1 and all(2 * x <= s for x in spins)
cnt = 0; best = None
vals = [Fr(0), Fr(1, 2), Fr(1)]
for js in itertools.product(vals, repeat=len(E)):
    if not any(js): continue
    j = dict(zip(E, js))
    ok = True
    for v in Q3.nodes():
        inc = [j[e] if e in j else j[(e[1], e[0])] for e in Q3.edges(v)]
        if not singlet(inc): ok = False; break
    if not ok: continue
    cnt += 1
    tot = sum(js)
    r = min(tot / x for x in js if x > 0)
    best = r if best is None else min(best, r)
print("Q3: nonzero admissible assignments with j_e <= 1:", cnt, " min sum_f j_f / j_e:", best)

def lp_opt(G, e):
    edges = list(G.edges(keys=True)) if G.is_multigraph() else list(G.edges())
    idx = {ed: k for k, ed in enumerate(edges)}
    A = []; b = []
    for v in G.nodes():
        inc = [ed for ed in edges if v in ed[:2]]
        for f in inc:
            row = np.zeros(len(edges)); row[idx[f]] = 1
            for f2 in inc:
                if f2 != f: row[idx[f2]] -= 1
            A.append(row); b.append(0)
    Aeq = np.zeros((1, len(edges))); Aeq[0, idx[e]] = 1
    res = linprog(np.ones(len(edges)), A_ub=np.array(A), b_ub=b, A_eq=Aeq, b_eq=[1], bounds=[(0, None)] * len(edges), method="highs")
    return res.fun
def gamma_formula(G, e):
    u, w = e[0], e[1]
    H = G.copy(); H.remove_edge(u, w)
    try: ge = nx.shortest_path_length(H, u, w) + 1
    except nx.NetworkXNoPath: ge = float('inf')
    def lclosed(x):
        # shortest closed walk at x in H with consecutive links different: BFS on (vertex, last edge)
        best = float('inf')
        from collections import deque
        start = [(x, None, 0)]
        dist = {}
        dq = deque()
        for y in H.neighbors(x):
            st = (y, frozenset((x, y))); dist[st] = 1; dq.append(st)
        while dq:
            y, last = dq.popleft(); d = dist[(y, last)]
            if y == x: best = min(best, d); continue
            for z in H.neighbors(y):
                le = frozenset((y, z))
                if le == last: continue
                st = (z, le)
                if st not in dist: dist[st] = d + 1; dq.append(st)
        return best
    return min(ge, 1 + (lclosed(u) + lclosed(w)) / 2)
graphs = {"Petersen": nx.petersen_graph(), "Heawood": nx.heawood_graph(), "McGee": nx.LCF_graph(24, [12, 7, -7], 8),
          "Tutte-Coxeter": nx.LCF_graph(30, [-13, -9, 7, -7, 9, 13], 5), "dodecahedron": nx.dodecahedral_graph(),
          "box {-1,0,1}^3": nx.grid_graph(dim=[3, 3, 3]), "K33": nx.complete_bipartite_graph(3, 3), "C5": nx.cycle_graph(5),
          "two triangles + bridge": nx.Graph([(0, 1), (1, 2), (0, 2), (2, 3), (3, 4), (4, 5), (3, 5)]),
          "triangles joined by 2-path": nx.Graph([(0, 1), (1, 2), (0, 2), (2, 6), (6, 3), (3, 4), (4, 5), (3, 5)])}
for name, G in graphs.items():
    g = nx.girth(G)
    opts = [lp_opt(G, e) for e in G.edges()]
    form = [gamma_formula(G, e) for e in G.edges()]
    print(f"{name}: girth {g}; LP optimum min {min(opts):.6f}, max {max(opts):.6f}; max |LP - gamma_e| = {max(abs(a - b) for a, b in zip(opts, form)):.2e}")
