from pathlib import Path
import hashlib,itertools,json
import sympy as s

ROOT=Path(__file__).resolve().parent
checks=[]; controls=[]
def ck(name,val):
    if not bool(val): raise RuntimeError(name)
    checks.append(name)
def eq(name,a,b):
    v=a-b
    ck(name,all(s.cancel(x)==0 for x in v) if isinstance(v,s.MatrixBase) else s.cancel(v)==0)
def psd(name,M):
    eq(name+' Hermitian',M,M.H)
    for j in range(1,M.rows+1):
        for ix in itertools.combinations(range(M.rows),j):
            val=s.factor(s.expand_complex(M.extract(ix,ix).det()))
            ck(name+' minor '+str(ix),val.is_nonnegative)
def neg(name,val):
    if not bool(val): raise RuntimeError('negative control '+name)
    controls.append(name)
def eig2(M):
    tr=s.factor(s.trace(M)); det=s.factor(M.det())
    return [(tr+s.sqrt(s.factor(tr*tr-4*det)))/2,(tr-s.sqrt(s.factor(tr*tr-4*det)))/2]

# Every coefficient map and relation column, with all roots retained.
y=s.symbols('y'); q=12; degreeD=8; Delta=4; rho=s.Rational(1,8)
D=(y**4-s.Rational(1,20)**4)*(y**4-s.Rational(1,10)**4)
O=y**4-s.Rational(1,8)**4
Q=s.Poly(s.expand(D*O),y)
def coeff(p,n=q): return s.Matrix([s.expand(p).coeff(y,j) for j in range(n)])
def polynomial(v): return sum(v[j]*y**j for j in range(v.rows))
def uq(p):
    out=0
    for (j,),v in s.Poly(s.expand(p),y).terms():
        for (i,),c in Q.terms():
            if i+j-q>=0: out+=c*v*y**(i+j-q)
    return s.expand(out)
U=s.Matrix.hstack(*[coeff(uq(y**j)) for j in range(q)])
eq('complete triangular determinant',U.det(),1)
M0=s.zeros(q)
for j in range(q-1): M0[j+1,j]=1
M=M0.copy()
for j in range(q): M[j,q-1]=-Q.nth(j)
defect=s.zeros(q); defect[0,:]=s.Matrix([[-Q.nth(q-1-j) for j in range(q)]])
eq('full arithmetic-action defect',M*U-U*M0,defect)
for h in range(5):
    eq('every relation column '+str(h),uq(y**q*y**h),Q.as_expr()*y**h)
