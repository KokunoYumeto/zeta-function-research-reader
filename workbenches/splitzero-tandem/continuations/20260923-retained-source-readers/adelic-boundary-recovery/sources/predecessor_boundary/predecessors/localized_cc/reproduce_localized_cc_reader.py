from pathlib import Path
import hashlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

R=Path(__file__).resolve().parent
out=R/'localized_cc_delivery'
out.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans'})
fig,ax=plt.subplots(figsize=(12,8.8),facecolor='white')
ax.set(xlim=(0,12),ylim=(0,9));ax.axis('off')
def box(x,y,w,h,text,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.12',linewidth=1.3,edgecolor=color,facecolor='#f9fafb'))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=13,linespacing=1.7)
def arrow(a,b,text=None,offset=(0,0)):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=15,linewidth=1.5,color='#303b4b'))
    if text:ax.text((a[0]+b[0])/2+offset[0],(a[1]+b[1])/2+offset[1],text,ha='center',va='center',fontsize=11)
ax.text(.1,8.65,'The actual localized support retains the difference',fontsize=18,weight='bold')
ax.text(.1,8.12,r'$Y=\operatorname{Spec}G_L(\mathbb{Z}),\quad S=\operatorname{Spec}_{\mathrm{lat}}L,\quad J\in S$',fontsize=15)
box(.25,6.0,4.5,1.2,'Pullback coefficient at a support prime\n'+r'$G_L(W)$','#285d7d')
box(7.1,6.0,4.5,1.2,'Actual localized coefficient\n'+r'$L_J$','#804520')
arrow((4.95,6.6),(6.9,6.6),r'$(w,\lambda)\mapsto[\lambda]_J$',(0,.48))
ax.text(6,5.65,r'Invert $e$: amplitudes map to labels. Localize labels by $L\to L_J$.',ha='center',fontsize=12)
ax.text(.3,4.96,r'Independent degrees $0,1,2$; test input $(0,1,0)\in L_J^3$',fontsize=14,weight='bold')
box(.25,3.2,4.5,1.05,r'$P_J(0,1,0)=(0,1,0)$'+'\nSame-parity support propagation','#285d7d')
box(7.1,3.2,4.5,1.05,r'$Q_J(0,1,0)=(1,1,0)$'+'\nAll lower degrees receive support','#804520')
ax.text(6,2.77,r'$0\ne1$ in every proper prime localization $L_J$: $P_J\ne Q_J$.',ha='center',fontsize=13)
arrow((2.5,3.0),(4.25,1.92))
arrow((9.35,3.0),(7.75,1.92))
box(3.1,.72,5.8,1.2,'Additive group reflection of the full sheaf\n'+r'$\mathcal{M}_k\longrightarrow i_*\mathcal{H}_k$'+'\n'+r'$P\longmapsto I,\quad Q\longmapsto I$', '#3c6550')
ax.text(6,.17,'The arrows below denote group reflection; its support stalk is zero.',ha='center',fontsize=11)
fig.text(.04,.022,'Proofs: ULC4-10; CLS3-8. Exact algebraic diagram, not a numerical sample.\nAdelic source: Alain Connes and Caterina Consani, arXiv:2501.06560v1, Section 4.',fontsize=10,color='#3c4654')
fig.subplots_adjust(left=.025,right=.985,bottom=.08,top=.985)
fig.savefig(out/'LOCALIZED_SUPPORT_MAP.png',dpi=180)
fig.savefig(out/'LOCALIZED_SUPPORT_MAP.svg')
plt.close(fig)

