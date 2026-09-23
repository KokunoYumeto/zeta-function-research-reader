from pathlib import Path
import json
import hashlib
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

R = Path(__file__).resolve().parent
out = R / 'cc_weil_boundary_delivery'
out.mkdir(exist_ok=True)
figout = R / 'cc_weil_boundary_figures'
figout.mkdir(exist_ok=True)
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11,
                     'mathtext.fontset': 'dejavusans'})
fig = plt.figure(figsize=(12, 8), facecolor='white')
fig.text(.055, .95, 'The exact Hurwitz boundary and its retained support', fontsize=17, weight='bold')
ax = fig.add_axes([.09,.42,.43,.43])
t = np.linspace(-.94, .7, 501)
ax.plot(t, np.pi*t*(1+t)*(1+2*t)/2, color='#155b8a', lw=2)
ax.axhline(0, color='#777777', lw=.8)
ax.scatter([-.5,0],[0,0],color='#17693c',s=45,zorder=4)
ax.annotate('t = −1/2',(-.5,0),(-.72,1.3),arrowprops={'arrowstyle':'->'},fontsize=10)
ax.annotate('t = 0',(0,0),(.14,.75),arrowprops={'arrowstyle':'->'},fontsize=10)
ax.set_xlabel('Original Hurwitz displacement t > −1')
ax.set_ylabel(r'$c_1(t,1)=\pi t(1+t)(1+2t)/2$')
ax.set_title('Exact leading boundary coefficient (b = 1)', fontsize=11)
fig.text(.57,.83,'Every boundary coefficient is retained:',fontsize=11,weight='bold')
fig.text(.57,.765,r'$c_m(t,b)=\frac{(-1)^{m+1}\pi^m B_{2m+1}(1+t)}{(m-1)!\,b^{2m}}$',fontsize=15)
fig.text(.57,.69,'These are exactly the Mellin residues at s = −2m.',fontsize=10)
fig.text(.57,.61,r'$\partial\Psi_{t,b}=(c_m(t,b))_{m\geq1}$',fontsize=15)
fig.text(.57,.54,r'$\ker\partial=\mathcal{B}$',fontsize=18)
fig.text(.57,.48,'The kernel statement includes every derivative.',fontsize=10)
fig.text(.07,.32,'Mixed cancellation retains a nonzero function and supported zero',fontsize=13,weight='bold')
fig.text(.08,.252,r'$u=\Psi_{a-1,b}+\Psi_{-a,b}\ne0,\quad 0<a<1,\qquad\partial u=0$',fontsize=17)
fig.text(.08,.176,r'$G_L(\partial)(u,1_L)=(0,1_L)=e\ne\tau=(0,0_L)$',fontsize=17)
fig.text(.07,.095,'The lattice L is nontrivial. The two marked t values classify individual shifts; reflected sums cancel every boundary term.',fontsize=9.5)
fig.text(.07,.045,'Exact formulas and analytic remainder bounds: HCB5–14, HCB18–24, HCB30–33. Human source: Connes–Consani–Marcolli,\nmath/0703392v1, SCK and degmodifyV. This plot is not a sampled zero plot or an RH conclusion.',fontsize=8.5,color='#505a63')
for ext in ('png','svg','pdf'):
    fig.savefig(figout / ('HURWITZ_WEIL_BOUNDARY.'+ext),dpi=180)
plt.close(fig)

fig=plt.figure(figsize=(12,6.8),facecolor='white')
fig.text(.06,.94,'Exact arithmetic receivers: endpoint jets and the full primary block',fontsize=16,weight='bold')
fig.text(.06,.845,r'$\mathcal{M}f_b(s)=2b^s\zeta(s)\left[\frac{\pi^2\Gamma((s+4)/2)}{2\pi^{(s+4)/2}}-\frac{3\pi\Gamma((s+2)/2)}{4\pi^{(s+2)/2}}\right]$',fontsize=15)
fig.text(.065,.71,'Endpoints s = 0 and s = 1',fontsize=13,weight='bold',color='#165e87')
fig.text(.065,.64,r'$\mathcal{M}f_b(0)=1/4,\qquad\mathcal{M}f_b(1)=b/4$',fontsize=15)
fig.text(.065,.55,'Finite combinations at distinct widths adjust every finite endpoint jet.\nThe actual restriction-image class and its numerical trace stay fixed.',fontsize=11)
fig.text(.065,.40,'At an original nontrivial zero ρ of multiplicity m',fontsize=13,weight='bold',color='#165e87')
fig.text(.065,.325,r'$\mathcal{O}/h^{\min(m,N)}\mathcal{O},\quad h=s-\rho,\qquad\mathsf{N}[v]=[hv]$',fontsize=17)
fig.text(.065,.235,r'$[1]\ \longmapsto\ [h]\ \longmapsto\ [h^2]\ \longmapsto\ 0\qquad (m=N=3)$',fontsize=17)
fig.text(.065,.15,r'$(\mathsf{N}^{\uparrow})^3(v,\lambda)=(0,\lambda)=e\cdot(v,\lambda)$',fontsize=17)
fig.text(.065,.052,'WJI7–18 prove the general block and all scaling factors. The three-step chain is the explicitly stated m = N = 3 example.\nTrivial-zero and pole contributions require the retained original multiplier and embedded lattices; no divisor is discarded.',fontsize=9,color='#505a63')
for ext in ('png','svg','pdf'):
    fig.savefig(figout / ('WEIL_JETS_AND_SUPPORT.'+ext),dpi=180)
