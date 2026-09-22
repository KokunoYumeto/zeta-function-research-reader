"""Reproduce the diagrams, finite checks, and standalone LaTeX locally."""
from pathlib import Path
import shutil
import subprocess
import sys

root = Path(__file__).resolve().parent
pandoc = shutil.which("pandoc")
if not pandoc:
    raise SystemExit("Pandoc is required to generate the standalone TeX sources.")
for script in ("check_finite_models.py", "check_integer_corners.py",
               "check_prismatic_formulas.py", "check_chain_comparison.py", "check_frobenius_cross_effect.py", "draw_figures.py",
               "draw_integer_figures.py", "draw_prismatic_figures.py", "draw_chain_figure.py", "draw_retained_figures.py", "draw_node_figure.py", "draw_primitive_figure.py", "check_native_dual.py"):
    subprocess.run([sys.executable, str(root / script)], cwd=root, check=True)
stems=("COEFFICIENT_BRANCH", "FOUR_CORNERS_OVER_Z",
       "PRISMATIC_COMPARISON", "CHAIN_COMPARISON", "CROSS_EFFECTS",
       "HOMOTOPY_DEFECT", "FROBENIUS_CROSS_EFFECT", "NODE_COTANGENT", "MIXED_SUPPORT", "PRIMITIVE_DUAL_NUMBERS", "NATIVE_DUAL_NUMBER_RECEIVER", "IDEMPOTENT_DEFORMATION", "LITERATURE_AND_GCT_BRIDGE", "RECEIVERS")
def body(text):
    return text.split("---\n",2)[2] if text.startswith("---\n") else text
cumulative="# Identity Absorber Square — complete proofs\n\n"
for stem in stems:
    cumulative+="\n\n"+body((root/f"{stem}.md").read_text(encoding="utf-8"))
(root/"CUMULATIVE.md").write_text(cumulative,encoding="utf-8")
for stem in (*stems, "CUMULATIVE"):
    subprocess.run([pandoc, f"{stem}.md", "--from=markdown+tex_math_single_backslash",
                    "--standalone", "--toc", "-V", "geometry:margin=24mm",
                    "--include-in-header=TEX_HEADER.tex",
                    "-o", f"{stem}.tex"], cwd=root, check=True)
