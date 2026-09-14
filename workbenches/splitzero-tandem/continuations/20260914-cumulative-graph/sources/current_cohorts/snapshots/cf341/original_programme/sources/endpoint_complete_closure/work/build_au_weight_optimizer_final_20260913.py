"""Build and render the current OW.1--40 source without altering older evidence."""
from pathlib import Path
import hashlib, json, subprocess, datetime, re, shutil

W=Path(__file__).resolve().parent
SOURCE=W/'au_weight_optimizer_20260913.tex'
DEST=W/'au_weight_optimizer_final_build_20260913'
DEST.mkdir(exist_ok=True)
def pin(p):
    data=p.read_bytes()
    return {'path':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
receipt={'schema':'au-optimizer-final-build-v1','source':pin(SOURCE),'started':now(),'jobs':[]}
def run(argv,name):
    begin=now()
    result=subprocess.run(argv,cwd=W,capture_output=True)
    out=DEST/(name+'.stdout'); err=DEST/(name+'.stderr')
    out.write_bytes(result.stdout); err.write_bytes(result.stderr)
    job={'argv':argv,'cwd':str(W),'started':begin,'finished':now(),
         'exit_code':result.returncode,'stdout':pin(out),'stderr':pin(err)}
    receipt['jobs'].append(job)
    (DEST/'BUILD.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    if result.returncode: raise RuntimeError(name+' failed; inspect retained output')
    return result
for passnum in (1,2):
    run([shutil.which('pdflatex'),'-interaction=nonstopmode','-halt-on-error',
         '-output-directory='+str(DEST),str(SOURCE)],'pdflatex-'+str(passnum))
PDF=DEST/(SOURCE.stem+'.pdf')
run([shutil.which('pdftoppm'),'-r','110','-png',str(PDF),str(DEST/'page')],'render')
run([shutil.which('pdftotext'),'-layout',str(PDF),str(DEST/'extracted.txt')],'extract')
text=(DEST/'extracted.txt').read_text(encoding='utf-8')
log=(DEST/(SOURCE.stem+'.log')).read_text(encoding='utf-8',errors='replace')
issues=[line for line in log.splitlines() if re.search(r'Overfull|Underfull|Warning:|^!',line)]
labels=[f'OW.{n}' for n in range(1,41)]+['OW.22a']
missing=[label for label in labels if label not in text]
if pin(SOURCE)!=receipt['source']: raise RuntimeError('Source changed during build')
receipt.update(finished=now(),pdf=pin(PDF),pages=text.count('\f'),
               images=[pin(p) for p in sorted(DEST.glob('page-*.png'))],
               log=pin(DEST/(SOURCE.stem+'.log')),layout_log_issues=issues,
               missing_labels=missing,visual_inspection='pending actual all-page view')
(DEST/'BUILD.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'pdf':receipt['pdf'],'pages':receipt['pages'],'issues':issues,'missing':missing}))
if issues or missing: raise RuntimeError('Review actual compiler/extraction findings')
