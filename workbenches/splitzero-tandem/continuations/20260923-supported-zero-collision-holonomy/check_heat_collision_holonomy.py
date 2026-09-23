"""Bounded exact algebra checks for HH8, HH20, HH33--43.

The analytic proof and the actual arithmetic coefficients remain in
HEAT_COLLISION_HOLONOMY.tex. The polynomial heat examples below test the
full-unit formula and its failure when the unit derivative is omitted;
they do not replace the original H_t or certify a zeta zero statement.
"""
import json
from pathlib import Path
import sympy as s

x, t, kappa, alpha, phase = s.symbols("x t kappa alpha phase")
checks = []

def check(name, value):
    ok = bool(value)
    checks.append({"name": name, "passed": ok})
    if not ok:
        raise AssertionError(name)

def is_zero_matrix(A):
    return all(s.simplify(v) == 0 for v in A)

for m in range(1, 9):
    N = s.zeros(m)
    for j in range(m - 1):
        N[j + 1, j] = 1
    I = s.eye(m)
    expN = sum((alpha**j * N**j / s.factorial(j) for j in range(m)),
               s.zeros(m))
    C = expN - I
    inv = sum(((-phase * C / (phase - 1))**j for j in range(m)),
              s.zeros(m)) / (phase - 1)
    check(f"m={m}: full nonresonant inverse",
          is_zero_matrix((phase * expN - I) * inv - I))
    h = sum((alpha**j * N**j / s.factorial(j + 1) for j in range(m)),
            s.zeros(m))
    hinv = sum(((I-h)**j for j in range(m)), s.zeros(m))
    check(f"m={m}: resonant complete factorization",
          is_zero_matrix(expN-I-alpha*N*h))
    check(f"m={m}: resonant unit inverse", is_zero_matrix(h*hinv-I))
    check(f"m={m}: resonant rank", C.subs(alpha, 2*s.I).rank() == m-1)

    # Exact full-unit heat solution:
    # H=e^(kappa*x-kappa^2*t) W, W=P_m(x-2*kappa*t,t).
    # Hence H_t=-H_xx and U_x/U=kappa, retaining a nonconstant unit.
    W = s.expand(sum(
        (-1)**j * s.factorial(m) * t**j
        * (x-2*kappa*t)**(m-2*j)
        / (s.factorial(j)*s.factorial(m-2*j))
        for j in range(m//2+1)))
    Wx = s.diff(W, x)
    correct_numerator = s.diff(W,t)+s.diff(W,x,2)+2*kappa*Wx
    check(f"m={m}: connection with full exponential unit",
          s.expand(correct_numerator) == 0)
    omitted = s.rem(s.diff(W,t)+s.diff(W,x,2), W, x)
    check(f"m={m}: omitted-unit negative control",
          s.simplify(omitted + 2*kappa*Wx) == 0 and omitted != 0)
    # Newton sums from the exact coefficient polynomial, without root sampling.
    P = s.Poly(W.subs({kappa:0,t:1}), x)
    p2 = -2*P.nth(m-2) if m >= 2 else s.Integer(0)
    p4 = (2*P.nth(m-2)**2-4*(P.nth(m-4) if m >= 4 else 0)
          if m >= 2 else s.Integer(0))
    check(f"m={m}: second leading-root sum", p2 == 2*m*(m-1))
    check(f"m={m}: fourth leading-root sum",
          s.expand(p4-4*m*(m-1)*(2*m-3)) == 0)

# A full nontrivial actual-coordinate pair: arbitrary even shift and odd unit.
u, b0, R0, L = s.symbols("u b0 R0 L", real=True, nonzero=True)
V = s.Matrix([[1,b0+u*R0],[1,b0-u*R0]])
P = s.Matrix([[0,1],[1,0]])
J = s.Matrix([[1,b0],[0,R0]])
G = s.diag(2,2*u*u)
check("exact shifted pair inclusion and trace congruence",
      is_zero_matrix(V.T*V-J.T*G*J))
M = s.simplify(V.inv()*P*V)
check("exact shifted pair parameter involution", is_zero_matrix(M*M-s.eye(2)))
check("exact shifted pair trace isometry",
      is_zero_matrix(M.T*(V.T*V)*M-V.T*V))
phase_plus = s.exp(s.I*L*(b0+u*R0)/2)
phase_minus = s.exp(s.I*L*(b0-u*R0)/2)
D = s.diag(phase_plus,phase_minus)
comm = P*D-D*P
norm = s.simplify(s.trace(s.conjugate(comm).T*comm))
check("exact pair Hilbert--Schmidt factor 8",
      s.simplify(s.expand_complex(norm-8*s.sin(L*u*R0/2)**2)) == 0)

out = {"scope":"Exact finite auxiliary algebra checks, not arithmetic zero certification",
       "count":len(checks), "all_passed":all(c["passed"] for c in checks),
       "checks":checks}
path = Path(__file__).with_name("HEAT_COLLISION_HOLONOMY_CHECKS.json")
path.write_text(json.dumps(out, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"count":len(checks), "all_passed":out["all_passed"]}))
