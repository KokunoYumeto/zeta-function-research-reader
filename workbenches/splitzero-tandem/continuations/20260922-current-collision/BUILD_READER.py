from pathlib import Path
import json, re, subprocess, shutil, tempfile, hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pypdf import PdfReader
P=Path(__file__).parent
fig,axes=plt.subplots(1,2,figsize=(10,4.7),layout='constrained')
a,d,eps,mu,eta=.8,.7,1.,.6,.14
r=.08+.06j;D=a*d-abs(r)**2
for ax,xlim,ylim in [(axes[0],(0,.61),(-.52,.48)),(axes[1],(.49,.605),(-.23,.20))]:
    rr=np.linspace(*xlim,900); jj=np.linspace(*ylim,900)
    RHO,J=np.meshgrid(rr,jj)
    Y=-(J+2*eps*r.imag*RHO)/(2*eps*np.sqrt(D))
    R=RHO*(mu-RHO)-Y**2
    mid=(D*mu+(r.real**2-r.imag**2-D)*RHO-r.imag*J/eps)/(a*d)
    Zmin=mid-2*np.sqrt(D)*abs(r.real)/(a*d)*np.sqrt(np.maximum(0,R))
    ellipse=(R>=0)&(RHO>=0)&(RHO<=mu)
    cap=ellipse&(Zmin<=eta**2)
    ax.contourf(RHO,J,ellipse.astype(float),levels=[.5,1.5],colors=['#e5e9ed'])
    ax.contourf(RHO,J,cap.astype(float),levels=[.5,1.5],colors=['#376f91'])
    ax.contour(RHO,J,R,levels=[0],colors=['#70828f'],linewidths=.8)
    ax.set(xlim=xlim,ylim=ylim,xlabel=r'Actual source overlap $\rho_f$',ylabel=r'Marked current $j$')
    ax.grid(alpha=.16)
axes[0].set_title('Shared phase: full ellipse and retained coordinate cap')
axes[1].set_title('The same feasible region, enlarged')
axes[0].text(.02,.96,r'$|c_g|\leq0.14$ selects the blue region',transform=axes[0].transAxes,va='top',fontsize=9)
fig.suptitle(r'PO7: auxiliary measured Gram $a=0.8,\ d=0.7,\ r=0.08+0.06i,\ \epsilon=1,\ \mu=0.6$',fontsize=11)
fig.savefig(P/'JOINT_CURRENT_OVERLAP.png',dpi=180);plt.close(fig)

fig,ax=plt.subplots(figsize=(7.6,4.6),layout='constrained')
for c,color in [(.025,'#265e83'),(.1,'#9b5437'),(.2,'#73568d')]:
    margin=np.linspace(4*c,2,500)
    ax.plot(.5+margin,c/(margin*(margin-c)),label=rf'$c={c}$',color=color)
    ax.scatter([.5+4*c],[1/(12*c)],color=color,s=22)
ax.set(xlabel=r'Physical height ratio $|\operatorname{Im}\zeta|/b$',ylabel=r'Upper bound for $b\|G_*-G_0\|$',title=r'CRX8: $c/[\varrho(\varrho-c)]$, with $\varrho=|\operatorname{Im}\zeta|/b-1/2$')
ax.set_yscale('log');ax.grid(alpha=.18);ax.legend()
fig.savefig(P/'EXTERIOR_COLLISION_BOUND.png',dpi=180);plt.close(fig)

def outer(raw):
    # Preserve an explicit TeX space at a wrapped source line before stripping.
    # A dangling backslash would otherwise join the inserted \quad command.
    raw=re.sub(r'(?<!\\)\\[ \t]*(?=\r?\n|$)',r'\\;',raw)
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


