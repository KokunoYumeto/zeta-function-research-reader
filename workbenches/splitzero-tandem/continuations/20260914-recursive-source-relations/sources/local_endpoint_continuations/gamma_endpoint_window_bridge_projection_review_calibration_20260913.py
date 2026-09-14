"""Independent exact EW.51 check through monic remainder kernels.

This computes no Schur block. The original-S quotient is carried through
x=S-1, whose ordered degree-one change of basis has determinant one.
The actual source mass is 9/16 and the actual relation is x*x=2.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import hashlib
import json


def rising(a, j):
    out = 1
    for i in range(j):
        out *= a + i
    return out


def multiply_x(v):
    return (2 * v[1], v[0])


remainders = [(1, 0), (0, 1)]
for j in range(1, 5):
    xpj = multiply_x(remainders[j])
    aprev = j * (j + 7)
    remainders.append(tuple(xpj[i] + aprev * remainders[j - 1][i] for i in range(2)))

mass = F(9, 16)
norms = [mass * factorial(j) * rising(8, j) for j in range(6)]
k00 = k01 = k11 = F(0)
volumes = {}
kernel_records = []
for j, rem in enumerate(remainders):
    k00 += F(rem[0] * rem[0], 1) / norms[j]
    k01 += F(rem[0] * rem[1], 1) / norms[j]
    k11 += F(rem[1] * rem[1], 1) / norms[j]
    det = k00 * k11 - k01 * k01
    if j >= 1:
        if det <= 0:
            raise ArithmeticError("The exact quotient kernel is not positive.")
        volumes[j] = 1 / det
        kernel_records.append(
            {"degree": j, "K_x": [[str(k00), str(k01)], [str(k01), str(k11)]],
             "V_original_S": str(volumes[j])}
        )

expected = {
    (2, 1): (F(30), F(20191, 4860)),
    (2, 2): (F(1320), F(3073295611, 216513000)),
    (3, 2): (F(2640), F(295913127219469, 36104825790000)),
}
checks = []
for (n, r), (expected_u, expected_ratio) in expected.items():
    m = n + r
    u = norms[m] / norms[n]
    ratio = volumes[n - 1] * volumes[n] / (volumes[m - 1] * volumes[m])
    row = {"n": n, "r": r, "U": str(u), "R": str(ratio),
           "U_pass": u == expected_u, "R_pass": ratio == expected_ratio}
    checks.append(row)
    if not row["U_pass"] or not row["R_pass"]:
        raise ArithmeticError(f"EW.51 row failed: {row}")

report = {
    "method": "Exact monic-orthogonal-polynomial quotient remainder kernels; no Schur block.",
    "source_mass": str(mass),
    "reference_mass_retained_in_article": "1/4",
    "original_coordinate": "S=1+iu",
    "quotient_coordinate_map": "(a,b) in (1,x=S-1) maps to (a-b,b) in (1,S), determinant 1",
    "original_relation": "S^2-2S-1",
    "exact_quotient_relation": "x^2=2",
    "orthogonal_polynomial_recurrence": "p_(j+1)=x*p_j+j*(j+7)*p_(j-1)",
    "source_norm": "(9/16)*j!*(8)_j",
    "remainders_in_1_x": remainders,
    "kernel_records": kernel_records,
    "checks": checks,
    "distinct_scalar_checks": 6,
    "all_passed": all(row["U_pass"] and row["R_pass"] for row in checks),
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"all_passed": report["all_passed"], "distinct_scalar_checks": 6,
                  "output": str(output)}, indent=2))
