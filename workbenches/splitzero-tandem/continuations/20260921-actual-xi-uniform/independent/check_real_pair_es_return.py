"""Exact four-label order-two return and the full original correction."""
from pathlib import Path
import hashlib,json
import sympy as s
HERE=Path(__file__).resolve().parent
S=s.symbols('S');mu2,mu3,mu4,mu5=s.symbols('mu2 mu3 mu4 mu5',nonzero=True)
mom=[0,0,mu2,mu3,mu4,mu5]
roots=[s.Rational(3,4)+3*s.I,s.Rational(3,4)-3*s.I,s.Rational(1,4)+3*s.I,s.Rational(1,4)-3*s.I]
checks=[]
def check(name,expr):
    entries=list(expr) if isinstance(expr,s.MatrixBase) else [expr]
    for e in entries:assert s.cancel(s.expand(e))==0,(name,e)
    checks.append({'name':name,'entries':len(entries)})
V=s.Matrix([[r**n for n in range(4)] for r in roots]);L=V.inv()
lambda3=[(-24-2*s.I)/435,(-24+2*s.I)/435,(24-2*s.I)/435,(24+2*s.I)/435]
expected=s.Matrix([[lambda3[j]*(r**3-2*r*r+s.Rational(155,8)*r-s.Rational(147,8)) for j,r in enumerate(roots)],
                   [lambda3[j]*(r*r-2*r+s.Rational(155,8)) for j,r in enumerate(roots)],
                   [lambda3[j]*(r-2) for j,r in enumerate(roots)],lambda3])
check('every labelled Lagrange coefficient',L-expected)
check('original root determinant',V.det()+s.Rational(1305,4))
check('old constant kernel label vector',L*s.ones(4,1)-s.eye(4)[:,0])
check('old linear kernel label vector',L*s.Matrix(roots)-s.eye(4)[:,1])
B0=s.Matrix([[0,0,mu2,mu3],[0,0,0,3*mu2],[0,0,0,0],[0,0,0,0]])
B2=s.Matrix([[mu2,mu3,mu4,mu5],[0,3*mu2,4*mu3,5*mu4],[0,0,6*mu2,10*mu3],[0,0,0,10*mu2]])
B1=s.Matrix([[0,mu2,mu3,mu4],[0,0,2*mu2,3*mu3],[0,0,0,3*mu2],[0,0,0,0]])
Bder2=s.Matrix([[mu2,mu3,mu4,mu5],[0,mu2,2*mu3,3*mu4],[0,0,mu2,3*mu3],[0,0,0,mu2]])
mult=s.Matrix(4,4,lambda i,j:1 if i==j+1 else 0)
check('complete second-multiplication correction',B2-mult**2*B0-2*mult*B1-Bder2)
for n in range(4):
    expectedpoly=sum(s.binomial(n+2,k)*mom[n+2-k]*S**k for k in range(n+1))
    check(f'actual source monomial degree {n+2}',(s.Matrix([[1,S,S*S,S**3]])*B2[:,n])[0]-expectedpoly)
check('complete four-label determinant',(B2*L).det()+s.Rational(16,29)*mu2**4)
assert B0.rank()==2
checks.append({'name':'old rank exactly two','entries':1})
b,M=s.symbols('b M',positive=True)
h=lambda n:M*s.factorial(n)*s.rf(b,n)
rho2=lambda n:s.factorial(n)/s.rf(b,n)
ratio=mu2**8*180**2*s.prod(h(n) for n in range(4))/s.prod(h(n) for n in range(2,6))
expectedratio=(mu2/2)**8*s.prod(rho2(n+2)/rho2(n) for n in range(4))
check('full original Gamma Gram determinant ratio',ratio-expectedratio)
K=s.Matrix([[0,s.I,1/s.sqrt(2),1/s.sqrt(2)],[0,-1,-1-s.sqrt(2)*s.I,1-s.sqrt(2)*s.I],
            [s.I/2,-3*s.I,2*s.sqrt(2)+6*s.I,-2*s.sqrt(2)+6*s.I],
            [0,13,-34-19*s.sqrt(2)*s.I,34-19*s.sqrt(2)*s.I]])
