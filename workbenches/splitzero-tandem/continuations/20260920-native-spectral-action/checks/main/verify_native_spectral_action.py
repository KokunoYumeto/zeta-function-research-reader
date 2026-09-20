"""Exact finite algebra for NATIVE_SPECTRAL_ACTION.tex; no sampled arithmetic zeros."""
from __future__ import annotations
import argparse
import functools
import itertools
import json
from pathlib import Path
import sympy as s

t, z, x, w = s.symbols("t z x w")
checks = []

def equal(name, actual, expected):
    difference = actual - expected
    if isinstance(difference, s.MatrixBase):
        ok = all(s.cancel(e) == 0 for e in difference)
    else:
        ok = s.cancel(s.expand(difference)) == 0
    if not ok:
        raise RuntimeError(f"{name}: actual={actual}, expected={expected}")
    checks.append(name)

@functools.lru_cache(None)
def compositions(total, count):
    if count == 1:
        return ((total,),)
    return tuple((j,) + rest for j in range(total + 1)
                 for rest in compositions(total - j, count - 1))

def dd_monomial(degree, nodes):
    n = len(nodes)
    if degree < n - 1:
        return s.Integer(0)
    return sum((s.prod(v ** a for v, a in zip(nodes, powers))
                for powers in compositions(degree - n + 1, n)),
               s.Integer(0))

def cyclic_monomial(lambdas, V, degree, n):
    if degree == 0:
        return s.Integer(0)
    return sum((s.prod(V[inds[j], inds[(j + 1) % n]]
                       for j in range(n))
                * degree * dd_monomial(degree - 1,
                                      tuple(lambdas[j] for j in inds))
                for inds in itertools.product(range(len(lambdas)), repeat=n)),
               s.Integer(0))

def adjoint(X, G):
    return G.inv() * X.conjugate().T * G

_trace_coefficient_cache = {}
def trace_coefficients(A, V, m):
    key = (A.rows, tuple(A), tuple(V), m)
    if key not in _trace_coefficient_cache:
        coefficients = [s.eye(A.rows)]
        for degree in range(m):
            updated = []
            for n in range(degree+2):
                entry = s.zeros(A.rows)
                if n < len(coefficients):
                    entry += coefficients[n]*A
                if n > 0:
                    entry += coefficients[n-1]*V
                updated.append(entry.applyfunc(s.expand))
            coefficients = updated
        _trace_coefficient_cache[key] = [s.expand(s.trace(C))
                                         for C in coefficients]
    return _trace_coefficient_cache[key]

def direct_coefficient(A, V, m, n):
    coefficients = trace_coefficients(A,V,m)
    return coefficients[n] if n < len(coefficients) else s.Integer(0)

def trace_polynomial(A,V,m):
    return sum(value*t**n for n,value in enumerate(trace_coefficients(A,V,m)))

# Cyclic coefficients include a repeated eigenvalue and arbitrary nonselfadjoint V.
lambdas = (-1, -1, 2)
D = s.diag(*lambdas)
V = s.Matrix([[1, 2, -1], [3, -2, 4], [2, 1, 5]])
for m in range(0, 9):
    for n in range(1, 5):
        cyc = cyclic_monomial(lambdas, V, m, n)
        equal(f"cyclic-coefficient-m{m}-n{n}",
              direct_coefficient(D, V, m, n), cyc / n)
        equal(f"cyclic-derivative-m{m}-n{n}",
              s.factorial(n) * direct_coefficient(D, V, m, n),
              s.factorial(n - 1) * cyc)
        c_phase = s.Rational(3,2)
        S_base = c_phase*s.eye(3)+s.I*D
        S_nodes = tuple(c_phase+s.I*v for v in lambdas)
        equal(f"original-S-cyclic-phase-m{m}-n{n}",
              direct_coefficient(S_base, -s.I*V, m, n),
              (-s.I)**n*cyclic_monomial(S_nodes,V,m,n)/n)

