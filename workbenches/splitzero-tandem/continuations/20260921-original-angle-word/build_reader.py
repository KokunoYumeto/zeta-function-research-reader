from pathlib import Path
import subprocess,re,json,shutil,tempfile,math
from PIL import Image,ImageDraw
from pypdf import PdfReader
P=Path(__file__).parent;O=P/'reader';O.mkdir(exist_ok=True)
head=r'''\documentclass[11pt]{article}
\usepackage[a4paper,margin=24mm]{geometry}
\usepackage{amsmath,amssymb,mathtools,amsthm,mathrsfs,tikz,pgfplots,longtable,booktabs,array,calc,enumitem}
\usepackage[hidelinks,hypertexnames=false]{hyperref}\usepackage{xurl}
\usepackage{fontspec}\setmainfont{DejaVu Serif}
\usetikzlibrary{arrows.meta,positioning,calc}\pgfplotsset{compat=1.18}
\setlength{\emergencystretch}{4em}\providecommand{\tightlist}{}\newcounter{none}
\setcounter{secnumdepth}{0}\allowdisplaybreaks
\title{The original projection-angle spectrum\\and arithmetic word}
\author{Split-Zero research programme}
\date{21 September 2026\\SZ-20260921-019}
\begin{document}\maketitle
Every original projection direction now has an explicit inverse-growth
bound, with the entire lower-root constraint retained. The complete
long arithmetic word has a controlled spectrum, rectangle resultant,
and observed heat return. The original-root and weighted-source
innovation formulas are joined by an exact vector identity, including
the physical complex phase and source mass.

The centered projection-angle spectrum has a further direction law:
over the entire cutoff window its total downward movement is
$O_{h,A}(\log(q+2)/k)$, tending to zero. The same result holds for
both original Gamma source orders. This sharpens a bounded path
variation to its endpoint increase. Its proof follows the actual
positive source increments, with no discarded low directions.

The native determinant coefficient at order $kq$ remains the
period-dependent endpoint statistic given in AD12--14 and RX17--19.
It has not been assigned a value. The negative intermediate observed
heat return is retained at its exact scope; it does not assign the
separate complex-current signs. Every finite guard, inherited source
status and auxiliary example is identified below.
\begingroup\small\tableofcontents\endgroup\clearpage
\section*{The full projection and its two increments}
\addcontentsline{toc}{section}{The full projection and its two increments}
In the original orthonormal Gamma frame, $E_N$ evaluates every lower
root and $W_N$ contains every original invariant functional. Adding
one degree gives the exact diagram
\[
\begin{array}{ccc}
\ker E_N&\lhook\joinrel\longrightarrow&\ker[E_N,e_N]
=\ker E_N\oplus\mathbb Ct_N\\
\downarrow W_N&&\downarrow[W_N,w_N]\\
\mathbb C^r&=&\mathbb C^r.
\end{array}
\]
The new unit vector and its actual observed image are
\[
t_N=\frac1{\sqrt{\kappa_N}}
\binom{-E_N^*(E_NE_N^*)^{-1}e_N}{1},\qquad
a_N=[W_N,w_N]t_N,
\]
\[
C_{N+1}=C_N+a_Na_N^*,\qquad
B_{N+1}=B_N+w_Nw_N^*.
\]
The first increment retains the full lower-root projection. The second
uses the unrestricted source. RX7--8 proves the exact relation of $a_N$
to the weighted monic source innovation. AD4 then separates their two
effects on every ordered squared angle:
\[
\begin{aligned}
\sum_j(\log s_{j,N}-\log s_{j,N+1})_+
&\le\log\frac{\det B_{N+1}}{\det B_N},\\
\sum_j(\log s_{j,N+1}-\log s_{j,N})_+
&\le\log\frac{\det C_{N+1}}{\det C_N}.
\end{aligned}
\]
The complete first allowance telescopes to $O(q\log q)$, while the
arithmetic determinant scale is $rq\asymp kq$. This is the mechanism
behind the direction law. It bounds all downward steps together.

\begin{figure}[ht]\centering
\begin{tikzpicture}\begin{axis}[width=.92\textwidth,height=6cm,
xlabel={Auxiliary Gamma degree $D$},ylabel={$\log s_{j,D}$},
legend style={at={(.5,-.25)},anchor=north,legend columns=2}]
\addplot[teal!80!black,thick,mark=*]coordinates{ANGLE_ONE};
\addlegendentry{Larger squared angle}
\addplot[orange!80!black,thick,mark=square*]coordinates{ANGLE_TWO};
\addlegendentry{Smaller squared angle}
\end{axis}\end{tikzpicture}
\caption{A finite check with the complete lower-root set $\{i,-i\}$
and observation evaluations at $3+2i$ and $-2+i$, in the original
Gamma polynomial convention. Every plotted value comes from the full
projector. Individual angles can move in both directions. The
downward allowance is their complete unprojected Gram increase
(AD4--8). This is an auxiliary example, not native period data.}
\end{figure}\clearpage
\section*{The rectangle profile of the entire word}
\addcontentsline{toc}{section}{The rectangle profile of the entire word}
The literal pivot-interior polynomial $D$ has $q'=(k-7)^2$ roots.
The word $D(M)$ vanishes on that entire primary subspace and has
$\Delta=16k-48$ positive singular directions. Their values retain
the complete cross-resultant between the interior and boundary roots.
FW11--22 evaluates it through the original rectangle potential,
with all lattice, displacement and phase corrections.

\begin{figure}[ht]\centering
\begin{tikzpicture}\begin{axis}[width=.92\textwidth,height=6cm,
xlabel={Edge coordinate $t\in[0,1]$},ylabel={Rectangle potential},
legend style={at={(.5,-.25)},anchor=north,legend columns=1}]
\addplot[teal!80!black,thick]coordinates{HORIZONTAL};
\addlegendentry{$U(rt,1)$: horizontal edge}
\addplot[orange!80!black,thick]coordinates{VERTICAL};
\addlegendentry{$U(r,t)$: vertical edge}
\end{axis}\end{tikzpicture}
\caption{The exact FW rectangle formulas sampled at $r=\gamma/\delta=12$.
Here $U(u,v)=(4r)^{-1}\int_{-r}^r\int_{-1}^1
\log((u-s)^2+(v-t)^2)\,dt\,ds$. The two edge profiles meet at the
corner. FW23--33 proves their pushforward relation to the full
scaled logarithmic spectrum; this parameter illustration makes
no assertion about a native zeta quartet.}
\end{figure}
The full original observed action also retains the collision kernel.
Its intermediate heat return is
\[
\mathcal R\operatorname{Tr}Y_N=-2\Delta+
\operatorname{Tr}\Gamma_{q-1}+\operatorname{Tr}\Gamma_q+o(1),
\qquad0<\Gamma_N\preceq I_{8k-16}.
\]
FW39--49 proves this through the original quotient map, including
the finite $d<m$ correction and the later relative determinant.
The complete human and programme citations occur at the point of
use in each proof and in the accompanying source ledger.
\clearpage
'''
data=(json.loads((P/'ANGLE_DIRECTION_CHECKS.json').read_text()) if (P/'ANGLE_DIRECTION_CHECKS.json').exists() else json.loads((P/'CHECKS.json').read_text())['direction'])['spectra']
for i,key in enumerate(['ANGLE_ONE','ANGLE_TWO']):head=head.replace(key,' '.join('('+str(z['degree'])+','+z['log_angles'][i]+')'for z in data))
def F(a,b):
    if a==0 or b==0:return 0.0
    return a*b*math.log(a*a+b*b)-3*a*b+a*a*math.atan(b/a)+b*b*math.atan(a/b)
