from pathlib import Path
import json,re,hashlib,subprocess
import numpy as np
import mpmath as mp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pypdf import PdfReader
P=Path(__file__).parent;R=P/'reader';R.mkdir(exist_ok=True)
def source(name,sub):return P/sub/name if (P/sub/name).exists() else P/name
mp.mp.dps=35
def scalar(mu):
    K=2*mp.ellipk(mu)/mp.pi;E=2*mp.ellipe(mu)/mp.pi
    t=2*(E/((1-mu)*K)-1);f=-mp.log(mu)/2
    return float(t),float(t*f+2*mp.log(K)),float(f)
mu1=mp.findroot(lambda mu:2*(mp.ellipe(mu)/((1-mu)*mp.ellipk(mu))-1)-1,(.5,.55))
mu=np.r_[np.geomspace(1e-8,1e-3,200),np.linspace(.001,float(mu1),1000)]
values=np.array([scalar(mp.mpf(float(v))) for v in mu]);t,J,f=values.T
t=np.r_[0,t];J=np.r_[0,J]
eta0=2*np.log(4/np.pi)-2;eta=eta0-J;half=.28581630680480845015
plt.rcParams.update({'font.size':10,'axes.titlesize':11})
fig,axs=plt.subplots(3,1,figsize=(6.5,8.0),layout='constrained')
axs[0].plot(t,J,color='#006778',label=r'Exact profile $J(t)$')
axs[0].axhline(J[-1]/2,color='#999999',ls=':',lw=1)
axs[0].axvline(half,color='#ad4500',ls='--',lw=1)
axs[0].plot([half],[J[-1]/2],'o',color='#ad4500')
axs[0].annotate(r'$t_{1/2}=0.2858163068\ldots$',xy=(half,J[-1]/2),xytext=(.43,.18),arrowprops={'arrowstyle':'->','color':'#ad4500'},fontsize=9)
axs[0].set(xlabel=r'Original cutoff fraction $t=j/q$',ylabel=r'$J(t)$',title=r'IR8: $\log(\det H_{K,q-1}/\det H_{K,N_j})=mqJ(t)+o(kq)$',xlim=(0,1))
axs[0].legend(fontsize=9)
axs[1].plot(values[:,0],f,color='#006778',label=r'$f(t)=J\,^{\prime}(t)$')
axs[1].plot(values[:,0],-.5*np.log(values[:,0]),ls='--',color='#ad4500',label=r'Leading endpoint term $-\frac{1}{2}\log t$')
axs[1].set(xlabel=r'Original cutoff fraction $t$',ylabel='Increment density',title=r'IR14–16: complete positive measure, total mass $J(1)$',xlim=(0,1),ylim=(0,3))
axs[1].legend(fontsize=9)
xi=np.linspace(eta[-1]-.14,eta0+.14,1000)
limit=np.interp(xi,eta[::-1],(1-t)[::-1],left=0,right=1)
q=324;centres=eta0-np.interp(np.arange(q)/q,t,J)
comp=np.mean(np.exp(-np.exp(np.clip(q*(centres[:,None]-xi[None,:]),-700,700))),axis=0)
axs[2].plot(xi,limit,color='#006778',label=r'Limit $\mathcal{H}(\xi)$')
axs[2].plot(xi,comp,ls='--',color='#ad4500',label=r'Centre comparison, $k=17$, $q=324$')
axs[2].set(xlabel=r'Physical heat exponent $\xi$: $\tau=q^{-2q}e^{-q\xi}$',ylabel='Heat average',title='PH28–35: original measured heat retains its angle defect',ylim=(-.03,1.03))
axs[2].legend(fontsize=8)
for ax in axs:ax.grid(alpha=.2)
fig.savefig(R/'CUTOFF_PROFILE.png',dpi=230);plt.close(fig)
head=r'''\documentclass[10pt]{article}
\usepackage[a4paper,margin=19mm]{geometry}
\usepackage{amsmath,amssymb,mathtools,amsthm,mathrsfs,longtable,booktabs,array,calc,enumitem,float,graphicx}
\usepackage[hidelinks,hypertexnames=false]{hyperref}\usepackage{xurl}
\usepackage{fontspec}\setmainfont{DejaVu Serif}
\setlength{\emergencystretch}{4em}\providecommand{\tightlist}{}
\setcounter{secnumdepth}{0}\allowdisplaybreaks
\DeclareMathOperator{\Log}{Log}
\title{The original kernel across the complete cutoff window\\Measured phase, heat, and full subquotients}
\author{Split-Zero research programme}
\date{22 September 2026\\SZ-20260922-025}
\begin{document}\maketitle
The original constrained kernel has a computed logarithmic volume at every
source cutoff $N_j=q-1+j$, including all four prescribed endpoints:
\[
 \log\frac{\det H_{K,q-1}}{\det H_{K,N_j}}
 =mqJ(j/q)+o(kq),\qquad 0\le j\le q+1.
\]
Here $q=(k+1)^2$, $m=8k-16$, the period and stipulated simple quartet are fixed,
and the same complete kernel is retained throughout. Its actual relative
spectra satisfy the stronger uniform logarithmic estimate IR6. The profile
passes through every specified complete fixed subquotient of diverging rank.

The proof supplies uniform Gamma-power asymptotics through the first cutoff,
the entire growing-jet minimum, and the original invariant-row comparison.
An exact elliptic coordinate gives a convergent endpoint correction and
certifies where half the limiting volume loss occurs. The original measured
phase receives a moving transition; the measured heat retains its finite
angle defect and receives a sharper physical smoothing error.

Both final incoming responses are incorporated. The separate complex
arithmetic-current signs remain a further calculation. No RH proof or
numerical evaluation of a hypothetical zero is claimed.
\begingroup\small\tableofcontents\endgroup\clearpage
\section*{The original cutoff and its measured return}
\addcontentsline{toc}{section}{The original cutoff and its measured return}
\begin{figure}[H]\centering
\includegraphics[height=.74\textheight,width=\textwidth,keepaspectratio]{CUTOFF_PROFILE.png}
\caption{Top: the exact scalar in the original kernel-volume formula IR8.
The half-volume position is certified in EP18. Middle: its increment density
IR14--16, whose total mass is $J(1)=C_\partial/2$; the divergence at zero is
integrable and the correction is proved in EP15--16. Bottom: the evaluated
limiting heat distribution PH31 and its finite scalar-centre comparison.
The dashed curve is not a numerical native response. PH34--35 bounds the
actual response error and preserves its full angle defect. Elliptic formulas
use B. C. Carlson's DLMF19.5 and19.8, with original TeX and a full derivation
in EP1--17. Plot sampling is numerical; the proofs and interval certificates
are separate.}
\end{figure}
'''
parts=[('Original maps, complete subquotients, and receivers',P/'INTEGRATED_PROFILE_AND_RECEIVERS.md'),('Uniform Gamma powers and every original jet',source('POWER_CUTOFF_PROFILE_PROOF.md','independent_power_profile')),('Exact elliptic profile and certified position',P/'ELLIPTIC_PROFILE_PROOF.md'),('Original measured phase and complete heat',source('PHASE_HEAT_PROOFS.md','independent_phase_heat'))]
text=head
for title,p in parts:
    proc=subprocess.run(['pandoc',str(p),'-f','markdown+tex_math_single_backslash+tex_math_dollars+raw_tex','-t','latex','--wrap=none'],capture_output=True,check=True,encoding='utf-8')
    body=proc.stdout
    body=body.replace(r''' a_k^{\rm src}\|g\|_{\mathrm{pow},N}^{\,2}
 \le\|U_Qg\|_{G_N}^{\,2}
 \le b_k^{\rm src}\|g\|_{\mathrm{pow},N}^{\,2},\quad
 a_k^{\rm src}=\ell_ke^{-C},\quad b_k^{\rm src}=u_ke^C,\quad
 \chi_k=\log(b_k^{\rm src}/a_k^{\rm src})=2C+\log(u_k/\ell_k).''',r'''\begin{gathered}
 a_k^{\rm src}\|g\|_{\mathrm{pow},N}^{\,2}
 \le\|U_Qg\|_{G_N}^{\,2}
 \le b_k^{\rm src}\|g\|_{\mathrm{pow},N}^{\,2},\\
 a_k^{\rm src}=\ell_ke^{-C},\quad b_k^{\rm src}=u_ke^C,\quad
 \chi_k=\log(b_k^{\rm src}/a_k^{\rm src})=2C+\log(u_k/\ell_k).
 \end{gathered}''')
    body=re.sub(r'\\texttt\{([^{}]+)\}',lambda m:r'\path{'+m[1].replace(r'\_','_')+'}' if len(m[1])>25 else m[0],body)
    text+='\n\\clearpage\\part{'+title+'}\n'+body
text+='\n\\end{document}\n'
tex=R/'CUTOFF_PROFILE_READER.tex';tex.write_text(text,encoding='utf-8')
for i in range(2):
    proc=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error',tex.name],cwd=R,capture_output=True,text=True,encoding='utf-8',errors='replace')
    (R/'LATEX_OUTPUT.txt').write_text(proc.stdout,encoding='utf-8')
    if proc.returncode:raise RuntimeError(proc.stdout[-5000:])
pdf=tex.with_suffix('.pdf');log=tex.with_suffix('.log').read_text(encoding='utf-8',errors='replace')
receipt={'pages':len(PdfReader(pdf).pages),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'overfull':re.findall(r'Overfull[^\n]*',log),'undefined':re.findall(r'[^\n]*undefined[^\n]*',log),'missing':re.findall(r'[^\n]*Missing character[^\n]*',log),'visual':'pending'}
(P/'READER_BUILD.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
