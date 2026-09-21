from pathlib import Path
import subprocess,re,json,shutil,tempfile
from PIL import Image,ImageDraw
from pypdf import PdfReader
import sympy as sp
P=Path(__file__).parent;O=P/'reader';O.mkdir(exist_ok=True)
head=r'''\documentclass[11pt]{article}
\usepackage[a4paper,margin=24mm]{geometry}
\usepackage{amsmath,amssymb,mathtools,amsthm,mathrsfs,tikz,pgfplots,longtable,booktabs,array,calc,enumitem}
\usepackage[hidelinks,hypertexnames=false]{hyperref}\usepackage{xurl}
\usepackage{fontspec}\setmainfont{DejaVu Serif}
\usetikzlibrary{arrows.meta,positioning,calc}\pgfplotsset{compat=1.18}
\setlength{\emergencystretch}{4em}\providecommand{\tightlist}{}\newcounter{none}
\setcounter{secnumdepth}{0}\allowdisplaybreaks
\title{The original invariant determinant\\and an arithmetic collision}
\author{Split-Zero research programme}
\date{21 September 2026\\SZ-20260921-018}
\begin{document}\maketitle
The original observation kernel can be taken through a collision involving
$(k-7)^2$ roots of the full arithmetic polynomial. The literal polynomial
word is singular on the full quotient and injective on the entire original
kernel. Its image has the evaluated four-cutoff return
\[
\mathcal R\log\det[(D(M)I_K)^*G_ND(M)I_K]
=(8k-16)C_\partial q+O_h(k^2\log(q+2)).
\]
The corresponding boundary quotient has return $o(kq)$. Their different
metrics are joined by a complete positive graph determinant, with all
cross terms retained. IC19--34 proves the word estimate for the actual
unpaired factor and every kernel direction, including its finite guards.

The complete invariant determinant now also has two executable forms:
one uses a positive rational Gamma reference and the full projected row
covariance; the other uses positive changes of the original relation
Gram at each cutoff. Every invariant row remains in both formulas. The
sharper existing comparison for the same physical source is propagated
into the finite error, giving $O_{h,A}(q\log(q+2))$ rather than the weaker
bound available from the older source-width statement alone.

The initial original-period kernel coefficient and the original complex
current signs remain unevaluated. Numerical values below are explicitly
identified scalar references or auxiliary finite examples. They are not
assigned to hypothetical zeta zeros. Earlier source hypotheses and the
inherited status of equilibrium and high-endpoint results remain explicit.
\begingroup\small\tableofcontents\endgroup\clearpage
\section*{The actual collision and the two metrics}
\addcontentsline{toc}{section}{The actual collision and the two metrics}
\begin{figure}[ht]\centering
\begin{tikzpicture}[scale=.37]
\foreach \a in {0,...,13}{\foreach \b in {0,...,13}{
\ifnum\a>3\ifnum\a<10\ifnum\b>3\ifnum\b<10
\fill[teal!85!black](\b,\a)circle(.14);
\else\fill[orange!85!black](\b,\a)circle(.11);\fi
\else\fill[orange!85!black](\b,\a)circle(.11);\fi
\else\fill[orange!85!black](\b,\a)circle(.11);\fi
\else\fill[orange!85!black](\b,\a)circle(.11);\fi}}
\draw[->](-.8,-.8)--(14,-.8)node[right]{$b$};
\draw[->](-.8,-.8)--(-.8,14)node[above]{$a$};
\foreach \j in {0,4,9,13}{\node[below]at(\j,-.8){\small\j};\node[left]at(-.8,\j){\small\j};}
\draw[teal!80!black,thick](3.55,3.55)rectangle(9.45,9.45);
\node[anchor=west,align=left]at(16,10){\textcolor{teal!85!black}{Interior: $D=0$}\\$q'=36$ roots};
\node[anchor=west,align=left]at(16,6){\textcolor{orange!85!black}{Boundary: $O=0$}\\$\Delta=160$ roots};
\node[anchor=west,align=left]at(16,1){$Q=DO$, $q=196$\\$\omega_{ab}=(2b-13)\gamma-i(2a-13)\delta$};
\end{tikzpicture}
\caption{Exact index diagram for the algebraic sample $k=13$ and pivot
$(r_*,s_*)=(4,4)$. The axes are the integer indices, not the complex-plane
distance. This sample illustrates IC2--8; it is not an assertion that
IC19's eventual analytic guards hold at $k=13$. The conductor pivot
forces $x_{\mathcal I}=Fx_\partial$ on the actual kernel, proving
$K\cap\ker D(M)=0$.}
\end{figure}
\[
\begin{array}{ccc}
I_Kc&\xrightarrow{D(M)}&[D P_Kc]\\
\downarrow\pi_\partial&&\downarrow[D p]\mapsto[p]_O\\
J_\partial c&&[P_Kc]_O
\end{array}
\]
The left target uses the attained boundary metric $G_N^\partial$.
The right target uses the complete source $|D|^2d\mu_k$ at degree
$N-q'$. The exact cost of the original conductor-zero section is
$\log\det(I+\Xi_N^*\Xi_N)$ (IC35--38). No isometry is inserted.
\clearpage
\section*{Every added coefficient and every complete relation}
\addcontentsline{toc}{section}{Every added coefficient and every complete relation}
The original moment matrix and the complete row matrix grow by one
column at each cutoff. Their Schur complements give
\[
C_M=C_{M-1}+f_Mf_M^*/\nu_M,\qquad
s_M=f_M^*C_{M-1}^{-1}f_M/\nu_M\ge0.
\]
The new complete relation has squared distance $\rho_L$ from all earlier
relations, and leading coefficient $a_L=\mu_v\binom{q+L}{v}$.
The original kernel loses the exact volume factor
\[
d_L=\frac{\rho_L}{|a_L|^2\nu_{g+L}(1+s_{g+L})}\ge1.
\]
CL13--14 also identifies its precise energy content: $d_L$ is one plus
the new relation's energy in the original residual kernel divided by
its new source energy plus its observed energy. Every projection uses
the old attained metric $Q_{L-1}$.
\begin{figure}[ht]\centering
\begin{tikzpicture}
\begin{axis}[ybar,width=.93\textwidth,height=6cm,xlabel={Relation index $L$},
ylabel={Weighted $\log d_L$},xtick={0,1,2,3,4,5,6},ymin=0,
enlarge x limits=.10,bar width=12pt]
\addplot[fill=teal!65,draw=teal!80!black] coordinates {BAR_DATA};
\end{axis}\end{tikzpicture}
\caption{Exact auxiliary complex-shift example CI26, shown with
decimal heights. The four original signs give weights $1,2,2,2,2,2,1$;
their sum is the full graph-kernel return $6.0207468765\ldots$.
All two observation rows and seven complete relation columns are present.
CI14--16 proves positivity and the exact sum. The rational factors are
retained in the executed checker receipt. This is not a native zero packet.}
\end{figure}
The finite source map underlying these calculations is KF1--55 and
CG29--32, with its complete physical comparison carried forward.
The scalar reference is evaluated by integer Hankel condensation
(CI17--24), using the identity in Christian Krattenthaler,
\emph{Advanced Determinant Calculus}, Section 2.3,
\href{https://arxiv.org/abs/math/9902004v3}{arXiv:math/9902004v3}.
\clearpage
'''
values=(json.loads((P/'CUTOFF_INNOVATION_CHECKS.json').read_text()) if (P/'CUTOFF_INNOVATION_CHECKS.json').exists() else json.loads((P/'CHECKS.json').read_text())['cutoff'])['retention_factors']
bars=' '.join('('+key+','+str(float(sp.log(sp.Rational(value)))*(1 if key in ['0','6'] else 2))+')' for key,value in values.items())
head=head.replace('BAR_DATA',bars)
finite=[P/'finite_derivation/FINITE_INVARIANT_PROOFS.md'] if (P/'finite_derivation').exists() else [P/'FINITE_INVARIANT_PROOFS.md']
if len(finite)!=1: raise RuntimeError('Expected one completed finite proof source')
collision=P/'collision_derivation/COLLISION_PROOFS.md' if (P/'collision_derivation').exists() else P/'COLLISION_PROOFS.md'
parts=[('The complete finite invariant determinant',finite[0]),('The arithmetic collision and original word image',collision),('Positive cutoff increments and exact scalar execution',P/'CUTOFF_INNOVATION_PROOFS.md')]
text=head
for title,f in parts:
    target=O/(f.stem+'.tex')
    r=subprocess.run(['pandoc',str(f),'-f','markdown+tex_math_single_backslash+tex_math_dollars+raw_tex','-t','latex','--wrap=none','-o',str(target)],capture_output=True,text=True)
    if r.returncode:raise RuntimeError(r.stderr)
    tex=target.read_text(encoding='utf-8')
    tex=re.sub(r'\\texttt\{([a-fA-F0-9]{40}|[a-fA-F0-9]{64})\}',lambda m:r'\nolinkurl{'+m[1]+'}',tex)
    tex=tex.replace(r' \ell_{k,2q}\|p\|_\sigma^2\le\|p\|_{\mu_k}^2\le u_k\|p\|_\sigma^2,',r'\begin{gathered}\ell_{k,2q}\|p\|_\sigma^2\le\|p\|_{\mu_k}^2\le u_k\|p\|_\sigma^2,\\')
    tex=tex.replace(r' \tag{FI1}',r'\end{gathered}\tag{FI1}')
    tex=tex.replace(r'\omega_{ab}=(2b-k)\gamma-i(2a-k)\delta,\quad',r'\begin{gathered}\omega_{ab}=(2b-k)\gamma-i(2a-k)\delta,\quad')
    tex=tex.replace(r'0<\delta<\tfrac12,\quad\gamma>2,\quad',r'0<\delta<\tfrac12,\quad\gamma>2,\\')
    tex=tex.replace(r'E_k=\mathbb C[y]/(Q_k),\quad M[f]=[yf].',r'E_k=\mathbb C[y]/(Q_k),\quad M[f]=[yf].\end{gathered}')
    tex=tex.replace(r'\nu_M^{-1}(-H_{M-1}^{-1}h_M,1)^{\mathsf T}(-H_{M-1}^{-1}h_M,1)^*',r'\nu_M^{-1}\binom{-H_{M-1}^{-1}h_M}{1}\binom{-H_{M-1}^{-1}h_M}{1}^{*}')
    tex=tex.replace(r'and \(\nu_M^{-1}\binom',r'and\[\nu_M^{-1}\binom')
    tex=tex.replace(r'{1}^{*}\). Multiplication',r'{1}^{*}.\] Multiplication')
    tex=re.sub(r'(?<![A-Za-z0-9])([a-fA-F0-9]{64})(?![A-Za-z0-9])',lambda m:r'\nolinkurl{'+m[1]+'}',tex)
    text+='\n\\clearpage\\part{'+title+'}\n'+tex
