"""Exact rational checks for FINITE_PRIME_WINDOW_EXTENSION.md.

No floating arithmetic or zeta-zero samples are used.
The independent finite prime coefficient checker is a separate companion.
"""

from fractions import Fraction as Q
from math import factorial


def exp_upper(x: Q, last: int) -> Q:
    """Taylor sum through last, plus its positive geometric tail bound."""
    assert x >= 0 and x < last + 2
    return (
        sum((x**j / factorial(j) for j in range(last + 1)), Q(0))
        + x ** (last + 1)
        / factorial(last + 1)
        / (1 - x / (last + 2))
    )


def main() -> None:
    width = Q(1, 32)
    radius = Q(1, 64)
    coefficients = (
        Q(1, 4), -Q(1, 48), -Q(1, 32), Q(7, 11520),
        Q(5, 1536), -Q(31, 1935360), -Q(61, 184320),
        Q(127, 309657600), Q(277, 8257536),
    )
    kernel_error = (
        sum((abs(coefficients[j]) * width**j for j in range(1, 9)), Q(0))
        + 2 * (width / 2) ** 9 / (1 - width / 2)
    )
    moment_error = (width / 4) ** 4 / (20 * (1 - width**2 / 32) ** 2)
    total_error = width * kernel_error + (Q(3, 2) + width / 4) * moment_error
    assert total_error == Q(
        71188529564304798199252001,
        3342234102951354835992890572800,
    )
    assert total_error < Q(1, 40000)

    log_lower = Q(23201, 10000)
    assert exp_upper(log_lower, 16) < Q(112, 11)
    log2_lower = 2 * sum(
        (Q(1, (2 * j + 1) * 3 ** (2 * j + 1)) for j in range(4)), Q(0)
    )
    harmonic_256 = sum((Q(1, j) for j in range(1, 257)), Q(0))
    assert harmonic_256 - 8 * log2_lower < Q(29, 50)
    q_lower = Q(3, 2) + log_lower - Q(29, 50) - Q(1, 40000)
    assert q_lower == Q(129603, 40000)
    assert q_lower > Q(81, 25)

    norm_lower = Q(45, 2) / radius**5 + Q(3, 4) / radius**3 + 1 / (32 * radius)
    assert norm_lower == 24159387650
    start = Q(583, 800)
    assert start - width == Q(279, 400) > Q(2, 3)
    assert 1 + Q(4, 3) + Q(4, 3)**2 / 2 > 3
    arch_majorant = 4 * (9 + 55 * Q(1, 3) + 31 * Q(1, 3)**2 + Q(1, 3)**3) / (1 - Q(1, 3))**5
    assert arch_majorant == 936
    assert arch_majorant / norm_lower < Q(1, 2**24)

    assert 256 / (1 - width) == Q(8192, 31) < 265
    coefficient_bound = Q(223, 125)
    whole_bound = coefficient_bound + Q(1, 2**24)
    margin = Q(81, 25) - whole_bound
    assert margin == Q(182, 125) - Q(1, 2**24)
    assert margin > Q(7, 5)
    assert whole_bound < Q(9, 5)

    print("All rational diagonal, mass, archimedean, and interval checks passed.")
    print("Exact profile error:", total_error)
    print("Diagonal coefficient >", q_lower, ">", Q(81, 25))
    print("N >", norm_lower)
    print("R/N < 1/16777216")
    print("Combined coefficient bound:", whole_bound)
    print("Margin below q:", margin)


if __name__ == "__main__":
    main()
