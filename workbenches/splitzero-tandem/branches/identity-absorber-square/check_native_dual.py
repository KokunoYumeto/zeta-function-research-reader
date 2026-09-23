from pathlib import Path
import json
import sympy as s
P=Path(__file__).parent
G=s.diag(1,4,9,16)
f=s.Matrix([1,0,0,0]);g=s.Matrix([0,s.Rational(1,2),0,0]);e=s.Matrix([0,0,s.Rational(1,3),0]);h=s.Matrix([0,0,0,s.Rational(1,4)])
dag=lambda x:x.H*G
ep=s.Integer(5);R=ep*f*dag(e);T=s.sqrt(ep)*(f*dag(g)+g*dag(e));W=s.I*(G*R-R.H*G)
checks=[]
def eq(name,a,b):
    z=a-b
    if isinstance(z,s.MatrixBase):good=all(s.simplify(c)==0 for c in z)
    else:good=s.simplify(z)==0
    if not good:raise ArithmeticError(name)
    checks.append(name)
eq('actual orthonormal metric',s.Matrix.hstack(f,g,e,h).H*G*s.Matrix.hstack(f,g,e,h),s.eye(4))
eq('nonzero nilpotent square',R**2,s.zeros(4))
eq('root square retains epsilon',T**2,R)
eq('root cube',T**3,s.zeros(4))
eq('Laurent inverse',(s.eye(4)+T)*(s.eye(4)-T+T**2),s.eye(4))
eq('node j goes to original R',T*T,R)
eq('node j squared relation',(T*T)**2,s.zeros(4))
eq('dual module unit basis',R*e,ep*f)
eq('dual module scalar nilpotent part',R*f,s.zeros(4,1))
eq('nonflat g direction',R*g,s.zeros(4,1))
eq('nonflat h direction',R*h,s.zeros(4,1))
eq('current zero g',W*g,s.zeros(4,1))
eq('current zero h',W*h,s.zeros(4,1))
eq('rank of R',R.rank(),1)
eq('rank of T',T.rank(),2)
eq('current nullity',4-W.rank(),2)
eq('Tor dimension',(4-R.rank())-R.rank(),2)
a,b,c,d=s.symbols('a b c d')
eq('entire dual-number product',(a*s.eye(4)+b*R)*(c*s.eye(4)+d*R),a*c*s.eye(4)+(a*d+b*c)*R)
Pi=e*dag(e)+f*dag(f);H=s.eye(4)-Pi
eq('support idempotent',Pi**2,Pi)
eq('support left primitive',Pi*R,R)
eq('support right primitive',R*Pi,R)
eq('square root plane diagonal',Pi*T*Pi,s.zeros(4))
eq('square root complementary diagonal',H*T*H,s.zeros(4))
eq('mixed product on plane',(Pi*T*H)*(H*T*Pi),R)
eq('mixed reverse product',(H*T*Pi)*(Pi*T*H),s.zeros(4))
m,n=s.symbols('m n',integer=True)
eq('supported monoid including signed integers',(Pi+m*R)*(Pi+n*R),Pi+(m+n)*R)
a0,a1,a2,b0,b1,b2=s.symbols('a0 a1 a2 b0 b1 b2')
rho=lambda x,y,z:x*H+y*Pi+z*R
eq('full support-algebra product',rho(a0,a1,a2)*rho(b0,b1,b2),rho(a0*b0,a1*b1,a1*b2+a2*b1))
nn=e+f+s.I*g;PB=s.eye(4)-nn*dag(nn)/3
Phi=lambda X:PB*X*PB
eq('actual fixture observation projection',PB**2,PB)
eq('complete support compression defect',Phi(Pi)-Phi(Pi)**2,PB*Pi*(s.eye(4)-PB)*Pi*PB)
eq('complete primitive compression defect',-Phi(R)**2,PB*R*(s.eye(4)-PB)*R*PB)
eq('entire multiplicative defect',Phi(rho(a0,a1,a2)*rho(b0,b1,b2))-Phi(rho(a0,a1,a2))*Phi(rho(b0,b1,b2)),PB*rho(a0,a1,a2)*(s.eye(4)-PB)*rho(b0,b1,b2)*PB)
if Phi(Pi)**2==Phi(Pi):raise ArithmeticError('Unsupported compression homomorphism escaped')
if R*R==R:raise ArithmeticError('Wrong square-root negative control escaped')
if T*T==s.zeros(4):raise ArithmeticError('Wrong infinitesimal negative control escaped')
r={'status':'passed','exact_checks':len(checks),'negative_controls_rejected':3,'scope':'Auxiliary 4-dimensional nonidentity metric; exact maps only, not a native-period numerical evaluation','checks':checks}
(P/'NATIVE_DUAL_CHECKS.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in r.items() if k!='checks'},indent=2))
