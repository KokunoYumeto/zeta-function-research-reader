"""Standalone exact replay for the original inverse-fibre coefficient heat flow.

Original coordinates/constants/signs remain in the recorded expressions.
Algebraic reductions below certify displayed identities; no numerical inference,
Lean process, external source edit, or network request is used.
"""
from pathlib import Path
import hashlib
import json
import sys
from resource_ceiling import install_memory_ceiling
RESOURCE = install_memory_ceiling()
import sympy as S

ROOT = Path(__file__).resolve().parents[2]
checks = {}
def zero(name, expression):
    values = list(expression) if isinstance(expression, S.MatrixBase) else [expression]
    residuals = [S.cancel(S.together(v)) for v in values]
    passed = all(v == 0 for v in residuals)
    checks[name] = passed
    if not passed:
        raise AssertionError((name, residuals))

x,y,w,a,b,c,r,alpha,tau = S.symbols('x y w a b c r alpha tau')
coords = (x,y,w)
F = S.Matrix([
 (1+x*y)**3*w+y**2*(1+x*y)*(4+3*x*y),
 y+3*x*(1+x*y)**2*w+3*x*y**2*(4+3*x*y),
 2*x-3*x**2*y-x**3*w,
])
DF = F.jacobian(coords)
zero('original_determinant_minus_two',S.expand(DF.det())+2)
P = c*r**3-2*r**2+b*r-2*a
H = S.Matrix([1/alpha,r-alpha,5*alpha**2-3*r*alpha-c*alpha**3])
F_H = F.subs(dict(zip(coords,H)),simultaneous=True).applyfunc(S.cancel)
zero('full_inverse_chart_before_target_constraint',
     F_H-S.Matrix([r**2+r*alpha-c*r**3,4*r+2*alpha-3*c*r**2,c]))
ar = S.diff(P,r)/2
zero('inverse_second_target_equation',(F_H[1]-b).subs(alpha,ar))
zero('inverse_first_target_equation',2*(F_H[0].subs(alpha,ar)-a)-P)
zero('inverse_recovers_root_coordinate',(H[1]+1/H[0])-r)
zero('inverse_recovers_alpha',1/H[0]-alpha)
zero('inverse_coordinate_volume',H.jacobian((r,alpha,c)).det()+alpha)
zero('inverse_chart_to_target_volume',F_H.jacobian((r,alpha,c)).det()-2*alpha)
zero('entire_xzero_boundary',F.subs(x,0)-S.Matrix([w+4*y**2,y,0]))

disc = 4*(b*b-c*b**3+18*a*b*c-16*a-27*a*a*c*c)
zero('full_cubic_discriminant',S.discriminant(P,r)-disc)
zero('c_zero_quadratic_discriminant',S.discriminant(P.subs(c,0),r)-(b*b-16*a))
triple_a = S.Rational(4,27)/c**2
triple_b = S.Rational(4,3)/c
triple_r = S.Rational(2,3)/c
zero('unique_c_nonzero_triple_root_parameters',
     P.subs({a:triple_a,b:triple_b},simultaneous=True)-c*(r-triple_r)**3)
special_boundary = S.Matrix([0,b,a-4*b*b])
zero('c_zero_additional_finite_point',
     F.subs(dict(zip(coords,special_boundary)),simultaneous=True)-S.Matrix([a,b,0]))

grads = [S.Matrix([S.diff(F[i],z) for z in coords]) for i in range(3)]
W = [(-grads[(i+1)%3].cross(grads[(i+2)%3])/2).applyfunc(S.expand) for i in range(3)]
for i in range(3):
    zero('inverse_jacobian_column_'+str(i+1),DF*W[i]-S.eye(3)[:,i])
    zero('piola_divergence_'+str(i+1),sum(S.diff(W[i][j],coords[j]) for j in range(3)))
