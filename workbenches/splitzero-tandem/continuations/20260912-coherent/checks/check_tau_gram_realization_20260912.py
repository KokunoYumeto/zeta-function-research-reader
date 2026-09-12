"""Exact calibration of finite-source Gram realization; no analytic certification."""
from pathlib import Path
import json
import sympy as s


def exact_equal(left, right, label):
    difference = (left - right).applyfunc(s.simplify)
    if difference != s.zeros(*difference.shape):
        raise RuntimeError(f"{label}: {difference}")


i = s.I
F = s.Matrix([[2, 1+i, 0], [0, 3, 1], [0, 0, 2], [0, 0, 0], [0, 0, 0]])
R_m = s.Matrix([[0, 0], [0, 0], [0, 0], [s.Rational(1, 3), 0], [0, s.Rational(1, 2)]])
B_m = s.Matrix([[1, i], [2, -1], [i, 3]])
R_0 = R_m - F * B_m
H = F.H * F
exact_equal(-H.inv() * F.H * R_0, B_m, "computed minimizing correction")
exact_equal(F.H * R_m, s.zeros(3, 2), "residual orthogonality")
C = s.Matrix([[1, 0], [0, 1], [0, 0]])
H_C = C.H * H * C
H_C_root = (H_C + 6*s.eye(2)) / (3*s.sqrt(3))
exact_equal(H_C_root * H_C_root, H_C, "positive Gram square root")
Delta_root = s.Matrix([[2, i], [-i, 2]])
Delta = Delta_root * Delta_root
G_m = R_m.H * R_m
G_target = G_m + Delta
B = B_m + C * H_C_root.inv() * Delta_root
R = R_0 + F * B
exact_equal(R.H * R, G_target, "realized prescribed positive Gram")
T = s.Matrix([[1, 1+i], [0, 2], [i, -1]])
exact_equal((R_0+F*(B_m+T)).H*(R_0+F*(B_m+T)),
            G_m+T.H*H*T, "complete fixed-level Gram expression")
# A full rank two increment cannot occur with a one-dimensional source.
if Delta.rank() != 2:
    raise RuntimeError("rank obstruction calibration did not have rank two")
one_source = s.Matrix([[1, 2+i]])
if (one_source.H * one_source).rank() > 1:
    raise RuntimeError("one-source rank obstruction failed")
result = {
    "all_passed": True,
    "exact_checks": 7,
    "scope": "finite complex matrix calibration only; no theta density, zeta packet, or RH certification",
    "sympy": s.__version__,
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result))
