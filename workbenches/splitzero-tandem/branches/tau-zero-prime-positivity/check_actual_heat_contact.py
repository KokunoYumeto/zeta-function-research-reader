from pathlib import Path
import sympy as S
import json
O=Path(__file__).resolve().parent
x,t,w,b,c=S.symbols('x t w b c')
checks=[]
def check(name,expr):
    assert S.cancel(expr)==0,(name,expr)
    checks.append(name)
# Independent finite heat evolution, retaining the original 1/4.
for m in range(1,7):
    p=x**m*(1+2*x+3*x**2+x**3)
    heat=sum(t**j*S.diff(p,x,2*j)/(4**j*S.factorial(j)) for j in range(S.degree(p,x)//2+1))
    check(f'heat_equation_m{m}',S.diff(heat,t)-S.diff(heat,x,2)/4)
    L=S.diff(heat,x)/heat
    B1=(S.diff(L,x,2)+2*L*S.diff(L,x))/4
    check(f'first_logarithmic_derivative_m{m}',S.diff(L,t)-B1)
    J=S.diff(L,t).subs(t,0)
    H=5+7*x+11*x**2+13*x**3
    actual=S.residue(H*J/x**0,x,0)
    check(f'full_simple_pole_m{m}',actual+S.Rational(m*(m-1),4)*22+S.Rational(m,2)*2*7)
    for power in [3,2]:
        expected=-S.Rational(m*(m-1),2)*5 if power==3 else -S.Rational(m*(m-1),2)*7-S.Rational(m,2)*2*5
        check(f'weighted_pole_order{power}_m{m}',S.residue(x**(power-1)*H*J,x,0)-expected)
    contact=S.Rational(m*(m-1),2)*(5/x**3+7/x**2+11/x)
    residual=-S.Rational(m,2)*2*(5/x**2+7/x)
    for power in [1,2,3]:
        check(f'contact_cancel_order{power}_m{m}',S.residue(x**(power-1)*(H*J+contact-residual),x,0))
# A finite local model checks the higher motion order without assuming first velocity.
p=x+x**4
heat=p+t*S.diff(p,x,2)/4+t**2*S.diff(p,x,4)/32
check('stationary_simple_first_order',S.diff(heat,t).subs({x:0,t:0}))
check('stationary_simple_second_motion',heat.subs(x,-3*t**2/4).expand().coeff(t,2))
L=S.diff(heat,x)/heat
check('second_motion_resolvent_double_pole',S.residue(x*S.diff(L,t,2).subs(t,0),x,0)+S.Rational(3,2))
report={'status':'passed','exact_checks':len(checks),'checks':checks,'scope':'Independent exact finite polynomial heat evolutions, weighted principal parts, complete contact cancellation, and a stationary-first-order local model. These checks do not prove convergence or RH; the complete analytic proofs are GC, CH, and RT.'}
(O/'ACTUAL_HEAT_CONTACT_CHECKS.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({'status':report['status'],'exact_checks':len(checks)}))
