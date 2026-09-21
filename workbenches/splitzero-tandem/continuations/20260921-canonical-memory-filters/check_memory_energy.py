"""Exact finite algebra and separately labelled floating point fixtures for ME1–34."""
from pathlib import Path
import json
import math
import numpy as np
import sympy as sp
from scipy.integrate import quad

HERE = Path(__file__).resolve().parent
exact = []
numeric = []

def eq(name, left, right):
    diff = left - right
    ok = all(sp.simplify(x) == 0 for x in diff) if isinstance(diff, sp.MatrixBase) else sp.simplify(diff) == 0
    if not ok:
        raise AssertionError((name, diff))
    exact.append(name)

def chk(name, condition, value=None):
    if not bool(condition):
        raise AssertionError((name, value))
    numeric.append({"name": name, "value": value})

def blocks(H, m):
    return H[:m, :m], H[:m, m:], H[m:, m:]

# Rational congruences provide nonidentity physical metrics and nontrivial observations.
for q in range(2, 7):
    for m in range(1, q):
        n = q - m
        W = sp.eye(q)
        for i in range(q - 1):
            W[i, i + 1] = sp.Rational(i + 1, q + 2)
        G = W.T * W
        Mi = sp.diag(*range(2, q + 2))
        for i in range(q):
            for j in range(i + 1, q):
                Mi[i, j] = sp.Rational((i + 2) * (j + 1), q + 3)
        M = W.inv() * Mi * W
        Lambda = W[m:, :]
        Q = (Lambda * G.inv() * Lambda.T).inv()
        L = G.inv() * Lambda.T * Q
        J = W.inv()[:, :m]
        H = Mi.T * Mi
        A, B, DH = blocks(H, m)
        S = DH - B.T * A.inv() * B
        Z = sp.eye(n) + B.T * A.inv() ** 2 * B
        En = (Lambda * (M.T * G * M).inv() * Lambda.T).inv()
        tag = f"q{q}_m{m}"
        eq(tag + "_quotient_metric", Q, sp.eye(n))
        eq(tag + "_section_projection", Lambda * L, sp.eye(n))
        eq(tag + "_section_isometry", L.T * G * L, Q)
        eq(tag + "_kernel_isometry", J.T * G * J, sp.eye(m))
        eq(tag + "_cross_orthogonality", J.T * G * L, sp.zeros(m, n))
        eq(tag + "_energy_quotient", En, S)
        eq(tag + "_Schur_determinant", S.det() * A.det(), M.det() ** 2)
        eq(tag + "_graph_determinant", Z.det() * A.det() ** 2, (A ** 2 + B * B.T).det())
        Len = L - J * A.inv() * B
        eq(tag + "_energy_lift_projection", Lambda * Len, sp.eye(n))
        eq(tag + "_energy_lift_norm", Len.T * G * Len, Z)
        eq(tag + "_energy_lift_energy", Len.T * M.T * G * M * Len, S)
        eq(tag + "_memory_inverse_identity", A.det() * H.inv()[:m, :m].det(), A.det() * DH.det() / H.det())
        z = sp.Rational(3, 7)
        F = z * sp.eye(n) + DH - B.T * (z * sp.eye(m) + A).inv() * B
        eq(tag + "_regularized_Schur", F.det() * (z * sp.eye(m) + A).det(), (z * sp.eye(q) + H).det())

# A nonunit observed coordinate and a nonidentity coefficient metric check every Q factor.
W = sp.Matrix([[1, sp.Rational(2, 3), 0], [0, 1, sp.Rational(1, 5)], [0, 0, 1]])
G = W.T * W
T = sp.Matrix([[2, 1], [0, 3]])
Lam = T * W[1:, :]
Q = (Lam * G.inv() * Lam.T).inv()
L = G.inv() * Lam.T * Q
Mi = sp.Matrix([[2, 3, 1], [0, 3, 2], [0, 0, 4]])
M = W.inv() * Mi * W
A, B, DH = blocks(Mi.T * Mi, 1)
S = DH - B.T * A.inv() * B
Z = sp.eye(2) + B.T * A.inv() ** 2 * B
En = (Lam * (M.T * G * M).inv() * Lam.T).inv()
eq("nonunit_observed_energy_congruence", En, T.inv().T * S * T.inv())
eq("nonunit_observed_energy_determinant", En.det() / Q.det(), M.det() ** 2 / A.det())
Len = L - W.inv()[:, :1] * A.inv() * B * T.inv()
eq("nonunit_observed_lift_norm", Len.T * G * Len, T.inv().T * Z * T.inv())
eq("nonunit_observed_lift_energy", Len.T * M.T * G * M * Len, En)

