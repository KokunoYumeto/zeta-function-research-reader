"""Exact Cartesian replay for arbitrary translations of the original Gaussian.

All original scales and both amplitudes are retained.  Symbolic reduction of
an equality does not replace or rescale the fields being compared.  This is
an identity replay; the endpoint and integrability proofs are in the review.
"""
from pathlib import Path
import hashlib
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
checks = {}


def smooth_jet_notation(expression):
    """Identify dummy-bound partial derivatives by their original argument slot.

    SymPy can display the same mixed partial with different bound dummy names.
    For the stipulated smooth fields, commuting these partials is exact.  This
    replacement retains the function, every evaluation argument, and all four
    derivative orders, and leaves centre derivatives untouched.
    """
    names = {'u1', 'u2', 'u3', 'f1', 'f2', 'f3', 'p'}

    def jet(derivative, substitutions=None):
        function = derivative.expr
        if str(function.func) not in names:
            return None
        arguments = function.args
        orders = [0]*len(arguments)
        for variable, count in derivative.variable_count:
            slots = [j for j, argument in enumerate(arguments) if argument == variable]
            if len(slots) != 1:
                raise AssertionError(('Non-partial derivative in a smooth jet', derivative))
            orders[slots[0]] += count
        if substitutions:
            arguments = tuple(argument.subs(substitutions, simultaneous=True)
                              for argument in arguments)
        label = str(function.func)+'_jet_'+'_'.join(map(str, orders))
        return sp.Function(label)(*arguments)

    replacements = {}
    for atom in expression.atoms(sp.Subs):
        if isinstance(atom.expr, sp.Derivative):
            value = jet(atom.expr, dict(zip(atom.variables, atom.point)))
            if value is not None:
                replacements[atom] = value
    expression = expression.xreplace(replacements)
    replacements = {}
    for atom in expression.atoms(sp.Derivative):
        value = jet(atom)
        if value is not None:
            replacements[atom] = value
    return expression.xreplace(replacements)


def zero(name, expression):
    answer = sp.simplify(sp.expand(smooth_jet_notation(sp.sympify(expression).doit())))
    checks[name] = {"passed": answer == 0, "residual": str(answer)}
    if answer != 0:
        raise AssertionError((name, answer))


def curl(field, coordinates):
    return sp.Matrix([
        sp.diff(field[2], coordinates[1])-sp.diff(field[1], coordinates[2]),
        sp.diff(field[0], coordinates[2])-sp.diff(field[2], coordinates[0]),
        sp.diff(field[1], coordinates[0])-sp.diff(field[0], coordinates[1])])


def lap(expression, coordinates):
    return sum(sp.diff(expression, coordinate, 2) for coordinate in coordinates)


# Generic smooth fields verify the morphism on residuals, not just on solutions.
t = sp.symbols('t', real=True)
source_time = sp.symbols('source_time', real=True)
xyz = sp.symbols('x1 x2 z', real=True)
yy = sp.symbols('y1 y2 y3', real=True)
nu = sp.symbols('nu', positive=True)
centre = sp.Matrix([sp.Function(f'd{j}')(t) for j in range(1, 4)])
speed = centre.diff(t)
arguments = (*yy, source_time)
base_u = sp.Matrix([sp.Function(f'u{j}')(*arguments) for j in range(1, 4)])
base_p = sp.Function('p')(*arguments)
base_f = sp.Matrix([sp.Function(f'f{j}')(*arguments) for j in range(1, 4)])
sub = {yy[j]: xyz[j]-centre[j] for j in range(3)}
sub[source_time] = t


def translate(expression):
    return expression.subs(sub, simultaneous=True)


translated_u = base_u.applyfunc(translate)
translated_p = translate(base_p)
translated_f = sp.Matrix([
    translate(base_f[i]-sum(speed[j]*sp.diff(base_u[i], yy[j])
                            for j in range(3))) for i in range(3)])
for i in range(3):
    original = (sp.diff(base_u[i], source_time)
                +sum(base_u[j]*sp.diff(base_u[i], yy[j]) for j in range(3))
                +sp.diff(base_p, yy[i])-nu*lap(base_u[i], yy)-base_f[i])
    translated = (sp.diff(translated_u[i], t)
                  +sum(translated_u[j]*sp.diff(translated_u[i], xyz[j])
                       for j in range(3))
                  +sp.diff(translated_p, xyz[i])
                  -nu*lap(translated_u[i], xyz)-translated_f[i])
    zero(f'generic_full_momentum_translation_{i+1}', translated-translate(original))
