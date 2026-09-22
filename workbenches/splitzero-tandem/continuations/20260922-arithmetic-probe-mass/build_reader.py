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
\title{Positive arithmetic probes, kernel mass\\and the original short-sector metric}
\author{Split-Zero research programme}
\date{22 September 2026\\SZ-20260922-022}
\begin{document}\maketitle
The original kernel determinant has a positive decomposition by observation
depth. Each newly observed layer contributes an exact quotient determinant.
Eight powers leave a remainder at most $256E_k=O_h(q)$, and 81 specified
positive arithmetic probes recover that depth without numerical derivatives.
The proof retains the original source metric, coordinates, four cutoffs and signs.

The same measured kernel masses now give a tighter upper matrix and a lower
matrix, with a calculated finite determinant interval. A sharp inverse-energy
block estimate improves the mass multiplier from $5/4$ to $9/8$.

Removing complete long chains introduces a further metric issue:
minimizing over their hidden coordinates differs from minimizing over
their terminal coordinates as well. Their exact positive correction has
rank at most 128, and its four-cutoff return can have either sign.
The complete physical current and its complex cross terms are carried
through both minima. Canonical projective sections record the original
inclusion and arithmetic action by the two homogeneous variables.

These are proved original-data receivers and error bounds. The native
$kq$ coefficient and separate current signs still require their actual
period-dependent values. The complete arguments, source maps and exact
verification records follow.
\begingroup\small\tableofcontents\endgroup\clearpage
\section*{A positive determinant at every observation depth}
\addcontentsline{toc}{section}{A positive determinant at every observation depth}
\[
 K_s=\bigcap_{j=0}^s\ker(\Lambda M^j),\quad
 t_s=\dim K_s,\quad
 X_s=-\mathcal R\log\det C_{s,N},\quad
 \mathcal Rf=f_{q-1}+f_q-f_{2q-1}-f_{2q}.
\]
\begin{figure}[H]\centering
\begin{tikzpicture}[>=Latex,
 box/.style={draw,rounded corners,text width=11.7cm,align=center,inner sep=9pt}]
\node[box](a){Full original source $G_N$ and observation $\Lambda$\\
 $V_N[P]=\Lambda P(M)G_N^{-1}P(M)^*\Lambda^*$};
\node[box,below=12mm of a](b){81 positive polynomial probes at depth eight\\
 Exact complex polarization $\longrightarrow$ full selected Gram};
\node[box,below=12mm of b](c){Complete Schur minimum $C_{s,N}$\\
 Each increment is the inverse metric on $K_{s-1}/K_s$};
\node[box,below=12mm of c](d){Increasing four-cutoff determinant\\
 $0=X_0\le X_1\le\cdots\le X_d=\mathcal K_k$};
\draw[->](a)--(b);\draw[->](b)--(c);\draw[->](c)--(d);
\end{tikzpicture}
\caption{All arrows are exact maps in AP4--18. The rank of a layer specifies
its dimension; its displayed original quotient metric supplies the value.
Every nonnegative increment is bounded by $2(t_{s-1}-t_s)E_k$.
The full source estimate is inherited with its original human-source
citations from 021 BD11.}
\end{figure}
\[
 0\le\mathcal K_k-X_8\le256E_k,\qquad
 E_k=2\log C_{\rm rem}+\log(u_k/\ell_k)=O_h(q).
\]
\clearpage
\section*{The terminal metric correction remains in the original source}
\addcontentsline{toc}{section}{The terminal metric correction remains in the original source}
After eliminating only the long hidden coordinates, retain the complete
metric on the short ambient coordinates and long terminal coordinates:
\[
 G^{(1)}=\begin{pmatrix}A&B\\B^*&C\end{pmatrix}>0.
\]
\begin{figure}[H]\centering
\begin{tikzpicture}[>=Latex,box/.style={draw,rounded corners,align=center,text width=5.7cm,inner sep=8pt}]
\node[box](a)at(0,0){Long terminals fixed to zero\\
 $H_S^K=I_S^*AI_S$};
