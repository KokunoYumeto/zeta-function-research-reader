"""Source-level TeX checks; no rendering or publication."""

from pathlib import Path
import hashlib
import re

root = Path(__file__).resolve().parent
main = root / "DEBRUIJN_THETA_TRANSPORT.tex"
fragment = root / "weighted_theta" / "WEIGHTED_THETA_METRIC_SECTIONS.tex"
contents = []


def require(condition, message):
    if not condition:
        raise RuntimeError(str(message))


for source in [main, fragment]:
    text = source.read_text(encoding="utf-8")
    require(not any(ord(c) < 32 and c not in "\n\r\t" for c in text), source)
    require(not re.search(r"\bpl" + r"ain\b", text, re.I), source)
    stripped = re.sub(r"(?<!\\)%[^\n]*", "", text)
    stack = []
    for match in re.finditer(r"\\(begin|end)\{([^}]+)\}", stripped):
        direction, name = match.groups()
        if direction == "begin":
            stack.append(name)
        else:
            require(bool(stack) and stack.pop() == name, (source, name, match.start()))
    require(not stack, (source, stack))
    braces = 0
    for match in re.finditer(r"(?<!\\)[{}]", stripped):
        braces += 1 if match.group() == "{" else -1
        require(braces >= 0, (source, match.start()))
    require(braces == 0, (source, braces))
    contents.append(text)
    print("PASS:", source.name, "environment nesting, braces, controls, and vocabulary")

combined = "\n".join(contents)
labels = re.findall(r"\\label\{([^}]+)\}", combined)
require(len(labels) == len(set(labels)), "Duplicate labels")
refs = set(re.findall(r"\\(?:eqref|ref)\{([^}]+)\}", combined))
require(refs.issubset(set(labels)), sorted(refs - set(labels)))
cites = {key.strip() for group in re.findall(r"\\cite\{([^}]+)\}", combined)
         for key in group.split(",")}
bibitems = set(re.findall(r"\\bibitem\{([^}]+)\}", combined))
require(cites.issubset(bibitems), sorted(cites - bibitems))
require("pairwise disjoint closed interiors" in combined, "Missing contour-domain requirement")
print("PASS: all", len(labels), "labels unique, all references and citations resolved")
for source in [main, fragment, root / "exact_tests.py", root / "static_checks.py"]:
    print("SHA256:", source.relative_to(root), hashlib.sha256(source.read_bytes()).hexdigest())
