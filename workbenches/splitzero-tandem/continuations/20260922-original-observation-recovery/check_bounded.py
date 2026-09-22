"""Exact finite checks for BD1--18; fixtures do not substitute native data."""
from pathlib import Path
import json,hashlib,time
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.domains import QQ

HERE=Path(__file__).resolve().parent
z,w,y,t=s.symbols("z w y t")
I=s.I
checks=[]
def eq(name,a,b=0):
    if isinstance(a,s.MatrixBase) or isinstance(b,s.MatrixBase):
        a=s.Matrix(a);b=s.zeros(*a.shape) if b==0 else s.Matrix(b)
        residual=(a-b).applyfunc(s.simplify)
        if residual!=s.zeros(*residual.shape): raise ArithmeticError((name,residual))
    else:
        residual=s.simplify(a-b)
        if residual!=0: raise ArithmeticError((name,residual))
    checks.append({"name":name,"kind":"exact","pass":True})
def yes(name,p):
    if not p: raise ArithmeticError(name)
    checks.append({"name":name,"kind":"exact","pass":True})
def rank(A):
    return len(DomainMatrix.from_Matrix(A).to_field().rref()[1])
def adjpoly(A):
    return A.conjugate().T.subs(s.conjugate(z),w)

started=time.time()
M=s.Matrix([[0,0,1,0,0],[1,0,0,0,1],[0,1,1,0,0],[0,0,0,0,1],[0,0,1,1,I]])
La=s.Matrix([[0,0,1,0,0],[0,0,0,0,1]])
u=s.Matrix([1,I,1,1,2]); cov=s.eye(5)+u*u.H
G=s.eye(5)-u*u.H/9
EK=s.eye(5)[:,[0,1,3]]; EB=s.eye(5)[:,[2,4]]
P=s.Matrix([[z**2,z,1,0,0],[0,0,0,z,1]])
D=s.Matrix([[1-z-z**3,-z**2],[-z,1-I*z-z**2]])
eq("fixture covariance inverse",G*cov,s.eye(5))
eq("polynomial kernel columns",P*(s.eye(5)-z*M)*EK)
eq("terminal inclusion",P*EB,s.eye(2))
eq("complete D including terminal action",P*(s.eye(5)-z*M)*EB,D)
eq("polynomial intertwining",P*(s.eye(5)-z*M),D*La)
eq("all determinant coefficients",D.det(),(s.eye(5)-z*M).det())
UU=(s.eye(5)-z*M)*EK
UU=UU.row_join(EB)
eq("unimodular determinant",UU.det(),-1)
eq("inverse bottom rows",UU.inv()[3:5,:],P)
C=s.expand(1)*P*cov*adjpoly(P)
expected=P*adjpoly(P)+s.Matrix([z*z+I*z+1,z+2])*s.Matrix([[w*w-I*w+1,w+2]])
eq("full covariance polynomial",C,expected)
Q=(La*cov*La.H).inv()
eq("observed metric",Q,s.Matrix([[s.Rational(5,6),-s.Rational(1,3)],[-s.Rational(1,3),s.Rational(1,3)]]))
H=EK.H*G*EK; V=EK.H*cov*EB; W=EB.H*cov*EB
RK=EK.H*cov*EK-V*W.inv()*V.H
eq("full hidden inverse Schur",RK,H.inv())
eq("actual hidden determinant",H.det(),s.Rational(2,3))
retain=[1,2]
eq("retained covariance determinant",RK.extract(retain,retain).det(),s.Rational(4,3))
eq("omitted metric determinant",H[0,0],s.Rational(8,9))
eq("complete determinant factor",H.det()*RK.extract(retain,retain).det(),H[0,0])
Cs={(i,j):C.applyfunc(lambda f:s.expand(f).coeff(z,i).coeff(w,j)) for i in range(3) for j in range(3)}
Pjs=[P.applyfunc(lambda f:s.expand(f).coeff(z,i)) for i in range(3)]
for i in range(3):
    for j in range(3):eq(f"coefficient Gram block {i},{j}",Cs[i,j],Pjs[i]*cov*Pjs[j].H)