zero('generic_divergence_translation',
     sum(sp.diff(translated_u[i], xyz[i]) for i in range(3))
     -translate(sum(sp.diff(base_u[i], yy[i]) for i in range(3))))
generic_curl_u = curl(base_u, yy)
generic_curl_f = curl(base_f, yy)
for i in range(3):
    zero(f'generic_vorticity_translation_{i+1}',
         curl(translated_u, xyz)[i]-translate(generic_curl_u[i]))
    zero(f'generic_force_curl_translation_{i+1}',
         curl(translated_f, xyz)[i]
         -translate(generic_curl_f[i]-sum(
             speed[j]*sp.diff(generic_curl_u[i], yy[j]) for j in range(3))))
inverse_sub = {xyz[j]: yy[j]+centre[j] for j in range(3)}
for i in range(3):
    zero(f'generic_inverse_velocity_{i+1}',
         translated_u[i].subs(inverse_sub, simultaneous=True)-base_u[i].subs(source_time, t))
    recovered_force = translated_f[i]+sum(
        speed[j]*sp.diff(translated_u[i], xyz[j]) for j in range(3))
    zero(f'generic_inverse_force_{i+1}',
         recovered_force.subs(inverse_sub, simultaneous=True)-base_f[i].subs(source_time, t))
zero('generic_inverse_pressure',
     translated_p.subs(inverse_sub, simultaneous=True)-base_p.subs(source_time, t))

# Full Gaussian in the original three Cartesian coordinates.
x1, x2, z = xyz
A, B, beta = sp.symbols('A B beta', real=True)
k, tau = sp.symbols('k tau', positive=True)
b = sp.Matrix(sp.symbols('dprime1 dprime2 dprime3', real=True))
s = x1*x1+x2*x2
rho = s+z*z
v = k*rho
G = sp.exp(-k*rho)
q, h = A*G, B*G
u = sp.Matrix([2*k*z*q*x1-h*x2, 2*k*z*q*x2+h*x1, 2*q*(1-k*s)])
xi = A*k*G*(10-4*v)
omega = sp.Matrix([2*k*z*h*x1-x2*xi, 2*k*z*h*x2+x1*xi, 2*h*(1-k*s)])
P = lambda w: 10*(1+beta)-(4+32*beta)*w+8*beta*w*w
Q = lambda w: 140-112*w+16*w*w
R = lambda w: 6*(1-beta)-(4+16*beta)*w+8*beta*w*w
S = lambda w: 60-80*w+16*w*w
Rh = B*G*((1-2*beta*v)/tau+nu*k*(10-4*v))
Elinear = A*k*G*(P(v)/tau+nu*k*Q(v))
Enonlinear = z*G*G*(A*A*k*k*(16*v-56)+4*k*B*B)
Exi = Elinear+Enonlinear
Flinear = A*G*(R(v)/tau+nu*k*S(v))/2
Fnonlinear = z*G*G*(4*A*A*k*(v-3)+B*B)
f = sp.Matrix([-x2*Rh, x1*Rh, Flinear+Fnonlinear])
p = (z*q*((1-beta-2*beta*v)/tau+nu*k*(10-4*v))
     +q*q*(1-2*v)/2-h*h/(4*k))


def physical_time_derivative(expression):
    return ((1-beta)*A*sp.diff(expression, A)/tau
            +B*sp.diff(expression, B)/tau
            +2*beta*k*sp.diff(expression, k)/tau-sp.diff(expression, tau))


drift_u = sp.Matrix([sum(b[j]*sp.diff(u[i], xyz[j]) for j in range(3))
                     for i in range(3)])
fd = f-drift_u
drift_omega = sp.Matrix([sum(b[j]*sp.diff(omega[i], xyz[j]) for j in range(3))
                         for i in range(3)])
cf = curl(f, xyz)
cfd = curl(fd, xyz)
for i in range(3):
    zero(f'original_cartesian_vorticity_{i+1}', curl(u, xyz)[i]-omega[i])
    zero(f'full_original_cartesian_momentum_{i+1}',
         physical_time_derivative(u[i])
         +sum(u[j]*sp.diff(u[i], xyz[j]) for j in range(3))
         +sp.diff(p, xyz[i])-nu*lap(u[i], xyz)-f[i])
    zero(f'full_translated_cartesian_momentum_{i+1}',
         physical_time_derivative(u[i])-drift_u[i]
         +sum(u[j]*sp.diff(u[i], xyz[j]) for j in range(3))
         +sp.diff(p, xyz[i])-nu*lap(u[i], xyz)-fd[i])
    zero(f'full_cartesian_translation_curl_{i+1}', cfd[i]-cf[i]+drift_omega[i])
