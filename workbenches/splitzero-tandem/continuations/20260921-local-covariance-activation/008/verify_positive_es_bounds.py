"""Exhaustive bounded positive ES witness check; no numerical approximations.

The general proof is POSITIVE_ES_BOUNDARY_BODY.tex. This enumerates every
unordered positive witness for primes p=1 mod 12 up to 1201, using the exact
factor identity (a*y-p*x)(a*z-p*x)=(p*x)^2, a=4*x-p.
"""
from pathlib import Path
from fractions import Fraction
import hashlib,json
import sympy as s
B=Path(__file__).resolve().parent

def vp(n,p):
    assert n
    n=abs(n);v=0
    while n%p==0:n//=p;v+=1
    return v

counts={};first={};maxima={};total=0;nonunit=0
for p in s.primerange(13,1202):
    p=int(p)
    if p%12!=1:continue
    for x in range((p+3)//4,3*p//4+1):
        a=4*x-p;px=p*x
        # Positive sorted solutions have a*y-p*x <= p*x.
        factors=s.factorint(px)
        divisors=[1]
        for q,e in factors.items():
            divisors=[d*int(q)**j for d in divisors for j in range(2*e+1)]
        for d in divisors:
            if d>px or (d+px)%a:continue
            e=px*px//d
            if (e+px)%a:continue
            y=(d+px)//a;z=(e+px)//a
            if y<x:continue
            assert x<y<z and p not in (x,y,z)
            assert Fraction(1,x)+Fraction(1,y)+Fraction(1,z)==Fraction(4,p)
            roots=[p,x,y,z];div=[v for v in (x,y,z) if v%p==0]
            units=[v for v in (x,y,z) if v%p]
            assert len(div) in (1,2) and all(vp(v,p)==1 for v in div)
            if len(div)==1:
                xx,yy=units;Z=div[0]//p;n=vp(yy-xx,p)
                assert 4*Z>=3*p+1
                assert 32*yy<=(p+3)*(3*p+1)
                assert 32*(yy-xx)<=(p+3)*(3*p-7)
                assert n<=1
            else:
                xx=units[0];Y,Z=sorted(v//p for v in div)
                assert 2*xx<=p and 6*Y<=p+3
                assert 12*Z<=p*(p+3) and Z<p*p
                n=max(vp(div[0]-p,p),vp(div[1]-p,p),vp(div[1]-div[0],p))
                assert n<=2
            key=f'{len(div)}-divisible-gap-{n}'
            counts[key]=counts.get(key,0)+1
            first.setdefault(key,roots)
            total+=1
            if sum(roots)%p==0:nonunit+=1;continue
            bs=[sum(vp(roots[i]-roots[j],p) for j in range(4) if j!=i) for i in range(4)]
            ms=[b//2 for b in bs];eps=[b%2 for b in bs]
            branch=[3*m+e for m,e in zip(ms,eps)]
            c=len(div)
            assert 2*c>=max(branch)
            assert (c>=max(branch))==(c==1)
            maxima[key]=max(maxima.get(key,0),max(branch))
proof=B/'POSITIVE_ES_BOUNDARY_BODY.tex'
out={'status':'PASS','prime_upper_bound':1201,'complete_unordered_witnesses':total,
     'nonunit_S_witnesses':nonunit,'stratum_counts':counts,'first_witness_by_stratum':first,
     'maximum_conductor_exponent_by_stratum':maxima,
     'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest() if proof.exists() else None,
     'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'scope':'Exhaustive finite witnesses up to the stated bound; the source proves the universal inequalities.'}
(B/'POSITIVE_ES_BOUNDARY_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
