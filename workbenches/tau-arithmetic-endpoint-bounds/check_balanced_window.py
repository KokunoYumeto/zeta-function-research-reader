"""Finite exact regression of the balanced-window algebra; not analytic proof."""
import argparse, fractions, importlib.util, json, math, pathlib

BASE=pathlib.Path(__file__).resolve().parent
checks=0
def ck(test,label):
    global checks
    checks+=1
    if not test: raise AssertionError(label)
parser=argparse.ArgumentParser()
parser.add_argument('--fail-control',action='store_true')
args=parser.parse_args()
if args.fail_control: ck(False,'intentional balanced-window control failure')
Q=fractions.Fraction
for n in range(3,61):
    ell=Q(2*n**(2*n+1),2*n+1)*Q(2**n,math.comb(2*n,n))**2
    ck(ell>=Q(2*n**(2*n+1),(2*n+1)*4**n),'Legendre lower factor')
    ck((2*n)**3<=6**n,'polynomial-factor power inequality')
    for r in range((n+1)//2,n+1):
        # This root-free identity includes the 2 from the sum of moments.
        raw=Q(2*(4*n)**(2*(n+r))*(2*n+1)*4**n,2*n**(2*n+1))
        reduced=Q((4*n)**(2*r)*8**(2*n)*(2*n+1),n)
        ck(raw==reduced,'root-free degree cancellation')
        ck(reduced<=3*(256*n)**(2*r),'uniform combinatorial factor')
        ck(2*math.factorial(2*(n+r))/ell<=reduced,'factorial replacement')
        ck(Q(n+r,r)<=3,'Laplace exponent')
        for k in (3,n):
            ck(Q(k,2*r)<=1,'mass exponent')
            ck(Q(k-3,2*r)<=1,'compact-mass exponent')
            ck(Q(n+k-3,4*r)<=1,'gamma exponent')
            ck(1+n+k-3<=2*n,'polynomial base')
for k in range(3,61):
    for m in (1,2,7):
        q=(1+k*(m-1))*(k+1)**2
        r=q-1
        ck(q>=k and 2*r>=q and r<=q,'near-diagonal admissibility')
        # Delta=1 here; exact dimension cancels the multiplicity factor.
        L=2*(1+k*(m-1))*(k+1)*((k+1)**2//4)
        ck(Q(L,q)>=Q(k,2),'quartet trace lower factor')
for q in range(3,30):
    V={j:Q(1,(j+2)**3) for j in (q-1,q,2*q-1,2*q)}
    ratio=V[q-1]*V[q]/(V[2*q-1]*V[2*q])
    central=V[q]/V[2*q-1]
    ck(ratio==central**2*(V[q-1]/V[q])*(V[2*q-1]/V[2*q]),'four-volume exact overlap')
    ck(ratio>=central**2,'four-volume monotonicity')
source_checker=BASE/'check_endpoint_bounds.py'
if not source_checker.exists(): source_checker=BASE/'source_stage'/'Tau_Arithmetic_Endpoint_Bounds'/'check_endpoint_bounds.py'
spec=importlib.util.spec_from_file_location('supplied_endpoint',source_checker)
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
for n,k,r in [(3,3,2),(3,3,3),(4,3,2),(4,4,3),(4,4,4)]:
    _,norms=module.orthogonal(n+r,k)
    # On w=e^-|t| the actual third convolution >=(3/2)e^-|u|,
    # vartheta=2(1-e^-1)>1; e<3 weakens this to a rational bound.
    lower=Q(3,2)*Q(1,3)**(n+k-3)*module.norm_legendre(n,module.sp.Integer(n))
    upper=math.factorial(2*(n+r))*2**(2*(n+r))*2*module.sp.Rational(8,3)**k
    ck(bool(norms[n]>=lower),'unnormalized Laplace lower fixture')
    ck(bool(norms[n+r]<=upper),'unnormalized Laplace upper fixture')
    ck(bool(norms[n+r]/norms[n]<=upper/lower),'balanced Laplace ratio fixture')
print(json.dumps({'status':'PASS','checks':checks,'scope':'Finite exact algebraic regressions only; no analytic or Lean certificate'},sort_keys=True))