# Repeated-node identity, including all-equal nodes.
for nodes in ((0,), (1, 1), (-2, 0, 2), (1, 1, 1), (-1, -1, 2, 2)):
    for m in range(0, 9):
        lhs = m * dd_monomial(m - 1, nodes) if m else s.Integer(0)
        rhs = sum(dd_monomial(m, nodes + (node,)) for node in nodes)
        equal(f"repeated-node-{nodes}-m{m}", lhs, rhs)

# Divided-difference cancellation in the nilpotent second derivative.
for a, b, c in ((-2, 3, 1), (1, 1, 1), (2, 2, -1), (0, 1, 0)):
    for m in range(0, 9):
        derivative_dd = lambda nodes: (
            m * dd_monomial(m - 1, nodes) if m else s.Integer(0))
        lhs = (derivative_dd((a, b)) - derivative_dd((a, c))
               - derivative_dd((c, b)) + derivative_dd((c, c)))
        equal(f"second-cancellation-{a}-{b}-{c}-m{m}", lhs,
              (a - c) * (b - c) * derivative_dd((a, b, c, c)))

models = []
# Native-form algebra example: actual mass-three comparison measure, not arithmetic.
G0 = s.diag(3, 1)
A0 = s.Matrix([[0, s.Rational(1, 3)], [1, 0]])
r0 = s.Matrix([s.Rational(4, 3), 0])
ell0 = s.Matrix([[0, 1]])
models.append(("mass-three-quotient", G0, A0, r0, ell0, s.diag(1, -1)))
models.append(("genuine-original-Jordan-block", G0, A0,
               s.Matrix([s.Rational(1,3),0]), ell0, s.diag(1,-1)))
G_jordan = s.Matrix(4,4,lambda j,l:
                    s.Rational(3,j+l+1) if (j+l)%2==0 else 0)
M_jordan = s.Matrix([[0,0,0,-1],[1,0,0,0],
                     [0,1,0,-2],[0,0,1,0]])
r_jordan = s.Matrix([s.Rational(32,35),0,s.Rational(20,7),0])
ell_jordan = s.Matrix([[0,0,0,1]])
Q_jordan = r_jordan*ell_jordan
models.append(("nonreal-Jordan-multiplicities",G_jordan,
               M_jordan+Q_jordan,r_jordan,ell_jordan,s.diag(1,-1,1,-1)))

# Nonidentity G and repeated eigenvalues, via an explicitly retained coordinate map.
D1 = s.diag(-2, -2, 0, 2, 2)
P1 = s.zeros(5)
for j in range(5):
    P1[j, 4-j] = 1
r1 = s.Matrix([1, 2, 0, 2, 1])
ell1 = s.Matrix([[1, 1, 0, -1, -1]])
U = s.Matrix([[2,1,0,0,0],[0,3,1,0,0],[0,0,1,1,0],
              [0,0,0,2,1],[0,0,0,0,1]])
models.append(("repeated-nonidentity-metric", U.T*U, U.inv()*D1*U,
               U.inv()*r1, ell1*U, U.inv()*P1*U))
models.append(("zero-correction", s.diag(2, 3), s.diag(-1, 1),
               s.zeros(2, 1), s.Matrix([[1, 2]]),
               s.Matrix([[0, s.sqrt(s.Rational(3,2))],
                         [s.sqrt(s.Rational(2,3)), 0]])))

