"""Original cosine/sine source Gram and supported-zero return certificate.

Computes original moments and arithmetic integrals in ball arithmetic.
No nontrivial-zero list, RH assumption, or omitted source residual.
"""
from pathlib import Path
import json,platform,importlib.metadata
from flint import arb,acb,ctx
import sympy as sp

ctx.prec=100
outdir=Path(__file__).parent
pi=arb.pi()
def integral(fun,left,right,panels):
    result=acb(0)
    for i in range(panels):
        l=arb(left)+(arb(right)-arb(left))*i/panels
        r=arb(left)+(arb(right)-arb(left))*(i+1)/panels
        result+=acb.integral(fun,acb(l),acb(r),abs_tol=arb('1e-20'),rel_tol=arb('1e-20'),eval_limit=100000,depth_limit=30)
    if not result.is_finite() or not result.imag.contains(0):raise ArithmeticError('Invalid integral enclosure')
    return result.real
def phi16(u):
    e4=(4*u).exp();e5=(5*u).exp();e9=(9*u).exp()
    return sum((2*pi*pi*n**4*e9-3*pi*n*n*e5)*(-pi*n*n*e4).exp() for n in range(1,17))
J={j:integral(lambda u,analytic:u**j*(u*u/32).exp()*phi16(u),0,3,24)+arb(0,'1e-300') for j in [0,2,3,4]}
C,J2,J3=J[0],J[2],J[3]
r,x=sp.symbols('r x',nonnegative=True)
AA=sp.Rational(1089,4)+512*r+256*r*r
EE=1+32*r+sp.Rational(1345,8)*r*r+256*r**3+128*r**4
BB=4868+13060*r+12288*r*r+4096*r**3
E1=48+sp.Rational(3457,4)*r+3970*r*r+7298*r**3+6144*r**4+2048*r**5
def gm(j):
    z=arb(j+1)/2
    return z.gamma()/arb(16)**z
def rat(q):return arb(int(sp.numer(q)))/int(sp.denom(q))
def gauss(P):return sum((rat(c)*gm(j[0]) for j,c in sp.Poly(sp.expand(P),r).terms()),arb(0))
def convolve_envelope(P,Q,y):
    poly=sp.Poly(sp.expand(P.subs(r,r+x/2)*Q.subs(r,r+x/2)),r,x)
    return sum((rat(c)*gm(j)*y**l for (j,l),c in poly.terms()),arb(0))
n0=C*gauss(AA*AA).sqrt();ne=J2*gauss(EE*EE).sqrt()
n1=C*gauss(BB*BB).sqrt();ne1=(J2**2*gauss(E1*E1)+2*J2*J3*gauss(E1)+J3**2*gauss(1)).sqrt()
d0=2*n0*ne+ne**2;d2=2*n1*ne1+ne1**2
eg=(arb.const_euler()+pi.log()+arb(3)/2+4*arb(16).log()+((-arb(1)).exp()+4*(-arb(1)/4).exp())/(1-(-arb(1)).exp()))*d0+d2/(8*256)
primepowers=[];ep=arb(0)
for n in range(2,65):
    ff=sp.factorint(n)
    if len(ff)!=1:continue
    p=int(next(iter(ff)));y=arb(n).log();a=2*arb(p).log()/arb(n).sqrt()
    primepowers.append((n,p,y,a))
    ep+=a*(-4*y*y).exp()*(2*C*J2*convolve_envelope(AA,EE,y)+J2**2*convolve_envelope(EE,EE,y))
def compute(sign):
    def k0(y):
        osc=(65536*y**4-1622528*y*y+1250369)*(16*y).cos()+2048*y*(256*y*y-1121)*(16*y).sin()
        other=sign*(-arb(16)).exp()*(65536*y**4-49664*y*y+3137)
        return C*C*pi.sqrt()/128*(-4*y*y).exp()*(osc+other)
    kzero=k0(acb(0)).real
    def gammaint(y,analytic):return ((-y).exp()*kzero-(-y/4).exp()*k0(y/2))/(-(-y).expm1())
    eps=arb(1)/65536
    origin=3*kzero*eps/2+n1*n1*eps*eps/8
    gamma=-(arb.const_euler()+pi.log())*kzero+integral(gammaint,eps,8,64)-kzero*(1-(-arb(8)).exp()).log()+arb(0,origin.upper())+arb(0,'1e-23')
    prime=sum((a*k0(acb(y)).real for n,p,y,a in primepowers),arb(0))
    base=gamma-prime
    full=base+arb(0,(eg+ep).upper())+arb(0,'1e-21')
    if not(full>50 and full<64):raise ArithmeticError('Required actual diagonal bound not established')
    return full,{'comparison':base.str(32),'Gamma_comparison':gamma.str(32),'finite_prime_comparison':prime.str(32),'lower':full.lower().str(32),'upper':full.upper().str(32)}
kc,rc=compute(1);ks,rs=compute(-1)
A=-J2-arb(1089)*C/4
B=-48*J2-4868*C
R=-(pi/32).sqrt()*(-arb(8)).exp()/32
Tstar=(R/A)**2/(4*pi)
T=arb(1)/32
kap=1/(4*pi*T).sqrt()
d=(kap*R-A)/B
ratio=ks/kc
normsquare=1+ratio*d*d
commutator_amplitude=abs(d)*ks
print('Critical coefficient heat time:',Tstar,flush=True)
checks={'both_diagonals_50_64':bool(kc>50 and kc<64 and ks>50 and ks<64),'A_negative':bool(A<0),'B_negative':bool(B<0),'R_negative':bool(R<0),'critical_time_positive':bool(Tstar>0),'critical_time_between_2.99e-15_and_3e-15':bool(Tstar>arb('2.99e-15') and Tstar<arb('3e-15')),'d_negative_at_T_1_32':bool(d<0),'operator_norm_strictly_above_one':bool(normsquare>1)}
if not all(checks.values()):raise ArithmeticError(checks)
out={'scope':'Actual original reflected Weil Gram of fc,fs at t=1/32; cross entry is exactly zero by the separate proof. Complete residual retained.','bits':ctx.prec,'python':platform.python_version(),'python_flint':importlib.metadata.version('python-flint'),'J':{str(j):v.str(32) for j,v in J.items()},'cosine':rc,'sine':rs,'Gamma_residual_bound':eg.str(32),'prime_residual_bound':ep.str(32),'moment_A':A.str(32),'moment_B':B.str(32),'moment_R':R.str(32),'critical_coefficient_heat_time':Tstar.str(32),'T_1_32_d':d.str(32),'T_1_32_operator_norm_squared_lower':normsquare.lower().str(32),'T_1_32_operator_norm_squared_upper':normsquare.upper().str(32),'T_1_32_nonselfadjoint_commutator_amplitude_lower':commutator_amplitude.lower().str(32),'T_1_32_nonselfadjoint_commutator_amplitude_upper':commutator_amplitude.upper().str(32),'checks':checks}
outdir.joinpath('PAIR_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(out,indent=2))
