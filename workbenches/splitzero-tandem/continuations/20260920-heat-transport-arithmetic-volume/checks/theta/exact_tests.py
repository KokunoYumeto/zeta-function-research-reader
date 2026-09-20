"""Exact algebra checks for SZ-20260920-046.

All finite polynomial roots below are synthetic test data, not asserted
arithmetic zeros. Analytic convergence and Volterra endpoint estimates are
proved in DEBRUIJN_THETA_TRANSPORT.tex, not inferred from these checks.
"""

import sympy as sp


x = sp.symbols("x", positive=True)
s, t, a, b, c, rho, y, ell = sp.symbols("s t a b c rho y ell")
F = sp.Function("F")
D = lambda f: -x * sp.diff(f, x)
S_t = lambda f: s * f + t * sp.diff(f, s) / 2


class CheckFailure(RuntimeError):
    pass


def require(condition, message):
    if not condition:
        raise CheckFailure(str(message))


def zero(expr):
    require(sp.simplify(sp.expand(expr)) == 0, expr)


def expect_failure(label, operation):
    try:
        operation()
    except CheckFailure:
        print("CONTROL REJECTED:", label)
        return
    raise CheckFailure("Incorrect formula was accepted: " + label)


def heat_polynomial(p):
    degree = sp.Poly(p, s).degree()
    return sp.expand(sum((t / 4) ** j * sp.diff(p, s, 2 * j)
                         / sp.factorial(j) for j in range(degree // 2 + 1)))


def polynomial_operator(p, argument, operator):
    coeffs = sp.Poly(p, s).all_coeffs()
    value = 0
    for coefficient in coeffs:
        value = operator(value) + coefficient * argument
    return sp.expand(value)


checks = []

gaussian = sp.exp(-sp.pi * x**2)
psi = (4 * sp.pi**2 * x**4 - 6 * sp.pi * x**2) * gaussian
zero(D(D(gaussian) - gaussian) - psi)
zero(2 * (s / 2) * (s / 2 + 1) - 3 * s / 2 - s * (s - 1) / 2)
checks.append("Original Gaussian polynomial and all Mellin factors")

U = sp.exp(t * sp.log(x)**2 / 4)
zero(U * D(F(x) / U) - D(F(x)) - t * sp.log(x) * F(x) / 2)
Dt = lambda f: D(f) + t * sp.log(x) * f / 2
zero(Dt(Dt(F(x))) - (D(D(F(x))) + t * sp.log(x) * D(F(x))
     - t * F(x) / 2 + t**2 * sp.log(x)**2 * F(x) / 4))
zero(S_t(S_t(F(s))) - (s**2 * F(s) + t * s * sp.diff(F(s), s)
     + t * F(s) / 2 + t**2 * sp.diff(F(s), s, 2) / 4))
checks.append("Euler and Mellin noncommuting squares, including both scalar signs")

zero(t * y**2 / 4 - t * (y + ell)**2 / 4
     + t * y * ell / 2 + t * ell**2 / 4)
y1, y2 = sp.symbols("y1 y2")
zero(t * (y1 + y2)**2 / 2 - t * (y1**2 + y2**2) / 2 - t * y1 * y2)
require(sp.expand(t * (y1 + y2)**2 / 2 - t * (y1**2 + y2**2) / 2) != 0,
        "The tensor square-of-sum error must be nonzero")
checks.append("Theta integer weights and full tensor sum of logarithmic squares")

h = (s - 2)**3 * (s + sp.I)**2
R = 3 + s + s**2
for ratio in [1 + s, R, s**5 - 2 * s + 7]:
    left = heat_polynomial(sp.expand(h * ratio))
    right = polynomial_operator(h, heat_polynomial(ratio), S_t)
    zero(left - right)
unit_inverse = sp.invert(R, h, s)
zero(sp.rem(sp.expand(R * unit_inverse - 1), h, s))
zero(sp.diff(heat_polynomial(sp.expand(h * R)) - h * heat_polynomial(R), t).subs(t, 0)
     - (sp.diff(h, s, 2) * R + 2 * sp.diff(h, s) * sp.diff(R, s)) / 4)
checks.append("Repeated divisor Weyl transport and complete local unit inverse")

q = sp.exp(-sp.pi * (x**2 + x**-2))
f = D(q) - rho * q
zero(sp.diff(x**rho * q, x) + x**(rho - 1) * f)
Va = lambda f: D(f) - a * f
Vb = lambda f: D(f) - b * f
zero(Va(Vb(q)) - Vb(Va(q)))
checks.append("Volterra integrating-factor sign and repeated-factor order independence")

# Original physical normalization: dx/x=2du, Phi_D=4Phi_RT,
# and the full-line transform of an even function is twice its cosine integral.
require(2 * 4 * 2 == 16, "Rodgers--Tao factor must be 16")
require(sp.Rational(1, 2) * 16 == 8, "Xi-to-Rodgers--Tao factor must be 8")
zero(sp.Rational(1, 4) * (2 / sp.I)**2 + 1)
checks.append("Rodgers--Tao factor 16, xi factor 8, and backward heat sign")

# A two-root selected packet of a three-root polynomial times a nonconstant
# zero-free entire factor. Its exterior term includes the third root and 2.
g0 = sp.exp(2 * s) * s * (s - 1) * (s - 3)
selected = [sp.Integer(0), sp.Integer(1)]
external_b = 2 + 1 / (s - 3)
velocities = []
for root in selected:
    velocity = -sp.diff(g0, s, 2).subs(s, root) / (4 * sp.diff(g0, s).subs(s, root))
    internal = sum(1 / (root - other) for other in selected if other != root)
    zero(velocity + (internal + external_b.subs(s, root)) / 2)
    velocities.append(velocity)
for power in range(1, 9):
    test = s**power
    fp = sp.diff(test, s)
    direct = sum(fp.subs(s, root) * velocity for root, velocity in zip(selected, velocities))
    paired = -(fp.subs(s, 0) - fp.subs(s, 1)) / (2 * (0 - 1))
    exterior = -sum(fp.subs(s, root) * external_b.subs(s, root) for root in selected) / 2
    zero(direct - paired - exterior)
checks.append("Simple selected-packet root and paired trace formulas with full exterior")

# Repeated roots: direct residues independently check the contour formula.
g_multiple = sp.exp(2 * s) * s**2 * (s - 1)**3 * (s - 3)
packet = [(sp.Integer(0), 2), (sp.Integer(1), 3)]
for power in range(1, 9):
    test = s**power
    fp = sp.diff(test, s)
    fpp = sp.diff(test, s, 2)
    contour = -sum(sp.residue(fp * sp.diff(g_multiple, s, 2) / g_multiple, s, root)
                   for root, mult in packet) / 4
    diagonal = -sum(mult * (mult - 1) * fpp.subs(s, root) for root, mult in packet) / 4
    cross = -sp.Rational(2 * 3, 2) * (fp.subs(s, 0) - fp.subs(s, 1)) / (0 - 1)
    exterior = -sum(mult * fp.subs(s, root) * external_b.subs(s, root)
                    for root, mult in packet) / 2
    zero(contour - diagonal - cross - exterior)
checks.append("Repeated-root contour traces, multiplicities, and retained exterior ratio")

# Exact finite Gram test with a nontrivial kernel. These matrices are synthetic.
E = sp.Matrix([[1, 0, 1], [0, 1, 2]])
K0 = sp.diag(3, 2, 5)
Kprime = sp.Matrix([[5, 1, 0], [1, 4, 1], [0, 1, 3]])
K = K0 + t * Kprime
Gt = (E * K.inv() * E.T).inv()
G0 = (E * K0.inv() * E.T).inv()
lift = K0.inv() * E.T * G0
require(E * lift == sp.eye(2), "The attained lift must be a right inverse")
require(sp.simplify(lift.T * K0 * lift - G0) == sp.zeros(2),
        "The lift must retain the original Gram matrix")
require(sp.simplify(Gt.diff(t).subs(t, 0) - lift.T * Kprime * lift) == sp.zeros(2),
        "The quotient metric derivative must equal the lifted derivative")
checks.append("Attained finite quotient metric, exact lift, and first metric derivative")

# Tensor collision exponents are maxima, not sums of colliding exponents.
roots_orders = [(0, 2), (1, 1)]
exponents = {}
for r1, m1 in roots_orders:
    for r2, m2 in roots_orders:
        exponents[r1 + r2] = max(exponents.get(r1 + r2, 0), 1 + m1 - 1 + m2 - 1)
require(exponents == {0: 3, 1: 2, 2: 1}, "Collision exponents must use the maximum")
require(sum(exponents.values()) == 6, "The cyclic tensor dimension must be 6")
require(sum(m for r, m in roots_orders)**2 == 9, "The full tensor dimension must be 9")
checks.append("Exact sum-collision cyclic exponents versus full tensor dimension")

# Deliberately wrong formulas must fail in both ordinary and optimized Python.
expect_failure("wrong forward-heat sign",
               lambda: zero(heat_polynomial(s**2) - (s**2 - t / 2)))
expect_failure("wrong heat coefficient 1/2 in place of 1/4",
               lambda: zero(heat_polynomial(s**2) - (s**2 + t)))
expect_failure("wrong Rodgers--Tao factor 8 in place of 16",
               lambda: require(2 * 4 * 2 == 8, "Missing whole-line factor 2"))
expect_failure("omitted exterior term in selected-packet velocity",
               lambda: zero(velocities[0] + sp.Rational(1, 2) / (selected[0] - selected[1])))
checks.append("Four deliberate heat-factor, heat-sign, and exterior-omission controls")

for check in checks:
    print("PASS:", check)
print(f"PASS: {len(checks)} exact check groups; no arithmetic zero approximation used.")
