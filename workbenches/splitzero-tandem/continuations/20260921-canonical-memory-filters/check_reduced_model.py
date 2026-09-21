"""Finite checks for RM1--30; fixtures do not certify asymptotic inputs."""
from pathlib import Path
import json, math
import sympy as s
import numpy as np
from scipy.linalg import eigh, expm, svdvals

OUT=Path(__file__).resolve().parent
exact=[]
numeric=[]
def eq(name,a,b):
    dif=a-b
    good=all(s.simplify(v)==0 for v in dif) if isinstance(dif,s.MatrixBase) else s.simplify(dif)==0
    if not good: raise AssertionError(name)
    exact.append(name)
def check(name,lhs,rhs,tol=2e-10):
    if not lhs<=rhs+tol*max(1,abs(lhs),abs(rhs)): raise AssertionError((name,lhs,rhs))
    numeric.append({'name':name,'lhs':float(lhs),'bound':float(rhs)})
def arr(a): return np.array(a.evalf(),dtype=complex)
def root(a):
    w,v=eigh(a); return (v*np.sqrt(w))@v.conj().T
def op(a): return float(svdvals(a)[0])
def tn(a): return float(svdvals(a).sum())

# Exact original polynomial/source maps, with one full source relation.
y=s.symbols('y'); I=s.I
Q=s.Poly(s.prod(y-(b*s.Integer(3)+I*a/s.Integer(4)) for a in [-1,1] for b in [-1,1]),y)
p=s.Poly((y-1)**2,y); q=4; N=4; d=2
def coeff(f,n):
    f=s.Poly(f,y); return s.Matrix([f.nth(j) for j in range(n)])
J=s.Matrix.hstack(*(coeff(s.rem(s.Poly(y**j,y),Q),q) for j in range(N+1)))
M=s.Matrix.hstack(*(coeff(s.rem(s.Poly(y**(j+1),y),Q),q) for j in range(q)))
nodes=[-3,-2,-1,1,2,3]; weights=[1,2,3,4,2,1]
D=s.Matrix(N+1,N+1,lambda i,j:sum(w*x**(i+j) for x,w in zip(nodes,weights)))
G=(J*D.inv()*J.T).inv(); L=D.inv()*J.T*G
eq('original section is right inverse',J*L,s.eye(q))
eq('original full source isometry',L.T*D*L,G)
eq('original relation is orthogonal to minimum section',coeff(Q,N+1).T*D*L,s.zeros(1,q))
Lambda=s.Matrix([[1,0,0,I],[0,1,0,0],[0,0,1,0]])
QB=(Lambda*G.inv()*Lambda.conjugate().T).inv()
LB=G.inv()*Lambda.conjugate().T*QB
eq('RM1 original observed section',Lambda*LB,s.eye(3))
eq('RM1 original observed metric',LB.conjugate().T*G*LB,QB)
X=(M-s.eye(q))**-2; U=X[:,0:d]
Rem=s.Matrix.hstack(*(coeff(s.rem(s.Poly(y**j,y),p),d) for j in range(N+1)))
Quo=s.Matrix.hstack(*(coeff(s.div(s.Poly(y**j,y),p)[0],N-d+1) for j in range(N+1)))
Tp=Rem*L; B=J[:,0:N-d+1]*Quo*L
eq('RM2 complete original polynomial division',X,B+U*Tp)
Cp=s.Matrix.hstack(*(coeff(s.rem(s.Poly(y**(j+1),y),p),d) for j in range(d)))
eq('RF63 full original multiplication defect',M*U,U*Cp+s.eye(q)[:,0]*s.Matrix([[0,1]]))
eq('RF63 physical-coordinate multiplication', (s.eye(q)/2+I*M)*U,U*(s.eye(d)/2+I*Cp)+I*s.eye(q)[:,0]*s.Matrix([[0,1]]))
Hp=U.T*G*U
eq('RF64 pulled-back compression',Hp.inv()*U.T*G*M*U,Cp+Hp.inv()*U.T*G*s.eye(q)[:,0]*s.Matrix([[0,1]]))
IK=s.Matrix([-I,0,0,1]); HK=(IK.conjugate().T*G*IK)[0]
HKE=(IK.conjugate().T*M.T*G*M*IK)[0]
EB=(Lambda*(M.T*G*M).inv()*Lambda.conjugate().T).inv()
eq('BR1 exact full original kernel frame',Lambda*IK,s.zeros(3,1))
eq('BR5 original energy quotient determinant',EB.det()/QB.det(),M.det()**2*HK/HKE)
eq('BR3 full source and kernel action factor',(M.T*G*M).det()/G.det(),M.det()**2)

