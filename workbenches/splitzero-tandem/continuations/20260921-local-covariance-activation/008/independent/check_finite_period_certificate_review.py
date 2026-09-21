"""Independent local-inverse and implementation audit of the finite period test."""
from pathlib import Path
import contextlib
import hashlib
import io
import json
from flint import arb, acb_mat

B = Path(__file__).resolve().parent.parent
script = B / 'certify_finite_period_zero.py'
raw = script.read_bytes()
expected = '041728c2ba636914c9c6dbbc294da396b7b1233b9967fb0b4af9cdb3baa8b2b8'
assert hashlib.sha256(raw).hexdigest() == expected
source = raw.decode('utf-8')
prefix, sep, _ = source.partition('atcenter=evaluate(center);onbox=evaluate(diskbox)')
assert sep
ns = {'__file__': str(script), '__name__': 'certificate_independent_review'}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(prefix, str(script), 'exec'), ns)
Rbox, _ = ns['matrix'](ns['diskbox'])
Rcenter, _ = ns['matrix'](ns['center'])
A = Rcenter.inv().mid()
identity = acb_mat([[1 if i == j else 0 for j in range(4)] for i in range(4)])
error = identity - A * Rbox
row_sums = [sum((error[i,j].abs_upper() for j in range(4)), arb(0)) for i in range(4)]
assert all(s < 1 for s in row_sums)
# A is a single exact dyadic matrix. The enclosed product error proves
# injectivity of every actual R(z) in the box by a Neumann series.
atcenter = ns['evaluate'](ns['center'])
onbox = ns['evaluate'](ns['diskbox'])
f0, fp0, _ = atcenter[0]
eps = f0.abs_upper()
m = fp0.abs_lower()
variation = (onbox[0][1]-fp0).abs_upper()
assert eps < arb('5e-63') and m > 434 and variation < 8
assert eps + variation * ns['radius'] < m * ns['radius']
assert onbox[0][2].imag > arb('3.68')
for j in range(1,4):
    assert onbox[j][0].abs_lower() > 0
alpha = onbox[0][1]
for j in range(1,4):
    alpha *= onbox[j][0]
assert alpha.abs_lower() > 1524
# An independent formal composition checks every coefficient of FPZ16.
import sympy as sp
t = sp.symbols('t')
m1, m2, m3 = sp.symbols('m1 m2 m3')
omega = -sp.I*t + sp.I*t**3/3
weighted = sp.series(sp.exp(-4*omega)*(m1*omega+m2*omega**2/2+m3*omega**3/6),t,0,4).removeO().expand()
desired = -sp.I*m1*t+(4*m1-m2/2)*t**2+sp.I*(m3/6-2*m2+sp.Rational(25,3)*m1)*t**3
assert sp.expand(weighted-desired) == 0
result = {
    'status': 'PASS',
    'reviewed_script_sha256': expected,
    'inverse_certificate': 'Exact dyadic A = midpoint of the centre inverse; every row sum of |I - A R(z)| is strictly below one throughout the full box.',
    'neumann_row_bounds': [x.str(40) for x in row_sums],
    'rouche_bounds': {'center_value_upper': '<5e-63', 'center_derivative_lower': '>434', 'derivative_variation_upper': '<8', 'radius': '1e-14'},
    'period_derivative_product_lower': '>1524',
    'weighted_coefficients_FPZ16': 'All coefficients through degree three verified by independent formal composition.',
    'scope': 'Geometric parameter family, delta=1/4 and gamma=3, with a nonzero real unit. No zeta-zero or arithmetic-unit assertion.',
}
out = B / 'independent' / 'FINITE_PERIOD_CERTIFICATE_REVIEW_CHECK.json'
out.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(json.dumps(result, indent=2))