selected=[(0,0),(0,1),(1,0),(1,1),(2,0)]
selectors=s.Matrix.vstack(*[Pjs[i][a,:] for i,a in selected])
yes("selectors contain each coordinate",selectors.det()!=0)
coefgram=s.Matrix(5,5,lambda a,b:Cs[selected[a][0],selected[b][0]][selected[a][1],selected[b][1]])
eq("all coefficients recover complete source covariance",selectors.inv()*coefgram*selectors.inv().H,cov)
L=cov*La.H*Q
MB=La*M*L
eq("full observed arithmetic matrix",MB,s.Matrix([[1+I/6,I/3],[s.Rational(7,6),s.Rational(1,3)+I]]))
D1=D.diff(z).subs(z,0)
eq("gauge correction gives original arithmetic",Cs[1,0]*Q-D1,MB)
b=s.Matrix([1,I])
phi=(I*b.H*(Q*MB-MB.H*Q)*b)[0]
wrong=(I*b.H*Q*(Cs[1,0]-Cs[0,1])*Q*b)[0]
eq("original current sign",phi,-s.Rational(7,18))
eq("current without connection term",wrong,s.Rational(5,18))
T0=Cs[1,1]-Cs[1,0]*Q*Cs[0,1]
eq("zero curvature",s.trace(Q*T0),s.Rational(49,36))
Md=G.inv()*M.H*G
r=s.Rational(1,13)
def energy(a):return (s.eye(5)-s.conjugate(a)*Md)*(s.eye(5)-a*M)
eq("four ordered energies recover M",(energy(-r)-energy(r))/(4*r)+(energy(-I*r)-energy(I*r))/(4*I*r),M)
Ep=L.H*G*energy(I*r)*L
Em=L.H*G*energy(-I*r)*L
eq("fixed-section paired energy current",(b.H*(Em-Ep)*b)[0]/(2*r),phi)
S={(i,j):La*(M**i)*cov*((M.H)**j)*La.H for i in range(3) for j in range(3)}
for i in range(3):
    for j in range(3):
        eq(f"local jet residual {i},{j}",S[i,j]-S[i,0]*Q*S[0,j],La*M**i*EK*H.inv()*EK.H*(M.H)**j*La.H)
obs=s.Matrix.vstack(*[La*M**i for i in range(3)])
eq("observable full stack rank",rank(obs),5)
for j,target in enumerate([3,1,0]):
    eq(f"fixture K_{j} dimension",5-rank(s.Matrix.vstack(*[La*M**i for i in range(j+1)])),target)
v=s.Matrix([1+I,2,-1,I,3])
vb=La*v; X=V*Q; av=EK.H*v-X*vb
Z=EK.H*M*EB+EK.H*M*EK*X-X*EB.H*M*EB-X*EB.H*M*EK*X
xx=EK*av; ww=L*vb
eq("first complex cross pairing",(xx.H*G*M*ww)[0],(av.H*H*Z*vb)[0])
eq("second complex cross pairing",(ww.H*G*M*xx)[0],(vb.H*Q*EB.H*M*EK*av)[0])
eq("physical i phases preserve cross product",s.conjugate((xx.H*G*I*M*ww)[0])*(ww.H*G*I*M*xx)[0],s.conjugate((xx.H*G*M*ww)[0])*(ww.H*G*M*xx)[0])
F=s.Matrix([[1,1,0,0,0],[0,1,I,0,0],[0,0,2,0,0],[0,0,0,1,1],[0,0,0,0,3]])
Mt=F*M*F.inv(); Lat=La*F.inv(); Gt=F.inv().H*G*F.inv()
eq("nonunitary coordinate covariance transport",Lat*Gt.inv()*Lat.H,La*cov*La.H)
eq("nonunitary current transport",Lat*Mt*Gt.inv()*Lat.H,S[1,0])
print("five-dimensional fixture complete",flush=True)

# Repeated irreducible factors, all derivative orders retained.
upper=[(a,b) for a in range(6) for b in range(6)]
lower=[(a,b) for a in range(4) for b in range(4)]
coeff={(a,b):s.binomial(2,a)*s.binomial(2,b) for a in range(3) for b in range(3)}
stack=s.zeros(0,36)
dims=[]
for h in range(5):
    Cmom=s.zeros(16,36)
    for row,(a,b) in enumerate(lower):
        for (u0,v0),aa in coeff.items():Cmom[row,upper.index((a+u0,b+v0))]=aa*(u0+I*v0)**h
    stack=stack.col_join(Cmom); dims.append(36-rank(stack))
