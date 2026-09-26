# LP: minimise sum_f j_f subject to j_e = 1, j >= 0 and the polygon inequalities j_f <= sum_{f' at v, f' != f} j_f' at every vertex.
# The girth form of Lemma 4.2 predicts the optimum is exactly girth(G) for every edge e (real weights, no integrality).
import networkx as nx, numpy as np
from scipy.optimize import linprog
res=[]
def ok(n,c,i=""): res.append(c); print(("[PASS] " if c else "[FAIL] ")+n+(": "+str(i) if i!="" else ""))
def lp_min(G):
    E=list(G.edges()); m=len(E); vals=[]
    rows=[]
    for v in G.nodes():
        inc=[i for i,(a,b) in enumerate(E) if v in (a,b)]
        for f in inc:
            row=np.zeros(m); row[f]=1
            for g in inc:
                if g!=f: row[g]-=1
            rows.append(row)
    Aub=np.array(rows); bub=np.zeros(len(rows))
    for e in range(m):
        Aeq=np.zeros((1,m)); Aeq[0,e]=1
        r=linprog(np.ones(m),A_ub=Aub,b_ub=bub,A_eq=Aeq,b_eq=[1],bounds=[(0,None)]*m,method='highs')
        vals.append(r.fun)
    return min(vals), max(vals)
tests=[("K3",nx.complete_graph(3)),("K4",nx.complete_graph(4)),("Q3 cube",nx.hypercube_graph(3)),("K33",nx.complete_bipartite_graph(3,3)),
       ("Petersen",nx.petersen_graph()),("Heawood",nx.heawood_graph()),("McGee (girth 7)",nx.LCF_graph(24,[12,7,-7],8)),
       ("Tutte-Coxeter (girth 8)",nx.LCF_graph(30,[-13,-9,7,-7,9,13],5)),("cubic box L=1 {-1,0,1}^3",nx.grid_graph(dim=[3,3,3])),
       ("dodecahedron (girth 5)",nx.dodecahedral_graph())]
for name,G in tests:
    g=nx.girth(G); lo,hi=lp_min(G)
    ok(f"{name}: girth {g}; LP min of sum_f j_f / j_e over edges e in [{lo:.6f}, {hi:.6f}]", abs(lo-g)<1e-7, "")
print("ALL PASS" if all(res) else "FAILURES")
