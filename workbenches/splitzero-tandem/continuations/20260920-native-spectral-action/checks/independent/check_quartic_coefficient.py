"""Exact MC35 replay supplement; guards survive Python optimization."""
import argparse
import json
from pathlib import Path
import sympy as s

t = s.symbols("t", real=True)
count = 0
negative = 0
Q = s.Matrix([[0, 1], [0, 0]])
r = s.Matrix([1, 0])
ell = s.Matrix([[0, 1]])
for G, A in [
    (s.diag(2, 3), s.Matrix([[1, 3+3*s.I], [2-2*s.I, 4]])),
    (s.diag(2, 3), s.Matrix([[0, s.Rational(1, 2)], [s.Rational(1, 3), 0]])),
]:
    gamma = (ell*A*r)[0]
    J4 = s.trace((A-t*Q)**4)
    formula = s.trace(A**4)-4*t*(ell*A**3*r)[0]+2*t**2*gamma**2
    for value in [
        G*A-A.conjugate().T*G,
        J4-formula,
        s.diff(J4, t, 2)-4*gamma**2,
        s.trace(A*Q*A*Q)-gamma**2,
        s.trace(Q*A*Q*A)-gamma**2,
    ]:
        values = list(value) if isinstance(value, s.MatrixBase) else [value]
        if any(s.simplify(v) != 0 for v in values):
            raise RuntimeError("Quartic exact check failed.")
        count += 1
    if s.simplify(s.diff(J4, t, 2)) == 0:
        raise RuntimeError("Wrong zero-Hessian control unexpectedly passed.")
    negative += 1
result = {"status": "PASS", "exact_identity_checks": count,
          "rejected_wrong_formula_controls": negative,
          "scope": "MC35 only; full complex coefficient retained.",
          "sympy_version": s.__version__}
parser = argparse.ArgumentParser()
parser.add_argument("--output", type=Path)
args = parser.parse_args()
rendered = json.dumps(result, indent=2)
if args.output:
    args.output.write_text(rendered+"\n", encoding="utf-8")
print(rendered)
