from pathlib import Path
import subprocess, re, json, shutil
from PIL import Image,ImageDraw
from pypdf import PdfReader
P=Path(__file__).parent;O=P/'reader';O.mkdir(exist_ok=True)
head=r'''\documentclass[11pt]{article}
\usepackage[a4paper,margin=24mm]{geometry}
\usepackage{amsmath,amssymb,mathtools,amsthm,mathrsfs,tikz,pgfplots,longtable,booktabs,array,calc,enumitem}
\usepackage[hidelinks,hypertexnames=false]{hyperref}\usepackage{xurl}
\usepackage{fontspec}\setmainfont{DejaVu Serif}
\usetikzlibrary{arrows.meta,positioning}\pgfplotsset{compat=1.18}
\setlength{\emergencystretch}{3em}\providecommand{\tightlist}{}
\setcounter{secnumdepth}{0}
\title{Moving rational sources, arithmetic collisions\\and complete observed memory}
\author{Split-Zero research programme}
\date{21 September 2026\\SZ-20260921-017}
\begin{document}\maketitle
The original arithmetic observation now has a kernel-energy bound valid
throughout source activation. This bound controls the complete observed
memory at its late spectral scale, where the earlier comparison for
subexponential regularizers did not apply. The mass in this receiver is
the actual derivative of its Schur pencil:
\[
A_N\succeq a_NI,\qquad
W_N=\mathcal F_N'(0)=I+B_N^\dagger A_N^{-2}B_N.
\]
The proof retains every coupling block. In the original four-cutoff
return, at the specified critical source activation and native late
regularizer, it gives
\[
\mathcal R\log\frac{\det\mathcal F_N(z_k^*)}{\det\mathcal F_N(0)}
=2q\log(4/\pi)+o(q).
\]
At the canonical endpoint the same quantity is
$4q\log(4/\pi)+o(q)$ (KG39--42). The mass-weighted full observed
heat and the explicit energy-graph heat both have return two in the
strict critical interval. The raw observed weights remain in their
own exact formulas.

A second result allows all rational poles to move and collide inside
a fixed compact set disjoint from the original arithmetic lattice.
The source and observed Grams have the same harmonic activation scale;
every least filter singular value is determined up to $e^{o(q)}$.
The full observed heat operator is localized in the observed rational
sector with a quantitative trace-norm error (MF9, MF34--41).

At collisions with the arithmetic spectrum itself, a polynomial frame
continues the entire sector. PC1--10 evaluates its resultant and its
complete primary kernel. PC15--34 gives corrected chain sections,
retains any new observation kernel, and proves its exact determinant
transfer. Every source coordinate, original minimum and kernel factor
is retained. These finite boundary formulas extend the maps; they do
not import an off-spectrum analytic bound across a vanishing observed
fraction.

The first canonical kernel allocation and the original complex-current
phases still require their own evaluations. The complete proofs below
state the finite source guards and the exact retained status of the
high-endpoint analytic inputs. Source files and earlier complete
providers accompany this reader. Published edition 016 is preserved.
\begingroup\small\tableofcontents\endgroup\clearpage
\section*{Two different effects at the same arithmetic collision}
\addcontentsline{toc}{section}{Two effects at the same arithmetic collision}
For the exact auxiliary algebra $Q=y^2+1$, take $D=y-z$ and
$z=i+t$, with the real parameter $t$ shown below.
The coefficient metric is $G=I$ only in this stated example.
The globally defined frame is $F_D=(z,1)^{\mathsf T}$.
\begin{figure}[ht]\centering
\begin{tikzpicture}
\begin{axis}[width=.95\textwidth,height=6.6cm,domain=-2:2,samples=151,
xlabel={$t$ in $z=i+t$},ylabel={exact observed fraction},
xmin=-2,xmax=2,ymin=0,ymax=.57,grid=major,
legend style={at={(.5,1.03)},anchor=south,draw=none,font=\small}]
\addplot[blue,very thick]{1/(2+x*x)};
\addlegendentry{$\Lambda(a,b)=b:\ 1/(2+t^2)$}
\addplot[red,dashed,very thick]{x*x/(2*(2+x*x))};
\addlegendentry{$\Lambda(a,b)=a-ib:\ t^2/[2(2+t^2)]$}
\end{axis}
\end{tikzpicture}
\caption{PC29--30 gives both exact curves from the full quotient
metric $Q_B=(\Lambda\Lambda^*)^{-1}$. At $t=0$ the rational
numerator inverse has a pole in both cases. The first observation
continues to detect the sector. The second acquires the one-dimensional
kernel $Z=\mathbb C(i,1)^{\mathsf T}$, retained by PC25 and PC27.
This is an exact finite illustration, not a computed zeta-zero packet.}
\end{figure}
\begin{figure}[ht]\centering
\begin{tikzpicture}[>=Stealth]
\node[draw,minimum width=4cm,minimum height=1cm](e)at(0,0){$E\xrightarrow{\Lambda}B$};
\node[draw,minimum width=7cm,minimum height=1cm](r)at(0,-3)
{$Z\oplus(E/V)\xrightarrow{\ (z,c)\mapsto\bar\Lambda c\ }B/W$};
\draw[->]([xshift=-1cm]e.south)--node[left]{$p$}([xshift=-1cm]r.north);
\draw[->]([xshift=1cm]r.north)--node[right]{$j$}([xshift=1cm]e.south);
\node[align=center]at(0,-4.3){$Z=V\cap\ker\Lambda,\quad W=\Lambda V$\\
$pj=I,\qquad I-jp=dh+hd$};
\end{tikzpicture}
\caption{The exact reduction retains the new kernel $Z$ when
observation rank drops. The minimum source section is adjusted by
$(I-h\Lambda)$; PC17--28 proves every arrow and its metric.
PC32--34 gives the positive-determinant transfer on $K/Z$ and
retains the inherited metric on $Z$.}
\end{figure}\clearpage
\section*{The full memory and its actual mass}
\addcontentsline{toc}{section}{The full memory and its actual mass}
\begin{figure}[ht]\centering
\begin{tikzpicture}[>=Stealth]
\node[draw,minimum width=3.5cm,minimum height=1cm](k)at(0,0){$K,\ A\succeq a_NI$};
\node[draw,minimum width=3.5cm,minimum height=1cm](b)at(7,0){$LB,\ D_H$};
\draw[->](b.north) .. controls +(0,1.2) and +(0,1.2) .. node[above]{$B_H$}(k.north);
\draw[->](k.south) .. controls +(0,-1.2) and +(0,-1.2) .. node[below]{$B_H^\dagger$}(b.south);
\node[draw,align=center,text width=11.5cm]at(3.5,-2.9)
{$\mathcal F(z)=zI+D_H-B_H^\dagger(A+zI)^{-1}B_H$\\[3pt]
$S=\mathcal F(0),\qquad W=\mathcal F'(0)$};
\node[align=center]at(3.5,-4.4)
{$\displaystyle\frac{S+zW}{1+z/a_N}\preceq\mathcal F(z)\preceq S+zW,\quad z\ge0$};
\end{tikzpicture}
\caption{KG17--30 retains the full arithmetic energy blocks and
proves the displayed finite relative estimate. The mass $W$ is the
first time moment of the original memory, plus the identity.
The Schur construction is connected to the original-author treatment
of Dusson, Sigal and Stamm, \emph{The Feshbach--Schur map and
perturbation theory} (2021), theorem \texttt{thm:isospF} and
equation \texttt{QP},
\href{https://arxiv.org/abs/2105.02058v1}{arXiv:2105.02058v1}.
The activated arithmetic estimates and their complete proofs are KG1--42.}
\end{figure}\clearpage
'''
def convert(name):
    t=O/(Path(name).stem+'.tex')
    r=subprocess.run(['pandoc',str(P/name),'-f','markdown+tex_math_single_backslash+tex_math_dollars+raw_tex','-t','latex','--wrap=none','-o',str(t)],capture_output=True,text=True)
    if r.returncode:raise RuntimeError(r.stderr)
    return re.sub(r'(?<![A-Za-z0-9])([A-Fa-f0-9]{64})(?![A-Za-z0-9])',lambda m:r'\nolinkurl{'+m[1]+'}',t.read_text(encoding='utf-8'))
