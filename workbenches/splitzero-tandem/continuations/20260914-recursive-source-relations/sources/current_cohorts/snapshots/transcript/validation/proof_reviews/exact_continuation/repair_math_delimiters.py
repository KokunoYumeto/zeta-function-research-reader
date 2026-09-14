from pathlib import Path
import re

p = Path("output/tau_f1_transcript_audit_2026-09-13/proofs/tau_exact_continuation.md")
s = p.read_bytes().decode("utf-8")
print("Control characters:", [(repr(c), s.count(c)) for c in "\b\t\f\r" if c in s])
for i, c in enumerate(s):
    if c in "\b\t\f" or c == "\r" and (i + 1 == len(s) or s[i + 1] != "\n"):
        print("CONTROL", repr(s[max(0, i - 35):i + 45]))
s = s.replace("\r\n", "\n")
s = s.replace("\rho", r"\rho").replace("\tau", r"\tau").replace("\bar", r"\bar")
# The original source writer escaped display TeX but JavaScript consumed some
# inline delimiter escapes. Restore only balanced prose parentheses and the
# explicitly identified TeX commands; equation locators retain parentheses.
out = []
display = False
unescaped = {"Theta", "mathcal", "mathscr", "sum", "phi", "overline", "ell",
             "epsilon", "rho", "iota", "tau", "sigma", "eta", "bar"}
for line in s.splitlines():
    if line == r"\[":
        display = True
        out.append(line)
        continue
    if line == r"\]":
        display = False
        out.append(line)
        continue
    if display or line.startswith("#") or line.startswith(("title:", "author:", "date:", "---")):
        out.append(line)
        continue
    pos = 0
    repaired = ""
    while pos < len(line):
        start = line.find("(", pos)
        if start < 0:
            repaired += line[pos:]
            break
        depth = 1
        end = start + 1
        while end < len(line) and depth:
            if line[end] == "(":
                depth += 1
            elif line[end] == ")":
                depth -= 1
            end += 1
        if depth:
            raise ValueError(f"Unbalanced prose parenthesis: {line}")
        body = line[start + 1:end - 1]
        repaired += line[pos:start]
        if re.fullmatch(r"\d+(?:\.\d+)?", body):
            repaired += line[start:end]
        else:
            body = re.sub(r"(?<!\\)\b(" + "|".join(sorted(unescaped)) + r")\b",
                          lambda m: "\\" + m.group(1), body)
            repaired += r"\(" + body + r"\)"
        pos = end
    out.append(repaired)
p.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
print("Restored math delimiters:", p.read_text(encoding="utf-8").count(r"\("))
