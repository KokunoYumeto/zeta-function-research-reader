#!/usr/bin/env python3
"""Read-only archive-manifest checks and independent finite-suite reruns."""
from pathlib import Path
import hashlib,json,subprocess,sys,zipfile
root=Path(__file__).resolve().parent
parents=[('exponential','Tau_Deligne_Exponential_Comparison','check_exponential.py'),('constituent','Tau_Deligne_Logarithmic_Constituent_Control','check_constituents.py')]
records=[]
for short,name,checker in parents:
    archive=Path('/mnt/data')/(name+'_2026-09-13.zip')
    folder=Path('/mnt/data/_sga_trace_work')/(name+'_2026-09-13')/name
    payload=json.loads((folder/'MANIFEST.json').read_text())
    manifest=payload.get('files',payload.get('entries'))
    if not isinstance(manifest,list):raise RuntimeError('Unsupported manifest structure')
    for row in manifest:
        p=folder/row['path'];data=p.read_bytes()
        if len(data)!=row['bytes'] or hashlib.sha256(data).hexdigest()!=row['sha256']:
            raise RuntimeError('Manifest mismatch: '+str(p))
    runs=[]
    for mode in ['normal','optimized']:
        out=(root/'checks'/f'{short}-{mode}.json').resolve()
        cmd=[sys.executable]+(['-O'] if mode=='optimized' else [])+[str(folder/checker),'--json',str(out)]
        p=subprocess.run(cmd,cwd=folder,capture_output=True,text=True,timeout=35)
        (root/'checks'/f'{short}-{mode}.log').write_text(p.stdout+p.stderr)
        runs.append({'command':cmd,'returncode':p.returncode,'report':json.loads(out.read_text())})
        if p.returncode:raise RuntimeError('parent suite failed')
    if runs[0]['report']!=runs[1]['report']:raise RuntimeError('parent mode reports differ')
    records.append({'name':name,'archive_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'verified_manifest_entries':len(manifest),'runs':runs})
(root/'checks'/'parent-replay.json').write_text(json.dumps(records,indent=2)+'\n')
print([(r['name'],r['verified_manifest_entries'],r['runs'][0]['report']) for r in records])
