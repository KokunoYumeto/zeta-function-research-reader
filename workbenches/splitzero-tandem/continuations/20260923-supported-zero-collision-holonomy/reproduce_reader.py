from pathlib import Path
import subprocess
root=Path(__file__).resolve().parent
for _ in range(3):
    subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error','SUPPORTED_ZERO_COLLISION_HOLONOMY.tex'],cwd=root,check=True)
