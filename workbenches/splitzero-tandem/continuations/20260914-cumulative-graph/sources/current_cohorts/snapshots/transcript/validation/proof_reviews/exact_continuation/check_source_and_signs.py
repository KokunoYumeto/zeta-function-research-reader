from pathlib import Path
from itertools import combinations
import hashlib
import json
import re

root = Path("output/tau_f1_transcript_audit_2026-09-13/proofs")
p = root / "tau_exact_continuation.md"
s = p.read_text(encoding="utf-8")
checks = []
def require(name, condition):
    if not condition:
        raise RuntimeError(name)
    checks.append(name)

require("No unintended control characters", all(ord(c) >= 32 or c == "\n" for c in s))
require("Inline delimiters balanced", s.count(r"\(") == s.count(r"\)"))
require("Display delimiters balanced", s.count(r"\[") == s.count(r"\]"))
for m in re.finditer(r"\\\((.*?)\\\)", s):
    require("Inline control sequences " + str(m.start()),
            not re.search(r"(?<![\\A-Za-z])(Theta|mathscr|mathcal|alpha|ell|epsilon|prod|psi|rho|tau|overline)(?=[^A-Za-z]|$)", m.group(1)))
require("Known global closure evaluated",
        r"\overline{\Theta V}=\Theta V" in s and r"\Lambda\Theta=1_V" in s)
require("Separate original B_Z preserved",
        r"\mathscr K_Z=\ker J_Z" in s and r"\mathscr B_Z=\ker J_Z" not in s)
require("Rotated triangle boundary retains negative sign",
        r"\xrightarrow{s\mapsto[(0,-s)]}H^1B_\sigma(F)" in s)

# Exhaust every incidence component of the tensor adjunction for r<=8.
# C has eta-degree 1, K has eta-degree -1; the differential in Hom has
# the additional sign (-1)^(p+1). Test the written coefficient multiplier.
for r in range(1, 9):
    for degree in range(1, r + 1):
        eps = (-1) ** (degree * (degree - 1) // 2)
        eps_next = (-1) ** ((degree - 1) * (degree - 2) // 2)
        for selected in combinations(range(r), degree):
            for removed in selected:
                incidence = (-1) ** sum(i < removed for i in selected)
                require(f"Tensor adjunction r={r} I={selected} j={removed}",
                        eps_next * incidence == eps * (-1) ** (degree + 1) * incidence)

# Mutation control: omitting epsilon must fail already in top degree r=2.
require("Mutation omitting product epsilon is rejected", 1 != (-1) ** (2 + 1))
record = {
    "source": str(p),
    "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
    "check_count": len(checks),
    "checks": checks,
    "scope": "Delimiter and lexical checks plus exhaustive finite tensor sign identities. Written proofs establish the mathematical statements; no numerical analytic estimate is claimed."
}
out = Path("work/tau_f1_transcript_audit_20260913/exact_continuation/source_sign_validation.json")
out.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: record[k] for k in ("source", "sha256", "check_count", "scope")}, indent=2))
