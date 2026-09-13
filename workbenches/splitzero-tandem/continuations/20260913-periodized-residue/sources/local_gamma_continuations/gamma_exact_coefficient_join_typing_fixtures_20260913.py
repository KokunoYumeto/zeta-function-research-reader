"""Independent finite algebra/metric fixtures; no selected-zero certification."""
import hashlib
import json
from pathlib import Path
import sympy as sp

S, u, z, s1, s2, s3 = sp.symbols('S u z s1 s2 s3')
checks = []

def check(name, actual, expected):
    delta = actual - expected
    ok = all(sp.simplify(x) == 0 for x in delta) if isinstance(delta, sp.MatrixBase) else sp.simplify(delta) == 0
    checks.append({'name': name, 'pass': bool(ok)})
    if not ok:
        raise RuntimeError(name + ': ' + str(delta))

# Gamma lambda=1/2, k=2 has full reference transform sec(theta)^2.
# Positive one-factor multiplier 1+t^2 has transform 2 sec(theta)^3;
# its literal two-factor sum transform is 4 sec(theta)^6, mass four.
N, q, c = 3, 2, sp.Integer(1)
chi = (S-c)**2 - 2
reference_series = sp.series(sp.sec(z)**2, z, 0, 14).removeO().expand()
changed_series = sp.series(4*sp.sec(z)**6, z, 0, 14).removeO().expand()
moments = lambda series: [sp.factorial(j)*series.coeff(z, j) for j in range(14)]
refmom, chmom = moments(reference_series), moments(changed_series)
L = sp.Matrix(N+1, N+1, lambda a,j: sp.binomial(j,a)*c**(j-a)*sp.I**a if a<=j else 0)
Href = sp.Matrix(N+1, N+1, lambda i,j: refmom[i+j])
Hch = sp.Matrix(N+1, N+1, lambda i,j: chmom[i+j])
Mr, Mh = L.conjugate().T*Href*L, L.conjugate().T*Hch*L
check('unchanged S-coordinate phase determinant', L.det(), sp.I**(N*(N+1)//2))
check('original S source determinant equals u determinant', Mh.det(), Hch.det())
check('original c translation retained in offdiagonal', Mh[0,1], 4)
check('literal two-factor changed mass retained', Mh[0,0], 4)

def integral(poly, mom):
    p=sp.Poly(sp.expand(poly),u)
    return sp.expand(sum(v*mom[e[0]] for e,v in p.terms()))

for i in range(N+1):
    for j in range(N+1):
        check(f'original integrand congruence {i},{j}', Mh[i,j], integral((c-sp.I*u)**i*(c+sp.I*u)**j,chmom))

B=sp.Matrix(N+1,N-q+1, lambda i,j: sp.expand(chi*S**j).coeff(S,i))
J=sp.Matrix(q,N+1,lambda i,j: sp.rem(S**j,chi,S).coeff(S,i))
Gr=(J*Mr.inv()*J.conjugate().T).inv()
Gh=(J*Mh.inv()*J.conjugate().T).inv()
Rr=Mr.inv()*J.conjugate().T*Gr
Rh=Mh.inv()*J.conjugate().T*Gh
K=(B.conjugate().T*Mh*B).inv()*B.conjugate().T*Mh*Rr
check('original multiplication columns killed by quotient', J*B, sp.zeros(q,N-q+1))
check('reference minimum section is right inverse', J*Rr, sp.eye(q))
check('arithmetic minimum section is right inverse', J*Rh, sp.eye(q))
check('section difference with original negative sign', Rh-Rr, -B*K)
check('arithmetic orthogonality of corrected section', B.conjugate().T*Mh*(Rr-B*K), sp.zeros(N-q+1,q))
check('quotient determinant source/relation ratio', Gh.det(), Mh.det()/(B.conjugate().T*Mh*B).det())
Qfirst=sp.Matrix.hstack(sp.eye(N+1)[:,:q],B)
check('quotient-first orientation determinant', Qfirst.det(),1)
wrong_sign = sp.simplify(Rh-Rr-B*K) != sp.zeros(N+1,q)
if not wrong_sign:
    raise RuntimeError('Fixture does not reject reversed section sign')

# Endpoint N=q-1 has no multiplication columns and unique representatives.
Me=Mh[:q,:q]
Je=sp.eye(q)
Ge=(Je*Me.inv()*Je.T).inv()
check('endpoint quotient equals original source Gram',Ge,Me)
check('endpoint section independent of source metric',Me.inv()*Je.T*Ge,sp.eye(q))

# Cochain division is tested in a nonreduced algebra with collisions.
h=lambda s: (s-1)**2*(s-2)
ann=(S-2)**3*(S-3)**2*(S-4)
rem=sp.expand(ann.subs(S,s1+s2))
quotients=[]
for si in (s1,s2):
    qi,rem=sp.div(rem,h(si),si)
    quotients.append(qi)
check('successive monic divisions final tensor remainder',rem,0)
check('literal two-factor ideal relation',sum(h(si)*qi for si,qi in zip((s1,s2),quotients)),ann.subs(S,s1+s2))
comp=sp.Matrix(3,3,lambda i,j: sp.rem(S**(j+1),h(S),S).coeff(S,i))
a=sp.kronecker_product(comp,sp.eye(3))+sp.kronecker_product(sp.eye(3),comp)
identity=sp.eye(9)
ann_a=sp.zeros(9)
for (e,),coeff in sp.Poly(ann,S).terms(): ann_a+=coeff*a**e
check('cyclic annihilator retains all nilpotent powers',ann_a,sp.zeros(9))
unit=sp.Matrix([1,0,0])
tensorunit=sp.kronecker_product(unit,unit)
krylov=sp.Matrix.hstack(*(a**j*tensorunit for j in range(6)))
check('six original sum powers remain independent',krylov.rank(),6)
upsilon=2*sp.eye(3)+comp
check('complete local unit multiplication invertible',upsilon.det(),36)
mapped=sp.kronecker_product(upsilon,upsilon)*krylov
check('arithmetic unit multiplication preserves cyclic injection',mapped.rank(),6)

# Three factors expose both alternating signs, including middle degree.
chi3=(S-3)**4
rest=sp.expand(chi3.subs(S,s1+s2+s3)); q3=[]
for si in (s1,s2,s3):
    qi,rest=sp.div(rest,(si-1)**2,si);q3.append(qi)
check('three-factor division remainder',rest,0)
boundary=sum((-1)**i*(-1)**i*(si-1)**2*qi for i,(si,qi) in enumerate(zip((s1,s2,s3),q3)))
check('three-factor cochain signs cancel exactly',boundary,chi3.subs(S,s1+s2+s3))
wrong_boundary=sum((-1)**i*(si-1)**2*qi for i,(si,qi) in enumerate(zip((s1,s2,s3),q3)))
if sp.expand(wrong_boundary-boundary)==0:
    raise RuntimeError('Fixture does not reject unsigned primitive')

out={'scope':'Independent exact finite algebra and positive-measure fixtures; the fixture centres are not asserted zeta zeros.',
     'source':str(Path(__file__).name),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'checks':checks,'count':len(checks),'all_pass':all(c['pass'] for c in checks),
     'negative_controls':{'reversed_section_correction_sign_rejected':bool(wrong_sign),'unsigned_three_factor_primitive_rejected':True},
     'metric_fixture':{'k':2,'lambda':'1/2','c':'1','N':3,'chi':'(S-1)^2-2','reference_transform':'sec(theta)^2','changed_transform':'4 sec(theta)^6','K':str(K)}}
print(json.dumps(out,indent=2))
