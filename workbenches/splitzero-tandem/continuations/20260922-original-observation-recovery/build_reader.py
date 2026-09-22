from pathlib import Path
import subprocess,re,json,shutil,tempfile
from pypdf import PdfReader
from PIL import Image,ImageDraw
P=Path(__file__).parent
O=P/'reader';O.mkdir(exist_ok=True)
head=r'''\documentclass[11pt]{article}
\usepackage[a4paper,margin=24mm]{geometry}
\usepackage{amsmath,amssymb,mathtools,amsthm,mathrsfs,tikz,pgfplots,longtable,booktabs,array,calc,enumitem,float}
\usepackage[hidelinks,hypertexnames=false]{hyperref}\usepackage{xurl}
\usepackage{fontspec}\setmainfont{DejaVu Serif}
\usetikzlibrary{arrows.meta,positioning,calc}\pgfplotsset{compat=1.18}
\setlength{\emergencystretch}{4em}\providecommand{\tightlist}{}\newcounter{none}
\setcounter{secnumdepth}{0}\allowdisplaybreaks
\title{Finite recovery of the original observation\\and its kernel determinant}
\author{Split-Zero research programme}
\date{22 September 2026\\SZ-20260922-021}
\begin{document}\maketitle
The original measured resolvent now gives a finite reconstruction of every
primary kernel angle. Its zero-frequency response has exactly the same
eigenvalues strictly between zero and one as the kernel-angle matrix.
Their zero and unit multiplicities are calculated, and their positive
determinants agree. The proof keeps the complete original metric and gives
the actual map between the corresponding eigenspaces.

Scalar determinant measurements retain less information. The loss is
bounded sharply by the full-word spectral width and three original
dimensions. A recovered scalar leading coefficient supplies the kernel
return through $kq$ without extracting individual roots. This is an exact
recovery formula with finite error bounds; the native scalar values still
require evaluation.

The arithmetic observation has a separate complete construction from its
original conductor. Eight powers leave at most 128 directions; eighty powers
recover the whole space on the proved original period domain. A polynomial
quotient keeps every arithmetic pole, every source coefficient and the
derivative term needed for the current's sign. A direct source estimate
proves that the 128-direction determinant contributes only $O(q)$.

All three calculations preserve the cutoffs $q-1,q,2q-1,2q$ and signs
$+,+,-,-$. The period-dependent kernel coefficient and the original
projected-current values remain unevaluated. The complete proofs follow;
the unchanged predecessor proofs and human source records accompany them.
\begingroup\small\tableofcontents\endgroup\clearpage
\section*{Three exact receivers for the same original kernel}
\addcontentsline{toc}{section}{Three exact receivers for the same original kernel}
\[
 Q=(\Lambda G^{-1}\Lambda^*)^{-1},\quad L=G^{-1}\Lambda^*Q,\quad
 H_K=I_K^*GI_K,\quad H=G^{-1}T^*GT .
\]
\begin{figure}[H]\centering
\begin{tikzpicture}[>=Latex,node distance=11mm,
 box/.style={draw,rounded corners,align=center,text width=12cm,inner sep=7pt}]
\node[box] (data) {Original response matrices\\
 $\mathscr Y(z)=\Lambda z(zI+H)^{-1}L$};
\node[box,below=of data] (rec) {Anchored differences and an actual invertible Loewner minor\\
 $F(x)=C_1^*(xI+A)^{-1}C_1$ \quad (MR2--5)};
\node[box,below=of rec] (end) {Recovered zero-frequency matrix and original angles\\
 $Y_*=\Lambda P_{\ker T}^G L$, \quad
 $\det_+Y_*=\det_+\Gamma_K$ \quad (MR7--11)};
\node[box,below=of end] (orig) {Original fixed-frame kernel determinant, on the transverse domain\\
 $\log\det H_K=\log\det B_K-\log\det_+Y_*$ \quad (MR17)};
\draw[->] (data)--(rec);\draw[->](rec)--(end);\draw[->](end)--(orig);
\end{tikzpicture}
\caption{Every arrow is a proved map in the original metric. The classical
Loewner factorization is credited to Mayo--Antoulas and to
Zhang--Gosea--Antoulas at the exact source locations in the proof.
Zero-angle intersections are retained in MR11 and SD10.
The scalar alternative uses $24k-64$ determinant samples at each cutoff,
with its sharp finite loss in SD6--7.}
\end{figure}
\[
0\le\mathcal K_k-\mathcal R[-\log\det_+Y_{*,N}]
\le2m\omega_k=o(kq),\qquad
\mathcal Rf=f_{q-1}+f_q-f_{2q-1}-f_{2q}.
\]
\clearpage
\section*{The polynomial quotient retains the current correction}
\addcontentsline{toc}{section}{The polynomial quotient retains the current correction}
The exact finite example in BD18 has two observation chains of lengths
$(2,1)$. Its original action and metric are printed in full there.
\[
 P(z)=\begin{pmatrix}z^2&z&1&0&0\\0&0&0&z&1\end{pmatrix},
\quad
 D(z)=\begin{pmatrix}1-z-z^3&-z^2\\-z&1-iz-z^2\end{pmatrix}.
\]
\begin{figure}[H]\centering
\begin{tikzpicture}[>=Latex]
\node[draw,circle,minimum size=15mm] (k10) at(0,1.8){$e_{1,0}$};
\node[draw,circle,minimum size=15mm] (k11) at(3,1.8){$e_{1,1}$};
\node[draw,circle,minimum size=15mm] (k12) at(6,1.8){$e_{1,2}$};
\draw[->](k10)--node[above]{$A$}(k11);
\draw[->](k11)--node[above]{$A$}(k12);
\node at(0,.6){$z^2$};\node at(3,.6){$z$};\node at(6,.6){$1$};
\node[draw,circle,minimum size=15mm](s0) at(0,-1){$e_{2,0}$};
\node[draw,circle,minimum size=15mm](s1) at(3,-1){$e_{2,1}$};
\draw[->](s0)--node[above]{$A$}(s1);
\node at(0,-2.2){$z$};\node at(3,-2.2){$1$};
\node[draw,rounded corners,align=center,text width=5cm] at(9,-.6)
 {Terminal actions remain in $D(z)$\\
 $P(z)(I-zA)=D(z)\Lambda$};
\end{tikzpicture}
\caption{The displayed arrows are the nonterminal action only.
They do not claim invariant cyclic summands.
The omitted terminal arrows are retained exactly by $D(z)$ (BD4--5).
The printed powers are the corresponding quotient-row coefficients.
The full coefficient Gram recovers the original source metric (BD9).}
\end{figure}
In this same example, for $b=(1,i)^{\mathsf T}$ and its original
attained output metric $Q$,
\[
 M_B=\mathcal C_{10}Q-D'(0),\qquad
 i b^*(QM_B-M_B^*Q)b=-\frac7{18}.
\]
Using only $\mathcal C_{10}Q$ gives $5/18$ instead.
The missing contribution is exactly $-2/3$.
These are auxiliary exact matrix values, not a native xi-packet sign.
\clearpage
'''
parts=[('Matrix recovery and every original angle','MATRIX_RECOVERY_PROOFS.md'),
 ('Scalar recovery and its sharp information loss','SCALAR_RECOVERY_PROOFS.md'),
 ('Bounded arithmetic probes and complete source control','BOUNDED_DEGREE_PROOFS.md'),
 ('Sources, reading coverage and mathematical status','READER_SOURCES.md')]
