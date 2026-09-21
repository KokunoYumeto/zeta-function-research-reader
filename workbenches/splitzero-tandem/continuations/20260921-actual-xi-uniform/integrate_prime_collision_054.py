from pathlib import Path
from collections import Counter
import hashlib,json,re
B=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
old=B/'public_es_total_050/FABLE_TO_ORIGINAL_CONDUCTOR.tex'
assert sha(old)=='efb34b95a4f99b1848eea9ce7f4c285aabd49a806b074cfd51a1fe11f07ee46d'
names=['PRIME_SPECIALIZATION_BODY.tex','independent/INTEGRAL_SIGNED_REVIEW.tex',
 'POSITIVE_ES_BOUNDARY_BODY.tex','independent/POSITIVE_ES_STRATA_REVIEW.tex',
 'independent/ES_COLLISION_COMPLETE.tex','ORIGINAL_COLLISION_QUOTIENT_BODY.tex']
pieces=[]
for name in names:
    t=(B/name).read_text(encoding='utf-8')
    if name.endswith('ES_COLLISION_COMPLETE.tex'):
        t=t[t.index(r'\section{Scope, source, and original objects}'):t.index(r'\begin{thebibliography}')]
        for oldkey,newkey in [('Received','DefiningPrimeReceived'),('Programme','Fable050'),('ES','ES488'),('Gamma','DLMF18Source')]:
            t=re.sub(r'(\\cite(?:\[[^]]*\])?\{)'+oldkey+r'(\})',lambda m:m[1]+newkey+m[2],t)
    pieces.append(t)
intro=r'''
\section{Defining-prime and collision continuation: domains and strengthened conclusions}
The following complete proofs extend the coefficient result ET1--39.
PS and ISR calculate the exact arithmetic comparison, including the
fractional chart when $p\mid S$. PB and PES then use positivity:
the one-divisible gap satisfies $n\le1$, and every actual two-divisible
witness has $n=1$. The higher gap formulas in PS16 and ISR16--17 are
retained as general algebraic calculations; PB1--8 proves that they
create no exception to the coefficient-ideal inclusion for an actual
positive witness on the original $p\nmid S$ chart.
ECC retains the complete original signed collision and both original
metrics. OCQ computes the actual original conductor on their quotient:
its four inverse singular values have finite limits, and each inverse
exterior norm is bounded by that of the unchanged original conductor.
These domains and conclusions strengthen the earlier comparison without
asserting that a local algebra conductor is the original linear operator.
'''
t=old.read_text(encoding='utf-8')
marker=r'\section{Visual atlas of the exact correspondence}'
assert t.count(marker)==1
t=t.replace(marker,intro+'\n'+'\n'.join(pieces)+'\n'+marker)
t=t.replace('{figures_es_total/}{./}','{figures_es_total/}{figures_prime_collision/}{./}')
t=t.replace(r'\begin{document}',r'\providecommand{\Res}{\operatorname{Res}}'+'\n'+r'\begin{document}',1)
fig=r'''
\clearpage
\section{The defining prime and the original collision quotient}
\begin{figure}[p]
\centering\includegraphics[width=\linewidth]{20_prime_and_original_collision.png}
\caption{Exact symbolic diagram of the full arithmetic inclusion and the
actual original collision quotient. PS6--25 and ISR1--34 retain all eight
signed arithmetic directions, every unit and every inclusion entry.
PB1--8 and PES1--12 impose the original positivity constraint; the
one-divisible valuation-one stratum is permitted by the proved bound,
not asserted to occur. The integral-ideal statement assumes $p\nmid S$;
the different fractional chart and its exact twist are ISR18--23.
ECC31--43 calculates the raw signed covariance and trace losses in each
original metric. The displayed four states are the colliding block of
the complete eight-state algebra, whose complementary block is retained
in ECC11. OCQ1--11 proves that the same raw-to-jet change acts at both
receivers, gives every finite inverse singular value of the induced
original conductor, and proves its exterior bound by the unchanged
original conductor inverse. The image is not a zeta-zero trajectory.
Human sources at use: \cite{ES488,Tao,DLMF18Source,JouveRV}; immediate
received proposal: \cite{DefiningPrimeReceived}.}
\end{figure}
'''
t=t.replace(r'\begin{thebibliography}',fig+'\n'+r'\begin{thebibliography}',1)
bib=r'''
\bibitem{Fable050} Split-Zero programme,
\emph{The ES--Fable inverse correspondence in the original weighted
conductor}, complete preceding source, 20 September 2026,
programme result SZ-20260920-050. Principal SHA-256:
\texttt{efb34b95a4f99b1848eea9ce7f4c285aabd49a806b074cfd51a1fe11f07ee46d}.
All of its proofs and human-source citations remain in this cumulative
edition; ECC uses FC20--32, RD1--15, RS21--25 and GD14--17.
'''
t=t.replace(r'\end{thebibliography}',bib+'\n'+r'\end{thebibliography}',1)
t=t.replace('Its separate integral-prime, gluing, and covariance assertions are not\nadopted merely by this citation. Their exact review status is recorded\nin the source-use ledger.',
'''Its integral-prime, gluing, collision and covariance assertions are now
proved with the stated corrections in PS1--25, ISR1--34, ECC1--48,
PB1--8 and PES1--12. OCQ1--11 additionally proves the actual original
quotient-conductor comparison. Exact source reading and derivation
coverage are recorded in the source-use ledger.''')
tags=re.findall(r'\\tag\{([^}]+)\}',t)
duplicates=[a for a,n in Counter(tags).items() if n>1]
assert not duplicates,duplicates
(B/'FABLE_TO_ORIGINAL_CONDUCTOR.tex').write_text(t,encoding='utf-8')
out={'result_id':'SZ-20260920-054','frozen050_sha256':sha(old),
 'principal_sha256':sha(B/'FABLE_TO_ORIGINAL_CONDUCTOR.tex'),
 'new_sources':{name:sha(B/name) for name in names},'unique_tags':len(tags),
 'figures':t.count(r'\includegraphics'),'scope':'Complete original defining-prime, positivity, signed collision and actual quotient-conductor proofs. Goal remains active.'}
(B/'PRIME_COLLISION_054_INTEGRATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
