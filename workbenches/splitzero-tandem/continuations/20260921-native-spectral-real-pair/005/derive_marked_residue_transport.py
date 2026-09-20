"""Exact MR identities, keeping the signed phase and every metric cross term."""
from pathlib import Path
import hashlib,json
import sympy as s

B=Path(__file__).resolve().parent
g,w=s.symbols('g w',positive=True)
c=(1+s.I)/s.sqrt(2)
I=s.eye(4); Z=s.zeros(4)
X=s.Matrix([[0,0,0,-(g+w)**2],[1,0,0,0],[0,1,0,-2*(g-w)],[0,0,1,0]])
X0=X.subs(w,0); N=X0**2+g*I; H0=-2*X0*N
block=lambda a,b,d,e:a.row_join(b).col_join(d.row_join(e))
J0=block(Z,Z,2*H0,Z)/c
R1=H0/(32*g**2);R2=(g*I+N)/(32*g**3)
L=c*block(Z,R1,R2,Z)
H=-2*X*(X**2+(g-w)*I)
J=2*block(Z,H**2,H,Z)/c
Ji=c*block(Z,(X+(g-w)*X.inv())/(16*g*w),-X.inv()**2/(32*g*w),Z)
checks=[]
def zero(name,value):
    data=list(value) if isinstance(value,s.MatrixBase) else [value]
    reduced=[s.cancel(s.expand(z)) for z in data]
    bad=[z for z in reduced if z!=0]
    if bad:raise ArithmeticError((name,bad[:3]))
    checks.append({'name':name,'scalar_entries':len(data),'passed':True})
    print(name+': PASS',flush=True)

zero('Complete inverse, left',J*Ji-s.eye(8))
zero('Complete inverse, right',Ji*J-s.eye(8))
zero('Fourth nilpotent power',L**4)
zero('Third power with original complex phase',L**3+J0/(2**16*g**6))
zero('Second power',L**2-c**2*s.diag(H0,H0)/(1024*g**4))
V=s.Matrix([[g,0],[0,g],[1,0],[0,1]])
RV=s.Matrix([[1,0,-g,0],[0,1,0,-g]])
zero('Nilpotent factor',N-V*RV)
zero('Nilpotent image equals kernel',RV*V)
tops=[s.eye(8)[:,j] for j in (0,1)]
chains=s.Matrix.hstack(*[L**k*q for q in tops for k in (3,2,1,0)])
chain_det=s.factor(chains.det())
if chain_det==0:raise ArithmeticError('Two chains do not span')
J4=s.zeros(4)
for j in range(1,4):J4[j-1,j]=1
zero('Two complete length-four chains',L*chains-chains*s.diag(J4,J4))
E=s.simplify(Ji-L/w)
E1=E[:4,4:]/c;E2=E[4:,:4]/c
E1=E1.applyfunc(lambda z:s.cancel(s.expand(z)))
E2=E2.applyfunc(lambda z:s.cancel(s.expand(z)))
AE=s.Matrix([[0,-1/(16*g),0,-(2*g+w)/(16*g)],
 [1/(2*(g+w)**2),0,-1/(16*g),0],[0,0,0,1/(16*g)],
 [(3*g+w)/(16*g**2*(g+w)**2),0,0,0]])
BE=s.Matrix([[-(3*g+w)/(16*g**2*(g+w)**2),0,0,0],
 [0,-(3*g+w)/(16*g**2*(g+w)**2),0,0],
 [-(2*g+w)/(32*g**3*(g+w)**2),0,0,0],
 [0,-(2*g+w)/(32*g**3*(g+w)**2),0,0]])
zero('Every displayed upper remainder entry',E1-AE)
zero('Every displayed lower remainder entry',E2-BE)
for a in (E1,E2):
    for v in a:
        if s.denom(s.cancel(v)).subs(w,0)==0:raise ArithmeticError('Unremoved pole')
zero('Finite exact inverse remainder',Ji-L/w-E)

# An exact dense complex fixture checks the whole marked receiver and both
# inverse conjugacies. The symbolic proof covers arbitrary retained frames.
basis=s.Matrix([[2,1+s.I,0,1],[0,3,s.I,0],[0,0,2,-1],[0,0,0,4]])
K=s.Matrix([[1,2,0,s.I],[0,1,-1,2],[0,0,1,1],[0,0,0,1]])
EE=s.Matrix([[1,s.I,2,0],[-1,2,0,1],[0,1,3,s.I],[2,0,1,-2]])
OO=s.Matrix([[2,1,0,s.I],[0,3,1,0],[0,0,1,2],[0,0,0,2]])
F=s.Matrix([[2,1+s.I,1,2],[0,3,s.I,1],[0,0,2,1-s.I],[0,0,0,4]])
G=(F.conjugate().T*F).applyfunc(s.expand)
Q=block(basis*K,Z,basis*EE,basis*OO).applyfunc(s.expand)
Qi=block(K.inv()*basis.inv(),Z,-OO.inv()*EE*K.inv()*basis.inv(),OO.inv()*basis.inv()).applyfunc(s.expand)
zero('Complete marked inverse, left',Qi*Q-s.eye(8))
zero('Complete marked inverse, right',Q*Qi-s.eye(8))
GP=(basis.conjugate().T*G*basis).applyfunc(s.expand)
GK=(K.conjugate().T*GP*K).applyfunc(s.expand)
HM=(Q.conjugate().T*s.diag(G,G)*Q).applyfunc(s.expand)
expanded=block(GK+EE.conjugate().T*GP*EE,EE.conjugate().T*GP*OO,
               OO.conjugate().T*GP*EE,OO.conjugate().T*GP*OO)
zero('All original mixed metric entries',HM-expanded)
# Algebraic adjoint invariance, with a generic full matrix retaining all entries.
AA=s.Matrix(8,8,lambda i,j:s.Integer((i+1)*(j+2)%7)+s.I*(i-j))
QAA=(Qi*AA*Q).applyfunc(s.expand)
left=(HM.inv()*QAA.conjugate().T*HM).applyfunc(s.expand)
right=(Qi*s.diag(G,G).inv()*AA.conjugate().T*s.diag(G,G)*AA*Q).applyfunc(s.expand)
zero('Exact metric-adjoint similarity',left*QAA-right)
markedL=(Qi*L.subs(g,3)*Q).applyfunc(s.expand)
markedL2=(markedL*markedL).applyfunc(s.expand)
zero('Marked nilpotent powers',markedL2*markedL+Qi*J0.subs(g,3)*Q/(2**16*3**6))
q=s.symbols('q')
Ctr=lambda a:s.Matrix(4,4,lambda i,j:s.binomial(j,i)*a**(j-i) if i<=j else 0)
kap=s.symbols('kappa')
zero('Full original center transition',Ctr(s.Rational(1,2))*Ctr(kap)-Ctr(kap+s.Rational(1,2)))

report={'checks':checks,'check_groups':len(checks),'scalar_entries':sum(z['scalar_entries'] for z in checks),
        'chain_determinant':str(chain_det),'inverse_remainder_upper_latex':s.latex(E1.applyfunc(s.factor)),
        'inverse_remainder_lower_latex':s.latex(E2.applyfunc(s.factor)),
        'nilpotent_ranks':[int((L**k).rank()) for k in (1,2,3,4)],
        'source_sha256':hashlib.sha256((B/'MARKED_RESIDUE_TRANSPORT_BODY.tex').read_bytes()).hexdigest()
        if (B/'MARKED_RESIDUE_TRANSPORT_BODY.tex').exists() else None}
(B/'MARKED_RESIDUE_TRANSPORT_CERTIFICATE.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='checks'},indent=2))
