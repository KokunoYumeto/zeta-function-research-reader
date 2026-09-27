# Independent check (claude-ab) of the referee's Proposition D on shear paths.
# Definitions as in the reader's Prop. 2.1: W_a = {(m,n): m|pa, n|pa, gcd(m,n)=1, R_a | m+n}, R_a = 4a-p,
# shells p/4 < a < p; an L-edge (a,m,n)->(a+1,m+n,n), a J-edge (a,m,n)->(a+1,m,m+n), image in W_{a+1}.
from math import gcd
import sys, time
t0=time.time()
def sieve(n):
    s=bytearray([1])*(n+1); s[0]=s[1]=0
    for i in range(2,int(n**0.5)+1):
        if s[i]: s[i*i::i]=bytearray(len(s[i*i::i]))
    return s
X=10**7
S=sieve(X+10)
def divisors(n):
    ds=[1]; x=n; f=2
    while f*f<=x:
        if x%f==0:
            e=0
            while x%f==0: x//=f; e+=1
            ds=[d*f**k for d in ds for k in range(e+1)]
        f+=1 if f==2 else 2
    if x>1: ds=[d*x**k for d in ds for k in range(2)]
    return ds
# Part 1: brute force on the full graph for primes below 1200 (all edges, both shears), no use of the edge shape.
maxdeg_ok=True; viol=0; first={}
for p in range(3,1200):
    if not S[p]: continue
    W={}
    for a in range(p//4+1,p):
        R=4*a-p; D=divisors(p*a)
        W[a]={(m,n) for m in D for n in D if gcd(m,n)==1 and (m+n)%R==0}
    out={}; inn={}
    for a in range(p//4+1,p-1):
        for (m,n) in W[a]:
            for t in ((m+n,n),(m,m+n)):
                if t in W[a+1]:
                    out[(a,m,n)]=out.get((a,m,n),0)+1; inn[(a+1,)+t]=inn.get((a+1,)+t,0)+1
                    if not ((t[1]==1 and t[0]==m+1) or (t[0]==1 and t[1]==n+1)): viol+=1   # edge shape: n=1 or m=1
    if any(v>1 for v in out.values()) or any(v>1 for v in inn.values()): maxdeg_ok=False
    # longest path
    L={}
    for a in range(p-1,p//4,-1):
        for (m,n) in W[a]:
            best=0
            for t in ((m+n,n),(m,m+n)):
                if a+1<p and t in W.get(a+1,()): best=max(best,1+L[(a+1,)+t])
            L[(a,m,n)]=best
    k=max(L.values()) if L else 0
    for j in range(1,k+1): first.setdefault(j,p)
    if k>=2 and p%3!=2: print("VIOLATION of (a) at",p)
print("P1 full graph p<1200: in/out-degree<=1:",maxdeg_ok,"; edges not of the proved shape:",viol,"; least p with a path of length k:",first)
# Part 2: complete enumeration of L-paths of length k (k>=2) with p<X via the proved edge shape:
# vertices (a+i, m+i, 1), m+i | a+i, R+4i | m+i+1 (i=0..k).  (J-paths are the mirror images.)
def paths(k,X):
    found={}
    R=1
    while 3*R<=X:
        # CRT for m: m = -(i+1) mod (R+4i), i=0..k
        m0,M=0,1
        ok=True
        for i in range(k+1):
            q=R+4*i; r=(-(i+1))%q
            # solve m0 + M*t = r mod q
            g=gcd(M,q)
            if (r-m0)%g: ok=False; break
            Mg=M//g; qg=q//g
            t=((r-m0)//g)*pow(Mg,-1,qg)%qg if qg>1 else 0
            m0=m0+M*t; M=M*qg; m0%=M
        if not ok: R+=2; continue
        m=m0 if m0>0 else M
        while 4*m-R<=X:
            from math import lcm
            Lm=1
            for i in range(k+1): Lm=lcm(Lm,m+i)
            a=m
            while 4*a-R<=X:
                p=4*a-R
                if p>3 and a+k<p and S[p]:
                    found.setdefault(p,[]).append((R,a,m))
                a+=Lm
            m+=M
        R+=2
    return found
P2=paths(2,X)
n2=sum(1 for p in range(2,X) if S[p] and p%3==2)
print("P2 primes p<1e7 with a two-edge L-path:",len(P2),"; paths:",sum(len(v) for v in P2.values()),"; primes = 2 mod 3 below 1e7:",n2,"; share %.4f"%(len(P2)/n2))
print("   all such p are 2 mod 3:",all(p%3==2 for p in P2),"; R(R+4)|p+4 on every path:",all((p+4)%(R*(R+4))==0 for p,v in P2.items() for (R,a,m) in v),
      "; diagonal (a=m) paths:",sum(1 for v in P2.values() for (R,a,m) in v if a==m))
n131=[p for p in range(131,X,180) if S[p]]
print("   primes = 131 mod 180 below 1e7:",len(n131),"; all have a two-edge path:",all(p in P2 for p in n131))
print("   least primes = 2 mod 3 without one:",[p for p in range(2,120) if S[p] and p%3==2 and p not in P2])
for k in (3,4,5):
    Pk=paths(k,X)
    print("least prime <1e7 with a path of length",k,":",min(Pk) if Pk else None,"; number of such primes:",len(Pk))
print("runtime %.0f s"%(time.time()-t0))
