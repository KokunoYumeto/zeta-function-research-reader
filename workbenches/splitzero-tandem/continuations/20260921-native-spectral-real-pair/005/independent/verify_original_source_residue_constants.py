"""Exact algebra for RS1--29, including dense complex positive Grams."""
from pathlib import Path
import hashlib
import json
import sympy as s

HERE=Path(__file__).resolve().parent
checks=[]
def check(name,expr):
    if isinstance(expr,s.MatrixBase): ok=all(s.cancel(x)==0 for x in expr)
    else: ok=s.cancel(expr)==0
    assert ok,(name,expr)
    checks.append(name)

g,w,b=s.symbols('g w b',positive=True)
X=s.Matrix([[0,0,0,-(g+w)**2],[1,0,0,0],[0,1,0,-2*(g-w)],[0,0,1,0]])
Id=s.eye(4)
H=-2*X*(X**2+(g-w)*Id)
check('RS1 quartic companion identity',X**4+2*(g-w)*X**2+(g+w)**2*Id)
check('RS3 square identity',H**2+16*g*w*X**2)
check('RS3 X determinant',X.det()-(g+w)**2)
J=2*s.BlockMatrix([[s.zeros(4),H**2],[H,s.zeros(4)]]).as_explicit()
Jinv=s.BlockMatrix([[s.zeros(4),(X**2+(g-w)*Id)*X.inv()/(16*g*w)],[-X.inv()**2/(32*g*w),s.zeros(4)]]).as_explicit()
check('RS4 full left inverse',Jinv*J-s.eye(8))
check('RS4 full right inverse',J*Jinv-s.eye(8))
c=(1+s.I)/s.sqrt(2)
check('RS3 reflected phase modulus',c*s.conjugate(c)-1)
check('RS18 reflected phase determinant',c**8-1)
X0=X.subs(w,0)
N=X0**2+g*Id
H0=H.subs(w,0)
V=s.Matrix([[g,0],[0,g],[1,0],[0,1]])
R=s.Matrix([[1,0,-g,0],[0,1,0,-g]])
Jg=s.Matrix([[0,-g],[1,0]])
check('RS5 N square',N**2)
check('RS5 H0 square',H0**2)
check('RS9 N factorization',N-V*R)
check('RS9 factor cross vanishes',R*V)
check('RS9 restricted X factorization',X0*V-V*Jg)
check('RS9 H0 factorization',H0+2*V*Jg*R)
check('RS6 inverse square identity',X0.inv()**2+(g*Id+N)/g**2)
res=(w*Jinv).applyfunc(lambda z:s.cancel(z).subs(w,0))
check('RS6 full pole coefficient',res-s.BlockMatrix([[s.zeros(4),H0/(32*g**2)],[(g*Id+N)/(32*g**3),s.zeros(4)]]).as_explicit())
check('RS18 exact derivative determinant',H.det()-256*g**2*w**2*(g+w)**2)
check('RS18 exact multiplier determinant via blocks',2**8*H.det()**3-2**32*g**6*w**6*(g+w)**6)

chi=s.symbols('chi',positive=True)
lam=s.symbols('lambda')
T=s.Matrix([[g,chi],[0,g]])
check('RS13 triangular squared characteristic polynomial',(T.T*T).charpoly(lam).as_expr()-(lam**2-(2*g**2+chi**2)*lam+g**4))
plus=(s.sqrt(4*g*g+chi*chi)+chi)/(64*g**3)
minus=(s.sqrt(4*g*g+chi*chi)-chi)/(64*g**3)
check('RS17 positive pair product',plus*minus-1/(2**10*g**4))
print('Generic identities and singular pair checked.',flush=True)