def U(u,v,r=12):return (F(r-u,1-v)+F(r+u,1-v)+F(r-u,1+v)+F(r+u,1+v))/(4*r)
head=head.replace('HORIZONTAL',' '.join(f'({j/100},{U(12*j/100,1):.15g})'for j in range(101)))
head=head.replace('VERTICAL',' '.join(f'({j/100},{U(12,j/100):.15g})'for j in range(101)))
parts=[('Every original projection-angle direction',P/'angle_derivation/ANGLE_PROOFS.md'),('The complete long arithmetic word',P/'word_derivation/WORD_PROOFS.md'),('Original-root innovations and selected volumes',P/'ROOT_INNOVATION_AND_EXTRACTION_PROOFS.md'),('Direction of the complete angle spectrum',P/'ORIGINAL_ANGLE_DIRECTION_PROOFS.md')]
text=head
for title,f in parts:
    if not f.is_file():f=P/f.name
    target=O/(f.stem+'.tex')
    r=subprocess.run(['pandoc',str(f),'-f','markdown+tex_math_single_backslash+tex_math_dollars+raw_tex','-t','latex','--wrap=none','-o',str(target)],capture_output=True,text=True)
    if r.returncode:raise RuntimeError(r.stderr)
    tex=target.read_text(encoding='utf-8')
    tex=re.sub(r'\\texttt\{([a-fA-F0-9]{40}|[a-fA-F0-9]{64})\}',lambda m:r'\nolinkurl{'+m[1]+'}',tex)
    tex=tex.replace(r'k\equiv1\pmod4,\quad k\ge17,\quad q=(k+1)^2,\quad',r'\begin{gathered}k\equiv1\pmod4,\quad k\ge17,\quad q=(k+1)^2,\\')
    tex=tex.replace(r'\quad R_h=\sqrt{\delta^2+\gamma^2}.',r'\quad R_h=\sqrt{\delta^2+\gamma^2}.\end{gathered}')
    def tagged(m):
        body,tag=m[1],m[2]
        if tag=='AS5':body=body.replace(r'C_N=W_NP_NW_N^*,',r'\begin{gathered}C_N=W_NP_NW_N^*,').replace(r'C_N^\circ=',r'\\ C_N^\circ=')+r'\end{gathered}'
        if tag in ['AS40','AS47']:
            body=r'\begin{gathered}'+body.replace(r'\le',r'\\\le').replace('\n=', '\n'+r'\\=')+r'\end{gathered}'
        return r'\['+body+r'\tag{'+tag+r'}\]'
    tex=re.sub(r'\\\[((?:(?!\\\]).)*?)\\tag\{(AS5|AS40|AS47)\}\s*\\\]',tagged,tex,flags=re.S)
    tex=tex.replace(r"d_{\mathrm{cond}}(S')=\mathcal T_A\chi(S')/\chi'(S'),\quad",r"\begin{gathered}d_{\mathrm{cond}}(S')=\mathcal T_A\chi(S')/\chi'(S'),\\")
    tex=tex.replace(r"\quad p_A(y)=d_{\mathrm{cond}}(c'+iy)/(a_Ai^g).",r"\\ p_A(y)=d_{\mathrm{cond}}(c'+iy)/(a_Ai^g).\end{gathered}")
    tex=tex.replace(r'b_-=\ell_k/A,\quad b_+=u_kB_0,\quad',r'\begin{gathered}b_-=\ell_k/A,\quad b_+=u_kB_0,\\')
    tex=tex.replace(r'C_V=\max\{1,\Delta\max(1,R)^{\Delta-1}\},\quad',r'C_V=\max\{1,\Delta\max(1,R)^{\Delta-1}\},\\')
    tex=tex.replace(r'C_{V^{-1}}=\max\left\{1,\sqrt\Delta\left(\frac{1+R}{2\delta}\right)^{\Delta-1}\right\}.',r'C_{V^{-1}}=\max\left\{1,\sqrt\Delta\left(\frac{1+R}{2\delta}\right)^{\Delta-1}\right\}.\end{gathered}')
    tex=tex.replace(r"\(a_N=i^{-(N-v+1)}f_{N-v-q'+1}/\sqrt{\nu_{N-v-q'+1}}\)",r"\[a_N=i^{-(N-v+1)}f_{N-v-q'+1}/\sqrt{\nu_{N-v-q'+1}}\]")
    text+='\n\\clearpage\\part{'+title+'}\n'+tex
