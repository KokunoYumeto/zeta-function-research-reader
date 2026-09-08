"""Independent exact audit of the tensor commutors; no author checker import.

Finite rational substitutions validate all source ratio-weight pairs.  The
generic-q proof is reviewed separately; substitutions are not claimed to
prove a rational-function identity.  The small-braid subaudit is symbolic.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import factorial
from pathlib import Path
import hashlib
import json
import argparse
from collections import Counter

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
COUNT = 0

def require(value, label):
    global COUNT
    COUNT += 1
    if not value:
        raise AssertionError(label)

@lru_cache(None)
def qi(n, q):
    if n < 0:
        return -qi(-n, q)
    return sum((q**(n - 1 - 2*k) for k in range(n)), F(0))

def clean(v):
    return {key: val for key, val in v.items() if val}

def scaled(v, a):
    return clean({key: a*val for key, val in v.items()})

def add(out, key, val):
    out[key] = out.get(key, F(0)) + val

def action(v, m, n, q, which):
    out = {}
    for (i, j), val in v.items():
        if which == 'F':
            if i < m:
                add(out, (i+1,j), val*qi(i+1,q))
            if j < n:
                add(out, (i,j+1), val*q**(m-2*i)*qi(j+1,q))
        elif which == 'E':
            if i:
                add(out, (i-1,j), val*qi(m-i+1,q)*q**(-n+2*j))
            if j:
                add(out, (i,j-1), val*qi(n-j+1,q))
        elif which == 'K':
            add(out, (i,j), val*q**(m+n-2*i-2*j))
        else:
            raise ValueError(which)
    return clean(out)

def gamma(m,n,r):
    return F((-1)**r*factorial(n)*factorial(m-r),
             factorial(n-r)*factorial(m))

@lru_cache(None)
def strings(m,n,q):
    out = {}
    for r in range(min(m,n)+1):
        z = {}
        for i in range(r+1):
            a = F((-1)**i)*q**(i*(n-2*r+i+1))
            for j in range(i):
                a *= qi(n-r+j+1,q)/qi(m-j,q)
            z[i,r-i] = a
        h = m+n-2*r
        require(not action(z,m,n,q,'E'), ('highest',m,n,q,r))
        require(z.get((0,r)) == 1, ('nonzero highest',m,n,q,r))
        w = z
        for s in range(h+1):
            require(bool(w), ('nonzero string',m,n,q,r,s))
            out[r,s] = w
            require(action(w,m,n,q,'K') == scaled(w,q**(h-2*s)),
                    ('weight',m,n,q,r,s))
            require(action(w,m,n,q,'E') == (
                scaled(out[r,s-1],qi(h-s+1,q)) if s else {}),
                    ('raising',m,n,q,r,s))
            w = scaled(action(w,m,n,q,'F'), 1/qi(s+1,q))
        require(not w, ('terminal lowering',m,n,q,r))
        require(gamma(m,n,r)*gamma(n,m,r) == 1,
                ('gamma inverse',m,n,r))
    require(len(out) == (m+1)*(n+1), ('dimension',m,n,q))
    return out

def inverse(mat):
    n = len(mat)
    a = [list(row)+[F(i==j) for j in range(n)]
         for i,row in enumerate(mat)]
    for j in range(n):
        pivot = next((i for i in range(j,n) if a[i][j]), None)
        require(pivot is not None, ('invertible weight block',n,j))
        a[j],a[pivot] = a[pivot],a[j]
        v = a[j][j]
        a[j] = [x/v for x in a[j]]
        for i in range(n):
            if i != j and a[i][j]:
                v = a[i][j]
                a[i] = [x-v*y for x,y in zip(a[i],a[j])]
    require(all(a[i][j] == F(i==j) for i in range(n) for j in range(n)),
            ('left inverse elimination',n))
    ans = [row[n:] for row in a]
    require(all(sum(mat[i][k]*ans[k][j] for k in range(n)) == F(i==j)
                for i in range(n) for j in range(n)), ('right inverse',n))
    return ans

@lru_cache(None)
def commutor(m,n,q):
    ws = strings(m,n,q)
    wt = strings(n,m,q)
    out = {}
    for k in range(m+n+1):
        coords = [(i,k-i) for i in range(m+1) if 0<=k-i<=n]
        labels = [(r,s) for r,s in ws if r+s == k]
        require(len(coords) == len(labels), ('weight dimension',m,n,k))
        mat = [[ws[label].get(coord,F(0)) for label in labels]
               for coord in coords]
        inv = inverse(mat)
        for j,coord in enumerate(coords):
            v = {}
            for l,(r,s) in enumerate(labels):
                for target,val in wt[r,s].items():
                    add(v,target, val*gamma(m,n,r)*inv[l][j])
            out[coord] = clean(v)
    return out

def map_apply(v, mat):
    out = {}
    for coord,val in v.items():
        for target,coeff in mat[coord].items():
            add(out,target,val*coeff)
    return clean(out)

def audit(m,n,q):
    J = commutor(m,n,q)
    Ji = commutor(n,m,q)
    for coord,v in J.items():
        basic = {coord:F(1)}
        require(map_apply(v,Ji) == basic, ('commutor inverse',m,n,q,coord))
        for op in ['E','F','K']:
            require(action(v,n,m,q,op) == map_apply(action(basic,m,n,q,op),J),
                    ('original-coordinate intertwining',m,n,q,coord,op))
        if q == 1:
            require(v == {(coord[1],coord[0]):F(1)},
                    ('actual flip specialization',m,n,coord))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--observe-source', action='store_true',
                        help='Require and revalidate the full archived primary source.')
    args = parser.parse_args()
    ranges = [
        (F(1),range(10)), (F(2),range(10)),
        (F(3,2),[1,3,5,7,9]),
    ]
    cases = []
    for q,domain in ranges:
        for m in domain:
            for n in domain:
                audit(m,n,q)
                cases.append([m,n,str(q)])
    require(1260*1261//2 == 794430, 'symmetric rank')
    require(1260*1259//2 == 793170, 'exterior rank')
    require(794430+793170 == 1260**2, 'full tensor dimension')
    g = [[0,0,1,1,1],[0,1,2,3,2],[1,2,4,4,3],
         [1,3,4,4,2],[1,2,3,2,1]]
    ns = [9,7,5,3,1]
    require(sum(g[i][j]*(ns[i]+1)*(ns[j]+1)
                for i in range(5) for j in range(5)) == 1260,
            'full-source decomposition dimension')
    require(g[4][4] == 1, 'rank-one detecting sector')
    basis_path = ROOT/'agents/full_source_generators/source_basis/basis_1260.json'
    matrices_path = ROOT/'agents/full_source_generators/full_generators.json'
    basis_data = json.loads(basis_path.read_text(encoding='utf-8'))
    basis = basis_data['basis']
    matrices = json.loads(matrices_path.read_text(encoding='utf-8'))['matrices']
    require(basis_data['retained_labels']['T']['basis_index'] == 126,
            'original retained T index')
    require(basis[126]['weight_V'] == [12,3], 'original T ratio weight nine')
    require(not matrices['EV'][126], 'original Laurent E_V T is zero')
    ef = {}
    v = matrices['FV'][126]
    require(bool(v), 'original Laurent F_V T nonzero')
    for row,coefficients in v:
        for row2,coefficients2 in matrices['EV'][row]:
            for exp,c in coefficients:
                for exp2,c2 in coefficients2:
                    add(ef,(row2,exp+exp2),c*c2)
    ef = clean(ef)
    require(ef == {(126,k):1 for k in range(-8,9,2)},
            'original Laurent E_V F_V T exactly [9]T')
    require(any(sum(c for exp,c in coefficients) for row,coefficients in v),
            'original lowering nonzero after q=1')
    for row,coefficients in v:
        require(basis[row]['weight_V'] == [11,4], 'lowered source weight')
    weights = Counter((b['weight_V'][0],b['weight_W'][0]) for b in basis)
    for i,a in enumerate([12,11,10,9,8]):
        for j,b in enumerate([12,11,10,9,8]):
            require(weights[a,b]-weights[a+1,b]-weights[a,b+1]+weights[a+1,b+1]
                    == g[i][j], ('source weight finite difference',a,b))
    require(all(sum(b['weight_V']) == sum(b['weight_W']) == 15 for b in basis),
            'both original central degrees fifteen')
    proof = ROOT/'tex/quantum_tensor_symmetry.tex'
    hash_file = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    transcript_path = HERE/'source_coproduct_transcript.json'
    transcript = json.loads(transcript_path.read_text(encoding='utf-8'))
    require(transcript['source_sha256'] == '5c5b990306c3b817d822df9f5088fdd42dda146fc3449155a0b2f6202d2ed49e',
            'observed primary source hash provenance')
    require(transcript['line_start'] == 1767 and transcript['line_end'] == 1769,
            'observed primary equation location')
    require(transcript['lines'][0] == r'\be \label{e U_q coproduct}',
            'observed primary coproduct label')
    equation = transcript['lines'][1]
    require(r'\Delta(E_i) = E_i \tsr K_i^{-1} + 1 \tsr E_i' in equation,
            'original source E coproduct line 1768')
    require(r'\Delta(F_i) = F_i \tsr 1 + K_i \tsr F_i' in equation,
            'original source F coproduct line 1768')
    if args.observe_source:
        primary = ROOT/transcript['source_relative_path']
        require(hash_file(primary) == transcript['source_sha256'],
                'reobserved complete primary source hash')
        primary_lines = primary.read_text(encoding='utf-8').splitlines()
        require(primary_lines[transcript['line_start']-1:transcript['line_end']] == transcript['lines'],
                'reobserved exact primary source excerpt')
    report = {
        'status':'passed','checks':COUNT,'cases':cases,
        'scope':'Exact rational coefficient calculations, all m,n=0..9 at q=1,2; all original odd ratio weights at q=3/2. Proof review supplies generic-q claims; symbolic small-braid checker is separate.',
        'proof_sha256':hash_file(proof),
        'primary_source_sha256':transcript['source_sha256'],
        'primary_coproduct_transcript_sha256':hash_file(transcript_path),
        'source_observation_mode':'reobserved full archived source' if args.observe_source else 'replayed exact observed transcript; full shelf not required',
        'character_proof_sha256':hash_file(ROOT/'tex/character_decomposition.tex'),
        'full_generators_sha256':hash_file(matrices_path),
        'full_basis_sha256':hash_file(basis_path),
        'checker_sha256':hash_file(Path(__file__)),
        'findings':[],
    }
    (HERE/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'passed','checks':COUNT,'cases':len(cases)}))

if __name__ == '__main__':
    main()