preamble=r'''\documentclass[11pt,a4paper]{article}
\usepackage[margin=24mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{amsmath,amssymb,amsthm,amscd,mathtools,mathrsfs,array,longtable,booktabs,graphicx,microtype,xurl}
\usepackage[hidelinks,hypertexnames=false]{hyperref}
\allowdisplaybreaks
\emergencystretch=3em
\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}\newtheorem{definition}[theorem]{Definition}
\newtheorem{remark}[theorem]{Remark}
\providecommand{\C}{\mathbb C}\providecommand{\R}{\mathbb R}
\providecommand{\Q}{\mathbb Q}\providecommand{\Z}{\mathbb Z}
\providecommand{\N}{\mathbb N}\providecommand{\Spec}{\operatorname{Spec}}
\providecommand{\SpecLat}{\operatorname{Spec}_{\mathrm{lat}}}
\title{Adelic Coefficients on the Full Split-Support Base\\
Prime Transport, Localized Supports, and Synchronization}
\author{Programme derivations with the original human sources cited throughout}
\date{23 September 2026}
\begin{document}\maketitle
This reader constructs the entire divisor-indexed family of the original
Connes--Consani adelic coefficient sheaves and its exact extension to an
arbitrary bounded distributive support lattice. It retains the rational
prime maps, original Haar measures, mixed-prime cohomology, actual
support localizations, and both original-zeta endpoint contributions.
The incoming finite heat/translation construction is applied to those
same sheaves. The different projectors remain visible at support primes
even though their additive group reflections agree. No identification
of the resulting positive quotient metric with Weil's form is assumed.
The complete arguments are CDV1--25, ULC1--18, and CLS1--13.
The appendices retain the support-localization and Mellin proofs used
by them. The source archive also retains the complete predecessor
sources and the unchanged original author archives.
\tableofcontents\clearpage
\begin{figure}[p]\centering
\includegraphics[width=\textwidth]{LOCALIZED_SUPPORT_MAP.png}
\caption{The exact source and support comparisons. The vector
$(0,1,0)$ is a lattice-valued coefficient vector, not a vector of
complex amplitudes. The bottom arrows refer to the amplitude reflection
of the sheaf; at a support point its target is zero. ULC4--10 and
CLS3--8 prove all displayed maps.}
\end{figure}\clearpage
'''
parts=[preamble]
for name in ['CC_DIVISOR_COEFFICIENT_FAMILY.tex','ARBITRARY_SUPPORT_CC_COEFFICIENTS.tex','CC_LOCALIZED_SHIFT_SYNCHRONIZATION.tex']:
    parts.extend(['\n% Complete proof source: '+name+'\n',(R/'independent'/name).read_text(encoding='utf-8'),'\n\\clearpage\n'])
parts.append('\n\\appendix\n')
fsc=(R/'independent/FULL_SUPPORT_SHEAF_COMPARISON.tex').read_text(encoding='utf-8')
fsc=fsc.split('\\subsection{Tropical coefficients, labels, and Frobenius zero}',1)[0]
parts.extend(['\n% Complete FSC1-9 subsection source; full FSC retained in archive.\n',fsc,'\n\\clearpage\n'])
ztc=(R/'independent/ORIGINAL_ZETA_THETA_CORRECTION.tex').read_text(encoding='utf-8')
ztc=ztc.split('\\subsection{A direct theta sum for the original arithmetic family}',1)[1]
ztc=ztc.split('For the original cosine heat kernel, retain',1)[0]
parts.extend([r'\section{Original arithmetic theta sums and both Mellin endpoints}'+'\n',
              r'''The original functions here are $F_t(s)=\sum_{n\ge0}(n+1+t)^{-s}$ for real $t>-1$ and $\Re s>1$, and $F_0=\zeta$. This is the complete ZTC2--10 calculation from the retained original-zeta reconstruction. The Gaussian Poisson identity used at ZTC9 is proved directly below. Its classical kernel provenance is Brad Rodgers and Terence Tao, \href{https://arxiv.org/abs/1801.05914v5}{arXiv:1801.05914v5}, source equations \texttt{phidef}, \texttt{htdef}, \texttt{hoz}, \texttt{sas}. No heat deformation of zeta is needed for this Mellin comparison.
''',ztc])
parts.append(r'''
\paragraph{Proof of the Gaussian Poisson identity used above.}
For $x>0$, periodize $e^{-\pi x y^2}$. All derivatives converge
uniformly on a unit interval, by Gaussian bounds on the summands.
The $m$th Fourier coefficient is its unfolded integral over $\mathbb R$,
$x^{-1/2}e^{-\pi m^2/x}$. To verify that transform directly at scale
one, differentiation under the integral and integration by parts give
$\widehat f'(\eta)=-2\pi\eta\widehat f(\eta)$; the Gaussian integral
gives $\widehat f(0)=1$. Scaling gives the coefficient just stated.
Their absolute convergence permits evaluation of the Fourier series
at zero, giving $1+2K_0(x)=x^{-1/2}(1+2K_0(1/x))$.
Rearranging with all terms retained gives ZTC9.
\end{document}
''')
(out/'CC_LOCALIZED_SUPPORT_READER.tex').write_text(''.join(parts),encoding='utf-8')

