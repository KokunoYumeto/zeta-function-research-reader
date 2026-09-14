from pathlib import Path
import subprocess,shutil
root=Path(__file__).resolve().parent
build=root/'build'
build.mkdir(exist_ok=True)
for step in range(3):
    subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','-output-directory='+str(build),'Tau_Theta_Hankel_Certification.tex'],cwd=root,check=True)
shutil.copyfile(build/'Tau_Theta_Hankel_Certification.pdf',root/'Tau_Theta_Hankel_Certification.pdf')
