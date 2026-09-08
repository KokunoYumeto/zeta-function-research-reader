# Portable adaptation of tao2024/metric_lift/checks/replay_metric_checks.py
# Only import/output/inventory handling changed; the delimited mathematics is a raw source byte slice.
from __future__ import annotations
from fractions import Fraction
from itertools import combinations
import sympy as s
import sympy as sp
import sympy as S
from portable_common import begin, finish
begin('tao_metric')
# BEGIN UNCHANGED MATHEMATICAL BODY
CHECKS = []


def equal(name, lhs, rhs, scope):
    """Record original sides and prove zero residual by exact rational algebra."""
    raw = lhs - rhs
    residual = sp.cancel(sp.together(raw))
    CHECKS.append({
        "name": name, "scope": scope, "lhs": str(lhs), "rhs": str(rhs),
        "raw_residual": str(raw), "exact_residual": str(residual),
        "passed": residual == 0,
    })
    if residual != 0:
        raise AssertionError(f"{name}: {residual}")


def matrix_equal(name, lhs, rhs, scope):
    assert lhs.shape == rhs.shape
    for i in range(lhs.rows):
        for j in range(lhs.cols):
            equal(f"{name}[{i},{j}]", lhs[i, j], rhs[i, j], scope)


# Adapted-basis check: (v,w,e1,e2), with e1,e2 in ker(theta) intersect ker(eta).
# Positivity: a>0, ac-b^2>0; k11>0, k11*k22-k12^2>0.
a, b, c, k11, k12, k22 = sp.symbols("a b c k11 k12 k22", real=True)
H = sp.Matrix([[a, b], [b, c]])
K = sp.Matrix([[k11, k12], [k12, k22]])
G = sp.diag(H, K)
z0, z1, z2, z3 = sp.symbols("z0 z1 z2 z3", real=True)
z = sp.Matrix([z0, z1, z2, z3])
forms = sp.Matrix([[a, b, 0, 0], [b, c, 0, 0]])
coefficients = H.inv() * forms * z
matrix_equal("adapted_projection_coefficients", coefficients, sp.Matrix([z0, z1]), "n=4, general H and K")
matrix_equal("prescribed_forms_are_first_metric_rows", G[:2, :], forms, "n=4, general H and K")
equal("adapted_block_determinant", G.det(), H.det() * K.det(), "n=4, general H and K")

# General frame check in dimension two. No v or w coordinate is normalized.
h11, h12, h22 = sp.symbols("h11 h12 h22", real=True)
v1, v2, w1, w2 = sp.symbols("v1 v2 w1 w2", real=True)
h2 = sp.Matrix([[h11, h12], [h12, h22]])
T = sp.Matrix([[v1, w1], [v2, w2]])
frame_gram = T.T * h2 * T
equal("two_dimensional_volume_squared", frame_gram.det(), h2.det() * T.det()**2,
      "n=2: vol_h(v,w)=sqrt(det h)*(v1*w2-v2*w1), with the chosen orientation")

# The integer m is positive. Positive q ensures the real power is unambiguous.
q = sp.symbols("q", positive=True)
m = sp.symbols("m", positive=True, integer=True)
lam = q ** (sp.Integer(2) / m)
equal("all_positive_integer_dimensions_scaling_power", lam**m, q**2,
      "all integers m>=1; this checks the power identity used by the multilinear determinant proof")
equal("positive_volume_ratio", sp.sqrt(q**2), q, "q>0 fixes the positive square-root branch")
equal("one_transverse_direction_determinant", (q**2 * sp.Matrix([[k11]])).det(), q**2*k11, "m=1")
equal("two_transverse_directions_determinant", (q*K).det(), q**2*K.det(), "m=2, full K")

