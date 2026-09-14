from pathlib import Path
import subprocess,shutil
root=Path(__file__).resolve().parent
build=root/'build'
build.mkdir(exist_ok=True)
for step in range(3):
    subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','-output-directory='+str(build),'Tau_Relation_Window_Spectral_Transport.tex'],cwd=root,check=True)
shutil.copyfile(build/'Tau_Relation_Window_Spectral_Transport.pdf',root/'Tau_Relation_Window_Spectral_Transport.pdf')
