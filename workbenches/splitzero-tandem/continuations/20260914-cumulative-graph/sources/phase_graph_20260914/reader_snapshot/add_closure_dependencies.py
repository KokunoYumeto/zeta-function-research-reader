"""Add complete accepted proof bodies; preserve originals and presentation operations."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
extra_path=ROOT/'EXTRA_DEPENDENCIES.json';extra=json.loads(extra_path.read_text())
intake=ROOT/'dependency_audit/DIRECT_CLOSURE_FILES.json'
if intake.exists():
    audit=json.loads(intake.read_text())
    entries=audit['files']+audit.get('further_direct_dependencies',[])
    for e in entries:
        e.setdefault('title','The original Gamma endpoint-window calculation')
        e.setdefault('role',e.get('reason','Complete original direct proof dependency'))
        if e['key'] not in {x['key'] for x in extra['files']}:
            assert sha(Path(e['path']))==e['sha256']
            extra['files'].append(e)
extra_path.write_text(json.dumps(extra,indent=2)+'\n')
reflow_path=ROOT/'DISPLAY_REFLOWS.json';ref=json.loads(reflow_path.read_text())
ops=[{
 'old':r''' (S-k/2-(2a-k)\delta-i(2b-k)\gamma)^{1+k(m-1)},
 \quad q=[1+k(m-1)](k+1)^2,\quad E=\mathbb{C}[S]/(\chi).''',
 'new':r''' (S-k/2-(2a-k)\delta-i(2b-k)\gamma)^{1+k(m-1)},\\
 q=[1+k(m-1)](k+1)^2,\quad E=\mathbb{C}[S]/(\chi).''',
 'reason':'Place the unchanged cyclic degree and full quotient after the complete characteristic polynomial on the next line'},
 {'old':r''' s_i=\tfrac12+it_i,\quad u=\sum_it_i,\quad S(u)=k/2+iu,
 \quad\tau_k=\sum_i\Phi(s_i),\quad w(t)=|v_h(\tfrac12+it)|^2/(2\pi),\\''',
 'new':r''' s_i=\tfrac12+it_i,\quad u=\sum_it_i,\quad S(u)=k/2+iu,\\
 \tau_k=\sum_i\Phi(s_i),\quad w(t)=|v_h(\tfrac12+it)|^2/(2\pi),\\''',
 'reason':'Reflow the unchanged source-coordinate and density definitions onto two lines'}]
for op in ops:
    if op not in ref['files'].setdefault('PGRT',[]):ref['files']['PGRT'].append(op)
reflow_path.write_text(json.dumps(ref,indent=2)+'\n')
print(json.dumps({'extra_sources':len(extra['files']),'closure_intake_present':intake.exists()}))
