"""Exact rational certificate for the original width 1/32 prime-power window.

Uses integer arithmetic, Fraction, and integer square roots only.
No floating-point transcendental value enters a comparison.
"""

from fractions import Fraction as Q
from math import isqrt
from pathlib import Path
import json


OUT = Path(__file__).resolve().parent
LOG_DEN = 10**12
SQRT_DEN = 10**9
TERMS = 16


def floorq(x):
    return x.numerator // x.denominator


def ceilq(x):
    return -((-x.numerator) // x.denominator)


def atanh_log_bounds(z):
    assert Q(0) <= z <= Q(1, 3)
    lower = 2 * sum((z ** (2*j+1) / (2*j+1) for j in range(TERMS)), Q(0))
    remainder = 2 * z ** (2*TERMS+1) / ((2*TERMS+1)*(1-z*z))
    return lower, lower + remainder


LOG2_LO, LOG2_HI = atanh_log_bounds(Q(1, 3))


def log_bounds(p):
    k = p.bit_length() - 1
    z = Q(p - 2**k, p + 2**k)
    lo, hi = atanh_log_bounds(z)
    lo += k*LOG2_LO
    hi += k*LOG2_HI
    return Q(floorq(LOG_DEN*lo), LOG_DEN), Q(ceilq(LOG_DEN*hi), LOG_DEN)


def sqrt_bounds(n):
    root = isqrt(n*SQRT_DEN**2)
    lo = Q(root, SQRT_DEN)
    hi = lo if root*root == n*SQRT_DEN**2 else Q(root+1, SQRT_DEN)
    assert lo*lo <= n <= hi*hi
    return lo, hi


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


# Analytic range and ratio bounds are proved in the companion Markdown.
# These are their exact final rational comparisons.
assert Q(25, 36) < Q(279, 400)
assert Q(256*32, 31) < 265
assert Q(16, 15) == 1/(1-Q(1, 16))

prime_powers = {}
for p in range(2, 265):
    if is_prime(p):
        n = p
        while n <= 264:
            assert n not in prime_powers
            prime_powers[n] = p
            n *= p

assert len(prime_powers) == 72
assert prime_powers[257] == 257
assert prime_powers[263] == 263
assert prime_powers[256] == 2
assert prime_powers[243] == 3

weights = {}
rows = []
for n, p in sorted(prime_powers.items()):
    log_lo, log_hi = log_bounds(p)
    sqrt_lo, sqrt_hi = sqrt_bounds(n)
    weight_lo, weight_hi = log_lo/sqrt_hi, log_hi/sqrt_lo
    weights[n] = weight_lo, weight_hi
    rows.append({
        "n": n, "prime_base": p,
        "log_lower": str(log_lo), "log_upper": str(log_hi),
        "sqrt_lower": str(sqrt_lo), "sqrt_upper": str(sqrt_hi),
        "weight_lower": str(weight_lo), "weight_upper": str(weight_hi),
    })

window_rows = []
for m in sorted(prime_powers):
    if m == 2:  # Excluded by log 2 < 279/400 = 583/800 - 1/32.
        continue
    indices = [n for n in sorted(prime_powers) if m <= n and 15*n < 16*m]
    lower = sum((weights[n][0] for n in indices), Q(0))
    upper = sum((weights[n][1] for n in indices), Q(0))
    window_rows.append({
        "minimum": m, "indices": indices,
        "lower": str(lower), "upper": str(upper),
        "upper_numerator_over_1e9": ceilq(10**9*upper),
    })
    if m != 227:
        assert upper < Q(1511, 1000)

star = [227, 229, 233, 239, 241]
star_row = next(row for row in window_rows if row["minimum"] == 227)
assert star_row["indices"] == star
star_lower = Q(star_row["lower"])
star_upper = Q(star_row["upper"])
assert Q(1783796, 10**6) < star_lower
assert star_upper < Q(1783797, 10**6) < Q(223, 125) < 2
assert Q(1783796246, 10**9) < star_lower
assert star_upper < Q(1783796247, 10**9)
assert Q(1511, 1000) < star_lower

# Feasibility of the true logarithmic window centered at
# a* = (log 227 + log 241)/2, rather than only the ratio superset.
assert Q(14, 227) < Q(1, 16)
assert 227*241 < 256**2
assert Q(4, 3) > Q(583, 800)

certificate = {
    "domain": {"a_lower": "583/800", "a_upper": "log(256)", "half_width": "1/32"},
    "method": "Exact integer and rational arithmetic; 16-term atanh logarithm enclosure and integer-square-root enclosure.",
    "prime_power_count_through_264": len(prime_powers),
    "admissible_minimum_count": len(window_rows),
    "exact_maximizing_indices": star,
    "exact_maximum": "sum(log(p)/sqrt(p) for p in [227,229,233,239,241])",
    "maximum_lower": str(star_lower),
    "maximum_upper": str(star_upper),
    "short_maximum_enclosure": ["1783796246/1000000000", "1783796247/1000000000"],
    "short_uniform_upper_bound": "223/125",
    "all_other_superset_packets_upper_bound": "1511/1000",
    "weights": rows,
    "ratio_superset_packets": window_rows,
    "status": "all_exact_assertions_passed",
}
(OUT/"FINITE_PRIME_WINDOW_COEFFICIENT_CERTIFICATE.json").write_text(
    json.dumps(certificate, indent=2) + "\n", encoding="utf-8")

table = ["| Minimum prime power | All prime powers in its ratio superset | Upper numerator over $10^9$ |",
         "|---:|:---|---:|"]
for row in window_rows:
    table.append(f"| {row['minimum']} | {', '.join(map(str,row['indices']))} | {row['upper_numerator_over_1e9']} |")
(OUT/"FINITE_PRIME_WINDOW_PACKETS.md").write_text(
    "# Exact rational packet table\n\n"
    "Each upper bound is the displayed integer divided by $10^9$. "
    "It is an outward rounding of the exact upper fraction in the companion JSON.\n\n"
    + "\n".join(table) + "\n", encoding="utf-8")

print(json.dumps({
    "status": certificate["status"],
    "prime_powers": len(prime_powers),
    "packets": len(window_rows),
    "maximizer": star,
    "certified_enclosure": certificate["short_maximum_enclosure"],
    "uniform_bound": certificate["short_uniform_upper_bound"],
}, indent=2))
