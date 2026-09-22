"""Exact auxiliary identities for the original cutoff profile.

The Landen coordinate is an explicit change of scalar variable only.
Original programme metrics and polynomial coordinates are not changed.
"""
import sympy as s
from pathlib import Path
import json
P=Path(__file__).parent
w,mu,t=s.symbols('w mu t',positive=True)
K,E=s.symbols('K E')
checks=[]
def check(name,x):
    x=s.factor(x)
    if x!=0:raise ArithmeticError((name,x))
    checks.append(name)
# Parameter differential equations for K(sqrt(z)), E(sqrt(z)).
z=4*w/(1+w)**2
dK=(E/(1-z)-K)/(2*z); dE=(E-K)/(2*z)
def dd(x):return s.diff(x,w)+s.diff(x,K)*dK*s.diff(z,w)+s.diff(x,E)*dE*s.diff(z,w)
F=K/(1+w)
check('Exact transformed K differential equation',w*(1-w*w)*dd(dd(F))+(1-3*w*w)*dd(F)-w*F)
# E at modulus w follows from K(w) and its derivative.
Em=(1-w*w)*(w*dd(F)+F)
check('Exact E transformation',2*Em-(1-w*w)*F-(1+w)*E)
# Original r -> mu dictionary.
r=(1-w)/(1+w)
check('Original t dictionary',(2*E-(1-w*w)*K)/((1+w)*r*(1+w)*K)-1-(2*E/((1-w*w)*K)-2))
N=7
coeff=[s.binomial(2*n,n)**2/s.Integer(16)**n for n in range(N)]
k=sum(coeff[n]*mu**n for n in range(N))
e=1-sum(coeff[n]*mu**n/s.Integer(2*n-1) for n in range(1,N))
T=s.series(2*(e/((1-mu)*k)-1),mu,0,6).removeO().expand()
inv=t
inverse_coeff={1:s.Integer(1)}
for n in range(2,6):
    a=s.Symbol('a')
    trial=inv+a*t**n
    residual=s.series(T.subs(mu,trial)-t,t,0,n+1).removeO().expand().coeff(t,n)
    v=s.solve(residual,a)[0];inv=trial.subs(a,v);inverse_coeff[n]=v
check('Series inverse through degree five',s.series(T.subs(mu,inv)-t,t,0,6).removeO())
u=s.expand(inv/t-1)
freg=s.series(-sum((-1)**(n+1)*u**n/s.Integer(n) for n in range(1,5))/2,t,0,5).removeO().expand()
if not all(v.is_Rational for v in s.Poly(freg,t).all_coeffs()):raise ArithmeticError('Nonrational formal-series coefficient')
Jreg=s.integrate(freg,(t,0,t))
# Exact profile derivative, using parameter mu and the elliptic ODE.
T_exact=2*(E/((1-mu)*K)-1)
Kp=(E/(1-mu)-K)/(2*mu);Ep=(E-K)/(2*mu)
def dm(x):return s.diff(x,mu)+s.diff(x,K)*Kp+s.diff(x,E)*Ep
check('Exact stationary cancellation in dJ/dmu',-T_exact/(2*mu)+2*Kp/K)
record={'passed':len(checks),'checks':checks,'t_of_mu_through_degree5':str(T),'mu_of_t_through_degree5':str(inv),'f_plus_half_log_t':str(freg),'J_minus_half_t_one_minus_log_t':str(Jreg),'scope':'Exact finite algebra and rational series coefficients; analytic convergence and remainder proof in ELLIPTIC_PROFILE_PROOF.md.'}
(P/'profile_scalar_exact.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record,indent=2))
