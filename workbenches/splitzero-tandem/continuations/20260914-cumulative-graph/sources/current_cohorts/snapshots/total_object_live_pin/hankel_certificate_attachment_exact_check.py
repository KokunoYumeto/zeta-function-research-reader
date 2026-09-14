"""Read the sealed Hankel certificate using exact rational arithmetic only.

This does not import flint, evaluate theta integrals, or change source inputs.
It writes only its own compact attachment receipt beside this script.
"""
from fractions import Fraction
from pathlib import Path
import argparse
import hashlib
import json
import sys

sys.set_int_max_str_digits(100000)
WORKSPACE = (Path(__file__).resolve().parent / "../../..").resolve()
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument(
    "--input-dir", type=Path,
    default=WORKSPACE / "work/theta_certified_hankel_20260913",
    help="Directory containing the sealed certificate, its source, and exact endpoint receipt.",
)
parser.add_argument(
    "--method-tex", type=Path,
    default=WORKSPACE / "work/tau_theta_hankel_error_control_20260913.tex",
    help="Original TC proof source whose SHA256 is recorded in the receipt.",
)
args = parser.parse_args()
INPUT = args.input_dir.resolve()
METHOD_TEX = args.method_tex.resolve()
OUTPUT = Path(__file__).with_name("HANKEL_FINITE_CERTIFICATE_ATTACHMENT_EXACT.json")
CERTIFICATE = INPUT / "certificate_dimension16_1024.json"
EXPECTED = "869ebacd3f82e46c3fe5fac1f07bcbaae7f4c333e1a5ba2e0ffcb1f91884a0fc"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def endpoint(v):
    denominator = int(v["denominator"])
    assert denominator > 0
    assert denominator & (denominator - 1) == 0
    return Fraction(int(v["numerator"]), denominator)


def interval(v):
    lower, upper = endpoint(v["lower"]), endpoint(v["upper"])
    assert lower <= upper
    return lower, upper


def all_intervals(v):
    if isinstance(v, dict):
        if {"lower", "upper"} <= v.keys():
            interval(v)
            return 1
        return sum(all_intervals(x) for x in v.values())
    if isinstance(v, list):
        return sum(all_intervals(x) for x in v)
    return 0


def fraction_record(v):
    return {"numerator": str(v.numerator), "denominator": str(v.denominator)}


data = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
receipt = json.loads((INPUT / "EXACT_ENDPOINT_RECEIPT.json").read_text())
assert sha(CERTIFICATE) == EXPECTED == receipt["certificate_sha256"]
source_hash = sha(INPUT / "certify_theta_hankel.py")
assert source_hash == data["source_sha256"] == receipt["source_sha256"]
assert data["status"] == "positive_definite_certified"
assert data["dimension"] == 16
assert data["precision_bits"] == 1024 and data["target_bits"] == 850
assert data["first_omitted_n"] == 20 and data["length"] == 4
assert len(data["moments"]) == 33
assert [x["J"] for x in data["moments"]] == list(range(0, 65, 2))
assert len(data["a"]) == 33 and len(data["b"]) == 32
assert interval(data["a"][0])[0] > 0
assert all(len(x["pieces"]) == 8 for x in data["moments"])
assert all(
    Fraction(p["left"]) == Fraction(j, 2)
    and Fraction(p["right"]) == Fraction(j + 1, 2)
    and interval(p["imag"])[0] <= 0 <= interval(p["imag"])[1]
    for m in data["moments"] for j, p in enumerate(m["pieces"])
)
assert all(interval(m["decay_denominator"])[0] > 0 for m in data["moments"])
ordered_intervals = all_intervals(data)
assert ordered_intervals == 1400

matrices = []
for shift, numerator, exponent in [(0, 6, 107), (1, 7, 111)]:
    matrix = data["matrices"][str(shift)]
    rows, lower = matrix["rows"], matrix["L"]
    assert matrix["status"] == "positive_definite_certified"
    assert len(rows) == 16 and [r["dimension"] for r in rows] == list(range(1, 17))
    assert len(lower) == 16 and all(len(row) == 16 for row in lower)
    assert all(interval(row["pivot"])[0] > 0 for row in rows)
    assert all(interval(row["leading_determinant"])[0] > 0 for row in rows)
    assert all(interval(lower[i][j]) == (Fraction(int(i == j)),) * 2
               for i in range(16) for j in range(i, 16))
    absolute = [[max(abs(v) for v in interval(x)) for x in row] for row in lower]
    max_row = max(sum(absolute[i][j] for j in range(i)) for i in range(16))
    max_column = max(sum(absolute[i][j] for i in range(j + 1, 16)) for j in range(16))
    assert max_row < Fraction(1, 64)
    assert max_column < Fraction(1, 64)
    pivot_floor = Fraction(numerator, 10**exponent)
    assert all(interval(row["pivot"])[0] > pivot_floor for row in rows)
    gamma = Fraction(63, 64)**2 * pivot_floor
    matrices.append({
        "shift": shift,
        "strictly_positive_pivots": 16,
        "strictly_positive_leading_determinants": 16,
        "every_pivot_lower_endpoint_strictly_above": fraction_record(pivot_floor),
        "unit_lower_triangular_shape_exact": True,
        "max_off_diagonal_absolute_row_sum_upper": fraction_record(max_row),
        "max_off_diagonal_absolute_column_sum_upper": fraction_record(max_column),
        "both_sums_strictly_below_one_over_64": True,
        "strict_coefficient_norm_squared_lower_multiplier": fraction_record(gamma),
    })

result = {
    "status": "PASS",
    "scope": "Exact endpoint/provenance/triangular norm comparisons; no theta quadrature or new coefficient/LDL recursion performed.",
    "certificate_sha256": EXPECTED,
    "certificate_source_sha256": source_hash,
    "checker_sha256": sha(Path(__file__)),
    "method_tex_sha256": sha(METHOD_TEX),
    "ordered_dyadic_intervals_checked": ordered_intervals,
    "moment_count": 33,
    "finite_integral_piece_count": 264,
    "a_coefficient_count": 33,
    "b_coefficient_count": 32,
    "original_a0_positive": True,
    "matrices": matrices,
}
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "receipt": str(OUTPUT),
                  "certificate_sha256": EXPECTED,
                  "ordered_dyadic_intervals": ordered_intervals,
                  "positive_pivots": 32, "positive_leading_determinants": 32,
                  "strict_one_over_64_bounds": True,
                  "gamma": [m["strict_coefficient_norm_squared_lower_multiplier"]
                            for m in matrices]}, indent=2))
