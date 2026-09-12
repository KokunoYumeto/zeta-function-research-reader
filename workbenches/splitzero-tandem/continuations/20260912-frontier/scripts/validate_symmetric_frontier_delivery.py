"""Verify the untouched source archive, add-only patch, and finite check modes."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
STAGE=ROOT/'sources/web_symmetric_frontier_delivery'
SOURCE=STAGE/'Tau_Symmetric_Frontier_Control'
OUT=ROOT/'checks/symmetric_frontier_fresh'
OUT.mkdir(parents=True,exist_ok=True)

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    provenance=json.loads((STAGE/'LOCAL_STAGING_PROVENANCE.json').read_text(encoding='utf-8-sig'))
    def verify():
        for row in provenance['files']:
            if sha(STAGE/row['archive_entry'])!=row['sha256']:
                raise RuntimeError('Changed source '+row['archive_entry'])
        if sha(Path(provenance['archive']))!=provenance['archive_sha256']:
            raise RuntimeError('Changed archive')
    verify()
    patch_files=[]
    current=None
    payload=[]
    in_hunk=False
    def finish():
        if current is not None:
            local=SOURCE/Path(current).name
            if b''.join(payload)!=local.read_bytes():
                raise RuntimeError('Patch bytes differ '+current)
            patch_files.append(dict(path=current,sha256=sha(local),bytes=local.stat().st_size))
    for line in (SOURCE/'INTEGRATION.patch').read_bytes().splitlines(keepends=True):
        if line.startswith(b'diff --git '):
            finish();current=None;payload=[];in_hunk=False
        elif line.startswith(b'+++ b/'):
            current=line[len(b'+++ b/'):].decode().strip()
        elif line.startswith(b'@@ '):
            in_hunk=True
        elif in_hunk:
            if line.startswith(b'+'):
                payload.append(line[1:])
            elif line.startswith(b'\\ No newline'):
                payload[-1]=payload[-1].rstrip(b'\r\n')
            else:
                raise RuntimeError('Patch is not strictly additive')
    finish()
    if len(patch_files)!=8:raise RuntimeError('Expected eight add-only files')
    runs=[]
    for name,optimized,negative in [('normal',False,False),('optimized',True,False),
                                    ('negative-normal',False,True),('negative-optimized',True,True)]:
        report=OUT/(name+'.json')
        cmd=[sys.executable]+(['-O'] if optimized else [])+[str(SOURCE/'check_frontier_control.py'),'--json',str(report)]
        if negative:cmd.append('--negative-control')
        result=subprocess.run(cmd,cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,
                              text=True,encoding='utf-8',errors='replace')
        (OUT/(name+'.log')).write_text(result.stdout,encoding='utf-8')
        data=json.loads(report.read_text())
        if result.returncode!=(1 if negative else 0) or data['tests_run']!=(23 if negative else 22):
            raise RuntimeError('Unexpected exit/test count '+name)
        if data['errors'] or data['failures']!=(1 if negative else 0):
            raise RuntimeError('Unexpected failures '+name)
        runs.append(dict(name=name,command=cmd,returncode=result.returncode,result=data))
    if (OUT/'normal.json').read_bytes()!=(OUT/'optimized.json').read_bytes():
        raise RuntimeError('Normal and optimized JSON differ')
    verify()
    archive=Path(provenance['archive'])
    duplicate=archive.with_name(archive.name.replace(' (1)',''))
    receipt=dict(success=True,python=sys.executable,archive_sha256=sha(archive),
                 archive_and_staged_sources_unchanged=True,
                 duplicate_archive=str(duplicate),duplicate_archive_same_bytes=sha(duplicate)==sha(archive),
                 patch_files_match_exactly=patch_files,runs=runs,
                 scope='Exact finite Gaussian calibration methods, not infinite arithmetic moments, Lean certificates or RH.')
    (OUT/'validation_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(success=True,methods_per_mode=22,negative_controls_exit=1,
                         additive_patch_files=len(patch_files),originals_unchanged=True)))

if __name__=='__main__':main()
