"""Exact finite checks for SG11--SG23. The general proofs are in the source."""
from pathlib import Path
from itertools import product
import hashlib,json
P=Path(__file__).resolve().parent
checks=0
def check(x):
    global checks
    assert x
    checks+=1
def add(x,y):return tuple((a+b)%9 for a,b in zip(x,y))
def mul(x,y):return ((x[0]*y[0])%9,(x[0]*y[1]+x[1]*y[0])%9)
def scale(k,x):return (k*x[0]%9,k*x[1]%9)
def deriv(x):return (0,6*x[1]%9) # 3/8 = 6 modulo 9
def power(x,n):
    out=(1,0)
    for _ in range(n):out=mul(out,x)
    return out
elements=list(product(range(9),repeat=2))
nil={x for x in elements if power(x,3)==(0,0)}
check(nil=={x for x in elements if x[0]%3==0})
check(len(nil)==27)
nil2={mul(x,y) for x in nil for y in nil}
check(nil2=={(0,0),(0,3),(0,6)})
check({mul(x,y) for x in nil2 for y in nil}=={(0,0)})
check({deriv(x) for x in elements}==nil2)
check({deriv(x) for x in nil}==nil2)
check({x for x in elements if x[0]%3==0}==nil) # Frobenius kernel
for x in elements:
    check(deriv(deriv(x))==(0,0))
    check(scale(3,deriv(x))==(0,0))
    for y in elements:
        check(deriv(add(x,y))==add(deriv(x),deriv(y)))
        check(deriv(mul(x,y))==add(mul(deriv(x),y),mul(x,deriv(y))))
        check(mul(x,y)[0]%3==(x[0]*y[0])%3)
# Exact map Q_N -> Nil(D): a=[epsilon] maps to -3, b=[T] maps to T.
N=list(product(range(3),range(9)))
def image(n):return (-3*n[0]%9,n[1]%9)
check({image(n) for n in N}==nil)
check(len({image(n) for n in N})==len(N))
for n in N:
    check(mul((0,1),image(n))==image((0,-3*n[0]%9)))
    check(mul((6,0),image(n))==image((0,-3*n[1]%9)))
    check(deriv(image(n))==image((0,6*n[1]%9)))
    for m in N:
        check(add(image(n),image(m))==image(((n[0]+m[0])%3,(n[1]+m[1])%9)))
proof=P/'SUPPORTED_PRISM_SPECTRUM_DERIVATION.md'
result={'status':'passed','checks':checks,'ring':'(Z/9)[T]/T^2',
    'ring_elements':81,'nilradical_elements':27,'residue_image_elements':3,
    'scope':'All ring pairs for Leibniz and addition; all nilradical elements and module maps. General integral and spectrum proofs remain in SG1--SG23.',
    'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest()}
(P/'SUPPORTED_PRISM_QUOTIENT_CHECKS.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
