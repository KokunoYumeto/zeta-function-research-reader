"""Exhaustive finite-table checks and exact integer samples for the four-corner proofs."""
from itertools import product, combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
T,O="tau","Omega"

def add(x,y,mod=None):
    if O in (x,y): return O
    if x==T: return y
    if y==T: return x
    return x+y if mod is None else (x+y)%mod

def mul(x,y,mod=None):
    if O in (x,y): return O
    if T in (x,y): return T
    return x*y if mod is None else x*y%mod

L=(T,0,O)
C=(0,1,2)
def hom(f,src,dst,a1,m1,a2,m2):
    return all(f[a1(x,y)]==a2(f[x],f[y]) and f[m1(x,y)]==m2(f[x],f[y])
               for x,y in product(src,repeat=2))

c_to_l=[]
for vals in product(L,repeat=3):
    f=dict(zip(C,vals))
    if hom(f,C,L,max,min,add,mul): c_to_l.append(vals)
expected={(T,T,T),(0,0,0),(O,O,O),(T,T,0),(T,0,0)}
assert set(c_to_l)==expected
l_to_c=[]
for vals in product(C,repeat=3):
    f=dict(zip(L,vals))
    if hom(f,L,C,add,mul,max,min): l_to_c.append(vals)
assert set(l_to_c)=={(0,0,0),(1,1,1),(2,2,2)}
closed=[]
for size in (1,2,3):
    for subset in combinations(L,size):
        assert all(add(x,y) in subset and mul(x,y) in subset for x,y in product(subset,repeat=2))
        closed.append(subset)
f={0:O,1:T,2:0}
assert all(f[min(x,y)]==mul(f[x],f[y]) for x,y in product(C,repeat=2))
assert not hom(f,C,L,max,min,add,mul)

def partitions(n):
    def grow(seq):
        if len(seq)==n: yield tuple(seq); return
        for x in range(max(seq)+2): yield from grow(seq+[x])
    yield from grow([0])

def canon(labels):
    seen={}
    return tuple(seen.setdefault(x,len(seen)) for x in labels)

congruences=[]
for n in (2,3,4):
    for literal in (False,True):
        xs=tuple(range(n))+(T,)+((O,) if literal else ())
        idx={x:i for i,x in enumerate(xs)}
        found=set(); count=0
        for p in partitions(len(xs)):
            count+=1
            ok=all(p[idx[add(x,z,n)]]==p[idx[add(y,z,n)]]
                   and p[idx[mul(x,z,n)]]==p[idx[mul(y,z,n)]]
                   for x,y,z in product(xs,repeat=3) if p[idx[x]]==p[idx[y]])
            if ok: found.add(p)
        expected=set()
        for d in range(1,n+1):
            if n%d: continue
            rings=[("r",r%d) for r in range(n)]
            tail=[O] if literal else []
            expected.add(canon(rings+[T]+tail))
            expected.add(canon(rings+[("r",0)]+tail))
        if literal: expected.add((0,)*len(xs))
        assert found==expected,(n,literal,found-expected,expected-found)
        congruences.append({"input":f"Z/{n}Z","object":"H" if literal else "S",
                            "partitions_checked":count,"congruences":len(found)})

integers=tuple(range(-8,9))
def nu(x):
    return O if x==O else T if x==0 else 0
rank={T:0,0:1,O:2}
def q(x): return 0 if x==T else x
def rho(x): return x if x in (T,O) else 0
xs=integers+(T,O)
for x,y in product(xs,repeat=2):
    assert q(add(x,y))==add(q(x),q(y))
    assert q(mul(x,y))==mul(q(x),q(y))
    assert rho(add(x,y))==add(rho(x),rho(y))
    assert rho(mul(x,y))==mul(rho(x),rho(y))
for x,y in product(integers+(O,),repeat=2):
    assert nu(mul(x,y))==mul(nu(x),nu(y))
    assert rank[nu(add(x,y))]<=rank[add(nu(x),nu(y))]
image={(q(x),rho(x)) for x in xs}
compatible={(n,s) for n in integers for s in (T,0)}|{(O,O)}
constrained={(n,s) for n,s in compatible if rank[nu(n)]<=rank[s]}
assert image==constrained
assert compatible-image=={(n,T) for n in integers if n!=0}
def mono(x): return O if x==T else x
for x,y in product(integers+(T,),repeat=2):
    assert mono(mul(x,y))==mul(mono(x),mono(y))
assert mono(add(T,1))!=add(mono(T),1)

report={
 "status":"passed",
 "scope":"Complete finite-table maps and congruences of finite quotient models; exact integer samples supplement the full proofs.",
 "all_C_to_H_maps_by_complete_idempotent_image":c_to_l,
 "all_L_to_C_maps":l_to_c,
 "finite_subalgebras_in_L":closed,
 "C_L_monoid_isomorphism_and_addition_failure":True,
 "finite_congruence_classifications":congruences,
 "integer_sample_range":[-8,8],
 "arithmetic_and_state_maps":True,
 "zero_test_multiplicative_and_sum_inequality":True,
 "constrained_reconstruction_and_missing_pairs":True,
 "S_A_monoid_isomorphism_and_addition_failure":True
}
(ROOT/"INTEGER_CORNER_CHECKS.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
print(json.dumps(report,indent=2))
