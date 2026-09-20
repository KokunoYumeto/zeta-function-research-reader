from pathlib import Path
from collections import Counter
import hashlib,json,re
B=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
old=B/'public_prime_collision_054/FABLE_TO_ORIGINAL_CONDUCTOR.tex'
assert sha(old)=='14a5912f55f4749780bbe5a8904419aab1ad3687044a1f7458924a3e23918861'
names=['independent/POSITIVE_ONE_DIVISIBLE_EXTENSION.tex','SIGNED_ORIGINAL_RETURN_BODY.tex','ESCAPE_QUOTIENT_RETURN_BODY.tex']
t=old.read_text(encoding='utf-8')
replacements={
r'''fractional chart when $p\mid S$. PB and PES then use positivity:
the one-divisible gap satisfies $n\le1$, and every actual two-divisible
witness has $n=1$.''':r'''fractional chart when $p\mid S$. PB and PES first use positivity;
OE1--8 now proves that every actual positive witness has $p\nmid S$
and that its one-divisible unit gap has $n=0$. Every actual two-divisible
witness has clustered gap $n=1$. The fractional chart remains a formal
algebraic extension, not an additional actual positive-witness case.''',
r'''inclusion. For $p\mid S$ the original coefficient columns are the
fractional lattice of ISR18--23, so PES8 is not incorrectly stated
as an inclusion of an undefined original integral order.''':r'''inclusion. OE1--8 below now excludes $p\mid S$ for every actual
positive witness, so the inclusion applies to the entire stated class.
ISR18--23 retains the formal fractional-lattice calculation outside it.''',
r'''\subsection{Exact parameters for the remaining two bounded questions}
The proofs above do not establish that the remaining one-divisible
case $n=1$ is realizable or impossible, and do not prove that $p\mid S$
is impossible. The following exact derivation constrains both questions.''':r'''\subsection{Exact parameters used to exclude the two residue events}
The following complete parameter derivation is retained. The positivity
argument alone left its two residue events open; OE1--8 below now
excludes both by quadratic reciprocity, using these same identities.''',
'The two still possible residue events have exact tests':'The two residue events, both excluded by OE7--8, have the exact tests',
'''These are exact necessary conditions and a finite-search parametrization;
neither event is excluded merely because a bounded search finds none.''':'''These exact parameter tests are inputs to OE1--8. Their exclusion
comes from its universal Jacobi-symbol argument, independently of any
finite enumeration.''',
r'''PB1--8 and PES1--12 impose the original positivity constraint; the
one-divisible valuation-one stratum is permitted by the proved bound,
not asserted to occur. The integral-ideal statement assumes $p\nmid S$;
the different fractional chart and its exact twist are ISR18--23.''':r'''OE1--18 strengthens PB1--8 and PES1--12: the two unit denominators
have opposite quadratic characters. The one-divisible valuation-one
event and $p\mid S$ are both impossible for actual positive witnesses.
The updated diagram therefore has exactly the two actual arithmetic
strata. ISR18--23 remains a formal extension beyond this witness class.''',
'20_prime_and_original_collision.png':'20_prime_and_original_collision_current.png',
'{figures_prime_collision/}{./}':'{figures_prime_collision/}{figures_reciprocity_057/}{./}',
}
for a,b in replacements.items():
    assert a in t,a[:150]
    t=t.replace(a,b)
