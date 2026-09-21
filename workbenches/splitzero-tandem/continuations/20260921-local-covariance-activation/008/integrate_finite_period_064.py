from pathlib import Path
from collections import Counter
import hashlib,json,re
B=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
old=B/'public_period_complex_061/FABLE_TO_ORIGINAL_CONDUCTOR.tex'
assert sha(old)=='8739afeab8d76ebfa4fc5d15d8e8486d8da923beff8675a212cbbda61e00cc18'
t=old.read_text(encoding='utf-8')
def standalone_body(path,title,replacements):
    v=(B/path).read_text(encoding='utf-8').split(r'\begin{document}\maketitle',1)[1].split(r'\begin{thebibliography}',1)[0]
    for a,b in replacements.items():v=v.replace(a,b)
    return '\\section{'+title+'}\n'+v
prd=standalone_body('independent/ACTUAL_PERIOD_RECEIVER_DISCRIMINANT.tex',
 'The actual period receiver excludes every repeated complex root near infinite period',
 {r'\cite{CJR}':r'\cite{ComplexReceiver061}',r'\cite{PIN}':r'\cite{PeriodInverse061}',
  r'\cite{PCL}':r'\cite{PCLOriginal}',r'\cite{PZ}':r'\cite{PeriodZeroOriginal}',
  r'\cite{FC,EQR}':r'\cite{ES488,WCF}',r'\cite{FC}':r'\cite{ES488,WCF}'})
fsr=standalone_body('independent/FINITE_SINGULAR_ES_RETURN.tex',
 'The complete four-label return at the finite singular period',
 {r'\cite{FinitePeriod}':r'\cite{FinitePeriod064}',r'\cite{FC,WCF}':r'\cite{ES488,WCF}'})
(B/'ACTUAL_PERIOD_RECEIVER_BODY.tex').write_text(prd,encoding='utf-8')
(B/'FINITE_SINGULAR_ES_RETURN_BODY.tex').write_text(fsr,encoding='utf-8')
names=['independent/FINITE_PERIOD_UNIT_TEST.tex','ACTUAL_PERIOD_RECEIVER_BODY.tex',
       'FINITE_PERIOD_ZERO_BODY.tex','FINITE_SINGULAR_ES_RETURN_BODY.tex']
marker=r'\section{Visual atlas of the exact correspondence}'
assert t.count(marker)==1
t=t.replace(marker,'\n'+'\n'.join((B/n).read_text(encoding='utf-8') for n in names)+'\n'+marker)
intro=r'''
The finite-period continuation now constructs a rigorously enclosed complex
period in the original geometric coefficient family with symbol order one.
FPZ1--26 gives the exact point, all omitted-series bounds, the five-prime
orbit proof and every inverse exterior pole in the original Gamma metrics.
FSR1--24 gives the complete four-label return, the nonzero obstruction to
discarding the lost scalar, its exact restoration and the actual-order
correction. FUT1--26 proves a unit-uniform real-period exclusion near
infinite period and supplies the coefficient needed for the general
finite-complex-zero theorem. PRD1--30 evaluates the actual period moments
and excludes every repeated receiver root in its proved period region.
These statements concern the specified original geometric family.
No arithmetic zeta-zero quartet is identified by the numerical parameter
choice in FPZ1, and no arithmetic RH conclusion is asserted.

'''
t=t.replace(r'\section{Four points, including the coordinates hidden by local symmetry}',intro+r'\section{Four points, including the coordinates hidden by local symmetry}',1)
t=t.replace('{figures_period_continuation/}{./}','{figures_period_continuation/}{figures_finite_period_064/}{./}')
captions=[
 ('28_certified_finite_period','The unique simple finite inverse-period zero, FPZ1--14. Both infinite tails and every displayed strict bound are certified. The disk uses the exact rational centre in FPZ4. The full point belongs to the specified geometric family, with no assertion that its quartet consists of zeta zeros. Original coefficients: \\cite{PCLOriginal}; inclusion arithmetic: Fredrik Johansson \\cite{human:arb2016}.'),
 ('29_finite_inverse_exterior','The finite rank loss in the fixed old four-dimensional spaces, FPZ15--24. One inverse singular value has pole four and all four inverse exterior ranks have pole four. Every constant uses the original moments, centres and Gamma weights. The actual order-one quotient is also explicitly retained. Original Gamma measure and human sources: \\cite{WCF,DLMF18Source}.'),
 ('30_actual_receiver_roots','All three actual receiver branches, PRD1--30. The displayed coordinate is the explicitly inverted affine map X/h minus 2; every original scalar and moment remains in the proof. PRD14 supplies the proved period radius. These boundary roots are simple and exclude every repeated complex-centre candidate in that region. Original coefficient and Gamma sources: \\cite{PCLOriginal,WCF,ES488}.'),
 ('31_singular_four_labels','The exact three-dimensional zero-mean label space at the singular conductor, FSR4--20. The three displayed coordinates are an orthonormal chart of the real label hyperplane, with its inverse printed. They do not replace the original complex Gamma metric, whose full scalar cross term is FSR20. All four M,N,T,E marks remain distinct; the completed return also retains their lost scalar. Canonical marked construction and human attribution: \\cite{ES488}.')]
