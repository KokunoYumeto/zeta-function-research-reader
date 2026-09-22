from pathlib import Path
import sympy as s,json,hashlib
P=Path(__file__).parent;I=s.I;z=s.symbols('z',positive=True);count=0;negative_controls=0;fixtures=[]
def eq(a,b,label):
 global count
 if isinstance(a,s.MatrixBase):
  if a.shape!=b.shape or any(s.cancel(x)!=0 for x in a-b):raise ArithmeticError(label)
 elif s.cancel(a-b)!=0:raise ArithmeticError(label)
 count+=1
def clean(a):return a.applyfunc(s.cancel)
def psd(a,label):
 from itertools import combinations
 eq(a,a.H,label+' Hermitian')
 for k in range(1,a.rows+1):
  for inds in combinations(range(a.rows),k):
   d=s.factor(a.extract(inds,inds).det())
   if d.is_nonnegative is not True:raise ArithmeticError(f'{label} minor {inds}: {d}')
   global count
   count+=1
tests=[
 ('complex crossing',s.Matrix([[1,I,0],[0,2,1],[1,0,0]]),2),
 ('rank intersecting',s.Matrix([[0,1,0,0],[0,0,I,0],[0,0,0,0],[0,0,0,0]]),2),
 ('repeated energies',s.diag(0,2,2,0),2),
 ('nonnormal word',s.Matrix([[1,0,I,0],[1,2,0,I],[0,1,3,0],[I,0,0,0]]),2),
 ('positive defect',s.Matrix([[0,0],[1,0]]),1),
 ('negative defect',s.Matrix([[1,1],[0,0]]),1),
 ('mixed rankone',s.Matrix([[1,I,1],[0,0,0],[0,0,0]]),1)
]
for label,T0,n in tests:
 print('Checking',label,flush=True)
 q=T0.rows;m=q-n
 R=s.eye(q)
 for j in range(q-1):R[j,j+1]=1+I
 inv=R.inv();G=clean(inv.H*inv);T=clean(R*T0*inv)
 V=s.eye(n)
 for j in range(n):V[j,j]=j+2
 if n>1:V[0,1]=I
 Lambda=V*s.eye(q)[:n,:]*inv
 IK=R*s.eye(q)[:,n:]
 if m>1:
  W=s.eye(m);W[0,1]=1+I;IK=IK*W
 Q=clean(clean(Lambda*G.inv()*Lambda.H).inv());L=clean(G.inv()*Lambda.H*Q)
 HK=clean(IK.H*G*IK);H=clean(G.inv()*T.H*G*T)
 Ebb=clean(L.H*T.H*G*T*L);Ekk=clean(IK.H*T.H*G*T*IK);X=clean(IK.H*T.H*G*T*L)
 eq(Lambda*L,s.eye(n),label+' section');eq(IK.H*G*L,s.zeros(m,n),label+' orthogonality')
 U=L.row_join(IK);eq(U.H*G*U,s.diag(Q,HK),label+' full metric')
 # Keep the original coordinates; each test uses a nonidentity metric and value frame.
 for zz in [s.Rational(1,3),s.Integer(1),s.Integer(4)]:
  D=clean(X.H*clean(zz*HK+Ekk).inv()*X);F=clean(zz*Q+Ebb-D)
  Y=clean(Lambda*zz*clean(zz*s.eye(q)+H).inv()*L)
  eq(Y,zz*F.inv()*Q,label+' memory resolvent')
  eq(D,Ebb-zz*Q*(Y.inv()-s.eye(n)),label+' reverse recovery')
  eq(Y.det(),zz**n*(zz*HK+Ekk).det()/(HK.det()*(zz*s.eye(q)+H).det()),label+' PR original determinant')
  a=-(zz*HK+Ekk).inv()*X
  energy=(L+IK*a).H*T.H*G*T*(L+IK*a)+zz*a.H*HK*a
  eq(energy,Ebb-D,label+' attained full minimum');psd(energy,label+' effective positive')
  psd(D,label+' positive memory')
  Yenergy=zz*(zz*Q+Ebb).inv()*Q
  psd(Q*(Y-Yenergy),label+' observed energy comparison')
  eq(Y.det()/Yenergy.det(),(zz*Q+Ebb).det()/F.det(),label+' determinant gain')
 # For minimality use the exact equivalent orthonormal coordinates of T0.
 H0=T0.H*T0;A=H0[n:,n:];C=H0[n:,:n]
 blocks=[A**j*C for j in range(m)];Wcyc=s.Matrix.hstack(*blocks)
 moments=s.BlockMatrix([[C.H*A**(i+j)*C for j in range(m)]for i in range(m)]).as_explicit()
 eq(moments,Wcyc.H*Wcyc,label+' full phase moment Gram');eq(s.Integer(moments.rank()),s.Integer(Wcyc.rank()),label+' memory dimension')
 for v in A.nullspace():eq(v.H*C,s.zeros(1,n),label+' zero energy residue')
 # Minimal cyclic space is reducing; exact closure, without generic eigenspaces.
 if Wcyc.rank():eq(s.Integer(Wcyc.row_join(A*Wcyc).rank()),s.Integer(Wcyc.rank()),label+' invariant memory')
 fixtures.append({'name':label,'q':q,'observation_rank':n,'kernel_rank':m,'memory_rank':Wcyc.rank(),'word_rank':T0.rank(),'kernel_energy_rank':A.rank()})
 # RM19-21: recompute the minimum section for a coherently perturbed full metric.
 Gtilde=clean(inv.H*s.diag(*[s.Rational(1,2) if j%2==0 else s.Integer(2) for j in range(q)])*inv)
 Qt=clean(clean(Lambda*Gtilde.inv()*Lambda.H).inv());Lt=clean(Gtilde.inv()*Lambda.H*Qt)
 Ht=clean(Gtilde.inv()*T.H*Gtilde*T);Delta=T.rank();p=(T*IK).rank();kap=s.Integer(4)
 psd(Gtilde-G/2,label+' lower full metric');psd(2*G-Gtilde,label+' upper full metric')
 eq(Lambda*Lt,s.eye(n),label+' perturbed actual section')
 for zz in [s.Rational(1,100),s.Integer(1),s.Integer(100)]:
  Y0=clean(Lambda*zz*clean(zz*s.eye(q)+H).inv()*L)
  Yt=clean(Lambda*zz*clean(zz*s.eye(q)+Ht).inv()*Lt)
  ratio=s.cancel(Yt.det()/Y0.det())
  if not (ratio>=kap**(-Delta-p) and ratio<=kap**(Delta+p)):raise ArithmeticError(label+' uniform nonzero-rank determinant bound')
  count+=1
  # Scaling Gtilde by4/5 leaves its measured endomorphism unchanged and
  # puts its relative eigenvalues in[2/5,8/5], so epsilon=3/5 in RM23.
  diff=clean(Yt-Y0)
  psd(9*Q-diff.H*Q*diff,label+' original complex-response error')
 if label in ('positive defect','negative defect'):
  Edef=H0[:n,:n]-C.H*(s.eye(m)+A).inv()*C-T0[:n,:n].H*T0[:n,:n]
  eq(Edef,s.Matrix([[1 if label=='positive defect' else -s.Rational(1,2)]]),label+' exact sign')
  negative_controls+=1

