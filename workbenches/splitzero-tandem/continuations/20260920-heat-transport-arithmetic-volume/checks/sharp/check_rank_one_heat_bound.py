"""Exact finite checks supporting, not replacing, RANK_ONE_HEAT_BOUND.tex.

No floating-point computation is used. The proof of the uniform inequality
is the interlacing/log-measure argument in the TeX file.
"""

from itertools import combinations
import json
import sys

import sympy as sp


CHECKS = []
CONTROLS = []


def exact(matrix):
    return matrix.applyfunc(sp.simplify)


def require(name, truth):
    if not bool(truth):
        raise RuntimeError(name)
    CHECKS.append(name)


def equal_matrix(name, actual, expected):
    require(name, (actual - expected).applyfunc(sp.simplify).is_zero_matrix)


def is_psd(matrix):
    matrix = exact(matrix)
    if matrix != matrix.H:
        return False
    for size in range(1, matrix.rows + 1):
        for indices in combinations(range(matrix.rows), size):
            determinant = sp.simplify(matrix.extract(indices, indices).det())
            if determinant.is_nonnegative is not True:
                return False
    return True


def valid_comparison(x, y, kappa):
    return (
        is_psd(x)
        and is_psd(y - x)
        and is_psd(kappa * x - y)
        and (y - x).rank() <= 1
    )


def reject(name, invalid_claim):
    if bool(invalid_claim):
        raise RuntimeError("failure control accepted: " + name)
    CONTROLS.append(name)


def pseudodeterminant(matrix):
    matrix = exact(matrix)
    rank = matrix.rank()
    if rank == 0:
        return sp.Integer(1)
    return sp.simplify(sum(
        matrix.extract(indices, indices).det()
        for indices in combinations(range(matrix.rows), rank)
    ))


