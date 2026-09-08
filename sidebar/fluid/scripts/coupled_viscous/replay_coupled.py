"""Portable replay: original mathematical computation block retained byte-for-byte.

I/O and provenance are adapted explicitly; see provenance/replay_adaptations.json.
Complete analytic proofs are in tex/coupled_viscous_control.tex.
"""
from __future__ import annotations

from pathlib import Path
import hashlib
import json
import sympy as s
import sympy as sp
from portable_support import start_replay

PORTABLE_CONTEXT, OUTPUT_DIRECTORY = start_replay(__file__)
CHECKS = []
checks = []


def zero(name, expr):
    entries = list(expr) if isinstance(expr, s.MatrixBase) else [expr]
    residues = [s.trigsimp(s.expand(v)) for v in entries]
    ok = all(v == 0 for v in residues)
    checks.append({"name": name, "passed": ok,
                   "residuals": [str(v) for v in residues]})
    if not ok:
        raise AssertionError((name, residues))

J = s.Matrix([[0,-1],[1,0]])
def vec(stem):
    return s.Matrix(s.symbols(stem + '1 ' + stem + '2'))
def outer(a,b):
    return a*b.T

# A general trace-free D and nonzero phase. Norm factors remain symbolic.
d11,d12,d21 = s.symbols('d11 d12 d21')
D = s.Matrix([[d11,d12],[d21,-d11]])
z = vec('z')
G = vec('G')
Theta,Omega,lam = s.symbols('Theta Omega lambda', nonzero=True)
r2 = (z.T*z)[0]
a = -(J*z).dot(G)/(lam*r2)
B = lam*Theta*z
S = Omega*outer(J*z,z)/r2
Bprime = lam*a*Omega*z-D.T*B
zero('one_layer_gradient_coupling', Bprime+D.T*B+S.T*G)
zero('own_shear_annihilates_temperature_gradient', S.T*B)
zero('tracefree_square', D*D+D.det()*s.eye(2))
zero('rank_one_shear_trace', s.trace(S))

# Three general layers with all cross terms and activation derivatives retained.
n = 3
Bs=[vec('B'+str(i)+'_') for i in range(n)]
zs=[vec('z'+str(i)+'_') for i in range(n)]
Os=s.symbols('Omega0:'+str(n))
ws=s.symbols('w0:'+str(n))
wds=s.symbols('wd0:'+str(n))
dths=s.symbols('dtheta0:'+str(n))
alphad=s.symbols('alphad')
D0=alphad*J
B0=vec('base_')
Ss=[Os[i]*outer(J*zs[i],zs[i])/zs[i].dot(zs[i]) for i in range(n)]
# B_i is parallel to z_i, the sole geometric relation needed in this identity.
betas=s.symbols('beta0:'+str(n))
Bs=[betas[i]*zs[i] for i in range(n)]
Gtot=B0+sum((ws[i]*Bs[i] for i in range(n)),s.zeros(2,1))
Dtot=D0+sum((ws[i]*Ss[i] for i in range(n)),s.zeros(2,2))
Gprime=-D0.T*B0
for i in range(n):
    Gold=B0+sum((ws[k]*Bs[k] for k in range(i)),s.zeros(2,1))
    Dold=D0+sum((ws[k]*Ss[k] for k in range(i)),s.zeros(2,2))
    Bdot=-Dold.T*Bs[i]-Ss[i].T*Gold-dths[i]*Bs[i]
    Gprime += wds[i]*Bs[i]+ws[i]*Bdot
rhs=sum(((wds[i]-ws[i]*dths[i])*Bs[i] for i in range(n)),s.zeros(2,1))
zero('three_layer_aggregate_damped_gradient', Gprime+Dtot.T*Gtot-rhs)

