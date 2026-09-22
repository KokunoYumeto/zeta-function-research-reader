"""Exact full-source and subquotient identities in complex finite fixtures."""
from pathlib import Path
import json
import sympy as s
I=s.I
checks=[]
def verify(label,X,Y):
    if isinstance(X,s.MatrixBase):ok=(X-Y).applyfunc(s.simplify)==s.zeros(*X.shape)
    else:ok=s.simplify(X-Y)==0
    if not ok:raise ArithmeticError(label)
    checks.append(label)
A=s.Matrix([[1,I,2,0],[0,2,1-I,1],[1,0,1,I],[0,1,0,2]])
G=A.H*A+s.eye(4)
K=s.eye(4)[:,:2];Lmb=s.Matrix([[0,0,1,0],[0,0,0,1]])
HK=K.H*G*K;Q=(Lmb*G.inv()*Lmb.H).inv();L=G.inv()*Lmb.H*Q
verify('Original full projection resolution',K*HK.inv()*K.H*G+L*Lmb,s.eye(4))
vectors=[s.Matrix([1,I,2,1-I]),K*s.Matrix([1,I]),L*s.Matrix([2,I]),s.zeros(4,1)]
for idx,u in enumerate(vectors):
    rho=(u.H*G*u)[0];b=K.H*G*u;chi=(b.H*HK.inv()*b)[0];beta=(u.H*Lmb.H*Q*Lmb*u)[0]
    verify(f'{idx} complete energy split',rho,chi+beta)
    Gn=(G.inv()+u*u.H).inv();HKn=K.H*Gn*K
    verify(f'{idx} full inverse update',Gn,G-G*u*u.H*G/(1+rho))
    verify(f'{idx} kernel metric update',HKn,HK-b*b.H/(1+rho))
    verify(f'{idx} positive determinant fraction',HKn.det()/HK.det(),(1+beta)/(1+rho))
    R=s.Matrix([[1,1+I]])
    Qz=(R*HKn.inv()*R.H).inv();Sz=HKn.inv()*R.H*Qz
    verify(f'{idx} full affine minimum section',R*Sz,s.eye(1))
    verify(f'{idx} full affine minimum metric',Sz.H*HKn*Sz,Qz)
    Z=s.Matrix([[-1-I],[1]])
    verify(f'{idx} complete quotient orthogonality',Z.H*HKn*Sz,s.zeros(1,1))
P=Path(__file__).parent
record={'passed':len(checks),'checks':checks,'scope':'Exact auxiliary complex matrices; includes kernel, minimum-section, mixed and zero source columns. No native arithmetic period or analytic asymptotic tested.'}
(P/'receiver_exact.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record,indent=2))