def run():
    imaginary = sp.I
    identity = sp.eye(3)
    # Positive Hermitian S, with its complex off-diagonal entries retained.
    s0 = sp.Matrix([[2, imaginary, 0], [-imaginary, 3, 1], [0, 1, 2]])
    require("S positive leading minor 1", s0[:1, :1].det() > 0)
    require("S positive leading minor 2", s0[:2, :2].det() > 0)
    require("S positive leading minor 3", s0.det() > 0)
    equal_matrix("S Hermitian", s0, s0.H)
    sinv = exact(s0.inv())
    g0 = exact(s0 * s0)
    u = sp.Matrix([1, 2 * imaginary, 2]) / 3
    v = sp.Matrix([2, imaginary, -2]) / 3
    require("u unit", (u.H * u)[0] == 1)
    require("v unit", (v.H * v)[0] == 1)
    require("u orthogonal v with conjugate transpose", (u.H * v)[0] == 0)
    omega = sp.Integer(3)
    b = exact(3 * sinv * u)
    g = exact(exact(g0.inv() + b * b.H / omega).inv())
    kappa = sp.simplify(g0.det() / g.det())
    require("prescribed determinant ratio", kappa == 4)
    require("original update ratio formula", sp.simplify(kappa - 1 - (b.H * g0 * b)[0] / omega) == 0)
    equal_matrix("original inverse metric update", g.inv(), g0.inv() + b * b.H / omega)
    p = exact(u * u.H)
    d = exact(identity - p / 2)
    hmetric = exact(identity - 3 * p / 4)
    equal_matrix("P Hermitian", p, p.H)
    equal_matrix("P idempotent", p * p, p)
    require("P rank one", p.rank() == 1)
    equal_matrix("transported update retains complex b", s0 * b * b.H * s0 / omega, 3 * p)
    equal_matrix("D square", d * d, hmetric)
    equal_matrix("D inverse square", d.inv() * d.inv(), identity + 3 * p)
    equal_matrix("exact original G", g, s0 * hmetric * s0)
    equal_matrix("T0 isometry", s0.H * s0, g0)
    t1 = exact(d * s0)
    equal_matrix("T1 isometry", t1.H * t1, g)
    equal_matrix("T1 inverse", t1.inv(), s0.inv() * d.inv())
    original_unit = sp.Matrix([1, imaginary, 2 - imaginary])
    equal_matrix("original vector return via T0", s0.inv() * (s0 * original_unit), original_unit)
    equal_matrix("original vector return via T1", s0.inv() * d.inv() * (t1 * original_unit), original_unit)

    matrices = {
        "full rank complex": sp.Matrix([[1, imaginary, 2], [3 - imaginary, 2, 0], [0, 1, 4 + imaginary]]),
        "rank two complex": sp.Matrix([[1, imaginary, 2], [0, 2, imaginary], [0, 0, 0]]),
        "positive equality direction": s0.inv() * (u * v.H) * s0,
        "negative equality direction": s0.inv() * (v * u.H) * s0,
        "zero": sp.zeros(3),
    }
    for name, matrix in matrices.items():
        matrix = exact(matrix)
        a = exact(s0 * matrix * sinv)
        c = exact(d * a)
        bb = exact(d * a * d.inv())
        original0 = exact(g0.inv() * matrix.H * g0 * matrix)
        original1 = exact(g.inv() * matrix.H * g * matrix)
        equal_matrix(name + ": exact G0 adjoint transport", s0 * original0 * s0.inv(), a.H * a)
        equal_matrix(name + ": exact G adjoint transport", t1 * original1 * t1.inv(), bb.H * bb)
        require(name + ": G0 characteristic polynomial", original0.charpoly().all_coeffs() == (a.H * a).charpoly().all_coeffs())
        require(name + ": G characteristic polynomial", original1.charpoly().all_coeffs() == (bb.H * bb).charpoly().all_coeffs())
        equal_matrix(name + ": left difference", a.H * a - c.H * c, sp.Rational(3, 4) * a.H * p * a)
        equal_matrix(name + ": right difference", bb * bb.H - c * c.H, 3 * c * p * c.H)
        require(name + ": left PSD rank-one comparison", valid_comparison(c.H * c, a.H * a, kappa))
        require(name + ": right PSD rank-one comparison", valid_comparison(c * c.H, bb * bb.H, kappa))
        require(name + ": original and comparison ranks", a.rank() == c.rank() == bb.rank() == matrix.rank())
        ratio_left = sp.simplify(pseudodeterminant(a.H * a) / pseudodeterminant(c.H * c))
        ratio_right = sp.simplify(pseudodeterminant(bb * bb.H) / pseudodeterminant(c * c.H))
        require(name + ": left determinant budget", 1 <= ratio_left <= kappa)
        require(name + ": right determinant budget", 1 <= ratio_right <= kappa)
        require(name + ": left-right singular spectra", (bb.H * bb).charpoly().all_coeffs() == (bb * bb.H).charpoly().all_coeffs())

    equal_matrix("positive equality exact B", d * (u * v.H) * d.inv(), u * v.H / 2)
    equal_matrix("negative equality exact B", d * (v * u.H) * d.inv(), 2 * v * u.H)
    equal_matrix("positive squared spectrum projector", (u * v.H).H * (u * v.H), v * v.H)
    equal_matrix("negative squared spectrum projector", (v * u.H).H * (v * u.H), u * u.H)
    k = sp.Symbol("k", positive=True)
    x = sp.Symbol("x", positive=True)
    lower = sp.log(k) / (k - 1)
    upper = k * lower
    require("optimizer endpoint ratio", sp.simplify(upper / lower - k) == 0)
    require("optimizer endpoint distance", sp.simplify(upper - lower - sp.log(k)) == 0)
    require("density derivative", sp.simplify(sp.diff(x * sp.exp(-x), x) - (1 - x) * sp.exp(-x)) == 0)
    require("heat primitive", sp.diff(-sp.exp(-x), x) == sp.exp(-x))
    require("log-measure primitive", sp.diff(sp.log(x), x) == 1 / x)
    exact_lower = sp.log(4) / 3
    exact_upper = 4 * exact_lower
    exact_d = sp.Rational(3, 4) * 4 ** (-sp.Rational(1, 3))
    require("exact positive heat equality", sp.simplify(sp.exp(-exact_lower) - sp.exp(-exact_upper) - exact_d) == 0)
    require("exact negative heat equality", sp.simplify(sp.exp(-exact_upper) - sp.exp(-exact_lower) + exact_d) == 0)
    require("exact threshold equality", sp.simplify(exact_lower * sp.exp(-exact_lower) - exact_upper * sp.exp(-exact_upper)) == 0)
    require("rank-zero comparison accepted", valid_comparison(sp.zeros(2), sp.zeros(2), 4))
    require("kappa-one equality accepted", valid_comparison(sp.eye(2), sp.eye(2), 1))
    require("zero-update comparison accepted", valid_comparison(sp.eye(2), sp.eye(2), 4))

    reject("rank-two update is outside lemma", valid_comparison(sp.eye(2), 2 * sp.eye(2), 2))
    reject("rank-changing update is outside lemma", valid_comparison(sp.diag(1, 0), sp.eye(2), 4))
    reject("wrong order is outside lemma", valid_comparison(2 * sp.eye(2), sp.eye(2), 4))
    reject("insufficient relative bound", valid_comparison(sp.eye(2), sp.diag(4, 1), 3))
    reject("transpose loses complex phase", (u.T * v)[0] == 0)
    reject("transpose gives original metric update", g.inv() == g0.inv() + b * b.T / omega)
    reject("wrong determinant ratio", kappa == 1 + (b.H * b)[0] / omega)
    reject("reversed metric square root", d.inv() * d.inv() == hmetric)
    reject("false double constant sharpness", sp.simplify(exact_d - 2 * exact_d) == 0)

    print(json.dumps({
        "status": "passed",
        "arithmetic": "exact SymPy; no floating point",
        "checks": len(CHECKS),
        "failure_controls": len(CONTROLS),
        "python_optimized": not __debug__,
        "python_version": sys.version.split()[0],
        "sympy_version": sp.__version__,
        "claim": "Finite identity checks only; uniform inequality proved in RANK_ONE_HEAT_BOUND.tex",
        "check_names": CHECKS,
        "failure_control_names": CONTROLS,
    }, indent=2))


if __name__ == "__main__":
    run()
