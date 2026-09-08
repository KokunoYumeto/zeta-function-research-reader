"""Run all 91 retained coupled-viscous checks using only included files.

Run from any working directory: python path/to/scripts/check_coupled_viscous.py
Python and SymPy are required. No PDF source, network, TeX engine or Lean is used.
"""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'scripts' / 'coupled_viscous'
sys.path.insert(0, str(PACKAGE))
from portable_support import MANIFEST, sha256, verify_inventory


def main() -> None:
    context_before = verify_inventory()
    manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
    output_dir = ROOT / 'checks' / 'coupled_viscous'
    output_dir.mkdir(parents=True, exist_ok=True)
    runs = []
    all_checks = []
    for replay in manifest['replay_adaptations']:
        relative = replay['portable']
        result = subprocess.run([sys.executable, str(ROOT / relative)], cwd=ROOT,
                                capture_output=True, text=True, encoding='utf-8')
        if result.returncode:
            print(result.stdout, end='')
            print(result.stderr, end='', file=sys.stderr)
            raise SystemExit(result.returncode)
        receipt_path = ROOT / replay['output_receipt']
        receipt = json.loads(receipt_path.read_text(encoding='utf-8'))
        checks = receipt['checks']
        if len(checks) != replay['expected_checks'] or not all(c['passed'] for c in checks):
            raise AssertionError(f'Incorrect check count or failed identity in {relative}')
        if receipt['portable_provenance'] != {
                **context_before, 'portable_script_sha256': sha256(ROOT / relative)}:
            raise AssertionError(f'Replay proof-byte receipt mismatch: {relative}')
        runs.append({'script': relative, 'script_sha256': sha256(ROOT / relative),
                     'checks': len(checks), 'all_passed': True,
                     'receipt': replay['output_receipt'], 'receipt_sha256': sha256(receipt_path)})
        all_checks.extend({'script': relative, **item} for item in checks)
        print(f'{Path(relative).name}: PASS ({len(checks)} exact checks)')
    context_after = verify_inventory()
    if context_after != context_before:
        raise AssertionError('Included proof, program or manifest bytes changed during replay')
    if len(all_checks) != 91:
        raise AssertionError('Expected exactly 91 original finite symbolic checks')
    report = {
        'schema': 'coupled-viscous-portable-aggregate-v1',
        'status': 'PASS', 'all_passed': True, 'number_of_checks': len(all_checks),
        'runs': runs, 'checks': all_checks,
        'portable_provenance': context_before,
        'included_files_unchanged_after_replay': True,
        'scope': 'Exact finite symbolic identities only. Complete analytic arguments are in '
                 'tex/coupled_viscous_control.tex. Source infinite estimates remain attributed '
                 'to the identified source; this replay does not prove them.',
        'infinite_viscous_sequence_proved': False,
        'navier_stokes_disproof_established': False, 'lean_used': False,
    }
    output = ROOT / 'checks' / 'coupled_viscous_checks.json'
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(json.dumps({'all_passed': True, 'number_of_checks': 91,
                      'output': output.relative_to(ROOT).as_posix()}))


if __name__ == '__main__':
    main()
