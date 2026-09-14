from pathlib import Path
import subprocess,json,re,hashlib
P=Path(__file__).resolve().parent
B=P.parent.parent/'cumulative_source_v1'
C=P/'compile'; C.mkdir(exist_ok=True)
pre=(B/'tex/main.tex').read_text(encoding='utf-8').split(r'\begin{document}',1)[0]
pre=re.sub(r'\\input\{([^}]+)\}',lambda m:r'\input{'+(B/m.group(1)).as_posix()+'}',pre)
inputs=[P/'derived/tex/cohorts/cf/13_ACM.tex',P/'derived/tex/cohorts/cf/31_HC.tex',P.parent.parent/'recursive_metric_transport.tex',P.parent.parent/'incoming_pr29_metric/incoming_source_metric_control.tex']
doc=pre+'\n'+r'\begin{document}'+'\n'
doc+='\n'.join(r'\input{'+p.as_posix()+'}' for p in inputs)
doc+='\n'+r'\end{document}'+'\n'
(C/'cf_active_patch_check.tex').write_text(doc,encoding='utf-8')
exe=r'runtime:tex/miktex/bin/x64/lualatex.exe'
runs=[]
for i in range(2):
    proc=subprocess.run([exe,'-interaction=nonstopmode','-halt-on-error','cf_active_patch_check.tex'],cwd=C,capture_output=True,text=True,encoding='utf-8',errors='replace')
    (C/f'run{i+1}.txt').write_text(proc.stdout+proc.stderr,encoding='utf-8')
    runs.append({'pass':i+1,'returncode':proc.returncode})
    if proc.returncode: break
log=(C/'cf_active_patch_check.log').read_text(encoding='utf-8',errors='replace')
receipt={'runs':runs,'undefined_references':bool(re.search(r'undefined references|Reference .* undefined',log)),'multiply_defined_labels':bool(re.search(r'multiply defined',log)),'errors':[x for x in log.splitlines() if x.startswith('!')],'overfull':[x for x in log.splitlines() if 'Overfull' in x],'pages':re.findall(r'Output written on .*?\((\d+) pages?',log)}
(P/'COMPILE_RECEIPT.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt,indent=2))