text+=r'\end{document}'
out=O/'INVARIANT_DETERMINANT_COLLISION_READER.tex';out.write_text(text,encoding='utf-8')
for j in range(3):
    r=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error',out.name],cwd=O,capture_output=True,text=True,encoding='utf-8',errors='replace')
    (O/'LATEX_OUTPUT.txt').write_text(r.stdout,encoding='utf-8')
    if r.returncode:raise RuntimeError(r.stdout[-5000:])
pdf=out.with_suffix('.pdf');count=len(PdfReader(pdf).pages)
qa=Path(tempfile.gettempdir())/'splitzero018-rendered';qa.mkdir(exist_ok=True)
shutil.copyfile(pdf,qa/'reader.pdf')
render=subprocess.run(['pdftoppm','-r','80','-png','reader.pdf','page'],cwd=qa,capture_output=True,text=True)
if render.returncode:raise RuntimeError(render.stderr)
pages=[f for f in sorted(qa.glob('page-*.png')) if int(f.stem.split('-')[-1])<=count]
for st in range(0,len(pages),4):
    im=Image.new('RGB',(1400,2000),'#e4e8eb');draw=ImageDraw.Draw(im)
    for j,f in enumerate(pages[st:st+4]):
        a=Image.open(f).convert('RGB');a.thumbnail((685,965));x=(j%2)*700+(700-a.width)//2;y=(j//2)*1000+25
        im.paste(a,(x,y));draw.text((x,y-18),f.name,fill='black')
    im.save(qa/f'contact-{st//4+1:02d}.png')
log=out.with_suffix('.log').read_text(encoding='utf-8',errors='replace')
report=dict(pages=count,overfull=re.findall(r'Overfull[^\n]*',log),undefined=re.findall(r'[^\n]*undefined[^\n]*',log),missing=re.findall(r'[^\n]*Missing character[^\n]*',log),visual='pending',pdf=str(pdf),qa=str(qa))
(P/'READER_BUILD.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps(report))
