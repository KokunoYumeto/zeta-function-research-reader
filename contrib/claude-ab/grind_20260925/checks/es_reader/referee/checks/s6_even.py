import numpy as np
from fractions import Fraction as F
A1 = np.array([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2 = np.array([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
Ai = np.array([[1,0,0,0],[0,1,0,0],[0,1,1,0],[-1,0,0,1]])
def perm(A, D):
    N = D**3; out = np.empty(N, dtype=np.int64)
    X = np.arange(N); x = X // (D*D); y = (X // D) % D; z = X % D
    v1 = (A[1,0] + A[1,1]*x + A[1,2]*y + A[1,3]*z) % D
    v2 = (A[2,0] + A[2,1]*x + A[2,2]*y + A[2,3]*z) % D
    v3 = (A[3,0] + A[3,1]*x + A[3,2]*y + A[3,3]*z) % D
    return (v1*D*D + v2*D + v3)
def cycles_on(pm, S):
    seen=set(); c=0
    for s in S:
        if s in seen: continue
        c+=1; t=s
        while t not in seen: seen.add(t); t=int(pm[t])
    return c
def analyse(D):
    P1, P2, Pi = perm(A1,D), perm(A2,D), perm(Ai,D)
    N = D**3; seen=np.zeros(N, bool); res=[]
    for s in range(N):
        if seen[s]: continue
        orb=[s]; seen[s]=True; k=0
        while k < len(orb):
            t=orb[k]; k+=1
            for P in (P1,P2):
                u=int(P[t])
                if not seen[u]: seen[u]=True; orb.append(u)
        n=len(orb); g = F(n - cycles_on(P1,orb) - cycles_on(P2,orb) - cycles_on(Pi,orb), 2) + 1
        res.append((n, str(g)))
    return sorted(res)
for D in (2, 4, 8, 16, 32, 12):
    print(D, analyse(D))
