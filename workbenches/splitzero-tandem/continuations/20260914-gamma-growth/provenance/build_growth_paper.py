"""Build the current complete Gamma growth supplement with literal source copies."""
from pathlib import Path
import hashlib,json,shutil,subprocess

work=Path(__file__).resolve().parent
outer=Path(r'C:\Users\[[user]]\Documents\math\output\Split_Zero_Mixed_Boundary_Continuation_2026-09-14')
prior=outer/'20_COMPLETE_GAMMA_RETURN'
out=outer/'21_GAMMA_GROWTH'
out.mkdir(exist_ok=True)
for name in ['sources','dependencies','originals','provenance']:
    shutil.copytree(prior/name,out/name,dirs_exist_ok=True)
new=out/'sources'/'growth';new.mkdir(exist_ok=True)
mapping={
 'WGP.tex':work/'original_product_expansion.tex',
 'RWB.tex':work/'recurrence_bounds.tex',
 'EIQ.tex':work/'equilibrium'/'independent'/'EXACT_SQRT_LOG_EQUILIBRIUM.tex',
 'GEL.tex':work/'equilibrium'/'GAMMA_ENSEMBLE_LEADING_RETURN.tex',
 'WGR.tex':work/'signed_growth_receiver.tex',
}
pins=[]
transports=[]
rawdir=out/'originals'/'growth';rawdir.mkdir(exist_ok=True)
letpath=out/'sources'/'LET.tex'
lettext=letpath.read_text(encoding='utf-8')
oldlet='The exact bulk difference\n'
newlet='\\newpage\nThe exact bulk difference\n'
if lettext.count(oldlet)!=1:raise ValueError('non-unique LET page placement')
letpath.write_text(lettext.replace(oldlet,newlet,1),encoding='utf-8')
transports.append(dict(file='sources/LET.tex',before=oldlet,after=newlet,purpose='place full ratio definition at top of next page'))
for dest,src in mapping.items():
    raw=src.read_bytes();(rawdir/dest).write_bytes(raw)
    typed=raw.decode('utf-8')
    replacements=[]
    if dest=='RWB.tex':
        old=typed[typed.index('\\[\n'):typed.index(' \\tag{RWB1}')]
        revised=old.replace('\\[\n','\\[\n \\begin{gathered}\n',1).replace('dy,\n \\quad \\nu','dy,\\\\\n \\nu',1).replace('d\\nu(t),\n \\quad h','d\\nu(t),\\\\\n h',1)
        revised+=' \\end{gathered}\n'
        replacements.append((old,revised))
    if dest=='EIQ.tex':
        replacements.append(('$R(z)=\\sqrt{(z-a)(z-b)}$ on', '\\[R(z)=\\sqrt{(z-a)(z-b)}\\]\non'))
    for before,after in replacements:
        if typed.count(before)!=1:raise ValueError((dest,'non-unique reflow'))
        typed=typed.replace(before,after,1)
        transports.append(dict(file=dest,before=before,after=after,purpose='display wrapping only'))
    typedbytes=typed.encode('utf-8');(new/dest).write_bytes(typedbytes)
    pins.append(dict(source=str(src),destination=str(new/dest),sha256=hashlib.sha256(raw).hexdigest(),typeset_sha256=hashlib.sha256(typedbytes).hexdigest(),bytes=len(raw)))
for src in work.glob('REVIEW*.md'):
    shutil.copy2(src,out/'provenance'/src.name)
review=work/'equilibrium'/'review'/'INDEPENDENT_GEL_EIQ_REVIEW.md'
if review.exists():shutil.copy2(review,out/'provenance'/review.name)
for name in ['explore_positive.py','EXPLORATORY_VALUES.json','TASK_LOG.md']:
    shutil.copy2(work/name,out/'provenance'/name)
tex=r'''\documentclass[11pt,a4paper]{article}
\usepackage{fontspec}
\setmainfont{Cambria}
\setsansfont{Calibri}
\setmonofont{Consolas}
\usepackage[margin=23mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,mathrsfs}
\usepackage[unicode,hidelinks]{hyperref}
\hypersetup{pdftitle={Growth of the Complete Original Gamma Return},pdfauthor={Split-Zero research programme}}
\newcommand{\C}{\mathbb C}
\allowdisplaybreaks
\emergencystretch=2em
\title{Growth of the Complete Original Gamma Return\\[3pt]
\large Finite positive bounds, exact equilibrium and arithmetic transport}
\author{Split-Zero research programme}
\date{14 September 2026}
\begin{document}
\maketitle
This paper continues the complete low-endpoint, parity and positive-shift
calculation. It proves finite positive bounds for the unchanged Gamma
functional, evaluates its leading coefficient by a full equilibrium proof,
and returns that value through the original arithmetic and mixed-state maps.
The full previous low and high source definitions and exact positive
recurrence are printed first. All prerequisite proof sources accompany
the editable paper; historical editions remain preserved.

\part*{Original source, low endpoint and exact finite recurrence}
\input{sources/LET.tex}
\clearpage
\input{sources/PHT.tex}
\clearpage
\part*{The actual growth calculation}
\input{sources/growth/WGP.tex}
\clearpage
\input{sources/growth/RWB.tex}
\clearpage
\paragraph{Dictionary for the following auxiliary integral calculation.}
The real elliptic modulus denoted $k$ within EIQ is the $\kappa$ of GEL:
$\kappa=k_{\mathrm{EIQ}}\in(0,1)$. EIQ's midpoint $m$ is
$m_{\mathrm{EIQ}}=(u^2+v^2)/2$. The original packet still has
$k_{\mathrm{packet}}=4l+1$ and integer multiplicity $m_{\mathrm{packet}}$.
The ensemble map GEL3 supplies parameters $\alpha=a/n$ and
$\beta=\pi q/(2n)$; its original coupled sequences converge to
$(\alpha,\beta)=(2,\pi)$. This is the explicit parameter dictionary
connecting the next two sections to the original packet and source.
\input{sources/growth/EIQ.tex}
\clearpage
\input{sources/growth/GEL.tex}
\clearpage
\input{sources/growth/WGR.tex}
\end{document}
'''
(out/'Gamma_Growth_and_Arithmetic_Return.tex').write_text(tex,encoding='utf-8')
(out/'NEW_PROOF_SOURCE_PINS.json').write_text(json.dumps(pins,indent=2),encoding='utf-8')
(out/'GROWTH_DISPLAY_TRANSPORTS.json').write_text(json.dumps(transports,indent=2),encoding='utf-8')
args=['xelatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','-recorder','Gamma_Growth_and_Arithmetic_Return.tex']
for run in [1,2]:
    result=subprocess.run(args,cwd=out,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    (out/f'build_run_{run}.txt').write_text(result.stdout,encoding='utf-8')
    if result.returncode:
        print(result.stdout[-7000:]);raise SystemExit(result.returncode)
print(json.dumps({'output':str(out),'proofs':pins,'build':'two xelatex passes completed'},indent=2))
