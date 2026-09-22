from pathlib import Path
import json
import sympy as S

P=Path(__file__).parent
checks=[]
def eq(name,left,right):
    diff=left-right
    if isinstance(diff,S.MatrixBase):
        ok=all(S.simplify(x)==0 for x in diff)
    else:
        ok=S.simplify(diff)==0
    if not ok: raise ArithmeticError(name+': '+str(diff))
    checks.append(name)

I=S.I
G=S.diag(1,4,9,16,25,36)
Ghalf=S.diag(1,2,3,4,5,6)
Einv=Ghalf.inv()
z=S.Matrix([1,I,1,1,1,1])
House=S.eye(6)-z*z.H/3
J=Einv*House[:,[0,2,4,5]]
dag=lambda X:X.H*G
Pb=J*dag(J)
e=Einv[:,0]; f=Einv[:,1]
eps=S.Rational(7,3)
Pi=e*dag(e)+f*dag(f)
R=eps*f*dag(e)
u=dag(J)*e; v=dag(J)*f
U=u.row_join(v); C=U.H*U
a=C[0,0]; r=C[0,1]; d=C[1,1]; det=C.det(); alpha=1-a
As=U*U.H; Rb=eps*v*u.H
Q=S.eye(6)-Pb
g=u/S.sqrt(a); h=(v-r/a*u)/S.sqrt(det/a)
V=g.row_join(h)
Pr=U*C.inv()*U.H
eq('original isometry',dag(J)*J,S.eye(4))
eq('original projector',Pb*Pb,Pb)
eq('support compression',dag(J)*Pi*J,As)
eq('current frame orthonormal',V.H*V,S.eye(2))
eq('range projector',Pr*Pr,Pr)
eq('support kernel square',As-As*As,dag(J)*Pi*Q*Pi*J)
eq('support frame full complex cross term',V.H*As*V,S.Matrix([[a+abs(r)**2/a,r*S.sqrt(det)/a],[S.conjugate(r)*S.sqrt(det)/a,d-abs(r)**2/a]]))
eq('primitive multiplicativity defect',dag(J)*R*Q*R*J,-Rb*Rb)
eq('primitive observed relation',Rb*Rb,eps*r*Rb)
eq('hidden Gram cross', (dag(e)*Q*f)[0],-r)
Fdev=As-d*Pr
eq('second support error column',(h.H*Fdev.H*Fdev*h)[0],d*abs(r)**2/a)
eq('complete support error polynomial',As-As*As-d*(1-d)*Pr,(1-2*d)*Fdev-Fdev*Fdev)

sr,si=S.symbols('s_real s_imag',real=True)
s=sr+I*si
Fs=R+s*e*dag(e)
Fb=dag(J)*Fs*J
lam=a*s+eps*r
eq('source quadratic relation',Fs*Fs,s*Fs)
eq('observed quadratic relation',Fb*Fb,lam*Fb)
eq('observed full hidden return',dag(J)*Fs*Q*Fs*J,(alpha*s-eps*r)*Fb)
eq('observed triangular family',V.H*Fb*V,S.Matrix([[lam,0],[eps*S.sqrt(det),0]]))
star=-eps*r/a
Nnil=Rb+star*u*u.H
eq('shifted nilpotent',Nnil*Nnil,S.zeros(4))
eq('shifted original frame map',Nnil,eps*S.sqrt(det)*h*g.H)
eq('shifted Hilbert Schmidt norm',S.trace(Nnil.H*Nnil),eps**2*det)
eq('observed fibre current',I*(Fb-Fb.H),I*(Rb-Rb.H)-2*si*u*u.H)
W0=I*(Rb-Rb.H)
Wstar=I*(Nnil-Nnil.H)
eq('collision imaginary coordinate',S.im(star),S.trace(W0)/(2*a))
eq('collision current difference',Wstar-W0,2*eps*S.im(r)*g*g.H)
eq('constant observed current determinant',(V.H*(I*(Fb-Fb.H))*V).det(),-eps**2*det)
rankcol=S.Matrix([1,eps*S.sqrt(det)/lam])
eq('exact eigenprojection squared norm',(rankcol.H*rankcol)[0],1+eps**2*det/(lam*S.conjugate(lam)))

