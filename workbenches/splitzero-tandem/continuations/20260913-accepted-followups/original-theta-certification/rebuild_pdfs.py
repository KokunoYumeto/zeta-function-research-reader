from pathlib import Path
import subprocess
from pypdf import PdfWriter
root=Path(__file__).resolve().parent
for folder,engine,entry,target in [
 (root,"pdflatex","Tau_Theta_Hankel_Certification.tex","Tau_Theta_Hankel_Certification.pdf"),
 (root/"support_reader","lualatex","main.tex","Original_Theta_Hankel_Complete_Proofs.pdf")]:
 build=folder/"build";build.mkdir(exist_ok=True)
 for _ in range(2):
  subprocess.run([engine,"-interaction=nonstopmode","-halt-on-error","-output-directory=build",entry],cwd=folder,check=True)
 generated=build/(Path(entry).stem+".pdf")
 (folder/target).write_bytes(generated.read_bytes())
writer=PdfWriter()
writer.append(str(root/"Tau_Theta_Hankel_Certification.pdf"),outline_item="Original theta moments and finite certification")
writer.append(str(root/"support_reader/Original_Theta_Hankel_Complete_Proofs.pdf"),outline_item="Complete original sources and independent proofs")
with (root/"Tau_Theta_Hankel_Complete_Proofs.pdf").open("wb") as f: writer.write(f)