U = (2*W[0]+6*F[2]*W[1]).applyfunc(S.expand)
h_original=2-3*x*y-x*x*w
q_original=3*h_original*(1+x*y)-2
U_factored=S.Matrix([
 x**3*(q_original**2-3*h_original),
 x*(q_original**2-q_original-3*h_original),
 3*q_original+(3*h_original+3*x*y-7)*q_original**2+(21-9*x*y)*h_original-9*h_original**2,
])
zero('full_polynomial_lift_component_formula',U-U_factored)
zero('lifted_heat_pushforward',DF*U-S.Matrix([2,6*F[2],0]))
zero('lifted_heat_divergence',sum(S.diff(U[j],coords[j]) for j in range(3)))
zero('lift_preserves_target_c',grads[2].dot(U))
zero('lift_preserves_heat_invariant',(grads[1]-3*F[0]*grads[2]-3*F[2]*grads[0]).dot(U))
Pi=F[2]*r**3-2*r**2+F[1]*r-2*F[0]
zero('global_heat_transport_operator',sum(S.diff(Pi,coords[i])*U[i] for i in range(3))-S.diff(Pi,r,2))

P_tau = P.subs({a:a+2*tau,b:b+6*c*tau},simultaneous=True)
zero('original_coefficient_forward_heat',S.diff(P_tau,tau)-S.diff(P_tau,r,2))
disc_derivative = 2*S.diff(disc,a)+6*c*S.diff(disc,b)
zero('discriminant_heat_derivative',disc_derivative+8*(3*b*c-4)**2)
disc_flow = disc.subs({a:a+2*tau,b:b+6*c*tau},simultaneous=True)
A = 3*b*c-4
zero('full_discriminant_heat_evolution',
     disc_flow-(disc-8*A*A*tau-144*A*c*c*tau*tau-864*c**4*tau**3))
z = S.symbols('z')
K = 2*b/(3*c)-S.Rational(16,27)/c**2-2*a
ell = b-S.Rational(4,3)/c
zero('retained_depressed_coordinate_identity',P.subs(r,z+S.Rational(2,3)/c)-(c*z**3+ell*z+K))
zero('depressed_constant_heat_invariant',2*S.diff(K,a)+6*c*S.diff(K,b))

q = 3*c*r-2
rdot = -q/alpha
alphadot = 3*c-q*q/alpha
Hdot = H.diff(r)*rdot+H.diff(alpha)*alphadot
U_H = U.subs(dict(zip(coords,H)),simultaneous=True)
zero('complete_explicit_inverse_chart_dynamic_lift',Hdot-U_H)
zero('root_heat_velocity',rdot+S.diff(P,r,2)/(2*alpha))
zero('alpha_heat_velocity',alphadot-(3*c+(3*c*r-2)*rdot))
invariant = 4*r+2*alpha-6*c*r*r-3*c*r*alpha+3*c*c*r**3
zero('heat_invariant_original_chart',invariant-(F_H[1]-3*c*F_H[0]))
zero('inverse_chart_hamiltonian_r',alpha*rdot-S.diff(invariant,alpha))
zero('inverse_chart_hamiltonian_alpha',alpha*alphadot+S.diff(invariant,r))
zero('inverse_chart_weighted_volume',S.diff(alpha*rdot,r)+S.diff(alpha*alphadot,alpha))
zero('boundary_heat_velocity',U.subs(x,0)-S.Matrix([0,0,2]))
delta=S.symbols('delta')
triple_flow=P.subs({a:triple_a+2*delta,b:triple_b+6*c*delta,r:z+triple_r},simultaneous=True)
zero('triple_heat_orbit_exact_roots',triple_flow-c*z*(z*z+6*delta))
zero('triple_central_inverse_denominator',S.diff(triple_flow,z).subs(z,0)/2-3*c*delta)
zero('triple_outer_inverse_denominator',S.rem(S.diff(triple_flow,z)/2+6*c*delta,z*z+6*delta,z))

# The actual target flow v=(2,6c,0), on Euclidean (a,b,c), has
# identically zero convective acceleration and component Laplacian.
target_coords = (a,b,c)
v = S.Matrix([2,6*c,0])
zero('target_shear_divergence',sum(S.diff(v[i],target_coords[i]) for i in range(3)))
zero('target_shear_acceleration',v.jacobian(target_coords)*v)
zero('target_shear_laplacian',v.applyfunc(lambda f:sum(S.diff(f,z,2) for z in target_coords)))

def curl(V):
    return S.Matrix([S.diff(V[2],y)-S.diff(V[1],w),
                     S.diff(V[0],w)-S.diff(V[2],x),
                     S.diff(V[1],x)-S.diff(V[0],y)])
