from pathlib import Path
import hashlib
import json
import subprocess
import sys

root = Path(__file__).resolve().parent
script = root / 'gamma_seed_coefficient_certificate_20260913.py'
source = root / 'toda_theta_input_tail_result_normal_20260912.json'
positive = []
for mode in ('normal', 'optimized'):
    path = root / f'gamma_seed_coefficient_result_{mode}_20260913.json'
    result = json.loads(path.read_text(encoding='utf-8'))
    if result['status'] != 'passed' or result['optimization_flag'] != (mode == 'optimized'):
        raise RuntimeError('Previously executed positive certificate result is invalid')
    if result['script_sha256'] != hashlib.sha256(script.read_bytes()).hexdigest():
        raise RuntimeError('Positive result script pin changed')
    positive.append({'mode': mode, 'path': path.name,
                     'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                     'execution_in_this_validator': False})
left = json.loads((root / positive[0]['path']).read_text(encoding='utf-8'))
right = json.loads((root / positive[1]['path']).read_text(encoding='utf-8'))
left.pop('optimization_flag')
right.pop('optimization_flag')
if left != right:
    raise RuntimeError('Positive outputs differ beyond their optimization flags')
negative = []
for mode in ('normal', 'optimized'):
    target = root / f'gamma_seed_coefficient_negative_result_{mode}_20260913.json'
    if target.exists():
        raise RuntimeError('A negative result path already exists')
    command = [sys.executable, '-B'] + (['-O'] if mode == 'optimized' else [])
    command += [str(script), '--input', str(source), '--output', str(target), '--negative-control']
    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    stdout = root / f'gamma_seed_coefficient_negative_{mode}_stdout_20260913.txt'
    stderr = root / f'gamma_seed_coefficient_negative_{mode}_stderr_20260913.txt'
    stdout.write_text(completed.stdout, encoding='utf-8')
    stderr.write_text(completed.stderr, encoding='utf-8')
    expected = 'ValueError: deliberate false Gamma determinant-correction bound rejected'
    if completed.returncode != 1 or expected not in completed.stderr or completed.stdout or target.exists():
        raise RuntimeError('Negative control did not fail exactly as intended')
    negative.append({'mode': mode, 'command': command, 'returncode': completed.returncode,
                     'stdout': stdout.name, 'stdout_sha256': hashlib.sha256(stdout.read_bytes()).hexdigest(),
                     'stderr': stderr.name, 'stderr_sha256': hashlib.sha256(stderr.read_bytes()).hexdigest(),
                     'output_created': target.exists(), 'execution_in_this_validator': True})
receipt = {'status': 'passed', 'script_sha256': hashlib.sha256(script.read_bytes()).hexdigest(),
           'validator_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'input_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
           'positive_records_verified': positive, 'negative_runs': negative,
           'positive_outputs_equal_except_optimization_flag': True,
           'quadrature_rerun': False}
output = root / 'gamma_seed_coefficient_validation_20260913.json'
output.write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'status': 'passed', 'positive_result_records_verified': len(positive),
                  'negative_runs': len(negative), 'receipt': output.name}))
