# Casimir lemma, girth form: on a simple graph of girth g, every block with a nonzero vertex-singlet has sum_f j_f >= g * j_e.
# SU(2) singlet condition at a vertex: sum of incident 2j even and max 2j <= sum of the others (polygon inequality).
# Exhaustive over spins 2j in {0..maxtwo} per edge, pruned edge-by-edge; min over nonzero assignments of sum_f j_f / j_e.
import itertools, networkx as nx
from fractions import Fraction as Fr
res=[]
def ok(n,c,i=""): res.append(c); print(("[PASS] " if c else "[FAIL] ")+n+(": "+str(i) if i!="" else ""))
def min_ratio(G, maxtwo):
    E=list(G.edges()); V=list(G.nodes()); idx={e:i for i,e in enumerate(E)}
    inc={v:[i for i,(a,b) in enumerate(E) if v in (a,b)] for v in V}
    # order vertices' completion: a vertex is checkable when all its incident edges are assigned
    last={}
    for v in V: last[v]=max(inc[v]) if inc[v] else -1
    checks_at={}
    for v in V: checks_at.setdefault(last[v],[]).append(v)
    best=[None]; count=[0]
    tw=[0]*len(E)
    def vertex_ok(v):
        s=[tw[i] for i in inc[v]]; t=sum(s)
        return t%2==0 and 2*max(s)<=t if s else True
    def rec(i):
        if i==len(E):
            if any(tw):
                count[0]+=1; T=sum(tw)
                r=min(Fr(T,x) for x in tw if x)
                if best[0] is None or r<best[0]: best[0]=r
            return
        for x in range(maxtwo+1):
            tw[i]=x
            if all(vertex_ok(v) for v in checks_at.get(i,[])): rec(i+1)
        tw[i]=0
    rec(0); return best[0], count[0]
graphs=[("triangle K3",nx.complete_graph(3),3),("K4",nx.complete_graph(4),3),("C4",nx.cycle_graph(4),2),
        ("cube Q3",nx.hypercube_graph(3),2),("C5",nx.cycle_graph(5),3),("Petersen",nx.petersen_graph(),1),
        ("C6",nx.cycle_graph(6),3),("Heawood (girth 6)",nx.heawood_graph(),1),("C7",nx.cycle_graph(7),2),
        ("K_{3,3} (girth 4)",nx.complete_bipartite_graph(3,3),2),("theta(2,3,3) paths (girth 5)",None,2),
        ("3x3 grid (girth 4)",nx.grid_2d_graph(3,3),2),("2x2x2 cubic box piece",nx.grid_graph(dim=[3,3,2]),1)]
# theta graph: two vertices joined by internally disjoint paths of lengths 2,3,3 -> girth 5
T=nx.Graph(); T.add_edges_from([(0,'a'),('a',1),(0,'b1'),('b1','b2'),('b2',1),(0,'c1'),('c1','c2'),('c2',1)])
graphs[10]=("theta(2,3,3) (girth 5)",T,3)
for name,G,mt in graphs:
    g=nx.girth(G)
    r,c=min_ratio(G,mt)
    ok(f"{name}: girth {g}, spins 2j<= {mt}: min sum_f j_f/j_e = {r} >= girth, attained", r==g, f"{c} singlet assignments")
print("ALL PASS" if all(res) else "FAILURES")