# Full, variable two-dimensional base metric; no diagonal or flat assumption.
x, y, s = sp.symbols("x y s", real=True)
base_coords = (x, y)
all_coords = (x, y, s)
A = sp.Function("A", real=True)(x, y)
B = sp.Function("B", real=True)(x, y)
C = sp.Function("C", real=True)(x, y)
f = sp.Function("f", real=True)(x, y)
base = sp.Matrix([[A, B], [B, C]])
warped = sp.diag(base, f**2)
base_inv = base.inv()
warped_inv = warped.inv()
D = A*C - B**2
matrix_equal("warped_inverse", warped_inv, sp.diag(base_inv, f**-2), "n=2 base, circle fiber")
equal("warped_determinant", warped.det(), f**2 * D, "n=2 base, f>0")


def christoffel(metric, coordinates):
    inv = metric.inv()
    dim = len(coordinates)
    return [[[sum(inv[k, ell]*(sp.diff(metric[ell, j], coordinates[i])
                           + sp.diff(metric[ell, i], coordinates[j])
                           - sp.diff(metric[i, j], coordinates[ell]))
                    for ell in range(dim))/2
              for j in range(dim)] for i in range(dim)] for k in range(dim)]


base_gamma = christoffel(base, base_coords)
warped_gamma = christoffel(warped, all_coords)
for k in range(3):
    for i in range(3):
        for j in range(3):
            if k < 2 and i < 2 and j < 2:
                expected = base_gamma[k][i][j]
            elif k == 2 and ((i == 2) != (j == 2)):
                horizontal = j if i == 2 else i
                expected = sp.diff(f, base_coords[horizontal]) / f
            elif k < 2 and i == 2 and j == 2:
                expected = -f * sum(base_inv[k, ell]*sp.diff(f, base_coords[ell]) for ell in range(2))
            else:
                expected = sp.Integer(0)
            equal(f"warped_christoffel[{k},{i},{j}]", warped_gamma[k][i][j], expected,
                  "n=2 base, full variable symmetric metric; all 27 components")

X = [sp.Function("X1", real=True)(x,y), sp.Function("X2", real=True)(x,y)]
Y = [sp.Function("Y1", real=True)(x,y), sp.Function("Y2", real=True)(x,y)]
div_base = sum(sp.diff(X[i], base_coords[i]) for i in range(2)) + sum(base_gamma[i][i][j]*X[j] for i in range(2) for j in range(2))
div_warp = sum(sp.diff(X[i], base_coords[i]) for i in range(2)) + sum(warped_gamma[i][i][j]*X[j] for i in range(3) for j in range(2))
drift_X = sum(X[i]*sp.diff(f, base_coords[i])/f for i in range(2))
equal("horizontal_divergence", div_warp, div_base + drift_X, "arbitrary base X, independent of s")

# Direct comparison with the volume divergence formula on D>0 and f>0.
rho = sp.sqrt(D)
div_base_density = sum(sp.diff(rho*X[i], base_coords[i]) for i in range(2))/rho
div_warp_density = sum(sp.diff(f*rho*X[i], base_coords[i]) for i in range(2))/(f*rho)
equal("base_connection_equals_volume_divergence", div_base, div_base_density, "D>0")
equal("warped_connection_equals_volume_divergence", div_warp, div_warp_density, "D>0, f>0")

for k in range(3):
    conn_warp = (sum(X[i]*sp.diff(Y[k], base_coords[i]) for i in range(2)) if k < 2 else 0) + sum(warped_gamma[k][i][j]*X[i]*Y[j] for i in range(2) for j in range(2))
    conn_base = (sum(X[i]*sp.diff(Y[k], base_coords[i]) for i in range(2)) + sum(base_gamma[k][i][j]*X[i]*Y[j] for i in range(2) for j in range(2))) if k < 2 else 0
    equal(f"horizontal_connection_preservation[{k}]", conn_warp, conn_base, "arbitrary base X,Y lifted independently of s")

