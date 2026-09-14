"""Rebuild the mathematically revised reader from its fixed current sources.

The historical source-preparation adapters are retained as provenance. This
entrypoint does not rerun them: it verifies and compiles the complete revised
prepared bodies, so a rebuild cannot restore superseded mathematical text.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil
import subprocess
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / 'build'
PDF = ROOT / 'Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf'
PINS = ROOT / 'provenance/CURRENT_COMPILED_SOURCE_PINS.json'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def warning_scan(log):
    return {name: re.findall(pattern,log,re.M) for name,pattern in {
        'undefined_controls':r'^.*Undefined control sequence.*$',
        'missing_characters':r'^Missing character:.*$',
        'latex_warnings':r'^.*LaTeX Warning:.*$',
        'font_warnings':r'^.*Font Warning:.*$',
        'overfull_boxes':r'^Overfull .*$',
    }.items()}

def used_source_files():
    used = {}
    external_authored=[]
    for line in (BUILD/'reader.fls').read_text(encoding='utf-8',errors='replace').splitlines():
        if not line.startswith('INPUT '):
            continue
        path = Path(line[6:])
        if not path.is_absolute():
            path = ROOT/path
        path = path.resolve()
        if not path.is_file():
            continue
        if not path.is_relative_to(ROOT.resolve()):
            if path.suffix.lower() in ['.tex','.md','.py','.json','.lean'] and not any(
                name in path.as_posix().lower() for name in ['/miktex/','/texlive/']):
                external_authored.append(str(path))
            continue
        if path.suffix.lower() in ['.aux','.toc','.out','.log','.bbl']:
            continue
        name=path.relative_to(ROOT.resolve()).as_posix()
        used[name]={'bytes':path.stat().st_size,'sha256':digest(path)}
    if external_authored:
        raise RuntimeError('Authored source dependency outside the standalone repository: '+repr(external_authored))
    return dict(sorted(used.items()))

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--record-source-pins',action='store_true',help='Authoring use only: pin the revised source after its accepted assembly.')
    args=parser.parse_args()
    if not args.record_source_pins:
        pins=json.loads(PINS.read_text(encoding='utf-8'))
        for name,row in pins['files'].items():
            path=ROOT/name
            if not path.is_file() or path.stat().st_size!=row['bytes'] or digest(path)!=row['sha256']:
                raise RuntimeError('Current source changed: '+name)
    engine=shutil.which('xelatex')
    if engine is None:
        raise RuntimeError('XeLaTeX is required.')
    BUILD.mkdir(exist_ok=True)
    for pass_number in range(1,4):
        result=subprocess.run([engine,'-interaction=nonstopmode','-halt-on-error','-file-line-error','-recorder',
            '-output-directory=build','-jobname=reader','tex/main.tex'],cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        (BUILD/f'current-xelatex-{pass_number}.txt').write_bytes(result.stdout)
        if result.returncode:
            raise RuntimeError('Compilation failed; see build/current-xelatex-'+str(pass_number)+'.txt')
    log=(BUILD/'reader.log').read_text(encoding='utf-8',errors='replace')
    warnings=warning_scan(log)
    sources=used_source_files()
    if args.record_source_pins:
        PINS.parent.mkdir(exist_ok=True)
        PINS.write_text(json.dumps({'files':sources,'count':len(sources),'source_preparation_replayed':False},indent=2)+'\n',encoding='utf-8')
    elif sources!=pins['files']:
        raise RuntimeError('Actual compiled source membership differs from the sealed current reader.')
    if warnings['undefined_controls'] or warnings['missing_characters']:
        raise RuntimeError('Unresolved commands or glyphs require correction before delivery.')
    shutil.copy2(BUILD/'reader.pdf',PDF)
    import fitz
    with fitz.open(PDF) as document:
        pages=len(document)
    receipt={'status':'compiled-current-revised-source','created_utc':datetime.now(timezone.utc).isoformat(),
        'pdf':PDF.name,'pdf_sha256':digest(PDF),'pdf_bytes':PDF.stat().st_size,'pages':pages,
        'compiled_sources':sources,'warnings':warnings,'source_preparation_replayed':False,
        'visual_review':'recorded separately after final PDF compilation'}
    (BUILD/'CURRENT_BUILD_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'pages':pages,'pdf_sha256':receipt['pdf_sha256'],'warning_counts':{k:len(v) for k,v in warnings.items()}}))

if __name__=='__main__':
    main()
