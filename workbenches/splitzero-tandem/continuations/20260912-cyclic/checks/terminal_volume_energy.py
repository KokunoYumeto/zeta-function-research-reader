"""Exact volume-energy identity calibration on symmetry packets.

Explicit Gaussian moment fixtures supplement the arithmetic proof. Original
monomial coordinates and repeated critical jets are retained in every check.
"""
import json
import sys
from pathlib import Path
import sympy as sp

s = sp.Symbol('s')
R = sp.Rational
v = R(1,16)
q = [sp.Integer(1), s-R(1,2)]
for k in range(1,7):
    q.append(sp.expand((s-R(1,2))*q[k]+k*v*q[k-1]))
norms = [sp.factorial(k)*v**k for k in range(len(q))]
checks = []

def eq(name, a, b):
    x = a-b
    values = list(x) if isinstance(x, sp.MatrixBase) else [x]
    if any(sp.simplify(z) != 0 for z in values):
        raise RuntimeError(f'{name}: {x}')
    checks.append(name)

def residue(poly,h):
    p = sp.Poly(sp.rem(poly,h,s),s)
    return sp.Matrix([p.nth(0),p.nth(1)])

packets = {
    'reflected_pair': (s-R(3,4))*(s-R(1,4)),
    'critical_node_pair': (s-R(1,2))**2+v,
    'critical_repeated_jet': (s-R(1,2))**2,
}
for name,h in packets.items():
    h=sp.expand(h)
    A=sp.Matrix.hstack(residue(s,h),residue(s*s,h))
    columns=[residue(p,h) for p in q]
    K=[sum((columns[k]*columns[k].H/norms[k] for k in range(N+1)),sp.zeros(2)) for N in range(7)]
    eq(name+'/real_A',A,sp.conjugate(A))
    eq(name+'/reflection_trace',sp.trace(A),1)
    for n in range(3,7):
        label=f'{name}/n{n}'
        M=K[n-1].inv()/norms[n-1]
        alpha=(columns[n-1].H*M*columns[n-1])[0]
        beta=(columns[n].H*M*columns[n])[0]
        gamma=(columns[n].H*M*columns[n-1])[0]
        current=sp.simplify(K[n-2].det()/K[n-1].det())
        following=sp.simplify(K[n-1].det()/K[n].det())
        W=A*K[n-1]+K[n-1]*A.H-K[n-1]
        energy=sp.simplify(-W.det()/K[n-1].det())
        eq(label+'/gamma_exact_zero',gamma,0)
        eq(label+'/current_volume',current,1-alpha)
        eq(label+'/next_volume',following,n*v/(n*v+beta))
        eq(label+'/energy_scalar_closure',energy,alpha*beta)
        eq(label+'/energy_volume_closure',energy,n*v*(1-current)*(1-following)/following)

receipt={'scope':'exact Gaussian moment identity calibration on conjugation-and-reflection packets; no arithmetic asymptotic estimate','python_optimization':sys.flags.optimize,'checks_passed':len(checks),'checks':checks}
suffix='.optimized.json' if sys.flags.optimize else '.json'
Path(__file__).with_suffix(suffix).write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'checks_passed':len(checks),'packets':list(packets)}))
