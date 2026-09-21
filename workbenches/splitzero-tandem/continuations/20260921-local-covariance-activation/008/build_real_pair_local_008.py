"""Integrate complete local-object proofs from immutable edition006."""
from pathlib import Path
from collections import Counter
import hashlib,json,re,subprocess
B=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
base=B/'public_real_pair_direction_20260921_006/FABLE_TO_ORIGINAL_CONDUCTOR.tex'
assert sha(base)=='ece8b9d31e6ef5c2cb5737dc087ec1da9197ad684c114db3d0e16f6d70b3a9ae'
proofs=['independent/REAL_PAIR_LOCAL_ALGEBRA.tex','REAL_PAIR_MOVING_QUOTIENT.tex','independent/REAL_PAIR_ANGLE_CONSTANTS.tex']
body='\n'.join((B/n).read_text(encoding='utf-8') for n in proofs)
t=base.read_text(encoding='utf-8')
public=json.loads((B/'REAL_PAIR_006_REMOTE_RECEIPT.json').read_text())['verified_targets']
bib=''
for key,entry,loc in [('RPD006',public[0],'RPD1--30 and RPD12a'),('RPD31Source',public[1],'RPD31')]:
    bib+=r'\bibitem{'+key+'} Split-Zero programme, result SZ-20260921-006, '+loc+'. '+r'\href{'+entry['url']+'}{Pinned complete public proof: '+loc+'}.\n'
t=t.replace(r'\end{thebibliography}',bib+r'\end{thebibliography}')
marker=r'\section{Visual atlas of the exact correspondence}';assert t.count(marker)==1
t=t.replace(marker,body+'\n'+marker)
t=t.replace('{figures_real_pair_direction/}{./}','{figures_real_pair_direction/}{figures_real_pair_local/}{./}')
intro=r'''Result SZ-20260921-008 constructs the complete local two-branch
module of the certified geometric member and its exact original-metric
comparison to inverse-exterior equation (11).  RLA1--35 and RQT1--22
retain both original parameters, all analytic units, each actual-order
domain and all four ES states.  The complete preceding proofs remain
in this cumulative source.  The geometric member has not been
identified with arithmetic zeta data.

'''
t=t.replace(r'\section{Four points, including the coordinates hidden by local symmetry}',intro+r'\section{Four points, including the coordinates hidden by local symmetry}',1)
figure=r'''
\clearpage
\begin{figure}[p]\centering
\includegraphics[width=\linewidth]{38_real_pair_local_object.png}
\caption{The two parameter branches are the exact coordinate axes of
RLA6--10; their coupled module, rather than an uncoupled sum, is
RLA14--18.  These are schematic local germs, not a metric drawing or
a certified numerical neighborhood.  The right chart is the actual
real parameter slice through the exact inverse RLA9.  A collision of
nonzero spectral roots does not make $g_0$ vanish.  RQT3--16 constructs
the bottom maps with the original Gamma metric: $T_0$ maps to
orthonormal quotient coordinates $q$, while the alternative coordinate
$w=M^{-1/2}q$ has Gram $M$.  Both angle sines and their full volume
correction are computed exactly.  Original family and metric:
\cite{PCLOriginal,WCF}; certified root: \cite{RPZ005}; complete
directional antecedent: \cite{RPD006}.}
\end{figure}
'''
t=t.replace(r'\begin{thebibliography}',figure+'\n'+r'\begin{thebibliography}',1)
tags=re.findall(r'\\tag\{([^}]+)\}',t);assert all(x==1 for x in Counter(tags).values())
(B/'FABLE_TO_ORIGINAL_CONDUCTOR.tex').write_text(t,encoding='utf-8')
prior=(B/'REAL_PAIR_DIRECTIONAL_CONTINUATION.tex').read_text(encoding='utf-8')
pre=prior.split(r'\begin{document}',1)[0]
pre=re.sub(r'\\title\{[^\n]+\}',lambda _:r'\title{Two local branches and the exact conductor quotient}',pre)
pre=pre.replace('{figures_real_pair_direction/}{./}','{figures_real_pair_direction/}{figures_real_pair_local/}{./}')
start=r'''\begin{document}\maketitle
\noindent Result SZ-20260921-008.  This reader gives the complete
RLA1--35 and RQT1--22 proofs.  The original certified point and
directional proofs are linked at their exact public editions and
included in the accompanying cumulative source and source archive.
All claims concern the stated geometric family.  The notation
$\alpha,\beta$ denotes its two spectral roots; the original unit
scale and quartet constant are explicitly distinguished below.
\tableofcontents\clearpage
'''
used={k for m in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',body+figure) for k in m.split(',')}
part=t.split(r'\begin{thebibliography}',1)[1].split(r'\end{thebibliography}',1)[0]
items={k:block for block,k in re.findall(r'(\\bibitem\{([^}]+)\}[\s\S]*?)(?=\\bibitem\{|\Z)',part)}
assert not used-items.keys(),used-items.keys()
landscape=figure.replace(r'\begin{figure}[p]',r'\begin{landscape}\begin{figure}[p]').replace(r'\end{figure}',r'\end{figure}\end{landscape}\clearpage').replace(r'width=\linewidth',r'width=.94\linewidth')
reader=pre+start+body+landscape+r'\begin{thebibliography}{99}'+'\n'+''.join(items[k] for k in sorted(used))+r'\end{thebibliography}'+'\n'+r'\end{document}'+'\n'
(B/'REAL_PAIR_LOCAL_OBJECT.tex').write_text(reader,encoding='utf-8')
out=B/'output/pdf';out.mkdir(exist_ok=True,parents=True)
draft=B/'texcheck_real_pair_local';draft.mkdir(exist_ok=True)
runs=[]
for name,is_draft,dest in [('REAL_PAIR_LOCAL_OBJECT.tex',False,out),('FABLE_TO_ORIGINAL_CONDUCTOR.tex',True,draft)]:
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
receipt={'result_id':'SZ-20260921-008','base_sha256':sha(base),'principal_sha256':sha(B/'FABLE_TO_ORIGINAL_CONDUCTOR.tex'),
 'proof_sha256':{n:sha(B/n) for n in proofs},'reader_sha256':sha(B/'REAL_PAIR_LOCAL_OBJECT.tex'),
 'pdf_sha256':sha(out/'REAL_PAIR_LOCAL_OBJECT.pdf'),'tags':len(tags),'figures':t.count(r'\includegraphics'),'runs':runs,'visual_review':'pending'}
(B/'REAL_PAIR_LOCAL_INTEGRATION.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