# Equality case in the sharp shared-top-direction bound, plus a nonzero energy graph.
M = sp.Matrix([[2, 1], [1, 2]])
H = M.T * M
A, B, DH = blocks(H, 1)
Z = sp.eye(1) + B.T * A.inv() ** 2 * B
S = DH - B.T * A.inv() * B
eq("sharp_complement_product", A.det() * DH.det(), sp.Rational((3 ** 2 + 1) ** 2, 4))
eq("sharp_memory_exponential", A.det() * DH.det() / H.det(), sp.Rational(25, 9))
eq("nonzero_graph_metric", Z[0], sp.Rational(41, 25))
eq("nonzero_graph_energy", S[0], sp.Rational(9, 5))
eq("energy_weighted_kernel_det", A.det() * Z.det(), sp.Rational(41, 5))
eq("isometric_graph_energy", S.det() / Z.det(), sp.Rational(45, 41))
z = sp.symbols('z', positive=True)
swap = sp.Matrix([[0, 1], [1, 0]])
eq("singular_observed_full_H", swap.T * swap, sp.eye(2))
eq("singular_observed_memory_ratio", (z + 1) ** 2 / (z * sp.eye(2) + swap.T * swap).det(), 1)
eq("singular_observed_leakage_ratio", (z + 1) / z, 1 + 1 / z)

# All numerical checks are synthetic; none is a native moment or period evaluation.
rng = np.random.default_rng(20260921)
max_identity_error = 0.0
for q in range(2, 10):
    for m in range(1, q):
        X = rng.normal(size=(q, q)) + 1j * rng.normal(size=(q, q))
        U, _ = np.linalg.qr(X)
        X = rng.normal(size=(q, q)) + 1j * rng.normal(size=(q, q))
        V, _ = np.linalg.qr(X)
        sv = np.r_[4.0, np.linspace(1.3, 0.4, q - 1)]
        M = U @ np.diag(sv) @ V.conj().T
        H = M.conj().T @ M
        A, B, DH = blocks(H, m)
        D = M[:m, m:]
        MB = M[m:, m:]
        E = MB.conj().T @ MB
        eigH, eigA, eigD = [np.linalg.eigvalsh(T) for T in (H, A, DH)]
        logdet = lambda T: float(np.linalg.slogdet(T)[1])
        g0 = logdet(A) + logdet(DH) - logdet(H)
        sharp = (q - 2) * math.log(1.3 ** 2) + 2 * math.log((4 ** 2 + 1.3 ** 2) / 2) - logdet(H)
        tag = f"q{q}_m{m}"
        chk(tag + "_sharp_memory_bound", -1e-10 <= g0 <= sharp + 1e-9, g0)
        Z = np.eye(q - m) + B.conj().T @ np.linalg.solve(A, np.linalg.solve(A, B))
        S = DH - B.conj().T @ np.linalg.solve(A, B)
        Dstar = 2 * math.log(4) + 2 * (m - 1) * math.log(1.3)
        chk(tag + "_improved_graph_bound", logdet(A) + logdet(Z) <= Dstar + 1e-9, logdet(A) + logdet(Z))
        old = 2 * logdet(A) + logdet(Z)
        new = logdet(A @ A + B @ B.conj().T)
        max_identity_error = max(max_identity_error, abs(old - new))
        chk(tag + "_graph_identity", abs(old - new) < 1e-9, abs(old - new))
        previous = g0
        for zz in (1e-6, 0.01, 0.4, 3.0, 100.0):
            g = sum(np.log(zz + eigA)) + sum(np.log(zz + eigD)) - sum(np.log(zz + eigH))
            ell = logdet(zz * np.eye(q - m) + DH) - logdet(zz * np.eye(q - m) + E)
            rankH = np.linalg.matrix_rank(B)
            rankD = np.linalg.matrix_rank(D)
            bd = lambda rank: 0 if rank == 0 else math.log1p(16 / zz) + (rank - 1) * math.log1p(1.3 ** 2 / zz)
            chk(tag + f"_z{zz}_memory", -1e-9 <= g <= min(previous, bd(rankH)) + 1e-8, float(g))
            chk(tag + f"_z{zz}_leakage", -1e-9 <= ell <= bd(rankD) + 1e-8, ell)
            previous = g
        # The heat integral is integrated on log time; cancellation below exp(-12) is negligible here.
        def integrand(u):
            t = math.exp(u)
            return float(np.exp(-t * eigH).sum() - np.exp(-t * eigA).sum() - np.exp(-t * eigD).sum())
        value, error = quad(integrand, -12, 8, epsabs=2e-10, epsrel=2e-10)
        chk(tag + "_zero_heat_integral", abs(value - g0) < 2e-8, abs(value - g0))
        for t in (0.003, 0.02, 0.5, 2.0, 20.0):
            Qmix = float(np.exp(-t * eigH).sum() - np.exp(-t * eigA).sum() - np.exp(-t * eigD).sum())
            chk(tag + f"_heat_positive_t{t}", Qmix >= -1e-11, Qmix)

result = {
    "status": "PASS", "exact_check_count": len(exact), "numerical_check_count": len(numeric),
    "scope": "Exact rational algebra and separately labelled synthetic floating point fixtures; no native moments or period data evaluated.",
    "max_numerical_graph_identity_error": max_identity_error,
    "exact_checks": exact, "numerical_checks": numeric,
}
(HERE / 'MEMORY_ENERGY_CHECK_RESULTS.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
print(json.dumps({k: v for k, v in result.items() if k not in ('exact_checks', 'numerical_checks')}, indent=2))