# Dense, non-parity Grams check the entire squared singular polynomial.
# The general proof is RS9--13; finite fixtures do not replace that proof.
L1=s.Matrix([[2,1+s.I,-1,2-s.I],[0,3,2*s.I,1],[0,0,2,1-s.I],[0,0,0,1]])
L2=s.Matrix([[1,2-s.I,1+s.I,-1],[0,2,3+s.I,2],[0,0,3,-2*s.I],[0,0,0,2]])
for gvalue in (s.Rational(1,3),s.Rational(7,2),s.Integer(11)):
    for lindex,L in enumerate((L1,L2)):
        G=(L.conjugate().T*L).applyfunc(s.expand)
        Ginv=G.inv().applyfunc(s.expand)
        NN=N.subs(g,gvalue); HH=H0.subs(g,gvalue)
        VV=V.subs(g,gvalue); RR=R.subs(g,gvalue); JJ=Jg.subs(g,gvalue)
        P=(RR*Ginv*RR.conjugate().T).applyfunc(s.expand)
        Q=(VV.conjugate().T*G*VV).applyfunc(s.expand)
        KN=(Ginv*NN.conjugate().T*G*NN).applyfunc(s.expand)
        KH=(Ginv*HH.conjugate().T*G*HH).applyfunc(s.expand)
        an=s.expand(s.trace(KN)); bn=s.expand((an**2-s.trace(KN**2))/2)
        ah=s.expand(s.trace(KH)); bh=s.expand((ah**2-s.trace(KH**2))/2)
        suffix=f'g={gvalue} Gram={lindex}'
        check('RS10 N trace '+suffix,an-s.trace(P*Q))
        check('RS10 N product '+suffix,bn-P.det()*Q.det())
        check('RS10 H trace '+suffix,ah-4*s.trace(P*JJ.conjugate().T*Q*JJ))
        check('RS10 H product '+suffix,bh-16*gvalue**2*bn)
        check('RS8 N polynomial '+suffix,KN.charpoly(lam).as_expr()-lam**2*(lam**2-an*lam+bn))
        check('RS8 H polynomial '+suffix,KH.charpoly(lam).as_expr()-lam**2*(lam**2-ah*lam+bh))
        GG=gvalue*Id+NN
        KGG=(Ginv*GG.conjugate().T*G*GG).applyfunc(s.expand)
        base=lam**2-2*gvalue**2*lam+gvalue**4
        expected=base**2-an*lam*base+bn*lam**2
        check('RS13 complete four-value polynomial '+suffix,KGG.charpoly(lam).as_expr()-expected)
print('All six complete dense-metric spectral fixtures checked.',flush=True)

z0,z1,z2,z3=s.symbols('unit0 unit1 unit2 unit3',nonzero=True)
xi0=1/z0; xi1=-z1/z0**2
xi2=z1**2/z0**3-z2/z0**2
xi3=-z1**3/z0**4+2*z1*z2/z0**3-z3/z0**2
xi=[xi0,xi1,xi2,xi3]
Txi=s.Matrix(4,4,lambda i,j:xi[j-i] if j>=i else 0)
Tunit=s.Matrix(4,4,lambda i,j:[z0,z1,z2,z3][j-i] if j>=i else 0)
V0=s.Matrix([[1,0,b,0],[0,1,0,3*b+2],[0,0,2,0],[0,0,0,6]])
F=s.Matrix([[xi0,xi1,b*xi0+2*xi2,(3*b+2)*xi1+6*xi3],[0,xi0,2*xi1,(3*b+2)*xi0+6*xi2],[0,0,2*xi0,6*xi1],[0,0,0,6*xi0]])
BF=s.Matrix([[z0,z1,z2-b*z0/2,z3-b*z1/2],[0,z0,z1,z2-(3*b+2)*z0/6],[0,0,z0/2,z1/2],[0,0,0,z0/6]])
check('RS21 finite reciprocal',Txi*Tunit-Id)
check('RS24 source coefficient construction',F-Txi*V0)
check('RS25 full inverse left',BF*F-Id)
check('RS25 full inverse right',F*BF-Id)
check('RS25 inverse construction',BF-V0.inv()*Tunit)
check('RS26 source triangular determinant',F.det()-12/z0**4)
Di=s.diag(1,s.I,-1,-s.I)
check('RS24 physical phase is unitary',Di.conjugate().T*Di-Id)

# This source-metric fixture retains all complex inverse coefficients and weights.
values={b:s.Rational(3,2),z0:2+s.I,z1:-1+2*s.I,z2:3-s.I,z3:2+3*s.I}
fv=F.subs(values).applyfunc(s.expand_complex)
bfv=BF.subs(values).applyfunc(s.expand_complex)
k=[s.rf(s.Rational(3,2),2+j)/s.factorial(2+j) for j in range(4)]
mass=s.symbols('original_mass',positive=True)
GU=(mass*Di.conjugate().T*fv.conjugate().T*s.diag(*k)*fv*Di).applyfunc(s.expand)
GUinv=(Di.conjugate().T*bfv*s.diag(*[1/kk for kk in k])*bfv.conjugate().T*Di/mass).applyfunc(s.expand)
check('RS25 dense source metric inverse',GU*GUinv-Id)
check('RS26 dense source metric determinant',GU.det()-144*mass**4*s.prod(k)*abs(1/(2+s.I))**8)

src=HERE/'ORIGINAL_SOURCE_RESIDUE_SINGULAR_CONSTANTS.tex'
record={'result':'PASS','exact_check_count':len(checks),'checks':checks,
        'source':src.name,'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
        'scope':'Generic operator identities, full inverse and residue, two-by-two singular derivation, full characteristic polynomials for six dense complex metric fixtures, exact original moment inverse and source metric.'}
(HERE/'ORIGINAL_SOURCE_RESIDUE_SINGULAR_CONSTANTS_EXACT.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in record.items() if k!='checks'},indent=2))
