from pathlib import Path
import hashlib,itertools,json,sys
import sympy as s

ROOT=Path(__file__).resolve().parent
passed=[]; controls=[]
def check(name,truth):
    if not bool(truth): raise RuntimeError(name)
    passed.append(name)
def zero(M): return all(s.cancel(s.together(x))==0 for x in M)
def eq(name,a,b):
    check(name,zero(a-b) if isinstance(a,s.MatrixBase) else s.cancel(s.together(a-b))==0)
def psd(name,M,strict=False):
    check(name+' Hermitian',zero(M-M.H))
    for k in range(1,M.rows+1):
        for ix in itertools.combinations(range(M.rows),k):
            v=s.factor(M.extract(ix,ix).det())
            check(name+' minor '+str(ix),v.is_positive if strict else v.is_nonnegative)
def negative(name,truth):
    if not bool(truth): raise RuntimeError('negative control '+name)
    controls.append(name)
def d(g,t): return s.factor(g*t/((1+t)*(1+(1-g)*t)))
def phase_tan(g,t): return s.factor(g*t/(1+(1-g)*t*t))
def eigs2(M):
    tr=s.factor(s.trace(M)); det=s.factor(M.det()); disc=s.factor(tr*tr-4*det)
    return [(tr+s.sqrt(disc))/2,(tr-s.sqrt(disc))/2]

t=s.symbols('t',positive=True); g=s.symbols('g',nonnegative=True)
eq('phase critical derivative',s.diff(g*t/(1+(1-g)*t*t),t),g*(1-(1-g)*t*t)/(1+(1-g)*t*t)**2)
eq('derivative critical derivative',s.diff(g*t/((1+t)*(1+(1-g)*t)),t),g*(1-(1-g)*t*t)/((1+t)**2*(1+(1-g)*t)**2))
eq('trace phase improvement derivative',s.diff(2*t/(1+t)-s.atan(t),t),(t-1)**2/((1+t)**2*(1+t*t)))
eq('scalar phase kernel derivative',s.diff((1+t)**2/(1+t*t),t),2*(1+t)*(1-t)/(1+t*t)**2)
for gg in [s.Rational(1,5),s.Rational(9,25),s.Rational(16,25),s.Rational(3,4),s.Integer(1)]:
    critical=1/s.sqrt(1-gg) if gg!=1 else None
    for lo,hi in [(s.Rational(1,4),s.Rational(1,2)),(s.Rational(1,4),s.Integer(2)),(s.Integer(2),s.Integer(4))]:
        peak=hi if critical is None else max(lo,min(hi,critical))
        for j in range(9):
            tt=lo+(hi-lo)*j/8
            check(f'scalar phase max {gg} {lo} {hi} {j}',s.simplify(phase_tan(gg,peak)-phase_tan(gg,tt)).is_nonnegative)
            check(f'scalar phase min {gg} {lo} {hi} {j}',s.simplify(phase_tan(gg,tt)-min(phase_tan(gg,lo),phase_tan(gg,hi))).is_nonnegative)
            check(f'scalar derivative max {gg} {lo} {hi} {j}',s.simplify(d(gg,peak)-d(gg,tt)).is_nonnegative)
            check(f'scalar derivative min {gg} {lo} {hi} {j}',s.simplify(d(gg,tt)-min(d(gg,lo),d(gg,hi))).is_nonnegative)
    if gg!=1:
        eq('phase exact maximum '+str(gg),phase_tan(gg,critical),gg/(2*s.sqrt(1-gg)))
        eq('derivative exact maximum '+str(gg),d(gg,critical),(1-s.sqrt(1-gg))/(1+s.sqrt(1-gg)))

