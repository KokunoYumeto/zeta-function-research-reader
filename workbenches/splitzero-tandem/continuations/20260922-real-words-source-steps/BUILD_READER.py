from pathlib import Path
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import re,subprocess,tempfile,shutil,json,hashlib
from pypdf import PdfReader
P=Path(__file__).parent
plt.rcParams.update({'font.size':10})
fig,ax=plt.subplots(2,1,figsize=(7.1,7.6),height_ratios=[1,1.2],layout='constrained')
ax[0].axis('off');ax[0].set(xlim=(0,1),ylim=(0,1))
ax[0].text(.5,.95,'The actual source step carries the collision trace into curvature',ha='center',fontsize=12)
ax[0].text(.5,.76,r'$D(t)=G_N^{-1}+t\,uu^*,\quad u=b_{N+1}/\sqrt{\omega_{N+1}}$',ha='center',fontsize=12)
ax[0].text(.5,.57,r'$\chi_{\rm coll}=a_{N+1}\,{\rm Im}\,\sigma_{*,N+1}-a_N\,{\rm Im}\,\sigma_{*,N}$',ha='center',fontsize=12)
ax[0].text(.5,.36,r'$\Delta{\rm tr}\,W_B=2\chi_{\rm coll},\qquad \lambda=\frac{(1+\beta)t}{1+\beta t}$',ha='center',fontsize=13)
ax[0].text(.5,.13,r'$\Phi=(1-\lambda)\Phi_N+\lambda\Phi_{N+1}+\frac{2w\chi_{\rm coll}}{1+\beta}\lambda(1-\lambda)$',ha='center',fontsize=12)
tt=np.geomspace(.0003,1,1000)
for beta,color in [(3,'#9b5425'),(31,'#246a86'),(255,'#7656a0')]:
    ax[1].plot(tt,beta*tt*(1-tt)/(1+beta*tt)**2,label=rf'$\beta={beta}$',color=color,lw=2)
    at=1/(beta+2);peak=beta/(4*(1+beta))
    ax[1].scatter([at],[peak],color=color,zorder=5)
    ax[1].annotate(rf'$t=1/{beta+2}$',(at,peak),xytext=(at*.56,peak-.055),fontsize=9,arrowprops=dict(arrowstyle='->',color=color))
ax[1].set_xscale('log')
ax[1].set(xlabel=r'Original source parameter $t$ (logarithmic display)',ylabel=r'$\beta t(1-t)/(1+\beta t)^2$',title='Exact correction factor; auxiliary leverages, no assigned native trace',ylim=(-.008,.274))
ax[1].axhline(.25,color='#777777',ls=':',lw=1);ax[1].text(.055,.257,r'Limit $1/4$',fontsize=9)
ax[1].grid(alpha=.16);ax[1].legend(loc='lower left')
fig.savefig(P/'SOURCE_CURVATURE.png',dpi=200);plt.close(fig)

fig,ax=plt.subplots(2,1,figsize=(7.1,7.7),height_ratios=[1,1.2],layout='constrained')
ax[0].axis('off');ax[0].set(xlim=(0,1),ylim=(0,1))
ax[0].text(.5,.96,'Every polynomial boundary column retains its actual quotient metric',ha='center',fontsize=12)
ax[0].text(.5,.77,r'$[p_{N-d+1}],\ldots,[p_N]\quad|\quad[p_{N+1}],\ldots,[p_{N+d}]$',ha='center',fontsize=12)
ax[0].text(.5,.57,r'$F:\ \mathbb{C}^{2d}\longrightarrow E,\qquad K_0=F^*G_NF>0$',ha='center',fontsize=14)
ax[0].text(.5,.34,r'$\langle x,W_px\rangle_G=\|c_+\|^2-\|c_-\|^2$',ha='center',fontsize=15)
ax[0].text(.5,.11,r'$\mathrm{In}\,W_{p,t}=(d,d,q-2d)\quad\mathrm{for\ all}\quad0\leq t\leq1$',ha='center',fontsize=13)
d=np.arange(1,163);lo=np.maximum(0,d-120)
ax[1].fill_between(d,lo,d,color='#6a899d',alpha=.28,label=r'Allowed count for either sign')
ax[1].plot(d,d,color='#345b75',lw=2,label=r'Upper bound $d$')
ax[1].plot(d,lo,color='#81422b',lw=2,label=r'Forced lower bound $(d-m)_+$')
ax[1].plot([162,162],[42,162],color='#8b426b',lw=2)
ax[1].scatter([162],[42],color='#8b426b',zorder=6)
ax[1].annotate(r'$d=162:\ n_+\geq42,\ n_-\geq42$',(162,42),xytext=(43,27),fontsize=10,arrowprops=dict(arrowstyle='->',color='#8b426b'))
ax[1].set(xlim=(0,166),ylim=(-3,170),xlabel=r'Polynomial degree $d$',ylabel='Observed directions of either sign',title=r'Original size-five example: $k=17,\ q=324,\ m=120$')
ax[1].legend(loc='upper left',fontsize=9);ax[1].grid(alpha=.16)
fig.savefig(P/'WORD_SIGNATURE_MAP.png',dpi=200);plt.close(fig)

