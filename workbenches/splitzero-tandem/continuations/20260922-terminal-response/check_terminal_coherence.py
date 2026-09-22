"""Exact complex-amplitude identities and complete auxiliary cardinal-quotient tests.

The finite Gamma examples have q=4 and a stated auxiliary observation. They
test the algebra; they are not the programme's native period calculations.
"""
from pathlib import Path
import json
import sympy as s
import numpy as np

P=Path(__file__).resolve().parent
exact=[]
finite=[]
negative=[]

def eq(name,a,b):
    d=a-b
    values=list(d) if isinstance(d,s.MatrixBase) else [d]
    if not all(s.simplify(v)==0 for v in values):
        raise ArithmeticError(name+': '+str(d))
    exact.append(name)

def le(name,a,b):
    a=float(np.real(a)); b=float(np.real(b))
    if a>b+2e-10*max(1,abs(a),abs(b)):
        raise ArithmeticError(f'{name}: {a} > {b}')
    finite.append({'name':name,'lhs':a,'rhs':b})

lp,ln=s.symbols('lambda_p lambda_n',positive=True)
A=s.sqrt(lp/(lp+ln));B=s.sqrt(ln/(lp+ln))
W=s.Matrix([[lp-ln,-s.I*s.sqrt(lp*ln)],[s.I*s.sqrt(lp*ln),0]])
wp=s.Matrix([-s.I*A,B]);wm=s.Matrix([s.I*B,A])
eq('TR14 positive current eigenvector',W*wp,lp*wp)
eq('TR14 negative current eigenvector',W*wm,-ln*wm)
eq('TR14 orthonormal positive vector',(wp.H*wp)[0],1)
eq('TR14 orthonormal negative vector',(wm.H*wm)[0],1)
eq('TR14 orthogonal sign vectors',(wp.H*wm)[0],0)
W4=s.diag(W,s.zeros(2))
Hbasis=s.eye(4)[:,1:]
eq('TR12a full maximal-isotropic form',Hbasis.H*W4*Hbasis,s.zeros(3))
eq('TR12a actual nondegenerate rank',W4.rank(),2)
eq('TR12a actual isotropic dimension',Hbasis.rank(),3)
if W4*s.eye(4)[:,1]==s.zeros(4,1):
    raise ArithmeticError('Isotropic-to-zero-operator negative control failed')
negative.append('identifying an isotropic current line with a zero-action line')
ag,bg,ah,bh=s.symbols('ag bg ah bh',real=True)
cg=ag+s.I*bg;ch=ah+s.I*bh
ypair=s.Matrix([cg,ch])
zp=(wp.H*ypair)[0];zm=(wm.H*ypair)[0]
eq('TR16 complete weighted amplitude',A*zp-B*zm,s.I*cg)
eq('TR16 complete complementary amplitude',B*zp+A*zm,ch)
eq('TR17 unweighted phase difference',zp-zm,s.I*(A+B)*cg+(B-A)*ch)
eq('TR18 exact coherence deficit',
   s.expand(zp*s.conjugate(zp)+zm*s.conjugate(zm)-2*s.re(zp*s.conjugate(zm))),
   s.expand((zp-zm)*s.conjugate(zp-zm)))
eq('TR20 exact residual-current decomposition',(ypair.H*W*ypair)[0],
   (lp-ln)*(ag*ag+bg*bg)+2*s.sqrt(lp*ln)*s.im(s.conjugate(cg)*ch))

# A deliberate sign-phase error must change the algebra.
wrong=s.Matrix([s.I*A,B])
if all(s.simplify(v)==0 for v in W*wrong-lp*wrong):
    raise ArithmeticError('Wrong current phase was not rejected')
negative.append('reversing the physical imaginary phase')
if s.simplify(s.expand(s.I*(A+B)*cg+(B-A)*ch))==0:
    raise ArithmeticError('Exact equal-amplitude replacement was not rejected')
negative.append('replacing exponentially coherent amplitudes by exact equality')

y=s.symbols('y',real=True)
mass=s.Integer(3)  # retained common source mass, not probability
h=[mass*s.factorial(j)*s.rf(s.Rational(1,2),j) for j in range(5)]
p=[s.Integer(1),y]
for j in range(1,4):
    p.append(s.expand(y*p[-1]-j*(s.Rational(j)-s.Rational(1,2))*p[-2]))