zero('full_gaussian_divergence', sum(sp.diff(u[j], xyz[j]) for j in range(3)))

# Arbitrary amplitudes in the swirl-origin test, including mixed poloidal/swirl.
origin = dict.fromkeys(xyz, 0)
for j in range(3):
    zero(f'swirl_vorticity_origin_gradient_{j+1}', sp.diff(omega[2], xyz[j]).subs(origin))
zero('translated_swirl_origin_curl', cfd[2].subs(origin)-2*B*(1/tau+10*nu*k))

# All parity statements use full Cartesian inversion and retain every term.
inversion = {coordinate: -coordinate for coordinate in xyz}


def invert(expression):
    return expression.subs(inversion, simultaneous=True)


omega_p = omega.subs(B, 0)
u_p = u.subs(B, 0)
curl_linear_p = curl(sp.Matrix([0, 0, Flinear]), xyz)
curl_nonlinear_p = curl(sp.Matrix([0, 0, Fnonlinear.subs(B, 0)]), xyz)
for i in range(3):
    zero(f'poloidal_velocity_even_{i+1}', invert(u_p[i])-u_p[i])
    zero(f'poloidal_vorticity_odd_{i+1}', invert(omega_p[i])+omega_p[i])
    zero(f'poloidal_force_curl_linear_odd_{i+1}', invert(curl_linear_p[i])+curl_linear_p[i])
    zero(f'poloidal_force_curl_nonlinear_even_{i+1}',
         invert(curl_nonlinear_p[i])-curl_nonlinear_p[i])
    for j in range(3):
        derivative = sp.diff(omega_p[i], xyz[j])
        zero(f'poloidal_vorticity_derivative_even_{i+1}_{j+1}', invert(derivative)-derivative)

c = sp.symbols('c', positive=True)
test_radius = sp.sqrt(c)/sp.sqrt(k)
odd_value = test_radius*A*k*sp.exp(-c)*(P(c)/tau+nu*k*Q(c))
even_drift = b[0]*A*k*sp.exp(-c)*(10-32*c+8*c*c)
point_values = {}
for sign in (1, -1):
    point = {x1: sign*test_radius, x2: 0, z: 0, B: 0}
    value = cfd[1].subs(point)
    point_values[sign] = value
    zero(f'exact_paired_point_value_{sign}', value-sign*odd_value+even_drift)
    zero(f'nonlinear_curl_at_test_point_{sign}', curl_nonlinear_p[1].subs(point))
zero('full_paired_point_drift_cancellation',
     (point_values[1]-point_values[-1])/2-odd_value)

# Return to the actual positive time and length scales, without setting any to 1.
sigma, Lstar, taustar = sp.symbols('sigma L_star tau_star', positive=True)
Ustar, Hstar = sp.symbols('U_star H_star', real=True)
scales = {A: Ustar*sigma**(beta-1), B: Hstar/sigma,
          k: 1/(Lstar**2*sigma**(2*beta)), tau: taustar*sigma}
dimensional_odd = (Ustar/(Lstar*taustar)*sigma**(-2)*sp.sqrt(c)*sp.exp(-c)
                   *(P(c)+nu*taustar/Lstar**2*sigma**(1-2*beta)*Q(c)))
dimensional_drift = (b[0]*Ustar/Lstar**2*sigma**(-beta-1)*sp.exp(-c)
                    *(10-32*c+8*c*c))
zero('paired_point_dimensional_time_scale', odd_value.subs(scales)-dimensional_odd)
zero('paired_point_dimensional_drift_scale', even_drift.subs(scales)-dimensional_drift)
zero('origin_swirl_dimensional_time_scale',
     (2*B*(1/tau+10*nu*k)).subs(scales)
     -2*Hstar/taustar*sigma**(-2)-20*nu*Hstar/Lstar**2*sigma**(-1-2*beta))
