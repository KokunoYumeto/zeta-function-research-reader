import hashlib
import json
from pathlib import Path

root=Path(__file__).parent
folder=root/'gamma_exact_coefficient_join_build_20260913'/'checks'
receipt=json.loads((folder/'replay_receipt.json').read_text())
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
expected={
 'coefficient-factorial':'generating-alpha-1/2-degree-4',
 'initial-mass':'literal-mass-alpha-13/2',
 'coordinate-sign':'original-S-congruence-k-3-n-3',
 'determinant-phase':'original-S-determinant-k-1-n-3',
 'derivative-degree':'finite-Gram-k-2-i-2-j-2-derivative-2',
 'cochain-sign':'negative-section-cochain-k-3',
}
rows=[]
for run in receipt['runs']:
    mode=run['mode'];result=folder/(mode+'.json');log=folder/(mode+'.log')
    data=json.loads(result.read_text())
    failed=[r['name'] for r in data['records'] if not r['passed']]
    mutant=data['mutant']
    wanted=[] if mutant is None else [expected[mutant]]
    predicates=[digest(result)==run['result_sha256'],digest(log)==run['log_sha256'],
                len(data['records'])==143,len({r['name'] for r in data['records']})==143,
                data['checks']==143,failed==wanted,failed==data['failed_checks']==run['failed_checks'],
                run['exit_code']==(0 if mutant is None else 1),
                [r['name'] for r in data['records'] if r['mutant']]==wanted]
    if not all(predicates):raise RuntimeError(mode+str(predicates))
    rows.append({'mode':mode,'result_and_log_hashes_verified':True,'exact_failed_records':failed,'checks':143})
if len(rows)!=14:raise RuntimeError('run count')
record={'source_sha256':digest(root/'gamma_exact_coefficient_join_20260913.tex'),
 'checker_sha256':digest(root/'gamma_exact_coefficient_join_check_20260913.py'),
 'replay_receipt_sha256':digest(folder/'replay_receipt.json'),
 'scope':'Independent inspection of all 14 stored 143-record results and actual log hashes; source checker read completely; no repeated execution claimed.',
 'all_pass':True,'runs':rows}
print(json.dumps(record,indent=2))
