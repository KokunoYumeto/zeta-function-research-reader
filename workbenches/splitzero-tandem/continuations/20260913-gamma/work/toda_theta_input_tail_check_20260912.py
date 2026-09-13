"""Certified theta-seed enclosures, with proved omitted-square-tail bounds.

The finite incomplete-gamma sum is evaluated with python-flint/Arb balls.
The proof in toda_theta_input_tail_20260912.tex supplies the infinite tail.
No selected zeta zero, packet determinant, or growing-degree control is tested.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import sys
from pathlib import Path
import flint
from flint import arb, acb, ctx, fmpq


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def stirling2(a, b):
    if a == b == 0:
        return 1
    if a == 0 or b == 0 or b > a:
        return 0
    return b * stirling2(a - 1, b) + stirling2(a - 1, b - 1)


def H(p, L, d):
    rho = (-d * (2 * L + 1)).exp()
    result = arb(0)
    for a in range(p + 1):
        for b in range(a + 1):
            result += (math.comb(p, a) * L ** (p - a) * stirling2(a, b)
                       * math.factorial(b) * rho ** b / (1 - rho) ** (b + 1))
    return result


def integral_power(power, b):
    order = arb(fmpq(power + 1, 2))
    return b.gamma_upper(order) / (2 * b ** order)


def seed_tail(J, theta0=arb(0), imaginary_bound=arb(0)):
    pi = arb.pi()
    d = pi * (-imaginary_bound).exp() * theta0.cos()
    require(d > 0, "tail domain must stay inside the analytic strip")
    def A(L):
        return (6 * pi * imaginary_bound.exp() * H(2, L, d)
                + 4 * pi ** 2 * (2 * imaginary_bound).exp() * H(4, L, d))
    L = J + 1
    return 16 * A(1) * A(L) * integral_power(8, d * (1 + L * L))


def derivative_tail(J):
    pi = arb.pi()
    def B(L):
        return (30 * pi * H(2, L, pi) + 60 * pi ** 2 * H(4, L, pi)
                + 16 * pi ** 3 * H(6, L, pi))
    L = J + 1
    return 4 * B(1) * B(L) * integral_power(12, pi * (1 + L * L))


def seed_finite(J, theta):
    pi = arb.pi()
    plus = acb(0, theta).exp()
    minus = acb(0, -theta).exp()
    result = acb(0)
    coeff = {1: -6, 2: 4}
    for m in range(1, J + 1):
        for n in range(1, J + 1):
            C = pi * (m * m * plus + n * n * minus)
            require(C.real > 0, "gamma argument left its proved branch")
            for r, cr in coeff.items():
                for s, cs in coeff.items():
                    alpha = arb(fmpq(2 * r + 2 * s + 1, 2))
                    result += (4 * cr * cs * (pi * m * m) ** r
                               * (pi * n * n) ** s * plus ** (r - s)
                               * C.gamma_upper(alpha) / C ** alpha)
    return result


def derivative_finite(J):
    pi = arb.pi()
    coeff = {1: 30, 2: -60, 3: 16}
    result = arb(0)
    for m in range(1, J + 1):
        for n in range(1, J + 1):
            C = pi * (m * m + n * n)
            for r, dr in coeff.items():
                for s, ds in coeff.items():
                    alpha = arb(fmpq(2 * r + 2 * s + 1, 2))
                    result += (dr * ds * (pi * m * m) ** r
                               * (pi * n * n) ** s
                               * C.gamma_upper(alpha) / C ** alpha)
    return result


def decimal_endpoint(integer, digits):
    sign = "-" if integer < 0 else ""
    s = str(abs(integer)).rjust(digits + 1, "0")
    return sign + s[:-digits] + "." + s[-digits:]


def enclose(ball, digits=40):
    scale = 10 ** digits
    lo = int((ball.lower() * scale).floor().fmpz()) - 1
    hi = int((ball.upper() * scale).ceil().fmpz()) + 1
    require(ball > arb(fmpq(lo, scale)), "lower decimal endpoint is not certified")
    require(ball < arb(fmpq(hi, scale)), "upper decimal endpoint is not certified")
    return {"lower": decimal_endpoint(lo, digits), "upper": decimal_endpoint(hi, digits),
            "exact_lower_dyadic": str(ball.lower().fmpq()),
            "exact_upper_dyadic": str(ball.upper().fmpq()),
            "ball": ball.str(65, more=True)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--negative-control", action="store_true")
    args = parser.parse_args()
    ctx.prec = 256
    ctx.threads = 1
    J = 8
    # Exact coefficient calculation: -2y(P'-P)-P/2, P=8y^2-12y.
    from fractions import Fraction
    P = {1: Fraction(-12), 2: Fraction(8)}
    got = {}
    for degree, coefficient in P.items():
        got[degree] = got.get(degree, 0) - (2 * degree + Fraction(1, 2)) * coefficient
        got[degree + 1] = got.get(degree + 1, 0) + 2 * coefficient
    require(got == {1: 30, 2: -60, 3: 16}, "original derivative coefficients changed")
    results = {}
    balls = {}
    for name, theta in [("M1_0", arb(0)), ("M1_one_tenth", arb(fmpq(1, 10)))]:
        finite = seed_finite(J, theta)
        require(finite.imag.contains(0), "real seed sum has no real value in its enclosure")
        tail = seed_tail(J, theta)
        require(tail > 0 and tail < arb("1e-90"), "tail enclosure is invalid or too wide")
        require(tail < arb("7e-107" if name == "M1_0" else "3e-106"),
                "published seed tail bound is not certified")
        full = finite.real + arb(0, tail.upper())
        require(full > 0, "seed mass positivity was not certified")
        balls[name] = full
        results[name] = {**enclose(full), "tail_bound_ball": tail.str(65, more=True),
                         "finite_ball": finite.str(65, more=True)}
    tail = derivative_tail(J)
    require(tail > 0 and tail < arb("1e-85"), "second-moment tail enclosure is invalid")
    require(tail < arb("4e-103"), "published second-moment tail bound is not certified")
    derivative = derivative_finite(J) + arb(0, tail.upper())
    require(derivative > 0, "second moment positivity was not certified")
    balls["M1_second_0"] = derivative
    results["M1_second_0"] = {**enclose(derivative), "tail_bound_ball": tail.str(65, more=True)}
    ratio = derivative / balls["M1_0"]
    results["a1_tensor_coefficient"] = enclose(ratio)
    # An explicit request injects a false numerical assertion; no Python assert is used.
    require(not args.negative_control or ratio < arb(1), "deliberate false recurrence bound rejected")
    payload = {"schema": "toda-theta-seed-arb-certificate-v1", "status": "passed",
               "python_flint": flint.__version__, "precision_bits": ctx.prec,
               "integer_cutoff_J": J, "optimization_flag": sys.flags.optimize,
               "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               "scope": "Three infinite analytic-seed values and a1^(k)/k, finite sums enclosed by Arb with proved infinite tails; no finite-packet or growing-degree estimate.",
               "negative_control": False, "results": results}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": payload["status"], "output": str(args.output),
                      "intervals": {k: {a: v[a] for a in ["lower", "upper"]} for k, v in results.items()}}, indent=2))


if __name__ == "__main__":
    main()
