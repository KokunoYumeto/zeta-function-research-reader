"""Exact finite-period phase identities and uniform real-boundary obstructions."""
from pathlib import Path
import hashlib
import json
import sympy as s

HERE = Path(__file__).resolve().parent
beta,eta,q,k=s.symbols('beta eta q k')
phi=1+q+q**2+q**3+q**4
field=s.QQ.frac_field(beta,eta,k)
checks=[]

def red(x):
    n,d=s.fraction(s.cancel(x))
    n=s.rem(n,k**2-(eta-beta**2/4),k)
    d=s.rem(d,k**2-(eta-beta**2/4),k)
    ph=s.Poly(phi,q,domain=field)
    n=s.Poly(n,q,domain=field)
    d=s.Poly(d,q,domain=field)
    return (n.rem(ph)*s.invert(d,ph)).rem(ph).as_expr()

def mat(M):
    return M.applyfunc(red)

def check(name,x,cyclotomic=True):
    entries=list(x) if isinstance(x,s.MatrixBase) else [x]
    for entry in entries:
        result=red(entry) if cyclotomic else s.simplify(s.expand(entry))
        assert result==0,(name,result)
    checks.append({'name':name,'entries':len(entries)})

def Rn(n):
    out=s.zeros(4)
    for a in range(1,5):
        for r in range(4):
            total=5*n+r+1-a
            for h in range(max(-1,total//4)+1):
                if (total-4*h)%2:
                    continue
                p=(total-4*h)//2
                L=p+h-n
                assert L>=0
                out[a-1,r]+=beta**p*eta**h/(3**p*s.factorial(p)*s.factorial(h))*(-1)**L*5**L*s.rf(s.Rational(a,5),L)
    return out

T=s.Matrix([[0,0,0,-eta],[1,0,0,0],[0,1,0,-beta],[0,0,1,0]])
K=(T**2+beta*s.eye(4)/2)/k
Q=s.Matrix([[0,0,1,0],[0,-1,0,beta],[1,0,-beta,0],[0,beta,0,eta-beta**2]])
e0=s.eye(4)[:,0]
check('original unit complex structure',K*K+s.eye(4))
check('original unit quadratic transform',K.T*Q*K+Q)
alpha,chi=s.symbols('alpha chi')
check('full original unit inverse',(alpha*s.eye(4)-chi*K)*(alpha*s.eye(4)+chi*K)-(alpha**2+chi**2)*s.eye(4))

R=[Rn(n) for n in range(5)]
Ri=[R[0].inv()]
for n in range(1,5):
    Ri.append(s.expand(-Ri[0]*sum((R[a]*Ri[n-a] for a in range(1,n+1)),s.zeros(4))))
D=s.diag(q,q**2,q**3,q**4)
G=[mat(sum((Ri[a]*D*R[n-a] for a in range(n+1)),s.zeros(4))) for n in range(5)]

def jet_vectors(W,Wbar):
    return [[mat(Wbar*gn*W*e0),mat(gn*W*e0+Wbar*gn*e0),mat(gn*e0)] for gn in G]

def coefficient(vectors,r,n):
    return red(sum((vectors[a][i].dot(Q*vectors[n-a][r-i])
                    for a in range(n+1)
                    for i in range(max(0,r-2),min(2,r)+1)),s.S.Zero))

# The actual first phase chart a=alpha(1+i x), x=chi/alpha.
p=[[mat(gn*e0),mat(gn*K*e0-K*gn*e0),mat(-K*gn*K*e0)] for gn in G]
c10=coefficient(p,1,0)
check('first phase simple derivative',c10-2*(q**4-q**2)/k)
first2=red(-coefficient(p,0,2)/c10)
check('first phase exact z2 coefficient',first2-k*beta**2*(beta**2-9*eta)*q**2*(q**2+3*q+1)/(162*(q+1)))
first4=red(-(coefficient(p,0,4)+coefficient(p,1,2)*first2+coefficient(p,2,0)*first2**2)/c10)
check('first phase z2 coefficient real',first2-first2.subs(q,q**4))
U=82*beta**4-2856*beta**2*eta+15120*eta**2
V=89*beta**4-168*beta**2*eta
first_obstruction=beta**3*k*(beta**2-9*eta)*(U*(q**3-q**2)+V*(1+2*q+q**2+q**3))/1102248
check('first phase exact z4 obstruction',first4-first4.subs(q,q**4)-first_obstruction)

# The actual second chart a=chi(-c+e+i), e=alpha/chi+c.
c=beta/(6*k)
W=-c*s.eye(4)+K
Wbar=-c*s.eye(4)-K
psecond=jet_vectors(W,Wbar)
csecond=coefficient(psecond,1,0)
check('second phase simple derivative',csecond-2*(1+c**2)*q**3*(q**3-q)/k)
second2=red(-coefficient(psecond,0,2)/csecond)
second_obstruction=beta**4*k*(beta**2-9*eta)*(4*beta**2-27*eta)*(11*q**3-3*q**2+8*q+4)/(6561*(beta**2-4*eta)*(2*beta**2-9*eta))
check('second phase exact z2 obstruction',second2-second2.subs(q,q**4)-second_obstruction)

# Exact real-imaginary extraction for the two conjugate factor pairs.
A=s.symbols('A0:4',real=True)
h=(s.sqrt(5)-1)/2
sin72=s.sqrt(10+2*s.sqrt(5))/4
zeta=(s.sqrt(5)-1)/4+s.I*sin72
N=sum(A[i]*q**i for i in range(4))
P1=4*A[0]+(s.sqrt(5)-1)*A[1]-(s.sqrt(5)+1)*(A[2]+A[3])
J1=2*A[1]+(s.sqrt(5)-1)*(A[2]-A[3])
P2=4*A[0]-(s.sqrt(5)+1)*A[1]+(s.sqrt(5)-1)*(A[2]+A[3])
J2=(s.sqrt(5)-1)*A[1]-2*A[2]+2*A[3]
check('first pair real-imaginary extraction',N.subs(q,zeta)-P1/4-s.I*sin72*J1/2,False)
check('second pair real-imaginary extraction',N.subs(q,zeta**2)-P2/4-s.I*sin72*J2/2,False)

# The complete degree-four Bezout matrix, with symbolic coefficients.
X,Y=s.symbols('X Y')
pp=s.symbols('p0:5');qq=s.symbols('r0:5')
cp=lambda i,j:pp[i]*qq[j]-pp[j]*qq[i]
Bez=s.Matrix([[cp(1,0),cp(2,0),cp(3,0),cp(4,0)],
              [cp(2,0),cp(3,0)+cp(2,1),cp(4,0)+cp(3,1),cp(4,1)],
              [cp(3,0),cp(4,0)+cp(3,1),cp(4,1)+cp(3,2),cp(4,2)],
              [cp(4,0),cp(4,1),cp(4,2),cp(4,3)]])
pv=sum(pp[i]*X**i for i in range(5));qv=sum(qq[i]*X**i for i in range(5))
form=(s.Matrix([[1,X,X**2,X**3]])*Bez*s.Matrix([1,Y,Y**2,Y**3]))[0]
check('complete quartic Bezout identity',(X-Y)*form-(pv*qv.subs(X,Y)-pv.subs(X,Y)*qv),False)

# Original z4 coefficient nonvanishing, by exact Bernstein coefficients.
t,H=s.symbols('t H',real=True)
F1=(169+48*H)*t**3+(-2583-378*H)*t**2+(11340-2835*H)*t+25515*H
F2=(48-169*H)*t**3+(-378+2583*H)*t**2+(-2835-11340*H)*t+25515
bern1=[25515*H,15120+21735*H,16464+15939*H,14848+11199*H]
bern2=[25515,21735-15120*H,15939-16464*H,11199-14848*H]
for n,(f,b) in enumerate([(F1,bern1),(F2,bern2)],1):
    check(f'original z4 Bernstein polynomial {n}',f-sum(b[j]*s.binomial(3,j)*(t/4)**j*(1-t/4)**(3-j) for j in range(4)),False)
d4=coefficient(p,0,4)
for jj,(power,sgn,ff) in enumerate([(4,-1,F1),(3,1,F2)],1):
    num=red(sgn*s.Integer(1653372)*d4.subs(q,q**power)/(beta*(beta**2-9*eta)))
    co=s.Poly(num,q)
    imag=co.nth(1)+h*(co.nth(2)-co.nth(3))
    check(f'actual original z4 imaginary coefficient {jj}',imag-eta**3*ff.subs({t:beta**2/eta,H:h}),False)

proof=HERE/'FINITE_PERIOD_UNIT_TEST.tex'
receipt={'status':'pass','groups':len(checks),'scalar_entries':sum(x['entries'] for x in checks),
         'checks':checks,'first_phase_z2':str(s.factor(first2)),
         'first_phase_z4_difference':str(first_obstruction),
         'second_phase_z2':str(s.factor(second2)),
         'second_phase_z2_difference':str(second_obstruction),
         'real_unit_z4_coefficient':str(s.factor(d4)),
         'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest() if proof.exists() else None,
         'scope':'Full original real-period unit-phase algebra and exact coefficient-boundary exclusion; no finite-period zero is asserted.'}
(HERE/'FINITE_PERIOD_UNIT_TEST_CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'pass','groups':receipt['groups'],'scalar_entries':receipt['scalar_entries']}),flush=True)
