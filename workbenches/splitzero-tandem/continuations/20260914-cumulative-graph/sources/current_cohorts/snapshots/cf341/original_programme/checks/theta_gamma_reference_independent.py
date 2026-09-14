"""Exact finite calibration of the Gamma-reference bridge.

This script proves no assertion about zeta values or zeros.  Its rational
polynomial-weight models check constants, coordinate maps, complete jets,
determinant quotients, and critical-root cancellation independently of the
analytic proof.  Every check remains enabled under python -O.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as S

t, s, v, z = S.symbols("t s v z")
HALF = S.Rational(1, 2)
checks: list[dict] = []


def eq(label, left, right):
    difference = left - right
    if isinstance(difference, S.MatrixBase):
        passed = all(S.simplify(x) == 0 for x in difference)
    else:
        passed = S.simplify(difference) == 0
    checks.append({"label": label, "passed": bool(passed)})


def condition(label, passed):
    checks.append({"label": label, "passed": bool(passed)})


def polys(lam, nmax):
    values = [S.Integer(1)]
    if nmax:
        values.append(t)
    for n in range(1, nmax):
        values.append(S.expand(t * values[n] - n * (n + 2 * lam - 1) * values[n - 1]))
    return values


def moments(lam, degree):
    # Fourier/Beta proof gives this moment generating function divided by
    # its exact mass 2**(1-2*lam)*Gamma(2*lam).  No floating point is used.
    coefficients = S.Poly(S.series(S.cos(v) ** (-2 * lam), v, 0, degree + 1).removeO(), v)
    return [S.factorial(j) * coefficients.nth(j) for j in range(degree + 1)]


def integrate(poly, values):
    polynomial = S.Poly(S.expand(poly), t)
    return S.expand(sum(coefficient * values[power[0]] for power, coefficient in polynomial.terms()))


def gram(weight, values, n):
    return S.Matrix(n + 1, n + 1, lambda i, j: integrate(t ** (i + j) * weight, values))


def affine_matrix(n):
    return S.Matrix(n + 1, n + 1, lambda row, col: S.binomial(col, row) * HALF ** (col - row) * S.I ** row if row <= col else 0)


def companion(poly, variable):
    p = S.Poly(poly, variable)
    degree = p.degree()
    return S.Matrix(degree, degree, lambda row, col: S.rem(variable ** (col + 1), p.as_expr(), variable).coeff(variable, row))


def confluent(rows, variable, n):
    return S.Matrix([[S.diff(variable ** col, variable, order).subs(variable, root) / S.factorial(order) for col in range(n + 1)] for root, order in rows])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--negative-control", action="store_true")
    args = parser.parse_args()

    families = {}
    for lam in (S.Rational(1, 4), S.Rational(3, 4), S.Rational(5, 4)):
        family = polys(lam, 10)
        families[lam] = family
        values = moments(lam, 24)
        for n in range(11):
            eq(f"lambda={lam}: leading coefficient b_{n}", S.Poly(family[n], t).LC(), 1)
            eq(f"lambda={lam}: parity b_{n}", family[n].subs(t, -t), (-1) ** n * family[n])
            for m in range(n + 1):
                expected = S.factorial(n) * S.rf(2 * lam, n) if n == m else 0
                if args.negative_control and lam == S.Rational(1, 4) and n == m == 1:
                    expected = -expected
                eq(f"lambda={lam}: orthogonality ({m},{n}) with original mass retained", integrate(family[m] * family[n], values), expected)

    for n in range(11):
        connection = sum(S.factorial(n) / S.factorial(n - 2 * k) * S.binomial(HALF, k) * families[S.Rational(3, 4)][n - 2 * k] for k in range(n // 2 + 1))
        inverse = sum(S.factorial(n) / S.factorial(n - 2 * k) * S.binomial(-HALF, k) * families[S.Rational(1, 4)][n - 2 * k] for k in range(n // 2 + 1))
        eq(f"parameter connection n={n}", families[S.Rational(1, 4)][n], connection)
        eq(f"inverse parameter connection n={n}", families[S.Rational(3, 4)][n], inverse)

    lam = S.Rational(1, 4)
    values = moments(lam, 24)
    weight = (1 + t ** 2) ** 2
    determinants = { -1: S.Integer(1) }
    norm_values = {}
    original_grams = {}
    for n in range(7):
        moment_matrix = gram(weight, values, n)
        original_grams[n] = moment_matrix
        family = families[lam]
        raw_reference = S.Matrix(n + 1, n + 1, lambda i, j: integrate(family[i] * family[j] * weight, values))
        reference_norms = [S.factorial(j) * S.rf(2 * lam, j) for j in range(n + 1)]
        # This determinant is exactly det J_N: all common original masses
        # cancel in J, while actual monic norms below retain that mass.
        determinant = S.factor(raw_reference.det() / S.prod(reference_norms))
        determinants[n] = determinant
        if n == 0:
            monic = S.Integer(1)
        else:
            lower = moment_matrix[:n, :n]
            coefficients = -lower.inv() * moment_matrix[:n, n]
            monic = t ** n + sum(coefficients[j] * t ** j for j in range(n))
        norm = integrate(monic * monic * weight, values)
        norm_values[n] = norm
        eq(f"weighted determinant monic norm n={n}", norm, reference_norms[n] * determinant / determinants[n - 1])
        condition(f"positive weighted determinant n={n}", determinant > 0)
        # Full affine coordinate transform retains phases and every entry.
        a = affine_matrix(n)
        direct_s = S.Matrix(n + 1, n + 1, lambda i, j: integrate((HALF - S.I * t) ** i * (HALF + S.I * t) ** j * weight, values))
        eq(f"original s Gram congruence n={n}", direct_s, a.conjugate().T * moment_matrix * a)
        eq(f"unimodular affine determinant n={n}", a.det() * S.conjugate(a.det()), 1)
        original_s_monic = S.expand(S.I ** n * monic.subs(t, -S.I * (s - HALF)))
        eq(f"original s monicity n={n}", S.Poly(original_s_monic, s).LC(), 1)
        eq(f"monic phase restoration n={n}", S.expand(S.I ** (-n) * original_s_monic.subs(s, HALF + S.I * t)), monic)
        if n >= 1:
            eq(f"weighted recurrence norm ratio n={n}", norm_values[n] / norm_values[n - 1], n * (n - HALF) * determinants[n] * determinants[n - 2] / determinants[n - 1] ** 2)

    # Complete packet with a double critical zero and a four-point
    # conjugation/reflection orbit.  These are calibration roots, not
    # assertions that xi vanishes at these points.
    h_s = S.expand((s - HALF) ** 2 * ((s - S.Rational(1, 4)) ** 2 + 1) * ((s - S.Rational(3, 4)) ** 2 + 1))
    degree = S.degree(h_s, s)
    h_t = S.expand(S.I ** (-degree) * h_s.subs(s, HALF + S.I * t))
    rows_s = [(HALF, 0), (HALF, 1), (S.Rational(1, 4) + S.I, 0), (S.Rational(1, 4) - S.I, 0), (S.Rational(3, 4) + S.I, 0), (S.Rational(3, 4) - S.I, 0)]
    rows_t = [(-S.I * (root - HALF), order) for root, order in rows_s]
    n = 6
    a = affine_matrix(n)
    jets_s, jets_t = confluent(rows_s, s, n), confluent(rows_t, t, n)
    jet_phases = S.diag(*[S.I ** order for _, order in rows_s])
    eq("full confluent affine intertwiner", jets_t * a, jet_phases * jets_s)
    metric_t = original_grams[n]
    metric_s = a.conjugate().T * metric_t * a
    kernel_s = jets_s * metric_s.inv() * jets_s.conjugate().T
    kernel_t = jets_t * metric_t.inv() * jets_t.conjugate().T
    eq("full confluent kernel congruence", kernel_t, jet_phases * kernel_s * jet_phases.conjugate().T)
    quotient_map = affine_matrix(degree - 1)
    generator_s, generator_t = companion(h_s, s), companion(h_t, t)
    eq("complete quotient generator intertwiner", quotient_map * generator_s, (HALF * S.eye(degree) + S.I * generator_t) * quotient_map)
    unit_s = S.eye(degree) + (generator_s - HALF * S.eye(degree)) ** 2
    unit_t = S.eye(degree) - generator_t ** 2
    eq("full local polynomial-unit intertwiner", quotient_map * unit_s, unit_t * quotient_map)
    condition("local polynomial unit is invertible", unit_s.det() != 0)
    line_h = S.expand(h_s.subs(s, HALF + S.I * t))
    line_amplitude = line_h * (1 + t ** 2)
    eq("critical packet quotient cancellation", S.cancel(line_amplitude / line_h), 1 + t ** 2)
    eq("monic denominator phase retained", S.cancel(line_amplitude / h_t), S.I ** degree * (1 + t ** 2))
    eq("double critical root retained", S.Poly(line_h, t).coeff_monomial(t), 0)
    eq("critical quotient germ value", S.cancel(line_amplitude / line_h).subs(t, 0), 1)
    eq("critical quotient full derivative", S.diff(S.cancel(line_amplitude / line_h), t, 2).subs(t, 0) / S.factorial(2), 1)

    failures = [check for check in checks if not check["passed"]]
    payload = {
        "schema": "split-zero-gamma-reference-independent-v1",
        "sympy_version": S.__version__,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "mode": "negative-control" if args.negative_control else "ordinary",
        "scope": "Exact rational polynomial calibrations only. No numerical zeta claim, zero-location assertion, asymptotic estimate, or formal proof certificate.",
        "original_measure_mass": "2^(1-2 lambda) Gamma(2 lambda); symbolic calibration moments divide by this explicitly retained mass",
        "checks": len(checks), "failures": failures,
        "passed": not failures, "details": checks,
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"checks": len(checks), "failed": len(failures), "output": str(output)}))
    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
