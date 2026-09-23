from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
R=Path(__file__).resolve().parent
out=R/'original_zeta_correction'
out.mkdir(exist_ok=True)
# This single TeX source retains the full supporting derivations, not only excerpts.
preamble = r'''\documentclass[11pt]{article}
\usepackage[a4paper,margin=25mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{amsmath,amssymb,amsthm,mathtools,mathrsfs,longtable,array,booktabs}
\usepackage{microtype}
\usepackage[hidelinks,hypertexnames=false]{hyperref}
\newtheorem{theorem}{Theorem}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{remark}[theorem]{Remark}
\providecommand{\R}{\mathbb R}
\providecommand{\C}{\mathbb C}
\providecommand{\Z}{\mathbb Z}
\providecommand{\N}{\mathbb N}
\providecommand{\dd}{\,d}
\title{Original zeta, shifted theta sums, and retained support}
\author{Programme derivations from the cited human sources}
\date{23 September 2026}
\begin{document}
\maketitle
The original functions, their complete transform multipliers, both
endpoint terms, boundary components, exceptional local lattices and
support labels are retained. The scalar kernel is recovered by an
explicit inverse Mellin integral. Neither this scalar inverse nor a
coefficient lift is asserted to reconstruct the entire arithmetic base.
\tableofcontents
\clearpage
'''
names = ['ORIGINAL_ZETA_THETA_CORRECTION.tex',
         'COMPLETION_FAITHFULNESS_DERIVATION.tex',
         'THETA_HEAT_FULL_SUPPORT.tex',
         'HURWITZ_THETA_FLOW_BRIDGE.tex',
         'HURWITZ_ALIGNMENT_FULL_MAP.tex']
parts = [preamble]
for j, name in enumerate(names):
    if j == 2:
        parts.append('\n\\appendix\n')
    parts.append('\n% Complete source: '+name+'\n')
    parts.append((R/'independent'/name).read_text(encoding='utf-8'))
    parts.append('\n\\clearpage\n')
parts.append('\\end{document}\n')
(out/'ORIGINAL_ZETA_RECONSTRUCTION.tex').write_text(''.join(parts), encoding='utf-8')

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,
                     'mathtext.fontset':'dejavusans'})
fig = plt.figure(figsize=(12,8.5),facecolor='white')
fig.text(.055,.952,'Original arithmetic functions: exact recovery and different deformations',
         fontsize=16,weight='bold')
fig.text(.055,.896,r'$A(s)=\frac{s(s-1)}{2}\pi^{-s/2}\Gamma(s/2),\quad s(z)=\frac{1}{2}+\frac{iz}{2},\quad (Uf)(z)=A(s(z))f(s(z))/8$',fontsize=13)
fig.text(.055,.82,r'$(F_t,\,D_t=\zeta-F_t)\quad\longleftrightarrow\quad(H_0,\,J_t=UD_t)$',fontsize=18)
fig.text(.055,.762,r'$F_t(s)=8[H_0(z(s))-J_t(z(s))]/A(s),\qquad t=-8J_t(i)$',fontsize=13)
fig.text(.055,.709,'The first component H₀ is constant in t. Dropping Jₜ loses the actual deformation.',fontsize=11,color='#923030')
ax = fig.add_axes([.09,.235,.37,.36])
t = np.linspace(-.4,.4,401)
ax.plot(t,-t*(1+t)*(1+2*t)/6,color='#155c89',lw=2)
ax.axhline(0,lw=.7,color='#9098a0'); ax.axvline(0,lw=.7,color='#9098a0')
ax.set_title('Actual Hurwitz family at s = −2',fontsize=11)
ax.set_xlabel('Hurwitz parameter t'); ax.set_ylabel(r'$F_t(-2)$')
ax.set_ylim(-.18,.06)
ax.text(.035,.07,r'$F_t(-2)=-t(1+t)(1+2t)/6$',transform=ax.transAxes,fontsize=10)
bx = fig.add_axes([.60,.235,.33,.36])
bx.plot(t,np.zeros_like(t),color='#955432',lw=2)
bx.axvline(0,lw=.7,color='#9098a0')
bx.set_title('Returned classical heat family at s = −2',fontsize=11)
bx.set_xlabel('Independent heat parameter h'); bx.set_ylabel(r'$f_h^{\mathrm{heat}}(-2)$')
bx.set_ylim(-.18,.06)
bx.text(.055,.07,r'$f_h^{\mathrm{heat}}(-2)=0$ for every real $h$',transform=bx.transAxes,fontsize=10)
fig.text(.07,.16,'Exact curves from proved identities, not numerical zero samples. The two time parameters are not identified.',fontsize=10)
fig.text(.055,.095,'With local coordinate η = s − s₀: at s₀ = −2m, retain I = ηO inside O; O/I records the cancelled simple zero.\nAt s₀ = 1, retain O inside I = η⁻¹O; I/O records the cancelled simple pole.',fontsize=10)
fig.text(.055,.035,'Proofs: ZTC4–4a, 13–21; CFD6–10, 18–27. Kernel provenance: Rodgers–Tao, arXiv:1801.05914v5;\nshifted family: supplied April 2026 programme source, thm:universal-flow. Full proofs and exact source identities accompany this image.',fontsize=8.5,color='#505a63')
for suffix in ['png','svg']:
    fig.savefig(out/f'ORIGINAL_ZETA_RECOVERY.{suffix}',dpi=180)
plt.close(fig)

