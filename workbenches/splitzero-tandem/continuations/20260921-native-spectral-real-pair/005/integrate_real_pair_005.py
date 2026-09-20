from pathlib import Path
from collections import Counter
import hashlib,json,re
B=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
old=B/'public_unit_phase_20260921_001/FABLE_TO_ORIGINAL_CONDUCTOR.tex'
assert sha(old)=='b74569fdcfa3dd01125943a340cac09efae90c63b4dd072a82f807c91b4c8330'
t=old.read_text(encoding='utf-8')
names=['REAL_PAIR_ZERO_BODY.tex','independent/REAL_PAIR_COLLISION.tex','independent/REAL_PAIR_ES_RETURN.tex']
allcut=B/'independent/REAL_PAIR_ALL_CUTOFFS.tex'
if allcut.exists():
    assert (B/'independent/REAL_PAIR_ALL_CUTOFFS_CHECK.json').exists()
    names.append(str(allcut.relative_to(B)).replace('\\','/'))
marker=r'\section{Visual atlas of the exact correspondence}'
assert t.count(marker)==1
t=t.replace(marker,'\n'.join((B/n).read_text(encoding='utf-8') for n in names)+'\n'+marker)
t=t.replace('{figures_unit_phase_20260921/}{./}','{figures_unit_phase_20260921/}{figures_real_pair_005/}{./}')
intro=r'''
Result SZ-20260921-005 constructs an actual positive real period of
the complete original geometric family. RPZ1--19 proves existence
and uniqueness from a two-real-variable contraction with all infinite
tails enclosed. Exactly the first and fourth factors vanish; the
period multiplicity and symbol order are both two. RPCJ1--23 and
RPE1--26 calculate the original inverse singular poles $(5,3,0,0)$,
all four inverse exterior poles $(5,8,8,8)$, and every original
weighted leading constant in degree three. They retain all four
distinct old ES outputs, calculate the exact order-two source map,
and recover both lost scalar coordinates with their entire original
metric and cross terms. The earlier OFM conjugation and positivity
are credited as prior results. The real-period member is geometric;
no identification with the restricted arithmetic zeta locus is made.

'''
if allcut.exists():
    intro+=r'''RPAC1--15 calculates every original cutoff, including the
complete resonance equation and both possible inverse spectra. The
full enclosing certificate proves nonresonance for each cutoff
$1\le D\le100$; all higher cutoffs retain the exact formulas.

'''
t=t.replace(r'\section{Four points, including the coordinates hidden by local symmetry}',intro+r'\section{Four points, including the coordinates hidden by local symmetry}',1)
figs=r'''
\clearpage
\section{The positive real pair and the complete four-label correction}
\begin{figure}[p]\centering
\includegraphics[width=\linewidth]{34_real_pair_certificate.png}
\caption{The exact real rectangle RPZ4 contains one zero of the complete
original factor, by RPZ5--14. The center marker is not the exact root.
The axes are display offsets with the full inverse coordinate rule.
The original unit and both conjugate pairs are retained; RPZ15--19
proves their exact orders. Original period: \cite{PCLOriginal}.
Inclusion arithmetic: Fredrik Johansson \cite{human:arb2016}.}
\end{figure}
\begin{figure}[p]\centering
\includegraphics[width=\linewidth]{35_real_pair_inverse_return.png}
\caption{RPCJ14--23 and RPE5--9 calculate the actual original
Gamma-metric poles and every constant. RPE10--26 retains four
distinct marks, the two lost old coordinates, their inverse and
all source metric cross terms, as well as the actual order-two
quotient. The displayed spaces are different exact domains of the
same original conductor. ES marking: \cite{ES488}; original
Gamma dictionary and human authors: \cite{WCF,DLMF18Source}.}
\end{figure}
'''
if allcut.exists():
    figs+=r'''
\begin{figure}[p]\centering
\includegraphics[width=\linewidth]{36_real_pair_all_cutoffs.png}
\caption{RPAC1--14 proves the complete original-cutoff inverse law and
both exact resonance alternatives, with all original moments and
weights. RPAC15 rigorously excludes resonance at every integer
cutoff from 1 through 100 for the actual certified real pair; the
lines join those integer exponents. It makes no all-degree
nonresonance assertion. Original construction: \cite{PCLOriginal,WCF};
inclusion arithmetic: Fredrik Johansson \cite{human:arb2016}.}
\end{figure}
'''
t=t.replace(r'\begin{thebibliography}',figs+'\n'+r'\begin{thebibliography}',1)
links=B/'PROGRAMME_CITATION_TARGETS_005.json'
if links.exists():
    for v in json.loads(links.read_text(encoding='utf-8'))['verified_targets']:
        key=v['bibkey'];start=t.index(r'\bibitem{'+key+'}')
        end=t.find(r'\bibitem{',start+1)
        if end<0:end=t.index(r'\end{thebibliography}',start)
        addition='\n'+r'\href{'+v['url']+'}{Pinned public proof: '+v['locator_tex']+'}.\n'
        t=t[:end]+addition+t[end:]
