"""Independent exact algebra behind the Gaussian-translation review.

Scope: Gaussian derivatives, reflected coefficient signs and numerical tail
constants. No zeta-zero location or full Weil sign is certified.
"""
from pathlib import Path
import hashlib
import json
import sympy as sp

x, epsilon, u, B = sp.symbols('x epsilon u B', real=True)
R = sp.symbols('R', positive=True)
checks = []


def exact(name, expr):
    assert sp.simplify(expr) == 0, (name, expr)
    checks.append(name)


for l in range(9):
    gaussian = sp.exp(-x*x/(4*epsilon))
    derivative = sp.diff(gaussian, x, l)/gaussian
    polynomial = sp.factorial(l)/2**l * sum(
        (-1)**(l-j)*x**(l-2*j)/(epsilon**(l-j)*sp.factorial(j)*sp.factorial(l-2*j))
        for j in range(l//2+1)
    )
    exact(f'gaussian_derivative_order_{l}', derivative-polynomial)

for j in range(6):
    for k in range(6):
        direct = (-1)**j*(-R)**(j+k)/(sp.factorial(j)*sp.factorial(k))
        recorded = (-1)**k*R**(j+k)/(sp.factorial(j)*sp.factorial(k))
        exact(f'fixed_divisor_sign_{j}_{k}',direct-recorded)

exact('complete_gaussian_square', u/2-(u-B)**2/(8*epsilon)
      +(u-B-2*epsilon)**2/(8*epsilon)-B/2-epsilon/2)
exact('corrected_B2', sp.Rational(2)/(sp.Rational(1,8)*sp.E)
      +1/(2*sp.Rational(1,8))-(16/sp.E+4))
exact('B4',16/(sp.Rational(1,8)**2*sp.E**2)
      +6/(sp.Rational(1,8)**2*sp.E)+3/(4*sp.Rational(1,8)**2)
      -(1024/sp.E**2+384/sp.E+48))
exact('tail_prefactor',sp.Rational(64,59)*(sp.Rational(1,2)+sp.Rational(9,640))-sp.Rational(329,590))
exact('exponential_partial_sum',sum(sp.Rational(7,3)**k/sp.factorial(k) for k in range(7))-sp.Rational(1071641,104976))
assert sp.Rational(994009,9216)>46*sp.Rational(7,3)
checks.append('tail_exponent_strict_rational_bound')
assert sp.Rational(1071641,104976)>10
checks.append('log_ten_strict_rational_bound')
assert 2*503*sp.Rational(329,590)<600
checks.append('full_prime_tail_prefactor_below_600')

source=Path(__file__).with_name('ORIGINAL_ZETA_GAUSSIAN_TRANSLATION_RECONSTRUCTION.md')
review=Path(__file__).with_name('ORIGINAL_ZETA_GAUSSIAN_TRANSLATION_REVIEW.md')
result={
    'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
    'review_sha256':hashlib.sha256(review.read_bytes()).hexdigest(),
    'exact_checks':len(checks),
    'checks':checks,
    'scope':'Independent algebra and rational inequalities; no numerical zero or full positivity certification.'
}
Path(__file__).with_name('GAUSSIAN_TRANSLATION_REVIEW_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({key:result[key] for key in ['source_sha256','review_sha256','exact_checks']}))
