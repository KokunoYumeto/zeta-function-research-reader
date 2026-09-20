"""Exact CRT, residue, full family and lower-block inverse verification."""
from pathlib import Path
import hashlib,json
import sympy as s
B=Path(__file__).resolve().parent
A,k,d,x=s.symbols('A k d x',nonzero=True)
kap=k*k-d*d; aa=k*k+d*d
f=(x-k)**2*(x*x-d*d);h=A*f
checks=[]
def zero(name,expr):
    vec=list(expr) if isinstance(expr,s.MatrixBase) else [expr]
    bad=[s.cancel(s.expand(v)) for v in vec if s.cancel(s.expand(v))!=0]
    if bad:raise ArithmeticError((name,bad[:2]))
    checks.append({'name':name,'entries':len(vec),'passed':True})
    print(name+': PASS',flush=True)
domain=s.QQ.frac_field(A,k,d)
hp=s.Poly(h,x,domain=domain)
def rem(q):return s.Poly(s.expand(q),x,domain=domain).rem(hp).as_expr()
eU=(x*x-d*d)*(3*k*k-d*d-2*k*x)/kap**2
eL=(x-k)**2*(aa+2*k*x)/kap**2
zero('Full projector sum',eU+eL-1)
zero('Upper projector idempotence',rem(eU*eU-eU))
zero('Lower projector idempotence',rem(eL*eL-eL))
zero('Projector orthogonality',rem(eU*eL))
PU=s.Matrix([[d*d*(d*d-3*k*k),k*d*d*kap],[2*k*d*d,-d*d*kap],
             [3*k*k-d*d,-k*kap],[-2*k,kap]])/kap**2
PL=s.Matrix([[k*k*aa,2*k**3*d*d],[-2*k*d*d,k*k*(k*k-3*d*d)],
             [d*d-3*k*k,-2*k**3],[2*k,aa]])/kap**2
inverse=s.Matrix([[1,k,k*k,k**3],[0,1,2*k,3*k*k],[1,0,d*d,0],[0,1,0,d*d]])
for name,P,polys in [('upper',PU,[eU,eU*(x-k)]),('lower',PL,[eL,eL*x])]:
    for j,q in enumerate(polys):
        zero(name+f' full inclusion column {j}',sum(P[i,j]*x**i for i in range(4))-rem(q))
