"""Exact vertical-moment counterexample; no arithmetic nu_Z claim."""
import json
import sys
from pathlib import Path
import sympy as S

R = S.Rational
checks = []

def eq(name, actual, expected):
    difference = actual - expected
    good = all(S.simplify(z) == 0 for z in difference) if isinstance(difference, S.MatrixBase) else S.simplify(difference) == 0
    if not good:
        raise RuntimeError(f"{name}: {actual!s} != {expected!s}")
    checks.append(name)

def positive(name, value):
    if value.is_positive is not True:
        raise RuntimeError(f"{name}: positivity undecided or false: {value}")
    checks.append(name)

atoms = [(R(0), R(115,288))]
for t, w in [(R(1,4),R(29,120)),(R(1,2),R(13,240)),(R(3,4),R(11,2520)),(R(1),R(1,6720))]:
    atoms.extend([(t,w),(-t,w)])
for j, (_, w) in enumerate(atoms):
    positive(f"positive atom {j}", w)
eq("probability", sum(w for _, w in atoms), S.Integer(1))
for k in range(9):
    expected = S.Integer(0) if k % 2 else S.factorial2(k-1) / S.Integer(16)**(k//2)
    eq(f"moment {k}", sum(w*t**k for t,w in atoms), expected)

s = S.Symbol("s")
x = s-R(1,2)
v = R(1,16)
q = [S.Integer(1), x, x*x+v, x**3+3*v*x, x**4+6*v*x*x+3*v*v]
q5 = x**5+10*v*x**3+15*v*v*x
kappa = [S.factorial(k)*v**k for k in range(5)]
for j in range(5):
    for k in range(5):
        value = sum(w*S.conjugate(q[j].subs(s,R(1,2)+S.I*t))*q[k].subs(s,R(1,2)+S.I*t) for t,w in atoms)
        eq(f"Gram {j},{k}", value, kappa[j] if j == k else S.Integer(0))
for k in range(4):
    eq(f"recurrence {k}", s*q[k]-q[k+1]-R(1,2)*q[k]+(k*v*q[k-1] if k else 0), S.Integer(0))
eq("recurrence 4", s*q[4]-q5-R(1,2)*q[4]+4*v*q[3], S.Integer(0))
for j in range(5):
    value = sum(w*S.conjugate(q[j].subs(s,R(1,2)+S.I*t))*q5.subs(s,R(1,2)+S.I*t) for t,w in atoms)
    eq(f"fifth polynomial orthogonality {j}", value, S.Integer(0))

h = s*s-s+R(3,16)
A = S.Matrix([[0,-R(3,16)],[1,1]])
c = S.Matrix([1,0])
T = S.Matrix([[1,R(3,4)],[1,R(1,4)]])
eq("evaluation intertwining", T*A, S.diag(R(3,4),R(1,4))*T)
eq("evaluation unit", T*c, S.ones(2,1))
columns = []
for p in q:
    remainder = S.Poly(S.rem(p,h,s),s)
    columns.append(S.Matrix([remainder.nth(0),remainder.nth(1)]))
expected_columns = [S.Matrix([1,0]),S.Matrix([-R(1,2),1]),S.Matrix([R(1,8),0]),S.Matrix([-R(1,8),R(1,4)]),S.Matrix([R(5,128),0])]
for k in range(5):
    eq(f"complete residue {k}", columns[k], expected_columns[k])
K = [sum((columns[k]*columns[k].H/kappa[k] for k in range(N+1)),S.zeros(2)) for N in range(5)]
remainder5 = S.Poly(S.rem(q5,h,s),s)
column5 = S.Matrix([remainder5.nth(0),remainder5.nth(1)])
eq("K3", K[3], S.Matrix([[R(53,3),-R(88,3)],[-R(88,3),R(176,3)]]))
eq("K4", K[4], S.Matrix([[R(131,6),-R(88,3)],[-R(88,3),R(176,3)]]))
eq("rank-one update", K[4]-K[3], R(25,6)*c*c.H)
energies = {}
lam = S.Symbol("lambda")
for N, expected in [(1,R(1,4)),(2,R(1,3)),(3,R(25,99)),(4,R(4225,15136))]:
    positive(f"positive leading minor {N}", K[N][0,0])
    positive(f"positive determinant {N}", K[N].det())
    L = A*K[N]+K[N]*A.H-K[N]
    eq(f"zero defect trace {N}", S.trace(K[N].inv()*L), S.Integer(0))
    energy_squared = S.factor(-L.det()/K[N].det())
    eq(f"energy squared {N}", energy_squared, expected)
    energies[N] = energy_squared
    if N in (3,4):
        eq(f"kernel recurrence {N}", K[N]-K[N-1], columns[N]*columns[N].H/kappa[N])
        following = columns[N+1] if N < 4 else column5
        eq(f"terminal defect identity {N}", L, (following*columns[N].H+columns[N]*following.H)/kappa[N])
        eq(f"generalized characteristic polynomial {N}", (L-lam*K[N]).det()/K[N].det(), lam**2-expected)
gap = energies[4]-energies[3]
eq("energy squared gap", gap, R(39875,1498464))
positive("strict consecutive increase", gap)

receipt = {"scope":"generic positive vertical moment measure, not arithmetic nu_Z", "python_optimization":sys.flags.optimize, "checks_passed":len(checks), "checks":checks, "epsilon_squared":{str(k):str(v) for k,v in energies.items()}, "gap":str(gap)}
suffix = ".optimized.json" if sys.flags.optimize else ".json"
Path(__file__).with_suffix(suffix).write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"checks_passed":len(checks),"epsilon_squared":receipt["epsilon_squared"],"gap":str(gap)}))
