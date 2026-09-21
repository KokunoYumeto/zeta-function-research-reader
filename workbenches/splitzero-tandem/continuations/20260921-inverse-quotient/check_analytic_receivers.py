"""Exact finite shifted-source and angle checks, plus declared numerical heat fixtures.
These supplement the written proof; no fixture is an off-critical zeta zero."""
from pathlib import Path
import json
import sympy as s
import numpy as np
P=Path(__file__).parent;checks=[];num=[]
def zero(A):return A.applyfunc(s.cancel)==s.zeros(*A.shape)
def ck(name,b):
 if not bool(b):raise AssertionError(name)
 checks.append(name)
def psd(A):
 A=A.applyfunc(s.cancel)
 # Sylvester shifted epsilon polynomial coefficients suffice here:
 # all eigenvalues nonnegative iff coefficients of det(tI+A) nonnegative for Hermitian A.
 t=s.Symbol('t');co=s.Poly((t*s.eye(A.rows)+A).det(),t).all_coeffs()
 return A==A.H and all(x>=0 for x in co)
def quotient(G,F):return (F*G.inv()*F.H).inv().applyfunc(s.cancel)
y=s.Symbol('y');Q=y**4-s.Rational(143,8)*y**2+s.Rational(21025,256)
q=4
def coeff(p,n):return s.Matrix([s.expand(p).coeff(y,j) for j in range(n)])
def remmat(N):return s.Matrix.hstack(*[coeff(s.rem(y**j,Q,y),q) for j in range(N+1)])
def src(N):
 # Full positive discrete source, mass13, declared auxiliary measure.
 return s.Matrix(N+1,N+1,lambda i,j:sum(s.Integer(x)**(i+j) for x in range(-6,7)))
def minsection(H,J):return (H.inv()*J.H*quotient(H,J)).applyfunc(s.cancel)
IK=s.eye(4)[:,:1]
for N in [3,4,7,8]:
 H=src(N);J=remmat(N);G=quotient(H,J)
 for r in [1,2]:
  L=N+r;HL=src(L);JL=remmat(L);GL=quotient(HL,JL)
  tau=s.eye(q)[r:,:]
  Mr=s.Matrix.hstack(*[coeff(s.rem(y**(r+j),Q,y),q) for j in range(q)])
  B=tau*Mr*IK
  low=[coeff(y**j,L+1) for j in range(r)]
  relations=[coeff(y**j*Q,L+1) for j in range(L-q+1)]
  R=s.Matrix.hstack(*(low+relations))
  E=s.Matrix.hstack(*[coeff(y**r*sum(IK[j,a]*y**j for j in range(q)),L+1) for a in range(IK.cols)])
  SH=(E.H*HL*E-E.H*HL*R*(R.H*HL*R).inv()*R.H*HL*E).applyfunc(s.cancel)
  target=(B.H*quotient(GL,tau)*B).applyfunc(s.cancel)
  ck(f'shift:{N}:{r}:complete_relation_minimum',zero(SH-target))
  pi=tau*Mr;hat=(IK.H*pi.H*quotient(G,pi)*pi*IK).applyfunc(s.cancel)
  mult=s.zeros(L+1,N+1)
  for j in range(N+1):mult[j+r,j]=1
  div=s.zeros(N+1,L+1)
  for j in range(r,L+1):div[j-r,j]=1
  Asq=s.trace(H.inv()*mult.H*HL*mult)
  Bsq=s.trace(HL.inv()*div.H*H*div)
  ck(f'shift:{N}:{r}:forward_bound',psd(Asq*hat-SH))
  ck(f'shift:{N}:{r}:inverse_bound',psd(Bsq*SH-hat))
  ck(f'shift:{N}:{r}:relation_count',R.rank()==r+L-q+1)
# Actual adjacent source identity with all earlier polynomial relations.
for N in [3,4,7,8]:
 H=src(N);HN=src(N+1);J=remmat(N);JN=remmat(N+1);G=quotient(H,J)
 pn=s.Matrix.vstack(-H.inv()*HN[:N+1,N+1],s.ones(1,1))
 omega=(pn.H*HN*pn)[0]
 R=s.Matrix.hstack(*[coeff(y**j*Q,N+2) for j in range(N+2-q)])
 HR=R.H*HN*R
 nu=HR[-1,-1] if HR.rows==1 else (HR[-1,-1]-(HR[-1,:-1]*HR[:-1,:-1].inv()*HR[:-1,-1])[0])
 val=JN*pn
 alpha=(val.H*G*val)[0]/omega
 ck(f'adjacent:{N}:full_monic_ratio',s.cancel(1+alpha-nu/omega)==0)