# Repeated full eigenvalue; retained complex cross blocks and observed mass.
Had=s.Matrix([[1,1,1,1],[1,-1,1,-1],[1,1,-1,-1],[1,-1,-1,1]])/2
Phase=s.diag(1,I,1,-I); W=Phase*Had
h=s.Rational(1,9); H=W*s.diag(h,h,3,7)*W.conjugate().T
A=H[:1,:1]; BH=H[:1,1:]; DH=H[1:,1:]
S=DH-BH.conjugate().T*A.inv()*BH
Z=s.eye(3)+BH.conjugate().T*A**-2*BH
LE=s.Matrix.vstack(-A.inv()*BH,s.eye(3)); C=W[1:,:2]
Theta=C.conjugate().T*C
Fh=DH-h*s.eye(3)-BH.conjugate().T*(A-h*s.eye(1)).inv()*BH
Fprime=s.eye(3)+BH.conjugate().T*(A-h*s.eye(1))**-2*BH
eq('RM24 repeated pole nullspace',Fh*C,s.zeros(3,2))
eq('RM24 repeated pole full mass',C.conjugate().T*Fprime*C,s.eye(2))
eq('RM24 repeated resolvent residue', (W[:,:2]*W[:,:2].conjugate().T)[1:,1:],C*C.conjugate().T)
eq('RM27 energy graph source metric',LE.conjugate().T*LE,Z)
eq('RM27 energy graph energy metric',LE.conjugate().T*H*LE,S)
eq('graph determinant exact identity',Z.det(),((H*H)[:1,:1]).det()/A.det()**2)
z=s.symbols('z')
Fz=DH+z*s.eye(3)-BH.conjugate().T*(A+z*s.eye(1)).inv()*BH
eq('RM18 full block determinant', (H+z*s.eye(4)).det(),(A+z*s.eye(1)).det()*Fz.det())
eq('RM18 full resolvent at zero',H.inv()[1:,1:],S.inv())
for i in range(2):
    for j in range(2):
        eq(f'RM26 joint collision orthogonality {i},{j}',(C[:,i].conjugate().T*Fprime*C[:,j])[0],int(i==j))
ee=eigh(arr(S),arr(Z),eigvals_only=True)
alpha=float(A[0,0]); hv=float(h)
for j in range(2):
    check(f'RM28 lower repeated eigenvalue {j}',hv,ee[j])
    check(f'RM28 upper repeated eigenvalue {j}',ee[j],hv/(1-hv/alpha))

# Exact divided-difference identity with unequal slow eigenvalues.
H2=W*s.diag(s.Rational(1,13),s.Rational(1,7),3,7)*W.conjugate().T
A2=H2[:1,:1]; B2=H2[:1,1:]
hs=[s.Rational(1,13),s.Rational(1,7)]
for i in range(2):
    for j in range(2):
        form=s.eye(3)+B2.conjugate().T*(A2-hs[i]*s.eye(1)).inv()*(A2-hs[j]*s.eye(1)).inv()*B2
        eq(f'RM26 unequal-pole orthogonality {i},{j}',(C[:,i].conjugate().T*form*C[:,j])[0],int(i==j))

