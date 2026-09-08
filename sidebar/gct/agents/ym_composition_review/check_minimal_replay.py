"""Replay an explicit authored-input allowlist with no source directories."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
from datetime import datetime,timezone

HERE=Path(__file__).resolve().parent
ALLOWED=[
    'ym_composition.tex','check_composition.py',
    'reproduce_composition.py',
    'coefficient_audit/input_transcript.json',
    'coefficient_audit/audit_inputs.py',
    'coefficient_audit/check_coefficients.py','coefficient_audit/REVIEW.md',
    'coefficient_audit/weight_identity/check.py','coefficient_audit/weight_identity/REVIEW.md',
    'domain_audit/check_domains_independently.py','domain_audit/REVIEW.md',
    'domain_audit/input_provenance.json',
    'domain_audit/hilbert_complexification/cubic_check/check_cubic_weights.py',
]
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%f')
target=HERE/'build/minimal_replay'/stamp/'agents/ym_composition_review'
target.mkdir(parents=True)
for name in ALLOWED:
    source=HERE/name
    assert source.is_file(), name
    dest=target/name
    dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(source,dest)
assert not any(p.is_dir() and p.name in ['source','sources','shelf'] for p in target.rglob('*'))
result=subprocess.run([sys.executable,str(target/'reproduce_composition.py')],cwd=target,
                      text=True,encoding='utf-8',errors='replace',capture_output=True)
assert (target/'reproduction.json').exists(), result.stdout+result.stderr
replay=json.loads((target/'reproduction.json').read_text())
report={
    'status':'passed' if result.returncode==0 and replay['status']=='passed' else 'failed',
    'exit_code':result.returncode,'minimal_tree':target.relative_to(HERE).as_posix(),
    'copied_files':{name:hashlib.sha256((target/name).read_bytes()).hexdigest() for name in ALLOWED},
    'proof_sha256':hashlib.sha256((HERE/'ym_composition.tex').read_bytes()).hexdigest(),
    'source_directories_absent':True,'external_authored_sibling_files_absent':True,
    'runs':[{k:r[k] for k in ['script','exit_code']} for r in replay['runs']],
    'stdout':result.stdout,'stderr':result.stderr,
}
(HERE/'minimal_replay_receipt.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':report['status'],'runs':len(report['runs']),'copied_files':len(ALLOWED)}))
if result.returncode: print(result.stdout+result.stderr)
sys.exit(result.returncode)
