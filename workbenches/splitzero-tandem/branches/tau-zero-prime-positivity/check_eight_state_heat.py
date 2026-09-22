"""Bounded exact identities for the signed eight-state heat comparison."""

from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import sympy as S

Q = S.Rational
checks = []


def check(name, expression, locators):
    values = list(expression) if isinstance(expression, (list, tuple, S.MatrixBase)) else [expression]
    residuals = [S.factor(S.simplify(S.cancel(value))) for value in values]
    nonzero = [str(value) for value in residuals if value != 0]
    checks.append({"name": name, "proof_locators": locators,
                   "passed": not nonzero, "scalar_identities": len(values),
                   "nonzero_residuals": nonzero})


def inertia(name, matrix, expected, locators):
    counts = [0, 0, 0]
    undecided = []
    for eigenvalue, multiplicity in matrix.eigenvals().items():
        if eigenvalue == 0:
            counts[2] += multiplicity
        elif eigenvalue.is_positive:
            counts[0] += multiplicity
        elif eigenvalue.is_negative:
            counts[1] += multiplicity
        else:
            undecided.append(str(eigenvalue))
    checks.append({"name": name, "proof_locators": locators,
                   "passed": counts == list(expected) and not undecided,
                   "inertia": counts, "expected_inertia": list(expected),
                   "undecided_eigenvalues": undecided})


R, h = S.symbols("R h", real=True)
s = S.symbols("s", positive=True)
F = R**3 - (1 + 16*h)*R + 16*h
Fminus = R**3 - (1 + 16*h)*R - 16*h
check("initial_root_polynomial", F.subs(h, 0) - R*(R-1)*(R+1), ["ESH9"])
check("marked_root_factorization", F - (R-1)*(R**2+R-16*h), ["ESH35"])
check("marked_derivative_and_heat_clock",
      [S.diff(F, R).subs(R, 1) - (2-16*h), (2-16*h)/8 - (Q(1,4)-2*h)],
      ["ESH36", "ESH39"])
check("native_between_path_map", Fminus.subs(R, -R) + F, ["ESH56", "ESH57"])
check("native_between_path_derivative",
      S.diff(Fminus, R).subs(R, -R) - S.diff(F, R), ["ESH57"])
derivative = S.diff(F, R).subs(h, (s**2-1)/64)
check("all_three_derivative_factors", [
    derivative.subs(R, 1) - (9-s**2)/4,
    derivative.subs(R, (-1+s)/2) - s*(s-3)/2,
    derivative.subs(R, (-1-s)/2) - s*(s+3)/2,
], ["ESH43", "ESH44"])
check("all_three_root_formulas", [
    F.subs({h: (s**2-1)/64, R: root}, simultaneous=True)
    for root in [1, (-1+s)/2, (-1-s)/2]
], ["ESH43"])
e1 = (R**2+R-16*h)/(2-16*h)
check("marked_root_idempotent", S.rem(S.together(e1**2-e1), F, R), ["ESH41"])
check("critical_factorization", F.subs(h, Q(1,8)) - (R-1)**2*(R+2), ["ESH48"])
epsilon = S.symbols("epsilon")
check("critical_derivative_coefficient",
      S.diff(F, R).subs({h: Q(1,8), R: 1+epsilon}) - 6*epsilon - 3*epsilon**2,
      ["ESH49"])
eminus = (R-1)**2/9
check("critical_root_idempotent",
      S.rem(eminus**2-eminus, F.subs(h, Q(1,8)), R), ["ESH50"])

I8 = S.eye(8)
ordinary_trace = S.diag(2,-2,2,4,2,4,2,-2)
deck = S.diag(1,-1,1,-1,1,-1,1,-1)
native = S.zeros(8)
for source, target, sign in [(0,0,1),(1,1,-1),(2,4,1),(3,5,-1),
                             (4,2,1),(5,3,-1),(6,6,1),(7,7,1)]:
    native[target, source] = sign
