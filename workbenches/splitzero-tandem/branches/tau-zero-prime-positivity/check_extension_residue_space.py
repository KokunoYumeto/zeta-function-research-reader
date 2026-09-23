"""Exact finite module checks for the coefficient-three extension calculations."""
from itertools import product
from pathlib import Path
import json
P=Path(__file__).resolve().parent
count=0
def ck(p):
    global count
    assert p
    count+=1
def N(a,b):return (a%3,b%9)
def addN(a,b):return N(a[0]+b[0],a[1]+b[1])
def scaleN(k,a):return N(k*a[0],k*a[1])
def epsN(a):return N(0,-3*a[1])
def TN(a):return N(0,-3*a[0])
ns=list(product(range(3),range(9)))
hom=[(n,m) for n in ns for m in ns if epsN(n)==scaleN(3,m) and epsN(m)==(0,0)]
ck(len(hom)==81)
def coord(pair):
    n,m=pair
    ck(n[1]%3==0 and m[1]%3==0)
    return n[0],m[0],((n[1]+m[1])//3)%3
classes={coord(p) for p in hom}
ck(len(classes)==27)
for n,m in hom:
    for k in ns:
        changed=(addN(n,scaleN(3,k)),addN(m,epsN(k)))
        ck(coord(changed)==coord((n,m)))
    A,B,W=coord((n,m))
    ck(coord((TN(n),TN(m)))==(0,0,(-A-B)%3))
    z=addN(n,m)
    ck(z==N(A+B,3*W))
# The explicit middle modules retain the original a,b,u,Tu coordinates.
for A,B,W in sorted(classes):
    def red(v):
        a,b,u,vv=v
        qu,ru=divmod(u,3)
        qv,rv=divmod(vv,3)
        return ((a+A*qu)%3,(b+3*W*qu-3*A*qv)%9,ru,rv)
    def add(v,w):return red(tuple(x+y for x,y in zip(v,w)))
    def scale(k,v):return red(tuple(k*x for x in v))
    def epsilon(v):
        a,b,u,vv=v
        return red((B*u,-3*b-3*B*vv,0,0))
    def T(v):
        a,b,u,vv=v
        return red((0,-3*a,0,u))
    def rho(v):
        # psi(v)=u + vv*T; rho(1)=(A+B)a+3Wb.
        a,b,u,vv=v
        z=addN(scaleN(u,N(A+B,3*W)),scaleN(vv,N(0,-3*(A+B))))
        return red((z[0],z[1],0,0))
    ms=list(product(range(3),range(9),range(3),range(3)))
    ck(len(ms)==243)
    epsimage=set()
    tripleimage=set()
    for v in ms:
        ck(red(v)==v)
        ev=epsilon(v)
        ck(epsilon(ev)==(0,0,0,0))
        ck(T(T(v))==scale(6,ev))
        ck(T(ev)==epsilon(T(v)))
        ck(rho(v)==add(scale(3,v),ev))
        # 8 inverse is 8 on these exponent-nine middle modules.
        fv=scale(8,add(scale(3,v),scale(-1,rho(v))))
        ck(fv==scale(-8,ev))
        ck(scale(5,fv)==scale(-40,ev))
        epsimage.add(ev);tripleimage.add(scale(3,v))
    ck(len(epsimage)==(3 if B==0 else 9))
    ck(len(tripleimage)==(3 if A==0 else 9))
    # canonical rho is an isomorphism exactly when A+B is nonzero
    rim={rho((0,0,u,v)) for u,v in product(range(3),repeat=2)}
    ck(len(rim)==(9 if (A+B)%3 else (3 if W else 1)))
report={'status':'passed','count':count,'extension_classes':27,'relation_homomorphisms':81,
 'middle_module_size':243,'scope':'Exact finite quotient checks. Full module and Ext proofs remain in the accompanying mathematical source; no positivity interpretation in characteristic three.'}
(P/'EXTENSION_RESIDUE_SPACE_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report))
