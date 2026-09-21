"""Exact symbolic replay of ECC1--48; does not replace the complete proof."""
from pathlib import Path
import hashlib
import json
import itertools
import sympy as s

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'ES_COLLISION_COMPLETE.tex'
RECEIVED = HERE.parent / 'defining_prime_intake_20260920' / 'DEFINING_PRIME_RECEIVED.md'
checks = []

def check(name, value, target=0):
    diff = value-target
    entries = list(diff) if isinstance(diff, s.MatrixBase) else [diff]
    reduced = [s.factor(s.cancel(v)) for v in entries]
    if any(v != 0 for v in reduced):
        raise AssertionError((name, reduced))
    checks.append({'name':name, 'scalar_entries':len(entries), 'passed':True})

def C(c):
    return s.Matrix(4,4,lambda i,j:s.binomial(j,i)*c**(j-i) if j>=i else 0)

P,w,s1,s3,R,t,A,h0,h1,q0,qt = s.symbols('P w s1 s3 R t A h0 h1 q0 qt', nonzero=True)
T,x,z = s.symbols('T x z')
g = T**3-s1*T**2+w*T-s3
rv = g.subs(T,P)
cr=s.Matrix([[1,P,P**2,P**3],[1,0,0,s3],[0,1,0,-w],[0,0,1,s1]])
base=s.Matrix([[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,0,0,0]])
cri=base+s.Matrix([-s3,w,-s1,1])*s.Matrix([[1,-1,-P,-P**2]])/rv
check('ECC4 CRT left inverse',cr*cri,s.eye(4))
check('ECC4 CRT right inverse',cri*cr,s.eye(4))
check('ECC4 signed determinant',cr.det(),-rv)

ht=h0+h1*t+t**2
k1=-(h1+t)/(h0*ht)
h=h0+h1*x+x*x
f=x*(x-t)*h
ec=h*(1/h0+k1*x)
rem=lambda p:s.rem(s.cancel(p),f,x)
check('ECC11 idempotent',rem(ec*ec-ec))
check('ECC11 local identity',s.rem(ec-1,x*(x-t),x))
check('ECC11 complementary vanishing',s.rem(ec,h,x))
check('ECC11 second inclusion column',rem(x*ec)-x*h/ht)
imat=s.Matrix([[1,0],[h1/h0+k1*h0,h0/ht],[1/h0+k1*h1,h1/ht],[k1,1/ht]])
for j,p in enumerate([ec,x*h/ht]):
    check('ECC11 complete inclusion column '+str(j),imat[:,j],s.Matrix([s.expand(p).coeff(x,k) for k in range(4)]))

a=(q0+qt)/2
b=(qt-q0)/(2*t)
sm=s.Matrix([[1,t/2,0,0],[0,0,a,t*qt/2],[0,s.Rational(1,2),0,0],[0,0,b,qt/2]])
si=s.Matrix([[1,0,-t,0],[0,0,2,0],[0,1/q0,0,-t/q0],
             [0,(1/qt-1/q0)/t,0,1/qt+1/q0]])
check('ECC9 complete signed return left',sm*si,s.eye(4))
check('ECC9 complete signed return right',si*sm,s.eye(4))
check('ECC9 determinant',sm.det(),-q0*qt/4)
q=q0+(qt-q0)*x/t
qi=1/q0+(1/qt-1/q0)*x/t
check('ECC7 retained unit inverse',s.rem(q*qi-1,x*(x-t),x))
check('ECC8 full odd return',s.rem(q.subs(x,(z*z+t)/2)*z-(a*z+b*z**3),z**4-t*t,z))
check('ECC8 quartic relation',s.rem(((z*z+t)/2)*((z*z-t)/2),z**4-t*t,z))

cz=s.Matrix([[1,0,-t,0],[0,1,0,-t],[1,0,t,0],[0,1,0,t]])
cs=s.Matrix([[1,0,0,0],[0,0,1,0],[1,t,0,0],[0,0,1,t]])
check('ECC12 literal normalization matrix',cz*sm,s.diag(1,q0,1,qt)*cs)
check('ECC12 zeta determinant',cz.det(),4*t*t)
check('ECC12 sigma determinant',cs.det(),-t*t)
check('ECC12 specialization kernel zeta2',cz.subs(t,0)*s.eye(4)[:,2],s.zeros(4,1))
check('ECC12 specialization kernel zeta3',cz.subs(t,0)*s.eye(4)[:,3],s.zeros(4,1))
eta,qbase=s.symbols('eta qbase',nonzero=True)
s0=s.Matrix([[1,0,0,0],[0,0,qbase,0],[0,s.Rational(1,2),0,0],[0,0,qbase*eta/4,qbase/2]])
conn=s.diag(0,1,s.Rational(1,2),s.Rational(3,2))
conn[3,2]=eta/2
check('ECC15 original connection residue',s0.inv()*s.diag(0,s.Rational(1,2),1,s.Rational(3,2))*s0,conn)

