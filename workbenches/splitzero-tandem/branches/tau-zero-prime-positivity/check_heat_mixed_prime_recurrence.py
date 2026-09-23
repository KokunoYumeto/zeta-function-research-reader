"""Exact differential-polynomial checks for the heat mixed-prime recurrence."""
from pathlib import Path
import sympy as S
import hashlib,json
P=Path(__file__).resolve().parent
u=S.symbols('u0:16')
def D(p):return S.expand(sum(S.diff(p,u[j])*u[j+1] for j in range(len(u)-1)))
def Dn(p,n):
    for _ in range(n):p=D(p)
    return p
B1=(u[2]+2*u[0]*u[1])/4
dirs=[Dn(B1,j) for j in range(13)]
p=u[0];checks=[];polys=[]
for k in range(7):
    poly=S.Poly(p,*u)
    maxdeg=poly.total_degree()
    assert maxdeg==k+1
    top=S.Add(*(c*S.prod(v**e for v,e in zip(u,mon)) for mon,c in poly.terms() if sum(mon)==k+1))
    expect=Dn(u[0]**(k+1),k)/(2**k*(k+1))
    assert S.expand(top-expect)==0
    checks.append({'order':k,'monomials':len(poly.terms()),'degree':maxdeg,'highest_degree_identity':True})
    polys.append(str(p))
    if k<6:p=S.expand(sum(S.diff(p,u[j])*dirs[j] for j in range(13)))
out={'status':'passed','orders_verified':checks,'polynomials':polys,'scope':'Finite exact checks through order 6 supplement the all-order proof.'}
src=P/'HEAT_MIXED_PRIME_RECURRENCE.md'
if src.exists():out['source_sha256']=hashlib.sha256(src.read_bytes()).hexdigest()
(P/'HEAT_MIXED_PRIME_CHECKS.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'status':'passed','orders':7,'monomial_counts':[x['monomials'] for x in checks]}))
