"""Exact identities for the new bridge; no source shelf, network, or Lean is used."""
from pathlib import Path
import hashlib
import json
import sympy as S

ROOT = Path(__file__).resolve().parent
checks = []

def zero(value, label):
    value = S.cancel(S.expand(value))
    assert value == 0, (label, value)
    checks.append(label)

def matzero(matrix, label):
    for i in range(matrix.rows):
        for j in range(matrix.cols):
            zero(matrix[i,j], f'{label}[{i},{j}]')

s,b,c,r,p,eta,q = S.symbols('s b c r p eta q')
m = b*b/16-2*s
n = m+4
beta = b/4
P = c*r**3-2*r**2+b*r-4*s
zero(S.diff(P,s)+6*c*S.diff(P,b)+(4-6*c*r), 'original cubic material lift')
T = S.Matrix([[1,beta,0,0],[0,1,0,0],[0,0,1,beta],[0,0,0,1]])
Ti = S.Matrix([[1,-beta,0,0],[0,1,0,0],[0,0,1,-beta],[0,0,0,1]])
matzero(T*Ti-S.eye(4), 'both exact basis maps')
Hs = S.diag(0,-1/m,-1/n,-1/m-1/n)
Hb = -b*Hs/16
Gs = S.Matrix([[0,beta/m,0,0],[0,-1/m,0,0],
                [0,0,-1/n,beta/m],[0,0,0,-1/m-1/n]])
Gb = S.Matrix([[0,S.Rational(1,4)-b*beta/(16*m),0,0],[0,b/(16*m),0,0],
                [0,0,b/(16*n),S.Rational(1,4)-b*beta/(16*m)],
                [0,0,0,b/(16*m)+b/(16*n)]])
matzero(Gs-(Ti*Hs*T+Ti*T.diff(s)), 'original basis s connection')
matzero(Gb-(Ti*Hb*T+Ti*T.diff(b)), 'original basis b connection')
matzero(Gb.diff(s)-Gs.diff(b)+Gs*Gb-Gb*Gs, 'full matrix curvature')
Js = S.diag(0,-1/m**2,-1/n**2,-1/m**2-1/n**2+2/(m*n))
Jb = S.diag(0,1/(16*m)-b*b/(256*m*m),1/(16*n)-b*b/(256*n*n),
    (1/m+1/n)/16-b*b*(1/m**2+1/n**2)/256+b*b/(128*m*n))
matzero(Js-Hs.diff(s)-Hs*Hs, 'all s second derivative coefficients')
matzero(Jb-Hb.diff(b)-Hb*Hb, 'all b second derivative coefficients')
# Independent verification that the second-order basis transport includes dT.
matzero(Gb.diff(b)+Gb*Gb-Ti*(T.diff(b,2)+2*Hb*T.diff(b)+Jb*T),
        'second axial derivative basis transport')
matzero(Gs.diff(s)+Gs*Gs-Ti*(T.diff(s,2)+2*Hs*T.diff(s)+Js*T),
        'second arithmetic derivative basis transport')

# Quotient arithmetic checks, with both original quadratic relations retained.
def reduce_cover(expr):
    expr=S.cancel(expr)
    num,den=S.fraction(expr)
    for var,relation in [(eta,eta**2-m),(p,p**2-n)]:
        num=S.rem(num,relation,var)
    return S.cancel(num/den)

zero(reduce_cover((p+eta)*(p-eta)/4-1), 'Laurent product')
zero(reduce_cover((p+eta)/2+(p-eta)/2-p), 'inverse p')
zero(reduce_cover((p+eta)/2-(p-eta)/2-eta), 'inverse eta')
zero(reduce_cover(-S.Rational(1,2)*(1/p+1/eta)+(p+eta)/(2*eta*p)),
     's derivative original Laurent q')
zero(reduce_cover(b*(1/p+1/eta)/32-b*(p+eta)/(32*eta*p)),
     'b derivative original Laurent q')

# Source coordinate inverse Jacobian, independently differentiated in Q,xi.
Q,X,xi,w = S.symbols('Q X xi w', positive=True)
h=S.symbols('h', real=True)
A=S.Rational(1,2)+h
D=S.Rational(1,2)-h
d=1-xi**2
ell=1-2*h*xi**2
tau=Q*d
z=Q**D*xi
jac=S.Matrix([[S.diff(tau,Q),S.diff(tau,xi)],[S.diff(z,Q),S.diff(z,xi)]])
# Factor positive Q powers before rational cancellation.
def powerzero(expr,label):
    expr=S.powsimp(S.expand_power_base(S.expand(expr),force=True),force=True)
    zero(expr,label)
powerzero(jac.det()-Q**D*ell, 'source exact positive Jacobian')
jt=S.Matrix([-1/ell,D*xi/(Q*ell)])
jz=S.Matrix([2*xi*Q**(1-D)/ell,d/(Q**D*ell)])
for i,expected in enumerate((-1,0)):
    powerzero((jac*jt)[i]-expected,f'source physical t inverse {i}')
for i,expected in enumerate((0,1)):
    powerzero((jac*jz)[i]-expected,f'source physical z inverse {i}')
powerzero(-X*jt[0]/Q-X/(Q*ell), 'source X physical time')
powerzero(-X*jz[0]/Q+2*xi*X/(Q**D*ell), 'source X physical axial')

