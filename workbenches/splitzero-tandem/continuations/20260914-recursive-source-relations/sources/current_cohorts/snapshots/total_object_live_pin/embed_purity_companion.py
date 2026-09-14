"""Embed the complete independently authored PSC proof, preserving its bytes."""
from pathlib import Path
import hashlib
import json

base = Path(__file__).resolve().parent
main = base / "purity_amplification_match.tex"
companion = base / "phase_scaling_audit/phase_gluing_and_centered_energy.tex"
body = main.read_text(encoding="utf-8")
extra = companion.read_text(encoding="utf-8")
assert r"\input{" not in extra, "Companion must be complete, without hidden inputs."
start = "% BEGIN complete independently authored PSC companion"
end = "% END complete independently authored PSC companion"
if start in body:
    left, tail = body.split(start, 1)
    _, right = tail.split(end, 1)
    body = left + start + "\n" + extra.rstrip() + "\n" + end + right
else:
    marker = r"\subsection{The actual match to the amplification calculation}"
    assert body.count(marker) == 1
    body = body.replace(marker, start + "\n" + extra.rstrip() + "\n" + end
                        + "\n\n" + marker)
main.write_text(body, encoding="utf-8")
receipt = {
    "companion": str(companion),
    "companion_sha256": hashlib.sha256(companion.read_bytes()).hexdigest(),
    "main": str(main),
    "main_sha256": hashlib.sha256(main.read_bytes()).hexdigest(),
    "embedded_companion_matches": (
        body.split(start + "\n", 1)[1].split("\n" + end, 1)[0]
        == extra.rstrip()),
}
(base / "purity_companion_receipt.json").write_text(
    json.dumps(receipt, indent=2), encoding="utf-8")
print(json.dumps(receipt, indent=2))