eq("repeated factor filtration dimensions",s.Matrix(dims),s.Matrix([20,13,6,2,0]))
X0,Y0=s.symbols("X Y")
poly=(1+X0)**2*(1+Y0)**2
def dd(f):return s.expand(X0*s.diff(f,X0)+I*Y0*s.diff(f,Y0))
ders=[poly]
for _ in range(2):ders.append(dd(ders[-1]))
eq("first derivative retains repeated factors",s.degree(s.gcd(poly,ders[1]),X0),1)
eq("second derivative removes common repeated factors",s.gcd(s.gcd(poly,ders[1]),ders[2]),1)
print("repeated-factor fixture complete",flush=True)

# Original 9 by 9 shift support: exact interpolation identities over Q(i).
shifts=[6*v-24-I*(s.Rational(u,2)-2) for u in range(9) for v in range(9)]
yes("81 original-shaped shifts distinct",len(set(shifts))==81)
# All 81 powers over a stated exact prime field; the universal identity is BD6.
prime=10009
ii=next(j for j in range(2,prime) if j*j%prime==prime-1)
sm=[(12*v-48-ii*(u0-4))%prime for u0 in range(9) for v in range(9)]
yes("prime-field original support has distinct nodes",len(set(sm))==81)
weights=[]
for jj,sh in enumerate(sm):
    den=1
    for kk,other in enumerate(sm):
        if jj!=kk:den=den*(sh-other)%prime
    weights.append(pow(den,-1,prime))
for h in range(81):
    eq(f"prime-field sharp support barycentric moment {h}",sum(aa*pow(sh,h,prime) for aa,sh in zip(weights,sm))%prime,1 if h==80 else 0)
for kk in [17,21]:
    covered=set()
    for uu,vv in [(0,0),(0,8),(8,0),(8,8)]:
        covered.update((a+uu,b+vv) for a in range(kk-7) for b in range(kk-7))
    eq(f"four corners cover original k={kk}",len(covered),(kk+1)**2)
print("original-shaped support complete",flush=True)

# Literal polynomial source and the entire relation kernel.
Qpoly=y**3-2*y-1
JN=s.Matrix(3,6,lambda i,j:s.Poly(s.rem(y**j,Qpoly,y),y).nth(i))
hs=s.diag(1,2,3,4,5,6)+s.ones(6,6)
GG=(JN*hs.inv()*JN.H).inv()
ll=hs.inv()*JN.H*GG
eq("literal residue source minimum section",JN*ll,s.eye(3))
relation=s.Matrix([-1,-2,0,1,0,0])
eq("whole ideal relation killed by residue map",JN*relation,s.zeros(3,1))
P3=s.Matrix([[z*z,z,1]])
eq("whole ideal relation killed by polynomial receiver",P3*JN*relation,s.zeros(1,1))
eq("physical source polynomial covariance",P3*GG.inv()*adjpoly(P3),(P3*JN)*hs.inv()*adjpoly(P3*JN))
eq("attained source metric",ll.H*hs*ll,GG)
eq("source minimum orthogonality",relation.H*hs*ll,s.zeros(1,3))

# Every pole and a nontrivial Jordan elementary divisor.
Ad=s.diag(1,2,3); lad=s.Matrix([[1,1,1]])
xd=s.Matrix([1,-2,1]); Fd=s.Matrix.hstack(xd,Ad*xd,Ad**2*xd)
Rd=(lad*Fd)[0,2]; Pd=s.Matrix([[z*z,z,1]])
Ah=Fd.inv()*Ad*Fd
Dd=(Pd*(s.eye(3)-z*Ah)*s.Matrix([0,0,1]))[0]
eq("simple-spectrum reduced denominator",Dd,(1-z)*(1-2*z)*(1-3*z))
Cd=(Pd*Fd.inv()*Fd.inv().H*adjpoly(Pd))[0]
for lam in [1,2,3]:
    zz=s.Rational(1,lam)
    residue=s.simplify(Rd**2*Cd.subs({z:zz,w:zz})/s.diff(Dd,z).subs(z,zz)**2)
    eq(f"noncancelled residue lambda={lam}",residue,s.Rational(1,lam**2))
Aj=s.Matrix([[2,1,0],[0,2,1],[0,0,2]]); lj=s.Matrix([[1,0,0]])
xj=s.Matrix([0,0,1]); Fj=s.Matrix.hstack(xj,Aj*xj,Aj**2*xj)
Dj=(Pd*(s.eye(3)-z*Fj.inv()*Aj*Fj)*s.Matrix([0,0,1]))[0]
eq("Jordan algebraic multiplicity retained",Dj,(1-2*z)**3)
eq("Jordan denominator zero order",s.diff(Dj,z,2).subs(z,s.Rational(1,2)),0)
yes("Jordan leading derivative nonzero",s.diff(Dj,z,3)!=0)

