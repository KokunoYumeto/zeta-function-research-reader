"""Exact Fraction transport of saved infinite theta moments to original source costs.

No special-function evaluation, quadrature or floating-point arithmetic occurs.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys

PIN = "8688e782d2283c8c236678c75785a6170504b5317067f7bb91cc237e67b616d1"


def need(condition, message):
    if not condition:
        raise RuntimeError(message)


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def sub(a, b):
    return a[0]-b[1], a[1]-b[0]


def mul(a, b):
    products = [x*y for x in a for y in b]
    return min(products), max(products)


def scale(a, value):
    return mul(a, (F(value), F(value)))


def div(a, b):
    need(b[0] > 0, "positive interval denominator required")
    return mul(a, (1/b[1], 1/b[0]))


def decimal(i, digits):
    sign = "-" if i < 0 else ""
    text = str(abs(i)).rjust(digits+1, "0")
    return sign+text[:-digits]+"."+text[-digits:]


def outward(interval):
    low, high = interval
    digits = 40
    scale_value = 10**digits
    low_integer = (scale_value*low).__floor__()-1
    high_integer = (scale_value*high).__ceil__()+1
    need(F(low_integer, scale_value) < low <= high < F(high_integer, scale_value), "exact rational endpoint transport failed")
    need(high_integer-low_integer == 3, "published exact interval width changed")
    return {"lower": decimal(low_integer, digits), "upper": decimal(high_integer, digits),
            "transport_lower_rational": str(low), "transport_upper_rational": str(high),
            "width_rational": str(F(high_integer-low_integer, scale_value))}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=Path(__file__).with_name("gamma_seed_intervals_20260913_normal.json"))
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--fault", choices=["none", "drop-cross-term", "unit-mass", "Q0-less-one"], default="none")
    args = parser.parse_args()
    data = args.input.read_bytes()
    need(hashlib.sha256(data).hexdigest() == PIN, "saved infinite moment receipt pin changed")
    receipt = json.loads(data)
    need(receipt["status"] == "passed" and receipt["fault"] == "none", "input is not a positive certificate")
    moment = {n: (F(receipt["results"]["mu_"+str(n)]["exact_lower_dyadic"]),
                  F(receipt["results"]["mu_"+str(n)]["exact_upper_dyadic"])) for n in [0, 2, 4, 6]}
    nu = div(moment[2], moment[0])
    eta = div(moment[4], moment[2])
    h2_margin = sub(mul(moment[4], moment[0]), mul(moment[2], moment[2]))
    a2_one = sub(eta, nu)
    a2_two = add(eta, nu)
    Q0 = scale(nu, F(2, 13))
    Q1_one = scale(a2_one, F(1, 15))
    rho = sub(eta, scale(nu, F(43, 13)))
    h2_one = sub(moment[4], div(mul(moment[2], moment[2]), moment[0]))
    h3_one = sub(moment[6], div(mul(moment[4], moment[4]), moment[2]))
    a3_one = div(h3_one, h2_one)
    Q2_one = scale(a3_one, F(2, 51))
    need(nu[0] > 0 and a2_one[0] > 0 and h2_margin[0] > 0, "strict source norm positivity lost")
    need(Q0[0] > 1 and rho[1] < 0, "strict source comparison signs lost")
    need(h3_one[0] > 0 and a3_one[0] > 0, "third source norm positivity lost")
    intervals = {"nu_mu2_over_mu0": nu, "eta_mu4_over_mu2": eta,
                 "h2_positive_numerator": h2_margin, "a2_k1": a2_one,
                 "a2_k2": a2_two, "Q0_all_k": Q0, "Q1_k1": Q1_one,
                 "rho_Q1_difference_numerator": rho,
                 "a3_k1": a3_one, "Q2_k1": Q2_one}
    failed = 0
    if args.fault == "drop-cross-term":
        # k=2, dropping the original 6 mu2^2 term from M4 gives eta-2nu.
        wrong = sub(eta, scale(nu, 2))
        failed = int(wrong[1] < a2_two[0] or a2_two[1] < wrong[0])
    elif args.fault == "unit-mass":
        failed = int(moment[2][0] > nu[1] or moment[2][1] < nu[0])
    elif args.fault == "Q0-less-one":
        failed = int(Q0[0] > 1)
    need(args.fault == "none" or failed == 1, "requested false source-cost claim was not rejected")
    payload = {"schema": "gamma-seed-source-costs-rational-v1", "status": "passed" if failed == 0 else "rejected",
               "optimization_flag": sys.flags.optimize, "input_sha256": PIN,
               "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               "arithmetic": "fractions.Fraction only; no quadrature, special functions or floats",
               "fault": args.fault, "failed_fault_checks": failed,
               "results": {name: outward(interval) for name, interval in intervals.items()},
               "scope": "Exact original source costs in fixed polynomial degrees one through three, from pinned infinite theta moment enclosures; seed quotient dimension zero."}
    args.output.write_text(json.dumps(payload, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"status": payload["status"], "fault": args.fault,
                      "intervals": {name: {side: value[side] for side in ["lower", "upper"]}
                                    for name, value in payload["results"].items()}}, indent=2))
    raise SystemExit(failed)


if __name__ == "__main__":
    main()
