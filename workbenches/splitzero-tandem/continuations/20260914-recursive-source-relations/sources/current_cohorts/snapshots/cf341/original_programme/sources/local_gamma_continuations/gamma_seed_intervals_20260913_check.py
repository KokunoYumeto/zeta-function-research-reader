"""Infinite theta moments and original gamma arithmetic coefficients, certified by Arb.

The proof is gamma_seed_intervals_20260913.tex. All polynomial coefficients
are exact Fractions; every infinite square has a proved positive tail.
No truncation-agreement inference or selected-zero calculation is used.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path
import sys
import flint
from flint import arb, ctx, fmpq


def need(condition, message):
    if not condition:
        raise RuntimeError(message)


def ball_fraction(value):
    value = Fraction(value)
    return arb(fmpq(value.numerator, value.denominator))


def derivative_polynomials(count=3):
    polynomials = [{1: Fraction(-12), 2: Fraction(8)}]
    for _ in range(count):
        next_polynomial = {}
        for a, coefficient in polynomials[-1].items():
            next_polynomial[a] = next_polynomial.get(a, Fraction(0)) - (2*a + Fraction(1, 2))*coefficient
            next_polynomial[a+1] = next_polynomial.get(a+1, Fraction(0)) + 2*coefficient
        polynomials.append({a: c for a, c in next_polynomial.items() if c})
    return polynomials


def gamma_polynomials(alpha, count=6):
    polynomials = [{0: Fraction(1)}, {1: Fraction(1)}]
    for n in range(1, count):
        polynomial = {a+1: c for a, c in polynomials[-1].items()}
        for a, c in polynomials[-2].items():
            polynomial[a] = polynomial.get(a, Fraction(0)) - n*(n+alpha-1)*c
        polynomials.append({a: c for a, c in polynomial.items() if c})
    return polynomials


def rising(alpha, n):
    value = Fraction(1)
    for j in range(n):
        value *= alpha+j
    return value


@lru_cache(None)
def stirling_second(n, j):
    if n == j == 0:
        return 1
    if n == 0 or j == 0 or j > n:
        return 0
    return j*stirling_second(n-1, j) + stirling_second(n-1, j-1)


def H(power, a, d):
    rho = (-d*(2*a+1)).exp()
    total = arb(0)
    for j in range(power+1):
        for b in range(j+1):
            total += (math.comb(power, j)*a**(power-j)*stirling_second(j, b)
                      * math.factorial(b)*rho**b/(1-rho)**(b+1))
    return total


def I(power, C):
    alpha = arb(fmpq(power+1, 2))
    return C.gamma_upper(alpha)/(2*C**alpha)


def moment_tail(P, J):
    pi = arb.pi()
    def A(a):
        return sum((ball_fraction(abs(c))*pi**p*H(2*p, a, pi)
                    for p, c in P.items()), arb(0))
    degree = max(P)
    L = J+1
    return 4*A(1)*A(L)*I(4*degree, pi*(1+L*L))


def all_finite_moments(polynomials, J):
    """Literal square sum, factor2 endpoint cancelling factor1/2 integral."""
    pi = arb.pi()
    maximum = 2*max(max(P) for P in polynomials)
    moments = [arb(0) for _ in polynomials]
    recurrence_checks = 0
    for m in range(1, J+1):
        for n in range(1, J+1):
            a, b = pi*m*m, pi*n*n
            C = a+b
            integral_twice = {}
            for power in range(2, maximum+1):
                alpha = arb(fmpq(2*power+1, 2))
                integral_twice[power] = C.gamma_upper(alpha)/C**alpha
            # A second exact formula checks special-function argument order.
            # The finite sums still use the direct incomplete-gamma balls.
            for power in range(2, maximum):
                candidate = ((power+ball_fraction(Fraction(1, 2)))/C
                             * integral_twice[power] + (-C).exp()/C)
                need(candidate.overlaps(integral_twice[power+1]),
                     "incomplete-gamma recurrence lost its endpoint term")
                recurrence_checks += 1
            for r, P in enumerate(polynomials):
                for i, ci in P.items():
                    for j, cj in P.items():
                        moments[r] += ball_fraction(ci*cj)*a**i*b**j*integral_twice[i+j]
    return moments, recurrence_checks


def decimal_integer(value, digits):
    sign = "-" if value < 0 else ""
    value = str(abs(value)).rjust(digits+1, "0")
    return sign + value[:-digits] + "." + value[-digits:]


def enclose(value, digits=40):
    scale = 10**digits
    low = int((value.lower()*scale).floor().fmpz())-1
    high = int((value.upper()*scale).ceil().fmpz())+1
    need(value > arb(fmpq(low, scale)), "decimal lower endpoint failed")
    need(value < arb(fmpq(high, scale)), "decimal upper endpoint failed")
    return {"lower": decimal_integer(low, digits), "upper": decimal_integer(high, digits),
            "lower_rational": str(Fraction(low, scale)), "upper_rational": str(Fraction(high, scale)),
            "exact_lower_dyadic": str(value.lower().fmpq()),
            "exact_upper_dyadic": str(value.upper().fmpq()),
            "ball": value.str(65, more=True)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--fault", choices=["none", "endpoint-factor", "reference-mass", "fourth-sign", "tail-omission"], default="none")
    args = parser.parse_args()
    ctx.prec = 256
    ctx.threads = 1
    J = 8
    P = derivative_polynomials()
    exact_P = [{1: -12, 2: 8}, {1: 30, 2: -60, 3: 16},
               {1: -75, 2: 330, 3: -224, 4: 32},
               {1: Fraction(375, 2), 2: -1635, 3: 2116, 4: -720, 5: 64}]
    need(P == exact_P, "the exact original theta derivative polynomials changed")
    alpha = Fraction(13, 2)
    b = gamma_polynomials(alpha)
    need(b[2] == {0: -alpha, 2: 1}, "gamma degree-two polynomial changed")
    need(b[4] == {0: Fraction(663, 4), 2: -47, 4: 1}, "gamma degree-four polynomial changed")
    need(b[6] == {0: Fraction(-69615, 8), 2: Fraction(13801, 4), 4: Fraction(-275, 2), 6: 1}, "gamma degree-six polynomial changed")
    need(b[0] == {0: 1} and b[1] == {1: 1} and
         b[3] == {1: Fraction(-43, 2), 3: 1} and
         b[5] == {1: Fraction(3931, 4), 3: -85, 5: 1},
         "gamma odd or initial polynomial changed")
    need([math.factorial(j)*rising(alpha, j) for j in [0, 2, 4, 6]] ==
         [1, Fraction(195, 2), Fraction(188955, 2), Fraction(1368978975, 4)],
         "original exact gamma denominator factors changed")
    finite, special_checks = all_finite_moments(P, J)
    moments, results = {}, {}
    for r in range(4):
        tail = moment_tail(P[r], J)
        need(tail > 0 and tail < arb("1e-85"), "proved omitted-square tail failed")
        need(tail < arb(["7e-107", "4e-103", "2e-99", "1.4e-95"][r]),
             "published rational tail cap failed")
        value = finite[r] + arb(0, tail.upper())
        need(value > 0, "an even moment lost certified strict positivity")
        moments[2*r] = value
        results[f"mu_{2*r}"] = {**enclose(value), "finite_ball": finite[r].str(65, more=True),
                                "tail_bound_ball": tail.str(65, more=True),
                                "tail_upper_rational": str(tail.upper().fmpq())}
    # Previously certified TI values are exact rational intervals, not floats.
    need(moments[0] > arb("1.2790072478464851404795335922671932744916") and
         moments[0] < arb("1.2790072478464851404795335922671932744919"), "original TI mass interval failed")
    need(moments[2] > arb("13.0555493025705584353926846581231936824343") and
         moments[2] < arb("13.0555493025705584353926846581231936824346"), "original TI second-moment interval failed")
    mass = arb(2)**ball_fraction(1-alpha) * ball_fraction(alpha).gamma()
    # Gamma(13/2)=10395 sqrt(pi)/64, and the original factor is 2^(-11/2).
    mass_closed = arb(10395)*arb.pi().sqrt()/(2048*arb(2).sqrt())
    need(mass.overlaps(mass_closed) and mass > 6 and mass < 7,
         "original gamma mass and its half-integer formula disagree")
    results["reference_mass"] = enclose(mass)
    coefficients = {}
    for j in [0, 2, 4, 6]:
        numerator = sum((ball_fraction(coefficient)*moments[a]
                         for a, coefficient in b[j].items()), arb(0))
        denominator_factor = math.factorial(j)*rising(alpha, j)
        coefficient = numerator/(mass*ball_fraction(denominator_factor))
        coefficients[j] = coefficient
        results[f"c_{j}"] = {**enclose(coefficient), "numerator_ball": numerator.str(65, more=True),
                              "denominator_factor_exact": str(denominator_factor)}
    need(coefficients[0] > 0 and coefficients[2] > 0 and coefficients[4] < 0 and coefficients[6] < 0,
         "the certified low-degree arithmetic coefficient signs changed")
    need((mass*coefficients[0]).overlaps(moments[0]), "source mass reconstruction failed")
    # Verify the exact finite coefficient map independently in the integer forms.
    alternatives = {
        2: (2*moments[2]-13*moments[0])/(195*mass),
        4: (4*moments[4]-188*moments[2]+663*moments[0])/(377910*mass),
        6: (8*moments[6]-1100*moments[4]+27602*moments[2]-69615*moments[0])/(2737957950*mass)}
    for j, value in alternatives.items():
        need(value.overlaps(coefficients[j]), "integer gamma coefficient map changed")
    # Faults test false mathematical claims against already enclosed infinite values.
    fault_passed = True
    fault_description = "none"
    if args.fault == "endpoint-factor":
        fault_description = "Discarding the factor two from inversion leaves the same fourth moment."
        fault_passed = (moments[4]/2).overlaps(moments[4])
    elif args.fault == "reference-mass":
        fault_description = "Assigning mass one to the gamma reference leaves its degree-zero coefficient unchanged."
        fault_passed = moments[0].overlaps(coefficients[0])
    elif args.fault == "fourth-sign":
        fault_description = "The original fourth gamma expansion coefficient is nonnegative."
        fault_passed = coefficients[4] >= 0
    elif args.fault == "tail-omission":
        fault_description = "The cutoff-zero theta square with zero error encloses the full positive seed mass."
        fault_passed = arb(0).overlaps(moments[0])
    payload = {"schema": "gamma-seed-infinite-moment-arb-v1", "status": "passed" if fault_passed else "rejected",
               "python_flint": flint.__version__, "precision_bits": ctx.prec, "arithmetic_threads": ctx.threads,
               "integer_cutoff_J": J, "optimization_flag": sys.flags.optimize,
               "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               "fault": args.fault, "fault_description": fault_description,
               "failed_fault_checks": 0 if fault_passed else 1,
               "incomplete_gamma_recurrence_checks": special_checks,
               "theta_polynomials": [{str(j): str(c) for j, c in poly.items()} for poly in P],
               "gamma_polynomials": [{str(j): str(c) for j, c in poly.items()} for poly in b],
               "reference_lambda": "13/4", "alpha": "13/2", "results": results,
               "scope": "Four infinite original analytic seed moments, gamma reference mass and c0,c2,c4,c6; exact finite polynomials, Arb balls and proved infinite square tails. No selected packet or growing-degree estimate."}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"status": payload["status"], "fault": args.fault,
                      "intervals": {name: {side: value[side] for side in ["lower", "upper"]}
                                    for name, value in results.items()}}, indent=2))
    if not fault_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
