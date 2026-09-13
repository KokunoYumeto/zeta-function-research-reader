"""Validate the local-only concrete correction proposal without changing the PR."""
import difflib
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parent
SOURCE=ROOT/'files/workbenches/tau-confluent-transfer'
PROPOSAL=ROOT/'proposed'
OUT=ROOT/'proposal_checks'; OUT.mkdir(exist_ok=True)
patch=[]; files=[]
for name in ['RESEARCH_NOTE.md','check_transfer_core.py']:
    before=(SOURCE/name).read_bytes(); after=(PROPOSAL/name).read_bytes()
    patch.extend(difflib.unified_diff(before.decode().splitlines(keepends=True),after.decode().splitlines(keepends=True),fromfile='a/workbenches/tau-confluent-transfer/'+name,tofile='b/workbenches/tau-confluent-transfer/'+name))
    files.append({'path':'workbenches/tau-confluent-transfer/'+name,'before_sha256':hashlib.sha256(before).hexdigest(),'proposed_sha256':hashlib.sha256(after).hexdigest()})
(ROOT/'PROPOSED_CORRECTION.patch').write_text(''.join(patch),encoding='utf-8')
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
results=[]
for label,flags in [('normal',[]),('optimized',['-O'])]:
    for negative in [False,True]:
        name=label+('_negative' if negative else '')
        command=[sys.executable,*flags,str(PROPOSAL/'check_transfer_core.py'),*(['--negative-control'] if negative else [])]
        run=subprocess.run(command,capture_output=True,text=True,encoding='utf-8',timeout=45 if not negative else 10,env=env,cwd=ROOT)
        (OUT/(name+'.stdout')).write_text(run.stdout,encoding='utf-8')
        (OUT/(name+'.stderr')).write_text(run.stderr,encoding='utf-8')
        record=None
        if negative:
            if run.returncode!=1 or 'deliberate negative control' not in run.stderr: raise ValueError('Proposal negative control failure')
        else:
            if run.returncode!=0: raise ValueError(run.stderr)
            record=json.loads(run.stdout)
            if record['tests_run']!=8 or not record['success'] or record['failures'] or record['errors']: raise ValueError('Proposal core failed')
        results.append({'mode':label,'negative_control':negative,'exit_code':run.returncode,'record':record})
normal=[r['record'] for r in results if not r['negative_control']]
if len(normal)!=2 or normal[0]!=normal[1]: raise ValueError('Proposed mode records differ')
receipt={'created_utc':datetime.now(timezone.utc).isoformat(),'based_on_pr_head':'dfcbba5cbf7fec8c9301fe242c13e741d762013e','proposal_only_not_applied_remotely':True,'changed_proposal_paths':files,'tests':results,'normal_optimized_records_identical':True,'nonzero_phase_fixture_included':True,'full_two_loss_identity_included':True,'raw_jet_coordinate_map_explicit':True,'scope':'Exactly two local proposed files; original downloaded PR source unchanged. Eight finite test methods per mode; not actual arithmetic, an asymptotic estimate, or Lean.'}
(ROOT/'PROPOSED_CORRECTION_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
