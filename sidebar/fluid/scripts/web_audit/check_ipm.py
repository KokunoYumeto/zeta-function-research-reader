# Portable adaptation of ipm/replay.py
# Only import/output/inventory handling changed; the delimited mathematics is a raw source byte slice.
from __future__ import annotations
from fractions import Fraction
from itertools import combinations
import sympy as s
import sympy as sp
import sympy as S
from portable_common import begin, finish
begin('ipm')
# BEGIN UNCHANGED MATHEMATICAL BODY
checks=[]
def check(name,lhs,rhs=0,conditions=None):
    residual=lhs-rhs
    reduced=s.cancel(s.expand(residual))
    ok=reduced==0
    checks.append({'name':name,'hypotheses':conditions or [],'lhs':str(lhs),
                   'rhs':str(rhs),'unreduced_residual':str(residual),
                   'exact_reduced_residual':str(reduced),'passed':ok})
    if not ok:
        raise AssertionError(name+': '+str(reduced))

x1,x2,t,t0,z=s.symbols('x1 x2 t t0 z',real=True)
k1,k2,A,a0,n=s.symbols('k1 k2 A a0 n',real=True)
kappa=k1**2+k2**2
m=s.Matrix([k1*k2/kappa,-k1**2/kappa])
k=s.Matrix([k1,k2])
domain=['k1,k2 real','k1**2+k2**2>0']
check('symbol_transversality',m.dot(k),conditions=domain)
check('symbol_evenness_1',m[0].subs({k1:-k1,k2:-k2},simultaneous=True),m[0],domain)
check('symbol_evenness_2',m[1].subs({k1:-k1,k2:-k2},simultaneous=True),m[1],domain)
for j in range(2):
    check(f'all_nonzero_harmonic_symbol_{j+1}',m[j].subs({k1:n*k1,k2:n*k2},simultaneous=True),m[j],domain+['n!=0'])
check('pressure_poisson',-kappa*(s.I*k2/kappa),-s.I*k2,domain)
for j in range(2):
    check(f'fourier_darcy_{j+1}',-s.I*k[j]*(s.I*k2/kappa)-(1 if j==1 else 0),m[j],domain)
check('symbol_length_squared',m.dot(m),k1**2/kappa,domain)

lam=A*k1**2/kappa
a=a0*s.exp(lam*(t-t0))
phase=k1*x1+k2*x2
H=s.Function('H')
h=s.Subs(s.Derivative(H(z),z),z,phase)
rho=A*x2+a*h
u=a*m*h
p=-A*x2**2/s.Integer(2)-a*k2/kappa*H(phase)
check('amplitude_ode',s.diff(a,t),lam*a,domain)
for j,xj in enumerate([x1,x2]):
    check(f'full_affine_darcy_{j+1}',u[j]+s.diff(p,xj)+(rho if j==1 else 0),conditions=domain+['h=H prime'])
check('full_affine_divergence',s.diff(u[0],x1)+s.diff(u[1],x2),conditions=domain)
check('full_affine_unforced_transport',s.diff(rho,t)+u[0]*s.diff(rho,x1)+u[1]*s.diff(rho,x2),conditions=domain+['h=H prime'])
check('full_affine_pressure_poisson',s.diff(p,x1,2)+s.diff(p,x2,2),-s.diff(rho,x2),domain)

I,hv,hp=s.symbols('I h hprime',real=True)
Jac=s.eye(2)+I*hp*m*k.T
check('flow_jacobian_determinant',Jac.det(),1,domain)
check('flow_phase_preservation',k.dot(I*m*hv),conditions=domain)
check('transported_density_bracket_derivative',A*m[1]*a+s.diff(a,t),conditions=domain)

# Full residual coefficient map, retaining the primary coefficient 2*pi.
sig_t,adv=s.symbols('sigma_t M0sigma_dot_grad_sigma')
check('primary_report_residual_intertwining',2*s.pi*sig_t+(2*s.pi)**2*adv,2*s.pi*(sig_t+2*s.pi*adv))
b,bd,sig_x2,Uadv,G=s.symbols('b bprime sigma_x2 Uadv G')
check('mean_translation_full_transport',2*s.pi*(G-Uadv)+2*s.pi*b*sig_x2+bd+2*s.pi*(Uadv-b*sig_x2),2*s.pi*G+bd)
barh,av,hprime=s.symbols('hbar a hprime')
fullv=av*m*(hv-barh)-av*barh*s.Matrix([0,1])
check('nonzero_mean_wave_self_advection',fullv.dot(av*k*hprime),-av**2*barh*k2*hprime,domain)

# Affine source coefficient: explicit map rather than setting 2*pi to one.
As,aas=s.symbols('A_source a_source')
check('source_report_growth_rate',(A*k1**2/kappa).subs(A,2*s.pi*As),2*s.pi*As*k1**2/kappa,domain)
check('source_report_affine_pressure_background',(-A*x2**2/2).subs(A,2*s.pi*As),-s.pi*As*x2**2)

# The exact addition/mollification identities viewed as polynomial identities.
rt,Srt,Smnon,v1,v2,rx,ry,w1,w2,tx,ty,tt,F,C=s.symbols('rt Srt Snon v1 v2 rx ry w1 w2 tx ty tt F C')
check('child_residual_all_four_terms',(rt+tt)+(v1+w1)*(rx+tx)+(v2+w2)*(ry+ty)-(rt+v1*rx+v2*ry),tt+v1*tx+v2*ty+w1*rx+w2*ry+w1*tx+w2*ty)
check('fixed_mollifier_exact_commutator',Srt+v1*rx+v2*ry,(Srt+Smnon)+(v1*rx+v2*ry-Smnon))

# Complete spatial and temporal cutoff expansion for the proved affine field.
chi,chit,r,r1,r2,chi1,chi2,U1,U2,E1,E2=s.symbols('chi chi_t r r_x1 r_x2 chi_x1 chi_x2 U1 U2 E1 E2')
Ugrad=U1*r1+U2*r2
direct=chit*r-chi*Ugrad+(chi*U1+E1)*(chi*r1+r*chi1)+(chi*U2+E2)*(chi*r2+r*chi2)
retained=chit*r+chi*(chi-1)*Ugrad+chi*r*(U1*chi1+U2*chi2)+r*(E1*chi1+E2*chi2)+chi*(E1*r1+E2*r2)
check('complete_affine_cutoff_force_all_terms',direct,retained)
mu,mud,n1,n2,ds1,ds2=s.symbols('mu muprime n1 n2 ds1 ds2')
check('moving_fourier_cutoff_symbol_chain_rule',(-n1/mu**2)*mud*ds1+(-n2/mu**2)*mud*ds2,-mud/mu**2*(n1*ds1+n2*ds2),['mu>0'])
c=s.Function('c')(t)
check('retained_pressure_gauge_x1',s.diff(c,x1))
check('retained_pressure_gauge_x2',s.diff(c,x2))

# END UNCHANGED MATHEMATICAL BODY
finish('ipm', checks)
