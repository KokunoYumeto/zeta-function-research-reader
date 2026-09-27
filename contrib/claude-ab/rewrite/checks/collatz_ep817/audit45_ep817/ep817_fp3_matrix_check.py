#!/usr/bin/env python3
"""EP-08 FP3: build this audit's own 7-state carry automaton for the radix-ten dictionary
(A=(10,{1,3}), B=(10,{2,4}), arity 5), and test (i) rank of the letter-product matrices,
(ii) spectral radius of cyclic words A^a B^b against theta(a,b)=(8*10^(a+b)+4*10^b-3)/9,
(iii) count >= spectral radius.  Exact integer matrices; eigenvalues by numpy (float) only
for comparison with the exact integer formula."""
import itertools
from collections import Counter
import numpy as np
def Hq(A,q):
    s={0}
    for a in A: s={x+c*a for x in s for c in range(q)}
    return s
XA,XB=Hq([1,3],5),Hq([2,4],5)
states=[frozenset(s) for r in range(1,4) for s in itertools.combinations(range(3),r)]
idx={S:i for i,S in enumerate(states)}
def mat(X):
    M=np.zeros((7,7),dtype=object)
    for S in states:
        for o in range(10):
            S2=frozenset((x+c)//10 for c in S for x in X if (x+c)%10==o)
            if S2: M[idx[S2],idx[S]]+=1
    return M
MA,MB=mat(XA),mat(XB)
def rank(M): return np.linalg.matrix_rank(M.astype(float))
print("rank(M_A)=",rank(MA),"rank(M_B)=",rank(MB),"rank(M_B M_A)=",rank(MB.dot(MA)),"rank(M_A M_B)=",rank(MA.dot(MB)))
sizes=np.array([len(S) for S in states],dtype=object); e0=np.zeros(7,dtype=object); e0[idx[frozenset([0])]]=1
def count(word):  # word read from level 0 upward: apply letters in order
    v=e0.copy()
    for ch in word: v=(MA if ch=='A' else MB).dot(v)
    return int(sizes.dot(v))
ok=True
for a in range(1,5):
    for b in range(1,5):
        w='A'*a+'B'*b
        P=np.identity(7,dtype=object)
        for ch in w: P=(MA if ch=='A' else MB).dot(P)
        rho=max(abs(np.linalg.eigvals(P.astype(float))))
        th=(8*10**(a+b)+4*10**b-3)//9
        th2=(8*10**(a+b)+4*10**a-3)//9
        good = abs(rho-th)/th<1e-9 or abs(rho-th2)/th2<1e-9
        ok&=good and count(w)>=rho-1e-6
        if a+b<=4: print(f"cyclic word A^{a}B^{b}: spectral radius {rho:.3f}; theta(a,b)={th}, theta(b,a)={th2}; count={count(w)}")
print("spectral radius of every cyclic A^a B^b (a,b<=4) equals a theta value and is <= the count:",ok)
