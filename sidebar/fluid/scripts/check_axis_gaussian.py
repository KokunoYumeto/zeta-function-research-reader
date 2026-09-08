"""Exact full-expression replay for the specified axisymmetric Gaussian family."""
from pathlib import Path
import hashlib
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
s, z, x1, x2, beta = sp.symbols('s z x1 x2 beta', real=True)
A, B = sp.symbols('A B', real=True)
k, tau, nu = sp.symbols('k tau nu', positive=True)
v = sp.symbols('v', real=True)
rho = s+z*z
G = sp.exp(-k*rho)
q, h = A*G, B*G
checks = {}


def zero(name, expr, cart=False):
    expr = sp.expand(expr.doit())
    if cart:
        expr = sp.rem(expr, x2*x2+x1*x1-s, x2)
    answer = sp.simplify(expr)
    checks[name] = {'passed': answer == 0, 'residual': str(answer)}
    if answer != 0:
        raise AssertionError((name, answer))


def dt(w):
    return ((1-beta)*A*sp.diff(w, A)/tau+B*sp.diff(w, B)/tau
            +2*beta*k*sp.diff(w, k)/tau-sp.diff(w, tau))


def M(w):
    return 4*s*sp.diff(w, s, 2)+8*sp.diff(w, s)+sp.diff(w, z, 2)


def L(w):
    return 4*s*sp.diff(w, s, 2)+4*sp.diff(w, s)+sp.diff(w, z, 2)


a, c = 2*k*z*q, 2*q*(1-k*s)
u = sp.Matrix([x1*a-x2*h, x2*a+x1*h, c])
adv = lambda w: 2*s*a*sp.diff(w, s)+c*sp.diff(w, z)
xi = A*k*G*(10-4*k*rho)
P = 10*(1+beta)-(4+32*beta)*v+8*beta*v*v
Q = 140-112*v+16*v*v
R = 6*(1-beta)-(4+16*beta)*v+8*beta*v*v
S = 60-80*v+16*v*v
CR = (1-2*beta*v)/tau+nu*k*(10-4*v)
CE = P/tau+nu*k*Q
CF = R/tau+nu*k*S
CN = 4*A*A*k*(v-3)+B*B
DN = A*A*k*k*(16*v-56)+4*k*B*B
Rh = B*G*CR.subs(v, k*rho)
Exi = A*k*G*CE.subs(v, k*rho)+z*G**2*DN.subs(v, k*rho)
F = A*G*CF.subs(v, k*rho)/2+z*G**2*CN.subs(v, k*rho)
p = (z*q*((1-beta-2*beta*k*rho)/tau+nu*k*(10-4*k*rho))
     +q*q*(1-2*k*rho)/2-h*h/(4*k))
f = sp.Matrix([-x2*Rh, x1*Rh, F])

zero('velocity_divergence', 2*a+2*s*sp.diff(a, s)+sp.diff(c, z))
zero('poloidal_radial_dictionary', a+sp.diff(q, z))
zero('poloidal_axial_dictionary', c-2*q-2*s*sp.diff(q, s))
zero('five_dimensional_vorticity', xi+M(q))
zero('q_time_derivative', dt(q)-q*(1-beta-2*beta*k*rho)/tau)
zero('h_time_derivative', dt(h)-h*(1-2*beta*k*rho)/tau)
zero('material_radius', adv(rho)-4*z*q)
zero('complete_swirl_advection_stretching_cancellation', adv(h)+2*a*h)
zero('full_swirl_residual', dt(h)+adv(h)-nu*M(h)+2*a*h-Rh)
zero('full_vorticity_residual', dt(xi)+adv(xi)-nu*M(xi)-sp.diff(h*h, z)-Exi)
zero('vorticity_diffusion', M(xi)+A*k*k*G*Q.subs(v, k*rho))
zero('vorticity_time_derivative', dt(xi)-A*k*G*P.subs(v, k*rho)/tau)
zero('force_tail_antiderivative', -2*sp.diff(F, s)-Exi)
zero('linear_force_polynomial_antiderivative', R-sp.diff(R, v)-P)
zero('viscous_force_polynomial_antiderivative', S-sp.diff(S, v)-Q)

