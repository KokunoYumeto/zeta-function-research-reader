"""Exact finite checks of integral endpoint transport. No numerical approximations."""
from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import comb, prod
from pathlib import Path
import hashlib, json

HERE=Path(__file__).resolve().parent
checks=0
def verify(assertion):
    global checks
    assert assertion
    checks+=1

def partitions(n, cap=None, length=4):
    if n==0:
        yield ()
    elif length:
        for first in range(min(n,cap or n),0,-1):
            for tail in partitions(n-first,first,length-1):
                yield (first,)+tail

def tableaux(shape, alphabet):
    cells=[(i,j) for i,row in enumerate(shape) for j in range(row)]
    lookup={c:k for k,c in enumerate(cells)}
    data=[]
    def rec(k):
        if k==len(cells):
            yield tuple(data)
            return
        i,j=cells[k]
        lower=max(data[lookup[i,j-1]] if j else 1,
                  data[lookup[i-1,j]]+1 if i else 1)
        for value in range(lower,alphabet+1):
            data.append(value)
            yield from rec(k+1)
            data.pop()
    if len(shape)<=alphabet:
        yield from rec(0)

def char(shape, weights):
    return Counter(sum(weights[x-1] for x in T) for T in tableaux(shape,len(weights)))

def add(a,b):
    out=Counter(a)
    for k,v in b.items():
        out[k]+=v
    return {k:v for k,v in out.items() if v}

def mul(a,b):
    out=Counter()
    for k,v in a.items():
        for l,w in b.items():
            out[k+l]+=v*w
    return {k:v for k,v in out.items() if v}

def power(a,n):
    out={0:1}
    for _ in range(n):
        out=mul(out,a)
    return out

def quantum(n):
    return {n-1-2*j:1 for j in range(n)}

def dimension(shape,m):
    padded=shape+(0,)*(m-len(shape))
    if len(shape)>m:
        return 0
    out=Fraction(1)
    for i in range(m):
        for j in range(i+1,m):
            out*=Fraction(padded[i]-padded[j]+j-i,j-i)
    verify(out.denominator==1)
    return out.numerator

def schur_determinant(shape,weights):
    """Independent Jacobi--Trudi polynomial, using complete symmetric DP."""
    size=len(shape)
    if not size:
        return {0:1}
    degree=shape[0]+size-1
    h=[{0:1}]+[{} for _ in range(degree)]
    for w in weights:
        for j in range(1,degree+1):
            h[j]=add(h[j],{k+w:v for k,v in h[j-1].items()})
    out={}
    for sigma in permutations(range(size)):
        sign=(-1)**sum(sigma[i]>sigma[j] for i in range(size) for j in range(i+1,size))
        term={0:sign}
        for i,j in enumerate(sigma):
            degree=shape[i]-i+j
            term=mul(term,h[degree] if degree>=0 else {})
        out=add(out,term)
    return out

def binomial_integer(n,k):
    return prod(n-j for j in range(k))//prod(range(1,k+1))

def t_expansion(poly,length):
    return [sum(v*binomial_integer(k,j) for k,v in poly.items()) for j in range(length)]

def modular_rank(matrix,p):
    a=[[x%p for x in row] for row in matrix]
    r=0
    for c in range(len(a[0]) if a else 0):
        pivot=next((i for i in range(r,len(a)) if a[i][c]),None)
        if pivot is None:
            continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=pow(a[r][c],-1,p)
        a[r]=[(x*inv)%p for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][c]:
                factor=a[i][c]
                a[i]=[(x-factor*y)%p for x,y in zip(a[i],a[r])]
        r+=1
    return r

C={10:1,4:-1,-4:-1,-10:1}
r={1:1,-1:-1}
h=mul(quantum(7),quantum(3))
verify(C==mul(power(r,2),h))
verify(C==mul({-10:1},mul({6:1,0:-1},{14:1,0:-1})))
for ell in (3,7):
    verify(any(v%ell for v in C.values()))
    verify({k:v%ell for k,v in quantum(ell).items() if v%ell}==
           {k:v%ell for k,v in power(r,ell-1).items() if v%ell})
    coeff=[comb(ell,j+1) for j in range(ell)]
    verify(coeff[0]==ell and coeff[-1]==1)
    verify(all(c%ell==0 for c in coeff[:-1]))
    verify(coeff[0]%(ell*ell)!=0)
    phi={j:1 for j in range(ell)}
    phi_minus={j:(-1)**j for j in range(ell)}
    verify(quantum(ell)==mul({1-ell:1},mul(phi,phi_minus)))

