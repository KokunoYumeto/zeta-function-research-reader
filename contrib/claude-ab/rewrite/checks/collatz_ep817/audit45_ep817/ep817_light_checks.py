#!/usr/bin/env python3
"""Light spot checks for EP-07 (cone dual C5) and EP-09 (recurrence R1/R2), written for this audit."""
def H(A):
    s={0}
    for a in A: s|={x+a for x in s}
    return s
def longest_ap(S):
    """length of the longest nonconstant AP in the finite set S (brute force)."""
    v=sorted(S); best=1 if S else 0
    for i in range(len(v)):
        for j in range(i+1,len(v)):
            d=v[j]-v[i]; L=2; x=v[j]+d
            while x in S: L+=1; x+=d
            best=max(best,L)
    return best
def mod_free(D,q,k):
    Dm={d%q for d in D}
    return not any(all((x+i*e)%q in Dm for i in range(k)) for x in Dm for e in range(1,q))
# EP-07 C5
A1,A2=[1,3,4,7],[1,2,4,8]
print("C5: ({1,3,4,7},31) modular-5-AP-free:",mod_free(H(A1),31,5),"| H({1,2,4,8}) =",sorted(H(A2))[:6],"... contains 0,1,2,3,4:",all(x in H(A2) for x in range(5)))
# EP-09 R1/R2: minimal gap sequences p_j^(r)
for r in (1,2,3):
    p=[]
    for j in range(10 if r>1 else 7):
        p.append(2**j if j<r else 2*p[j-1]+p[j-r])
    ok=True; rows=[]
    for n in range(1,len(p)+1):
        L=longest_ap(H(p[:n])); rows.append(L)
        ok&= (L==min(2**r,2**n))
    print(f"R1/R2 r={r}: p={p}; longest AP in H(prefix_n) for n=1..{len(p)}: {rows}; equals min(2^r,2^n): {ok}")