parts=[('Kernel energy and complete observed memory','KERNEL_GAP_PROOFS.md'),('Moving rational families and full filtered heat','ACTIVATED_RATIONAL_PROOFS.md'),('Arithmetic collisions and exact observation complexes','POLYNOMIAL_BOUNDARY_AND_CHAIN_PROOFS.md')]
text=head
for title,name in parts:text+='\n\\clearpage\\part{'+title+'}\n'+convert(name)+'\n'
text+=r'''
\section*{Human sources used in this continuation}
\addcontentsline{toc}{section}{Human sources used in this continuation}
Geneviève Dusson, Israel Michael Sigal and Benjamin Stamm,
\emph{The Feshbach--Schur map and perturbation theory} (2021),
\href{https://arxiv.org/abs/2105.02058v1}{arXiv:2105.02058v1}.
The original-author TeX was read at lines 398--507, specifically
\texttt{thm:isospF}, \texttt{QP} and \texttt{prop:U-prop-SA}.
KG17--38 uses the exact elimination and reconstruction framework;
the activated estimates are proved in this reader.

T. H. Koornwinder, R. Wong, R. Koekoek and R. F. Swarttouw,
with W. P. Reinhardt, DLMF Chapter 18:
\href{https://dlmf.nist.gov/18.23.E7}{18.23.7}
(Meixner--Pollaczek generating function) and
\href{https://dlmf.nist.gov/18.22.E8}{18.22.8}
(recurrence). Their original TeX equations were reread for MF20,
MF32 and MF42, through the full RF source bounds.

R. A. Askey and R. Roy, DLMF Chapter 5,
\href{https://dlmf.nist.gov/5.8.E3}{5.8.3} (Gamma product).
Its retained original TeX supplies the source-envelope identity in
MF5 and MF42 through IVO and RF. Complete versions, hashes,
reading coverage and exact programme proof links are recorded in
\texttt{SOURCE\_LEDGER.json} and the accompanying rational-source
ledger. A source reference records the stated use, not an exhaustive
reading claim or a new proof of the earlier high-endpoint asymptotic.
\end{document}
'''
out=O/'MOVING_RATIONAL_FAMILY_COMPLETE_READER.tex';out.write_text(text,encoding='utf-8')
for _ in range(3):
    r=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error',out.name],cwd=O,capture_output=True,text=True,encoding='utf-8',errors='replace')
    (O/'LATEX_OUTPUT.txt').write_text(r.stdout,encoding='utf-8')
    if r.returncode:raise RuntimeError(r.stdout[-5000:])
