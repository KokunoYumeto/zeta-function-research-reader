from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent
manifest = json.loads((ROOT/'sources'/'SOURCE_MANIFEST.json').read_text(encoding='utf-8'))
for entry in manifest['files']:
    path = ROOT / entry['path']
    if hashlib.sha256(path.read_bytes()).hexdigest() != entry['sha256']:
        raise RuntimeError('Source or evidence hash mismatch: ' + entry['path'])
for name in ['MCF.tex','MW.tex','MRE.tex','SP.tex','BC.tex','AW.tex','MARKED_PRODUCT_ORIGINAL_NOTE.tex']:
    if not (ROOT/'sources'/name).is_file():
        raise RuntimeError('Required complete proof source missing: ' + name)

PREAMBLE = r"""\documentclass[11pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage{lmodern,amsmath,amssymb,amsthm,mathtools,mathrsfs}
\usepackage[margin=18mm]{geometry}
\usepackage[bookmarks=false]{hyperref}
\hypersetup{colorlinks=true,linkcolor=blue,urlcolor=blue}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{remark}[theorem]{Remark}
\allowdisplaybreaks
\setlength{\emergencystretch}{6em}
\title{Continuing the Deligne programme over the marked $\tau$ base\\
Complete mixed-support, extension, boundary and source-control calculations}
\author{}
\date{13 September 2026}
\begin{document}
\maketitle
\section*{Reading scope and retained dependencies}
This reader contains the complete calculation bodies MCF, MW, MRE, SP,
BC and the earlier AW calculation, followed by the complete mathematical body of the original
marked-product continuation. Read the accompanying \texttt{PROMPT.md}
for the continuation task and \texttt{DELIGNE\_USAGE\_OVERVIEW.md} for the
source-grounded assessment of the Deligne machinery used so far.
The local \texttt{sources} directory preserves exact source copies and
their SHA256 manifest; the \texttt{evidence} directory preserves the
independent reviews and finite checks.

The inherited theta range and packet identities AG and CAU, their original
spaces and Euler inverses, and the cited Deligne statements remain named
inputs at their stated types. The new proofs retain those inputs and
construct their displayed maps explicitly. This document does not claim
to contain a proof of RH or a completed general six-operation formalism
for the marked support category. It gives calculations from which that
programme continues, including the actual mixed faces, their source
attachments, the singular boundary family, and its finite analytic forms.

The arbitrary length-two algebra in MRE is an explicit extension
calculation. Its use does not assert that an actual zero of $2\xi$ has
multiplicity two. The centered spectral nilpotent filtration and the
boundary inertia filtration are related only by maps constructed at
their specified types; their notation alone supplies no identification.

\paragraph{Exact attribution and correspondence with the earlier AW calculation.}
The earlier AW1--AW23 source is included in full below. Its AW7 already
proves the two complete window spectra, and AW14 already proves the
bound $(2q-1)\log\kappa$ together with the stronger full-spectrum
expression AW13. The corresponding spectra and final bound in SP
reproduce those earlier results. The overlap and common-range refinement
SP8--SP10 supplies additional control alongside AW13.

Here is the exact identification on the retained objects. Write
$u_{\rm AW}$ for AW's integration frequency, $t$ for its interpolation
parameter, and $y,x$ for the respective SP variables. Put
$y=u_{\rm AW}$ and $x=t$, retaining the deformation parameter $u$ of BC
as its independently defined parameter. Both sources are
$H=\mathcal P_{2q}$ with $S=k/2+iy$ and the same monic $\chi$.
Original equation (47) gives
\[
 r_{1/4}^{*k}(y)
  =\frac{c_{1/4}^{\,k}}{c_{k/4}}r_{k/4}(y)
  =\frac{(\sqrt{2\pi})^k}{c_{k/4}}
     \frac{|\Gamma(k/4+iy/2)|^2}{2\pi},
 \qquad c_{1/4}=\sqrt{2\pi}.
\]
Thus AW's $m_0,m_1$ are the same reference and arithmetic densities
used in SP, including their masses. Integration of the unchanged
monomial products gives
\[
 M_{\rm AW}(t)=M_{\rm SP}(x),\qquad
 M_{N,\rm AW}=I_N^*M_{\rm SP}I_N,\qquad
 B_{N,\rm SP}=I_N B_{N,\rm AW}.
\]
Substitution of these identities into AW4 and SP2 proves equality
of their source projections $P_N$ and relation projections $Q_N$.
The zero relation space gives $Q_{q-1}=0$ on both sides. Therefore
their actual endomorphisms satisfy
\[
 \begin{aligned}
 \mathcal R_{\rm SP}
 &=Q_{2q-1}+Q_{2q}-Q_q
   =(Q_{2q-1}-Q_{q-1})+(Q_{2q}-Q_q)=U_{\rm AW},\\
 \mathcal P_{\rm SP}
 &=(P_{2q-1}-P_{q-1})+(P_{2q}-P_q)=W_{\rm AW},\\
 T_{\rm SP}&=M_x^{-1}(M_1-M_0)=C_{\rm AW}(t).
 \end{aligned}
\]
AW's separately constructed isometry, denoted $T_{\rm AW}^{\rm iso}$
here, retains the exact relations
\[
 (T_{\rm AW}^{\rm iso})^*M_xT_{\rm AW}^{\rm iso}=M_x,
 \qquad
 \mathcal R_{\rm SP}
   =T_{\rm AW}^{\rm iso}\mathcal P_{\rm SP}
                (T_{\rm AW}^{\rm iso})^{-1}.
\]
It follows by cyclicity of the original finite trace that
\[
 \operatorname{Tr}((\mathcal R_{\rm SP}-\mathcal P_{\rm SP})T_{\rm SP})
  =\operatorname{Tr}\bigl(\mathcal P_{\rm SP}
       (T_{\rm AW}^{\rm iso})^{-1}[T_{\rm SP},T_{\rm AW}^{\rm iso}]\bigr),
\]
which is AW11 at the displayed original types. This records both
operators and their exact relation without assigning the isometry's
role to the metric derivative. The complete AW source also preserves
its cohomology observation and defect, and its $q=1$ refinements.
At MW10, the combined arithmetic and coefficient action is
$T_{a,q}=A_a\Psi_q$: on the stated $\Psi_q$-eigenspace its graded
eigenvalue is $\omega a^\rho$. This names that product explicitly;
the independently typed $T_{\rm AW}^{\rm iso}$ and $T_{\rm SP}$ retain
their definitions above. The original MW and SP source bodies are
preserved without alteration.

\tableofcontents
\clearpage
"""

