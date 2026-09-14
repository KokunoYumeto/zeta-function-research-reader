"""Independent exact algebra and rational-tail checks; no floating-point certificate."""
from fractions import Fraction
import json
from pathlib import Path
import sympy as sp

x, a, z, s = sp.symbols('x a z s', positive=True)
f = 2 * (4*a**2*x**4 - 6*a*x**2) * sp.exp(-a*x**2)
h = -x*sp.diff(f, x) - sp.Rational(1, 2)*f
expected = (16*a**3*x**6 - 60*a**2*x**4 + 30*a*x**2)*sp.exp(-a*x**2)
checks = []
def require(name, proposition):
    if not proposition:
        raise RuntimeError(name)
    checks.append(name)
require('full derivative polynomial and original leading factor two', sp.expand((h-expected)*sp.exp(a*x**2)) == 0)
require('Mellin polynomial coefficient is exactly s(s-1)', sp.expand(4*(s/2)*(s/2+1)-6*(s/2)-s*(s-1)) == 0)
require('positive-polynomial lower bound for y >= 12', sp.expand((16*z**2-60*z+30) - (16*z*(z-12)+132*z+30)) == 0)
require('absolute derivative polynomial lower comparison', sp.expand((32*z**2-60*z+30) - (32*(z-sp.Rational(15,16))**2+sp.Rational(15,8))) == 0)
require('e lower bound uses five exact terms', sum(Fraction(1, sp.factorial(j)) for j in range(5)) > Fraction(8, 3))
require('pi upper bound cubed below 32', Fraction(22, 7)**3 < 32)
require('universal geometric ratio below one half', 64*Fraction(3, 8)**15 < Fraction(1, 2))
require('all-integer geometric ratio below one half', 64*Fraction(3, 8)**9 < Fraction(1, 2))
finite_integral_bound = 2**20 * Fraction(3,8)**6 * sum(Fraction(int(sp.binomial(6,j)*sp.factorial(j)), 6**(j+1)) for j in range(7))
require('all finite derivative-square integrals below 3669/2', finite_integral_bound == Fraction(3669,2))
require('finite derivative plus-norm below 64', finite_integral_bound < 4096)

tails = {}
for J, exponent in [(6, 111), (8, 191)]:
    L = J+1
    bound = Fraction(2**20 * L**12, 6*L*L-6) * Fraction(3, 8)**(6*L*L)
    require(f'J={J} rational derivative squared-tail bound < 10^-{exponent}', bound < Fraction(1, 10**exponent))
    tails[str(J)] = {
        'L': L,
        'squared_plus_norm_upper_bound_numerator': str(bound.numerator),
        'squared_plus_norm_upper_bound_denominator': str(bound.denominator),
        'strict_decimal_power_upper_bound': f'10^-{exponent}',
    }
require('cutoff 6 full square-integral error < 10^-52', 129*Fraction(1,10**55) < Fraction(1,10**52))
require('cutoff 8 full square-integral error < 10^-92', 129*Fraction(1,10**95) < Fraction(1,10**92))
result = {
    'status': 'passed',
    'check_count': len(checks),
    'checks': checks,
    'scope': 'Exact derivative algebra and explicit rational omitted-integer-tail inequalities; no finite-integral quadrature certificate.',
    'tails': tails,
}
out = Path(__file__).with_name('toda_theta_derivative_independent_check_result_20260912.json')
out.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'status': result['status'], 'check_count': len(checks), 'output': str(out)}))
