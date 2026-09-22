from pathlib import Path
import subprocess,re,json,shutil,tempfile,math
from PIL import Image,ImageDraw
from pypdf import PdfReader
P=Path(__file__).parent;O=P/'reader';O.mkdir(exist_ok=True)
head=r'''\documentclass[11pt]{article}
\usepackage[a4paper,margin=24mm]{geometry}
\usepackage{amsmath,amssymb,mathtools,amsthm,mathrsfs,tikz,pgfplots,longtable,booktabs,array,calc,enumitem,float}
\usepackage[hidelinks,hypertexnames=false]{hyperref}\usepackage{xurl}
\usepackage{fontspec}\setmainfont{DejaVu Serif}
\usetikzlibrary{arrows.meta,positioning,calc}\pgfplotsset{compat=1.18}
\setlength{\emergencystretch}{4em}\providecommand{\tightlist}{}\newcounter{none}
\setcounter{secnumdepth}{0}\allowdisplaybreaks
\title{Original covariance growth\\and the measured arithmetic resolvent}
\author{Split-Zero research programme}
\date{22 September 2026\\SZ-20260922-020}
\begin{document}\maketitle
The original invariant covariance can now be approximated to a prescribed
accuracy with a total of $O(kq+k\log(1/\eta))$ scalar samples. The proof retains
every invariant row and every lower-root coefficient, and gives finite bounds
for errors in both. Comparing the low and high cutoffs directly also controls
the full complementary minimum when a small row subspace is separated.

The measured arithmetic resolvent has an exact matrix correction from its
observation kernel. This paper reconstructs that correction, determines its
smallest contributing kernel space and bounds the effect of coherent source
errors by its actual nonzero ranks. All complex cross blocks are retained.
The incoming signed determinant calculation is reproduced with its stated
analytic inputs and original four-cutoff signs.

The four-label ES receiver has a separate complete calculation: all four
first singular corrections, its inverse-column correction, the exact
exceptional kernel and cokernel, and every fixed scalar observation of the
slow heat. Its original arithmetic scope is preserved.

The period-dependent native kernel coefficient through $kq$ and the separate
complex-current signs remain unevaluated. The results here supply proved
reductions, finite error bounds and further exact values; they do not assign
those remaining quantities. Complete inherited proof sources, their precise
reading records and human citations accompany this edition.
\begingroup\small\tableofcontents\endgroup\clearpage
\section*{The actual minimum and the kernel correction}
\addcontentsline{toc}{section}{The actual minimum and the kernel correction}
The onto observation $\Lambda:E\to B$ has its original kernel $K$.
The source metric $G$ determines the minimum section $L$ and value metric $Q$.
The exact splitting map and energy are
\[
 U_0(b,a)=Lb+I_Ka,\qquad
 U_0^*GU_0=\begin{pmatrix}Q&0\\0&H_K\end{pmatrix},\qquad
 U_0^*T^*GTU_0=\begin{pmatrix}E_{BB}&X^*\\X&E_{KK}\end{pmatrix}.
\]
\begin{figure}[H]\centering
\begin{tikzpicture}[>=Latex,node distance=18mm,
 box/.style={draw,rounded corners,align=center,text width=5.9cm,inner sep=7pt}]
\node[box] (b) {Observed vector $b\in B$\\with its metric $Q$};
\node[box,right=10mm of b] (forcing) {Kernel forcing\\$Xb\in\mathbb C^m$};
\node[box,below=22mm of b] (full) {Sum of the two transported vectors\\$Lb+I_Ka_z\in E$};
\node[box,below=22mm of forcing] (a) {Exact minimizing kernel coordinate\\$a_z=-(zH_K+E_{KK})^{-1}Xb$};
\draw[->] (b)--node[above] {$X$}(forcing);
\draw[->] (b)--node[left] {$L$}(full);
\draw[->] (forcing)--node[left,font=\small] {$-(zH_K+E_{KK})^{-1}$}(a);
\draw[->] (a)--node[above] {$I_K$}(full);
\end{tikzpicture}
\caption{The exact full minimum in RM1--8. The arrows labelled $L$ and
$I_K$ supply the two summands of the full vector. Both cross blocks remain.
The kernel correction is $D(z)=X^*(zH_K+E_{KK})^{-1}X$.
The correction subtracts from $zQ+E_{BB}$, and the observed endomorphism is
$\mathscr Y(z)=z[zQ+E_{BB}-D(z)]^{-1}Q$.
This is the finite Feshbach--Schur construction; the proof cites Dusson,
Sigal and Stamm at its precise original-author source location.}
\end{figure}
The contributing kernel space is the span of $A^jCb$, where
$A=H_K^{-1/2}E_{KK}H_K^{-1/2}$ and $C=H_K^{-1/2}XQ^{-1/2}$.
Its exact dimension is the rank of the phase-bearing moment matrix
$[C^*A^{i+j}C]_{i,j=0}^{m-1}$ (RM12--14). Reducing kernel directions with
zero coupling have an explicitly proved cancellation; none is discarded
on the basis of a rank count alone.
\clearpage
\section*{An exact finite comparison of the three actions}
\addcontentsline{toc}{section}{An exact finite comparison of the three actions}
RM22 evaluates the example $G=I_3$, $T=\operatorname{diag}(0,2,3i)$ and
$\Lambda=\left(\begin{smallmatrix}-1&1&0\\-i&0&1\end{smallmatrix}\right)$.
Its kernel frame is $(1,1,i)^{\mathsf T}$ and
\[
 D(z)=\frac1{9(3z+13)}
 \begin{pmatrix}1&14i\\-14i&196\end{pmatrix}.
\]
\begin{figure}[H]\centering
\begin{tikzpicture}\begin{semilogxaxis}[width=.95\textwidth,height=7cm,
 xlabel={Original positive parameter $z$},ylabel={Measured determinant},
 xmin=.02,xmax=100,ymin=0,ymax=1,
 legend style={at={(.5,-.24)},anchor=north,legend columns=1}]
\addplot[teal!80!black,thick]coordinates{FULL_CURVE};\addlegendentry{Full original measured action}
\addplot[orange!85!black,thick,dashed]coordinates{ARITH_CURVE};\addlegendentry{Arithmetic word compressed first}
\addplot[violet,thick,dotted]coordinates{ENERGY_CURVE};\addlegendentry{Positive energy compressed first}
\end{semilogxaxis}\end{tikzpicture}
\caption{Exact rational functions from RM22, sampled only to draw the curves.
The full action is always above the compressed positive-energy action (RM15).
Its comparison with the compressed arithmetic word changes sign at
$z=(\sqrt{11335}-47)/39$. The figure is an auxiliary finite example,
not a native period calculation. All source coordinates and phases are
specified in RM22 and the reproducible builder.}
\end{figure}
For the actual growing-dimensional word, a coherent full metric enclosure
$\alpha G\preceq\widetilde G\preceq\beta G$ gives the uniform bound
\[
 |\log\det\mathscr Y_{\widetilde G}(z)-\log\det\mathscr Y_G(z)|
 \le (\Delta+p)\log(\beta/\alpha),
\]
where $\Delta=\operatorname{rank}T$ and $p=\operatorname{rank}(TI_K)$.
RM19--21 proves the moving-section comparison. Fixed enclosure ratios cost
$O(k)$ on the original word, below its $kq$ determinant scale.
\clearpage
\section*{Every original lower-root constraint in the sampling map}
\addcontentsline{toc}{section}{Every original lower-root constraint in the sampling map}
The row functions give physical moments
$L_N[j,n]=(-i)^nn![w^n]A_{z_j}(w)$. The matrix $J_N$ contains all coefficient
columns of multiplication by the full monic lower polynomial $Q_-$.
The exact relation to the orthogonal projection is
\[
 \begin{array}{ccc}
 \mathcal P_{N-v-q'}&\xrightarrow{\ J_N:\ p\mapsto Q_-p\ }&\mathcal P_{N-v}\\
 &&\downarrow L_N\\
 &&\mathbb C^r.
 \end{array}
\]
\[
 C_N=(L_NJ_N)(J_N^*H_NJ_N)^{-1}(L_NJ_N)^*,\qquad
 B_N=L_NH_N^{-1}L_N^*.
\]
Here $H_N$ is the full physical Gamma Gram; its mass remains $\sqrt{2\pi}$.
CS19 proves this map equals the full lower-root projector. CS21--23 keeps
the error in every coefficient of $J_N$, through the original metric,
before any determinant is taken. The result is a certified approximation
of these complete maps. The sample count alone is not a count of bit
operations, zero isolation or numerical evaluation of the native period.
\clearpage
'''
xs=[10**(-1.7+j*3.7/160)for j in range(161)]
for key,fn in [('FULL_CURVE',lambda z:z*(3*z+13)/(3*(z+4)*(z+9))),('ARITH_CURVE',lambda z:9*z*z/(9*z*z+52*z+36)),('ENERGY_CURVE',lambda z:3*z*z/(3*z*z+26*z+36))]:
 head=head.replace(key,' '.join(f'({z:.12g},{fn(z):.12g})'for z in xs))