\node[box](b)at(7.2,0){Long terminals also minimized\\
 $H_S^E=I_S^*(A-BC^{-1}B^*)I_S$};
 \draw[->](a.north) to[out=60,in=120] node[above,font=\small]{Exact minimum} (b.north);
\node[draw,align=center,text width=12cm,inner sep=8pt](c)at(3.6,-2.2)
 {$H_S^K-H_S^E=B_KC^{-1}B_K^*\succeq0$\\
 $\operatorname{rank}(H_S^K-H_S^E)\le\ell_s\le128$ at depth eight};
\draw[->](a)--(c);\draw[->](b)--(c);
\end{tikzpicture}
\caption{PEN17--20 prove the exact metric correction. $B_K=I_S^*B$,
and $\ell_s$ counts complete long chains. The two minima retain different
terminal constraints; the formula gives their connecting map. Their
four-cutoff log-determinant difference has absolute value at most
$2\ell_sE_k$, but need not be nonnegative.}
\end{figure}
In the complete nested auxiliary example of PEN9,
$H_S^K=1$ at every cutoff, while $H_S^E$ is $3/4$ at the two low
cutoffs and $1/2$ at the two high cutoffs. Hence
\[
 \mathcal R\log\det H_K-\mathcal R\log\det H_S^E
 =-2\log(3/2)<0.
\]
The source is positive and nested in this example. The negative return
is caused by the specified metric correction, not by a missing positivity
assumption. These are auxiliary values, not a native period evaluation.
\clearpage

