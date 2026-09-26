# ES checks: (1) least denominator < p/2 for p = 1 mod 4 (sharp form of Thm 1.1(a)); exception family for p = 3 mod 4
# (2) shell count (b) for every a > p/4 with p not dividing a (not only a < p)
# (3) two-shell survivors are = 1 mod 24 (proof: a=(p+3)/4 even when p=13 mod 24); simplified R7 criterion at p = 1 mod 24
# (4) R3/R7 criteria for all primes p = 1 mod 4 (not only 1 mod 12)
import sympy as sp
from fractions import Fraction as Fr
from math import gcd
res=[]
def ok(n,c,i=""): res.append(c); print(("[PASS] " if c else "[FAIL] ")+n+(": "+str(i) if i!="" else ""))
def all_solutions(p):
    # all x<=y<=z with 4/p = 1/x+1/y+1/z
    sols=[]
    for x in range(p//4+1, 3*p//4+1):
        r=Fr(4,p)-Fr(1,x)
        if r<=0: continue
        # y from max(x, ceil(1/r)) to floor(2/r)
        ylo=max(x, int(1/r)+1 if (1/r).denominator!=1 else int(1/r)+1)
        # careful: need 1/y < r strictly -> y > 1/r
        import math
        ylo=max(x, math.floor(1/r)+1)
        yhi=math.floor(2/r)
        for y in range(ylo, yhi+1):
            s=r-Fr(1,y)
            if s>0 and s.numerator==1 and s.denominator>=y:
                sols.append((x,y,s.denominator))
    return sols
bad=0; exc=0; nsol=0; maxratio=Fr(0)
for p in sp.primerange(3, 1200):
    for (x,y,z) in all_solutions(p):
        nsol+=1
        if p%4==1:
            if not (4*x>p and 2*x<p and x<y): bad+=1
        else:
            if 2*x>p:
                if (x,y,z)==((p+1)//2,(p+1)//2,p*(p+1)//4): exc+=1
                else: bad+=1
ok("least denominator x < p/2 and x < y for every solution at every prime p = 1 mod 4 < 1200; for p = 3 mod 4 x > p/2 only in ((p+1)/2,(p+1)/2,p(p+1)/4)", bad==0, f"{nsol} solutions, {exc} exceptional (p = 3 mod 4)")
# every p=3 mod 4 has the exceptional solution
ok("the exceptional solution occurs for every p = 3 mod 4 < 1200", all(((p+1)//2,(p+1)//2,p*(p+1)//4) in all_solutions(p) for p in sp.primerange(3,1200) if p%4==3))
# (2) shell count for a in (p/4, 3p] with p not dividing a
def divs_sq(a):
    f=sp.factorint(a); ds=[1]
    for q,e in f.items(): ds=[d*q**k for d in ds for k in range(2*e+1)]
    return ds
def brute_pairs(p,a):
    r=Fr(4,p)-Fr(1,a); cnt=0
    import math
    for y in range(math.floor(1/r)+1, math.floor(2/r)+1):
        s=r-Fr(1,y)
        if s>0 and s.numerator==1: cnt+= (2 if s.denominator!=y else 1)
    return cnt
bad=0; tot=0
for p in sp.primerange(3,120):
    for a in range(p//4+1, 3*p+1):
        if 4*a<=p or a%p==0: continue
        R=4*a-p; D=divs_sq(a)
        E=[u for u in D if (4*u+1)%R==0]; M=[u for u in D if (u+a)%R==0]
        tot+=1
        if brute_pairs(p,a)!=2*len(E)+len(M): bad+=1
ok("Thm 1.1(b) count 2|E_a|+|M_a| for every a in (p/4, 3p] with p not dividing a (p<120 prime)", bad==0, f"{tot} pairs (p,a)")
# (3) two-shell survivors below 10^6
def r3_occ(a):  # a = (p+3)/4 = 1 mod 3: occupied iff prime factor = 2 mod 3
    return any(q%3==2 for q in sp.factorint(a))
def r7_occ(a):
    f=sp.factorint(a); n3=sum(e for q,e in f.items() if q%7==3); n24=sum(e for q,e in f.items() if q%7 in (2,4))
    return any(q%7 in (5,6) for q in f) or n3>=3 or (n3>=1 and n24>=1)
def r7_occ_simpl(a):  # claimed simplification when a is even (p = 1 mod 24): any prime factor that is a QNR mod 7
    return any(q%7 in (3,5,6) for q in sp.factorint(a))
surv=[]; mismatch=0; n13=0; n13occ=0
for p in sp.primerange(13,10**6):
    if p%12!=1: continue
    a3=(p+3)//4; a7=(p+7)//4
    if p%24==13:
        n13+=1; n13occ+= (a3%2==0 and r3_occ(a3))
    else:
        if a7%2!=0: mismatch+=1
        if r7_occ(a7)!=r7_occ_simpl(a7): mismatch+=1
    if not r3_occ(a3) and not r7_occ(a7): surv.append(p)
ok("two-shell survivors below 10^6", len(surv)==989 and all(p%24==1 for p in surv), f"{len(surv)} survivors, first {surv[:3]}")
ok("p = 13 mod 24: a=(p+3)/4 is even so the residual-3 shell is always occupied", n13==n13occ, f"{n13} primes")
ok("p = 1 mod 24: a=(p+7)/4 is even and the R7 criterion equals 'a has a prime factor = 3,5,6 mod 7'", mismatch==0)
# (4) R3 and R7 criteria for all p = 1 mod 4 (incl. p = 5 mod 12), against the shell sets
bad3=0; bad7=0; cnt=0
for p in sp.primerange(5, 3*10**4):
    if p%4!=1: continue
    cnt+=1
    a=(p+3)//4; R=3; D=divs_sq(a)
    occ=any((4*u+1)%R==0 or (u+a)%R==0 for u in D)
    if p%3==1 and occ!=r3_occ(a): bad3+=1
    if p%3==2 and not occ: bad3+=1   # always occupied (u=1 in M)
    a=(p+7)//4; R=7; D=divs_sq(a)
    occ=any((4*u+1)%R==0 or (u+a)%R==0 for u in D)
    if p!=7 and occ!=r7_occ(a): bad7+=1
ok("R3 criterion (p = 1 mod 12) and 'always occupied' (p = 5 mod 12) against the shell sets, all p = 1 mod 4 < 3e4", bad3==0, f"{cnt} primes")
ok("R7 criterion holds for every prime p = 1 mod 4 < 3e4 (not only p = 1 mod 12)", bad7==0)
print("ALL PASS" if all(res) else "FAILURES")