cstar = (7-sp.sqrt(14))/2
zero('selected_radius_viscous_polynomial', Q(cstar))
zero('selected_radius_time_polynomial', P(cstar)-(1-6*beta)*(10-4*cstar))
zero('selected_radius_time_coefficient', 10-4*cstar-(-4+2*sp.sqrt(14)))
zero('all_nonexceptional_exponents_exact_pair',
     dimensional_odd.subs(c, cstar)
     -Ustar/(Lstar*taustar)*sigma**(-2)*sp.sqrt(cstar)*sp.exp(-cstar)
     *(1-6*beta)*(10-4*cstar))
zero('exceptional_polynomial_identity', P(c).subs(beta, sp.Rational(1, 6))-Q(c)/12)
zero('exceptional_time_test_value', P(1).subs(beta, sp.Rational(1, 6))-sp.Rational(11, 3))
zero('exceptional_viscous_test_value', Q(1)-44)
zero('exceptional_dimensional_exact_pair',
     dimensional_odd.subs({c: 1, beta: sp.Rational(1, 6)})
     -Ustar/(sp.E*Lstar*taustar)*sigma**(-2)
     *(sp.Rational(11, 3)+44*nu*taustar/Lstar**2*sigma**sp.Rational(2, 3)))
for i in range(3):
    zero(f'zero_amplitude_velocity_{i+1}', u[i].subs({A: 0, B: 0}))
    zero(f'zero_amplitude_force_{i+1}', fd[i].subs({A: 0, B: 0}))
    zero(f'pressure_adjustment_curl_{i+1}',
         curl(sp.Matrix([sp.diff(base_p, coordinate) for coordinate in yy]), yy)[i])
zero('zero_amplitude_pressure', p.subs({A: 0, B: 0}))

# The frame-velocity variant retains acceleration; no constant is L2 on R3.
boosted_u = translated_u+speed
boosted_f = base_f.applyfunc(translate)+speed.diff(t)
for i in range(3):
    boosted_residual = (sp.diff(boosted_u[i], t)
                        +sum(boosted_u[j]*sp.diff(boosted_u[i], xyz[j]) for j in range(3))
                        +sp.diff(translated_p, xyz[i])
                        -nu*lap(boosted_u[i], xyz)-boosted_f[i])
    original = (sp.diff(base_u[i], source_time)
                +sum(base_u[j]*sp.diff(base_u[i], yy[j]) for j in range(3))
                +sp.diff(base_p, yy[i])-nu*lap(base_u[i], yy)-base_f[i])
    zero(f'full_accelerated_frame_residual_{i+1}', boosted_residual-translate(original))
    affine_pressure = translated_p-sum(speed.diff(t)[j]*xyz[j] for j in range(3))
    affine_residual = (sp.diff(boosted_u[i], t)
                       +sum(boosted_u[j]*sp.diff(boosted_u[i], xyz[j]) for j in range(3))
                       +sp.diff(affine_pressure, xyz[i])
                       -nu*lap(boosted_u[i], xyz)-translate(base_f[i]))
    zero(f'accelerated_frame_affine_pressure_residual_{i+1}',
         affine_residual-translate(original))
zero('translation_drift_energy_density_is_divergence',
     sum(u[i]*drift_u[i] for i in range(3))
     -sum(b[j]*sp.diff(sum(component*component for component in u), xyz[j])/2
          for j in range(3)))

files = ['tex/axis_gaussian_concentration.tex', 'tex/gaussian_translation.tex',
         'scripts/check_gaussian_translation.py', 'research/gaussian_translation_review.md']
result = {
    'schema': 'gaussian-translation-exact-checks/v1',
    'all_passed': all(row['passed'] for row in checks.values()),
    'exact_check_count': len(checks),
    'checks': checks,
    'sympy_version': sp.__version__,
    'retained_parameters': ['nu>0', 'T>0', 'tau_star>0', 'L_star>0',
                            'U_star real', 'H_star real', 'beta real',
                            'tau=T-t', 'sigma=tau/tau_star',
                            'arbitrary smooth d:[0,T)->R3'],
    'artifacts': [{'path': name, 'sha256': hashlib.sha256((ROOT/name).read_bytes()).hexdigest()}
                  for name in files if (ROOT/name).exists()],
    'scope': 'Exact residual, curl, parity and coefficient replay; full analytical proof in the review.',
    'endpoint_conclusion': 'Every nonzero amplitude pair and every real beta, for every smooth center, violates a globally uniform bound on first spatial derivatives of the force, independently of pressure.',
    'classical_navier_stokes_counterexample_established': False,
    'lean_runs': 0,
}
(ROOT/'checks/gaussian_translation_checks.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(f'{len(checks)} exact Gaussian translation checks passed.')