Gdeck = deck.T*ordinary_trace
Gnative = native.T*ordinary_trace
check("deck_trace_Gram", Gdeck-S.diag(2,2,2,-4,2,-4,2,2), ["ESH22"])
order = [0,1,2,4,3,5,6,7]
native_blocks = S.diag(S.diag(2,2), S.Matrix([[0,2],[2,0]]),
                       S.Matrix([[0,-4],[-4,0]]), S.diag(2,-2))
check("native_trace_Gram", Gnative.extract(order, order)-native_blocks, ["ESH23"])
check("native_and_deck_involutions", list(native**2-I8)+list(deck**2-I8), ["ESH15", "ESH18"])
inertia("coefficient_conjugation_inertia", ordinary_trace, (6,2,0), ["ESH21"])
inertia("deck_inertia", Gdeck, (6,2,0), ["ESH22"])
inertia("native_inertia", Gnative, (5,3,0), ["ESH24"])

missing = S.Matrix([0,0,0,0,0,0,Q(1,2),-S.I/2])
retained = S.conjugate(missing)
check("missing_state_deck_stability", deck*S.conjugate(missing)-missing, ["ESH27"])
check("missing_state_native_exchange", native*S.conjugate(missing)-retained, ["ESH27"])
check("missing_state_pure_native_stability", native*missing-missing, ["ESH27"])
corner = S.Matrix.hstack(*[I8[:, j] for j in range(6)], retained)
Gdeck7 = S.simplify(S.conjugate(corner).T*Gdeck*corner)
Gnative7 = S.simplify(S.conjugate(corner).T*Gnative*corner)
inertia("seven_state_deck_quotient", Gdeck7, (5,2,0), ["ESH29"])
inertia("seven_state_native_restriction", Gnative7, (4,2,1), ["ESH30"])
infinity_points = S.Matrix.hstack(missing, retained)
check("restored_native_hyperbolic_pair",
      S.conjugate(infinity_points).T*Gnative*infinity_points-S.Matrix([[0,1],[1,0]]),
      ["ESH30b"])
check("separate_deck_positive_points",
      S.conjugate(infinity_points).T*Gdeck*infinity_points-S.eye(2), ["ESH27", "ESH28"])
inertia("native_stable_six_factor_quotient", Gnative[:6,:6], (4,2,0), ["ESH30a"])

theta_matrix = S.Matrix([[0,-1],[1,0]])
positive_map = S.diag(1,Q(1,2))
native_map = S.diag(1,S.I/2)
check("positive_infinity_quarter_relation", (theta_matrix/2)**2+S.eye(2)/4, ["ESH33"])
check("native_infinity_initial_relation", (S.I*theta_matrix/2)**2-S.eye(2)/4, ["ESH34"])
check("positive_infinity_quarter_form",
      S.conjugate(positive_map).T*S.diag(2,2)*positive_map-S.diag(2,Q(1,2)), ["ESH33"])
check("native_infinity_initial_form",
      S.conjugate(native_map).T*S.diag(2,-2)*native_map-S.diag(2,-Q(1,2)), ["ESH34"])
sign2 = S.diag(1,-1)
check("positive_infinity_involution", sign2*S.conjugate(positive_map)-positive_map*sign2, ["ESH33"])
check("native_infinity_involution", S.conjugate(native_map)-native_map*sign2, ["ESH34"])

N4 = S.zeros(4)
for j in range(3):
    N4[j+1,j] = 1
N2 = S.Matrix([[0,0],[1,0]])
eps_matrix = N4**2/6
check("critical_length_four_relations", list(eps_matrix**2)+list(N4**2-6*eps_matrix)+list(N4**4), ["ESH49"])
qmatrix = S.Matrix([[1,0,0,0],[0,1,0,0]])
check("critical_marked_quotient", qmatrix*N4-N2*qmatrix, ["ESH54"])
local_Gram = S.Matrix(4,4,lambda i,j: (-1)**i*S.trace(N4**(i+j)))
check("critical_length_four_trace", local_Gram-S.diag(4,0,0,0), ["ESH52"])
check("critical_trace_factor_two",
      local_Gram-2*qmatrix.T*S.diag(2,0)*qmatrix, ["ESH55"])
