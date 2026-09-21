from pathlib import Path
from collections import Counter
import hashlib,json,re
B=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
old=B/'public_finite_period_064/FABLE_TO_ORIGINAL_CONDUCTOR.tex'
assert sha(old)=='4ed4495de25947a7f02c714f10b89b86cc3590da6ab794e167371751b6a2c4b1'
t=old.read_text(encoding='utf-8')
names=['independent/ARBITRARY_UNIT_NONCONSTANCY.tex','UNIT_PHASE_PERSISTENCE_BODY.tex','GLOBAL_UNIT_CONDUCTOR_BODY.tex','independent/GLOBAL_CONDUCTOR_ZERO_CONSEQUENCE.tex']
marker=r'\section{Visual atlas of the exact correspondence}'
assert t.count(marker)==1
t=t.replace(marker,'\n'.join((B/n).read_text(encoding='utf-8') for n in names)+'\n'+marker)
t=t.replace(r'\date{20 September 2026}',r'\date{21 September 2026}',1)
t=t.replace('{figures_finite_period_064/}{./}','{figures_finite_period_064/}{figures_unit_phase_20260921/}{./}')
intro=r'''
Result SZ-20260921-001 extends the finite-period construction to the
complete original unit family. ANP1--32 proves nonconstancy and existence
of nonzero finite complex zeros for every original quartet and unit,
with all coefficient and exact elimination tables. UPP1--20 certifies
a moving simple-zero graph in an explicit complex phase disk, proves
its nonzero tangent and gives the complete original weighted inverse
exterior constants both along period variation and along phase variation
at the fixed certified period. The full four-label ES correction and
augmented return persist. Global zero existence alone asserts neither
five-orbit admissibility nor order one at each guaranteed zero.
GUC1--5 nevertheless proves that every original quartet and unit has
a finite complex-period singularity of the actual fixed old conductor,
with divergence of every inverse exterior rank and its exact top
exterior pole, without assuming either of those additional properties.
GFC1--21 gives the complete finite minor-derivative construction of
every exact exterior pole and constant, and exhausts all possible
symbol orders, including identically vanishing symbols.

'''
t=t.replace(r'\section{Four points, including the coordinates hidden by local symmetry}',intro+r'\section{Four points, including the coordinates hidden by local symmetry}',1)
figures=r'''
\clearpage
\section{The certified unit-phase graph and global finite-zero argument}
\begin{figure}[p]\centering
\includegraphics[width=\linewidth]{32_unit_phase_graph.png}
\caption{The exact certified period disk and tangent direction, UPP1--16.
The arrow length is a display choice and does not depict the root curve.
The marker represents the enclosed base root. The full original unit,
all four factors and the Gamma metrics are retained. Arithmetic source:
Fredrik Johansson \cite{human:arb2016}; original period: \cite{PCLOriginal}.}
\end{figure}
\begin{figure}[p]\centering
\includegraphics[width=\linewidth]{33_unit_global_and_exterior.png}
\caption{ANP1--32 proves finite nonzero factor zeros on the whole original
unit domain. UPP17--20 proves the two transverse inverse-exterior limits
in the certified region, including all original weighted constants.
The global existence result alone supplies no assertion about the
symbol order or five-orbit locus at each zero. Original ES marking and
human sources: \cite{ES488}; Gamma metric: \cite{WCF,DLMF18Source}.}
\end{figure}
'''
t=t.replace(r'\begin{thebibliography}',figures+'\n'+r'\begin{thebibliography}',1)
tags=re.findall(r'\\tag\{([^}]+)\}',t)
assert all(n==1 for n in Counter(tags).values())
cites={k for m in re.findall(r'\\cite\{([^}]+)\}',t) for k in m.split(',')}
bibs=set(re.findall(r'\\bibitem\{([^}]+)\}',t));assert not cites-bibs,cites-bibs
assert not re.search(r'[A-Z]:[\\/](?:Users|user)[\\/]',t)
(B/'FABLE_TO_ORIGINAL_CONDUCTOR.tex').write_text(t,encoding='utf-8')
out={'result_id':'SZ-20260921-001','frozen064_sha256':sha(old),
     'principal_sha256':sha(B/'FABLE_TO_ORIGINAL_CONDUCTOR.tex'),
     'new_sources':{n:sha(B/n) for n in names},'unique_tags':len(tags),'figures':t.count(r'\includegraphics')}
(B/'UNIT_PHASE_001_INTEGRATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
