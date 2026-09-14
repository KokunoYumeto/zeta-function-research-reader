"""Independent exact algebra check of the formal-boundary coefficient formula.

This rational polynomial is a test of the proved identities, not a substitute
for the actual packet polynomial or evidence of an RH conclusion.
"""
import json
from pathlib import Path
import sympy as sp

s, y, u = sp.symbols('s y u')
h = s**2 * (s + 1)
phase = sp.integrate(h, s)
d = sp.degree(h, s)
order = 4
C = sp.zeros(d)
B = sp.zeros(d)
for b in range(d):
    quotient, remainder = sp.div(phase * s**b, h, s)
    for a in range(d):
        C[a, b] = sp.expand(remainder).coeff(s, a)
        B[a, b] = sp.expand(sp.diff(quotient, s)).coeff(s, a)
G = -C / u**2 + B / u
rows = []
residues = []
critical_values = []
for rho, multiplicity in [(sp.Integer(0), 2), (sp.Integer(-1), 1)]:
    N = multiplicity + 1
    c = phase.subs(s, rho)
    aphase = sp.cancel(N * (phase.subs(s, rho + y) - c) / y**N)
    assert aphase.subs(y, 0) == 1  # The retained test branches are b_rho=1.
    for a in range(multiplicity):
        row = []
        for b in range(d):
            value = sp.Integer(0)
            for q in range(order + 1):
                j = a + q * N
                coefficient = sp.series(
                    (rho + y)**b * aphase**(-sp.Rational(j + 1, N)),
                    y, 0, j + 1
                ).removeO().expand().coeff(y, j)
                multiplier = sp.prod(a + 1 + ell * N for ell in range(q))
                value += (-u)**q * multiplier * coefficient
            row.append(value)
        rows.append(row)
        residues.append(sp.Rational(a + 1, N))
        critical_values.append(c)
T = sp.Matrix(rows)
D = sp.diag(*[-c/u**2 + beta/u for c, beta in zip(critical_values, residues)])
def trunc(expression, top):
    return sp.series(sp.expand(expression), u, 0, top).removeO().expand()

defect = T.diff(u) + D*T - T*G
for value in defect:
    assert trunc(value, order - 1) == 0, value
assert trunc(T.det(), order + 1) == 1
assert sp.trace(G) == sp.trace(D)
receipt = {
    'scope': 'Exact rational test polynomial h=s^2(s+1); not an actual RH packet',
    'T_series_order': order,
    'T0': [[str(v) for v in row] for row in T.subs(u, 0).tolist()],
    'jacobian_weighted_CRT_determinant': '1',
    'connection_identity_checked_laurent_powers': [-2, -1, 0, 1, 2],
    'determinant_identity_checked_powers': [0, 1, 2, 3, 4],
    'trace_identity': True,
    'status': 'PASS',
}
destination = Path(__file__).with_name('review_exact_check.json')
destination.write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
print(json.dumps(receipt))