j=s.Matrix([[(qt**-2-q0**-2)/t,qt**-2],[qt**-2,t*qt**-2]])
ji=s.Matrix([[-t*q0**2,q0**2],[q0**2,(qt**2-q0**2)/t]])
check('ECC17 residue inverse left',j*ji,s.eye(2))
check('ECC17 residue inverse right',ji*j,s.eye(2))
check('ECC17 determinant',j.det(),-1/(q0**2*qt**2))
l1=(qt**-3-q0**-3)/t
l3=qt**-3+q0**-3
bz=s.Matrix([[0,l1,0,l3],[l1,0,l3,0],[0,l3,0,t*t*l1],[l3,0,t*t*l1,0]])
be=s.BlockMatrix([[s.zeros(2),j],[j,s.zeros(2)]]).as_explicit()
check('ECC20 full residue return',sm.T*bz*sm,be)
check('ECC20 residue determinant',bz.det(),16/(q0**6*qt**6))
cofactor=l3+l1*z*z
coinv=q0**3*qt**3*(l3-l1*z*z)/4
check('ECC19 full residue cofactor inverse',s.rem(cofactor*coinv-1,z**4-t*t,z))
check('ECC19 derivative limit',s.limit(l1.subs(qt,q0*(1+eta*t/2)),t,0),-3*eta/(2*q0**3))

a0,at=s.symbols('a0 at',nonzero=True)
hm=s.Matrix([[-t*a0,0],[a0+at,t*at]])
hi=s.Matrix([[-1/(t*a0),0],[(a0+at)/(t*t*a0*at),1/(t*at)]])
hi2=s.Matrix([[1/(t*t*a0*a0),0],[(a0+at)*(a0-at)/(t**3*a0*a0*at*at),1/(t*t*at*at)]])
check('ECC21 original odd square inverse',hm*hi,s.eye(2))
check('ECC21 inverse square',hi*hi,hi2)
theta=2*s.BlockMatrix([[s.zeros(2),hm*hm],[hm,s.zeros(2)]]).as_explicit()
thetai=s.BlockMatrix([[s.zeros(2),hi],[hi2,s.zeros(2)]]).as_explicit()/2
check('ECC21 trace inverse left',theta*thetai,s.eye(4))
check('ECC21 trace inverse right',thetai*theta,s.eye(4))
check('ECC21 trace determinant',theta.det(),-16*t**6*a0**3*at**3)
av=s.symbols('av',nonzero=True)
lim=t*t*thetai.subs({a0:av,at:av*(1+eta*t)})
lim=lim.applyfunc(lambda z:s.limit(z,t,0))
nm=s.Matrix([[0,0],[1,0]])
limtarget=s.BlockMatrix([[s.zeros(2),2*nm/av],[(s.eye(2)-2*eta*nm)/av**2,s.zeros(2)]]).as_explicit()/2
check('ECC41 all trace inverse leading entries',lim,limtarget)
check('ECC41 forward limit',theta.subs({t:0,a0:av,at:av}),s.BlockMatrix([[s.zeros(2),s.zeros(2)],[4*av*nm,s.zeros(2)]]).as_explicit())

c,d=s.symbols('c d')
check('ECC22 full shift composition',C(c)*C(d),C(c+d))
check('ECC22 inverse',C(c)*C(-c),s.eye(4))
g0,g1,g2,g3,bp=s.symbols('g0 g1 g2 g3 bp',nonzero=True)
xi=[1/g0,-g1/g0**2,g1*g1/g0**3-g2/g0**2,-g1**3/g0**4+2*g1*g2/g0**3-g3/g0**2]
ff=s.Matrix([[xi[0],xi[1],bp*xi[0]+2*xi[2],(3*bp+2)*xi[1]+6*xi[3]],
 [0,xi[0],2*xi[1],(3*bp+2)*xi[0]+6*xi[2]],[0,0,2*xi[0],6*xi[1]],[0,0,0,6*xi[0]]])
