# Portable adaptation of secondary/replay_secondary.py
# Only import/output/inventory handling changed; the delimited mathematics is a raw source byte slice.
from __future__ import annotations
from fractions import Fraction
from itertools import combinations
import sympy as s
import sympy as sp
import sympy as S
from portable_common import begin, finish
begin('secondary')
# BEGIN UNCHANGED MATHEMATICAL BODY
checks = []

def verify(name, left, right):
    difference = S.cancel(S.expand(left - right))
    passed = difference == 0
    checks.append(dict(name=name, left=str(left), right=str(right),
                       difference=str(difference), passed=passed))
    if not passed:
        raise AssertionError(name + ': ' + str(difference))

y1, y2, t, N, nu = S.symbols('y1 y2 t N nu', positive=True)
coordinates = (y1, y2)
gradient = lambda f: S.Matrix([S.diff(f, y1), S.diff(f, y2)])
J = S.Matrix([[0,-1],[1,0]])
A = S.diag(1/(2*y2), 1)
C = S.diag(1,2*y2)
L = lambda f: S.diff(f,y1,2)/(2*y2)+S.diff(f,y2,2)
Q = lambda f: S.diff(f,y1,2)+2*y2*S.diff(f,y2,2)
M = lambda f: Q(f)+4*S.diff(f,y2)
Psi0 = -y2**3/3
Gamma0 = y1*y2+t*y2**2
v0 = J*gradient(Psi0)
D0 = lambda f: S.diff(f,t)+(v0.dot(gradient(f)))
phi = y1-t*y2**2
zeta = gradient(phi)
a = 1+y1*y2+t*y1
b = y1**2+y2**2+t*y2
s = N*phi
Fs, Ps = s**3, s**4/4
Fp, Fpp = 3*s**2, 6*s
gamma, psi = a*Fs, b*Ps
w, eta = J*gradient(psi), L(psi)
kappa, q = zeta.dot(A*zeta), zeta.dot(C*zeta)
h = 2*(A*gradient(b)).dot(zeta)+b*L(phi)
e = L(b)
verify('nonlinear_material_phase_transport',D0(phi),0)
verify('axisymmetric_symbol_relation',q,2*y2*kappa)
verify('exact_wave_velocity_component_1',w[0],(N*b*J*zeta*Fs+J*gradient(b)*Ps)[0])
verify('exact_wave_velocity_component_2',w[1],(N*b*J*zeta*Fs+J*gradient(b)*Ps)[1])
verify('exact_variable_coefficient_wave_vorticity',eta,N**2*kappa*b*Fp+N*h*Fs+e*Ps)
verify('exact_wave_diffusion',Q(gamma),N**2*q*a*Fpp+N*(2*(C*gradient(a)).dot(zeta)+a*Q(phi))*Fp+Q(a)*Fs)
verify('exact_material_vorticity_derivative',D0(eta),D0(N**2*kappa*b)*Fp+N*D0(h)*Fs+D0(e)*Ps)
self_advection = N*b*(J*zeta).dot(gradient(a))*Fs**2+a*N*(J*gradient(b)).dot(zeta)*Ps*Fp+(J*gradient(b)).dot(gradient(a))*Ps*Fs
verify('localized_wave_self_advection',w.dot(gradient(gamma)),self_advection)
xi0 = L(Psi0)
EG = lambda G,P: S.diff(G,t)+(J*gradient(P)).dot(gradient(G))-nu*Q(G)
EX = lambda G,P: S.diff(L(P),t)+(J*gradient(P)).dot(gradient(L(P)))-S.diff(G**2,y1)/(2*y2)**2-nu*M(L(P))
verify('complete_circulation_residual_difference',EG(Gamma0+gamma,Psi0+psi)-EG(Gamma0,Psi0),D0(a)*Fs+w.dot(gradient(Gamma0))+w.dot(gradient(gamma))-nu*Q(gamma))
verify('complete_vorticity_residual_difference',EX(Gamma0+gamma,Psi0+psi)-EX(Gamma0,Psi0),D0(eta)+w.dot(gradient(xi0))+w.dot(gradient(eta))-S.diff(2*Gamma0*gamma+gamma**2,y1)/(2*y2)**2-nu*M(eta))
cutoff = 1+y1**2*y2+t*y2
test = y1**3+y2**4+t*y1*y2
for name,operator,B,drift in [('L',L,A,0),('Q',Q,C,0),('M',M,C,4*S.diff(cutoff,y2))]:
    right = 2*(B*gradient(cutoff)).dot(gradient(test))+(sum(B[i,j]*S.diff(cutoff,coordinates[i],coordinates[j]) for i in range(2) for j in range(2))+drift)*test
    verify(name+'_cutoff_commutator',operator(cutoff*test)-cutoff*operator(test),right)

