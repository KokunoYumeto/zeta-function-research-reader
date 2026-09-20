"""Independent exact replay of EC1--EC15, using explicit exception guards."""
import argparse
import json
from pathlib import Path
import sympy as s

t, c = s.symbols("t c", real=True)
z, x = s.symbols("z x")
count = 0
negative = 0


def check(value, name):
    global count
    entries = list(value) if isinstance(value, s.MatrixBase) else [value]
    if any(s.simplify(s.expand(v)) != 0 for v in entries):
        raise RuntimeError("Failed exact check: " + name)
    count += 1


def reject(value, name):
    global negative
    entries = list(value) if isinstance(value, s.MatrixBase) else [value]
    if all(s.simplify(s.expand(v)) == 0 for v in entries):
        raise RuntimeError("Wrong formula unexpectedly passed: " + name)
    negative += 1


G2 = s.diag(3, 1)
A2 = s.Matrix([[0, s.Rational(1, 3)], [1, 0]])
r2 = s.Matrix([s.Rational(1, 3), 0])
ell2 = s.Matrix([[0, 1]])
Q2 = r2 * ell2
T2 = A2 - t * Q2
M2 = T2.subs(t, 1)
check(G2*A2 - A2.T*G2, "EC1 metric")
check(Q2**2, "EC1 nilpotence")
check(T2**2 - (1-t)*s.eye(2)/3, "EC2 full polynomial square")
check(M2**2, "EC2 Jordan square")
reject(M2, "endpoint is not the zero matrix")
check((ell2*(z*s.eye(2)-T2).inv()*r2)[0] - 1/(3*z*z-1+t),
      "EC3 scalar resolvent")
check((z*s.eye(2)-M2).inv() - s.eye(2)/z - M2/z**2,
      "EC3 full double-pole resolvent")
check((z*s.eye(2)-T2).det() - (z*z-(1-t)/3), "EC3 characteristic")

G4 = s.Matrix(4, 4, lambda i, j: s.Rational(3, i+j+1) if (i+j)%2 == 0 else 0)
M4 = s.Matrix([[0,0,0,-1],[1,0,0,0],[0,1,0,-2],[0,0,1,0]])
r4 = s.Matrix([s.Rational(32,35),0,s.Rational(20,7),0])
ell4 = s.Matrix([[0,0,0,1]])
Q4 = r4*ell4
A4 = M4+Q4
T4 = A4-t*Q4
for n, expected in enumerate([3,3,s.Rational(4,5),s.Rational(48,875)], start=1):
    check(G4[:n,:n].det()-expected, "EC6 positive principal determinant")
check(G4*A4-A4.T*G4, "EC7 retained metric adjoint")
check(Q4**2, "EC7 nilpotence")
check((r4.T*G4*r4)[0]-s.Rational(15472,1225), "EC8 column factor")
check((ell4*G4.inv()*ell4.T)[0]-s.Rational(175,12), "EC8 row factor")
epsilon2 = s.trace(G4.inv()*Q4.T*G4*Q4)
check(epsilon2-s.Rational(3868,21), "EC8 complete epsilon")
check(M4.charpoly(z).as_expr()-(z*z+1)**2, "EC9 complete characteristic")
check((M4*M4+s.eye(4))**2, "EC9 retained nilpotent square")
reject(M4*M4+s.eye(4), "both Jordan blocks are nonzero")
check(s.Matrix.hstack(*[M4**j*s.eye(4)[:,0] for j in range(4)])-s.eye(4),
      "EC9 cyclic basis")
if not (epsilon2-16).is_positive:
    raise RuntimeError("Aggregate inequality failed.")
count += 1
reject(s.Integer(4)-2, "distinct-only count is not aggregate")
d = z**4-s.Rational(6,7)*z*z+s.Rational(3,35)
npoly = s.Rational(20,7)*z*z+s.Rational(32,35)
check((ell4*(z*s.eye(4)-A4).inv()*r4)[0]-npoly/d,
      "EC11 direct initial scalar")
check((ell4*(z*s.eye(4)-M4).inv()*r4)[0]-npoly/(z*z+1)**2,
      "EC11 direct endpoint scalar")
