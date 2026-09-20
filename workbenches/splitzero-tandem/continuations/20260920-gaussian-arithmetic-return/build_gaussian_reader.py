from pathlib import Path
import subprocess,json,re,hashlib,shutil
from datetime import datetime,timezone
P=Path(__file__).parent
native=(P/'NATIVE_GAUSSIAN_TRANSFER.tex').read_text(encoding='utf-8')
gm_file=P/'GAUSSIAN_EQUILIBRIUM_MOMENTS.tex'
if not gm_file.exists():gm_file=P/'independent_moments/GAUSSIAN_EQUILIBRIUM_MOMENTS.tex'
gm=gm_file.read_text(encoding='utf-8')
gm_body=gm.split('\\begin{document}\\maketitle',1)[1].split('\\end{document}',1)[0]
figure=r'''
\clearpage
\begin{figure}[p]\centering
\includegraphics[width=\textwidth,height=.78\textheight,keepaspectratio]{GAUSSIAN_NATIVE_MECHANISM.png}
\caption{The exact mechanism, with the original source and relation masses.
The curves evaluate NG10 and NG20 at $s=1$; their numerical samples
illustrate the proved density, while GM17 proves positivity exactly.
The singularity at zero is integrable. The original observation conclusion
uses $m_0=1$ and the proved five-orbit domain $|u|\ge R_*$, as in NG24.
The four original cutoffs and signs feed NG27; in the lower panel
$I_s=-H_s'(1/1024)$, distinct from the Bessel function in NG25. Human formula sources
are Koornwinder et al.\ \cite{dlmf}, Forrester's treatment of
Andr\'eief \cite{forrester}, and Carlson \cite{Carlson}.}
\end{figure}\clearpage
'''
combined=native.replace('\\begin{thebibliography}{9}',figure+'\\begin{thebibliography}{9}',1)
combined=combined.replace('\\end{document}','\\clearpage\n\\appendix\n\\section*{Complete independent endpoint and sign derivation}\n'+gm_body+'\n\\end{document}')
combined=combined.replace('This note proves\nneither that convergence nor the individual projected phase signs.', 'This independent appendix proves neither that convergence nor the individual projected phase signs. Sections 1--5 of the present reader supply the spectral transfer on the precise observation domain NG24.')
combined=combined.replace('\\texttt{44b9591515c12b07d065f8a4fc4b3b9dd9c30b5c85f334b70d325aaeaf0880ac}',r'\nolinkurl{44b9591515c12b07d065f8a4fc4b3b9dd9c30b5c85f334b70d325aaeaf0880ac}')
combined=combined.replace('received 20 September 2026, SHA256\n'+r'\nolinkurl{44b9591515c12b07d065f8a4fc4b3b9dd9c30b5c85f334b70d325aaeaf0880ac}.','received 20 September 2026. Exact source SHA256 is recorded in the accompanying reading ledger.')
bibliographies=re.findall(r'\\begin\{thebibliography\}\{9\}(.*?)\\end\{thebibliography\}',combined,flags=re.S)
combined=re.sub(r'\\begin\{thebibliography\}\{9\}.*?\\end\{thebibliography\}','',combined,flags=re.S)
combined=combined.replace('\\end{document}', '\\clearpage\n\\begin{thebibliography}{9}\n'+'\n'.join(bibliographies)+'\n\\end{thebibliography}\n\\end{document}')
(P/'GAUSSIAN_ARITHMETIC_RETURN.tex').write_text(combined,encoding='utf-8')
logs=[]
for run in range(2):
 r=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','GAUSSIAN_ARITHMETIC_RETURN.tex'],cwd=P,capture_output=True,text=True)
 logs.append(r.stdout)
 if r.returncode:
  print(r.stdout[-6000:]);raise SystemExit(r.returncode)
(P/'BUILD_STDOUT.txt').write_text('\n'.join(logs),encoding='utf-8')
warnings=[s for s in logs[-1].splitlines() if any(x in s for x in ['Overfull','Underfull','Warning','Output written'])]
print('\n'.join(warnings))
qa=P/'qa';qa.mkdir(exist_ok=True)
r=subprocess.run(['pdftoppm','-r','85','-png',str(P/'GAUSSIAN_ARITHMETIC_RETURN.pdf'),str(qa/'page')],capture_output=True,text=True)
if r.returncode:raise RuntimeError(r.stderr)
print(json.dumps({'pages':len(list(qa.glob('page-*.png'))),'render_folder':str(qa)}))
