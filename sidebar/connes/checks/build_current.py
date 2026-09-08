"""Build sequentially under the existing one-worker Windows job policy."""
from pathlib import Path
import ast
import ctypes
import os
import subprocess

ROOT=Path(__file__).resolve().parents[1]
tree=ast.parse((ROOT/"checks"/"verify_exact.py").read_text(encoding="utf-8"))
node=next(n for n in tree.body if isinstance(n,ast.FunctionDef)
          and n.name=="install_memory_ceiling")
exec(compile(ast.Module(body=[node],type_ignores=[]),"<resource policy>","exec"))
resource=install_memory_ceiling()
for run in range(2):
    result=subprocess.run(["pdflatex","-interaction=nonstopmode","-halt-on-error",
                           "main.tex"],cwd=ROOT/"tex",capture_output=True,text=True)
    if result.returncode:
        print(result.stdout[-6500:])
        raise SystemExit(result.returncode)
print("Two sequential TeX builds completed under the recorded memory policy.")
