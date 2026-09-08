"""Independent pathwise Laurent audit of the signed two-sheet cover.

No author implementation is imported. Every commutator is enumerated as
length-two colored paths on the original coefficient graph, retaining the
sign-sheet parity and full Laurent coefficients.
"""
from pathlib import Path
from collections import defaultdict
from hashlib import sha256
import json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
source=ROOT/'agents/full_source_generators/full_generators.json'
basis_path=ROOT/'agents/full_source_generators/source_basis/basis_1260.json'
assert sha256(source.read_bytes()).hexdigest()=='e26086722e2910dc9ffff7d57314a25e80b79bb00bfb1808a42bf97761377253'
assert sha256(basis_path.read_bytes()).hexdigest()=='77233bf1fb129fd3dd7077987f1ae2ea62619aaff1ff178432a342fa2f15b767'
data=json.loads(source.read_text())['matrices']
basis=json.loads(basis_path.read_text())['basis']
n=len(basis)

def add_product(out, key, p, q, scale):
    target=out[key]
    for e,c in p:
        for f,d in q:
            target[e+f]+=scale*c*d

def clean(out):
    return {key:{e:c for e,c in poly.items() if c} for key,poly in out.items()
            if any(poly.values())}

def quantum_integer(h):
    if h==0:
        return []
    return [(e,1 if h>0 else -1) for e in range(1-abs(h),abs(h),2)]

def sign(p):
    signs={1 if c>0 else -1 for e,c in p}
    assert len(signs)==1
    return signs.pop()

def commutator(left,right,start):
    original=defaultdict(lambda:defaultdict(int))
    cover=defaultdict(lambda:defaultdict(int))
    for first,second,scale in [(right,left,1),(left,right,-1)]:
        for mid,p in data[first][start]:
            for end,q in data[second][mid]:
                path_sign=sign(p)*sign(q)
                add_product(original,end,p,q,scale)
                add_product(cover,(end,int(path_sign<0)),p,q,scale*path_sign)
    if left[1:]==right[1:]:
        assert left.startswith('E') and right.startswith('F')
        h=basis[start]['weight_'+left[1:]][0]-basis[start]['weight_'+left[1:]][1]
        for exponent,coefficient in quantum_integer(h):
            original[start][exponent]-=coefficient
            cover[(start,0)][exponent]-=coefficient
    original=clean(original)
    cover=clean(cover)
    assert not original, (left,right,start,original)
    even={end:p for (end,sheet),p in cover.items() if sheet==0}
    odd={end:p for (end,sheet),p in cover.items() if sheet==1}
    assert even==odd, (left,right,start)
    return even

def serial(defect):
    return [[end,[[e,c] for e,c in sorted(poly.items())]]
            for end,poly in sorted(defect.items())]

relations=[]
for left,right in [('EV','FV'),('EW','FW'),('EV','EW'),('EV','FW'),('FV','EW'),('FV','FW')]:
    count=0
    first=None
    retained=None
    for start in range(n):
        defect=commutator(left,right,start)
        if defect:
            count+=1
            if first is None:
                first={'source':start,'delta':serial(defect)}
            if start==126:
                retained=serial(defect)
    relations.append({'commutator':[left,right], 'source_relation_holds_all_columns':True,
                      'cover_defect_lands_in_diagonal_kernel_all_columns':True,
                      'nonzero_plus_sheet_source_columns':count,
                      'first_nonzero':first,'T_source_delta':retained})
receipt={'status':'pass','source_sha256':sha256(source.read_bytes()).hexdigest(),
         'basis_sha256':sha256(basis_path.read_bytes()).hexdigest(),
         'relations':relations,
         'scope':'All six original Chevalley commutators, evaluated exactly by original length-two Laurent paths; cover defects retained on both sheets.'}
(HERE/'cover_verification.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'status':'pass','nonzero_defect_columns':[(r['commutator'],r['nonzero_plus_sheet_source_columns']) for r in relations]}))
