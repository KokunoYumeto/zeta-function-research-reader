"""Exact symbolic checks for ISP1--ISP53; finite algebra examples are not zeta zeros."""

import json
from pathlib import Path
import sympy as sp

checks = []


def check(name, actual, expected):
    difference = actual - expected
    if isinstance(difference, sp.MatrixBase):
        ok = all(sp.simplify(entry) == 0 for entry in difference)
    else:
        ok = sp.simplify(difference) == 0
    if not ok:
        raise AssertionError((name, difference))
    checks.append(name)


a, b, t, zeta = sp.symbols('a b t zeta', positive=True)
N = sp.Matrix([[0, 0, 0], [b, 0, 0], [0, 0, 0]])
P = sp.diag(1, 1, 0)
K = sp.Matrix([[0, a/(2*b), 0], [0, 0, 0], [0, 0, 0]])
W = sp.I*(N-N.conjugate().T)
check('nilpotent square', N*N, sp.zeros(3))
check('isolated determinant', (sp.eye(3)-t*N).det(), 1)
check('current square', W*W, b*b*P)
check('current positive eigenvector', W*sp.Matrix([1, sp.I, 0]), b*sp.Matrix([1, sp.I, 0]))
check('current negative eigenvector', W*sp.Matrix([1, -sp.I, 0]), -b*sp.Matrix([1, -sp.I, 0]))
check('trivialization commutator', K*N-N*K, a*sp.diag(1, -1, 0)/2)

c11, c22, c33, c12, c13, c23 = sp.symbols('c11 c22 c33 c12 c13 c23', real=True)
C = sp.Matrix([[c11, c12, c13], [c12, c22, c23], [c13, c23, c33]])
T = sp.eye(3)+t*K
Tinv = sp.eye(3)-t*K
M = C+N+a*t*sp.diag(1, 0, 0)
first = (Tinv*M*T).applyfunc(lambda x: sp.expand(x).coeff(t, 0)+t*sp.expand(x).coeff(t, 1))
check('full C first order with mixed H couplings', first, C+N+t*(C*K-K*C+a*P/2))
H = zeta*sp.eye(3)-C-N
check('full characteristic polynomial perturbation', (zeta*sp.eye(3)-M).det(), H.det()-a*t*H.adjugate()[0, 0])
check('nonzero characteristic derivative leading coefficient', sp.Poly(a*H.adjugate()[0, 0], zeta).LC(), a)

m = sp.symbols('m', positive=True)
I = sp.sqrt(b/m)*sp.Matrix([[1, 0], [0, -sp.I], [0, 0], [0, 0]])
B = m*sp.Matrix([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
check('exact current to packet isometry', I.conjugate().T*B*I, W[:2, :2])
Npacket = sp.zeros(4)
Npacket[1, 0] = -sp.I*b
check('packet nilpotent intertwining', Npacket*I, I*N[:2, :2])

s = sp.symbols('s')
alpha = [sp.Rational(3, 4)+3*sp.I, sp.Rational(1, 4)+3*sp.I,
         sp.Rational(3, 4)-3*sp.I, sp.Rational(1, 4)-3*sp.I]
h = sp.prod((s-x)**2 for x in alpha).expand()
q = 2+3*s-sp.I*s**3+sp.Rational(7, 3)*s**7
qrect = sp.expand(q-h*((1-s)*q.subs(s, 0)/h.subs(s, 0)+s*q.subs(s, 1)/h.subs(s, 1)))
check('endpoint zero', qrect.subs(s, 0), 0)
check('endpoint one', qrect.subs(s, 1), 0)
check('all quartet jets preserved by remainder', sp.rem(qrect-q, h, s), 0)
for i, root in enumerate(alpha):
    for derivative in range(2):
        check(f'quartet {i} derivative {derivative}', sp.diff(qrect-q, s, derivative).subs(s, root), 0)

bK = s**3*(s-1)**3
inverse_bK = sp.invert(bK, h, s)
qK = bK*sp.rem(inverse_bK*q, h, s)
check('arbitrary endpoint order section', sp.rem(qK-q, h, s), 0)
for endpoint in (0, 1):
    for derivative in range(3):
        check(f'endpoint {endpoint} derivative {derivative}', sp.diff(qK, s, derivative).subs(s, endpoint), 0)

# A singular support block with its entire kernel retained.
D = sp.diag(2, 0, 3)
Dplus = sp.diag(sp.Rational(1, 2), 0, sp.Rational(1, 3))
A = sp.Matrix([[1, 0, sp.I], [2, 0, 3]])
H2 = sp.Matrix([[4, 1+sp.I], [1-sp.I, 8]])
R = sp.eye(5)
R[2:5, 0:2] = Dplus*A.conjugate().T
Q = H2.row_join(A).col_join(A.conjugate().T.row_join(D))
S = sp.diag(H2-A*Dplus*A.conjugate().T, D)
check('singular support square completion', Q, R.conjugate().T*S*R)

lam = sp.symbols('lambda', real=True)
Fplane = sp.Matrix([[lam, 0], [b, 0]])
Tplane = sp.Matrix([[1, lam], [0, b]])
Mregular = sp.Matrix([[0, 0], [1, lam]])
Gtrace = sp.Matrix([[2, lam], [lam, lam**2]])
Ghs = sp.Matrix([[2, lam], [lam, lam**2+b**2]])
Qtrace = sp.Matrix([[2, -lam/b], [-lam/b, lam**2/b**2]])
check('observed regular module isomorphism', Fplane*Tplane, Tplane*Mregular)
check('original vector metric pullback', Tplane.conjugate().T*Tplane, sp.Matrix([[1, lam], [lam, lam**2+b**2]]))
Fbasis = [sp.eye(2), Fplane]
check('matrix Hilbert Schmidt metric pullback', sp.Matrix([[sp.trace(X.conjugate().T*Y) for Y in Fbasis] for X in Fbasis]), Ghs)
check('positive retained infinitesimal square', Ghs-Gtrace, sp.diag(0, b**2))
check('exact observed adjoint defect', Fplane-Fplane.conjugate().T, -sp.I*W[:2, :2])
check('Hilbert Schmidt multiplication adjoint defect', Ghs*Mregular-Mregular.conjugate().T*Ghs, sp.Matrix([[0, -b**2], [b**2, 0]]))
check('trace metric transported to original plane', Tplane.inv().conjugate().T*Gtrace*Tplane.inv(), Qtrace)
check('selfadjointness in transported trace form', Qtrace*Fplane, Fplane.conjugate().T*Qtrace)

result = {'status': 'passed', 'exact_checks': len(checks), 'checks': checks,
          'scope': 'Finite symbolic identities; sampled quartet points are not asserted zeta zeros.'}
target = Path(__file__).with_name('INFINITESIMAL_SUPPORT_POSITIVITY_CHECKS.json')
target.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(json.dumps(result, indent=2))
