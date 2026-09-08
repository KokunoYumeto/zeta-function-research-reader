"""Exact spectral-distribution, heat, and original-coordinate checks."""
from pathlib import Path
import hashlib,json
import sympy as S

ROOT=Path(__file__).resolve().parents[1]
t,s,v,r,u,lam=S.symbols('t s v r u lambda')
c0=-S.Rational(59,275184)
beta=S.Rational(1,336)
c1=S.Rational(1,1296)
c2=S.Rational(3,132496)
rows=[]
def exact(name,expr):
    terms=list(expr) if isinstance(expr,S.MatrixBase) else [expr]
    residuals=[S.expand(S.together(q).as_numer_denom()[0]) for q in terms]
    assert all(q==0 for q in residuals),(name,residuals)
    rows.append({'id':name,'status':'exact_zero_residual','entries':len(terms)})

def d(h):
    return c0*h.subs(lam,3)-beta*S.diff(h,lam).subs(lam,3)+c1*h.subs(lam,S.Rational(9,2))+c2*h.subs(lam,S.Rational(13,2))
exact('source_connected_spin_channels',S.Rational(1,324)+S.Rational(3,676)-S.Rational(1,144)-S.Rational(127,219024))
exact('source_zeroth_moment',d(S.Integer(1))-S.Rational(127,219024))
exact('source_first_moment',d(lam))
Q=S.Matrix([[3,-1,0,0],[0,3,0,0],[0,0,S.Rational(9,2),0],[0,0,0,S.Rational(13,2)]])
initial=S.Matrix([c0,beta,c1,c2])
heat=S.diag(S.exp(9*t/4),S.exp(9*t/4),S.exp(81*t/16),S.exp(169*t/16))
heat[0,1]=-3*t*S.exp(9*t/4)/2
exact('full_jordan_heat_ode',S.diff(heat,t)-Q*Q*heat/4)
exact('full_jordan_initial',heat.subs(t,0)-S.eye(4))
fourier=S.Matrix([[S.exp(3*S.I*s),-S.I*s*S.exp(3*S.I*s),S.exp(9*S.I*s/2),S.exp(13*S.I*s/2)]])
exact('four_dimensional_fourier_intertwining',fourier.diff(s)-S.I*fourier*Q)
J=(c0-t/S.Integer(224)-S.I*s/336)*S.exp(9*t/4+3*S.I*s)+c1*S.exp(81*t/16+9*S.I*s/2)+c2*S.exp(169*t/16+13*S.I*s/2)
exact('spectral_packet_all_terms',J-(fourier*heat*initial)[0])
exact('packet_direct_distribution',J-d(S.exp(t*lam**2/4+S.I*s*lam)))
exact('packet_Newman_heat',S.diff(J,t)+S.diff(J,s,2)/4)
tau=S.symbols('tau')
phys=(c0+beta*tau)*S.exp(-3*tau)+c1*S.exp(-S.Rational(9,2)*tau)+c2*S.exp(-S.Rational(13,2)*tau)
exact('physical_time_dictionary',J.subs({t:0,s:S.I*tau})-phys)
exact('physical_time_first_derivative',S.diff(phys,tau).subs(tau,0))
small=c0+S.Rational(23,32)*c1-S.Rational(17,32)*c2
large=S.Rational(1,672)-(-c0+c1+c2)
exact('multiplier_small_region_bound',small-S.Rational(575,1752192))
exact('multiplier_large_region_bound',large-S.Rational(10291,21464352))
assert large>small>0
rows.append({'id':'uniform_bound_order','status':'exact_rational_inequality','small':str(small),'large':str(large)})
z=S.Function('Z')
shifted=c0*z(s+3)-beta*S.diff(z(s+3),s)+c1*z(s+S.Rational(9,2))+c2*z(s+S.Rational(13,2))
f=S.Function('f')
for energy in [S.Integer(3),S.Rational(9,2),S.Rational(13,2)]:
    exact(f'root_correspondence_{energy}',(-u*u/2+r*r/2-energy).subs(u*u,r*r-2*energy))
    spatial={S.Symbol('x'):-1/(2*u),S.Symbol('y'):3*u,S.Symbol('w'):26*u*u}
    x,y,w=spatial
    F1=(1+x*y)**3*w+y*y*(1+x*y)*(4+3*x*y)
    exact(f'original_target_shift_{energy}',(F1.subs(spatial,simultaneous=True)+r*r-2*energy).subs(u*u,r*r-2*energy))
fu=z(-u*u/2)
exact('derivative_channel_on_cover',S.diff(fu,u)/u+S.Subs(S.diff(z(s),s),s,-u*u/2))
g=shifted.subs(s,-r*r/2)
exact('full_transformed_root_generator',-S.diff(g,r,2)/(4*r*r)+S.diff(g,r)/(4*r**3)+S.diff(shifted,s,2).subs(s,-r*r/2)/4)

proofs=[]
for name in ('xi4_spectral_packet.tex','xi4_arithmetic_transport.tex','xi4_spatial_transport.tex','xi4_source_proof.tex'):
    p=ROOT/'tex'/name
    if p.exists(): proofs.append({'path':f'tex/{name}','sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
receipt={'status':'pass','check_count':len(rows),'checks':rows,'proofs':proofs,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact coefficient, matrix, multiplier-bound constants, and chain-rule identities; all analytic claims proved in TeX.','counterexample_established':False}
(ROOT/'checks/xi4_transport_checks.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps({'status':'pass','check_count':len(rows)}))
