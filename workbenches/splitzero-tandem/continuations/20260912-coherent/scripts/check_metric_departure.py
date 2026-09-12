"""Exact finite calibrations of MD1--MD9; no arithmetic zero certificate."""
from pathlib import Path
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
rows = []

def check(name, value):
    if not bool(value):
        raise RuntimeError(name)
    rows.append(name)

def zero(x):
    return s.cancel(s.expand(x)) == 0

def departure_case(name, A, G):
    d = A.rows
    vals = [z for z, m in A.eigenvals().items() for _ in range(m)]
    delta = [s.re(z)-s.Rational(1, 2) for z in vals]
    W = A.adjoint()*G + G*A - G
    L = G.inv()*W
    dep = s.cancel(s.expand(s.trace(G.inv()*A.adjoint()*G*A)
                           - sum(s.conjugate(z)*z for z in vals)))
    check(name+':trace', zero(s.trace(L)-2*sum(delta)))
    check(name+':square_trace', zero(s.trace(L*L)-4*sum(x*x for x in delta)-2*dep))
    check(name+':departure_nonnegative', dep >= 0)
    if W.rank() <= 2:
        target = abs(sum(delta)) + s.sqrt(2*sum(x*x for x in delta)+dep-sum(delta)**2)
        values = L.eigenvals()
        eps = max(abs(x) for x in values)
        check(name+':rank_two_exact_norm', zero(eps-target))
    return dep, L

G = s.Matrix([[4, 1+s.I], [1-s.I, 3]])
A = s.Matrix([[0, s.Rational(61, 16)-2*s.I], [1, 1+4*s.I]])
departure_case('retained_companion', A, G)
departure_case('off_line_reflected_pair', s.diag(s.Rational(1,4)+2*s.I,
                                              s.Rational(3,4)+2*s.I), G)
departure_case('critical_distinct', s.diag(s.Rational(1,2)+s.I,
                                        s.Rational(1,2)+3*s.I), G)
departure_case('one_coordinate', s.Matrix([[s.Rational(2,3)+s.I]]), s.Matrix([[7]]))

for r in [2, 3, 4]:
    N = s.zeros(r)
    for k in range(r-1):
        N[k+1, k] = 1
    G = s.diag(*(s.Rational(1, 9)**k for k in range(r)))
    A = (s.Rational(1,2)+2*s.I)*s.eye(r)+N
    dep, L = departure_case(f'full_jet_{r}', A, G)
    eps2 = max(s.cancel(x*x) for x in L.eigenvals())
    bound = s.Rational(r, 2)*eps2
    for k in range(r):
        for ell in range(1, r-k):
            check(f'full_jet_{r}:ratio_{k}_{ell}', G[k+ell,k+ell]/G[k,k] <= bound**ell)
    check(f'full_jet_{r}:condition', 9**(r-1) >= bound**(-(r-1)))

K = s.Matrix([[3, s.I], [-s.I, 5]])
A = s.Matrix([[s.Rational(1,2), 0], [1, s.Rational(1,2)]])
U = 2*s.eye(2)+3*A
G = U.adjoint()*K.inv()*U
check('original_local_unit:commutes', A*U == U*A)
check('original_local_unit:trace_congruence', zero(s.trace(G.inv()*A.adjoint()*G*A)
                                                -s.trace(K*A.adjoint()*K.inv()*A)))

result = {'all_passed': True, 'passed': len(rows), 'checks': rows,
          'scope': 'Exact rational/algebraic packet and metric calibrations, not actual zeta zero locations',
          'sympy_version': s.__version__,
          'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
dest = ROOT/'checks'/'metric_departure.json'
dest.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k != 'checks'}))