F = sp.Function("F", real=True)(x,y)
def scalar_laplacian(gamma, inverse, coordinates, field):
    dim = len(coordinates)
    return sum(inverse[i,j]*(sp.diff(field, coordinates[i], coordinates[j])
                 - sum(gamma[k][i][j]*sp.diff(field, coordinates[k]) for k in range(dim)))
               for i in range(dim) for j in range(dim))

lap_base = scalar_laplacian(base_gamma, base_inv, base_coords, F)
lap_warp = scalar_laplacian(warped_gamma, warped_inv, all_coords, F)
drift_F = sum(base_inv[i,j]*sp.diff(f, base_coords[i])*sp.diff(F, base_coords[j])/f for i in range(2) for j in range(2))
equal("base_scalar_laplacian_drift", lap_warp, lap_base + drift_F,
      "Delta=div grad; F independent of s; full variable base metric")
gradF = [sum(base_inv[i,j]*sp.diff(F,base_coords[j]) for j in range(2)) for i in range(2)]
lap_warp_density = sum(sp.diff(f*rho*gradF[i], base_coords[i]) for i in range(2))/(f*rho)
equal("laplacian_connection_equals_density_expression", lap_warp, lap_warp_density, "D>0, f>0")

# An actual counterexample to unconditional scalar-Laplacian preservation.
# x,y remain the original flat coordinates on R^2; f=exp(x), F=x exactly.
flat = sp.eye(2)
flat_warp = sp.diag(1, 1, sp.exp(2*x))
flat_gamma = christoffel(flat, base_coords)
flat_warp_gamma = christoffel(flat_warp, all_coords)
equal("counterexample_base_laplacian", scalar_laplacian(flat_gamma, flat.inv(), base_coords, x), 0,
      "M=R^2, h=dx^2+dy^2, F=x")
equal("counterexample_warp_laplacian", scalar_laplacian(flat_warp_gamma, flat_warp.inv(), all_coords, x), 1,
      "M x S^1, hbar=dx^2+dy^2+exp(2x)ds^2, f=exp(x), F=x")

# Independent second-order vector/form operator extension. The base is exactly
# flat R^2, while f(x,y), X1(x,y), X2(x,y), and form coefficients remain arbitrary.
# This is supplemental to the dimension-independent proof, not a replacement.
flat_general_warp = sp.diag(1, 1, f**2)
fgw_inverse = flat_general_warp.inv()
fgw_gamma = christoffel(flat_general_warp, all_coords)
Z = [sp.diff(f, coordinate)/f for coordinate in base_coords]
lifted_X = X + [sp.Integer(0)]


def rough_vector(field, coordinates, gamma, inverse):
    dim = len(coordinates)
    first = [[sp.diff(field[k], coordinates[j])
              + sum(gamma[k][j][ell]*field[ell] for ell in range(dim))
              for k in range(dim)] for j in range(dim)]
    return [sum(inverse[i,j]*(sp.diff(first[j][k], coordinates[i])
                    + sum(gamma[k][i][ell]*first[j][ell] for ell in range(dim))
                    - sum(gamma[ell][i][j]*first[ell][k] for ell in range(dim)))
                for i in range(dim) for j in range(dim)) for k in range(dim)]


flat_rough = rough_vector(X, base_coords, flat_gamma, flat)
warped_rough = rough_vector(lifted_X, all_coords, fgw_gamma, fgw_inverse)
for k in range(3):
    expected = (flat_rough[k] + sum(Z[j]*sp.diff(X[k],base_coords[j]) for j in range(2))
                - sum(Z[j]*X[j] for j in range(2))*Z[k]) if k < 2 else 0
    equal(f"rough_vector_warped_drift_and_rank_one_term[{k}]", warped_rough[k], expected,
          "flat R^2 base; arbitrary f(x,y)>0 and arbitrary horizontal X; coordinate trace of the full second covariant derivative")


def form_component(form, indices):
    if len(set(indices)) != len(indices):
        return sp.Integer(0)
    sign = (-1)**sum(indices[i]>indices[j] for i in range(len(indices)) for j in range(i+1,len(indices)))
    return sign * form.get(tuple(sorted(indices)), sp.Integer(0))