\clearpage
\section*{A tighter interval from the same four kernel masses}
\addcontentsline{toc}{section}{A tighter interval from the same four kernel masses}
For the complete auxiliary fixture in KM30, the original kernel angle is
$\Gamma=1/6$, and the exact common-frame mass is
\[
 W(\sigma)=6+\frac{27}{50}\frac{\sigma^2}{(1+2\sigma/5)^2}.
\]
Use $R_3(\sigma)=W(\sigma)/21-4W(\sigma/2)/7+32W(\sigma/4)/21$.
The old upper endpoint is $R_3(\sigma/2)$; the new one subtracts the
proved lower-contraction term. The lower endpoint is unchanged.
\begin{figure}[H]\centering
\begin{tikzpicture}
\begin{axis}[width=13.7cm,height=7.3cm,xlabel={Original mass parameter $\sigma$},
ylabel={$10^4(\text{endpoint}-6)$},xmin=0,xmax=1,ymin=-1.15,ymax=2.05,
grid=major,legend style={at={(0.02,.98)},anchor=north west,font=\small},
tick label style={font=\small}]
\addplot[blue,thick] coordinates {(0.00000000,0.0000000000) (0.01250000,-0.0000000905) (0.02500000,-0.0000014234) (0.03750000,-0.0000070859) (0.05000000,-0.0000220227) (0.06250000,-0.0000528734) (0.07500000,-0.0001078190) (0.08750000,-0.0001964369) (0.10000000,-0.0003295626) (0.11250000,-0.0005191603) (0.12500000,-0.0007781998) (0.13750000,-0.0011205400) (0.15000000,-0.0015608195) (0.16250000,-0.0021143527) (0.17500000,-0.0027970324) (0.18750000,-0.0036252373) (0.20000000,-0.0046157449) (0.21250000,-0.0057856503) (0.22500000,-0.0071522880) (0.23750000,-0.0087331604) (0.25000000,-0.0105458690) (0.26250000,-0.0126080502) (0.27500000,-0.0149373156) (0.28750000,-0.0175511953) (0.30000000,-0.0204670848) (0.31250000,-0.0237021961) (0.32500000,-0.0272735107) (0.33750000,-0.0311977368) (0.35000000,-0.0354912690) (0.36250000,-0.0401701507) (0.37500000,-0.0452500388) (0.38750000,-0.0507461718) (0.40000000,-0.0566733397) (0.41250000,-0.0630458558) (0.42500000,-0.0698775313) (0.43750000,-0.0771816519) (0.45000000,-0.0849709556) (0.46250000,-0.0932576136) (0.47500000,-0.1020532113) (0.48750000,-0.1113687327) (0.50000000,-0.1212145450) (0.51250000,-0.1316003855) (0.52500000,-0.1425353494) (0.53750000,-0.1540278793) (0.55000000,-0.1660857561) (0.56250000,-0.1787160901) (0.57500000,-0.1919253150) (0.58750000,-0.2057191810) (0.60000000,-0.2201027507) (0.61250000,-0.2350803944) (0.62500000,-0.2506557876) (0.63750000,-0.2668319086) (0.65000000,-0.2836110371) (0.66250000,-0.3009947540) (0.67500000,-0.3189839407) (0.68750000,-0.3375787807) (0.70000000,-0.3567787607) (0.71250000,-0.3765826727) (0.72500000,-0.3969886167) (0.73750000,-0.4179940037) (0.75000000,-0.4395955595) (0.76250000,-0.4617893288) (0.77500000,-0.4845706798) (0.78750000,-0.5079343091) (0.80000000,-0.5318742472) (0.81250000,-0.5563838641) (0.82500000,-0.5814558755) (0.83750000,-0.6070823491) (0.85000000,-0.6332547112) (0.86250000,-0.6599637540) (0.87500000,-0.6871996422) (0.88750000,-0.7149519209) (0.90000000,-0.7432095231) (0.91250000,-0.7719607776) (0.92500000,-0.8011934167) (0.93750000,-0.8308945847) (0.95000000,-0.8610508461) (0.96250000,-0.8916481939) (0.97500000,-0.9226720586) (0.98750000,-0.9541073163) (1.00000000,-0.9859382979)};
\addlegendentry{Lower endpoint $L_3$}
\addplot[teal,thick] coordinates {(0.00000000,0.0000000000) (0.01250000,0.0000000004) (0.02500000,0.0000000137) (0.03750000,0.0000001031) (0.05000000,0.0000004295) (0.06250000,0.0000012958) (0.07500000,0.0000031877) (0.08750000,0.0000068114) (0.10000000,0.0000131295) (0.11250000,0.0000233926) (0.12500000,0.0000391699) (0.13750000,0.0000623762) (0.15000000,0.0000952978) (0.16250000,0.0001406149) (0.17500000,0.0002014234) (0.18750000,0.0002812538) (0.20000000,0.0003840883) (0.21250000,0.0005143770) (0.22500000,0.0006770517) (0.23750000,0.0008775383) (0.25000000,0.0011217682) (0.26250000,0.0014161878) (0.27500000,0.0017677670) (0.28750000,0.0021840067) (0.30000000,0.0026729442) (0.31250000,0.0032431593) (0.32500000,0.0039037773) (0.33750000,0.0046644727) (0.35000000,0.0055354712) (0.36250000,0.0065275510) (0.37500000,0.0076520434) (0.38750000,0.0089208325) (0.40000000,0.0103463546) (0.41250000,0.0119415965) (0.42500000,0.0137200931) (0.43750000,0.0156959251) (0.45000000,0.0178837156) (0.46250000,0.0202986265) (0.47500000,0.0229563538) (0.48750000,0.0258731237) (0.50000000,0.0290656870) (0.51250000,0.0325513138) (0.52500000,0.0363477882) (0.53750000,0.0404734015) (0.55000000,0.0449469465) (0.56250000,0.0497877105) (0.57500000,0.0550154685) (0.58750000,0.0606504761) (0.60000000,0.0667134624) (0.61250000,0.0732256220) (0.62500000,0.0802086080) (0.63750000,0.0876845236) (0.65000000,0.0956759144) (0.66250000,0.1042057603) (0.67500000,0.1132974672) (0.68750000,0.1229748589) (0.70000000,0.1332621687) (0.71250000,0.1441840308) (0.72500000,0.1557654718) (0.73750000,0.1680319023) (0.75000000,0.1810091084) (0.76250000,0.1947232429) (0.77500000,0.2092008165) (0.78750000,0.2244686898) (0.80000000,0.2405540638) (0.81250000,0.2574844720) (0.82500000,0.2752877713) (0.83750000,0.2939921337) (0.85000000,0.3136260374) (0.86250000,0.3342182586) (0.87500000,0.3557978628) (0.88750000,0.3783941961) (0.90000000,0.4020368772) (0.91250000,0.4267557889) (0.92500000,0.4525810695) (0.93750000,0.4795431049) (0.95000000,0.5076725200) (0.96250000,0.5370001710) (0.97500000,0.5675571372) (0.98750000,0.5993747127) (1.00000000,0.6324843987)};
\addlegendentry{New upper $U_3^\sharp$}
\addplot[orange,thick] coordinates {(0.00000000,0.0000000000) (0.01250000,0.0000000702) (0.02500000,0.0000011169) (0.03750000,0.0000056218) (0.05000000,0.0000176650) (0.06250000,0.0000428788) (0.07500000,0.0000884018) (0.08750000,0.0001628347) (0.10000000,0.0002761966) (0.11250000,0.0004398827) (0.12500000,0.0006666227) (0.13750000,0.0009704403) (0.15000000,0.0013666140) (0.16250000,0.0018716378) (0.17500000,0.0025031842) (0.18750000,0.0032800665) (0.20000000,0.0042222037) (0.21250000,0.0053505847) (0.22500000,0.0066872340) (0.23750000,0.0082551786) (0.25000000,0.0100784146) (0.26250000,0.0121818757) (0.27500000,0.0145914019) (0.28750000,0.0173337086) (0.30000000,0.0204363573) (0.31250000,0.0239277262) (0.32500000,0.0278369817) (0.33750000,0.0321940510) (0.35000000,0.0370295948) (0.36250000,0.0423749807) (0.37500000,0.0482622576) (0.38750000,0.0547241304) (0.40000000,0.0617939355) (0.41250000,0.0695056162) (0.42500000,0.0778937002) (0.43750000,0.0869932757) (0.45000000,0.0968399697) (0.46250000,0.1074699258) (0.47500000,0.1189197832) (0.48750000,0.1312266555) (0.50000000,0.1444281108) (0.51250000,0.1585621514) (0.52500000,0.1736671951) (0.53750000,0.1897820557) (0.55000000,0.2069459250) (0.56250000,0.2251983545) (0.57500000,0.2445792383) (0.58750000,0.2651287955) (0.60000000,0.2868875537) (0.61250000,0.3098963328) (0.62500000,0.3341962291) (0.63750000,0.3598285997) (0.65000000,0.3868350473) (0.66250000,0.4152574057) (0.67500000,0.4451377252) (0.68750000,0.4765182588) (0.70000000,0.5094414481) (0.71250000,0.5439499104) (0.72500000,0.5800864257) (0.73750000,0.6178939235) (0.75000000,0.6574154710) (0.76250000,0.6986942609) (0.77500000,0.7417735994) (0.78750000,0.7866968952) (0.80000000,0.8335076477) (0.81250000,0.8822494371) (0.82500000,0.9329659126) (0.83750000,0.9857007833) (0.85000000,1.0404978072) (0.86250000,1.0974007819) (0.87500000,1.1564535350) (0.88750000,1.2176999145) (0.90000000,1.2811837805) (0.91250000,1.3469489953) (0.92500000,1.4150394161) (0.93750000,1.4854988854) (0.95000000,1.5583712240) (0.96250000,1.6337002222) (0.97500000,1.7115296327) (0.98750000,1.7919031629) (1.00000000,1.8748644676)};
\addlegendentry{Earlier upper $R_3(\sigma/2)$}
\addplot[black,dashed,domain=0:1]{0};\addlegendentry{Exact value $6$}
\end{axis}
\end{tikzpicture}
\caption{The same four scales $\sigma,\sigma/2,\sigma/4,\sigma/8$ give all
three endpoints. KM20--25 prove their order at every $0<\sigma\le1$.
Plot coordinates are generated from exact rational expressions at 81
rational parameter values, rounded only for display. The vertical factor
$10^4$ magnifies the error; it does not rescale the underlying source metric.
These are the stated auxiliary matrices, not a native xi-packet value.}
\end{figure}
At $\sigma=1$ the strengthened exact interval is
\[
 \frac{1572060375}{262014368}
 <6<
 \frac{284595}{47432}
 <\frac{7968825}{1328096}.
\]
'''
parts=[('Positive probes and increasing depth determinants','PROBE_PROOFS.md'),('Common kernel mass and sharper determinant intervals','MASS_PROOFS.md'),('Canonical pencil maps and the complete physical current','PENCIL_PROOFS.md'),('Sources and receiving calculations','READER_SOURCES.md')]
text=head
for title,name in parts:
 f=P/name
 if not f.exists():
  alt={'PROBE_PROOFS.md':'probe_derivation','MASS_PROOFS.md':'mass_derivation','PENCIL_PROOFS.md':'pencil_derivation'}.get(name)
  if alt:f=P/alt/name
 if not f.exists():raise RuntimeError('Proof not ready: '+name)
 target=O/(f.stem+'.tex')
 r=subprocess.run(['pandoc',str(f),'-f','markdown+tex_math_single_backslash+tex_math_dollars+raw_tex','-t','latex','--wrap=none','-o',str(target)],capture_output=True,text=True)
 if r.returncode:raise RuntimeError(r.stderr)
 tex=target.read_text(encoding='utf-8')
 tex=tex.replace(r''' H=G^{-1}T^*GT,\quad V=\ker T,\quad \nu=\operatorname{rank}T,\quad
 Q=(\Lambda G^{-1}\Lambda^*)^{-1},\quad L=G^{-1}\Lambda^*Q,
 \quad H_K=I_K^*GI_K.''',r'''\begin{gathered}
 H=G^{-1}T^*GT,\quad V=\ker T,\quad \nu=\operatorname{rank}T,\\
 Q=(\Lambda G^{-1}\Lambda^*)^{-1},\quad L=G^{-1}\Lambda^*Q,
 \quad H_K=I_K^*GI_K.
 \end{gathered}''')
 tex=tex.replace(r''' F(z):=zY(z)^{-1}=zI+B_0-C^*(zI+A)^{-1}C,
 \quad W_B=F'(0)=I+C^*A^{-2}C,
 \quad W_K=I+A^{-1}CC^*A^{-1}.''',r'''\begin{gathered}
 F(z):=zY(z)^{-1}=zI+B_0-C^*(zI+A)^{-1}C,\\
 W_B=F'(0)=I+C^*A^{-2}C,\qquad
 W_K=I+A^{-1}CC^*A^{-1}.
 \end{gathered}''')
 tex=tex.replace(r''' \log\det L_r\le-\log\det\Gamma\le\log\det U_r^\sharp,\qquad
 \log\det U_r^\sharp-\log\det L_r
 =\log\det(I+\beta L_r^{-1/2}DL_r^{-1/2}).''',r'''\begin{gathered}
 \log\det L_r\le-\log\det\Gamma\le\log\det U_r^\sharp,\\
 \log\det U_r^\sharp-\log\det L_r
 =\log\det(I+\beta L_r^{-1/2}DL_r^{-1/2}).
 \end{gathered}''')
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
out=O/'ARITHMETIC_PROBE_MASS_READER.tex'
out.write_text(text,encoding='utf-8')
for _ in range(3):
 r=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error',out.name],cwd=O,capture_output=True,text=True,encoding='utf-8',errors='replace')
 (O/'LATEX_OUTPUT.txt').write_text(r.stdout,encoding='utf-8')
 if r.returncode:raise RuntimeError(r.stdout[-5000:])
pdf=out.with_suffix('.pdf');pages=len(PdfReader(pdf).pages)
qa=Path(tempfile.gettempdir())/'splitzero022-rendered';qa.mkdir(exist_ok=True)
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

# Figure coordinates above are the exact-rational samples W,R,L,U defined here.
from fractions import Fraction as F
def mass_figure_values(i):
 x=F(i,80)
 W=lambda s:F(6)+F(27,50)*s*s/(1+F(2,5)*s)**2
 R=lambda s:W(s)/21-F(4,7)*W(s/2)+F(32,21)*W(s/4)
 return x,(R(x/2)-F(212,1593)*R(x))/(1-F(212,1593)),(R(x/2)-R(x)/16)/(1-F(1,16)),R(x/2)
