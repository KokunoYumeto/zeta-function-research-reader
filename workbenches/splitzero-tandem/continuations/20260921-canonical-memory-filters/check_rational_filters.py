"""Exact checks for RF1--67. Fixtures do not certify native arithmetic moments."""
from pathlib import Path
import hashlib
import itertools
import json
import sympy as s

y, w, z = s.symbols("y w z")
checks = []

def check(condition, label):
    if condition is not True and condition != s.true:
        raise AssertionError(label)
    checks.append(label)

def zero(expr, label):
    if isinstance(expr, s.MatrixBase):
        check(all(s.cancel(x) == 0 for x in expr), label)
    else:
        check(s.cancel(expr) == 0, label)

def coeff(poly, n):
    poly = s.Poly(poly, y)
    return s.Matrix([poly.nth(j) for j in range(n)])

def mod(poly, relation):
    return s.rem(poly, relation, y)

def matrix_map(fn, domain, target):
    return s.Matrix.hstack(*(coeff(fn(y**j), target) for j in range(domain)))

def matrix_poly(poly, matrix):
    result = s.zeros(matrix.rows)
    for c in s.Poly(poly, y).all_coeffs():
        result = result * matrix + c*s.eye(matrix.rows)
    return result

def psd(matrix, label):
    zero(matrix-matrix.conjugate().T, label + ": Hermitian")
    for n in range(1, matrix.rows+1):
        for idx in itertools.combinations(range(matrix.rows), n):
            v = s.factor(matrix.extract(idx, idx).det())
            check(v >= 0, label + ": principal minor " + str(idx))

# Full multiplicity remainders obtained by contour residues.
for roots in [(13,13,7), (13,7,7), (13,13,13)]:
    p = s.prod(y-r for r in roots)
    f = 1/(w*w+1)
    ppw = p.subs(y,w)
    divided = s.cancel((ppw-p)/(w-y))
    rem_contour = s.expand(sum(s.residue(f*divided/ppw, w, r)
                               for r in set(roots)))
    expected = s.invert(y*y+1,p,y)
    zero(rem_contour-expected, "Hermite contour remainder " + str(roots))
    for r in set(roots):
        for j in range(roots.count(r)):
            zero(s.diff(expected-1/(y*y+1),y,j).subs(y,r),
                 "All pole derivatives " + str((roots,r,j)))
    # Complete quotient division by repeated factors in the actual order.
    poly = y**8+2*y**5-3*y+7
    quotient = poly
    for r in roots:
        quotient = s.cancel((quotient-quotient.subs(y,r))/(y-r))
    zero(quotient-s.div(poly,p,y)[0],
         "Sequential quotient division " + str(roots))

# The complete centered conductor has shifts 0,6 and coefficients 1,-1.
# For delta=1/4, gamma=3 these are two actual allowed shifts.
for roots in [(13,7),(13,13,7),(13,7,7)]:
    p=s.prod(y-r for r in roots)
    d=len(roots); v=1; L=2*d
    a=sum(s.Rational(j+1,j+2)*y**j for j in range(d))
    B=s.expand(p*p.subs(y,y+6))
    response=a/p-a.subs(y,y+6)/p.subs(y,y+6)
    num=s.cancel(B*response)
    check(s.Poly(num,y).degree() == L-v-1,
          "Sharp unreduced numerator degree " + str(roots))
    # Confirm a translated pole collision has not been removed.
    check(s.Poly(B,y).degree()==L, "Complete denominator multiplicity "+str(roots))
    if 7 in roots:
        check(B.subs(y,7) == 0 and s.diff(B,y).subs(y,7) == 0,
              "Translated pole collision at7 "+str(roots))
    cseries=s.series((a/p).subs(y,1/z),z,0,d+1).removeO()
    bseries=s.series(response.subs(y,1/z),z,0,v+d+1).removeO()
    c=[s.expand(cseries).coeff(z,n) for n in range(1,d+1)]
    b=[s.expand(bseries).coeff(z,n) for n in range(1,v+d+1)]
    inverse=s.series(z/(1-s.exp(-6*z)),z,0,d).removeO()
    recovered=[]
    for n in range(1,d+1):
        value=s.factorial(n-1)*sum(
            inverse.coeff(z,n-ell)*b[v+ell-1]/s.factorial(v+ell-1)
            for ell in range(1,n+1))
        recovered.append(s.simplify(value))
    zero(s.Matrix(c)-s.Matrix(recovered), "Full Laurent convolution inverse "+str(roots))
    # Polynomial part, taken directly as the nonnegative Laurent powers.
    rec=s.expand(p*sum(recovered[n-1]/y**n for n in range(1,d+1)))
    rec=sum(rec.coeff(y,j)*y**j for j in range(d))
    zero(rec-a,"Original numerator recovered "+str(roots))

