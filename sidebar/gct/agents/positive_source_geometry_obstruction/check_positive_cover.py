"""Exact original-basis sign obstruction and full positive-cover certificate.

Only the standard library is used. Laurent polynomials are sparse integer
dictionaries. All writes stay beside this script; source inputs are read only.
Default reproduction reads only the frozen matrices, basis and small preserved
source-observation receipt. --observe-source additionally observes the optional
primary-source shelf and verifies its hash and preserved bounded excerpt.
"""
from pathlib import Path
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
import hashlib
import json
import argparse

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
SOURCE=ROOT/'agents/full_source_generators'
MF=SOURCE/'full_generators.json'
BF=SOURCE/'source_basis/basis_1260.json'
SOURCE_OBSERVATION=HERE/'source_observation.json'
EXPECTED_PRIMARY='5c5b990306c3b817d822df9f5088fdd42dda146fc3449155a0b2f6202d2ed49e'
EXPECTED_M='e26086722e2910dc9ffff7d57314a25e80b79bb00bfb1808a42bf97761377253'
EXPECTED_B='77233bf1fb129fd3dd7077987f1ae2ea62619aaff1ff178432a342fa2f15b767'
checks=0
def ck(test):
    global checks
    assert test
    checks+=1
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def clean(a): return {e:c for e,c in a.items() if c}
def add(a,b,scale=1):
    out=dict(a)
    for e,c in b.items(): out[e]=out.get(e,0)+scale*c
    return clean(out)
def mul(a,b):
    out=defaultdict(int)
    for e,c in a.items():
        for f,d in b.items(): out[e+f]+=c*d
    return clean(out)
def qi(n):
    if n<0: return {e:-c for e,c in qi(-n).items()}
    return {e:1 for e in range(1-n,n,2)} if n else {}
def val(a,q): return sum((Fraction(c)*q**e for e,c in a.items()),Fraction(0))
def serial(a): return [[e,c] for e,c in sorted(a.items())]
def vadd(a,b,scale=1):
    out={i:dict(p) for i,p in a.items()}
    for i,p in b.items():
        out[i]=add(out.get(i,{}),p,scale)
        if not out[i]: del out[i]
    return out
def action(M,v):
    out={}
    for j,a in v.items():
        for i,b in M[j].items():
            out[i]=add(out.get(i,{}),mul(a,b))
            if not out[i]: del out[i]
    return out
def single(i): return {i:{0:1}}
def diag_action(v,polys): return {i:mul(p,polys[i]) for i,p in v.items() if mul(p,polys[i])}
def project(v,n):
    out={}
    for i,p in v.items():
        j=i%n
        out[j]=add(out.get(j,{}),p,1 if i<n else -1)
        if not out[j]: del out[j]
    return out
def inject(v,n): return dict(v)|{i+n:p for i,p in v.items()}

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--observe-source',action='store_true',
                    help='Additionally read the optional primary-source shelf and verify its hash and bounded excerpt.')
args=parser.parse_args()
preserved=json.loads(SOURCE_OBSERVATION.read_text(encoding='utf-8'))
assert preserved['kind']=='preserved_primary_source_observation'
assert preserved['source_sha256']==EXPECTED_PRIMARY
assert preserved['source_loci']=={
    'sign_coherence':[7240,7323],
    'prior_sign_readjustment_obstruction':[7324,7326],
    'printed_endpoint_and_paths':[7328,7350]}
for excerpt in preserved['bounded_excerpts']:
    assert hashlib.sha256(excerpt['text'].encode('utf-8')).hexdigest()==excerpt['utf8_sha256']
observation={'mode':'preserved_receipt_only','source_observed_this_run':False,
             'receipt_sha256':sha(SOURCE_OBSERVATION),
             'source_sha256_basis':'preserved source observation; optional shelf was not read'}
if args.observe_source:
    primary=ROOT/preserved['source_relative_path']
    if not primary.is_file():
        parser.error('--observe-source requires the optional primary source at '+str(primary))
    primary_bytes=primary.read_bytes()
    observed_sha=hashlib.sha256(primary_bytes).hexdigest()
    assert observed_sha==EXPECTED_PRIMARY,'Observed primary-source hash differs from the preserved source pin'
    primary_lines=primary_bytes.decode('utf-8').splitlines(keepends=True)
    for excerpt in preserved['bounded_excerpts']:
        observed=''.join(primary_lines[excerpt['first_line']-1:excerpt['last_line']])
        assert observed==excerpt['text'],'Observed bounded source excerpt differs from the preserved observation'
    observation={'mode':'live_optional_source_observation','source_observed_this_run':True,
                 'receipt_sha256':sha(SOURCE_OBSERVATION),'observed_source_sha256':observed_sha,
                 'verified_bounded_excerpt_count':len(preserved['bounded_excerpts'])}

ck(sha(MF)==EXPECTED_M)
ck(sha(BF)==EXPECTED_B)
raw=json.loads(MF.read_text(encoding='utf-8'))
basis=json.loads(BF.read_text(encoding='utf-8'))
n=basis['dimension']
ck(n==1260)
mats={name:[{i:dict(p) for i,p in col} for col in cols]
      for name,cols in raw['matrices'].items()}
