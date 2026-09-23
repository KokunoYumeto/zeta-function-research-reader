"""Independent exact transport and reflection checks for EPR1–13.

No AP numerical enclosure or RH sign is certified by these identities.
"""
from pathlib import Path
import hashlib
import json
import sympy as sp

x,w,c,a,b=sp.symbols('x w c a b',real=True)
t,t0=sp.symbols('t t0',positive=True)
Q=sp.Function('Q')
H=sp.Function('H')
P=w*w-sp.Rational(1,4)
checks=[]


def exact(name, expression):
    value=sp.simplify(expression)
    assert value==0,(name,value)
    checks.append(name)


for sign in [1,-1]:
    phase=-x*x/(4*t)+sign*sp.I*x/(2*t)
    exact(f'chiral_drift_sign_{sign}',2*sp.diff(phase,x)+x/t-sign*sp.I/t)
    exact(f'chiral_scalar_sign_{sign}',sp.diff(phase,t)+sp.diff(phase,x,2)-sp.diff(phase,x)**2-sp.Rational(1,4)/t**2+sp.Rational(1,2)/t)
    arg=sp.Rational(1+sign,2)+sp.I*t*w
    M=sp.sqrt(sp.pi*t)/8*sp.exp(t*w*w-sp.Rational(1,4)/t-sign*sp.I*w)*Q(arg)
    scalar=-w*w+sp.Rational(1,2)/t+sp.Rational(1,4)/t**2+sign*sp.I*w/t
    exact(f'chiral_mellin_PDE_{sign}',sp.diff(M,t)-w/t*sp.diff(M,w)-scalar*M)
    F=P*M
    exact(f'filtered_mellin_PDE_{sign}',sp.diff(F,t)-w/t*sp.diff(F,w)-(scalar-2*w*w/(t*P))*F)
    w0=t*w/t0
    E=sp.sqrt(t/t0)*sp.exp(t*w*w-t0*w0*w0-sp.Rational(1,4)/t+sp.Rational(1,4)/t0)
    M0=sp.sqrt(sp.pi*t0)/8*sp.exp(t0*w0*w0-sp.Rational(1,4)/t0-sign*sp.I*w0)*Q(sp.Rational(1+sign,2)+sp.I*t0*w0)
    exact(f'chiral_time_rotation_{sign}',M-E*sp.exp(sign*sp.I*(w0-w))*M0)

hc=sp.exp(-x*x/(4*t))*H(x)*sp.cos(x/(2*t))
fc=sp.diff(hc,x,2)-hc/4
expected=sp.Subs(sp.diff(H(x),x,2),x,0)-(1/(2*t)+1/(4*t*t)+sp.Rational(1,4))*H(0)
exact('cosine_first_source_moment',fc.subs(x,0)-expected)
exact('source_moment_time_1_over_32',(1/(2*t)+1/(4*t*t)+sp.Rational(1,4)).subs(t,sp.Rational(1,32))-sp.Rational(1089,4))
exact('two_translate_orientation',sp.exp(a*c)*sp.exp(-b*c)-sp.exp((a-b)*c))
exact('negative_source_shift_Taylor_orientation',sp.exp(-a*c)*sp.exp(b*c)-sp.exp((b-a)*c))

# Algebraic numerator behind the endpoint-curvature ordinate estimate.
z,B=sp.symbols('z B',real=True)
exact('ordinate_bound_cross_multiplication',(z+B)*(z+1)-((z+B)**2+z*(1-4*B))-B*(3*z+1-B))

pi=sp.pi
Tstar=2*(pi-1)/(pi-1+sp.Rational(8,21))
exact('closed_time_interval_phase_endpoint',1+sp.Rational(8,21)*Tstar/(2-Tstar)-pi)
exact('fixed_time_phase_constant',1+sp.Rational(8,21)*sp.Rational(1,32)/(2-sp.Rational(1,32))-sp.Rational(1331,1323))

base=Path(__file__).parent
source=base/'ENDPOINT_PAIR_TRANSPORT_AND_WEIL_MATRIX.md'
review=base/'ENDPOINT_PAIR_TRANSPORT_REVIEW.md'
result={
    'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
    'review_sha256':hashlib.sha256(review.read_bytes()).hexdigest(),
    'scope':'EPM1–47, EPR1–13; exact PDE, chiral transport, source moments, translation orientation and phase constants. No AP numerical audit.',
    'exact_checks':len(checks),'checks':checks
}
(base/'ENDPOINT_PAIR_TRANSPORT_REVIEW_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['source_sha256','review_sha256','exact_checks']}))
