from pathlib import Path
from itertools import combinations
import hashlib,json
import sympy as s
B0=Path(__file__).resolve().parent
A,B,C,D,P,W=s.symbols('A B C D P W',nonzero=True)
z=s.symbols('z')
checks=[]
def eq(name,expr):
    vals=list(expr) if isinstance(expr,(s.MatrixBase,list,tuple)) else [expr]
    for n,v in enumerate(vals):
        if s.cancel(s.expand(v))!=0:raise AssertionError((name,n,v))
    checks.append({'name':name,'scalar_entries':len(vals),'passed':True})
F=625*A*D**3-125*C*D**2+25*B*C*C*D-4*C**4
p3=P**3+P**2/A+B*P/A+4*C/(5*A)
eq('coefficient polynomial under exact inclusion',s.rem(F.subs(D,-C*P/5),p3,P))
nu=s.Matrix([A,A*W-P-A*P**2,-5*A*P*W/4,A*P**2*W/4])
eq('complete parametrization',F.subs(dict(zip([A,B,C,D],nu)),simultaneous=True))
eq('normalized cubic inverse',p3.subs({B:nu[1],C:nu[2]},simultaneous=True))
eq('parameter W inverse',(B+P+A*P*P).subs(B,nu[1])/A-W)
K=s.diag(1,-C/5,C*C/25)
MD=s.Matrix([[0,0,4*C**4/(625*A)],[1,0,-B*C*C/(25*A)],[0,1,C/(5*A)]])
MP=s.Matrix([[0,0,-4*C/(5*A)],[1,0,-B/A],[0,1,-1/A]])
eq('scalar inclusion multiplication',K*MD-(-C*MP/5)*K)
eq('all normalized companion coefficients',MP**3+MP**2/A+B*MP/A+4*C*s.eye(3)/(5*A))
eq('all original companion coefficients',625*A*MD**3-125*C*MD**2+25*B*C*C*MD-4*C**4*s.eye(3))
eq('inclusion determinant',K.det()+C**3/125)
# Closure of the coefficient conductor: C² times all normal basis products.
for j in range(3):
    mat=K.inv()*C**2*MP**j
    assert all(not s.denom(s.cancel(e)).has(C) for e in mat)
checks.append({'name':'all27 conductor closure coefficients have no C denominator','scalar_entries':27,'passed':True})
J=nu.jacobian([A,P,W])
mi=s.Matrix([5*A*(2*A*P**2+A*W+P)/4,-A*P*(2*A*P**2+2*A*W+P)/4,5*A*A*P*P*W/16,-5*A*A*P**4*W/16])
eq('all Jacobian maximal minors',s.Matrix([J[list(I),:].det() for I in combinations(range(4),3)])-mi)
eq('both complete rank-two kernels',list(J.subs({P:0,W:0})*s.Matrix([0,A,1]))+list(J.subs({W:0,P:-1/(2*A)})*s.Matrix([0,1,0])))
assert J.subs({P:0,W:0}).rank()==2 and J.subs({W:0,P:-1/(2*A)}).rank()==2
checks.append({'name':'both critical Jacobian ranks','scalar_entries':2,'passed':True})
r=s.symbols('r')
h=A*r**4+r**3+B*r*r+C*r+D
hn=h.subs({B:nu[1],C:nu[2],D:nu[3]},simultaneous=True)
eq('all original critical quartic factors',[hn.subs({P:0,W:0})-r**3*(A*r+1),hn.subs({W:0,P:-1/(2*A)})-A*r*r*(r+1/(2*A))**2])
eq('both critical derivative remainders',[s.rem(s.diff(r**3*(A*r+1),r),r**3,r)-3*r*r,s.diff(r**3*(A*r+1),r).subs(r,-1/A)+1/A**2,s.rem(s.diff(A*r*r*(r+1/(2*A))**2,r),r*r,r)-r/(2*A),s.rem(s.diff(A*r*r*(r+1/(2*A))**2,r).subs(r,r-1/(2*A)),r*r,r)-r/(2*A)])
X=s.Matrix([[0,0,0,-D/A],[1,0,0,-C/A],[0,1,0,-B/A],[0,0,1,-1/A]])
Z=s.Matrix([[C,-4*D,D/A,D*(2*A*B-1)/A**2],[2*B,-3*C,-(4*A*D-C)/A,(2*A*B*C+A*D-C)/A**2],[3,-2*B,-(3*A*C-B)/A,-(4*A*A*D-2*A*B*B-A*C+B)/A**2],[4*A,-1,-(2*A*B-1)/A,-(3*A*A*C-3*A*B+1)/A**2]])
eq('every derivative-action entry',Z-(4*A*X**3+3*X**2+2*B*X+C*s.eye(4)))
eq('original root quartic',A*X**4+X**3+B*X**2+C*X+D*s.eye(4))
X8=s.diag(X,X)
Y8=s.BlockMatrix([[s.zeros(4),Z],[s.eye(4),s.zeros(4)]]).as_explicit()
eq('all signed commutator entries',X8*Y8-Y8*X8)
eq('all signed square entries',Y8**2-(4*A*X8**3+3*X8**2+2*B*X8+C*s.eye(8)))
KK=s.kronecker_product(K,s.eye(8))
full=[]
for name,Q in [('root',X8),('sign',Y8)]:
    Q0=Q.subs(D,0);Q1=Q.diff(D)
    eq(name+' exact first degree in D',Q-Q0-D*Q1)
    QS=s.kronecker_product(s.eye(3),Q0)+s.kronecker_product(MD,Q1)
    QN=s.kronecker_product(s.eye(3),Q0)+s.kronecker_product(-C*MP/5,Q1)
    eq('all24 inclusion '+name+' entries',KK*QS-QN*KK)
    full.append(QS)
