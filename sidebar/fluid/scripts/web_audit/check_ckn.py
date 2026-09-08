# Portable adaptation of ckn/replay_exact.py
# Only import/output/inventory handling changed; the delimited mathematics is a raw source byte slice.
from __future__ import annotations
from fractions import Fraction
from itertools import combinations
import sympy as s
import sympy as sp
import sympy as S
from portable_common import begin, finish
begin('ckn')
# BEGIN UNCHANGED MATHEMATICAL BODY
x1, x2, x3, t, s, theta = sp.symbols('x1 x2 x3 t s theta', real=True)
nu = sp.symbols('nu', positive=True)
x = sp.Matrix([x1, x2, x3])
variables = list(x)
c, d = sp.symbols('cos_theta sin_theta', real=True)
R = sp.Matrix([[c, -d, 0], [d, c, 0], [0, 0, 1]])
orthogonality = sp.groebner([c*c+d*d-1], c, d, domain='EX')
u = sp.Matrix([x1**2+x2*x3+t*x2, x1*x2+x3**2+t**2,
               x2**2-x1*x3+t*x1])
p = x1*x2*x3+t*x1**2
f = sp.Matrix([x1+t*x2, x2+t*x3, x3+t*x1])
phi = x1**2+2*x2**2+3*x3**2+t*x1*x2+t**2
checks = []

def evaluate_at(obj, point):
    return obj.subs(dict(zip(variables, point)), simultaneous=True)

def lap(obj):
    if isinstance(obj, sp.MatrixBase):
        return obj.applyfunc(lap)
    return sum(sp.diff(obj, v, 2) for v in variables)

def grad(obj):
    return sp.Matrix([sp.diff(obj, v) for v in variables])

def residual(velocity, pressure, force, visc=nu, time=t):
    return velocity.diff(time)+velocity.jacobian(x)*velocity-visc*lap(velocity)+grad(pressure)-force

def lei_density(velocity, pressure, force, test, visc=nu, time=t):
    e = velocity.dot(velocity)/2
    gu = velocity.jacobian(x)
    return e*(sp.diff(test,time)+visc*lap(test))+(e+pressure)*velocity.dot(grad(test))+force.dot(velocity)*test-visc*sum(q*q for q in gu)*test

def check(name, expression):
    entries = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
    residues = []
    for q in entries:
        numerator, denominator = sp.fraction(sp.cancel(sp.expand(q)))
        # Exact polynomial certificate under cos(theta)^2+sin(theta)^2=1.
        # Original formulas and all nonzero denominators remain in the script.
        remainder = orthogonality.reduce(numerator)[1]
        residues.append(sp.cancel(remainder/denominator))
    good = all(q == 0 for q in residues)
    checks.append({'name': name, 'passed': good,
                   'component_residues': [str(q) for q in residues]})
    print(name, 'passed' if good else 'FAILED', flush=True)
    if not good:
        raise AssertionError((name, residues))

y = R.T*x
ur, pr, fr = R*evaluate_at(u,y), evaluate_at(p,y), R*evaluate_at(f,y)
check('rotation_orthogonality', R.T*R-sp.eye(3))
check('rotation_orientation', R.det()-1)
check('rotation_gradient', ur.jacobian(x)-R*evaluate_at(u.jacobian(x),y)*R.T)
check('rotation_divergence', sp.trace(ur.jacobian(x))-evaluate_at(sp.trace(u.jacobian(x)),y))
check('rotation_laplacian', lap(ur)-R*evaluate_at(lap(u),y))
check('rotation_convection', ur.jacobian(x)*ur-R*evaluate_at(u.jacobian(x)*u,y))
check('rotation_pressure_gradient', grad(pr)-R*evaluate_at(grad(p),y))
check('rotation_full_ns_residual', residual(ur,pr,fr)-R*evaluate_at(residual(u,p,f),y))
psi = evaluate_at(phi,R*x)
check('rotation_local_energy_density', lei_density(ur,pr,fr,phi)-evaluate_at(lei_density(u,p,f,psi),y))

v = u.subs(t,s/nu)/nu
pressure = p.subs(t,s/nu)/nu**2
force = f.subs(t,s/nu)/nu**2
test = phi.subs(t,s/nu)
check('viscosity_full_ns_residual', residual(v,pressure,force,1,s)-residual(u,p,f).subs(t,s/nu)/nu**2)
check('viscosity_local_energy_with_time_jacobian', nu*lei_density(v,pressure,force,test,1,s).subs(s,nu*t)-lei_density(u,p,f,phi)/nu**2)

radial_square = x.dot(x)
eta = sp.Function('eta')
W = sp.Matrix([-x2,x1,0])
V = eta(radial_square)*W
check('example_divergence', sp.trace(V.jacobian(x)))
check('example_convection', V.jacobian(x)*V+eta(radial_square)**2*sp.Matrix([x1,x2,0]))
dummy = sp.symbols('q',real=True)
eta1 = sp.diff(eta(dummy),dummy).subs(dummy,radial_square)
eta2 = sp.diff(eta(dummy),dummy,2).subs(dummy,radial_square)
check('example_laplacian', lap(V)-(4*radial_square*eta2+10*eta1)*W)
a = sp.Function('a')(t)
example_force = sp.diff(a,t)*V+a**2*V.jacobian(x)*V-nu*a*lap(V)
check('example_exact_forced_ns', residual(a*V,sp.S.Zero,example_force))
T = sp.symbols('T', positive=True)
plateau_force = (W-sp.Matrix([x1,x2,0]))/(T-t)**2
check('example_plateau_force_norm', plateau_force.dot(plateau_force)-2*(x1*x1+x2*x2)/(T-t)**4)

k = sp.Matrix(sp.symbols('k1 k2 k3',real=True))
P = sp.eye(3)-k*k.T/k.dot(k)
check('helmholtz_projection_idempotent', P*P-P)
check('helmholtz_projection_self_adjoint', P.T-P)
check('helmholtz_projection_divergence_free', k.T*P)

# END UNCHANGED MATHEMATICAL BODY
finish('ckn', checks)
