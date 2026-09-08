"""Exact scale/residual arithmetic for the sourced dissipative layer programme.

This checks finite identities, not the source's analytic infinite-layer theorem.
The auxiliary q below is precisely sqrt(2*alpha/7), not a change of physical units.
No network, Lean, or sibling workspace is needed.
"""
from pathlib import Path
import argparse
import hashlib
import json
import sympy as S

ROOT = Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--source-root',type=Path,default=None,
                    help='Optional directory containing the two retrieved primary source files; rehash and compare them.')
args=parser.parse_args()
q, r, delta = S.symbols('q r delta', positive=True)
alpha = 7*q**2/2
a = q
R = 2/(7*q)
s = (2+3*alpha-14*q)/4
ell = 1+alpha-s-2*a
d = s-r
checks = []

def eq(name, left, right=0):
    residual = S.factor(left-right)
    ok = residual == 0
    checks.append({'name': name, 'left': str(left), 'right': str(right),
                   'residual': str(residual), 'passed': ok})
    if not ok:
        raise AssertionError((name, residual))

eq('a_squared', a*a, 2*alpha/7)
eq('a_equals_alpha_R', a, alpha*R)
eq('reciprocal_R', 1/R, 7*a/2)
eq('ell_alternative', ell, (2+alpha)/4+3*a/2)
eq('outer_support_margin', ell-a-1/R-s, (a-alpha)/2)
eq('local_symbol_separation_margin', 3*ell-1-2/R, s+a)
eq('optimized_outer_exponent', a+r+1+2/R-3*ell, r-s)
eq('self_cost_balance', 2*a+ell-1-alpha, -s)
eq('quadratic_cutoff_polynomial', (2+3*alpha)**2-56*alpha,
   9*alpha**2-44*alpha+4)
alpha0 = (22-8*S.sqrt(7))/9
eq('cutoff_root', 9*alpha0**2-44*alpha0+4)
z = S.symbols('z', real=True)
eq('cutoff_factorization', 9*z**2-44*z+4,
   9*(z-alpha0)*(z-(22+8*S.sqrt(7))/9))
eq('self_integrated_exponent', 2*a+ell+r+S.Rational(2,5)*d-1+2*delta-alpha,
   -S.Rational(3,5)*d+2*delta)
eq('inner_integrated_exponent', r+S.Rational(2,5)*d+2*delta+a-ell+1/R,
   -S.Rational(3,5)*d-(a-alpha)/2+2*delta)
eq('outer_integrated_exponent', a+r+1+2/R-(3-delta)*ell,
   -d+ell*delta)
E1 = S.Rational(2,5)*d+a+ell+alpha+(r-1)*(1-delta)
E2 = S.Rational(2,5)*d+2*a+alpha+r+s+2/R-2*ell
eq('diffusion_pointwise_first', E1,
   2*alpha-a-S.Rational(3,5)*d+(1-r)*delta)
eq('diffusion_pointwise_second', E2, 2*alpha-a-S.Rational(3,5)*d)
eq('diffusion_integrated_first', E1-alpha,
   alpha-a-S.Rational(3,5)*d+(1-r)*delta)
eq('diffusion_integrated_second', E2-alpha,
   alpha-a-S.Rational(3,5)*d)
eq('switch_seed_exponent', S.Rational(2,5)*d-a+a+r-s, -S.Rational(3,5)*d)
eq('self_uniform_margin', -S.Rational(3,5)*d+2*d/12, -S.Rational(13,30)*d)
eq('outer_uniform_margin', -d+S.Rational(5,6)*d/12, -S.Rational(67,72)*d)

# A full finite-mode residual, retaining the sign of damping and viscosity.
x1,x2,x3,t,nu,sigma,k,g = S.symbols('x1 x2 x3 t nu sigma k g', real=True)
x = S.Matrix([x1,x2,x3])
U = S.Matrix([sigma*x1,-sigma*x2,0])
w = S.Matrix([S.exp((sigma-g)*t)*S.sin(k*x3),0,0])
transport = w.diff(t)+w.jacobian(x)*U-U.jacobian(x)*w
for j in range(3):
    eq(f'finite_mode_forward_damping_component_{j+1}',transport[j],-g*w[j])
lap_w = S.Matrix([sum(S.diff(wi,xj,2) for xj in x) for wi in w])
for j in range(3):
    eq(f'finite_mode_viscous_residual_component_{j+1}',
       transport[j]-nu*lap_w[j], (nu*k**2-g)*w[j])
rho = S.symbols('rho', real=True)
eq('switch_coefficient_maximum_identity', rho*(1-rho),
   S.Rational(1,4)-(rho-S.Rational(1,2))**2)

witness_sub = {q:S.Rational(1,7),r:S.Rational(3,112),delta:S.Rational(1,448)}
witness = {key:S.factor(value.subs(witness_sub)) for key,value in {
    'alpha':alpha,'R':R,'a':a,'s':s,'ell':ell,'r':r,'d':d,'nu':d/200,
    'delta':delta,'switch_exponent':-S.Rational(3,5)*d,
    'self_exponent':-S.Rational(3,5)*d+2*delta,
    'inner_exponent':-S.Rational(3,5)*d-(a-alpha)/2+2*delta,
    'outer_exponent':-d+ell*delta,
    'diffusion_first_exponent':E1-alpha,
    'diffusion_second_exponent':E2-alpha,
}.items()}
for key, value in witness.items():
    if key.endswith('_exponent'):
        assert value < 0, (key, value)
for name, bound in {'d_over_12':d/12,'diffusion_margin':(a-alpha)/4,
                    'frequency_margin':(1-1/R)/2,'absolute_margin':S.Rational(1,10)}.items():
    margin = S.factor((bound-delta).subs(witness_sub))
    assert margin >= 0, (name,margin)
    checks.append({'name':'witness_delta_bound_'+name,'margin':str(margin),'passed':True})

classical = {'alpha':'2','R':str(1/S.sqrt(7)),
             'a':str(2/S.sqrt(7)), 's':str(2-S.sqrt(7)),
             'diffusion_margin_alpha_minus_a':str(2-2/S.sqrt(7)),
             'increasing_frequencies':False, 'positive_s':False,
             'negative_diffusion_margin':False}
proof = ROOT/'tex/forced_program_scaling.tex'
sources=json.loads((ROOT/'sources/forced_program_source_hashes.json').read_text(encoding='utf-8'))
if args.source_root is not None:
    for entry in sources:
        path=args.source_root/entry['file']
        actual=hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != entry['sha256']:
            raise AssertionError(('primary source hash mismatch',str(path),actual,entry['sha256']))
result = {'schema':'forced-layer-scale-audit/v1','all_passed':True,
          'claim_scope':'Exact finite algebra and sign checks; no validation of the full source blow-up theorem or classical Navier-Stokes disproof.',
          'symbol_dictionary':{'q':'sqrt(2*alpha/7)','alpha':'7*q**2/2',
                               'M_n':'N**(R**n)','A_n':'M_n**a','L_n':'M_n**ell',
                               'nu':'(s-r)/200 is the physical viscosity'},
          'checks':checks,'rational_witness':{k:str(v) for k,v in witness.items()},
          'classical_endpoint':classical,'source_hashes':sources,
          'sources_rehashed':args.source_root is not None,
          'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest()}
out=ROOT/'checks/forced_program_scaling_checks.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'{len(checks)} exact checks passed; all six witness exponents are negative.')
print(out)