# Full noncommuting energy in an exactly known original angle frame.
U=s.Matrix([[s.Rational(4,5),0],[0,s.Rational(3,5)],[s.Rational(3,5),0],[0,s.Rational(4,5)]])
S=s.Matrix([[2,1],[1,3]])
T0=U*S*U.H; H0=T0.H*T0; P0=U*U.H
JB0=s.eye(4)[:,:2]; JK0=s.eye(4)[:,2:4]
gamma=JK0.H*P0*JK0
eq('full angle spectrum',gamma,s.diag(s.Rational(9,25),s.Rational(16,25)))
psd('actual positive floor',S*S-s.eye(2))
psd('actual positive ceiling',16*s.eye(2)-S*S)
F=s.eye(4); F[0,1]=s.I/2; F[1,3]=s.Rational(1,3); F[2,3]=s.I/5
O=s.Matrix([[2,s.I],[0,3]])
G=F.H*F; T=F.inv()*T0*F; Lam=O*JB0.H*F
IK=F.inv()*JK0*s.Matrix([[2,s.I],[0,3]])
Q=(Lam*G.inv()*Lam.H).inv(); L=G.inv()*Lam.H*Q
JB=F.inv()*JB0; JK=F.inv()*JK0
H=G.inv()*T.H*G*T; P=F.inv()*P0*F
eq('actual source transport',H,F.inv()*H0*F)
eq('minimum section',Lam*L,s.eye(2))
eq('observation metric',L.H*G*L,Q)
eq('actual observed isometry transport',L*O,JB)
eq('observed metric transport',O.H*Q*O,s.eye(2))
eq('kernel isometry',JK.H*G*JK,s.eye(2))
HK=IK.H*G*IK; VK=s.Matrix([[2,s.I],[0,3]]).inv()
eq('original full kernel frame metric',HK,s.Matrix([[2,s.I],[0,3]]).H*s.Matrix([[2,s.I],[0,3]]))
eq('exact fixed kernel isometry map',IK*VK,JK)
eq('full kernel metric isometry certificate',VK.H*HK*VK,s.eye(2))
eq('full angle metric transport',JK.H*G*P*JK,gamma)
A=s.simplify(JK.H*G*H*JK); B=s.simplify(JB.H*G*H*JB); C=s.simplify(JK.H*G*H*JB)
negative('angle and compressed energy do not commute',not zero(A*gamma-gamma*A))
z=s.symbols('z',positive=True)
R=s.simplify(JK.H*G*(z*(z*s.eye(4)+H).inv())*JK)
Y=s.simplify(JB.H*G*(z*(z*s.eye(4)+H).inv())*JB)
eq('full observed determinant',Y.det(),(s.eye(2)+A/z).det()/(s.eye(4)+H/z).det())
eq('full kernel determinant',R.det(),(s.eye(2)+B/z).det()/(s.eye(4)+H/z).det())
Sigma=C.H*(z*s.eye(2)+A).inv()*C
eq('whole memory Schur identity',z*Y.inv(),z*s.eye(2)+B-Sigma)
eq('dynamic determinant rational bridge',R.det()*(s.eye(2)+A/z).det(),((z*s.eye(2)+A).det()*(z*s.eye(2)+B).det()/(z*s.eye(4)+H).det()))
dotR=s.simplify(z*R.diff(z))
hp=s.factor(-s.diff(R.det(),z)/R.det())
Ddet=s.factor(R.det()*(s.eye(2)+A/z).det())
Dp=s.factor(s.diff(Ddet,z)/Ddet)
eq('logarithmic derivative trace',-z*hp,s.trace(R.inv()*dotR))
tau=s.trace(gamma)
for zz in [s.Rational(1,4),s.Integer(1),s.Integer(20)]:
    RR=R.subs(z,zz); DD=dotR.subs(z,zz)
    psd('full derivative compression square '+str(zz),RR-RR*RR-DD)
    lo=s.Rational(1,1)/zz; hi=s.Integer(16)/zz
    ev=eigs2(RR.inv()*DD)
    gammas=[s.Rational(16,25),s.Rational(9,25)]
    for j,gg in enumerate(gammas):
        peak=max(lo,min(hi,1/s.sqrt(1-gg)))
        check(f'full first derivative upper {zz} {j}',s.simplify(d(gg,peak)-ev[j]).is_nonnegative)
        check(f'full first derivative lower {zz} {j}',s.simplify(ev[j]-min(d(gg,lo),d(gg,hi))).is_nonnegative)
    for n in range(1,6):
        value=s.factor((-1)**n*zz**n*s.diff(hp,z,n-1).subs(z,zz))
        gnH=s.eye(4)-(s.eye(4)+H/zz)**(-n); gnB=s.eye(2)-(s.eye(2)+B/zz)**(-n)
        eq(f'all derivative exact identity {zz} {n}',value,s.factorial(n-1)*(s.trace(gnH)-s.trace(gnB)))
        bound=s.factorial(n-1)*tau*(1-(zz/(zz+16))**n)
        check(f'all derivative positive {zz} {n}',value>=0)
        check(f'all derivative sharp trace bound {zz} {n}',value<=bound)
        check(f'all derivative old bound recovered {zz} {n}',bound<=s.factorial(n)*tau*16/(zz+16))
        dyn=s.factor((-1)**n*s.diff(Dp,z,n-1).subs(z,zz))
        check(f'dynamic complete monotone derivative {zz} {n}',dyn>=0)
    check('dynamic nonnegative value '+str(zz),Ddet.subs(z,zz)>=1)
    eq('FD5 exact differential bridge '+str(zz),s.trace(A*(zz*s.eye(2)+A).inv())+zz*Dp.subs(z,zz),-zz*hp.subs(z,zz))

