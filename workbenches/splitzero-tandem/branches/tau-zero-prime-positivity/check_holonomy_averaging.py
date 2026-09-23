"""Exact finite checks for HWA; analytic arguments are in the complete proof."""
from pathlib import Path
from itertools import permutations, product
import json
import sympy as s

B=Path(__file__).resolve().parent
checks=[]
def check(name, condition):
    assert condition, name
    checks.append(name)
def perm_matrix(p):
    return s.eye(8)[:,list(p)]
def parity(p):
    return (-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
G=[]
for p in permutations(range(4)):
    for signs in product([1,-1],repeat=4):
        if s.prod(signs)!=parity(p): continue
        q=tuple(2*p[j]+(k if signs[j]==1 else 1-k) for j in range(4) for k in range(2))
        G.append(perm_matrix(q))
check('The determinant-one signed group has 192 different actions',len(G)==192 and len({tuple(m) for m in G})==192)
Sigma=perm_matrix((1,0,3,2,5,4,7,6))
QS=perm_matrix((0,1,3,2,5,4,6,7))
QJ=perm_matrix((0,1,5,4,3,2,7,6))
Pe=(s.eye(8)+Sigma)/2
one=s.ones(8,1); Pc=one*one.T/8
avgS=sum((m.T*QS*m for m in G),s.zeros(8))/192
avgJ=sum((m.T*QJ*m for m in G),s.zeros(8))/192
check('HWA10 conjugate-deck exact conjugation sum',avgS==Pe)
check('HWA10 native exact conjugation sum',avgJ==Pe/3+2*Pc/3)
check('HWA20 vector average',sum(G,s.zeros(8))/192==Pc)
check('Both involutions belong to the actual group',any(QS==m for m in G) and any(QJ==m for m in G))
check('Original native eigenvalues',QJ.eigenvals()=={s.Integer(1):5,s.Integer(-1):3})
check('Original conjugate-deck eigenvalues',QS.eigenvals()=={s.Integer(1):6,s.Integer(-1):2})
check('Averaged native full spectrum',avgJ.eigenvals()=={s.Integer(1):1,s.Rational(1,3):3,s.Integer(0):4})
check('Averaged conjugate-deck full spectrum',avgS.eigenvals()=={s.Integer(1):4,s.Integer(0):4})
check('Native defect full spectrum',(QJ-avgJ).eigenvals()=={s.Integer(0):1,s.Rational(2,3):2,s.Rational(-4,3):1,s.Integer(1):2,s.Integer(-1):2})
check('Conjugate-deck defect full spectrum',(QS-avgS).eigenvals()=={s.Integer(0):4,s.Integer(1):2,s.Integer(-1):2})
E=s.zeros(4,8); I=s.zeros(8,4); O=s.zeros(4,8)
for j in range(4):
    E[j,2*j]=E[j,2*j+1]=s.Rational(1,2)
    O[j,2*j]=s.Rational(1,2);O[j,2*j+1]=-s.Rational(1,2)
    I[2*j,j]=I[2*j+1,j]=1
check('Exact even retraction and kernel rank',E*I==s.eye(4) and I*E==Pe and E.rank()==4)
x=s.Matrix(s.symbols('x0:8'));y=s.Matrix(s.symbols('y0:8'))
check('HWA18 all multiplication-defect coordinates',all(s.expand(z)==0 for z in E*x.multiply_elementwise(y)-(E*x).multiply_elementwise(E*y)-(O*x).multiply_elementwise(O*y)))
ins=s.zeros(8,2)
ins[2,0]=ins[3,0]=ins[4,1]=ins[5,1]=1/s.sqrt(2)
endpoint=s.Matrix([[0,1],[1,0]])
check('HWA29 native endpoint involution',QJ*ins==ins*endpoint)
check('HWA29 exact endpoint pairing',ins.T*QJ*ins==endpoint)
ae=s.Matrix([[s.Rational(1,2),s.Rational(1,6)],[s.Rational(1,6),s.Rational(1,2)]])
check('HWA30 exact averaged endpoint',ins.T*avgJ*ins==ae)
check('HWA32 endpoint defect eigenvalues',(ae-endpoint).eigenvals()=={s.Rational(-1,3):1,s.Rational(4,3):1})
for vec,old,new in [(s.Matrix([1,-1]),-2,s.Rational(2,3)),(s.Matrix([1,1]),2,s.Rational(4,3))]:
    check('Actual endpoint values '+str(list(vec)),(vec.T*endpoint*vec)[0]==old and (vec.T*ae*vec)[0]==new)
# Exact original coefficient-to-point comparison retains i and sqrt(2).
T=s.diag(*[s.Matrix([[1,t],[1,-t]]) for t in [s.I,s.sqrt(2),s.sqrt(2),s.I]])
check('HWA4 retained conjugate-deck coefficient form',s.simplify(T.conjugate().T*QS*T)==s.diag(2,2,2,-4,2,-4,2,2))
check('Finite trace of unit is retained',all((one.T*m*one)[0]==8 for m in [QJ,QS,avgJ,avgS]))
report={'status':'passed','checks':len(checks),'group_order':len(G),'items':checks,'proof':'HOLONOMY_AVERAGING_WEIL_ENDPOINT_DERIVATION.md','scope':'Exact finite matrix and endpoint identities; full analytic proof is written separately.'}
(B/'HOLONOMY_AVERAGING_CHECKS.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({'status':'passed','checks':len(checks),'group_order':len(G)}))
