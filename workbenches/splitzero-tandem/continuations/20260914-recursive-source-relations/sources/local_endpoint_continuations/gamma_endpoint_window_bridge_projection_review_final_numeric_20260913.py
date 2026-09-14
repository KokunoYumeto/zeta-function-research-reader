"""Read-only independent checks of the final EW.57--59 displayed data.

Permutation determinants and local Gauss--Jordan inversion are implemented here.
No parent checker is imported or replayed. This checks final displayed numbers,
not the complete coefficient-box propagation or any arithmetic-source input.
"""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import hashlib
import json

BASE = Path(__file__).parent
SOURCE = BASE / "gamma_endpoint_window_bridge_20260913.tex"
RECEIPT = BASE / "gamma_endpoint_window_bridge_supplement_20260913.json"
SOURCE_HASH = "e8d6152532c98532a062b5840834d934b28f29490ec926f47c2bce1af3493854"
RECEIPT_HASH = "d6c5bb0d01fc2950f875e7924f2999cc180d4dbac1f4d4e1272a851f23e43640"
rows = []


def check(label, condition):
    rows.append({"label": label, "passed": bool(condition)})
    if not condition:
        raise ArithmeticError(label)


def transpose(a):
    return [list(x) for x in zip(*a)]


def product(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def determinant(a):
    n = len(a)
    value = F(0)
    for p in permutations(range(n)):
        inversions = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        term = F((-1) ** inversions)
        for i in range(n):
            term *= a[i][p[i]]
        value += term
    return value


def inverse(a):
    n = len(a)
    z = [list(a[i]) + [F(i == j) for j in range(n)] for i in range(n)]
    for i in range(n):
        pivot_row = next(j for j in range(i, n) if z[j][i])
        z[i], z[pivot_row] = z[pivot_row], z[i]
        pivot = z[i][i]
        z[i] = [v / pivot for v in z[i]]
        for j in range(n):
            if j != i:
                factor = z[j][i]
                z[j] = [z[j][k] - factor * z[i][k] for k in range(2 * n)]
    return [row[n:] for row in z]


check("source pin", hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_HASH)
check("supplement pin", hashlib.sha256(RECEIPT.read_bytes()).hexdigest() == RECEIPT_HASH)
receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
jobs = [job for job in receipt["jobs"] if job["mutant"] is None and not job["optimized"]]
check("one normal unchanged job", len(jobs) == 1)
pipeline = jobs[0]["result"]["coefficient_pipeline"]
check("normal unchanged job passed", jobs[0]["returncode"] == 0)

h_int = [[9, 9, -63, -207], [9, 81, 81, -1863],
         [-63, 81, 2025, 2025], [-207, -1863, 2025, 93393]]
h0 = [[F(v, 16) for v in row] for row in h_int]
inverse_int = [[8019, -1863, 351, -27], [-1863, 1501, -147, 29],
               [351, -147, 39, -3], [-27, 29, -3, 1]]
h0_inverse = [[F(v, 2430) for v in row] for row in inverse_int]
identity = product(h0, h0_inverse)
for i in range(4):
    for j in range(4):
        check(f"EW58 inverse product ({i},{j})", identity[i][j] == F(i == j))
trace = sum(h0_inverse[i][i] for i in range(4))
check("EW58 inverse trace exact", trace == F(956, 243))
check("EW58 inverse trace below four", trace < 4)
check("EW57 central matrix agrees", h0 == [[F(v) for v in row] for row in pipeline["H_center"]])

epsilon = F(1, 10**12)
delta = [54 * epsilon + 28 * epsilon**2,
         F(1029, 2) * epsilon + F(873, 2) * epsilon**2,
         F(2109, 2) * epsilon + F(1773, 2) * epsilon**2,
         29754 * epsilon + 32878 * epsilon**2]
for i, value in enumerate(delta):
    check(f"EW57 diagonal ({i}) equals receipt", value == F(pipeline["delta_diagonal"][i]))
    check(f"EW58 diagonal ({i}) positive and below 10^-6", 0 < value < F(1, 10**6))

h_minus = [[h0[i][j] - (delta[i] if i == j else 0) for j in range(4)] for i in range(4)]
h_plus = [[h0[i][j] + (delta[i] if i == j else 0) for j in range(4)] for i in range(4)]
check("EW58 lower matrix agrees", h_minus == [[F(v) for v in row] for row in pipeline["H_lower"]])
check("EW58 upper matrix agrees", h_plus == [[F(v) for v in row] for row in pipeline["H_upper"]])

j_all = [[F(1), F(0), F(1), F(2)], [F(0), F(1), F(2), F(5)]]


def source_data(h):
    source_dets = [F(1)] + [determinant([row[:j] for row in h[:j]]) for j in range(1, 5)]
    omega = {n: source_dets[n + 1] / source_dets[n] for n in (2, 3)}
    volumes = {}
    for n in (1, 2, 3):
        hn = [row[:n + 1] for row in h[:n + 1]]
        jn = [row[:n + 1] for row in j_all]
        kernel = product(product(jn, inverse(hn)), transpose(jn))
        volumes[n] = 1 / determinant(kernel)
    return omega, volumes


omega_minus, v_minus = source_data(h_minus)
omega_plus, v_plus = source_data(h_plus)
u_minus = omega_minus[3] / omega_plus[2]
u_plus = omega_plus[3] / omega_minus[2]
r_minus = v_minus[1] * v_minus[2] / (v_plus[2] * v_plus[3])
r_plus = v_plus[1] * v_plus[2] / (v_minus[2] * v_minus[3])
endpoints = pipeline["endpoint_data"]
check("EW59 lower U independently computed", u_minus == F(endpoints["lower"]["U"]))
check("EW59 upper U independently computed", u_plus == F(endpoints["upper"]["U"]))
check("EW59 lower R independently computed", r_minus == F(endpoints["lower"]["R"]))
check("EW59 upper R independently computed", r_plus == F(endpoints["upper"]["R"]))
check("EW59 monotone corner domain", 0 < u_minus <= u_plus and 1 < r_minus <= r_plus)

for name in ("lower", "actual", "upper"):
    data = endpoints[name]
    u, ratio = F(data["U"]), F(data["R"])
    radicals = (u * ratio, u / ratio)
    roots = [[F(v) for v in pair] for pair in data["root_intervals"]]
    for j, ((lo, hi), radicand) in enumerate(zip(roots, radicals)):
        check(f"EW59 {name} root {j} positive ordered", 0 < lo < hi)
        check(f"EW59 {name} root {j} lower power", lo * lo <= radicand)
        check(f"EW59 {name} root {j} upper power", radicand <= hi * hi)
    recorded = [F(v) for v in data["endpoint_interval"]]
    check(f"EW59 {name} interval lower reconstruction", recorded[0] == (roots[0][0] - roots[1][1]) / 2)
    check(f"EW59 {name} interval upper reconstruction", recorded[1] == (roots[0][1] - roots[1][0]) / 2)

displayed = [F(10247872526420120792621067, 2**81),
             F(10247872551311149445602506, 2**81)]
recorded = [F(v) for v in pipeline["final_endpoint_interval"]]
check("EW59 lower displayed dyadic", displayed[0] == recorded[0])
check("EW59 upper displayed dyadic", displayed[1] == recorded[1])
check("EW59 final corner lower", displayed[0] == F(endpoints["lower"]["endpoint_interval"][0]))
check("EW59 final corner upper", displayed[1] == F(endpoints["upper"]["endpoint_interval"][1]))
actual = [F(v) for v in endpoints["actual"]["endpoint_interval"]]
check("EW59 interior interval strictly enclosed", displayed[0] < actual[0] < actual[1] < displayed[1])

report = {
    "source_sha256": SOURCE_HASH,
    "supplement_sha256": RECEIPT_HASH,
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "scope": "Final EW.57 inverse/trace, EW.58 diagonal bounds and matrices, EW.59 rational corners and root endpoints. No replay of the parent suite.",
    "checks": rows,
    "check_count": len(rows),
    "provenance_and_run_selection_checks": 4,
    "mathematical_checks": len(rows) - 4,
    "all_passed": all(row["passed"] for row in rows),
}
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: report[k] for k in ("check_count", "mathematical_checks", "provenance_and_run_selection_checks", "all_passed")}))
