from pathlib import Path
import hashlib, json, re, subprocess

R=Path(__file__).resolve().parent
B=R/'compile'
B.mkdir(exist_ok=True)
source=R/'incoming_source_metric_control.tex'
wrapper=B/'INCOMING_METRIC_CHECK.tex'
wrapper.write_text(r'''\documentclass[11pt]{article}
\usepackage[a4paper,margin=25mm]{geometry}
\usepackage{amsmath,amssymb,mathtools,mathrsfs}
\usepackage[T1]{fontenc}
\begin{document}
'''+r'\input{../incoming_source_metric_control.tex}'+'\n'+r'\end{document}'+'\n',encoding='utf-8')
engine=Path(r'runtime:tex\miktex\bin\x64\lualatex.exe')
runs=[]
for i in (1,2):
    result=subprocess.run([str(engine),'-interaction=nonstopmode','-halt-on-error',wrapper.name],cwd=B,capture_output=True,text=True,encoding='utf-8',errors='replace')
    (B/f'run{i}.txt').write_text(result.stdout+'\n'+result.stderr,encoding='utf-8')
    runs.append({'pass':i,'returncode':result.returncode})
    if result.returncode: break
log=(B/'INCOMING_METRIC_CHECK.log').read_text(encoding='utf-8',errors='replace') if (B/'INCOMING_METRIC_CHECK.log').exists() else ''
body=source.read_text(encoding='utf-8')
tags=re.findall(r'\\tag\{(ISM\d+)\}',body)
receipt={'tex_source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'source_lines':len(body.splitlines()),'tags':tags,'expected_tags':tags==[f'ISM{i}' for i in range(1,44)],
 'latex_runs':runs,'latex_success':len(runs)==2 and all(r['returncode']==0 for r in runs),
 'undefined_control_sequences':len(re.findall('Undefined control sequence',log)),
 'undefined_references':len(re.findall(r'Reference .* undefined',log)),
 'overfull_boxes':re.findall(r'Overfull \\[hv]box.*',log),
 'lean_status':'uncompiled user-supplied draft; no Lean/Lake/Elan execution',
 'pdf_status':'Internal compilation check only; not a visually reviewed deliverable PDF'}
(R/'VALIDATION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
entries=[]
for p in sorted(R.rglob('*')):
    if p.is_file() and 'compile' not in p.relative_to(R).parts and p.name!='MANIFEST.json':
        entries.append({'path':p.relative_to(R).as_posix(),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(R/'MANIFEST.json').write_text(json.dumps({'files':entries,'scope':'Complete new intake; no shared live source edited; original source and draft preserved'},indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
