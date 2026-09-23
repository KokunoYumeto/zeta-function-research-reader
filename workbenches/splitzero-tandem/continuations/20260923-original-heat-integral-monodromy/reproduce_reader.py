from pathlib import Path
import subprocess
root=Path(__file__).resolve().parent
for _ in range(3):
    subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error','ORIGINAL_HEAT_MONODROMY_AND_TRACE_RESPONSES.tex'],cwd=root,check=True)
