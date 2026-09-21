from pathlib import Path
import hashlib,json,re,subprocess
B=Path(__file__).resolve().parent
I=json.loads((B/'REAL_PAIR_005_INTEGRATION.json').read_text(encoding='utf-8'))
t=(B/'FABLE_TO_ORIGINAL_CONDUCTOR.tex').read_text(encoding='utf-8')
assert hashlib.sha256((B/'FABLE_TO_ORIGINAL_CONDUCTOR.tex').read_bytes()).hexdigest()==I['principal_sha256']
preamble=t.split(r'\begin{document}',1)[0]
preamble=preamble.replace(r'\usepackage{graphicx}',r'\usepackage{graphicx}'+'\n'+r'\usepackage{pdflscape}')
preamble=preamble.replace(r'\title{The ES--Fable inverse correspondence in the original weighted conductor}',r'\title{A positive real period and its complete ES--Fable conductor return}')
body='\n'.join((B/n).read_text(encoding='utf-8') for n in I['new_sources'])
intro=r'''
\begin{document}\maketitle
\noindent Result SZ-20260921-005. This supplement gives the complete
new root certificate, local inverse calculation and four-label return.
All earlier proof sections cited by equation name are supplied in the
complete cumulative \texttt{FABLE\_TO\_ORIGINAL\_CONDUCTOR.tex}
and its full supporting sources. Verified public programme sources
have pinned links and exact proof locations in the bibliography.
The quartet in the construction is a specified geometric member.
\tableofcontents
\clearpage
'''
figs=t[t.index(r'\section{The positive real pair and the complete four-label correction}'):t.index(r'\begin{thebibliography}')]
figs=figs.replace(r'\section{The positive real pair and the complete four-label correction}','',1)
figs=figs.replace(r'\begin{figure}[p]',r'\clearpage\begin{landscape}\begin{figure}[p]')
figs=figs.replace(r'\end{figure}',r'\end{figure}\end{landscape}\clearpage')
figs=figs.replace(r'width=\linewidth',r'width=.92\linewidth')
used={key for m in re.findall(r'\\cite\{([^}]+)\}',body+figs) for key in m.split(',')}
bibpart=t.split(r'\begin{thebibliography}',1)[1].split(r'\end{thebibliography}',1)[0]
blocks=re.findall(r'(\\bibitem\{([^}]+)\}[\s\S]*?)(?=\\bibitem\{|\Z)',bibpart)
items={key:block for block,key in blocks}
assert not used-items.keys(),used-items.keys()
reader=preamble+intro+body+'\n'+r'\clearpage'+'\n'+figs+'\n'+r'\begin{thebibliography}{99}'+'\n'+''.join(items[k] for k in sorted(used))+r'\end{thebibliography}'+'\n'+r'\end{document}'+'\n'
source=B/'REAL_PAIR_005.tex';source.write_text(reader,encoding='utf-8')
O=B/'output/pdf';O.mkdir(parents=True,exist_ok=True)
check=B/'texcheck_real_pair_005';check.mkdir(exist_ok=True)
runs=[]
for filename,draft,destination in [('REAL_PAIR_005.tex',False,O),('FABLE_TO_ORIGINAL_CONDUCTOR.tex',True,check)]:
    passes=[]
    for n in [1,2]:
        cmd=['pdflatex','-interaction=nonstopmode','-halt-on-error','-output-directory='+str(destination)]
        if draft:cmd.append('-draftmode')
        p=subprocess.run(cmd+[filename],cwd=B,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=180)
        (destination/f'{Path(filename).stem}_pass{n}.txt').write_bytes(p.stdout)
        passes.append({'pass':n,'exit_code':p.returncode})
        if p.returncode:
            print(p.stdout.decode('utf-8',errors='replace')[-5000:]);raise SystemExit(p.returncode)
    log=(destination/(Path(filename).stem+'.log')).read_text(encoding='utf-8',errors='replace')
    missing=re.findall(r'LaTeX Warning: (?:Citation|Reference).*undefined',log)
    assert not missing,missing
    runs.append({'file':filename,'sha256':hashlib.sha256((B/filename).read_bytes()).hexdigest(),
                 'passes':passes,'unresolved_citations_or_references':missing,'overfull_boxes':log.count('Overfull'),
                 'duplicate_destination_warnings':log.count('destination with the same identifier'),
                 'pdf_generated':not draft})
out={'result_id':'SZ-20260921-005','principal_sha256':I['principal_sha256'],'runs':runs,
     'visual_review':'Pending rendered-page inspection; compilation alone is not visual validation.'}
(check/'COMPILATION_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
