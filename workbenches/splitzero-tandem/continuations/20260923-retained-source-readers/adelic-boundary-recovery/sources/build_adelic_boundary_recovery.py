from pathlib import Path
import hashlib
import json
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

R = Path(__file__).resolve().parent
OUT = R / 'adelic_boundary_recovery_delivery'
OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family': 'DejaVu Sans', 'mathtext.fontset': 'dejavusans'})

fig = plt.figure(figsize=(12, 8.6), facecolor='white')
ax = fig.add_axes([0, 0, 1, 1]); ax.set_axis_off()
def label(x, y, s, size=15, color='#17232e', **kw):
    ax.text(x,y,s,fontsize=size,color=color,transform=ax.transAxes,**kw)
def arrow(a,b,color='#28658c'):
    ax.annotate('',xy=b,xytext=a,xycoords='axes fraction',
                arrowprops={'arrowstyle':'->','lw':2,'color':color})
label(.055,.95,'The source is recovered by retaining its prime boundary',18,weight='bold')
label(.055,.897,'Exact algebraic maps; arbitrary nontrivial bounded distributive lattice L.',11)
label(.08,.79,r'$Q_0=M_0/IM_0$',22)
label(.60,.79,r'$V^K\oplus\mathcal{B}_{\mathrm{pr}}$',22)
arrow((.34,.80),(.57,.80)); label(.385,.835,r'$\Omega=(\rho,\beta)$',14)
label(.38,.745,'bijection',11)
arrow((.70,.72),(.70,.58)); label(.72,.65,'first component',11)
label(.645,.52,r'$V^K$',22)
arrow((.20,.72),(.60,.55)); label(.34,.605,r'$\rho=\mathcal{P}\Phi$',15)
label(.065,.45,r'$\ker\rho=\mathcal{B}_{\mathrm{pr}}=\bigoplus_{p\ \mathrm{prime}}\mathbb{C}^{2}$',19)
label(.065,.36,r'$\beta([\sum_a t_a\otimes h_a])=\sum_p\ell_p\otimes\sum_a v_p(a)\left(h_a(0),\int_{\mathbb{R}}h_a(x)\,dx\right)$',16)
label(.065,.265,r'$\Omega^{-1}(F,b)=[t_1\otimes\mathcal{P}^{-1}F]+j(b)$',18)
label(.065,.183,r'$\mathcal{P}h(y)=2\sum_{n\geq1}h(ny),\qquad\mathcal{M}(\mathcal{P}h)(s)=2\zeta(s)\mathcal{M}_+h(s)\quad(\Re s>1)$',16)
label(.065,.103,r'$G_L(\rho)(c,1_L)=e\ne\tau\quad(0\ne c\in\ker\rho)$',17)
label(.065,.043,'Proof: ABR1-19, ABR29-30. Sources: Connes, math/9811068v1, III(6)-(19);\nConnes, Consani and Marcolli, math/0703392v1, actual restriction image. One common label per object.',9)
for ext in ('png','svg'):
    fig.savefig(OUT / ('EXACT_SOURCE_RECOVERY.'+ext),dpi=170)
plt.close(fig)

fig = plt.figure(figsize=(12,7.5),facecolor='white')
ax=fig.add_axes([0,0,1,1]);ax.set_axis_off()
label(.06,.94,'A finite exact test of every mixed boundary coefficient',18,weight='bold')
label(.06,.86,r'$S(y)=\sum_{k\geq1}v_k g(ky/B)+\sum_{k=1}^{K}d_k g(ky/B)$',19)
label(.06,.78,'v is Q-periodic; d retains every omitted initial frequency; B retains the original scale.',11)
label(.06,.675,r'$M=K+\lfloor(Q-1)/2\rfloor$',20)
label(.06,.58,r'$C_1=\cdots=C_M=0\quad\Longleftrightarrow\quad C_m=0\ (m\geq1)$',20)
label(.06,.49,r'$\Longleftrightarrow\quad d_k=0\ (1\leq k\leq K),\quad v_r=v_{Q-r}\ (1\leq r<Q)$',18)
label(.06,.37,'The two endpoint values survive the complete boundary cancellation:',12,weight='bold')
label(.06,.28,r'$\int_0^\infty S(y)\,\frac{dy}{y}=\frac{v_0}{4},\qquad\int_0^\infty S(y)\,dy=\frac{B}{4Q}\sum_{r=1}^{Q}v_r$',21)
label(.06,.17,r'$\widetilde v_k+\widetilde d_k=\widetilde w_k+(0,\sigma_k)$',20)
label(.06,.115,'Separate input labels retain the omitted-initial support even when its amplitude cancels.',11)
label(.06,.035,'Proof: RMK1-15, RMK17-26, RMK30-32; original full Gaussian polynomial g is defined in RMK1.\nThis is a complete finite-rational boundary classification, not an all-tests positivity theorem.',9)
for ext in ('png','svg'):
    fig.savefig(OUT/('FINITE_MIXED_BOUNDARY.'+ext),dpi=170)
