"""Exact finite calibrations of TC13--TC28; no arithmetic zero certification."""
from pathlib import Path
import json
import sympy as s

checks = []

def record(name, value):
    if value is not True:
        raise AssertionError((name, value))
    checks.append(name)

def zero(M):
    return all(s.simplify(x) == 0 for x in M)

def positive(M):
    return M == M.conjugate().T and all(
        s.simplify(M[:j, :j].det()) > 0 for j in range(1, M.rows + 1))

def sylvester_inverse(M, G):
    d = M.rows
    xs = s.symbols(f"x0:{d*d}")
    X = s.Matrix(d, d, xs)
    eq = M.conjugate().T * X + X * M + G
    sol = s.solve(list(eq), xs)
    return s.simplify(X.subs(sol))

for name, A, G0, eps in [
    ("critical_nilpotent",
     s.Matrix([[s.Rational(1, 2), 1], [0, s.Rational(1, 2)]]),
     s.Matrix([[2, 1+s.I], [1-s.I, 3]]), s.Rational(1, 4)),
    ("reflection_pair",
     s.diag(s.Rational(1, 4)+2*s.I, s.Rational(3, 4)+2*s.I),
     s.Matrix([[3, 1+s.I], [1-s.I, 4]]), s.Rational(3, 4)),
]:
    Id = s.eye(A.rows)
    Gp = sylvester_inverse(A-(1+eps)/2*Id, G0)
    Gn = sylvester_inverse(-A+(1-eps)/2*Id, G0)
    G = Gp + Gn
    W = A.conjugate().T*G + G*A - G
    record(name+"_positive_plus", bool(positive(Gp)))
    record(name+"_positive_minus", bool(positive(Gn)))
    record(name+"_positive_gram", bool(positive(G)))
    record(name+"_bilateral_sign", zero(W-eps*(Gp-Gn)))
    record(name+"_upper_slack", zero(eps*G-W-2*eps*Gn))
    record(name+"_lower_slack", zero(eps*G+W-2*eps*Gp))

# Closed CRT moment formula, with every local nilpotent term retained.
eps = s.Rational(1, 4)
N = s.Matrix([[0, 1], [0, 0]])
G0 = s.Matrix([[2, 1+s.I], [1-s.I, 3]])
Imom = lambda k: s.factorial(k)*(eps**(-k-1)+(-1)**k*eps**(-k-1))
Gformula = s.zeros(2)
for i in range(2):
    for j in range(2):
        Gformula += Imom(i+j)/s.factorial(i)/s.factorial(j) * \
            (N**i).conjugate().T*G0*N**j
A = s.eye(2)/2+N
Gsolve = sylvester_inverse(A-(1+eps)/2*s.eye(2), G0) + \
    sylvester_inverse(-A+(1-eps)/2*s.eye(2), G0)
record("all_nilpotent_moment_terms", zero(Gformula-Gsolve))

# Rank-two aggregate bound can exceed the single-eigenvector bound.
# Diagonal entries of H are 1/4,1/4,-1/4,-1/4, but eigenvalues are +/-1/2.
p = s.Matrix([1, 1, 0, 0])/s.sqrt(2)
q = s.Matrix([0, 0, 1, 1])/s.sqrt(2)
H = (p*p.T-q*q.T)/2
record("aggregate_rank_two", H.rank() == 2)
record("aggregate_zero_trace", s.trace(H) == 0)
record("aggregate_positive_diagonal_sum",
       sum(max(H[j,j], 0) for j in range(4)) == s.Rational(1, 2))
record("aggregate_bound_exact", max(abs(x) for x in H.eigenvals()) == s.Rational(1, 2))

# Exact determinant recurrence with a non-diagonal Hermitian Gram.
G = s.Matrix([[3, s.I], [-s.I, 2]])
z = s.Matrix([1, 1+s.I])
eta = s.Integer(10)
Gnext = G-z*z.conjugate().T/eta
u = (z.conjugate().T*G.inv()*z)[0]
record("rank_one_update_positive", bool(positive(Gnext)))
record("rank_one_determinant_identity",
       s.simplify(u-eta*(1-Gnext.det()/G.det())) == 0)

receipt = {
    "scope": "Exact finite identities TC13--TC28; no analytic density, RH, zero location, or actual theta quadrature certificate",
    "sympy_version": s.__version__,
    "passed": len(checks), "checks": checks, "all_passed": True
}
target = Path(__file__).with_suffix(".json")
target.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
print(json.dumps(receipt, indent=2))
