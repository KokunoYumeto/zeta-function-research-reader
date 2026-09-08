# Portable adaptation of secondary/source_check/replay_audit.py
# Only import/output/inventory handling changed; the delimited mathematics is a raw source byte slice.
from __future__ import annotations
from fractions import Fraction
from itertools import combinations
import sympy as s
import sympy as sp
import sympy as S
from portable_common import begin, finish
begin('threshold')
checks = []
# BEGIN UNCHANGED MATHEMATICAL BODY
# Prove the displayed six-decimal rounding without trusting floating-point sqrt.
# For x near alpha0, alpha0>x iff sqrt(7)<(22-9*x)/8.
# Both right-hand sides below are positive, so squaring is equivalent.
lo = Fraction(9266550, 100000000)
hi = Fraction(9266551, 100000000)
lo_root_upper = (22 - 9 * lo) / 8
hi_root_lower = (22 - 9 * hi) / 8
checks.append({"name": "alpha0_exact_enclosure",
               "passed": lo_root_upper > 0 and hi_root_lower > 0
               and lo_root_upper ** 2 > 7 and hi_root_lower ** 2 < 7,
               "interval": [str(lo), str(hi)],
               "six_decimal_rounding": "0.092666"})

# END UNCHANGED MATHEMATICAL BODY
finish('threshold', checks)
