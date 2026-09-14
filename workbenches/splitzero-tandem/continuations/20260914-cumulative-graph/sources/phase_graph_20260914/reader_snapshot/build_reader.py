"""Compile the fixed isolated reader; source preparation is a separate operation."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,shutil,subprocess,os,sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).resolve().parent
BUILD=ROOT/'build'
BUILD.mkdir(exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((ROOT/'SOURCE_MANIFEST.json').read_text(encoding='utf-8'))
expected={'tex/main.tex':manifest['main_sha256']}
for entry in manifest['files']:
    assert sha(ROOT/entry['original'])==entry['sha256'],('Original source pin',entry['key'])
    expected[Path(entry['body']).as_posix()]=entry['body_sha256']
for path,digest in expected.items():
    assert sha(ROOT/path)==digest,('Prepared source pin',path)
engine=shutil.which('xelatex')
if not engine:
    candidate=Path(os.environ['LOCALAPPDATA'])/'Programs/MiKTeX/miktex/bin/x64/xelatex.exe'
    if candidate.exists():engine=str(candidate)
if not engine:raise RuntimeError('XeLaTeX is required')
for n in range(1,4):
    p=subprocess.run([engine,'-interaction=nonstopmode','-halt-on-error','-file-line-error','-recorder',
        '-output-directory=build','-jobname=reader','tex/main.tex'],cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    (BUILD/f'xelatex-{n}.txt').write_bytes(p.stdout)
    if p.returncode:
        print(p.stdout.decode('utf-8',errors='replace')[-4000:])
        raise SystemExit(p.returncode)
log=(BUILD/'reader.log').read_text(encoding='utf-8',errors='replace')
warnings={k:re.findall(pattern,log,re.M) for k,pattern in {
'undefined_controls':r'^.*Undefined control sequence.*$',
'missing_characters':r'^Missing character:.*$',
'latex_warnings':r'^.*LaTeX Warning:.*$',
'font_warnings':r'^.*Font Warning:.*$',
'overfull_boxes':r'^Overfull .*$'}.items()}
sources={}
external=[]
for line in (BUILD/'reader.fls').read_text(encoding='utf-8',errors='replace').splitlines():
    if not line.startswith('INPUT '):continue
    p=Path(line[6:])
    if not p.is_absolute():p=ROOT/p
    p=p.resolve()
    if not p.is_file():continue
    if p.is_relative_to(ROOT):
        if p.suffix=='.tex':sources[p.relative_to(ROOT).as_posix()]=sha(p)
    elif p.suffix=='.tex' and 'miktex' not in str(p).lower():external.append(str(p))
assert not external,external
assert sources==expected,{'missing':sorted(set(expected)-set(sources)), 'extra':sorted(set(sources)-set(expected)),
    'changed':[p for p in set(expected)&set(sources) if expected[p]!=sources[p]]}
import fitz
pdf=ROOT/'Phase_Graph_Mixed_Residual_Reader.pdf'
shutil.copyfile(BUILD/'reader.pdf',pdf)
with fitz.open(pdf) as doc:pages=len(doc)
receipt={'utc':datetime.now(timezone.utc).isoformat(),'pdf':pdf.name,'pdf_sha256':sha(pdf),'pages':pages,'compiled_sources':sources,'warnings':warnings,'visual_review':'pending'}
(ROOT/'BUILD_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'pages':pages,'pdf_sha256':sha(pdf),'warning_counts':{k:len(v) for k,v in warnings.items()}}))
