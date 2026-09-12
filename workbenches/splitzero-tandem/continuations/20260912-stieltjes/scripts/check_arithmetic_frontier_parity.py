"""Exact finite Gaussian calibrations of AP.1--AP.22.

The chosen measure is dnu=sqrt(8/pi)*exp(-8*t**2)dt on the original
s=1/2+i*t line, with mass 1 and variance 1/16. These are comparison
packets, not zeros of zeta; no actual-zeta moment or RH estimate is
certified. All quotient and tensor matrices use original monomials.
"""
from __future__ import annotations

import argparse
from functools import lru_cache
import hashlib
from itertools import combinations, product
import json
from pathlib import Path
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "tex" / "arithmetic_frontier_parity.tex"
s = sp.Symbol("s")
t = sp.Symbol("t", real=True)
lam = sp.Symbol("lambda")
half = sp.Rational(1, 2)
variance = sp.Rational(1, 16)
unit_polynomial = 1 + (s-half)**2
records = []


def check(name, condition):
    records.append({"name": name, "passed": bool(condition)})


def scalar_zero(value):
    return sp.cancel(sp.expand(value)) == 0


def equal(name, left, right):
    difference = sp.Matrix(left)-sp.Matrix(right)
    check(name, all(scalar_zero(value) for value in difference))


def matrix_data(matrix):
    return [[str(value) for value in matrix.row(i)] for i in range(matrix.rows)]


def compositions(total, count):
    if count == 1:
        return [(total,)]
    return [(first,)+tail for first in range(total+1)
            for tail in compositions(total-first, count-1)]


def tensor(matrices):
    result = matrices[0]
    for matrix in matrices[1:]:
        result = sp.kronecker_product(result, matrix)
    return result


@lru_cache(None)
def q(n):
    if n == 0:
        return sp.Integer(1)
    if n == 1:
        return s-half
    return sp.expand((s-half)*q(n-1)+(n-1)*variance*q(n-2))


def kappa(n):
    return sp.factorial(n)*variance**n


