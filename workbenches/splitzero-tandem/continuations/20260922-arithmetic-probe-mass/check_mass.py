from pathlib import Path
import hashlib, itertools, json, sys
from functools import lru_cache
import sympy as s

ROOT = Path(__file__).resolve().parent
checks = []
controls = []
def check(name, truth):
    if not bool(truth):
        raise RuntimeError(name)
    checks.append(name)
def zero(M):
    return all(s.simplify(x) == 0 for x in M)
def equal(name, a, b):
    check(name, zero(a-b) if isinstance(a, s.MatrixBase) else s.simplify(a-b)==0)
def psd(name, M):
    check(name+' Hermitian', zero(M-M.H))
    for size in range(1,M.rows+1):
        for ix in itertools.combinations(range(M.rows),size):
            x=s.simplify(M.extract(ix,ix).det())
            check(name+' minor '+str(ix), x.is_nonnegative)
def control(name, truth):
    if not bool(truth):
        raise RuntimeError('negative control failed: '+name)
    controls.append(name)
def weights(r):
    ss=[s.Rational(1,2**i) for i in range(r)]
    base=(-1)**(r-1)*s.prod(ss)/sum(1/x for x in ss)
    return [s.factor(base/(ss[i]**2*s.prod(ss[i]-ss[j] for j in range(r) if i!=j))) for i in range(r)]
def S(r,x):
    return sum(1/(1+x/s.Integer(2)**i) for i in range(r))
def ratio(r,x):
    return s.factor(s.Rational(1,2**(r+1))*(1+x)/(1+x/s.Integer(2)**r)*S(r,x/2)/S(r,x))
def psi(r,c,sigma):
    nodes=[sigma/s.Integer(2)**i for i in range(r)]
    return s.factor(c**(r-1)*s.prod(nodes)*sum(1/(1+c*x) for x in nodes)/(sum(1/x for x in nodes)*s.prod(1+c*x for x in nodes)))
