#!/usr/bin/env python3
"""Confirm (independently of the C searches) the exact g_4(n) for n<=5 by exhaustive Python
enumeration of admissible sets, and confirm the n=7 witness set found by g4_upper7.c."""
import itertools
def H(A):
    s={0}
    for a in A: s|={x+a for x in s}
    return s
def free4(S):
    v=sorted(S)
    for i in range(len(v)):
        for j in range(i+1,len(v)):
            df=v[j]-v[i]
            if df%3==0 and v[i]+df//3 in S and v[i]+2*df//3 in S: return False
    return True
def admissible(n,Nmax):
    res=[]
    def rec(p,Hs,st):
        if len(p)==n: res.append(tuple(p)); return
        for a in range(st,Nmax+1):
            H2=Hs|{x+a for x in Hs}
            if free4(H2): rec(p+[a],H2,a+1)
    rec([],{0},1); return res
for n,Nmax in [(1,10),(2,10),(3,10),(4,20),(5,45)]:
    sets_=admissible(n,Nmax); mn=min(max(A) for A in sets_)
    opt=sorted(A for A in sets_ if max(A)==mn)
    print(f"n={n}: admissible n-subsets of [1,{Nmax}]: {len(sets_)}; least maximum = {mn}; optimal sets: {opt}")
for W in [(2,29,45,74,77,79),(1,3,39,180,219,243,246)]:
    print(f"set {W}: distinct={len(set(W))==len(W)}, |H|={len(H(W))}, H 4-AP-free={free4(H(W))}")
