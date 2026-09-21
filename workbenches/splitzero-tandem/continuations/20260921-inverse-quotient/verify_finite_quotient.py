"""Exact finite checks for supplied inverse-quotient equations (3)--(31).

The example is a finite algebra calculation, not an arithmetic test packet.
No spectral profile, asymptotic result, or RH endpoint is tested here.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent
checks = []


def require(condition, detail):
    if not condition:
        raise AssertionError(detail)


def reduce_matrix(a):
    return a.applyfunc(sp.cancel)


def equal(name, left, right):
    if isinstance(left, sp.MatrixBase) or isinstance(right, sp.MatrixBase):
        residual = reduce_matrix(left - right)
        require(residual == sp.zeros(*residual.shape), (name, residual))
    else:
        residual = sp.cancel(left - right)
        require(residual == 0, (name, residual))
    checks.append(name)


def positive(name, a):
    equal(name + ": Hermitian", a, a.H)
    for j in range(1, a.rows + 1):
        value = sp.cancel(a[:j, :j].det())
        require(value.is_positive is True, (name, j, value))
    checks.append(name)


def quotient(g, p):
    gram = reduce_matrix((p * g.inv() * p.H).inv())
    section = reduce_matrix(g.inv() * p.H * gram)
    return gram, section


y = sp.Symbol("y")
q = 6
N = 7
Q = y**6 + 2 * y**4 - y**3 + 3 * y + 2


def coefficient(p, size=q):
    poly = sp.Poly(p, y)
    return sp.Matrix([poly.nth(j) for j in range(size)])


def remainder(p):
    return sp.rem(p, Q, y)


J = sp.Matrix.hstack(*[coefficient(remainder(y**j)) for j in range(N + 1)])
M = sp.Matrix.hstack(*[coefficient(remainder(y**(j + 1))) for j in range(q)])
require(M.det() != 0, "Original multiplication must be invertible.")
base = sp.eye(N + 1)
for i in range(N):
    base[i, i + 1] = sp.Rational(i + 1, i + 2) + sp.I / (i + 3)
source_gram = reduce_matrix(base.H * sp.diag(*range(2, N + 3)) * base)
positive("Original rational complex source Gram", source_gram)
G, L = quotient(source_gram, J)
equal("Original quotient minimum J L = I", J * L, sp.eye(q))
equal("Original quotient section isometry", L.H * source_gram * L, G)
I_K = sp.eye(q)[:, 4:6]
Lambda = sp.eye(q)[:4, :]
H_K = reduce_matrix(I_K.H * G * I_K)
Q_B, L_B = quotient(G, Lambda)
P_B = reduce_matrix(L_B * Lambda)
P_K = reduce_matrix(I_K * H_K.inv() * I_K.H * G)
equal("Kernel and observed projections sum to I", P_K + P_B, sp.eye(q))


def make_level(r):
    U = sp.Matrix.hstack(*[(M ** (-j))[:, 0] for j in range(1, r + 1)])
    Phi = reduce_matrix(Lambda * U)
    require(Phi.rank() == r, "Original inverse-sector observation rank")
    P = reduce_matrix((M**r)[r:q, :])
    inclusion = sp.eye(q)[:, :q - r]
    equal(f"r={r}: quotient formula (10)", P * inclusion, sp.eye(q - r))
    equal(f"r={r}: quotient kills inverse powers", P * U, sp.zeros(q - r, r))
    require(P.rank() == q - r, "Explicit quotient rank")
    # The first independent rows provide a fixed algebraic quotient frame.
    pivots = list(Phi.T.rref()[1])
    other = [j for j in range(Lambda.rows) if j not in pivots]
    pivot_map = sp.eye(Lambda.rows)[pivots, :]
    other_map = sp.eye(Lambda.rows)[other, :]
    rho = reduce_matrix(other_map - Phi[other, :] * Phi[pivots, :].inv() * pivot_map)
    equal(f"r={r}: rho Phi = 0", rho * Phi, sp.zeros(len(other), r))
    Gbar, S = quotient(G, P)
    Qbar, Srho = quotient(Q_B, rho)
    Lambar = reduce_matrix(rho * Lambda * inclusion)
    Qbar_direct, Lbar = quotient(Gbar, Lambar)
    equal(f"r={r}: commuting observation (12)", Lambar * P, rho * Lambda)
    equal(f"r={r}: iterated quotient metric (14)", Qbar, Qbar_direct)
    HE = reduce_matrix(U.H * G * U)
    HB = reduce_matrix(Phi.H * Q_B * Phi)
    Gamma = reduce_matrix(I_K.H * G * U)
    Hhat = reduce_matrix(H_K - Gamma * HE.inv() * Gamma.H)
    equal(f"r={r}: observed Schur complement (3)", HB, HE - Gamma.H * H_K.inv() * Gamma)
    equal(f"r={r}: kernel quotient Schur complement (4)", (P * I_K).H * Gbar * (P * I_K), Hhat)
    positive(f"r={r}: inverse-sector observation positive", HB)
    positive(f"r={r}: kernel quotient positive", Hhat)
    equal(f"r={r}: determinant identity (6)", HE.det() * Hhat.det(), HB.det() * H_K.det())
    # a is an exact finite lower factor, not the programme asymptotic factor.
    a = sp.cancel(1 / sp.trace(HB.inv() * HE))
    require(a.is_positive is True, "Finite lower factor is positive")
    if r > 1:
        positive(f"r={r}: exact rational sandwich lower bound", reduce_matrix(HB - a * HE))
        positive(f"r={r}: propagated kernel lower bound (5)", reduce_matrix(Hhat - a * H_K))
    h = reduce_matrix(U * HB.inv() * Phi.H * Q_B)
    j0 = reduce_matrix((sp.eye(q) - h * Lambda) * S)
    j1 = Srho
    equal(f"r={r}: chain section degree zero", P * j0, sp.eye(q - r))
    equal(f"r={r}: chain section degree one", rho * j1, sp.eye(Lambda.rows - r))
    equal(f"r={r}: chain section commutes", Lambda * j0, j1 * Lambar)
    equal(f"r={r}: homotopy degree zero (17)", sp.eye(q) - j0 * P, h * Lambda)
    equal(f"r={r}: homotopy degree one (17)", sp.eye(Lambda.rows) - j1 * rho, Lambda * h)
    equal(f"r={r}: h inverse on V", h * Phi, U)
    equal(f"r={r}: degree-zero homotopy on original K", j0 * P * I_K, I_K)
    frame = I_K.row_join(U)
    equal(f"r={r}: augmented kernel determinant (19)", (frame.H * G * frame).det(), H_K.det() * HB.det())
    # A fixed complement selected algebraically, not by a moving metric.
    Z = sp.eye(Lambda.rows)[:, other]
    equal(f"r={r}: fixed complement section", rho * Z, sp.eye(len(other)))
    C = Phi.row_join(Z)
    equal(f"r={r}: exact target determinant frame factor (20)",
          sp.conjugate(C.det()) * C.det() * Q_B.det(), HB.det() * Qbar.det())
    PbarK = reduce_matrix(sp.eye(q - r) - Lbar * Lambar)
    return dict(r=r, U=U, Phi=Phi, P=P, inclusion=inclusion, rho=rho, G=Gbar,
                Q=Qbar, S=S, Lambar=Lambar, Lbar=Lbar, PbarK=PbarK,
                a=a, angle_rank=Gamma.rank())


levels = {r: make_level(r) for r in [1, 2, 3]}


def inverse_step(r, s):
    source, target = levels[r], levels[r + s]
    step = reduce_matrix(target["P"] * M**(-s) * source["inclusion"])
    drop = sp.eye(q - r)[s:q - r, :]
    equal(f"r={r},s={s}: exact Taylor division (24)", step, drop)
    equal(f"r={r},s={s}: kernel P_<s (25)", step[:, :s], sp.zeros(q - r - s, s))
    require(step.rank() == q - r - s, "Taylor division is onto")
    return step


I12 = inverse_step(1, 1)
I23 = inverse_step(2, 1)
I13 = inverse_step(1, 2)
equal("Taylor division composition (27)", I23 * I12, I13)
B12 = reduce_matrix(levels[2]["Lambar"] * I12 * levels[1]["Lbar"])
B23 = reduce_matrix(levels[3]["Lambar"] * I23 * levels[2]["Lbar"])
B13 = reduce_matrix(levels[3]["Lambar"] * I13 * levels[1]["Lbar"])
equal("Observed action with complete kernel leakage (29)",
      levels[2]["Lambar"] * I12,
      B12 * levels[1]["Lambar"] + levels[2]["Lambar"] * I12 * levels[1]["PbarK"])
defect = reduce_matrix(B13 - B23 * B12)
memory = reduce_matrix(levels[3]["Lambar"] * I23 * levels[2]["PbarK"] * I12 * levels[1]["Lbar"])
equal("Observed composition with full memory (30)", defect, memory)
require(defect != sp.zeros(*defect.shape), "This check must exercise nonzero memory.")
require(defect.rank() <= I_K.cols, "Memory has the original kernel rank bound")
checks.append("Observed composition defect is genuinely nonzero")

for s in [1, 2]:
    division = sp.zeros(N + 1)
    for j in range(s, N + 1):
        division[j - s, j] = 1
    U = sp.Matrix.hstack(*[(M ** (-j))[:, 0] for j in range(1, s + 1)])
    F = sp.Matrix.vstack(*[L[s - j, :] for j in range(1, s + 1)])
    A = reduce_matrix(J * division * L)
    equal(f"s={s}: exact full inverse decomposition (22)", M**(-s), A + U * F)
    target = levels[1 + s]
    equal(f"s={s}: original kernel-to-observation identity (31)",
          target["rho"] * Lambda * M**(-s) * I_K,
          target["rho"] * Lambda * A * I_K)
    # A positive source norm control is exact even though the imported Gamma
    # value itself is outside this finite example's scope.
    b_squared = sp.cancel(sp.trace(G.inv() * A.H * G * A))
    require(b_squared.is_positive is True, "Finite norm-control quantity is positive")
    checks.append(f"s={s}: finite exact source norm upper bound exists")

c = sp.Rational(3, 2)
T = sp.Matrix(q, q, lambda a, b: sp.binomial(b, a) * c**(b - a) * sp.I**a if a <= b else 0)
G_S = reduce_matrix(T.H * G * T)
I_K_S = reduce_matrix(T.inv() * I_K)
equal("Original S=k/2+iy phase and frame congruence", I_K_S.H * G_S * I_K_S, H_K)
equal("Substitution triangular phase", T.det(), sp.I ** (q * (q - 1) // 2))

result = {
    "scope": "Finite exact identities (3)--(31); no arithmetic profile or asymptotic replay",
    "number_of_checks": len(checks),
    "all_checks": checks,
    "example": {"polynomial_Q": str(Q), "dimension_q": q, "source_cutoff_N": N,
                "kernel_dimension": I_K.cols,
                "source_gram": str(source_gram),
                "fixed_Lambda": str(Lambda), "fixed_I_K": str(I_K)},
    "finite_lower_factors": {str(r): str(levels[r]["a"]) for r in levels},
    "angle_ranks": {str(r): levels[r]["angle_rank"] for r in levels},
    "nonzero_memory_shape": list(defect.shape),
    "nonzero_memory_rank": defect.rank(),
    "nonzero_memory_matrix": str(defect),
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
(ROOT / "EXACT_CHECKS.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"success": True, "checks": len(checks), "memory_rank": defect.rank()}, indent=2))
