"""Exact replay of the original-coordinate axis/five-dimensional transfer.

The TeX proves smoothness, support, the force integral, pressure existence,
Newton inversion and integral identities. This script checks independent
pointwise Cartesian/coordinate identities with arbitrary smooth coefficients;
it does not assert an infinite construction or a Navier--Stokes singularity.
"""
from pathlib import Path
import hashlib
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
s, z, t, x1, x2 = sp.symbols('s z t x1 x2', real=True)
nu = sp.symbols('nu', positive=True)
q = sp.Function('q')(s, z, t)
h = sp.Function('h')(s, z, t)
g = sp.Function('g')(s, z, t)
F = sp.Function('F')(s, z, t)
eta = sp.Function('eta')(t)
checks = {}


def zero(name, expression, cartesian=False):
    expanded = sp.expand(expression.doit())
    if cartesian:
        # Exact polynomial division by the defining relation s=x1²+x2².
        # No parameter, derivative, sign, or nonzero factor is discarded.
        expanded = sp.rem(expanded, x2**2+x1**2-s, x2)
    residual = sp.expand(expanded)
    if residual != 0:
        residual = sp.simplify(residual)
    checks[name] = {'passed': residual == 0, 'residual': str(residual)}
    if residual != 0:
        raise AssertionError((name, residual))


def L(w):
    return 4*s*sp.diff(w, s, 2)+4*sp.diff(w, s)+sp.diff(w, z, 2)


def M(w):
    return 4*s*sp.diff(w, s, 2)+8*sp.diff(w, s)+sp.diff(w, z, 2)


def cartdiff(w, i):
    if i == 0:
        return sp.diff(w, x1)+2*x1*sp.diff(w, s)
    if i == 1:
        return sp.diff(w, x2)+2*x2*sp.diff(w, s)
    return sp.diff(w, z)


def lap(w):
    return sum(cartdiff(cartdiff(w, i), i) for i in range(3))


def curl(w):
    return sp.Matrix([cartdiff(w[2], 1)-cartdiff(w[1], 2),
                      cartdiff(w[0], 2)-cartdiff(w[2], 0),
                      cartdiff(w[1], 0)-cartdiff(w[0], 1)])


a = -sp.diff(q, z)
c = 2*q+2*s*sp.diff(q, s)
xi = -M(q)
u = sp.Matrix([x1*a-x2*h, x2*a+x1*h, c])
adv = lambda w: 2*s*a*sp.diff(w, s)+c*sp.diff(w, z)
D = lambda w: sp.diff(w, t)+adv(w)
Rh = D(h)-nu*M(h)+2*a*h
Exi = D(xi)-nu*M(xi)-sp.diff(h*h, z)

zero('meridional_divergence_coefficients', 2*a+2*s*sp.diff(a, s)+sp.diff(c, z))
zero('cartesian_velocity_divergence', sum(cartdiff(u[i], i) for i in range(3)), True)
zero('azimuthal_vorticity_coefficient', sp.diff(a, z)-2*sp.diff(c, s)-xi)
omega = sp.Matrix([-x1*sp.diff(h, z)-x2*xi,
                   -x2*sp.diff(h, z)+x1*xi,
                   2*h+2*s*sp.diff(h, s)])
for i in range(3):
    zero(f'cartesian_vorticity_component_{i+1}', curl(u)[i]-omega[i], True)
zero('scalar_three_dimensional_laplacian', lap(g)-L(g), True)
zero('first_coordinate_laplacian', lap(x1*g)-x1*M(g), True)
zero('second_coordinate_laplacian', lap(x2*g)-x2*M(g), True)
zero('scalar_material_operator', sum(u[i]*cartdiff(g, i) for i in range(3))-adv(g), True)

radial_advection = a*a-h*h+adv(a)
swirl_advection = 2*a*h+adv(h)
advection = sp.Matrix([x1*radial_advection-x2*swirl_advection,
                       x2*radial_advection+x1*swirl_advection, adv(c)])
for i in range(3):
    zero(f'full_cartesian_advection_{i+1}',
         sum(u[j]*cartdiff(u[i], j) for j in range(3))-advection[i], True)

f = sp.Matrix([-x2*Rh, x1*Rh, F])
A = nu*M(a)-sp.diff(a, t)-a*a-adv(a)+h*h
B = F+nu*L(c)-sp.diff(c, t)-adv(c)
pressure_gradient = sp.Matrix([x1*A, x2*A, B])
for i in range(3):
    zero(f'complete_momentum_residual_{i+1}',
         f[i]+nu*lap(u[i])-sp.diff(u[i], t)-advection[i]-pressure_gradient[i], True)
zero('azimuthal_momentum_residual', Rh+nu*M(h)-sp.diff(h, t)-adv(h)-2*a*h)
zero('meridional_pressure_closure', sp.diff(A, z)-2*sp.diff(B, s)+2*sp.diff(F, s)+Exi)
zero('diffusion_commutator', sp.diff(L(g), s)-M(sp.diff(g, s)))

expected_force_curl = sp.Matrix([-x1*sp.diff(Rh, z)+2*x2*sp.diff(F, s),
                                 -x2*sp.diff(Rh, z)-2*x1*sp.diff(F, s),
                                 2*Rh+2*s*sp.diff(Rh, s)])
for i in range(3):
    zero(f'cartesian_force_curl_{i+1}', curl(f)[i]-expected_force_curl[i], True)

