"""Verify and replay unchanged cyclic-sum source bytes with SymPy 1.14.0.

All output goes to --output, outside the source tree. The previous PR20 source
and archive are optional explicit inputs for the retained-subset comparison.
This replays finite regression methods, not a Lean or arithmetic certificate.
"""
from __future__ import annotations
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path, PurePosixPath
import argparse
import ast
import datetime as dt
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
import zipfile

def sha(data):return hashlib.sha256(data).hexdigest()
def save(path,data):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def snapshot(root):
    if root.is_file():return {root.name:{'sha256':sha(root.read_bytes()),'bytes':root.stat().st_size}}
    return {p.relative_to(root).as_posix():{'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size}
            for p in sorted(root.rglob('*')) if p.is_file()}
def archive_inventory(archive,source):
    prefix=source.name+'/'
    rows=[]
    with zipfile.ZipFile(archive) as z:
        files=[i for i in z.infolist() if not i.is_dir()]
        if len(files)!=len({i.filename for i in files}):raise RuntimeError('Duplicate archive members')
        for info in files:
            member=PurePosixPath(info.filename)
            if member.is_absolute() or '..' in member.parts or '\\' in info.filename or ':' in info.filename or not info.filename.startswith(prefix):
                raise RuntimeError('Unexpected archive member '+info.filename)
            rel=info.filename[len(prefix):]
            data=z.read(info)
            target=source/rel
            rows.append({'path':rel,'archive_entry':info.filename,'bytes':len(data),
                         'sha256':sha(data),'stage_match':target.is_file() and target.read_bytes()==data})
    if not all(row['stage_match'] for row in rows):raise RuntimeError('Archive differs from staged source')
    return rows
def verify_manifest(path,source):
    obj=json.loads(path.read_text(encoding='utf-8-sig'))
    rows=[]
    for rel,expected in obj.items():
        file=source/rel
        data=file.read_bytes()
        rows.append({'path':rel,'bytes':len(data),'sha256':sha(data),
                     'matches':len(data)==expected['bytes'] and sha(data)==expected['sha256']})
    if not all(row['matches'] for row in rows):raise RuntimeError('Source manifest mismatch')
    return rows

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',required=True,type=Path)
    parser.add_argument('--archive',required=True,type=Path)
    parser.add_argument('--output',required=True,type=Path)
    parser.add_argument('--previous-source',type=Path)
    parser.add_argument('--previous-archive',type=Path)
    parser.add_argument('--handoff',type=Path)
    parser.add_argument('--protected',type=Path,action='append',default=[])
    args=parser.parse_args()
    source,archive,out=args.source.resolve(),args.archive.resolve(),args.output.resolve()
    if source==out or source in out.parents:raise RuntimeError('Output must be outside source')
    for path in args.protected:
        resolved=path.resolve()
        if out==resolved or resolved in out.parents:raise RuntimeError('Output enters a protected path')
    import sympy
    declared=json.loads((source/'VALIDATION.json').read_text(encoding='utf-8'))
    if sympy.__version__!=declared['sympy'] or sympy.__version__!='1.14.0':
        raise RuntimeError('Use the source-declared SymPy 1.14.0')
    before=snapshot(source)
    protected_before={str(path.resolve()):snapshot(path.resolve()) for path in args.protected}
    archive_before=sha(archive.read_bytes())
    out.mkdir(parents=True,exist_ok=True)
    rows=archive_inventory(archive,source)
    if len(rows)!=43 or archive.stat().st_size!=443378 or archive_before!='e0e4d0ecda69e4738dcb4cdd3b750e623d863eac8b44f353737393e720a840a7':
        raise RuntimeError('Unexpected cyclic delivery archive identity')
    manifests=verify_manifest(source/'MANIFEST.sha256.json',source)
    checker=source/'check_cyclic_sum.py'
    code=checker.read_text(encoding='utf-8')
    tree=ast.parse(code)
    methods=[node.name for cls in tree.body if isinstance(cls,ast.ClassDef) and cls.name=='ExactChecks'
             for node in cls.body if isinstance(node,ast.FunctionDef) and node.name.startswith('test_')]
    imports=[]
    for node in ast.walk(tree):
        if isinstance(node,ast.Import):imports.extend(alias.name for alias in node.names)
        elif isinstance(node,ast.ImportFrom):imports.append(node.module)
    if len(methods)!=24:raise RuntimeError('Expected exactly 24 declared test methods')
    receipt={'schema':'split-zero-cyclic-source-replay-v1','started_utc':dt.datetime.now(dt.timezone.utc).isoformat(),
             'status':'running','source':str(source),'archive':str(archive),
             'archive_sha256':archive_before,'archive_bytes':archive.stat().st_size,
             'python':sys.version,'executable':sys.executable,'sympy':sympy.__version__,
             'sympy_file':sympy.__file__,'source_recorded_python':declared['python'],
             'runtime_scope':'README requires Python 3 and SymPy. The replay pins source-recorded SymPy 1.14.0; actual Python/platform are recorded separately rather than equated with the source build.',
             'archive_members':rows,'manifest_entries':manifests,
             'unlisted_archive_members':sorted(set(row['path'] for row in rows)-set(row['path'] for row in manifests)),
             'checker':{'path':'check_cyclic_sum.py','sha256':sha(checker.read_bytes()),
                        'bytes':checker.stat().st_size,'lines':len(code.splitlines()),'methods':methods,
                        'imports':sorted(set(imports)),'python_assert_statements':sum(isinstance(n,ast.Assert) for n in ast.walk(tree)),
                        'review_scope':'The complete checker was inspected before execution. Its top-level main runs the declared unittest class, writes only the explicitly provided JSON path, and returns the unittest result. No shell, network, Lean, or credential access is used.'},
             'nested_manifest_files':[p.relative_to(source).as_posix() for p in sorted((source/'sources').rglob('*MANIFEST*.json'))],
             'scope':'Independent archive/source inventory and finite exact regression replay only. No full proof audit, zeta-zero certification, analytic enclosure, Lean execution, or remote CI is asserted.'}
    if args.handoff:
        handoff=args.handoff.read_bytes()
        receipt['separate_user_handoff']={'bytes':len(handoff),'sha256':sha(handoff),
                                        'matches_archived_handoff':handoff==(source/'HANDOFF.md').read_bytes(),
                                        'interpretation':'Read as source data; it does not grant new execution or publication authority.'}
    if args.previous_source and args.previous_archive:
        previous=args.previous_source.resolve()
        previous_rows=archive_inventory(args.previous_archive.resolve(),previous)
        previous_manifest=verify_manifest(previous/'MANIFEST.sha256.json',previous)
        retained=[]
        for path in sorted((source/'sources').rglob('*')):
            if not path.is_file():continue
            rel=path.relative_to(source/'sources').as_posix()
            prior=previous/rel
            retained.append({'current_path':'sources/'+rel,'previous_path':rel,'bytes':path.stat().st_size,
                             'sha256':sha(path.read_bytes()),'matches_previous_source':prior.is_file() and prior.read_bytes()==path.read_bytes()})
        if not all(row['matches_previous_source'] for row in retained):raise RuntimeError('Retained previous source mismatch')
        supplied={row['previous_path'] for row in retained}
        receipt['previous_delivery_relationship']={
            'previous_archive_sha256':sha(args.previous_archive.read_bytes()),
            'previous_archive_members':len(previous_rows),'previous_manifest_entries':len(previous_manifest),
            'independently_verified_previous_archive':True,'retained_members':retained,
            'prior_archive_members_not_in_current_subset':sorted(set(row['path'] for row in previous_rows)-supplied),
            'prior_manifest_entries_not_in_current_subset':sorted(set(row['path'] for row in previous_manifest)-supplied),
            'scope':'The cyclic archive retains only these prior source files. Its source-manifest receipt refers to the earlier separate 51-member/48-entry PR20 ZIP, which was rechecked independently here; that entire earlier ZIP is not bundled inside this cyclic ZIP.'}
    save(out/'replay_receipt.json',receipt)

    def run(mode,optimized,negative):
        folder=out/mode;folder.mkdir(parents=True,exist_ok=True)
        local=folder/checker.name;shutil.copyfile(checker,local)
        result=folder/'result.json'
        cmd=[sys.executable,'-B']+(['-O'] if optimized else [])+[str(local),'--json',str(result)]+(['--fail-control'] if negative else [])
        env=dict(os.environ);env['PYTHONDONTWRITEBYTECODE']='1'
        started=time.monotonic()
        process=subprocess.run(cmd,cwd=folder,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        (folder/'stdout.log').write_bytes(process.stdout);(folder/'stderr.log').write_bytes(process.stderr)
        record=json.loads(result.read_text())
        expected=(process.returncode==(1 if negative else 0) and record['test_methods']==24 and record['errors']==0
                  and record['failures']==(1 if negative else 0) and record['success'] is (not negative))
        row={'mode':mode,'command':cmd,'exit_code':process.returncode,'elapsed_seconds':round(time.monotonic()-started,3),
             'record':record,'expected_behavior':expected,'checker_sha256':sha(local.read_bytes()),
             'result_sha256':sha(result.read_bytes()),'stdout_sha256':sha((folder/'stdout.log').read_bytes()),
             'stderr_sha256':sha((folder/'stderr.log').read_bytes())}
        print(json.dumps({'mode':mode,'exit_code':process.returncode,'expected_behavior':expected,
                          'elapsed_seconds':row['elapsed_seconds']}),flush=True)
        return row
    modes=[('normal',False,False),('optimized',True,False),('negative_normal',False,True),('negative_optimized',True,True)]
    with ThreadPoolExecutor(max_workers=2) as pool:
        receipt['runs']=list(pool.map(lambda row:run(*row),modes))
    receipt.update(success_records_byte_identical=(out/'normal/result.json').read_bytes()==(out/'optimized/result.json').read_bytes(),
                   negative_records_byte_identical=(out/'negative_normal/result.json').read_bytes()==(out/'negative_optimized/result.json').read_bytes(),
                   source_bytes_unchanged=before==snapshot(source),
                   archive_bytes_unchanged=archive_before==sha(archive.read_bytes()),
                   protected_paths=[{'path':path,'files':len(value),'unchanged':value==snapshot(Path(path))}
                                    for path,value in protected_before.items()],
                   finished_utc=dt.datetime.now(dt.timezone.utc).isoformat())
    success=all(row['expected_behavior'] for row in receipt['runs']) and receipt['source_bytes_unchanged'] and receipt['archive_bytes_unchanged'] and all(row['unchanged'] for row in receipt['protected_paths'])
    receipt['status']='passed' if success else 'failed'
    receipt['output_files']=[{'path':p.relative_to(out).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())}
                             for p in sorted(out.rglob('*')) if p.is_file() and p.name!='replay_receipt.json']
    save(out/'replay_receipt.json',receipt)
    print(json.dumps({'status':receipt['status'],'archive_members':len(rows),'manifest_entries':len(manifests),
                      'retained_previous_members':len(receipt.get('previous_delivery_relationship',{}).get('retained_members',[])),
                      'receipt':str(out/'replay_receipt.json')}),flush=True)
    return 0 if success else 1

if __name__=='__main__':raise SystemExit(main())
