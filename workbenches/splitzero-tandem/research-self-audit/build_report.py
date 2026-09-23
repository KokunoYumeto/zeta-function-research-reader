"""Build the research self-audit from its two Markdown sources.

Requires Python 3, Pandoc, and a LaTeX distribution providing pdflatex.
The generated TeX and PDF contain the report and its evidence register.
"""
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent
name = "RESEARCH_SELF_AUDIT"
report = (ROOT / f"{name}.md").read_text(encoding="utf-8")
evidence = (ROOT / "EVIDENCE_REGISTER.md").read_text(encoding="utf-8")
combined = report + "\n\n\\clearpage\n\n" + evidence
# Retain the mathematical content; use portable punctuation for the PDF.
combined = combined.replace("\u2011", "-").replace("\u2013", "-").replace("\u2014", " - ")
for executable in ("pandoc", "pdflatex"):
    if shutil.which(executable) is None:
        raise RuntimeError(f"Required executable missing: {executable}")

with tempfile.TemporaryDirectory(prefix="research-audit-") as scratch:
    work = Path(scratch)
    src = work / "combined.md"
    src.write_text(combined, encoding="utf-8")
    header = work / "header.tex"
    header.write_text(r"""\usepackage{microtype}
\setlength{\emergencystretch}{4em}
\allowdisplaybreaks[2]
\setcounter{tocdepth}{1}
""", encoding="utf-8")
    tex = ROOT / f"{name}.tex"
    subprocess.run([
        "pandoc", str(src), "--from=markdown+tex_math_dollars", "--to=latex",
        "--standalone", "--output", str(tex), "--include-in-header", str(header),
        "-V", "documentclass=article", "-V", "fontsize=11pt",
        "-V", "papersize=a4", "-V", "geometry:margin=24mm",
        "-V", "colorlinks=true", "-V", "urlcolor=blue", "-V", "linkcolor=blue",
    ], check=True)
    for _ in range(2):
        result = subprocess.run([
            "pdflatex", "-interaction=nonstopmode", "-halt-on-error",
            f"-output-directory={work}", str(tex),
        ], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
        if result.returncode:
            raise RuntimeError(result.stdout.decode("utf-8",errors="replace")[-10000:])
    output = ROOT / f"{name}.pdf"
    shutil.copyfile(work / f"{name}.pdf", output)
    log = (work / f"{name}.log").read_text(encoding="utf-8",errors="replace")
    issues = [s for s in log.splitlines() if "Overfull" in s or "Missing character" in s or "Warning" in s]
    print(f"Created {output.name} ({output.stat().st_size} bytes)")
    print("Layout/build notices:", issues)
