"""Exact original-coordinate checks for tex/viscous_strain_layer.tex.

Analytic cutoff smoothness and all-time energy are proved in the TeX.
This replay checks the full vector equation and every localization term.
"""
from pathlib import Path
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
x1, x2, x3, t = s.symbols('x1 x2 x3 t', real=True)
sigma, nu = s.symbols('sigma nu', positive=True)
K1, K3, a0 = s.symbols('K1 K3 a0', real=True)
x = (x1, x2, x3)
checks = {}

def clean(z):
    return s.factor(s.trigsimp(s.simplify(z)))

def zero(name, z):
    values = list(z) if isinstance(z, s.MatrixBase) else [z]
    residues = [clean(v) for v in values]
    checks[name] = {'passed': all(v == 0 for v in residues),
                    'residuals': [str(v) for v in residues]}
    if not checks[name]['passed']:
        raise AssertionError((name, residues))

def grad(z): return s.Matrix([s.diff(z, v) for v in x])
def div(v): return sum(s.diff(v[i], x[i]) for i in range(3))
def curl(v): return s.Matrix([s.diff(v[2], x2)-s.diff(v[1], x3),
                             s.diff(v[0], x3)-s.diff(v[2], x1),
                             s.diff(v[1], x1)-s.diff(v[0], x2)])
def lap(v): return v.applyfunc(lambda z: sum(s.diff(z, y, 2) for y in x))

k1 = K1*s.exp(-sigma*t)
k = s.Matrix([k1, 0, K3])
q = k.dot(k)
phi = k1*x1+K3*x3
a = a0*s.exp(sigma*t-nu*(K1**2*(1-s.exp(-2*sigma*t))/(2*sigma)+K3**2*t))
D = s.diag(sigma, -sigma, 0)
X = s.Matrix(x)
e2 = s.Matrix([0, 1, 0])
u = D*X+a*s.cos(phi)*e2
p = -sigma**2*(x1**2+x2**2)/2
potential = -X.cross(D*X)/3+a/q*e2.cross(k)*s.sin(phi)
zero('phase_transport', s.diff(phi,t)+(D*X).dot(grad(phi)))
zero('amplitude_evolution', s.diff(a,t)-(sigma-nu*q)*a)
zero('full_divergence', div(u))
zero('full_NS_momentum', s.diff(u,t)+u.jacobian(x)*u+grad(p)-nu*lap(u))
omega = a*s.sin(phi)*s.Matrix([K3,0,-k1])
zero('full_vorticity', curl(u)-omega)
zero('vector_potential', curl(potential)-u)
zero('vorticity_log_rate', sigma-nu*q+s.diff(q,t)/(2*q)-(sigma*K3**2/q-nu*q))
zero('neutral_wavevector_subfamily', a.subs(K1,0)-a0*s.exp((sigma-nu*K3**2)*t))
zero('expanding_wavevector_component_cancellation',
     (a*k1).subs(K3,0)-a0*K1*s.exp(-nu*K1**2*(1-s.exp(-2*sigma*t))/(2*sigma)))

# Check the entire localization product rule with arbitrary fields, without
# tying the audit to a chosen numerical cutoff or phase. The uncut residual
# is retained explicitly and only then set to zero in the proved application.
chi = s.Function('chi')(*x)
eta = s.Function('eta')(t)
uu = s.Matrix([s.Function('u'+str(i))(*x,t) for i in range(3)])
ww = s.Matrix([s.Function('w'+str(i))(*x,t) for i in range(3)])
pp = s.Function('p')(*x,t)
V = chi*uu+ww
U = eta*V
P = eta**2*chi*pp
cut_grad_u = uu.jacobian(x)*grad(chi)
lap_chi = sum(s.diff(chi,y,2) for y in x)
force = (
    s.diff(eta,t)*V+eta*s.diff(ww,t)
    -nu*eta*(2*cut_grad_u+lap_chi*uu+lap(ww))
    +eta*chi*(eta*chi-1)*uu.jacobian(x)*uu
    +eta*chi*(eta-1)*grad(pp)
    +eta**2*(chi*uu.dot(grad(chi))*uu+chi*ww.jacobian(x)*uu
              +chi*uu.jacobian(x)*ww+ww.dot(grad(chi))*uu
              +ww.jacobian(x)*ww+pp*grad(chi))
)
uncut_residual=s.diff(uu,t)+uu.jacobian(x)*uu+grad(pp)-nu*lap(uu)
zero('all_localization_terms',
     s.diff(U,t)+U.jacobian(x)*U+grad(P)-nu*lap(U)-force-eta*chi*uncut_residual)
AA = s.Matrix([s.Function('A'+str(i))(*x,t) for i in range(3)])
zero('curl_cutoff_product', curl(chi*AA)-chi*curl(AA)-grad(chi).cross(AA))
zero('localized_divergence', div(eta*curl(chi*AA)))

result = {'schema_version': 1, 'scope': 'Exact viscous strain wave and compact localization identities; no singularity claim.',
          'checks': checks, 'passed': all(c['passed'] for c in checks.values()),
          'original_parameters': ['sigma>0','nu>0','a0 real','(K1,K3) nonzero',
                                  '0<R0<R1','0<T0<T1'],
          'navier_stokes_disproof_established': False}
out = ROOT/'checks'/'viscous_strain_checks.json'
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':result['passed'],'checks':len(checks),'output':str(out)}))