for key,addition in {
    'Cumulative':r''' The exact accepted source is included as
\nolinkurl{source_dependencies/ACCEPTED_782_CUMULATIVE.tex}.
Its DFX4--5 occur at lines 30623--30633 and CNC1--2 at
38157--38178. No live public link to this exact source edition
is asserted before publication of the included file.''',
    'ES488':r''' The complete original version-69 author source,
with the stated hash and byline, is included as
\nolinkurl{source_dependencies/ES_READER_V69.tex}.''',
    'PeriodZeroOriginal':r''' The full exact provider is included as
\nolinkurl{source_dependencies/PERIOD_ZERO_COMPLETE_PROOF.tex};
no unverified public target is substituted for that source.'''
}.items():
    start=t.index(r'\bibitem{'+key+'}');end=t.find(r'\bibitem{',start+1)
    if end<0:end=t.index(r'\end{thebibliography}',start)
    t=t[:end]+addition+'\n'+t[end:]
# Keep the formal supplied derivation and its provenance; private conversational
# intake is retained locally, not carried in the new public source archive.
t=t.replace(r'\texttt{Fable\_Conductor\_Continuation\_20260920/PROOF.md}',
            r'\texttt{source\_intake/PROOF.md}')
t=t.replace('The original incoming file and exact source hash are retained in this edition.',
            'The complete supplied mathematical derivation and its exact source hash are retained in this edition; private correspondence is retained separately.')
t=t.replace(r'''20 September 2026. The complete unchanged incoming source is retained as
\texttt{source\_intake/INCOMING.md} in this edition's source archive.
No author name was supplied.''',r'''20 September 2026. The original correspondence is retained privately.
The complete public derivation of the inputs used here is given in
AR1--23 of this cumulative source. It is a derivation, not a republication
of the correspondence. No author name was supplied.''')
tags=re.findall(r'\\tag\{([^}]+)\}',t)
assert all(n==1 for n in Counter(tags).values()),[k for k,v in Counter(tags).items() if v>1]
cites={k for m in re.findall(r'\\cite\{([^}]+)\}',t) for k in m.split(',')}
bibs=set(re.findall(r'\\bibitem\{([^}]+)\}',t));assert not cites-bibs,cites-bibs
assert not re.search(r'[A-Z]:[\\/](?:Users|user)[\\/]',t)
(B/'FABLE_TO_ORIGINAL_CONDUCTOR.tex').write_text(t,encoding='utf-8')
out={'result_id':'SZ-20260921-005','frozen001_sha256':sha(old),
     'principal_sha256':sha(B/'FABLE_TO_ORIGINAL_CONDUCTOR.tex'),
     'new_sources':{n:sha(B/n) for n in names},'unique_tags':len(tags),'figures':t.count(r'\includegraphics'),
     'citation_target_map':sha(links) if links.exists() else None}
(B/'REAL_PAIR_005_INTEGRATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
