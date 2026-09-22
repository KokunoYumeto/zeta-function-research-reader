from pathlib import Path
import shutil,subprocess,tempfile,re,json,hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pypdf import PdfReader

P=Path(__file__).parent
R=Path(tempfile.mkdtemp(prefix='splitzero028-reader-'))
plt.rcParams.update({'font.size':10,'axes.titlesize':12})
fig,ax=plt.subplots(2,1,figsize=(7.1,7.4),height_ratios=[1.15,1],layout='constrained')
ax[0].set(xlim=(0,1),ylim=(0,1));ax[0].axis('off')
box=dict(boxstyle='round,pad=.5',facecolor='#edf5f7',edgecolor='#17667b',linewidth=1.3)
ax[0].text(.17,.82,r'$H=\{e,f\}^{\perp}$',ha='center',bbox=box)
ax[0].text(.81,.82,r'$\mathrm{span}\{e,f\}$',ha='center',bbox=box)
ax[0].annotate('',(.65,.86),(.34,.86),arrowprops=dict(arrowstyle='->',color='#17667b',lw=2))
ax[0].text(.49,.96,r'$X_g=\sqrt{\epsilon}\,f g^\dagger$',ha='center',fontsize=11)
ax[0].annotate('',(.34,.74),(.65,.74),arrowprops=dict(arrowstyle='->',color='#a34c24',lw=2))
ax[0].text(.49,.65,r'$Y_g=\sqrt{\epsilon}\,g e^\dagger$',ha='center',fontsize=11)
ax[0].text(.5,.47,r'$X_gY_g=R,\qquad Y_gX_g=0$',ha='center',fontsize=13)
ax[0].text(.5,.32,r'Original observation: $F\mapsto J^\dagger FJ$',ha='center',fontsize=11)
ax[0].text(.5,.17,r'$\mathbb{E}(X_{B,g}Y_{B,g})=sR_B$',ha='center',fontsize=13)
ax[0].text(.5,.02,r'$i\mathbb{E}(X_BY_B-Y_B^*X_B^*)=sW_B,\quad 1/s<6$',ha='center',fontsize=12)
ax[0].set_title('MP7–24: ordered mixed support retains the signed current',pad=14)
alpha=.08
d=np.linspace(alpha+.005,1,400)
ax[1].fill_between(d,1-alpha,np.ones_like(d),color='#bee4e8',label=r'Proved band $1-\alpha\leq\vartheta_+\leq1$')
ax[1].fill_between(d,d-alpha,d,color='#f0d6be',label=r'Proved band $d-\alpha\leq\vartheta_-\leq d$')
ax[1].plot(d,np.ones_like(d),color='#17667b',lw=2)
ax[1].plot(d,d-alpha,color='#a34c24',lw=2)
ax[1].set(xlabel=r'Actual second-vector retention $d$',ylabel='Support eigenvalue',xlim=(.08,1),ylim=(0,1.1),title=r'ST8: both support eigenvalues, including the second direction')
ax[1].legend(fontsize=8.5,loc='center left');ax[1].grid(alpha=.2)
fig.savefig(P/'MIXED_SUPPORT_MAP.png',dpi=200);plt.close(fig)

fig,axes=plt.subplots(3,1,figsize=(7.1,9.0),height_ratios=[1,1,1],layout='constrained')
axes[0].axis('off');axes[0].set(xlim=(0,1),ylim=(0,1))
axes[0].text(.5,.94,'DF3–13: the collision is shifted by the full kernel return',ha='center',fontsize=12)
axes[0].text(.5,.74,r'$F_B(s)=(\epsilon v+su)u^*,\quad \lambda(s)=as+\epsilon r$',ha='center',fontsize=13)
axes[0].text(.19,.47,r'Native $s=0$'+'\n'+r'$R_B^2=\epsilon r R_B$',ha='center',bbox=box)
axes[0].text(.78,.47,r'$s_*=-\epsilon r/a$'+'\n'+r'$\widetilde R^2=0$',ha='center',bbox=box)
axes[0].annotate('',(.61,.49),(.36,.49),arrowprops=dict(arrowstyle='->',lw=2,color='#a34c24'))
axes[0].text(.5,.23,r'$\mathrm{Im}\,s_*={\mathrm{tr}\,W_B(0)}/{(2a)}$',ha='center',fontsize=13)
axes[0].text(.5,.05,'A real parameter reaches the collision exactly when the current trace vanishes.',ha='center',fontsize=9.5)
xx=np.linspace(0,1,501)
yy=(7*xx-1)*(5*xx-3)/(64*(1+xx)**2)
axes[1].plot(xx,yy,color='#17667b',lw=2)
axes[1].axhline(0,color='#777777',lw=.8)
axes[1].scatter([1/7,3/5],[0,0],color='#a34c24',zorder=5)
axes[1].annotate(r'$t=1/7$',(1/7,0),xytext=(.18,.018),arrowprops=dict(arrowstyle='->'),fontsize=10)
axes[1].annotate(r'$t=3/5$',(3/5,0),xytext=(.64,-.008),arrowprops=dict(arrowstyle='->'),fontsize=10)
axes[1].set(xlabel=r'Exact source parameter $t$, with adjacent endpoints $0,1$',ylabel='Observed marked current',title='SC18–23: two sign crossings with the same eigenclass')
axes[1].grid(alpha=.18)
axes[1].text(.46,.85,r'$\Phi(t)=\frac{(7t-1)(5t-3)}{64(1+t)^2}$',transform=axes[1].transAxes,fontsize=13)
a0=np.log(4/np.pi);a1=.06651895202027391967
bb=np.linspace(0,a0+.035,500)
ff=4*(np.maximum(a0-bb,0)-np.maximum(a1-bb,0))
axes[2].plot(bb,ff,color='#17667b',lw=2)
axes[2].axvline(a1,color='#a34c24',ls=':',lw=1)
axes[2].axvline(a0,color='#a34c24',ls=':',lw=1)
axes[2].set(xlabel=r'Time exponent $b$ in $|t|=e^{-bq}$',ylabel=r'Four-cutoff $\log\kappa\,/q$',title='EE39: the complete original four-cutoff condition profile',ylim=(-.045,.81))
axes[2].text(.006,.74,r'$4(a_0-a_1)=0.7001820930\ldots$',fontsize=10)
axes[2].text(a1+.004,.10,r'$a_1=\psi(1)$',fontsize=9)
axes[2].text(a0-.07,.24,r'$a_0=\log(4/\pi)$',fontsize=9)
axes[2].grid(alpha=.18)
fig.savefig(P/'OBSERVED_COLLISION.png',dpi=200);plt.close(fig)