intro=r'''
\section{Reciprocity, signed arithmetic defects, and the full nonlinear quotient}
OE1--18 closes the previously remaining positive Type I residue cases:
the two unit denominators have opposite quadratic characters. Both
the unit-gap coincidence and the nonintegral-leading-coefficient case
are excluded for every actual positive witness. All earlier larger
formal strata are retained with this explicit restriction.
SGR1--15 calculates every signed integral defect, the complete
sign-invariant suborder, the full affine-state return and every original
metric singular value. Its common rational model proves the exact
arithmetic-to-complex base-change relation. EQR1--13 evaluates all
nonlinear escape cases on the original collision quotient and returns
every complementary direction with both complete original norms.
The rational sign involution has a pole in every fixed quotient of
this form. The original conductor retains its established finite
inverse-exterior bounds; no original leading-moment zero is inferred
from the poles of the separately calculated nonlinear maps.
'''
marker=r'\section{Visual atlas of the exact correspondence}'
assert t.count(marker)==1
t=t.replace(marker,intro+'\n'+'\n'.join((B/n).read_text(encoding='utf-8') for n in names)+'\n'+marker)
figs=r'''
\clearpage
\section{The exact signed arithmetic and nonlinear returns}
\begin{figure}[p]
\centering\includegraphics[width=\linewidth]{21_signed_arithmetic_original_metrics.png}
\caption{Exact arithmetic clusters and the complete original-metric
return, OE7--18 and SGR1--15. Positions in the upper boxes encode
residue-cluster membership, not a Euclidean metric. The cyclic
intersection defects retain their complete original generators in
SGR2--3. SGR15 gives their common rational model and both base changes.
The lower curve is the proved universal function of the actual
original-metric scalar $\nu$, not a sampled original spectrum.
SGR9--12 gives every singular value and every exterior norm.
Human sources at use: \cite{ElsholtzTao2015,ES488,Tao,WCF}.}
\end{figure}
\begin{figure}[p]
\centering\includegraphics[width=\linewidth]{22_nonlinear_escape_complete_quotient.png}
\caption{Complete case diagram for the original nonlinear states on
ECC44, proved in EQR1--13. Every row retains both roots and both signs.
The exact fixed original receiver decides the displayed jet tests;
no exceptional arithmetic period is asserted to exist from this diagram.
EQR3--4 gives the complete inverse and both attained original norms.
If the quotient is bounded, its nonzero escaping complement is EQR12.
The cancelling pair's next coefficient is the nonzero quantity in
EQR10. The separate rational sign-involution pole is evaluated exactly
in EQR13. Original polynomial and metric sources: \cite{ES488,Tao,WCF}.}
\end{figure}
'''
t=t.replace(r'\begin{thebibliography}',figs+'\n'+r'\begin{thebibliography}',1)
bib=r'''
\bibitem{ElsholtzTao2015} Christian Elsholtz and Terence Tao,
\emph{Counting the number of solutions to the Erd\H{o}s--Straus
equation on unit fractions}, Journal of the Australian Mathematical
Society \textbf{94} (2013), 50--105. Original author-source edition:
\href{https://arxiv.org/abs/1107.1010v6}{arXiv:1107.1010v6},
2 August 2015; \href{https://arxiv.org/src/1107.1010v6}{original TeX archive}.
OE1--8 uses Section~2, Proposition \texttt{type-1}, equations
\texttt{I-1}, \texttt{I-2}, \texttt{I-6}, \texttt{I-7},
and the displayed \texttt{quadratic} and \texttt{quadratic-2} laws.
The printed exponent in \texttt{quadratic-1} is explicitly corrected
and its corrected Jacobi extension proved in OE3; the author source
is preserved unchanged. Original TeX SHA-256:
\texttt{b0469a67a737b7f4e77778310c87e22f5783ae9704f70aa55919a4a40104611c}.
'''
t=t.replace(r'\end{thebibliography}',bib+'\n'+r'\end{thebibliography}',1)
tags=re.findall(r'\\tag\{([^}]+)\}',t)
assert all(n==1 for n in Counter(tags).values())
(B/'FABLE_TO_ORIGINAL_CONDUCTOR.tex').write_text(t,encoding='utf-8')
out={'result_id':'SZ-20260920-057','frozen054_sha256':sha(old),
 'principal_sha256':sha(B/'FABLE_TO_ORIGINAL_CONDUCTOR.tex'),
 'new_sources':{n:sha(B/n) for n in names},'unique_tags':len(tags),
 'figures':t.count(r'\includegraphics'),'current_scope':'Complete OE, SGR and EQR proofs; exclusive goal remains active.'}
(B/'RECIPROCITY_SIGNED_057_INTEGRATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
