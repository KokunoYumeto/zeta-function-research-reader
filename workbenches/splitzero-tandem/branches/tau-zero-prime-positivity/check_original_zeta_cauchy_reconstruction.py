"""Exact independent Laurent-residue checks for OZK7, OZK11, OZK16, OZK17.

These checks concern rational identities. They do not certify any zeta zero
location, numerical trace, or positivity assertion.
"""
from pathlib import Path
import hashlib
import json
import sympy as sp

s, h, sigma, x = sp.symbols('s h sigma x')
records = []


def check(name, difference):
    value = sp.cancel(difference)
    assert value == 0, (name, value)
    records.append(name)


for m in range(1, 4):
    pole = sp.Integer(2*m+1)
    a = -2*m
    for j in range(4):
        for k in range(4):
            A = (1-s-pole)**(-j-1)*(s-pole)**(-k-1)
            direct = sp.residue(A/(s-a), s, a)
            formula = (-1)**(j+k)*sp.binomial(j+k+1, j+1)/sp.Integer(4*m+1)**(j+k+2)
            check(f'resonant_constant_m{m}_j{j}_k{k}', direct-formula)

# Compute the complete original signed-divisor trace for a meromorphic
# rational model. Its local units are nonconstant, and the test pole collides
# with its first zero. Direct divisor evaluation uses Laurent constant terms.
f = (s+2)*(s-sp.Rational(1, 3))**2/(s-1)
logderivative = sp.cancel(sp.diff(f, s)/f)
divisor = [(-2, 1), (sp.Rational(1, 3), 2), (1, -1)]
for j in range(3):
    for k in range(3):
        A = (1-s-3)**(-j-1)*(s-3)**(-k-1)
        direct = sum(n*sp.residue(A/(s-a), s, a) for a, n in divisor)
        formula = -sum(sp.residue(A*logderivative, s, a) for a in [-2, 3])
        formula += sp.residue(A/(s+2), s, -2)
        check(f'full_signed_divisor_with_unit_j{j}_k{k}', direct-formula)

Ajk = lambda j,k: (1-x-sigma)**(-j-1)*(x-sigma)**(-k-1)
check('antisymmetric_entry', Ajk(0,1)-Ajk(1,0)-(1-2*x)/((1-x-sigma)**2*(x-sigma)**2))

# Local regular-unit residue identity with arbitrary symbolic coefficients.
aa = sp.symbols('a0:5')
bb = sp.symbols('b0:4')
n = sp.symbols('n', integer=True)
A = sum(aa[i]*h**(i-4) for i in range(5))
logf = n/h + sum(bb[i]*h**i for i in range(4))
check('local_full_unit_residue', sp.residue(A*logf,h,0) - n*aa[4] - sum(aa[3-i]*bb[i] for i in range(4)))

source = Path(__file__).with_name('ORIGINAL_ZETA_CAUCHY_RECONSTRUCTION.md')
result = {
    'proof_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'exact_checks': len(records),
    'checks': records,
    'scope': 'Exact rational and Laurent-residue identities only; no numerical zero or positivity certification.'
}
Path(__file__).with_name('ORIGINAL_ZETA_CAUCHY_EXACT_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'exact_checks': len(records), 'proof_sha256': result['proof_sha256']}))
