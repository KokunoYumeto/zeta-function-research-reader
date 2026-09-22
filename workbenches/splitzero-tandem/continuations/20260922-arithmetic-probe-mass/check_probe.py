from pathlib import Path
import sympy as s,json,hashlib
P=Path(__file__).resolve().parent
checks=[];negative=[]
def eq(name,a,b):
 if isinstance(a,s.MatrixBase):
  good=a.shape==b.shape and all(s.simplify(v)==0 for v in a-b)
 else:good=s.simplify(a-b)==0
 if not good:raise ArithmeticError(name)
 checks.append(name)
def yes(name,v):
 if not v:raise ArithmeticError(name)
 checks.append(name)
def psd(name,A):
 eq(name+'/Hermitian',A,A.H)
 from itertools import combinations
 for n in range(1,A.rows+1):
  for ix in combinations(range(A.rows),n):yes(name+str(ix),s.simplify(A.extract(ix,ix).det())>=0)
def scalar(a):return a[0] if isinstance(a,s.MatrixBase) else a
y=s.symbols('y');I=s.I
pol=s.Poly(s.prod(y-j for j in [2,3,4,5]),y)
M=s.zeros(4)
for j in range(3):M[j+1,j]=1
for j in range(4):M[j,3]=-pol.nth(j)
La=s.Matrix([[0,0,0,1]]);IK=s.eye(4)[:,:3]
eq('literal original companion polynomial',M.charpoly(y).as_expr(),pol.as_expr())
u=s.Matrix([1,I,1,1]);v=s.Matrix([1,1,I,2])
allC={};allD={};allH={}
for N in range(4):
 cov=s.eye(4)+u*u.H+N*v*v.H;G=cov.inv()
 Q=(La*cov*La.H).inv();L=cov*La.H*Q;HK=IK.H*G*IK
 allH[N]=HK
 powers=[M**j for j in range(4)]
 S=[[La*powers[i]*cov*powers[j].H*La.H for j in range(4)]for i in range(4)]
 def V(A):return La*A*cov*A.H*La.H
 for i in range(4):
  eq(f'{N}/diagonal{i}',V(powers[i]),S[i][i])
  for j in range(i+1,4):
   plus=V(powers[i]+powers[j])-S[i][i]-S[j][j]
   imag=V(powers[i]+I*powers[j])-S[i][i]-S[j][j]
   eq(f'{N}/complex probe{i}{j}',(plus+I*imag)/2,S[i][j])
   yes(f'{N}/invertible plus{i}{j}',(powers[i]+powers[j]).det()!=0)
   yes(f'{N}/invertible imaginary{i}{j}',(powers[i]+I*powers[j]).det()!=0)
 allC[N]={0:s.zeros(0)};allD[N]={}
 for depth in range(1,4):
  stack=s.Matrix.vstack(*[La*powers[j]for j in range(depth+1)])
  gram=stack*cov*stack.H
  C=gram[1:,1:]-gram[1:,:1]*Q*gram[:1,1:]
  J=stack[1:,:]*IK
  eq(f'{N}/whole Schur{depth}',C,J*HK.inv()*J.H)
  allC[N][depth]=C
  prev=C[:-1,:-1]
  D=C[-1:,-1:]-(C[-1:,:-1]*prev.inv()*C[:-1,-1:] if depth>1 else s.zeros(1))
  allD[N][depth]=D
  eq(f'{N}/nested determinant{depth}',C.det(),(prev.det()if depth>1 else 1)*D.det())
  source=s.eye(4)[:,:4-depth]
  row=La*powers[depth]*source
  h=source.H*G*source
  eq(f'{N}/actual quotient{depth}',D,row*h.inv()*row.H)
  lift=h.inv()*row.H*D.inv()
  eq(f'{N}/quotient section{depth}',row*lift,s.eye(1))
  eq(f'{N}/quotient energy{depth}',lift.H*h*lift,D.inv())
  tail=HK[:3-depth,:3-depth]
  change=s.Matrix.vstack(J,s.eye(3)[:3-depth,:])
  eq(f'{N}/fixed frame determinant{depth}',HK.det()*C.det(),tail.det()*(change.det()*s.conjugate(change.det())))
 # Both physical phase expressions use the same original section.
 b=s.Matrix([1+I]);MB=La*M*L
 current=scalar(I*b.H*(Q*MB-MB.H*Q)*b)
 Tc=(V(s.eye(4)+I*M)-V(s.eye(4)-I*M))/2
 eq(f'{N}/complete current',current,scalar(b.H*Q*Tc*Q*b))
 # Finite positive-regularizer covariance equals the original response.
 W=s.eye(4)+I*M;T=W.inv();z=s.Rational(1,5);H=G.inv()*T.H*G*T
 Y=La*z*(z*s.eye(4)+H).inv()*L
 sig=La*(T.H*G*T+z*G).inv()*La.H
 eq(f'{N}/positive regularizer',Y*Q.inv()/z,sig)
 if N==0:
  yes('wrong imaginary phase fails',(V(s.eye(4)+I*M)-V(s.eye(4))-V(M))!= -Tc)
  negative.append('wrong imaginary phase')
  raw=S[1][1];true=allC[N][1]
  yes('raw lower Gram fails',raw!=true);negative.append('raw lower Gram')
for depth in range(1,4):
 for lo,hi in [(0,2),(1,3)]:
  psd(f'nested source innovation{depth}/{lo}{hi}',allD[hi][depth]-allD[lo][depth])
 ratio=s.simplify(allD[2][depth].det()*allD[3][depth].det()/(allD[0][depth].det()*allD[1][depth].det()))
 yes(f'positive signed increment{depth}',ratio>=1)
product=s.prod(allD[2][d].det()*allD[3][d].det()/(allD[0][d].det()*allD[1][d].det())for d in range(1,4))
eq('full original telescoping return',product,allH[0].det()*allH[1].det()/(allH[2].det()*allH[3].det()))
a,b,t=s.symbols('a b t',positive=True)
c=b*t*t/a;z=t/(a*(1-t))
eq('evaluated regularizer',b*a*z/(1+a*z)+c/z,b*(2*t-t*t))
zz=s.symbols('z',positive=True)
eq('stationary regularizer',s.diff(b*a*zz/(1+a*zz)+c/zz,zz).subs(zz,z),0)
eta=b*(2*t-t*t)
eq('noise threshold',b*(1-(1-t))**2/a,c)
receipt={'status':'PASS','exact_checks':len(checks),'negative_controls':negative,'checks':checks,
 'proof_sha256':hashlib.sha256((P/'PROBE_PROOFS.md').read_bytes()).hexdigest(),
 'scope':'Exact auxiliary complex matrices and finite acquisition identities; no native period data assigned.',
 'fixture_return_ratio':str(s.factor(product))}
(P/'PROBE_CHECKS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in receipt.items()if k!='checks'}))