Ap = nu*M(a)-dt(a)-a*a-adv(a)+h*h
Bp = F+nu*L(c)-dt(c)-adv(c)
zero('radial_pressure_gradient', 2*sp.diff(p, s)-Ap)
zero('axial_pressure_gradient', sp.diff(p, z)-Bp)
zero('full_pressure_closure', sp.diff(Ap, z)-2*sp.diff(Bp, s))
zero('pressure_origin_gauge', p.subs({s: 0, z: 0})-A*A/2+B*B/(4*k))


def cd(w, i):
    if i == 0:
        return sp.diff(w, x1)+2*x1*sp.diff(w, s)
    if i == 1:
        return sp.diff(w, x2)+2*x2*sp.diff(w, s)
    return sp.diff(w, z)


def curl(w):
    return sp.Matrix([cd(w[2], 1)-cd(w[1], 2),
                      cd(w[0], 2)-cd(w[2], 0),
                      cd(w[1], 0)-cd(w[0], 1)])


om = sp.Matrix([2*k*z*h*x1-x2*xi, 2*k*z*h*x2+x1*xi, 2*h*(1-k*s)])
cf = sp.Matrix([-x1*sp.diff(Rh, z)-x2*Exi,
                -x2*sp.diff(Rh, z)+x1*Exi, 2*Rh+2*s*sp.diff(Rh, s)])
for i in range(3):
    zero(f'cartesian_vorticity_{i+1}', curl(u)[i]-om[i], True)
    zero(f'cartesian_force_curl_{i+1}', curl(f)[i]-cf[i], True)
    residual = (dt(u[i])+sum(u[j]*cd(u[i], j) for j in range(3))
                +cd(p, i)-nu*sum(cd(cd(u[i], j), j) for j in range(3))-f[i])
    zero(f'complete_cartesian_momentum_{i+1}', residual, True)
zero('origin_force', F.subs({s: 0, z: 0})-A*(3*(1-beta)/tau+30*nu*k))
zero('origin_swirl_force_curl', cf[2].subs({s: 0, z: 0})-2*B*(1/tau+10*nu*k))
zero('origin_poloidal_curl_derivative', Exi.subs({s: 0, z: 0})
     -10*(1+beta)*A*k/tau-140*nu*A*k*k)
zero('origin_swirl_vorticity', om[2].subs({s: 0,z: 0})-2*B)
zero('physical_poloidal_vorticity_test',
     om[1].subs({s: 1/k,z: 0,x1: 1/sp.sqrt(k),x2: 0})-6*A*sp.sqrt(k)/sp.E)
zero('origin_poloidal_velocity', c.subs({s: 0,z: 0})-2*A)
cstar = (7-sp.sqrt(14))/2
zero('viscous_test_radius_root', Q.subs(v, cstar))
zero('test_radius_time_polynomial', P.subs(v, cstar)-(1-6*beta)*(10-4*cstar))
zero('exceptional_beta_polynomials', P.subs(beta, sp.Rational(1, 6))-Q/12)
zero('exceptional_beta_test_radius', P.subs({beta: sp.Rational(1, 6), v: 1})-sp.Rational(11, 3))
zero('exceptional_viscous_test_value', Q.subs(v, 1)-44)

# Dimension-specific Gaussian moments.  The common integral I_m is retained.
def mom(poly, m, dim=3):
    return sp.expand(sum(co*sp.rf(sp.Rational(dim, 2), powers[0])/sp.Integer(m)**powers[0]
                         for powers, co in sp.Poly(sp.expand(poly), v).terms()))

zero('five_dimensional_energy_moment', mom(4*k*A*A*v+B*B, 2, 5)-5*k*A*A-B*B)
zero('five_dimensional_dissipation_moment',
     mom(A*A*k*k*(10-4*v)**2+4*k*B*B*v, 2, 5)-35*A*A*k*k-5*k*B*B)
