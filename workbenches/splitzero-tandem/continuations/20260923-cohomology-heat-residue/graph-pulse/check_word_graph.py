"""Exact auxiliary checks for GC8, GC18--22; no simulated zeta zeros."""
from pathlib import Path
import json
import sympy as s

x,t=s.symbols('x t',real=True)
count=0
def equal(a,b,label):
    global count
    if isinstance(a,s.MatrixBase):
        ok=(a-b).applyfunc(s.simplify)==s.zeros(*a.shape)
    else: ok=s.simplify(a-b)==0
    if not ok: raise ArithmeticError(label)
    count+=1
def moment(j):
    return s.integrate(x**j*(3+2*x+x*x),(x,-1,1))
Gfixed=s.Matrix([[4,1+s.I,0],[1-s.I,3,1],[0,1,2]])
cases=[[(0,1,2)],[(s.I,1,1),(-s.I,1,1)],[(0,3,2)],[(s.I,2,1),(-s.I,2,1)]]
all_minima=[]
for specs in cases:
    d=sum(m for z,m,delta in specs)
    nu=s.prod((x-z)**m for z,m,delta in specs).expand()
    grams=[]
    for n in range(d-1,d+3):
        H=s.Matrix(n+1,n+1,lambda i,j:moment(i+j))
        rows=[]
        for z,m,delta in specs:
            phi=z+delta*t+s.Rational(3,7)*t*t
            rows.extend([[s.expand(phi**k).coeff(t,j) for k in range(n+1)] for j in range(m)])
        E=s.Matrix(rows)
        En=E[:,:d]
        G=(E*H.inv()*E.H).inv()
        native_cols=[]
        for j in range(n-d+1):
            native_cols.append(s.Matrix([s.expand(x**j*nu).coeff(x,i) for i in range(n+1)]))
        Q=s.eye(n+1)[:,:d]
        if native_cols:
            R=s.Matrix.hstack(*native_cols)
            B=R.H*H*R
            S=Q.H*H*Q-Q.H*H*R*B.inv()*R.H*H*Q
            equal(H.det(),B.det()*S.det(),'full Schur determinant')
            equal(E*R,s.zeros(d,len(native_cols)),'all relation jets')
        else:
            B=s.eye(0);S=H
        equal(G,En.inv().H*S*En.inv(),'original jet Gram')
        equal(G.det(),H.det()/(B.det()*s.conjugate(En.det())*En.det()),'coordinate determinant')
        anchor=Gfixed if d==3 else s.eye(d)*3+s.ones(d)
        equal((G+anchor).det(),G.det()*(s.eye(d)+G.inv()*anchor).det(),'whole graph correction')
        if grams:
            diff=grams[-1]-G
            if not diff.is_positive_semidefinite:
                # Exact principal-minor criterion, including zero minors.
                import itertools
                for r in range(1,d+1):
                    for J in itertools.combinations(range(d),r):
                        if s.simplify(diff.extract(J,J).det())<0: raise ArithmeticError('monotone minimum')
            count+=1
        grams.append(G)
    all_minima.append(grams)

# Original-source versus quotient action: exact complex matrices, non-isometric S.
S=s.Matrix([[1,s.I,0],[0,2,1],[1,0,2],[s.I,1,0]])
H=s.Matrix([[1,s.I,0,0],[-s.I,2,1,0],[0,1,-2,2],[0,0,2,3]])
G=S.H*S
M=s.Matrix([[2+s.I,0,0],[0,1,1],[0,0,1]])
D=H*S-S*M
equal(S.H*D-D.H*S,M.H*G-G*M,'actual skew defect')
u=s.Matrix([1,0,0]); a=(S*u).H*D*u
equal(s.im(a[0]),-((S*u).H*S*u)[0],'nonreal eigenvector sign')
u0=s.Matrix([0,1,0]);u1=s.Matrix([0,0,1])
equal(((S*u0).H*D*u1-(D*u0).H*S*u1)[0],-((S*u0).H*S*u0)[0],'Jordan defect sign')

out={'status':'passed','exact_predicates':count,
     'scope':'Auxiliary polynomial measures and finite matrices; verifies coordinate factors, full Schur determinants, monotonicity and action-defect signs. No certification of actual zero locations, native asymptotics or RH.',
     'source_mass':str(moment(0)),
     'families':'Simple real, conjugate imaginary, triple jet with nontrivial coordinate substitution, and two double jets.'}
Path(__file__).with_name('WORD_GRAPH_VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
