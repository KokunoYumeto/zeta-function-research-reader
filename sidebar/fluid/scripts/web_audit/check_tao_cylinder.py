# Portable adaptation of tao2024/replay.py
# Only import/output/inventory handling changed; the delimited mathematics is a raw source byte slice.
from __future__ import annotations
from fractions import Fraction
from itertools import combinations
import sympy as s
import sympy as sp
import sympy as S
from portable_common import begin, finish
begin('tao_cylinder')
# BEGIN UNCHANGED MATHEMATICAL BODY
x = s.symbols('x', real=True)
phi, v, w, vv, vw, wv, ww, dv, dw, vphi, wphi = s.symbols(
    'phi v w nabla_v_v nabla_v_w nabla_w_v nabla_w_w div_v div_w v_phi w_phi')
D = 1+x*x
a = phi/D
U = (v+x*w)/D**2
checks = []

def check(name, actual, expected):
    residual = s.cancel(s.expand(actual-expected))
    ok = residual == 0
    checks.append({'name': name, 'passed': ok,
                   'actual': str(actual), 'expected': str(expected),
                   'residual': str(residual)})
    if not ok:
        raise AssertionError((name, residual))

check('rational axial derivative', s.diff(a,x), -2*x*phi/D**2)
check('rational transverse derivative', s.diff(U,x), (w-4*x*v-3*x*x*w)/D**3)
connection = (vv+x*(vw+wv)+x*x*ww)/D**4
R = a*s.diff(U,x)+connection
coeffs = (vv+phi*w, vw+wv-4*phi*v, ww-3*phi*w)
check('full transverse residual numerator', R, sum(coeffs[k]*x**k for k in range(3))/D**4)
div = s.diff(a,x)+(dv+x*dw)/D**2
check('full divergence numerator', div, (dv+x*(dw-2*phi))/D**2)
old_relations = {vv: -phi*w, vw: 2*phi*v-wv, ww: 3*phi*w}
check('printed -2 coefficient exact residual', R.subs(old_relations), -2*x*phi*v/D**4)
new_relations = {vv: -phi*w, vw: 4*phi*v-wv, ww: 3*phi*w}
check('corrected -4 coefficient exact residual', R.subs(new_relations), 0)
axial_acceleration = a*s.diff(a,x)+(vphi+x*wphi)/D**3
J = x/(4*D**2)+3*x/(8*D)+s.Rational(3,8)*s.atan(x)
p = -(2*phi**2-wphi)/(4*D**2)-vphi*J
check('pressure primitive J', s.diff(J,x), 1/D**3)
check('exact reconstructed axial momentum', axial_acceleration+s.diff(p,x), 0)
for name, integrand, result in [
    ('axial energy integral', D**-2, s.pi/2),
    ('v transverse energy integral', D**-4, 5*s.pi/16),
    ('mixed transverse energy integral', x*D**-4, 0),
    ('w transverse energy integral', x*x*D**-4, s.pi/16),
]:
    check(name, s.integrate(integrand,(x,-s.oo,s.oo)), result)

# Time-dependent modulation is recomputed with full chain rule, not by
# substituting the claimed residual into the ansatz.
t,z=s.symbols('t z', real=True)
L=s.Function('L')(t)
M=s.Function('M')(t)
F=s.Function('F')
G=s.Function('G')
modU=F(x/L)/M
moda=L*G(x/L)/M
expected_mod=-s.diff(M,t)/M**2*F(x/L)-s.diff(L,t)*x/(M*L**2)*s.diff(F(z),z).subs(z,x/L)
check('time modulation transverse chain rule', s.diff(modU,t), expected_mod)
expected_ax=(s.diff(L,t)/M-L*s.diff(M,t)/M**2)*G(x/L)-s.diff(L,t)*x/(M*L)*s.diff(G(z),z).subs(z,x/L)
check('time modulation axial chain rule', s.diff(moda,t), expected_ax)
check('time modulation stationary transport factor', moda*s.diff(modU,x), G(x/L)*s.diff(F(z),z).subs(z,x/L)/M**2)

# Algebraic Levi-Civita identity in arbitrary symmetric connection jets
# and arbitrary metric first jets satisfying metric compatibility.
n=3
V=s.symbols('V0:3')
H=s.Matrix(n,n,lambda i,j:s.Symbol('h'+str(min(i,j))+str(max(i,j))))
dV=s.Matrix(n,n,lambda i,j:s.Symbol(f'd{i}V{j}'))
Gamma=lambda k,i,j:s.Symbol('G'+str(k)+str(min(i,j))+str(max(i,j)))
dh=lambda k,i,j:sum(Gamma(r,k,i)*H[r,j]+Gamma(r,k,j)*H[i,r] for r in range(n))
theta=[sum(H[i,j]*V[j] for j in range(n)) for i in range(n)]
dtheta=lambda k,i:sum(dh(k,i,j)*V[j]+H[i,j]*dV[k,j] for j in range(n))
accel=[sum(V[k]*dV[k,j] for k in range(n))+sum(Gamma(j,k,l)*V[k]*V[l] for k in range(n) for l in range(n)) for j in range(n)]
for i in range(n):
    contraction=sum(V[k]*(dtheta(k,i)-dtheta(i,k)) for k in range(n))
    d_energy=sum(dh(i,k,l)*V[k]*V[l]+H[k,l]*(dV[i,k]*V[l]+V[k]*dV[i,l]) for k in range(n) for l in range(n))
    check(f'Levi-Civita one-form identity component {i}', contraction+d_energy/2, sum(H[i,j]*accel[j] for j in range(n)))

# END UNCHANGED MATHEMATICAL BODY
finish('tao_cylinder', checks)
