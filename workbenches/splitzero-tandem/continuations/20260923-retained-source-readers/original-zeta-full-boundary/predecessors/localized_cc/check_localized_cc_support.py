from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib
import json
import math

R=Path(__file__).resolve().parent
checks=0
negative=0
def require(condition):
    global checks
    assert condition
    checks+=1

for kind,size in [('chain',2),('chain',3),('chain',4),('boolean',4)]:
    top=size-1
    join=(lambda a,b:max(a,b)) if kind=='chain' else (lambda a,b:a|b)
    meet=(lambda a,b:min(a,b)) if kind=='chain' else (lambda a,b:a&b)
    zero=(Q(0),0); one=(Q(1),top); e=(Q(0),top)
    def add(x,y): return (x[0]+y[0],join(x[1],y[1]))
    def mul(x,y): return (x[0]*y[0],meet(x[1],y[1]))
    def scale(a,x): return mul((Q(a),top),x)
    def power(x,n):
        ans=one
        for _ in range(n): ans=mul(ans,x)
        return ans
    def F(a,b,N=3):
        M=[[zero for _ in range(N+1)] for _ in range(N+1)]
        for i in range(N+1):
            for j in range(i,N+1):
                v=zero; d=j-i
                for k in range(d//2+1):
                    coefficient=Q((-1)**k*math.factorial(j),math.factorial(i)*math.factorial(k)*math.factorial(d-2*k))
                    v=add(v,scale(coefficient,mul(power(a,k),power(b,d-2*k))))
                M[i][j]=v
        return M
    def matmul(A,B):
        n=len(A)
        C=[[zero for _ in range(n)] for _ in range(n)]
        for i,j in product(range(n),repeat=2):
            for k in range(n): C[i][j]=add(C[i][j],mul(A[i][k],B[k][j]))
        return C
    def act(A,v):
        ans=[]
        for row in A:
            a=zero
            for x,y in zip(row,v): a=add(a,mul(x,y))
            ans.append(a)
        return ans
    params=[(Q(0),a) for a in range(size)]+[(Q(1),top),(Q(-1),top)]
    for a,b,c,d in product(params,repeat=4):
        require(matmul(F(a,b),F(c,d))==F(add(a,c),add(b,d)))
    P=F(e,zero); Qm=F(e,e); I=F(zero,zero)
    require(matmul(P,P)==P);require(matmul(Qm,Qm)==Qm)
    require(matmul(P,Qm)==Qm);require(matmul(Qm,P)==Qm)
    require(P!=Qm);negative+=1
    for labs in product(range(size),repeat=4):
        v=[(Q(0),x) for x in labs]
        pv=act(P,v);qv=act(Qm,v)
        for i in range(4):
            lp=lq=0
            for j in range(i,4):
                lq=join(lq,labs[j])
                if (j-i)%2==0:lp=join(lp,labs[j])
            require(pv[i]==(Q(0),lp));require(qv[i]==(Q(0),lq))
        def total(v):
            a=0
            for _,l in v:a=join(a,l)
            return a
        require(total(pv)==total(v));require(total(qv)==total(v))
    # Compute every lattice prime and its actual denominator equivalence.
    for mask in range(1<<size):
        J={i for i in range(size) if mask>>i&1}
        if 0 not in J or top in J:continue
        if any(join(a,b) not in J for a,b in product(J,repeat=2)):continue
        if any(meet(a,b) not in J for a in J for b in range(size)):continue
        if any(meet(a,b) in J and a not in J and b not in J for a,b in product(range(size),repeat=2)):continue
        def eq(a,b):return any(meet(a,n)==meet(b,n) for n in range(size) if n not in J)
        require(not eq(0,top))
        for a,b,c in product(range(size),repeat=3):
            if eq(a,b):
                require(eq(join(a,c),join(b,c)))
                require(eq(meet(a,c),meet(b,c)))
        # Degree-one input distinguishes the localized P and Q at every prime.
        v=[zero,one,zero,zero]
        require(eq(act(P,v)[0][1],0));require(eq(act(Qm,v)[0][1],top))
        require(not eq(act(P,v)[0][1],act(Qm,v)[0][1]));negative+=1

receipt={'checks':checks,'negative_controls':negative,
         'scope':'Exact finite supplementary checks. General proofs are CDV, ULC and CLS, not an inference from samples.',
         'sources':{n:hashlib.sha256((R/'independent'/n).read_bytes()).hexdigest() for n in
                    ['CC_DIVISOR_COEFFICIENT_FAMILY.tex','ARBITRARY_SUPPORT_CC_COEFFICIENTS.tex','CC_LOCALIZED_SHIFT_SYNCHRONIZATION.tex']}}
(R/'LOCALIZED_CC_SUPPORT_EXACT_CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
