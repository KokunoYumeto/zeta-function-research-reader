from pathlib import Path
import json,hashlib,re,subprocess,tempfile,shutil
import numpy as np
import mpmath as mp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pypdf import PdfReader
P=Path(__file__).parent
R=Path(tempfile.mkdtemp(prefix='splitzero026-reader-'))
mp.mp.dps=40
def scalar(z):
    F=2*mp.ellipk(z)/mp.pi
    t=2*(mp.ellipe(z)/((1-z)*mp.ellipk(z))-1)
    J=2*mp.log(F)-t*mp.log(z)/2
    L=mp.log(4/(mp.pi*(1+t)*(1-z)*F))
    psi=(1+t)*L+t*mp.log(z)/4
    return float(t),float(J),float(psi)
z1=mp.findroot(lambda z:scalar(z)[0]-1,(.51,.53))
values=np.array([scalar(mp.mpf(float(z))) for z in np.r_[np.geomspace(1e-10,.001,100),np.linspace(.001,float(z1),650)]])
t,j,psi=values.T
t=np.r_[0,t];j=np.r_[0,j];psi=np.r_[float(mp.log(4/mp.pi)),psi]
plt.rcParams.update({'font.size':10,'axes.titlesize':11})
fig,axs=plt.subplots(3,1,figsize=(6.7,8.9),layout='constrained',gridspec_kw={'height_ratios':[1.15,1.15,.9]})
axs[0].plot(t,j,color='#006c78',label=r'$J(t)$: kernel log-volume loss per $mq$')
axs[0].plot(t,psi,color='#a64500',label=r'$\psi(t)$: arithmetic-current log magnitude per $q$')
axs[0].set(xlim=(0,1),xlabel=r'Original cutoff $t=j/q$, $N_j=q-1+j$',ylabel='Exact scalar profile',title=r'RC10–15: $J^\prime=2\psi-2(1+t)\psi^\prime$')
axs[0].legend(fontsize=9);axs[0].grid(alpha=.2)
rate=np.maximum(psi-.125,0)
axs[1].plot(t,rate,color='#006c78',label=r'$\log\sigma_{\max}(V_N)/q$ limit')
axs[1].plot(t,-rate,color='#a64500',label=r'$\log\sigma_{\min}(V_N)/q$ limit')
axs[1].plot(t,2*rate,ls='--',color='#64419a',label=r'$\log\mathrm{cond}_{Q_B}(V_N)/q$ limit')
axs[1].axhline(0,lw=.7,color='gray');axs[1].set(xlim=(0,1),xlabel=r'Original cutoff $t=j/q$',ylabel='Leading exponential rate',title=r'RC29–30: $V_N=\exp(i e^{-q/8}\Lambda M L_N)$')
axs[1].legend(fontsize=8,loc='upper right');axs[1].grid(alpha=.2)
ax=axs[2];ax.axis('off');ax.set_xlim(0,1);ax.set_ylim(0,1)
ax.text(.14,.73,r'$B,\ Q_{B,N}$',ha='center',va='center',bbox=dict(boxstyle='round',fc='#e0f1f3',ec='#006c78'))
ax.text(.83,.73,r'$K=\ker\Lambda,\ G_N|_K$',ha='center',va='center',bbox=dict(boxstyle='round',fc='#f7e8dc',ec='#a64500'))
ax.annotate('',xy=(.68,.82),xytext=(.28,.82),arrowprops=dict(arrowstyle='->',color='#a64500',lw=1.8))
ax.text(.48,.94,r'$M_{KB}=(I-P)MJ_N$',ha='center',fontsize=10)
ax.annotate('',xy=(.28,.64),xytext=(.68,.64),arrowprops=dict(arrowstyle='->',color='#006c78',lw=1.8))
ax.text(.48,.49,r'$M_{BK}=J_N^\dagger M|_K$',ha='center',fontsize=10)
ax.text(.5,.26,r'Hidden return: $M_{BK}e^{i(t-s)M_{KK}}M_{KB}$',ha='center',fontsize=11)
ax.text(.5,.08,'CE24–29: exact mixed maps and full Volterra memory',ha='center',fontsize=10)
fig.savefig(P/'CURRENT_CONNECTIONS.png',dpi=220);plt.close(fig)
shutil.copyfile(P/'CURRENT_CONNECTIONS.png',R/'CURRENT_CONNECTIONS.png')
head=r'''\documentclass[10pt]{article}
\usepackage[a4paper,margin=19mm]{geometry}
\usepackage{amsmath,amssymb,mathtools,amsthm,mathrsfs,longtable,booktabs,array,calc,enumitem,float,graphicx,needspace}
\usepackage[hidelinks,hypertexnames=false]{hyperref}\usepackage{xurl}
\usepackage{fontspec}\setmainfont{DejaVu Serif}
\setlength{\emergencystretch}{4em}\providecommand{\tightlist}{}
\setcounter{secnumdepth}{0}\allowdisplaybreaks
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\newcommand{\C}{\mathbb C}\newcommand{\Pp}{\mathcal P}
\newcommand{\Rr}{\mathcal R}\newcommand{\tr}{\operatorname{Tr}}
\newcommand{\remm}{\operatorname{rem}}\newcommand{\rank}{\operatorname{rank}}
\newcommand{\diag}{\operatorname{diag}}\newcommand{\eps}{\varepsilon}
\newcommand{\Id}{I}\newcommand{\norm}[1]{\left\lVert#1\right\rVert}
\title{Original arithmetic current and effective cutoff control\\Complete source increments, observed evolution, and hidden return}
\author{Split-Zero research programme}
\date{22 September 2026\\SZ-20260922-026}
\begin{document}\maketitle
The original kernel-volume profile and the first-order arithmetic-current
profile are connected by the exact identity
\[
J'(t)=2\psi(t)-2(1+t)\psi'(t).
\]
This edition proves a finite reconstruction from the actual source increments,
sharper complete-kernel localization and local source-window bounds, and
the original observed current's two signed directions. It calculates both
extreme singular values of the compressed arithmetic evolution and its
exact relation to the full evolution through the hidden kernel.

Both incoming manuscripts are printed in full, followed or preceded by the
complete independent derivations that strengthen them. All original cutoffs,
source minima, invariant rows, physical coordinates and mixed blocks are
retained. The earlier complete mathematical source collection accompanies
this reader as an unchanged byte prefix plus new sources.

The fixed-data simple-quartet domain is retained throughout. RC35--44 applies
the earlier conductor theorem on its proved period domain: the terminal
eigenclass has subexponential normalized current and exponentially balanced
weights in the two observed sign sectors. Its residual individual sign is
still governed by the exact complex pairing RC32. These results do not establish RH.
\begingroup\small\tableofcontents\endgroup\clearpage
\section*{The two profiles and the actual hidden return}
\addcontentsline{toc}{section}{The two profiles and the actual hidden return}
\begin{figure}[H]\centering
\includegraphics[width=\textwidth,height=.75\textheight,keepaspectratio]{CURRENT_CONNECTIONS.png}
\caption{Top: the two evaluated profiles in their original cutoff coordinate.
RC10--15 proves their connecting map and finite increment reconstruction.
Middle: the limits of both extreme singular values and condition number
for the original intrinsic evolution at time $e^{-q/8}$, CE19--23 and RC29--30.
The displayed curves sample the universal elliptic formulas; they are not
computed native-period matrices. Bottom: exact maps of the observed and
hidden source spaces. The complete two-step return, with all mixed terms,
occurs in the Volterra identity CE27. Elliptic conventions and formulas
are B. C. Carlson's DLMF19.5 and19.8, with original equation sources and
complete derivations retained.}
\end{figure}
'''
parts=[
('Connecting the original cutoff and arithmetic current','CUTOFF_CURRENT_CONNECTION.md'),
('Finite Gamma minimum and complete coefficient covariance','EFFECTIVE_GAMMA_AND_JET_PROOF.md'),
('Effective original localization and every fixed subquotient','LOCALIZATION_PROOF.md'),
('Original observed current: complete incoming proof','OBSERVED_CURRENT_PLANE.tex'),
('Signed-time evolution and full hidden-source defect','EVOLUTION_PROOF.md'),
('Effective cutoff: complete incoming proof','EFFECTIVE_CUTOFF_PROOF.md')]
text=head
for title,name in parts:
    src=P/name
    if src.suffix=='.tex':
        body=src.read_text(encoding='utf-8').split(r'\begin{document}',1)[1].rsplit(r'\end{document}',1)[0]
        body=body[body.index(r'\section{'):]
    else:
        body=subprocess.run(['pandoc',str(src),'-f','markdown+tex_math_single_backslash+tex_math_dollars+raw_tex','-t','latex','--wrap=none'],capture_output=True,check=True,encoding='utf-8').stdout
        body=re.sub(r'\\texttt\{([^{}]+)\}',lambda m:r'\path{'+m[1].replace(r'\_','_')+'}' if len(m[1])>25 else m[0],body)
    body=body.replace(r'\def\LTcaptype{none}',r'\def\LTcaptype{table}')
    if name=='EFFECTIVE_CUTOFF_PROOF.md':
        body=body.replace(r'{\def\LTcaptype{table}',r'{\footnotesize\def\LTcaptype{table}')
        for width in ['0.18','0.41','0.41']:
            body=body.replace(r'\real{0.3333}',r'\real{'+width+'}',1)
    body=body.replace(r'''e=b_N/\sqrt{E_N},\quad f=b_{N+1}/\sqrt{F_N},\quad
\langle e,f\rangle_G=0,\quad \|e\|_G=\|f\|_G=1,
\quad M=C+R,\quad C=C^\dagger,\quad R=\epsilon f e^\dagger,
\quad \epsilon=\sqrt{E_NF_N}/\omega_N. \tag{CE5}''',r'''\begin{gathered}
e=b_N/\sqrt{E_N},\quad f=b_{N+1}/\sqrt{F_N},\quad
\langle e,f\rangle_G=0,\quad \|e\|_G=\|f\|_G=1,\\
M=C+R,\quad C=C^\dagger,\quad R=\epsilon f e^\dagger,
\quad \epsilon=\sqrt{E_NF_N}/\omega_N.
\end{gathered}\tag{CE5}''')
    text+='\n\\clearpage\\part{'+title+'}\n'+body
