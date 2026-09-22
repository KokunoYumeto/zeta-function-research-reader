from pathlib import Path
import sympy as s,json,hashlib
P=Path(__file__).resolve().parent
count=0
def equal(a,b):
 global count
 if isinstance(a,s.MatrixBase):
  if a.shape!=b.shape or any(s.simplify(t)!=0 for t in a-b):raise ArithmeticError((a,b))
 elif s.simplify(a-b)!=0:raise ArithmeticError((a,b))
 count+=1
def projector(F,G):
 return F*(F.H*G*F).inv()*F.H*G if F.cols else s.zeros(G.rows)
def frame(M,n):
 ns=M.nullspace()
 return s.Matrix.hstack(*ns) if ns else s.zeros(n,0)
z,u=s.symbols('z u')
I=s.I
T=s.Matrix([[1,I,1,0],[0,1/s.sqrt(2),0,s.sqrt(2)],[0,0,0,0],[0,0,0,0]])
Lam=s.eye(4)[:2,:];K=s.eye(4)[:,2:]
def test(T,Lam,G,K,anchor=True):
 q=G.rows;n=Lam.rows;m=K.cols
 Qb=(Lam*G.inv()*Lam.H).inv()
 L=G.inv()*Lam.H*Qb;HK=K.H*G*K
 H=G.inv()*T.H*G*T
 V=frame(T,q);d=V.cols
 Pv=projector(V,G)
 Y0=Lam*Pv*L
 Gamma=HK.inv()*K.H*G*(s.eye(q)-Pv)*K
 equal(Lam*L,s.eye(n));equal(L.H*G*L,Qb)
 equal(L.H*G*K,s.zeros(n,m))
 equal((1-u)**m*(s.eye(n)-u*Y0).det(),(1-u)**d*(s.eye(m)-u*Gamma).det())
 zeros=(s.Matrix.hstack(K,V).rank())
 t=m+d-zeros
 equal(m-Gamma.rank(),t);equal(Y0.rank(),d-t)
 def pdet(A):
  return s.prod(v**mult for v,mult in A.eigenvals().items() if v!=0)
 equal(pdet(Y0),pdet(Gamma))
 if not anchor:return
 equal(HK,s.eye(m))
 R=s.Integer(4)
 A=K.H*T.H*G*T*K/R;C=K.H*T.H*G*T*L/R;B=L.H*T.H*G*T*L/R
 if A.det()==0:return
 def Y(x):
  return Lam*x*R*(x*R*s.eye(q)+H).inv()*L
 def Z(x):
  return s.simplify(x*Qb*(Y(x).inv()-s.eye(n)))
 def F(x):
  return s.simplify((Z(x)-Z(1))/(x-1))
 for x in [s.Integer(2),s.Integer(4)]:
  equal(Z(x),B-C.H*(x*s.eye(m)+A).inv()*C)
  equal(F(x),C.H*(s.eye(m)+A).inv()*(x*s.eye(m)+A).inv()*C)
 xs=[2+s.Rational(i,m) for i in range(m)]
 ys=[4+s.Rational(i,m) for i in range(m)]
 LL=s.BlockMatrix([[(F(x)-F(y))/(y-x) for y in ys] for x in xs]).as_explicit()
 SS=s.BlockMatrix([[(y*F(y)-x*F(x))/(y-x) for y in ys] for x in xs]).as_explicit()
 cols=LL.rref()[1];rows=LL[:,list(cols)].T.rref()[1];rank=len(cols)
 if rank:
  L0=LL.extract(rows,cols);S0=SS.extract(rows,cols)
  BL=s.Matrix.vstack(*[F(x) for x in xs]).extract(rows,range(n))
  BR=s.Matrix.hstack(*[F(y) for y in ys]).extract(range(n),cols)
  F0=BR*S0.inv()*BL
  Fp=-BR*S0.inv()*L0*S0.inv()*BL
  for x in [s.Rational(3,2),s.Integer(7)]:
   equal(F(x),BR*(S0+x*L0).inv()*BL)
 else:F0=s.zeros(n);Fp=s.zeros(n)
 E0=Z(1)-F0;W0=F0-Fp
 equal(E0,B-C.H*A.inv()*C);equal(W0,C.H*A.inv()**2*C)
 Z0=frame(E0,n)
 rec=Z0*(Z0.H*(Qb+W0)*Z0).inv()*Z0.H*Qb if Z0.cols else s.zeros(n)
 equal(rec,Y0)
 return Y0,Gamma
y,g=test(T,Lam,s.eye(4),K)
equal(y,s.Matrix([[s.Rational(9,14),-2*I/7],[2*I/7,s.Rational(4,7)]]))
equal(g,s.Matrix([[s.Rational(5,14),-I/7],[I/7,s.Rational(6,7)]]))
Pv=projector(frame(T,4),s.eye(4));Pb=Lam.H*Lam
for val,mul,vectors in g.eigenvects():
 for x in vectors:
  bv=Lam*Pb*Pv*K*x
  equal(y*bv,val*bv)
  equal((bv.H*bv)[0],val*(1-val)*(x.H*x)[0])
F=s.Matrix([[1,I,0,1],[0,2,1,0],[0,0,1,I],[0,0,0,1]])
test(F.inv()*T*F,Lam*F,F.H*F,F.inv()*K)
test(T,Lam,s.eye(4),K*s.Matrix([[2,I],[0,3]]),False)
# Repeated positive poles and a reducing invisible positive direction.
test(s.Matrix([[1,0,1,0],[0,0,0,2],[0,0,0,0],[0,0,0,0]]),Lam,s.eye(4),K)
test(s.Matrix([[1,0,1,0],[0,1,0,1],[0,0,0,0],[0,0,0,0]]),Lam,s.eye(4),K)
# Zero-angle intersection, zero word, empty kernel, and full positive energy.
test(s.diag(0,2,0,3),Lam,s.eye(4),K,False)
test(s.zeros(4),Lam,s.eye(4),K,False)
test(s.diag(0,2,3),s.eye(3),s.eye(3),s.zeros(3,0),False)
test(s.diag(1,2,3,4),Lam,s.eye(4),K)
e=s.symbols('e',positive=True)
G=s.diag((1-e)/e,1);lam=s.Matrix([[-1,1]]);k=s.Matrix([1,1]);t=s.diag(0,1)
qb=(lam*G.inv()*lam.H).inv();l=G.inv()*lam.H*qb
equal((lam*z*(z*s.eye(2)+t).inv()*l)[0],(z+e)/(z+1))
equal((k.H*G*k)[0],1/e)
# Negative controls: matrix equality is not implied by the spectral morphism;
# determinant of the full response at zero loses its zero multiplicity.
negative=0
if y==g:raise ArithmeticError('false coordinate identity')
negative+=1
yy= s.diag(0,s.Rational(2,7))
if yy.det()==s.Rational(2,7):raise ArithmeticError('false ordinary determinant')
negative+=1
receipt={'exact_checks':count,'negative_controls':negative,'status':'passed','scope':'finite exact matrix identities, nonidentity metric transport, repeated energies, reducing memory, rank-changing intersections; no native period evaluation','proof_sha256':hashlib.sha256((P/'MATRIX_RECOVERY_PROOFS.md').read_bytes()).hexdigest()}
(P/'MATRIX_CHECKS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt))