HEAD=r'''\documentclass[11pt]{article}
\usepackage[a4paper,margin=21mm]{geometry}
\usepackage{amsmath,amssymb,mathtools,graphicx,adjustbox,float,longtable,booktabs,array,calc}
\usepackage[hidelinks,hypertexnames=false]{hyperref}\usepackage{xurl,fontspec}
\setmainfont{DejaVu Serif}\setmonofont{DejaVu Sans Mono}
\providecommand{\tightlist}{}\setlength{\emergencystretch}{4em}
\setcounter{secnumdepth}{0}\allowdisplaybreaks
\title{The original current, its source overlap and the collision resolvent}
\author{Split-Zero research programme}\date{22 September 2026\\SZ-20260922-030}
\begin{document}\maketitle
The same two complex coordinates determine the marked arithmetic current and
the next-source overlap. We calculate their joint feasible region, including
the retained coordinate cap, and the sharp bound for every real linear
combination needed by the native source step. The measured-mass interval is
handled without assuming monotonicity. All metric maps and equality cases
are included.

The second calculation retains the full arithmetic operator and controls its
change at the observed dual-number collision on the stated exterior frequency
region. Its error is bounded by the original source leakage and area data at
all four cutoffs. The interior native phase and its particular marked sign
remain unevaluated. This source includes complete proofs and the unchanged
preceding proof collection.
\tableofcontents\clearpage
\begin{figure}[H]\centering\includegraphics[width=\linewidth]{JOINT_CURRENT_OVERLAP.png}
\caption{PO4--8 gives an exact coordinate map and reconstruction of the shared
phase. The grey ellipse drops the coordinate cap; the blue region retains it.
The right panel enlarges the same region. These displayed positive Gram data
are auxiliary probes, with all constants printed above the figure. They are
not evaluated native periods or zeta zeros. PO9--18 optimizes a common phase
in this region instead of combining two independently chosen extrema.}
\end{figure}
\begin{figure}[H]\centering\includegraphics[width=.94\linewidth]{EXTERIOR_COLLISION_BOUND.png}
\caption{CRX7--8 proves the plotted upper bounds for the full original
resolvent, including its selfadjoint part. Here $b=\epsilon\sqrt D$ and
$c=|r|/\sqrt D$. Each curve starts at its exact sufficient margin
$\varrho=4c$. The physical frequency is related to the horizontal coordinate
by the displayed ratio; the figure does not identify different cutoff scales.
The curves are proved bounds at the stated auxiliary values of $c$, not
sampled native resolvent norms. CRX10--12 retains the logarithmic determinant
and all four original cutoff errors.}
\end{figure}
'''
text=HEAD
for index,name in enumerate(['PHASE_OVERLAP_PROOF.md','COLLISION_RESOLVENT_EXTERIOR.md'],1):
    source=(P/name).read_text(encoding='utf-8')
    tex=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+tex_math_dollars+raw_tex','-t','latex','--wrap=none'],input=source,text=True,encoding='utf-8',capture_output=True,check=True).stdout
    tex=re.sub(r'\\(hypertarget|label)\{([^}]+)\}',lambda m:'\\'+m.group(1)+'{part'+str(index)+'-'+m.group(2)+'}',tex)
    tex=re.sub(r'\\\[(.*?)\\\]',display,tex,flags=re.S)
    text+='\n\\clearpage\n'+break_code(tex)
text+='\n\\end{document}\n'
R=Path(tempfile.mkdtemp(prefix='splitzero030-'));stem='CURRENT_AND_COLLISION'
(R/(stem+'.tex')).write_text(text,encoding='utf-8')
for name in ['JOINT_CURRENT_OVERLAP.png','EXTERIOR_COLLISION_BOUND.png']:shutil.copyfile(P/name,R/name)
for _ in range(3):
    run=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error',stem+'.tex'],cwd=R,capture_output=True,text=True,encoding='utf-8',errors='replace')
    if run.returncode:raise RuntimeError(run.stdout[-5000:])
for ext in ['pdf','tex']:shutil.copyfile(R/(stem+'.'+ext),P/(stem+'.'+ext))
log=(R/(stem+'.log')).read_text(encoding='utf-8',errors='replace')
qa={'pages':len(PdfReader(P/(stem+'.pdf')).pages),'pdf_sha256':hashlib.sha256((P/(stem+'.pdf')).read_bytes()).hexdigest(),'overfull':re.findall(r'Overfull[^\n]*',log),'undefined':re.findall(r'[^\n]*undefined[^\n]*',log),'missing_glyphs':re.findall(r'Missing character:[^\n]*',log),'visual_inspection':'pending'}
(P/'BUILD_QA.json').write_text(json.dumps(qa,indent=2),encoding='utf-8')
print(json.dumps(qa))
