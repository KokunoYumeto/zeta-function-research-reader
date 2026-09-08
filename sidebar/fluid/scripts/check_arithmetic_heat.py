"""Run the three frozen arithmetic heat replays: exactly 30 + 113 + 16 checks.

Python 3.10+ and SymPy are required. No source project, network, PDF, TeX or
Lean process is required. Full analytic proofs are in the included TeX bodies.
"""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'scripts' / 'arithmetic_heat'
sys.path.insert(0, str(PACKAGE))
from portable_support import MANIFEST, check_passed, sha256, verify_inventory


def main() -> None:
    before = verify_inventory()
    manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
    runs = []
    combined = []
    for replay in manifest['replay_adaptations']:
        script = ROOT / replay['portable']
        result = subprocess.run([sys.executable, str(script)], cwd=ROOT,
                                capture_output=True, text=True, encoding='utf-8')
        if result.returncode:
            print(result.stdout, end='')
            print(result.stderr, end='', file=sys.stderr)
            raise SystemExit(result.returncode)
        receipt_file = ROOT / replay['output_receipt']
        receipt = json.loads(receipt_file.read_text(encoding='utf-8'))
        checks = receipt['checks']
        if len(checks) != replay['expected_checks'] or not all(check_passed(c) for c in checks):
            raise AssertionError(f'Failed checks or wrong count: {script.name}')
        original_receipt = json.loads((ROOT / replay['source_checks_receipt']).read_text(encoding='utf-8'))
        if checks != original_receipt['checks']:
            raise AssertionError(f'Actual check outputs differ from frozen source receipt: {script.name}')
        if receipt['portable_provenance'] != {**before, 'portable_script_sha256': sha256(script)}:
            raise AssertionError(f'Component proof-byte receipt mismatch: {script.name}')
        runs.append({'script': replay['portable'], 'script_sha256': sha256(script),
                     'checks': len(checks), 'all_passed': True,
                     'original_check_outputs_preserved': True,
                     'receipt': replay['output_receipt'], 'receipt_sha256': sha256(receipt_file)})
        combined.extend({'script': replay['portable'], **check} for check in checks)
        print(f'{script.name}: PASS ({len(checks)} exact checks)')
    if before != verify_inventory():
        raise AssertionError('Included proof, program or manifest bytes changed during replay')
    if len(combined) != 159:
        raise AssertionError('Expected exactly 159 source checks')
    report = {
        'schema': 'arithmetic-heat-portable-aggregate-v1',
        'status': 'PASS', 'all_passed': True, 'number_of_checks': len(combined),
        'runs': runs, 'checks': combined,
        'portable_provenance': before,
        'included_input_bytes_unchanged': True,
        'original_check_outputs_preserved': True,
        'scope': 'Exact finite algebraic and Taylor-jet identities. Complete analytic proofs remain '
                 'in the three frozen TeX bodies; check counts do not prove convergence or existence.',
        'RH_counterexample_established': False,
        'navier_stokes_disproof_established': False,
        'later_xi4_material_included': False, 'lean_used': False,
    }
    destination = ROOT / 'checks' / 'arithmetic_heat_checks.json'
    destination.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(json.dumps({'all_passed': True, 'number_of_checks': len(combined),
                      'output': destination.relative_to(ROOT).as_posix()}))


if __name__ == '__main__':
    main()
