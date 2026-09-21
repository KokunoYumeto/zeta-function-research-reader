from pathlib import Path
import json
import sympy as sp

out = Path(__file__).parent
out.mkdir(parents=True, exist_ok=True)

I = sp.I
T = sp.diag(1, 2, 3, 5)
S = sp.Matrix([[1, I/2, 0, 1],
               [0, 1, sp.Rational(1, 3), 0],
               [0, 0, 1, -I],
               [0, 0, 0, 1]])
G0 = 16*T + S.H*S
W = sp.Matrix([[1, 0], [I, 1], [0, 1], [1, -I]])
GJ = (T.inv() + W*W.H).inv()
Lambda = sp.Matrix([[1, I, 0, 0],
                    [0, 1, 1, 0],
                    [0, 0, 1, 1+I]])
roots = [3+I/4, 3-I/4, -3+I/4, -3-I/4]
U = sp.Matrix([[z**-1, z**-2] for z in roots])
F = Lambda*U
Q0 = (Lambda*G0.inv()*Lambda.H).inv()
H0 = F.H*Q0*F
R = H0.inv()*F.H*Q0
trace_bound = sp.simplify(sp.trace(T.inv()*G0))
joint_bound = sp.simplify(sp.trace(T*GJ.inv()))
checks = []

def exact_zero(name, matrix):
    matrix = matrix.applyfunc(sp.simplify)
    if any(entry != 0 for entry in matrix):
        raise ArithmeticError(name)
    checks.append(name)

def exact_psd(name, matrix):
    from itertools import combinations
    matrix = matrix.applyfunc(sp.simplify)
    exact_zero(name + ": Hermitian", matrix-matrix.H)
    n = matrix.rows
    for size in range(1, n+1):
        for indices in combinations(range(n), size):
            minor = sp.simplify(matrix.extract(indices, indices).det())
            if minor.is_nonnegative is not True:
                raise ArithmeticError(f"{name}: minor {indices} = {minor}")
    checks.append(name + ": every principal minor")

exact_zero("Retained left inverse", R*F-sp.eye(2))
exact_zero("Canonical dual minimum", R*Q0.inv()*R.H-H0.inv())
exact_psd("Trace control of the full cross Gram",
          trace_bound*H0.inv()-R*Lambda*T.inv()*Lambda.H*R.H)

for alpha in [sp.Rational(0), sp.Rational(1, 17),
              sp.Rational(1, 2), sp.Rational(1)]:
    C = (1-alpha)*G0.inv()+alpha*GJ.inv()
    G = C.inv()
    Q = (Lambda*C*Lambda.H).inv()
    H = F.H*Q*F
    lower_denominator = (1-alpha)+alpha*joint_bound*trace_bound
    exact_psd(f"Observed harmonic lower bound at alpha={alpha}",
              H-H0/lower_denominator)
    if alpha < 1:
        exact_psd(f"Canonical upper bound at alpha={alpha}",
                  H0/(1-alpha)-H)
    if alpha > 0:
        exact_psd(f"Joint-section upper bound at alpha={alpha}",
                  U.H*T*U/alpha-H)
    P = C*Lambda.H*Q*Lambda
    exact_zero(f"Original observation projector at alpha={alpha}", P*P-P)
    exact_zero(f"Original metric adjoint at alpha={alpha}", P.H*G-G*P)

receipt = {
    "passed": True,
    "named_checks": len(checks),
    "scope": "Exact finite complex-rational auxiliary matrices. "
             "Not an evaluation of an xi packet, arithmetic moments, or a period.",
    "checks": checks
}
(out/"SUPPLIED_32_CHECK_REPLAY.json").write_text(json.dumps(receipt, indent=2))
print(json.dumps({"passed": True, "named_checks": len(checks),
                  "receipt": str(out/"SUPPLIED_32_CHECK_REPLAY.json")}, indent=2))
