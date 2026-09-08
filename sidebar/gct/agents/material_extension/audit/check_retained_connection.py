"""Independent exact audit of the retained material connection and conic basis.

Run with Python and SymPy. All equalities are identities of rational functions;
none are numerical sampling. The geometric domains are recorded in AUDIT.md.
"""
from pathlib import Path
import hashlib
import json
import sympy as S

b, s, eta = S.symbols('b s eta')
delta = b**2 - 32*s
h = b**2/S.Integer(16) - 2*s
L = 4 + b**2/S.Integer(16) - 2*s
I = S.eye(4)
e0 = I[:, 0]
results = []

def check(name, expression):
    entries = list(expression) if isinstance(expression, S.MatrixBase) else [expression]
    good = all(S.cancel(entry) == 0 for entry in entries)
    results.append({'name': name, 'passed': bool(good), 'scalar_identities': len(entries)})
    if not good:
        raise AssertionError((name, expression))

K = S.Matrix([[0,0,0,-1], [1,0,0,0], [0,1,0,h+2], [0,0,1,0]])
K_inverse = -K**3 + (h+2)*K
E = K - K_inverse
P = K + K_inverse
R = b*I/4 + E
check('companion quartic', K**4 - (h+2)*K**2 + I)
check('retained Laurent inverse on both sides', (K*K_inverse-I).col_join(K_inverse*K-I))
check('eta square with original b and s', E**2-h*I)
check('p square with original b and s', P**2-L*I)
check('original retained quadratic for r', R**2-b*R/2+2*s*I)
check('conic exact identity', P**2-E**2-4*I)
check('recover q and q inverse', ((P+E)/2-K).col_join((P-E)/2-K_inverse))

T = S.Matrix([[1,b/4,0,-h-2],
              [0,-h-1,h+3,b*(h+3)/4],
              [0,0,0,2],
              [0,1,-1,-b/4]])
check('four exact basis columns', T-S.Matrix.hstack(e0,R*e0,P*e0,R*P*e0))
check('basis conversion determinant exactly four', T.det()-4)

# Derivation of q from q=(p+eta)/2. The inverse eta*p is E*P/(h*L).
Dq = -K*E*P*e0/(h*L)
J = S.Matrix.hstack(S.zeros(4,1), Dq, 2*K*Dq, 3*K**2*Dq)
def Dv(v):
    return v.diff(s) + J*v
check('differentiate defining quartic exactly', 4*K**3*Dq+2*K**2*e0-2*(h+2)*K*Dq)
check('Db equals zero', Dv(b*e0))
check('Ds equals one', Dv(s*e0)-e0)
check('Deta equals minus inverse eta', Dv(E*e0)+E*e0/h)
check('Dp equals minus inverse p', Dv(P*e0)+P*e0/L)
check('Dr with original b retained', Dv(R*e0)+E*e0/h)

A = S.Matrix([[0,4*b/delta],[0,-16/delta]])
Gamma = S.diag(A,A-S.eye(2)/L)
check('connection in ordered basis 1,r,p,rp', T.diff(s)+J*T-T*Gamma)
B = S.Matrix([[0,64*b/delta**2],[0,-256/delta**2]])
Z = S.diag(B,B-2*A/L-S.eye(2)/L**2)
check('all exact zero order coefficients', Gamma.diff(s)+Gamma**2-Z)
check('square connection through original companion basis',
      Dv(Dv(T))-T*Z)

# Original inverse F, with no coordinate normalization.
x = -1/(2*eta)
y = b/4+3*eta
w = 26*eta**2+3*b*eta/2
F1 = (1+x*y)**3*w+y**2*(1+x*y)*(4+3*x*y)
F2 = y+3*x*(1+x*y)**2*w+3*x*y**2*(4+3*x*y)
F3 = 2*x-3*x**2*y-x**3*w
check('original F1 equals 2s on eta squared h', F1-(b**2/16-eta**2))
check('original F2 equals retained b', F2-b)
check('original F3 equals zero', F3)
check('source r equals y plus inverse x', y+1/x-(b/4+eta))
check('alpha equals minus two eta', (-2*(b/4+eta)+b/2)+2*eta)
De = lambda expr: -S.diff(expr,eta)/eta
check('Dx', De(x)+1/(2*eta**3))
check('Dy', De(y)+3/eta)
check('Dw retains b term', De(w)+52+3*b/(2*eta))
check('D squared x', De(De(x))+3/(2*eta**5))
check('D squared y', De(De(y))+3/eta**3)
check('D squared w retains b term', De(De(w))+3*b/(2*eta**3))
check('full source drift target derivative', S.Matrix([De(F1)-2,De(F2),De(F3)]))

# Reduction of the retained D^2 coefficients at b=0 is exact, and not used
# to establish any of the identities above.
check('exact b zero specialization of r connection', A.subs(b,0)-S.diag(0,1/(2*s)))

receipt = {
    'status': 'passed',
    'check_count': len(results),
    'scalar_identity_count': sum(r['scalar_identities'] for r in results),
    'domain': 'Q[b,s,delta^(-1),L^(-1)] with delta=b^2-32s and L=4+b^2/16-2s; H only requires eta nonzero',
    'ordered_basis': ['1','r','p','rp'],
    'method': 'Exact rational-function identities over Q; no numerical sampling.',
    'sympy_version': S.__version__,
    'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'checks': results,
}
Path(__file__).with_name('checks.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(f"PASS {len(results)} checks, {receipt['scalar_identity_count']} exact scalar identities")
