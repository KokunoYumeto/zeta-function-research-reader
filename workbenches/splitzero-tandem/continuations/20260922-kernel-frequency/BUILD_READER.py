from pathlib import Path
import subprocess,re,json,hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pypdf import PdfReader
from PIL import Image,ImageDraw
P=Path(__file__).parent
R=P/'reader';R.mkdir(exist_ok=True)
plt.rcParams.update({'font.size':9})
fig,ax=plt.subplots(2,1,figsize=(6.4,6.2),layout='constrained')
k=65;q=(k+1)**2;Delta=16*k-48
cp=1.35428198782529213288398977515384818
etaL=2*np.log(4/np.pi)-2;etaH=etaL-cp/2
b=np.linspace(etaH-.18,etaL+.18,2500)
f=lambda x:np.arctan(np.exp(np.clip(x,-700,700)))
ax[0].plot(b,2*Delta/k*(f(q*(etaL-b))-f(q*(etaH-b))),color='#005f73',label='Finite comparison, k=65')
ax[0].plot([b.min(),etaH,etaH,etaL,etaL,b.max()],[0,0,16*np.pi,16*np.pi,0,0],ls='--',color='#bb3e03',label=r'Limit: $16\pi$ on $(\eta_H,\eta_L)$')
ax[0].set(xlabel=r'Original frequency exponent $b$: $\omega=q^{2q}e^{bq}$',ylabel='Four-cutoff phase divided by k',title='PT17: the full measured phase comparison')
ax[0].legend(fontsize=8,loc='upper right');ax[0].grid(alpha=.2)
x=np.geomspace(.01,100,1000);g=.25;t=np.minimum(x,1/np.sqrt(1-g))
ax[1].semilogx(x,2*g*x/(1+x),ls=':',color='#777777',label='Earlier bound')
ax[1].semilogx(x,g*np.arctan(x),ls='--',color='#bb3e03',label=r'New trace bound: $\gamma\arctan x$')
ax[1].semilogx(x,np.arctan(t)-np.arctan((1-g)*t),color='#005f73',label=r'Sharp bound for $\gamma=1/4$')
ax[1].set(xlabel=r'Original energy ratio $x=u/\omega$',ylabel=r'Upper bound for $-\mathrm{Im}\,h(i\omega)$',title='SF23–24: one retained angle')
ax[1].legend(fontsize=8,loc='upper left');ax[1].grid(alpha=.2)
fig.savefig(R/'EXACT_COMPARISONS.png',dpi=220);plt.close(fig)
head=r'''\documentclass[10pt]{article}
\usepackage[a4paper,margin=22mm]{geometry}
\usepackage{amsmath,amssymb,mathtools,amsthm,mathrsfs,longtable,booktabs,array,calc,enumitem,float,graphicx,tikz}
\usepackage[hidelinks,hypertexnames=false]{hyperref}\usepackage{xurl}
\usepackage{fontspec}\setmainfont{DejaVu Serif}
\usetikzlibrary{arrows.meta,positioning}
\setlength{\emergencystretch}{4em}\providecommand{\tightlist}{}
\setcounter{secnumdepth}{0}\allowdisplaybreaks
\DeclareMathOperator{\Log}{Log}
\title{The original kernel coefficient\\and its measured frequency return}
\author{Split-Zero research programme}
\date{22 September 2026\\SZ-20260922-024}
\begin{document}\maketitle
On the retained fixed-period simple-quartet domain, the complete original
four-cutoff kernel determinant satisfies
\[
 \mathcal K_k=(8k-16)C_\partial(k+1)^2+o(k(k+1)^2),\qquad
 10.83425590260233706<8C_\partial<10.83425590260233707.
\]
The argument retains the original conductor, source metrics, complete minima,
root factors and all exceptional directions. The growing-jet and diagonal
arguments are proved in full. An exact endpoint formula identifies the
logarithmic equilibrium statistic with the original elliptic coefficient.

The earlier uniform-return calculation then controls the entire measured
frequency curve. The finite phase and derivative bounds are sharpened using
all original projection angles. All six incoming continuations have separate
reading and source records. These results do not provide a hypothetical zeta
zero or assign the separate phase-bearing arithmetic-current signs.
\begingroup\small\tableofcontents\endgroup\clearpage
\section*{The exact route through the original kernel}
\addcontentsline{toc}{section}{The exact route through the original kernel}
\begin{figure}[H]\centering
\begin{tikzpicture}[>=Latex,box/.style={draw,rounded corners,align=center,text width=12.2cm,inner sep=7pt}]
\node[box](a){Original $K_k=\ker\Lambda_k$, with its full metric $I_K^*G_NI_K$\\
 Fixed conductor symbol $\mathcal E(z)=z^{v_0}b(z)$};
\node[box,below=8mm of a](b){Residue map $l-L_Rf_0$; exact good subspace $K_{k,R}$\\
 Omitted codimension $\le v_0+c_R$, retained as a complete quotient};
\node[box,below=8mm of b](c){$A_kp=P_{\ge q-s}U_Q^{-1}p$,\quad $U_QF=[Q_ky^{-q}F]_+$\\
 Full affine fibres and both integration regions: CK9--11};
\node[box,below=8mm of c](d){Every jet in $|y|^{2(q-s)}d\sigma$: PJ1--70\\
 Complete right inverse, parity, root gaps and diagonal minimum};
\node[box,below=8mm of d](e){EL3: $L(\alpha,\beta)=2(\alpha+1)\log w-\alpha\log z-2$\\
 CK14: $\mathcal K_k=mC_\partial q+o(kq)$};
\draw[->](a)--(b);\draw[->](b)--(c);\draw[->](c)--(d);\draw[->](d)--(e);
\end{tikzpicture}
\caption{Every arrow is the stated original-coordinate map or complete metric
comparison. CK12 retains the rank-one arithmetic-action defect of $U_Q$.
The complementary quotient costs $O((v_0+c_R)q)$ for each fixed radius;
it is never deleted from the determinant. CK1--14 and PJ1--70 give the
complete proofs. Human Gamma and polynomial sources are credited there.}
\end{figure}\clearpage
\section*{Measured phase and sharp frequency error}
\addcontentsline{toc}{section}{Measured phase and sharp frequency error}
\begin{figure}[H]\centering
\includegraphics[width=\textwidth]{EXACT_COMPARISONS.png}
\caption{Top: the explicit comparison curve in PT12, at the displayed
finite $k=65$, and the limiting step in PT17. It is not a numerical evaluation
of a native response. PT17 bounds the integral distance of the actual phase
from this curve using the complete original spectra. Bottom: the sharp
one-angle bound SF23--24, with $\gamma=1/4$ and $x=u/\omega$, alongside the
earlier and new trace bounds. SF25--27 construct exact matrices attaining
the sharp curve. The script retains these exact functions; displayed samples
are rounded for plotting.}
\end{figure}
For the entire original phase, PT12 gives
\[
 \int_0^\infty\left|\mathcal R\Theta(\omega)-2\Delta
 \left(\arctan\frac{e^{c_L}}\omega-\arctan\frac{e^{c_H}}\omega\right)\right|
 \frac{d\omega}\omega\le\frac\pi2\mathcal B,
 \qquad\mathcal B=o(kq).
\]
The proof establishes absolute convergence and retains both frequency ends.
The separate complex arithmetic current still uses its original polar insertion.
'''
parts=[('Original kernel and all receiving calculations','COMBINED_KERNEL_AND_RECEIVERS.md'),('The complete Gamma-power minimum','POWER_JET_PROOF.md'),('The exact elliptic logarithmic moment','ELLIPTIC_LOG_MOMENT_PROOF.md'),('Complete measured phase transport','PHASE_TRANSPORT_PROOFS.md'),('Sharp finite frequency bounds','FREQUENCY_PROOFS.md')]
text=head
for title,name in parts:
    f=P/name;out=R/(f.stem+'.tex')
    r=subprocess.run(['pandoc',str(f),'-f','markdown+tex_math_single_backslash+tex_math_dollars+raw_tex','-t','latex','--wrap=none','-o',str(out)],capture_output=True,text=True)
    if r.returncode:raise RuntimeError(r.stderr)
    tex=out.read_text(encoding='utf-8')
    tex=tex.replace(r''' H=G^{-1}T^*GT,\quad V=\ker T,\quad
 Q=(\Lambda G^{-1}\Lambda^*)^{-1},\quad L=G^{-1}\Lambda^*Q,\quad
 H_K=I_K^*GI_K,\quad
 J_B=LQ^{-1/2},\quad J_K=I_KH_K^{-1/2}.''',r'''\begin{gathered}
 H=G^{-1}T^*GT,\quad V=\ker T,\quad Q=(\Lambda G^{-1}\Lambda^*)^{-1},\\
 L=G^{-1}\Lambda^*Q,\quad H_K=I_K^*GI_K,\quad
 J_B=LQ^{-1/2},\quad J_K=I_KH_K^{-1/2}.
 \end{gathered}''')
    tex=re.sub(r'\\texttt\{([^{}]+)\}',lambda m:r'\path{'+m[1].replace(r'\_','_')+'}' if len(m[1])>25 else m[0],tex)
    tex=re.sub(r'(?<![a-zA-Z0-9{/_])([a-f0-9]{40,64})(?![a-f0-9])',lambda m:r'\nolinkurl{'+m[1]+'}',tex)
    text+='\n\\clearpage\\part{'+title+'}\n'+tex
text+='\n\\end{document}\n'
out=R/'KERNEL_AND_FREQUENCY_READER.tex';out.write_text(text,encoding='utf-8')
for _ in range(2):
    r=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error',out.name],cwd=R,capture_output=True,text=True,encoding='utf-8',errors='replace')
    (R/'LATEX_OUTPUT.txt').write_text(r.stdout,encoding='utf-8')
    if r.returncode:raise RuntimeError(r.stdout[-4500:])
pdf=out.with_suffix('.pdf');pages=len(PdfReader(pdf).pages)
log=out.with_suffix('.log').read_text(encoding='utf-8',errors='replace')
report={'pages':pages,'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'overfull':re.findall(r'Overfull[^\n]*',log),'undefined':re.findall(r'[^\n]*undefined[^\n]*',log),'missing':re.findall(r'[^\n]*Missing character[^\n]*',log),'visual':'pending'}
(P/'READER_BUILD.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