bff=s.Matrix([[g0,g1,g2-bp*g0/2,g3-bp*g1/2],[0,g0,g1,g2-(3*bp+2)*g0/6],[0,0,g0/2,g1/2],[0,0,0,g0/6]])
check('ECC25 full moment inverse left',ff*bff,s.eye(4))
check('ECC25 full moment inverse right',bff*ff,s.eye(4))

# Exact positive covariance test retaining complex cross terms. This supplements
# the universally quantified linear-algebra proof; it is not claimed exhaustive.
qr=s.Matrix([[1,s.I,0,s.Rational(1,3)],[0,2,1,s.I],[0,0,3,1+s.I],[0,0,0,4]])
hinv=qr*qr.conjugate().T
hh=hinv.inv()
pv=s.Rational(5,2)
tv=s.Rational(2,3)
v=lambda r:s.Matrix([[1,r,r*r,r**3]])
ev=s.Matrix.vstack(v(pv),(v(pv+tv)-v(pv))/tv)
jv=ev*hinv*ev.conjugate().T
ev0=s.Matrix.vstack(v(pv),s.Matrix([[0,1,2*pv,3*pv*pv]]))
jv0=ev0*hinv*ev0.conjugate().T
kv=jv0[0,0]
lv=s.factor(jv0.det()/kv)
gv0=jv0.inv()
check('ECC41 original metric constant K/L',gv0[1,1]*jv0[0,0],kv/lv)
qq=(v(pv)*qr)
qqp=ev0[1,:]*qr
wedge=sum((qq[i]*qqp[j]-qq[j]*qqp[i])*s.conjugate(qq[i]*qqp[j]-qq[j]*qqp[i]) for i in range(4) for j in range(i+1,4))
check('ECC34 complete wedge determinant',kv*lv,wedge)

sv0,svt=s.symbols('sv0 svt', nonzero=True)
om=s.Matrix.vstack(s.Matrix.hstack(v(pv),sv0*v(pv)),s.Matrix.hstack(v(pv),-sv0*v(pv)),
                  s.Matrix.hstack(v(pv+tv),svt*v(pv+tv)),s.Matrix.hstack(v(pv+tv),-svt*v(pv+tv)))
zm=s.Matrix([[s.Rational(1,2),s.Rational(1,2),0,0],[-1/(2*tv),-1/(2*tv),1/(2*tv),1/(2*tv)],
 [1/(2*sv0),-1/(2*sv0),0,0],[-1/(2*tv*sv0),1/(2*tv*sv0),1/(2*tv*svt),-1/(2*tv*svt)]])
check('ECC38 exact raw-to-jet map',zm*om,s.diag(ev,ev))
zmi=s.Matrix([[1,0,sv0,0],[1,0,-sv0,0],[1,tv,svt,tv*svt],[1,tv,-svt,-tv*svt]])
check('ECC38 full jet inverse',zm*zmi,s.eye(4))
check('ECC38 determinant squared',(zm.det())**2,1/(16*sv0**2*svt**2*tv**4))
omn=om.subs({sv0:2*s.I,svt:3})
cov=omn*s.diag(hinv,hinv)*omn.conjugate().T
right=s.diag(hinv,hinv)*omn.conjugate().T*cov.inv()
check('ECC36 entire evaluation minimum right inverse',omn*right,s.eye(4))
check('ECC36 attained full metric',right.conjugate().T*s.diag(hh,hh)*right,cov.inv())
check('ECC39 exact positive jet covariance',zm.subs({sv0:2*s.I,svt:3})*cov*zm.subs({sv0:2*s.I,svt:3}).conjugate().T,s.diag(jv,jv))
rootrows=s.Matrix.vstack(v(pv),v(pv+tv))
kk=rootrows*hinv*rootrows.conjugate().T
check('ECC37 complete raw covariance determinant',cov.det(),16*36*kk.det()**2)
un=s.Matrix([[1,1,0,0],[0,0,1,1],[1,-1,0,0],[0,0,1,-1]])/s.sqrt(2)
check('ECC32 exact signed covariance blocks',un*cov*un.conjugate().T,s.diag(2*kk,2*s.diag(2*s.I,3)*kk*s.diag(-2*s.I,3)))