names=['SUPPORT_SPECTRUM_AND_TERMINAL_MASS.md','MIXED_PROBE_PROOF.md','OBSERVED_DEFORMATION_AND_CURRENT.md','STABLE_HIDDEN_ACTION_AND_SIGN_STEPS.md','EVOLUTION_EXTENSION_PROOF.md']

def split_outer(raw):
    # Split only at actual outer math separators. Never split a matrix, boxed
    # group, delimiter pair or fraction argument.
    parts=[];start=0;braces=0;env=0;delims=0;i=0
    while i<len(raw):
        if raw.startswith('\\begin{',i):env+=1
        if raw.startswith('\\end{',i):env-=1
        if raw.startswith('\\left',i):delims+=1
        if raw.startswith('\\right',i):delims-=1
        c=raw[i]
        if c=='{' and (i==0 or raw[i-1]!='\\'):braces+=1
        if c=='}' and (i==0 or raw[i-1]!='\\'):braces-=1
        step=0
        if braces==env==delims==0:
            if c=='\n':step=1
            elif raw.startswith('\\qquad',i):step=6
            elif raw.startswith('\\quad',i):step=5
        if step:
            chunk=raw[start:i].strip()
            if chunk:parts.append(chunk)
            i+=step;start=i;continue
        i+=1
    chunk=raw[start:].strip()
    if chunk:parts.append(chunk)
    # Avoid dozens of one-symbol lines; join short outer chunks up to 100 chars.
    out=[];current=''
    for chunk in parts:
        if current and len(current)+len(chunk)<100:
            current+='\\quad '+chunk
        else:
            if current:out.append(current)
            current=chunk
    if current:out.append(current)
    return out

def display(m):
    raw=m.group(1).strip()
    tag=re.search(r'\\tag\{([^}]+)\}',raw)
    label=tag.group(1) if tag else None
    raw=re.sub(r'\\tag\{[^}]+\}','',raw).strip()
    if raw.startswith(r'\boxed{') and raw.endswith('}'):
        inner=raw[7:-1]
        chunks=split_outer(inner)
        if len(chunks)>1:raw=r'\boxed{\begin{gathered}'+r'\\ '.join(chunks)+r'\end{gathered}}'
    chunks=split_outer(raw)
    if len(chunks)>1:raw=r'\begin{gathered}'+r'\\ '.join(chunks)+r'\end{gathered}'
    # max width is a guard for a few long indivisible identities; most displays
    # remain at the same font size after the explicit outer-line splits.
    return '\n\\begin{equation*}\n'+('\\tag{'+label+'}\n' if label else '')+r'\begin{adjustbox}{max width=.92\linewidth}$\displaystyle '+raw+r'$\end{adjustbox}'+'\n\\end{equation*}\n'