d, delta = sp.symbols('d delta', real=True)
subcoeff = {tau: 1/d, nu: delta/k}
force_swirl = B*B/(8*k)*(35*d*d*beta*beta-20*d*d*beta+4*d*d
                         -60*d*beta*delta+40*d*delta+140*delta*delta)
force_even = 15*A*A/16*(39*d*d*beta*beta-20*d*d*beta+4*d*d
                       -84*d*beta*delta+56*d*delta+252*delta*delta)
force_odd = (371*A**4*k*k-76*A*A*B*B*k+4*B**4)/(32*k)
curl_swirl = 5*B*B/8*(23*d*d*beta*beta-12*d*d*beta+4*d*d
                      -28*d*beta*delta+56*d*delta+252*delta*delta)
curl_even = 35*A*A*k/8*(27*d*d*beta*beta-12*d*d*beta+4*d*d
                        -36*d*beta*delta+72*d*delta+396*delta*delta)
curl_odd = (455*A**4*k*k-84*A*A*B*B*k+4*B**4)/8
zero('exact_L2_force_swirl', (2*B*B/(3*k)*mom(v*CR*CR, 2)).subs(subcoeff)-force_swirl)
zero('exact_L2_force_even', (A*A/4*mom(CF*CF, 2)).subs(subcoeff)-force_even)
zero('exact_L2_force_odd', mom(v*CN*CN, 4)/(3*k)-force_odd)
zero('exact_L2_curl_swirl', (sp.Rational(8,3)*B*B*mom(v*v*(sp.diff(CR,v)-CR)**2,2)).subs(subcoeff)-curl_swirl)
zero('exact_L2_curl_even', (sp.Rational(2,3)*A*A*k*mom(v*CE*CE,2)).subs(subcoeff)-curl_even)
zero('exact_L2_curl_odd', sp.Rational(2,15)*mom(v*v*DN*DN,4)/(k*k)-curl_odd)

mu = sp.symbols('mu', real=True)
delta_CR = sp.diff(CR, v)-CR
angular_swirl_curl = sp.integrate(
    4*v*v*(1-mu*mu)*mu*mu*delta_CR**2
    +4*(CR+v*(1-mu*mu)*delta_CR)**2, (mu,-1,1))/2
zero('independent_cartesian_angular_swirl_curl_norm',
     (B*B*mom(angular_swirl_curl,2)).subs(subcoeff)-curl_swirl)
zero('independent_angular_radial_factor', sp.integrate(1-mu*mu,(mu,-1,1))/2-sp.Rational(2,3))
zero('independent_angular_mixed_factor', sp.integrate((1-mu*mu)*mu*mu,(mu,-1,1))/2-sp.Rational(2,15))

# Exact energy work through the five-dimensional measure (no numerical quadrature).
work_moment = mom(A*A*k*CE+B*B*CR, 2, 5)
zero('complete_force_work', work_moment
     -((1-sp.Rational(5,2)*beta)*(5*A*A*k+B*B)/tau
        +nu*(35*A*A*k*k+5*B*B*k)))

sigma, Lstar, taustar = sp.symbols('sigma Lstar taustar', positive=True)
Ustar, Hstar = sp.symbols('Ustar Hstar', real=True)
zero('width_power_time_derivative', -sp.diff(Lstar*sigma**beta,sigma)/taustar
     +beta*Lstar*sigma**beta/(taustar*sigma))
zero('polynomial_amplitude_gradient_scale',
     Ustar*sigma**(beta-1)/(Lstar*sigma**beta)-Ustar/Lstar/sigma)
zero('energy_time_exponent', 2*(beta-1)+3*beta-(5*beta-2))
zero('swirl_energy_time_exponent', -2+5*beta-(5*beta-2))
zero('dissipation_time_exponent', 2*(beta-1)+beta-(3*beta-2))
zero('time_force_scaling_exponent', beta-1-1-(beta-2))
zero('viscous_force_scaling_exponent', beta-1-2*beta-(-beta-1))