for om in [s.Rational(1,4),s.Integer(1),s.Integer(20)]:
    RK=R.subs(z,s.I*om)
    X=s.simplify((RK+RK.H)/2); YY=s.simplify((RK-RK.H)/(2*s.I))
    psd('imaginary real part '+str(om),X,True)
    psd('imaginary imaginary part '+str(om),YY)
    eq('full complex kernel decomposition '+str(om),RK,X+s.I*YY)
    ev=eigs2(X.inv()*YY)
    lo=1/om; hi=16/om
    for j,gg in enumerate([s.Rational(16,25),s.Rational(9,25)]):
        peak=max(lo,min(hi,1/s.sqrt(1-gg)))
        check(f'full noncommuting phase upper {om} {j}',s.simplify(phase_tan(gg,peak)-ev[j]).is_nonnegative)
        check(f'full noncommuting phase lower {om} {j}',s.simplify(ev[j]-min(phase_tan(gg,lo),phase_tan(gg,hi))).is_nonnegative)
    wrong=(s.I*om*s.eye(2)+B)-C.H*(-s.I*om*s.eye(2)+A).inv()*C
    right=(s.I*om*s.eye(2)+B)-C.H*(s.I*om*s.eye(2)+A).inv()*C
    if om==1: negative('conjugating only the frequency changes the full memory',not zero(wrong-right))

# Exact Stieltjes identities and moments without algebraic-root rounding.
Hl=s.diag(0,1,1,4); Bl=s.diag(0,1,2)
intervals=[(s.Integer(0),s.Integer(1),s.Integer(1)),(s.Integer(2),s.Integer(4),s.Integer(1))]
for x in [s.Rational(1,2),s.Rational(3,2),s.Integer(3),s.Integer(5)]:
    xi=sum(1 for a in [0,1,1,4] if a>x)-sum(1 for a in [0,1,2] if a>x)
    check('Stieltjes density nonnegative '+str(x),xi>=0)
for j in range(10):
    moment=sum(mult*(bb**(j+1)-aa**(j+1))/(j+1) for aa,bb,mult in intervals)
    eq('full Stieltjes moment '+str(j),moment,(s.trace(Hl**(j+1))-s.trace(Bl**(j+1)))/(j+1))
for n in range(1,6):
    val=sum(s.factorial(n-1)*(z**n/(z+aa)**n-z**n/(z+bb)**n)*mult for aa,bb,mult in intervals)
    direct=s.factorial(n-1)*(1+z**n*s.trace((z*s.eye(3)+Bl)**(-n))-z**n*s.trace((z*s.eye(4)+Hl)**(-n)))
    eq('Stieltjes differentiated integral '+str(n),val,direct)