# Degree-Hilbert function and the polynomial annihilator equations.
for h in range(6):
    symbols=s.symbols(f"t0:{5*(h+1)}")
    row=s.Matrix([[sum(symbols[a*(h+1)+j]*z**j for j in range(h+1)) for a in range(5)]])
    expr=row*(s.eye(5)-z*M)*EK
    equations=[s.expand(v).coeff(z,j) for v in expr for j in range(h+2)]
    matrix=s.linear_eq_to_matrix(equations,symbols)[0]
    eq(f"intrinsic Hilbert function h={h}",len(symbols)-rank(matrix),max(h-2+1,0)+max(h-1+1,0))

# Exact interpolation at rational nodes; Fourier nonaliasing checked as integers.
d=2; ell=2*d+1
for h in range(d+1):
    for a in range(d+1):
        for b0 in range(d+1):
            eq(f"Fourier alias exclusion {h},{a},{b0}",int((a-b0-h)%ell==0),int(a-b0==h))
    nodes=[s.Rational(j+1,d+2) for j in range(d-h+1)]
    for degree in range(d-h+1):
        interp=s.interpolate([(tt,tt**degree) for tt in nodes],t)
        eq(f"radial inverse h={h},degree={degree}",interp,t**degree)

# Remainder coefficients and complete homogeneous quotient, including degree 2q.
roots=[1+I,1-I,-1+I,-1-I]; qp=s.prod(y-r for r in roots)
hh=[s.Integer(1)]
for j in range(1,5):
    hh.append(s.expand(s.prod((1-r*t)**-1 for r in roots)).series(t,0,5).removeO().coeff(t,j))
for degree in range(4,9):
    quotient,remainder=s.div(y**degree,qp,y)
    expectedq=sum(hh[j]*y**(degree-4-j) for j in range(degree-4+1))
    eq(f"literal homogeneous quotient degree={degree}",quotient,expectedq)
    eq(f"literal remainder fibre degree={degree}",y**degree-qp*quotient,remainder)
for j in range(9):
    pp=s.legendre(j,2*y-3)
    yes(f"Legendre coefficient estimate degree={j}",sum(abs(c) for c in s.Poly(pp,y).all_coeffs())<=11**j)
    eq(f"shifted Legendre exact norm degree={j}",s.integrate(pp**2,(y,1,2)),s.Rational(1,2*j+1))

# Scalar information minimum attained by selecting real sample rows.
basis=[]
for i in range(5):
    for j in range(i,5):
        if i in [2,4] and j in [2,4]:continue
        B=s.zeros(5);B[i,j]=1;B[j,i]=1;basis.append(B)
        if i!=j:
            B=s.zeros(5);B[i,j]=I;B[j,i]=-I;basis.append(B)
eq("unknown real Hermitian dimension",len(basis),21)
rows=[]
for aa,bb in [(a,b0) for a in range(5) for b0 in range(5)]:
    zz=s.Rational(aa,7)+I*s.Rational(bb,7)
    PP=P.subs(z,zz)
    sampled=[PP*B*PP.H for B in basis]
    rows.extend([[s.re(V[0,0]) for V in sampled],[s.re(V[1,1]) for V in sampled],
                 [s.re(V[0,1]) for V in sampled],[s.im(V[0,1]) for V in sampled]])
measurement=s.Matrix(rows)
eq("scalar measurements attain information minimum",rank(measurement),21)
piv=DomainMatrix.from_Matrix(measurement.T).to_field().rref()[1]
selected_measurement=measurement[list(piv),:]
yes("selected minimum-size scalar inverse exists",selected_measurement.det()!=0)
print("all checks passed",len(checks),flush=True)
proof=HERE/"BOUNDED_DEGREE_PROOFS.md"
result={"status":"PASS","exact_checks":len(checks),"elapsed_seconds":time.time()-started,
        "checks":checks,"proof_sha256":hashlib.sha256(proof.read_bytes()).hexdigest(),
        "scope":"Exact auxiliary fixtures and identities; no native period coefficient, xi moment, EIQ value, or current sign has been assigned.",
        "sympy_version":s.__version__}
(HERE/"BOUNDED_CHECKS.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
