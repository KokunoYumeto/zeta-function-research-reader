import sympy as sp
from fractions import Fraction as Fr
res=[]
def ok(n,c,i=""): res.append(c); print(("[PASS] " if c else "[FAIL] ")+n+(": "+str(i) if i!="" else ""))
def r3_occ(a): return any(q%3==2 for q in sp.factorint(a))
def r7_occ(a):
    f=sp.factorint(a); n3=sum(e for q,e in f.items() if q%7==3); n24=sum(e for q,e in f.items() if q%7 in (2,4))
    return any(q%7 in (5,6) for q in f) or n3>=3 or (n3>=1 and n24>=1)
surv=[p for p in sp.primerange(13,10**6) if p%12==1 and not r3_occ((p+3)//4) and not r7_occ((p+7)//4)]
ok("all 989 two-shell survivors are = 1 mod 24 and = 1, 2 or 4 mod 7 (p a square mod 7)", len(surv)==989 and all(p%24==1 and p%7 in (1,2,4) for p in surv), f"residues mod 168 present: {sorted({p%168 for p in surv})}")
# the five identities: for p = 1 mod 24, 4/p = 1/(ABD)+1/(ACD)+1/(pBCD), D=(p+R)/(4AB), C=(A+pB)/R
fams={(3,7):(1,2,7),(5,7):(2,1,7),(6,7):(1,1,7),(2,5):(1,2,15),(3,5):(2,1,15)}
bad=0; used=0; cov=0; tot=0
for p in sp.primerange(25,2*10**6):
    if p%24!=1: continue
    tot+=1
    fam=None
    for (r,mod),f in fams.items():
        if p%mod==r: fam=f; break
    if fam is None:
        if p%840 not in (1,121,169,289,361,529): bad+=1
        continue
    cov+=1
    A,B,R=fam
    assert (p+R)%(4*A*B)==0 and (A+p*B)%R==0
    D=(p+R)//(4*A*B); C=(A+p*B)//R
    if Fr(1,A*B*D)+Fr(1,A*C*D)+Fr(1,p*B*C*D)!=Fr(4,p): bad+=1
ok("five identities (A,B,R)=(1,2,7),(2,1,7),(1,1,7),(1,2,15),(2,1,15) for p = 3,5,6 mod 7 and 2,3 mod 5 cover every prime p = 1 mod 24 < 2e6 outside the six unit-square classes mod 840", bad==0, f"{cov} of {tot} primes covered")
print("ALL PASS" if all(res) else "FAILURES")