# Original k=9 upper and k=1 lower lattice: check the complete induced map.
delta=s.Rational(1,4); gamma=s.Integer(3)
def lattice(k):
    return [(2*b-k)*gamma-s.I*(2*a-k)*delta
            for a in range(k+1) for b in range(k+1)]
upper=lattice(9); lower=lattice(1)
check(all(t in upper and t+6 in upper for t in lower),
      "Both actual conductor shifts land in the upper lattice")
Qlower=s.Poly(s.prod(y-r for r in lower),y).as_expr().expand()
p=(y-13)*(y-7); B=s.expand(p*p.subs(y,y+6))
for a in (s.Integer(1),y):
    num=s.cancel(B*(a/p-a.subs(y,y+6)/p.subs(y,y+6)))
    response_mod=s.rem(num*s.invert(B,Qlower,y),Qlower,y)
    for r in lower:
        zero(response_mod.subs(y,r)-
             (a/p-a.subs(y,y+6)/p.subs(y,y+6)).subs(y,r),
             "Complete lower quotient at original root "+str((a,r)))
    check(s.Poly(num,y).degree()<4, "Finite degree guard gives unreduced numerator "+str(a))
p=(y-13)**2*(y-7);B=s.expand(p*p.subs(y,y+6))
num=s.cancel(B*(y**2/p-(y+6)**2/p.subs(y,y+6)))
check(s.Poly(num,y).degree()==4 and s.rem(num,Qlower,y)!=num,
      "Degree guard failure actually changes the numerator")

# A full positive polynomial-source fixture, with every relation retained.
# Its moment source is discrete and auxiliary; its quotient is the literal Q_1.
Q=Qlower
q=4; N=6
nodes=list(range(-3,4))
weights=[s.Rational(j+1,7) for j in range(7)]
source=s.Matrix([[sum(weights[t]*nodes[t]**(i+j) for t in range(7))
                  for j in range(N+1)] for i in range(N+1)])
check(source.det()>0,"Positive complete degree6 moment source")
J=matrix_map(lambda f:mod(f,Q),N+1,q)
G=s.simplify((J*source.inv()*J.T).inv())
minimum=s.simplify(source.inv()*J.T*G)
zero(J*minimum-s.eye(q),"Full minimum section is a right inverse")
zero(minimum.T*source*minimum-G,"Minimum section retains the quotient metric")
zero((s.eye(N+1)-minimum*J).T*source*minimum,
     "Orthogonality to the entire source relation space")
M=matrix_map(lambda f:mod(y*f,Q),q,q)
p=s.expand((y-13)**2);d=2
p_inv=s.invert(p,Q,y)
U=matrix_map(lambda f:mod(f*p_inv,Q),d,q)
Remainder=matrix_map(lambda f:s.rem(f,p,y),N+1,d)
Quotient=matrix_map(lambda f:s.div(f,p,y)[0],N+1,N-d+1)
Jsmall=matrix_map(lambda f:mod(f,Q),N-d+1,q)
Tp=s.simplify(Remainder*minimum)
Bp=s.simplify(Jsmall*Quotient*minimum)
F=s.simplify(U*Tp)
X=matrix_poly(p,M).inv()
zero(X-Bp-F,"Complete filtered inverse decomposition")
check(Tp.rank()==d and F.rank()==d,"Actual remainder and finite-rank term both have rank2")
check(G*M != M.conjugate().T*G,"Source fixture retains a nonselfadjoint original action")
low=s.eye(q)[:,:d]
error=s.eye(d)-Tp*low
zero(Tp*low-(s.eye(d)-error),"Exact remainder-projection defect")
right=s.simplify(low*(s.eye(d)-error).inv())
zero(Tp*right-s.eye(d),"Explicit low-polynomial right inverse of remainder map")