def delta(r,ss):
    return s.Rational(r,2**r-1)*s.Rational(1,2**(r*(r-1)//2))*ss**(r+1)
def refined(r,ss):
    return s.Rational(1,2**r-1)*s.Rational(1,2**(r*(r-1)//2))*s.Rational(r,r+1)**(r+1)*ss**(r+1)
def extrap(r,sigma,mass):
    out=s.zeros(mass(sigma).rows)
    for i,w in enumerate(weights(r)):
        out += w*mass(sigma/s.Integer(2)**i)
    return s.simplify(out)

for r in range(1,13):
    w=weights(r)
    equal(f'r{r} total coefficient',sum(w),1)
    for j in range(2,r+1):
        equal(f'r{r} moment{j}',sum(w[i]/s.Integer(2)**(i*j) for i in range(r)),0)
    ar=sum(abs(v) for v in w)
    equal(f'r{r} exact absolute sum',ar,s.prod((1+s.Rational(1,2**j))/(1-s.Rational(1,2**j)) for j in range(2,r+1)))
    check(f'r{r} coefficient bound',ar<3)
    theta=ratio(r,s.Integer(1)); chi=s.Rational(1,2**(r+1))
    equal(f'r{r} endpoint theta',theta,S(r,s.Rational(1,2))/((2**r+1)*S(r,s.Integer(1))))
    equal(f'r{r} endpoint chi',ratio(r,s.Integer(0)),chi)
    check(f'r{r} theta bound',theta<=s.Rational(4,3*(2**r+1)))
    check(f'r{r} positive lower guard',theta*delta(r,s.Integer(1))/(1-theta)<1)
    previous=chi
    for j in range(10):
        x=s.Rational(j,9)
        current=ratio(r,x)
        check(f'r{r} increasing ratio{j}',previous<=current<=theta)
        previous=current
    for c in [s.Rational(1,20),s.Rational(1,4),s.Rational(2,5),s.Rational(3,4),s.Integer(1)]:
        for sigma in [s.Rational(1,2),s.Integer(1)]:
            direct=sum(w[i]*(sigma/s.Integer(2)**i)**2/(1+c*sigma/s.Integer(2)**i)**2 for i in range(r))
            exact=psi(r,c,sigma)
            equal(f'r{r} psi c{c} sigma{sigma}',direct,exact)
            check(f'r{r} psi positivity c{c} sigma{sigma}',exact>0)
            equal(f'r{r} ratio identity c{c} sigma{sigma}',psi(r,c,sigma/2)/exact,ratio(r,c*sigma))
            check(f'r{r} old delta c{c} sigma{sigma}',exact<=delta(r,sigma))
            check(f'r{r} block delta c{c} sigma{sigma}',c*(1-c)*exact<=refined(r,sigma))
    for t in [s.Integer(0),chi,theta]:
        coeff=[((w[i-1] if i else 0)-t*(w[i] if i<r else 0))/(1-t) for i in range(r+1)]
        equal(f'r{r} interval coefficients t{t}',sum(coeff),1)
        equal(f'r{r} interval absolute sum t{t}',sum(abs(x) for x in coeff),ar*(1+t)/(1-t))

equal('theta1',ratio(1,s.Integer(1)),s.Rational(4,9))
equal('theta2',ratio(2,s.Integer(1)),s.Rational(44,175))
equal('theta3',ratio(3,s.Integer(1)),s.Rational(212,1593))
equal('r3 weights',s.Matrix(weights(3)),s.Matrix([s.Rational(1,21),-s.Rational(4,7),s.Rational(32,21)]))
check('delta8 decimal guard',delta(8,s.Integer(1))<s.Rational(12,10**11))
check('delta16 decimal guard',delta(16,s.Integer(1))<s.Rational(2,10**40))

def original(T,G,Lam,J):
    H=s.simplify(G.inv()*T.H*G*T)
    Q=s.simplify((Lam*G.inv()*Lam.H).inv())
    L=s.simplify(G.inv()*Lam.H*Q)
    v=T.nullspace()
    V=s.Matrix.hstack(*v) if v else s.zeros(T.rows,0)
    Pv=V*(V.H*G*V).inv()*V.H*G if v else s.zeros(T.rows)
    P=s.simplify(s.eye(T.rows)-Pv)
    Gamma=s.simplify(J.H*G*P*J)
    @lru_cache(maxsize=None)
    def mass(sigma):
        Hf=s.simplify(H*(sigma*s.eye(H.rows)+H).inv())
        A=s.simplify(J.H*G*Hf*J)
        return s.simplify(A.inv()*(J.H*G*Hf*Hf*J)*A.inv()) if J.cols else s.zeros(0)
    return H,Q,L,P,Gamma,mass

T=s.diag(0,1,2); G=s.eye(3)
Lam=s.Matrix([[-2,5,0],[-1,0,5]])
IK=s.Matrix([5,2,1]); HK=(IK.H*G*IK)[0]
# One-dimensional coordinate formula avoids introducing an irrational isometry.
H=T.H*T; Q=(Lam*Lam.H).inv(); L=Lam.H*Q
gamma=s.Rational(1,6)
def fixture_mass(sigma):
    return s.Matrix([[6+s.Rational(27,50)*sigma**2/(1+s.Rational(2,5)*sigma)**2]])
def obs_mass(sigma):
    Hf=s.diag(0,1,1) if sigma==0 else H*(sigma*s.eye(3)+H).inv()
    E=(IK.H*Hf*IK)[0]; X=IK.H*Hf*L
    return s.simplify(Q+X.H*(HK/E**2)*X)
equal('fixture HK',HK,30)
equal('fixture angle', (IK.H*s.diag(0,1,1)*IK)[0]/HK,gamma)
for sigma in [s.Rational(1,8),s.Rational(1,4),s.Rational(1,2),s.Integer(1),s.Integer(2)]:
    Hf=H*(sigma*s.eye(3)+H).inv(); E=(IK.H*Hf*IK)[0]
    equal('fixture exact mass '+str(sigma),HK*(IK.H*Hf*Hf*IK)[0]/E**2,fixture_mass(sigma)[0])
    equal('fixture observed determinant '+str(sigma),obs_mass(sigma).det()/Q.det(),fixture_mass(sigma)[0])
old=extrap(3,s.Integer(1),fixture_mass)[0]; half=extrap(3,s.Rational(1,2),fixture_mass)[0]
th=ratio(3,s.Integer(1)); ch=s.Rational(1,16)
lo=s.factor((half-th*old)/(1-th)); up=s.factor((half-ch*old)/(1-ch))
equal('fixture R3',old,s.Rational(1992825,332024))
equal('fixture U3',half,s.Rational(7968825,1328096))
equal('fixture L3',lo,s.Rational(1572060375,262014368))
equal('fixture original interval ratio',half/lo,s.Rational(48910877,48908545))
check('fixture strengthened interval',lo<6<up<half)
equal('fixture strengthened upper exact value',up,s.Rational(284595,47432))
print('SHARP_UPPER',up)
equal('observed monotonicity determinant',(obs_mass(1)-obs_mass(s.Rational(1,2))).det(),-s.Rational(1,3136))
equal('observed extrapolation determinant',((4*obs_mass(s.Rational(1,2))-obs_mass(1))/3-obs_mass(0)).det(),-s.Rational(4,11025))
control('observed matrices cannot replace common kernel matrices',(obs_mass(1)-obs_mass(s.Rational(1,2))).det()<0)
Hf=H*(s.eye(3)+H).inv(); E=(IK.H*Hf*IK)[0]; X=IK.H*Hf*L
control('middle kernel metric cannot be omitted',s.simplify((Q+X.H*X/E**2).det()/Q.det()-fixture_mass(s.Integer(1))[0])!=0)

# Complex nonunitary transport preserves all original source and target forms.
B=s.Matrix([[1,0,1,1,0],[0,2,1,0,1],[1,1,0,1,1]])
T0=B.col_join(s.zeros(2,5)); J0=s.eye(5)[:,3:5]; LB=s.eye(5)[:,0:3]
Smat=s.eye(5); Smat[0,1]=s.I; Smat[1,2]=s.Rational(1,2); Smat[2,4]=s.I/3; Smat[3,4]=s.Rational(1,5)
O=s.Matrix([[2,s.I,0],[0,1,1],[0,0,3]])
G=Smat.H*Smat; T=Smat.inv()*T0*Smat; J=Smat.inv()*J0; Lam=O*LB.H*Smat
H,Q,L,P,Gamma,mass=original(T,G,Lam,J)
equal('nonidentity metric isometry',J.H*G*J,s.eye(2))
equal('original observation section',Lam*L,s.eye(3))
equal('original observation metric',L.H*G*L,Q)
equal('nonunitary observation transport',O.H*Q*O,s.eye(3))
equal('full source conjugate transport',H,Smat.inv()*(T0.H*T0)*Smat)
check('nonidentity source retained',not zero(G-s.eye(5)))
check('nonidentity observation retained',not zero(Q-s.eye(3)))
psd('Gamma positive',Gamma)
Ainv=Gamma.inv()
pos=B*B.H
l=s.factor(pos.det()/s.trace(pos)**2)
sigma=l
equal('positive rank',T.rank(),3)
check('finite original positive floor',l>0)
for sig in [sigma,sigma/2,sigma/4,sigma/8]:
    M=mass(sig)
    psd('mass-angle lower '+str(sig),M-Ainv)
    kap=1+(sig/l)**2/(4*(1+sig/l))
    psd('mass sharper upper '+str(sig),kap*Ainv-M)
control('kernel masses need not commute',not zero(mass(sigma)*mass(sigma/2)-mass(sigma/2)*mass(sigma)))
for r in [1,2,3]:
    R=extrap(r,sigma,mass); Rh=extrap(r,sigma/2,mass)
    th=ratio(r,s.Integer(1)); ch=s.Rational(1,2**(r+1)); D=R-Rh
    LL=s.simplify((Rh-th*R)/(1-th)); UU=s.simplify((Rh-ch*R)/(1-ch))
    psd(f'matrix r{r} positive error',R-Ainv)
    psd(f'matrix r{r} lower contraction',Rh-Ainv-ch*(R-Ainv))
    psd(f'matrix r{r} upper contraction',th*(R-Ainv)-(Rh-Ainv))
    psd(f'matrix r{r} improved delta',refined(r,s.Integer(1))*Ainv-(R-Ainv))
    psd(f'matrix r{r} lower positive',LL)
    psd(f'matrix r{r} lower enclosure',Ainv-LL)
    psd(f'matrix r{r} upper enclosure',UU-Ainv)
    equal(f'matrix r{r} interval gap',UU-LL,(th-ch)/((1-th)*(1-ch))*D)
    check(f'matrix r{r} defect rank',D.rank()<=1)
    equal(f'matrix r{r} exact determinant width',UU.det()/LL.det(),(s.eye(2)+(th-ch)/((1-th)*(1-ch))*LL.inv()*D).det())
    eta=s.Rational(1,1000)
    noisy=[(1+(-1)**i*eta)*mass(sigma/s.Integer(2)**i) for i in range(r+1)]
    endpoints=[]
    for tt in [th,ch]:
        w=weights(r); cc=[((w[i-1] if i else 0)-tt*(w[i] if i<r else 0))/(1-tt) for i in range(r+1)]
        kappas=[1+s.Rational(1,2**i)**2/(4*(1+s.Rational(1,2**i))) for i in range(r+1)]
        ee=sum(abs(cc[i])*eta*kappas[i] for i in range(r+1))
        approx=s.zeros(2)
        for i in range(r+1): approx+=cc[i]*noisy[i]
        exact=LL if tt==th else UU
        psd(f'matrix r{r} noisy positive t{tt}',approx)
        psd(f'matrix r{r} noisy upper t{tt}',ee*Ainv-(approx-exact))
        psd(f'matrix r{r} noisy lower t{tt}',ee*Ainv+(approx-exact))
        endpoints.append(approx/(1+ee) if tt==th else approx/(1-ee))
    psd(f'matrix r{r} certificate lower',Ainv-endpoints[0])
    psd(f'matrix r{r} certificate upper',endpoints[1]-Ainv)

# Construct the single realization metric from moment Grams.
Ybasis=s.Matrix([[2,s.I],[0,3]])
Ab=s.diag(s.Rational(9,16),s.Rational(7,9))
C1=s.Matrix([[1,s.I,1],[0,1,2]])/10
Ast=Ybasis.inv()*Ab*Ybasis
Cst1=Ybasis.inv()*C1
BR=C1.H*Ybasis
M0=BR*Cst1
Cselect=Cst1[:,0:2]
Hselect=M0[0:2,0:2]
Pstar=s.simplify(Cselect.H.inv()*Hselect*Cselect.inv())
equal('recovered common realization metric',Pstar,Ybasis.H*Ybasis)
equal('recovered energy is metric selfadjoint',Pstar*Ast,Ast.H*Pstar)
equal('recovered input-output metric relation',Pstar*Cst1,BR.H)
Fstar=Ybasis.inv()*s.diag(s.Rational(5,4),s.Rational(4,3))*Ybasis
equal('recovered positive square-root functional identity',Fstar*Fstar,s.eye(2)+Ast)
equal('recovered square root metric selfadjoint',Pstar*Fstar,Fstar.H*Pstar)
Cbar=s.diag(s.Rational(5,4),s.Rational(4,3))*C1
Cstar=Fstar*Cst1
Bbar=Cbar.H*Ab.inv()*Cbar+s.eye(3)/10
Zanchor=Bbar-C1.H*C1
Brec=s.simplify(Zanchor+Cst1.H*Pstar*Cst1)
equal('recovered original observed energy',Brec,Bbar)
Ebase=Bbar.row_join(Cbar.H).col_join(Cbar.row_join(Ab))
Erec=Brec.row_join(Cstar.H*Pstar).col_join((Pstar*Cstar).row_join(Pstar*Ast))
Iso=s.diag(s.eye(3),Ybasis)
equal('recovered full energy pullback',Erec,Iso.H*Ebase*Iso)
Gbase=s.diag(Q,s.eye(2)); Grec=s.diag(Q,Pstar)
equal('recovered full source pullback',Grec,Iso.H*Gbase*Iso)
equal('recovered filtered physical operator',Grec.inv()*Erec,Iso.inv()*Gbase.inv()*Ebase*Iso)
# The full boundary covariance and original fixed coefficient volume.
F=s.Matrix([[2,s.I],[0,3]]); IK=J*F; HK=IK.H*G*IK
pi=B*Smat; Cp=pi*G.inv()*pi.H; Jp=pi*IK; Bp=s.simplify(Jp.H*Cp.inv()*Jp)
equal('full boundary minimum form',Bp,IK.H*G*P*IK)
equal('native determinant exact factor',HK.det(),Bp.det()*Ainv.det())
eps=s.Rational(1,100); Ctilde=(1+eps)*Cp; Btilde=Jp.H*Ctilde.inv()*Jp
psd('boundary covariance lower certificate',Bp-(1-eps)*Btilde)
psd('boundary covariance upper certificate',(1+eps)*Btilde-Bp)
for scale in [s.Integer(4),s.Integer(3),s.Integer(2),s.Integer(1)]:
    equal('scaled original boundary factor '+str(scale),(scale*HK).det(),(scale*Bp).det()*Ainv.det())
equal('four signed original determinant transfer',(4*HK).det()*(3*HK).det()/((2*HK).det()*HK.det()),(4*Bp).det()*(3*Bp).det()/((2*Bp).det()*Bp.det()))

# Complementary Schur map, computed without choosing eigenvalue phases.
R=P*J
vb=T.nullspace(); VV=s.Matrix.hstack(*vb)
constraints=s.Matrix.vstack(R.H*G,VV.H*G)
nn=constraints.nullspace(); N=s.Matrix.hstack(*nn)
Er=R.H*G*H*R; cross=R.H*G*H*N
Sigform=N.H*G*H*N-cross.H*Er.inv()*cross
sigdet=s.factor(Sigform.det()/(N.H*G*N).det())
AK=J.H*G*H*J; ascalar=s.factor(AK.det()/pos.det())
equal('scalar leading coefficient complementary map',ascalar,Gamma.det()/sigdet)

# Intersections, unit-angle invisible memory, zero words and empty kernels.
Tz=s.diag(T0,s.Integer(2),s.Integer(0)); Gz=s.eye(7); Lamz=s.eye(7)[:3,:]
Jz=s.eye(7)[:,3:6]
Hz,Qz,Lz,Pz,Gzangle,mz=original(Tz,Gz,Lamz,Jz)
equal('invisible positive angle retained',Gzangle,s.diag(Gamma,s.Integer(1)))
equal('invisible positive mass retained',mz(sigma),s.diag(mass(sigma),s.Integer(1)))
IKz=s.eye(7)[:,3:7]; fullangle=IKz.H*Pz*IKz
equal('zero intersection nullity',4-fullangle.rank(),1)
equal('positive quotient full dimension',Gzangle.rows,3)
for name,Tedge,Ledge,Jedge in [
 ('empty kernel',s.diag(0,1),s.eye(2),s.zeros(2,0)),
 ('zero word',s.zeros(2),s.Matrix([[1,0]]),s.zeros(2,0))]:
    _,_,_,_,ga,ma=original(Tedge,s.eye(2),Ledge,Jedge)
    equal(name+' positive determinant',ga.det(),1)
    equal(name+' mass determinant',ma(s.Integer(1)).det(),1)
control('analytic defect rank does not bound independent full-rank noise',(s.Rational(101,100)*s.eye(3)).det()!=1)
for a in [s.Rational(1,3),s.Integer(2),s.Integer(7)]:
    Tcone=s.diag(0,1); Gcone=s.diag(1,a); Lcone=s.Matrix([[1,0]])
    Hc,Qc,Lc,Pc,Gac,mc=original(Tcone,Gcone,Lcone,s.Matrix([0,1/s.sqrt(a)]))
    equal('invisible metric cone response '+str(a),(Lcone*(s.eye(2)+Hc).inv()*Lc)[0],1)
    equal('invisible metric cone mass '+str(a),mc(s.Integer(1))[0],1)
    equal('invisible metric cone angle '+str(a),Gac[0],1)
    equal('invisible metric cone original volume '+str(a),(s.Matrix([0,1]).H*Gcone*s.Matrix([0,1]))[0],a)

receipt={'status':'PASS','checks':len(checks),'negative_controls':len(controls),'check_names':checks,'controls':controls,'fixture_sharp_upper':str(up),'proof_sha256':hashlib.sha256((ROOT/'MASS_PROOFS.md').read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'optimized':not __debug__}
name='MASS_CHECKS_OPTIMIZED.json' if not __debug__ else 'MASS_CHECKS.json'
(ROOT/name).write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:receipt[k] for k in ['status','checks','negative_controls','fixture_sharp_upper','proof_sha256','checker_sha256','optimized']}))