# An independent exact finite family exercises the inequalities at collisions,
# zero cross entries and complex cross entries, including non-small leakage.
tests=0
for den in (2,3,5):
 for x in (0,1,2):
  for y in (0,1):
   Z=S.Matrix([[S.Rational(x,den),I*S.Rational(y,den)],[S.Rational(1,den),S.Rational(2,den)]])
   C0=(S.eye(2)+Z.H*Z).inv()
   a0=C0[0,0];d0=C0[1,1];r0=C0[0,1];t0=abs(r0)**2;D0=C0.det(); al=1-a0
   assert al>=0 and D0>0 and S.simplify(al*(1-d0)-t0)>=0
   assert S.simplify(a0*al-t0)>=0
   assert S.simplify(al-(d0-D0))>=0
   gdiag=a0+t0/a0
   assert gdiag<=1 and t0/a0<=al
   tests+=1

negative=[]
for name,condition in [
 ('observation is multiplicative on primitive',Rb*Rb==S.zeros(4)),
 ('observed support stays idempotent',As*As==As),
 ('source and observed collision parameters coincide',star==0),
 ('complex collision leaves whole current unchanged',Wstar==W0),
 ('original support may be replaced by range projector',As==Pr)
]:
    if condition:raise ArithmeticError('Negative control failed: '+name)
    negative.append(name)