def exterior_derivative(form, degree, coordinates):
    return {indices: sum((-1)**r*sp.diff(form_component(form,indices[:r]+indices[r+1:]),coordinates[indices[r]])
                         for r in range(degree+1))
            for indices in combinations(range(len(coordinates)),degree+1)}


def covariant_form_component(form, indices, derivative_index, coordinates, gamma):
    return sp.diff(form_component(form,indices),coordinates[derivative_index]) - sum(
        gamma[ell][derivative_index][indices[r]]
        *form_component(form,indices[:r]+(ell,)+indices[r+1:])
        for r in range(len(indices)) for ell in range(len(coordinates)))


def codifferential(form, degree, coordinates, gamma, inverse):
    if degree == 0:
        return {}
    dim = len(coordinates)
    return {indices: -sum(inverse[i,j]*covariant_form_component(form,(j,)+indices,i,coordinates,gamma)
                          for i in range(dim) for j in range(dim))
            for indices in combinations(range(dim),degree-1)}


def hodge_laplacian(form, degree, coordinates, gamma, inverse):
    d_delta = exterior_derivative(codifferential(form,degree,coordinates,gamma,inverse),degree-1,coordinates) if degree else {():sp.Integer(0)}
    delta_d = codifferential(exterior_derivative(form,degree,coordinates),degree+1,coordinates,gamma,inverse)
    return {indices: form_component(d_delta,indices)+form_component(delta_d,indices)
            for indices in combinations(range(len(coordinates)),degree)}


def contraction(form, degree, vector, dim):
    if degree == 0:
        return {}
    return {indices: sum(vector[j]*form_component(form,(j,)+indices) for j in range(dim))
            for indices in combinations(range(dim),degree-1)}


def lie_form_component(form, indices, vector, coordinates):
    return (sum(vector[j]*sp.diff(form_component(form,indices),coordinates[j]) for j in range(len(coordinates)))
            +sum(sp.diff(vector[j],coordinates[indices[r]])*form_component(form,indices[:r]+(j,)+indices[r+1:])
                 for r in range(len(indices)) for j in range(len(coordinates))))


P = sp.Function("P", real=True)(x,y)
Q = sp.Function("Q", real=True)(x,y)
R = sp.Function("R", real=True)(x,y)
base_forms = [(0,{():F}),(1,{(0,):P,(1,):Q}),(2,{(0,1):R})]
for degree, form in base_forms:
    # The same dictionary on the product represents pullback: omitted vertical
    # components are exactly zero, including their covariant derivatives' input.
    delta_base = codifferential(form,degree,base_coords,flat_gamma,flat)
    delta_warp = codifferential(form,degree,all_coords,fgw_gamma,fgw_inverse)
    i_Z = contraction(form,degree,Z+[sp.Integer(0)],3)
    if degree > 0:
        for indices in combinations(range(3),degree-1):
            equal(f"codifferential_pullback_k{degree}{indices}",form_component(delta_warp,indices),
                  form_component(delta_base,indices)-form_component(i_Z,indices),
                  "flat R^2 base; full arbitrary base form of this degree; all output components including vertical")
    hodge_base = hodge_laplacian(form,degree,base_coords,flat_gamma,flat)
    hodge_warp = hodge_laplacian(form,degree,all_coords,fgw_gamma,fgw_inverse)
    for indices in combinations(range(3),degree):
        lie_Z = lie_form_component(form,indices,Z+[sp.Integer(0)],all_coords)
        equal(f"hodge_pullback_minus_lie_derivative_k{degree}{indices}",form_component(hodge_warp,indices),
              form_component(hodge_base,indices)-lie_Z,
              "flat R^2 base; delta=-trace covariant derivative and Delta_H=d delta+delta d; k=0,1,2 checked separately")

# END UNCHANGED MATHEMATICAL BODY
finish('tao_metric', CHECKS)
