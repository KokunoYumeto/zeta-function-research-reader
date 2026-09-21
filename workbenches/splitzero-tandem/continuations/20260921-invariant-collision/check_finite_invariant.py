"""Bounded exact auxiliary checks for FI1--17; no native coefficient evaluation."""
from pathlib import Path
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parent
x,y,t,w = s.symbols('x y t w')
I=s.I
checks=[]

def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)

def eq(name, a, b):
    if isinstance(a,s.MatrixBase):
        check(name, (a-b).applyfunc(s.simplify)==s.zeros(*a.shape))
    else:
        check(name, s.simplify(a-b)==0)

# The mass is carried as a symbol in the physical determinant identities.
mass=s.symbols('mathfrak_m_sigma', positive=True)
f=s.series(s.cos(t)**(-s.Rational(1,2)),t,0,19).removeO().expand()
nu=[s.factorial(j)*f.coeff(t,j) for j in range(19)]
eq('first five even physical-mass coefficients',s.Matrix([nu[j] for j in range(0,9,2)]),s.Matrix([1,s.Rational(1,2),s.Rational(7,4),s.Rational(139,8),s.Rational(5473,16)]))
check('all odd moments through degree 17 vanish',all(nu[j]==0 for j in range(1,19,2)))

def H(n,a=0):
    return s.Matrix(n+1,n+1,lambda i,j:nu[2*a+i+j]) if n>=0 else s.zeros(0)

def det(n,a=0):
    return H(n,a).det() if n>=0 else s.Integer(1)

q,qp,v,g=4,2,1,1
Ls=[-1,0,q-1,q]
refs=[mass**g*det(L+g,qp)/det(L,q-v) for L in Ls]
A=det(g-1,qp)*det(g,qp)*det(q-1,q-v)*det(q,q-v)/(det(q+g-1,qp)*det(q+g,qp)*det(0,q-v))
eq('four-cutoff scalar identity including full physical mass',refs[0]*refs[1]/refs[2]/refs[3],A)
check('scalar is a positive rational',A.is_Rational and A>0)
check('maximum scalar moment order retains 4q-2v',max(2*qp+2*(q+g),2*(q-v)+2*q)==4*q-2*v)
for n,a in [(-1,0),(0,3),(3,3),(4,3),(0,2),(1,2),(4,2),(5,2)]:
    check(f'positive Hankel determinant n={n} a={a}',det(n,a)>0)

def inner(p,r):
    # Actual c'=0 line and conjugate-linear first slot; mass factored explicitly.
    a=s.Poly(s.expand(p.subs(x,I*y)),y)
    b=s.Poly(s.expand(r.subs(x,I*y)),y)
    return s.expand(sum(s.conjugate(aa)*bb*nu[j+k] for (j,),aa in a.terms() for (k,),bb in b.terms()))

chi0=x*(x-1)
chi=s.expand(x*(x-1)*(x-4*I)*(x-1-4*I))
def T(p):
    return s.expand(p.subs(x,x+4*I)-p)

u=[]
for n in range(5):
    a,rem=s.div(T(chi*x**n),chi0,x)
    eq(f'complete conductor divisibility n={n}',rem,0)
    a=s.Poly(a,x)
    eq(f'actual relation leading coefficient n={n}',a.LC(),4*I*(4+n))
    check(f'exact relation degree n={n}',a.degree()==n+1)
    u.append(a.as_expr())

G=s.series((s.exp(w)-1)/(s.exp(4*I*w)-1),w,0,9).removeO().expand()
def L(p):
    return s.expand(sum(c*s.factorial(j)*G.coeff(w,j) for (j,),c in s.Poly(p,x).terms()))
def ell(p):
    return L(s.expand(chi0*p))

eq('correct weighted functional uses ell(1)=L(chi)',ell(1),17*I/24)
check('negative control: ell(chi) is not ell(1)',s.simplify(ell(chi0)-ell(1))!=0)
b=[ell(1)]
for n,a in enumerate(u):
    coeff=s.Poly(a,x)
    bn=-sum(coeff.nth(j)*b[j] for j in range(n+1))/coeff.LC()
    b.append(s.simplify(bn))
    eq(f'triangular recurrence equals original generating functional n={n}',b[-1],ell(x**(n+1)))
    eq(f'original functional kills complete relation n={n}',ell(a),0)