parts=[('The complete measured resolvent and kernel memory','ORIGINAL_RESOLVENT_MEMORY_PROOFS.md'),('Relative growth and growing pole removal','GROWTH_PROOFS.md'),('Sampling every original invariant row','SAMPLING_PROOFS.md'),('The four-label arithmetic receiver','ES_COMPLETE_PROOFS.md'),('The received primary-word determinant calculation','RECEIVED_RESOLVENT_PROOFS.md'),('Human sources and exact programme receivers','READER_SOURCES.md')]
def typeset_equations(tex):
 # These changes introduce line breaks or typeset the incoming ASCII notation.
 # The mathematical Markdown sources remain unchanged alongside the reader.
 replacements=[
 (r''' \det\mathscr Y(z)=\frac{z(3z+13)}{3(z+4)(z+9)},\quad
 \det Y_{\rm energy}(z)=\frac{3z^2}{3z^2+26z+36},\quad
 \det Y_{\rm arithmetic}(z)=\frac{9z^2}{9z^2+52z+36}.''',r'''\begin{gathered}
 \det\mathscr Y(z)=\frac{z(3z+13)}{3(z+4)(z+9)},\\
 \det Y_{\rm energy}(z)=\frac{3z^2}{3z^2+26z+36},\quad
 \det Y_{\rm arithmetic}(z)=\frac{9z^2}{9z^2+52z+36}.
 \end{gathered}'''),
 (r'''k\equiv1\pmod4,\quad k\ge17,\quad q=(k+1)^2,\quad k'=k-8,
\quad q'=(k-7)^2,\quad0<\delta<1/2,\quad\gamma>2,
\quad R_h=\sqrt{\delta^2+\gamma^2},\quad q\ge2kR_h.''',r'''\begin{gathered}
k\equiv1\pmod4,\quad k\ge17,\quad q=(k+1)^2,\quad k'=k-8,\\
q'=(k-7)^2,\quad0<\delta<1/2,\quad\gamma>2,\\
R_h=\sqrt{\delta^2+\gamma^2},\quad q\ge2kR_h.
\end{gathered}'''),
 (r'''d\sigma(y)=|\Gamma(1/4+iy/2)|^2\,dy/(2\pi),\quad
M_\sigma=\sqrt{2\pi},\quad
p_{n+1}=yp_n-n(n-1/2)p_{n-1},\quad h_n=M_\sigma n!(1/2)_n,''',r'''\begin{gathered}
d\sigma(y)=|\Gamma(1/4+iy/2)|^2\,dy/(2\pi),\quad M_\sigma=\sqrt{2\pi},\\
p_{n+1}=yp_n-n(n-1/2)p_{n-1},\quad h_n=M_\sigma n!(1/2)_n.
\end{gathered}'''),
 (r'''\ell_k=\log(q/k),\qquad C_{\rm ang}=\max\left\{0,
-q^{-1}\log(c_k/b_k^+)-2\ell_k,\ 
q^{-1}\log(\mathfrak U_k/b_k^-)+2\ell_k-{2q'\over q}\log r\right\}.''',r'''\begin{gathered}
\ell_k=\log(q/k),\\
C_{\rm ang}=\max\left\{\begin{aligned}0,&\ -q^{-1}\log(c_k/b_k^+)-2\ell_k,\\
&q^{-1}\log(\mathfrak U_k/b_k^-)+2\ell_k-{2q'\over q}\log r\end{aligned}\right\}.
\end{gathered}'''),
 (r''' p_{n+1}=yp_n-n(n-1/2)p_{n-1},\qquad
 \gamma_n=\|p_n\|_\sigma^2=M_\sigma n!(1/2)_n,
 \qquad\sum_{n\ge0}\frac{p_n(y)}{n!}t^n=(1+t^2)^{-1/4}e^{y\arctan t}.''',r'''\begin{gathered}
 p_{n+1}=yp_n-n(n-1/2)p_{n-1},\qquad \gamma_n=\|p_n\|_\sigma^2=M_\sigma n!(1/2)_n,\\
 \sum_{n\ge0}\frac{p_n(y)}{n!}t^n=(1+t^2)^{-1/4}e^{y\arctan t}.
\end{gathered}'''),
 (r''' \operatorname{codim}\mathcal Z_R\le a_0+b_0R,\quad
 \max_{|w|\le R}|A_z(w)|\le M_k(R)\|z\|,
 \quad M_k(R)=C_A\sqrt{n_E}e^{(2kR_h+8+4B_A)R},\quad z\in\mathcal Z_R.''',r'''\begin{gathered}
 \operatorname{codim}\mathcal Z_R\le a_0+b_0R,\quad \max_{|w|\le R}|A_z(w)|\le M_k(R)\|z\|,\\
 M_k(R)=C_A\sqrt{n_E}e^{(2kR_h+8+4B_A)R},\quad z\in\mathcal Z_R.
\end{gathered}'''),
 (r''' \rho_A=\min\{1,(v+1)!d_A/(2A_1\bar B_A^{v+1}e^{\bar B_A})\},\quad
 M_{0,k}=2\sqrt{n_E}\rho_A^{-v}d_A^{-1}e^{(4+kR_h)\rho_A},
 \quad\max_{|w|\le\rho_A}|A_z(w)|\le M_{0,k}\|z\|.''',r'''\begin{gathered}
 \rho_A=\min\{1,(v+1)!d_A/(2A_1\bar B_A^{v+1}e^{\bar B_A})\},\\
 M_{0,k}=2\sqrt{n_E}\rho_A^{-v}d_A^{-1}e^{(4+kR_h)\rho_A},\quad
 \max_{|w|\le\rho_A}|A_z(w)|\le M_{0,k}\|z\|.
\end{gathered}'''),
 (r'''R_1(x)=i\left[x^3+\left(\frac{19S^2}{7}+e_2\right)x-\frac{10S^3}{7}+\frac{Se_2}{2}-\frac{3e_3}{4}\right],
\quad R_2(x)=\frac{5S^2-13Sx}{7},\quad R_3(x)=\frac{i(S-4x)}{28},
\quad \mathfrak r_\nu=\sum_jR_\nu(\ell_j)/d_j^2.''',r'''\begin{gathered}
R_1(x)=i\left[x^3+\left(\frac{19S^2}{7}+e_2\right)x-\frac{10S^3}{7}+\frac{Se_2}{2}-\frac{3e_3}{4}\right],\\
R_2(x)=\frac{5S^2-13Sx}{7},\quad R_3(x)=\frac{i(S-4x)}{28},\quad
\mathfrak r_\nu=\sum_jR_\nu(\ell_j)/d_j^2.
\end{gathered}'''),
 (r'''\|G^{1/2}(O^{-1}/(p\sqrt w)-a_*e_0^*)Q^{-1/2}\|
\le\sqrt{\lambda_{\max}(G)/\lambda_{\min}(Q)}\,
\|O^{-1}/(p\sqrt w)-a_*e_0^*\|,
\quad a_*=\sqrt3(-i,1,0,0)^{\mathsf T}/8.''',r'''\begin{gathered}
\|G^{1/2}(O^{-1}/(p\sqrt w)-a_*e_0^*)Q^{-1/2}\|\\
\le\sqrt{\lambda_{\max}(G)/\lambda_{\min}(Q)}\,
\|O^{-1}/(p\sqrt w)-a_*e_0^*\|,\\
a_*=\sqrt3(-i,1,0,0)^{\mathsf T}/8.
\end{gathered}'''),
 (r'''A^\partial_{2q}=\frac{\Delta e^2}{M_\sigma}
(2q+1)^{3/2}(4q+1)^{R_k+1},\quad
B_k^\partial=\Delta M_\sigma
\left(\frac{2\Delta+R_k}{2\delta}\right)^{2(\Delta-1)},
\quad R_k=k\sqrt{\delta^2+\gamma^2},\quad M_\sigma=\sqrt{2\pi}.''',r'''\begin{gathered}
A^\partial_{2q}=\frac{\Delta e^2}{M_\sigma}(2q+1)^{3/2}(4q+1)^{R_k+1},\\
B_k^\partial=\Delta M_\sigma\left(\frac{2\Delta+R_k}{2\delta}\right)^{2(\Delta-1)},\\
R_k=k\sqrt{\delta^2+\gamma^2},\quad M_\sigma=\sqrt{2\pi}.
\end{gathered}'''),
 (r'''\mathcal K_k=\mathcal R\log\det H_{K,N},\qquad
E_k^{deep}=\min\{4(m+\Delta)E_k,\ 2m\omega_k+4(\Delta-m)E_k\}+2(m+\Delta)e^{-q}=o(kq).''',r'''\begin{gathered}
\mathcal K_k=\mathcal R\log\det H_{K,N},\\
E_k^{deep}=\min\{4(m+\Delta)E_k,\ 2m\omega_k+4(\Delta-m)E_k\}\\
\hfill{}+2(m+\Delta)e^{-q}=o(kq).
\end{gathered}'''),
 (r'''Let P\_lambda be the full positive spectral projections of H and put B\_lambda=J\_B\^{}dagger P\_lambda J\_B\textgreater=0. In the exact observed orthonormal frame,''',r'''Let \(P_\lambda\) be the full positive spectral projections of \(H\) and put \(B_\lambda=J_B^\dagger P_\lambda J_B\succeq0\). In the exact observed orthonormal frame,'''),
 (r'''For a fixed coefficient isomorphism S, use T'=STS\^{}-1, G'=S\textsuperscript{-*GS}-1, Lambda'=Lambda S\^{}-1. Then L'=SL, H'=SHS\^{}-1, and mathscrY'(z)=mathscrY(z) exactly. The original S=k/2+iy coefficient change and the full-unit isometries must be applied by this paired transport.''',r'''For a fixed coefficient isomorphism \(S\), use \(T'=STS^{-1}\), \(G'=S^{-*}GS^{-1}\), \(\Lambda'=\Lambda S^{-1}\). Then \(L'=SL\), \(H'=SHS^{-1}\), and \(\mathscr Y'(z)=\mathscr Y(z)\) exactly. The original \(S=k/2+iy\) coefficient change and the full-unit isometries must be applied by this paired transport.'''),
 (r'''epsilon\_k\^{}edge=o(1)''',r'''\(\epsilon_k^{\rm edge}=o(1)\)'''),
 ]
 for a,b in replacements:tex=tex.replace(a,b)
 def filename(m):
  value=m[1].replace(r'\_', '_').replace(r'\ ', ' ')
  return r'\path{'+value+'}' if '/' in value or len(value)>40 else m[0]
 tex=re.sub(r'\\texttt\{([^{}]+)\}',filename,tex)
 tex=tex.replace('bee43be41d2f6f872869d5e258fa5f752335a5ad',r'\nolinkurl{bee43be41d2f6f872869d5e258fa5f752335a5ad}')
 tex=tex.replace('256bfb0f4eb295bf3094c81f6c166cafdb96c316',r'\nolinkurl{256bfb0f4eb295bf3094c81f6c166cafdb96c316}')
 tex=tex.replace(r'workbenches/splitzero-tandem/continuations/20260921-local-covariance-activation/ 009/CONDUCTOR\_DIVISOR\_COVARIANCE\_RETURN.tex',r'\path{workbenches/splitzero-tandem/continuations/20260921-local-covariance-activation/009/CONDUCTOR_DIVISOR_COVARIANCE_RETURN.tex}')
 return tex