# Exact derivative identities on nonorthogonal, complex coefficient frames.
G0=s.Matrix([[5,s.I,1,0],[-s.I,4,0,1],[1,0,3,s.I],[0,1,-s.I,4]])
K=s.Matrix([[1,0],[0,1],[0,0],[0,0]])
V=s.Matrix([[1,2],[s.I,1],[1,0],[0,1]])
S=K.row_join(V)
for d in [1,2,3]:
 Z=s.Matrix([[1,s.I,0],[2,1,1],[0,1,2],[1,0,s.I]])[:,:d]
 Om=Z*Z.H
 for t in [s.Rational(1,3),s.Integer(2),s.Integer(17)]:
  G=(G0.inv()+t*Om).inv()
  def proj(X):return X*(X.H*G*X).inv()*X.H*G
  A=(proj(K)+proj(V)-proj(S)).applyfunc(s.cancel)
  ck(f'angle:{d}:{t}:Gselfadjoint',zero(A.H*G-G*A))
  ck(f'angle:{d}:{t}:tracezero',s.cancel(s.trace(A))==0)
  ck(f'angle:{d}:{t}:paired_cubic',s.cancel(s.trace(A**3))==0)
  ck(f'angle:{d}:{t}:spectral_upper',psd(G-G*A))
  ck(f'angle:{d}:{t}:spectral_lower',psd(G+G*A))
  gp=-G*Om*G
  deriv=sum(s.trace((X.H*G*X).inv()*X.H*gp*X)*sg for X,sg in [(K,1),(V,1),(S,-1)])
  ck(f'angle:{d}:{t}:derivative',s.cancel(deriv+s.trace(Om*G*A))==0)
# Symbolic coefficient identity with original endpoint logarithms.
a0,lw,lz,lc,log2=s.symbols('a0 lw lz lc log2',real=True)
L=6*lw-2*lz-2;psi1=lw+lc/2-2*log2;J1=2*(log2-1)-L/2
ck('coefficient:C_equals_Cpartial',s.expand(4*(a0-psi1-J1-1)-(4*a0+8*lw-4*lz-2*lc))==0)
# Numerical positive heat: exact rank-one inverse perturbation, non-invariant observation kernel.
def nck(name,b):
 if not bool(b):raise AssertionError(name)
 num.append(name)
u=np.array([1.,0,0,0]);phi=np.array([100.,13.,7.,3.])
Bi=np.diag([1.,2.,3.,4.]);Minv=Bi+np.outer(u,phi);M=np.linalg.inv(Minv)
eta=np.linalg.norm(Bi,2)/(np.linalg.norm(phi)-np.linalg.norm(Bi,2))
K=np.array([[20.],[1.],[3.],[.5]]);PK=K@np.linalg.inv(K.T@K)@K.T;PB=np.eye(4)-PK
V=np.eye(4)[:,:2];W=PB@V;PW=W@np.linalg.inv(W.T@W)@W.T;Pr=PB-PW
lam,U=np.linalg.eigh(M.T@M);theta=u@PB@u
for tau in [.01,1.,100.,10000.]:
 H=(U*np.exp(-tau*lam))@U.T
 actual=np.trace(Pr@H);upper=eta**2*np.exp(-tau*lam[0])+3*np.exp(-tau/16)
 nck(f'heat:{tau}:quadratic_residual',actual<=upper+1e-11 and actual>=-1e-12)
 rel=2*eta/theta+3/theta*np.exp(-tau*(1/16-lam[0]))
 nck(f'heat:{tau}:projection_split',abs(np.trace(PB@H)-np.trace(PW@H)-actual)<1e-11)
nck('heat:reference_line_killed',np.linalg.norm(Pr@u)<1e-11)
# Numerical integrated sharp-rank bound for the exact angle fixtures above.
G0n=np.array(G0.tolist(),complex)
Kn=np.array([[1,0],[0,1],[0,0],[0,0]],complex)
Vn=np.array([[1,2],[1j,1],[1,0],[0,1]],complex);Sn=np.column_stack([Kn,Vn])
def ld(A):return np.linalg.slogdet(A)[1]
def delta(G):return ld(Kn.conj().T@G@Kn)+ld(Vn.conj().T@G@Vn)-ld(Sn.conj().T@G@Sn)
eg,egv=np.linalg.eigh(G0n);gs=(egv*np.sqrt(eg))@egv.conj().T
for d in [1,2,3]:
 Z=np.array([[1,1j,0],[2,1,1],[0,1,2],[1,0,1j]],complex)[:,:d];O=Z@Z.conj().T
 c=np.linalg.eigvalsh(gs@O@gs)[-1]
 for t in [.01,1.,10.,100.]:
  G=np.linalg.inv(np.linalg.inv(G0n)+t*O)
  nck(f'angle:{d}:{t}:integrated',abs(delta(G)-delta(G0n))<=min(2,d)*np.log1p(t*c)+1e-8)
report={'status':'passed','exact_checks':len(checks),'numerical_checks':len(num),'exact':checks,'numerical':num,'scope':'Discrete-source full-relation shifted minima; complex nonorthogonal covariance derivatives; symbolic coefficient identity; declared finite heat and integrated-angle examples. No actual zeta quartet or asymptotic computation.'}
(P/'RECEIVER_EXACT_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['status','exact_checks','numerical_checks']}))