potential = -F[1]*grads[2]-S.Rational(3,2)*F[2]**2*grads[0]
zero('global_polynomial_vector_potential',curl(potential)-U)
lap_U = U.applyfunc(lambda f:sum(S.diff(f,z,2) for z in coords))
accel_U = U.jacobian(coords)*U
nu = S.symbols('nu',positive=True)
force = accel_U-nu*lap_U
curl_force_axis = curl(force).subs({x:0,y:0},simultaneous=True).applyfunc(S.expand)
zero('exact_Euclidean_force_curl_axis',curl_force_axis-S.Matrix([0,0,108*nu*w]))
U_axis = U.subs({x:0,y:0},simultaneous=True)
jets=S.Matrix([10*x**3,6*x-12*x*x*y-18*w*x**3,2-54*x*y-18*w*x*x])
for i,lower_degree in enumerate((5,5,4)):
    remainder=S.Poly(S.expand(U[i]-jets[i]),x,y)
    checks['exact_transverse_remainder_ideal_'+str(i+1)]=all(sum(monomial)>=lower_degree for monomial,coefficient in remainder.terms() if coefficient!=0)
    if not checks['exact_transverse_remainder_ideal_'+str(i+1)]:
        raise AssertionError('Transverse jet remainder mismatch')
checks['euclidean_same_velocity_force_has_nonzero_curl'] = any(z != 0 for z in curl_force_axis)
if not checks['euclidean_same_velocity_force_has_nonzero_curl']:
    raise AssertionError('Need a different Euclidean curl certificate')
t = S.symbols('t')
P_back = P.subs({a:a-2*t,b:b-6*c*t},simultaneous=True)
zero('Newman_time_is_negative_heat_time',S.diff(P_back,t)+S.diff(P_back,r,2))

source_frozen = Path('[local]/Documents/math/output/navier_stokes_research_2026-09-08/sources/inverse_fibre_heat_source_hashes.json')
source_provenance = json.loads(source_frozen.read_text(encoding='utf-8')) if source_frozen.exists() else {}
result = {
 'schema_version':1,
 'resource':RESOURCE,
 'status':'pass',
 'checks':checks,
 'number_of_checks':len(checks),
 'all_passed':all(checks.values()),
 'sympy_version':S.__version__,
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'source_provenance':source_provenance,
 'original_coordinate_renaming':'third original spatial t is w; evolution variable is tau',
 'original_polynomial_map':[str(f) for f in F],
 'inverse_fibre_polynomial':str(P),
 'inverse_chart':[str(h) for h in H],
 'inverse_chart_domain':'P(r)=0 and alpha=P_r(r)/2 != 0; over C, or real roots and real parameters for the real chart',
 'boundary_chart':'c=0 has exactly one x=0 point (0,b,a-4b^2)',
 'c_nonzero_triple_fibre':'a=4/(27*c^2), b=4/(3*c) gives P=c*(r-2/(3*c))^3 and empty original fibre',
 'target_heat_flow':['a+2*tau','b+6*c*tau','c'],
 'target_stationary_NS_velocity':[str(f) for f in v],
 'source_polynomial_lift':[str(f) for f in U],
 'source_axis_velocity':[str(f) for f in U_axis],
 'source_Euclidean_force_curl_at_x_y_zero':[str(f) for f in curl_force_axis],
 'retained_viscosity':'nu>0',
 'intrinsic_metric':'g=(DF)^T DF, det g=4, local orientation reversal det DF=-2',
 'source_intrinsic_oriented_curl':'curl_g U=6 W_1, for standard source orientation',
 'flow_time_sign':'forward heat tau; Newman t=-tau',
 'discriminant_heat_derivative':str(S.expand(disc_derivative)),
 'written_proofs':'tex/satellites/26_incompressible_fibre_heat.tex',
 'navier_stokes_disproof_established':False,
 'RH_counterexample_established':False,
 'lean_used':False,
}
output=Path(__file__).with_name('inverse_fibre_heat_results.json')
if "--write" in sys.argv:
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'number_of_checks':len(checks),'all_passed':all(checks.values()),
 'U_axis':[str(f) for f in U_axis],
 'curl_force_axis':[str(f) for f in curl_force_axis],
 'output':output.relative_to(ROOT).as_posix()},indent=2))