text=head
for title,name in parts:
 f=P/name
 if not f.exists():raise RuntimeError('Required complete proof not ready: '+name)
 target=O/(f.stem+'.tex')
 run=subprocess.run(['pandoc',str(f),'-f','markdown+tex_math_single_backslash+tex_math_dollars+raw_tex','-t','latex','--wrap=none','-o',str(target)],capture_output=True,text=True)
 if run.returncode:raise RuntimeError(run.stderr)
 tex=typeset_equations(target.read_text(encoding='utf-8'))
 tex=re.sub(r'\\texttt\{([a-fA-F0-9]{40}|[a-fA-F0-9]{64})\}',lambda m:r'\nolinkurl{'+m[1]+'}',tex)
 text+='\n\\clearpage\\part{'+title+'}\n'+tex
text+=r'\end{document}'
out=O/'ORIGINAL_GROWTH_RESOLVENT_READER.tex';out.write_text(text,encoding='utf-8')
for j in range(3):
 run=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error',out.name],cwd=O,capture_output=True,text=True,encoding='utf-8',errors='replace')
 (O/'LATEX_OUTPUT.txt').write_text(run.stdout,encoding='utf-8')
 if run.returncode:raise RuntimeError(run.stdout[-6000:])
pdf=out.with_suffix('.pdf');pages=len(PdfReader(pdf).pages)
qa=Path(tempfile.gettempdir())/'splitzero020-rendered';qa.mkdir(exist_ok=True);shutil.copyfile(pdf,qa/'reader.pdf')
run=subprocess.run(['pdftoppm','-r','80','-png','reader.pdf','page'],cwd=qa,capture_output=True,text=True)
if run.returncode:raise RuntimeError(run.stderr)
files=[f for f in sorted(qa.glob('page-*.png'))if int(f.stem.split('-')[-1])<=pages]
for st in range(0,len(files),4):
 im=Image.new('RGB',(1400,2000),'#e4e8eb');draw=ImageDraw.Draw(im)
 for j,f in enumerate(files[st:st+4]):
  a=Image.open(f).convert('RGB');a.thumbnail((685,965));x=(j%2)*700+(700-a.width)//2;y=(j//2)*1000+25
  im.paste(a,(x,y));draw.text((x,y-18),f.name,fill='black')
 im.save(qa/f'contact-{st//4+1:02d}.png')
log=out.with_suffix('.log').read_text(encoding='utf-8',errors='replace')
report=dict(pages=pages,overfull=re.findall(r'Overfull[^\n]*',log),undefined=re.findall(r'[^\n]*undefined[^\n]*',log),missing=re.findall(r'[^\n]*Missing character[^\n]*',log),visual='pending',pdf=pdf.name,qa='splitzero020-rendered')
(P/'READER_BUILD.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps(report))