# A separate dimension count retains four transverse coordinates for R5.
X = sp.symbols('X1:5', real=True)
rho = sum(v*v for v in X)
G5 = sp.Function('G')(rho, z, t)
lap5 = sum(sp.diff(G5, v, 2) for v in X)+sp.diff(G5, z, 2)
abstract_G = sp.Function('G')(s, z, t)
zero('five_dimensional_laplacian_intertwining', lap5-M(abstract_G).subs(s, rho))
div5 = 4*a+2*s*sp.diff(a, s)+sp.diff(c, z)
zero('five_dimensional_divergence', div5+2*sp.diff(q, z))
zero('weighted_five_dimensional_flux', adv(q)+q*div5)
zero('five_dimensional_scalar_advection',
     -2*s*sp.diff(q, z)*sp.diff(g, s)+(2*q+2*s*sp.diff(q, s))*sp.diff(g, z)-adv(g))

zero('cartesian_velocity_energy_density', u.dot(u)-s*(sp.diff(q, z)**2+h*h)-c*c, True)
zero('meridional_energy_boundary_difference',
     4*(q+s*sp.diff(q, s))**2-4*s*s*sp.diff(q, s)**2-4*sp.diff(s*q*q, s))
zero('cartesian_enstrophy_density',
     omega.dot(omega)-s*(sp.diff(h, z)**2+xi*xi)-(2*h+2*s*sp.diff(h, s))**2, True)
zero('swirl_enstrophy_boundary_difference',
     4*(h+s*sp.diff(h, s))**2-4*s*s*sp.diff(h, s)**2-4*sp.diff(s*h*h, s))
zero('force_work_density', u.dot(f)-s*h*Rh-c*F, True)
zero('force_work_integration_by_parts', c*F-sp.diff(2*s*q*F, s)+2*s*q*sp.diff(F, s))
zero('five_dimensional_energy_coupling_cancellation',
     -sp.diff(q, z)*h*h+div5*h*h/2+2*sp.diff(q, z)*h*h)

flux_radial = (2*q*sp.diff(q, s, t)-q*xi*a
               +2*nu*(q*sp.diff(xi, s)-xi*sp.diff(q, s))
               -h*h*a/2+2*nu*h*sp.diff(h, s))
flux_axial = (q*sp.diff(q, z, t)-q*xi*c
              +nu*(q*sp.diff(xi, z)-xi*sp.diff(q, z))
              +q*h*h-h*h*c/2+nu*h*sp.diff(h, z))
flux_div = 4*flux_radial+2*s*sp.diff(flux_radial, s)+sp.diff(flux_axial, z)
energy_density_dt = (4*s*sp.diff(q, s)*sp.diff(q, s, t)
                     +sp.diff(q, z)*sp.diff(q, z, t)+h*sp.diff(h, t))
zero('complete_local_five_dimensional_energy_flux',
     energy_density_dt+nu*(xi*xi+4*s*sp.diff(h, s)**2+sp.diff(h, z)**2)
     -q*Exi-h*Rh-flux_div)

qt, ht = eta*q, eta*h
at, ct = -sp.diff(qt, z), 2*qt+2*s*sp.diff(qt, s)
xit = -M(qt)
Dt = lambda w: sp.diff(w, t)+2*s*at*sp.diff(w, s)+ct*sp.diff(w, z)
zero('full_time_cutoff_swirl_residual',
     Dt(ht)-nu*M(ht)+2*at*ht
     -eta*Rh-sp.diff(eta, t)*h-eta*(eta-1)*(adv(h)+2*a*h))
zero('full_time_cutoff_vorticity_residual',
     Dt(xit)-nu*M(xit)-sp.diff(ht*ht, z)
     -eta*Exi-sp.diff(eta, t)*xi-eta*(eta-1)*(adv(xi)-sp.diff(h*h, z)))

rad = sp.symbols('rad', positive=True)
sphere4 = 2*sp.pi**sp.Rational(5, 2)/sp.gamma(sp.Rational(5, 2))
sphere3 = 2*sp.pi**2/sp.gamma(2)
phi = rad**(-3)/(8*sp.pi**2)
zero('newton_kernel_radial_harmonicity', sp.diff(phi, rad, 2)+4*sp.diff(phi, rad)/rad)
zero('newton_kernel_flux_constant', -sp.diff(phi, rad)*rad**4*sphere4-1)
zero('three_dimensional_radial_measure', 2*sp.pi*rad/(2*rad)-sp.pi)
zero('five_dimensional_radial_measure', sphere3*rad**3/(2*rad)-sp.pi**2*rad**2)
zero('energy_measure_coefficient', sp.pi**2/sp.pi-sp.pi)

proof_path = ROOT/'tex/axis_five_dimensional_transfer.tex'
result = {
    'schema_version': 1,
    'scope': ('Original-coordinate, arbitrary-function Cartesian, material, diffusion, '
              'curl, full momentum residual, measure, energy boundary, force-work, '
              'time-cutoff and five-dimensional Newton coefficient identities. '
              'Analytic domain/support/pressure and integral arguments are in the proof.'),
    'original_coordinates': ['x1', 'x2', 'z', 's=x1^2+x2^2>=0', 'physical time t'],
    'five_dimensional_coordinates': ['X in R^4', 'z in R', 's=|X|^2'],
    'retained_hypotheses': ['nu>0', 'smooth on an actual open neighborhood of s>=0',
                            'fixed compact coefficient support 0<=s<=S, |z|<=Z',
                            '0<T0<T1 for the global time-cutoff construction'],
    'proof_sha256': hashlib.sha256(proof_path.read_bytes()).hexdigest(),
    'sympy_version': sp.__version__,
    'checks': checks,
    'all_passed': all(check['passed'] for check in checks.values()),
    'classical_navier_stokes_counterexample_established': False,
}
out = ROOT/'checks/axis_transfer_checks.json'
out.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(f'{len(checks)} exact axis-transfer checks passed.')