receipt={'exact_identity_count':len(checks),'exact_identities':checks,'exact_inequality_cases':tests,'negative_controls':negative,'scope':'Exact auxiliary matrix identities and finite rational inequality cases. Analytic native bounds are proved in ST1–20 and DF1–14; these checks do not evaluate period-dependent arithmetic matrices or an RH zero.','auxiliary_original_metric_diagonal':[1,4,9,16,25,36],'observed_gram':str(C),'collision':str(star)}
P.joinpath('SUPPORT_DEFORMATION_VERIFICATION.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps({'identities':len(checks),'inequality_cases':tests,'negative_controls':len(negative),'status':'passed'}))


# Complete stable-sign and source-step checks follow.
from pathlib import Path
import json
import sympy as S
P=Path(__file__).parent
I=S.I;t=S.symbols('t',real=True);s=S.symbols('s',real=True)
checks=[]
def eq(name,l,r):
    z=l-r
    vals=list(z) if isinstance(z,S.MatrixBase) else [z]
    if any(S.simplify(v)!=0 for v in vals):raise ArithmeticError(name+': '+str(z))
    checks.append(name)

def path(label,M,x,K,u,omega=None):
    G=S.eye(3);Gt=G-t/(1+t*(u.H*u)[0])*u*u.H
    PK=K*(K.H*K).inv()*K.H;h=PK*x;y=x-h
    uK=PK*u;uB=u-uK;a=(uK.H*uK)[0];beta=(uB.H*uB)[0];rho=(uB.H*x)[0];eta=(uK.H*h)[0]
    Ht=K*(K.H*Gt*K).inv()*K.H*Gt;ht=Ht*x;yt=x-ht
    sx=t/(1+beta*t);Gs=S.eye(3)-s/(1+a*s)*u*u.H
    ys=y+s*rho*uK;hs=h-s*rho*uK
    eq(label+' hidden path',ht,h-sx*rho*uK)
    eq(label+' metric path',Gt,Gs.subs(s,sx))
    eq(label+' complete observed row',ys.H*Gs,y.H-s*S.conjugate(rho)*uB.H)
    Y=(y.H*y)[0];Ys=(ys.H*Gs*ys)[0]
    eq(label+' observed norm',Ys,Y-s*abs(rho)**2)
    pair=lambda z,w:(z.H*w)[0]
    if omega is not None:
        eq(label+' unchanged eigenclass',M*x,omega*x)
        q0=-2*S.im(omega*Y-pair(y,M*h))
        q1=-2*S.im(rho*pair(y,M*uK)-omega*abs(rho)**2+S.conjugate(rho)*pair(uB,M*h))
        q2=2*abs(rho)**2*S.im(pair(uB,M*uK))
        curr=-2*S.im((yt.H*Gt*M*yt)[0])
        eq(label+' current quadratic',curr,q0+q1*sx+q2*sx*sx)
        j=(q0+q1*s+q2*s*s)/(Y-s*abs(rho)**2)
        eq(label+' normalized curvature',S.diff(j,s,2),2*(q2*Y**2+q1*Y*abs(rho)**2+q0*abs(rho)**4)/(Y-s*abs(rho)**2)**3)
    W0=pair(y,M*h)
    W1=-rho*pair(y,M*uK)-S.conjugate(rho)*pair(uB,M*h)
    W2=abs(rho)**2*pair(uB,M*uK)
    Z0=pair(h,M*y)
    Z1=rho*pair(h,M*uK)+a*Z0-S.conjugate(rho)*pair(uK,M*y)-S.conjugate(eta)*pair(u,M*y)
    Z2=a*rho*pair(h,M*uK)-abs(rho)**2*pair(uK,M*uK)-rho*S.conjugate(eta)*pair(u,M*uK)+a*S.conjugate(rho)*pair(uB,M*y)
    Z3=a*W2
    W=W0+W1*s+W2*s*s;Z=Z0+Z1*s+Z2*s*s+Z3*s**3
    eq(label+' complete forward cross polynomial',(ys.H*Gs*M*hs)[0],W)
    eq(label+' complete reverse cross polynomial',(hs.H*Gs*M*ys)[0],Z/(1+a*s))
    eq(label+' top imaginary coefficient',S.im(S.conjugate(Z3)*W2),0)
    top=S.Poly(S.expand(S.im(S.conjugate(Z)*W)),s)
    if top.degree()>4:raise ArithmeticError(label+' quartic failed')
    checks.append(label+' imaginary degree at most four')
    return S.simplify(-2*S.im((yt.H*Gt*M*yt)[0])),S.simplify((ht.H*Gt*M*yt)[0]),S.simplify((yt.H*Gt*M*ht)[0])

C=S.Matrix([[0,-S.Rational(3,5),0],[-S.Rational(3,5),0,-S.Rational(4,5)],[0,-S.Rational(4,5),0]])
M=C+S.Rational(10,3)*S.Matrix([0,1,0])*S.Matrix([[1,0,0]])
x=S.Matrix([S.Rational(3,10),I/2,S.Rational(2,5)]);K=S.Matrix([0,4*I/5,S.Rational(3,5)])
h=K*(K.H*x)[0];y=x-h
cur,z,w=path('first sign reversal',M,x,K,K+y,-I)
eq('displayed reversal rational current',cur,10*(4181*t-3750)/(113*t+1250)**2)
eq('displayed negative initial current',cur.subs(t,0),-S.Rational(3,125))
eq('displayed positive endpoint current',cur.subs(t,1),S.Rational(4310,1857769))
M2=S.Matrix([[0,0,0],[I/2,-3*I/256,0],[-67*I/256,0,-3*I/256]])
x2=S.Matrix([0,1,1]);K2=S.Matrix([1,0,0]);u2=S.Matrix([1,1,0])
cur,z,w=path('two sign crossings',M2,x2,K2,u2,-3*I/256)
eq('displayed two crossings',cur,(7*t-1)*(5*t-3)/(64*(1+t)**2))
A=S.Matrix([[0,0,0],[1,0,0],[I,0,0]])
cur,z,w=path('attained quartic',A,x2,K2,u2)
eq('displayed quartic reverse pairing',z,t**3/((1+t)**2*(1+2*t)))
eq('displayed quartic forward pairing',w,-t/(1+t)**2-I*t/(1+t))
eq('displayed quartic imaginary numerator',S.im(S.conjugate(z)*w),-t**4/((1+2*t)*(1+t)**3))

# Test the complete moving projection derivative in a nonidentity metric and
# with a Hermitian derivative that is not a scalar multiple of that metric.
G0=S.diag(2,3,5);Ed=S.Matrix([[1,I,0],[-I,2,1],[0,1,3]])
Gt=G0+t*Ed;PK=K2*(K2.H*Gt*K2).inv()*K2.H*Gt;PB=S.eye(3)-PK
eq('complete moving kernel projection derivative',S.diff(PK,t).subs(t,0),(PK*Gt.inv()*Ed*PB).subs(t,0))
ht=PK*x2;yt=x2-ht
num=(yt.H*Gt*M2*ht)[0]
expected=(yt.H*Ed*PB*M2*ht+yt.H*Gt*M2*PK*Gt.inv()*Ed*yt)[0]
eq('hidden-action derivative cancellation',S.diff(num,t).subs(t,0),expected.subs(t,0))

rr=S.symbols('r',positive=True);v=S.symbols('v',positive=True)
prim=v+v*S.sqrt((1+rr**2)*v**2-1)-S.acosh(v*S.sqrt(1+rr**2))/S.sqrt(1+rr**2)
eq('stability integral primitive',S.diff(prim,v),1+2*S.sqrt((1+rr**2)*v**2-1))
out={'source':'SC1–24 and supplied22September stable-sign calculation','exact_identity_count':len(checks),'identities':checks,'scope':'Exact generic-path and explicit auxiliary examples. Does not claim a native-period sign or replace the full source metric by an auxiliary metric.','status':'passed'}
(P/'SIGN_STABILITY_VERIFICATION.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'checks':len(checks),'status':'passed'}))


# Complete growing-jet and measured-inverse checks follow.
import json, hashlib, math
from pathlib import Path
import sympy as sp
import numpy as np
from scipy.linalg import expm, svdvals
import mpmath as mp

OUT=Path(__file__).resolve().parent
exact=[]; numeric=[]; negative=[]
def eq(label,a,b=0):
    if isinstance(a,sp.MatrixBase) or isinstance(b,sp.MatrixBase):
        d=sp.Matrix(a)-sp.Matrix(b)
        ok=all(sp.simplify(x)==0 for x in d)
    else: ok=sp.simplify(a-b)==0
    if not ok: raise ArithmeticError(label)
    exact.append(label)
def bounded(label,x,y):
    if not (math.isfinite(float(x)) and float(x)<=float(y)*(1+3e-10)+1e-12):
        raise ArithmeticError(f'{label}: {x}>{y}')
    numeric.append(label)
def neq(label,a,b=0):
    if isinstance(a,sp.MatrixBase) or isinstance(b,sp.MatrixBase):
        ok=any(sp.simplify(x)!=0 for x in sp.Matrix(a)-sp.Matrix(b))
    else: ok=sp.simplify(a-b)!=0
    if not ok: raise ArithmeticError('negative control failed '+label)
    negative.append(label)

eps,z,t=sp.symbols('eps z t',positive=True)
h=1/eps
C=sp.Matrix([[0,0,h],[0,0,1],[h,1,0]])
e=sp.Matrix([1,0,0]); f=sp.Matrix([0,1,0])
R=eps*f*e.T; M=C+R
J=sp.Matrix([[1,0],[0,1],[0,0]])
P=J*J.T; Pi=sp.eye(3)-P
RB=J.T*R*J; CB=J.T*C*J
eq('full rank-one squares to zero',R**2,sp.zeros(3))
eq('full characteristic polynomial',(z*sp.eye(3)-M).det(),z**3-(1+h*h)*z-1)
eq('determinant lemma',1-eps*(e.T*(z*sp.eye(3)-C).inv()*f)[0],
   (z*sp.eye(3)-M).det()/(z*sp.eye(3)-C).det())
eq('full resolvent rank-one formula',
   (z*sp.eye(3)-M).inv()-(z*sp.eye(3)-C).inv(),
   eps*(z*sp.eye(3)-C).inv()*f*e.T*(z*sp.eye(3)-C).inv()/
   (1-eps*(e.T*(z*sp.eye(3)-C).inv()*f)[0]))
U=[J.T*(sp.I*M)**n*J/sp.factorial(n) for n in range(7)]
Um=[(-1)**n*x for n,x in enumerate(U)]
def conv(A,B,n): return sum((A[j]*B[n-j] for j in range(n+1)),sp.zeros(A[0].rows,B[0].cols))
eq('measured group defect at t2',conv(Um,U,2),-sp.Matrix([[h*h,h],[h,1]]))
neq('time reversal is not the measured inverse',conv(Um,U,2),sp.zeros(2))
neq('compression is not multiplicative',J.T*M**2*J,(J.T*M*J)**2)
detcoefs=[]
for n in range(5):
    detcoefs.append(sum(U[j][0,0]*U[n-j][1,1]-U[j][0,1]*U[n-j][1,0] for j in range(n+1)))
eq('measured determinant t2',detcoefs[2],-(1+h*h)/2)
eq('measured determinant t3',detcoefs[3],sp.I/6)
Dminus=[(-sp.I)**n*(M**n)[2,2]/sp.factorial(n) for n in range(5)]
for n in range(5): eq(f'complementary determinant degree{n}',detcoefs[n],Dminus[n])
# Formal observed inverse and exact Schur complement through degree four.
V=[sp.eye(2)]
for n in range(1,5): V.append(-sum((V[j]*U[n-j] for j in range(n)),sp.zeros(2)))
B=[((-sp.I*M)**n/sp.factorial(n))[:2,2:3] for n in range(5)]
Cp=[((-sp.I*M)**n/sp.factorial(n))[2:3,:2] for n in range(5)]
Di=[sp.Integer(1)]
for n in range(1,5): Di.append(-sum(Di[j]*Dminus[n-j] for j in range(n)))
for n in range(5):
    corr=sum((B[i]*Di[j]*Cp[n-i-j] for i in range(n+1) for j in range(n-i+1)),sp.zeros(2))
    eq(f'actual measured inverse Schur degree{n}',V[n],Um[n]-corr)
for n in range(1,8):
    tel=sum((M**(n-1-j)*R*C**j for j in range(n)),sp.zeros(3))
    eq(f'exact telescoping word{n}',M**n-C**n,tel)
# Source metric non-unitary transport.
F=sp.Matrix([[1,sp.I/3,0],[0,2,sp.Rational(1,5)],[0,0,3]])
G=F.H*F; Mt=F.inv()*M*F; Ct=F.inv()*C*F; Jt=F.inv()*J
adj=lambda A:G.inv()*A.H*G
eq('transported selfadjoint C',adj(Ct),Ct)
eq('transported isometry',Jt.H*G*Jt,sp.eye(2))
eq('transported observed action',Jt.H*G*Mt*Jt,J.T*M*J)
eq('transported full characteristic',(z*sp.eye(3)-Mt).det(),(z*sp.eye(3)-M).det())
# Exact shear Gram eigenvalue identity.
x,S=sp.symbols('x S',positive=True)
N=sp.Matrix([[0,1],[0,0]]); Sh=sp.eye(2)+sp.I*x*N
eq('shear Gram determinant',(Sh.H*Sh).det(),1)
eq('shear Gram trace',sp.trace(Sh.H*Sh),x*x+2)
spoly=sp.Poly(S**2-x*S-1,S)
eq('shear root square satisfies Gram polynomial',
   sp.rem(S**4-(x*x+2)*S*S+1,spoly.as_expr(),S),0)
# The Gram lower-eigenvalue statement alone cannot prove det>=Theta.
Theta=sp.Rational(1,5); Gram=sp.diag(Theta,Theta)
neq('matrix lower bound alone does not give determinant certificate',Gram.det(),Theta)
# Complete finite jet quotient and source transfer; no per-row metric cost.
A=sp.Matrix([[2,sp.Rational(1,3),0,0],[0,3,sp.Rational(1,7),0],
             [0,0,4,sp.Rational(1,9)],[0,0,0,5]])
G0=sp.eye(4); G1=A.T*A
Elo=sp.Matrix([[0,0],[0,0],[1,0],[0,1]])
Jet=sp.Matrix([[1,0,0,0],[0,1,0,0]])
Hjet=(Jet*G1.inv()*Jet.T).inv()
Sch=G1[:2,:2]-G1[:2,2:]*G1[2:,2:].inv()*G1[2:,:2]
eq('whole jet fibre minimum',Hjet,Sch)
neq('jet quotient not leading principal metric',Hjet,G1[:2,:2])
# Finite triangular normalized conductor inverse geometric series.
Tri=sp.Matrix([[sp.Rational(2,5),0,0],[sp.Rational(1,7),sp.Rational(3,7),0],
               [sp.Rational(-1,9),sp.Rational(2,9),sp.Rational(4,9)]])
D=sp.diag(*[Tri[i,i] for i in range(3)])
Ht=D.inv()*(Tri-D)
eq('finite triangular nilpotence',Ht**3,sp.zeros(3))
eq('complete triangular inverse',(sp.eye(3)-Ht+Ht**2)*D.inv(),Tri.inv())
# Direct coefficients of Gamma monic sequence and full ideal.
y=sp.symbols('y')
polys=[sp.Integer(1),y]
for n in range(1,14): polys.append(sp.expand(y*polys[-1]-n*(sp.Rational(2*n-1,2))*polys[-2]))
Q=(y-sp.I)*(y+sp.I)*(y-2*sp.I)*(y+2*sp.I)
for n in range(4,12):
    target=sp.Poly(Q*polys[n-4],y).as_expr(); rem=target; vals={}
    for d in range(n,-1,-1):
        coef=sp.Poly(rem,y).coeff_monomial(y**d)
        vals[d]=coef; rem=sp.expand(rem-coef*polys[d])
    eq(f'complete monic basis conversion degree{n}',rem,0)
    B0=2*(n+1); Z=2*(n+1)*max(1,2,B0)
    for j in range(n+1):
        if abs(vals[n-j])>Z**j: raise ArithmeticError('coefficient conversion bound')
        exact.append(f'jet coefficient degree{n} depth{j}')
# Feedback and actual inverse finite numerical checks.
for ep in [1,2,5,20,100]:
    cv=np.array(C.subs(eps,ep)).astype(complex); mv=np.array(M.subs(eps,ep)).astype(complex)
    rv=np.array(R.subs(eps,ep)).astype(complex)
    c=max(1,np.linalg.norm(cv,2)); rho=8*3*max(1,c,2)
    for j in range(9):
        actual=np.linalg.norm(np.array(Pi).astype(complex)@np.linalg.matrix_power(cv,j)@np.array([1,0,0]))
        bounded(f'actual source power eps{ep} j{j}',actual,c**j/ep)
        gj=ep*(np.linalg.matrix_power(cv,j))[0,1]
        bounded(f'feedback coefficient eps{ep} j{j}',abs(gj),rho**(j+1))
    for ang in [0,.25,1,2,3]:
        zz=rho*np.exp(1j*ang)
        bounded(f'characteristic resolvent eps{ep} angle{ang}',
                np.linalg.norm(np.linalg.inv(zz*np.eye(3)-mv)-np.linalg.inv(zz*np.eye(3)-cv),2),
                2*ep/rho**2)
    for tt in [1e-7,1e-5,1e-3]:
      for sign in [-1,1]:
        ts=sign*tt; X=expm(1j*ts*mv); Xi=expm(-1j*ts*mv); uv=X[:2,:2]
        FF=c*tt+2*ep/rho*(np.expm1(rho*tt)-rho*tt)
        bounded(f'full finite remainder eps{ep} t{ts}',np.linalg.norm(X-np.eye(3)-1j*ts*rv,2),FF)
        ek=math.exp(c*tt)*(1/ep+(c*tt)**4/math.factorial(4))
        kap=np.expm1(rho*tt)-rho*tt
        dk=c*tt+ep*tt*ek/(1-kap)
        bounded(f'hidden source evolution eps{ep} t{ts}',np.linalg.norm((X-np.eye(3))[:,2],2),dk)
        schur=Xi[:2,:2]-Xi[:2,2:3]@Xi[2:3,:2]/Xi[2,2]
        bounded(f'measured inverse identity eps{ep} t{ts}',np.linalg.norm(np.linalg.inv(uv)-schur,2),1e-10)
        bounded(f'measured inverse estimate eps{ep} t{ts}',np.linalg.norm(np.linalg.inv(uv)-Xi[:2,:2],2),
                dk/(1-dk)*(tt*ep+FF))
        bounded(f'complementary determinant finite eps{ep} t{ts}',abs(np.linalg.det(uv)-Xi[2,2]),1e-10)
        bounded(f'measured log determinant bound eps{ep} t{ts}',abs(np.log(np.linalg.det(uv))),-np.log(1-dk))
# Independent elliptic constants in the exact original Landen coordinate.
mp.mp.dps=75
Ffun=lambda zz:2*mp.ellipk(zz)/mp.pi
Tfun=lambda zz:2*(mp.ellipe(zz)/((1-zz)*mp.ellipk(zz))-1)
zz=mp.findroot(lambda zz:Tfun(zz)-1,(mp.mpf('.45'),mp.mpf('.55')))
a0=mp.log(4/mp.pi)
a1=2*mp.log(4/(2*mp.pi*(1-zz)*Ffun(zz)))+mp.log(zz)/4
J1=2*mp.log(Ffun(zz))-mp.log(zz)/2
vals={'z1':zz,'a0':a0,'a1':a1,'C_monic':2*(a0-a1),
      'C_boundary':2*J1,'plateau':4*(a0-a1)}
if not(abs(vals['plateau']-mp.mpf('.700182093000866100'))<mp.mpf('1e-17')): raise ArithmeticError('plateau')
if not(abs(vals['C_boundary']-mp.mpf('1.354281987825292132'))<mp.mpf('1e-17')): raise ArithmeticError('boundary')
if not vals['C_boundary']>3*vals['C_monic']: raise ArithmeticError('constant collision control')
negative.append('monic allowance difference is not the kernel-volume coefficient')
# Two different ranks retained: arbitrary positive Gram certificate valid by determinant.
for aa,dd,rr in [(sp.Rational(9,10),sp.Rational(3,4),sp.Rational(1,10)),
                (sp.Rational(4,5),sp.Rational(7,8),sp.I/12)]:
    Cg=sp.Matrix([[aa,rr],[sp.conjugate(rr),dd]])
    det=Cg.det(); eq('actual area algebra',aa*dd-det,abs(rr)**2)
    if not aa*dd>=det: raise ArithmeticError('determinant area')
    exact.append('epsilonB lower area certificate')
# Closure receipt records samples as samples, not native matrices.
data={'status':'passed','exact_checks':len(exact),'numerical_inequalities':len(numeric),
      'negative_controls':len(negative),'exact_labels':exact,'numeric_labels':numeric,
      'negative_labels':negative,'profile_values':{k:mp.nstr(v,65) for k,v in vals.items()},
      'scope':'Auxiliary exact finite identities and numerical inequalities; analytic source and clock proofs are EE1–48. No hypothetical native zeta matrices were numerically evaluated.'}
(OUT/'EVOLUTION_EXTENSION_VERIFICATION.json').write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({k:data[k] for k in ['status','exact_checks','numerical_inequalities','negative_controls','profile_values']},indent=2))

