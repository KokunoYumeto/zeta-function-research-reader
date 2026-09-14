"""Exact finite algebra checks for the full-packet formal phase comparison.

The polynomials below are test inputs for the algebraic identities only.
Their roots are NOT asserted to be zeros of xi or to furnish RH evidence.
All arithmetic is rational. No numerical tolerance is used.
"""

from __future__ import annotations

from fractions import Fraction as F
from functools import lru_cache
import hashlib
import json
from math import comb, factorial
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parent
s, y = sp.symbols("s y")


def rational(value):
    value = sp.Rational(value)
    return F(int(value.p), int(value.q))


def mul(a, b, order):
    result = [F(0)] * (order + 1)
    for i, ai in enumerate(a[: order + 1]):
        if ai:
            for j, bj in enumerate(b[: order + 1 - i]):
                if bj:
                    result[i + j] += ai * bj
    return result


def power(a, exponent, order):
    assert exponent >= 0
    result = [F(1)] + [F(0)] * order
    for _ in range(exponent):
        result = mul(result, a, order)
    return result


def compose(a, b, order):
    result = [F(0)] * (order + 1)
    bp = [F(1)] + [F(0)] * order
    for ai in a[: order + 1]:
        if ai:
            result = [x + ai * z for x, z in zip(result, bp)]
        bp = mul(bp, b, order)
    return result


@lru_cache(maxsize=None)
def fractional_power(a_tuple, exponent, order):
    """Coefficients of A^exponent, A(0)=1, by finite binomial convolution."""
    a = list(a_tuple)
    assert a[0] == 1
    z = a[:]
    z[0] = F(0)
    zp = [F(1)] + [F(0)] * order
    result = [F(0)] * (order + 1)
    coefficient = F(1)
    for k in range(order + 1):
        for j, val in enumerate(zp):
            result[j] += coefficient * val
        zp = mul(zp, z, order)
        coefficient *= (exponent - k) / (k + 1)
    return tuple(result)


def polys_coeffs(poly, variable, order):
    poly = sp.Poly(sp.expand(poly), variable)
    return [rational(poly.nth(i)) for i in range(order + 1)]


def matrix_strings(matrix):
    return [[str(value) for value in row] for row in matrix.tolist()]


def local_remainder_monomial(n, m):
    """Return (a,q,coefficient) for coefficient * u^q * w^a, or None."""
    N = m + 1
    q, a = divmod(n, N)
    if a == m:
        return None
    coefficient = (-1) ** q
    for ell in range(q):
        coefficient *= a + 1 + ell * N
    return a, q, coefficient


