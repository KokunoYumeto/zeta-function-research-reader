# Check length-5 paths at p = 1183451 and p = 3533141 directly from the definitions.
from math import gcd
def isprime(n):
    if n<2: return False
    i=2
    while i*i<=n:
        if n%i==0: return False
        i+=1
    return True
def in_W(p,a,m,n):
    R=4*a-p
    return R>=1 and (p*a)%m==0 and (p*a)%n==0 and gcd(m,n)==1 and (m+n)%R==0
for p in (109391,1183451,3533141):
    print(p,"prime:",isprime(p),"p mod 4:",p%4,"p mod 3:",p%3)
    for R in range(1,60,2):
        if (p+R)%4: continue
        a=(p+R)//4
        k=0
        while a+k+1<p and in_W(p,a+k+1,a+k+1,1) and in_W(p,a,a,1): k+=1
        if k>=4: print("   diagonal path from a=(p+R)/4, R=%d: length %d; R+4i for i<=k:"%(R,k),[R+4*i for i in range(k+1)],"(p+4)=",p+4)
