"""Rebuild the three complete readers from the distributed editable LaTeX."""
from pathlib import Path
import subprocess
root=Path(__file__).resolve().parent
for lane in ('gct','identity','counterfactual'):
    for _ in range(3):
        subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error','CONTINUATION.tex'],cwd=root/lane,check=True)