M=s.Matrix([[0,0,-4*C**3/(125*A)],[-5/C,0,B*C/(5*A)],[0,-5/C,-1/A]])
MI=s.Matrix([[-5*B/(4*C),-C/5,0],[25/(4*C*C),0,-C/5],[-125*A/(4*C**3),0,0]])
eq('distinguished action comparison',K*M-MP*K)
eq('both full inverse products',list(M*MI-s.eye(3))+list(MI*M-s.eye(3)))
eq('action determinant and characteristic',[M.det()+4*C/(5*A),MI.det()+5*A/(4*C),M.charpoly(z).as_expr()-(z**3+z*z/A+B*z/A+4*C/(5*A))])
MM=s.kronecker_product(M,s.eye(8))
for name,Q in zip(['root','sign'],full):eq('all24 distinguished '+name+' commutation',MM*Q-Q*MM)
N=s.Matrix([[0,0,0],[-5,0,0],[0,-5,0]])
eq('full residue limit',(C*M).applyfunc(lambda x:s.limit(x,C,0))-N)
L=s.zeros(3);L[2,0]=-125*A/4
eq('full cubic inverse limit',(C**3*MI).applyfunc(lambda x:s.limit(x,C,0))-L)
NN=s.kronecker_product(N,s.eye(8))
assert [NN.rank(),(NN**2).rank(),(NN**3).rank()]==[16,8,0]
checks.append({'name':'all24 residue power ranks16,8,0','scalar_entries':3,'passed':True})
x,y,zz,w=s.symbols('x y zz w',complex=True)
Zinv=s.Matrix([[x,y,0],[zz,0,y],[w,0,0]])
Q=Zinv.H*Zinv
rr=s.conjugate(x)*x+s.conjugate(zz)*zz+s.conjugate(w)*w
tt=s.conjugate(y)*y;qq=s.conjugate(w)*w
eq('all exact finite spectral coefficients',Q.charpoly(z).as_expr()-(z-tt)*(z*z-(rr+tt)*z+tt*qq))
# A dense exact complex metric checks both original roles without diagonalizing them.
G=s.Matrix([[3,1+s.I],[1-s.I,4]])
Zfix=MI.subs({A:s.Rational(-1,2),B:2+s.I,C:s.Rational(3,7)+s.I/5})
Gbig=s.kronecker_product(s.eye(3),G)
V=s.kronecker_product(Zfix,s.eye(2))
eq('full metric cancellation with complex off-diagonal entries',Gbig.inv()*V.H*Gbig*V-s.kronecker_product(Zfix.H*Zfix,s.eye(2)))
GU=s.Matrix([[7,2-s.I],[2+s.I,5]])
GW=s.Matrix([[4,1+s.I],[1-s.I,6]])
eq('cross-receiver full metric square',s.kronecker_product(s.eye(3),GW).inv()*V.H*s.kronecker_product(s.eye(3),GU)*V-s.kronecker_product(Zfix.H*Zfix,GW.inv()*GU))
src=B0/'ES_COEFFICIENT_TOTAL_EXTENSION_BODY.tex'
out={'status':'PASS','check_groups':len(checks),'scalar_entries':sum(c['scalar_entries'] for c in checks),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'checks':checks,'scope':'Exact full inclusion/action identities and spectra. Ring normality, conductor necessity, Tor interpretation, positivity and all limiting exterior proofs are in the source; not inferred from finite fixtures.'}
(B0/'ES_COEFFICIENT_TOTAL_EXTENSION_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ['status','check_groups','scalar_entries','source_sha256']}))
