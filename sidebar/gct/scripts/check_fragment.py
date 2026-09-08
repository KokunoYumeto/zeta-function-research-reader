"""Compile the delivered body and bibliography in an isolated minimal wrapper."""
from pathlib import Path
import subprocess,json,re,hashlib
ROOT=Path(__file__).resolve().parents[1]
folder=ROOT/'build/fragment_check'
folder.mkdir(parents=True,exist_ok=True)
body=(ROOT/'complete_proof_fragment.tex').read_text(encoding='utf-8')
assert not re.search(r'\\(?:input|include)\{',body), 'Body must contain all proof text'
labels=re.findall(r'\\label\{([^}]+)\}',body)
assert len(labels)==len(set(labels)), 'Duplicate label'
(folder/'fragment.tex').write_text(body,encoding='utf-8')
(folder/'references.bib').write_bytes((ROOT/'complete_bibliography.bib').read_bytes())
wrapper=r'''\documentclass[11pt,a4paper]{article}
\usepackage[margin=27mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern,amsmath,amssymb,amsthm,booktabs,hyperref,mathrsfs}
\newtheorem{proposition}{Proposition}[section]
\newtheorem{theorem}[proposition]{Theorem}
\newtheorem{lemma}[proposition]{Lemma}
\newtheorem{corollary}[proposition]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[proposition]{Definition}
\newtheorem{remark}[proposition]{Remark}
\setlength{\emergencystretch}{2em}
\begin{document}
\input{fragment.tex}
\bibliographystyle{plain}
\bibliography{references}
\end{document}
'''
(folder/'wrapper.tex').write_text(wrapper,encoding='utf-8')
commands=[['pdflatex','-interaction=nonstopmode','-halt-on-error','wrapper.tex'],
          ['bibtex','wrapper'],
          ['pdflatex','-interaction=nonstopmode','-halt-on-error','wrapper.tex'],
          ['pdflatex','-interaction=nonstopmode','-halt-on-error','wrapper.tex']]
runs=[]
for i,command in enumerate(commands):
    process=subprocess.run(command,cwd=folder,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    output=process.stdout.decode('utf-8',errors='replace')
    (folder/f'step-{i}.txt').write_text(output,encoding='utf-8')
    runs.append({'command':command,'exit_code':process.returncode})
    if process.returncode:
        print(output[-7000:]); raise SystemExit(process.returncode)
log=(folder/'wrapper.log').read_text(encoding='utf-8',errors='replace')
warnings=[x for x in log.splitlines() if any(t in x for t in ['Overfull','undefined','multiply defined','LaTeX Warning'])]
receipt={'all_passed':not warnings,
         'fragment_sha256':hashlib.sha256((ROOT/'complete_proof_fragment.tex').read_bytes()).hexdigest(),
         'logical_text_sha256':hashlib.sha256(body.encode()).hexdigest(),
         'no_external_inputs':True,'unique_labels':len(labels),'wrapper':wrapper,'runs':runs,'warnings':warnings}
(ROOT/'checks/fragment.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt))
if warnings: raise SystemExit(1)
