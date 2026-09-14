from pathlib import Path
import re
import subprocess

base = Path("output/tau_f1_transcript_audit_2026-09-13/proofs/tau_exact_continuation")
common = ["pandoc", str(base.with_suffix(".md")),
          "--from=markdown+tex_math_single_backslash+raw_tex", "--to=latex"]
for standalone in (False, True):
    target = base.with_suffix(".tex") if standalone else Path(str(base) + "_fragment.tex")
    cmd = common + ["--output=" + str(target)]
    if standalone:
        cmd += ["--standalone", "--variable=geometry:margin=1in",
                "--variable=fontsize:11pt",
                "--include-in-header=work/tau_f1_transcript_audit_20260913/exact_continuation/latex_header.tex"]
    subprocess.run(cmd, check=True)
    s = target.read_text(encoding="utf-8")
    def wrap_code(m):
        body = m.group(1)
        if re.fullmatch("[0-9a-f]{64}", body):
            body = r"\allowbreak{}".join(body[i:i + 8] for i in range(0, 64, 8))
        elif "/" in body:
            body = body.replace("/", r"/\allowbreak{}").replace(r"\_", r"\_\allowbreak{}")
        return r"\texttt{" + body + "}"
    s = re.sub(r"\\texttt\{([^{}]*)\}", wrap_code, s)
    target.write_text(s, encoding="utf-8", newline="\n")
    print(target)
