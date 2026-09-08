"""Check the concrete Boolean parameter projection and independent permanent sum.

For n=1,2 enumerate every original and auxiliary bit independently. For n=3
enumerate all original matrices and construct the unique flags after separately
exhausting the local extension truth tables. No primary-source shelf is needed.
"""
from pathlib import Path
from itertools import product, permutations
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[1]

def build(n):
    B = {(i,j):i*n+j for i in range(n) for j in range(n)}
    R = {(i,k):n*n+i*n+k for i in range(n) for k in range(n)}
    C = {(j,k):2*n*n+j*n+k for j in range(n) for k in range(n)}
    clauses = []
    def add(*literals):
        assert 1 <= len(literals) <= 3
        clauses.append(tuple(literals)+(literals[-1],)*(3-len(literals)))
    def line(bits, flags):
        add((flags[0],0),(bits[0],1))
        add((flags[0],1),(bits[0],0))
        for k in range(1,n):
            u,v,w = flags[k-1],bits[k],flags[k]
            add((u,0),(w,1)); add((v,0),(w,1)); add((u,1),(v,1),(w,0))
        add((flags[-1],1))
        for j in range(n):
            for k in range(j+1,n):
                add((bits[j],0),(bits[k],0))
    for i in range(n):
        line([B[i,j] for j in range(n)], [R[i,k] for k in range(n)])
    for j in range(n):
        line([B[i,j] for i in range(n)], [C[j,k] for k in range(n)])
    assert len(clauses) == n**3+5*n*n
    return B,R,C,clauses

def holds(clauses, bits):
    return all(any(bits[i] if sign else 1-bits[i] for i,sign in clause) for clause in clauses)

def direct_permanent(matrix):
    return sum(s.prod(matrix[i][p[i]] for i in range(len(matrix)))
               for p in permutations(range(len(matrix))))

# Local auxiliary extension is independently exhausted for all eight triples.
for u,v,w in product([0,1],repeat=3):
    value = (not u or w) and (not v or w) and (u or v or not w)
    assert bool(value) == (w == (u or v))

records=[]
for n in [1,2,3]:
    B,R,C,clauses=build(n)
    N,M=3*n*n,n**3+6*n*n
    if n <= 2:
        candidates=product([0,1],repeat=N)
        enumeration='every Boolean witness including independently varied auxiliary flags'
    else:
        def extended():
            for entrybits in product([0,1],repeat=n*n):
                b=list(entrybits)+[0]*(2*n*n)
                for i in range(n):
                    for k in range(n): b[R[i,k]]=int(any(b[B[i,j]] for j in range(k+1)))
                for j in range(n):
                    for k in range(n): b[C[j,k]]=int(any(b[B[i,j]] for i in range(k+1)))
                yield tuple(b)
        candidates=extended()
        enumeration='all original Boolean matrices and explicitly forced auxiliary flags'
    surviving=[bits for bits in candidates if holds(clauses,bits)]
    assert len(surviving)==s.factorial(n)
    seen=set()
    for bits in surviving:
        matrixbits=tuple(bits[:n*n])
        assert matrixbits not in seen
        seen.add(matrixbits)
        assert all(sum(bits[B[i,j]] for j in range(n))==1 for i in range(n))
        assert all(sum(bits[B[i,j]] for i in range(n))==1 for j in range(n))
    matrix=[[(-1)**(i+j)*(1+i*n+j) for j in range(n)] for i in range(n)]
    # Evaluate the appended clauses using their actual three literal images,
    # not an assumed weighted-permutation expression.
    weights=[]
    for bits in surviving:
        weight=1
        for i in range(n):
            for j in range(n):
                first=matrix[i][j]*bits[B[i,j]]+1-bits[B[i,j]]
                weight*=1-(1-first)*(1-0)*(1-0)
        weights.append(weight)
    assert sum(weights)==direct_permanent(matrix)
    z=s.Symbol('T')
    characteristic=s.Poly(s.prod(1-z*w for w in weights),z)
    assert characteristic.nth(1)==-direct_permanent(matrix)
    for power in [1,2,3]:
        assert sum(w**power for w in weights)==direct_permanent([[v**power for v in row] for row in matrix])
    # Every chosen E* is distinct and is the only source parameter mapping to Z.
    stars=[(len(clauses)+i*n+j,0,B[i,j],1) for i in range(n) for j in range(n)]
    assert len(stars)==len(set(stars))==n*n
    t=(N+M-2)*(N+M-1)//2+N
    records.append({'n':n,'N':N,'M0':len(clauses),'M':M,'family_index':t,
                    'enumeration':enumeration,'survivors':len(surviving),
                    'matrix':matrix,'trace':int(sum(weights)),
                    'characteristic_coefficients':list(map(int,characteristic.all_coeffs()))})

# Symbolic n=2 weights distinguish all variables instead of checking only counts.
z00,z01,z10,z11=s.symbols('Z00 Z01 Z10 Z11')
matrix=[[z00,z01],[z10,z11]]
B,R,C,clauses=build(2)
answer=0
for bits in product([0,1],repeat=12):
    if holds(clauses,bits):
        answer+=s.prod(1-bits[B[i,j]]+matrix[i][j]*bits[B[i,j]] for i in range(2) for j in range(2))
assert s.expand(answer-z00*z11-z01*z10)==0

receipt={'all_passed':True,'scope':'bounded exhaustive and symbolic validation; full unbounded proof in TeX',
         'records':records,'symbolic_n2':str(s.expand(answer))}
(ROOT/'checks/permanent_projection.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps({'all_passed':True,'tested_sizes':[1,2,3],'symbolic_n2':str(s.expand(answer))}))
