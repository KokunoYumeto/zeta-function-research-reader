"""Build the Xi pullback and uniform-rate reader from sealed edition008."""
from pathlib import Path
from collections import Counter
import hashlib,json,re,subprocess
B=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
base=B/'public_real_pair_local_20260921_008/FABLE_TO_ORIGINAL_CONDUCTOR.tex'
assert sha(base)=='ecb3a99bd46da1a1cf116be9ae27d05b022f71d498b2178cc21adec90b3fe973'
proofs=['ALPOGE_FABLE_ROLE.tex','independent/ACTUAL_UNIT_HERMITE_PULLBACK.tex','ACTUAL_XI_CERTIFICATE_BODY.tex',
        'independent/REAL_PAIR_UNIFORM_COEFFICIENTS.tex','REAL_PAIR_CUTOFF_MATRIX.tex']
body='\n'.join((B/n).read_text(encoding='utf-8') for n in proofs)
t=base.read_text(encoding='utf-8')
public008=json.loads((B/'REAL_PAIR_008_REMOTE_RECEIPT.json').read_text(encoding='utf-8'))['verified_targets'][0]['url']
public_rqt=json.loads((B/'REAL_PAIR_008_REMOTE_RECEIPT.json').read_text(encoding='utf-8'))['verified_targets'][1]['url']
bib=r'''\bibitem{AlpogeAnnouncement} Levent Alp\"oge,
original announcement of the explicit three-dimensional Jacobian
counterexample, 20 July 2026, 02:19:17 UTC,
\url{https://x.com/__alpoge__/status/2079028340955197566}.
The announcement credits Akhil for the question and Fable for the
work leading to the displayed polynomial. The original X syndication
response is retained as
\nolinkurl{source_dependencies/ALPOGE_ORIGINAL_ANNOUNCEMENT_20260720.json}.
The canonical ES reader identifies Akhil Mathew and Claude Fable~5.
Tao's later exposition is cited separately.
\bibitem{RLA008} Split-Zero programme, result SZ-20260921-008,
\emph{The full two-branch local algebra of the actual real pair},
RLA1--35. Complete proof source \texttt{REAL\_PAIR\_LOCAL\_ALGEBRA.tex}
is retained in the accompanying source collection and in this cumulative
edition. Its original certified-point sources are the pinned RPZ and RPD
proofs cited separately.
'''
bib+=r'\href{'+public008+r'}{Pinned complete public proof: RLA1--35}.'+'\n'
bib+=r'''\bibitem{RQT008} Split-Zero programme, result SZ-20260921-008,
\emph{The moving quotient, its exact kernel and the original equation (11)},
RQT1--19, with RQT20--22 in the accompanying angle-constant proof.
'''
bib+=r'\href{'+public_rqt+r'}{Pinned complete public proof: RQT1--19}.'+'\n'
assert r'\bibitem{RLA008}' not in t
t=t.replace(r'\end{thebibliography}',bib+r'\end{thebibliography}')
t=t.replace('Levent Alp\\"oge with credit to Fable; Tao\'s exposition \\cite{Tao}',
            'Levent Alp\\"oge, whose original announcement credits Akhil for the question\n'
            'and Fable for the work \\cite{AlpogeAnnouncement}; Tao\'s exposition \\cite{Tao}')
