"""Compile the complete, pinned twenty-eight-section TeX reader and source appendices."""
from pathlib import Path
import hashlib, json, shutil, subprocess

root=Path(__file__).resolve().parents[1]
engine=shutil.which('xelatex')
if not engine: raise RuntimeError('XeLaTeX is required; see README.md for fonts/packages')
for n in range(1,4):
    r=subprocess.run([engine,'-interaction=nonstopmode','-halt-on-error','-file-line-error',
                      '-output-directory=build','-jobname=reader','tex/main.tex'],
                     cwd=root,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    (root/'build'/f'local-xelatex-{n}.log').write_bytes(r.stdout)
    if r.returncode: raise RuntimeError(f'XeLaTeX pass {n} failed; see build/local-xelatex-{n}.log')
pdf=root/'build/reader.pdf'
dest=root/'Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf'
shutil.copy2(pdf,dest)
print(json.dumps({'pdf':dest.name,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),
                  'bytes':dest.stat().st_size,
                  'note':'A rebuild may differ in PDF metadata; archived build and visual receipts describe the contributed PDF.'}))
