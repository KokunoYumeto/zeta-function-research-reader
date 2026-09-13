"""Verify retained CJ executions and build/render the current proof without rerunning checks."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess
from pypdf import PdfReader

W = Path(__file__).resolve().parent.parent
T = W / 'work'
B = T / 'consecutive_first_window_build_20260913'
V = T / 'consecutive_first_window_final_visual_20260913'
V.mkdir(exist_ok=True)
source = T / 'consecutive_first_window_join_20260913.tex'
checker = T / 'check_consecutive_first_window_join_20260913.py'

def pin(p):
    b = p.read_bytes()
    return {'workspace_relative': p.relative_to(W).as_posix(), 'bytes': len(b),
            'sha256': hashlib.sha256(b).hexdigest()}

R = T / 'consecutive_first_window_replay_20260913'
replay = json.loads((R/'REPLAY.json').read_text())
if replay['checker_sha256'] != pin(checker)['sha256']:
    raise RuntimeError('Checker differs from executed checker')
ordinary = json.loads((T/'consecutive_first_window_checks_normal_v2_20260913.json').read_text())
if (ordinary['passed'], ordinary['failed'], ordinary['runtime']['optimization']) != (378,0,0):
    raise RuntimeError('Ordinary positive result mismatch')
jobs = replay['actual_jobs']
if len(jobs) != 7:
    raise RuntimeError('Unexpected retained job count')
for j in jobs:
    for f in j['files']:
        actual = pin(R/f['path'])
        if (actual['bytes'], actual['sha256']) != (f['bytes'], f['sha256']):
            raise RuntimeError('Retained execution file mismatch')
    output = json.loads((R/j['files'][0]['path']).read_text())
    expected = {'none':(378,0,0), 'omit_phase':(350,28,1),
                'terminal_square':(326,52,1), 'interior_single':(340,38,1)}[output['mutation']]
    if (output['passed'],output['failed'],j['returncode']) != expected:
        raise RuntimeError('Retained check outcome mismatch')
    if sum(x['passed'] for x in output['checks']) != output['passed']:
        raise RuntimeError('Per-check counts do not match')
    if output['mutation']=='none' and (output['checks'],output['cases']) != (ordinary['checks'],ordinary['cases']):
        raise RuntimeError('Positive mode outputs disagree')
history = json.loads((T/'consecutive_first_window_checks_normal_20260913.json').read_text())
if (history['passed'],history['failed']) != (348,30):
    raise RuntimeError('Historical development evidence changed')

argv = ['pdflatex','-interaction=nonstopmode','-halt-on-error',
        '-output-directory='+str(B), str(source)]
p = subprocess.run(argv, cwd=W, capture_output=True, timeout=120)
(V/'build.stdout').write_bytes(p.stdout)
(V/'build.stderr').write_bytes(p.stderr)
if p.returncode:
    raise RuntimeError('TeX build failed')
pdf = B/'consecutive_first_window_join_20260913.pdf'
log = B/'consecutive_first_window_join_20260913.log'
bad = [x for x in log.read_text(errors='replace').splitlines()
       if any(y in x for y in ('Overfull', 'Underfull', 'undefined', 'Rerun to', 'LaTeX Warning', 'Package rerunfilecheck Warning'))]
if bad:
    raise RuntimeError('TeX layout/reference warning: '+repr(bad))
render_argv = ['pdftoppm','-r','110','-png',str(pdf),str(V/'page')]
p2 = subprocess.run(render_argv,cwd=W,capture_output=True,timeout=120)
(V/'render.stdout').write_bytes(p2.stdout)
(V/'render.stderr').write_bytes(p2.stderr)
if p2.returncode:
    raise RuntimeError('Page rendering failed')
pages = len(PdfReader(pdf).pages)
pngs = sorted(V.glob('page-*.png'))
if len(pngs)!=pages:
    raise RuntimeError('Rendered page count mismatch')
receipt = {'utc':datetime.now(timezone.utc).isoformat(),
 'kind':'Retained execution verification plus current source build/render',
 'new_mathematical_check_executions':0, 'retained_jobs_verified':8,
 'historical_failed_development_preserved':True,
 'positive_checks_each_mode':378, 'negative_failures_each_mode':{'omit_phase':28,'terminal_square':52,'interior_single':38},
 'source':pin(source), 'checker':pin(checker), 'replay_receipt':pin(R/'REPLAY.json'),
 'pdf':pin(pdf), 'pages':pages,'build_argv':argv,'build_returncode':p.returncode,
 'render_argv':render_argv,'render_returncode':p2.returncode,
 'layout_or_reference_warnings':bad,'rendered_pages':[pin(x) for x in pngs],
 'visual_review':'Awaiting direct inspection of every rendered page; this receipt does not claim that inspection.'}
(T/'consecutive_first_window_closure_execution_20260913.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'pdf':receipt['pdf'],'pages':pages,'retained_jobs_verified':8,'new_mathematical_check_executions':0},indent=2))
