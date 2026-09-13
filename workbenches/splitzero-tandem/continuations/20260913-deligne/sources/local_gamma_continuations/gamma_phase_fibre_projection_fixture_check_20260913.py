"""Exact independent finite models for GP.6--11 and GP.20--23.

These are algebraic fixtures, not arithmetic packet measurements.
"""
import json
from pathlib import Path
import sympy as s

I = s.I
Q = s.Rational
checks = []

def equal(label, actual, expected):
    residual = s.simplify(actual - expected)
    ok = residual == (s.zeros(*residual.shape) if isinstance(residual, s.MatrixBase) else 0)
    checks.append({"label": label, "passed": bool(ok)})
    if not ok:
        raise RuntimeError(f"{label}: residual {residual}")

def adjoint(A, G_source, G_target):
    return G_source.inv() * A.conjugate().T * G_target

def display(value):
    return str(value)

# One exact fibre with original mass 7 and conditional masses 1/3, 2/3.
mass = s.Integer(7)
G = s.diag(Q(7, 3), Q(14, 3))
G_sum = s.Matrix([[mass]])
U = s.ones(2, 1)
C = s.Matrix([[Q(1, 3), Q(2, 3)]])
a = s.Matrix([1 + I, 2 + I])
T = s.diag(*a)
b = s.Integer(4)
a_k = Q(5, 3) + I
variance = Q(2, 9)
G_h = T.conjugate().T * G * T
G_h_sum = s.Matrix([[mass * b]])
T_sum = s.Matrix([[2]])
C_h = s.Matrix([[Q(1, 6), Q(5, 6)]])
P = U * C
P_h = U * C_h
J = T * U * T_sum.inv()
J_star = adjoint(J, G_sum, G)
Q_projection = J * J_star
gamma = Q(5, 6) + I / 2
N = J - U * gamma
N_star = adjoint(N, G_sum, G)

equal("base sum adjoint and original mass", adjoint(U, G_sum, G), C)
equal("arithmetic sum adjoint", adjoint(U, G_h_sum, G_h), C_h)
equal("T isometry", T.conjugate().T * G * T, G_h)
equal("T_sum isometry", T_sum.conjugate().T * G_sum * T_sum, G_h_sum)
equal("J exact adjoint conjugation", J_star, T_sum.inv() * C * T.conjugate())
equal("J isometry", J_star * J, s.eye(1))
equal("transported arithmetic projection", Q_projection, T * P_h * T.inv())
equal("fibre angle", C * J, s.Matrix([[gamma]]))
equal("orthogonal relative image", C * N, s.zeros(1, 1))
equal("relative defect", N_star * N, s.Matrix([[Q(1, 18)]]))
equal("unscaled conditional variance", (C * s.Matrix([2, 5]))[0] - a_k * s.conjugate(a_k), variance)
equal("mass retained in relative norm", (a - U * a_k).conjugate().T * G * (a - U * a_k), s.Matrix([[mass * variance]]))
equal("projection idempotence", Q_projection * Q_projection, Q_projection)
equal("projection metric adjoint", adjoint(Q_projection, G, G), Q_projection)
equal("projection difference trace", s.trace((P - Q_projection) ** 2), Q(1, 9))
commutator = P * Q_projection - Q_projection * P
equal("commutator Hilbert Schmidt norm", s.trace(adjoint(commutator, G, G) * commutator), Q(17, 162))
equal("two-point variance integral", Q(1, 2) * 2 * Q(1, 3) * Q(2, 3) * (a[0] - a[1]) * s.conjugate(a[0] - a[1]), variance)

