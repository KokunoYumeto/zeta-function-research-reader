"""Exact supplementary checks for RD1--RD31; the source contains the full proofs."""
from pathlib import Path
import json,hashlib
import sympy as s
P=Path(__file__).resolve().parent
x,T,e,z=s.symbols('x T epsilon z')
checks=[]
def check(name,actual,expected):
    if isinstance(actual,s.MatrixBase):
        ok=actual.shape==expected.shape and all(s.expand(a-b)==0 for a,b in zip(actual,expected))
    else:ok=s.simplify(actual-expected)==0
    assert ok,(name,actual,expected)
    checks.append(name)
def algebra(var,poly,t2,basis):
    def red(a):
        a=s.rem(s.Poly(s.expand(a),T),s.Poly(T*T-t2,T)).as_expr()
        return s.expand(sum(s.rem(s.Poly(a.coeff(T,k),var),s.Poly(poly,var)).as_expr()*T**k for k in range(2)))
    def vec(a):
        p=s.Poly(red(a),var,T)
        return s.Matrix([p.coeff_monomial(b) for b in basis])
    def mul(a):return s.Matrix.hstack(*[vec(a*b) for b in basis])
    return red,vec,mul
bb=[1,x,x*x,T,x*T,x*x*T]
bc=[1,e,T,e*T]
rb,vb,mb=algebra(x,x*x*(x+3),3*x*(x+2),bb)
rc,vc,mc=algebra(e,e*e,6*e,bc)
lb=lambda f:vb(f)[5]
lc=lambda f:vc(f)[3]
GB=s.Matrix([[lb(a*b) for b in bb] for a in bb])
GC=s.Matrix([[lc(a*b) for b in bc] for a in bc])
G=s.Matrix([[0,0,1],[0,1,-3],[1,-3,9]])
check('integral B Gram',GB,s.BlockMatrix([[s.zeros(3),G],[G,s.zeros(3)]]).as_explicit())
check('integral C Gram',GC,s.Matrix([[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]))
check('G inverse',G.inv(),s.Matrix([[0,3,1],[3,1,0],[1,0,0]]))
check('B determinant',abs(GB.det()),1)
check('C determinant',abs(GC.det()),1)
JB=6*x*(x+2)*T
JC=4*e*T
n1=x*(x+3)
n3=T*n1
db=lambda f:rb(s.diff(rb(f),T)*(-n3/s.Integer(8)))
dc=lambda f:rc(s.diff(rc(f),T)*(-3*e*T/s.Integer(8)))
q=lambda f:rc(rb(f).subs(x,e))
for i,b in enumerate(bb):
    check(f'B trace {i}',mb(b).trace(),lb(JB*b))
    check(f'quotient dual {i}',lc(q(b)),lb((x+3)*b))
    check(f'quotient derivation {i}',q(db(b)),dc(q(b)))
    check(f'B dual Lie {i}',-lb(db(b)),lb(n1*b)/8)
    check(f'B square zero {i}',db(db(b)),0)
    check(f'quotient trace {i}',mc(q(b)).trace(),lb(4*n3*b))
for i,b in enumerate(bc):
    check(f'C trace {i}',mc(b).trace(),lc(JC*b))
    check(f'C dual Lie {i}',-lc(dc(b)),3*lc(e*b)/8)
    check(f'C square zero {i}',dc(dc(b)),0)
check('trace decomposition',rb(JB-4*n3-2*x*x*T),0)
check('B Jacobian Lie',db(JB),0)
check('B weight Jacobian',rb(n1*JB),0)
check('C Jacobian Lie',dc(JC),0)
check('C weight Jacobian',rc(e*JC),0)
check('integral coefficient Jacobian',s.Matrix([[3*x*(x+2),-6*(x+1)],[0,2*T]]).det(),JB)
J=s.zeros(4)
for i in range(4):J[i,3-i]=s.I*(-1)**i
K=s.zeros(4);K[3,0]=-4*s.I
D=s.zeros(4);D[3,1]=-s.Rational(1,16)
a=s.symbols('a',real=True)
V=s.eye(4)+a*D
check('residue Hermitian',J.conjugate().T,J)
check('trace via residue',J*K,s.diag(4,0,0,0))
check('K selfadjoint',K.conjugate().T*J,J*K)
check('K square zero',K*K,s.zeros(4))
defect=s.zeros(4);defect[0,1]=-s.I*a/16;defect[1,0]=s.I*a/16
check('full residue variation',V.conjugate().T*J*V-J,defect)
check('trace variation',V.conjugate().T*(J*K)*V,J*K)
check('residue involution square',J*J,s.eye(4))
check('residue inertia trace',s.trace(J),0)
d=s.expand(((z-s.Rational(1,2)-s.Rational(1,4))**2+9)*((z-s.Rational(1,2)+s.Rational(1,4))**2+9))
for m in [1,2,3]:
    h=s.expand(d**m);n=4*m
    rem=lambda p:s.rem(s.Poly(p,z),s.Poly(h,z)).as_expr()
    lam=lambda p:rem(p).coeff(z,n-1)
    sharp=lambda p:s.conjugate(p).subs(s.conjugate(z),1-z)
    check(f'packet reflection m{m}',h.subs(z,1-z),h)
    Gp=s.Matrix([[lam(z**(i+j)) for j in range(n)] for i in range(n)])
    check(f'packet duality determinant m{m}',abs(Gp.det()),1)
    Q=s.Matrix([[s.I*lam(sharp(z**i)*z**j) for j in range(n)] for i in range(n)])
    M=s.Matrix.hstack(*[s.Matrix([rem(-s.I*s.diff(h,z)*z**j).coeff(z,i) for i in range(n)]) for j in range(n)])
    check(f'packet residue Hermitian m{m}',Q.conjugate().T,Q)
    check(f'packet K adjoint m{m}',M.conjugate().T*Q,Q*M)
    check(f'packet K rank m{m}',M.rank(),4)
    if m>1:check(f'packet K square m{m}',M*M,s.zeros(n))
    for j in range(n):
        reg=s.Matrix.hstack(*[s.Matrix([rem(z**(j+k)).coeff(z,i) for i in range(n)]) for k in range(n)])
        check(f'packet exact trace m{m} basis{j}',reg.trace(),lam(s.diff(h,z)*z**j))
proof=P/'COLLISION_RESIDUE_DUALITY_DERIVATION.md'
report={'status':'passed','count':len(checks),'checks':checks,'proof':proof.name,'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),'scope':'Exact integral and rational identities supplement the complete RD proofs. Sample quartets are polynomial checks, not claimed zeta zeros.'}
(P/'COLLISION_RESIDUE_DUALITY_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':report['status'],'count':len(checks)}))
