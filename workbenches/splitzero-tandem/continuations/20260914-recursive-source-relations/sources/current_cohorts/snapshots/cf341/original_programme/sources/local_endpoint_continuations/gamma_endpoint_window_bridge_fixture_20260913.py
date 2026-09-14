"""Exact auxiliary endpoint-window calculations; no arithmetic-zeta claim.

The one-factor reference has lambda=1 and mass 1/2.  Its Jacobi
recurrence generates moments, B(t)=1+t^2/4 multiplies that measure,
and a literal twofold convolution produces the source in S=1+i*u.
Only Fraction and integer arithmetic is used in mathematical checks.
Run --replay to record ordinary/-O runs and actual formula mutations.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as Q
from functools import lru_cache
import hashlib
import json
from math import comb
from pathlib import Path
import subprocess
import sys

MAX_DEGREE = 7
ROOT_BITS = 80
DELTA = Q(1, 10**6)
MUTANTS = ("mass", "tensor_cross", "schur_z", "window_ratio", "omega_denominator", "endpoint_half")


def identity(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def trans(a):
    return [list(x) for x in zip(*a)]


def mul(a, b):
    return [[sum((x*y for x, y in zip(row, col)), Q(0)) for col in trans(b)] for row in a]


def add(a, b, sign=1):
    return [[x+sign*y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def determinant(a):
    if not a:
        return Q(1)
    m = [row[:] for row in a]
    result = Q(1)
    for j in range(len(m)):
        pivot = next((i for i in range(j, len(m)) if m[i][j]), None)
        if pivot is None:
            return Q(0)
        if pivot != j:
            m[j], m[pivot] = m[pivot], m[j]
            result = -result
        p = m[j][j]
        result *= p
        for i in range(j+1, len(m)):
            factor = m[i][j]/p
            for k in range(j+1, len(m)):
                m[i][k] -= factor*m[j][k]
    return result


def inverse(a):
    n = len(a)
    m = [row[:] + ident for row, ident in zip(a, identity(n))]
    for j in range(n):
        pivot = next(i for i in range(j, n) if m[i][j])
        m[j], m[pivot] = m[pivot], m[j]
        p = m[j][j]
        m[j] = [x/p for x in m[j]]
        for i in range(n):
            if i != j:
                p = m[i][j]
                m[i] = [x-p*y for x, y in zip(m[i], m[j])]
    return [row[n:] for row in m]


def principal(a, size):
    return [row[:size] for row in a[:size]]


def pivots(a):
    previous = Q(1)
    result = []
    for size in range(1, len(a)+1):
        value = determinant(principal(a, size))
        result.append(value/previous)
        previous = value
    return result


def gamma_moments(alpha, mass, degree):
    # t*b_j = b_(j+1) + j*(j+alpha-1)*b_(j-1), b_0=1.
    expansion = [Q(1)]
    result = []
    for power in range(degree+1):
        result.append(mass*expansion[0])
        following = [Q(0)]*(len(expansion)+1)
        for j, value in enumerate(expansion):
            following[j+1] += value
            if j:
                following[j-1] += j*(j+alpha-1)*value
        expansion = following
    return result


def convolution_moments(a, b, degree, omit_cross=False):
    return [sum((Q(comb(j, ell))*a[ell]*b[j-ell]
                 for ell in range(j+1)
                 if not omit_cross or ell in (0, j)), Q(0))
            for j in range(degree+1)]


def gram_s(moment, degree):
    # Conjugate-linear-first Gram: (1-i*u)^a (1+i*u)^b.
    result = []
    for a in range(degree+1):
        row = []
        for b in range(degree+1):
            real = Q(0)
            imaginary = Q(0)
            for ell in range(a+1):
                for j in range(b+1):
                    term = comb(a, ell)*comb(b, j)*(-1)**ell*moment[ell+j]
                    phase = (ell+j) % 4
                    if phase == 0:
                        real += term
                    elif phase == 1:
                        imaginary += term
                    elif phase == 2:
                        real -= term
                    else:
                        imaginary -= term
            if imaginary:
                raise ArithmeticError("This symmetric fixture must have real original-S Gram entries.")
            row.append(real)
        result.append(row)
    return result


def reduction(degree):
    # chi(S)=S^2-2*S-1, in the original quotient basis (1,S).
    columns = [[Q(1), Q(0)], [Q(0), Q(1)]]
    for j in range(2, degree+1):
        columns.append([2*x+y for x, y in zip(columns[-1], columns[-2])])
    return trans(columns[:degree+1])


def relations(degree):
    return [[Q((-1, -2, 1)[i-j]) if 0 <= i-j <= 2 else Q(0)
             for j in range(degree-1)] for i in range(degree+1)]


def key(a):
    return tuple(tuple(row) for row in a)


@lru_cache(maxsize=None)
def quotient_cached(matrix):
    h = [list(row) for row in matrix]
    j = reduction(len(h)-1)
    return key(inverse(mul(mul(j, inverse(h)), trans(j))))


def quotient(h):
    return [list(row) for row in quotient_cached(key(h))]


def volume(h):
    return determinant(quotient(h))


def omega(h, degree):
    return determinant(principal(h, degree+1))/determinant(principal(h, degree))


def schur(h, n, r):
    lower = principal(h, n)
    cross = [row[n:n+r+1] for row in h[:n]]
    bottom = [row[n:n+r+1] for row in h[n:n+r+1]]
    projection = mul(inverse(lower), cross)
    w = add(bottom, mul(trans(cross), projection), -1)
    j = reduction(n+r)
    j_lower = [row[:n] for row in j]
    j_new = [row[n:] for row in j]
    f = add(j_new, mul(j_lower, projection), -1)
    z = mul(mul(trans(f), quotient(lower)), f)
    return w, f, z, projection


def root_interval(value, exponent, bits=ROOT_BITS):
    """Dyadic enclosure, certified by integer powers and cross products."""
    if value < 0 or exponent <= 0:
        raise ValueError("positive-root domain")
    scale = 1 << bits
    numerator = value.numerator * scale**exponent
    denominator = value.denominator
    lo, hi = 0, 1
    while hi**exponent*denominator <= numerator:
        hi *= 2
    while hi-lo > 1:
        mid = (hi+lo)//2
        if mid**exponent*denominator <= numerator:
            lo = mid
        else:
            hi = mid
    if lo**exponent*denominator == numerator:
        return (Q(lo, scale), Q(lo, scale))
    return (Q(lo, scale), Q(hi, scale))


def endpoint_interval(u, ratio, r, omit_half=False):
    first = root_interval(u*ratio, 2*r)
    second = root_interval(u/ratio, 2*r)
    divisor = 1 if omit_half else 2
    return ((first[0]-second[1])/divisor,
            (first[1]-second[0])/divisor), first, second


def string_tree(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {str(k): string_tree(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [string_tree(x) for x in value]
    return value


def run_checks(mutant=None):
    checks = []

    def check(group, label, condition):
        checks.append({"group": group, "label": label, "passed": bool(condition)})

    mass = Q(1) if mutant == "mass" else Q(1, 2)
    one_reference = gamma_moments(2, mass, 2*MAX_DEGREE+2)
    one_weighted = [one_reference[j]+one_reference[j+2]/4 for j in range(2*MAX_DEGREE+1)]
    source = convolution_moments(one_weighted, one_weighted, 2*MAX_DEGREE, mutant == "tensor_cross")
    reference = convolution_moments(one_reference, one_reference, 2*MAX_DEGREE)
    reference_independent = gamma_moments(4, Q(1, 4), 2*MAX_DEGREE+4)
    density_values = [Q(54, 35)*reference_independent[j]
                      + Q(39, 280)*reference_independent[j+2]
                      + Q(3, 1120)*reference_independent[j+4]
                      for j in range(2*MAX_DEGREE+1)]
    check("moments", "one-factor reference mass", one_reference[0] == Q(1, 2))
    check("moments", "one-factor weighted mass", one_weighted[0] == Q(3, 4))
    check("moments", "two-factor literal reference mass", reference[0] == Q(1, 4))
    check("moments", "two-factor literal weighted mass", source[0] == Q(9, 16))
    check("moments", "reference even moments degree zero through eight",
          one_reference[::2][:5] == [Q(1, 2), Q(1), Q(8), Q(136), Q(3968)])
    check("moments", "weighted sum even moments degree zero through eight",
          source[::2][:5] == [Q(9, 16), Q(9, 2), Q(117), Q(5472), Q(385272)])
    for degree in range(2*MAX_DEGREE+1):
        check("moments", f"degree {degree}: convolution/reference recurrence",
              reference[degree] == reference_independent[degree])
        check("moments", f"degree {degree}: convolution/full density polynomial",
              source[degree] == density_values[degree])

    h = gram_s(source, MAX_DEGREE)
    h_reference = gram_s(reference, MAX_DEGREE)
    h_lower = add(h, [[DELTA*x for x in row] for row in identity(MAX_DEGREE+1)], -1)
    h_upper = add(h, [[DELTA*x for x in row] for row in identity(MAX_DEGREE+1)])
    expected_h3 = [[Q(x, 16) for x in row] for row in
                   ((9, 9, -63, -207), (9, 81, 81, -1863),
                    (-63, 81, 2025, 2025), (-207, -1863, 2025, 93393))]
    check("source", "complete original-S degree-three Gram", principal(h, 4) == expected_h3)
    source_pivots, lower_pivots, upper_pivots = pivots(h), pivots(h_lower), pivots(h_upper)
    for j in range(MAX_DEGREE+1):
        check("positive-pivots", f"degree {j}: source", source_pivots[j] > 0)
        check("positive-pivots", f"degree {j}: lower envelope", lower_pivots[j] > 0)
        check("positive-pivots", f"degree {j}: upper envelope", upper_pivots[j] > 0)

    volumes, norms, gamma_volumes = {}, {}, {}
    for j in range(1, MAX_DEGREE+1):
        hj = principal(h, j+1)
        b = relations(j)
        jj = reduction(j)
        g = quotient(hj)
        lift = mul(mul(inverse(hj), trans(jj)), g)
        v = determinant(g)
        boundary_det = determinant(mul(mul(trans(b), hj), b)) if j >= 2 else Q(1)
        check("quotient", f"degree {j}: relation map", mul(jj, b) == [[Q(0)]*(j-1) for _ in range(2)])
        check("quotient", f"degree {j}: least lift right inverse", mul(jj, lift) == identity(2))
        check("quotient", f"degree {j}: source norm of least lift", mul(mul(trans(lift), hj), lift) == g)
        check("quotient", f"degree {j}: volume determinant line", v == determinant(hj)/boundary_det)
        check("quotient", f"degree {j}: volume positive", v > 0)
        volumes[j], norms[j] = v, omega(h, j)
        gamma_volumes[j] = volume(principal(h_reference, j+1))

    windows = []
    for n in range(2, MAX_DEGREE):
        for r in range(1, MAX_DEGREE-n+1):
            top = n+r
            w, f, z, projection = schur(h, n, r)
            z_actual = z
            if mutant == "schur_z":
                z = [[Q(0)]*(r+1) for _ in range(r+1)]
            w_prefix, z_prefix = principal(w, r), principal(z, r)
            w_first, z_first = principal(w, 1), principal(z, 1)
            t = determinant(add(w, z))/determinant(w)
            t_prefix = determinant(add(w_prefix, z_prefix))/determinant(w_prefix)
            t_first = determinant(add(w_first, z_first))/determinant(w_first)
            ratio_block = t*t_prefix*(t_first if mutant == "window_ratio" else 1/t_first)
            ratio_direct = volumes[n-1]*volumes[n]/(volumes[top-1]*volumes[top])
            divisor = determinant(w_prefix)**(2 if mutant == "omega_denominator" else 1)
            omega_top_block = determinant(w)/divisor
            u = norms[top]/norms[n]
            e, eroot1, eroot2 = endpoint_interval(u, ratio_direct, r, mutant == "endpoint_half")
            label = f"({n},{r})"
            check("windows", label+": full determinant update", t == volumes[n-1]/volumes[top])
            check("windows", label+": prefix determinant update", t_prefix == volumes[n-1]/volumes[top-1])
            check("windows", label+": first determinant update", t_first == volumes[n-1]/volumes[n])
            check("windows", label+": four-volume ratio", ratio_block == ratio_direct)
            check("windows", label+": first original monic norm", w[0][0] == norms[n])
            check("windows", label+": last original monic norm", omega_top_block == norms[top])
            k_lower = inverse(quotient(principal(h, n)))
            k_top = inverse(quotient(principal(h, top+1)))
            check("windows", label+": full quotient inverse update",
                  add(k_lower, mul(mul(f, inverse(w)), trans(f))) == k_top)
            check("windows", label+": Schur source determinant",
                  determinant(w)*determinant(principal(h, n)) == determinant(principal(h, top+1)))
            check("windows", label+": positive window ratio", ratio_direct > 1)
            check("windows", label+": endpoint nonnegative", 0 <= e[0] <= e[1])
            for ix, radicand, enclosure in ((1, u*ratio_direct, eroot1), (2, u/ratio_direct, eroot2)):
                check("root-certificates", label+f": root {ix} exact lower power", enclosure[0]**(2*r) <= radicand)
                check("root-certificates", label+f": root {ix} exact upper power", radicand <= enclosure[1]**(2*r))
                check("root-certificates", label+f": root {ix} dyadic width", enclosure[1]-enclosure[0] <= Q(1, 1 << ROOT_BITS))
            honest = ((eroot1[0]-eroot2[1])/2, (eroot1[1]-eroot2[0])/2)
            check("root-certificates", label+": endpoint half factor via interval identity", e == honest)
            if r == 1:
                square = u*(ratio_direct+1/ratio_direct-2)/4
                check("root-certificates", label+": independent quadratic endpoint identity", e[0]**2 <= square <= e[1]**2)

            v_lo = {j: volume(principal(h_lower, j+1)) for j in {n-1, n, top-1, top}}
            v_hi = {j: volume(principal(h_upper, j+1)) for j in {n-1, n, top-1, top}}
            u_lo = omega(h_lower, top)/omega(h_upper, n)
            u_hi = omega(h_upper, top)/omega(h_lower, n)
            ratio_lo = v_lo[n-1]*v_lo[n]/(v_hi[top-1]*v_hi[top])
            ratio_hi = v_hi[n-1]*v_hi[n]/(v_lo[top-1]*v_lo[top])
            e_lo, _, _ = endpoint_interval(u_lo, ratio_lo, r)
            e_hi, _, _ = endpoint_interval(u_hi, ratio_hi, r)
            envelope = (e_lo[0], e_hi[1])
            check("envelopes", label+": source norm ratio enclosure", 0 < u_lo < u < u_hi)
            check("envelopes", label+": four-volume ratio enclosure", 1 < ratio_lo < ratio_direct < ratio_hi)
            check("envelopes", label+": endpoint interval strict containment", envelope[0] < e[0] <= e[1] < envelope[1])
            check("envelopes", label+": endpoint interval positivity", 0 < envelope[0] < envelope[1])
            record = {"n": n, "r": r, "omega_n": norms[n], "omega_top": norms[top],
                      "U": u, "R": ratio_direct, "T_full": t, "T_prefix": t_prefix,
                      "T_first": t_first, "W": w, "F": f, "Z": z_actual,
                      "source_projection_coefficients": projection,
                      "root_exponent": 2*r, "root_radicands": [u*ratio_direct, u/ratio_direct],
                      "root_intervals": [eroot1, eroot2], "endpoint_interval": e,
                      "source_envelope_U": [u_lo, u_hi], "source_envelope_R": [ratio_lo, ratio_hi],
                      "source_envelope_endpoint_interval": envelope}
            windows.append(record)
    failures = [item for item in checks if not item["passed"]]
    counts = Counter(item["group"] for item in checks)
    return string_tree({"schema": "gamma-endpoint-window-exact-fixture-v1", "mutant": mutant,
                       "status": "pass" if not failures else "rejected",
                       "fixture": {"lambda": 1, "k": 2, "c": 1, "c_lambda": Q(1, 2),
                                   "C_k": Q(1, 4), "B": "1+t^2/4", "chi": "S^2-2S-1",
                                   "q": 2, "max_degree": MAX_DEGREE, "delta": DELTA,
                                   "root_dyadic_bits": ROOT_BITS, "scope": "auxiliary polynomial weight, not actual zeta data"},
                       "checks_count": len(checks), "checks_by_group": dict(counts),
                       "failure_count": len(failures), "failures": failures, "checks": checks,
                       "one_factor_reference_moments": one_reference,
                       "one_factor_weighted_moments": one_weighted,
                       "two_factor_reference_moments": reference,
                       "two_factor_weighted_moments": source, "H_7": h, "J_7": reduction(7),
                       "source_pivots": source_pivots, "lower_envelope_pivots": lower_pivots,
                       "upper_envelope_pivots": upper_pivots, "source_monic_norms": norms,
                       "quotient_volumes": volumes, "reference_quotient_volumes": gamma_volumes,
                       "windows": windows})


def replay():
    script = Path(__file__).resolve()
    jobs = []
    for optimized in (False, True):
        for mutant in (None,) + MUTANTS:
            command = [sys.executable] + (["-O"] if optimized else []) + [str(script)]
            if mutant:
                command += ["--mutant", mutant]
            started = datetime.now(timezone.utc).isoformat()
            done = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
            stopped = datetime.now(timezone.utc).isoformat()
            decoded = json.loads(done.stdout)
            wanted = 1 if mutant else 0
            jobs.append({"command": command, "optimized": optimized, "mutant": mutant,
                         "started_utc": started, "finished_utc": stopped,
                         "returncode": done.returncode, "expected_returncode": wanted,
                         "expected_outcome": done.returncode == wanted and decoded["status"] == ("rejected" if mutant else "pass"),
                         "stdout_sha256": hashlib.sha256(done.stdout).hexdigest(),
                         "stderr_sha256": hashlib.sha256(done.stderr).hexdigest(),
                         "stderr_utf8": done.stderr.decode("utf-8"), "result": decoded})
    receipt = {"schema": "gamma-endpoint-window-exact-fixture-replay-v1",
               "script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
               "python_executable": sys.executable, "python_version": sys.version,
               "job_count": len(jobs), "all_expected_outcomes": all(j["expected_outcome"] for j in jobs),
               "distinct_mathematical_checks_per_job": jobs[0]["result"]["checks_count"],
               "scope": "Fifteen finite auxiliary windows; mode repetitions do not add distinct checks; no startup guards or asserts used for formula rejections.",
               "jobs": jobs}
    out = script.with_suffix(".json")
    out.write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"receipt": str(out), "sha256": hashlib.sha256(out.read_bytes()).hexdigest(),
                      "all_expected_outcomes": receipt["all_expected_outcomes"],
                      "jobs": [{"optimized": j["optimized"], "mutant": j["mutant"],
                                "returncode": j["returncode"], "checks": j["result"]["checks_count"],
                                "failures": j["result"]["failure_count"]} for j in jobs]}, indent=2))
    return 0 if receipt["all_expected_outcomes"] else 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutant", choices=MUTANTS)
    parser.add_argument("--replay", action="store_true")
    arguments = parser.parse_args()
    if arguments.replay:
        return replay()
    result = run_checks(arguments.mutant)
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