plt.close(fig)

names=['ORIGINAL_ZETA_THETA_CORRECTION.tex',
       'CC_ADELIC_COINVARIANT_BRIDGE_INDEPENDENT.tex',
       'RATIONAL_MIXED_BOUNDARY_KERNEL.tex']
preamble=r'''\documentclass[11pt]{article}
\usepackage[a4paper,margin=23mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{amsmath,amssymb,amsthm,mathtools,mathrsfs,graphicx,microtype}
\usepackage[hidelinks,hypertexnames=false]{hyperref}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\title{Original zeta, faithful source recovery, and mixed boundaries}
\author{Programme derivations with the cited human-source provenance}
\date{23 September 2026}
\begin{document}\maketitle
The preceding theta-origin explanation required correction: lifting
the coefficients of an imported classical theta kernel does not derive
that kernel from the whole absolute base. Chapter 1 gives the original
zeta and shifted-Hurwitz comparison, retaining its multiplier, both
endpoints, embedded local modules, product, and support labels.

Chapter 2 computes the complete algebraic kernel of actual radial
adelic periodization. Its prime-boundary coordinates and explicit
inverse give a faithful joint receiver. This receiver is a map on the
specified original source; it is not an asserted identification with
the whole absolute geometry or its spectral quotient. The higher
mixed-prime connecting classes and the two real-idele endpoint
characters are proved with their original signs and factors.

Chapter 3 gives the complete finite rational mixed-boundary criterion,
including a sharp number of scalar equations for its obstruction
space, an actual adelic antecedent, both endpoint values, compact-unit
characters and the correction for separately labelled initial terms.
No statement of positivity for every Weil test, or proof or disproof
of RH, is made. The complete programme predecessor proof sources
accompany these new derivations. Human primary sources are linked
at their original hosts.
\tableofcontents\clearpage
\begin{figure}[p]\centering
\includegraphics[width=\textwidth]{EXACT_SOURCE_RECOVERY.png}
\caption{The joint map retains all algebraic source information.
Periodization alone loses exactly the displayed prime boundary.
The lifted zero image retains its support label.}\end{figure}\clearpage
\begin{figure}[p]\centering
\includegraphics[width=\textwidth]{FINITE_MIXED_BOUNDARY.png}
\caption{A finite test determines the entire boundary in the stated
rational family. Its zero-boundary functions retain two distinct
endpoint values and their original support contributions.}\end{figure}
\clearpage
'''
parts=[preamble];manifest={}
for name in names:
    p=R/'independent'/name; data=p.read_bytes()
    manifest[name]=hashlib.sha256(data).hexdigest()
    src=data.decode('utf-8')
    # Display-layout changes only; retain all mathematical factors and terms.
    if name == 'CC_ADELIC_COINVARIANT_BRIDGE_INDEPENDENT.tex':
        src=src.replace('$H_t(Z)=\\int_0^\\infty e^{tu^2}\\Phi(u)\\cos(Zu)\\,du$.',
                        '\\[H_t(Z)=\\int_0^\\infty e^{tu^2}\\Phi(u)\\cos(Zu)\\,du.\\]')
    if name == 'RATIONAL_MIXED_BOUNDARY_KERNEL.tex':
        src=src.replace('$xe^{a x}/(e^x-1)=\\sum_{n\\geq0}B_n(a)x^n/n!$.',
                        '\\[xe^{a x}/(e^x-1)=\\sum_{n\\geq0}B_n(a)x^n/n!.\\]')
        a=src.index(r'\begin{equation}\tag{RMK1}')
        b=src.index(r'\end{equation}',a)+len(r'\end{equation}')
        src=src[:a]+'{\\small\n'+src[a:b]+'\n}'+src[b:]
        a=src.index(r'\begin{equation}\tag{RMK2}')
        b=src.index(r'\end{equation}',a)
        block=src[a:b].replace(r'\tag{RMK2}',r'\tag{RMK2}\begin{gathered}')
        block=block.replace(r'B=D b_0,\quad',r'B=D b_0,\\')
        src=src[:a]+block+'\\end{gathered}\n'+src[b:]
    src=re.sub(r'\\texttt\{([0-9a-f]{64})\}',
               lambda m:r'\texttt{'+r'\allowbreak{}'.join(m[1][i:i+16] for i in range(0,64,16))+'}',src)
    parts.extend(['\n% Complete source: '+name+'\n',src,'\n\\clearpage\n'])
parts.append('\n\\end{document}\n')
(OUT/'ADELIC_BOUNDARY_RECOVERY_READER.tex').write_text(''.join(parts),encoding='utf-8')
(OUT/'BUILD_SOURCE_HASHES.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'directory':str(OUT),'source_hashes':manifest},indent=2))
