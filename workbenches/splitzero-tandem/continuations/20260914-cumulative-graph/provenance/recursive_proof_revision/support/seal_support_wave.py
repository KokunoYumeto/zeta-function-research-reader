from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,re,subprocess

S=Path(__file__).resolve().parent
exe=r'runtime:tex\miktex\bin\x64\lualatex.exe'
p=subprocess.run([exe,'-interaction=nonstopmode','-halt-on-error','SUPPORT_WAVE_CHECK.tex'],cwd=S/'updated',capture_output=True,text=True,encoding='utf-8',errors='replace')
(S/'compile_final.txt').write_text(p.stdout+p.stderr,encoding='utf-8')
log=(S/'updated/SUPPORT_WAVE_CHECK.log').read_text(encoding='utf-8',errors='replace')
validation={'exit':p.returncode,'pages':re.findall(r'Output written on .*?\((\d+) pages',log),'overfull_boxes':re.findall(r'Overfull \\[hv]box.*',log),'undefined_references':re.findall(r"LaTeX Warning: Reference `(.*?)'",log),'scope':'Final four complete source chapters. sec:research-state belongs to the root current-results chapter. Internal compile PDF; root owns published PDF QA.'}
assert p.returncode==0
assert not validation['overfull_boxes']
assert set(validation['undefined_references']) <= {'sec:research-state'}
(S/'FINAL_COMPILE.json').write_text(json.dumps(validation,indent=2),encoding='utf-8')

paths=[]
for sub in ['provenance','updated/tex','fragments','filtration/originals','filtration/revised']:
    paths.extend(p for p in (S/sub).rglob('*') if p.is_file())
for name in ['PROPAGATION.md','VALIDATION.json','FINAL_COMPILE.json','build_support_wave.py','validate_support_wave.py','seal_support_wave.py','filtration/PROPAGATION.md','filtration/INVENTORY.json','filtration/LOGBOOK.md','filtration/verify_stage.py']:
    if (S/name).exists():paths.append(S/name)
def info(p):
    b=p.read_bytes();return {'path':str(p.relative_to(S)).replace('\\','/'),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'lines':len(b.splitlines())}
rows=[info(p) for p in sorted(set(paths))]
manifest={'schema':'support-backpropagation-source-wave-v1','utc':datetime.now(timezone.utc).isoformat(),'historical_baseline':'workspace:/work/cumulative_deligne_build_20260913_v2','live_sources_modified':False,'publication_performed':False,'files':rows}
(S/'MANIFEST.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
pins={r['path']:r['sha256'] for r in rows if r['path'].startswith('updated/tex/') or r['path'].startswith('filtration/revised/')}
print(json.dumps({'manifest_sha256':hashlib.sha256((S/'MANIFEST.json').read_bytes()).hexdigest(),'files':len(rows),'validation':validation,'source_pins':pins},indent=2))
