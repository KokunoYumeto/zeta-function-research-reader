"""Exact symbolic checks for the ES quarter, tetrahedral and heat trace maps.

Run with Python and SymPy. The neighboring JSON receipt records the precise
finite scope. The accompanying Markdown supplies the complete proofs, including
universal and nonexistence assertions that are not replaced by these checks.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from datetime import datetime, timezone
from pathlib import Path

import sympy as S


Q = S.Rational
sqrt = S.sqrt
a, h = S.symbols("a h", real=True)
t = S.symbols("t", positive=True)
c, d, e, f = S.symbols("c d e f")
I2, I4 = S.eye(2), S.eye(4)
E11 = S.Matrix([[1, 0], [0, 0]])
E12 = S.Matrix([[0, 1], [0, 0]])
E21 = S.Matrix([[0, 0], [1, 0]])
E22 = S.Matrix([[0, 0], [0, 1]])
raw_basis = [I4[:, j] for j in range(4)]
results: list[dict] = []


def entries(value):
    if isinstance(value, S.MatrixBase):
        return list(value)
    if isinstance(value, (tuple, list)):
        return [entry for item in value for entry in entries(item)]
    return [S.sympify(value)]


def reduced(value):
    return S.factor(S.cancel(S.simplify(value)))


def is_zero(value):
    return all(reduced(entry) == 0 for entry in entries(value))


def check(name, expressions, locators, domain="real a; exact algebraic constants"):
    residuals = [reduced(value) for value in entries(expressions)]
    nonzero = [str(value) for value in residuals if value != 0]
    item = {
        "name": name,
        "proof_locators": locators,
        "domain": domain,
        "scalar_identities": len(residuals),
        "passed": not nonzero,
    }
    if nonzero:
        item["nonzero_residuals"] = nonzero
    results.append(item)


def check_boolean(name, condition, locators, details):
    results.append({
        "name": name,
        "proof_locators": locators,
        "domain": "the 24 explicitly enumerated permutations of four labels",
        "passed": bool(condition),
        "details": details,
    })


def vec(matrix):
    return S.Matrix([matrix[0, 0], matrix[0, 1], matrix[1, 0], matrix[1, 1]])


def permutation_matrix(permutation):
    matrix = S.zeros(4)
    for column, row in enumerate(permutation):
        matrix[row, column] = 1
    return matrix


G = S.Matrix([
    [Q(1, 16), 0, 0, -Q(7, 144)],
    [0, Q(2, 9), 0, 0],
    [0, 0, 1, 0],
    [-Q(7, 144), 0, 0, Q(1, 16)],
])
A0 = S.diag(Q(1, 4), Q(1, 4), -Q(1, 4), Q(1, 4))
A = S.diag(Q(1, 4), Q(1, 4), a, Q(1, 4))
Pminus = S.diag(0, 0, 1, 0)
ah = -Q(1, 4) + 2 * h
Ah = A.subs(a, ah)
B = G * A
Qraw = 4 * A0

check("negative_projector", [Pminus - I4 / 2 + 2 * A0,
                              Pminus**2 - Pminus], ["ESQ2", "ESQ3"])
check("heat_operator_and_self_adjointness", [Ah - A0 - 2 * h * Pminus,
                                           A.T * G - G * A],
      ["ESQ11", "ESQ12"])
check("heat_rank_one_derivative", S.diff(G * Ah, h) - 2 * Pminus, ["ESQ15"])
check("scalar_heat_time", Ah.subs(h, Q(1, 4)) - I4 / 4, ["ESQ11"])
check("marked_source_values", [
    ((2 * raw_basis[2]).T * G * Ah * (2 * raw_basis[2]))[0] - 4 * ah,
    (raw_basis[1].T * G * Ah * raw_basis[1])[0] - Q(1, 18),
], ["ESQ15a"])

Cquarter = S.Matrix([
    [1, 0, 2, 1],
    [Q(1, 2), 0, 0, -Q(1, 2)],
    [0, 1, 0, 0],
    [Q(1, 4), 0, -Q(1, 2), Q(1, 4)],
])
Cquarter_inverse = S.Matrix([
    [Q(1, 4), 1, 0, 1],
    [0, 0, 1, 0],
    [Q(1, 4), 0, 0, -1],
    [Q(1, 4), -1, 0, 1],
])
Iquarter = S.Matrix([
    [0, 0, 0, 1], [0, Q(1, 4), 0, 0],
    [0, 0, Q(1, 4), 0], [Q(1, 16), 0, 0, 0],
])
check("original_quarter_inverse", [Cquarter * Cquarter_inverse - I4,
                                   Cquarter_inverse * Cquarter - I4],
      ["ESQ5", "ESQ6"])
check("original_quarter_intertwiner", Cquarter * A0 - Iquarter * Cquarter,
      ["ESQ7", "ESQ8"])
check("entire_heat_intertwiner",
      Cquarter * Ah - (h * I4 + (1 - 4 * h) * Iquarter) * Cquarter,
      ["ESQ16"])
alpha, beta0, beta1, gamma = S.symbols("alpha beta0 beta1 gamma", real=True)
coefficient_vector = S.Matrix([alpha, beta0, beta1, gamma])
metric_target = Cquarter_inverse.T * G * Cquarter_inverse
form_target = Cquarter_inverse.T * B * Cquarter_inverse
check("transported_coefficient_metric", (coefficient_vector.T * metric_target
      * coefficient_vector)[0] - (alpha + 4 * gamma)**2 / 576
      - Q(2, 9) * (beta0**2 + beta1**2) - (alpha / 4 - gamma)**2,
      ["ESQ17"])
check("transported_coefficient_heat_form", (coefficient_vector.T * form_target
      * coefficient_vector)[0] - (alpha + 4 * gamma)**2 / 2304
      - (beta0**2 + beta1**2) / 18 - a * (alpha / 4 - gamma)**2,
      ["ESQ18"])

T = S.Matrix([
    [Q(1, 24), 0, 0, Q(1, 24)],
    [1 / (6 * sqrt(2)), 0, 0, -1 / (6 * sqrt(2))],
    [0, 1 / (3 * sqrt(2)), 0, 0],
    [0, 0, 1, 0],
])
T_inverse = S.Matrix([
    [12, 3 * sqrt(2), 0, 0],
    [0, 0, 3 * sqrt(2), 0],
    [0, 0, 0, 1],
    [12, -3 * sqrt(2), 0, 0],
])
check("trace_isometry_inverse", [T * T_inverse - I4, T_inverse * T - I4],
      ["ESQ24", "ESQ25"])
check("full_trace_isometry", T.T * S.diag(1, 1, 1, a) * T - B,
      ["ESQ26", "ESQ27"])
check("fixed_metric_in_trace_coordinates", T.T * S.diag(4, 4, 4, 1) * T - G,
      ["ESQ30"])
check("trace_coordinate_heat_operator",
      T * A - S.diag(Q(1, 4), Q(1, 4), Q(1, 4), a) * T, ["ESQ30"])
check("raw_reflection_trace_intertwiner", T * Qraw - S.diag(1, 1, 1, -1) * T,
      ["ESQ29"])
half_to_full = S.diag(1, 1, 1 / sqrt(2), 1 / sqrt(2))
check("HEB_half_to_full_trace_factor",
      half_to_full.T * S.diag(1, 1, 2, 2 * a) * half_to_full
      - S.diag(1, 1, 1, a), ["ESQ28"])
s = S.symbols("s")
check("HEB_endpoint_polynomial", (s - Q(1, 2))**2 + ah
      - (s * (s - 1) + 2 * h), ["ESQ32"])
endpoint_inverse = S.Matrix([[Q(1, 2), Q(1, 2)], [-1, 1]])
check("HEB_endpoint_half_pairing",
      endpoint_inverse.T * S.diag(1, -Q(1, 4)) * endpoint_inverse
      - S.Matrix([[0, Q(1, 2)], [Q(1, 2), 0]]), ["ESQ33", "ESQ34"])


def rho(first, second):
    return S.Matrix([[first, -a * second], [second, first]])


Ka = E21 - a * E12
Jalgebra = S.diag(1, -1)
N = S.Matrix([[1, 0], [0, -a], [0, 1], [1, 0]])
check("quadratic_matrix_relation", Ka**2 + a * I2, ["ESQ36"])
check("quadratic_algebra_multiplication",
      rho(c, d) * rho(e, f) - rho(c * e - a * d * f, c * f + d * e),
      ["ESQ36"], "real a; arbitrary real or complex c,d,e,f")
check("quadratic_regular_trace", S.trace(rho(c, d)) - 2 * c, ["ESQ20", "ESQ36"])
check("quadratic_algebra_involution",
      Jalgebra * S.conjugate(rho(c, d)) * Jalgebra
      - rho(S.conjugate(c), -S.conjugate(d)),
      ["ESQ37"], "real a; complex c,d; conjugation explicit")
check("quadratic_reflected_trace",
      S.trace(Jalgebra * S.conjugate(rho(c, d)) * Jalgebra * rho(e, f)) / 2
      - S.conjugate(c) * e - a * S.conjugate(d) * f,
      ["ESQ38"], "real a; complex c,d,e,f; conjugation explicit")
check("raw_reflection_algebra_defect",
      Qraw * vec(rho(c, d)) - vec(rho(c, -d)) + 2 * a * d * vec(E12),
      ["ESQ38a"])
check("complex_raw_reflection_algebra_defect",
      Qraw * vec(S.conjugate(rho(c, d)))
      - vec(rho(S.conjugate(c), -S.conjugate(d)))
      + 2 * a * S.conjugate(d) * vec(E12),
      ["ESQ38a"], "real a; complex c,d; conjugation explicit")
check("algebra_embedding_ES_form",
      N.T * B * N - S.diag(Q(1, 144), a + a**2 / 18), ["ESQ39"])
check("collision_algebra_corner", [Ka.subs(a, 0) - E21,
      rho(c, d).subs(a, 0) - c * I2 - d * E21, E21**2], ["ESQ40"])

R = S.Matrix([
    [Q(1, 4), sqrt(3) / 2, 0, Q(3, 4)],
    [-sqrt(3) / 4, -Q(1, 2), 0, sqrt(3) / 4],
    [0, 0, 1, 0],
    [Q(3, 4), -sqrt(3) / 2, 0, Q(1, 4)],
])
Jnative = permutation_matrix((3, 1, 2, 0))
R_trace = S.Matrix([
    [1, 0, 0, 0], [0, -Q(1, 2), sqrt(3) / 2, 0],
    [0, -sqrt(3) / 2, -Q(1, 2), 0], [0, 0, 0, 1],
])
check("native_D3_relations", [R**3 - I4, Jnative**2 - I4,
                              Jnative * R * Jnative - R**2], ["ESQ41"])
check("native_D3_trace_coordinate_action",
      [T * R - R_trace * T, T * Jnative - S.diag(1, -1, 1, 1) * T],
      ["ESQ42", "ESQ43"])
check("native_D3_fixed_metric_and_heat_symmetry",
      [R.T * G * R - G, Jnative.T * G * Jnative - G,
       R * A - A * R, Jnative * A - A * Jnative,
       R.T * B * R - B, Jnative.T * B * Jnative - B], ["ESQ44"])
check("native_D3_fixes_collision_corner",
      [R * vec(I2) - vec(I2), R * vec(E21) - vec(E21),
       Jnative * vec(I2) - vec(I2), Jnative * vec(E21) - vec(E21)],
      ["ESQ40", "ESQ44"])
R_E12 = S.Matrix(2, 2, list(R * vec(E12)))
check("native_rotation_is_not_matrix_multiplicative", R_E12**2 - Q(3, 4) * I2,
      ["ESQ44"])

ray_infinity = S.Matrix([-6, 0, 0, -6])
ray_zero = S.Matrix([2, 2, 0, 2])
ray_plus = S.Matrix([2 + sqrt(3), -1, 0, 2 - sqrt(3)])
ray_minus = S.Matrix([2 - sqrt(3), -1, 0, 2 + sqrt(3)])
rays = [ray_infinity, ray_zero, ray_plus, ray_minus]
ray_matrix = S.Matrix.hstack(*rays)
ray_gram = Q(4, 3) * I4 - S.ones(4) / 3
check("tetrahedral_ray_Gram_and_sum",
      [ray_matrix.T * G * ray_matrix - ray_gram,
       sum(rays, S.zeros(4, 1))], ["ESQ45", "ESQ47"])
positive_rows = [0, 1, 3]
positive_ray_basis = S.Matrix.hstack(ray_zero, ray_plus, ray_minus)[positive_rows, :]
check("positive_ray_basis_determinant", positive_ray_basis.det() + 24 * sqrt(3),
      ["ESQ47"])
check("native_D3_ray_action", [R * ray_zero - ray_plus, R * ray_plus - ray_minus,
      R * ray_minus - ray_zero, R * ray_infinity - ray_infinity,
      Jnative * ray_zero - ray_zero, Jnative * ray_plus - ray_minus,
      Jnative * ray_minus - ray_plus], ["ESQ48"])

K = S.Matrix([
    [Q(1, 3), -Q(8, 3), 0, -Q(2, 3)],
    [-Q(1, 6), Q(1, 3), 0, -Q(1, 6)],
    [0, 0, 1, 0],
    [-Q(2, 3), -Q(8, 3), 0, Q(1, 3)],
])
normal = ray_zero - ray_infinity
check("geometric_tetrahedral_transposition", [
    K - I4 + Q(3, 4) * normal * normal.T * G,
    (normal.T * G * normal)[0] - Q(8, 3),
    K * ray_zero - ray_infinity, K * ray_infinity - ray_zero,
    K * ray_plus - ray_plus, K * ray_minus - ray_minus,
    K.T * G * K - G, K * A - A * K,
], ["ESQ49", "ESQ50"])

W = S.Matrix.hstack(*[raw_basis[2] / 2 + sqrt(3) * ray / 2 for ray in rays])
W_inverse = W.T * G
uniform = S.ones(4, 1)
check("tetrahedral_orthonormal_frame", [W.T * G * W - I4,
      W * W_inverse - I4, W_inverse * raw_basis[2] - uniform / 2],
      ["ESQ51", "ESQ52"])
check("tetrahedral_uniform_projector",
      W_inverse * Pminus * W - uniform * uniform.T / 4, ["ESQ52", "ESQ53"])
frame_operator = I4 / 4 + (a - Q(1, 4)) * uniform * uniform.T / 4
check("tetrahedral_frame_heat_form_and_operator",
      [W_inverse * A * W - frame_operator, W.T * B * W - frame_operator],
      ["ESQ53", "ESQ54"])

raw_metric_preserving = []
raw_heat_commuting = []
for permutation in itertools.permutations(range(4)):
    permutation_name = "".join(str(index) for index in permutation)
    P = permutation_matrix(permutation)
    geometric = Pminus + Q(3, 4) * sum(
        (rays[permutation[index]] * rays[index].T * G for index in range(4)),
        S.zeros(4),
    )
    check("geometric_S4_" + permutation_name,
          [geometric - W * P * W_inverse, geometric.T * G * geometric - G,
           geometric * A - A * geometric], ["ESQ47a", "ESQ52", "ESQ53"])
    G_permuted = P * G * P.T
    A_permuted = P * A * P.T
    check("transported_raw_permutation_" + permutation_name,
          [P.T * G_permuted * P - G, A_permuted * P - P * A,
           G_permuted * A_permuted - P * B * P.T,
           (T * P.T).T * S.diag(1, 1, 1, a) * (T * P.T) - P * B * P.T],
          ["ESQ55", "ESQ56"])
    if is_zero(P.T * G * P - G):
        raw_metric_preserving.append(list(permutation))
    if is_zero(P * A - A * P):
        raw_heat_commuting.append(list(permutation))
check_boolean("raw_metric_permutation_classification",
              raw_metric_preserving == [[0, 1, 2, 3], [3, 1, 2, 0]], ["ESQ55"],
              {"metric_preserving_permutations": raw_metric_preserving,
               "index_order": ["E11", "E12", "E21", "E22"]})
check_boolean("raw_heat_permutation_classification",
              raw_heat_commuting == [list(p) for p in itertools.permutations(range(4))
                                     if p[2] == 2], ["ESQ55"],
              {"commuting_permutations_for_symbolic_a": raw_heat_commuting,
               "exceptional_scalar_value": "a=1/4, equivalently h=1/4"})

simplex = [raw_basis[2]] + [sqrt(15) * ray / 4 - raw_basis[2] / 4 for ray in rays]
simplex_matrix = S.Matrix.hstack(*simplex)
check("regular_four_simplex", [
    simplex_matrix.T * G * simplex_matrix - Q(5, 4) * S.eye(5) + S.ones(5) / 4,
    sum(simplex, S.zeros(4, 1)),
    sum(simplex[1:], S.zeros(4, 1)) / 4 + raw_basis[2] / 4,
], ["ESQ57", "ESQ58"])
check("simplex_quarter_axis_intertwiner",
      Cquarter * (-raw_basis[2] / 4) - S.Matrix([-Q(1, 2), 0, 0, Q(1, 8)]),
      ["ESQ59"])

La = S.Matrix([
    [-17 / (9 * a), 17 / (54 * a**2), 1 / (9 * a)],
    [1, -1 / (6 * a), 0],
    [0, -sqrt(3) / (3 * sqrt(-a)), 0],
])
L0 = S.Matrix([
    [Q(68, 9), Q(136, 27), -Q(4, 9)],
    [1, Q(2, 3), 0],
    [0, -2 * sqrt(3) / 3, 0],
])
offset = S.Matrix([Q(17, 9), Q(3, 2), 0])
vF = S.Matrix([1, 0, 17])
L_negative = La.subs(a, -t**2)
ga_negative = L_negative.T * L_negative
negative_domain = "a=-t^2, t>0; precisely the real parameter region a<0"
check("moving_spatial_original_specialization", La.subs(a, -Q(1, 4)) - L0,
      ["ESQ63", "ESQ65"], "a=-1/4")
check("moving_spatial_determinant",
      L_negative.det() - sqrt(3) / (27 * t**3), ["ESQ65"], negative_domain)
check("moving_spatial_normal_and_unit_length", [
    L_negative * vF - S.Matrix([0, 1, 0]),
    ga_negative * vF - S.Matrix([1, 1 / (6 * t**2), 0]),
    (vF.T * ga_negative * vF)[0] - 1,
], ["ESQ66", "ESQ68"], negative_domain)
check("fixed_original_spatial_normal", [
    L0 * vF - S.Matrix([0, 1, 0]),
    L0.T * L0 * vF - S.Matrix([1, Q(2, 3), 0]),
], ["ESQ64"], "the original spatial metric at a=-1/4")

p0 = S.Matrix([0, 0, -t**2])
pplus = S.Matrix([-1 / (2 * t), 3 * t, 26 * t**2])
pminus = S.Matrix([1 / (2 * t), -3 * t, 26 * t**2])
target = S.Matrix([-t**2, 0, 0])
centroid = S.Matrix([0, 0, 17 * t**2])
moving_points = [p0, pplus, pminus, target]
expected_images = [
    S.Matrix([2, Q(3, 2), 0]),
    S.Matrix([-1, Q(3, 2), -sqrt(3)]),
    S.Matrix([-1, Q(3, 2), sqrt(3)]),
    S.Matrix([0, Q(3, 2) - t**2, 0]),
]
for label, point, expected in zip(
        ["finite", "positive_root", "negative_root", "target"],
        moving_points, expected_images):
    check("moving_spatial_image_" + label, L_negative * point + offset - expected,
          ["ESQ61", "ESQ67"], negative_domain)
check("moving_spatial_centroid_face_displacement", [
    (p0 + pplus + pminus) / 3 - centroid,
    target - centroid + t**2 * vF,
    (pplus - p0).cross(pminus - p0) - 27 * t * S.Matrix([6 * t**2, 1, 0]),
    *[point[1] + 6 * t**2 * point[0] for point in [p0, pplus, pminus]],
], ["ESQ62"], negative_domain)


def main():
    directory = Path(__file__).resolve().parent
    proof = directory / "ES_QUARTER_HEAT_TRACE_DERIVATION.md"
    receipt = directory / "ES_QUARTER_HEAT_TRACE_CHECKS.json"
    failed = [result["name"] for result in results if not result["passed"]]
    report = {
        "status": "PASS" if not failed else "FAIL",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "checker": Path(__file__).name,
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "proof": proof.name,
        "proof_sha256": hashlib.sha256(proof.read_bytes()).hexdigest(),
        "sympy_version": S.__version__,
        "method": "Exact symbolic reduction of displayed matrix and polynomial identities; no floating-point sampling.",
        "scope": [
            "Original quarter intertwiner and inverse, rank-one heat operator and fixed metric.",
            "Full trace-coordinate inverse isometry, half-trace factor and endpoint polynomial.",
            "Quadratic algebra embedding, reflected involution, raw-reflection defect and collision corner.",
            "Native D3, all 24 geometric tetrahedral permutations, tetrahedral orthonormal frame and raw metric transport.",
            "Regular four-simplex Gram matrix and quarter-axis identity.",
            "Actual moving spatial affine map for a<0: all four images, determinant, centroid, face and unit normal.",
        ],
        "proof_scope_boundary": "The Markdown contains the full proofs, including universal map claims, nonexistence of ring maps, signatures and domains. This receipt checks only the explicitly listed finite identities; it asserts no global Weil positivity or zeta-zero conclusion.",
        "check_count": len(results),
        "scalar_identity_count": sum(result.get("scalar_identities", 0) for result in results),
        "failed_checks": failed,
        "checks": results,
    }
    receipt.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "checks": len(results),
                      "scalar_identities": report["scalar_identity_count"],
                      "failed_checks": failed, "receipt": receipt.name}, indent=2))
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
