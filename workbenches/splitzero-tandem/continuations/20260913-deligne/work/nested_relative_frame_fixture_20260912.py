"""One exact original-coordinate nested relative-frame calibration.

This is a finite-dimensional calibration, not a replacement for the analytic
proof. No TeX, build, frozen edition, or publication stage is edited.
"""
from pathlib import Path
import hashlib
import json
import sys

import sympy as sp


OUT = Path(__file__).resolve().with_suffix("")
u = sp.symbols("u", real=True)
I = sp.I
p = 1 + u
q = 1 + u + u**2
jL = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1],
                [p, 2*p, -p], [2*q, -q, q]])
E = sp.Matrix([[1, 0], [0, 1], [1, 1]])
jM = jL * E
dL = jL.diff(u)
dM = jM.diff(u)
WL = jL.H * jL
WM = jM.H * jM
BL = jL.H * dL
BM = jM.H * dM
GL = WL.inv() * BL
GM = WM.inv() * BM
PL = jL * WL.inv() * jL.H
PM = jM * WM.inv() * jM.H
NL = (sp.eye(5) - PL) * dL
NM = (sp.eye(5) - PM) * dM
A = (PL - PM) * dM
R = NL * E
K = GL * E - E * GM


def exact(matrix):
    """Complete exact rational-function arithmetic, without changing frames."""
    return matrix.applyfunc(sp.cancel)


def is_zero(matrix):
    return all(sp.cancel(entry) == 0 for entry in matrix)


records = []


def equal(name, left, right):
    ok = is_zero(left - right)
    records.append({"name": name, "passed": ok})
    if not ok:
        raise RuntimeError(f"Exact identity failed: {name}: {exact(left-right)}")


def nonzero(name, value):
    ok = not is_zero(value)
    records.append({"name": name, "passed": ok})
    if not ok:
        raise RuntimeError(f"Required nonzero witness vanished: {name}")


equal("original weighted inclusion", WM, E.H * WL * E)
equal("original fixed-phase larger-frame B", BL, WL.diff(u) / 2)
equal("original fixed-phase smaller-frame B", BM, WM.diff(u) / 2)
equal("direct projector nesting", PL * PM, PM)
equal("larger projector Hermitian", PL.H, PL)
equal("smaller projector Hermitian", PM.H, PM)
equal("normal derivative partition", NM, A + R)
equal("orthogonal normal summands", A.H * R, sp.zeros(2))
equal("connection weighted compression", GM, WM.inv() * E.H * WL * GL * E)
equal("transition coefficient embedding", A, jL * K)
equal("transition coefficient W-orthogonality", E.H * WL * K, sp.zeros(2))
equal("complete normal Gram partition", NM.H * NM, R.H * R + K.H * WL * K)

c = sp.Matrix([1 + I*u, u**2 - I])
dc = c.diff(u)
original_derivative = (jM * c).diff(u)
tangent = jM * (dc + GM * c)
transition = A * c
remaining = R * c
equal("complete original coefficient derivative", original_derivative,
      tangent + transition + remaining)
equal("tangent orthogonal to transition", tangent.H * transition, sp.zeros(1))
equal("tangent orthogonal to remaining", tangent.H * remaining, sp.zeros(1))
equal("complete coefficient derivative energy", original_derivative.H * original_derivative,
      tangent.H * tangent + transition.H * transition + remaining.H * remaining)

sample = lambda matrix: exact(matrix.subs(u, 1))
nonzero("larger weight non-even at u=1", WL.subs(u, 1) - WL.subs(u, -1))
nonzero("smaller weight non-even at u=1", WM.subs(u, 1) - WM.subs(u, -1))
nonzero("larger weights do not commute between u=0 and u=1",
        WL.subs(u, 0) * WL.subs(u, 1) - WL.subs(u, 1) * WL.subs(u, 0))
nonzero("smaller weights do not commute between u=0 and u=1",
        WM.subs(u, 0) * WM.subs(u, 1) - WM.subs(u, 1) * WM.subs(u, 0))
nonzero("transition derivative nonzero at u=1", sample(A))
nonzero("remaining normal derivative nonzero at u=1", sample(R))
nonzero("transition coefficient energy nonzero at u=1", sample(transition.H * transition))
nonzero("remaining coefficient energy nonzero at u=1", sample(remaining.H * remaining))


def encode(matrix):
    return [[str(entry) for entry in row] for row in matrix.tolist()]


symbolic = {
    "j_L": jL, "E": E, "j_M": jM, "j_L_prime": dL,
    "j_M_prime": dM, "W_L": WL, "W_M": WM,
    "B_L": BL, "B_M": BM, "c": c, "c_prime": dc,
    "original_coefficient_derivative": original_derivative,
}
at_one = {
    "j_L": jL, "j_M": jM, "W_L": WL, "W_M": WM,
    "B_L": BL, "B_M": BM, "Gamma_L": GL, "Gamma_M": GM,
    "Pi_L": PL, "Pi_M": PM, "A": A, "N_L_E": R, "N_M": NM,
    "K": K, "A_star_A": A.H*A, "E_star_N_L_star_N_L_E": R.H*R,
    "N_M_star_N_M": NM.H*NM, "original_coefficient_derivative": original_derivative,
    "tangent_vector": tangent, "transition_vector": transition, "remaining_vector": remaining,
    "original_energy": original_derivative.H*original_derivative,
    "tangent_energy": tangent.H*tangent, "transition_energy": transition.H*transition,
    "remaining_energy": remaining.H*remaining,
    "weight_commutator_L_0_1": WL.subs(u, 0)*WL-WL*WL.subs(u, 0),
    "weight_commutator_M_0_1": WM.subs(u, 0)*WM-WM*WM.subs(u, 0),
}
result = {
    "title": "Original-coordinate nested relative-frame exact fixture",
    "scope": "One polynomial family with r_L=3, r_M=2, ambient dimension 5; all rational identities hold for every real u. No arithmetic density or uniform analytic bound is asserted.",
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "python": sys.version.split()[0], "sympy": sp.__version__,
    "optimized_python": not __debug__,
    "dimensions": {"ambient": 5, "larger": 3, "smaller": 2},
    "domains": "j_L(u): C^3 -> C^5; E: C^2 -> C^3; j_M(u): C^2 -> C^5; u in R; ambient standard Hermitian product; coefficient weights W_L and W_M are retained exactly.",
    "symbolic_original_data": {name: encode(mat) for name, mat in symbolic.items()},
    "sample_u_1": {name: encode(sample(mat)) for name, mat in at_one.items()},
    "checks": records,
    "check_count": len(records),
    "passed": all(row["passed"] for row in records),
}
suffix = "_optimized.json" if not __debug__ else ".json"
destination = OUT.with_name(OUT.name + suffix)
destination.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"output": destination.name, "checks": len(records), "passed": result["passed"],
                  "sample_energy": result["sample_u_1"]["original_energy"],
                  "energy_parts": {name: result["sample_u_1"][name] for name in
                                   ["tangent_energy", "transition_energy", "remaining_energy"]}}))
