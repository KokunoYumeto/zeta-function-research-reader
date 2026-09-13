"""Independent finite auxiliary fixtures for the arithmetic volume comparison.

Uses exact rational/Gaussian-rational arithmetic. Analytic inequalities remain
the written proof's responsibility. The fixture source has asymmetric weights.
"""
import argparse
import hashlib
import itertools
import json
from pathlib import Path
import sympy as s

parser = argparse.ArgumentParser()
parser.add_argument('--output', required=True)
args = parser.parse_args()
checks = []

def check(name, value):
    if not bool(value):
        raise RuntimeError(name)
    checks.append(name)

u = s.symbols('u')

def gram(N, moment):
    return s.Matrix(N + 1, N + 1, lambda i, j: moment(i + j))

def remmat(N, psi):
    q = s.degree(psi, u)
    return s.Matrix(q, N + 1, lambda i, j: s.Poly(s.rem(u**j, psi, u), u).nth(i))

def jetmat(N, roots):
    rows = []
    for z, order in roots:
        for d in range(order):
            rows.append([s.diff(u**j, u, d).subs(u, z) for j in range(N + 1)])
    return s.Matrix(rows)

def positive_semidefinite(M):
    check('Hermitian matrix %d' % len(checks), M == M.adjoint())
    for size in range(1, M.rows + 1):
        for ids in itertools.combinations(range(M.rows), size):
            check('nonnegative principal minor %s at %d' % (ids, len(checks)),
                  s.simplify(M.extract(ids, ids).det()) >= 0)

roots = [(s.I, 2), (-s.I, 2)]
psi = s.expand((u - s.I)**2 * (u + s.I)**2)
q = 4
def mu_nu(j):
    return s.Rational(2, j + 1) if j % 2 == 0 else s.Integer(0)
nodes = [s.Rational(-2), s.Rational(1, 3), s.Rational(5, 4)]
weights = [s.Rational(1, 7), s.Rational(2, 5), s.Rational(3, 11)]
def mu_actual(j):
    return mu_nu(j) + sum(w * x**j for w, x in zip(weights, nodes))
check('asymmetric measure has nonzero first moment', mu_actual(1) != 0)
Z = jetmat(q - 1, roots)
expected_Z = s.prod(s.factorial(d) for z, order in roots for d in range(order))
expected_Z *= s.prod((roots[b][0] - roots[a][0])**(roots[a][1] * roots[b][1])
                     for a in range(len(roots)) for b in range(a + 1, len(roots)))
check('raw confluent Vandermonde includes exact row-order sign and factorials',
      s.expand(Z.det() - expected_Z) == 0)
# A second jet-only fixture makes the raw order-two factorial nontrivial.
triple_roots = [(s.I, 3), (-s.I, 3)]
Z3 = jetmat(5, triple_roots)
check('order-two raw factorial is retained', Z3.det() == 4 * (-2*s.I)**9)
source_var = s.symbols('S')
center, scale = s.Rational(3,2), s.Rational(5,7)
coefficient_map = s.Matrix(6, 6, lambda i,j:
    s.Poly((center+s.I*scale*u)**j,u).nth(i))
source_rows = []
phases = []
for z,order in triple_roots:
    for derivative in range(order):
        source_rows.append([s.diff(source_var**j,source_var,derivative).subs(
            source_var,center+s.I*scale*z) for j in range(6)])
        phases.append((s.I*scale)**derivative)
check('raw jet chart phase for every order through two',
      s.simplify(Z3*coefficient_map-s.diag(*phases)*s.Matrix(source_rows))==s.zeros(6))
def integrate_actual_polynomial(poly):
    return sum(coef*mu_actual(degree[0]) for degree,coef in s.Poly(poly,u).terms())
check('source Gram chart exact congruence',
      s.simplify(coefficient_map.adjoint()*gram(5,mu_actual)*coefficient_map -
      s.Matrix(6,6,lambda i,j: integrate_actual_polynomial(
          (center-s.I*scale*u)**i*(center+s.I*scale*u)**j)))==s.zeros(6))
check('scaled quotient determinant exact phase and magnitude',
      coefficient_map.det()==(s.I*scale)**15)
