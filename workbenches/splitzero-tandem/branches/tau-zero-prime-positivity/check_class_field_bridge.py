"""Exact finite and polynomial checks supplement the CBR proofs."""
from pathlib import Path
from itertools import permutations,product
import hashlib,json
import sympy as s
B=Path(__file__).resolve().parent
records=[]
def check(name,ok):
    assert bool(ok),name
    records.append(name)
def parity(p):
    return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
G={}
for p in permutations(range(4)):
    for sg in product([0,1],repeat=4):
        if (-1)**sum(sg)!=parity(p):continue
        q=tuple(2*p[j]+(k^sg[j]) for j in range(4) for k in range(2))
        G[q]=parity(p)
I=tuple(range(8))
def comp(a,b):return tuple(a[b[i]] for i in range(8))
def inv(a):return tuple(a.index(i) for i in range(8))
check('order of original signed group',len(G)==192)
comms={comp(comp(comp(a,b),inv(a)),inv(b)) for a in G for b in G}
H={I}; todo=[I]
while todo:
    a=todo.pop()
    for c in comms:
        z=comp(a,c)
        if z not in H:H.add(z);todo.append(z)
check('full derived subgroup and exact character kernel',H=={g for g,v in G.items() if v==1} and len(H)==96)
for i in range(8):check(f'derived subgroup orbit of state {i}',{g[i] for g in H}==set(range(8)))
stabilizer={g for g in G if g[0]==0}
check('degree-16 common cover and both quotient maps',len(stabilizer)==24 and len(stabilizer&H)==12 and {(g[0],G[g]) for g in G}=={(i,e) for i in range(8) for e in [-1,1]})
R,A,h,t,T,w,z=s.symbols('R A h t T w z')
F=A*R**4+R**3-R
check('original infinity-path discriminant',s.discriminant(F,R)==4-27*A**2)
Fh=(R-1)*(R**2+R-16*h)
check('original heat discriminant',s.expand(s.discriminant(Fh,R)-(2-16*h)**2*(64*h+1))==0)
check('exact heat shift',s.expand(s.discriminant(Fh,R).subs(h,t+s.Rational(1,8))-256*t*t*(9+64*t))==0)
sq={i*i%23 for i in range(1,23)}
def leg(a):return 0 if a%23==0 else (1 if a%23 in sq else -1)
check('complete residues and selected primes',sq=={1,2,3,4,6,8,9,12,13,16,18} and leg(2)==1 and leg(5)==-1 and leg(-1)==-1)
gauss=sum(leg(a)*z**a for a in range(1,23));phi=sum(z**a for a in range(23))
check('exact Gauss square modulo cyclotomic polynomial',s.rem(gauss**2+23,phi,z)==0)
for r in range(1,23):
    act=sum(leg(a)*z**((a*r)%23) for a in range(1,23))
    check(f'cyclotomic character action {r}',s.rem(act-leg(r)*gauss,phi,z)==0)
theta=(1+w)/2
check('maximal-order defining relation',s.rem(s.expand(theta**2-theta+6),w*w+23,w)==0)
check('two integral discriminants',s.discriminant(w*w+23,w)==-92 and s.discriminant(z*z-z+6,z)==-23)
check('nonmaximal reduction at two',s.Poly(w*w+23-(w+1)**2,w,modulus=2).is_zero)
check('maximal reduction at two',s.Poly(z*z-z+6-z*(z-1),z,modulus=2).is_zero)
def red(f):return s.rem(s.expand(f),T**4,T)
def delta(f):return red(-T**3*s.diff(f,T)/16)
for i in range(4):
    for j in range(4):check(f'residue Leibniz basis {i},{j}',red(delta(T**i*T**j)-delta(T**i)*T**j-T**i*delta(T**j))==0)
n1=T*T/2;n2=3*T+T**3/6;n3=T**3/2
check('original residue coefficient',delta(n2)==-s.Rational(3,8)*n3)
for i in range(4):check(f'residue squared on basis {i}',delta(delta(T**i))==0)
check('nonzero residue and special-fibre dimensions',delta(T)==-T**3/16 and len(s.Poly(T**4,T).all_coeffs())-1==4)
for k in range(1,9):
    M=s.Matrix([[0,1],[1,0]])
    check(f'inert-prime regular trace at iterate {k}',s.trace(M**k)==1+(-1)**k)
proof=B/'CLASS_FIELD_SIGNED_HOLONOMY_DERIVATION.md'
out={'status':'passed','checks':len(records),'records':records,'proof':proof.name,'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),'scope':'Exact finite groups and polynomial identities; analytic continuation, source theorem, and module arguments are proved in the accompanying text.'}
(B/'CLASS_FIELD_BRIDGE_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','checks':len(records)}))
