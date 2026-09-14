"""Exact rational arithmetic for LHT.10--LHT.16; no numeric zero test."""
from fractions import Fraction as F
from math import comb, factorial
import json
from pathlib import Path

terms = [F(16 * comb(4, r) * factorial(r + 2),
           2 ** (r + 3) * 3 ** (r + 1)) for r in range(5)]
assert terms == [F(4, 3), F(8, 3), F(8, 3), F(40, 27), F(10, 27)]
assert sum(terms) == F(230, 27)
exp_partial = sum(F(3 ** j, factorial(j)) for j in range(9))
assert exp_partial == F(89641, 4480) and exp_partial > 20
second_moment_upper = sum(terms) * F(1, 19)
assert second_moment_upper == F(230, 513)
real_part_lower = 1 - F(17, 8) * second_moment_upper
assert real_part_lower == F(97, 2052) and real_part_lower > 0
report = {
    "status": "PASS",
    "scope": "Exact rational arithmetic only; analytic proof is in low_height_theta.tex",
    "inner_sum_terms": [str(x) for x in terms],
    "exponential_partial_sum": str(exp_partial),
    "g_second_derivative_at_1_strict_upper": str(second_moment_upper),
    "g_real_part_closed_rectangle_strict_lower": str(real_part_lower),
    "rectangle": "0 <= Re(s) <= 1, |Im(s)| <= 2",
}
out = Path(__file__).with_name("low_height_theta_exact_checks.json")
out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, indent=2))
