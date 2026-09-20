"""Bounded independent mathematical checks; never rewrite the main receipt."""
from pathlib import Path
import hashlib
import json
import sys

root = Path(__file__).resolve().parents[1]
source_path = root / "certify_real_pair.py"
source = source_path.read_text(encoding="utf-8")
receipt = json.loads((root / "REAL_PAIR_CERTIFICATE.json").read_text(encoding="utf-8"))
assert hashlib.sha256(source_path.read_bytes()).hexdigest() == receipt["script_sha256"]
# Reuse only the arithmetic and exact formula evaluation, before its file writer.
scope = {"__file__": str(source_path), "__name__": "reviewed_arithmetic"}
sys.argv = [str(source_path)]
exec(compile(source.split("def txt(v):", 1)[0], str(source_path), "exec"), scope)
arb, acb, acb_mat = (scope[k] for k in ("arb", "acb", "acb_mat"))
Rbox = scope["matrix"](scope["box"])[0]
Rcenter = scope["Rc"]
inv_center = Rcenter.inv()
B = acb_mat([[acb(inv_center[i,j].real.mid(), inv_center[i,j].imag.mid())
              for j in range(4)] for i in range(4)])
defect = scope["Id"] - B*Rbox
rowbounds = [sum((defect[i,j].abs_upper() for j in range(4)), arb(0))
             for i in range(4)]
assert all(v < 1 for v in rowbounds)
checks = scope["checks"]
assert all(checks.values())
P = scope["P"]
assert all(P[i,j].rad().is_zero() for i in range(2) for j in range(2))
assert scope["box"].real > 0
assert 1+scope["xinterval"].real**2 > 3
assert scope["c"] > 82176
assert scope["bx"] > 34.96
assert scope["dreal"] > 3382
assert scope["exception"] < -5695694
assert all(v < arb("0.000002") for v in scope["inclusion"])
print(json.dumps({
    "script_sha256": receipt["script_sha256"],
    "status": "REVIEWED_COMPLETE_REAL_PAIR_ROOT",
    "complete_R_neumann_rows": [str(v) for v in rowbounds],
    "exact_dyadic_P_entries": True,
    "positive_real_period": str(1/scope["box"].real),
    "unit_denominator": str(1+scope["xinterval"].real**2),
    "centre_z_radius": str(scope["center"].real.rad()),
    "centre_x_radius": str(scope["xc"].rad()),
    "requested_radius_enclosure": str(scope["radius"]),
    "actual_period_box_radius": str(scope["box"].real.rad()),
    "weighted_self_map_rows": [str(v) for v in scope["inclusion"]],
    "original_checks": checks,
}, indent=2))
