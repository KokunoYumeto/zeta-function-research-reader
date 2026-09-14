"""Static validation and final source receipt; does not compile or render TeX."""
from pathlib import Path
import hashlib
import json
import re

base = Path(__file__).resolve().parent
target = base / "arithmetic_gluing.tex"
source = target.read_text(encoding="utf-8")
stack = []
for match in re.finditer(r"\\(begin|end)\{([^}]+)\}", source):
    kind, environment = match.groups()
    if kind == "begin":
        stack.append(environment)
    else:
        assert stack and stack.pop() == environment, (kind, environment)
assert not stack

balance = 0
for index, character in enumerate(source):
    if character not in "{}":
        continue
    backslashes = 0
    previous = index - 1
    while previous >= 0 and source[previous] == "\\":
        backslashes += 1
        previous -= 1
    if backslashes % 2 == 0:
        balance += 1 if character == "{" else -1
    assert balance >= 0, index
assert balance == 0
tags = re.findall(r"\\tag\{([^}]+)\}", source)
assert len(tags) == len(set(tags))
record = {
    "file": target.name,
    "line_count": len(source.splitlines()),
    "equation_tags": tags,
    "balanced_braces": True,
    "balanced_environments": True,
    "sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
    "independent_receipt_sha256": hashlib.sha256(
        (base / "divisor_review.md").read_bytes()
    ).hexdigest(),
    "pdf_build": "root-owned; this check does not compile or render",
}
(base / "ARITHMETIC_GLUING_STATIC_CHECK.json").write_text(
    json.dumps(record, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps({k: v for k, v in record.items() if k != "equation_tags"}, indent=2))