marker=r'\section{Visual atlas of the exact correspondence}';assert t.count(marker)==1
t=t.replace(marker,body+'\n'+marker)
t=t.replace('{figures_real_pair_local/}{./}','{figures_real_pair_local/}{figures_actual_xi_uniform/}{./}')
intro=r'''Result SZ-20260921-011 constructs the actual Xi-jet pullback with its
full residual, evaluates it at the four certified marks, and proves both
leading inverse singular rates at the original growing Gamma cutoffs.
The local Xi calculation excludes that geometric singular member from
the tested arithmetic graph; it does not prove a global zero exclusion.
ALF1--3, AUH1--30, RXT1--9, RUC1--30 and RCM1--17 give the complete new
derivations, with preceding results retained below.

'''
t=t.replace(r'\section{Four points, including the coordinates hidden by local symmetry}',intro+r'\section{Four points, including the coordinates hidden by local symmetry}',1)
figure39=r'''
\clearpage
\begin{figure}[p]\centering
\includegraphics[width=\linewidth]{39_actual_xi_pullback.png}
\caption{The exact Xi-jet morphism carries the residual $L$ as well as
the quotient values. AUH1--30 proves the maps. RXT1--9 certifies a
positive zeroth moment for the extension over the full original
period interval, and a separate residual exclusion on the stated
quartet rectangle. The latter does not enlarge the domain of the
conductor-factor bounds. The geometric singular point remains the
one proved in \cite{RPZ005}; the original period family is
\cite{PCLOriginal}. Riemann completion and interval arithmetic:
\cite{DLMFXi,human:arb2016}. The originating Jacobian counterexample
is Alp\"oge--Fable \cite{AlpogeAnnouncement}; the four-mark extension
is \cite{ES488}. Box positions are schematic.}
\end{figure}
'''
figure40=r'''
\clearpage
\begin{figure}[p]\centering
\includegraphics[width=\linewidth]{40_uniform_inverse_rates.png}
\caption{RUC1--30 and RCM1--17 retain both actual spectral roots,
the full unit, the analytic remainder and every lower-diagonal
correction. The determinant identity prevents coefficient-phase
cancellation from removing both leading inverse rates. The Gamma
comparison applies at the four original quadratic cutoffs with the
parameter fixed. The principal-part rank mechanism is the earlier
WCF15--18 \cite{WCF}; the full local factorization is RLA6--10
\cite{RLA008}. The originating collision construction is
Alp\"oge--Fable \cite{AlpogeAnnouncement}, with the ES four-mark
extension \cite{ES488}. No numerical root neighborhood is asserted by this
diagram. All constants and quantified neighborhoods are in the proofs.}
\end{figure}
'''
figures=figure39+figure40
t=t.replace(r'\begin{thebibliography}',figures+'\n'+r'\begin{thebibliography}',1)
tags=re.findall(r'\\tag\{([^}]+)\}',t);assert all(v==1 for v in Counter(tags).values())
(B/'FABLE_TO_ORIGINAL_CONDUCTOR.tex').write_text(t,encoding='utf-8')
prior=(B/'REAL_PAIR_LOCAL_OBJECT.tex').read_text(encoding='utf-8')
pre=prior.split(r'\begin{document}',1)[0]
pre=re.sub(r'\\title\{[^\n]+\}',lambda _:r'\title{Actual Xi data and the two conductor inverse rates}',pre)
pre=pre.replace('{figures_real_pair_local/}{./}','{figures_real_pair_local/}{figures_actual_xi_uniform/}{./}')
start=r'''\begin{document}\maketitle
\noindent This calculation continues the transport of the
Alp\"oge--Fable Jacobian counterexample, announced by Levent Alp\"oge
with credit to Akhil and Fable \cite{AlpogeAnnouncement}, through
the ES four-mark extension \cite{ES488} into the original weighted
conductor. Section~\ref{sec:alpoge-fable-role} gives the exact role
and attribution of each construction.

\noindent Result SZ-20260921-011 contains the complete ALF1--3, AUH1--30, RXT1--9,
RUC1--30 and RCM1--17 proofs. The Xi-jet residual is retained,
and the tested quartet is excluded from the actual simple-zero
locus in a certified neighborhood. The conductor extension there
has order zero at every finite cutoff. The separate two-root
geometric calculation gives uniform coefficient bounds and both
inverse singular rates at the original growing Gamma cutoffs.
The complete earlier proofs accompany the cumulative source.
No global arithmetic zero exclusion is claimed.
\tableofcontents\clearpage
'''
used={k for m in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',body+figures) for k in m.split(',')}
part=t.split(r'\begin{thebibliography}',1)[1].split(r'\end{thebibliography}',1)[0]
items={k:block for block,k in re.findall(r'(\\bibitem\{([^}]+)\}[\s\S]*?)(?=\\bibitem\{|\Z)',part)}
assert not used-items.keys(),used-items.keys()
landscape=figures.replace(r'\begin{figure}[p]',r'\begin{landscape}\begin{figure}[p]').replace(r'\end{figure}',r'\end{figure}\end{landscape}\clearpage').replace(r'width=\linewidth',r'width=.94\linewidth')
reader=pre+start+body+landscape+r'\begin{thebibliography}{99}'+'\n'+''.join(items[k] for k in sorted(used))+r'\end{thebibliography}'+'\n'+r'\end{document}'+'\n'
(B/'ACTUAL_XI_UNIFORM_CONDUCTOR.tex').write_text(reader,encoding='utf-8')
out=B/'output/pdf';out.mkdir(exist_ok=True,parents=True)
draft=B/'texcheck_actual_xi_uniform';draft.mkdir(exist_ok=True)
runs=[]
for name,is_draft,dest in [('ACTUAL_XI_UNIFORM_CONDUCTOR.tex',False,out),('FABLE_TO_ORIGINAL_CONDUCTOR.tex',True,draft)]:
    passes=[]
    for k in [1,2]:
        cmd=['pdflatex','-interaction=nonstopmode','-halt-on-error','-output-directory='+str(dest)]
        if is_draft:cmd.append('-draftmode')
        p=subprocess.run(cmd+[name],cwd=B,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=180)
        (dest/f'{Path(name).stem}_pass{k}.txt').write_bytes(p.stdout)
        assert p.returncode==0,p.stdout[-4500:]
        passes.append({'pass':k,'exit_code':0})
    log=(dest/(Path(name).stem+'.log')).read_text(encoding='utf-8',errors='replace')
    missing=re.findall(r'LaTeX Warning: (?:Citation|Reference).*undefined',log);assert not missing,missing
    runs.append({'file':name,'passes':passes,'overfull_boxes':log.count('Overfull'),'unresolved':missing,'duplicate_destinations':log.count('destination with the same identifier')})
receipt={'result_id':'SZ-20260921-011','base_edition':'SZ-20260921-008','base_sha256':sha(base),'principal_sha256':sha(B/'FABLE_TO_ORIGINAL_CONDUCTOR.tex'),
         'proof_sha256':{n:sha(B/n) for n in proofs},'reader_sha256':sha(B/'ACTUAL_XI_UNIFORM_CONDUCTOR.tex'),
         'pdf_sha256':sha(out/'ACTUAL_XI_UNIFORM_CONDUCTOR.pdf'),'tags':len(tags),'figures':t.count(r'\includegraphics'),
         'runs':runs,'visual_review':'pending'}
(B/'ACTUAL_XI_UNIFORM_INTEGRATION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