ERRATA = r"""\clearpage
\appendix
\section*{Original marked-product note: literal source and reading corrections}
\addcontentsline{toc}{section}{Original marked-product note and literal corrections}
The following appendix preserves the complete original body, including
its abstract and scope statements. Only its document wrapper,
\verb|\maketitle| and \verb|\tableofcontents| controls are removed here.
The separate \texttt{MARKED\_PRODUCT\_ORIGINAL\_NOTE.tex} is byte exact.
The original frequency symbol is $y$ in $S=k/2+iy$; the deformation
parameter is $u$. In the original analytic displays, the measure
written $du$ after defining a density in $y$ is read as $dy$, and the
frequency arguments written $c+iu$ are read as $c+iy$.
These are distinct original variables, and this correction does not
specialize or replace either one.

The sentence following original equation (64) overstates positivity
of the relative derivative. For the literal positive source Grams
$M(0)$ and $M(1)$, the identities
\[
 M(0)\bigl(M(0)^{-1}M(1)\bigr)=M(1),\qquad
 M(0)\bigl(M(0)^{-1}(M(1)-M(0))\bigr)=M(1)-M(0)
\]
prove that the first endomorphism is positive and self-adjoint in the
$M(0)$ metric and that the second is self-adjoint. The second need
not be positive: when $M(1)=M(0)/2$, it equals $-I/2$.
Its original operator norm and the resulting midpoint enclosure
remain meaningful without the extra positivity assertion.

The two nonnegative source/relation operators whose densities occur
in the signed four-endpoint cancellation each have trace $2q$.
Their rank is $q+1$, with spectrum $1,2,\ldots,2,1$ on their range
(the multiplicity of $2$ is $q-1$). The earlier AW7 proves this from the
actual nested source and relation projections; SP6--SP8 reproduce
that spectrum on the identical operators proved above. Thus a kernel mass
$2q$ is read as that trace, not as rank $2q$. The complete exact
cancellation is retained in SP1--SP13. Its final bound is the earlier
AW14, whose full-spectrum refinement AW13 is also included; the
additional overlap and common-range refinement is SP8--SP10.

\begin{center}\large
The marked $\tau$-base, weight-matched external products,\\
and the signed arithmetic four-endpoint correction
\end{center}
"""

parts=[PREAMBLE]
insertions=[]
for name in ['MCF.tex','MW.tex','MRE.tex','SP.tex']:
    body=(ROOT/'sources'/name).read_text(encoding='utf-8-sig')
    if r'\begin{document}' in body or r'\end{document}' in body:
        raise RuntimeError('Proof fragment unexpectedly includes a document wrapper: '+name)
    parts += ['\n% BEGIN EXACT PROOF BODY: '+name+'\n', body, '\n% END EXACT PROOF BODY: '+name+'\n\\clearpage\n']
    insertions.append({'source':'sources/'+name,'body_sha256_lf':hashlib.sha256(body.encode()).hexdigest(),'transformation':'UTF-8 decode and universal newline conversion only; mathematical TeX body unchanged'})
boundary=(ROOT/'sources'/'BC.tex').read_text(encoding='utf-8-sig')
if boundary.count(r'\begin{document}')!=1 or boundary.count(r'\end{document}')!=1:
    raise RuntimeError('Unexpected boundary source document boundaries')
bc_preamble,body=boundary.split(r'\begin{document}',1)
body=body.split(r'\end{document}',1)[0]
if body.count(r'\maketitle')!=1:
    raise RuntimeError('Unexpected boundary title display count')