# A packet is exactly c*sigma^power*x^gamma*exp(-m|x|²/(Lstar² sigma^(2 beta))).
# These recurrences supply every mixed derivative, and the proof supplies its
# explicit Gamma-function Lp bound.  No original amplitude or length is set to one.
def packet_space(packet, axis):
    co, power, gamma, m = packet
    output = []
    if gamma[axis]:
        reduced = list(gamma); reduced[axis] -= 1
        output.append((co*gamma[axis], power, tuple(reduced), m))
    raised = list(gamma); raised[axis] += 1
    output.append((-2*m*co/Lstar**2, power-2*beta, tuple(raised), m))
    return output


def packet_time(packet):
    co, power, gamma, m = packet
    output = [(-power*co/taustar, power-1, gamma, m)]
    for axis in range(3):
        raised = list(gamma); raised[axis] += 2
        output.append((-2*beta*m*co/(taustar*Lstar**2),
                       power-2*beta-1, tuple(raised), m))
    return output


xyz = sp.symbols('xx yy zz', real=True)
power, coeff = sp.symbols('power coeff', real=True)
def packet_expression(packet):
    co, exponent, gamma, m = packet
    return (co*sigma**exponent*sp.prod(xx**gg for xx,gg in zip(xyz,gamma))
            *sp.exp(-m*sum(xx*xx for xx in xyz)/(Lstar**2*sigma**(2*beta))))

test_packet = (coeff, power, (2,1,3), 2)
for axis in range(3):
    zero(f'full_spatial_packet_recurrence_{axis+1}',
         sp.diff(packet_expression(test_packet),xyz[axis])
         -sum(packet_expression(pac) for pac in packet_space(test_packet,axis)))
zero('full_temporal_packet_recurrence',
     -sp.diff(packet_expression(test_packet),sigma)/taustar
     -sum(packet_expression(pac) for pac in packet_time(test_packet)))

files = ['tex/axis_gaussian_concentration.tex', 'scripts/check_axis_gaussian.py',
         'research/axis_gaussian_concentration.md']
result = {
    'schema_version': 1,
    'status': 'exact_specified_gaussian_family_calculation',
    'retained_parameters': ['nu>0','T>0','tau_star>0','L_star>0',
                             'U_star real','H_star real','beta real',
                             'tau=T-t','sigma=tau/tau_star','centre z=0'],
    'domain': 'original R^3, 0<=t<T; actual smooth extension through s=0',
    'checks': checks,
    'exact_check_count': len(checks),
    'all_passed': all(row['passed'] for row in checks.values()),
    'sympy_version': sp.__version__,
    'artifacts': [{'path': name, 'sha256': hashlib.sha256((ROOT/name).read_bytes()).hexdigest()}
                  for name in files if (ROOT/name).exists()],
    'endpoint_findings': {
        'both_amplitudes_zero': 'identically zero solution and force, all beta',
        'H_star_nonzero': 'fixed-origin force curl diverges for every beta',
        'U_star_nonzero': 'canonical axial force at origin diverges for every beta',
        'all_nonzero_amplitude_pairs': 'uniform force curl diverges for every beta, independently of pressure',
        'expanding_width_caveat': 'for beta<0, poloidal circular test points escape to spatial infinity; uniform-bound exclusion is not asserted to be a local fixed-point exclusion',
        'energy': 'positive constant sigma^(5 beta-2); bounded iff beta>=2/5 for nonzero amplitudes',
        'other_pressure_or_force': 'no smooth-through-T Schwartz forcing can realize this same nonzero family',
    },
    'classical_navier_stokes_counterexample_established': False,
    'lean_runs': 0,
}
(ROOT/'research/axis_gaussian_concentration.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'{len(checks)} exact Gaussian-family checks passed.')
