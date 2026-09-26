# Lemma: for any 4-admissible B, q>=0 and lower digit sets W_j in {{1,7,8},{2,3,5}}, {19^j w: w in W_j, j<q} U 19^q B is 4-admissible.
import random, numpy as np
random.seed(20260926)
def Hmask(A):
    S=sum(A); h=np.zeros(S+1,dtype=bool); h[0]=True
    for a in A: h[a:]=h[a:]|h[:S+1-a].copy()
    return h
def has4(h):
    S=len(h)-1
    for d in range(1,S//3+1):
        if np.any(h[:S+1-3*d] & h[d:S+1-2*d] & h[2*d:S+1-d] & h[3*d:]): return True
    return False
def rand_adm(size,maxel):
    for _ in range(100000):
        B=sorted(random.sample(range(1,maxel+1),size))
        if not has4(Hmask(B)): return B
W=[(1,7,8),(2,3,5)]
bad=0; n=0
for trial in range(140):
    if trial<100: q=1; size=random.choice([2,3,4,5]); B=rand_adm(size,random.choice([45,60]))
    else: q=2; size=random.choice([2,3,4]); B=rand_adm(size,20)
    lower=[19**j*w for j in range(q) for w in random.choice(W)]
    C=lower+[19**q*b for b in B]
    if len(set(C))!=len(C): continue
    n+=1
    if has4(Hmask(C)): bad+=1
print(f"random 4-admissible top blocks B, q in {{1,2}}, mixed lower digit sets: {n} unions tested, non-admissible: {bad}")
C=[1,7,8]+[19*b for b in [1,2,3]]; print("negative control: top block {1,2,3} (not 4-admissible) -> union has a 4-AP:", has4(Hmask(C)))
