"""Integrate the accepted directional proof from the immutable real-pair edition."""
from pathlib import Path
from collections import Counter
import hashlib, json, re, subprocess

B=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
base=B/'public_real_pair_20260921_005/FABLE_TO_ORIGINAL_CONDUCTOR.tex'
assert sha(base)=='557988797c9143543b951dff10338ce8ce8bba412bba458ff71c059dec428662'
check=json.loads((B/'independent/REAL_PAIR_DIRECTIONAL_GEOMETRY_CHECK.json').read_text(encoding='utf-8'))
proof=B/'independent/REAL_PAIR_DIRECTIONAL_GEOMETRY.tex'
assert check['status']=='PASS'
assert check['source_sha256'][proof.name]==sha(proof)
assert check['checker_sha256']==sha(B/'independent/check_real_pair_directional_geometry.py')
assert check['root_certificate_sha256']==sha(B/'REAL_PAIR_CERTIFICATE.json')
body=proof.read_text(encoding='utf-8')+'\n'+(B/'REAL_PAIR_DIRECTION_CERTIFICATE_BODY.tex').read_text(encoding='utf-8')
title='The original real conductor: every resonance direction and the complete pole transition'
intro=r'''Result SZ-20260921-006, the directional continuation
RPD1--31 (including RPD12a), constructs
the exact real derivative isomorphism at the certified RPZ point,
all resonance lines at every cutoff, and the full transition when a
path turns toward such a line.  It retains the actual order-two
quotient, every Gamma weight and center, and the curvature introduced
by the original period coordinate.  The complete preceding certified
root and four-label return are included in this cumulative source.

'''
t=base.read_text(encoding='utf-8')
verified=json.loads((B/'PROGRAMME_CITATION_TARGETS_006.json').read_text(encoding='utf-8'))['verified_targets']
bibadd=''
for item in verified:
    bibadd+=(r'\bibitem{'+item['bibkey']+'} Split-Zero programme, result SZ-20260921-005, '
             +r'\nolinkurl{'+item['file']+'}, '+item['locator_tex']+'. '
             +r'\href{'+item['url']+'}{Pinned complete public proof: '+item['locator_tex']+'}.\n')
t=t.replace(r'\end{thebibliography}',bibadd+r'\end{thebibliography}')
marker=r'\section{Visual atlas of the exact correspondence}'
assert t.count(marker)==1
t=t.replace(marker,body+'\n'+marker)
t=t.replace('{figures_real_pair_005/}{./}','{figures_real_pair_005/}{figures_real_pair_direction/}{./}')
t=t.replace(r'\section{Four points, including the coordinates hidden by local symmetry}',intro+r'\section{Four points, including the coordinates hidden by local symmetry}',1)
figure=r'''
\clearpage
\begin{figure}[p]\centering
\includegraphics[width=\linewidth]{37_real_pair_directional_geometry.png}
\caption{RPD3--5 gives the exact original real derivative and its complete
quadratic form; RPD20--22 constructs every resonance line.  Three
degree-three representatives and their antipodal rays are displayed
at the midpoints of the enclosing intervals in RPD31.  The left axes
have different scales; the middle panel is the image under the exact
derivative, not an asserted isometry.  RPD23--30 proves the complete
curved-path pole transition and original-period correction.  The plot
records tangent geometry, not a finite spectral zero curve.  Full
original family and metric: \cite{PCLOriginal,WCF}; inclusion
arithmetic: Fredrik Johansson \cite{human:arb2016}.}
\end{figure}
'''
t=t.replace(r'\begin{thebibliography}',figure+'\n'+r'\begin{thebibliography}',1)
tags=re.findall(r'\\tag\{([^}]+)\}',t);assert all(n==1 for n in Counter(tags).values())
(B/'FABLE_TO_ORIGINAL_CONDUCTOR.tex').write_text(t,encoding='utf-8')

