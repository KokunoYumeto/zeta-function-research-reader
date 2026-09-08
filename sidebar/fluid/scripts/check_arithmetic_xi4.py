"""Run the frozen 22 xi4 transport checks and separate source regressions."""
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'scripts/arithmetic_xi4'
sys.path.insert(0, str(PACKAGE))
from portable_support import MANIFEST, sha256, verify_inventory

def main():
    before = verify_inventory()
    manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
    runs = []
    transport = None
    auxiliary = {}
    for entry in manifest['replays']:
        script = ROOT / entry['portable']
        result = subprocess.run([sys.executable, str(script)], cwd=ROOT,
                                capture_output=True, text=True, encoding='utf-8')
        if result.returncode:
            print(result.stdout, end='')
            print(result.stderr, end='', file=sys.stderr)
            raise SystemExit(result.returncode)
        receipt_path = ROOT / entry['output_receipt']
        receipt = json.loads(receipt_path.read_text(encoding='utf-8'))
        original = json.loads((ROOT / entry['source_checks_receipt']).read_text(encoding='utf-8'))
        if receipt.pop('portable_provenance') != {**before, 'portable_script_sha256':sha256(script)}:
            raise AssertionError(f'Component inventory mismatch: {script.name}')
        if 'expected_checks' in entry:
            checks = receipt['checks']
            if receipt['check_count'] != 22 or len(checks) != 22 or checks != original['checks']:
                raise AssertionError('Expected all 22 unchanged original transport check outputs')
            if not all(c['status'] in ('exact_zero_residual','exact_rational_inequality') for c in checks):
                raise AssertionError('Transport check failure')
            if receipt['status'] != 'pass':
                raise AssertionError('Transport receipt did not pass')
            expected_proofs = [{'path':p['parent_copy'],'sha256':p['source_sha256']} for p in manifest['source_proof_snapshot']]
            if receipt['proofs'] != expected_proofs or receipt['checker_sha256'] != sha256(script):
                raise AssertionError('Transport output has incorrect proof/program provenance')
            for key in ('status','check_count','checks','scope','counterexample_established'):
                if receipt[key] != original[key]:
                    raise AssertionError(f'Changed source receipt field: {key}')
            transport = receipt
            print('check_xi4_transport.py: PASS (22 exact source checks)')
        else:
            if receipt != original:
                raise AssertionError(f'Original auxiliary output changed: {script.name}')
            auxiliary[script.name] = receipt
            print(f'{script.name}: PASS (original receipt fields preserved)')
        runs.append({'script':entry['portable'],'script_sha256':sha256(script),
                     'receipt':entry['output_receipt'],'receipt_sha256':sha256(receipt_path),
                     'all_passed':True,'original_check_outputs_preserved':True})
    if transport is None or len(auxiliary) != 2 or before != verify_inventory():
        raise AssertionError('Missing replay or changed included inputs')
    report = {'schema':'arithmetic-xi4-portable-aggregate-v1','status':'PASS','all_passed':True,
              'number_of_checks':22,'checks':transport['checks'],'auxiliary_source_checks':auxiliary,
              'runs':runs,'portable_provenance':before,'included_input_bytes_unchanged':True,
              'original_check_outputs_preserved':True,'previous_159_checks_recounted':False,
              'scope':'Exactly 22 new finite transport identities; original rational source and 146-block/25-tag rendering regressions reported separately. Complete analytic proofs are retained in full TeX and original Markdown.',
              'RH_counterexample_established':False,'navier_stokes_disproof_established':False,
              'current_189_page_parent_edition_modified':False,'lean_used':False}
    destination = ROOT / 'checks/arithmetic_xi4_checks.json'
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(report, indent=2, ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({'all_passed':True,'number_of_checks':22,'auxiliary_replays':2,
                      'output':destination.relative_to(ROOT).as_posix()}))

if __name__ == '__main__':
    main()
