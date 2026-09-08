"""Small exact checks supplementing the complete proof in satellite 29j.

No NS existence proof, numerical integration, zero search or Lean check.
"""
from pathlib import Path
import hashlib
import json
import sys
import time
import sympy as s

ROOT = Path(__file__).resolve().parents[2]
PROOF = ROOT / "tex/satellites/29j_ns_stress_arithmetic.tex"
OUT = Path(__file__).with_name("ns_stress_arithmetic_checks.json")
checks = []
start = time.monotonic()


def eq(name, expression):
    ok = s.expand(expression) == 0
    checks.append({"id": name, "passed": bool(ok)})
    if not ok:
        raise AssertionError((name, expression))


x, y, z = s.symbols("x y z", real=True)
coords = (x, y, z)
F = s.Matrix([
    (1+x*y)**3*z+y*y*(1+x*y)*(4+3*x*y),
    y+3*x*(1+x*y)**2*z+3*x*y*y*(4+3*x*y),
    2*x-3*x*x*y-x**3*z,
])
S = s.diag(s.Rational(1, 2), 1, 1)*F
J = S.jacobian(coords)
eq("J.determinant", J.det()+1)
Ji = -J.adjugate()
for a in range(3):
    for b in range(3):
        eq(f"inverse.left.{a}.{b}", (Ji*J-s.eye(3))[a,b])
        eq(f"inverse.right.{a}.{b}", (J*Ji-s.eye(3))[a,b])

# Polynomial verification of the connection identities without replacing J.
G = [s.simplify(J.diff(c)*Ji) for c in coords]
for i in range(3):
    for a in range(3):
        for b in range(3):
            eq(f"connection.frame.{i}.{a}.{b}",
               (G[i]*J-J.diff(coords[i]))[a,b])
for i in range(3):
    for j in range(i+1, 3):
        curvature = G[j].diff(coords[i])-G[i].diff(coords[j])-G[i]*G[j]+G[j]*G[i]
        for a in range(3):
            for b in range(3):
                eq(f"connection.curvature.{i}.{j}.{a}.{b}", curvature[a,b])

r = s.symbols("r", real=True)
Jr = J.subs({x:r,y:0,z:0})
want = s.Matrix([[0,0,s.Rational(1,2)],[0,1,3*r],[2,-3*r*r,-r**3]])
for a in range(3):
    eq(f"sample.shift.{a}", S[a].subs({x:r,y:0,z:0})-[0,0,2*r][a])
    for b in range(3):
        eq(f"sample.J.{a}.{b}", Jr[a,b]-want[a,b])
row = (s.Matrix([[-6*r,1,0]])*Jr)
for b in range(3):
    eq(f"actual.swirl.inverse.{b}", row[b]-[0,1,0][b])
nu, Xin, tau = s.symbols("nu Xin tau", positive=True)
eq("sample.cauchy.factor", (1+36*r*r).subs(r,s.sqrt(2*nu*Xin*tau))
   -(1+72*nu*Xin*tau))

# All product terms of the nonlinear residual in the exact frame.
u = s.symbols("u:3")
w = s.symbols("w:3")
du = s.symbols("du:3")
dw = s.symbols("dw:3")
eq("increment.all.quadratic.cross.terms",
   sum((u[i]+w[i])*(du[i]+dw[i]) for i in range(3))
   -sum(u[i]*du[i]+u[i]*dw[i]+w[i]*du[i]+w[i]*dw[i] for i in range(3)))
a, b, c = s.symbols("a b c", real=True)
eq("translations.cocycle", (a-b)+(b-c)-(a-c))
eq("translations.inverse", (a-b)+(b-a))

record = {
    "schema_version": 1,
    "id": "NS-ACTUAL-STRESS-ARITHMETIC-20260908-001",
    "status": "exact_algebra_checks_pass",
    "scope": "Polynomial frame/inverse/curvature, actual sample, full nonlinear cross terms. Analytical identities are proved in TeX; no complete source-proof verification.",
    "source_proof": str(PROOF.relative_to(ROOT)).replace("\\", "/"),
    "source_proof_sha256": hashlib.sha256(PROOF.read_bytes()).hexdigest(),
    "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "checks": checks,
    "check_count": len(checks),
    "all_passed": all(c["passed"] for c in checks),
    "elapsed_seconds": time.monotonic()-start,
    "python_version": sys.version,
    "sympy_version": s.__version__,
    "lean_used": False,
    "numerical_zero_search": False,
    "source_existence_independently_certified": False,
}
OUT.write_text(json.dumps(record, indent=2)+"\n", encoding="utf-8")
print(json.dumps({k:record[k] for k in ("status","check_count","elapsed_seconds")}))