for name, G, A, r, ell, parity in models:
    dim = A.rows
    Q = r * ell
    T = A - t * Q
    Qdag = adjoint(Q, G)
    gamma = (ell * A * r)[0]
    eps2 = s.trace(Qdag * Q)
    d = (z*s.eye(dim)-A).det()
    kappa = s.cancel((ell * (z*s.eye(dim)-A).inv() * r)[0])
    chi = (z*s.eye(dim)-(A-Q)).det()
    pt = (z*s.eye(dim)-T).det()
    equal(name+"-selfadjoint", adjoint(A,G), A)
    equal(name+"-square-zero", Q*Q, s.zeros(dim))
    equal(name+"-zero-row-pairing", (ell*r)[0], 0)
    equal(name+"-nilpotent-trace", s.trace(Q), 0)
    if name == "genuine-original-Jordan-block":
        equal(name+"-nonzero-Jordan-entry", (A-Q)[1,0], 1)
        equal(name+"-Jordan-square", (A-Q)**2, s.zeros(dim))
        equal(name+"-full-repeated-characteristic", chi, z**2)
    if name == "nonreal-Jordan-multiplicities":
        M = A-Q
        equal(name+"-complete-characteristic",chi,(z*z+1)**2)
        equal(name+"-repeated-minimal-polynomial",
              (M*M+s.eye(dim))**2,s.zeros(dim))
        equal(name+"-nonzero-first-nilpotent",
              (M*M+s.eye(dim))[0,0],1)
        equal(name+"-one-dimensional-eigenspace-plus-i",
              dim-(M-s.I*s.eye(dim)).rank(),1)
        equal(name+"-one-dimensional-eigenspace-minus-i",
              dim-(M+s.I*s.eye(dim)).rank(),1)
    equal(name+"-parity-isometry", parity.T*G*parity, G)
    equal(name+"-parity-A", parity*A*parity, -A)
    equal(name+"-parity-Q", parity*Q*parity, -Q)
    equal(name+"-full-determinant", pt, (1-t)*d+t*chi)
    equal(name+"-secular-determinant", pt, d*(1+t*kappa))
    equal(name+"-scalar-even", kappa.subs(z,-z), kappa)
    RA = (z*s.eye(dim)-A).inv()
    # Multiplication checks the exact rational inverse without a second heavy inverse.
    candidate = RA-t*RA*Q*RA/(1+t*kappa)
    equal(name+"-resolvent", (z*s.eye(dim)-T)*candidate, s.eye(dim))
    equal(name+"-resolvent-trace", s.trace(candidate-RA),
          t*s.diff(kappa,z)/(1+t*kappa))
    equal(name+"-endpoint-scalar-resolvent",
          (ell*candidate*r)[0], kappa/(1+t*kappa))
    moments = [(ell*A**j*r)[0] for j in range(12)]
    original_moments = [(ell*(A-Q)**j*r)[0] for j in range(9)]
    for m in range(0,9):
        trace_poly = trace_polynomial(A,-Q,m)
        # Residue F' kappa^n computed as a finite product of its moment series.
        kp = [s.Integer(0)] + moments[:m]
        kp_power = [s.Integer(1)] + [s.Integer(0)]*m
        predicted = s.trace(A**m)
        for n in range(1,m+1):
            kp_power = [
                sum(kp_power[j]*kp[d-j] for j in range(d+1))
                for d in range(m+1)
            ]
            residue = m*kp_power[m]
            predicted += (-t)**n*residue/n
        equal(name+f"-all-trace-coefficients-m{m}", trace_poly, predicted)
        equal(name+f"-degree-cutoff-m{m}",
              sum(trace_poly.coeff(t,j)*t**j
                  for j in range(m//2+1,m+1)), 0)
        if m%2:
            equal(name+f"-odd-trace-m{m}", trace_poly, 0)
        endpoint_kp = [s.Integer(0)] + original_moments[:m]
        endpoint_power = [s.Integer(1)] + [s.Integer(0)]*m
        for n in range(1,4):
            endpoint_power = [
                sum(endpoint_power[j]*endpoint_kp[d-j]
                    for j in range(d+1))
                for d in range(m+1)
            ]
            equal(name+f"-original-endpoint-m{m}-n{n}",
                  s.diff(trace_poly,t,n).subs(t,1),
                  (-1)**n*s.factorial(n-1)*m*endpoint_power[m])
    equal(name+"-quadratic-trace", trace_polynomial(A,-Q,2),
          s.trace(A*A)-2*t*gamma)
    equal(name+"-quartic-trace", trace_polynomial(A,-Q,4),
          s.trace(A**4)-4*t*(ell*A**3*r)[0]+2*t**2*gamma**2)
    # t is real for the metric formula; compute the adjoint as A-t Qdag explicitly.
    H = s.trace((A-t*Qdag)*(A-t*Q))
    C = s.I*t*(Qdag-Q)
    equal(name+"-metric-action", H,
          s.trace(A*A)-t*(gamma+s.conjugate(gamma))+t*t*eps2)
    equal(name+"-metric-curvature", s.diff(H,t,2), 2*eps2)
    equal(name+"-defect-trace", s.trace(C*C), 2*t*t*eps2)
    J = s.trace((A-w*Qdag)*(A-z*Q))
    equal(name+"-mixed-curvature", s.diff(J,z,w), eps2)
    dil = s.BlockMatrix([[s.zeros(dim),T],
                         [A-t*Qdag,s.zeros(dim)]]).as_explicit()
    equal(name+"-dilation-trace", s.trace(dil*dil), 2*H)
    for t_value in (0,s.Rational(1,2),1):
        equal(name+f"-dilation-determinant-t{t_value}",
              (z*s.eye(2*dim)-dil.subs(t,t_value)).det(),
              (z*z*s.eye(dim)-((A-t*Qdag)*T).subs(t,t_value)).det())
    c = s.Rational(3,2)
    B = c*s.eye(dim)+s.I*T
    equal(name+"-S-determinant", (z*s.eye(dim)-B).det(),
          s.I**dim*pt.subs(z,(z-c)/s.I))
    equal(name+"-S-defect",
          B+(c*s.eye(dim)-s.I*(A-t*Qdag))-2*c*s.eye(dim), C)
    for degree in range(0,6):
        transported = sum(s.binomial(degree,j)*c**(degree-j)*s.I**j
                          *trace_polynomial(A,-Q,j) for j in range(degree+1))
        equal(name+f"-S-polynomial-phase-{degree}",
              trace_polynomial(c*s.eye(dim)+s.I*A,-s.I*Q,degree), transported)

# Identical complete trace paths with different metric curvature, retaining parity.
path_data = []
for a,b in ((s.Integer(1),s.Integer(1)),(s.Integer(2),s.Integer(1))):
    A = s.diag(-2,-1,1,2)
    r = s.Matrix([a,b,b,a])
    ell = s.Matrix([[1/a,1/b,-1/b,-1/a]])
    Q = r*ell
    path_data.append(((z*s.eye(4)-(A-t*Q)).det(), s.trace(Q.T*Q)))
equal("same-full-polynomial-different-metric",path_data[0][0],path_data[1][0])
equal("first-curvature",path_data[0][1],16)
equal("second-curvature",path_data[1][1],25)

# Deliberate-failure controls must fail; explicit exceptions survive Python -O.
controls = {}
for name, wrong, correct in [
    ("wrong-n-factor",s.Integer(4),s.Integer(2)),
    ("nilpotent-means-isospectral",(z*s.eye(2)-(A0-r0*ell0)).det(),
      (z*s.eye(2)-A0).det()),
    ("zero-holomorphic-curvature-means-zero-epsilon",s.Integer(0),
      s.trace(adjoint(r0*ell0,G0)*(r0*ell0))),
    ("same-traces-means-same-metric-curvature",path_data[0][1],path_data[1][1]),
]:
    if s.cancel(wrong-correct)==0:
        raise RuntimeError("Negative control failed to detect: "+name)
    controls[name]="rejected"

parser=argparse.ArgumentParser()
parser.add_argument("--output",default="CHECKS.json")
args=parser.parse_args()
report={"status":"passed","exact_check_count":len(checks),
        "negative_control_count":len(controls),"negative_controls":controls,
        "sympy_version":s.__version__,"models":[m[0] for m in models],
        "scope":"Finite exact algebra; no arithmetic-zero sampling or endpoint claim.",
        "checks":checks}
Path(args.output).write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:v for k,v in report.items() if k!="checks"}))