def test_case(name, roots, branches, qmax):
    h = sp.prod((s - rho) ** m for rho, m in roots).expand()
    d = sum(m for _, m in roots)
    primitive_indef = sp.integrate(h, s)
    phi = sp.expand(primitive_indef - primitive_indef.subs(s, 0))
    assert sp.diff(phi, s) == h and phi.subs(s, 0) == 0

    C = sp.zeros(d)
    B = sp.zeros(d)
    for bglobal in range(d):
        quotient, remainder = sp.div(phi * s**bglobal, h, domain=sp.QQ)
        assert sp.expand(phi * s**bglobal - h * quotient - remainder) == 0
        derivative = sp.diff(quotient, s)
        assert sp.degree(derivative, s) < d
        for j in range(d):
            C[j, bglobal] = sp.expand(remainder).coeff(s, j)
            B[j, bglobal] = sp.expand(derivative).coeff(s, j)

    T = [sp.zeros(d) for _ in range(qmax + 1)]
    critical = []
    beta = []
    local_records = []
    offset = 0
    direct_checks = inverse_checks = relation_checks = 0
    for (rho, m), branch in zip(roots, branches):
        N = m + 1
        c = sp.expand(phi.subs(s, rho))
        ay = sp.cancel(N * (phi.subs(s, rho + y) - c) / y**N).expand()
        assert sp.denom(ay) == 1
        a0 = rational(ay.subs(y, 0))
        branch = F(branch)
        assert branch**N == a0 and branch != 0
        A = polys_coeffs(ay / sp.Rational(a0.numerator, a0.denominator), y, sp.degree(ay, y))

        def lagrange_coefficient(bglobal, n):
            ap = fractional_power(tuple(A), -F(n + 1, N), n)
            f = [F(comb(bglobal, j)) * F(rho) ** (bglobal - j)
                 for j in range(bglobal + 1)]
            return branch ** (-(n + 1)) * sum(
                f[j] * ap[n - j] for j in range(min(bglobal, n) + 1)
            )

        for a in range(m):
            critical.append(c)
            beta.append(sp.Rational(a + 1, N))
            for q in range(qmax + 1):
                n = a + q * N
                remainder = local_remainder_monomial(n, m)
                assert remainder is not None
                aa, qq, multiplier = remainder
                assert (aa, qq) == (a, q)
                for bglobal in range(d):
                    value = multiplier * lagrange_coefficient(bglobal, n)
                    T[q][offset + a, bglobal] = sp.Rational(value.numerator, value.denominator)

        # A second route explicitly constructs psi and composes power series.
        # Verify the inverse coordinate through w^12 and pullbacks through w^11.
        direct_order = 12
        psi = [F(0)]
        for j in range(1, direct_order + 1):
            ap = fractional_power(tuple(A), -F(j, N), j - 1)
            psi.append(branch ** (-j) * ap[j - 1] / j)
        wofy = [F(0)] + [branch * x for x in fractional_power(tuple(A), F(1, N), direct_order - 1)]
        identity = [F(0), F(1)] + [F(0)] * (direct_order - 1)
        for composed in [compose(wofy, psi, direct_order), compose(psi, wofy, direct_order)]:
            assert composed == identity
            inverse_checks += direct_order + 1
        psiprime = [F(j + 1) * psi[j + 1] for j in range(direct_order)]
        original_coord = psi[:]
        original_coord[0] = F(rho)
        for bglobal in range(d):
            pullback = mul(power(original_coord, bglobal, direct_order - 1), psiprime, direct_order - 1)
            for n in range(direct_order):
                assert pullback[n] == lagrange_coefficient(bglobal, n)
                direct_checks += 1

        # The monomial remainder must annihilate every exact local image
        # (u*d/dw+w^m)w^r, through all orders needed by T and beyond.
        max_r = (qmax + 2) * N
        for r in range(max_r + 1):
            image = {}
            for n, u_shift, scalar in [(r + m, 0, 1), (r - 1, 1, r)]:
                if scalar == 0:
                    continue
                remainder = local_remainder_monomial(n, m)
                if remainder is not None:
                    a, q, coeff = remainder
                    key = (a, q + u_shift)
                    image[key] = image.get(key, 0) + scalar * coeff
            assert all(v == 0 for v in image.values())
            relation_checks += 1

        local_records.append({
            "rho": str(rho), "multiplicity": m, "N": N,
            "critical_value": str(c), "a_y": str(ay), "branch_b": str(branch),
            "largest_pullback_exponent_used": m - 1 + qmax * N,
            "psi_through_degree_6": [str(x) for x in psi[:7]],
        })
        offset += m

    C0 = sp.diag(*critical)
    B0 = sp.diag(*beta)
    verified_orders = list(range(-2, qmax - 1))
    scalar_connection_checks = 0
    for r in verified_orders:
        # Coefficient of u^r in T'+(-C0/u^2+B0/u)T-T(-C/u^2+B/u).
        residue = -C0 * T[r + 2] + T[r + 2] * C
        if r + 1 >= 0:
            residue += (r + 1) * T[r + 1] + B0 * T[r + 1] - T[r + 1] * B
        assert residue == sp.zeros(d), (name, r, residue)
        scalar_connection_checks += d * d

    # Independent weighted CRT: J lists original Taylor coefficients,
    # and W is computed by actual truncated pullback on y^j dy.
    J = sp.zeros(d)
    W = sp.zeros(d)
    offset = 0
    for (rho, m), branch in zip(roots, branches):
        N = m + 1
        c = phi.subs(s, rho)
        ay = sp.cancel(N * (phi.subs(s, rho + y) - c) / y**N).expand()
        a0 = ay.subs(y, 0)
        A = polys_coeffs(ay / a0, y, sp.degree(ay, y))
        branch = F(branch)
        for a in range(m):
            ap = fractional_power(tuple(A), -F(a + 1, N), a)
            for j in range(a + 1):
                value = branch ** (-(a + 1)) * ap[a - j]
                W[offset + a, offset + j] = sp.Rational(value.numerator, value.denominator)
            for bglobal in range(a, d):
                J[offset + a, bglobal] = comb(bglobal, a) * rho ** (bglobal - a)
        offset += m
    assert T[0] == W * J
    expected_jdet = sp.prod((rj - ri) ** (mi * mj)
                           for i, (ri, mi) in enumerate(roots)
                           for rj, mj in roots[i + 1 :])
    expected_wdet = sp.prod(sp.Rational(branch) ** (-(m * (m + 1) // 2))
                           for (_, m), branch in zip(roots, branches))
    assert J.det() == expected_jdet
    assert W.det() == expected_wdet
    assert T[0].det() == expected_jdet * expected_wdet != 0
    T0inv = T[0].inv()
    assert T[0] * T0inv == sp.eye(d) and T0inv * T[0] == sp.eye(d)
    # Inverse constructed by the same displayed weighted CRT factorization.
    assert T0inv == J.inv() * W.inv()

    # Formal inverse through every stored order: useful check that no T jet
    # or u-dependent off-primary coefficient has been discarded.
    Sinv = [T0inv]
    for n in range(1, qmax + 1):
        coefficient = sp.zeros(d)
        for j in range(1, n + 1):
            coefficient += T[j] * Sinv[n - j]
        Sinv.append(-T0inv * coefficient)
    inverse_matrix_checks = 0
    for n in range(qmax + 1):
        target = sp.eye(d) if n == 0 else sp.zeros(d)
        for left, right in [(T, Sinv), (Sinv, T)]:
            product = sp.zeros(d)
            for j in range(n + 1):
                product += left[j] * right[n - j]
            assert product == target
            inverse_matrix_checks += d * d

    # The trace identity forces the scalar determinant series to be
    # constant. Verify the nontrivial positive u coefficients directly.
    u = sp.Symbol("u")
    trunc = sum((T[q] * u**q for q in range(qmax + 1)), sp.zeros(d))
    determinant = sp.Poly(trunc.det(), u)
    assert determinant.nth(0) == T[0].det()
    for q in range(1, qmax + 1):
        assert determinant.nth(q) == 0

    return {
        "name": name, "status": "PASS", "interpretation": "Algebraic test input only; roots are not xi-zero data.",
        "h": str(h), "Phi_with_Phi_0_equal_0": str(phi), "dimension": d,
        "local_branches": local_records,
        "T_stored_through_u_power": qmax,
        "connection_identity_verified_u_powers": verified_orders,
        "connection_scalar_equalities": scalar_connection_checks,
        "coordinate_inverse_scalar_equalities": inverse_checks,
        "independent_pullback_scalar_equalities": direct_checks,
        "local_exact_image_remainder_checks": relation_checks,
        "formal_matrix_inverse_scalar_equalities": inverse_matrix_checks,
        "C": matrix_strings(C), "B": matrix_strings(B),
        "C0": matrix_strings(C0), "B0": matrix_strings(B0),
        "J_original_Taylor_CRT": matrix_strings(J), "W_density_coordinate_map": matrix_strings(W),
        "T0": matrix_strings(T[0]), "T0_inverse": matrix_strings(T0inv),
        "det_J": str(J.det()), "det_W": str(W.det()), "det_T0": str(T[0].det()),
        "det_T_positive_coefficients_verified_zero_through": qmax,
        "T_coefficient_matrices": [matrix_strings(tq) for tq in T],
        "source_truncation_justification": "For u^r, r=-2,...,qmax-2, the connection identity uses only T_(r+2) and T_(r+1); all these coefficients are retained. Each T_q row is computed from the exact pullback coefficient at w^(a+qN), so higher w coefficients cannot contribute to u^q.",
    }


def main():
    cases = [
        test_case("two_unequal_primaries_unit_branches", [(2, 1), (3, 2)], [1, 1], 8),
        test_case("two_unequal_primaries_nonunit_branches", [(2, 1), (10, 2)], [8, 2], 8),
        test_case("two_unequal_primaries_negative_square_branch", [(2, 1), (10, 2)], [-8, 2], 8),
    ]
    receipt = {
        "status": "PASS", "arithmetic": "Exact rational arithmetic; no floating point or tolerance.",
        "scope": "Finite checks of the formal coordinate/remainder/connection formulas, not a proof of their all-order generalization or of RH.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python": sys.version.split()[0], "sympy": sp.__version__,
        "case_count": len(cases), "cases": cases,
    }
    target = ROOT / "formal_phase_comparison_exact_checks.json"
    target.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    summary = {"status": receipt["status"], "case_count": len(cases), "receipt": str(target),
               "connection_scalar_equalities": sum(c["connection_scalar_equalities"] for c in cases),
               "det_T0_by_case": [c["det_T0"] for c in cases]}
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
