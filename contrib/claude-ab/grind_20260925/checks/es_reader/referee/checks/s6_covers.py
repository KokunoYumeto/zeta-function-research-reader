import numpy as np
from fractions import Fraction as F
A1 = np.array([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2 = np.array([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
Ai = np.array([[1,0,0,0],[0,1,0,0],[0,1,1,0],[-1,0,0,1]])
I = np.eye(4, dtype=int)
print("A1^3=I:", (np.linalg.matrix_power(A1,3)==I).all(), " A2^4=I:", (np.linalg.matrix_power(A2,4)==I).all(),
      " A1A2Ainf=I:", (A1@A2@Ai==I).all(), " A2^2 != I:", not (A2@A2==I).all())
def perm(A, D):
    pts = [(x,y,z) for x in range(D) for y in range(D) for z in range(D)]
    idx = {p:i for i,p in enumerate(pts)}
    out = []
    for (x,y,z) in pts:
        v = A @ np.array([1,x,y,z])
        out.append(idx[(int(v[1])%D, int(v[2])%D, int(v[3])%D)])
    return out
def cycles_on(pm, S):
    seen=set(); c=0
    for s in S:
        if s in seen: continue
        c+=1; t=s
        while t not in seen: seen.add(t); t=pm[t]
    return c
def analyse(D):
    P1, P2, Pi = perm(A1,D), perm(A2,D), perm(Ai,D)
    N = D**3; seen=[False]*N; comps=[]
    for s in range(N):
        if seen[s]: continue
        orb=[s]; seen[s]=True; k=0
        while k < len(orb):
            t=orb[k]; k+=1
            for P in (P1,P2):
                u=P[t]
                if not seen[u]: seen[u]=True; orb.append(u)
        comps.append(orb)
    res=[]
    for orb in comps:
        n=len(orb); c1=cycles_on(P1,orb); c2=cycles_on(P2,orb); ci=cycles_on(Pi,orb)
        g = F(n - c1 - c2 - ci, 2) + 1
        res.append((n, g))
    return sorted(res)
for D in list(range(1,16,2)) + [21,25,27,33,45] + [2,4,6,8]:
    r = analyse(D)
    if D % 2:
        if D % 3:
            pred = [(D**3, F(5*D**3-12*D**2-17*D+24, 24))]
        else:
            pred = sorted([(D**3//9, F(5*D**3-12*D**2-81*D+216, 216)), (8*D**3//9, F(5*D**3-12*D**2-9*D+27, 27))])
        print("D =", D, "orbits/genera:", [(n, str(g)) for n,g in r], " matches reader:", r == pred)
    else:
        print("D =", D, "(even) orbits/genera:", [(n, str(g)) for n,g in r])
