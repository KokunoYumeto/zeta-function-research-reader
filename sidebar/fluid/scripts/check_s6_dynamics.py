"""Exact scalar-sector and positive-viscosity periodic NS checks.

Default replay is standalone with frozen source hashes. Optional --source-root
rereads the audited relative files. No network, numerical sampling, or Lean.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--source-root', type=Path)
args = parser.parse_args()
provenance = json.loads((ROOT/'sources'/'s6_dynamics_source_hashes.json').read_text(encoding='utf-8'))
checks = {}


def zero(name, expression):
    vals = list(expression) if isinstance(expression, s.MatrixBase) else [expression]
    reduced = [s.trigsimp(s.simplify(v)) for v in vals]
    checks[name] = all(v == 0 for v in reduced)
    if not checks[name]:
        raise AssertionError((name, reduced))


h,k0,beta0 = s.symbols('h k beta',real=True)
m2,Gamma,kappa = s.symbols('m2 Gamma kappa',positive=True)
Phi = s.diag(h+k0,h-k0,-2*h)
triplet = s.Matrix([0,0,beta0])
source_s = s.trace(Phi**2)+2*triplet.dot(triplet)
source_a = m2+Gamma*source_s
cubic = s.det(Phi)-(triplet.T*Phi*triplet)[0]
zero('source_trace_metric',source_s-(6*h*h+2*k0*k0+2*beta0*beta0))
zero('source_cubic',cubic-2*h*(k0*k0+beta0*beta0-h*h))
adj_difference = Phi.adjugate()-triplet*triplet.T
tf = adj_difference-s.trace(adj_difference)*s.eye(3)/3
matrix_force = -source_a*Phi+kappa*tf
hforce = -source_a*h-kappa*h*h+kappa*(k0*k0+beta0*beta0)/3
kforce = -(source_a-2*kappa*h)*k0
bforce = -(source_a-2*kappa*h)*beta0
zero('full_tracefree_matrix_sector',matrix_force-s.diag(hforce+kforce,hforce-kforce,-2*hforce))
zero('full_triplet_sector',-(source_a*s.eye(3)+kappa*Phi)*triplet-s.Matrix([0,0,bforce]))
potential = m2*source_s/2+Gamma*source_s**2/4-kappa*cubic
zero('retained_kinetic_weights',s.Matrix([
    -s.diff(potential,h)/6-hforce,
    -s.diff(potential,k0)/2-kforce,
    -s.diff(potential,beta0)/2-bforce,
]))
hdot,kdot,bdot = s.symbols('h_dot k_dot beta_dot',real=True)
Phi_dot = s.diag(hdot+kdot,hdot-kdot,-2*hdot)
b_dot = s.Matrix([0,0,bdot])
zero('full_gauge_current',Phi*Phi_dot-Phi_dot*Phi+triplet*b_dot.T-b_dot*triplet.T)
den = 1-6*Gamma*h/kappa
a = (m2+12*Gamma*h**2)/den
R2 = 3*a*h/kappa+3*h**2
omega2 = (m2-2*kappa*h+24*Gamma*h**2)/den
zero('retained_a_equation',a-(m2+Gamma*(6*h*h+2*R2)))
zero('retained_h_equation',-a*h-kappa*h*h+kappa*R2/3)
zero('retained_frequency_equation',omega2-(a-2*kappa*h))
d0 = s.sqrt(kappa*kappa-24*Gamma*m2)
h0 = (kappa+d0)/(24*Gamma)
zero('frequency_numerator_factorization',m2-2*kappa*h+24*Gamma*h*h-24*Gamma*(h-(kappa-d0)/(24*Gamma))*(h-h0))

x1,x2,x3,t = s.symbols('x1 x2 x3 t',real=True)
lam,nu,eta,sigma,R,omega = s.symbols('lambda nu eta sigma R omega',positive=True)
coords=(x1,x2,x3)
B1=s.Matrix([s.sin(lam*x3),s.cos(lam*x3),0])
B2=s.Matrix([0,s.sin(lam*x1),s.cos(lam*x1)])


def div(v):
    return sum(s.diff(v[i],coords[i]) for i in range(3))


def curl(v):
    return s.Matrix([s.diff(v[2],x2)-s.diff(v[1],x3),
                     s.diff(v[0],x3)-s.diff(v[2],x1),
                     s.diff(v[1],x1)-s.diff(v[0],x2)])


def lap(v):
    return v.applyfunc(lambda z: sum(s.diff(z,x,2) for x in coords))


def grad(z):
    return s.Matrix([s.diff(z,x) for x in coords])


for i,mode in enumerate((B1,B2),1):
    zero(f'B{i}_divergence',div(mode))
    zero(f'B{i}_oriented_curl',curl(mode)-lam*mode)
    zero(f'B{i}_laplace',lap(mode)+lam**2*mode)
    zero(f'B{i}_pointwise_norm',mode.dot(mode)-1)
c=s.cos(lam*x3)*s.sin(lam*x1)
zero('cross_inner_product',B1.dot(B2)-c)
K=R*s.cos(omega*sigma*t)
B=R*s.sin(omega*sigma*t)
d=s.exp(-nu*lam**2*t)
velocity=eta*d*(K*B1+B*B2)
pressure=-eta**2*d**2*K*B*c
force=eta*sigma*omega*d*(-B*B1+K*B2)
convection=velocity.jacobian(coords)*velocity
zero('full_velocity_divergence',div(velocity))
zero('full_NS_residual',s.diff(velocity,t)+convection-nu*lap(velocity)+grad(pressure)-force)
zero('nonlinear_pressure_cancellation',convection+grad(pressure))
zero('initial_velocity',velocity.subs(t,0)-eta*R*B1)
zero('coefficient_integrated_work',K*(-sigma*omega*B)+B*(sigma*omega*K))
zero('pointwise_work_retained',velocity.dot(force)-eta**2*d**2*sigma*omega*(K*K-B*B)*c)
energy=eta**2*R**2*d**2/2
zero('exact_energy_identity',s.diff(energy,t)+nu*lam**2*eta**2*R**2*d**2)

# lambda=2*pi*n gives period 1/n. The one-mode-period integral proves
# the zero cross-average on the unit cube for every positive integer n.
period=2*s.pi/lam
zero('cross_mode_zero_average',s.integrate(s.integrate(c,(x1,0,period)),(x3,0,period)))
zero('translation_x3_flips_only_B1',B1.subs(x3,x3+s.pi/lam)+B1)
zero('translation_x3_preserves_B2',B2.subs(x3,x3+s.pi/lam)-B2)
zero('translation_x1_flips_only_B2',B2.subs(x1,x1+s.pi/lam)+B2)
zero('translation_x1_preserves_B1',B1.subs(x1,x1+s.pi/lam)-B1)
gb=s.diag(-1,1,-1)
gs=s.Matrix([[0,1,0],[1,0,0],[0,0,-1]])
for name,g in [('beta',gb),('both',gs)]:
    zero(f'gauge_{name}_unitary',g*g.T-s.eye(3))
    zero(f'gauge_{name}_det_one',g.det()-1)
zero('gauge_beta_phi',gb*Phi*gb.T-Phi)
zero('gauge_beta_triplet',gb*triplet+triplet)
zero('gauge_both_phi',gs*Phi*gs.T-Phi.subs(k0,-k0))
zero('gauge_both_triplet',gs*triplet+triplet)
spacing,gym=s.symbols('a g_YM',positive=True)
zero('wilson_force_coefficient',2*(2*gym**2/spacing)*(1/(2*gym**2*spacing))-2/spacing**2)

source_validation={'mode':'frozen_provenance','original_sources_reread':False}
if args.source_root is not None:
    for relative,expected in provenance['source_sha256'].items():
        actual=hashlib.sha256((args.source_root/relative).read_bytes()).hexdigest()
        if actual != expected:
            raise AssertionError('Source changed: '+relative)
    source_validation={'mode':'explicit_source_revalidation','original_sources_reread':True,'all_hashes_match':True}

result={
    'schema_version':1,
    'scope':'Exact retained scalar sector and positive-viscosity periodic NS map; analytical proofs in tex/s6_dynamics_bridge.tex.',
    'source_sha256':provenance['source_sha256'],
    'source_revalidation':source_validation,
    'checks':checks,
    'all_exact_checks_passed':all(checks.values()),
    'target_domain':'R^3/Z^3, standard flat metric and orientation, lambda=2*pi*n, positive integer n',
    'retained_target_parameters':['nu>0','eta>0','sigma>0','tau=sigma*t'],
    'target_force':'eta*sigma*omega*exp(-nu*lambda^2*t)*(-beta(sigma*t)*B1+k(sigma*t)*B2)',
    'target_pressure':'-eta^2*exp(-2*nu*lambda^2*t)*k(sigma*t)*beta(sigma*t)*cos(lambda*x3)*sin(lambda*x1)',
    'gauge_scope':'Marked fixed-h circle; gauge sign orbits correspond to effective half-period translation orbits. General source state space is not identified with the image.',
    'global_smooth_target_solution':True,
    'navier_stokes_disproof_established':False,
    'lean_used':False,
}
out=ROOT/'checks'/'s6_dynamics_checks.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'checks':len(checks),'all_passed':all(checks.values()),'output':out.relative_to(ROOT).as_posix()},indent=2))
