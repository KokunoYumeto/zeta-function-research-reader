"""Independent exact identities for the marked residue transport and its bounds."""
from pathlib import Path
import hashlib
import json
import sympy as s

HERE=Path(__file__).resolve().parent
checks=[]
def check(name,expr):
    if isinstance(expr,s.MatrixBase): ok=all(s.cancel(z)==0 for z in expr)
    else: ok=s.cancel(expr)==0
    assert ok,(name,expr)
    checks.append(name)

g,w=s.symbols('g w',positive=True)
c=(1+s.I)/s.sqrt(2)
Id=s.eye(4)
X=s.Matrix([[0,0,0,-(g+w)**2],[1,0,0,0],[0,1,0,-2*(g-w)],[0,0,1,0]])
H=-2*X*(X**2+(g-w)*Id)
X0=X.subs(w,0)
N=X0**2+g*Id
H0=H.subs(w,0)
R1=H0/(32*g**2)
R2=(g*Id+N)/(32*g**3)
L=c*s.BlockMatrix([[s.zeros(4),R1],[R2,s.zeros(4)]]).as_explicit()
Theta0=2/c*s.BlockMatrix([[s.zeros(4),s.zeros(4)],[H0,s.zeros(4)]]).as_explicit()
check('Limit square phase',L**2-c**2*s.diag(H0,H0)/(1024*g**4))
check('Limit cube phase',L**3+Theta0/(2**16*g**6))
check('Limit fourth power',L**4)
check('Limit rank 6',s.Integer(L.rank()-6))
check('Limit square rank 4',s.Integer((L**2).rank()-4))
check('Limit cube rank 2',s.Integer((L**3).rank()-2))
e0=s.eye(8)[:,0]; e1=s.eye(8)[:,1]
chains=s.Matrix.hstack(*[L**j*e for e in (e0,e1) for j in (3,2,1,0)])
check('Two full chains determinant',chains.det()+1/(2**56*g**22))
J4=s.zeros(4)
for j in range(1,4): J4[j-1,j]=1
check('Two chains action',L*chains-chains*s.diag(J4,J4))
V=s.Matrix([[g,0],[0,g],[1,0],[0,1]])
check('First chain last image',H0*Id[:,0]+2*V[:,1])
check('Second chain last image',H0*Id[:,1]-2*g*V[:,0])

# Exact inverse remainder: Theta^{-1}=L/w+c[[0,Arem],[Brem,0]].
Arem=s.Matrix([[0,-1/(16*g),0,-(2*g+w)/(16*g)],
               [1/(2*(g+w)**2),0,-1/(16*g),0],
               [0,0,0,1/(16*g)],
               [(3*g+w)/(16*g**2*(g+w)**2),0,0,0]])
Brem=s.Matrix([[-(3*g+w)/(16*g**2*(g+w)**2),0,0,0],
               [0,-(3*g+w)/(16*g**2*(g+w)**2),0,0],
               [-(2*g+w)/(32*g**3*(g+w)**2),0,0,0],
               [0,-(2*g+w)/(32*g**3*(g+w)**2),0,0]])
Jinv=s.BlockMatrix([[s.zeros(4),(X**2+(g-w)*Id)*X.inv()/(16*g*w)],
                   [-X.inv()**2/(32*g*w),s.zeros(4)]]).as_explicit()
check('Exact full inverse remainder',c*Jinv-L/w-c*s.BlockMatrix([[s.zeros(4),Arem],[Brem,s.zeros(4)]]).as_explicit())
Abound=s.Matrix([[0,1/(16*g),0,s.Rational(3,16)],
                 [1/(2*g**2),0,1/(16*g),0],[0,0,0,1/(16*g)],
                 [1/(4*g**3),0,0,0]])
Bbound=s.Matrix([[1/(4*g**3),0,0,0],[0,1/(4*g**3),0,0],
                 [3/(32*g**4),0,0,0],[0,3/(32*g**4),0,0]])
beta=s.Rational(9,256)+3/(256*g**2)+1/(4*g**4)+3/(16*g**6)+9/(512*g**8)
check('Remainder squared bound sum',sum(z*z for z in Abound)+sum(z*z for z in Bbound)-beta)
# For entry inequalities on 0<=w<=g, substitute g=w+u. Clearing
# positive denominators leaves polynomials in u,w with nonnegative coefficients.
u=s.symbols('u',positive=True)
for name,mat,bnd in [('upper',Arem,Abound),('lower',Brem,Bbound)]:
    for i in range(4):
        for j in range(4):
            if bnd[i,j]==0: continue
            for sign in (1,-1):
                expr=s.cancel((bnd[i,j]+sign*mat[i,j]).subs(g,w+u))
                num,den=s.fraction(expr)
                # Exact denominator positivity is checked by its polynomial coefficients too.
                for part,label in [(num,'numerator'),(den,'denominator')]:
                    coefficients=s.Poly(s.expand(part),u,w).coeffs()
                    assert all(q>=0 for q in coefficients), (name,i,j,sign,label,part)
                checks.append(f'Remainder entry bound {name}[{i},{j}] sign={sign}')

