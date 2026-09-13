"""Transfer pinned, already tail-certified theta moments to Gamma coefficients.

No quadrature is rerun. This records new outward enclosures of exact FE.28--30
from the preserved TI dyadic intervals and a fresh Arb enclosure of pi.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
import sys

import flint
from flint import arb, ctx, fmpq


EXPECTED_INPUT_SHA256 = "2d5ebb1a40f1f33cff8d227ae57d68fb3ae0a18d084b74973d08fcf2c1cc32cc"
EXPECTED_INPUT_SCRIPT_SHA256 = "db01839848cb6b67d24f5702789f6b9eb27d523a80c40cc58b25b9634ce101c5"


def require(value, message):
    if not value:
        raise ValueError(message)


def rational(value):
    return fmpq(value.numerator, value.denominator)


def input_interval(entry):
    lower = Fraction(entry["exact_lower_dyadic"])
    upper = Fraction(entry["exact_upper_dyadic"])
    require(Fraction(entry["lower"]) < lower < upper < Fraction(entry["upper"]),
            "TI rational endpoint nesting failed")
    ball = arb(rational((lower + upper) / 2), rational((upper - lower) / 2))
    require(ball.contains(rational(lower)) and ball.contains(rational(upper)),
            "Arb construction did not contain both preserved input endpoints")
    return ball, lower, upper


def decimal(integer, digits):
    sign = "-" if integer < 0 else ""
    value = str(abs(integer)).rjust(digits + 1, "0")
    return sign + value[:-digits] + "." + value[-digits:]


def enclose(ball, digits=40):
    scale = 10 ** digits
    lower = int((ball.lower() * scale).floor().fmpz()) - 1
    upper = int((ball.upper() * scale).ceil().fmpz()) + 1
    require(ball > arb(fmpq(lower, scale)), "decimal lower endpoint failed")
    require(ball < arb(fmpq(upper, scale)), "decimal upper endpoint failed")
    return {"lower": decimal(lower, digits), "upper": decimal(upper, digits),
            "exact_lower_dyadic": str(ball.lower().fmpq()),
            "exact_upper_dyadic": str(ball.upper().fmpq()),
            "ball": ball.str(65, more=True)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--negative-control", action="store_true")
    args = parser.parse_args()
    raw = args.input.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == EXPECTED_INPUT_SHA256,
            "preserved TI input receipt hash changed")
    source = json.loads(raw)
    require(source["status"] == "passed" and source["negative_control"] is False,
            "TI receipt does not record a successful positive run")
    require(source["script_sha256"] == EXPECTED_INPUT_SCRIPT_SHA256,
            "TI proof checker identity changed")
    ctx.prec = 256
    ctx.threads = 1
    mu, mu_lower, mu_upper = input_interval(source["results"]["M1_0"])
    nu, nu_lower, nu_upper = input_interval(source["results"]["M1_second_0"])
    require(0 < mu_lower < mu_upper and 0 < nu_lower < nu_upper,
            "actual seed finite source positivity not certified")
    alpha = fmpq(13, 2)
    gamma_mass = arb(fmpq(10395, 2048)) * (arb.pi() / 2).sqrt()
    require(gamma_mass > 0, "original Gamma mass is not positive")
    c0 = mu / gamma_mass
    numerator_c2 = nu - alpha * mu
    require(numerator_c2 > 0, "actual second Gamma coefficient numerator not positive")
    c2 = numerator_c2 / (gamma_mass * 2 * alpha * (alpha + 1))
    q0 = nu / (alpha * mu)
    require(c0 > 0 and c2 > 0 and q0 > 1, "actual coefficient signs not certified")
    ratio_lower = nu_lower / (Fraction(13, 2) * mu_upper)
    ratio_upper = nu_upper / (Fraction(13, 2) * mu_lower)
    require(q0.contains(rational(ratio_lower)) and q0.contains(rational(ratio_upper)),
            "Arb ratio does not contain the independent rational interval division")
    require(not args.negative_control or q0 < 1,
            "deliberate false Gamma determinant-correction bound rejected")
    result = {
        "schema": "gamma-seed-coefficient-transfer-certificate-v1",
        "status": "passed", "negative_control": False,
        "optimization_flag": sys.flags.optimize,
        "python_flint": flint.__version__, "precision_bits": ctx.prec,
        "input_receipt_sha256": EXPECTED_INPUT_SHA256,
        "input_checker_sha256": EXPECTED_INPUT_SCRIPT_SHA256,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "quadrature_rerun": False,
        "scope": "New Gamma coefficient c0,c2 and first source determinant correction enclosures from pinned infinite-tail-certified actual theta moments; all-k degree-one source formulas FE.25--30; seed packet quotient dimension zero.",
        "results": {"gamma_mass_lambda_13_over_4": enclose(gamma_mass),
                    "c0": enclose(c0), "c2": enclose(c2),
                    "Q0_all_tensor_degrees": enclose(q0)},
        "exact_rational_Q0_interval": {"lower": str(ratio_lower),
                                       "upper": str(ratio_upper)},
        "all_k_source_certificate": {
            "integer_domain": "k >= 1",
            "basis_1_u_diagonal": ["mu^k", "k*mu^(k-1)*nu"],
            "lower_diagonal": ["mu_lower^k", "k*mu_lower^(k-1)*nu_lower"],
            "upper_diagonal": ["mu_upper^k", "k*mu_upper^(k-1)*nu_upper"],
            "mu_lower": str(mu_lower), "mu_upper": str(mu_upper),
            "nu_lower": str(nu_lower), "nu_upper": str(nu_upper),
            "original_spectral_basis_map_columns": [["1", "0"], ["k/2", "i"]],
            "quotient_dimension": 0, "quotient_determinant": "1"}}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "passed", "optimization_flag": sys.flags.optimize,
                      "intervals": {key: {edge: value[edge] for edge in ("lower", "upper")}
                                    for key, value in result["results"].items()}}, indent=2))


if __name__ == "__main__":
    main()