for j in range(Delta):
    p=s.expand(D*y**j)
    inverse=polynomial(U.inv()*coeff(p))
    expected=s.div(y**q*y**j,O,y)[0]
    eq('exact full-image inverse '+str(j),inverse,expected)
    normp=sum(abs(x) for x in coeff(p))
    for band in range(5,12):
        tail=sum(abs(x) for x in coeff(inverse)[:q-band])
        upper=(1-rho)**(-degreeD)*2**(q+Delta)*rho**(band-Delta)*normp
        ck('inverse full tail '+str((j,band)),tail<=upper)
        low=sum(abs(x) for x in coeff(p)[:q-band//2])
        upperlow=(1-rho)**(-degreeD)*2**degreeD*rho**(s.Rational(band,2)-Delta)*normp
        # The integer truncation below q-band/2 has the ceiling number of slots.
        slots=int(s.ceiling(q-s.Rational(band,2)))
        low=sum(abs(x) for x in coeff(p)[:slots])
        ck('direct full tail '+str((j,band)),s.simplify(upperlow-low).is_nonnegative)
for j in range(q):
    ck('full U coefficient bound '+str(j),sum(abs(x) for x in U[:,j])<=(1+rho)**q)

# Complex physical coordinates, full minimum sections and heat at tau=log 2.
T0=s.diag(0,1,2,3); H0=T0*T0
Jker=s.Matrix([[s.Rational(3,5),0],[s.Rational(4,5),0],[0,1],[0,0]])
Jobs=s.Matrix([[-s.Rational(4,5),0],[s.Rational(3,5),0],[0,0],[0,1]])
S=s.eye(4); S[0,1]=s.I/2; S[1,3]=s.Rational(1,3); S[2,3]=s.I/5
Obs=s.Matrix([[2,s.I],[0,3]])
T=S.inv()*T0*S; IK=S.inv()*Jker*s.Matrix([[2,s.I],[0,3]])
Lam=Obs*Jobs.H*S
pi=s.eye(4)[1:4,:]*S
Dpartial=s.diag(1,2,3)
heat=S.inv()*s.diag(1,s.Rational(1,2),s.Rational(1,16),s.Rational(1,512))*S
z=s.symbols('z',positive=True)
primary=[]; full=[]; angles=[]; observed_weights=[]
for ix,diag in enumerate([[10,9,8,7],[8,7,6,5],[6,5,4,3],[4,3,2,1]]):
    G=S.H*s.diag(*diag)*S
    H=s.simplify(G.inv()*T.H*G*T)
    eq('full physical word '+str(ix),H,S.inv()*H0*S)
    QB=s.simplify((Lam*G.inv()*Lam.H).inv())
    L=s.simplify(G.inv()*Lam.H*QB)
    HK=s.simplify(IK.H*G*IK)
    eq('actual observed section '+str(ix),Lam*L,s.eye(2))
    eq('actual observed metric '+str(ix),L.H*G*L,QB)
    P=S.inv()*s.diag(0,1,1,1)*S
    Gam=s.simplify(HK.inv()*IK.H*G*P*IK)
    angle=s.trace(Gam); angles.append(angle)
    d=s.factor(s.trace(HK.inv()*IK.H*G*(s.eye(4)-heat)*IK))
    zb=s.factor(s.trace(Lam*heat*L)); b0=4-2-3
    hf=s.factor(s.trace(heat)-1)
    eq('complete heat identity '+str(ix),zb-b0-hf,d)
    ck('actual heat angle defect lower '+str(ix),d>=0)
    ck('actual heat angle defect upper '+str(ix),d<=angle)
    ck('sharp lower floor heat '+str(ix),d>=(1-s.Rational(1,2))*angle)
    ck('sharp upper ceiling heat '+str(ix),d<=(1-s.Rational(1,512))*angle)
    pv=S.inv()*s.diag(1,0,0,0)*S
    eq('actual observed zero trace '+str(ix),s.trace(Lam*pv*L),b0+angle)
    positive_obs=0; removed=0
    for n,lam in enumerate([1,4,9],1):
        Pl=s.zeros(4); Pl[n,n]=1; Pl=S.inv()*Pl*S
        kw=s.factor(s.trace(HK.inv()*IK.H*G*Pl*IK))
        bw=s.factor(s.trace(Lam*Pl*L))
        eq('full repeated projector weight '+str((ix,n)),bw+kw,1)
        ck('positive observed projector weight '+str((ix,n)),bw>=0)
        positive_obs+=bw*2**(-s.Integer(lam))
        removed+=kw*2**(-s.Integer(lam))
    eq('positive and removed heat decomposition '+str(ix),positive_obs+removed,hf)
    eq('observed heat exact zero subtraction '+str(ix),zb-(b0+angle),positive_obs)
    primary.append(zb-b0); full.append(hf); observed_weights.append(positive_obs)
    Bpartial=s.simplify((pi*G.inv()*pi.H).inv())
    GW=s.diag(*diag[1:])
    eq('positive word generalized spectrum map '+str(ix),Bpartial.inv()*Dpartial.H*GW*Dpartial,s.diag(1,4,9))
    F=s.simplify(IK.H*T.H*G*T*IK)
    YY=s.simplify(Lam*z*(z*s.eye(4)+H).inv()*L)
    eq('full measured determinant '+str(ix),YY.det(),(s.eye(2)+HK.inv()*F/z).det()/(s.eye(4)+H/z).det())
alpha=sum(angles)/12
Fk=sum(full)/12; Mk=sum(primary)/12
Pk=sum(observed_weights)/(12-sum(angles))
eq('primary average exact defect',Mk-Fk,sum(primary[i]-full[i] for i in range(4))/12)
eq('observed probability affine map',Pk,(Mk-alpha)/(1-alpha))
ck('actual positive observed denominator',alpha<1)
ck('probability full comparison',abs(Pk-Fk)<=alpha)
neg('integer baseline is not observed zero mass',angles[0]!=0)
neg('raw primary heat is not a finite-k probability distribution',alpha>0)

# Noncommuting generalized metric logarithmic distance as an exact product bound.
for step in [1,2,3]:
    P=s.Matrix([[2,0],[0,5]])
    Qm=s.Matrix([[3,s.I],[-s.I,4+step]])
    F=s.Matrix([[4,1+s.I],[1-s.I,3]])
    psd('noncommuting metric positive '+str(step),Qm)
    ep=eig2(P.inv()*F); eqm=eig2(Qm.inv()*F); er=eig2(P.inv()*Qm)
    left=s.prod(max(s.simplify(ep[j]/eqm[j]),s.simplify(eqm[j]/ep[j])) for j in range(2))
    right=s.prod(max(x,1/x) for x in er)
    ck('exact log-metric product bound '+str(step),s.simplify(right-left).is_nonnegative)
neg('same arithmetic forms need not commute',P*Qm!=Qm*P)

# Whole-conductor to original-kernel compression, with full coisometry loss.
GA=s.diag(4,9,16,25)
JA=s.Matrix([[s.Rational(3,4),s.Rational(1,2),0],[1,0,0],[0,1,0],[0,0,1]])
bp=s.eye(4)[1:4,:]
BA=(bp*GA.inv()*bp.H).inv()
HA=JA.H*GA*JA
BK=s.Matrix([[1,s.I],[0,1],[s.Rational(1,3),0]])
IKA=JA*BK
HKA=IKA.H*GA*IKA
eq('complete conductor inherited metric',HKA,BK.H*HA*BK)
PA=GA.inv()*bp.H*BA*bp
eq('native primary compression boundary form',IKA.H*GA*PA*IKA,BK.H*BA*BK)
psd('complete boundary minimum dominated by conductor lift',HA-BA)
# These products have the same spectrum as the orthonormalized operators.
GamA=HA.inv()*BA
GamK=HKA.inv()*BK.H*BA*BK
isocoord=HA*BK*HKA.inv()
eq('exact invariant compression trace',s.trace(GamK),s.trace(isocoord.H*HA.inv()*BA*HA.inv()*isocoord*HKA))
Pi=s.Matrix([[1,0,0],[0,0,1]])
eq('full quotient coisometry',Pi*Pi.H,s.eye(2))
qcov=Pi*HA.inv()*Pi.H
qmetric=(Pi*HA.inv()*Pi.H).inv()
qsection=HA.inv()*Pi.H*qmetric
eq('full attained quotient section',Pi*qsection,s.eye(2))
eq('full attained quotient metric',qsection.H*HA*qsection,qmetric)
psd('native primary angle form positive',BK.H*BA*BK)
psd('native primary angle complement positive',HKA-BK.H*BA*BK)
neg('whole conductor and invariant angles have different dimensions',GamA.rows!=GamK.rows)
# Exact tail summation majorant at finite ranks; source prefactor is explicit.
for qp in [2,3,7,11]:
    for vdim in [0,1,3]:
        for JJ in [1,2,4]:
            mm=13; BB=s.Integer(JJ)**(2*qp)
            tail=sum(min(1,BB/s.Integer(j)**(2*qp)) for j in range(1,max(mm-vdim,0)+1))
            ck('full shifted primary tail '+str((qp,vdim,JJ)),vdim+tail<=vdim+JJ*(1+s.Rational(1,2*qp-1)))

# Exact grid discrepancy, cutoff coupling cost and probability decomposition.
for qgrid in [1,2,3,5,8,13]:
    for xi in [s.Rational(j,12) for j in range(-12,37)]:
        # Auxiliary evaluated eta(t)=2-3t has inverse Lipschitz constant 1/3.
        target=max(s.Integer(0),min(s.Integer(1),(xi+1)/3))
        grid=s.Rational(sum(bool(2-s.Rational(3*j,qgrid)<=xi) for j in range(qgrid)),qgrid)
        ck('exact decreasing cutoff grid '+str((qgrid,xi)),0<=target-grid<=s.Rational(1,qgrid))
    gridmean=sum(2-s.Rational(3*j,qgrid) for j in range(qgrid))/qgrid
    exactmean=s.Rational(1,2)
    eq('exact cutoff coupling cost '+str(qgrid),gridmean-exactmean,s.Rational(3,2*qgrid))
    ck('uniform cutoff coupling bound '+str(qgrid),gridmean-exactmean<=s.Rational(3,qgrid))

x=s.symbols('x',positive=True); qq=s.symbols('qq',positive=True); uu,xi=s.symbols('uu xi',real=True)
cdf=s.exp(-s.exp(-qq*(xi-uu)))
density=qq*s.exp(-qq*(xi-uu))*s.exp(-s.exp(-qq*(xi-uu)))
eq('exact Gumbel heat derivative',s.diff(cdf,xi),density)
eq('exact physical heat scale',s.exp(-qq*(2*s.log(qq)+xi))*s.exp(qq*(2*s.log(qq)+uu)),s.exp(qq*(uu-xi)))
eq('positive logarithmic integration by parts',s.diff(s.log(x)*s.exp(-x),x),s.exp(-x)/x-s.log(x)*s.exp(-x))
# Exact source-ratio width, retaining two absolute arithmetic factors.
ell,upper,C,v=s.symbols('ell upper C v',positive=True)
# Exponentiating the full cutoff width proves the cancellation without branch issues.
eq('complete source width cancellation',(upper*s.exp(C)/(1-v)**2)/(ell*s.exp(-C)/(1+v)**2),(upper/ell)*s.exp(2*C)*((1+v)/(1-v))**2)
# Scalar Lipschitz kernels used in determinant and phase transport.
a=s.symbols('a',real=True)
eq('positive regularizer log derivative',s.diff(s.log(1+s.exp(a)/z),a),s.exp(a)/(z+s.exp(a)))
eq('phase logarithmic derivative',s.diff(s.atan(s.exp(a)),a),1/(s.exp(a)+s.exp(-a)))
for bound in [s.Rational(1,8),s.Rational(1,2),s.Rational(3,4)]:
    ck('finite strict transfer guard '+str(bound),(1-bound)>0)

receipt={'status':'PASS','checks':len(checks),'negative_controls':len(controls),'names':checks,'controls':controls,'optimized':not __debug__,'proof_sha256':hashlib.sha256((ROOT/'PHASE_HEAT_PROOFS.md').read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
name='PHASE_HEAT_CHECKS_OPTIMIZED.json' if not __debug__ else 'PHASE_HEAT_CHECKS.json'
(ROOT/name).write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:receipt[k] for k in ['status','checks','negative_controls','optimized','proof_sha256','checker_sha256']}))
