"""Exact finite checks for the independent endpoint-product review.

Run with Python normally or with -O. No test relies on an assert statement.
The written review contains the general proof; this executable checks finite
algebraic fixtures and rejects concrete mutations of the claimed formulas.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import itertools
import json
from pathlib import Path
import sys

import sympy as sp


MUTATIONS = (
    "none", "local-remainder", "budget-denominator", "endpoint-orientation",
    "phase-feasibility", "interior-multiplicity",
)


def product(values):
    result = Q(1)
    for value in values:
        result *= value
    return result


def local_terms(ds):
    return [(1 - a) * (1 - b) / b for a, b in zip(ds, ds[1:])]


def window_formula(ds, mutation="none"):
    r = len(ds) - 1
    multiplicity = 1 if mutation == "interior-multiplicity" else 2
    return ((1 - ds[0]) * (1 - ds[r])
            * product((1 - d) ** multiplicity for d in ds[1:r])
            / product(ds[1:]))


def exp_negative_budget(ds):
    return ds[0] * ds[-1] * product(d * d for d in ds[1:-1])


def maximizing_sequence(r, x, mutation="none"):
    if r < 1 or not Q(0) < x < Q(1, 2):
        raise ValueError("r must be positive and x must lie in (0,1/2)")
    first, last = 1 / (1 + 2 * x), 1 - 2 * x
    if mutation == "endpoint-orientation":
        first, last = last, first
    return [first] + [(1 - x) / (1 + x)] * (r - 1) + [last]


def maximum_formula(r, x, mutation="none"):
    endpoint = (1 - 2 * x * x if mutation == "budget-denominator"
                else 1 - 4 * x * x)
    return Q(4) ** r * x ** (2 * r) / (endpoint * (1 - x * x) ** (r - 1))


def phase_polynomial(y, squared_phases):
    return product(y + a for a in squared_phases)


def phase_feasible(k, squared_phases, mutation="none"):
    if mutation == "phase-feasibility":
        return k >= 0
    return k >= phase_polynomial(Q(0), squared_phases)


class Ledger:
    def __init__(self):
        self.records = []

    def check(self, name, actual, expected=True):
        good = bool(actual == expected)
        record = {"name": name, "passed": good}
        if not good:
            record["actual"] = str(actual)
            record["expected"] = str(expected)
        self.records.append(record)


def run(mutation):
    ledger = Ledger()
    a, b, p = sp.symbols("a b p")
    radicand_numerator = (1 - a * b) ** 2 - 4 * a * (1 - a) * (1 - b)
    remainder = ((1 - 2 * a + a * b) ** 2 if mutation != "local-remainder"
                 else (1 - 2 * a - a * b) ** 2)
    ledger.check("symbolic local comparison remainder",
                 sp.Poly(sp.expand(radicand_numerator - remainder), a, b).is_zero)
    ledger.check("symbolic incompatible equality at positive budget",
                 sp.expand((1 + p) ** 2 - 4 * p), sp.expand((p - 1) ** 2))

    # Independent multiplication of the local radius factors.
    fractions = [Q(1), Q(1, 2), Q(2, 3), Q(3, 7), Q(4, 5)]
    for r in range(1, 9):
        for shift in range(len(fractions)):
            ds = [fractions[(j + shift) % len(fractions)] for j in range(r + 1)]
            ledger.check(f"window factorization r={r} shift={shift}",
                         window_formula(ds, mutation), product(local_terms(ds)))

    for r in range(1, 9):
        for x in [Q(1, 20), Q(1, 9), Q(1, 4), Q(2, 5), Q(9, 20)]:
            ds = maximizing_sequence(r, x, mutation)
            raw_product = product(local_terms(ds))
            closed_product = maximum_formula(r, x, mutation)
            tag = f"r={r} x={x}"
            ledger.check(f"maximum expression {tag}", closed_product, raw_product)
            exponential_budget = ((1 - 2 * x) / (1 + 2 * x)
                                  * ((1 - x) / (1 + x)) ** (2 * (r - 1)))
            ledger.check(f"full budget exponential {tag}",
                         exp_negative_budget(ds), exponential_budget)
            lam = 1 / (2 * x)
            ledger.check(f"first multiplier equation {tag}",
                         ds[0] / (1 - ds[0]), lam)
            ledger.check(f"last multiplier equation {tag}",
                         1 / (1 - ds[-1]), lam)
            for j in range(1, r):
                ledger.check(f"interior multiplier equation {tag} j={j}",
                             1 + 2 * ds[j] / (1 - ds[j]), 2 * lam)
            weights = [1] + [2] * (r - 1) + [1]
            for j, (d, weight) in enumerate(zip(ds, weights)):
                # Exact d-coordinate value of the t-coordinate Hessian entry.
                entry = -weight * d / (1 - d) ** 2
                ledger.check(f"negative Hessian diagonal {tag} j={j}", entry < 0)
            for c in [Q(9, 10), Q(19, 20), Q(21, 20), Q(11, 10)]:
                competitor = list(ds)
                competitor[0] *= c
                competitor[-1] /= c
                if all(Q(0) < d <= 1 for d in competitor):
                    ledger.check(f"endpoint perturbation preserves budget {tag} c={c}",
                                 exp_negative_budget(competitor), exp_negative_budget(ds))
                    ledger.check(f"endpoint perturbation strictly decreases {tag} c={c}",
                                 product(local_terms(competitor)) < closed_product)
                if r > 1:
                    competitor = list(ds)
                    competitor[0] *= c * c
                    competitor[1] /= c
                    if all(Q(0) < d <= 1 for d in competitor):
                        ledger.check(f"mixed perturbation preserves budget {tag} c={c}",
                                     exp_negative_budget(competitor), exp_negative_budget(ds))
                        ledger.check(f"mixed perturbation strictly decreases {tag} c={c}",
                                     product(local_terms(competitor)) < closed_product)
            if r == 1:
                # For r=1, exp(B) is rational, so sinh^2(B/2) is rational.
                z = exponential_budget
                ledger.check(f"one-step sinh equality {tag}",
                             maximum_formula(r, x, mutation), (1 - z) ** 2 / (4 * z))
            else:
                local_equalities = [1 - 2 * aa + aa * bb == 0
                                    for aa, bb in zip(ds, ds[1:])]
                pair_products = [aa * bb for aa, bb in zip(ds, ds[1:])]
                jensen_equal = all(q == pair_products[0] for q in pair_products)
                ledger.check(f"strict sinh equality excluded {tag}",
                             not (all(local_equalities) and jensen_equal))

    # Fixed four-endpoint optimizer and exact scalar realization.
    for r in range(2, 9):
        for alpha, beta, u in itertools.product([Q(1, 3), Q(3, 4)], repeat=3):
            ds = [alpha] + [u] * (r - 1) + [beta]
            t = u ** (r - 1)
            fixed_formula = ((1 - alpha) * (1 - beta) / (beta * t)
                             * (1 - u) ** (2 * (r - 1)))
            tag = f"r={r} alpha={alpha} beta={beta} u={u}"
            ledger.check(f"fixed endpoint maximum {tag}", fixed_formula,
                         product(local_terms(ds)))
            if r > 2:
                competitor = list(ds)
                c = Q(9, 10)
                competitor[1] *= c
                competitor[2] /= c
                ledger.check(f"fixed endpoint interior product {tag}",
                             product(competitor[1:-1]), t)
                ledger.check(f"fixed endpoint strict perturbation {tag}",
                             product(local_terms(competitor)) < fixed_formula)
            epsilon_squared = Q(11, 5)
            terms = local_terms(ds)
            ratios = [epsilon_squared / term for term in terms]
            omega = [Q(7)]
            for ratio in ratios:
                omega.append(omega[-1] * ratio)
            volumes = [Q(13)]
            for d in ds:
                volumes.append(volumes[-1] * d)
            omega_ratio = omega[-1] / omega[0]
            ledger.check(f"literal initial monic norm {tag}", omega[0], Q(7))
            ledger.check(f"literal initial quotient volume {tag}", volumes[0], Q(13))
            ledger.check(f"realized norm endpoint product {tag}",
                         omega_ratio * fixed_formula, epsilon_squared ** r)
            for j, term in enumerate(terms):
                ledger.check(f"realized local identity {tag} j={j}",
                             omega[j + 1] / omega[j] * term, epsilon_squared)

    # Zero endpoints, all-unit budget, and the separate r=1 formula.
    for r in range(1, 9):
        for zero_at in range(r + 1):
            ds = [Q(2, 3)] * (r + 1)
            ds[zero_at] = Q(1)
            terms = local_terms(ds)
            ledger.check(f"zero contraction radius product r={r} at={zero_at}",
                         product(terms), Q(0))
            ledger.check(f"zero contraction allowance minimum r={r} at={zero_at}",
                         min(terms), Q(0))
        ones = [Q(1)] * (r + 1)
        ledger.check(f"zero budget domain r={r}", exp_negative_budget(ones), Q(1))
        ledger.check(f"zero budget objective r={r}", window_formula(ones, mutation), Q(0))
    for alpha, beta in itertools.product([Q(1), Q(1, 2), Q(2, 3)], repeat=2):
        ledger.check(f"single-step complete formula alpha={alpha} beta={beta}",
                     window_formula([alpha, beta], mutation), (1 - alpha) * (1 - beta) / beta)

    # Exact polynomial feasibility and strict monotonicity, with repeated zeros.
    for r in range(1, 9):
        for zero_count in range(r + 1):
            phases_squared = [Q(0)] * zero_count + [Q(j + 1, 3) ** 2
                                                     for j in range(r - zero_count)]
            p0 = phase_polynomial(Q(0), phases_squared)
            ledger.check(f"phase threshold equality at zero r={r} zeros={zero_count}",
                         phase_feasible(p0, phases_squared, mutation))
            for y in [Q(1, 7), Q(2, 3), Q(9, 2)]:
                k = phase_polynomial(y, phases_squared)
                tag = f"r={r} zeros={zero_count} y={y}"
                ledger.check(f"positive threshold feasibility {tag}",
                             phase_feasible(k, phases_squared, mutation))
                ledger.check(f"threshold strictly above P0 {tag}", k > p0)
                ledger.check(f"threshold strict lower bracket {tag}",
                             phase_polynomial(y / 2, phases_squared) < k)
                ledger.check(f"threshold strict upper bracket {tag}",
                             phase_polynomial(y + Q(1, 9), phases_squared) > k)
            if p0 > 0:
                ledger.check(f"infeasible phase budget rejected r={r}",
                             phase_feasible(p0 / 2, phases_squared, mutation), False)

    return ledger.records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mutation", choices=MUTATIONS, default="none")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    records = run(args.mutation)
    failures = [row for row in records if not row["passed"]]
    result = {
        "schema": "endpoint-product-independent-checks-v1",
        "mutation": args.mutation,
        "python_optimized": bool(sys.flags.optimize),
        "python_version": sys.version.split()[0],
        "sympy_version": sp.__version__,
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "check_count": len(records),
        "passed_count": len(records) - len(failures),
        "failed_count": len(failures),
        "passed": not failures,
        "records": records,
    }
    if args.output:
        args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in (
        "mutation", "python_optimized", "check_count", "passed_count",
        "failed_count", "passed", "checker_sha256")}, sort_keys=True))
    if failures:
        print(json.dumps({"first_failures": failures[:5]}, sort_keys=True))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