plt.close(fig)

names=['ORIGINAL_ZETA_THETA_CORRECTION.tex',
       'CC_EXACT_TRIVIAL_CORRESPONDENCE.tex',
       'CC_SUPPORTED_WEIL_QUOTIENT.tex',
       'CC_WEIL_JET_INTERPOLATION.tex',
       'HURWITZ_CC_TEST_SPACE_BOUNDARY.tex',
       'CC_RATIONAL_MIXED_BOUNDARY.tex']
preamble=r'''\documentclass[11pt]{article}
\usepackage[a4paper,margin=24mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{amsmath,amssymb,amsthm,mathtools,graphicx,microtype}
\usepackage[hidelinks,hypertexnames=false]{hyperref}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\title{Original zeta, adelic correspondences, and the full Hurwitz boundary}
\author{Programme derivations from the cited human sources}
\date{23 September 2026}
\begin{document}\maketitle
This reader applies the original Connes--Consani--Marcolli restriction
map and trace domain to the programme's unchanged Hurwitz family and
arbitrary split-support lattice. It retains the original zeta and
Hurwitz functions, every Gamma and Haar factor, both endpoint values,
every boundary residue, all primary-block nilpotents and all support
labels. The analytic trace theorem is a precisely cited source input;
no new positivity theorem or RH conclusion is asserted.

The first chapter corrects the preceding theta-origin, completion,
and fibre explanations. Its maps have their specified domains:
meromorphic modules, embedded holomorphic lattices, the transported
product, and the common-label support carrier. Scalar zero preservation
does not by itself prove preservation of the programme's multiplication
or Weil pairing. The following chapters construct the actual adelic
restriction and full boundary receivers.

The chapters give the complete new derivations. The source archive
also retains the original author archive, the preceding complete
programme sources used for comparisons, exact source identities,
reproducible figures and supplementary checks. Original-zeta Mellin
endpoints and exceptional local lattices remain explicit throughout.
\tableofcontents\clearpage
\begin{figure}[p]\centering
\includegraphics[width=\textwidth]{HURWITZ_WEIL_BOUNDARY.pdf}
\caption{The complete boundary is a sequence, not only its first
coordinate. The plotted first coefficient is exact at $b=1$.
Reflected mixtures cancel every coefficient while retaining
their nonzero function and supported zero.}\end{figure}
\begin{figure}[p]\centering
\includegraphics[width=\textwidth]{WEIL_JETS_AND_SUPPORT.pdf}
\caption{Actual restriction-image functions adjust endpoint jets
without changing the spectral class. At a nontrivial zero the full
primary block survives, including its nilpotent and its supported-zero
power. The displayed three-step example has $m=N=3$.}\end{figure}
\clearpage
'''
parts=[preamble]
def reader_layout(source):
    # Presentation only: preserve every token of the mathematical expressions.
    source = re.sub(r'\\texttt\{([0-9a-f]{64})\}',
                    lambda m: r'\texttt{' + r'\allowbreak{}'.join(
                        m[1][i:i+16] for i in range(0,64,16)) + '}', source)
    for tag in ('HCB13','HCB30'):
        start = source.index(r'\begin{equation}\tag{'+tag+'}')
        stop = source.index(r'\end{equation}', start)
        block = source[start:stop]
        if tag == 'HCB13':
            block = block.replace(' \\qquad\n', ' \\\\\n')
        else:
            block = block.replace('},\\quad\n', '},\\\\\n').replace('),\\quad\n', '),\\\\\n')
        block = block.replace(r'\tag{'+tag+'}', r'\tag{'+tag+r'}\begin{gathered}',1)
        source = source[:start] + block + '\\end{gathered}\n' + source[stop:]
    return source
for name in names:
    source = (R/'independent'/name).read_text(encoding='utf-8')
    if name == 'HURWITZ_CC_TEST_SPACE_BOUNDARY.tex':
        source = reader_layout(source)
    else:
        source = re.sub(r'\\texttt\{([0-9a-f]{64})\}',
                        lambda m: r'\texttt{' + r'\allowbreak{}'.join(
                            m[1][i:i+16] for i in range(0,64,16)) + '}', source)
    parts += ['\n% Complete programme source: '+name+'\n',
              source,'\n\\clearpage\n']
parts += ['\n\\end{document}\n']
(out/'CC_WEIL_BOUNDARY_READER.tex').write_text(''.join(parts),encoding='utf-8')
for file in figout.glob('*.pdf'):
    (out/file.name).write_bytes(file.read_bytes())
record={'sources':{n:hashlib.sha256((R/'independent'/n).read_bytes()).hexdigest() for n in names},
        'reader_sha256':hashlib.sha256((out/'CC_WEIL_BOUNDARY_READER.tex').read_bytes()).hexdigest()}
(R/'CC_WEIL_BUILD_SOURCE_HASHES_PRIVATE.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record,indent=2))
