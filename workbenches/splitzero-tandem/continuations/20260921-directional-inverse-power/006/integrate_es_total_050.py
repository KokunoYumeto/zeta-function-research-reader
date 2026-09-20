from pathlib import Path
from collections import Counter
import re,hashlib,json
B=Path(__file__).resolve().parent
old=B/'public_global_residue_042/FABLE_TO_ORIGINAL_CONDUCTOR.tex'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(old)=='4283c3ff215112f239403104a038abeb29c64ce60ae2f60184b9989957b408c7'
root=B/'ES_COEFFICIENT_TOTAL_EXTENSION_BODY.tex'
review=B/'independent/ES_TOTAL_EXTENSION_REVIEW.tex'
t=old.read_text(encoding='utf-8')
marker=r'\section{Visual atlas of the exact correspondence}'
assert t.count(marker)==1
t=t.replace(marker,root.read_text(encoding='utf-8')+'\n'+review.read_text(encoding='utf-8')+'\n'+marker)
t=t.replace('{figures_global_residue/}{./}','{figures_global_residue/}{figures_es_total/}{./}')
received=B/'defining_prime_intake_20260920/DEFINING_PRIME_RECEIVED.md'
fig=r'''
\clearpage
\section{The whole signed-cover coefficient comparison}
\begin{figure}[p]
\centering\includegraphics[width=\linewidth]{19_es_total_coefficient_extension.png}
\caption{An exact symbolic diagram of ET1--39, not a plot of arithmetic
zeta zeros. The three coefficient directions retain every one of the
eight signed basis directions; they are not labelled as twenty-four
distinct geometric points. ET13--15 proves the full inclusion, its
quotient, its conductor ideal and its specialized Tor sequence.
ET16--22 gives every root and sign action, all commutation maps, and
the eight length-three residue chains. ET23--36 returns the complete
inverse through the fixed original source and target, evaluates all
finite singular values and every exterior norm with the original
moments and Gamma factors present. ET37--39 gives a finite two-sided
bound in every exterior degree. Independent proofs are ETR1--31.
Immediate coefficient source: \cite[eqs.\ (3)--(8)]{DefiningPrimeReceived}.
Original human polynomial and ES provenance: \cite{Tao,ES488};
the original Gamma dictionary is retained in FC20--24 and RS21--26.}
\end{figure}
'''
t=t.replace(r'\begin{thebibliography}',fig+'\n'+r'\begin{thebibliography}',1)
bib=r'''\bibitem{DefiningPrimeReceived} Received AI-generated web calculation,
\emph{The ES bridge at the defining prime of an actual Erdos--Straus witness},
20 September 2026, complete supplied account, equations (1)--(47).
No human author name was supplied.
Original received SHA-256: \texttt{'''+sha(received)+r'''}.
The whole account was read. Its coefficient proposal (3)--(8) is
proved and extended here in ET1--39 to the complete signed cover and
the full original-conductor inverse-exterior cost.
Its separate integral-prime, gluing, and covariance assertions are not
adopted merely by this citation. Their exact review status is recorded
in the source-use ledger.
'''
t=t.replace(r'\end{thebibliography}',bib+'\n'+r'\end{thebibliography}',1)
tags=re.findall(r'\\tag\{([^}]+)\}',t)
dups=[k for k,v in Counter(tags).items() if v>1]
assert not dups,dups
(B/'FABLE_TO_ORIGINAL_CONDUCTOR.tex').write_text(t,encoding='utf-8')
receipt={'result_id':'SZ-20260920-050','prior_principal':sha(old),'principal':sha(B/'FABLE_TO_ORIGINAL_CONDUCTOR.tex'),'root_source':sha(root),'review_source':sha(review),'unique_tags':len(tags),'figures':t.count(r'\includegraphics'),'frozen042_unchanged':sha(old)}
(B/'ES_TOTAL_050_INTEGRATION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))

