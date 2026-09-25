from pathlib import Path
import subprocess
folder=Path(__file__).resolve().parent
for _ in range(2):
    subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error','CUMULATIVE_ALGEBRA.tex'],cwd=folder,check=True)