text+='\n\\end{document}\n'
tex=R/'CURRENT_AND_CUTOFF_READER.tex';tex.write_text(text,encoding='utf-8')
for i in range(3):
    proc=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error',tex.name],cwd=R,capture_output=True,text=True,encoding='utf-8',errors='replace')
    (R/'LATEX_OUTPUT.txt').write_text(proc.stdout,encoding='utf-8')
    if proc.returncode:raise RuntimeError(proc.stdout[-6500:])
pdf=tex.with_suffix('.pdf');log=tex.with_suffix('.log').read_text(encoding='utf-8',errors='replace')
# The delivered TeX finds its figure beside it, independent of scratch directory.
delivery=text.replace('{../CURRENT_CONNECTIONS.png}','{CURRENT_CONNECTIONS.png}')
(P/tex.name).write_text(delivery,encoding='utf-8')
(P/pdf.name).write_bytes(pdf.read_bytes())
receipt={'pages':len(PdfReader(pdf).pages),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
'overfull':re.findall(r'Overfull[^\n]*',log),'undefined':re.findall(r'[^\n]*undefined[^\n]*',log),
'missing':re.findall(r'[^\n]*Missing character[^\n]*',log),'visual':'pending'}
(R/'BUILD_QA.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
print('Build receipt: '+str(R/'BUILD_QA.json'))