pdf=out.with_suffix('.pdf');count=len(PdfReader(pdf).pages)
qa=O/'qa';qa.mkdir(parents=True,exist_ok=True)
shutil.copyfile(pdf,qa.parent/pdf.name)
subprocess.run(['pdftoppm','-r','75','-png',pdf.name,'qa/page'],cwd=qa.parent,capture_output=True,check=True)
pages=[p for p in sorted(qa.glob('page-*.png')) if int(p.stem.split('-')[-1])<=count]
for st in range(0,len(pages),4):
    im=Image.new('RGB',(1400,2000),'#e4e8eb');dr=ImageDraw.Draw(im)
    for j,p in enumerate(pages[st:st+4]):
        a=Image.open(p).convert('RGB');a.thumbnail((685,965));x=(j%2)*700+(700-a.width)//2;y=(j//2)*1000+25
        im.paste(a,(x,y));dr.text((x,y-18),p.name,fill='black')
    im.save(qa/f'contact-{st//4+1:02d}.png')
log=out.with_suffix('.log').read_text(encoding='utf-8',errors='replace')
report={'pages':count,'overfull':re.findall(r'Overfull[^\n]*',log),'undefined':re.findall(r'[^\n]*undefined[^\n]*',log),'missing':re.findall(r'[^\n]*Missing character[^\n]*',log),'visual':'pending','pdf':str(pdf),'qa':str(qa)}
(P/'READER_BUILD.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps(report))