def Tw(f,weight):
    return (-weight*f+D*xi*S.diff(f,xi)+X*S.diff(f,X))/ell
def Zw(f,weight):
    return (2*weight*xi*f+d*S.diff(f,xi)-2*xi*X*S.diff(f,X))/ell
def dt(f):
    return -S.diff(f,Q)/ell+X*S.diff(f,X)/(Q*ell)+D*xi*S.diff(f,xi)/(Q*ell)
def dz(f):
    return 2*xi*Q**(1-D)*S.diff(f,Q)/ell-2*xi*X*S.diff(f,X)/(Q**D*ell)+d*S.diff(f,xi)/(Q**D*ell)

for i,j in [(0,0),(1,0),(0,1),(2,3),(3,2)]:
    f=X**i*xi**j
    powerzero(dt(Q**w*f)-Q**(w-1)*Tw(f,w),f'weighted actual t [{i},{j}]')
    powerzero(dz(Q**w*f)-Q**(w-D)*Zw(f,w),f'weighted actual z [{i},{j}]')
    # Equality of mixed derivatives includes both shifted weight operators.
    zero(Zw(Tw(f,w),w-1)-Tw(Zw(f,w),w-D),f'weighted flatness [{i},{j}]')

# Source nonlinear material weights, vector frame factors and pressure balance.
zero(A+D-1, 'source material axial weight')
zero((-2*A-D)-(-A-1), 'source axial pressure weight')
zero((w-2*D)-(w-1+2*h), 'source axial viscous weight')
zero(1-A-D, 'negative coefficient germ exponent')
rho=S.symbols('rho',positive=True)
for degree in range(5):
    f=(rho*rho/(2*Q))**degree
    radial=S.diff(f,rho,2)+S.diff(f,rho)/rho
    expected=(2*X*S.diff(X**degree,X,2)+2*S.diff(X**degree,X))/Q
    zero(radial.subs(rho**2,2*Q*X)-expected,f'cylindrical radial exact [{degree}]')
    zero(((radial-f/rho**2).subs(rho**2,2*Q*X))-(expected-X**degree/(2*Q*X)),
        f'vector frame exact [{degree}]')
F=S.Function('F')(X,xi)
E=S.sqrt(2*X)*F
PiX=E**2/(2*X)
zero(S.sqrt(2*X)*PiX-E**2/S.sqrt(2*X), 'source centrifugal pressure exact cancellation')
# Integrate incompressibility for independently specified polynomial U profiles.
y=S.symbols('y')
for degree in range(5):
    U=X**degree*(1+xi+xi**2)
    av=S.integrate(U.subs(X,y),(y,0,X))/X
    V=X*(2*xi*U-2*D*xi*av-d*S.diff(av,xi))/ell
    zero(S.diff(V,X)+Zw(U,-A),f'source integrated divergence [{degree}]')

# Both source physical time and all four arithmetic sheets retain real structure.
aa,pp=S.symbols('aa pp',positive=True)
mm=S.symbols('mm',real=True)
for sign_eta in [-1,1]:
    for sign_p in [-1,1]:
        qsheet=(sign_p*pp+S.I*sign_eta*aa)/2
        replacements={aa**2:-mm,pp**2:mm+4}
        zero(S.expand(qsheet*S.conjugate(qsheet)).subs(replacements)-1,
             f'unit circle norm [{sign_eta},{sign_p}]')
        zero(S.expand(qsheet+S.conjugate(qsheet))-sign_p*pp,
             f'unit circle p recovery [{sign_eta},{sign_p}]')
        zero(S.expand(qsheet-S.conjugate(qsheet))-sign_eta*S.I*aa,
             f'unit circle eta recovery [{sign_eta},{sign_p}]')

C=q**10-q**4-q**(-4)+q**(-10)
quantum7=sum(q**j for j in range(-6,7,2))
quantum3=q*q+1+q**(-2)
zero(C-(q-q**(-1))**2*quantum7*quantum3,'original full GCT factorization')
zero(quantum7-((q+1/q)**6-5*(q+1/q)**4+6*(q+1/q)**2-1),'original quantum7 polynomial')
t=S.symbols('t')
B=-42+196*t-280*t*t+160*t**3-32*t**4
Ct=-2*t*(3-2*t)*(7-28*t+28*t*t-8*t**3)
zero(Ct-t*B, 'exact full finite-negative polynomial')
zero((m*(n**3-5*n*n+6*n-1)*(n-1)).subs({b:0,s:t})-Ct,
     'original retained b coefficient pullback')
zero(B.subs(t,0)+42, 'negative leading coefficient')
zero(S.rem(Ct,t,t), 'finite value zero at endpoint')
zero(S.diff(Ct,t).subs(t,0)+42, 'simple endpoint zero derivative')

receipt={'status':'pass','checks':len(checks),'labels':checks,
 'scope':'Exact coordinate, algebra, connection, nonlinear leading-profile residual ingredients and finite-negative coefficient identities; no full NS theorem verification.',
 'source_access_during_replay':False,
 'hashes':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
           for name in ['ns_scaling_bridge.tex','check_ns_scaling_bridge.py']}}
(ROOT/'verification.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:receipt[k] for k in ['status','checks','source_access_during_replay']}))
