"""Finite fixtures for heat_memory_proofs.md.

Exact checks use SymPy rational arithmetic. Random checks use a recorded seed
and double precision; their output is evidence of these finite cases only.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import expm, expm_frechet
import sympy as sp

ROOT = Path(__file__).resolve().parent
SEED = 20260921
rng = np.random.default_rng(SEED)
record = {
    "seed": SEED,
    "numpy_version": np.__version__,
    "scipy_version": scipy.__version__,
    "sympy_version": sp.__version__,
    "exact": {},
    "numerical": {},
}


def herm(a):
    return (a + a.conj().T) / 2


def psd_min(a):
    return float(np.linalg.eigvalsh(herm(a)).min(initial=0))


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def random_complex(shape):
    return rng.normal(size=shape) + 1j * rng.normal(size=shape)


def heat(a, t):
    vals, vecs = np.linalg.eigh(herm(a))
    return (vecs * np.exp(-t * np.maximum(vals, 0))) @ vecs.conj().T


def trace_real(a):
    return float(np.trace(a).real)


def logdet(a):
    sign, result = np.linalg.slogdet(a)
    check(abs(sign - 1) < 1e-7, "positive determinant sign")
    return float(result)


def inverse_sqrt(a):
    w, v = np.linalg.eigh(herm(a))
    return (v / np.sqrt(w)) @ v.conj().T


def exact_counterexample():
    M = sp.Matrix([[0, 0, 0], [1, 0, -2], [-2, -1, 0]])
    H = M.T * M
    eigs = [0, 3, 7]
    check(set(H.eigenvals()) == set(eigs), "exact H spectrum")
    eye = sp.eye(3)
    result = sp.zeros(3)
    for lam in eigs:
        projector = eye
        for mu in eigs:
            if mu != lam:
                projector = projector * (H - mu * eye) / (lam - mu)
        result += sp.Rational(1, 2) ** lam * projector
    difference = result[1:, 1:] - sp.diag(sp.Rational(1, 2), sp.Rational(1, 16))
    expected = sp.Matrix([
        [sp.Rational(1523, 5376), -sp.Rational(403, 2688)],
        [-sp.Rational(403, 2688), sp.Rational(95, 1344)],
    ])
    check(difference == expected, "exact compressed heat matrix")
    check(difference.det() == -sp.Rational(211, 86016), "exact negative determinant")
    check(sp.trace(difference) == sp.Rational(1903, 5376), "exact positive trace")
    check(H == sp.Matrix([[5, 2, -2], [2, 1, 0], [-2, 0, 4]]), "exact Gram")
    record["exact"]["operator_order_counterexample"] = {
        "time": "log(2)",
        "H_eigenvalues": eigs,
        "difference": [[str(x) for x in difference.row(i)] for i in range(2)],
        "determinant": str(difference.det()),
        "trace": str(sp.trace(difference)),
    }


def exact_schur_realization():
    # A has a zero eigenspace and repeated positive eigenvalue.
    # Noncommuting residues are retained.
    A = sp.diag(0, 2, 2, 5)
    B = sp.Matrix([[0, 0], [1, 2], [2, 0], [1, -1]])
    Ap = sp.diag(0, sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(1, 5))
    C2 = B[1:3, :].T * B[1:3, :] / 2
    C5 = B[3:4, :].T * B[3:4, :] / 5
    T = B.T * Ap * B
    S = sp.Matrix([[3, 1], [1, 2]])
    D = S + T
    H = A.row_join(B).col_join(B.T.row_join(D))
    z = sp.Rational(7, 3)
    F = z * sp.eye(2) + S + z / (z + 2) * C2 + z / (z + 5) * C5
    check(T == C2 + C5, "exact residue sum")
    check(C2 * C5 != C5 * C2, "fixture residues genuinely fail to commute")
    check((z * sp.eye(6) + H).inv()[4:, 4:] == F.inv(), "exact compressed resolvent")
    check(F == z * sp.eye(2) + D - B.T * (z * sp.eye(4) + A).inv() * B,
          "exact memory pencil")
    record["exact"]["singular_A_noncommuting_memory"] = {
        "A_eigenvalues": [0, 2, 2, 5],
        "C2": [[str(x) for x in C2.row(i)] for i in range(2)],
        "C5": [[str(x) for x in C5.row(i)] for i in range(2)],
        "memory_state_dimension": int(C2.rank() + C5.rank()),
        "original_kernel_dimension": 4,
        "compressed_resolvent_identity": True,
        "residue_commutator_nonzero": True,
    }


def numerical_blocks():
    cases = 0
    worst_violation = 0.0
    largest_observed_error = 0.0
    noncommuting_cases = 0
    time_grid = [0.0, 1e-7, 0.002, 0.1, 1.0, 40.0]
    for q, m in [(3, 1), (5, 2), (7, 3), (6, 4)]:
        n = q - m
        for sample in range(12):
            M = random_complex((q, q))
            if sample % 3 == 0:
                M[-1, :] = 0
            H = M.conj().T @ M
            A, B, D = H[:m, :m], H[:m, m:], H[m:, m:]
            leakage = M[:m, m:]
            MB = M[m:, m:]
            J = MB.conj().T @ MB
            rc = np.linalg.matrix_rank(B)
            rd = np.linalg.matrix_rank(leakage)
            bnorm2 = float(np.linalg.norm(B, "fro") ** 2)
            dnorm2 = float(np.linalg.norm(leakage, "fro") ** 2)
            check(np.linalg.norm(D - J - leakage.conj().T @ leakage) < 1e-9,
                  "full leakage block")
            vals, vecs = np.linalg.eigh(herm(A))
            Ap = (vecs * np.where(vals > 1e-10, 1 / np.maximum(vals, 1e-100), 0)) @ vecs.conj().T
            T = B.conj().T @ Ap @ B
            S = herm(D - T)
            check(psd_min(S) >= -1e-7, "positive Schur remainder")
            residues = []
            for j, lam in enumerate(vals):
                if lam > 1e-10:
                    w = B.conj().T @ vecs[:, j:j+1]
                    residues.append((lam, w @ w.conj().T / lam))
            if len(residues) > 1:
                comm = residues[0][1] @ residues[1][1] - residues[1][1] @ residues[0][1]
                if np.linalg.norm(comm) > 1e-8:
                    noncommuting_cases += 1

            for t in time_grid:
                EH, EA, ED, EJ = heat(H, t), heat(A, t), heat(D, t), heat(J, t)
                mix = trace_real(EH) - trace_real(EA) - trace_real(ED)
                gap = trace_real(EH[m:, m:]) - trace_real(ED)
                leak_gap = trace_real(EJ) - trace_real(ED)
                err = trace_real(EH[m:, m:]) - trace_real(EJ)
                bupper = min(rc, t*t*bnorm2)
                dupper = min(rd, t*dnorm2)
                violations = [-mix, mix - bupper, -gap, gap - mix,
                              -leak_gap, leak_gap - dupper, -err - dupper, err - bupper]
                worst_violation = max(worst_violation, max(violations))
                check(max(violations) <= 3e-8, "heat bounds")
                largest_observed_error = max(largest_observed_error, abs(err))
                cases += 1

            for z in [0.01, 0.5, 3.0]:
                F = z*np.eye(n) + D - B.conj().T @ np.linalg.solve(z*np.eye(m)+A, B)
                compressed = np.linalg.inv(z*np.eye(q)+H)[m:, m:]
                check(np.linalg.norm(compressed - np.linalg.inv(F)) < 3e-7,
                      "memory resolvent")
                g = logdet(z*np.eye(m)+A) + logdet(z*np.eye(n)+D) - logdet(z*np.eye(q)+H)
                g2 = logdet(z*np.eye(n)+D) - logdet(F)
                ell = logdet(z*np.eye(n)+D) - logdet(z*np.eye(n)+J)
                gbound = rc*math.log1p(min(np.linalg.norm(A,2),np.linalg.norm(D,2))/z)
                ellbound = rd*math.log1p(np.linalg.norm(leakage,2)**2/z)
                check(abs(g-g2)<1e-7, "determinant Schur identity")
                check(-1e-8 <= g <= min(gbound, bnorm2/z**2)+1e-7, "g bounds")
                check(-1e-8 <= ell <= ellbound+1e-7, "leakage determinant bound")
                check(abs((logdet(F)-logdet(z*np.eye(n)+J))-(ell-g)) < 1e-7,
                      "retained leakage minus memory")
                zz = z + 0.8j
                Fz = zz*np.eye(n) + D - B.conj().T @ np.linalg.solve(zz*np.eye(m)+A, B)
                check(np.linalg.eigvalsh((Fz-Fz.conj().T)/(2j)).min() > 0,
                      "upper half-plane positivity")
    record["numerical"]["random_full_blocks"] = {
        "matrix_samples": 48,
        "heat_time_cases": cases,
        "time_grid": time_grid,
        "max_roundoff_bound_violation": worst_violation,
        "largest_absolute_observed_error": largest_observed_error,
        "noncommuting_residue_cases": noncommuting_cases,
    }


def numerical_metric_derivatives():
    cases = 0
    max_heat_ratio = 0.0
    max_rank_heat_ratio = 0.0
    max_projection_difference = 0.0
    max_observed_ratio = 0.0
    max_fd_error = 0.0
    for q, m in [(3,1), (5,2), (7,4)]:
        for sample in range(8):
            p = 3
            xs = rng.normal(size=p)
            velocity = rng.normal(size=p)
            omegas = []
            for i in range(p):
                Z = random_complex((q, q))
                omegas.append(Z @ Z.conj().T / q)
            baseline = np.diag(np.linspace(0.5, 1.5, q))
            C = baseline + sum(math.exp(xs[i])*omegas[i] for i in range(p))
            Cp = sum(velocity[i]*math.exp(xs[i])*omegas[i] for i in range(p))
            G = np.linalg.inv(C)
            Gp = -G @ Cp @ G
            F = inverse_sqrt(G)
            B = herm(F.conj().T @ Gp @ F)
            M0 = random_complex((q, q))
            if sample % 2 == 0:
                M0[-2:, :] = 0
            MM = np.linalg.solve(F, M0 @ F)
            H = MM.conj().T @ MM
            Hp = MM.conj().T @ B @ MM - (B @ H + H @ B)/2
            Pphysical = np.eye(q)[:, :m]
            Kframe = np.linalg.solve(F, Pphysical)
            gram = Kframe.conj().T @ Kframe
            P = Kframe @ np.linalg.solve(gram, Kframe.conj().T)
            Pp = ((np.eye(q)-P) @ B @ P + P @ B @ (np.eye(q)-P))/2
            delta = max(0.0, *velocity) - min(0.0, *velocity)
            check(np.ptp(np.linalg.eigvalsh(B)) <= delta + 1e-9,
                  "connection spectral width")
            rank = np.linalg.matrix_rank(M0)
            basic = (1/math.e + 0.5)*math.sqrt(q)*delta/2
            refined = delta/2*(math.sqrt(rank)/math.e+math.sqrt(min(q,2*rank))/2)
            ell = q-m
            observed_bound = delta*(min(ell,q-ell)/4+(1/math.e+0.5)*math.sqrt(ell*q)/2)
            for t in [0.0, 0.001, 0.03, 0.4, 10.0]:
                Z, Zp = expm_frechet(-t*H, -t*Hp)
                hs = np.linalg.norm(Zp, "fro")
                max_heat_ratio = max(max_heat_ratio, hs/basic)
                max_rank_heat_ratio = max(max_rank_heat_ratio, hs/refined)
                check(hs <= basic+2e-8 and hs <= refined+2e-8, "uniform derivative bounds")
                obsderiv = trace_real(-Pp @ Z + (np.eye(q)-P) @ Zp)
                max_observed_ratio = max(max_observed_ratio, abs(obsderiv)/observed_bound)
                check(abs(obsderiv) <= observed_bound+2e-8, "observed derivative bound")
                # Compare against the fixed original coordinates, including
                # the actual changing metric projection and metric adjoint.
                eps = 2e-6
                obs = []
                for s in [-eps, eps]:
                    Cs = baseline + sum(math.exp(xs[i]+s*velocity[i])*omegas[i] for i in range(p))
                    Gs = np.linalg.inv(Cs)
                    Hs = np.linalg.solve(Gs, M0.conj().T @ Gs @ M0)
                    Ks = Pphysical @ np.linalg.solve(Pphysical.conj().T @ Gs @ Pphysical,
                                                     Pphysical.conj().T @ Gs)
                    obs.append(trace_real((np.eye(q)-Ks) @ expm(-t*Hs)))
                fd = (obs[1]-obs[0])/(2*eps)
                max_fd_error = max(max_fd_error, abs(fd-obsderiv))
                check(abs(fd-obsderiv) <= 2e-5, "frame derivative versus original coordinates")
                cases += 1
            # A moving basis u'=B u/2 directly checks the projection sign.
            eps = 1e-6
            projections = []
            for s in [-eps, eps]:
                frameK = expm(s*B/2) @ Kframe
                projections.append(frameK @ np.linalg.solve(frameK.conj().T@frameK,frameK.conj().T))
            pdiff = np.linalg.norm((projections[1]-projections[0])/(2*eps)-Pp)
            max_projection_difference = max(max_projection_difference, pdiff)
            check(pdiff <= 2e-8, "moving fixed-kernel projection sign")
    record["numerical"]["metric_paths"] = {
        "path_samples": 24,
        "heat_time_cases": cases,
        "largest_HS_derivative_over_intake_bound": max_heat_ratio,
        "largest_HS_derivative_over_rank_bound": max_rank_heat_ratio,
        "largest_observed_derivative_over_bound": max_observed_ratio,
        "largest_original_coordinate_derivative_difference": max_fd_error,
        "largest_projection_derivative_difference": max_projection_difference,
    }


def scalar_fixtures():
    largest_first = 0.0
    largest_second = 0.0
    for x in [0.0, *np.logspace(-6, 4, 100), 1.0]:
        for y in [0.0, *np.logspace(-6, 4, 100), 1.0]:
            dd = math.exp(-x) if x == y else abs((math.exp(-x)-math.exp(-y))/(x-y))
            a = math.sqrt(x*y)*dd
            b = (x+y)*dd/2
            check(a <= 1/math.e+1e-10 and b <= 0.5+1e-10, "scalar divided differences")
            largest_first = max(largest_first, a)
            largest_second = max(largest_second, b)
    psi_checks = []
    for delta in [0.001,0.2,1.0,4.0,20.0]:
        u = delta/math.expm1(delta)
        psi = (1-math.exp(-delta))*math.exp(-u)
        attained = math.exp(-u)-math.exp(-math.exp(delta)*u)
        check(abs(psi-attained)<1e-12, "sharper endpoint scalar maximum")
        check(psi <= min(delta/math.e,1)+1e-12, "endpoint linear bound")
        psi_checks.append({"delta":delta,"max_scalar_difference":psi})
    record["numerical"]["scalar_divided_differences"] = {
        "largest_sqrt_xy_factor": largest_first,
        "bound_sqrt_xy_factor": 1/math.e,
        "largest_arithmetic_factor": largest_second,
        "bound_arithmetic_factor": 0.5,
        "finite_change_maxima": psi_checks,
    }


if __name__ == "__main__":
    exact_counterexample()
    exact_schur_realization()
    numerical_blocks()
    numerical_metric_derivatives()
    scalar_fixtures()
    record["status"] = "PASS"
    target = ROOT / "heat_memory_fixture_results.json"
    target.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(record, indent=2))