critical_Gram = S.diag(local_Gram, S.diag(2,-18), S.diag(2,2))
inertia("complete_critical_inertia", critical_Gram, (4,1,3), ["ESH53"])
inertia("critical_completed_seven_quotient", S.diag(local_Gram,S.diag(2,-18),S.ones(1)),
        (3,1,3), ["ESH53", "ESH55"])
inertia("critical_original_three_point_fibre", S.diag(2,-18,1), (2,1,0), ["ESH55"])

c0,d0 = S.symbols('c0 d0',real=True)
MR = S.Matrix([[0,0,-d0],[1,0,c0],[0,1,0]])
Ppoly = S.Matrix([[3,0,2*c0],[0,2*c0,-3*d0],[2*c0,-3*d0,2*c0**2]])
Qpoly = S.Matrix([[3*c0,-9*d0,4*c0**2],[-9*d0,4*c0**2,-12*c0*d0],[4*c0**2,-12*c0*d0,4*c0**3+9*d0**2]])
check('fixed_basis_root_trace',S.Matrix(3,3,lambda i,j:S.trace(MR**(i+j)))-Ppoly,['ESH60','ESH61','ESH62'])
check('fixed_basis_derivative_trace',S.Matrix(3,3,lambda i,j:S.trace((3*MR**2-c0*S.eye(3))*MR**(i+j)))-Qpoly,['ESH62'])
Mc=MR.subs({c0:3,d0:2})
Rc=S.diag(Mc,Mc)
Tc=S.zeros(6);Tc[:3,3:]=3*Mc**2-3*S.eye(3);Tc[3:,:3]=S.eye(3)
n1=(Rc-S.eye(6))*(Rc+2*S.eye(6));n2=Tc*(Rc+2*S.eye(6));n3=Tc*n1
for name,expression in [('n1_square',n1**2),('n1_n3',n1*n3),('n2_n3',n2*n3),('n3_square',n3**2),('n2_square',n2**2-18*n1),('n1_n2',n1*n2-3*n3),('n2_cube',n2**3-54*n3),('n2_fourth',n2**4)]:
    check(name,expression,['ESH68','ESH69','ESH71'])
qfixed=S.Matrix([[1,1,1,0,0,0],[0,0,0,1,1,1]])
check('fixed_basis_radical_quotient',list(qfixed*n1)+list(qfixed*n2-3*N2*qfixed)+list(qfixed*n3),['ESH72'])
critical_fixed=S.diag(2*Ppoly.subs({c0:3,d0:2}),-2*Qpoly.subs({c0:3,d0:2}),2,2)
inertia('critical_full_polynomial_basis',critical_fixed,(4,1,3),['ESH64','ESH65','ESH66'])

base = Path(__file__).resolve().parent
proof = base / "EIGHT_STATE_HEAT_COMPARISON.md"
failed = [item["name"] for item in checks if not item["passed"]]
receipt = {
    "status": "FAIL" if failed else "PASS",
    "generated_at_utc": datetime.now(timezone.utc).isoformat(),
    "checker": Path(__file__).name,
    "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "proof": proof.name,
    "proof_sha256": hashlib.sha256(proof.read_bytes()).hexdigest(),
    "sympy_version": S.__version__,
    "method": "Exact symbolic identities and exact finite-matrix inertia; no floating-point sampling.",
    "domains": ["Complex fibre algebras with the displayed conjugate-linear involutions.",
                "Heat path h real; forward signature theorem uses h>=0 and s=sqrt(1+64h)>=1.",
                "Marked-root idempotent only when h!=1/8; collision quotient checked separately."],
    "scope_boundary": "The proof supplies the full scheme, map, universal-ideal and all-parameter sign arguments. These checks verify the listed algebraic identities and finite matrices, not a global Weil or zeta-zero statement.",
    "check_count": len(checks),
    "scalar_identity_count": sum(item.get("scalar_identities",0) for item in checks),
    "failed_checks": failed,
    "checks": checks,
}
output = base / "EIGHT_STATE_HEAT_CHECKS.json"
output.write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":receipt["status"],"checks":len(checks),
                  "scalar_identities":receipt["scalar_identity_count"],
                  "failed_checks":failed,"receipt":output.name},indent=2))
raise SystemExit(1 if failed else 0)