kzero,kt,crr,cii,u,vv=s.symbols('kzero kt crr cii u vv',real=True)
herm=s.Matrix([[kzero,crr+s.I*cii],[crr-s.I*cii,kt]])
la=s.symbols('lambda')
check('ECC33 even characteristic polynomial',(2*herm).charpoly(la).as_expr(),la**2-2*(kzero+kt)*la+4*herm.det())
odd=s.Matrix([[u*kzero,(crr+s.I*cii)*s.sqrt(u*vv)],[(crr-s.I*cii)*s.sqrt(u*vv),vv*kt]])
check('ECC33 odd characteristic polynomial',(2*odd).charpoly(la).as_expr(),la**2-2*(u*kzero+vv*kt)*la+4*u*vv*herm.det())

# Exact collision limits of the covariance determinants in a genuinely complex
# fixed positive metric, using the full displayed ES path.
tr=s.symbols('tr',real=True)
vpair=s.Matrix.vstack(v(pv),v(pv+tr))
kpair=vpair*hinv*vpair.conjugate().T
check('ECC35 full evaluation determinant limit',s.limit(kpair.det()/tr**2,tr,0),kv*lv)
ptr=s.symbols('ptr',nonzero=True)
zt=2*ptr*(ptr+t)/(5*ptr+7*t)
aa=-(5*ptr+7*t)/(22*ptr**2+35*ptr*t+7*t*t)
hh0=-ptr**2*(3*ptr+5*t)/(5*ptr+7*t)
hh1=-zt
check('ECC44 original ES equation',1/(ptr+t)+1/(2*ptr)+1/zt,4/ptr)
check('ECC44 exact leading coefficient',aa,-1/(ptr+(ptr+t)+2*ptr+zt))
check('ECC44 original h constant',hh0,(-ptr)*(ptr-zt))
check('ECC45 original odd square at collision',(aa*hh0).subs(t,0),3*ptr/22)
check('ECC45 full cofactor derivative',(hh1/hh0).subs(t,0),2/(3*ptr))

up=s.symbols('up')
ap=2*ptr
zp=ptr*(ap*ap-up)/(4*(ap*ap-up)-2*ptr*ap)
check('ECC47 denominator-collision ES equation',2*ap/(ap*ap-up)+1/zp,4/ptr)
check('ECC47 third denominator limit',zp.subs(up,0),ptr/3)
denpoly=((T-ap)**2-up)*(T-zp)
check('ECC47 exact discriminant',s.discriminant(denpoly,T),4*up*((ap-zp)**2-up)**2)

# Signed actions on the eight individual root/sign states. These finite
# checks verify the group calculation, while ECC46--48 proves actual loops.
def signed_action(perm,bits):
    return tuple(2*perm[i]+(j^bits[i]) for i in range(4) for j in range(2))
def compose(a,b):
    return tuple(a[b[i]] for i in range(8))
generators=[]
for j in [1,2,3]:
    bits=[0,0,0,0]
    bits[0]=bits[j]=1
    generators.append(signed_action(range(4),bits))
for j,k in [(1,2),(2,3)]:
    perm=list(range(4)); perm[j],perm[k]=perm[k],perm[j]
    bits=[0,0,0,0]; bits[j]=1
    generators.append(signed_action(perm,bits))
identity=tuple(range(8))
group={identity}
todo=[identity]
while todo:
    element=todo.pop()
    for gen in generators:
        new=compose(element,gen)
        if new not in group:
            group.add(new); todo.append(new)
allowed=set()
for tail in itertools.permutations([1,2,3]):
    perm=(0,)+tail
    parity=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))%2
    for bits in itertools.product([0,1],repeat=4):
        if sum(bits)%2==parity:
            allowed.add(signed_action(perm,bits))
check('ECC48 exact monodromy group order',s.Integer(len(group)),s.Integer(48))
check('ECC48 complete allowed signed actions',s.Integer(len(group.symmetric_difference(allowed))),s.Integer(0))

certificate={
 'status':'PASS',
 'scope':'Exact symbolic identities ECC1--48, finite monodromy group and fixed complex-metric replay; analytic positivity, actual loops, all limits and universal exterior claims have full proofs in the source.',
 'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
 'received_sha256':hashlib.sha256(RECEIVED.read_bytes()).hexdigest(),
 'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'check_groups':len(checks),
 'scalar_entries':sum(x['scalar_entries'] for x in checks),
 'checks':checks,
 'sympy_version':s.__version__,
 'limitations':['No new assertion about actual conductor order or RH.',
                'Algebraic checks and one exact complex positive metric do not replace the universal metric proofs.'],
}
(HERE/'ES_COLLISION_COMPLETE.json').write_text(json.dumps(certificate,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:certificate[k] for k in ['status','check_groups','scalar_entries','source_sha256']},indent=2))
