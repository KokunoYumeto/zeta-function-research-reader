"""Verify the portable source closure; this does not certify mathematical claims."""
from pathlib import Path
import hashlib
import json
import re

root = Path(__file__).resolve().parent
manifest_path = root / "SOURCE_DEPENDENCIES.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
sha = lambda data: hashlib.sha256(data).hexdigest()
providers = {record["id"]: record for record in manifest["providers"]}

for record in providers.values():
    data = (root / record["staged"]).read_bytes()
    assert sha(data) == record["sha256"], record["staged"]
    assert len(data) == record["bytes"], record["staged"]

for record in manifest["proof_spans"]:
    original = (root / providers[record["provider"]]["staged"]).read_bytes()
    expected = original[record["start_byte"]:record["end_byte_exclusive"]]
    data = (root / record["staged"]).read_bytes()
    assert data == expected, record["staged"]
    assert sha(data) == record["sha256"], record["staged"]

entry = root / "Original_Observation_Addendum.tex"
inputs = re.findall(r"\\input\{([^}]+)\}", entry.read_text(encoding="utf-8"))
for relative in inputs:
    assert (root / relative).is_file(), relative
    assert str((root / relative).resolve()).startswith(str(root)), relative

result = {
    "source_sha256": providers["OPG"]["sha256"],
    "dependency_manifest_sha256": sha(manifest_path.read_bytes()),
    "entry_sha256": sha(entry.read_bytes()),
    "provider_hashes_verified": len(providers),
    "byte_exact_proof_spans_verified": len(manifest["proof_spans"]),
    "portable_entry_inputs_verified": inputs,
    "result": "PASS",
    "scope": "Byte preservation and portable input closure; mathematical acceptance is recorded separately in review/OPG_REVIEW.md.",
}
print(json.dumps(result, indent=2))
