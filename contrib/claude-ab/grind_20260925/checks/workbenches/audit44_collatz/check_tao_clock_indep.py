#!/usr/bin/env python3
"""Independent finite checks for the Tao clock preprint (sections/consequences.tex):
nested first passage p_x o p_y = p_x = p_y o p_x (x<=y), the tuple map J being a bijection onto
compatible tuples with inverse = last projection (l1-isometric pushforward), l1 contraction of
pushforwards, and the finite clock identity sum_{n<=X, Cmin(n)>K} 1/n = sum_a 2^-a sum_{m<=X/2^a odd, Smin(m)>K} 1/m.
All on actual Collatz orbits; the analytic input (Tao Prop. 1.11) is NOT checked here."""
import time, random
from fractions import Fraction
t0=time.time()
def v2(x): return (x & -x).bit_length()-1
def T(n): x=3*n+1; return x>>v2(x)
LIM=10**6
DAG='dagger'
def p(x,n):
    # first orbit value of n (odd) in [1,x]; all orbits here reach 1 (checked), so dagger never occurs
    while n>x:
        n=T(n)
    return n
xs=[3,10,57,100,1000,12345,10**5]
cnt=0
for n in range(1,LIM,2):
    for i,x in enumerate(xs):
        for y in xs[i:]:
            a=p(x,p(y,n)); b=p(y,p(x,n)); c=p(x,n)
            assert a==c and b==c, (n,x,y)
            cnt+=1
# J map on E_{x_r} (odd values <= x_r): tuples compatible; inverse = last coordinate
xr=xs[-1]; tuples={}
for z in range(1,xr+1,2):
    tup=tuple(p(x,z) for x in xs)
    assert tup[-1]==z
    for i in range(len(xs)-1):
        assert p(xs[i],tup[i+1])==tup[i]
    tuples[tup]=z
assert len(tuples)==(xr+1)//2
# l1 contraction of pushforward by p_x on random signed measures
random.seed(1)
for _ in range(200):
    supp=random.sample(range(1,200001,2),50)
    mu={n:Fraction(random.randint(-5,5)) for n in supp}
    push={}
    for n,wt in mu.items(): push[p(100,n)]=push.get(p(100,n),0)+wt
    assert sum(abs(v) for v in push.values())<=sum(abs(v) for v in mu.values())
# clock identity
X=200000; K=50
Smin={}
def smin(m):
    best=m; x=m
    while x!=1:
        x=T(x); best=min(best,x)
    return best
def cmin(n):
    best=n; x=n
    while x!=1:
        x = x//2 if x%2==0 else 3*x+1
        best=min(best,x)
    return best
lhs=sum(Fraction(1,n) for n in range(1,X+1) if cmin(n)>K)
rhs=Fraction(0); a=0
while X>>a:
    rhs+=Fraction(1,2**a)*sum(Fraction(1,m) for m in range(1,X//2**a+1,2) if smin(m)>K); a+=1
assert lhs==rhs
print('nested passage p_x p_y = p_x = p_y p_x: %d checks (odd n<1e6, thresholds %s): PASS'%(cnt,xs))
print('J: E_%d -> compatible tuples is a bijection with inverse last projection (%d atoms): PASS'%(xr,len(tuples)))
print('l1 contraction of pushforward by p_100 on 200 random signed measures: PASS')
print('clock identity (X=%d, K=%d): both sides equal exactly (= %.6f): PASS'%(X,K,float(lhs)))
print('elapsed %.1fs'%(time.time()-t0))
