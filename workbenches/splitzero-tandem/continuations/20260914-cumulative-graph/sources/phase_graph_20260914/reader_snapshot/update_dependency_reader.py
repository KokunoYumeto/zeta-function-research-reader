"""Preserve the prior reader exactly before accepted dependency/body updates."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil
ROOT=Path(__file__).resolve().parent
WAVE=ROOT.parent.parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
history=ROOT/'history'/('dependency_update_'+stamp)
history.mkdir(parents=True)
paths=[p for p in ROOT.rglob('*') if p.is_file() and p.relative_to(ROOT).parts[0] in ['originals','tex']]
paths += [ROOT/n for n in ['Phase_Graph_Mixed_Residual_Reader.pdf','BUILD_RECEIPT.json','SOURCE_MANIFEST.json','prepare_reader.py','EXTRA_DEPENDENCIES.json','DISPLAY_REFLOWS.json'] if (ROOT/n).exists()]
records=[]
for p in paths:
    dst=history/p.relative_to(ROOT);dst.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(p,dst);assert sha(p)==sha(dst)
    records.append({'path':p.relative_to(ROOT).as_posix(),'sha256':sha(p),'bytes':p.stat().st_size})
(history/'PRESERVED.json').write_text(json.dumps({'utc':stamp,'files':records},indent=2)+'\n')
extra_path=ROOT/'EXTRA_DEPENDENCIES.json'
extra=json.loads(extra_path.read_text())
for e in extra['files']:
    if e['key'] in ['PGRT','PGGL']:
        p=Path(e['path']);e['sha256']=sha(p)
        shutil.copyfile(p,ROOT/'originals'/(e['key']+'.tex'))
new=[('RMT',WAVE/'recursive_metric_transport.tex','Recursive propagation of the original signed metric bounds'),
     ('ISM',WAVE/'incoming_pr29_metric/incoming_source_metric_control.tex','Source enclosures and convergent signed projector control')]
keys={e['key'] for e in extra['files']}
for key,p,title in new:
    if key not in keys:
        extra['files'].append({'key':key,'path':str(p),'sha256':sha(p),'title':title,'role':'Complete direct dependency of the original arithmetic and holonomy endpoint transport'})
extra_path.write_text(json.dumps(extra,indent=2)+'\n')
reflow_path=ROOT/'DISPLAY_REFLOWS.json'
ref=json.loads(reflow_path.read_text())
old=r''' h(s)=\prod_{r\in\{\rho,\bar\rho,1-\rho,1-\bar\rho\}}(s-r)^m,
 \quad \rho=\tfrac12+\delta+i\gamma,\quad0<\delta<\tfrac12,
 \quad\gamma>2,\quad m,k\geq1,\\'''
new=r''' h(s)=\prod_{r\in\{\rho,\bar\rho,1-\rho,1-\bar\rho\}}(s-r)^m,
 \quad \rho=\tfrac12+\delta+i\gamma,\\
 0<\delta<\tfrac12,\quad\gamma>2,\quad m,k\geq1,\\'''
ref['files'].setdefault('PGRT',[]).append({'old':old,'new':new,'reason':'Reflow the unchanged full quartet and parameter domain onto two lines'})
reflow_path.write_text(json.dumps(ref,indent=2)+'\n')
print(json.dumps({'history':str(history),'preserved_files':len(records),'sources':len(extra['files'])}))
