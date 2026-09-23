"""Exact algebra checks for EPM and ERD; not a numerical RH test."""
from pathlib import Path
import hashlib,json
import sympy as s
B=Path(__file__).resolve().parent
x,w,t,t0,q=s.symbols('x w t t0 q',real=True,nonzero=True)
checks={}
def eq(name,a,b=0):
    v=s.simplify(s.expand(a-b))
    if v!=0: raise AssertionError((name,v))
    checks[name]=True
for sign in [1,-1]:
    a=-x*x/(4*t)+sign*s.I*x/(2*t)
    eq('source_drift_'+str(sign),2*s.diff(a,x),-x/t+sign*s.I/t)
    eq('source_scalar_'+str(sign),s.diff(a,t)+s.diff(a,x,2)-s.diff(a,x)**2,1/(4*t*t)-1/(2*t))
P=w*w-s.Rational(1,4)
eq('endpoint_polynomial',P,(w+s.Rational(1,2))*(w-s.Rational(1,2)))
eq('endpoint_log_derivative',s.diff(P,w)/P,2*w/P)
# Exact chiral combinations, leaving both original product values independent.
U,V=s.symbols('U V')
mc=s.exp(-s.I*w)*U+s.exp(s.I*w)*V
ms=(s.exp(-s.I*w)*U-s.exp(s.I*w)*V)/s.I
eq('chiral_plus',mc+s.I*ms,2*s.exp(-s.I*w)*U)
eq('chiral_minus',mc-s.I*ms,2*s.exp(s.I*w)*V)
eq('phase_derivative_c',s.diff(mc,w),ms)
eq('phase_derivative_s',s.diff(ms,w),-mc)
eq('characteristic_scalar',s.diff((q*q-s.Rational(1,4))/t+s.log(t)/2,t),
   -(q/t)**2+1/(2*t)+1/(4*t*t))
eq('characteristic_angle',s.diff(q/t0-q/t,t),q/t**2)
exp0=t*w*w-t0*(t*w/t0)**2-1/(4*t)+1/(4*t0)
expinv=t0*(t*w/t0)**2-t*w*w-1/(4*t0)+1/(4*t)
eq('transport_inverse_exponent',exp0+expinv)
eq('transport_inverse_angle',(t*w/t0-w)+(w-t*w/t0))
eq('phase_bound_at_1_32',1+s.Rational(8,21)*s.Rational(1,32)/(2-s.Rational(1,32)),s.Rational(1331,1323))
b,g=s.symbols('b g',real=True)
eq('curvature_rational_cross_multiplication',(g+b)*(g+1)-((g+b)**2+g*(1-4*b)),b*(3*g+1-b))
# Exact vanishing-factor differential recurrence; every derivative is g_t times a Laurent polynomial.
L=1/(2*t)+1/(4*t*t)
rat=s.Integer(1)
for n in range(1,9):
    rat=s.diff(rat,t)+L*rat
    expr=s.Poly(s.expand(rat).subs(t,1/x),x)
    checks['flat_derivative_Laurent_'+str(n)]=bool(all(k[0]>=0 for k,c in expr.terms()))
# Reflected coefficient and raw trivial-zero signs retain every parity.
for eta in [1,-1]:
    for j in range(3):
        for k in range(3):
            eq('raw_sign_'+str((eta,j,k)),eta*(-1)**j*(-1)**(j+k),eta*(-1)**k)
out={'scope':'Exact identities and derivative recurrence only; complete analytic proofs accompany them.',
     'checks':checks,'exact_checks':len(checks),'all_passed':all(checks.values()),
     'proof_sha256':{n:hashlib.sha256((B/n).read_bytes()).hexdigest()
     for n in ['ENDPOINT_RESONANT_ZERO_DETECTION.md','ENDPOINT_PAIR_TRANSPORT_AND_WEIL_MATRIX.md']}}
(B/'ENDPOINT_TRANSPORT_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