ck({name:basis['retained_labels'][name]['basis_index'] for name in ['T','T1','T2','Q']}
   ==dict(T=126,T1=146,T2=8,Q=144))
alpha=add(qi(7),qi(3),-1)
beta,gamma,d,p=qi(8),qi(6),qi(3),qi(2)
C={10:1,4:-1,-4:-1,-10:1}
retained=[(126,146,alpha),(126,8,beta),(146,144,gamma),(8,144,{e:-c for e,c in d.items()})]
for j,i,a in retained: ck(mats['FV'][j][i]==a)
ck(add(mul(alpha,gamma),mul(beta,d),-1)==mul(p,C))
ck(mul(mul({1:1,-1:-1},{1:1,-1:-1}),mul(qi(7),d))==C)
for q in [Fraction(1,10),Fraction(1,2),Fraction(9,10),Fraction(1),Fraction(11,10),Fraction(2),Fraction(10)]:
    A,B,G,D,P,c=[val(a,q) for a in [alpha,beta,gamma,d,p,C]]
    ck(min(A,B,G,D,P)>0)
    ck(-A*G/(B*D)==-1-P*c/(B*D))
    ck(-A*G/(B*D)<=-1)
    ck((c==0)==(q==1))
for signs in product([-1,1],repeat=4):
    edge_signs=[signs[0]*signs[1],signs[0]*signs[2],signs[1]*signs[3],-signs[2]*signs[3]]
    ck(__import__('math').prod(edge_signs)==-1)
    ck(sum(s<0 for s in edge_signs) in [1,3])

stats={}
lifts={}
absolute={}
for name,M in mats.items():
    pos=neg=terms=total_rank=0
    lift=[{} for _ in range(2*n)]
    absM=[{} for _ in range(n)]
    for j,col in enumerate(M):
        for i,a in col.items():
            signs={1 if c>0 else -1 for c in a.values()}
            ck(len(signs)==1)
            sg=next(iter(signs))
            pos+=sg>0; neg+=sg<0; terms+=len(a)
            total_rank+=sum(abs(c) for c in a.values())
            ap={e:abs(c) for e,c in a.items()}
            absM[j][i]=ap
            for sheet in range(2):
                lift[j+sheet*n][i+(sheet^(sg<0))*n]=ap
    for j in range(2*n):
        ck(project(lift[j],n)==action(M,project(single(j),n)))
    for j in range(n):
        ck(action(lift,inject(single(j),n))==inject(absM[j],n))
    lifts[name]=lift; absolute[name]=absM
    stats[name]={'nonzero_edges':pos+neg,'positive_edges':pos,'negative_edges':neg,
                 'laurent_terms':terms,'total_absolute_monomial_rank':total_rank,
                 'lift_edges':2*(pos+neg)}

# Full original Chevalley commutators and their exact diagonal-kernel defects.
# K_V and K_W have the original ratios q^(first weight-second weight).
defects={}
for color in ['V','W']:
    E,F=mats['E'+color],mats['F'+color]
    Et,Ft=lifts['E'+color],lifts['F'+color]
    hs=[b['weight_'+color][0]-b['weight_'+color][1] for b in basis['basis']]
    hpol=[qi(h) for h in hs]
    count=0
    first=None
    retained_defect=None
    for j in range(n):
        u=single(j)
        r=vadd(vadd(action(E,action(F,u)),action(F,action(E,u)),-1),{j:hpol[j]} if hpol[j] else {},-1)
        ck(not r)
        rt=vadd(vadd(action(Et,action(Ft,u)),action(Ft,action(Et,u)),-1),{j:hpol[j]} if hpol[j] else {},-1)
        ck(not project(rt,n))
        half={i:a for i,a in rt.items() if i<n}
        ck(rt==inject(half,n))
        if half:
            count+=1
            ser=[[i,serial(a)] for i,a in sorted(half.items())]
            if first is None: first={'source':j,'delta':ser}
            if j==126: retained_defect=ser
    defects[color]={'nonzero_even_source_columns':count,'first_nonzero':first,
                    'T_source_delta':retained_defect}

# Quotient/inclusion matrices: exact integral sequence, no division by two.
for j in range(n):
    ck(not project(inject(single(j),n),n))
    ck(project(single(j),n)==single(j))

receipt={'status':'passed','checks':checks,'dimension':n,'positive_cover_dimension':2*n,
         'matrices_sha256':sha(MF),'basis_sha256':sha(BF),'primary_source_sha256':preserved['source_sha256'],
         'source_loci':preserved['source_loci'],'source_observation':observation,
         'retained_edges':[{'source':j,'target':i,'coefficient':serial(a)} for j,i,a in retained],
         'all_q_positive_proof':'Every nonzero coefficient has one coefficient sign; the four retained magnitudes are explicit nonempty positive Laurent sums. Their loop quotient is strictly negative.',
         'stats':stats,'commutator_defects':defects,
         'scope':'Integral positive cover and exact free-generator quotient. The cover is not a full quantum-group module; the explicit nonzero relation defects land in its diagonal kernel.'}
(HERE/'verification.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','checks':checks,'stats':stats,'defects':defects,
                  'source_observation':observation}))