text+=r'\end{document}'
out=O/'ORIGINAL_ANGLE_WORD_READER.tex';out.write_text(text,encoding='utf-8')
for j in range(3):
    r=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error',out.name],cwd=O,capture_output=True,text=True,encoding='utf-8',errors='replace')
    (O/'LATEX_OUTPUT.txt').write_text(r.stdout,encoding='utf-8')
    if r.returncode:raise RuntimeError(r.stdout[-5000:])
pdf=out.with_suffix('.pdf');count=len(PdfReader(pdf).pages)
qa=Path(tempfile.gettempdir())/'splitzero019-rendered';qa.mkdir(exist_ok=True);shutil.copyfile(pdf,qa/'reader.pdf')
r=subprocess.run(['pdftoppm','-r','80','-png','reader.pdf','page'],cwd=qa,capture_output=True,text=True)
if r.returncode:raise RuntimeError(r.stderr)
pages=[f for f in sorted(qa.glob('page-*.png'))if int(f.stem.split('-')[-1])<=count]
for st in range(0,len(pages),4):
    im=Image.new('RGB',(1400,2000),'#e4e8eb');draw=ImageDraw.Draw(im)
    for j,f in enumerate(pages[st:st+4]):
        a=Image.open(f).convert('RGB');a.thumbnail((685,965));x=(j%2)*700+(700-a.width)//2;y=(j//2)*1000+25
        im.paste(a,(x,y));draw.text((x,y-18),f.name,fill='black')
    im.save(qa/f'contact-{st//4+1:02d}.png')
log=out.with_suffix('.log').read_text(encoding='utf-8',errors='replace')
report=dict(pages=count,overfull=re.findall(r'Overfull[^\n]*',log),undefined=re.findall(r'[^\n]*undefined[^\n]*',log),missing=re.findall(r'[^\n]*Missing character[^\n]*',log),visual='pending',pdf=str(pdf),qa=str(qa))
(P/'READER_BUILD.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps(report))
