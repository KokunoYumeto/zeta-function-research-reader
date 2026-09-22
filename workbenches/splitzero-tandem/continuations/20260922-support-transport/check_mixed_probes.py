"""Exact finite tests of canonical mixed probes and complete hidden returns."""
from pathlib import Path
from math import comb
import sympy as s
import json

P=Path(__file__).resolve().parent
checks=[]
negatives=[]
def eq(name,left,right):
    delta=left-right
    vals=list(delta) if isinstance(delta,s.MatrixBase) else [delta]
    if not all(s.cancel(v)==0 for v in vals):
        raise ArithmeticError(name+': '+str(delta))
    checks.append(name)
def reject(name,residual):
    vals=list(residual) if isinstance(residual,s.MatrixBase) else [residual]
    if all(s.cancel(v)==0 for v in vals):
        raise ArithmeticError('Negative control failed: '+name)
    negatives.append(name)

q=6;n=5;dH=q-2
epsilon=s.Integer(9)
e=s.eye(q)[:,0];f=s.eye(q)[:,1]
Pi=e*e.H+f*f.H;PH=s.eye(q)-Pi;R=epsilon*f*e.H
def rotation(i,j,c,t):
    O=s.eye(q);O[i,i]=O[j,j]=c;O[i,j]=-t;O[j,i]=t
    return O
O=(rotation(0,2,s.Rational(3,5),s.Rational(4,5))
   *rotation(1,3,s.Rational(5,13),s.Rational(12,13))
   *rotation(2,4,s.Rational(8,17),s.Rational(15,17))
   *rotation(3,5,s.Rational(7,25),s.Rational(24,25))
   *rotation(0,1,s.Rational(20,29),s.Rational(21,29))
   *rotation(4,5,s.Rational(9,41),s.Rational(40,41)))
O=s.diag(1,s.I,1,-s.I,1,1)*O
J=O[:,:n];PB=J*J.H;K=s.eye(q)-PB
u=J.H*e;v=J.H*f
a=(u.H*u)[0];beta=(v.H*v)[0];r=(u.H*v)[0]
A=J.H*Pi*J;Z=(s.eye(n)-A)/dH;ss=s.trace(Z);RB=J.H*R*J
WB=s.I*(RB-RB.H)
eq('original fixture isometry',J.H*J,s.eye(n))
eq('actual fixture observation projector',PB*PB,PB)
eq('MP5 complete hidden trace',ss,1-s.trace(PH*K)/dH)
eq('MP5 original observed support trace',ss,(n-a-beta)/dH)

def average_family(basis):
    names=('T','T2','adj2','pos1','pos2','xy','yx','hidden2',
           'hiddenpos1','hiddenpos2','hiddenxy','hiddenyx',
           'hiddenxadjx','hiddenyadjy','hiddenxxadj','hiddenyyadj')
    avg={name:s.zeros(n) for name in names}
    for j in range(dH):
      for phase in (1,s.I,-1,-s.I):
        g=phase*basis[:,j]
        X=3*f*g.H;Y=3*g*e.H;T=X+Y
        XB=J.H*X*J;YB=J.H*Y*J;TB=XB+YB
        eq(f'complete cubic square {j},{phase}',T*T,R)
        eq(f'complete cubic cube {j},{phase}',T*T*T,s.zeros(q))
        terms={
         'T':TB,'T2':TB*TB,'adj2':TB.H*TB.H,
         'pos1':TB.H*TB,'pos2':TB*TB.H,'xy':XB*YB,'yx':YB*XB,
         'hidden2':J.H*T*K*T*J,
         'hiddenpos1':J.H*T.H*K*T*J,'hiddenpos2':J.H*T*K*T.H*J,
         'hiddenxy':J.H*X*K*Y*J,'hiddenyx':J.H*Y*K*X*J,
         'hiddenxadjx':J.H*X.H*K*X*J,'hiddenyadjy':J.H*Y.H*K*Y*J,
         'hiddenxxadj':J.H*X*K*X.H*J,'hiddenyyadj':J.H*Y*K*Y.H*J}
        for name,term in terms.items():
            avg[name]+=term/(4*dH)
    return {key:value.applyfunc(s.cancel) for key,value in avg.items()}

