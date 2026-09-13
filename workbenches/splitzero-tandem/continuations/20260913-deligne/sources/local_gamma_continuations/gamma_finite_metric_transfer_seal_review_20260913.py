"""Pin the independently read GMT proof and verify every primary run record.

This verifier reads existing primary execution records. It does not rerun or
claim to have independently observed those twelve process executions.
"""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent


def pin(name):
    path = ROOT / name
    raw = path.read_bytes()
    return {'name': name, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}


def require(value, message):
    if not value:
        raise RuntimeError(message)


proof = pin('gamma_finite_metric_transfer_20260913.tex')
checker = pin('gamma_finite_metric_transfer_check_20260913.py')
validator = pin('gamma_finite_metric_transfer_validate_20260913.py')
validation = pin('gamma_finite_metric_transfer_validation_20260913.json')
primary = json.loads((ROOT / validation['name']).read_text(encoding='utf-8'))
require(primary['status'] == 'passed', 'Primary validation status')
require(primary['proof_sha256_at_execution'] == proof['sha256'], 'Final proof pin')
require(primary['checker_sha256'] == checker['sha256'], 'Final checker pin')
require(primary['validator_sha256'] == validator['sha256'], 'Primary validator pin')
expected_failure = {'mass': 'finite_gram_mass_factor',
                    'tensor-cross': 'retained_tensor_cross_coefficient',
                    'boundary-sign': 'boundary_resolvent_quadratic_loss',
                    'conjugation': 'original_coordinate_conjugation',
                    'schur-denominator': 'two_degree_source_recurrence'}
records = []
seen = set()
for job in primary['jobs']:
    output = pin(job['output'])
    payload = json.loads((ROOT / job['output']).read_text(encoding='utf-8'))
    fault = job['fault']
    key = (job['optimized'], fault)
    require(key not in seen, 'Duplicate primary job')
    seen.add(key)
    require(output['sha256'] == job['output_sha256'], 'Job output bytes')
    require(payload['script_sha256'] == checker['sha256'], 'Job checker identity')
    require(payload['python_optimized'] is job['optimized'], 'Observed optimization flag')
    require(('-O' in job['argv']) is job['optimized'], 'Requested optimization argument')
    require(payload['fault'] == fault, 'Actual fault selection')
    require(payload['check_count'] == 121 and len(payload['checks']) == 121, 'Exact check count')
    failures = [entry['name'] for entry in payload['checks'] if not entry['passed']]
    expected = [] if fault is None else [expected_failure[fault]]
    require(failures == expected == job['failed_checks'], 'Exact intended failed check')
    require(payload['failed_count'] == len(expected), 'Declared failed count')
    require(job['returncode'] == bool(fault), 'Recorded process exit code')
    require(job['stderr'] == '', 'Unexpected primary stderr')
    stdout = json.loads(job['stdout'])
    require(stdout['checks'] == 121 and stdout['failed'] == len(expected) and stdout['fault'] == fault,
            'Recorded stdout consistency')
    records.append({**output, 'optimized': job['optimized'], 'fault': fault,
                    'check_count': 121, 'failed_checks': failures,
                    'recorded_returncode': job['returncode']})
require(seen == {(mode,fault) for mode in (False,True) for fault in (None,*expected_failure)},
        'Full normal/optimized positive and five-fault coverage')
normal = json.loads((ROOT/'gamma_finite_metric_transfer_check_normal_20260913.json').read_text())
optimized = json.loads((ROOT/'gamma_finite_metric_transfer_check_optimized_20260913.json').read_text())
normal.pop('python_optimized')
optimized.pop('python_optimized')
require(normal == optimized, 'Positive result equality beyond optimization flag')
independent_script = pin('gamma_finite_metric_transfer_independent_check_20260913.py')
independent_result = pin('gamma_finite_metric_transfer_independent_check_result_20260913.json')
independent = json.loads((ROOT/independent_result['name']).read_text())
require(independent['status'] == 'passed' and independent['check_count'] == 37,
        'Independent result passed all 37 checks')
require(independent['script_sha256'] == independent_script['sha256'], 'Independent script pin')
require(all(check['passed'] for check in independent['checks']), 'Independent individual checks')
lines = (ROOT/proof['name']).read_text(encoding='utf-8').splitlines()
locators = {}
for number,line in enumerate(lines,1):
    for label in re.findall(r'\\tag\{(GMT\.[0-9]+[ab]?)\}',line):
        require(label not in locators, 'Duplicate GMT locator')
        locators[label] = number
require(set(locators) == {f'GMT.{i}' for i in range(1,43)} | {'GMT.29a','GMT.29b'},
        'Complete written formula coverage')
receipt = {'schema':'gmt-independent-full-review-receipt-v1', 'status':'passed',
           'proof':proof, 'proof_line_count':len(lines),'exact_formula_line_locators':locators,
           'checker':checker, 'validator':validator,'primary_validation':validation,
           'primary_records':records,'primary_processes_rerun_by_this_verifier':False,
           'primary_record_count':len(records),'primary_positive_check_count':121,
           'independent_script':independent_script,'independent_result':independent_result,
           'independent_check_count':37,
           'review':pin('gamma_finite_metric_transfer_independent_review_20260913.md'),
           'verifier':pin(Path(__file__).name),
           'author_repairs_verified':['t=0 quadratic-loss criterion',
               'strict bounded source and quotient envelopes',
               'explicit positive lower leading principal minors',
               'direct cosine integral proof',
               'typed coefficient c_B_j alias and w_B/m_B_k larger-domain inputs',
               'strict leading-minor check for representative loss upper form'],
           'scope':'Full written GMT.1--42 plus 29a/b mathematical review; independent MGF/Schur and symbolic derivative computations; verification of existing primary execution records; no Lean or nonempty-packet interval computation.'}
out = ROOT/'gamma_finite_metric_transfer_independent_review_receipt_20260913.json'
out.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','proof':proof,'review':receipt['review'],
                  'checker_sha256':checker['sha256'],'primary_records_verified':len(records),
                  'independent_checks':37,'receipt_sha256':hashlib.sha256(out.read_bytes()).hexdigest()}))
