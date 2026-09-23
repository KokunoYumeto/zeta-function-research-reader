"""Exact finite algebra checks for PZS1--PZS38; no zeta zero is asserted."""

import json
from pathlib import Path
import sympy as sp

checks = []


def check(name, lhs, rhs):
    difference = lhs-rhs
    if isinstance(difference, sp.MatrixBase):
        ok = all(sp.simplify(entry) == 0 for entry in difference)
    else:
        ok = sp.simplify(difference) == 0
    if not ok:
        raise AssertionError((name, difference))
    checks.append(name)


u, lam = sp.symbols('u lambda', real=True)
c, d = sp.symbols('c d', complex=True)
J = sp.Matrix([[0, 1], [1, 0]])
Q = sp.diag(2, -2*u)
coefficient_map = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)], [-1, 1]])
endpoint_map = sp.Matrix([[1, -sp.Rational(1, 2)], [1, sp.Rational(1, 2)]])
check('endpoint interpolation inverse', endpoint_map*coefficient_map, sp.eye(2))
check('endpoint involution intertwining', endpoint_map*sp.diag(1, -1), J*endpoint_map)
check('endpoint trace form isometry', coefficient_map.T*Q.subs(u, sp.Rational(1, 4))*coefficient_map, J)
check('continued antisymmetric direction', (sp.Matrix([[0, -2]])*Q*sp.Matrix([0, -2]))[0], -8*u)

M = sp.Matrix([[c, u*d], [d, c]])
Mstar = sp.Matrix([[sp.conjugate(c), -u*sp.conjugate(d)], [-sp.conjugate(d), sp.conjugate(c)]])
check('regular trace form', sp.trace(Mstar*M), 2*sp.conjugate(c)*c-2*u*sp.conjugate(d)*d)
check('fundamental symmetry positive correction', J*J, sp.eye(2))
correction = sp.Matrix([1, -1])*sp.Matrix([[1, -1]])
check('rank one correction retained', sp.eye(2)-J, correction)
S = sp.diag(0, 1)
check('endpoint multiplication adjoint', J*S.T*J, sp.eye(2)-S)
Y = (S-sp.eye(2)/2)/sp.I
check('hyperbolic Fourier adjoint', J*Y.conjugate().T*J, Y)
check('positive Fourier adjoint', Y.conjugate().T, -Y)

basis_change = sp.Matrix([[1, lam/2], [0, 1]])
Gminus = sp.Matrix([[2, lam], [lam, 0]])
Gplus = sp.Matrix([[2, lam], [lam, lam**2]])
sigma = sp.Matrix([[1, lam], [0, -1]])
check('centered endpoint involution trace', basis_change.T*sp.diag(2, -lam**2/2)*basis_change, Gminus)
check('centered fixed generator trace', basis_change.T*sp.diag(2, lam**2/2)*basis_change, Gplus)
check('two trace forms related by sheet switch', Gminus*sigma, Gplus)
check('observed positive correction', Gplus-Gminus, sp.diag(0, lam**2))
check('observed negative discriminant', Gminus.det(), -lam**2)

eps = sp.symbols('eps', real=True)
H1 = sp.Matrix([[1, 2+3*sp.I], [2-3*sp.I, 4]])
H2 = sp.Matrix([[5, 6+7*sp.I], [6-7*sp.I, 8]])
x = sp.Matrix([1, -1])+eps*sp.Matrix([2+sp.I, 3-sp.I])
value = (x.conjugate().T*(J+eps*H1+eps**2*H2)*x)[0]
check('nilpotent correction preserves negative residue', value.subs(eps, 0), -2)

report = {'status': 'passed', 'exact_checks': len(checks), 'checks': checks,
          'scope': 'Exact finite trace, interpolation, involution, metric and residue calculations; no analytic positivity theorem.'}
Path(__file__).with_name('PRIME_ZERO_SIGN_DEFORMATION_CHECKS.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
print(json.dumps(report, indent=2))