basis=s.eye(q)[:,2:]
avg=average_family(basis)
eq('canonical first moment vanishes',avg['T'],s.zeros(n))
eq('MP11 complete square',avg['T2'],ss*RB+epsilon*r*Z)
eq('MP11 adjoint complete square',avg['adj2'],ss*RB.H+epsilon*s.conjugate(r)*Z)
eq('MP12 first positive moment',avg['pos1'],epsilon*(beta*Z+ss*u*u.H))
eq('MP12 second positive moment',avg['pos2'],epsilon*(a*Z+ss*v*v.H))
eq('MP13 full hidden square return',avg['hidden2'],(1-ss)*RB-epsilon*r*Z)
eq('MP14 first positive hidden return',avg['hiddenpos1'],epsilon*((1-beta)*Z+(1-ss)*u*u.H))
eq('MP14 second positive hidden return',avg['hiddenpos2'],epsilon*((1-a)*Z+(1-ss)*v*v.H))
eq('MP15 ordered product',avg['xy'],ss*RB)
eq('MP15 reverse product',avg['yx'],epsilon*r*Z)
eq('MP16 ordered hidden return',avg['hiddenxy'],(1-ss)*RB)
eq('MP16 reverse hidden return',avg['hiddenyx'],-epsilon*r*Z)
eq('MP17 positive hidden X*X',avg['hiddenxadjx'],epsilon*(1-beta)*Z)
eq('MP17 positive hidden Y*Y',avg['hiddenyadjy'],epsilon*(1-ss)*u*u.H)
eq('MP17 positive hidden XX*',avg['hiddenxxadj'],epsilon*(1-ss)*v*v.H)
eq('MP17 positive hidden YY*',avg['hiddenyyadj'],epsilon*(1-a)*Z)
cord=s.I*(avg['xy']-avg['xy'].H)
csq=s.I*(avg['T2']-avg['adj2'])
eq('MP19 exact ordered current',cord,ss*WB)
eq('MP20 ordered current recovery',cord/ss,WB)
eq('MP21 square current trace',s.trace(csq),2*ss*s.trace(WB))
eq('MP21 unordered current recovery',csq/ss-s.trace(csq)*Z/(2*ss**2),WB)
eq('complete hidden signed return',s.I*(avg['hidden2']-avg['hidden2'].H),
   (1-ss)*WB-s.trace(WB)*Z)

# A complete unitary change of auxiliary basis leaves every displayed average.
U=s.diag(1,s.I,-1,-s.I)*s.Matrix([[1,1,1,1],[1,-1,1,-1],
                              [1,1,-1,-1],[1,-1,-1,1]])/2
eq('complex change of full auxiliary basis',U.H*U,s.eye(dH))
changed=average_family(basis*U)
for name in avg:
    eq('basis-independent average '+name,changed[name],avg[name])

positive=avg['pos1']+avg['pos2'];t=s.trace(A)
scaled=positive*dH/epsilon
eq('MP25 exact support polynomial',scaled,t*s.eye(n)+(n-2*t)*A)
eq('MP25 exact support trace',s.trace(positive),2*epsilon*t*(n-t)/dH)
disc=s.cancel(n*n-2*dH*s.trace(positive)/epsilon)
found_t=s.cancel((n-s.sqrt(disc))/2)
eq('MP26 correct support trace branch',found_t,t)
eq('MP26 actual measured support recovered',(scaled-found_t*s.eye(n))/(n-2*found_t),A)
eq('actual support nonidempotence retained',A-A*A,J.H*Pi*K*Pi*J)