lam, m, sigma, d, c, z1, kap, qq = S.symbols('lambda m sigma d c zeta1 kappa q',nonzero=True)
Bm = S.Matrix([[-nu*N**2*qq*m**2,-d/(sigma*kap)],[sigma*c*z1,-nu*N**2*qq*m**2]])
verify('full_phase_harmonic_characteristic_polynomial',(lam*S.eye(2)-Bm).det(),(lam+nu*N**2*qq*m**2)**2+c*d*z1/kap)

x1,x2,x3,aa,k0,b0 = S.symbols('x1 x2 x3 a k0 b0',real=True, nonzero=True)
k = k0*S.exp(aa*t)
bv = b0*S.exp(aa*t-nu*k0**2*(S.exp(2*aa*t)-1)/(2*aa))
V = bv/k
verify('Kelvin_vorticity_amplitude_ode',S.diff(bv,t),(aa-nu*k**2)*bv)
verify('Kelvin_velocity_amplitude_ode',S.diff(V,t),-nu*k**2*V)
uv = S.Matrix([-aa*x1,aa*x2,-V*S.sin(k*x1)])
pressure = -aa**2*(x1**2+x2**2)/2
xx = (x1,x2,x3)
for i in range(3):
    residual = S.diff(uv[i],t)+sum(uv[j]*S.diff(uv[i],xx[j]) for j in range(3))+S.diff(pressure,xx[i])-nu*sum(S.diff(uv[i],x,2) for x in xx)
    verify('Kelvin_full_NS_component_'+str(i+1),residual,0)
verify('Kelvin_curl_component_2',S.diff(uv[0],x3)-S.diff(uv[2],x1),bv*S.cos(k*x1))
potential=S.Matrix([0,(bv/k**2)*S.cos(k*x1),-aa*x1*x2])
potential_curl=S.Matrix([S.diff(potential[2],x2)-S.diff(potential[1],x3),S.diff(potential[0],x3)-S.diff(potential[2],x1),S.diff(potential[1],x1)-S.diff(potential[0],x2)])
for i in range(3):
    verify('Kelvin_explicit_vector_potential_curl_'+str(i+1),potential_curl[i],uv[i])

beta,ref_s,Us,Ls,ts,K0,K1=S.symbols('beta s Ustar Lstar taustar profile_L2_squared profile_gradient_L2_squared',positive=True)
energy = Us**2*Ls**3*ref_s**(5*beta-2)*K0
enstrophy = Us**2*Ls*ref_s**(3*beta-2)*K1
energy_work = -S.diff(energy,ref_s)/(2*ts)+nu*enstrophy
factored = (Us**2*Ls**3/ts)*ref_s**(5*beta-3)*K0*(-(5*beta-2)/2+(nu*ts/Ls**2)*(K1/K0)*ref_s**(1-2*beta))
verify('selfsimilar_exact_work_factorization',S.expand_power_base(energy_work,force=False),S.expand_power_base(factored,force=False))
verify('selfsimilar_velocity_gradient_energy_exponent',(3*beta-2)-(5*beta-2)/2,(beta-2)/2)
verify('selfsimilar_force_energy_exponent',(5*beta-3)-(5*beta-2)/2,(5*beta-4)/2)
verify('selfsimilar_relative_viscous_exponent',(3*beta-2)-(5*beta-3),1-2*beta)

# END UNCHANGED MATHEMATICAL BODY
finish('secondary', checks)