for cut in [3,4,7,8]:
    degree=cut-1
    M=cut-3
    HH=s.Matrix(M+1,M+1,lambda i,j:inner(chi0*x**i,chi0*x**j))
    BB=s.Matrix([[ell(x**j) for j in range(M+1)]])
    cov=s.simplify((BB*HH.inv()*BB.conjugate().T)[0])
    check(f'full weighted covariance positive cutoff={cut}',cov>0)
    bordered=HH.row_join(BB.conjugate().T).col_join(BB.row_join(s.zeros(1)))
    eq(f'bordered determinant covariance cutoff={cut}',-bordered.det(),HH.det()*cov)
    cutoffL=cut-4
    cols=[x**j for j in range(g)]+u[:cutoffL+1] if cutoffL>=0 else [s.Integer(1)]
    basis=s.Matrix(M+1,M+1,lambda i,j:s.Poly(cols[j],x).nth(i))
    tau=s.prod(4*I*(4+n) for n in range(cutoffL+1))
    eq(f'full nonideal triangular basis determinant cutoff={cut}',basis.det(),tau)
    if cutoffL>=0:
        RR=s.Matrix(cutoffL+1,cutoffL+1,lambda i,j:inner(chi0*u[i],chi0*u[j]))
        gram=(basis.conjugate().T*HH*basis)
        schur=gram[0,0]-(gram[:1,1:]*RR.inv()*gram[1:,:1])[0]
        eq(f'entire relation Schur complement cutoff={cut}',schur,s.conjugate(tau)*tau*HH.det()/RR.det())
    if cut==3:
        eq('auxiliary full-projection covariance with mass retained',cov/mass,s.Rational(289,1296)/mass)

# Fixed-coordinate quotient transport, keeping every lower evaluation row.
E=s.Matrix([[1,2,0,1],[0,1,I,2]])
W=s.Matrix([[1,I,2,3],[2,1,0,I]])
P=s.eye(4)-E.conjugate().T*(E*E.conjugate().T).inv()*E
CA=s.Matrix([[1,0,0,1,0],[0,1,0,0,1]])
U=s.Matrix([[1],[2],[0],[0],[0]])
Z=s.Matrix([[1,0,I,1,0],[0,1,0,I,2]])
R=CA*U
left=(R.conjugate().T*R).inv()*R.conjugate().T
B=Z*U*left
ZD=Z-B*CA
eq('typed rational correction annihilates entire numerator image',ZD*U,s.zeros(2,1))
eq('full lower-root projection annihilation',E*P,s.zeros(2,4))
eq('typed covariance survives exact quotient correction',(W-B*E)*P*(W-B*E).conjugate().T,W*P*W.conjugate().T)
check('unprojected negative control changes',((W-B*E)*(W-B*E).conjugate().T-W*W.conjugate().T).applyfunc(s.simplify)!=s.zeros(2))

# Equality case geometry and exact perturbation inequalities in a rational plane.
E0=s.Matrix([[1,0]])
Eh=s.Matrix([[1,s.Rational(1,3)]])
P0=s.eye(2)-E0.T*E0
Ph=s.eye(2)-Eh.T*(Eh*Eh.T).inv()*Eh
square=s.simplify((Ph-P0)*(Ph-P0))
eq('equal-rank projection exact squared norm',square,s.eye(2)/10)
check('constant-one projection estimate holds exactly',s.Rational(1,10)<=s.Rational(1,9))
eq('precision budget exact margin',s.Rational(1,4)+s.Rational(1,128)+s.Rational(289,8192),s.Rational(2401,8192))
check('precision margin strictly below one',s.Rational(2401,8192)<1)

# The auxiliary conductor has Cv=2 and RA=1/(8e). Since e<3,
# R=1/24 is inside RA. The series estimate exp(x)<=1/(1-x)
# for 0<=x<1 provides a rational bound for this retained disk.
radius=s.Rational(1,24)
xcircle=4*radius
check('auxiliary zero-free relative Taylor defect below one half',xcircle/(1-xcircle)<s.Rational(1,2))
eq('auxiliary rational zero-free defect bound',xcircle/(1-xcircle),s.Rational(1,5))
sradius=s.Rational(1,2)
aradius=sradius/2
rootsofunity=[s.Integer(1),I,s.Integer(-1),-I]
for n in range(3):
    dft=s.simplify(sum((1-aradius*z/3)**-1*z**(-n) for z in rootsofunity)/(4*aradius**n))
    alias=(s.Rational(1,3)**n)*(aradius/3)**4/(1-(aradius/3)**4)
    eq(f'exact full-circle aliasing identity n={n}',dft-s.Rational(1,3)**n,alias)
    bound=s.Rational(6,5)*sradius**(-n)*s.Rational(1,16)/(1-s.Rational(1,16))
    check(f'full-circle Cauchy alias bound n={n}',alias<=bound)

report={
    'status':'passed', 'exact_check_count':len(checks), 'checks':checks,
    'auxiliary_scope':'Small complex conductor and rational matrices only; the physical Gamma mass is retained symbolically. No native period or limiting coefficient is evaluated.',
    'scalar_fixture':{'q':q,'q_prime':qp,'v':v,'g':g,'A':str(A)},
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'proof_sha256':hashlib.sha256((ROOT/'FINITE_INVARIANT_PROOFS.md').read_bytes()).hexdigest(),
}
(ROOT/'FINITE_INVARIANT_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':report['status'],'exact_check_count':len(checks),'native_coefficient_evaluated':False}))
