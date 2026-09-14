"""Build only this lane's editable TeX and proof PDF; keep all logs locally."""
from pathlib import Path
import shutil
import subprocess
import re

ROOT = Path(__file__).resolve().parents[3]
WORK = Path(__file__).resolve().parent
OUT = ROOT / 'output/tau_f1_transcript_audit_2026-09-13/proofs'
stem = 'theta_scaling_cocycle'
subprocess.run([
    'pandoc', str(OUT / (stem + '.md')),
    '--from', 'markdown+tex_math_dollars+raw_tex', '--standalone',
    '--variable', 'documentclass=article', '--variable', 'fontsize=11pt',
    '--variable', 'geometry:margin=1in',
    '--include-in-header', str(WORK / 'pdf_header.tex'),
    '--output', str(OUT / (stem + '.tex')),
], check=True, cwd=ROOT)
tex_path = OUT / (stem + '.tex')
tex = tex_path.read_text(encoding='utf-8')
# Source hashes are literal text; xurl supplies line breaks without altering bytes.
tex = re.sub(r'\\texttt\{([0-9a-f]{64})\}', r'\\nolinkurl{\1}', tex)
tex_path.write_text(tex, encoding='utf-8')
fragment=tex.split('\\begin{document}',1)[1].rsplit('\\end{document}',1)[0].strip()+'\n'
(OUT / (stem + '.fragment.tex')).write_text(fragment,encoding='utf-8')
for run in range(2):
    result = subprocess.run([
        'pdflatex', '-interaction=nonstopmode', '-halt-on-error',
        '-output-directory=' + str(WORK), str(OUT / (stem + '.tex')),
    ], cwd=ROOT, capture_output=True, text=True)
    (WORK / f'build_pass_{run+1}.log').write_text(result.stdout + result.stderr, encoding='utf-8')
    if result.returncode:
        raise RuntimeError(result.stdout[-5000:] + result.stderr[-1000:])
log = (WORK / (stem + '.log')).read_text(encoding='utf-8', errors='replace')
diagnostics = [line for line in log.splitlines() if any(word in line for word in ('Overfull', 'Underfull', 'Warning', 'Output written'))]
print('\n'.join(diagnostics))
shutil.copy2(WORK / (stem + '.pdf'), OUT / (stem + '.pdf'))
print('Built ' + str(OUT / (stem + '.pdf')))
