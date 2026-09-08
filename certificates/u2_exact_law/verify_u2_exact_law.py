"""Exact rational cross-checks for the finite Haar U(2) derivative law.

This certificate compares two independently assembled finite calculations:

1. the U(2) Weyl-density Laurent constant term; and
2. the Beta(1/2,3/2) times uniform-circle pushforward model.

It uses only integers and fractions.  It is a check of the finite algebra and
moments, not a substitute for the Jacobian and fibre proof in the TeX corpus.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial
import json
import platform


Exponent = tuple[int, int]
Laurent = dict[Exponent, Fraction]


def multiply(left: Laurent, right: Laurent) -> Laurent:
    out: Laurent = {}
    for (a1, a2), ca in left.items():
        for (b1, b2), cb in right.items():
            exponent = (a1 + b1, a2 + b2)
            out[exponent] = out.get(exponent, Fraction(0)) + ca * cb
    return {exponent: coefficient for exponent, coefficient in out.items() if coefficient}


def power(base: Laurent, exponent: int) -> Laurent:
    out: Laurent = {(0, 0): Fraction(1)}
    factor = dict(base)
    remaining = exponent
    while remaining:
        if remaining & 1:
            out = multiply(out, factor)
        factor = multiply(factor, factor)
        remaining >>= 1
    return out


def reflect(base: Laurent) -> Laurent:
    return {(-a1, -a2): coefficient for (a1, a2), coefficient in base.items()}


def beta_moment(power_r: int) -> Fraction:
    """E[R^n] for R with parameters (1/2,3/2)."""
    out = Fraction(1)
    for j in range(power_r):
        out *= Fraction(2 * j + 1, 2 * (j + 2))
    return out


def circle_cos_even_moment(m: int) -> Fraction:
    """E[cos(phi)^(2m)] for uniform phi."""
    return Fraction(comb(2 * m, m), 4**m)


def model_moment(q: int) -> Fraction:
    """E[(4(1+R-2 sqrt(R) cos(phi)))^q] by a multinomial sum."""
    total = Fraction(0)
    for count_r in range(q + 1):
        for count_cross in range(q - count_r + 1):
            count_one = q - count_r - count_cross
            if count_cross % 2:
                continue
            multinomial = (
                factorial(q)
                // (
                    factorial(count_one)
                    * factorial(count_r)
                    * factorial(count_cross)
                )
            )
            half_cross = count_cross // 2
            coefficient = Fraction(multinomial * ((-2) ** count_cross))
            total += (
                coefficient
                * beta_moment(count_r + half_cross)
                * circle_cos_even_moment(half_cross)
            )
    return Fraction(4**q) * total


def haar_constant_term_moment(q: int) -> Fraction:
    """The normalized U(2) Weyl constant term of |2-z1-z2|^(2q)."""
    derivative: Laurent = {
        (0, 0): Fraction(2),
        (1, 0): Fraction(-1),
        (0, 1): Fraction(-1),
    }
    first_weyl_factor: Laurent = {
        (0, 0): Fraction(1),
        (1, -1): Fraction(-1),
    }
    second_weyl_factor: Laurent = {
        (0, 0): Fraction(1),
        (-1, 1): Fraction(-1),
    }
    integrand = multiply(
        multiply(power(derivative, q), power(reflect(derivative), q)),
        multiply(first_weyl_factor, second_weyl_factor),
    )
    return integrand.get((0, 0), Fraction(0)) / 2


def main() -> None:
    assert beta_moment(0) == 1
    assert beta_moment(1) == Fraction(1, 4)
    rows = []
    for q in range(1, 9):
        model = model_moment(q)
        haar = haar_constant_term_moment(q)
        assert model == haar
        assert model.denominator == 1
        rows.append({"q": q, "moment": model.numerator})
    assert rows[0] == {"q": 1, "moment": 5}
    print(
        json.dumps(
            {
                "status": "pass",
                "arithmetic": "exact rational",
                "python": platform.python_version(),
                "checked_moments": rows,
                "nonclaim": (
                    "The executable checks finite moments from two coordinate "
                    "assemblies; the measure pushforward still uses the written "
                    "Jacobian and fibre proof."
                ),
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )


if __name__ == "__main__":
    main()
