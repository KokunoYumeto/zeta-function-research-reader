from pathlib import Path
import subprocess, json, hashlib, sys
import fitz
from PIL import Image, ImageDraw
root = Path(__file__).resolve().parent
script = root / 'toda_theta_input_tail_check_20260912.py'
records = []
for mode in [0, 1]:
    for negative in [False, True]:
        label = ('optimized' if mode else 'normal') + ('_negative' if negative else '')
        result_path = root / ('toda_theta_input_tail_result_' + label + '_20260912.json')
        cmd = [sys.executable] + (['-O'] if mode else []) + [str(script), '--output', str(result_path)]
        if negative:
            cmd += ['--negative-control']
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
        stdout = root / ('toda_theta_input_tail_' + label + '_stdout_20260912.txt')
        stderr = root / ('toda_theta_input_tail_' + label + '_stderr_20260912.txt')
        stdout.write_text(proc.stdout, encoding='utf-8')
        stderr.write_text(proc.stderr, encoding='utf-8')
        if negative:
            if proc.returncode == 0 or 'deliberate false recurrence bound rejected' not in proc.stderr:
                raise RuntimeError('negative control did not fail with the exact expected check')
            if result_path.exists():
                raise RuntimeError('negative control unexpectedly published a successful receipt')
        elif proc.returncode:
            raise RuntimeError(proc.stderr)
        records.append({'mode': mode, 'negative': negative, 'returncode': proc.returncode,
                        'stdout': stdout.name, 'stderr': stderr.name,
                        'result': None if negative else result_path.name})
normal = json.loads((root / 'toda_theta_input_tail_result_normal_20260912.json').read_text())
optimized = json.loads((root / 'toda_theta_input_tail_result_optimized_20260912.json').read_text())
normal.pop('optimization_flag')
optimized.pop('optimization_flag')
if normal != optimized:
    raise RuntimeError('mode records differ beyond the optimization flag')
receipt = {'status': 'passed', 'records': records, 'normal_optimized_math_identical': True,
           'script_sha256': hashlib.sha256(script.read_bytes()).hexdigest()}
(root / 'toda_theta_input_tail_replay_receipt_20260912.json').write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
pdf_path = root / 'toda_theta_input_tail_20260912.pdf'
doc = fitz.open(pdf_path)
qa = root / 'toda_theta_input_tail_qa_20260912'
qa.mkdir(exist_ok=True)
thumbs = []
for i, page in enumerate(doc):
    pix = page.get_pixmap(matrix=fitz.Matrix(1.35, 1.35), alpha=False)
    path = qa / ('page-%02d.png' % (i+1))
    pix.save(path)
    im = Image.open(path).convert('RGB')
    im.thumbnail((430, 590))
    thumbs.append((i+1, im))
for j in range(0, len(thumbs), 4):
    sheet = Image.new('RGB', (900, 1250), 'white')
    draw = ImageDraw.Draw(sheet)
    for a, (i, im) in enumerate(thumbs[j:j+4]):
        x, y = (a%2)*450+10, (a//2)*625+22
        draw.text((x, y-17), 'Page '+str(i), fill='black')
        sheet.paste(im, (x,y))
    sheet.save(qa / ('contact-%02d.jpg' % (j//4+1)))
print(json.dumps({'status': 'passed', 'modes': len(records), 'rendered_pages': len(doc),
                  'pdf_sha256': hashlib.sha256(pdf_path.read_bytes()).hexdigest()}, indent=2))
