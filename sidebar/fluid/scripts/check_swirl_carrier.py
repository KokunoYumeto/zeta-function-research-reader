"""Exact original-coordinate replay of the complete swirl carrier map."""
from pathlib import Path
import hashlib
import json
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
y1,t=s.symbols('y1 t',real=True)
y2,nu,mu,c=s.symbols('y2 nu mu c',positive=True)
y=(y1,y2)
h=s.Function('h')(y1,y2,t)
theta=s.Function('theta')(y1,y2,t)
psi=s.Function('Psi')(y1,y2,t)
chi=s.Function('chi')(y1,y2)
eta=s.Function('eta')(t)
checks={}

def Q(f): return s.diff(f,y1,2)+2*y2*s.diff(f,y2,2)
def M(f): return Q(f)+4*s.diff(f,y2)
def inner(f,g): return s.diff(f,y1)*s.diff(g,y1)+2*y2*s.diff(f,y2)*s.diff(g,y2)
def grad(f): return s.Matrix([s.diff(f,z) for z in y])
J=s.Matrix([[0,-1],[1,0]])
v0=J*grad(psi)
v=eta*v0
def D(f): return s.diff(f,t)+v.dot(grad(f))
def zero(name,expression):
    result=s.factor(s.expand(expression))
    if result != 0:
        result=s.simplify(result)
    checks[name]={'passed':result==0,'residual':str(result)}
    if result!=0: raise AssertionError((name,result))

zero('circulation_diffusion_product',Q(2*y2*h)-2*y2*M(h))
zero('circulation_transport_product',D(2*y2*h)-2*y2*D(h)-2*v[1]*h)
zero('square_meridional_source',s.diff((2*y2*h)**2,y1)/(2*y2)**2-s.diff(h*h,y1))
zero('square_diffusion_product',M(h*h)-2*h*M(h)-2*inner(h,h))
zero('swirl_rate_force_dictionary',
     D(2*y2*h)-nu*Q(2*y2*h)-2*y2*(D(h)-nu*M(h)+v[1]*h/y2))
H=s.sqrt(c+mu*theta)
Etheta=D(theta)-nu*M(theta)
zero('positive_root_diffusion_chain',D(H)-nu*M(H)-mu*Etheta/(2*H)-nu*mu**2*inner(theta,theta)/(4*H**3))
hh=eta*chi*H
Rh=(s.diff(eta,t)*chi*H+eta*chi*(mu*Etheta/(2*H)+nu*mu**2*inner(theta,theta)/(4*H**3)+v[1]*H/y2)
    +eta*H*(v.dot(grad(chi))-nu*M(chi))-eta*nu*mu*inner(chi,theta)/H)
zero('complete_cutoff_swirl_residual',D(hh)-nu*M(hh)+v[1]*hh/y2-Rh)
zero('general_cutoff_square_source',s.diff(hh**2,y1)-eta**2*(c*s.diff(chi**2,y1)+mu*s.diff(chi**2*theta,y1)))
xi0=s.diff(psi,y2,2)+s.diff(psi,y1,2)/(2*y2)
xi=eta*xi0
E0=s.diff(xi0,t)+v0.dot(grad(xi0))-nu*M(xi0)-mu*s.diff(theta,y1)
Exi=(eta*E0+s.diff(eta,t)*xi0+eta*(eta-1)*(v0.dot(grad(xi0))-mu*s.diff(theta,y1))
      -eta**2*c*s.diff(chi**2,y1))
# The plateau assumption is retained as an explicit correction for arbitrary
# chi and theta, then proved zero in the TeX from chi² theta=theta.
general_correction=-eta**2*mu*s.diff((chi**2-1)*theta,y1)
zero('complete_vorticity_activation_and_edge_terms',D(xi)-nu*M(xi)-s.diff(hh**2,y1)-Exi-general_correction)
zero('meridional_divergence',s.diff(v[0],y1)+s.diff(v[1],y2))
zero('swirl_energy_weight',(2*y2*hh)**2/(2*y2)-2*y2*eta**2*chi**2*(c+mu*theta))

result={'schema_version':1,'scope':'Exact swirl-rate, positive-carrier, cutoff and activation identities; analytical support, root domain, pressure and decay proofs in tex/swirl_carrier_transfer.tex.',
        'checks':checks,'all_passed':all(q['passed'] for q in checks.values()),
        'retained_domains':['y1=z','y2=r^2/2>0','nu>0','mu>0','c>mu*sup|theta|',
                            'chi=1 near all theta support','0<T0<T1'],
        'proof_sha256':hashlib.sha256((ROOT/'tex/swirl_carrier_transfer.tex').read_bytes()).hexdigest(),
        'classical_navier_stokes_counterexample_established':False}
out=ROOT/'checks/swirl_carrier_checks.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'{len(checks)} exact swirl-carrier checks passed.')