def outer(raw):
    # Preserve an explicit TeX space at a wrapped source line before stripping.
    # A dangling backslash would otherwise join the inserted \quad command.
    raw=re.sub(r'\\[ \t]+(?=\r?\n|$)',r'\\;',raw)
    out=[];start=0;braces=0;env=0;delims=0;i=0
    while i<len(raw):
        if raw.startswith('\\begin{',i):env+=1
        if raw.startswith('\\end{',i):env-=1
        if raw.startswith('\\left',i):delims+=1
        if raw.startswith('\\right',i):delims-=1
        if raw[i]=='{' and (i==0 or raw[i-1]!='\\'):braces+=1
        if raw[i]=='}' and (i==0 or raw[i-1]!='\\'):braces-=1
        step=0
        if braces==env==delims==0:
            if raw[i]=='\n':step=1
            elif raw.startswith('\\qquad',i):step=6
            elif raw.startswith('\\quad',i):step=5
        if step:
            chunk=raw[start:i].strip()
            if chunk:out.append(chunk)
            i+=step;start=i;continue
        i+=1
    if raw[start:].strip():out.append(raw[start:].strip())
    combined=[]
    for chunk in out:
        if combined and len(combined[-1])+len(chunk)<90:combined[-1]+='\\quad '+chunk
        else:combined.append(chunk)
    return combined
def display(m):
    raw=m.group(1).strip();tag=re.search(r'\\tag\{([^}]+)\}',raw)
    raw=re.sub(r'\\tag\{[^}]+\}','',raw).strip()
    if raw.startswith(r'\boxed{') and raw.endswith('}'):
        parts=outer(raw[7:-1])
        if len(parts)>1:raw=r'\boxed{\begin{gathered}'+r'\\ '.join(parts)+r'\end{gathered}}'
    parts=outer(raw)
    if len(parts)>1:raw=r'\begin{gathered}'+r'\\ '.join(parts)+r'\end{gathered}'
    return '\n\\begin{equation*}\n'+('\\tag{'+tag.group(1)+'}\n' if tag else '')+r'\begin{adjustbox}{max width=.92\linewidth}$\displaystyle '+raw+r'$\end{adjustbox}'+'\n\\end{equation*}\n'
def break_code(tex):
    result=[];pos=0;token=r'\texttt{'
    while True:
        at=tex.find(token,pos)
        if at<0:result.append(tex[pos:]);break
        result.append(tex[pos:at+len(token)]);i=at+len(token);start=i;depth=1
        while i<len(tex) and depth:
            if tex[i]=='{' and tex[i-1]!='\\':depth+=1
            elif tex[i]=='}' and tex[i-1]!='\\':depth-=1
            if depth:i+=1
        body=tex[start:i].replace('\\ ',' ')
        body=body.replace(r'\_',r'\_\allowbreak{}')
        body=body.replace('=',r'=\allowbreak{}').replace('/',r'/\allowbreak{}')
        body=body.replace(',',r',\allowbreak{}')
        result.append(body+'}');pos=i+1
    return ''.join(result)
