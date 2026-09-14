#!/usr/bin/env python3
"""Reproducible checks for JT6--JT10 in tex/jet_topology.tex.

Exact algebra checks and numerical quadratures are reported separately.  The
quadratures test specified functions/parameters; they do not prove the analytic
theorems, the density assertion, statements about actual zeta zeros, or RH.
No Python assertions are used: all checks run under python -O as well.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
from datetime import datetime, timezone

import mpmath as mp
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
mp.mp.dps = 65
TOL = mp.mpf("1e-44")
RESULTS = []


def record(name, kind, passed, **evidence):
    RESULTS.append({"name": name, "kind": kind, "passed": bool(passed), **evidence})


def exact_zero(expr):
    # This only decides equality of the fully retained expressions; it does not
    # replace the source coordinates, factorials, weight, or conjugation.
    return sp.cancel(sp.expand(expr)) == 0


def exact(name, lhs, rhs=0):
    record(name, "exact_symbolic", exact_zero(lhs - rhs),
           lhs=str(lhs), rhs=str(rhs))


def exact_matrix(name, lhs, rhs):
    record(name, "exact_symbolic", lhs.shape == rhs.shape and
           all(exact_zero(lhs[i, j] - rhs[i, j])
               for i in range(lhs.rows) for j in range(lhs.cols)),
           shape=list(lhs.shape))


def close(name, actual, expected):
    error = abs(actual - expected)
    scale = max(mp.mpf(1), abs(actual), abs(expected))
    record(name, "numerical_quadrature", error <= TOL * scale,
           actual=mp.nstr(actual, 55), expected=mp.nstr(expected, 55),
           absolute_error=mp.nstr(error, 8), scaled_tolerance=str(TOL))


def negative(name, correct, wrong):
    if isinstance(correct, sp.Basic) and isinstance(wrong, sp.Basic):
        detected = not exact_zero(correct - wrong)
        kind = "negative_control_exact"
        distance = str(sp.cancel(correct - wrong))
    else:
        distance_value = abs(correct - wrong)
        detected = distance_value > mp.mpf("1e-8")
        distance = mp.nstr(distance_value, 20)
        kind = "negative_control_numerical"
    record(name, kind, detected, discrepancy=distance)


def number(expr):
    real, imag = sp.expand_complex(expr).as_real_imag()
    return mp.mpc(str(sp.N(real, 70)), str(sp.N(imag, 70)))


def integrate(fun):
    return mp.quad(fun, [-mp.inf, -2, 0, 2, mp.inf])


def inner(f, h, a):
    return integrate(lambda y: mp.conj(f(y)) * h(y) * mp.exp(2 * a * abs(y)))


def riesz(rho, k, a):
    return lambda y: (y ** k / mp.factorial(k) *
                      mp.exp((mp.conj(rho) - mp.mpf("0.5")) * y - 2 * a * abs(y)))


def jet(f, rho, k):
    return integrate(lambda y: f(y) * y ** k / mp.factorial(k) *
                     mp.exp((rho - mp.mpf("0.5")) * y))


def gram_entry(a, rho_i, k, rho_j, l):
    z = rho_i + sp.conjugate(rho_j) - 1
    n = k + l
    return (sp.factorial(n) / (sp.factorial(k) * sp.factorial(l)) *
            (1 / (2 * a - z) ** (n + 1) +
             (-1) ** n / (2 * a + z) ** (n + 1)))


def check_jt6():
    y = sp.Symbol("y", real=True, nonnegative=True)
    rate = sp.Symbol("rate", positive=True)
    moments = {}
    for n in range(7):
        moments[n] = sp.integrate(y ** n * sp.exp(-rate * y), (y, 0, sp.oo))
        exact(f"JT6 gamma half-line moment n={n}", moments[n],
              sp.factorial(n) / rate ** (n + 1))
    for a, b in [(sp.Rational(3, 4), sp.Rational(1, 6)),
                 (sp.Rational(2, 3), -sp.Rational(1, 4)),
                 (sp.Rational(1, 5), sp.S.Zero)]:
        for k in range(4):
            exact_integral = (moments[2 * k].subs(rate, 2 * (a - b)) +
                              moments[2 * k].subs(rate, 2 * (a + b))) / sp.factorial(k) ** 2
            formula = sp.factorial(2 * k) / sp.factorial(k) ** 2 * (
                1 / (2 * (a - b)) ** (2 * k + 1) +
                1 / (2 * (a + b)) ** (2 * k + 1))
            exact(f"JT6 norm a={a}, b={b}, k={k}", exact_integral, formula)
            rho = number(sp.Rational(1, 2) + b + 3 * sp.I / 7)
            r = riesz(rho, k, mp.re(number(a)))
            close(f"JT6 Riesz norm quadrature a={a}, b={b}, k={k}",
                  inner(r, r, mp.re(number(a))), number(formula))
    a, b, k = sp.Rational(3, 4), sp.Rational(1, 6), 2
    norm = sp.factorial(2 * k) / sp.factorial(k) ** 2 * (
        1 / (2 * (a - b)) ** (2 * k + 1) + 1 / (2 * (a + b)) ** (2 * k + 1))
    negative("JT6 detects omitted Taylor factorial squared", norm,
             norm * sp.factorial(k) ** 2)
    length = sp.Symbol("L", positive=True)
    for k in range(4):
        truncated = sp.integrate(y ** (2 * k) / sp.factorial(k) ** 2, (y, 0, length))
        exact(f"JT6 boundary nondecaying end k={k}", truncated,
              length ** (2 * k + 1) / ((2 * k + 1) * sp.factorial(k) ** 2))
        exact(f"JT6 boundary doubling growth k={k}", truncated.subs(length, 2 * length),
              2 ** (2 * k + 1) * truncated)


def check_jt7_jt8():
    a = sp.Rational(3, 4)
    am = mp.re(number(a))
    rho1, rho2 = sp.Rational(2, 3) + 2 * sp.I / 5, sp.Rational(1, 3) - 3 * sp.I / 7
    indices = [(rho1, 0), (rho1, 1), (rho2, 0), (rho2, 1)]
    C = sp.Matrix([[gram_entry(a, ri, k, rj, l) for rj, l in indices]
                   for ri, k in indices]).applyfunc(sp.cancel)
    z, aa = sp.symbols("z aa")
    for k in range(4):
        for l in range(4):
            differentiated = sp.diff(1 / (2 * aa - z) + 1 / (2 * aa + z), z, k + l)
            differentiated /= sp.factorial(k) * sp.factorial(l)
            formula = (sp.factorial(k + l) / (sp.factorial(k) * sp.factorial(l)) *
                       (1 / (2 * aa - z) ** (k + l + 1) +
                        (-1) ** (k + l) / (2 * aa + z) ** (k + l + 1)))
            exact(f"JT7 differentiated Cauchy kernel k={k}, l={l}", differentiated, formula)
    exact_matrix("JT7 Hermitian Gram in stated index order", C, C.conjugate().T)
    for n in range(1, len(indices) + 1):
        determinant = sp.cancel(C[:n, :n].det(method="domain-ge"))
        record(f"JT7 positive leading principal minor n={n}", "exact_symbolic",
               determinant.is_positive is True, determinant=str(determinant))
    vectors = [riesz(number(rho), k, am) for rho, k in indices]
    for i, (rho, k) in enumerate(indices):
        for j in range(len(indices)):
            expected = number(C[i, j])
            close(f"JT7 Riesz inner product row={i}, col={j}", inner(vectors[i], vectors[j], am), expected)
            close(f"JT7 jet of Riesz vector row={i}, col={j}", jet(vectors[j], number(rho), k), expected)
    k, l = 2, 1
    zij = rho1 + sp.conjugate(rho2) - 1
    expected = gram_entry(a, rho1, k, rho2, l)
    wrong_sign = sp.factorial(k + l) / (sp.factorial(k) * sp.factorial(l)) * (
        1 / (2 * a - zij) ** (k + l + 1) + 1 / (2 * a + zij) ** (k + l + 1))
    negative("JT7 detects lost negative-half-line sign", expected, wrong_sign)
    wrong_z = rho1 + rho2 - 1
    wrong_conj = sp.factorial(k + l) / (sp.factorial(k) * sp.factorial(l)) * (
        1 / (2 * a - wrong_z) ** (k + l + 1) +
        (-1) ** (k + l) / (2 * a + wrong_z) ** (k + l + 1))
    negative("JT7 detects omitted centre conjugation", expected, wrong_conj)
    # The cross-centre order-zero entry is real for these reflected real parts;
    # the order-one entry is non-real and therefore detects the transpose.
    negative("JT7 detects transposed index convention", C[0, 3], C[3, 0])
    negative("JT7 detects omitted Taylor factorials", expected,
             expected * sp.factorial(k) * sp.factorial(l))
    Cinv = C.inv().applyfunc(sp.cancel)
    exact_matrix("JT8 exact right inverse matrix identity", C * Cinv, sp.eye(len(indices)))
    exact_matrix("JT8 exact section norm matrix identity", Cinv.conjugate().T * C * Cinv, Cinv)
    u = sp.Matrix([2 + 3 * sp.I, -1 + sp.I / 2, sp.Rational(3, 7) - 2 * sp.I,
                   -sp.Rational(2, 3) + sp.I / 5])
    coefficients = Cinv * u
    wm = [number(coefficient) for coefficient in coefficients]
    section = lambda y: sum(w * r(y) for w, r in zip(wm, vectors))
    for i, (rho, k) in enumerate(indices):
        close(f"JT8 section jet quadrature coordinate={i}", jet(section, number(rho), k), number(u[i]))
    norm_formula = (u.conjugate().T * Cinv * u)[0]
    close("JT8 section norm quadrature", inner(section, section, am), number(norm_formula))
    Cmp = mp.matrix([[number(Cinv[i, j]) for j in range(len(indices))] for i in range(len(indices))])
    f = lambda y: mp.exp(-(y - mp.mpf(1) / 3) ** 2) * (1 + 1j * y + y ** 2 / 7)
    jf = mp.matrix([jet(f, number(rho), k) for rho, k in indices])
    w = Cmp * jf
    projection = lambda y: sum(w[i] * vectors[i](y) for i in range(len(indices)))
    residual = lambda y: f(y) - projection(y)
    for i, (rho, k) in enumerate(indices):
        close(f"JT8 orthogonal residual jet coordinate={i}", jet(residual, number(rho), k), mp.mpf(0))
    close("JT8 orthogonal residual pairing", inner(projection, residual, am), mp.mpf(0))
    energy = (jf.H * Cmp * jf)[0]
    close("JT8 Pythagorean identity on Gaussian polynomial", inner(f, f, am),
          inner(residual, residual, am) + energy)
    wrong_inverse = mp.matrix([[number(C[i, j]) for j in range(len(indices))] for i in range(len(indices))])
    wrong_section_jets = wrong_inverse * wrong_inverse * mp.matrix([number(entry) for entry in u])
    negative("JT8 detects using Gram instead of inverse", wrong_section_jets[0], number(u[0]))


def check_jt10():
    y = sp.Symbol("y", real=True)
    f_expr = sp.exp(-(y - sp.Rational(1, 3)) ** 2) * (1 + sp.I * y + y ** 2 / 7)
    h_expr = sp.exp(-sp.Rational(3, 2) * (y + sp.Rational(1, 4)) ** 2) * (
        2 - y / 5 + sp.I * (y ** 2 + 1) / 3)
    d_f_expr = f_expr / 2 - sp.diff(f_expr, y)
    d_h_expr = h_expr / 2 - sp.diff(h_expr, y)
    exact("JT10 sesquilinear product derivative before integration",
          sp.conjugate(d_f_expr) * h_expr + sp.conjugate(f_expr) * d_h_expr -
          sp.conjugate(f_expr) * h_expr, -sp.diff(sp.conjugate(f_expr) * h_expr, y))
    f, h, df, dh = [sp.lambdify(y, expr, "mpmath") for expr in
                     [f_expr, h_expr, d_f_expr, d_h_expr]]
    for a in [mp.mpf(0), mp.mpf(1) / 5, mp.mpf(3) / 4]:
        lhs = inner(df, h, a) + inner(f, dh, a) - inner(f, h, a)
        sigma_pairing = inner(f, lambda t: mp.sign(t) * h(t), a)
        rhs = 2 * a * sigma_pairing
        close(f"JT10 independent weighted integration a={mp.nstr(a, 10)}", lhs, rhs)
        if a > 0:
            negative(f"JT10 detects reversed weight derivative sign a={a}", lhs, -rhs)
            negative(f"JT10 detects omitted factor two a={a}", lhs, a * sigma_pairing)
            no_conjugation_rhs = 2 * a * integrate(
                lambda t: f(t) * mp.sign(t) * h(t) * mp.exp(2 * a * abs(t)))
            negative(f"JT10 detects bilinear form replacing inner product a={a}", lhs, no_conjugation_rhs)
    record("JT10 test-function specification", "scope_metadata", True,
           f_log=str(f_expr), h_log=str(h_expr), D_log="1/2 - d/dy",
           F_original="x^(-1/2) f_log(log(x))", H_original="x^(-1/2) h_log(log(x))",
           measure_original="exp(2*a*abs(log(x))) dx",
           inner_product="conjugate-linear first argument")


def main():
    for group in [check_jt6, check_jt7_jt8, check_jt10]:
        try:
            print(f"Running {group.__name__}...", flush=True)
            group()
        except Exception as exc:
            record(group.__name__ + " raised an exception", "execution_error", False,
                   error_type=type(exc).__name__, message=str(exc))
    source = ROOT / "tex" / "jet_topology.tex"
    categories = sorted({result["kind"] for result in RESULTS})
    payload = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "python_optimization_level": sys.flags.optimize,
        "python_version": sys.version,
        "sympy_version": sp.__version__, "mpmath_version": mp.__version__,
        "working_precision_decimal_digits": mp.mp.dps,
        "source_file": "tex/jet_topology.tex",
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "JT6 exact moments and sample norms; JT7 symbolic kernel, rational Gram, and sample quadratures; JT8 exact finite matrices and independent sample sections; JT10 exact product identity and Gaussian-polynomial quadratures.",
        "analytic_proof_status": "These computations support the stated finite identities and test examples. Analytic proofs are in the TeX; numerical checks establish neither general analytic theorems nor RH.",
        "passed": sum(result["passed"] for result in RESULTS),
        "total": len(RESULTS),
        "all_passed": all(result["passed"] for result in RESULTS),
        "categories": {kind: {"passed": sum(r["passed"] for r in RESULTS if r["kind"] == kind),
                               "total": sum(r["kind"] == kind for r in RESULTS)} for kind in categories},
        "checks": RESULTS,
    }
    destination = ROOT / "checks" / ("jet_topology_optimized.json" if sys.flags.optimize else "jet_topology.json")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({key: payload[key] for key in ["passed", "total", "all_passed", "categories"]}, indent=2))
    print(f"Receipt: {destination}")
    for result in RESULTS:
        if not result["passed"]:
            print("FAIL: " + json.dumps(result))
    return 0 if payload["all_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