text=head
for title,name in parts:
 f=P/name
 if not f.exists():
  alt={'SCALAR_RECOVERY_PROOFS.md':'scalar_derivation','BOUNDED_DEGREE_PROOFS.md':'bounded_degree_derivation'}.get(name)
  if alt:f=P/alt/name
 if not f.exists():raise RuntimeError('Proof not ready: '+name)
 target=O/(f.stem+'.tex')
 r=subprocess.run(['pandoc',str(f),'-f','markdown+tex_math_single_backslash+tex_math_dollars+raw_tex','-t','latex','--wrap=none','-o',str(target)],capture_output=True,text=True)
 if r.returncode:raise RuntimeError(r.stderr)
 tex=target.read_text(encoding='utf-8')
 tex=tex.replace(r'''K=\ker\Lambda,\quad m=\dim K,\quad b=\dim B=q-m,\quad
Q=(\Lambda G^{-1}\Lambda^*)^{-1},\quad
L=G^{-1}\Lambda^*Q,\quad H_K=I_K^*GI_K.''',r'''\begin{gathered}
K=\ker\Lambda,\quad m=\dim K,\quad b=\dim B=q-m,\\
Q=(\Lambda G^{-1}\Lambda^*)^{-1},\quad
L=G^{-1}\Lambda^*Q,\quad H_K=I_K^*GI_K.
\end{gathered}''')
 tex=tex.replace(r'''H=G^{-1}T^*GT,\quad V=\ker T=\ker H,\quad
\Delta=\operatorname{rank}T,\quad d=q-\Delta,\quad
K_0=K\cap V,\quad t=\dim K_0,\quad p=m-t,\quad \delta_+=\Delta-p.''',r'''\begin{gathered}
H=G^{-1}T^*GT,\quad V=\ker T=\ker H,\quad
\Delta=\operatorname{rank}T,\quad d=q-\Delta,\\
K_0=K\cap V,\quad t=\dim K_0,\quad p=m-t,\quad \delta_+=\Delta-p.
\end{gathered}''')
 tex=tex.replace(r'SOURCE\_USE\_LEDGER.md',r'\path{SOURCE_USE_LEDGER.md}')
 tex=tex.replace('Zhang--Gosea--Antoulas','Zhang, Gosea and Antoulas')
 tex=re.sub(r'\\texttt\{([^{}]+)\}',lambda m:r'\path{'+m[1].replace(r'\_','_')+'}' if len(m[1])>35 else m[0],tex)
 tex=re.sub(r'(?<![a-zA-Z0-9{/_])([a-f0-9]{40,64})(?![a-f0-9])',lambda m:r'\nolinkurl{'+m[1]+'}',tex)
 text+='\n\\clearpage\\part{'+title+'}\n'+tex