# Complex observation, full kernel and attained minimum.
Lambda=s.Matrix([[1,s.I,0,1],[0,1,2,-s.I],[1,0,s.I,3]])
QB=(Lambda*G.inv()*Lambda.conjugate().T).inv()
PB=G.inv()*Lambda.conjugate().T*QB*Lambda
H=U.conjugate().T*G*U
HB=U.conjugate().T*Lambda.conjugate().T*QB*Lambda*U
psd(HB,"Observed rational Gram")
check(HB.det()>0,"Both rational directions survive the complete observation")
psd(H-HB,"Full observation contraction")
zero(PB*PB-PB,"Original observed projection is idempotent")
zero(PB.conjugate().T*G-G*PB,"Observed projection is selfadjoint in G")

Cp=matrix_map(lambda f:s.rem(y*f,p,y),d,d)
one=s.eye(q)[:,0]
e=s.eye(d)[:,d-1]
zero(M*U-U*Cp-one*e.T,"Exact monic-filter action defect")
MS=s.Rational(1,2)*s.eye(q)+s.I*M
zero(MS*U-U*(s.Rational(1,2)*s.eye(d)+s.I*Cp)-s.I*one*e.T,
     "Physical S coordinate and factor i")
compression=H.inv()*U.conjugate().T*G*M*U
zero(compression-Cp-H.inv()*U.conjugate().T*G*one*e.T,
     "Attained compression uses the pulled-back domain Gram")

pi=matrix_map(lambda f:s.div(mod(p*f,Q),p,y)[0],q,q-d)
zero(pi*U,"The rational frame is killed by the exact quotient")
zero(pi*s.eye(q)[:,:q-d]-s.eye(q-d),"Low polynomials give the exact quotient right inverse")
check(pi.rank()==q-d,"Exact quotient kernel has the required dimension")
K=s.Matrix.hstack(*Lambda.nullspace())
HK=K.conjugate().T*G*K
Gquot=(pi*G.inv()*pi.conjugate().T).inv()
Kquot=(pi*K).conjugate().T*Gquot*(pi*K)
zero(H.det()/HB.det()-HK.det()/Kquot.det(),
     "Both complete quotient angle determinant ratios agree")
check(s.simplify(Kquot.det())>0,"Original kernel remains injective in the rational quotient")

# Exact ES arithmetic and complete repeated-pole polynomials.
P=s.expand((y-13)*(y-4)*(y-18)*(y-468))
zero(P-(y**4-503*y**3+16738*y**2-168480*y+438048),
     "Literal ES polynomial coefficients")
zero(s.Rational(4,13)-s.Rational(1,4)-s.Rational(1,18)-s.Rational(1,468),
     "Literal ES unit-fraction witness")
zero(sum(s.Rational(1,r) for r in (13,4,18,468))-s.Rational(5,13),
     "Complete ES reciprocal trace")
for k in (1,2,5):
    repeated=s.Poly(P**k,y)
    check(repeated.degree()==4*k and repeated.LC()==1,"ES monic degree "+str(k))
    for r in (13,4,18,468):
        for n in range(k):
            zero(repeated.diff((y,n)).eval(r),
                 "ES complete pole multiplicity "+str((k,r,n)))
check(341**2-338*341+49==1072,"Algebraic ES sufficient threshold")
check(337**2-338*337+49<0,"Previous admitted integer fails the v0 J81 guard")
k=2**20+1;qq=(k+1)**2;qm=(k-7)**2;dd=4*k
check(k%4==1 and dd<=qq,"A large ES degree remains below the original quotient degree")
check(s.Rational(145,16)*k*k <= s.Rational(1,2**28)*qm*qm,
      "Explicit squared original root-radius guard at a declared large index")
check(81*dd<=qm and 2*qq+81*dd-qm+2<=2*qm,
      "Distinct algebraic and lower-kernel degree guards")

receipt={
    "passed":True,
    "check_count":len(checks),
    "checks":checks,
    "scope":"Exact colliding-pole Hermite remainders, full Laurent inverse, actual lattice shifts, auxiliary full polynomial-source minimum, complex observation, action and quotient identities, and ES arithmetic. These checks do not certify native arithmetic moments, profile asymptotics, or the analytic absorption guard at the small lattice fixtures.",
    "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
out=Path(__file__).with_name("RATIONAL_FILTER_CHECKS.json")
out.write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"passed":True,"check_count":len(checks),"receipt":str(out)}))