profiles={}
for n in range(8):
    for shape in partitions(n):
        profile=char(shape,[0,0,0,1])
        profiles[str(shape)]=dict(sorted(profile.items()))
        verify(sum(profile.values())==dimension(shape,4))
        verify(dict(profile)==schur_determinant(shape,[0,0,0,1]))
        padded=shape+(0,)*(4-len(shape))
        verify(min(profile)==padded[3] and max(profile)==padded[0])
        verify(profile.get(0,0)==dimension(shape,3))
        verify(4*sum(k*m for k,m in profile.items())==n*sum(profile.values()))
        branching=Counter()
        for size in range(n+1):
            for mu in partitions(size,length=3):
                mpad=mu+(0,)*(3-len(mu))
                if all(padded[i]>=mpad[i]>=padded[i+1] for i in range(3)):
                    branching[n-size]+=dimension(mu,3)
        verify(profile==branching)

original_shape=(7,5,3)
original=char(original_shape,[0,0,0,1])
verify(sum(original.values())==1260)
verify(original.get(0)==27)
verify(sum(original.values())-original.get(0)==1233)
verify(4*sum(k*m for k,m in original.items())==15*1260)
verify(dict(original)==schur_determinant(original_shape,[0,0,0,1]))
plus=sum(m for k,m in original.items() if k%2==0)
minus=sum(m for k,m in original.items() if k%2)
verify((plus,minus,plus-minus)==(615,645,-30))
x0=Fraction(3,2)
q3=x0+1
q7=x0**3+x0**2-2*x0-1
verify(q3==Fraction(5,2) and q7==Fraction(13,8))
verify(q3*q7==Fraction(65,16))
verify(-q3*q7/2==Fraction(-65,32))

nested=[]
for inner,outer in [((2,),(2,)),((1,1),(2,1)),((2,),(2,2)),((2,1),(1,1)),((1,1,1,1),(3,)),((1,1,1),(2,1))]:
    inner_weights=sorted(sum(x==4 for x in T) for T in tableaux(inner,4))
    profile=char(outer,inner_weights)
    verify(dict(profile)==schur_determinant(outer,inner_weights))
    d=len(inner_weights)
    verify(sum(profile.values())==dimension(outer,d))
    floor=sum(row*inner_weights[i] for i,row in enumerate(outer))
    ceiling=sum(row*inner_weights[d-1-i] for i,row in enumerate(outer))
    verify(min(profile)==floor and max(profile)==ceiling)
    verify(profile.get(0,0)==dimension(outer,inner_weights.count(0)))
    verify(4*sum(k*m for k,m in profile.items())==sum(inner)*sum(outer)*sum(profile.values()))
    nested.append({'inner':inner,'outer':outer,'weights':dict(sorted(profile.items())),
                   'floor':floor,'ceiling':ceiling})
verify(nested[0]['weights']=={0:21,1:18,2:12,3:3,4:1})
verify(sum(v if k%2==0 else -v for k,v in nested[0]['weights'].items())==13)

for exponent in range(1,9):
    cp=power(C,exponent)
    hp=power(h,exponent)
    rp=power(r,2*exponent)
    verify(cp==mul(rp,hp))
    verify(sum(hp.values())==21**exponent)
    jets=t_expansion(cp,max(18,8*exponent+1))
    for prime,order,lead in [(3,4*exponent,1),(7,8*exponent,pow(5,exponent,7)),
                             (5,2*exponent,pow(84,exponent,5)),(11,2*exponent,pow(84,exponent,11))]:
        verify(next(j for j,c in enumerate(jets) if c%prime)==order)
        verify(jets[order]%prime==lead)
        length=18
        matrix=[[jets[i-j] if i>=j else 0 for j in range(length)] for i in range(length)]
        verify(modular_rank(matrix,prime)==max(length-order,0))
    verify(next(j for j,c in enumerate(jets) if c)==2*exponent)
    verify(jets[2*exponent]==84**exponent)
    mod3,mod7=3**exponent,7**exponent
    e3=mod7*pow(mod7,-1,mod3)
    e7=mod3*pow(mod3,-1,mod7)
    verify((e3+e7)%(21**exponent)==1)
    verify((e3*e7)%(21**exponent)==0)

receipt={'status':'pass','checks':checks,'original_coefficient':C,
         'original_shape_profile':dict(sorted(original.items())),
         'original_shape_rank':1260,'specialized_rank':27,'specialized_defect':1233,
         'original_shape_determinant_exponent':sum(k*m for k,m in original.items()),
         'circle_inertia':[plus,minus,0],'circle_signature':plus-minus,
         'nested_profiles':nested,'small_shape_count':len(profiles),
         'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(HERE/'verification.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt))
