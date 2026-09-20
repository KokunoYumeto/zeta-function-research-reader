"""Exact finite tests for ENDPOINT_METRIC_HEAT.tex, without assertion shortcuts."""
from pathlib import Path
import hashlib
import json
import sympy as sp

HERE = Path(__file__).resolve().parent
checks = 0
controls = 0


def equal(label, left, right):
    global checks
    difference = left - right
    values = list(difference) if isinstance(difference, sp.MatrixBase) else [difference]
    if any(sp.simplify(sp.cancel(sp.expand(sp.expand_log(value, force=True)))) != 0 for value in values):
        raise RuntimeError(f"Equality failed: {label}: {difference}")
    checks += 1


def positive_or_zero(label, value):
    global checks
    value = sp.simplify(value)
    if value.is_nonnegative is not True:
        raise RuntimeError(f"Inequality failed or undecided: {label}: {value}")
    checks += 1


def differs(label, left, right):
    global controls
    difference = sp.simplify(left - right)
    if difference == 0:
        raise RuntimeError(f"Failure control was not detected: {label}")
    controls += 1


def adj(X, G):
    return G.inv() * X.conjugate().T * G


def trace(X):
    # The logarithmic-path coefficients are finite linear combinations of
    # logarithms of positive rationals. Keep those exact linear forms instead
    # of asking simplify() to combine them into enormous integer logarithms.
    return sp.cancel(sp.expand(sp.expand_log(sp.trace(X), force=True)))


I = sp.I
cases = [
    ("nilpotent-sharp", sp.eye(2), [1, 2],
     sp.Matrix([1, 0]), sp.Matrix([[0, 1]])),
    ("full-rank-complex", sp.Matrix([[1, 1], [0, 1]]), [1, 2],
     sp.eye(2), sp.Matrix([[1, I], [2, 3]])),
    ("rank-one-complex-three", sp.Matrix([[1, 1, 0], [0, 1, 1], [0, 0, 1]]), [1, 2, 3],
     sp.Matrix([1, I, 2]), sp.Matrix([[1, -I, 1]])),
    ("rank-two-three", sp.Matrix([[1, 0, I], [0, 1, 0], [0, 0, 1]]), [sp.Rational(1, 2), 1, sp.Rational(3, 2)],
     sp.Matrix([[1, 0], [I, 1], [0, 1]]), sp.Matrix([[1, 2 * I, 0], [0, 1, 2]])),
    ("scalar-metric", sp.Matrix([[1, I], [0, 1]]), [2, 2],
     sp.eye(2), sp.Matrix([[2, 1 + I], [3 * I, -1]])),
    ("zero-map", sp.eye(2), [1, 3], sp.zeros(2, 0), sp.zeros(0, 2)),
]
z = sp.symbols("z")
reports = []
for name, R, diagonal, U, V in cases:
    diagonal = [sp.sympify(x) for x in diagonal]
    G0 = R.conjugate().T * R
    S = R.inv() * sp.diag(*diagonal) * R
    G = S.conjugate().T * G0 * S
    C = G0.inv() * G
    M = U * V
    d, r = M.rows, U.cols
    alpha, beta = min(diagonal) ** 2, max(diagonal) ** 2
    chi = beta / alpha
    Mt = S * M * S.inv()
    M0d, Mtd = adj(M, G0), adj(Mt, G0)
    H0, Ht = M0d * M, Mtd * Mt
    D = Mt - M
    EH = Ht - H0
    equal(f"{name}: square root", S * S, C)
    equal(f"{name}: positive-root adjoint", adj(S, G0), S)
    equal(f"{name}: isometry", S.conjugate().T * G0 * S, G)
    equal(f"{name}: adjoint conjugacy", Mtd, S * adj(M, G) * S.inv())
    equal(f"{name}: metric heat conjugacy", Ht, S * adj(M, G) * M * S.inv())
    equal(f"{name}: commutator", D, (S * M - M * S) * S.inv())
    equal(f"{name}: full complex cross terms", EH, M0d * D + adj(D, G0) * M + adj(D, G0) * D)
    equal(f"{name}: traced cross terms", trace(EH),
          2 * sp.re(trace(M0d * D)) + trace(adj(D, G0) * D))
    equal(f"{name}: full determinant", (adj(M, G) * M).det(),
          M.det() * sp.conjugate(M.det()))
    equal(f"{name}: metric volume", G.det() / G0.det(), S.det() ** 2)
    equal(f"{name}: characteristic determinant", (z * sp.eye(d) - adj(M, G) * M).det(),
          z ** (d - r) * (z * sp.eye(r) - (U.conjugate().T * G * U) *
                            (V * G.inv() * V.conjugate().T)).det())
    equal(f"{name}: multiplication determinant", Mt.det(), M.det())
    J = sp.Matrix(2, d, lambda i, j: sp.Integer((i + 1) * (j + 2)) + (I if i == j else 0))
    unit = sp.Matrix([1] + [0] * (d - 1))
    Jt, unitt = J * S.inv(), S * unit
    equal(f"{name}: unit transport", Jt * unitt, J * unit)
    equal(f"{name}: arithmetic square", Jt * Mt * S, J * M)
    equal(f"{name}: multiplication of unit", Mt * unitt, S * M * unit)
    hsM2 = trace(H0)
    hsD2 = trace(adj(D, G0) * D)
    positive_or_zero(f"{name}: condition-ratio HS estimate",
                     (sp.sqrt(chi) - 1) ** 2 * hsM2 - hsD2)
    vectors = [sp.eye(d)[:, j] for j in range(d)]
    vectors += [sp.Matrix([1 + j * I for j in range(d)]),
                sp.Matrix([sp.Integer(j + 1) for j in range(d)])]
    for j, x in enumerate(vectors):
        quotient0 = (x.conjugate().T * M.conjugate().T * G0 * M * x)[0] / (x.conjugate().T * G0 * x)[0]
        quotientG = (x.conjugate().T * M.conjugate().T * G * M * x)[0] / (x.conjugate().T * G * x)[0]
        positive_or_zero(f"{name}: Rayleigh lower {j}", quotientG - quotient0 / chi)
        positive_or_zero(f"{name}: Rayleigh upper {j}", chi * quotient0 - quotientG)
    for n in range(1, 7):
        equal(f"{name}: holomorphic heat coefficient {n}", trace(Mt ** (2 * n)), trace(M ** (2 * n)))
        telescoping = sp.zeros(d)
        for j in range(n):
            telescoping += Ht ** (n - 1 - j) * EH * H0 ** j
        equal(f"{name}: finite Duhamel coefficient {n}", Ht ** n - H0 ** n, telescoping)
    # The logarithmic path has a fixed selfadjoint generator with the exact
    # original root eigenvalues. These coefficient identities prove that
    # the differentiated heat series has the stated trace-zero receiver.
    L = R.inv() * sp.diag(*[2 * sp.log(value) for value in diagonal]) * R
    equal(f"{name}: logarithm adjoint", adj(L, G0), L)
    equal(f"{name}: log-volume", trace(L), sp.log(G.det() / G0.det()))
    Mp = (L * Mt - Mt * L) / 2
    Hp = adj(Mp, G0) * Mt + Mtd * Mp
    equal(f"{name}: exact metric derivative", Hp, Mtd * L * Mt - (L * Ht + Ht * L) / 2)
    for n in range(1, 6):
        Bn = Mt * Ht ** (n - 1) * Mtd - Ht ** n
        equal(f"{name}: derivative trace-zero coefficient {n}", trace(Bn), 0)
        equal(f"{name}: full logarithmic derivative coefficient {n}",
              trace(Ht ** (n - 1) * Hp), trace(L * Bn))
    if chi == 1:
        equal(f"{name}: scalar metric leaves adjoint", adj(M, G), adj(M, G0))
        equal(f"{name}: scalar metric commutator zero", D, sp.zeros(d))
    reports.append({"name": name, "dimension": d, "rank": r,
                    "alpha": str(alpha), "beta": str(beta), "chi": str(chi),
                    "metric_determinant_ratio": str(sp.simplify(G.det() / G0.det())),
                    "M_HS_squared": str(hsM2), "commutator_HS_squared": str(hsD2)})

