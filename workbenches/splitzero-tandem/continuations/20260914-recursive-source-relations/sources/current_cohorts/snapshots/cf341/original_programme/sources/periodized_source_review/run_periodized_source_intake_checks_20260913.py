"""Run only the newly received suite and finite mutants, sequentially."""
from pathlib import Path
import hashlib
import json
import platform
import subprocess
import sys
import time
import sympy

WORK = Path(__file__).resolve().parent
OUT = WORK / 'periodized_source_checks_20260913'
OUT.mkdir(exist_ok=True)
SOURCE = Path(r'workspace:\output\split_zero_rh_tandem_2026-09-12\sources\web_periodized_source_delivery\Tau_Periodized_Source_Control\check_periodized.py')
NEG = WORK / 'periodized_source_negative_review_20260913.py'
original = SOURCE.read_bytes()
jobs = []
for optimized in (False, True):
    mode = 'optimized' if optimized else 'normal'
    prefix = [sys.executable] + (['-O'] if optimized else [])
    jobs.append((f'exact-{mode}', prefix + [str(SOURCE), '--output', str(OUT / f'exact-{mode}.json')], 0))
    for negative in ('zero-mode', 'laplacian'):
        jobs.append((f'builtin-{negative}-{mode}', prefix + [str(SOURCE), '--negative', negative], 1))
    jobs.append((f'substantive-negatives-{mode}', prefix + [str(NEG)], 0))
records = []
for label, args, expected in jobs:
    start = time.perf_counter()
    result = subprocess.run(args, capture_output=True, timeout=120)
    elapsed = time.perf_counter() - start
    stdout, stderr = OUT / (label + '.stdout'), OUT / (label + '.stderr')
    stdout.write_bytes(result.stdout)
    stderr.write_bytes(result.stderr)
    row = {'label': label, 'args': args, 'exit_code': result.returncode,
           'expected_exit_code': expected, 'elapsed_seconds': elapsed,
           'stdout': str(stdout), 'stdout_sha256': hashlib.sha256(result.stdout).hexdigest(),
           'stderr': str(stderr), 'stderr_sha256': hashlib.sha256(result.stderr).hexdigest()}
    records.append(row)
    if result.returncode != expected:
        raise RuntimeError(f'{label} exited {result.returncode}, expected {expected}; saved output in {OUT}')
normal = (OUT / 'exact-normal.json').read_bytes()
optimized = (OUT / 'exact-optimized.json').read_bytes()
if normal != optimized:
    raise RuntimeError('Normal and optimized suite result records differ')
if SOURCE.read_bytes() != original:
    raise RuntimeError('Original checker bytes changed')
report = {'scope': 'Only the newly received periodized-source suite; no earlier mathematical suites, calibration, Lean or network run.',
          'python': sys.version, 'sympy': sympy.__version__, 'platform': platform.platform(),
          'source': str(SOURCE), 'source_sha256': hashlib.sha256(original).hexdigest(),
          'positive_methods_per_mode': 16, 'normal_optimized_positive_records_identical': True,
          'built_in_negative_scope': {'zero-mode': 'Unconditional 1 != 0 rejection; only failure-path scope.',
                                      'laplacian': 'Concrete finite algebra rejects omitted -k boundary.'},
          'substantive_mutations_per_mode': 7,
          'source_mutations_persisted': False, 'runs': records}
receipt = OUT / 'RECEIPT.json'
receipt.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'receipt': str(receipt), 'sha256': hashlib.sha256(receipt.read_bytes()).hexdigest(),
                  'runs': len(records), 'positive_methods_per_mode': 16,
                  'substantive_mutations_per_mode': 7,
                  'normal_optimized_positive_records_identical': True}, indent=2))
