from pathlib import Path
import re

p = Path("output/tau_f1_transcript_audit_2026-09-13/proofs/tau_exact_continuation.md")
s = p.read_text(encoding="utf-8")
s = s.replace("\bigotimes", r"\bigotimes")
def fix(m):
    return r"\(" + re.sub(r"(?<![\\A-Za-z])(alpha|ell|epsilon|prod|psi)(?=[^A-Za-z]|$)",
                          lambda t: "\\" + t.group(1), m.group(1)) + r"\)"
s = re.sub(r"\\\((.*?)\\\)", fix, s)
s = s.replace(r"\mathscr B_Z", r"\mathscr K_Z")
s = s.replace(r"\nu_\rho(z)", r"u_\rho(z)")
if any(ord(c) < 32 and c != "\n" for c in s):
    raise ValueError("Unintended control character remains")
p.write_text(s, encoding="utf-8", newline="\n")
print("Balanced inline math:", s.count(r"\("), s.count(r"\)"))
print("Balanced display math:", s.count(r"\["), s.count(r"\]"))
print("Unescaped multiple-letter tokens in inline math:")
print(sorted(set(t for m in re.finditer(r"\\\((.*?)\\\)", s)
                 for t in re.findall(r"(?<![A-Za-z\\])[A-Za-z]{2,}", m.group(1)))))