kernels = {}
volumes = {}
for N in (q, 2*q - 1):
    J = remmat(N, psi)
    E = jetmat(N, roots)
    check('E equals Z J at N=%d' % N, E == Z * J)
    H = gram(N, mu_actual)
    Hnu = gram(N, mu_nu)
    K = J * H.inv() * J.adjoint()
    Kraw = E * H.inv() * E.adjoint()
    Knuraw = E * Hnu.inv() * E.adjoint()
    check('raw/remainder determinant conversion N=%d' % N,
          s.simplify(Kraw.det() - Z.det() * s.conjugate(Z.det()) * K.det()) == 0)
    B = s.Matrix(N + 1, N - q + 1,
                 lambda i, j: s.Poly(u**j * psi, u).nth(i))
    check('original relation kernel N=%d' % N, J * B == s.zeros(q, N-q+1))
    G = K.inv()
    check('source/relation determinant N=%d' % N,
          s.simplify(G.det() - H.det() / (B.adjoint() * H * B).det()) == 0)
    positive_semidefinite(s.simplify(Knuraw - Kraw))
    kernels[N] = Kraw
    volumes[N] = G.det()
check('central determinant orientation',
      s.simplify(volumes[q] / volumes[2*q-1] - kernels[2*q-1].det() / kernels[q].det()) == 0)
positive_semidefinite(s.simplify(kernels[2*q-1] - kernels[q]))

# Weighted diagonal Gram majorant and independent Cauchy--Binet expansion.
N = q
H = gram(N, mu_actual)
taus = [s.Rational(j+1, j+2) for j in range(N+1)]
D = sum(taus) * s.diag(*[H[j,j] / taus[j] for j in range(N+1)])
positive_semidefinite(D-H)
E = jetmat(N, roots)
ds = [s.Rational(j+2, (j+1)**2) for j in range(N+1)]
A = E * s.diag(*ds) * E.adjoint()
minor_sum = sum(s.simplify(E[:,list(ids)].det() * s.conjugate(E[:,list(ids)].det()))
                * s.prod(ds[j] for j in ids)
                for ids in itertools.combinations(range(N+1),q))
check('positive Cauchy--Binet sum including complex phases', s.simplify(A.det()-minor_sum)==0)

# Direct origin-jet kernel, parity Cauchy blocks, and exact Legendre determinant.
for q in (2,4,6):
    N = 2*q - 1
    H = gram(N, mu_nu)
    Bq = s.Matrix(q,q,lambda i,j: mu_nu(2*q+i+j))
    half = q//2
    def cauchy_det(x):
        return s.prod(s.factorial(j)**2 for j in range(half)) / s.prod(
            x+a+b for a in range(half) for b in range(half))
    check('exact relation Cauchy determinant q=%d' % q,
          Bq.det() == cauchy_det(s.Rational(q)+s.Rational(1,2))
                      * cauchy_det(s.Rational(q)+s.Rational(3,2)))
    for d in (q+1,2*q):
        exact = s.prod(s.Rational(2,2*j+1)*(s.Rational(2**j,s.binomial(2*j,j)))**2
                       for j in range(d))
        check('exact Legendre Gram determinant d=%d q=%d' % (d,q),
              gram(d-1,mu_nu).det() == exact)
    Jq = remmat(q,u**q)
    JN = remmat(N,u**q)
    Kq = Jq * gram(q,mu_nu).inv() * Jq.adjoint()
    KN = JN * H.inv() * JN.adjoint()
    ratio = gram(q,mu_nu).det()*Bq.det()/(mu_nu(2*q)*H.det())
    check('origin-jet central ratio q=%d' % q, s.simplify(KN.det()/Kq.det()-ratio)==0)

# A symbolic free family checks the degree-preserving quotient identity, not
# a distinct-centre Vandermonde at the merged fibre.
t=s.symbols('t',real=True)
psi1=(u-s.I)*(u+2*s.I)
psit=s.expand((u-t*s.I)*(u+2*t*s.I))
f=3+2*u-u**3+u**4
left=s.rem(f.subs(u,t*u),psi1,u)
right=s.rem(f,psit,u).subs(u,t*u)
check('monic family quotient substitution identity', s.expand(left-right)==0)
J=remmat(3,psit)
check('family remains surjective at merged fibre', J[:,:2]==s.eye(2))
H=gram(3,mu_actual)
K=s.simplify(J*H.inv()*J.adjoint())
check('merged fibre determinant positive', K.det().subs(t,0)>0)
check('exact determinant derivative in fixed source',
      s.simplify(s.diff(K.det(),t)-K.det()*s.trace(K.inv()*s.diff(K,t)))==0)

payload={
 'schema':'arithmetic-volume-upper-independent-fixture-v1',
 'status':'pass',
 'check_count':len(checks),
 'checks':checks,
 'arithmetic':'exact SymPy rational and Gaussian-rational',
 'actual_arithmetic_density_certified':False,
 'analytic_asymptotic_bound_certified_by_fixture':False,
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
Path(args.output).write_text(json.dumps(payload,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'pass','check_count':len(checks)}))