figures='\n\\clearpage\n\\section{The finite-period certificate and complete singular return}\n'
for n,c in captions:figures+='\\begin{figure}[p]\\centering\n\\includegraphics[width=\\linewidth]{'+n+'.png}\n\\caption{'+c+'}\n\\end{figure}\n'
t=t.replace(r'\begin{thebibliography}',figures+'\n'+r'\begin{thebibliography}',1)
bib=r'''
\bibitem{human:arb2016} Fredrik Johansson,
\emph{Arb: Efficient Arbitrary-Precision Midpoint-Radius Interval Arithmetic},
original author source, arXiv:1611.02831v1 (9 November 2016),
\url{https://arxiv.org/abs/1611.02831v1}.
Source sections ``Features and example applications'', ``Radii and
magnitude bounds'' and ``Precision and bounds'' support the stated
inclusion arithmetic. The complete FPZ series-tail and zero-count proofs
are given here; they are not attributed to the software paper.
\bibitem{FinitePeriod064} Supplied Split-Zero programme,
\emph{A certified finite geometric period with an order-one conductor symbol},
FPZ1--26 in this cumulative source; complete reproducible calculation
\texttt{certify\_finite\_period\_zero.py} and
\texttt{FINITE\_PERIOD\_ZERO\_CERTIFICATE.json}.
Independent mathematical review FPR1--32 is supplied separately.
\bibitem{PeriodInverse061} Supplied Split-Zero programme,
\emph{The exact four singular losses at the infinite-period boundary},
\texttt{PERIOD\_INVERSE\_BODY.tex}, PIN1--14, result SZ-20260920-061.
\bibitem{ComplexReceiver061} Supplied Split-Zero programme,
\emph{The complete complex-centre jet map of the original real-period receiver},
\texttt{COMPLEX\_RECEIVER\_JETS.tex}, CJR1--25 and CJR17a,
result SZ-20260920-061.
'''
t=t.replace(r'\end{thebibliography}',bib+'\n'+r'\end{thebibliography}',1)
tags=re.findall(r'\\tag\{([^}]+)\}',t)
assert all(n==1 for n in Counter(tags).values())
assert not re.search(r'[A-Z]:[\\/](?:Users|user)[\\/]',t)
cites=set(k for m in re.findall(r'\\cite\{([^}]+)\}',t) for k in m.split(','))
bibs=set(re.findall(r'\\bibitem\{([^}]+)\}',t));assert not cites-bibs,cites-bibs
(B/'FABLE_TO_ORIGINAL_CONDUCTOR.tex').write_text(t,encoding='utf-8')
out={'result_id':'SZ-20260920-064','frozen061_sha256':sha(old),
     'principal_sha256':sha(B/'FABLE_TO_ORIGINAL_CONDUCTOR.tex'),
     'new_sources':{n:sha(B/n) for n in names},'unique_tags':len(tags),'figures':t.count(r'\includegraphics')}
(B/'FINITE_PERIOD_064_INTEGRATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
