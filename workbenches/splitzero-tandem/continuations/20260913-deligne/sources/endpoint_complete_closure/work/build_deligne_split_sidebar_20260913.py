from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import time

work = Path(__file__).resolve().parent
build = work / 'deligne_split_sidebar_build_20260913'
build.mkdir(exist_ok=True)
source = work / 'deligne_split_sidebar_20260913.tex'
wrapper = work / 'deligne_split_sidebar_standalone_20260913.tex'

def pin(path):
    data = path.read_bytes()
    return {'path': str(path), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

xelatex = shutil.which('xelatex')
pdftoppm = shutil.which('pdftoppm')
if not xelatex or not pdftoppm:
    raise RuntimeError('XeLaTeX and pdftoppm are required')

jobs = []
for n in (1, 2):
    argv = [xelatex, '-interaction=nonstopmode', '-halt-on-error',
            '-output-directory=' + str(build), str(wrapper)]
    started = time.time()
    result = subprocess.run(argv, cwd=work, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout = build / f'final_xelatex_{n}.stdout.txt'
    stderr = build / f'final_xelatex_{n}.stderr.txt'
    stdout.write_bytes(result.stdout)
    stderr.write_bytes(result.stderr)
    jobs.append({'argv': argv, 'cwd': str(work), 'started_unix': started,
                 'elapsed_seconds': time.time() - started, 'returncode': result.returncode,
                 'stdout': pin(stdout), 'stderr': pin(stderr)})
    if result.returncode:
        raise RuntimeError('XeLaTeX failed; inspect the retained complete log')

pdf = build / (wrapper.stem + '.pdf')
argv = [pdftoppm, '-png', '-r', '110', str(pdf), str(build / 'page')]
started = time.time()
result = subprocess.run(argv, cwd=work, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout = build / 'final_pdftoppm.stdout.txt'
stderr = build / 'final_pdftoppm.stderr.txt'
stdout.write_bytes(result.stdout)
stderr.write_bytes(result.stderr)
jobs.append({'argv': argv, 'cwd': str(work), 'started_unix': started,
             'elapsed_seconds': time.time() - started, 'returncode': result.returncode,
             'stdout': pin(stdout), 'stderr': pin(stderr)})
if result.returncode:
    raise RuntimeError('pdftoppm failed; inspect retained log')

log = build / (wrapper.stem + '.log')
log_text = log.read_text(encoding='utf-8', errors='replace')
problems = [line for line in log_text.splitlines()
            if 'Overfull' in line or 'Undefined control sequence' in line
            or 'Missing character' in line or 'LaTeX Error' in line]
record = {'status': 'PASS' if not problems else 'LAYOUT_REVIEW_REQUIRED',
          'python': sys.version, 'source': pin(source), 'wrapper': pin(wrapper),
          'builder': pin(Path(__file__)), 'pdf': pin(pdf), 'tex_log': pin(log),
          'jobs': jobs, 'problems': problems,
          'rendered_pages': [pin(p) for p in sorted(build.glob('page-*.png'))],
          'visual_inspection': 'Not implied by rendering; separately recorded after viewing all pages.'}
receipt = work / 'deligne_split_sidebar_build_receipt_20260913.json'
receipt.write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'receipt': pin(receipt), 'status': record['status'],
                  'pdf': pin(pdf), 'rendered_page_count': len(record['rendered_pages']),
                  'problems': problems}))
