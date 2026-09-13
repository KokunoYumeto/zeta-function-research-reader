"""Replay the unchanged exterior-trace finite checker and verify its source.

Output is separate from the delivered archive and staged source. The previous
cyclic delivery is verified explicitly; its old embedded receipts are historical
data. An independently verified local cyclic replay may be attached by path.
"""
from __future__ import annotations
import argparse
import ast
from concurrent.futures import ThreadPoolExecutor
import datetime as dt
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import subprocess
import sys
import time
import zipfile

def digest(data): return hashlib.sha256(data).hexdigest()
def save(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
def snapshot(root):
    return {p.relative_to(root).as_posix(): digest(p.read_bytes())
            for p in sorted(root.rglob('*')) if p.is_file()}
def inventory(source, archive, expected_hash, expected_count):
    raw=archive.read_bytes()
    if digest(raw)!=expected_hash: raise RuntimeError('Archive identity mismatch')
    rows=[]
    with zipfile.ZipFile(archive) as z:
        infos=[i for i in z.infolist() if not i.is_dir()]
        if len(infos)!=expected_count or len({i.filename for i in infos})!=len(infos):
            raise RuntimeError('Unexpected archive inventory')
        prefix=source.name+'/'
        for info in infos:
            part=PurePosixPath(info.filename)
            if part.is_absolute() or '..' in part.parts or '\\' in info.filename or ':' in info.filename or not info.filename.startswith(prefix):
                raise RuntimeError('Unsafe archive member')
            rel=info.filename[len(prefix):]; data=z.read(info)
            if (source/rel).read_bytes()!=data: raise RuntimeError('Staged source differs: '+rel)
            rows.append({'path':rel,'bytes':len(data),'sha256':digest(data)})
    manifest=json.loads((source/'MANIFEST.sha256.json').read_text(encoding='utf-8-sig'))
    for rel, record in manifest.items():
        if rel not in {r['path'] for r in rows}: raise RuntimeError('Manifest path absent from archive')
        data=(source/rel).read_bytes()
        if len(data)!=record['bytes'] or digest(data)!=record['sha256']:
            raise RuntimeError('Manifest mismatch: '+rel)
    return {'archive_sha256':digest(raw),'archive_bytes':len(raw),'members':rows,
            'manifest_entries':len(manifest),'manifest_sha256':digest((source/'MANIFEST.sha256.json').read_bytes()),
            'unlisted_members':sorted({r['path'] for r in rows}-set(manifest))}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for key in ['source','archive','output','cyclic-source','cyclic-archive']:
        ap.add_argument('--'+key, required=True, type=Path)
    ap.add_argument('--cyclic-replay-receipt',type=Path)
    args=ap.parse_args()
    source=args.source.resolve(); archive=args.archive.resolve(); out=args.output.resolve()
    cyclic=args.cyclic_source.resolve(); cyclic_archive=args.cyclic_archive.resolve()
    if out==source or source in out.parents or out==cyclic or cyclic in out.parents:
        raise RuntimeError('Output must be outside source trees')
    import sympy
    if sympy.__version__!='1.14.0': raise RuntimeError('Use source-declared SymPy 1.14.0')
    before=snapshot(source); cyclic_before=snapshot(cyclic)
    exterior_inventory=inventory(source,archive,'168f977a9b54cf461f564e099fe55dc7b8feffbc09c563f541e0be2bb5746a94',35)
    cyclic_inventory=inventory(cyclic,cyclic_archive,'e0e4d0ecda69e4738dcb4cdd3b750e623d863eac8b44f353737393e720a840a7',43)
    if exterior_inventory['manifest_entries']!=34 or cyclic_inventory['manifest_entries']!=42:
        raise RuntimeError('Unexpected manifest scope')
    historical=json.loads((source/'checks/VERIFICATION.json').read_text())
    old=historical['source_manifest']
    if old['archive_sha256']!=cyclic_inventory['archive_sha256'] or old['entries']!=42 or old['source_note_sha256']!=digest((cyclic/'NOTE.tex').read_bytes()):
        raise RuntimeError('Historical cyclic identity mismatch')
    checker=source/'check_exterior_trace.py'; code=checker.read_text(encoding='utf-8'); tree=ast.parse(code)
    methods=[m.name for c in tree.body if isinstance(c,ast.ClassDef) and c.name=='Checks'
             for m in c.body if isinstance(m,ast.FunctionDef) and m.name.startswith('test_')]
    if len(methods)!=22: raise RuntimeError('Unexpected checker method inventory')
    imports=[]
    for n in ast.walk(tree):
        if isinstance(n,ast.Import): imports.extend(x.name for x in n.names)
        elif isinstance(n,ast.ImportFrom): imports.append(n.module)
    out.mkdir(parents=True,exist_ok=True)
    receipt={'schema':'split-zero-exterior-trace-replay-v1','status':'running',
      'started_utc':dt.datetime.now(dt.timezone.utc).isoformat(),
      'python':sys.version,'executable':sys.executable,'sympy':sympy.__version__,'sympy_file':sympy.__file__,
      'historical_python':historical['python'],'source':str(source),'archive':str(archive),
      'exterior_inventory':exterior_inventory,'cyclic_inventory':cyclic_inventory,
      'historical_source_scope':'The exterior ZIP contains receipts about the earlier cyclic ZIP, but no cyclic source members. The separate cyclic ZIP and its 42 manifest entries are independently checked here; its embedded previous-run statements are not called fresh executions.',
      'checker':{'sha256':digest(checker.read_bytes()),'bytes':checker.stat().st_size,'methods':methods,
       'imports':sorted(set(imports)),'python_assert_statements':sum(isinstance(n,ast.Assert) for n in ast.walk(tree)),
       'safety_read':'Complete source inspected: finite SymPy/unittest calculations; main writes only explicitly supplied result JSON. No subprocess, network, credentials, shell, Lean or source mutation.'},
      'scope':'Fresh four-mode finite exact regression replay and byte provenance. The cochain sign methods test parity factors, supported-zero methods test declared toy records, and Gaussian canonical examples use k=1,2. This is not a Lean certificate, full analytic verification, or arithmetic upper estimate.'}
    if args.cyclic_replay_receipt:
        p=args.cyclic_replay_receipt.resolve(); evidence=json.loads(p.read_text(encoding='utf-8'))
        if evidence['status']!='passed' or evidence['archive_sha256']!=cyclic_inventory['archive_sha256']:
            raise RuntimeError('Prior independent cyclic replay not passed or wrong archive')
        for item in evidence['output_files']:
            f=p.parent/item['path']; b=f.read_bytes()
            if digest(b)!=item['sha256'] or len(b)!=item['bytes']:
                raise RuntimeError('Prior cyclic output mismatch')
        receipt['independent_cyclic_replay']={'receipt_sha256':digest(p.read_bytes()),'receipt_path':str(p),
          'verified_output_files':len(evidence['output_files']),'runs':[
           {'mode':r['mode'],'exit_code':r['exit_code'],'record':r['record']} for r in evidence['runs']],
          'scope':'Existing fresh local four-mode cyclic replay adopted after validating every listed output byte. It was not rerun by this exterior replay.'}
    save(out/'replay_receipt.json',receipt)
    def run(item):
        mode,optimized,negative=item; folder=out/mode; folder.mkdir(parents=True,exist_ok=True)
        local=folder/checker.name; shutil.copyfile(checker,local); result=folder/'result.json'
        command=[sys.executable,'-B']+(['-O'] if optimized else [])+[str(local),'--json',str(result)]+(['--fail-control'] if negative else [])
        env=dict(os.environ); env['PYTHONDONTWRITEBYTECODE']='1'; start=time.monotonic()
        process=subprocess.run(command,cwd=folder,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        (folder/'stdout.log').write_bytes(process.stdout); (folder/'stderr.log').write_bytes(process.stderr)
        record=json.loads(result.read_text())
        good=(process.returncode==(1 if negative else 0) and record['test_methods']==22 and record['errors']==0 and record['failures']==(1 if negative else 0) and record['success'] is (not negative) and record['deliberate_failure'] is negative)
        row={'mode':mode,'command':command,'exit_code':process.returncode,'record':record,
             'expected_behavior':good,'elapsed_seconds':round(time.monotonic()-start,3)}
        print(json.dumps({'mode':mode,'exit_code':process.returncode,'expected_behavior':good}),flush=True)
        return row
    with ThreadPoolExecutor(max_workers=2) as pool:
        receipt['runs']=list(pool.map(run,[('normal',False,False),('optimized',True,False),('negative_normal',False,True),('negative_optimized',True,True)]))
    receipt['success_records_byte_identical']=(out/'normal/result.json').read_bytes()==(out/'optimized/result.json').read_bytes()
    receipt['negative_records_byte_identical']=(out/'negative_normal/result.json').read_bytes()==(out/'negative_optimized/result.json').read_bytes()
    receipt['source_bytes_unchanged']=before==snapshot(source)
    receipt['cyclic_source_bytes_unchanged']=cyclic_before==snapshot(cyclic)
    receipt['archives_unchanged']=(digest(archive.read_bytes())==exterior_inventory['archive_sha256'] and digest(cyclic_archive.read_bytes())==cyclic_inventory['archive_sha256'])
    receipt['status']='passed' if all(r['expected_behavior'] for r in receipt['runs']) and all(receipt[k] for k in ['success_records_byte_identical','negative_records_byte_identical','source_bytes_unchanged','cyclic_source_bytes_unchanged','archives_unchanged']) else 'failed'
    receipt['finished_utc']=dt.datetime.now(dt.timezone.utc).isoformat()
    receipt['output_files']=[{'path':p.relative_to(out).as_posix(),'bytes':p.stat().st_size,'sha256':digest(p.read_bytes())} for p in sorted(out.rglob('*')) if p.is_file() and p.name!='replay_receipt.json']
    save(out/'replay_receipt.json',receipt)
    print(json.dumps({'status':receipt['status'],'receipt':str(out/'replay_receipt.json')}),flush=True)
    return 0 if receipt['status']=='passed' else 1

if __name__=='__main__': raise SystemExit(main())
