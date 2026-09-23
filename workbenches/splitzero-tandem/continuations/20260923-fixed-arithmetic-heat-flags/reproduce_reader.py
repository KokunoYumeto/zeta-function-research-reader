from pathlib import Path
import subprocess
p=Path(__file__).resolve().parent
for _ in range(2):
    subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error','FIXED_ARITHMETIC_HEAT_FLAGS.tex'],cwd=p,check=True)