C=s.zeros(4)
for j in range(1,4):
    C[j-1,j]=C[j,j-1]=s.sqrt(j*(s.Rational(j)-s.Rational(1,2)))
e=s.eye(4)[:,3]

def num(v):return np.array(v.evalf(18).tolist(),dtype=complex)
def ip(a,b):return np.vdot(a,b)
def norm(a):return float(np.linalg.norm(a))

for gam in (s.Integer(3),s.Integer(10),s.Integer(30)):
  for delt in (s.Rational(1,4),s.Rational(1,3)):
    tag=f'Gamma-cardinal gamma={gam}, delta={delt}'
    Q=s.expand(((y-gam)**2+delt*delt)*((y+gam)**2+delt*delt))
    omega=gam-s.I*delt
    cardinal=s.cancel(s.div(Q,y-omega,y)[0]/s.diff(Q,y).subs(y,omega))
    eq(tag+' terminal cardinal value',cardinal.subs(y,omega),1)
    eq(tag+' full original root remainder',s.rem((y-omega)*cardinal,Q,y),0)
    # Exact coordinate map from degree<4 polynomials to the retained
    # mass-3 Gamma orthonormal basis.
    cols=s.Matrix([[s.Poly(p[j],y).nth(i) for j in range(4)] for i in range(4)])
    coeff=s.Matrix([s.Poly(cardinal,y).nth(i) for i in range(4)])
    x=s.diag(*[s.sqrt(a) for a in h[:4]])*cols.inv()*coeff
    remainder=s.rem(p[4],Q,y)
    b4=s.diag(*[s.sqrt(a) for a in h[:4]])*cols.inv()*s.Matrix([s.Poly(remainder,y).nth(i) for i in range(4)])
    R=b4*e.H/s.sqrt(h[3])
    M=C+R
    eq(tag+' exact original cardinal eigenclass',M*x,omega*x)
    eq(tag+' rank-one square zero',R*R,s.zeros(4))
    eq(tag+' selfadjoint full compression',C.H,C)
    # The named fixture observation retains a complete rank-three minimum.
    hidden=s.Matrix([3*s.I,4,0,s.Rational(1,10000)])
    hidden=hidden/s.sqrt((hidden.H*hidden)[0])
    Proj=s.eye(4)-hidden*hidden.H
    eq(tag+' actual fixture projection',Proj*Proj,Proj)
    xx=num(x).ravel(); ee=num(e).ravel();CC=num(C); RR=num(R)
    PP=num(Proj);eps=float(np.linalg.norm(RR,2))
    ff=num(b4).ravel()/norm(num(b4).ravel())
    uu=PP@ee; vv=PP@ff; yy=PP@xx
    aa=norm(uu)**2;dd=norm(vv)**2;rr=ip(uu,vv)
    determinant=aa*dd-abs(rr)**2
    alpha=norm(ee-uu)**2
    theta=norm(yy)**2/norm(xx)**2;thetaK=1-theta
    c=float(np.linalg.norm(CC,2));D=abs(complex(omega))+c
    gg=uu/np.sqrt(aa)
    hh=(vv-rr/aa*uu)/np.sqrt(determinant/aa)
    yhat=yy/norm(yy)
    cgn=ip(gg,yhat);chn=ip(hh,yhat)
    eta=min(1,(D/eps+np.sqrt(alpha*max(0,thetaK)))/np.sqrt(aa*theta))
    le(tag+' TR10 complex-coordinate bound',abs(cgn),eta)
    root=np.sqrt(determinant+rr.imag**2)
    lambdap=eps*(-rr.imag+root)
    lambdan=eps*(rr.imag+root)
    acoef=np.sqrt(lambdap/(lambdap+lambdan))
    bcoef=np.sqrt(lambdan/(lambdap+lambdan))
    wpv=-1j*acoef*gg+bcoef*hh
    wmv=1j*bcoef*gg+acoef*hh
    zpv=ip(wpv,yhat);zmv=ip(wmv,yhat)
    le(tag+' TR16 weighted complex residual',abs(acoef*zpv-bcoef*zmv-1j*cgn),1e-11)
    tracephase=abs(rr.imag)/root
    ampbound=np.sqrt(2)*eta+tracephase
    le(tag+' TR17 unweighted complex difference',abs(zpv-zmv),ampbound)
    phase_deficit=abs(zpv-zmv)**2
    le(tag+' TR18 doubled-order phase deficit',phase_deficit,ampbound**2)
    le(tag+' TR19 weight consequence',abs(abs(zpv)**2-abs(zmv)**2),
       2*eta+np.sqrt(2)*tracephase)
    current=1j*eps*(np.outer(vv,np.conjugate(uu))-np.outer(uu,np.conjugate(vv)))
    jn=ip(yhat,current@yhat).real
    main=2*eps*np.sqrt(determinant)*np.imag(np.conjugate(cgn)*chn)
    diagonal=-2*eps*rr.imag*abs(cgn)**2
    le(tag+' TR20 exact residual decomposition',abs(jn-main-diagonal),
       1e-10*max(1,abs(jn),abs(main)))
    le(tag+' TR20 absolute diagonal correction',abs(diagonal),2*eps*abs(rr)*eta**2)
    an=ip(ee,xx);bn=ip(ff,xx);squared=norm(xx)**2
    scalar=-1j*eps*np.conjugate(an)*bn/squared
    le(tag+' TR21 physical positive real part',abs(scalar.real-float(delt)),1e-9)
    ar=squared/abs(an)**2;br=squared/abs(bn)**2
    le(tag+' TR22 exact product relative residual',
       abs(ar*br*abs(scalar)**2/eps**2-1),1e-9)
    le(tag+' TR22 source-row lower amplification',eps**2/D**2,ar)
    le(tag+' TR22 source-row upper amplification',ar,eps**2/float(delt)**2)
    le(tag+' TR22 outgoing-row lower amplification',1,br)
    le(tag+' TR22 outgoing-row upper amplification',br,D**2/abs(scalar)**2)
    kval=(np.eye(4)-PP)@xx
    U=ip(ee,kval)/an;V=ip(ff,kval)/bn
    betaK=norm(ff-vv)**2
    le(tag+' TR24 exact first response bound',abs(U),eps*np.sqrt(alpha*max(0,thetaK))/abs(scalar))
    le(tag+' TR24 exact second response bound',abs(V),D*np.sqrt(betaK*max(0,thetaK))/abs(scalar))
    # This fixed fixture observation is complex: its complete cross phase
    # and diagonal current contribution remain in every preceding check.

