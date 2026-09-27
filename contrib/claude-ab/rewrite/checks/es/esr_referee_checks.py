# esr_referee_checks.py -- claude-ab (Opus 5.5), 27 September 2026.
# Checks, independent of the workbench code and of the referee's scripts, of the referee findings adopted in the ES reader, version 2:
# Prop. 3.4 (survivors hard mod 840), Props. 3.7-3.8 (group barrier, converse), the census domain, the shell at p=12289,
# the base rows and the square-row count of Cor. 4.7, and the even levels of the ES-09 covers (Sec. 5.2).

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

# ---- census base rows (Cor. 4.7) ----
# and count square rows of the final census domain.
from math import gcd
B1=[529,961,1681,2545,2689,3697,3985,5569,5713,8017,8737,9025,9601,10033,10609]
B25=[25,169,2473,3193,3481,4057,4489,5065,6073,6505,7225,8089,8233,9241,9529]
M=11088
assert M==16*9*7*11
sq={(x*x)%M for x in range(M) if gcd(x,M)==1}
print("unit squares mod 11088:",len(sq))
for r in B1+B25:
    assert gcd(r,M)==1, r
    assert r in sq, r
print("all 30 base rows are unit squares mod 11088: True")
print("B1 mod 72:",sorted({r%72 for r in B1}),"B25 mod 72:",sorted({r%72 for r in B25}))
print("mod 840 classes of base rows (mod 24 part):",sorted({r%24 for r in B1+B25}))
# census domain
dom=4590432000
assert dom==30*4*18*22*30*46*70
final=dom*190*82*166*238
print("final domain:",final, final==2825569908564480000)
odd_primes=[5,19,23,31,47,71,191,83,167,239]
sqrows=30
for q in odd_primes: sqrows*= (q-1)//2
print("square rows:",sqrows, "= final/2^10:", final//1024, final%1024==0, sqrows==final//1024)
forced=2757919929517785001
surv=final-forced
print("final survivors:",surv, "square rows <= survivors:", sqrows<=surv, "share of domain:", sqrows/final, "; share of survivors: %.4f"%(sqrows/surv))

# ---- prime R: the two barriers agree ----
def isprime_small(n):
    if n<2: return False
    i=2
    while i*i<=n:
        if n%i==0: return False
        i+=1
    return True
def factor(n):
    f={}; d=2
    while d*d<=n:
        while n%d==0: f[d]=f.get(d,0)+1; n//=d
        d+=1
    if n>1: f[n]=1
    return f
def subgroup(gens,R):
    G={1}; fr=[1]
    while fr:
        x=fr.pop()
        for g in gens:
            y=(x*g)%R
            if y not in G: G.add(y); fr.append(y)
    return G
n=diff=0
for p in range(5,1500):
    if not isprime_small(p) or p%4!=1: continue
    for a in range(p//4+1,p):
        R=4*a-p
        if not isprime_small(R): continue
        fa=factor(a); n+=1
        B=(R-1) not in subgroup([4%R]+[q%R for q in fa],R)
        J=all(pow(q,(R-1)//2,R)==1 for q in fa)
        if B!=J: diff+=1
print("prime R = 3 mod 4, shells of primes p = 1 mod 4 below 1500:",n,"; hypotheses differ:",diff)

# ---- ES-09 even levels ----
# g = 1 + (n - c(A1) - c(A2) - c(Ainf))/2 on an orbit of size n, c = number of cycles.
A1=[[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]]
A2=[[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]]
Ai=[[1,0,0,0],[0,1,0,0],[0,1,1,0],[-1,0,0,1]]
def mul(A,B): return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
I=[[int(i==j) for j in range(4)] for i in range(4)]
assert mul(mul(A1,A1),A1)==I and mul(mul(A2,A2),mul(A2,A2))==I and mul(mul(A1,A2),Ai)==I
def act(A,v,D):
    x=(1,)+v
    return tuple(sum(A[i][k]*x[k] for k in range(4))%D for i in range(1,4))
def analyse(D):
    pts=[(x,y,z) for x in range(D) for y in range(D) for z in range(D)]
    maps=[{v:act(A,v,D) for v in pts} for A in (A1,A2,Ai)]
    seen=set(); out=[]
    for v in pts:
        if v in seen: continue
        orb={v}; st=[v]
        while st:
            w=st.pop()
            for m in maps[:2]:
                u=m[w]
                if u not in orb: orb.add(u); st.append(u)
        seen|=orb
        cyc=[]
        for m in maps:
            done=set(); c=0
            for w in orb:
                if w in done: continue
                c+=1; t=w
                while t not in done: done.add(t); t=m[t]
            cyc.append(c)
        n=len(orb); g2=n-sum(cyc)+2   # 2g
        out.append((n, g2//2 if g2%2==0 else g2/2))
    return sorted(out)
for D in (2,4,8,16,32):
    r=analyse(D); print(D, r, " sizes D^3/4, 3D^3/4:", [n for n,_ in r]==[D**3//4, 3*D**3//4])
for D in (3,12): print(D, analyse(D))
