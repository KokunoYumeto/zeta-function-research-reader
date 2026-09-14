from pathlib import Path
import subprocess, json, hashlib, re
R=Path(r"workspace:\work\backpropagation_20260913\metric")
B=R/"compile"
B.mkdir(exist_ok=True)
parts=["tex/next_edition/AT_complete.tex","tex/next_edition/AW_complete.tex",
       "tex/tau_signed_projection_control.tex","tex/periodized_source_intake_proofs.tex",
       "tex/periodized_curvature_control_bridge.tex"]
preamble=r"""\documentclass[11pt,a4paper]{article}
\usepackage[margin=24mm]{geometry}
\usepackage{fontspec}
\setmainfont{Cambria}
\usepackage{amsmath,amssymb,amsthm,mathrsfs,mathtools}
\usepackage[unicode]{hyperref}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{remark}[theorem]{Remark}
\providecommand{\C}{\mathbb C}
\providecommand{\Tr}{\operatorname{Tr}}
\allowdisplaybreaks
\setlength{\emergencystretch}{3em}
\begin{document}
"""
body="".join("\\input{"+(R/"staged"/p).as_posix()+"}\n" for p in parts)
tex=B/"METRIC_PATCHES.tex"
tex.write_text(preamble+body+"\\end{document}\n",encoding="utf-8")
exe=r"runtime:tex\miktex\bin\x64\lualatex.exe"
runs=[]
for i in range(2):
    proc=subprocess.run([exe,"-interaction=nonstopmode","-halt-on-error",tex.name],
                        cwd=B,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    (B/f"run{i+1}.txt").write_bytes(proc.stdout)
    runs.append(dict(run=i+1,returncode=proc.returncode))
    if proc.returncode: break
log=(B/"METRIC_PATCHES.log").read_text(encoding="utf-8",errors="replace")
rec=dict(runs=runs,source_files=parts,
   errors=[s for s in log.splitlines() if s.startswith("!") or "Undefined control sequence" in s],
   undefined_references=[s for s in log.splitlines() if "undefined" in s.lower() and "Font" not in s],
   font_warnings=[s for s in log.splitlines() if "Font Warning" in s],
   overfull=[s for s in log.splitlines() if "Overfull" in s],
   pdf_sha256=hashlib.sha256((B/"METRIC_PATCHES.pdf").read_bytes()).hexdigest() if (B/"METRIC_PATCHES.pdf").exists() else None)
(B/"VALIDATION.json").write_text(json.dumps(rec,indent=2),encoding="utf-8")
print(json.dumps(rec,indent=2))
