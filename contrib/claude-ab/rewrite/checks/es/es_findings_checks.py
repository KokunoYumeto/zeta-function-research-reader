# claude-ab: independent checks of ES referee findings 2, 6, 12 and results B, C (27 Sep 2026).
from math import gcd
from fractions import Fraction as F
N=3*10**6+100
spf=list(range(N//4+50))
for i in range(2,int(len(spf)**0.5)+1):
    if spf[i]==i:
        for j in range(i*i,len(spf),i):
            if spf[j]==j: spf[j]=i
def isprime(n):
    if n<2: return False
    if n<len(spf): return spf[n]==n
    d=2
    while d*d<=n:
        if n%d==0: return False
        d+=1
    return True
S=bytearray([1])*(N+1); S[0]=S[1]=0
for i in range(2,int(N**0.5)+1):
    if S[i]: S[i*i::i]=bytearray(len(S[i*i::i]))
def factor(n):
    f={}
    if n<len(spf):
        while n>1:
            q=spf[n]; f[q]=f.get(q,0)+1; n//=q
        return f
    d=2
    while d*d<=n:
        while n%d==0: f[d]=f.get(d,0)+1; n//=d
        d+=1
    if n>1: f[n]=f.get(n,0)+1
    return f
def divres(a,R):
    cur={1%R}
    for q,e in factor(a).items():
        cur={(x*pow(q,k,R))%R for x in cur for k in range(2*e+1)}
    return cur
def occupied(p,R):
    a=(p+R)//4
    return bool(divres(a,R)&{(-pow(4,-1,R))%R,(-a)%R})
HARD={1,121,169,289,361,529}
surv=[p for p in range(13,10**6,12) if S[p] and not occupied(p,3) and not occupied(p,7)]
cls={}
for p in surv: cls.setdefault(p%840,p)
print("F2: two-shell survivors p=1 mod 12 below 1e6:",len(surv),"; all hard mod 840:",all(p%840 in HARD for p in surv),"; least per class:",dict(sorted(cls.items())))
c={1:0,25:0,49:0}
for p in range(25,3*10**6,24):
    if S[p] and not occupied(p,7) and not occupied(p,11): c[p%72]+=1
print("F6: p=1 mod 24 below 3e6 with the R=7 and R=11 shells empty:",sum(c.values()),"; by class mod 72:",c)
p=12289; a=3075; R=4*a-p; fa=factor(a)
divs=[1]
for q,e in fa.items(): divs=[d*q**k for d in divs for k in range(2*e+1)]
E=sorted(u for u in divs if (4*u+1)%R==0); M=sorted(u for u in divs if (u+a)%R==0)
least=min(b for b in range(p//4+1,p) if occupied(p,4*b-p))
sols=set()
for u in E: sols.add(tuple(sorted((a,p*(p*u+a)//R,(p*a+a*a//u)//R))))
for u in M: sols.add(tuple(sorted((a,p*(a+u)//R,p*(a+a*a//u)//R))))
print("F12: p=12289, a=3075=%s, R=%d; E=%s; M=%s; least occupied shell %d; unordered solutions with least denominator 3075: %d; valid: %s"%(
      fa,R,E,M,least,len(sols),all(F(1,x)+F(1,y)+F(1,z)==F(4,p) for x,y,z in sols)))
def jacobi(a,n):
    a%=n; r=1
    while a:
        while a%2==0:
            a//=2
            if n%8 in (3,5): r=-r
        a,n=n,a
        if a%4==3 and n%4==3: r=-r
        a%=n
    return r if n==1 else 0
def subgroup(gens,R):
    G={1%R}; fr=[1%R]
    while fr:
        x=fr.pop()
        for g in gens:
            y=(x*g)%R
            if y not in G: G.add(y); fr.append(y)
    return G
def order(g,R):
    k=1; x=g%R
    while x!=1: x=(x*g)%R; k+=1
    return k
nB=failB=strict=nC=failC=0
for p in range(5,1500):
    if not S[p]: continue
    for a in range(p//4+1,p):
        R=4*a-p
        if R<3: continue
        fa=factor(a); occ=bool(divres(a,R)&{(-pow(4,-1,R))%R,(-a)%R})
        G=subgroup([4%R]+[q%R for q in fa],R); nB+=1
        if (R-1) not in G:
            if occ: failB+=1
            if R%4==3 and not all(jacobi(q,R)==1 for q in fa): strict+=1
        if all(2*e>=order(q,R)-1 for q,e in fa.items()):
            H=subgroup([q%R for q in fa],R); nC+=1
            if (((R-1) in H) or ((-pow(4,-1,R))%R in H))!=occ: failC+=1
print("B: all shells of primes 5<=p<1500 with R>=3: %d; group barrier violated: %d; shells with R=3 mod 4 where B applies and the Jacobi barrier does not: %d"%(nB,failB,strict))
print("C: shells satisfying the exponent condition: %d; mismatches with the criterion: %d"%(nC,failC))
G=subgroup([4,2,13],51)
print("B example: p=53, a=26, R=51: G_a=%s; -1 in G_a: %s; (2/51)=%d; occupied: %s"%(sorted(G),50 in G,jacobi(2,51),occupied(53,51)))
