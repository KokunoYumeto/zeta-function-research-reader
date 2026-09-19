"""Independent exact coefficient-algebra check of the original quartet connection.

The explicit connection is derived independently in the companion file. This
test reconstructs all multiplication operators in the unchanged polynomial
coefficient basis and checks the implicit-root and logarithmic-scale equations.
"""
from pathlib import Path
import importlib.util
import json
import sympy as s

base = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "quartet_connection", base / "independent/signed_frame_connection_expressions.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
delta, gamma, Omega = module.delta, module.gamma, module.Omega
i = s.I
A = -s.Rational(1, 2)
B = delta**2-gamma**2-s.Rational(3, 4)
C = gamma**2-delta**2+s.Rational(1, 4)
D = -s.Rational(1, 32)-(gamma**2-delta**2)/4-(delta**2+gamma**2)**2/2
Id = s.eye(4)
Comp = s.Matrix([[0,0,0,-D/A],[1,0,0,-C/A],
                 [0,1,0,-B/A],[0,0,1,-1/A]])
F = 4*A*Comp**3+3*Comp**2+2*B*Comp+C*Id
Hsecond = 12*A*Comp**2+6*Comp+2*B*Id
J = s.Matrix([[0,0,0,0],[1,0,0,0],[0,2,0,0],[0,0,3,0]])
V = s.Matrix([
 [1,0,0,0],
 [-i*C,-2*i*B,-3*i,-4*i*A],
 [A*C**2-9*D,4*A*B*C-8*A*D-7*C,
  -16*A**2*D+4*A*B**2-2*A*C-5*B,-8*A**2*C+4*A*B-3],
 [-13*i*C**2+20*i*D/A,-52*i*B*C+76*i*D+20*i*C/A,
  208*i*A*D-52*i*B**2+5*i*C+20*i*B/A,
  104*i*A*C-66*i*B+20*i/A]])

def zero(expr):
    num = s.together(expr).as_numer_denom()[0]
    return s.Poly(s.expand(num), delta, gamma, extension=i).is_zero

def check_matrix(matrix, label):
    assert all(zero(entry) for entry in matrix), label
    print(label + ': passed', flush=True)

# Exact interpolation of root velocity epsilon on all four labelled roots.
X = Comp-s.Rational(1,2)*Id
Rvelocity = -(X**3+(gamma**2-3*delta**2)*X)/(2*delta*(delta**2+gamma**2))
hdot = s.diff(B,delta)*Comp**2+s.diff(C,delta)*Comp+s.diff(D,delta)*Id
hdotprime = 2*s.diff(B,delta)*Comp+s.diff(C,delta)*Id
check_matrix(F*Rvelocity+hdot, 'Implicit-root velocity in coefficient algebra')
# Multiply the SC5 identity by F^T to avoid deleting any denominator.
residual = ((Omega*V-s.diff(V,delta)-V*J*Rvelocity.T)*F.T
            +s.Rational(1,2)*V*(hdotprime.T+Rvelocity.T*Hsecond.T))
check_matrix(residual, 'All sixteen SC10 specialization identities')

R = Omega.applyfunc(lambda x: s.cancel(delta*x).subs(delta,0))
check_matrix((2*R+Id)*(2*R-Id)*(2*R-3*Id), 'Exact residue annihilator')
ea = s.Matrix([1,0,0,0])
xplus = s.Matrix([0,1,i,35*gamma**2-s.Rational(7,4)])
check_matrix(R*ea+ea/2, 'Original negative-residue vector')
check_matrix(R*xplus-3*xplus/2, 'Original positive-residue vector')

labels = [(1,1),(1,-1),(-1,1),(-1,-1)]
columns=[]
for eps,eta in labels:
    r=s.Rational(1,2)+eps*delta+i*eta*gamma
    d=4*delta*gamma*(eps*gamma-i*eta*delta)
    columns.append(s.Matrix([0,-r,3*i*d,(B-17*r+A*r**2)*d-2*A*d**2]))
E=s.Matrix.hstack(*columns)
E0=E.subs(delta,0)
expected_E0=s.Matrix([0,1,0,0])*s.Matrix([[
    -(s.Rational(1,2)+i*gamma),-(s.Rational(1,2)-i*gamma),
    -(s.Rational(1,2)+i*gamma),-(s.Rational(1,2)-i*gamma)]])
check_matrix(E0-expected_E0,'Full labelled boundary mean')
Mix=s.diff(E,delta)-Omega*E
check_matrix(Mix.applyfunc(lambda x:s.cancel(delta*x).subs(delta,0))+R*E0,
             'Full eight-state mixing residue')
Z=s.zeros(4)
Residue=Z.row_join(Z).col_join((-R*E0).row_join(R))
I8=s.eye(8)
check_matrix(Residue*(2*Residue+I8)*(2*Residue-I8)*(2*Residue-3*I8),
             'Full eight-state residue annihilator')
assert E0.rank()==1 and (-R*E0).rank()==1
eig=s.symbols('lambda')
assert s.factor(Residue.charpoly(eig).as_expr()
                -eig**4*(eig+s.Rational(1,2))*(eig-s.Rational(1,2))**2
                 *(eig-s.Rational(3,2)))==0
out={
 'all_assertions_passed':True,
 'checks':'exact polynomial numerator identities over Q(i)(delta,gamma)',
 'coefficient_connection_specialization':True,
 'residue_original_coordinates':[[str(x) for x in row] for row in R.tolist()],
 'full_residue_mixing_rank':1,
 'full_residue_characteristic_polynomial':str(s.factor(Residue.charpoly(eig).as_expr())),
 'no_numeric_sampling':True}
(base/'coefficient_connection_exact.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print('All independent coefficient and total-connection checks passed.',flush=True)
