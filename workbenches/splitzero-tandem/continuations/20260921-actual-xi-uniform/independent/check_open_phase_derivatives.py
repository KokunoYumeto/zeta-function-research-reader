"""Exact independent checks of the noncommuting and phase derivatives."""
from pathlib import Path
import hashlib
import json
import sympy as s

checks = []
A, R, R1, R2, Dj = s.symbols('A R R1 R2 Dj', commutative=False)
rules = {A: -A*R1*A, R: R1, R1: R2, R2: 0, Dj: 0}

def deriv(expr):
    expr = s.expand(expr)
    if expr.is_Add:
        return s.expand(sum(deriv(t) for t in expr.args))
    if expr.is_Number:
        return s.Integer(0)
    if expr.is_Symbol:
        return rules[expr]
    if expr.is_Mul:
        factors = expr.args
        return s.expand(sum(s.Mul(*factors[:k])*deriv(factors[k])*s.Mul(*factors[k+1:])
                            for k in range(len(factors))))
    raise ValueError(expr)

def equal(lhs, rhs, name):
    assert s.expand(lhs-rhs) == 0, name
    checks.append(name)

equal(deriv(deriv(A)), 2*A*R1*A*R1*A-A*R2*A, 'full noncommuting inverse second derivative')
equal(deriv(A*Dj*R), A*Dj*R1-A*R1*A*Dj*R, 'full conjugated first period derivative')
equal(deriv(deriv(A*Dj*R)),
      A*Dj*R2-2*A*R1*A*Dj*R1+2*A*R1*A*R1*A*Dj*R-A*R2*A*Dj*R,
      'full conjugated second period derivative')

x = s.symbols('x', real=True)
signs = [1,-1,-1,1]
for i, si in enumerate(signs):
    for j, sj in enumerate(signs):
        entry = (1+s.I*x*sj)/(1+s.I*x*si)
        delta = sj-si
        assert s.cancel(s.diff(entry,x)-s.I*delta*entry/(1+x*x)) == 0
        assert s.cancel(s.diff(entry,x,2)+((delta**2+2*s.I*x*delta)/(1+x*x)**2)*entry) == 0
        checks.append(f'phase first and second derivatives, original entry {i+1},{j+1}')

z, xi = s.symbols('z xi')
y = [s.Function(f'y{k}')(z,x,xi) for k in range(4)]
def bilinear(a,b):
    return a[0]*b[3]+a[3]*b[0]-a[1]*b[2]-a[2]*b[1]
def yd(v):
    return [s.diff(a,v) for a in y]
f = y[0]*y[3]-y[1]*y[2]
equal(s.diff(f,z), bilinear(y,yd(z)), 'original factor first period derivative')
equal(s.diff(f,z,2), bilinear(yd(z),yd(z))+bilinear(y,[s.diff(a,z,2) for a in y]),
      'original factor second period derivative')
equal(s.diff(f,x), bilinear(y,yd(x)), 'original factor phase derivative')
equal(s.diff(f,z,x), bilinear(yd(x),yd(z))+bilinear(y,[s.diff(a,z,x) for a in y]),
      'original factor mixed period-phase derivative')
equal(s.diff(f,xi), bilinear(y,yd(xi)), 'original factor first symbol derivative')
equal(s.diff(f,xi,z), bilinear(yd(z),yd(xi))+bilinear(y,[s.diff(a,xi,z) for a in y]),
      'original factor mixed symbol-period derivative')
equal(s.diff(f,xi,x), bilinear(yd(x),yd(xi))+bilinear(y,[s.diff(a,xi,x) for a in y]),
      'original factor mixed symbol-phase derivative')

n, w = s.symbols('n w', positive=True)
term = (2*n+2)*w**(n-2)/s.factorial(n-2)
ratio = s.simplify(term.subs(n,n+1)/term)
assert s.simplify(ratio-w*(n+2)/((n+1)*(n-1))) == 0
checks.append('complete second-derivative factorial-tail successive ratio')

base = Path(__file__).resolve().parent
proof = base/'OPEN_PHASE_DERIVATIVE_REVIEW.tex'
result = {
    'status': 'PASS',
    'exact_identity_groups': len(checks),
    'checks': checks,
    'proof_sha256': hashlib.sha256(proof.read_bytes()).hexdigest(),
    'scope': 'Exact differentiation and tail identities only. The receiving full-series phase enclosure supplies the numerical persistence interval.'
}
(base/'OPEN_PHASE_DERIVATIVE_CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