def model_checks(label,X,B,U,Tp,Lam):
    q=X.shape[0]; d=U.shape[1]
    Hp=U.conj().T@U; hr=root(Hp); V=U@np.linalg.inv(hr)
    F=U@Tp; K=hr@Tp@Tp.conj().T@hr; Y=Lam@V; theta=Y.conj().T@Y
    beta=op(B); kp=eigh(K,eigvals_only=True)[-1]; km=eigh(K,eigvals_only=True)[0]
    err=2*beta*np.sqrt(kp)+beta**2; a=eigh(theta,eigvals_only=True)[0]
    AA=X@X.conj().T; FF=F@F.conj().T
    HH=np.linalg.inv(AA)
    check(label+' RM7 operator',op(AA-FF),err)
    check(label+' RM7 HS',np.linalg.norm(AA-FF),2*beta*np.sqrt(np.trace(K).real)+np.sqrt(q)*beta**2)
    vb=Y@np.linalg.inv(root(theta))
    for z in [0.,.01,.4,2.]:
        r=Lam@np.linalg.inv(HH+z*np.eye(q))@Lam.conj().T
        r0=Y@np.linalg.inv(np.linalg.inv(K)+z*np.eye(d))@Y.conj().T
        check(label+f' RM9 z={z}',op(r-r0),err)
        dr=err*(1/km+z)/a
        if dr<1:
            rd=vb.conj().T@r@vb; r0d=vb.conj().T@r0@vb
            logratio=np.linalg.slogdet(r0d)[1]-np.linalg.slogdet(rd)[1]
            check(label+f' RM16 lower z={z}',-d*np.log1p(dr),logratio)
            check(label+f' RM16 upper z={z}',logratio,-d*np.log1p(-dr))
    for tau in [.1,1.,10.,100.]:
        hh=Lam@expm(-tau*HH)@Lam.conj().T
        h0=Y@expm(-tau*np.linalg.inv(K))@Y.conj().T
        eh=4/(math.e**2*tau)*(2*np.sqrt(q)*beta*np.sqrt(np.trace(K).real)+q*beta**2)
        check(label+f' RM11 tau={tau}',tn(hh-h0),eh)
        check(label+f' RM12 tau={tau}',abs(np.trace(hh)-np.trace(theta@expm(-tau*np.linalg.inv(K)))),eh)
    return op(theta@K-K@theta)

# Isometric coordinates used only for checking the original metric identities.
gg=root(arr(G)); qq=root(arr(QB))
orig_comm=model_checks('original polynomial fixture',gg@arr(X)@np.linalg.inv(gg),gg@arr(B)@np.linalg.inv(gg),gg@arr(U),arr(Tp)@np.linalg.inv(gg),qq@arr(Lambda)@np.linalg.inv(gg))
rng=np.random.default_rng(210921)
def unitary(n):
    a=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));return np.linalg.qr(a)[0]
comms=[]
for run in range(8):
    n=5;d=2; V=unitary(n)[:,:d]; T=30*unitary(n)[:d,:]
    T[1,:]*=2
    B=.003*(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))
    X=B+V@T; Lam=unitary(n)[:4,:]
    comms.append(model_checks(f'noncommuting fixture {run}',X,B,V,T,Lam))
if not all(x>1e-4 for x in comms): raise AssertionError('noncommuting negative control')
eq('repeated observed mass is not scalar',s.simplify(Theta[0,1]*s.conjugate(Theta[0,1])),s.Rational(1,16))
report={'status':'passed','exact_checks':len(exact),'numeric_checks':len(numeric),'exact':exact,'numeric':numeric,'noncommuting_model_commutators':comms,'original_polynomial_commutator':orig_comm,'scope':'Exact finite original source fixture and independent finite Hermitian models. No numerical certification of native Gamma moments, growing-degree asymptotics, or RH.'}
(OUT/'REDUCED_MODEL_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:report[k] for k in ['status','exact_checks','numeric_checks','scope']}))