# E=P_2(S), chi=S^2+(1+i)S+(2-i), quotient basis ([1],[S]).
# L maps the explicit frame (1,S,chi) into original monomial coordinates.
L = s.Matrix([[1, 0, 2 - I], [0, 1, 1 + I], [0, 0, 1]])
L_inv = L.inv()
M_coh_x = s.diag(4, 9, 2)
M_rel_x = s.Matrix([[2, 1, I], [1, 2, 1 + I], [-I, 1 - I, 3]])
M_h_x = M_coh_x + M_rel_x
B_x = s.Matrix([0, 0, 1])
R_coh_x = s.Matrix([[1, 0], [0, 1], [0, 0]])
pi_x = s.Matrix([[1, 0, 0], [0, 1, 0]])
K = s.simplify((B_x.conjugate().T * M_h_x * B_x).inv() * B_x.conjugate().T * M_rel_x * R_coh_x)
R_h_x = s.simplify(R_coh_x - B_x * K)
G_coh = R_coh_x.conjugate().T * M_coh_x * R_coh_x
G_arithmetic = s.simplify(R_h_x.conjugate().T * M_h_x * R_h_x)
term_boundary = s.simplify(K.conjugate().T * B_x.conjugate().T * M_coh_x * B_x * K)
term_relative = s.simplify(R_h_x.conjugate().T * M_rel_x * R_h_x)
Delta = s.simplify(G_arithmetic - G_coh)
root_inverse = s.diag(Q(1, 2), Q(1, 3))
E_q = s.simplify(root_inverse * Delta * root_inverse)
M_coh = s.simplify(L_inv.conjugate().T * M_coh_x * L_inv)
M_rel = s.simplify(L_inv.conjugate().T * M_rel_x * L_inv)
M_h = M_coh + M_rel
B = L * B_x
pi = pi_x * L_inv
R_coh = L * R_coh_x
R_h = s.simplify(L * R_h_x)

equal("monomial transport determinant", L.det(), 1)
equal("original polynomial relation", B, s.Matrix([2 - I, 1 + I, 1]))
equal("quotient annihilates relation", pi * B, s.zeros(2, 1))
equal("coherent section", pi * R_coh, s.eye(2))
equal("arithmetic section", pi * R_h, s.eye(2))
equal("coherent orthogonality", B.conjugate().T * M_coh * R_coh, s.zeros(1, 2))
equal("arithmetic orthogonality", s.simplify(B.conjugate().T * M_h * R_h), s.zeros(1, 2))
equal("nonzero correction K", K, s.Matrix([[-I / 5, (1 - I) / 5]]))
equal("monomial K formula", s.simplify((B.conjugate().T * M_h * B).inv() * B.conjugate().T * M_rel * R_coh), K)
equal("monomial two-term identity", s.simplify(R_h.conjugate().T * M_h * R_h), G_coh + term_boundary + term_relative)
equal("relative matrix principal minor 1", M_rel_x[:1, :1].det(), 2)
equal("relative matrix principal minor 2", M_rel_x[:2, :2].det(), 3)
equal("relative matrix principal minor 3", M_rel_x.det(), 5)
equal("strict quotient difference determinant", Delta.det(), Q(11, 5))
equal("boundary term rank-one determinant", term_boundary.det(), 0)
equal("relative term strict determinant", term_relative.det(), Q(47, 25))
equal("E_q determinant", E_q.det(), Q(11, 180))
equal("determinant correction", (s.eye(2) + E_q).det(), Q(76, 45))
equal("original determinant", G_arithmetic.det(), Q(304, 5))
equal("original determinant factorization", G_arithmetic.det(), G_coh.det() * (s.eye(2) + E_q).det())

results = {
    "status": "passed",
    "arithmetic_packet_claimed": False,
    "checks": checks,
    "fibre": {name: display(value) for name, value in {
        "original_gram": G, "arithmetic_gram": G_h,
        "P": P, "Q": Q_projection, "J": J, "J_star": J_star,
        "N": N, "gamma": gamma, "variance": variance,
    }.items()},
    "quotient": {name: display(value) for name, value in {
        "L": L, "pi": pi, "M_coh_monomial": M_coh,
        "M_rel_monomial": M_rel, "K": K, "R_h_monomial": R_h,
        "G_coh": G_coh, "G_h": G_arithmetic, "boundary_term": term_boundary,
        "relative_term": term_relative, "Delta": Delta, "E_q": E_q,
    }.items()},
}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
print(json.dumps(results, indent=2))