def expectation(poly):
    answer = sp.Integer(0)
    for (power,), coefficient in sp.Poly(sp.expand(poly), t).terms():
        if power % 2 == 0:
            answer += coefficient*sp.factorial2(power-1)*variance**(power//2)
    return sp.cancel(answer)


def gram_gaussian(left, right):
    return expectation(sp.conjugate(left.subs(s, half+sp.I*t))
                       *right.subs(s, half+sp.I*t))


def strict_positive(name, matrix):
    equal(name+":Hermitian", matrix.H, matrix)
    for order in range(1, matrix.rows+1):
        check(name+f":leading_minor_{order}", matrix[:order, :order].det() > 0)


def positive_semidefinite(name, matrix):
    """All principal minors: exact PSD criterion, never numerical eigenvalues."""
    equal(name+":Hermitian", matrix.H, matrix)
    for order in range(1, matrix.rows+1):
        for selected in combinations(range(matrix.rows), order):
            check(name+":"+",".join(map(str, selected)),
                  matrix.extract(selected, selected).det() >= 0)


def polynomial_matrix(poly, matrix):
    answer = sp.zeros(matrix.rows)
    for (power,), coefficient in sp.Poly(poly, s).terms():
        answer += coefficient*matrix**power
    return answer


class Packet:
    def __init__(self, polynomial, count):
        self.h = sp.Poly(sp.expand(polynomial), s)
        self.d = self.h.degree()
        self.k = count
        self.dimension = self.d**count
        self.A = sp.Matrix.hstack(*(self.remainder(s**(j+1)) for j in range(self.d)))
        self.C = sp.Matrix.hstack(*(self.remainder((1-s)**j) for j in range(self.d)))
        self.U = polynomial_matrix(unit_polynomial, self.A)
        self.Ak = sp.zeros(self.dimension)
        for j in range(count):
            self.Ak += tensor([self.A if i == j else sp.eye(self.d) for i in range(count)])
        self.Ck = tensor([self.C]*count)

    def remainder(self, polynomial):
        remainder = sp.rem(sp.Poly(polynomial, s), self.h)
        return sp.Matrix([remainder.nth(j) for j in range(self.d)])

    @lru_cache(None)
    def z(self, alpha):
        return tensor([self.U*self.remainder(q(n)) for n in alpha])

    def weight(self, alpha):
        return sp.prod(kappa(n) for n in alpha)

    def kernel(self, degree):
        result = sp.zeros(self.dimension)
        for level in range(degree+1):
            for alpha in compositions(level, self.k):
                column = self.z(alpha)
                result += column*column.H/self.weight(alpha)
        return result

    def frontier(self, degree):
        high = compositions(degree+1, self.k)
        low = compositions(degree, self.k)
        F = sp.Matrix.hstack(*(self.z(beta) for beta in high))
        Omega = sp.diag(*(self.weight(beta) for beta in high))
        Omega_low = sp.diag(*(self.weight(alpha) for alpha in low))
        L = sp.zeros(len(low), len(high))
        for col, beta in enumerate(high):
            for j in range(self.k):
                if beta[j]:
                    alpha = tuple(beta[i]-(i == j) for i in range(self.k))
                    L[low.index(alpha), col] += beta[j]*variance
        Z = sp.Matrix.hstack(*(self.z(alpha) for alpha in low))
        return low, high, F, Z*L, Omega, Omega_low, Z, L


def run_case(name, model, degree, negative_control):
    k, d, D = model.k, model.d, model.dimension
    Cinv = model.kernel(degree)
    G = Cinv.inv()
    Cnext = model.kernel(degree+1)
    Gnext = Cnext.inv()
    low, high, F, E, Omega, Omega_low, Z, incidence = model.frontier(degree)
    original_E = E.copy()
    if negative_control:
        # Corrupt the actual predecessor sign while preserving the metric,
        # unit, reflection and all degree data. The displacement must fail.
        E[:, 0] = -E[:, 0]
    Oi = Omega.inv()
    eta = (-1)**(k*d+degree+1)
    Ak, reflection = model.Ak, model.Ck
    W = Ak.H*G+G*Ak-k*G
    relative = Cinv*W
    source_A = Oi*F.H*G*F
    source_B = Oi*E.H*G*E
    positive_product = source_A*source_B
    T_original = F*Oi*E.H
    p = T_original.rank()
    gamma = max(sum((alpha[j]+1)*variance+(k-1)*alpha[j]*variance
                    for j in range(k)) for alpha in low)
    pi = sp.cancel(Gnext.det()/G.det())
    chi_relative = relative.charpoly(lam).as_expr()
    chi_positive = positive_product.charpoly(lam).as_expr()

    check(name+":degree_interpolates", degree >= k*(d-1))
    check(name+":packet_reflection", scalar_zero(model.h.as_expr().subs(s, 1-s)-(-1)**d*model.h.as_expr()))
    equal(name+":original_unit_parity", model.C*model.U, (-1)**d*model.U*model.C)
    strict_positive(name+":inverse_interpolation", Cinv)
    strict_positive(name+":metric", G)
    equal(name+":inverse_metric", Cinv*G, sp.eye(D))
    equal(name+":reflection_involution", reflection**2, sp.eye(D))
    equal(name+":reflection_generator", reflection*Ak, (k*sp.eye(D)-Ak)*reflection)
    equal(name+":reflection_isometry", reflection.H*G*reflection, G)
    equal(name+":reflection_weight", reflection.H*W*reflection, -W)
    equal(name+":frontier_parity", reflection*F, eta*F)
    equal(name+":predecessor_parity", reflection*E, -eta*E)
    equal(name+":frontier_orthogonality", F.H*G*E, sp.zeros(len(high)))
    equal(name+":incidence_predecessors", E, Z*incidence)
    equal(name+":exact_displacement", Ak*Cinv+Cinv*Ak.H-k*Cinv,
          F*Oi*E.H+E*Oi*F.H)
    equal(name+":exact_weight", W, G*(F*Oi*E.H+E*Oi*F.H)*G)
    equal(name+":inverse_metric_update", Cnext, Cinv+F*Oi*F.H)
    check(name+":trace_square", scalar_zero(sp.trace(relative**2)-2*sp.trace(positive_product)))
    check(name+":full_characteristic_identity", scalar_zero(
        lam**(2*len(high))*chi_relative-lam**D*chi_positive.subs(lam, lam**2)))
    check(name+":full_zero_multiplicity", sp.Poly(chi_relative, lam).terms()[-1][0][0] == D-2*p)
    check(name+":paired_inertia_from_rank", W.rank() == 2*p)
    check(name+":positive_product_rank", positive_product.rank() == p)
    check(name+":determinant_ratio", scalar_zero(pi*(sp.eye(len(high))+source_A).det()-1))
    check(name+":volume_ratio_positive", 0 < pi <= 1)
    incidence_N = Omega_low*incidence*Oi*incidence.H
    for row, alpha in enumerate(low):
        expected = sum((alpha[j]+1)*variance+(k-1)*alpha[j]*variance for j in range(k))
        check(name+":incidence_row_"+str(alpha), scalar_zero(sum(incidence_N.row(row))-expected))
    # Both matrices have order D=4; all 15 nonempty principal minors
    # are evaluated exactly, proving the two congruence bounds.
    positive_semidefinite(name+":incidence_domination",
                          gamma*Z*Omega_low.inv()*Z.H-E*Oi*E.H)
    positive_semidefinite(name+":full_metric_domination", gamma*Cinv-E*Oi*E.H)
    positive_semidefinite(name+":lower_degree_remainder", Cinv-Z*Omega_low.inv()*Z.H)
    positive_semidefinite(name+":frontier_source_gram", F.H*G*F) if len(high) <= 4 else None
    if k == 1:
        epsilon_squared = sp.cancel(positive_product[0, 0])
        check(name+":scalar_epsilon_squared_rank", epsilon_squared > 0 if p else epsilon_squared == 0)
        check(name+":scalar_exact_spectrum", scalar_zero(
            chi_relative-lam**(D-2*p)*(lam**2-epsilon_squared)**p))
        check(name+":scalar_exact_product", scalar_zero(
            epsilon_squared-(F.H*G*F)[0, 0]*(E.H*G*E)[0, 0]/Omega[0, 0]**2))
        check(name+":scalar_incidence_bound", epsilon_squared <= gamma*source_A[0, 0])
        check(name+":scalar_volume_bound", epsilon_squared <= gamma*(1/pi-1))
    else:
        epsilon_squared = None
    eigenvalues = [value for value, multiplicity in model.A.eigenvals().items()
                   for _ in range(multiplicity)]
    eigenvalue_tuples = [sum(values) for values in product(eigenvalues, repeat=k)]
    departure = sp.cancel(sp.trace(Cinv*Ak.H*G*Ak)-sum(sp.conjugate(value)*value for value in eigenvalue_tuples))
    delta_square_sum = sum((sp.re(value)-k*half)**2 for value in eigenvalue_tuples)
    check(name+":departure_nonnegative", departure >= 0)
    check(name+":departure_identity", scalar_zero(
        departure-sp.trace(positive_product)+2*delta_square_sum))

    return {
        "case": name, "k": k, "d": d, "D": D, "M": degree,
        "h": str(model.h.as_expr()), "original_unit": str(unit_polynomial),
        "unit_remainder": str(sp.rem(sp.Poly(unit_polynomial, s), model.h).as_expr()),
        "frontier_indices": high, "predecessor_indices": low,
        "source_dimension_r": len(high), "eta": eta, "p": p,
        "gamma": str(gamma), "pi": str(pi),
        "epsilon_squared_k1": str(epsilon_squared) if epsilon_squared is not None else None,
        "relative_characteristic_polynomial": str(sp.factor(chi_relative)),
        "source_product_characteristic_polynomial": str(sp.factor(chi_positive)),
        "trace_relative_square": str(sp.trace(relative**2)),
        "departure": str(departure), "delta_square_sum": str(delta_square_sum),
        "matrices": {"A_k": matrix_data(Ak), "reflection": matrix_data(reflection),
                     "inverse_interpolation": matrix_data(Cinv), "G": matrix_data(G),
                     "F": matrix_data(F), "E_plus": matrix_data(E),
                     "uncorrupted_E_plus": matrix_data(original_E), "Omega": matrix_data(Omega),
                     "W": matrix_data(W), "incidence": matrix_data(incidence)},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT/"checks"/"arithmetic_frontier_parity.json")
    parser.add_argument("--negative-control", action="store_true")
    args = parser.parse_args()
    for n in range(8):
        check(f"q_{n}:original_monic", sp.Poly(q(n), s).LC() == 1)
        check(f"q_{n}:reflection", scalar_zero(q(n).subs(s, 1-s)-(-1)**n*q(n)))
        if n < 7:
            check(f"q_{n}:original_recurrence", scalar_zero(
                s*q(n)-q(n+1)-half*q(n)+(n*variance*q(n-1) if n else 0)))
        for m in range(8):
            check(f"gaussian_gram_{n}_{m}", scalar_zero(
                gram_gaussian(q(n), q(m))-(kappa(n) if n == m else 0)))
    repeated = Packet((s-sp.Rational(1, 4))**2*(s-sp.Rational(3, 4))**2, 1)
    pair = Packet((s-sp.Rational(1, 4))*(s-sp.Rational(3, 4)), 2)
    check("repeated:full_characteristic", scalar_zero(repeated.A.charpoly(s).as_expr()-repeated.h.as_expr()))
    equal("repeated:full_annihilator", polynomial_matrix(repeated.h.as_expr(), repeated.A), sp.zeros(4))
    check("repeated:semisimple_annihilator_fails", polynomial_matrix(pair.h.as_expr(), repeated.A) != sp.zeros(4))
    jet = sp.Matrix([[root**j if order == 0 else (j*root**(j-1) if j else 0)
                      for j in range(4)] for root in (sp.Rational(1, 4), sp.Rational(3, 4))
                     for order in (0, 1)])
    local_generator = sp.diag(sp.Matrix([[sp.Rational(1, 4), 0], [1, sp.Rational(1, 4)]]),
                             sp.Matrix([[sp.Rational(3, 4), 0], [1, sp.Rational(3, 4)]]))
    check("repeated:jet_isomorphism", jet.det() != 0)
    equal("repeated:full_jet_generator", jet*repeated.A, local_generator*jet)
    equal("repeated:full_jet_unit", jet*repeated.U,
          polynomial_matrix(unit_polynomial, local_generator)*jet)
    check("repeated:unit_derivative_retained", (jet*repeated.U*jet.inv())[1, 0] == -half
          and (jet*repeated.U*jet.inv())[3, 2] == half)
    equal("pair:retained_unit_exact_quotient", pair.U, sp.Rational(17, 16)*sp.eye(2))
    results = []
    for M in (4, 5, 6):
        results.append(run_case(f"repeated_k1_M{M}", repeated, M,
                                args.negative_control and M == 4))
    for M in (2, 3, 4):
        results.append(run_case(f"pair_k2_M{M}", pair, M, False))
    # Two supplementary zero-rank cases isolate F=0 and E_+=0 respectively.
    # h=q_2 retains both Gaussian nodes 1/2 +/- i/4, with even degree
    # and the required unit reflection parity. The unit class is 15/16.
    critical = Packet(q(2), 1)
    for M in (1, 2):
        results.append(run_case(f"critical_zero_k1_M{M}", critical, M, False))
    failed = [record["name"] for record in records if not record["passed"]]
    receipt = {"all_passed": not failed, "passed": len(records)-len(failed),
               "total": len(records), "failed": failed, "negative_control": args.negative_control,
               "python_optimization": sys.flags.optimize, "sympy_version": sp.__version__,
               "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               "proof_sha256": hashlib.sha256(PROOF.read_bytes()).hexdigest(),
               "scope": __doc__.strip(), "mass": "1", "variance": "1/16",
               "gaussian_density": "sqrt(8/pi)*exp(-8*t**2)",
               "status": "Exact finite rational calibration; written AP proof, not Lean formalization",
               "checks": records, "cases": results}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({key: receipt[key] for key in ("all_passed", "passed", "total", "failed",
                                                  "negative_control", "python_optimization")}))
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