text+=r'\end{document}'
out=O/'ORIGINAL_OBSERVATION_RECOVERY_READER.tex'
out.write_text(text,encoding='utf-8')
for _ in range(3):
 r=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error',out.name],cwd=O,capture_output=True,text=True,encoding='utf-8',errors='replace')
 (O/'LATEX_OUTPUT.txt').write_text(r.stdout,encoding='utf-8')
 if r.returncode:raise RuntimeError(r.stdout[-5000:])
pdf=out.with_suffix('.pdf');pages=len(PdfReader(pdf).pages)
qa=Path(tempfile.gettempdir())/'splitzero021-rendered';qa.mkdir(exist_ok=True)
shutil.copyfile(pdf,qa/'reader.pdf')
r=subprocess.run(['pdftoppm','-r','80','-png','reader.pdf','page'],cwd=qa,capture_output=True,text=True)
if r.returncode:raise RuntimeError(r.stderr)
files=[f for f in sorted(qa.glob('page-*.png')) if int(f.stem.split('-')[-1])<=pages]
for st in range(0,len(files),4):
 im=Image.new('RGB',(1400,2000),'#e4e8eb');draw=ImageDraw.Draw(im)
 for j,f in enumerate(files[st:st+4]):
  a=Image.open(f).convert('RGB');a.thumbnail((685,965))
  x=(j%2)*700+(700-a.width)//2;y=(j//2)*1000+25
  im.paste(a,(x,y));draw.text((x,y-18),f.name,fill='black')
 im.save(qa/f'contact-{st//4+1:02d}.png')
log=out.with_suffix('.log').read_text(encoding='utf-8',errors='replace')
report={'pages':pages,'overfull':re.findall(r'Overfull[^\n]*',log),'undefined':re.findall(r'[^\n]*undefined[^\n]*',log),'missing':re.findall(r'[^\n]*Missing character[^\n]*',log),'visual':'pending','pdf':pdf.name,'qa':str(qa)}
(P/'READER_BUILD.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report))
