from pathlib import Path
import subprocess,shutil
root=Path(__file__).resolve().parent
build=root/"build"
build.mkdir(exist_ok=True)
for _ in range(2):
    subprocess.run(["lualatex","-interaction=nonstopmode","-halt-on-error","-file-line-error","-output-directory=build","main.tex"],cwd=root,check=True)
shutil.copyfile(build/"main.pdf",root/"Tau_Actual_Source_and_Metric_Addendum.pdf")
