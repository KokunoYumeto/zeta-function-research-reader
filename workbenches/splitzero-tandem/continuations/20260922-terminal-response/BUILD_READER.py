from pathlib import Path
import json,hashlib,subprocess,re,tempfile,shutil
import numpy as np
import mpmath as mp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pypdf import PdfReader

P=Path(__file__).parent
R=Path(tempfile.mkdtemp(prefix='splitzero027-reader-'))
mp.mp.dps=35
def profile(z):
    F=2*mp.ellipk(z)/mp.pi
    t=2*(mp.ellipe(z)/((1-z)*mp.ellipk(z))-1)
    L=mp.log(4/(mp.pi*(1+t)*(1-z)*F))
    return float(t),float((1+t)*L+t*mp.log(z)/4)
z1=mp.findroot(lambda z:profile(z)[0]-1,(.5,.55))
v=np.array([profile(mp.mpf(float(z))) for z in np.r_[np.geomspace(1e-10,.001,70),np.linspace(.001,float(z1),500)]])
t=np.r_[0,v[:,0]];psi=np.r_[float(mp.log(4/mp.pi)),v[:,1]]
plt.rcParams.update({'font.size':10})
fig,axes=plt.subplots(2,1,figsize=(6.6,7.2),layout='constrained',gridspec_kw={'height_ratios':[1.2,1]})
ax=axes[0]
ax.plot(t,2*psi,color='#9c3e15',label=r'$q^{-1}\log\alpha_{\rm resp}\ \longrightarrow\ 2\psi(t)$')
ax.plot(t,0*t,color='#087684',lw=2,label=r'$q^{-1}\log\beta_{\rm resp}\ \longrightarrow\ 0$')
ax.set(xlabel=r'Original degree parameter $t=(N+1-q)/q$',ylabel='Proved leading rate',xlim=(0,1),title='RD10–15: the exponential cost belongs to one denominator')
ax.legend(fontsize=9);ax.grid(alpha=.2)
ax=axes[1];ax.axis('off');ax.set(xlim=(0,1),ylim=(0,1))
ax.text(.18,.83,r'$c_g=\langle g,\widehat y\rangle$'+'\n'+r'$c_h=\langle h,\widehat y\rangle$',ha='center',va='center',bbox=dict(boxstyle='round',ec='#087684',fc='#eaf5f6'))
ax.text(.81,.83,r'$z_+=iA_*c_g+B_*c_h$'+'\n'+r'$z_-=-iB_*c_g+A_*c_h$',ha='center',va='center',bbox=dict(boxstyle='round',ec='#9c3e15',fc='#fbf0e9'))
ax.annotate('',xy=(.58,.83),xytext=(.39,.83),arrowprops=dict(arrowstyle='->',lw=1.8))
ax.text(.49,.98,'Exact unitary map',ha='center',fontsize=9)
ax.text(.5,.55,r'$A_*z_+-B_*z_-=i c_g,\qquad |c_g|\leq\eta_N$',ha='center',fontsize=12)
ax.text(.5,.33,r'$|z_+-z_-|^2\leq(\sqrt{2}\eta_N+\delta_N^{\rm tr})^2$',ha='center',fontsize=12)
ax.text(.5,.11,r'TR18: coherence deficit $\leq\exp[-2q\psi(t)+O(k\log q)]$',ha='center',fontsize=10)
fig.savefig(P/'TERMINAL_RESPONSE.png',dpi=210);plt.close(fig)
shutil.copyfile(P/'TERMINAL_RESPONSE.png',R/'TERMINAL_RESPONSE.png')
head=r'''\documentclass[10pt]{article}
\usepackage[a4paper,margin=19mm]{geometry}
\usepackage{amsmath,amssymb,mathtools,amsthm,mathrsfs,longtable,booktabs,array,calc,enumitem,float,graphicx}
\usepackage[hidelinks,hypertexnames=false]{hyperref}\usepackage{xurl}
\usepackage{fontspec}\setmainfont{DejaVu Serif}
\setlength{\emergencystretch}{4em}\providecommand{\tightlist}{}
\setcounter{secnumdepth}{0}\allowdisplaybreaks
\title{The original terminal arithmetic response\\Separate denominator rates and complex current coherence}
\author{Split-Zero research programme}
\date{22 September 2026\\SZ-20260922-027}
\begin{document}\maketitle
The two boundary denominators of the original arithmetic eigenclass have different
growth rates. The first carries the complete exponential amplification; the second
has logarithmic size at most $O(k+\log q)$. The actual observation responses retain
all their complex phases and complete kernel components.

On the established conductor period domain, the observed terminal class lies
exponentially close to a precisely defined complex hyperplane. This controls the
complex amplitudes in the current's positive and negative eigenspaces, improving
the preceding comparison of their squared magnitudes. The diagonal trace correction
to its current is absolutely exponentially small. The remaining sign belongs to
the retained imaginary cross-coordinate and is not assigned by these bounds.

All original sources, cutoffs, maps and metrics are retained. The preceding complete
proof collection is included unchanged in the accompanying recoverable source bank,
followed by these two complete new proofs and their reproducible auxiliary checks.
\tableofcontents
\clearpage
\begin{figure}[H]\centering
\includegraphics[width=.98\linewidth]{TERMINAL_RESPONSE.png}
\caption{Upper: the exact leading profiles in RD14, sampled from the retained
elliptic formulas; these curves are limiting rates, not finite native-period data.
The errors remain those stated in RD14--15. Lower: the exact complex-coordinate
map TR14--18 in the original metric. $A_*,B_*$ are positive and have squared sum
one. No phase angle is assigned at zero amplitude; the squared difference is valid
there as well. The complete proof retains every zero eigendirection. Human source
for the elliptic formulas: B. C. Carlson, DLMF 19.5 and 19.8; the programme-specific
receiving maps and estimates are proved in full below.}
\end{figure}
'''
text=head
for name in ['RESPONSE_DENOMINATORS.md','TERMINAL_COHERENCE_PROOF.md']:
    body=subprocess.run(['pandoc',str(P/name),'-f','markdown+tex_math_single_backslash+tex_math_dollars+raw_tex','-t','latex','--wrap=none'],capture_output=True,text=True,encoding='utf-8',check=True).stdout
    body=body.replace(r'''e=b_N/\sqrt{E_N},\qquad f=b_{N+1}/\sqrt{F_N},\qquad
\epsilon=\sqrt{E_NF_N}/\omega_N,\qquad
M=C+\epsilon f e^\dagger,\quad C=C^\dagger,\quad e\perp f,\quad
\|e\|=\|f\|=1.
\tag{TR4}''',r'''\begin{gathered}
e=b_N/\sqrt{E_N},\qquad f=b_{N+1}/\sqrt{F_N},\qquad
\epsilon=\sqrt{E_NF_N}/\omega_N,\\
M=C+\epsilon f e^\dagger,\quad C=C^\dagger,\quad e\perp f,\quad
\|e\|=\|f\|=1.
\end{gathered}\tag{TR4}''')
    body=body.replace(r'''\log\epsilon=q\psi(t_N)+O_{h,\varpi}(k\log q),\quad
-\log\Theta_N=O_{h,\varpi}(k\log q),\quad
\alpha\le e^{-2q\psi(t_N)+O_{h,\varpi}(k\log q)},\quad
\log D=O_h(k+\log q),''',r'''\begin{gathered}
\log\epsilon=q\psi(t_N)+O_{h,\varpi}(k\log q),\quad
-\log\Theta_N=O_{h,\varpi}(k\log q),\\
\alpha\le e^{-2q\psi(t_N)+O_{h,\varpi}(k\log q)},\quad
\log D=O_h(k+\log q).
\end{gathered}''')
    text+='\n\\clearpage\n'+body
text+='\n\\end{document}\n'
tex=R/'TERMINAL_RESPONSE_READER.tex';tex.write_text(text,encoding='utf-8')
for _ in range(3):
    r=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error',tex.name],cwd=R,capture_output=True,text=True,encoding='utf-8',errors='replace')
    (R/'LATEX_OUTPUT.txt').write_text(r.stdout,encoding='utf-8')
    if r.returncode: raise RuntimeError(r.stdout[-6000:])
pdf=tex.with_suffix('.pdf');log=tex.with_suffix('.log').read_text(encoding='utf-8',errors='replace')
shutil.copyfile(tex,P/tex.name);shutil.copyfile(pdf,P/pdf.name)
qa={'pages':len(PdfReader(pdf).pages),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
    'overfull':re.findall(r'Overfull[^\n]*',log),'undefined':re.findall(r'[^\n]*undefined[^\n]*',log),
    'missing':re.findall(r'[^\n]*Missing character[^\n]*',log),'visual':'pending'}
(R/'BUILD_QA.json').write_text(json.dumps(qa,indent=2)+'\n',encoding='utf-8')
print(json.dumps(qa,indent=2));print(str(R/'BUILD_QA.json'))
