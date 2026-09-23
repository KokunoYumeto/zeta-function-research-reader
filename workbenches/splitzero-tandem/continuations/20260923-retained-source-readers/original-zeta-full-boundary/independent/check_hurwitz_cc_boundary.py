"""Supplementary exact and high precision checks for HCB; not a proof substitute."""
import json
from pathlib import Path
import mpmath as mp
import sympy as sp

mp.mp.dps = 110
checks = []

def accept(name, error, tolerance=mp.mpf('1e-55')):
    error = abs(mp.mpf(error))
    if error > tolerance:
        raise AssertionError((name, str(error), str(tolerance)))
    checks.append({'name': name, 'absolute_error': str(error), 'tolerance': str(tolerance)})

x = sp.symbols('x')
g_symbol = (2*sp.pi**2*x**4-3*sp.pi*x**2)*sp.exp(-sp.pi*x**2)
for m in range(1, 9):
    actual = sp.expand(sp.series(g_symbol, x, 0, 2*m+1).removeO()).coeff(x,2*m)
    asserted = (-1)**m*sp.pi**m*(2*m+1)/sp.factorial(m-1)
    assert sp.simplify(actual-asserted) == 0
    checks.append({'name': f'exact_original_Taylor_coefficient_{m}', 'exact': True})

# Test the exact periodic-Bernoulli remainder against a different function
# whose shifted series is known in closed form; this checks sign and scaling.
for a_string in ['0.3', '1', '2.7']:
    a = mp.mpf(a_string)
    h = mp.mpf('0.4')
    q = int(mp.ceil(a))-1
    alpha = a-q
    J = 4
    direct = mp.exp(-a*h)/(1-mp.exp(-h))
    main = 1/h-mp.fsum(mp.bernpoly(j,a)/mp.factorial(j)*h**(j-1)*(-1)**(j-1)
                          for j in range(1,J+1))
    periodic = h*mp.quad(lambda u: mp.bernpoly(J,u-alpha+1)*mp.exp(-h*u), [0,alpha])
    periodic += h*mp.exp(-h*alpha)/(1-mp.exp(-h))*mp.quad(
        lambda u: mp.bernpoly(J,u)*mp.exp(-h*u),[0,1])
    remainder = (-1)**(J+1)*h**(J-1)/mp.factorial(J)*periodic
    for n in range(q):
        z = (n+alpha)*h
        remainder -= mp.exp(-z)-mp.fsum((-z)**j/mp.factorial(j) for j in range(J))
    accept(f'exact_EM_remainder_exp_a_{a_string}', direct-main-remainder)

def g(v):
    return (2*mp.pi**2*v**4-3*mp.pi*v**2)*mp.exp(-mp.pi*v**2)

def psi(a,b,y):
    # Finite arithmetic sum with a tail far below the check tolerance.
    cutoff = max(1, int(mp.ceil(12*b/y-a))+1)
    return mp.fsum(g((n+a)*y/b) for n in range(cutoff))

def mellin(a,b,s):
    return b**s*mp.pi**(-s/2)*mp.zeta(s,a)*(
        mp.gamma(s/2+2)-mp.mpf('1.5')*mp.gamma(s/2+1))

for a in [mp.mpf('0.3'),mp.mpf('0.5'),mp.mpf('1'),mp.mpf('2.7')]:
    b = mp.mpf('1.3')
    eps = mp.mpf('1e-32')
    for m in range(1,5):
        residue = (-1)**(m+1)*mp.pi**m*mp.bernpoly(2*m+1,a)/(mp.factorial(m-1)*b**(2*m))
        estimate = (eps*mellin(a,b,-2*m+eps)-eps*mellin(a,b,-2*m-eps))/2
        accept(f'full_Mellin_residue_a_{a}_m_{m}',estimate-residue,mp.mpf('1e-52'))
    accept(f'full_Mellin_finite_value_zero_a_{a}',mellin(a,b,0)-(a/2-mp.mpf('0.25')))
    estimate = (mellin(a,b,1+eps)+mellin(a,b,1-eps))/2
    accept(f'full_Mellin_finite_value_one_a_{a}',estimate-b/4,mp.mpf('1e-42'))

for a in [mp.mpf('0.3'),mp.mpf(1)/3,mp.mpf(1)/4,mp.mpf(1)/6]:
    b = mp.mpf('1.3')
    y = mp.mpf('0.7')
    reflected = psi(a,b,y)+psi(1-a,b,y)
    poiss = 2*b/y*mp.fsum(mp.cos(2*mp.pi*k*a)*g(k*b/y) for k in range(1,20))
    accept(f'reflected_Poisson_a_{a}',reflected-poiss)

for y in [mp.mpf('0.3'),mp.mpf('1.1'),mp.mpf('3')]:
    b = mp.mpf('0.9')
    f = lambda scale: psi(mp.mpf(1),scale,y)
    accept(f'actual_V_pair_thirds_y_{y}',psi(mp.mpf(1)/3,b,y)+psi(mp.mpf(2)/3,b,y)-f(3*b)+f(b))
    accept(f'actual_V_pair_fourths_y_{y}',psi(mp.mpf(1)/4,b,y)+psi(mp.mpf(3)/4,b,y)-f(4*b)+f(2*b))
    accept(f'actual_V_pair_sixths_y_{y}',psi(mp.mpf(1)/6,b,y)+psi(mp.mpf(5)/6,b,y)-f(6*b)+f(3*b)+f(2*b)-f(b))

result = {'status':'passed','count':len(checks),'working_decimal_precision':mp.mp.dps,
          'scope':'Finite exact and numerical checks supplement HCB proofs; no RH inference.',
          'checks':checks}
out = Path(__file__).with_name('HURWITZ_CC_BOUNDARY_CHECK.json')
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','count':len(checks),'output':str(out)}))
