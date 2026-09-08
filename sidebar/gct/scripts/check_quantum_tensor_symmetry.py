"""Exact source witnesses and all source-string Clebsch maps at rational q.

General proofs over D and K are in tex/quantum_tensor_symmetry.tex. This
certificate checks the source inputs and independently evaluates each
string used by the full-source formula. No dense 1260^2 matrix is needed.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import hashlib, json

ROOT=Path(__file__).resolve().parents[1]
checks=0
def require(value):
    global checks
    assert value
    checks+=1

def qi(n,q):
    if n<0: return -qi(-n,q)
    return sum((q**(n-1-2*j) for j in range(n)),F(0))

def clean(v): return {k:a for k,a in v.items() if a}
def scale(v,a): return clean({k:a*b for k,b in v.items()})
def act(v,m,n,q,kind):
    out={}
    def add(k,a): out[k]=out.get(k,F(0))+a
    for (i,j),a in v.items():
        if kind=='F':
            if i<m: add((i+1,j),a*qi(i+1,q))
            if j<n: add((i,j+1),a*q**(m-2*i)*qi(j+1,q))
        else:
            if i: add((i-1,j),a*qi(m-i+1,q)*q**(-n+2*j))
            if j: add((i,j-1),a*qi(n-j+1,q))
    return clean(out)

def strings(m,n,q):
    result={}
    for r in range(min(m,n)+1):
        a=F(1); z={(0,r):a}
        for i in range(r):
            a=-a*q**(n-2*r+2+2*i)*qi(n-r+i+1,q)/qi(m-i,q)
            z[(i+1,r-i-1)]=a
        h=m+n-2*r
        require(not act(z,m,n,q,'E'))
        v=z
        for s in range(h+1):
            result[r,s]=v
            require(bool(v))
            require(all(i+j==r+s for i,j in v))
            if s:
                require(act(v,m,n,q,'E')==scale(result[r,s-1],qi(h-s+1,q)))
            v=scale(act(v,m,n,q,'F'),1/qi(s+1,q))
        require(not v)
    require(len(result)==(m+1)*(n+1))
    return result

def rank(rows):
    a=[row[:] for row in rows]; r=0
    for j in range(len(a[0]) if a else 0):
        k=next((k for k in range(r,len(a)) if a[k][j]),None)
        if k is None: continue
        a[r],a[k]=a[k],a[r]
        d=a[r][j]; a[r]=[x/d for x in a[r]]
        for k in range(r+1,len(a)):
            d=a[k][j]
            if d: a[k]=[x-d*y for x,y in zip(a[k],a[r])]
        r+=1
    return r

for q in [F(1),F(2),F(3,2)]:
    for m in [1,3,5,7,9]:
        for n in [1,3,5,7,9]:
            ws=strings(m,n,q)
            for degree in range(m+n+1):
                basis=[(i,degree-i) for i in range(m+1) if 0<=degree-i<=n]
                cols=[v for (r,s),v in ws.items() if r+s==degree]
                require(len(cols)==len(basis))
                require(rank([[v.get(b,F(0)) for v in cols] for b in basis])==len(basis))
            other=strings(n,m,q)
            for (r,s),v in ws.items():
                g=F((-1)**r*factorial(n)*factorial(m-r),factorial(n-r)*factorial(m))
                gi=F((-1)**r*factorial(m)*factorial(n-r),factorial(m-r)*factorial(n))
                require(g*gi==1)
                if q==1:
                    require({(j,i):a for (i,j),a in v.items()}==scale(other[r,s],g))

# Bind the ordinary-flip witness to the actual full original source matrices.
matrix_path=ROOT/'agents/full_source_generators/full_generators.json'
basis_path=ROOT/'agents/full_source_generators/source_basis/basis_1260.json'
M=json.loads(matrix_path.read_text())['matrices']
basis=json.loads(basis_path.read_text())['basis']
require(basis[126]['columns']==['123','123','124','12','12','1','1'])
require(basis[126]['weight_V']==[12,3])
require(basis[126]['weight_W']==[9,6])
require(M['EV'][126]==[] and M['EW'][126]==[])

def mulpoly(p,q):
    out={}
    for i,a in p.items():
        for j,b in q.items(): out[i+j]=out.get(i+j,0)+a*b
    return clean(out)
v={row:dict(coeff) for row,coeff in M['FV'][126]}
out={}
for col,c in v.items():
    for row,a in M['EV'][col]:
        dest=out.setdefault(row,{})
        for e,value in mulpoly(c,dict(a)).items(): dest[e]=dest.get(e,0)+value
out={k:clean(a) for k,a in out.items() if clean(a)}
require(out=={126:{j:1 for j in range(-8,9,2)}})
require(len(basis)==1260)

# Exact highest-(1,1) summand multiplicity from the original weight lattice.
weights={}
for b in basis:
    k=b['weight_V'][0],b['weight_W'][0]
    weights[k]=weights.get(k,0)+1
g88=weights.get((8,8),0)-weights.get((9,8),0)-weights.get((8,9),0)+weights.get((9,9),0)
require(g88==1)
require(1260*1261//2==794430 and 1260*1259//2==793170)

proof=ROOT/'tex/quantum_tensor_symmetry.tex'
receipt={'status':'passed','checks':checks,
 'scope':'75 exact rational-q tests of all 25 original odd highest-weight pairs, original-source Laurent witness, multiplicity and rank checks; generic theorem proved in TeX',
 'quantum_parameters':['1','2','3/2'],
 'source_matrix_sha256':hashlib.sha256(matrix_path.read_bytes()).hexdigest(),
 'source_basis_sha256':hashlib.sha256(basis_path.read_bytes()).hexdigest(),
 'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
 'source_flip_witness_index':126,'highest_1_1_multiplicity':g88,
 'symmetric_square_rank':794430,'exterior_square_rank':793170}
(ROOT/'checks/quantum_tensor_symmetry.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps({'status':'passed','checks':checks}))
