# The classical mod-840 reduction, proved by two polynomial identities plus a finite congruence check.
import sympy as sp
from math import gcd
P,A,B,R=sp.symbols('p A B R', positive=True)
D=(P+R)/(4*A*B)
# middle: C=(A+B)/R ; exterior: C=(A+P*B)/R
Cm=(A+B)/R; Ce=(A+P*B)/R
idm=sp.simplify(1/(A*B*D)+1/(P*A*Cm*D)+1/(P*B*Cm*D)-4/P)
ide=sp.simplify(1/(A*B*D)+1/(A*Ce*D)+1/(P*B*Ce*D)-4/P)
print("middle identity 1/(ABD)+1/(pACD)+1/(pBCD)=4/p with D=(p+R)/(4AB), C=(A+B)/R:", idm==0)
print("exterior identity 1/(ABD)+1/(ACD)+1/(pBCD)=4/p with D=(p+R)/(4AB), C=(A+pB)/R:", ide==0)
units=[c for c in range(840) if gcd(c,840)==1 and c%24==1]
cov={}
for a_ in range(1,211):
    for b_ in range(1,211):
        if 210%(a_*b_): continue
        m=4*a_*b_
        for r_ in sp.divisors(a_+b_):
            for c in units:
                if (c+r_)%m==0: cov.setdefault(c,[]).append(('M',a_,b_,r_))
        for r_ in sp.divisors(105):
            if gcd(r_,a_*b_)!=1: continue
            for c in units:
                if (c+r_)%m==0 and (c*b_+a_)%r_==0: cov.setdefault(c,[]).append(('E',a_,b_,r_))
sq=sorted({x*x%840 for x in range(840) if gcd(x,840)==1})
print("unit classes = 1 mod 24:",len(units),"; covered:",len(cov),"; uncovered = unit squares:", sorted(set(units)-set(cov))==sq, sorted(set(units)-set(cov)))
# integrality: D integer iff 4AB | p+R (4AB | 840 so decided by c mod 840); C integer: middle R | A+B by construction,
# exterior R | A + pB decided by c mod R (R | 105); x,y,z positive. So each covered class is proved for all p in it.
# simplest family per class (smallest A*B, then R)
for c in sorted(cov):
    best=min(cov[c], key=lambda t:(t[1]*t[2],t[3],t[0]))
    print(f"  p = {c:3d} mod 840 (p mod 5 = {c%5}, p mod 7 = {c%7}): {best}")
# a compact description by residues mod 5 and 7 (p = 1 mod 24 throughout)