Hd=(H-H0).applyfunc(lambda z:s.cancel(z/w))
Hdexpected=s.Matrix([[0,2*(2*g+w),0,2*(-g**2+g*w+w**2)],
                     [2,0,2*(2*g+w),0],[0,-2,0,2*(6*g-w)],[0,0,-2,0]])
check('Exact H difference',Hd-Hdexpected)
Hbound=s.Matrix([[0,6*g,0,2*g*g],[2,0,6*g,0],[0,2,0,12*g],[0,0,2,0]])
check('H difference squared bound sum',sum(z*z for z in Hbound)-(4*g**4+216*g**2+12))
for i in range(4):
    for j in range(4):
        if Hbound[i,j]==0: continue
        for sign in (1,-1):
            expr=s.expand((Hbound[i,j]+sign*Hd[i,j]).subs(g,w+u))
            assert all(q>=0 for q in s.Poly(expr,u,w).coeffs()),(i,j,sign,expr)
            checks.append(f'H difference entry bound [{i},{j}] sign={sign}')

# All binomial translation parameters are retained symbolically.
aa,bb,center=s.symbols('aa bb center')
def C(q):
    return s.Matrix(4,4,lambda i,j:s.binomial(j,i)*q**(j-i) if j>=i else 0)
check('Binomial translation composition',C(aa)*C(bb)-C(aa+bb))
check('Centered receiver relation',C(s.Rational(1,2))*C(center-s.Rational(1,2))-C(center))

# This dense exact fixture checks all marked metric cross terms and operators.
K=s.Matrix([[1,2,0,s.I],[0,2,1,0],[0,0,3,1-s.I],[0,0,0,1]])
E=s.Matrix([[1,s.I,2,-1],[2,1,0,s.I],[0,3,-1,2],[1,0,s.I,3]])
O=s.Matrix([[2,1,0,s.I],[0,1,-s.I,2],[0,0,2,1],[0,0,0,3]])
Z=s.Matrix([[1,0,1,s.I],[0,2,s.I,0],[0,0,1,2],[0,0,0,2]])
F=s.Matrix([[2,1+s.I,2,-1],[0,3,s.I,2],[0,0,2,1-s.I],[0,0,0,1]])
G=(F.conjugate().T*F).applyfunc(s.expand)
Q=s.diag(Z,Z)*s.BlockMatrix([[K,s.zeros(4)],[E,O]]).as_explicit()
Qi=s.BlockMatrix([[K.inv()*Z.inv(),s.zeros(4)],
                  [-O.inv()*E*K.inv()*Z.inv(),O.inv()*Z.inv()]]).as_explicit()
check('Marked receiver left inverse',Qi*Q-s.eye(8))
check('Marked receiver right inverse',Q*Qi-s.eye(8))
Gold=(Z.conjugate().T*G*Z).applyfunc(s.expand)
GX=(K.conjugate().T*Gold*K).applyfunc(s.expand)
L0=s.BlockMatrix([[Id,s.zeros(4)],[E,O]]).as_explicit()
Hmarked=(Q.conjugate().T*s.diag(G,G)*Q).applyfunc(s.expand)
check('Every marked Gram cross term',Hmarked-L0.conjugate().T*s.diag(GX,Gold)*L0)
check('Marked Gram determinant',Hmarked.det()-abs(Q.det())**2*G.det()**2)
Lv=L.subs(g,s.Rational(5,2))
Lm=(Qi*Lv*Q).applyfunc(s.expand)
check('Marked nilpotent transport',Q*Lm-Lv*Q)
check('Marked phase cube',Lm**3+Qi*Theta0.subs(g,s.Rational(5,2))*Q/(2**16*s.Rational(5,2)**6))
check('Marked complete flag rank',s.Integer(Lm.rank()-6))
check('Marked square flag rank',s.Integer((Lm**2).rank()-4))
check('Marked cube flag rank',s.Integer((Lm**3).rank()-2))

source=HERE.parent/'MARKED_RESIDUE_TRANSPORT_BODY.tex'
uniform=HERE/'MARKED_RESIDUE_UNIFORM_ERROR_BODY.tex'
record={'result':'PASS','checks':checks,'exact_check_count':len(checks),
        'source':source.name,
        'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest() if source.exists() else None,
        'uniform_extension':uniform.name,
        'uniform_extension_sha256':hashlib.sha256(uniform.read_bytes()).hexdigest() if uniform.exists() else None,
        'scope':'Exact phased powers, full chains, generic inverse remainder and all entry bounds on 0<w<=g, binomial dictionary, dense marked-congruence fixture with every cross term.'}
(HERE/'MARKED_RESIDUE_TRANSPORT_REVIEW_EXACT.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in record.items() if k!='checks'},indent=2))
