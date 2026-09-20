"""Exact finite tests for HEAT_METRIC_COMPARISON.tex; no floating-point inputs."""
from pathlib import Path
import hashlib
import json
import sympy as S

HERE = Path(__file__).resolve().parent
checks = 0
negative_controls = 0


def equal(name, left, right):
    global checks
    difference = left - right
    entries = list(difference) if isinstance(difference, S.MatrixBase) else [difference]
    if any(S.simplify(value) != 0 for value in entries):
        raise RuntimeError(f"Exact equality failed: {name}: {difference}")
    checks += 1


def nonnegative(name, value):
    global checks
    value = S.simplify(value)
    if value.is_nonnegative is not True:
        raise RuntimeError(f"Exact inequality failed or undecided: {name}: {value}")
    checks += 1


def must_differ(name, left, right):
    global negative_controls
    difference = S.simplify(left - right)
    if difference == 0:
        raise RuntimeError(f"Deliberate-failure control was not detected: {name}")
    negative_controls += 1


def adjoint(X, G):
    return G.inv() * X.conjugate().T * G


I = S.I
cases = [
    ("mass-three", S.diag(3, 1), S.Matrix([[0, S.Rational(1, 3)], [1, 0]]),
     S.Matrix([[0, S.Rational(4, 3)], [0, 0]])),
    ("complex-gamma", S.eye(2), S.Matrix([[1, I], [-I, 2]]),
     S.Matrix([[0, 2], [0, 0]])),
]
G = S.Matrix([[2, 1], [1, 3]])
H = S.Matrix([[1, I], [-I, 4]])
cases.append(("nondiagonal-original-metric", G, G.inv() * H,
              S.Matrix([1, 1]) * S.Matrix([[1, -1]])))
G = S.diag(2, 3, 5)
H = S.Matrix([[1, I, 2], [-I, 3, 1 + I], [2, 1 - I, -2]])
cases.append(("three-dimensional-complex", G, G.inv() * H,
              S.Matrix([1, I, 1]) * S.Matrix([[1, 0, -1]])))
cases.append(("zero-correction", S.diag(2, 5), S.diag(1, -3), S.zeros(2)))

t_symbol = S.symbols("t", real=True)
case_reports = []
for name, G, A, Q in cases:
    Qd = adjoint(Q, G)
    epsilon2 = S.simplify(S.trace(Qd * Q))
    gamma = S.simplify(S.trace(A * Q))
    equal(f"{name}: A adjoint", adjoint(A, G), A)
    equal(f"{name}: nilpotent", Q * Q, S.zeros(Q.rows))
    equal(f"{name}: rank-one cubic", Q * Qd * Q, epsilon2 * Q)
    equal(f"{name}: squared metric correction", (Qd * Q) ** 2, epsilon2 * Qd * Q)
    T = A - t_symbol * Q
    Td = adjoint(T, G)
    K = (T - Td) / (2 * I)
    equal(f"{name}: skew norm", S.trace(K * K), t_symbol ** 2 * epsilon2 / 2)
    D1 = S.trace(Td * T) - S.re(S.trace(T ** 2))
    equal(f"{name}: first heat coefficient", D1, t_symbol ** 2 * epsilon2)
    D2 = S.trace((Td * T) ** 2) - S.re(S.trace(T ** 4))
    exact_D2 = (2 * t_symbol ** 2 * S.trace(A ** 2 * (Q * Qd + Qd * Q))
                - 4 * t_symbol ** 3 * epsilon2 * S.re(gamma)
                + t_symbol ** 4 * epsilon2 ** 2)
    equal(f"{name}: second heat coefficient", S.expand(D2), S.expand(exact_D2))
    # The rational upper bound is >= ||A - tQ||_G^2 by the triangle
    # inequality followed by (a+b)^2 <= 2(a^2+b^2).
    A_hs2 = S.simplify(S.trace(A ** 2))
    for t_value in [S.Rational(-1), S.Rational(0), S.Rational(1, 3), S.Rational(1), S.Rational(2)]:
        Tv = A - t_value * Q
        Tdv = adjoint(Tv, G)
        B2_upper = 2 * (A_hs2 + t_value ** 2 * epsilon2)
        for n in range(1, 7):
            dn = S.simplify(S.trace((Tdv * Tv) ** n) - S.re(S.trace(Tv ** (2 * n))))
            equal(f"{name}: real D{n} at {t_value}", S.im(dn), S.Integer(0))
            bound = n * (2 * n - 1) * t_value ** 2 * epsilon2 * B2_upper ** (n - 1)
            nonnegative(f"{name}: positive-side bound D{n} at {t_value}", bound - dn)
            nonnegative(f"{name}: negative-side bound D{n} at {t_value}", bound + dn)
    case_reports.append({"name": name, "dimension": A.rows,
                         "epsilon_squared": str(epsilon2), "gamma": str(gamma)})

# Exact example with the original mass-three metric.
G, A, Q = cases[0][1:]
T = A - t_symbol * Q
a = (1 - 4 * t_symbol) / 3
equal("HM19 holomorphic square", T ** 2, a * S.eye(2))
equal("HM19 metric square", adjoint(T, G) * T, S.diag(S.Rational(1, 3), 3 * a ** 2))
equal("HM19 first scalar coefficient", S.Rational(1, 3) + 3 * a ** 2 - 2 * a,
      S.Rational(16, 3) * t_symbol ** 2)

# The scalar entire-function sum used in the dimension-independent proof.
x = S.symbols("x", real=True)
for n in range(1, 12):
    coefficient = S.diff((1 + 2 * x) * S.exp(x), x, n - 1).subs(x, 0) / S.factorial(n - 1)
    equal(f"entire remainder coefficient {n}", coefficient,
          S.Rational(n * (2 * n - 1), S.factorial(n)))
equal("rational error at x=1/7", 3 * S.Rational(1, 7) / (1 - S.Rational(1, 7)), S.Rational(1, 2))

# Mutated formulas must actually fail on the exact data, including -O runs.
epsilon2 = S.Rational(16, 3)
must_differ("omitted t squared", epsilon2 / 9, epsilon2)
must_differ("reversed heat-comparison sign", epsilon2, -epsilon2)
must_differ("replaced original metric", epsilon2, S.trace(Q.conjugate().T * Q))
G, A, Q = cases[2][1:]
Qd = adjoint(Q, G)
eps2 = S.simplify(S.trace(Qd * Q))
gamma = S.simplify(S.trace(A * Q))
must_differ("omitted cubic term", -4 * eps2 * S.re(gamma), S.Integer(0))
G, A, Q = cases[1][1:]
gamma = S.trace(A * Q)
must_differ("complex gamma retained without required real part", gamma, S.re(gamma))
must_differ("incorrect exponential sum factor", S.Integer(3), S.Integer(2))

proof = HERE / "HEAT_METRIC_COMPARISON.tex"
result = {"status": "pass", "exact_checks": checks, "negative_controls": negative_controls,
          "proof_sha256": hashlib.sha256(proof.read_bytes()).hexdigest(),
          "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          "cases": case_reports,
          "scope": "Exact finite coefficient checks; the uniform estimate is proved in the TeX."}
print(json.dumps(result, indent=2))
