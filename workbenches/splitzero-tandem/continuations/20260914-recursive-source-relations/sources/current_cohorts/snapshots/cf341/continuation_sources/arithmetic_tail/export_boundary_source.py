"""Export the reviewed local boundary proof and internal Binet proof to TeX.

The source mathematics is retained verbatim before Pandoc's math-preserving
conversion. Only process/provenance paragraphs are omitted from public prose;
the original markdown files remain in the proof directory.
"""
from pathlib import Path
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("--binet", type=Path, required=True)
args = parser.parse_args()
base = Path(__file__).resolve().parent
boundary = (base / "tilt_audit/ACTUAL_BOUNDARY_TILT.md").read_text(encoding="utf-8-sig")
boundary = boundary.split("## Work record and scope", 1)[0].rstrip()
boundary = "\n".join(
    line for line in boundary.splitlines()
    if not line.startswith("Local originals inspected:")
)
boundary = boundary.replace(
    "The adjacent complete Binet calculation proves",
    "The complete Binet calculation included below proves",
).replace(
    "For the parent's subsequent comparison, one direct corollary is",
    "For the retained source comparison, one direct corollary is",
)
binet = args.binet.read_text(encoding="utf-8-sig")
binet = binet.split("## Provenance and independence", 1)[0].rstrip()
body = boundary + "\n\n" + binet.strip() + "\n"
public_md = base / "boundary_tilt_full_public.md"
tex = base / "boundary_tilt_full.tex"
public_md.write_text(body, encoding="utf-8")
subprocess.run([
    "pandoc", str(public_md),
    "--from=markdown+raw_tex+tex_math_single_backslash",
    "--to=latex", "--wrap=none", "--output", str(tex),
], check=True)
print(tex)