# The operator-norm inverse constant is attained on a top Z eigenvector.
null=A.nullspace()[0]
bvec=null/s.sqrt((null.H*null)[0])
Eerr=2*bvec*bvec.H-s.eye(n)
eq('MP22 extremal Hermitian error norm certificate',Eerr*Eerr,s.eye(n))
eq('MP22 actual top Z direction',Z*bvec,bvec/dH)
inv=Eerr/ss-s.trace(Eerr)*Z/(2*ss**2)
eq('MP22 sharp inverse norm achieved',(bvec.H*inv*bvec)[0],
   1/ss+(n-2)/(2*dH*ss**2))

# Exact coordinate transport through a nonunitary source frame.
F=s.diag(2,3,s.Rational(1,2),5,7,s.Rational(2,3))
F[0,2]=s.Rational(1,3);F[1,4]=s.I/4
G=F.H*F;Jc=F.inv()*J;ec=F.inv()*e;fc=F.inv()*f
Pc=Jc*Jc.H*G
eq('nonunitary original metric isometry',Jc.H*G*Jc,s.eye(n))
eq('nonunitary original metric observation',Pc,F.inv()*PB*F)
gc=F.inv()*basis[:,0]
Tc=3*(fc*gc.H*G+gc*ec.H*G)
T=3*(f*basis[:,0].H+basis[:,0]*e.H)
eq('nonunitary full mixed operator',Tc,F.inv()*T*F)
eq('nonunitary observed mixed operator',Jc.H*G*Tc*Jc,J.H*T*J)

reject('conjugating the reverse-product scalar',avg['yx']-epsilon*s.conjugate(r)*Z)
reject('dropping the unordered trace contamination',csq-ss*WB)
reject('identifying observation with an algebra map',avg['hidden2'])
reject('replacing actual support by an idempotent',A*A-A)
single=3*(v*(J.H*basis[:,0]).H+(J.H*basis[:,0])*u.H)
reject('using one auxiliary vector as the canonical family',single*single-avg['T2'])

# Exact blind-support obstruction: all observed cubic probes vanish but
# the observed current in the original supported plane is nonzero.
Jblind=s.eye(q)[:,:2]
for j in range(dH):
    Tg=3*(f*basis[:,j].H+basis[:,j]*e.H)
    eq(f'blind support mixed probe {j}',Jblind.H*Tg*Jblind,s.zeros(2))
reject('declaring blind mixed probes imply zero original current',
       s.I*Jblind.H*(R-R.H)*Jblind)

# The actual five-orbit rank count, checked exactly in every residue class.
def count_weights(k):
    ans=[0]*5
    for n1 in range(k+1):
      for n2 in range(k-n1+1):
        for n3 in range(k-n1-n2+1):
          n4=k-n1-n2-n3
          ans[(n1+2*n2+3*n3+4*n4)%5]+=1
    return ans
def ep(k):return 1 if k%5==0 else (-1 if k%5==1 else 0)
for k in range(2,36):
    raw=count_weights(k);small=count_weights(k-2)
    for residue in range(5):
        formula=(comb(k+3,3)+(4 if residue==0 else -1)*ep(k))//5
        eq(f'OCS32 complete degree {k} weight {residue}',raw[residue],formula)
    eq(f'OCS32 native lower-rank count {k}',raw[0]-max(small),
       ((k+1)**2)//5+(1 if k%5==0 else 0))
for k in range(17,202,4):
    qq=(k+1)**2;rank=qq//5+(1 if k%5==0 else 0)
    amplification=s.Rational(qq-2,rank-2)
    if not (amplification<=s.Rational(1610,309)<6):
        raise ArithmeticError('Native rank amplification bound failed')
    checks.append(f'MP24 exact native recovery bound k={k}')

receipt={'exact_check_count':len(checks),'exact_checks':checks,
         'negative_controls':negatives,
         'scope':'Complete finite complex mixed-family averages, adjoints, all hidden returns, positive support inversion, sharp Hermitian current inverse, source-frame transport, and exact five-orbit rank counts. Finite matrices are auxiliary; no native period matrix or terminal sign is inferred.'}
(P/'MIXED_PROBE_VERIFICATION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'exact_check_count':len(checks),'negative_controls':negatives},indent=2))
