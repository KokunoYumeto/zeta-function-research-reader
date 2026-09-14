from pathlib import Path
import hashlib,json,re
p=Path(__file__).resolve().parent
for stem,title in [('shifted_mellin_source_constants','Exact weighted theta-source constants'),('circle_theta_resolvent','Circle resolvent with all arithmetic jets')]:
    tex=(p/(stem+'.tex')).read_text(encoding='utf-8')
    body=tex.split(r'\begin{document}',1)[1].split(r'\end{document}',1)[0]
    body=body.replace(r'\maketitle','').strip()
    body=body.replace(r'\section',r'\subsection')
    definitions=''
    if stem.startswith('shifted'):
        definitions='\n'.join([r'\def\LCSB{\mathscr B}',r'\def\LCSV{\mathcal V}',r'\def\LCSM{\mathcal M}',r'\def\LCStr{\operatorname{Tr}}',r'\newtheorem{latecontroltheorem}{Theorem}[section]'])
        for a,b in [('B','LCSB'),('V','LCSV'),('M','LCSM'),('tr','LCStr')]:
            body=re.sub(r'\\'+a+r'(?![A-Za-z])',lambda m:'\\'+b,body)
        body=body.replace(r'\begin{theorem}',r'\begin{latecontroltheorem}').replace(r'\end{theorem}',r'\end{latecontroltheorem}')
    fragment='% Requires amsmath, amssymb, amsthm, mathrsfs in the parent preamble.\n'+r'\begingroup'+'\n'+definitions+'\n'+r'\section{'+title+'}\n'+body+'\n'+r'\endgroup'+'\n'
    (p/(stem+'_fragment.tex')).write_text(fragment,encoding='utf-8')

review={
 'reviewer':'/root/audit_late_control/review_shifted_mellin',
 'shifted_mellin':{'result':'All identities, phases, constants, finite trace bounds, and explicit L/J choices checked. Exact translated Gaussian fixture independently checked complex derivative cross terms.','corrections_integrated':['Require N>=deg chi-1 for quotient Grams on all E','Specify scalar holonomy phases']},
 'circle_resolvent':{'result':'Signs of resolvent comparison and nilpotent sum, resonant recursion, Laplacian boundary and nilpotent polynomial checked.','corrections_integrated':['Explicit admissible period L proves periodized injectivity','CRT idempotent embeds increasing local power basis','Twisted H2 domain stated','Boundary nonvanishing limited to nonresonant eigenvectors; resonant freedom retained']},
 'scope':'Written exact proof review and independent analytic Gaussian fixture; no arithmetic moment enclosure, full asymptotic bound, Lean, or external publication.'}
(p/'PROOF_REVIEW.json').write_text(json.dumps(review,indent=2)+'\n',encoding='utf-8')
names=['AUDIT_LATE_CONTROL.md','AUDIT_LATE_CONTROL.json','USER_INPUTS_VERBATIM.md','COVERAGE.json','shifted_mellin_source_constants.tex','shifted_mellin_source_constants.md','shifted_mellin_source_constants_fragment.tex','circle_theta_resolvent.tex','circle_theta_resolvent.md','circle_theta_resolvent_fragment.tex','PROOF_REVIEW.json']
manifest=[]
for name in names:
    data=(p/name).read_bytes()
    manifest.append({'file':name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
(p/'DELIVERY_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print(json.dumps(manifest,indent=2))
