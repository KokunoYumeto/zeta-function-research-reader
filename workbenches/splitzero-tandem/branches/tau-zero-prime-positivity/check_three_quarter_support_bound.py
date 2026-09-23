"""Exact rational checks for TQ1--TQ48 and the subsequent FC support bound."""

from fractions import Fraction as Q
from hashlib import sha256
from json import dumps
from math import factorial
from pathlib import Path


def series_coefficients():
    # e^(z/2) / (sinh(z)/z), then subtract 1 and divide by 2z.
    numerator = [Q(1, 2**n * factorial(n)) for n in range(10)]
    denominator = [
        Q(1, factorial(n + 1)) if n % 2 == 0 else Q(0)
        for n in range(10)
    ]
    quotient = []
    for n in range(10):
        quotient.append(
            numerator[n]
            - sum(denominator[j] * quotient[n - j] for j in range(1, n + 1))
        )
    assert quotient[0] == 1
    return [quotient[n + 1] / 2 for n in range(9)]


COEFFICIENTS = [
    Q(1, 4), -Q(1, 48), -Q(1, 32), Q(7, 11520), Q(5, 1536),
    -Q(31, 1935360), -Q(61, 184320), Q(127, 309657600),
    Q(277, 8257536),
]
assert series_coefficients() == COEFFICIENTS


def remainder_bound(width):
    return (
        sum(abs(COEFFICIENTS[j]) * width**j for j in range(1, 9))
        + 2 * (width / 2)**9 / (1 - width / 2)
    )


def exp_partial(value, last_index):
    return sum(value**j / factorial(j) for j in range(last_index + 1))


def report():
    small = Q(3, 4)
    extended = Q(19, 25)
    small_remainder = remainder_bound(small)
    assert small_remainder == Q(52650683261, 1503238553600)
    assert small_remainder < Q(9, 250)
    assert Q(9, 250) - small_remainder == Q(7329523343, 7516192768000)

    small_moment = (small / 4)**4 * Q(33, 32)**2 / 20
    assert small_moment == Q(88209, 1342177280)
    assert small_moment < Q(1, 15000)
    assert small / 4 * Q(1, 15000) == Q(1, 80000)
    assert Q(205, 243)**2 > Q(7, 11)

    log2_lower = 2 * sum(Q(1, (2*j + 1) * 3**(2*j + 1)) for j in range(4))
    assert log2_lower == Q(53056, 76545)
    harmonic = sum(Q(1, j) for j in range(1, 257))
    assert harmonic < Q(612435, 100000)
    gamma_upper = Q(612435, 100000) - 8 * log2_lower
    assert gamma_upper == Q(177361483, 306180000)
    assert gamma_upper < Q(29, 50)
    assert exp_partial(Q(43, 50), 7) - Q(33, 14) == Q(
        1126807544917, 187500000000000
    )
    assert exp_partial(Q(7, 10), 3) > 2

    small_constant = Q(3, 2) - Q(36, 25) - Q(27, 1000) - Q(1, 10000) - Q(1, 80000)
    assert small_constant == Q(2631, 80000) > Q(1, 32)

    extended_remainder = remainder_bound(extended)
    assert extended_remainder == Q(
        4199809019840292631, 117180000000000000000
    )
    assert extended_remainder < Q(9, 250)
    extended_moment = (extended / 4)**4 * Q(33, 32)**2 / 20
    assert extended_moment == Q(141919569, 2048000000000)
    assert (Q(3, 2) + extended / 4) * extended_moment < Q(1, 8000)
    assert 1 / (1 - (extended / 4)**2 / 2) < Q(33, 32)
    assert Q(1261, 1539)**2 > Q(7, 11)
    assert Q(22, 7) * extended == Q(418, 175)
    assert exp_partial(Q(7, 8), 6) > Q(418, 175)
    extended_constant = Q(3, 2) - Q(291, 200) - Q(171, 6250) - Q(1, 8000)
    assert extended_constant == Q(3503, 200000) > Q(1, 64)
    stronger_constant = Q(3, 2) - Q(109, 75) - Q(171, 6250) - Q(1, 8000)
    assert stronger_constant > extended_constant
    assert Q(25, 36) + Q(1, 16) < extended
    assert exp_partial(Q(25, 36), 4) > 2

    return {
        "arithmetic": "exact fractions only",
        "kernel_coefficients": [str(x) for x in COEFFICIENTS],
        "three_quarter": {
            "width": str(small),
            "kernel_remainder": str(small_remainder),
            "moment_bound": str(small_moment),
            "coercivity": str(small_constant),
            "margin_above_1_over_32": str(small_constant - Q(1, 32)),
        },
        "nineteen_twenty_fifths": {
            "width": str(extended),
            "kernel_remainder": str(extended_remainder),
            "moment_bound": str(extended_moment),
            "coercivity": str(extended_constant),
            "margin_above_1_over_64": str(extended_constant - Q(1, 64)),
            "stronger_scalar_route": str(stronger_constant),
        },
        "gamma_rational_upper": str(gamma_upper),
    }


if __name__ == "__main__":
    result = report()
    source = Path(__file__).with_name("INCOMING_PACKET_SOURCE.md")
    if source.exists():
        digest = sha256(source.read_bytes()).hexdigest()
        assert digest == "d3b1ac08c71f6104cfe011ba5e5b86f6fbe182916c0b0270511671b1f7165d5b"
        result["incoming_source_sha256"] = digest
    print(dumps(result, indent=2))
