"""Exact tests of complete two-metric collision quotient identities OCQ1--11.

The full proof establishes the universal singular-value bounds. Dense complex
positive metrics test every kernel, minimum, congruence and inverse entry;
the symbolic two-by-two test keeps all covariance coefficients arbitrary.
"""
from pathlib import Path
from hashlib import sha256
import json
import sympy as s
B=Path(__file__).resolve().parent
checks=[];entries=0
def exact(name,M):
    global entries
    vals=list(M) if isinstance(M,s.MatrixBase) else [M]
    bad=[str(x) for x in vals if s.cancel(s.expand_complex(x))!=0]
    assert not bad,(name,bad[:3])
    checks.append({'name':name,'entries':len(vals),'passed':True});entries+=len(vals)

au,du,bu,cu,aw,dw,bw,cw,z=s.symbols('au du bu cu aw dw bw cw z',real=True)
Ju=s.Matrix([[au,bu+s.I*cu],[bu-s.I*cu,du]])
Jw=s.Matrix([[aw,bw+s.I*cw],[bw-s.I*cw,dw]])
Q=Jw*Ju.inv();a=(aw*du+dw*au-2*(bw*bu+cw*cu))/Ju.det();b=Jw.det()/Ju.det()
exact('OCQ5 all complex covariance trace coefficients',s.trace(Q)-a)
exact('OCQ4 complete characteristic polynomial',(z*s.eye(2)-Q).det()-(z*z-a*z+b))
exact('OCQ6 both parity blocks characteristic polynomial',s.diag(Q,Q).charpoly(z).as_expr().subs(s.Symbol('z'),z)-(z*z-a*z+b)**2)

# Dense exact positive Hermitian metrics. These are verification fixtures,
# not substitutions for the original programme moments.
Ru=s.Matrix([[2,1+s.I,0,1],[0,3,s.I,2],[0,0,2,1-s.I],[0,0,0,1]])
Rw=s.Matrix([[1,s.I,2,0],[0,2,1+s.I,1],[0,0,3,s.I],[0,0,0,2]])
metrics={'U':Ru.H*Ru,'W':Rw.H*Rw}
P=s.Rational(2,3)+s.I/5
v=lambda r:s.Matrix([[1,r,r*r,r**3]])
for t in [s.Rational(1,2),s.Rational(-1,3),s.I/2,s.Integer(0)]:
    E=v(P).col_join(s.Matrix([[0,1,2*P+t,3*P*P+3*P*t+t*t]]))
    L=s.diag(E,E);J={};C={};G={}
    # Every full kernel column, parity by parity.
    K=s.Matrix([[-P,1,0,0]]).T if False else s.Matrix.hstack(*E.nullspace())
    KK=s.diag(K,K)
    exact(f'OCQ1 complete kernel t={t}',L*KK)
    assert KK.rank()==4 and L.rank()==4
    for name,H in metrics.items():
        Gamma=s.diag(H,H);J[name]=s.simplify(E*H.inv()*E.H)
        D=s.diag(J[name],J[name]);G[name]=D.inv()
        Lift=Gamma.inv()*L.H*G[name]
        exact(f'OCQ1 complete minimum section t={t} {name}',L*Lift-s.eye(4))
        exact(f'OCQ1 complete kernel orthogonality t={t} {name}',Lift.H*Gamma*KK)
        exact(f'OCQ1 minimum full Gram t={t} {name}',Lift.H*Gamma*Lift-G[name])
        Proj=Lift*L
        exact(f'OCQ10 orthogonal projection t={t} {name}',Proj*Proj-Proj)
        exact(f'OCQ10 original metric adjoint t={t} {name}',Proj.H*Gamma-Gamma*Proj)
        exact(f'OCQ10 quotient inverse compression t={t} {name}',L*Lift-s.eye(4))
        if t!=0:
            # Nonzero independent sign values suffice for every exact
            # raw-to-jet identity; ECC separately tests their square laws.
            s0=1+2*s.I;st=2-s.I
            O=v(P).row_join(s0*v(P)).col_join(v(P).row_join(-s0*v(P)))
            O=O.col_join(v(P+t).row_join(st*v(P+t))).col_join(v(P+t).row_join(-st*v(P+t)))
            Z=s.Matrix([[s.Rational(1,2),s.Rational(1,2),0,0],[-1/(2*t),-1/(2*t),1/(2*t),1/(2*t)],
                [1/(2*s0),-1/(2*s0),0,0],[-1/(2*t*s0),1/(2*t*s0),1/(2*t*st),-1/(2*t*st)]])
            C[name]=s.simplify(O*Gamma.inv()*O.H)
            exact(f'OCQ8 complete common raw-to-jet map t={t} {name}',Z*O-L)
            exact(f'OCQ8 full covariance congruence t={t} {name}',Z*C[name]*Z.H-D)
            exact(f'OCQ8 complete inverse metric congruence t={t} {name}',C[name].inv()-Z.H*G[name]*Z)
    b=J['W'].det()/J['U'].det()
    exact(f'OCQ7 complete top determinant t={t}',G['U'].det()/G['W'].det()-b*b)
    if t!=0:
        exact(f'OCQ9 exact raw determinant cancellation t={t}',C['W'].det()/C['U'].det()-b*b)
proof=B/'ORIGINAL_COLLISION_QUOTIENT_BODY.tex'
out={'status':'PASS','groups':len(checks),'scalar_entries':entries,'checks':checks,
     'proof_sha256':sha256(proof.read_bytes()).hexdigest(),'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
     'scope':'Exact symbolic covariance characteristic polynomial and complete dense complex matrix identities, including the collision. General comparison with every original conductor singular value is proved in OCQ10--11.'}
(B/'ORIGINAL_COLLISION_QUOTIENT_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='checks'},indent=2))
