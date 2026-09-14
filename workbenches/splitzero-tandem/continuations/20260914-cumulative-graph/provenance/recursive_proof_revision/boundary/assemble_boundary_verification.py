from pathlib import Path
import hashlib, json, re
ROOT=Path(r'workspace:')
OUT=ROOT/'work/backpropagation_20260913/boundary'
def sha(b):return hashlib.sha256(b).hexdigest()
source=ROOT/'work/marked_product_boundary_connection_20260913.tex'
b=source.read_bytes(); assert sha(b)=='6575b8e33ff00bef8b08e214b974b9bd1e966c3bed4b573c5ca274206a69e9fa'
txt=b.decode('utf-8-sig').replace('\r\n','\n')
update=(OUT/'staging/boundary/fragments/bc_single_primary_update.tex').read_text(encoding='utf-8').replace('\r\n','\n')
(OUT/'fragments/bc_single_primary_update.tex').write_text(update,encoding='utf-8')
start=txt.index('\\section{What follows in the programme}')
end=txt.index('\\section*{Source and verification record}',start)
revised=txt[:start]+update+'\n\n'+txt[end:]
old_scope='Neither a Stokes matrix nor an arithmetic uniform four-volume estimate is\nasserted.  The calculations identify and begin the intervening boundary\nwork rather than declaring the marked programme closed.'
new_scope='The exact single-primary branch now also includes its full period\nmatrix, boundary monodromy, finite cover, source-unit maps and finite-field\ncharacter decomposition. The general multi-primary sector transitions\nand original arithmetic uniform four-volume estimate remain continuing\ncalculations on the retained objects.'
assert revised.count(old_scope)==1
revised=revised.replace(old_scope,new_scope)
(OUT/'revised/tex/marked_product_boundary_connection.tex').write_text(revised,encoding='utf-8')
body=revised[revised.index('\\maketitle')+len('\\maketitle'):revised.rindex('\\end{document}')]
macros=r'''
\begingroup
\def\Tr{\operatorname{Tr}}
\def\coker{\operatorname{coker}}
\def\Spec{\operatorname{Spec}}
\def\rem{\operatorname{rem}}
\def\diag{\operatorname{diag}}
\def\C{\mathbb C}\def\F{\mathbb F}\def\A{\mathbb A}
\def\Gm{{\mathbb G_m}}\def\HH{\mathcal H}\def\BB{\mathscr B}
'''
(OUT/'proofs/BC_CURRENT_FRAGMENT.tex').write_text(macros+body+'\n\\endgroup\n',encoding='utf-8')
src=ROOT/'work/rh_counterfactual_20260913/total_object/tensor_primary_boundary_control.tex'
b=src.read_bytes(); assert sha(b)=='692b5fe8b3434974df0a38ff905d5d1bd456ffba3374c508cfed84df47d61f88'
(OUT/'proofs/TENSOR_ORIGINAL.tex').write_bytes(b)
files=['deligne_split_sidebar','deligne_exponential_determinant_extension','deligne_translation_bridge','sga_constituent_period_curvature','period_critical_kernel_bridge','period_laplacian_control_bridge','circle_critical_observation_diamond','residue_constituent_extension']
preamble=r'''\documentclass[11pt,a4paper]{article}
\usepackage[margin=24mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,mathrsfs,longtable,booktabs,array}
\usepackage[unicode,breaklinks=true]{hyperref}
\usepackage{xurl}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}\newtheorem{definition}[theorem]{Definition}
\newtheorem{example}[theorem]{Example}
\theoremstyle{remark}\newtheorem{remark}[theorem]{Remark}
\providecommand{\ran}{\operatorname{ran}}
\providecommand{\rank}{\operatorname{rank}}
\providecommand{\diag}{\operatorname{diag}}
\providecommand{\id}{\operatorname{id}}
\providecommand{\Tr}{\operatorname{Tr}}
\allowdisplaybreaks
\setlength{\emergencystretch}{3em}
\title{Boundary back-propagation verification: complete affected proof bodies}
\author{}\date{13 September 2026}
\begin{document}\maketitle
This verification reader includes complete revised earlier chapters and
the complete authoritative boundary proofs. Historical originals and
all exact edits are retained beside this source. References to other
chapters retain their identifiers for reintegration into the full book.
'''
master=preamble+'\n'.join('\\input{revised/tex/'+f+'.tex}' for f in files)
master+='\n\\input{proofs/BC_CURRENT_FRAGMENT.tex}\n\\input{proofs/SPC_ORIGINAL.tex}\n\\input{proofs/TENSOR_ORIGINAL.tex}\n\\end{document}\n'
(OUT/'BOUNDARY_VERIFICATION.tex').write_text(master,encoding='utf-8')
print(json.dumps(dict(bc_current_sha256=sha(revised.encode()),tensor_sha256=sha(b),master=str(OUT/'BOUNDARY_VERIFICATION.tex')),indent=2))