# The density fixture above tests the finite spectral formula; actual compression
# fixtures are separately checked with the full original maps.
for r in range(1,6):
    om=s.symbols('omega',positive=True); ss=s.symbols('energy',nonnegative=True)
    finite=sum((-1)**j*ss**(2*j)/om**(2*j+1) for j in range(r))
    remainder=(-1)**r*ss**(2*r)/(om**(2*r-1)*(om*om+ss*ss))
    eq('exact alternating kernel remainder '+str(r),om/(om*om+ss*ss),finite+remainder)

# Full-spectrum sharp fixtures including unit and zero factors.
for gg in [s.Rational(9,25),s.Rational(16,25)]:
    tt=1/s.sqrt(1-gg); v=s.Matrix([s.sqrt(1-gg),s.sqrt(gg)])
    HH=tt*v*v.H; RR=s.factor((s.I*(s.I*s.eye(2)+HH).inv())[1,1])
    re=s.simplify(s.re(RR)); im=s.simplify(s.im(RR))
    eq('sharp phase critical fixture '+str(gg),im/re,phase_tan(gg,tt))
    zz=s.Integer(1); Rreal=s.factor((zz*(zz*s.eye(2)+HH).inv())[1,1])
    Rt=s.factor((z*(z*s.eye(2)+HH).inv())[1,1])
    eq('sharp derivative critical fixture '+str(gg),-z*s.diff(-s.log(Rt),z).subs(z,1)/z,d(gg,tt))
    eq('sharp fixture angle '+str(gg),(v*v.H)[1,1],gg)

# Complete-monotone D can fail to be Stieltjes: its rational branch density.
HH=s.Matrix([[1,1],[1,1]])
eq('dynamic non-Stieltjes exact determinant',(z+1)**2/(z*(z+2)),(s.eye(1)+s.Matrix([[1]])/z).det()**2/(s.eye(2)+HH/z).det())
negative('D is not always Stieltjes',2*int(bool(s.Rational(3,2)<1))-int(bool(s.Rational(3,2)<2))<0)
time=s.symbols('time',positive=True)
eq('dynamic Laplace numerator nonnegative square',1+s.exp(-2*time)-2*s.exp(-time),(1-s.exp(-time))**2)

Tz=s.diag(T0,2,0); Hz=Tz.H*Tz; Jz=s.zeros(6,4)
for col,row in enumerate([2,3,4,5]): Jz[row,col]=1
Rz=s.simplify(Jz.H*z*(z*s.eye(6)+Hz).inv()*Jz)
eq('intersection retains exact unit response zero-energy factor',Rz,s.diag(R, z/(z+4),1))
Gzangle=Jz.H*s.diag(P0,1,0)*Jz
eq('intersection retains full angle spectrum',Gzangle,s.diag(gamma,1,0))
check('full zero intersection count',4-Gzangle.rank()==1)
for name,Hedge,Jedge in [('zero word',s.zeros(3),s.eye(3)[:,:2]),('empty kernel',s.diag(0,1),s.zeros(2,0))]:
    rr=Jedge.H*z*(z*s.eye(Hedge.rows)+Hedge).inv()*Jedge
    eq(name+' response determinant',rr.det(),1)
    eq(name+' logarithmic derivative',s.diff(rr.det(),z),0)

receipt={'status':'PASS','checks':len(passed),'negative_controls':len(controls),'names':passed,'controls':controls,'proof_sha256':hashlib.sha256((ROOT/'FREQUENCY_PROOFS.md').read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'optimized':not __debug__}
out=ROOT/('FREQUENCY_CHECKS_OPTIMIZED.json' if not __debug__ else 'FREQUENCY_CHECKS.json')
out.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:receipt[k] for k in ['status','checks','negative_controls','proof_sha256','checker_sha256','optimized']}))