zero('Both full CRT inverse products',s.diag(inverse*PU.row_join(PL)-s.eye(4),PU.row_join(PL)*inverse-s.eye(4)))
zero('Exact CRT determinant',inverse.det()-kap**2)
eps=s.symbols('eps')
zero('Full upper derivative',s.rem(s.expand(s.diff(h,x).subs(x,k+eps)),eps**2,eps)-2*A*kap*eps)
u=2*A*aa;v=-4*A*k*d*d
zero('Full lower derivative',s.rem(s.diff(h,x),x*x-d*d,x)-u*x-v)
lam=lambda q:s.Poly(rem(q),x).nth(3)/A
zero('Upper residue constant',lam(eU)+2*k/(A*kap**2))
zero('Upper residue linear term',lam(eU*(x-k))-1/(A*kap))
zero('Lower residue constant',lam(eL)-2*k/(A*kap**2))
zero('Lower residue linear term',lam(eL*x)-aa/(A*kap**2))
J=s.Matrix([[2*k,aa],[aa,2*k*d*d]])/(A*kap**2)
BL=s.zeros(4);BL[:2,2:]=J;BL[2:,:2]=J
zero('Full lower residue determinant',BL.det()-1/(A**4*kap**4))
X=s.Matrix([[0,d*d],[1,0]]);H=u*X+v*s.eye(2);DD=-4*A*A*d*d*kap**2
Hi=(v*s.eye(2)-u*X)/DD
Hii=((v*v+u*u*d*d)*s.eye(2)-2*u*v*X)/DD**2
zero('Both lower derivative inverse products',s.diag(H*Hi-s.eye(2),Hi*H-s.eye(2)))
zero('Full squared derivative inverse',Hii-Hi*Hi)
theta=s.zeros(4);theta[:2,2:]=2*H*H;theta[2:,:2]=2*H
thetai=s.zeros(4);thetai[:2,2:]=Hi/2;thetai[2:,:2]=Hii/2
zero('Both full lower inverse products',s.diag(theta*thetai-s.eye(4),thetai*theta-s.eye(4)))
TL=s.diag(s.Matrix([[4,0],[0,4*d*d]]),s.Matrix([[4*v,4*u*d*d],[4*u*d*d,4*v*d*d]]))
zero('Complete lower trace factorization',BL*theta-TL)
zero('Full lower multiplier determinant',theta.det()+1024*A**6*d**6*kap**6)
zero('Full lower trace determinant',TL.det()+1024*A**2*d**6*kap**2)
gamma=s.symbols('gamma',positive=True)
N=s.Matrix([[0,0],[1,0]])
KL=s.zeros(4);KL[:2,2:]=N/(8*gamma**2);KL[2:,:2]=(s.eye(2)-2*s.I*N/gamma)/(32*gamma**4)
limit=(d*d*thetai).applyfunc(s.cancel).subs(d,0).subs({A:-s.Rational(1,2),k:2*s.I*gamma})
zero('Full endpoint inverse coefficient',limit-KL)
theta_endpoint=s.BlockMatrix([[s.zeros(2),s.zeros(2)],[8*gamma**2*N,s.zeros(2)]]).as_explicit()
zero('Full endpoint forward map',theta.subs(d,0).subs({A:-s.Rational(1,2),k:2*s.I*gamma})-theta_endpoint)
assert KL.rank()==3
checks.append({'name':'Endpoint inverse rank three','entries':1,'passed':True})
p,z,r=s.symbols('p z r',real=True);tau=1-z
alpha=p*tau+z*(s.Rational(1,2)+s.I*gamma)
beta=2*p*tau/5+z*(s.Rational(1,2)-s.I*gamma)
chi=2*p*tau+z*(s.Rational(1,2)-s.I*gamma)
SS=22*p*tau/5+2*z
zero('Retained cubic coefficient sum',2*alpha+beta+chi-SS)
hz=-(r-alpha)**2*(r-beta)*(r-chi)/SS
zero('Complete ES endpoint',hz.subs(z,0)+5*(r-p)**2*(r-2*p/5)*(r-2*p)/(22*p))
zero('Complete paired-quartet endpoint',hz.subs(z,1)+((r-s.Rational(1,2))**2+gamma**2)**2/2)
zero('Original reciprocal ES identity',4/p-1/p-1/(2*p/5)-1/(2*p))
for sign in [-1,1]:
    zero(f'Lower signed derivative formula {sign}',s.diff(h,x).subs(x,sign*d)-2*A*sign*d*(sign*d-k)**2)
c,gE,g1E=s.symbols('c gE g1E',nonzero=True)
gU=gE/c**2;g1U=s.symbols('g1U')
unitlinear=g1E/gE-g1U/gU
zero('Exact residue unit constant test',c*(-g1U/gU**2)-c**3*(-g1E/gE**2+unitlinear/gE))
zero('Exact residue unit linear test',c/gU-c**3/gE)
for j in [1,2,3]:
    Z=s.Matrix([[j,1+s.I],[s.I,2]])
    G=Z.H*Z+s.eye(2);Gam=s.diag(G,G);K=KL.subs(gamma,j)
    L=Gam.inv()*K.H*Gam*K
    coeff=L.charpoly().all_coeffs()
    eta2=64*j**4*G[1,1]*G.inv()[0,0]
    zero(f'Original complex metric {j}: exact product of constants',-coeff[3]/eta2-s.Rational(1,2**32*j**24))
    zero(f'Original complex metric {j}: exact zero spectral factor',coeff[4])
source=B/'ES_RH_TOTAL_FAMILY_ROOT_BODY.tex'
data={'result':'PASS','groups':len(checks),'entries':sum(c['entries'] for c in checks),
      'checks':checks,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
      'scope':'Algebraic identities and exact complex-metric invariants. Positivity, flatness, parameter-domain claims and limits are proved in the TeX.'}
(B/'ES_RH_TOTAL_FAMILY_CERTIFICATE.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in data.items() if k!='checks'},indent=2))