prior=(B/'REAL_PAIR_005.tex').read_text(encoding='utf-8')
preamble=prior.split(r'\begin{document}',1)[0]
preamble=re.sub(r'\\title\{[^\n]+\}',lambda m:r'\title{'+title+'}',preamble)
preamble=preamble.replace('{figures_real_pair_005/}{./}','{figures_real_pair_005/}{figures_real_pair_direction/}{./}')
start=r'''\begin{document}\maketitle
\noindent Result SZ-20260921-006 supplies the complete RPD1--31 proof,
including RPD12a.  The complete earlier certified-root and four-label
proofs accompany it in \nolinkurl{REAL_PAIR_005.tex}, its readable
PDF, and \nolinkurl{FABLE_TO_ORIGINAL_CONDUCTOR.tex}.
The original-source citations below identify the precise public
providers.  Every claim concerns the specified geometric family.
\tableofcontents\clearpage
'''
used={k for m in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',body+figure) for k in m.split(',')}
bibpart=t.split(r'\begin{thebibliography}',1)[1].split(r'\end{thebibliography}',1)[0]
items={key:block for block,key in re.findall(r'(\\bibitem\{([^}]+)\}[\s\S]*?)(?=\\bibitem\{|\Z)',bibpart)}
assert not used-items.keys()
landscape=figure.replace(r'\begin{figure}[p]',r'\begin{landscape}\begin{figure}[p]').replace(r'\end{figure}',r'\end{figure}\end{landscape}\clearpage').replace(r'width=\linewidth',r'width=.94\linewidth')
reader=preamble+start+body+landscape+'\n'+r'\begin{thebibliography}{99}'+'\n'+''.join(items[k] for k in sorted(used))+r'\end{thebibliography}'+'\n'+r'\end{document}'+'\n'
(B/'REAL_PAIR_DIRECTIONAL_CONTINUATION.tex').write_text(reader,encoding='utf-8')
O=B/'output/pdf';O.mkdir(exist_ok=True,parents=True)
draft=B/'texcheck_real_pair_direction';draft.mkdir(exist_ok=True)
runs=[]
for name,is_draft,destination in [('REAL_PAIR_DIRECTIONAL_CONTINUATION.tex',False,O),('FABLE_TO_ORIGINAL_CONDUCTOR.tex',True,draft)]:
    passes=[]
    for k in [1,2]:
        cmd=['pdflatex','-interaction=nonstopmode','-halt-on-error','-output-directory='+str(destination)]
        if is_draft:cmd.append('-draftmode')
        p=subprocess.run(cmd+[name],cwd=B,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=180)
        (destination/f'{Path(name).stem}_pass{k}.txt').write_bytes(p.stdout)
        assert p.returncode==0,p.stdout[-5000:]
        passes.append({'pass':k,'exit_code':p.returncode})
    log=(destination/(Path(name).stem+'.log')).read_text(encoding='utf-8',errors='replace')
    missing=re.findall(r'LaTeX Warning: (?:Citation|Reference).*undefined',log)
    assert not missing,missing
    runs.append({'file':name,'sha256':sha(B/name),'passes':passes,'overfull_boxes':log.count('Overfull'),
                 'unresolved_citations_or_references':missing,'duplicate_destinations':log.count('destination with the same identifier')})
receipt={'result_id':'SZ-20260921-006','base_frozen005_sha256':sha(base),'principal_sha256':sha(B/'FABLE_TO_ORIGINAL_CONDUCTOR.tex'),
 'proof_sha256':sha(proof),'appendix_sha256':sha(B/'REAL_PAIR_DIRECTION_CERTIFICATE_BODY.tex'),
 'reader_source_sha256':sha(B/'REAL_PAIR_DIRECTIONAL_CONTINUATION.tex'),
 'pdf_sha256':sha(O/'REAL_PAIR_DIRECTIONAL_CONTINUATION.pdf'),
 'unique_tags':len(tags),'figures':t.count(r'\includegraphics'),'runs':runs,
 'visual_review':'Pending rendered page inspection.'}
(B/'REAL_PAIR_DIRECTION_INTEGRATION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
