"""Exact finite checks for CF9, CF12--13, CF26, and CF34."""
from pathlib import Path
import hashlib
import json
import math
import sympy as s

x, gamma, zeta2, lp, p = s.symbols("x gamma zeta2 log_pi pi")
count = 0


def need(condition, label):
    global count
    if not condition:
        raise ArithmeticError(label)
    count += 1


def equal(a, b, label):
    need(s.cancel(a-b) == 0, label)


# Retain the distinct original s(s-1), exponential and Gamma Laurent factors.
gamma_laurent = 2/x-gamma+(gamma**2+zeta2)*x/4
pi_taylor = 1-lp*x/2+lp**2*x**2/8
literal_product = s.expand(x*(x-1)*pi_taylor*gamma_laurent)
c0, c1, c2 = [literal_product.coeff(x, j) for j in range(3)]
equal(c0, -2, "CF12 constant")
equal(c1, 2+gamma+lp, "CF12 linear coefficient")
equal(c2, -(gamma+lp+(gamma+lp)**2/4+zeta2/4),
      "CF12 quadratic coefficient")
equal(c1/c0, -1-(gamma+lp)/2, "CF13 logarithmic derivative")
equal(2*c2/c0-(c1/c0)**2, -1+zeta2/4, "CF13 derivative of log derivative")
for n in range(1, 13):
    a = -2*n
    received = a*(a-1)*p**n * 2*(-1)**n/s.Integer(math.factorial(n))
    expected = 4*n*(2*n+1)*(-1)**n*p**n/s.Integer(math.factorial(n))
    equal(received, expected, f"CF9 retained residue factors n={n}")

# Nonconstant complete local units; do not replace a unit by its value.
unit = 2+3*x+5*x*x+7*x**3
h = 11+13*x+17*x*x+19*x**3+23*x**4
for k in [-1, 0, 1]:
    C = x**k*unit
    z = h/C
    au = s.diff(unit, x)/unit
    local_operator = (
        s.diff(z, x, 2)/4+(k/(2*x)+au/2)*s.diff(z, x)
        +(s.Rational(k*(k-1), 4)/x**2+k*au/(2*x)
          +(s.diff(au, x)+au**2)/4)*z)
    equal(local_operator, s.diff(h, x, 2)/(4*C),
          f"CF26 exact stalk operator k={k}")
    log_derivative = s.diff(C, x)/C
    regular = s.series(au, x, 0, 4).removeO()
    for q in range(4):
        A = 29+31*x+sum(s.Integer(37+2*j)/x**j for j in range(1, q+1))
        received = s.residue(A*log_derivative, x, 0)
        expected = 29*k+sum(s.Integer(37+2*j)*regular.coeff(x, j-1)
                            for j in range(1, q+1))
        equal(received, expected, f"CF34 meromorphic test k={k}, pole={q}")

# Signed factor orders and support joins keep both contributors at each zero.
labels = [1, 2, 4, 8, 16]
orders = {"zero": [1, 0, 0, -1, 0],
          "one": [0, 1, 0, 0, -1],
          "negative_even": [0, 0, 0, -1, 1]}
expected_labels = {"zero": 1|8, "one": 2|16, "negative_even": 8|16}
for name, row in orders.items():
    active = 0
    for order, label in zip(row, labels):
        if order:
            active |= label
    need(sum(row) == 0, f"CF39 ordinary order sum {name}")
    need(active == expected_labels[name] and active != 0,
         f"CF39 retained divisor support {name}")

base = Path(__file__).resolve().parent
proof = base/"COMPLETION_FACTOR_FULL_HEAT_MAP.tex"
result = {"status": "passed", "exact_checks": count,
          "proof_sha256": hashlib.sha256(proof.read_bytes()).hexdigest(),
          "scope": "Finite symbolic coefficient, residue, complete-unit operator, "
                   "meromorphic-test and support checks. The all-real-time "
                   "positivity and full divisor statements are proved analytically."}
(base/"COMPLETION_FACTOR_EXACT_CHECKS.json").write_text(
    json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps(result))
