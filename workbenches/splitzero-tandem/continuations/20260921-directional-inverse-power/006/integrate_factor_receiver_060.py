from pathlib import Path
from collections import Counter
import hashlib,json,re
B=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
old=B/'public_reciprocity_signed_057/FABLE_TO_ORIGINAL_CONDUCTOR.tex'
assert sha(old)=='5cc3eec96eb573678246ae209803290fe6cf5f2aefdbcc3608eb077b2c4ac4e1'
names=['ORIGINAL_FACTOR_MOMENT_BODY.tex','ACTUAL_REAL_RECEIVER_BODY.tex','independent/SIGNED_LOCAL_FIELDS.tex']
t=old.read_text(encoding='utf-8')
changes={
 r'v=\ord_0E_A\le80,\qquad\mu_v\ne0.':r'v=\ord_0E_A\le32,\qquad\mu_v\ne0.',
 '''The order bound follows again from the $81$ distinct exponents and their
first $81$ derivative matrix. It is not a numerical lower bound for the
first nonzero derivative.''':'''The $81$ distinct exponents first give the coarser bound $80$.
OFM1--4 below uses the four original quadratic factors to prove the
stronger bound $32$ displayed here, with a complete finite coefficient
map. This order bound alone is not a numerical lower bound for the
first nonzero derivative.''',
 r'the same derivative argument gives $v\le r_A-1$.':r'the same derivative argument and OFM4 give $v\le\min(32,r_A-1)$.',
 r'$r_A\le77$ and gives $v\le76$; it does not annihilate the original':r'$r_A\le77$, whose support-only bound $76$ is weaker than OFM4; it does not annihilate the original',
 r'map drops degree by $v\le80$ while the grid-degree difference is':r'map drops degree by $v\le32$ (OFM4) while the grid-degree difference is',
 r'''and this family makes no assertion of integral witnesses for arbitrary
$t$. Fix $P\ne0$.''':r'''and this family makes no assertion of integral witnesses for arbitrary
$t$. Fix $P\ne0$. The complete complex-domain classification is retained.
ARR1--12 below additionally evaluates the actual moments on real admitted
periods and proves that only EQR6 occurs when $P$ is real.''',
 '{figures_reciprocity_057/}{./}':'{figures_reciprocity_057/}{figures_factor_receiver_060/}{./}',
 '''no exceptional arithmetic period is asserted to exist from this diagram.
EQR3--4''':'''no exceptional arithmetic period is asserted to exist from this diagram.
ARR1--12 further excludes all bounded rows for real admitted periods
with real collision centre. EQR3--4'''
}
for a,b in changes.items():assert a in t,a[:120];t=t.replace(a,b)
marker=r'\section{Visual atlas of the exact correspondence}'
assert t.count(marker)==1
t=t.replace(marker,'\n'+'\n'.join((B/n).read_text(encoding='utf-8') for n in names)+'\n'+marker)
figs=r'''
\clearpage
\section{The original factor exclusion and the actual local sign action}
\begin{figure}[p]
\centering\includegraphics[width=\linewidth]{23_actual_factor_receiver.png}
\caption{The exact factor-to-receiver calculation, OFM1--17 and ARR1--12.
The individual nine-frequency supports give the complete order bound32.
On real admitted periods the actual moment map has strictly positive
determinant, with all75 rational coefficient bounds printed in ARR7--9.
Thus the first receiving polynomial has no repeated real root, and all
four signed collision states escape in both original quotient norms.
The displayed diagram retains the four factors and both root/sign choices;
it is not a numerical spectrum. Original sources and prior positivity:
\cite{ES488,PCLOriginal,WCF,DLMF18Source}.}
\end{figure}
\begin{figure}[p]
\centering\includegraphics[width=\linewidth]{24_actual_local_galois.png}
\caption{Every actual local Galois sign and its full original-metric
return, SLF1--19. Residue clusters are stated as label sets, without
assigning them a Euclidean geometry. All four Type II rows occur at
the displayed positive witnesses. The lower intersection formula
applies to a nontrivial Type II row; Type I and the split Type II row
preserve the whole original order. The common algebraic model and its
two separate base changes retain the full affine coordinates.
Human and programme sources: \cite{ElsholtzTao2015,ES488,Tao,WCF}.}
\end{figure}
'''
t=t.replace(r'\begin{thebibliography}',figs+'\n'+r'\begin{thebibliography}',1)
bib=r'''
\bibitem{PCLOriginal} Split-Zero programme,
\emph{The literal original conductor limit and an invertible pivot restriction},
\texttt{PCL\_COMPLETE.tex}, PCL1--16. Original supplied programme TeX;
the entire-period coefficient formula and prior positivity slice are
retained and cited at their use in OFM6--11. This is a programme source,
not an attribution of that construction to the classical human sources.
'''
t=t.replace(r'\end{thebibliography}',bib+'\n'+r'\end{thebibliography}',1)
tags=re.findall(r'\\tag\{([^}]+)\}',t);assert all(n==1 for n in Counter(tags).values())
(B/'FABLE_TO_ORIGINAL_CONDUCTOR.tex').write_text(t,encoding='utf-8')
out={'result_id':'SZ-20260920-060','frozen057_sha256':sha(old),
 'principal_sha256':sha(B/'FABLE_TO_ORIGINAL_CONDUCTOR.tex'),
 'new_sources':{n:sha(B/n) for n in names},'unique_tags':len(tags),
 'figures':t.count(r'\includegraphics'),'scope':'OFM1–17, ARR1–12 and SLF1–19; exclusive goal remains active.'}
(B/'FACTOR_RECEIVER_060_INTEGRATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
