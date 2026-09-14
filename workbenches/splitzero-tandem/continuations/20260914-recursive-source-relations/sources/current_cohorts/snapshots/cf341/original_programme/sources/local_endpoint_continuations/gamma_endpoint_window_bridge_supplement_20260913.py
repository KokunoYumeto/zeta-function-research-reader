"""Separate exact supplement to the immutable 416-check window fixture.

Checks EW.21 directly and runs a coefficient-box -> original-S Gram ->
positive matrix -> q-dimensional quotient -> endpoint certificate.
All mathematical operations use Fraction or integers.  --replay saves
ordinary/-O executions and genuine changed-formula rejections.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from math import comb, factorial
from pathlib import Path
import subprocess
import sys

DIRECTORY = Path(__file__).resolve().parent
CORE = DIRECTORY / "gamma_endpoint_window_bridge_fixture_20260913.py"
SAVED = CORE.with_suffix(".json")
CORE_SHA = "56be6cbd66ffd5272440e95f01104a0154bf0c4b5a2bab1d0a60cb7945071048"
SAVED_SHA = "07fb09d0783800245214ec00f06206104f2e46e37a3b45ba2594c36903a35609"
spec = importlib.util.spec_from_file_location("immutable_window_fixture", CORE)
f = importlib.util.module_from_spec(spec)
spec.loader.exec_module(f)
EPSILON = Q(1, 10**12)
MUTANTS = ("paired_prefix_power", "paired_first_power", "omit_quadratic_radius", "coefficient_mass")


def rational_matrix(a):
    return [[Q(x) for x in row] for row in a]


def polynomial_product(a, b, degree=6):
    result = [Q(0)]*(degree+1)
    for j, x in enumerate(a):
        for k, y in enumerate(b):
            if j+k <= degree:
                result[j+k] += x*y
    return result


def gamma_polynomials(beta=4, degree=6):
    polys = [[Q(1)], [Q(0), Q(1)]]
    for j in range(1, degree):
        following = [Q(0)]+polys[j]
        for ell, value in enumerate(polys[j-1]):
            following[ell] -= j*(j+beta-1)*value
        polys.append(following)
    return polys[:degree+1]


def test_polynomial(a, b):
    real, imaginary = [Q(0)]*7, [Q(0)]*7
    for ell in range(a+1):
        for j in range(b+1):
            term = Q(comb(a, ell)*comb(b, j)*(-1)**ell)
            degree = ell+j
            if degree % 4 == 0:
                real[degree] += term
            elif degree % 4 == 1:
                imaginary[degree] += term
            elif degree % 4 == 2:
                real[degree] -= term
            else:
                imaginary[degree] -= term
    return real, imaginary


def expand_monic(poly, basis):
    remainder, result = poly[:], [Q(0)]*7
    for j in reversed(range(7)):
        result[j] = remainder[j]
        for ell, value in enumerate(basis[j]):
            remainder[ell] -= result[j]*value
    return result, remainder


def source_from_ab(a, b):
    reference = f.gamma_moments(2, Q(1, 2), 8)
    weighted = [a*reference[j]+b*reference[j+2] for j in range(7)]
    summed = f.convolution_moments(weighted, weighted, 6)
    return reference, weighted, summed, f.gram_s(summed, 3)


def coefficients(a, b):
    return [a+2*b, Q(0), b, Q(0), Q(0), Q(0), Q(0)]


def coefficient_power(c):
    rising = [Q(factorial(j+1)) for j in range(7)]
    aa = [rising[j]*c[j] for j in range(7)]
    return polynomial_product(aa, aa)


def coefficient_gram(d, tests, mass=Q(1, 4)):
    real, imaginary = [], []
    for a in range(4):
        real_row, imag_row = [], []
        for b in range(4):
            rr, ii = tests[a][b]
            real_row.append(mass*sum((factorial(j)*rr[j]*d[j] for j in range(7)), Q(0)))
            imag_row.append(mass*sum((factorial(j)*ii[j]*d[j] for j in range(7)), Q(0)))
        real.append(real_row)
        imaginary.append(imag_row)
    return real, imaginary


def norm_and_volume_data(h):
    return {"omega_2": f.omega(h, 2), "omega_3": f.omega(h, 3),
            "G": {j: f.quotient(f.principal(h, j+1)) for j in (1, 2, 3)},
            "V": {j: f.volume(f.principal(h, j+1)) for j in (1, 2, 3)}}


def run_checks(mutant=None):
    checks = []

    def check(group, label, condition):
        checks.append({"group": group, "label": label, "passed": bool(condition)})

    check("provenance", "immutable base checker hash", hashlib.sha256(CORE.read_bytes()).hexdigest() == CORE_SHA)
    check("provenance", "immutable base receipt hash", hashlib.sha256(SAVED.read_bytes()).hexdigest() == SAVED_SHA)
    saved = json.loads(SAVED.read_text(encoding="utf-8"))["jobs"][0]["result"]
    paired = []
    for item in saved["windows"]:
        w, z = rational_matrix(item["W"]), rational_matrix(item["Z"])
        r = item["r"]
        wr, zr = f.principal(w, r), f.principal(z, r)
        prefix = f.determinant(wr)
        source = f.determinant(w)
        first = w[0][0]
        e = first+z[0][0]
        dd = f.determinant(f.add(wr, zr))*f.determinant(f.add(w, z))
        u, ratio = Q(item["U"]), Q(item["R"])
        argument1 = dd/(prefix**(1 if mutant == "paired_prefix_power" else 2)*e)
        argument2 = source**2*e/(first**(1 if mutant == "paired_first_power" else 2)*dd)
        label = f"({item['n']},{r})"
        check("paired-factors", label+": EW.21 first root argument", argument1 == u*ratio)
        check("paired-factors", label+": EW.21 second root argument", argument2 == u/ratio)
        paired.append({"n": item["n"], "r": r, "p": prefix, "s": source,
                       "w": first, "e": e, "D": dd, "U_R": argument1, "U_over_R": argument2})

    basis = gamma_polynomials()
    tests = []
    for a in range(4):
        row = []
        for b in range(4):
            rr, ii = test_polynomial(a, b)
            lr, remr = expand_monic(rr, basis)
            li, remi = expand_monic(ii, basis)
            check("test-map", f"({a},{b}): exact full complex monic expansion", all(x == 0 for x in remr+remi))
            check("test-map", f"({a},{b}): even real and odd imaginary coefficient parity",
                  all(lr[j] == 0 for j in (1, 3, 5)) and all(li[j] == 0 for j in (0, 2, 4, 6)))
            row.append((lr, li))
        tests.append(row)

    center_a, center_b = Q(1), Q(1, 4)
    actual_a, actual_b = 1+EPSILON, Q(1, 4)-EPSILON/4
    center_c, actual_c = coefficients(center_a, center_b), coefficients(actual_a, actual_b)
    radius_c = [EPSILON, Q(0), EPSILON, Q(0), Q(0), Q(0), Q(0)]
    d_center, d_actual = coefficient_power(center_c), coefficient_power(actual_c)
    rising = [Q(factorial(j+1)) for j in range(7)]
    aa = [rising[j]*abs(center_c[j]) for j in range(7)]
    ee = [rising[j]*radius_c[j] for j in range(7)]
    full_product = polynomial_product([x+y for x, y in zip(aa, ee)], [x+y for x, y in zip(aa, ee)])
    center_product = polynomial_product(aa, aa)
    quadratic = polynomial_product(ee, ee)
    radius_d = [x-y-(quadratic[j] if mutant == "omit_quadratic_radius" else 0)
                for j, (x, y) in enumerate(zip(full_product, center_product))]
    exact_radius_d = [3*EPSILON+EPSILON**2, Q(0), 21*EPSILON+12*EPSILON**2,
                      Q(0), 18*EPSILON+36*EPSILON**2, Q(0), Q(0)]
    for j in range(7):
        check("coefficient-box", f"degree {j}: actual one-factor input enclosure", abs(actual_c[j]-center_c[j]) <= radius_c[j])
        check("coefficient-box", f"degree {j}: complete tensor radius formula", radius_d[j] == exact_radius_d[j])
        check("coefficient-box", f"degree {j}: actual tensor coefficient enclosure", abs(d_actual[j]-d_center[j]) <= radius_d[j])
    check("coefficient-box", "actual multiplier constant positive", actual_a > 0)
    check("coefficient-box", "actual multiplier quadratic coefficient positive", actual_b > 0)

    center_reference, center_weighted, center_moments, h_center = source_from_ab(center_a, center_b)
    actual_reference, actual_weighted, actual_moments, h_actual = source_from_ab(actual_a, actual_b)
    candidate_mass = Q(1) if mutant == "coefficient_mass" else Q(1, 4)
    center_from_coeff, center_imag = coefficient_gram(d_center, tests, candidate_mass)
    actual_from_coeff, actual_imag = coefficient_gram(d_actual, tests, candidate_mass)
    for a in range(4):
        for b in range(4):
            check("coefficient-gram", f"({a},{b}): central coefficient/moment equality", center_from_coeff[a][b] == h_center[a][b])
            check("coefficient-gram", f"({a},{b}): actual coefficient/moment equality", actual_from_coeff[a][b] == h_actual[a][b])
            check("coefficient-gram", f"({a},{b}): exact imaginary cancellation", center_imag[a][b] == actual_imag[a][b] == 0)
    for j in range(7):
        measured = sum((basis[j][ell]*actual_moments[ell] for ell in range(j+1)), Q(0))
        check("coefficient-gram", f"degree {j}: measured Gamma polynomial moment", measured == Q(1, 4)*factorial(j)*d_actual[j])
    for j in (1, 3, 5):
        check("coefficient-gram", f"degree {j}: exact odd source moment", actual_moments[j] == 0)
    check("coefficient-gram", "actual one-factor mass retained", actual_weighted[0] == Q(3, 4)+EPSILON/4)
    check("coefficient-gram", "actual literal sum mass retained", actual_moments[0] == (Q(3, 4)+EPSILON/4)**2)

    entry_radii = [[Q(1, 4)*sum((factorial(j)*(abs(tests[a][b][0][j])+abs(tests[a][b][1][j]))*radius_d[j]
                                  for j in range(7)), Q(0)) for b in range(4)] for a in range(4)]
    delta = [sum(row, Q(0)) for row in entry_radii]
    diagonal = [[delta[a] if a == b else Q(0) for b in range(4)] for a in range(4)]
    h_lower, h_upper = f.add(h_center, diagonal, -1), f.add(h_center, diagonal)
    for a in range(4):
        for b in range(4):
            check("matrix-envelope", f"({a},{b}): actual entry enclosure", abs(h_actual[a][b]-h_center[a][b]) <= entry_radii[a][b])
            check("matrix-envelope", f"({a},{b}): symmetric rational radius", entry_radii[a][b] == entry_radii[b][a])

    corners = []
    for sign0 in (-1, 1):
        for sign2 in (-1, 1):
            cc = center_c[:]
            cc[0] += sign0*EPSILON
            cc[2] += sign2*EPSILON
            ca, cb = cc[0]-2*cc[2], cc[2]
            dc = coefficient_power(cc)
            _, _, cm, ch = source_from_ab(ca, cb)
            label = f"corner ({sign0},{sign2})"
            check("coefficient-corners", label+": positive constant", ca > 0)
            check("coefficient-corners", label+": positive quadratic coefficient", cb > 0)
            for j in range(7):
                check("coefficient-corners", label+f": degree {j} tensor enclosure", abs(dc[j]-d_center[j]) <= radius_d[j])
            for a in range(4):
                for b in range(4):
                    check("coefficient-corners", label+f": entry ({a},{b}) enclosure", abs(ch[a][b]-h_center[a][b]) <= entry_radii[a][b])
            corners.append({"c0_sign": sign0, "c2_sign": sign2, "A": ca, "B": cb, "d": dc, "moments": cm})

    matrix_pivots = {}
    for name, hh in (("lower", h_lower), ("actual", h_actual), ("upper", h_upper),
                     ("actual_minus_lower", f.add(h_actual, h_lower, -1)),
                     ("upper_minus_actual", f.add(h_upper, h_actual, -1))):
        pp = f.pivots(hh)
        matrix_pivots[name] = pp
        for j, p in enumerate(pp):
            check("positive-pivots", f"{name}: pivot {j}", p > 0)

    lower_data, actual_data, upper_data = map(norm_and_volume_data, (h_lower, h_actual, h_upper))
    for j in (1, 2, 3):
        for name, difference in (("actual_minus_lower", f.add(actual_data["G"][j], lower_data["G"][j], -1)),
                                 ("upper_minus_actual", f.add(upper_data["G"][j], actual_data["G"][j], -1))):
            pp = f.pivots(difference)
            for ell, p in enumerate(pp):
                check("quotient-envelope", f"degree {j} {name}: pivot {ell}", p > 0)
        check("quotient-envelope", f"degree {j}: quotient-volume enclosure", lower_data["V"][j] < actual_data["V"][j] < upper_data["V"][j])
    for j in (2, 3):
        check("quotient-envelope", f"degree {j}: original monic norm enclosure", lower_data[f"omega_{j}"] < actual_data[f"omega_{j}"] < upper_data[f"omega_{j}"])
    u = actual_data["omega_3"]/actual_data["omega_2"]
    u_lower = lower_data["omega_3"]/upper_data["omega_2"]
    u_upper = upper_data["omega_3"]/lower_data["omega_2"]
    vv, vl, vh = actual_data["V"], lower_data["V"], upper_data["V"]
    ratio = vv[1]*vv[2]/(vv[2]*vv[3])
    ratio_lower = vl[1]*vl[2]/(vh[2]*vh[3])
    ratio_upper = vh[1]*vh[2]/(vl[2]*vl[3])
    endpoint_data = {}
    for name, uu, rr in (("lower", u_lower, ratio_lower), ("actual", u, ratio), ("upper", u_upper, ratio_upper)):
        ei, root1, root2 = f.endpoint_interval(uu, rr, 1)
        for j, radicand, enclosure in ((1, uu*rr, root1), (2, uu/rr, root2)):
            check("endpoint", name+f": root {j} lower square", enclosure[0]**2 <= radicand)
            check("endpoint", name+f": root {j} upper square", radicand <= enclosure[1]**2)
        endpoint_data[name] = {"U": uu, "R": rr, "endpoint_interval": ei, "root_intervals": [root1, root2]}
    final_interval = (endpoint_data["lower"]["endpoint_interval"][0], endpoint_data["upper"]["endpoint_interval"][1])
    actual_interval = endpoint_data["actual"]["endpoint_interval"]
    check("endpoint", "positive U enclosure", 0 < u_lower < u < u_upper)
    check("endpoint", "positive four-volume enclosure above one", 1 < ratio_lower < ratio < ratio_upper)
    check("endpoint", "strict endpoint certificate", 0 < final_interval[0] < actual_interval[0] <= actual_interval[1] < final_interval[1])

    failures = [x for x in checks if not x["passed"]]
    return f.string_tree({"schema": "gamma-endpoint-window-supplement-v1", "mutant": mutant,
                          "status": "rejected" if failures else "pass", "checks_count": len(checks),
                          "failure_count": len(failures), "checks_by_group": dict(Counter(x["group"] for x in checks)),
                          "checks": checks, "failures": failures, "paired_factors": paired,
                          "coefficient_pipeline": {"epsilon": EPSILON, "n": 2, "r": 1, "m": 3,
                            "lambda": 1, "k": 2, "c": 1, "c_lambda": Q(1, 2), "C_k": Q(1, 4),
                            "chi": "S^2-2S-1", "q": 2, "actual_A": actual_a, "actual_B": actual_b,
                            "center_c": center_c, "actual_c": actual_c, "radius_c": radius_c,
                            "center_d": d_center, "actual_d": d_actual, "radius_d": radius_d,
                            "gamma_basis": basis, "full_complex_test_coefficients": tests,
                            "actual_reference_moments": actual_reference, "actual_weighted_moments": actual_weighted,
                            "actual_sum_moments": actual_moments, "H_center": h_center, "H_actual": h_actual,
                            "entry_radii": entry_radii, "delta_diagonal": delta,
                            "H_lower": h_lower, "H_upper": h_upper, "positive_pivots": matrix_pivots,
                            "lower_quotient_data": lower_data, "actual_quotient_data": actual_data,
                            "upper_quotient_data": upper_data, "corners": corners,
                            "endpoint_data": endpoint_data, "final_endpoint_interval": final_interval},
                          "scope": "Direct EW.21 checks on fifteen saved auxiliary windows; one complete finite coefficient-box pipeline at n=2,r=1; no arithmetic-zeta input claim."})


def replay():
    script = Path(__file__).resolve()
    jobs = []
    for optimized in (False, True):
        for mutant in (None,)+MUTANTS:
            command = [sys.executable]+(["-O"] if optimized else [])+[str(script)]
            if mutant:
                command += ["--mutant", mutant]
            start = datetime.now(timezone.utc).isoformat()
            job = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
            stop = datetime.now(timezone.utc).isoformat()
            result = json.loads(job.stdout)
            wanted = 1 if mutant else 0
            jobs.append({"command": command, "optimized": optimized, "mutant": mutant,
                         "started_utc": start, "finished_utc": stop, "returncode": job.returncode,
                         "expected_returncode": wanted, "expected_outcome": job.returncode == wanted and result["status"] == ("rejected" if mutant else "pass"),
                         "stdout_sha256": hashlib.sha256(job.stdout).hexdigest(),
                         "stderr_sha256": hashlib.sha256(job.stderr).hexdigest(),
                         "stderr_utf8": job.stderr.decode("utf-8"), "result": result})
    receipt = {"schema": "gamma-endpoint-window-supplement-replay-v1",
               "script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
               "dependencies": {CORE.name: CORE_SHA, SAVED.name: SAVED_SHA},
               "python_executable": sys.executable, "python_version": sys.version,
               "job_count": len(jobs), "all_expected_outcomes": all(j["expected_outcome"] for j in jobs),
               "jobs": jobs}
    target = script.with_suffix(".json")
    target.write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"receipt": str(target), "sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
                      "all_expected_outcomes": receipt["all_expected_outcomes"],
                      "jobs": [{"optimized": j["optimized"], "mutant": j["mutant"], "returncode": j["returncode"],
                                "checks": j["result"]["checks_count"], "failures": j["result"]["failure_count"]} for j in jobs]}, indent=2))
    return 0 if receipt["all_expected_outcomes"] else 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutant", choices=MUTANTS)
    parser.add_argument("--replay", action="store_true")
    args = parser.parse_args()
    if args.replay:
        return replay()
    result = run_checks(args.mutant)
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