# Exact attainment of the universal constant for a rational metric ratio.
kappa = sp.Integer(4)
heat_time = sp.log(kappa) / (kappa - 1)
attained = sp.exp(-heat_time) - sp.exp(-kappa * heat_time)
sharp = (1 - 1 / kappa) * kappa ** (-1 / (kappa - 1))
equal("sharp scalar constant", attained, sharp)
equal("small log-metric cost for rank-one metric change",
      sp.log(sp.diag(4, 1).det()), sp.log(4))

# Controls cover unjustified metric independence, missing complex cross
# terms, missing metric inverses, and a lost unit-coordinate map.
M = sp.Matrix([[0, 1], [0, 0]])
G0, G = sp.eye(2), sp.diag(4, 1)
differs("metric heat is not algebraic heat", trace(adj(M, G) * M), trace(M ** 2))
differs("metric heat is not metric independent", trace(adj(M, G) * M), trace(adj(M, G0) * M))
R = sp.Matrix([[1, 1], [0, 1]])
S = R.inv() * sp.diag(1, 2) * R
G0 = R.conjugate().T * R
M = sp.Matrix([[1, I], [2, 3]])
D = S * M * S.inv() - M
E = adj(S * M * S.inv(), G0) * S * M * S.inv() - adj(M, G0) * M
differs("cross terms omitted", trace(E), trace(adj(D, G0) * D))
differs("metric inverse omitted in adjoint", trace(G0.inv() * M.conjugate().T * G0 * M),
        trace(M.conjugate().T * G0 * M))
unit = sp.Matrix([1, 1])
J = sp.Matrix([[1, 2]])
differs("unit transform omitted", (J * S.inv() * unit)[0], (J * unit)[0])
differs("squared condition ratio instead of actual sharp ratio", kappa, kappa ** 2)

proof = HERE / "ENDPOINT_METRIC_HEAT.tex"
result = {"status": "pass", "exact_checks": checks, "negative_controls": controls,
          "proof_sha256": hashlib.sha256(proof.read_bytes()).hexdigest(),
          "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          "cases": reports,
          "scope": "Exact finite identities and sampled generalized quotients; complete uniform estimates are proved in the TeX."}
print(json.dumps(result, indent=2))
