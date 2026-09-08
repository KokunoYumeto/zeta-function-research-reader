"""Exact differential identities for the original polynomial material flow.

Generic test functions check the entire initial generator commutator,
including its first-order and matrix coefficients. Full finite-time
identities and operator-domain arguments are proved in the TeX section;
the separate endpoint script checks the finite-time trajectory matrices.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
checks = {}
def zero(name, expr):
    values = list(expr) if isinstance(expr, s.MatrixBase) else [expr]
    residuals = [s.expand(value) for value in values]
    checks[name] = all(value == 0 for value in residuals)
    if not checks[name]:
        raise AssertionError((name, residuals))

x,y,w = coords = s.symbols('x y w', real=True)
F = s.Matrix([
    (1+x*y)**3*w+y*y*(1+x*y)*(4+3*x*y),
    y+3*x*(1+x*y)**2*w+3*x*y*y*(4+3*x*y),
    2*x-3*x*x*y-x**3*w,
])
def grad(f): return s.Matrix([s.diff(f,q) for q in coords])
def lap(f): return sum(s.diff(f,q,2) for q in coords)
def div(v): return sum(s.diff(v[i],coords[i]) for i in range(3))
def curl(v):
    return s.Matrix([s.diff(v[2],y)-s.diff(v[1],w),
                     s.diff(v[0],w)-s.diff(v[2],x),
                     s.diff(v[1],x)-s.diff(v[0],y)])
W1 = -grad(F[1]).cross(grad(F[2]))/2
W2 = -grad(F[2]).cross(grad(F[0]))/2
U = (2*W1+6*F[2]*W2).applyfunc(s.expand)
DU = U.jacobian(coords)
omega = curl(U)
scalar = s.Function('phi')(x,y,w)
transport = lambda f: grad(f).dot(U)
S0 = DU+DU.T
zero('full_scalar_material_generator_derivative',
     transport(lap(scalar))-lap(transport(scalar))+div(S0*grad(scalar)))
zero('complete_first_order_diffusion_coefficient',
     s.Matrix([sum(s.diff(S0[i,j],coords[i]) for i in range(3))
               for j in range(3)])-U.applyfunc(lap))

V = s.Matrix([s.Function('V'+str(i))(x,y,w) for i in range(1,4)])
ad = lambda v: v.jacobian(coords)*U-DU*v
commutator = ad(V.applyfunc(lap))-ad(V).applyfunc(lap)
component_commutator = s.Matrix([transport(lap(v))-lap(transport(v)) for v in V])
matrix_correction = DU.applyfunc(lap)*V
for coordinate in coords:
    matrix_correction += 2*DU.diff(coordinate)*V.diff(coordinate)
zero('full_vector_generator_derivative_including_matrix_terms',
     commutator-component_commutator-matrix_correction)
zero('vorticity_stretching_identity',
     curl(DU*U)-omega.jacobian(coords)*U+DU*omega)
zero('Lie_covector_Bernoulli_gradient',DU.T*U-grad(U.dot(U)/2))

nu = s.symbols('nu', positive=True)
sigma,sigma_dot = s.symbols('sigma sigma_dot', real=True)
pressure = s.Function('p')(x,y,w)
force = DU*U-nu*U.applyfunc(lap)+grad(pressure)
actual_rescaled_force = sigma_dot*U+sigma*sigma*DU*U \
    -nu*sigma*U.applyfunc(lap)+sigma*sigma*grad(pressure)
written_rescaled_force = sigma_dot*U+sigma*sigma*force \
    +nu*(sigma*sigma-sigma)*U.applyfunc(lap)
zero('complete_time_rescaled_NS_force',actual_rescaled_force-written_rescaled_force)
zero('original_curl_axis',omega.subs({x:0,y:0},simultaneous=True)-s.Matrix([0,0,6]))
zero('original_laplacian_curl_axis',
     omega.applyfunc(lap).subs({x:0,y:0},simultaneous=True)-s.Matrix([0,0,-108*w]))
zero('all_pressure_rescaled_force_curl_axis',
     curl(actual_rescaled_force).subs({x:0,y:0},simultaneous=True)
     -s.Matrix([0,0,108*nu*sigma*w+6*sigma_dot]))
time = s.symbols('s', real=True)
rho = (1-s.exp(-8*time))/8
rate = s.exp(-8*time)
zero('retained_time_derivative',s.diff(rho,time)-rate)
zero('retained_time_inverse_identity',1-8*rho-s.exp(-8*time))
trajectory = s.Matrix([s.exp(4*time),-3*s.exp(-4*time)/2,13*s.exp(-8*time)/2])
actual_velocity = U.subs(dict(zip(coords,trajectory)),simultaneous=True)
zero('full_reparameterized_original_trajectory',trajectory.diff(time)-rate*actual_velocity)
zero('rescaled_force_curl_final_coefficients',
     (108*nu*sigma*w+6*sigma_dot).subs(
         {sigma:rate,sigma_dot:-8*rate},simultaneous=True)
     -(108*nu*s.exp(-8*time)*w-48*s.exp(-8*time)))

receipt = {
    'schema_version':1,'status':'pass','all_passed':all(checks.values()),
    'number_of_checks':len(checks),'checks':checks,'sympy_version':s.__version__,
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'scope':'Full generic-test-function initial scalar/vector generator derivatives, vorticity identity, and exact retained-time force and trajectory. Finite-time operator maps and function-space proofs are in the manuscript.',
    'lean_used':False,'navier_stokes_disproof_established':False,
}
(ROOT/'checks/material_generator_checks.json').write_text(
    json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(f"All {len(checks)} material-generator exact checks pass.")