check('unchanged four-label ES determinant',K.det()-77*s.sqrt(2)*s.I/2)
pairs=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
differences=[-4*s.I,-48,-48-4*s.I,-48+4*s.I,-48,-4*s.I]
check('six distinct original old output slopes',s.Matrix([lambda3[a]-lambda3[b]-differences[j]/435 for j,(a,b) in enumerate(pairs)]))
augment=s.Matrix([[0,0,mu2,mu3],[0,0,0,3*mu2],[1,0,0,0],[0,1,0,0]])
augment_inverse=s.Matrix([[0,0,1,0],[0,0,0,1],[1/mu2,-mu3/(3*mu2**2),0,0],[0,1/(3*mu2),0,0]])
check('entire two-scalar inverse in original coefficients',augment*augment_inverse-s.eye(4))
check('two-scalar augmented determinant',augment.det()-3*mu2**2)
c,y=s.symbols('c y',real=True)
m4=b*(3*b+2);m6=b*(15*b*b+30*b+16)
moments={0:1,1:0,2:b,3:0,4:m4,5:0,6:m6}
def integrate(poly):
    return s.expand(sum(coeff*moments[mon[0]] for mon,coeff in s.Poly(s.expand(poly),y).terms()))
Q=s.Matrix([[1,c],[c,c*c+b]])
U=s.Matrix([[c*c-b,c**3-3*c*b],[c**3+c*b,c**4-m4]])
H=s.Matrix([[c**4+2*c*c*b+m4,c*(c**4+2*c*c*b+m4)],
            [c*(c**4+2*c*c*b+m4),c**6+3*c**4*b+3*c*c*m4+m6]])
direct=s.Matrix(4,4,lambda i,j:integrate((c-s.I*y)**i*(c+s.I*y)**j))
check('all original Gamma moment and cross-term Gram entries',direct-Q.row_join(U).col_join(U.T.row_join(H)))
check('fourth Gamma moment from original recurrence',integrate((y*y-b)**2)-2*b*(b+1))
check('sixth Gamma moment from original recurrence',integrate((y**3-(3*b+2)*y)**2)-6*b*(b+1)*(b+2))
Qinverse=s.Matrix([[c*c+b,-c],[-c,1]])/b
check('exact original lost-coordinate Gram inverse',Q*Qinverse-s.eye(2))
expected_projection=s.Matrix([[-c*c-b,-2*c**3+2*c],[2*c,3*c*c-3*b-2]])
check('both original lost-coordinate metric cross corrections',Qinverse*U-expected_projection)
schur=s.Matrix([[2*b*(b+1),6*c*b*(b+1)],[6*c*b*(b+1),18*c*c*b*(b+1)+6*b*(b+1)*(b+2)]])
check('complete two-scalar quotient Gram',H-U.T*Qinverse*U-schur)
DY=s.Matrix([[1/mu2,-mu3/(3*mu2**2)],[0,1/(3*mu2)]])
metric_augmented=DY.T*H*DY
metric_augmented=metric_augmented.row_join(DY.T*U.T).col_join((U*DY).row_join(Q))
source_gram=Q.row_join(U).col_join(U.T.row_join(H))
check('all transported original augmented Gram entries',augment_inverse.T*source_gram*augment_inverse-metric_augmented)
out={'status':'pass','groups':len(checks),'scalar_entries':sum(c['entries'] for c in checks),'checks':checks,
     'proof_sha256':hashlib.sha256((HERE/'REAL_PAIR_ES_RETURN.tex').read_bytes()).hexdigest(),
     'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'scope':'Exact original four-label return, all six old-label differences, complete moment correction, two-scalar recovery and full original Gamma metric with every cross term; the selected real period is established by the separate full-series contraction certificate.'}
(HERE/'REAL_PAIR_ES_RETURN_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'pass','groups':out['groups'],'scalar_entries':out['scalar_entries']}),flush=True)