head=r'''\documentclass[11pt]{article}
\usepackage[a4paper,margin=21mm]{geometry}
\usepackage{amsmath,amssymb,mathtools,mathrsfs,graphicx,adjustbox,float,longtable,booktabs,array,calc}
\usepackage[hidelinks,hypertexnames=false]{hyperref}\usepackage{xurl,fontspec}
\setmainfont{DejaVu Serif}\setmonofont{DejaVu Sans Mono}
\providecommand{\tightlist}{}\setlength{\emergencystretch}{4em}
\setcounter{secnumdepth}{0}\allowdisplaybreaks
\title{Real word currents and native source steps\\Complete original-metric signatures, volumes and marked-current curvature}
\author{Split-Zero research programme}\date{22 September 2026\\SZ-20260922-029}
\begin{document}\maketitle
The original arithmetic quotient has a complete positive source minimum.
For a real polynomial word of degree $d\le q/2$, its Hermitian current has
$d$ positive, $d$ negative and $q-2d$ zero directions. We calculate its
full boundary Gram and signed product, extend the finite signature calculation
to rational and real divisor words, and prove that the actual adjacent source
addition preserves polynomial inertia throughout the step. The original
observation retains the dimension bounds proved in WG12--13.

The same source step has an exact marked-current formula. Its curvature is
determined by the change in the observed trace, equivalently the weighted
imaginary displacement of the two actual dual-number collision fibres.
This transports the new geometric datum into the original scalar sign test.
All complete proofs and source dependencies are included. The particular
terminal imaginary pairing remains unevaluated; no RH conclusion is asserted.

The first proof gives the current integrated receivers. The independent
word proof supplies full sign-coordinate and denominator arguments.
The complete incoming WS proof is retained with its original scope;
WG and the new native-step proofs state its strengthened receivers.
The published 028 inverse and constant corrections continue to govern earlier
claims. Human sources and pinned programme proof links occur at use.
\tableofcontents\clearpage
\begin{figure}[H]\centering\includegraphics[width=.94\linewidth]{WORD_SIGNATURE_MAP.png}
\caption{Upper: the full boundary and sign-coordinate maps of WD5--20 and
WG5--8. The original metric $K_0$ remains present in the inverse coordinate map.
The native adjacent-step inertia is proved in NW6--16. Lower: WG12's exact
dimension bounds at the original size-five degree $k=17$. The shaded interval
is a proved range, not computed observed eigenvalue counts. At half degree,
every native source-step point has at least \(42\) observed directions of each
sign. The observation and all kernel directions retain their actual metrics.}
\end{figure}\clearpage
\begin{figure}[H]\centering\includegraphics[width=.94\linewidth]{SOURCE_CURVATURE.png}
\caption{Upper: NV25--26 and WG14--15 carry the two collision fibres into
the current's exact curvature. Each endpoint uses its own support weight.
Lower: the exact scalar correction profile at three stated auxiliary
leverages. Multiplication by $Y_0\rho_f\Delta\operatorname{tr}W_B$
gives the native correction; no trace value is assigned by the picture.
Every marked peak lies at $t=1/(\beta+2)$ and has height
$\beta/[4(1+\beta)]$. The original $t=0$ endpoint is omitted only from the
logarithmic plotting axis; its value is exactly zero.}
\end{figure}
'''
names=['INTEGRATION_AND_RECEIVERS.md','WORD_SIGNATURE_PROOF.md','WHOLE_SPACE_PROOF.md','NATIVE_WORD_ACTIVATION_PROOF.md','NATIVE_SOURCE_STEP_PROOF.md']
text=head
for index,name in enumerate(names,1):
    source=(P/name).read_text(encoding='utf-8')
    tex=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+tex_math_dollars+raw_tex','-t','latex','--wrap=none'],input=source,text=True,encoding='utf-8',capture_output=True,check=True).stdout
    # Prefix Pandoc's navigation targets without changing mathematical labels.
    tex=re.sub(r'\\(hypertarget|label)\{([^}]+)\}',lambda m:'\\'+m.group(1)+'{part'+str(index)+'-'+m.group(2)+'}',tex)
    tex=re.sub(r'\\\[(.*?)\\\]',display,tex,flags=re.S)
    tex=break_code(tex)
    text+='\n\\clearpage\n'+tex
text+='\n\\end{document}\n'
R=Path(tempfile.mkdtemp(prefix='splitzero029-'))
stem='REAL_WORDS_AND_SOURCE_STEPS'
(R/(stem+'.tex')).write_text(text,encoding='utf-8')
for name in ['WORD_SIGNATURE_MAP.png','SOURCE_CURVATURE.png']:shutil.copyfile(P/name,R/name)
for _ in range(3):
    run=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error',stem+'.tex'],cwd=R,capture_output=True,text=True,encoding='utf-8',errors='replace')
    (R/'LATEX_OUTPUT.txt').write_text(run.stdout,encoding='utf-8')
    if run.returncode:raise RuntimeError(run.stdout[-7000:])
for ext in ['pdf','tex']:shutil.copyfile(R/(stem+'.'+ext),P/(stem+'.'+ext))
log=(R/(stem+'.log')).read_text(encoding='utf-8',errors='replace')
qa={'pages':len(PdfReader(P/(stem+'.pdf')).pages),'pdf_sha256':hashlib.sha256((P/(stem+'.pdf')).read_bytes()).hexdigest(),'overfull':re.findall(r'Overfull[^\n]*',log),'undefined':re.findall(r'[^\n]*undefined[^\n]*',log),'missing_glyphs':re.findall(r'Missing character:[^\n]*',log),'visual_inspection':'pending'}
(P/'BUILD_QA.json').write_text(json.dumps(qa,indent=2),encoding='utf-8')
print(json.dumps(qa))
