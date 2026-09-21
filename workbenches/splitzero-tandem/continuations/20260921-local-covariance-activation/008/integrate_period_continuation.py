from pathlib import Path
from collections import Counter
import hashlib,json,re
B=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
old=B/'public_factor_receiver_060/FABLE_TO_ORIGINAL_CONDUCTOR.tex'
assert sha(old)=='f73d37ad11289410d9c760aed99f0171bfdeae96d6b14e3886f6ca7cf1eee284'
t=old.read_text(encoding='utf-8')
ofm=B/'ORIGINAL_FACTOR_MOMENT_BODY.tex'
oldbody=ofm.read_text(encoding='utf-8')
credit='''The finite four-factor test and the bound $v\\le32$ were already
proved in the programme source PZ12 \\cite{PeriodZeroOriginal}. The
calculation here retains that source's credit, evaluates its exact
conjugate-period and weighted-factor returns, and uses them in the
marked receiver below.

'''
# Preserve the original proof while correcting its earlier-result attribution.
if credit not in oldbody:
    body=oldbody.replace('\\subsection{Every factor coefficient',credit+'\\subsection{Every factor coefficient',1)
    assert oldbody in t
    t=t.replace(oldbody,body,1)
    ofm.write_text(body,encoding='utf-8')
else:
    frozenbody=oldbody.replace(credit,'',1)
    assert frozenbody in t
    t=t.replace(frozenbody,oldbody,1)
t=t.replace('OFM1--4 below uses the four original quadratic factors to prove the\nstronger bound $32$ displayed here, with a complete finite coefficient\nmap.',
'''The earlier PZ12 calculation \\cite{PeriodZeroOriginal}, reproduced
with its finite coefficient map in OFM1--4 below, gives the stronger
bound $32$ displayed here.''')
cjr=(B/'independent/COMPLEX_RECEIVER_JETS.tex').read_text(encoding='utf-8')
cjr=cjr.split('\\begin{document}\\maketitle',1)[1].split('\\begin{thebibliography}',1)[0]
cjr=re.sub(r'\\R\b',lambda _:r'\mathbb R',cjr)
cjr=re.sub(r'\\C\b',lambda _:r'\mathbb C',cjr)
cjr=cjr.replace('\\cite{FC,ARR}','\\cite{ES488,WCF}').replace('\\cite{EQR}','\\cite{ES488,WCF}')
cjr='\\section{All complex centres of the actual real-period receiver}\n'+cjr
(B/'COMPLEX_RECEIVER_BODY.tex').write_text(cjr,encoding='utf-8')
names=['independent/ORIGINAL_PERIOD_BOUNDARY.tex','PERIOD_INVERSE_BODY.tex','COMPLEX_RECEIVER_BODY.tex']
marker=r'\section{Visual atlas of the exact correspondence}'
assert t.count(marker)==1
t=t.replace(marker,'\n'+'\n'.join((B/n).read_text(encoding='utf-8') for n in names)+'\n'+marker)
t=t.replace('{figures_factor_receiver_060/}{./}','{figures_factor_receiver_060/}{figures_period_continuation/}{./}')
figures=r'''
\clearpage
\section{The complete period-boundary and complex-centre calculation}
\begin{figure}[p]\centering
\includegraphics[width=\linewidth]{25_original_period_inverse.png}
\caption{The exact original $D=3$ inverse singular orders and every
exterior order, PIN1--14. Each displayed growth order has its full
nonzero constant in the proof. The actual real-unit phase is stated;
the finite original period remains invertible on PZU4's evaluated
domain. Both Gamma norms and the original centres are retained.
Sources: \cite{ES488,WCF,DLMF18Source,PeriodZeroOriginal}.}
\end{figure}
\begin{figure}[p]\centering
\includegraphics[width=\linewidth]{26_complex_receiver_region.png}
\caption{The exact excluded complex-centre region for real admitted
periods, CJR1--25 and CJR17a. Heights are symbolic; the drawing assigns
no numerical values to the original quartet or period. It shows the
$D\ne0$ case of CJR10; this $D$ is the determinant parameter, not
the polynomial cutoff. Every degenerate case and its full kernel are
proved in CJR14--18 and CJR24. The actual moments, not freely chosen
vectors, decide the residual tests. Sources: \cite{ES488,WCF}.}
\end{figure}
\begin{figure}[p]\centering
\includegraphics[width=\linewidth]{27_original_boundary_branches.png}
\caption{The two exact lower coefficient edges and all four nearby
zero branches of each original real-unit factor, OPB9--18. Coordinates
are exponents of the original variables, not new physical coordinates.
The complete coefficient formula and convergent remainders are retained.
The complete boundary phase classification is OPB5--6a,14,23.
Sources: \cite{ES488,PCLOriginal,PeriodZeroOriginal}.}
\end{figure}
'''
t=t.replace(r'\begin{thebibliography}',figures+'\n'+r'\begin{thebibliography}',1)
bib=r'''
\bibitem{PeriodZeroOriginal} Supplied Split-Zero programme,
\emph{An evaluated original-period domain with zero conductor vanishing
order; the two exceptional unit phases; universal period receivers},
\texttt{PERIOD\_ZERO\_COMPLETE\_PROOF.tex}, source collection
17 September 2026, PZ1--13, PZX1--6 and PZU1--11.
No individual byline is supplied in this programme proof fragment.
Exact source SHA-256:
\texttt{cbb4108de647f61af1e49deeeff46de97593eb9bfa9a6a33705dea344df3ec19}.
The unchanged complete source is included with the dependencies.
PZ12 already proves the four-factor order bound and moment test;
PZX supplies both inverse-period leading coefficients, and PZU the
finite zero-free period domain. These prior results are credited
at their use and are not claimed as new results of this continuation.
'''
t=t.replace(r'\end{thebibliography}',bib+'\n'+r'\end{thebibliography}',1)
tags=re.findall(r'\\tag\{([^}]+)\}',t)
assert all(n==1 for n in Counter(tags).values())
assert not re.search(r'[A-Z]:[\\/](?:Users|user)[\\/]',t)
(B/'FABLE_TO_ORIGINAL_CONDUCTOR.tex').write_text(t,encoding='utf-8')
receipt={'result_id':'SZ-20260920-061','frozen060_sha256':sha(old),'principal_sha256':sha(B/'FABLE_TO_ORIGINAL_CONDUCTOR.tex'),
 'new_sources':{n:sha(B/n) for n in names},'unique_tags':len(tags),'figures':t.count(r'\includegraphics'),
 'prior_result_credit':'PZ12 credited for order bound32 and finite test, PZ/PZX/PZU for phase loci and finite-period domain.'}
(B/'PERIOD_CONTINUATION_INTEGRATION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
