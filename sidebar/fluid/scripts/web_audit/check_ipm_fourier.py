# Portable adaptation of ipm/commutator/fourier_check/replay.py
# Only import/output/inventory handling changed; the delimited mathematics is a raw source byte slice.
from __future__ import annotations
from fractions import Fraction
from itertools import combinations
import sympy as s
import sympy as sp
import sympy as S
from portable_common import begin, finish
begin('ipm_fourier')
# BEGIN UNCHANGED MATHEMATICAL BODY
q, sigma = sp.symbols("q sigma", real=True)
I = sp.I
zero = (0, 0)
checks: list[dict] = []


def clean(poly):
    return {k: sp.expand(v) for k, v in poly.items() if sp.expand(v) != 0}


def add(*polys):
    out = {}
    for poly in polys:
        for k, value in poly.items():
            out[k] = out.get(k, 0) + value
    return clean(out)


def scale(poly, scalar):
    return clean({k: scalar * value for k, value in poly.items()})


def multiply(left, right):
    out = {}
    for k, a in left.items():
        for ell, b in right.items():
            j = (k[0] + ell[0], k[1] + ell[1])
            out[j] = out.get(j, 0) + a * b
    return clean(out)


def derivative(poly, coordinate):
    return clean({k: I * k[coordinate] * value for k, value in poly.items()})


def heat(poly):
    return clean({k: q ** (k[0] ** 2 + k[1] ** 2) * v for k, v in poly.items()})


def velocity(poly):
    components = ({}, {})
    for k, value in poly.items():
        if k == zero:
            continue
        square = k[0] ** 2 + k[1] ** 2
        components[0][k] = sigma * sp.Rational(k[0] * k[1], square) * value
        components[1][k] = -sigma * sp.Rational(k[0] ** 2, square) * value
    return tuple(clean(c) for c in components)


def pressure(poly):
    return clean({k: I * sigma * sp.Rational(k[1], k[0] ** 2 + k[1] ** 2) * v
                  for k, v in poly.items() if k != zero})


def transport(poly):
    v = velocity(poly)
    return add(multiply(v[0], derivative(poly, 0)),
               multiply(v[1], derivative(poly, 1)))


def sine(k, amplitude):
    return {k: amplitude / (2 * I), (-k[0], -k[1]): -amplitude / (2 * I)}


def assert_equal(name, actual, expected):
    difference = add(actual, scale(expected, -1))
    assert not difference, (name, difference)
    checks.append({"name": name, "passed": True,
                   "compared_modes": [list(k) for k in sorted(set(actual) | set(expected))]})


def evaluate_at(poly, x1, x2):
    return sp.expand_complex(sum(v * sp.exp(I * (k[0] * x1 + k[1] * x2))
                                 for k, v in poly.items())).expand()


def serial(poly):
    return [{"k": list(k), "coefficient": str(value)} for k, value in sorted(poly.items())]


rho = {(1, 0): sp.Rational(1, 2), (-1, 0): sp.Rational(1, 2),
       (1, 1): sp.Rational(1, 2), (-1, -1): sp.Rational(1, 2)}
v = velocity(rho)
p = pressure(rho)
expected_n = add(sine((2, 1), sigma / 4), sine((0, 1), 3 * sigma / 4))
expected_c = add(sine((2, 1), sigma * (q ** 3 - q ** 5) / 4),
                 sine((0, 1), 3 * sigma * (q ** 3 - q) / 4))
n = transport(rho)
rho_s = heat(rho)
v_s = velocity(rho_s)
n_s = transport(rho_s)
c = add(n_s, scale(heat(n), -1))

assert_equal("Darcy first component", v[0], scale(derivative(p, 0), -1))
assert_equal("Darcy second component", v[1],
             add(scale(derivative(p, 1), -1), scale(rho, -sigma)))
assert_equal("Original divergence", add(derivative(v[0], 0), derivative(v[1], 1)), {})
assert_equal("Transport coefficient identity", n, expected_n)
assert_equal("Heat and velocity commute, first component", v_s[0], heat(v[0]))
assert_equal("Heat and velocity commute, second component", v_s[1], heat(v[1]))
assert_equal("Transformed Darcy first component", v_s[0], scale(derivative(heat(p), 0), -1))
assert_equal("Transformed Darcy second component", v_s[1],
             add(scale(derivative(heat(p), 1), -1), scale(rho_s, -sigma)))
assert_equal("Transformed divergence", add(derivative(v_s[0], 0), derivative(v_s[1], 1)), {})
assert_equal("Heat transport is q cubed times original transport", n_s, scale(n, q ** 3))
assert_equal("Explicit defect coefficient identity", c, expected_c)
assert_equal("Stationary transformed forcing identity", add(heat(n), c), n_s)
flux = tuple(add(multiply(rho_s, v_s[j]), scale(heat(multiply(rho, v[j])), -1))
             for j in range(2))
assert_equal("Defect equals divergence of exact flux",
             add(derivative(flux[0], 0), derivative(flux[1], 1)), c)
assert_equal("Defect has zero spatial mean", {zero: c.get(zero, 0)}, {})
assert_equal("Defect at s=0 vanishes", {k: z.subs(q, 1) for k, z in c.items()}, {})
assert_equal("Defect at sigma=0 vanishes", {k: z.subs(sigma, 0) for k, z in c.items()}, {})
point_value = evaluate_at(c, sp.pi / 4, 0)
assert_equal("Exact point evaluation at (pi/4,0)", {zero: point_value},
             {zero: sigma * (q ** 3 - q ** 5) / 4})
assert_equal("Point value factorization", {zero: point_value},
             {zero: sigma * q ** 3 * (1 - q ** 2) / 4})
assert_equal("Coefficient sigma=1 specialization",
             {k: z.subs(sigma, 1) for k, z in c.items()},
             add(sine((2, 1), (q ** 3 - q ** 5) / 4),
                 sine((0, 1), 3 * (q ** 3 - q) / 4)))
assert_equal("Coefficient sigma=2*pi specialization",
             {k: z.subs(sigma, 2 * sp.pi) for k, z in c.items()},
             scale({k: z.subs(sigma, 1) for k, z in c.items()}, 2 * sp.pi))

# END UNCHANGED MATHEMATICAL BODY
finish('ipm_fourier', checks)
