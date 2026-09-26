# Sharp form of Prop 2.4: with n0 the least member >= 3 of the cylinder of w, every member n >= 3 has T^m(n) < n  iff  F_m(n0) < n0.
import itertools
from fractions import Fraction as Fr
def T(n):
    x=3*n+1; a=0
    while x%2==0: x//=2; a+=1
    return x,a
def words(Amax):
    # all exponent words with sum <= Amax (each a_i >= 1)
    out=[]
    def rec(w,s):
        if w: out.append(tuple(w))
        for a in range(1,Amax-s+1): rec(w+[a],s+a)
    rec([],0); return out
def affine(w):
    C=0; A=0
    for a in w: C=3*C+2**A; A+=a
    return len(w),C,A   # F(x)=(3^m x + C)/2^A
def cylinder_residue(w):
    # the odd residue r mod 2^(A+1) with exponent word starting with w: search
    m,C,A=affine(w); M=2**(A+1)
    for r in range(1,M,2):
        x=r; okw=True
        for a in w:
            x,b=T(x)
            if b!=a: okw=False; break
        if okw: return r,M
    return None
Amax=13
cnt_sharp=0; cnt_ref3=0; extra=0; bad=0; tested=0
for w in words(Amax):
    m,C,A=affine(w); D=2**A-3**m
    r,M=cylinder_residue(w)
    n0=r if r>=3 else r+M
    sharp = (3**m*n0+C) < 2**A*n0
    ref3 = (3**(m+1)+C) < 3*2**A
    cnt_sharp+=sharp; cnt_ref3+=ref3
    if sharp and not ref3: extra+=1
    assert not (ref3 and not sharp)
    # verify: members n >= 3 (first 40) descend at step m iff sharp
    alld=True
    for t in range(40):
        n=n0+t*M
        x=n
        for _ in range(m): x,_b=T(x)
        tested+=1
        if not (x<n): alld=False
    if alld!=sharp: bad+=1
print(f"words with A<={Amax}: {len(words(Amax))}; F_m(3)<3: {cnt_ref3}; sharp criterion F_m(n0)<n0: {cnt_sharp}; certified by the sharp form only: {extra}")
print(f"sharp criterion equals 'all tested members >=3 descend at step m' for every word: {bad==0} ({tested} starts tested)")
# example
w=(1,1,1,1,4); m,C,A=affine(w); r,M=cylinder_residue(w); print("example w=",w,": F(3)=",Fr(3**m*3+C,2**A)," D=",2**A-3**m," C=",C," n0=",r if r>=3 else r+M, " F(n0)<n0:", 3**m*(r if r>=3 else r+M)+C < 2**A*(r if r>=3 else r+M))
