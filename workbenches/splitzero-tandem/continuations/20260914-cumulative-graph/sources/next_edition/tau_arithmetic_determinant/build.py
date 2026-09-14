"""Build the editable companion without running any mathematical checker."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess
import time

parser = argparse.ArgumentParser()
parser.add_argument('--compiler', default='pdflatex')
parser.add_argument('--build-dir')
args = parser.parse_args()
root = Path(__file__).resolve().parent
build = Path(args.build_dir).resolve() if args.build_dir else root / 'build'
build.mkdir(parents=True, exist_ok=True)
records = []
for number in (1, 2, 3):
    command = [args.compiler, '-interaction=nonstopmode', '-halt-on-error',
               '-file-line-error', '-output-directory=' + str(build),
               'Tau_Arithmetic_Determinant_Transport.tex']
    start = time.perf_counter()
    run = subprocess.run(command, cwd=root, capture_output=True, timeout=180)
    (build / f'pdflatex-{number}.stdout').write_bytes(run.stdout)
    (build / f'pdflatex-{number}.stderr').write_bytes(run.stderr)
    records.append({'pass': number, 'exit_code': run.returncode,
                    'elapsed_seconds': time.perf_counter() - start,
                    'stdout_sha256': hashlib.sha256(run.stdout).hexdigest(),
                    'stderr_sha256': hashlib.sha256(run.stderr).hexdigest()})
    if run.returncode:
        (build / 'COMPILATION.json').write_text(json.dumps(records, indent=2) + '\n', encoding='utf-8')
        raise SystemExit(run.returncode)
pdf = build / 'Tau_Arithmetic_Determinant_Transport.pdf'
target = root / pdf.name
shutil.copyfile(pdf, target)
(build / 'COMPILATION.json').write_text(json.dumps(records, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'pdf': str(target), 'bytes': target.stat().st_size,
                  'sha256': hashlib.sha256(target.read_bytes()).hexdigest(),
                  'passes': records}, indent=2))
