"""Bounded replay of the supplied twelve-method packet; no predecessor imports."""
from __future__ import annotations

import ast
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
SOURCE = Path('workspace:/output/split_zero_rh_tandem_2026-09-12/sources/web_residue_constituent_delivery/Tau_Residue_Constituent_Curvature')
PYTHON = Path('runtime:research-python/python.exe')
DEPENDENCIES = Path('workspace:/work/kernel_layer_replay_dependencies_20260912')
EXECUTABLE = ROOT / 'executable'

def stamp():
    return datetime.now(timezone.utc).isoformat()

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def write_json(path, obj):
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

def must(condition, message):
    if not condition:
        raise RuntimeError(message)

def snapshot():
    return {p.relative_to(SOURCE).as_posix(): {'bytes': p.stat().st_size, 'sha256': sha(p)}
            for p in sorted(SOURCE.rglob('*')) if p.is_file()}

def main():
    started = stamp()
    before = snapshot()
    write_json(ROOT / 'raw_snapshot_before.json', before)
    manifest = json.loads((SOURCE / 'MANIFEST.json').read_text(encoding='utf-8'))
    rows = []
    seen = set()
    for row in manifest['files']:
        relative = row['path']
        resolved = (SOURCE / relative).resolve()
        must(resolved.is_relative_to(SOURCE.resolve()), 'Manifest escapes raw source: ' + relative)
        must(relative not in seen, 'Duplicate manifest row: ' + relative)
        seen.add(relative)
        actual = before.get(relative)
        valid = actual == {'bytes': row['bytes'], 'sha256': row['sha256']}
        rows.append({'path': relative, 'expected': {'bytes': row['bytes'], 'sha256': row['sha256']},
                     'actual': actual, 'valid': valid})
    unlisted = sorted(set(before) - seen - {'MANIFEST.json'})
    manifest_audit = {'checked_utc': stamp(), 'source_directory': str(SOURCE),
                      'manifest_sha256': sha(SOURCE / 'MANIFEST.json'),
                      'row_count': len(rows), 'all_rows_valid': all(r['valid'] for r in rows),
                      'unlisted_files_except_manifest': unlisted, 'rows': rows}
    write_json(ROOT / 'manifest_validation.json', manifest_audit)
    must(manifest_audit['all_rows_valid'] and not unlisted, 'Manifest mismatch; see receipt')

    script = SOURCE / 'check_residue_curvature.py'
    tree = ast.parse(script.read_text(encoding='utf-8'))
    classes = [n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == 'Tests']
    must(len(classes) == 1, 'Expected one delivered Tests class')
    methods = [n.name for n in classes[0].body if isinstance(n, ast.FunctionDef) and n.name.startswith('test_')]
    imports = [ast.unparse(n) for n in ast.walk(tree) if isinstance(n, (ast.Import, ast.ImportFrom))]
    assert_count = sum(isinstance(n, ast.Assert) for n in ast.walk(tree))
    code_audit = {
        'audited_utc': stamp(), 'reviewer_read_complete_checker': True,
        'reviewer_read_complete_run_checks': True, 'reviewer_read_complete_handoff': True,
        'script_sha256': sha(script), 'runner_sha256': sha(SOURCE / 'run_checks.py'),
        'test_methods_count': len(methods), 'test_methods': methods, 'imports': imports,
        'python_assert_statement_count': assert_count,
        'failure_mechanism': 'require explicitly raises AssertionError; eq calls require. Python -O cannot remove these checks.',
        'runner_processes_per_mode': ['twelve-method suite', 'negative rank', 'negative laplacian', 'negative curvature'],
        'source_write_analysis': 'Checker prints JSON or raises; delivered runner writes only its own checks directory. Copies run below executable, so raw source receives no writes.',
        'negative_failure_analysis': 'All three controls enter negative_control and fail the false rank, omitted forcing, or omitted |t|^2 identity through require/eq. There is no startup refusal guard.',
        'scope': 'Exact finite polynomial/rational complex fixtures only. No predecessor checks, Lean, quadrature, or arithmetic zero packet.',
    }
    write_json(ROOT / 'code_audit.json', code_audit)
    must(len(methods) == 12 and assert_count == 0, 'Unexpected method count or removable assertion')
    must(not EXECUTABLE.exists(), 'Fresh execution directory required; will not overwrite earlier evidence')
    (EXECUTABLE / 'checks').mkdir(parents=True)
    for filename in ['check_residue_curvature.py', 'run_checks.py']:
        shutil.copyfile(SOURCE / filename, EXECUTABLE / filename)
        must(sha(SOURCE / filename) == sha(EXECUTABLE / filename), 'Copy mismatch')

    import sympy
    must(Path(sys.executable).resolve() == PYTHON.resolve(), 'Wrong interpreter')
    must(sympy.__version__ == '1.14.0', 'Wrong SymPy version')
    must(Path(sympy.__file__).resolve().is_relative_to(DEPENDENCIES.resolve()), 'Wrong SymPy import location')
    env = os.environ.copy()
    env['PYTHONPATH'] = str(DEPENDENCIES)
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    runtime = {'python_executable': sys.executable, 'python_version': sys.version,
               'sympy_version': sympy.__version__, 'sympy_file': sympy.__file__,
               'PYTHONPATH': env['PYTHONPATH'], 'PYTHONDONTWRITEBYTECODE': env['PYTHONDONTWRITEBYTECODE'],
               'platform': sys.platform, 'outer_driver_argv': sys.argv}
    write_json(ROOT / 'runtime.json', runtime)
    batches = []
    expected_errors = {
        'rank': 'intentional rank negative control: actual rank is one',
        'laplacian': 'intentional Laplacian negative control: forcing was omitted',
        'curvature': 'intentional curvature negative control: |t|^2 was omitted',
    }
    for mode in ['normal', 'optimized']:
        argv = [str(PYTHON), str(EXECUTABLE / 'run_checks.py'), mode]
        start = time.perf_counter()
        run_started = stamp()
        run = subprocess.run(argv, cwd=EXECUTABLE, env=env, capture_output=True, timeout=180)
        elapsed = time.perf_counter() - start
        stdout_path = ROOT / (mode + '.runner.stdout.txt')
        stderr_path = ROOT / (mode + '.runner.stderr.txt')
        stdout_path.write_bytes(run.stdout)
        stderr_path.write_bytes(run.stderr)
        batch = {'mode': mode, 'argv': argv, 'cwd': str(EXECUTABLE), 'started_utc': run_started,
                 'finished_utc': stamp(), 'elapsed_seconds': elapsed, 'exit_code': run.returncode,
                 'stdout_path': str(stdout_path), 'stderr_path': str(stderr_path)}
        batches.append(batch)
        write_json(ROOT / 'batch_receipts.json', batches)
        must(run.returncode == 0, f'{mode} runner failed; see recorded stdout/stderr')
        receipt = json.loads((EXECUTABLE / 'checks' / ('EXECUTION_' + mode + '.json')).read_text())
        executions = receipt['executions']
        must(len(executions) == 4, 'Unexpected child process count')
        for index, execution in enumerate(executions):
            child_argv = execution['argv']
            must(('-O' in child_argv) == (mode == 'optimized'), 'Unexpected child optimization flag')
            stdout = (EXECUTABLE / execution['stdout']).read_text()
            stderr = (EXECUTABLE / execution['stderr']).read_text()
            if index == 0:
                success = json.loads(stdout)
                must(execution['exit_code'] == 0 and not stderr, 'Positive run did not exit cleanly')
                must(success['status'] == 'PASS' and success['methods'] == 12, 'Incomplete method pass')
                must(success['tests'] == methods and not success['errors'] and not success['failures'], 'Test inventory differs')
                execution['verified_methods'] = success['methods']
                execution['verified_test_names'] = success['tests']
            else:
                name = ['rank', 'laplacian', 'curvature'][index - 1]
                must(execution['exit_code'] == 1 and not stdout, 'Unexpected negative exit or stdout')
                must('negative_control(args.negative)' in stderr and expected_errors[name] in stderr, 'Not a substantive negative failure')
                must('AssertionError: ' + expected_errors[name] in stderr, 'Wrong negative exception')
                must(not any(s in stderr for s in ['ModuleNotFoundError', 'ImportError', 'SyntaxError']), 'Negative failed at startup')
                execution['verified_failure_formula'] = expected_errors[name]
                execution['verified_failure_is_substantive'] = True
        batch['child_receipt_path'] = str(EXECUTABLE / 'checks' / ('EXECUTION_' + mode + '.json'))
        batch['verified_executions'] = executions
        write_json(ROOT / 'batch_receipts.json', batches)
        print(mode + ': all 12 methods passed; 3 substantive false formulas rejected', flush=True)

    normal = (EXECUTABLE / 'checks' / 'normal.json').read_bytes()
    optimized = (EXECUTABLE / 'checks' / 'optimized.json').read_bytes()
    must(normal == optimized, 'Successful normal/optimized records differ')
    after = snapshot()
    write_json(ROOT / 'raw_snapshot_after.json', after)
    must(before == after, 'Raw packet changed during replay')
    result = {
        'status': 'PASS', 'started_utc': started, 'finished_utc': stamp(),
        'manifest_rows_verified': len(rows), 'raw_files_snapshot_count': len(before),
        'raw_packet_unchanged': True, 'method_count_each_mode': 12,
        'method_invocations_total': 24, 'negative_count_each_mode': 3,
        'substantive_negative_invocations_total': 6,
        'normal_optimized_records_byte_identical': True, 'runtime': runtime,
        'script_sha256': sha(script), 'runner_sha256': sha(SOURCE / 'run_checks.py'),
        'manifest_sha256': sha(SOURCE / 'MANIFEST.json'), 'batches': batches,
        'no_predecessor_checks_executed': True, 'no_lean_lake_elan_executed': True,
    }
    write_json(ROOT / 'replay_receipt.json', result)
    print(json.dumps({k: v for k, v in result.items() if k not in ['runtime', 'batches']}, indent=2), flush=True)

if __name__ == '__main__':
    main()