for pole in (s.I, -s.I):
    check(npoly.subs(z,pole)+s.Rational(68,35), "EC11 noncancelled numerator")

# Independent moment recurrence from the complete characteristic polynomial.
# a(t), b(t) retain the entire comparison-measure determinant.
a = s.Rational(-6,7)+s.Rational(20,7)*t
b = s.Rational(3,35)+s.Rational(32,35)*t
even4 = [s.Integer(4), -2*a]
for j in range(2,7):
    even4.append(s.expand(-a*even4[-1]-b*even4[-2]))
for j in range(7):
    check(even4[j]-s.trace(T4**(2*j)), "full matrix/recurrence trace")
    check(even4[j].subs(t,1)-4*(-1)**j, "endpoint repeated eigenvalue trace")

for degree in range(13):
    trace2 = s.Integer(0) if degree%2 else 2*((1-t)/3)**(degree//2)
    trace4 = s.Integer(0) if degree%2 else even4[degree//2]
    for order in range(1,7):
        rhs2 = (2*(-1)**order*s.factorial(order)/3**order
                if degree == 2*order else s.Integer(0))
        check(s.diff(trace2,t,order).subs(t,1)-rhs2,
              "EC5 all monomial endpoint derivatives")
        coefficient = s.Integer(0)
        if degree%2 == 0 and degree >= 2*order:
            j = degree//2
            for index in range(min(order,j-order)+1):
                remaining = j-order-index
                coefficient += (
                    s.binomial(order,index)*100**(order-index)*32**index
                    *(-1)**remaining*s.binomial(2*order+remaining-1,remaining)
                )
            coefficient /= s.Integer(35)**order
        rhs4 = (-1)**order*s.factorial(order-1)*degree*coefficient
        check(s.diff(trace4,t,order).subs(t,1)-rhs4,
              "SA41 nonreal Jordan endpoint residue")

for dimension, T in ((2,T2),(4,T4)):
    B = c*s.eye(dimension)+s.I*T
    original = (x*s.eye(dimension)-B).det()
    transported = s.I**dimension*(z*s.eye(dimension)-T).det().subs(
        z,(x-c)/s.I)
    check(original-transported, "EC13 full determinant phase")
    check((x*s.eye(dimension)-B) -
          s.I*((x-c)/s.I*s.eye(dimension)-T), "EC13 matrix phase")

for degree in range(9):
    f = x**degree
    B2 = c*s.eye(2)+s.I*T2
    original_trace = s.trace(B2**degree)
    for order in range(1,5):
        expected = (2*s.factorial(order)*s.diff(f,x,2*order).subs(x,c)/
                    (3**order*s.factorial(2*order)))
        check(s.diff(original_trace,t,order).subs(t,1)-expected,
              "EC15 original S-phase endpoint")

# Nonzero one-dimensional scalar cycle tests isolate (-i)^n without any
# nilpotence cancellation; the source phase identity is general polynomial algebra.
lam = s.Rational(2,5)
weight = s.Rational(3,7)
for order in range(1,6):
    degree = order+2
    direct = s.diff((c+s.I*lam-s.I*t*weight)**degree,t,order).subs(t,0)
    repeated_divdiff = (s.diff(x**degree,x,order).subs(x,c+s.I*lam)/
                        s.factorial(order-1))
    expected = (-s.I)**order*s.factorial(order-1)*repeated_divdiff*weight**order
    check(direct-expected, "SA35 isolated original coordinate phase")
    if order%2:
        reject(direct-(-1)*expected, "wrong odd phase sign")

result = {"status":"PASS", "exact_identity_checks":count,
          "rejected_wrong_formula_controls":negative,
          "comparison_metric_epsilon_squared":str(epsilon2),
          "aggregate_with_algebraic_multiplicity":"4",
          "main_checked_locators":"SA32--SA43",
          "independent_proof_locators":"EC1--EC15",
          "scope":"Finite exact tests and proofs; no arithmetic zero or asymptotic conclusion.",
          "sympy_version":s.__version__}
parser = argparse.ArgumentParser()
parser.add_argument("--output",type=Path)
args = parser.parse_args()
rendered = json.dumps(result,indent=2)
if args.output:
    args.output.write_text(rendered+"\n",encoding="utf-8")
print(rendered)
