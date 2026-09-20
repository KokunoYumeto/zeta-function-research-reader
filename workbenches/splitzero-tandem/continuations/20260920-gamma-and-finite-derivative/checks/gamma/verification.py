"""Supplemental exact checks for SZ-20260920-056; not a sampled proof."""

from fractions import Fraction as F
from math import comb


def add_term(poly, degree, u_coefficient=0, constant=0):
    old_u, old_c = poly.get(degree, (0, 0))
    poly[degree] = (old_u + u_coefficient, old_c + constant)


def kernel_identity():
    # q=exp(u).  Multiplication is by 3*(q^3-1)*q^2.
    # The first gamma term contributes 3*u*q^3*(q^2+q+1).
    actual = {}
    for degree in (5, 4, 3):
        add_term(actual, degree, 3)
    add_term(actual, 0, 3)
    # Remaining elementary terms contribute (2*u-4)*(q^5-q^2).
    add_term(actual, 5, 2, -4)
    add_term(actual, 2, -2, 4)
    expected = {5: (5, -4), 4: (3, 0), 3: (3, 0),
                2: (-2, 4), 0: (3, 0)}
    assert actual == expected


def exponential_coefficient(n):
    # n! times the coefficient of u^n in the exact E(u).
    value = -4 * 5**n + 4 * 2**n
    if n:
        value += (5 * n * 5**(n-1) + 3 * n * 4**(n-1)
                  + 3 * n * 3**(n-1) - 2 * n * 2**(n-1))
    if n == 1:
        value += 3
    return value


def coefficient_checks():
    assert [exponential_coefficient(n) for n in range(4)] == [0, 0, 0, 108]
    for n in range(2, 513):
        expanded = ((n-4) * 5**n + 3*n*4**(n-1)
                    + 3*n*3**(n-1) + (8-2*n)*2**(n-1))
        grouped = (n-4) * (5**n-2**n) + 3*n*(4**(n-1)+3**(n-1))
        assert exponential_coefficient(n) == expanded == grouped
        if n >= 3:
            assert grouped > 0
    # The proof handles all n>=4 because each grouped summand is nonnegative
    # and the second summand is positive. The loop is only an algebra audit.


def derivative_checks():
    # Elementary part of f: a*t*log(t)+b*log(t)+(c*log(3)+d)*(t-1).
    a, b, c, d = -F(4, 3), -F(2, 3), F(1, 3), F(4, 3)
    # First derivative: a*log(t)+(a+d)+c*log(3)+b/t.
    assert (a, a+d, c, b) == (-F(4, 3), 0, F(1, 3), -F(2, 3))
    # Second derivative: a/t-b/t^2.
    assert (a, -b) == (-F(4, 3), F(2, 3))
    # Gamma chain rule and substitution v=3u both retain exact scale factors.
    assert F(1, 3)**2 == F(1, 9)
    assert F(1, 9) * 3 * 3 == 1


def asymptotic_checks():
    # Each pair is (coefficient of t, constant).
    t_numerator = (1 + F(1, 3), -F(1, 2) + F(7, 6))
    t_denominator = (F(4, 3), 2-F(4, 3))
    assert t_numerator == t_denominator
    three_power = (-F(1, 3)+F(1, 3), -F(7, 6)-F(1, 3))
    e_power = (-1-F(1, 3)+F(4, 3), -F(5, 3)-F(4, 3))
    assert three_power == (0, -F(3, 2))
    assert e_power == (0, -3)
    assert e_power[1] + F(5, 3) == -F(4, 3)


def cutoff_checks():
    assert 2 * 316 == 632
    assert F(88, 7) < 13
    # Integral of the polynomial part in the exact positive pi certificate.
    assert F(1, 7)-F(4, 6)+F(5, 5)-F(4, 3)+4 == F(22, 7)
    # Multiply its polynomial part by (1+v^2), then subtract 4.
    quotient = {6: 1, 5: -4, 4: 5, 2: -4, 0: 4}
    product = {}
    for degree, coefficient in quotient.items():
        for shift in (0, 2):
            product[degree+shift] = product.get(degree+shift, 0) + coefficient
    product[0] -= 4
    assert {d: c for d, c in product.items() if c} == {
        8: 1, 7: -4, 6: 6, 5: -4, 4: 1}
    for j in range(31):
        assert sum(comb(2*j, m) for m in range(2*j+1)) == 4**j
        for m in range(71):
            derivative_factor = comb(2*j, m) if m <= 2*j else 0
            assert derivative_factor <= 4**j
    # r=0 and M=1 both have exponent zero and denominator one.
    assert F(0, 3) == 0 and F(1-1, 3) == 0
    # Exact second derivative coefficients of log Q.
    assert -F(1, 2) * F(1, 3)**2 == -F(1, 18)


if __name__ == "__main__":
    checks = (kernel_identity, coefficient_checks, derivative_checks,
              asymptotic_checks, cutoff_checks)
    for check in checks:
        check()
        print(f"PASS {check.__name__}")
    print("PASS: 5 exact-arithmetic check groups; coefficient audit through degree 512.")
    print("The infinite-domain proof is in proof.tex; no numerical sampling is used.")
