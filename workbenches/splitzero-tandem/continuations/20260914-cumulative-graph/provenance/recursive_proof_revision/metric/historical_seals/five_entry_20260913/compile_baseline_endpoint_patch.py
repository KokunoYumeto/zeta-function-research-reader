from pathlib import Path
import subprocess,json,re,hashlib
R=Path(__file__).resolve().parent
base=Path(r'workspace:/output/split_zero_rh_tandem_2026-09-12/current_source_20260913_periodized_residue')
pre=(base/'tex/main.tex').read_text(encoding='utf-8').split(r'\begin{document}',1)[0]
B=R/'endpoint_compile'
B.mkdir(exist_ok=True)
inputs=['build/endpoint_four_volume_threshold_source.tex','tex/arithmetic_volume_upper_route.tex','tex/endpoint_restriction_join.tex']
doc=pre+'\n'+r'\begin{document}'+'\n'+r'\section{Earlier endpoint proof with propagated signed control}'+'\n'
doc+='\n'.join(r'\input{'+(R/'baseline_patch'/p).as_posix()+'}' for p in inputs)
doc+='\n'+r'\input{'+(R.parent/'recursive_metric_transport.tex').as_posix()+'}'
replacements=json.loads((R/'ENDPOINT_CONCLUSION_REPLACEMENTS.json').read_text(encoding='utf-8'))
doc+='\n'+r'\section{Earlier conclusion replacement blocks}'+'\n'
doc+='\n'.join(r'\subsection{'+x['key']+'}'+'\n'+x['new'] for x in replacements)
doc+='\n'+r'\end{document}'+'\n'
(B/'endpoint_patch_check.tex').write_text(doc,encoding='utf-8')
exe=r'runtime:tex/miktex/bin/x64/lualatex.exe'
runs=[]
for i in range(2):
    p=subprocess.run([exe,'-interaction=nonstopmode','-halt-on-error','endpoint_patch_check.tex'],cwd=B,capture_output=True,text=True,encoding='utf-8',errors='replace')
    (B/f'run{i+1}.txt').write_text(p.stdout+p.stderr,encoding='utf-8')
    runs.append({'pass':i+1,'returncode':p.returncode})
    if p.returncode: break
log=(B/'endpoint_patch_check.log').read_text(encoding='utf-8',errors='replace')
result={'runs':runs,'undefined_references':bool(re.search(r'undefined references|Reference .* undefined',log)),'multiply_defined_labels':bool(re.search(r'multiply defined',log)),'errors':[x for x in log.splitlines() if x.startswith('!')],'overfull':[x for x in log.splitlines() if 'Overfull' in x],'pages':re.findall(r'Output written on .*?\((\d+) pages?',log)}
(R/'BASELINE_ENDPOINT_COMPILE.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