# Exact supplied complex illustration, with the original nonorthogonal observation.
T=s.diag(0,2,3*I);Lam=s.Matrix([[-1,1,0],[-I,0,1]]);Q=(Lam*Lam.H).inv();L=Lam.H*Q
Y=Lam*z*(z*s.eye(3)+T.H*T).inv()*L
eq(Y.det(),z*(3*z+13)/(3*(z+4)*(z+9)),'received PR16 determinant')
Tb=Lam*T*L;Ybad=z*(z*s.eye(2)+Q.inv()*Tb.H*Q*Tb).inv()
eq(Ybad.det(),9*z*z/(9*z*z+52*z+36),'received compressed arithmetic determinant')
eq(Y.det()-Ybad.det(),-2*z*(39*z*z+94*z-234)/(3*(z+4)*(z+9)*(9*z*z+52*z+36)),'RM22 signed difference')
cross=(s.sqrt(11335)-47)/39
eq(39*cross**2+94*cross-234,0,'RM22 exact crossing')
IK=s.Matrix([1,1,I]);X=IK.H*T.H*T*L
eq(X,s.Matrix([[-s.Rational(1,3),-14*I/3]]),'RM22 phase-bearing cross block')
eq((IK.H*T.H*T*IK)[0],13,'RM22 actual kernel energy')
if s.cancel(Y.det()-Ybad.det())==0:raise ArithmeticError('Compressed substitution negative control failed')
negative_controls+=1
f=P/'ORIGINAL_RESOLVENT_MEMORY_PROOFS.md'
receipt={'status':'passed','exact_checks':count,'negative_controls':negative_controls,'fixtures':fixtures,'proof_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'scope':'Exact finite complex matrices in original metrics; no native asymptotic coefficient evaluated.'}
(P/'RESOLVENT_MEMORY_CHECKS.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8');print(json.dumps(receipt,indent=2))