# Exact symbolic nonzero cross-phase test using a valid three-dimensional
# observed Gram, with no cardinal-source inference assigned to it.
rreal=s.Rational(1,10);rimag=s.Rational(1,20)
aval=s.Rational(4,5);dval=s.Rational(3,5)
det=aval*dval-rreal*rreal-rimag*rimag
uv=s.Matrix([[s.sqrt(aval),(rreal+s.I*rimag)/s.sqrt(aval)],
             [0,s.sqrt(det/aval)]])
gram=uv.H*uv
eq('complete complex Gram retained',gram,s.Matrix([[aval,rreal+s.I*rimag],[rreal-s.I*rimag,dval]]))
actual=s.I*(uv[:,1]*uv[:,0].H-uv[:,0]*uv[:,1].H)
eq('TR13 imaginary diagonal sign',actual,s.Matrix([[-2*rimag,-s.I*s.sqrt(det)],[s.I*s.sqrt(det),0]]))
if s.simplify(actual[0,0])==0:
    raise ArithmeticError('Complex trace removal negative control failed')
negative.append('discarding the original complex diagonal current')

receipt={'exact_identity_count':len(exact),'exact_identities':exact,
         'finite_inequality_count':len(finite),'finite_inequalities':finite,
         'negative_controls':negative,
         'scope':'Exact rank-two phase identities and complete degree-three Gamma cardinal-quotient fixtures with stated rank-three observation. These are auxiliary finite checks; no native-period matrix was evaluated and no residual sign theorem was inferred.'}
(P/'COHERENCE_VERIFICATION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:receipt[k] for k in ('exact_identity_count','finite_inequality_count','negative_controls')},indent=2))