head=r'''\documentclass[10pt]{article}
\usepackage[a4paper,margin=19mm]{geometry}
\usepackage{amsmath,amssymb,mathtools,amsthm,mathrsfs,longtable,booktabs,array,calc,enumitem,float,graphicx,adjustbox}
\usepackage[hidelinks,hypertexnames=false]{hyperref}\usepackage{xurl}
\usepackage{fontspec}\setmainfont{DejaVu Serif}
\setlength{\emergencystretch}{4em}\providecommand{\tightlist}{}
\setcounter{secnumdepth}{0}\setcounter{tocdepth}{1}\allowdisplaybreaks
\title{Split support through the original arithmetic observation\\Support, signed-current stability and longer arithmetic evolution}
\author{Split-Zero research programme}
\date{22 September 2026\\SZ-20260922-028}
\begin{document}\maketitle
The original split support and its mixed cubic maps survive the programme's actual
minimum-section observation in quantitatively controlled forms. This continuation
calculates both measured support eigenvalues, their complete hidden-kernel defect,
and their effect on the terminal arithmetic class. A complete finite family of
ordered mixed products recovers the original signed current with amplification
less than six, uniformly in the original degree. Positive mixed products recover
the measured support itself. The new deformation has a shifted collision whose
imaginary displacement records the current trace. All original source metrics,
period guards, complex phases and four cutoffs remain in the proofs.

The signed current has a finite metric-stability bound and an exact quadratic
numerator along each original source step. Growing source-jet control extends
the measured and intrinsic arithmetic evolution, including their actual inverses,
to a longer time interval and evaluates its lower condition-number plateau.
DF15--16 and EE47--48 correct the constant name in the earlier RD15:
the response coefficient is $4[\psi(0)-\psi(1)]=0.7001820930\ldots$;
the kernel-volume constant remains $C_\partial=1.3542819878\ldots$.
The exact integral map connecting the two is proved in those sections.

The new results strengthen the support receiver and terminal-current calculation.
The particular terminal signed mixed-product value remains to be evaluated; no
Riemann-hypothesis conclusion is asserted. Complete new proofs, exact auxiliary
checks and the preceding proof collection accompany this reader. Pinned public
sources and inherited human citations are given at their uses.
\tableofcontents
\clearpage
\begin{figure}[H]\centering\includegraphics[width=.94\linewidth]{MIXED_SUPPORT_MAP.png}
\caption{Upper: the two actual support blocks and their ordered product through
the original isometry, proved in MP7--24. The average uses every vector of an
orthonormal basis of the original complement; the result is independent of that
basis. Its inverse factor is bounded by the original five-orbit rank theorem.
Lower: the exact ST8 bands. To show both directions, the illustrative family uses
$\alpha=0.08$ and $|r|^2=\alpha(1-d)$, $d>\alpha$, giving exactly
$\vartheta_+=1$, $\vartheta_-=d-\alpha$. It is a positive contraction family,
not a numerical sample of native period data. Every actual matrix obeys the
proved bands without that illustration's parameter choice.}
\end{figure}
\clearpage
\begin{figure}[H]\centering\includegraphics[width=.90\linewidth]{OBSERVED_COLLISION.png}
\caption{Upper: the exact native-to-collision parameter map DF3--13. The source
family is the pinned ID1--24 construction; its original-metric receiver is proved
below. Middle: the exact finite example of SC23, with its specified fixed
$M,x,K$ and complete positive metric $G(t)=(I+tuu^*)^{-1}$. The two crossings
$1/7,3/5$ attain the quadratic degree bound of the original source-step formula.
This is an auxiliary finite example, not a native-period sign calculation.
The coefficient formulas and full metric are retained in the proof.
Lower: EE39's limiting four-cutoff profile
$4[(a_0-b)_+-(a_1-b)_+]$, with its proved $O(k\log q)$ unscaled error.
The values $a_i=\psi(i)$ come from the original elliptic formulas, EE47--48.
The new lower plateau holds for each fixed $0<b<a_1$ and at the proved
subexponential clock; the picture does not assign a value at literal $t=1$.}
\end{figure}
'''
text=head
for name in names:
    source=(P/name).read_text(encoding='utf-8')
    tex=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+tex_math_dollars+raw_tex','-t','latex','--wrap=none'],input=source,capture_output=True,text=True,encoding='utf-8',check=True).stdout
    tex=re.sub(r'\\\[(.*?)\\\]',display,tex,flags=re.S)
    text+='\n\\clearpage\n'+tex
text+='\n\\end{document}\n'
texpath=R/'SUPPORT_TRANSPORT_READER.tex';texpath.write_text(text,encoding='utf-8')
for name in ['MIXED_SUPPORT_MAP.png','OBSERVED_COLLISION.png']:
    shutil.copyfile(P/name,R/name)
for _ in range(3):
    run=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error',texpath.name],cwd=R,capture_output=True,text=True,encoding='utf-8',errors='replace')
    (R/'LATEX_OUTPUT.txt').write_text(run.stdout,encoding='utf-8')
    if run.returncode:raise RuntimeError(run.stdout[-7000:])
pdf=texpath.with_suffix('.pdf');log=texpath.with_suffix('.log').read_text(encoding='utf-8',errors='replace')
shutil.copyfile(texpath,P/texpath.name);shutil.copyfile(pdf,P/pdf.name)
qa={'pages':len(PdfReader(pdf).pages),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'build_directory':str(R),'overfull':re.findall(r'Overfull[^\n]*',log),'undefined':re.findall(r'[^\n]*undefined[^\n]*',log),'visual_inspection':'pending'}
(P/'BUILD_QA.json').write_text(json.dumps(qa,indent=2),encoding='utf-8')
print(json.dumps(qa))