body=body.replace(r'\maketitle','',1)
body=re.sub(r'\\(label|ref|eqref)\{([^}]+)\}',lambda match:'\\'+match[1]+'{BC:'+match[2]+'}',body)
macro_lines=[line for line in bc_preamble.splitlines() if line.startswith(r'\newcommand') or line.startswith(r'\DeclareMathOperator')]
parts[0]=parts[0].replace(r'\begin{document}', '\n'.join(macro_lines)+'\n'+r'\begin{document}',1)
parts += ['\n% BEGIN COMPLETE BOUNDARY SOURCE BODY\n\\begingroup\n',
          r'\renewcommand{\theequation}{BC\arabic{equation}}'+'\n',
          r'\renewcommand{\theHequation}{BC.\arabic{equation}}'+'\n',
          r'\setcounter{equation}{0}'+'\n',
          r'\section*{The original marked product at its boundary}'+'\n',
          r'\addcontentsline{toc}{section}{The original marked product at its boundary}'+'\n',
          body,'\n\\endgroup\n% END COMPLETE BOUNDARY SOURCE BODY\n\\clearpage\n']
insertions.append({'source':'sources/BC.tex','body_sha256_lf':hashlib.sha256(body.encode()).hexdigest(),'transformation':'Keep complete document body except maketitle; common article preamble supplies packages and theorem environments and retains every original source macro declaration; prefix every label/ref/eqref with BC: and printed automatic equation numbers with BC. No mathematical proof or prose is omitted.'})
aw=(ROOT/'sources'/'AW.tex').read_text(encoding='utf-8-sig')
if aw.count(r'\begin{document}')!=1 or aw.count(r'\end{document}')!=1:
    raise RuntimeError('Unexpected AW document boundaries')
aw_preamble,body=aw.split(r'\begin{document}',1)
body=body.split(r'\end{document}',1)[0]
if body.count(r'\maketitle')!=1:
    raise RuntimeError('Unexpected AW title display count')
body=body.replace(r'\maketitle','',1)
aw_macros=[line for line in aw_preamble.splitlines() if line.startswith(r'\newcommand')]
if aw_macros != [r'\newcommand{\C}{\mathbb C}',r'\newcommand{\Tr}{\operatorname{Tr}}',r'\newcommand{\cP}{\mathcal P}']:
    raise RuntimeError('Unexpected AW macro declarations: inspect collisions before assembly')
parts[0]=parts[0].replace(r'\begin{document}',r'\newcommand{\cP}{\mathcal P}'+'\n'+r'\begin{document}',1)
parts += ['\n% BEGIN COMPLETE EARLIER AW SOURCE BODY\n',
          r'\section*{Earlier AW calculation: the exact relation-window spectrum}'+'\n',
          r'\addcontentsline{toc}{section}{Earlier AW calculation: the exact relation-window spectrum}'+'\n',
          body,'\n% END COMPLETE EARLIER AW SOURCE BODY\n\\clearpage\n']
insertions.append({'source':'sources/AW.tex','body_sha256_lf':hashlib.sha256(body.encode()).hexdigest(),'transformation':'Keep complete original document body except maketitle. Common preamble imports cP; its existing C has the identical definition, and its declared Tr is the same math operator as the original operatorname{Tr}. All original proof prose and displays are unchanged.'})
original=(ROOT/'sources'/'MARKED_PRODUCT_ORIGINAL_NOTE.tex').read_text(encoding='utf-8-sig')
if original.count(r'\begin{document}')!=1 or original.count(r'\end{document}')!=1:
    raise RuntimeError('Unexpected original document boundaries')
body=original.split(r'\begin{document}',1)[1].split(r'\end{document}',1)[0]
for control in [r'\maketitle',r'\tableofcontents']:
    if body.count(control)!=1:
        raise RuntimeError('Unexpected original display control count: '+control)
    body=body.replace(control,'',1)
parts += [ERRATA,'\n% BEGIN COMPLETE ORIGINAL NOTE BODY\n',body,'\n% END COMPLETE ORIGINAL NOTE BODY\n',r'\end{document}'+'\n']
insertions.append({'source':'sources/MARKED_PRODUCT_ORIGINAL_NOTE.tex','body_sha256_lf':hashlib.sha256(body.encode()).hexdigest(),'transformation':'Keep complete document body, remove only maketitle and tableofcontents display controls; original preamble is supplied by the common reader. No mathematical or prose corrections are silently applied.'})
result=''.join(parts)
for prohibited in [r'\input{',r'\include{']:
    if prohibited in result:
        raise RuntimeError('Reader must be flattened: '+prohibited)
destination=ROOT/'COMPLETE_CONTROL_WORK.tex'
destination.write_text(result,encoding='utf-8',newline='\n')
receipt={'sha256':hashlib.sha256(destination.read_bytes()).hexdigest(),'bytes':destination.stat().st_size,'lines':len(result.splitlines()),'standalone_latex_source':True,'complete_bodies':insertions}
(ROOT/'evidence'/'READER_ASSEMBLY.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
