"""Auxiliary exact and numerical fixtures for UFR; no arithmetic zero computation."""
from pathlib import Path
import json,sympy as s,numpy as np
P=Path(__file__).parent;y=s.Symbol('y');exact=[];numeric=[]
def ck(n,v):
 if not bool(v):raise AssertionError(n)
 exact.append(n)
def coeff(f,n):return s.Matrix([s.expand(f).coeff(y,i) for i in range(n)])
for d,degree in [(1,1),(2,3),(2,4),(3,5)]:
 chi=s.prod(y+j for j in range(-1,degree));lower=s.prod(y+j for j in range(degree))
 D=(y-2)**d if degree!=3 else (y-2)*(y-3)
 L=2*d;B=s.expand(D*D.subs(y,y+1))
 T=s.Matrix.hstack(*[coeff(s.cancel(B*((y+1)**i/D.subs(y,y+1)-y**i/D)),L) for i in range(d)])
 J=s.Matrix.hstack(*[coeff(s.rem(s.invert(D,chi)*y**i,chi,y),degree+1) for i in range(d)])
 CA=s.Matrix.hstack(*[coeff(s.rem((y+1)**i-y**i,lower,y),degree) for i in range(degree+1)])
 MB=s.Matrix.hstack(*[coeff(s.rem(B*y**i,lower,y),L) for i in range(degree)])
 W=(T.H*T).inv()*T.H*MB
 ck(f'rational:{d}:{degree}:left_inverse',(W*CA*J-s.eye(d)).applyfunc(s.cancel)==s.zeros(d))
 ck(f'rational:{d}:{degree}:full_rank',T.rank()==d)
 ck(f'rational:{d}:{degree}:degree_guard',L-1<=degree and T[-1,:]==s.zeros(1,d))
 # Source and attained observation still carry a positive nonorthogonal metric.
 n=degree+1;G=s.eye(n)+s.ones(n,n)
 Gamma=CA*G.inv()*CA.H
 HD=J.H*G*J
 QB=Gamma.inv()
 HB=J.H*CA.H*QB*CA*J
 ck(f'rational:{d}:{degree}:positive_source',HD.det()>0 and HB.det()>0)
# Exact sharp projection improvement at Pythagorean fractions.
ell=s.Rational(9,25);eps=s.Rational(5,13)
u=s.Matrix([s.Rational(4,5),s.Rational(3,5)])
perp=s.Matrix([s.Rational(3,5),-s.Rational(4,5)])
x=s.Rational(12,13)*u+eps*perp
sharp=(s.sqrt(ell)*s.sqrt(1-eps**2)-s.sqrt(1-ell)*eps)**2
old=(s.sqrt(ell)*s.sqrt(1-eps**2)-eps)**2
ck('projection:sharp_equality',s.cancel(x[1]**2-sharp)==0)
ck('projection:strict_improvement',sharp>old)
ck('projection:distance',s.cancel(1-(u.dot(x))**2-eps**2)==0)
# Positive small source matrix has squared singular values.
G=s.Matrix([[3,s.I,0],[-s.I,4,1],[0,1,2]])
U=s.Matrix([[1,0],[s.I,1],[0,1]])
T=s.Matrix([[1,s.I,2],[0,2,1]])
HP=U.H*G*U;R=U*T
# Avoid choosing a non-rational square root: compare all nonzero spectral coefficients.
lam=s.Symbol('lam')
big=(lam*s.eye(3)-R*G.inv()*R.H*G).det()
small=(lam*s.eye(2)-T*G.inv()*T.H*HP).det()
ck('filter:squared_singular_polynomial',s.cancel(big-lam*small)==0)
# Noncommuting full-rank families: exact derivative identity and trace-zero pair.
K=s.eye(3)[:,:1];V=s.Matrix([[1],[s.I],[1]]);SV=K.row_join(V)
Z1=s.Matrix([[1,0],[s.I,1],[0,2]]);Z2=s.Matrix([[0,1],[1,1],[s.I,0]])
O1=Z1*Z1.H;O2=Z2*Z2.H
Gbase=G
for t1,t2 in [(s.Rational(1,3),s.Integer(2)),(s.Integer(5),s.Rational(1,2))]:
 C=Gbase.inv()+t1*O1+t2*O2;g=C.inv();Cp=2*t1*O1-3*t2*O2;gp=-g*Cp*g
 def proj(X):return X*(X.H*g*X).inv()*X.H*g
 A=proj(K)+proj(V)-proj(SV)
 der=sum(sign*s.trace((X.H*g*X).inv()*X.H*gp*X) for X,sign in [(K,1),(V,1),(SV,-1)])
 ck(f'weights:{t1}:{t2}:trace_zero',s.cancel(s.trace(A))==0)
 ck(f'weights:{t1}:{t2}:angle_derivative',s.cancel(der+s.trace(Cp*g*A))==0)
# Explicit numerical path fixtures test the integrated finite bound with original frames.
def nck(n,v):
 if not bool(v):raise AssertionError(n)
 numeric.append(n)
Gn=np.array(Gbase.tolist(),complex);kn=np.array(K.tolist(),complex);vn=np.array(V.tolist(),complex);sn=np.column_stack([kn,vn])
ons=[np.array(O1.tolist(),complex),np.array(O2.tolist(),complex)]
def metric(w):return np.linalg.inv(np.linalg.inv(Gn)+sum(np.exp(wi)*oi for wi,oi in zip(w,ons)))
def delta(g):
 return sum(sig*np.linalg.slogdet(X.conj().T@g@X)[1] for X,sig in [(kn,1),(vn,1),(sn,-1)])
for a,b in [([-8,2],[3,-4]),([0,0],[.1,.2]),([5,5],[15,15]),([-10,-10],[-9,-8])]:
 v=np.array(b)-a;width=max(0,*v)-min(0,*v)
 nck(f'weights:{a}:{b}:global',abs(delta(metric(b))-delta(metric(a)))<=width+1e-8)
# The physical S-to-y map retains the phase on every numerator coefficient.
y,S=s.symbols('y S');centre=s.Rational(9,2)
p=y**3+(2+s.I)*y**2-3*y+5;d=3
D=s.expand(s.I**d*p.subs(y,(S-centre)/s.I))
ck('physical:monic_denominator',s.Poly(D,S).LC()==1)
for j in range(d):
 numerator=s.expand(s.I**d*((S-centre)/s.I)**j)
 ck(f'physical:numerator:{j}',s.cancel((numerator/D).subs(S,centre+s.I*y)-y**j/p)==0)
# A full complex Hermitian congruence transports both metrics identically.
Tr=s.Matrix([[s.expand(s.I**d*((S-centre)/s.I)**j).coeff(S,i) for j in range(d)] for i in range(d)])
ck('physical:invertible_numerator_frame',Tr.det()!=0)
HB=s.Matrix([[2,s.I,0],[-s.I,2,0],[0,0,1]])
ck('physical:same_metric_lower_bound',all(A[:j,:j].det()>0 for A in [G-HB,Tr.H*(G-HB)*Tr] for j in range(1,4)))
report={'status':'passed','exact_checks':len(exact),'numerical_checks':len(numeric),'exact':exact,'numerical':numeric,'scope':'Auxiliary rational conductor examples including qprime<Jd, repeated/translated-colliding poles; exact sharp-angle and squared-singular identities; noncommuting source-weight fixtures; exact complex physical-coordinate transport.'}
(P/'FAMILY_RECEIVER_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['status','exact_checks','numerical_checks']}))