# The one-layer polar formulas, retaining the laboratory orientation e(phi).
ph,pi,ad,O,w=s.symbols('phi phi_i alpha_dot O w', real=True)
e=s.Matrix([s.sin(ph),s.cos(ph)])
ei=s.Matrix([s.sin(pi),s.cos(pi)])
Dp=ad*J+w*O*outer(J*ei,ei)
zdot=-Dp.T*e
rhodot=w*O*s.sin(ph-pi)*s.cos(ph-pi)
phdot=-ad-w*O*s.sin(ph-pi)**2
zero('polar_phase_vector', zdot-rhodot*e+phdot*J*e)
Fctl=w*O*s.sin(pi)*s.sin(ph-pi)/s.cos(ph)
zero('laboratory_phase_feedback', zdot[0]-(Fctl-ad)*s.cos(ph))
zero('factored_feedback', Fctl-(-w*O*s.sin(ph-pi)**2+rhodot*s.tan(ph)))
u,vv=vec('u'),vec('v')
det=lambda aa,bb:s.det(s.Matrix.hstack(aa,bb))
zero('adjacent_oriented_determinant_derivative', det(-D.T*u,vv)+det(u,-D.T*vv))

# Later-stage coefficient map, including all d_2 factors.
A,chi,d,Z,sigma,sin_s,cos_phi,cos_vartheta,chi1,R=s.symbols(
    'A chi d Z sigma sin_s cos_phi cos_vartheta chi1 R', nonzero=True)
c2=A/sigma**2*d/sin_s
g=1-Z/d
d2=A/(sigma**2*sin_s)*(d*(cos_phi-1)-Z*(cos_vartheta-1))/chi
zero('parent_vorticity_model_coefficient',
     A/(sigma**2*sin_s*chi)*(d*cos_phi-Z*cos_vartheta)-(c2*g/chi+d2))
aa=(A*d/chi+R)/(lam*chi)
k=A/sigma**2*d/sin_s*chi1/chi**2+chi1*R/(chi*sigma**2*sin_s)
zero('new_amplitude_quadratic_coefficient', aa*lam*chi1/(sigma**2*sin_s)-k)

# Damping in amplitude quotient and in logarithmic amplitude.
at,bt,dt,dw,c,v=s.symbols('a b dtheta domega c v')
quotient=c*((bt*Theta-dw*Omega)/Theta-Omega*(at*Omega-dt*Theta)/Theta**2)
zero('damped_quotient', quotient-(c*bt-at/c*(c*Omega/Theta)**2+(dt-dw)*c*Omega/Theta))
zero('damped_log_amplitude', (at*Omega-dt*Theta)/Theta-(at*Omega/Theta-dt))

# Coordinate homogeneity: compare the full original Laplacian to transformed one.
mu,nu,kap,visc=s.symbols('mu nu_AB kappa_th epsilon_v', positive=True)
zero('thermal_diffusion_units', kap*(nu**2/mu)*mu**2-(nu**3/mu)*(kap*mu**2/nu))
zero('momentum_diffusion_units', visc*(nu/mu)*mu**2-(nu**2/mu)*(visc*mu**2/nu))
lamhat=s.symbols('lambda_hat',positive=True)
zero('physical_gain_threshold', (nu**2/mu)*lamhat**(-s.Rational(7,8))*(mu*lamhat)/(2*sigma)
     -nu**2/(2*sigma)*lamhat**s.Rational(1,8))

PORTABLE_RECEIPT = {
    'schema': 'coupled-viscous-portable-component-v1',
    'component': 'replay_coupled.py',
    'checks': checks,
    'checks_count': len(checks),
    'all_passed': all(item['passed'] for item in checks),
    'sympy_version': sp.__version__,
    'portable_provenance': PORTABLE_CONTEXT,
    'scope': 'Original exact finite symbolic identities; analytic proofs remain in the included TeX. The historical source hash is not a fresh PDF verification.',
    'infinite_viscous_sequence_proved': False,
    'navier_stokes_disproof_established': False,
    'lean_used': False,
}
(OUTPUT_DIRECTORY / 'coupled_replay.json').write_text(
    json.dumps(PORTABLE_RECEIPT, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print(json.dumps({'all_passed': PORTABLE_RECEIPT['all_passed'],
                  'checks_count': PORTABLE_RECEIPT['checks_count']}))
