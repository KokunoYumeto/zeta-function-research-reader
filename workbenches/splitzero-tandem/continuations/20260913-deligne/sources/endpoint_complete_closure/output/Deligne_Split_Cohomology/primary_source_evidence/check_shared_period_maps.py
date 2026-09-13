"""Independent finite regression for shared XD1--26 and DT1--13.

Declared polynomial/matrix fixtures, not arithmetic zeta packets. No network,
Lean, quadrature, publication, or modification of owner sources. The general
proof is the owner's retained TeX, reviewed separately by the parent.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import unittest
from pathlib import Path

import sympy as s

X, u, t, a = s.symbols("X u t a")
MUTATION = None


def equal(left, right=0):
    if isinstance(left, s.MatrixBase):
        return all(s.cancel(s.expand(v)) == 0 for v in left - right)
    return s.cancel(s.expand(left - right)) == 0


def col(poly, q):
    return s.Matrix([s.expand(poly).coeff(X, b) for b in range(q)])


def companion(f):
    q = s.degree(f, X)
    return s.Matrix.hstack(*[col(s.rem(X ** (b + 1), f, X), q)
                             for b in range(q)])


def twisted_remainder(poly, f):
    rem = s.expand(poly)
    while rem != 0 and s.degree(rem, X) >= s.degree(f, X):
        p = s.Poly(rem, X)
        quotient = p.LC() * X ** (p.degree() - s.degree(f, X))
        rem = s.expand(rem - f * quotient - u * s.diff(quotient, X))
    return rem


def matrix_poly(poly, mat):
    q = mat.rows
    return sum((coef * mat ** power[0]
                for power, coef in s.Poly(poly, X).terms()), s.zeros(q))


def fixture(q):
    return X ** q + sum(s.Rational(b + 1, b + 2) * X ** b
                       for b in range(q))


class SharedMaps(unittest.TestCase):
    def test_twisted_reduction_exact_and_strict_degree(self):
        for q in range(1, 6):
            f = fixture(q) - t
            for m in range(1, q + 1):
                for b in range(q):
                    quotient, rem = s.div(X ** (m + b), f, X)
                    correction = -u * s.diff(quotient, X)
                    self.assertTrue(equal(twisted_remainder(X ** (m + b), f),
                                          rem + correction))
                    self.assertTrue(correction == 0 or s.degree(correction, X) < b)

    def test_connection_trace_matches_ordinary_companion(self):
        for q in range(1, 6):
            f = fixture(q) - t
            mat = companion(f)
            for m in range(1, q + 1):
                twisted = s.Matrix.hstack(*[
                    col(twisted_remainder(X ** (m + b), f), q)
                    for b in range(q)])
                self.assertTrue(equal(s.trace(twisted), s.trace(mat ** m)))

    def test_full_potential_gradient(self):
        for q in range(1, 5):
            cs = s.symbols(f"c0:{q}")
            chi = X ** q + sum(cs[b] * X ** b for b in range(q))
            phi = s.integrate(chi, X) - t * X
            mat = companion(chi - t)
            potential = s.expand(s.trace(matrix_poly(phi, mat)))
            for b, c in enumerate(cs):
                target = s.trace(mat ** (b + 1)) / (b + 1)
                self.assertTrue(equal(s.diff(potential, c), target))
            sign = 1 if MUTATION == "flip-period-sign" else -1
            self.assertTrue(equal(s.diff(potential, t), sign * s.trace(mat)))

    def test_repeated_root_potential_counts_all_multiplicities(self):
        lam = s.symbols("lam")
        for q in range(1, 6):
            chi = s.expand((X - lam) ** q)
            phi = s.integrate(chi, X)
            mat = companion(chi)
            self.assertTrue(equal(s.trace(matrix_poly(phi, mat)),
                                  -q * (-lam) ** (q + 1) / (q + 1)))

    def test_translation_matrix_and_generator(self):
        for q in range(1, 6):
            chi = fixture(q)
            ca = s.Matrix(q, q, lambda r, b:
                          s.binomial(b, r) * a ** (b - r) if r <= b else 0)
            self.assertTrue(equal(ca * ca.subs(a, -a), s.eye(q)))
            self.assertEqual(ca.det(), 1)
            self.assertTrue(equal(ca * companion(chi.subs(X, X - a) - t),
                                  (companion(chi - t) + a * s.eye(q)) * ca))

    def test_translation_potential_constant_is_retained(self):
        for q in range(1, 6):
            phi = s.integrate(fixture(q), X)
            constant = 0 if MUTATION == "drop-potential-constant" else phi.subs(X, -a)
            translated = phi.subs(X, X - a) - constant
            actual = translated.subs(X, X + a) - t * (X + a)
            target = phi - t * X - phi.subs(X, -a) - t * a
            self.assertTrue(equal(actual, target))

    def test_determinant_potential_translation_with_multiplicity(self):
        for q in range(1, 5):
            chi = fixture(q)
            phi = s.integrate(chi, X)
            phia = s.expand(phi.subs(X, X - a) - phi.subs(X, -a))
            fa = s.trace(matrix_poly(phia - t * X,
                                    companion(chi.subs(X, X - a) - t)))
            f0 = s.trace(matrix_poly(phi - t * X, companion(chi - t)))
            self.assertTrue(equal(fa - f0, q * (-phi.subs(X, -a) - t * a)))

    def test_fixed_ray_phase_gram(self):
        zeta = s.symbols("zeta")
        for q in range(1, 7):
            d = q + 1
            cyclo = s.cyclotomic_poly(d, zeta)
            gram = s.zeros(q)
            for l in range(1, d):
                for m in range(1, d):
                    expression = sum(
                        zeta ** ((j * (m - l)) % d)
                        - zeta ** ((-j * l) % d)
                        - zeta ** ((j * m) % d) + 1 for j in range(d))
                    gram[l - 1, m - 1] = s.rem(expression, cyclo, zeta)
            self.assertEqual(gram, d * (s.eye(q) + s.ones(q)))
            self.assertEqual(gram.det(), d ** d)

    def test_rank_one_orientation_and_potential(self):
        lam = s.symbols("lam")
        mat = companion(X - lam - t)
        potential = s.trace(matrix_poly(X ** 2 / 2 - (lam + t) * X, mat))
        self.assertTrue(equal(potential, -(lam + t) ** 2 / 2))
        # Gamma_1=-ell_0+ell_1 has phase -i at real u>0.
        self.assertEqual(s.exp(s.I * s.pi / 2) * ((-1) - 1), -2 * s.I)

    def test_original_metric_and_control_translation(self):
        for q in (2, 3):
            aa = 1 + 2 * s.I
            ca = s.Matrix(q, q, lambda r, b:
                          s.binomial(b, r) * aa ** (b - r) if r <= b else 0)
            mat = companion(fixture(q))
            mata = ca.inv() * (mat + aa * s.eye(q)) * ca
            lower = s.eye(q) + s.ones(q, 1) * s.ones(1, q)
            gram = lower.H * lower + s.eye(q)
            grama = ca.H * gram * ca
            k = 5
            control = mat.H * gram + gram * mat - k * gram
            controla = mata.H * grama + grama * mata - k * grama
            self.assertTrue(equal(controla,
                                  ca.H * (control + (aa + s.conjugate(aa)) * gram) * ca))
            self.assertTrue(equal(s.trace(grama.inv() * controla),
                                  s.trace(gram.inv() * control) + 2 * q))

    def test_two_metric_period_comparison_cancellation(self):
        q = 3
        ca = s.Matrix(q, q, lambda r, b:
                      s.binomial(b, r) * (1 + s.I) ** (b - r) if r <= b else 0)
        pi = s.Matrix([[1, 2, s.I], [0, 3, 1], [0, 0, 2]])
        gi, gj = s.diag(7, 5, 3), s.diag(4, 3, 2)
        scalar = 2 - s.I
        for gram in (gi, gj):
            old = gram.inv() * pi.H * pi
            new = (ca.H * gram * ca).inv() * (scalar * pi * ca).H * (scalar * pi * ca)
            self.assertTrue(equal(new, 5 * ca.inv() * old * ca))
            self.assertTrue(equal(new.det(), 5 ** q * old.det()))
        self.assertTrue(equal((gj.inv() * pi.H * pi).det() /
                              (gi.inv() * pi.H * pi).det(), gi.det() / gj.det()))

    def test_finite_field_translation_character_exponents(self):
        for p, q in ((7, 2), (11, 3)):
            chi = X ** q + 2 * X + 1
            phi = s.integrate(chi, X)
            def residue(value):
                value = s.Rational(value)
                return int(value.p * pow(int(value.q), -1, p) % p)
            for av in (1, 2, 4):
                for uv in (1, 2):
                    tv = 3
                    gamma = residue((-phi.subs(X, -av) - tv * av) / uv)
                    for xv in range(p):
                        original = residue((phi.subs(X, xv) - tv * xv) / uv)
                        translated = residue((phi.subs(X, xv) - phi.subs(X, -av)
                                              - tv * (xv + av)) / uv)
                        self.assertEqual(translated, (original + gamma) % p)


def main():
    global MUTATION
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=["flip-period-sign", "drop-potential-constant"])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    MUTATION = args.mutation
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(SharedMaps)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    owner = Path("workspace:/work")
    inputs = [owner / "deligne_exponential_determinant_extension_20260913.tex",
              owner / "deligne_translation_bridge_20260913.tex", Path(__file__)]
    receipt = {
        "scope": "independent exact finite regression, not general analytic certification or Lean",
        "tests_run": result.testsRun,
        "failures": len(result.failures), "errors": len(result.errors),
        "successful": result.wasSuccessful(), "mutation": MUTATION,
        "sympy": s.__version__,
        "inputs": [{"name": p.name, "bytes": p.stat().st_size,
                    "sha256": hashlib.sha256(p.read_bytes()).hexdigest()} for p in inputs],
    }
    if args.output:
        args.output.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt))
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
