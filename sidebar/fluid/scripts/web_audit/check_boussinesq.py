# Portable adaptation of scripts/independent_boussinesq.py
# Only import/output/inventory handling changed; the delimited mathematics is a raw source byte slice.
from __future__ import annotations
from fractions import Fraction
from itertools import combinations
import sympy as s
import sympy as sp
import sympy as S
from portable_common import begin, finish
begin('boussinesq')
# BEGIN UNCHANGED MATHEMATICAL BODY
checks=[]
def check(label,expr):
 vals=list(expr) if isinstance(expr,s.MatrixBase) else [expr]
 residuals=[s.trigsimp(s.expand(v)) for v in vals]
 if any(v!=0 for v in residuals): raise AssertionError((label,residuals))
 checks.append({'label':label,'residuals':[str(v) for v in residuals]})
X,Y,tau,x,y,t=s.symbols('X Y tau x y t',real=True)
mu,v=s.symbols('mu upsilon',positive=True)
kap,nu=s.symbols('kappa_ref nu_ref',nonnegative=True)
coords=[X,Y]
u=s.Matrix([s.Function('u1')(X,Y,tau),s.Function('u2')(X,Y,tau)])
th=s.Function('theta')(X,Y,tau);p=s.Function('pressure')(X,Y,tau)
fth=s.Function('f_theta')(X,Y,tau)
fu=s.Matrix([s.Function('f1')(X,Y,tau),s.Function('f2')(X,Y,tau)])
def adv(vel,a,xx):return sum(vel[i]*s.diff(a,xx[i]) for i in range(2))
def lap(a,xx):return sum(s.diff(a,q,2) for q in xx)
def ref(a):return a.subs({X:mu*x,Y:mu*y,tau:v*t},simultaneous=True)
up=v/mu*ref(u);thp=v**2/mu*ref(th);pp=v**2/mu**2*ref(p)
er=s.diff(th,tau)+adv(u,th,coords)-kap*lap(th,coords)-fth
ep=s.diff(thp,t)+adv(up,thp,[x,y])-v/mu**2*kap*lap(thp,[x,y])-v**3/mu*ref(fth)
check('generic scalar residual intertwining',ep-v**3/mu*ref(er))
for i in range(2):
 er=s.diff(u[i],tau)+adv(u,u[i],coords)+s.diff(p,coords[i])-(th if i==1 else 0)-nu*lap(u[i],coords)-fu[i]
 ep=s.diff(up[i],t)+adv(up,up[i],[x,y])+s.diff(pp,[x,y][i])-(thp if i==1 else 0)-v/mu**2*nu*lap(up[i],[x,y])-v**2/mu*ref(fu[i])
 check('generic momentum residual component '+str(i+1),ep-v**2/mu*ref(er))
check('divergence intertwining',s.diff(up[0],x)+s.diff(up[1],y)-v*ref(s.diff(u[0],X)+s.diff(u[1],Y)))
check('curl intertwining',s.diff(up[1],x)-s.diff(up[0],y)-v*ref(s.diff(u[1],X)-s.diff(u[0],Y)))
psi=s.Function('psi')(X,Y,tau);psip=v/mu**2*ref(psi)
check('streamfunction velocity',s.Matrix([-s.diff(psip,y),s.diff(psip,x)])-v/mu*ref(s.Matrix([-s.diff(psi,Y),s.diff(psi,X)])))
check('streamfunction vorticity',lap(psip,[x,y])-v*ref(lap(psi,coords)))
for a,b in [(0,0),(2,3),(3,1)]:
 check(f'force scalar mixed derivative {a},{b}',s.diff(v**3/mu*ref(fth),x,a,t,b)-v**(3+b)*mu**(a-1)*ref(s.diff(fth,X,a,tau,b)))
J=s.Matrix([[0,-1],[1,0]])
fi,fj,ad,si,rr=s.symbols('phi_i phi_j alpha_dot s_i radius',real=True)
ei=s.Matrix([s.sin(fi),s.cos(fi)]);ej=s.Matrix([s.sin(fj),s.cos(fj)])
z=rr*ej;D=ad*J+si*(J*ei)*ei.T;zd=-D.T*z;d=fj-fi
rhod=si*s.sin(d)*s.cos(d);phid=-ad-si*s.sin(d)**2
check('one shear radial projection',(ej.T*zd)[0]-rr*rhod)
check('one shear angle projection',((J*ej).T*zd)[0]+rr*phid)
check('angle reconstruction of complete covector',zd-rr*(rhod*ej-phid*(J*ej)))
z1,z2=s.symbols('zeta1 zeta2',nonzero=True);zz=s.Matrix([z1,z2])
F=-si*ei[0]*((J*ei).T*zz)[0]/z2
check('laboratory first-component feedback',(-D.T*zz)[0]-(F-ad)*z2)
Om=s.symbols('Omega');S=Om*(J*ej)*ej.T
check('shear trace',s.trace(S));check('shear square',S*S)
lam,Th,G1,G2,k=s.symbols('lambda_ref Theta_ref G1 G2 k',nonzero=True)
G=s.Matrix([G1,G2]);dotprod=((J*zz).T*G)[0]
check('amplitude scalar ODE dilation',-((J*zz).T*(v**2*G))[0]/(mu*lam*k)*(v*Om)-v**3/mu*(-dotprod/(lam*k)*Om))
check('amplitude vorticity ODE dilation',(mu*lam)*z1*(v**2/mu*Th)-v**2*(lam*z1*Th))
Q,kq=s.symbols('Q kq',integer=True);beta=s.Rational(1,8)
check('retained signed seed gain exponent',(-kq-6)+(kq+5+beta)-(-s.Rational(7,8)))
z0,B0,tt=s.symbols('z0 B0 time',nonzero=True,real=True)
zz0=s.exp(tt)*z0
Bexpr=B0*s.exp(tt)*(1+z0**2)/(1+zz0**2)
def rational_check(label,expr):
 residual=s.cancel(expr)
 if residual!=0:raise AssertionError((label,residual))
 checks.append({'label':label,'residuals':['0']})
rational_check('pendulum positive amplitude ODE',s.diff(Bexpr,tt)-Bexpr*(1-zz0**2)/(1+zz0**2))
rational_check('pendulum amplitude initial value',Bexpr.subs(tt,0)-B0)
rational_check('pendulum angle derivative',s.diff(2*s.atan(zz0),tt)-2*zz0/(1+zz0**2))

# END UNCHANGED MATHEMATICAL BODY
finish('boussinesq', checks)
