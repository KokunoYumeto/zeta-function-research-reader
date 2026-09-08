"""Build the cumulative reader, stopping on unresolved diagnostics."""
from pathlib import Path
import json
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
compiler = shutil.which('pdflatex')
if not compiler:
    raise SystemExit('pdflatex must be available on PATH.')
runs = []
for index in range(1, 4):
    completed = subprocess.run(
        [compiler, '-interaction=nonstopmode', '-halt-on-error', 'main.tex'],
        cwd=ROOT/'tex', capture_output=True, text=True, errors='replace')
    (ROOT/'tex'/f'build-pass-{index}.txt').write_text(completed.stdout, encoding='utf-8')
    runs.append({'pass': index, 'exit_code': completed.returncode})
    if completed.returncode:
        print(completed.stdout[-6000:])
        raise SystemExit(completed.returncode)
log = (ROOT/'tex'/'main.log').read_text(encoding='utf-8', errors='replace')
diagnostics = [line for line in log.splitlines()
               if re.search(r'^(?:Overfull|Underfull|!|LaTeX Warning|Package .* Warning|pdfTeX warning)', line, re.I)]
result = {'schema_version': 1, 'compiler': 'pdflatex', 'runs': runs,
          'diagnostics': diagnostics, 'passed': not diagnostics,
          'visual_qa_included': False}
(ROOT/'checks'/'pdf_build.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
if diagnostics:
    print('\n'.join(diagnostics))
    raise SystemExit(1)
print('Three PDF build passes succeeded; no remaining diagnostics. Visual review is separate.')
