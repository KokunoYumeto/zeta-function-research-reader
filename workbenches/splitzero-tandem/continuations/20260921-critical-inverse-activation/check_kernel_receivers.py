from pathlib import Path
import json
import sympy as s
from itertools import combinations
P=Path(__file__).parent
I=s.I
T=s.diag(1,2,3,5)
S=s.Matrix([[1,I/2,0,1],[0,1,s.Rational(1,3),0],[0,0,1,-I],[0,0,0,1]])
G0=16*T+S.H*S
Wj=s.Matrix([[1,0],[I,1],[0,1],[1,-I]])
GJ=(T.inv()+Wj*Wj.H).inv()
Lam=s.Matrix([[1,I,0,0],[0,1,1,0],[0,0,1,1+I]])
roots=[3+I/4,3-I/4,-3+I/4,-3-I/4]
M=s.diag(*roots)
U=s.Matrix([[z**-1,z**-2] for z in roots])
K=s.Matrix.hstack(*Lam.nullspace())
F=Lam*U
E=s.eye(4)
for j in range(4):
  Frame=K.row_join(U).row_join(E[:,j])
  if Frame.det()!=0: W=E[:,j];break
beta=s.Matrix.hstack(*s.Matrix([[1,z] for z in roots]).T.nullspace()).T
pi=beta*M**2
trace=s.simplify(s.trace(T.inv()*G0))
joint=s.simplify(s.trace(T*GJ.inv()))
c=s.simplify(trace*joint)
checks=[]
def zero(name,A):
 A=A.applyfunc(s.simplify)
 if any(x!=0 for x in A):raise AssertionError(name)
 checks.append(name)
def scalar(name,x):zero(name,s.Matrix([x]))
def psd(name,A):
 zero(name+" Hermitian",A-A.H)
 for l in range(1,A.rows+1):
  for ii in combinations(range(A.rows),l):
   z=s.simplify(A.extract(ii,ii).det())
   if z.is_nonnegative is not True:raise AssertionError((name,ii,z))
 checks.append(name+" principal minors")
zero("exact inverse-sector kernel",pi*U)
zero("original observation kernel",Lam*K)
zero("physical shift to low polynomials",beta*M**2*U)
for alpha in [s.Rational(0),s.Rational(1,17),s.Rational(1)]:
 C=(1-alpha)*G0.inv()+alpha*GJ.inv()
 G=C.inv();QB=(Lam*C*Lam.H).inv()
 A=K.H*G*K;D=U.H*G*U;cross=K.H*G*U
 HB=F.H*QB*F
 Hat=(pi*K).H*(pi*C*pi.H).inv()*(pi*K)
 zero(f"{alpha} full observed minimum",HB-(D-cross.H*A.inv()*cross))
 zero(f"{alpha} full inverse quotient minimum",Hat-(A-cross*D.inv()*cross.H))
 scalar(f"{alpha} exact angle determinant",A.det()*HB.det()-Hat.det()*D.det())
 psd(f"{alpha} kernel quotient loss",A-Hat)
 # The complement is attained in B after the entire observed inverse sector.
 rem=(Lam*W).H*QB*(Lam*W)-(Lam*W).H*QB*F*HB.inv()*F.H*QB*(Lam*W)
 scalar(f"{alpha} three original determinant factors",(Frame.H*G*Frame).det()-A.det()*HB.det()*rem.det())
 shifted=(beta*M**2*K).H*(beta*M**2*C*(M**2).H*beta.H).inv()*(beta*M**2*K)
 zero(f"{alpha} shifted attained source isometry",shifted-Hat)
 d=1-alpha+alpha*c
 psd(f"{alpha} full space lower metric",G-G0/d)
 psd(f"{alpha} full space upper metric",G0-G)
 if alpha==0:
  A0=A;HB0=HB;rem0=rem
 else:
  scalar(f"{alpha} exact source cost splitting",
    G0.det()/G.det()-(A0.det()/A.det())*(HB0.det()/HB.det())*(rem0.det()/rem.det()))
out={"passed":True,"exact_checks":len(checks),"checks":checks,
"scope":"Exact complex-rational auxiliary example with original observation and complete attained minima. Does not simulate an arithmetic packet or verify an asymptotic coefficient."}
(P/"KERNEL_RECEIVER_CHECKS.json").write_text(json.dumps(out,indent=2),encoding="utf-8")
print(json.dumps({"passed":True,"exact_checks":len(checks)}))

