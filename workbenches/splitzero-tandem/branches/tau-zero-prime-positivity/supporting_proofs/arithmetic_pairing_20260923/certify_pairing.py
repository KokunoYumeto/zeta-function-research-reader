"""Interval certificate for the original endpoint test. No zero data used.

All integration uses python-flint acb.integral. Tail constants are proved in
the companion mathematical source; no floating quadrature is certified here.
"""
from pathlib import Path
import json, platform, importlib.metadata
from flint import arb,acb,ctx
import sympy as sp

ctx.prec=100
ROOT=Path(__file__).parent
pi=arb.pi()
def integral(fun,left,right,panels):
    total=acb(0)
    for i in range(panels):
        l=arb(left)+(arb(right)-arb(left))*i/panels
        r=arb(left)+(arb(right)-arb(left))*(i+1)/panels
        total+=acb.integral(fun,acb(l),acb(r),abs_tol=arb('1e-20'),rel_tol=arb('1e-20'),eval_limit=100000,depth_limit=30)
    if not total.is_finite():raise ArithmeticError('Nonfinite quadrature')
    if not total.imag.contains(0):raise ArithmeticError('Imaginary component excludes zero')
    return total.real
def phifinite(u):
    e4=(4*u).exp(); e5=(5*u).exp();e9=(9*u).exp()
    return sum((2*pi*pi*n**4*e9-3*pi*n*n*e5)*(-pi*n*n*e4).exp() for n in range(1,17))
J={}
for j in [0,2,3,4]:
    J[j]=integral(lambda u,analytic: u**j*(u*u/32).exp()*phifinite(u),0,3,24)+arb(0,'1e-300')
    print('J',j,J[j],flush=True)
# Tail radius 1e-300 requires the original-theta tail proof in INDEPENDENT_TAIL_BOUNDS.md.
C=J[0];J2=J[2];J3=J[3]
assert C>arb('0.06216254') and C<arb('0.06216255')
assert J2>0 and J2<arb('0.000719')
assert J3>0 and J3<arb('0.000120')
def k0(y):
    pol=(65536*y**4-1622528*y*y+1250369)*(16*y).cos()+2048*y*(256*y*y-1121)*(16*y).sin()
    other=(-arb(16)).exp()*(65536*y**4-49664*y*y+3137)
    return C*C*pi.sqrt()/128*(-4*y*y).exp()*(pol+other)
kzero=k0(acb(0)).real
def gamfun(y,analytic):
    return ((-y).exp()*kzero-(-y/4).exp()*k0(y/2))/(-(-y).expm1())
r=sp.symbols('r',nonnegative=True)
A=sp.Rational(1089,4)+512*r+256*r*r
E=1+32*r+sp.Rational(1345,8)*r*r+256*r**3+128*r**4
E1=48+sp.Rational(3457,4)*r+3970*r*r+7298*r**3+6144*r**4+2048*r**5
B=13060*r+4096*r**3+4868+12288*r*r
def gaussian_abs(pol):
    pp=sp.Poly(sp.expand(pol),r)
    total=arb(0)
    for j,cc in pp.terms():
        coeff=arb(int(sp.numer(cc)))/int(sp.denom(cc))
        exponent=arb(j[0]+1)/2
        total+=coeff*exponent.gamma()/arb(16)**exponent
    return total
normf=C*gaussian_abs(A*A).sqrt()
norme=J2*gaussian_abs(E*E).sqrt()
delta0=2*normf*norme+norme*norme
normfp=C*gaussian_abs(B*B).sqrt()
normep=(J2**2*gaussian_abs(E1*E1)+2*J2*J3*gaussian_abs(E1)+J3**2*gaussian_abs(1)).sqrt()
delta2=2*normfp*normep+normep**2
eps=arb(1)/65536
origin_error=3*kzero*eps/2+normfp**2*eps**2/8
gamma0=-(arb.const_euler()+pi.log())*kzero+integral(gamfun,eps,8,64)-kzero*(1-(-arb(8)).exp()).log()+arb(0,origin_error.upper())+arb(0,'1e-23')
prime0=arb(0);prime_error=arb(0)
for n in range(2,65):
    factors=sp.factorint(n)
    if len(factors)!=1:continue
    p=int(next(iter(factors)));y=arb(n).log()
    coeff=2*arb(p).log()/arb(n).sqrt()
    prime0+=coeff*k0(acb(y)).real
    # Expand the nonnegative envelope at r+y/2 without interval-to-symbol conversion.
    def conv_abs(P,Q):
        pol=sp.Poly(sp.expand(P.subs(r,r+sp.Symbol('x')/2)*Q.subs(r,r+sp.Symbol('x')/2)),r,sp.Symbol('x'))
        val=arb(0)
        for (j,k),cc in pol.terms():
            c=arb(int(sp.numer(cc)))/int(sp.denom(cc))
            exponent=arb(j+1)/2
            val+=c*y**k*exponent.gamma()/arb(16)**exponent
        return val
    prime_error+=coeff*(-4*y*y).exp()*(2*C*J2*conv_abs(A,E)+J2*J2*conv_abs(E,E))
h=arb(1)/16
gamma_error=(arb.const_euler()+pi.log()+arb(3)/2+4*(1/h).log()+((-arb(1)).exp()+4*(-arb(1)/4).exp())/(1-(-arb(1)).exp()))*delta0+delta2*h*h/8
K0=gamma0-prime0
K=K0+arb(0,(gamma_error+prime_error).upper())+arb(0,'1e-21')
checks={'delta0_lt_0.303':bool(delta0<arb('0.303')),'delta2_lt_175':bool(delta2<175),'gamma_error_lt_6.1':bool(gamma_error<arb('6.1')),'prime_error_lt_0.45':bool(prime_error<arb('0.45')),'K0_between_56.95_and_56.97':bool(K0>arb('56.95') and K0<arb('56.97')),'full_K_between_50_and_64':bool(K>50 and K<64)}
if not all(checks.values()):raise ArithmeticError(checks)
out={'scope':'Original endpoint test t=1/32; full-source error included. Tail proof required alongside this certificate.','bits':ctx.prec,'python':platform.python_version(),'python_flint':importlib.metadata.version('python-flint'),'J':{str(j):v.str(32) for j,v in J.items()},'k0_at_zero':kzero.str(32),'origin_error':origin_error.str(32),'Gamma0':gamma0.str(32),'Prime0_finite':prime0.str(32),'K0':K0.str(32),'delta0':delta0.str(32),'delta2':delta2.str(32),'Gamma_error':gamma_error.str(32),'Prime_error':prime_error.str(32),'K_full_lower_directed':K.lower().str(32),'K_full_upper_directed':K.upper().str(32),'certified_rational_enclosure':[50,64],'checks':checks}
ROOT.joinpath('CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(out,indent=2))
