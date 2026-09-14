"""Assemble an additive cumulative successor; never edit the sealed baseline.

This script prepares source only.  It does not invoke TeX or certify a PDF.
The complete predecessor tree is copied and byte-verified before mutation.
Every replaced predecessor file is retained at its original relative path
under history/cumulative_1624_predecessor.  New originals and presentation
bodies have separate manifests; label transports are reversible.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil
from datetime import datetime, timezone

WAVE = Path(r"workspace:\work\backpropagation_20260913")
BASE = Path(r"workspace:\output\Split_Zero_Recursive_Integration_2026-09-13\repository")
STAGE = WAVE / "cumulative_graph_successor_v2"
HISTORY = STAGE / "history/cumulative_1624_predecessor"
SUPPORT = WAVE / "cumulative_graph_successor_support"

def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024*1024), b''):
            h.update(block)
    return h.hexdigest()

def row(path):
    return {'bytes': path.stat().st_size, 'sha256': sha(path)}

def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')

def preserve(relative):
    path = STAGE / relative
    target = HISTORY / relative
    if not path.exists():
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        original = json.loads((STAGE/'provenance/CUMULATIVE_PREDECESSOR_MANIFEST.json').read_text(encoding='utf-8'))['files'][relative]
        if row(target) != original:
            raise RuntimeError('Predecessor history mismatch: '+relative)
    else:
        shutil.copy2(path, target)

def initialize():
    if STAGE.exists():
        raise RuntimeError('Refusing to initialize over an existing successor stage.')
    STAGE.mkdir(parents=True)
    files = {}
    for source in sorted(BASE.rglob('*')):
        if not source.is_file():
            continue
        relative = source.relative_to(BASE).as_posix()
        target = STAGE / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        files[relative] = row(source)
        if row(target) != files[relative]:
            raise RuntimeError('Complete-byte copy mismatch: '+relative)
    receipt = {'status':'complete_predecessor_tree_copied_and_byte_verified',
               'created_utc':datetime.now(timezone.utc).isoformat(),
               'files':files, 'count':len(files),
               'total_bytes':sum(item['bytes'] for item in files.values()),
               'baseline_mutations':0,'tex_runs':0,'new_pdf_certified':False}
    save(STAGE/'provenance/CUMULATIVE_PREDECESSOR_MANIFEST.json',receipt)
    for relative in ['tex/main.tex','tex/research_conclusion.tex','tex/cohorts/cf/13_ACM.tex',
                     'tex/cohorts/cf/31_HC.tex','CURRENT_SOURCE_MANIFEST.json',
                     'provenance/CURRENT_COMPILED_SOURCE_PINS.json','README_CURRENT_EDITION.md',
                     'Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf',
                     'build/CURRENT_BUILD_RECEIPT.json']:
        preserve(relative)
    save(STAGE/'provenance/SUCCESSOR_SOURCE_ASSEMBLY_STATE.json',{
        'status':'predecessor_preserved_waiting_for_final_new_source_pins',
        'tex_runs':0,'new_pdf_certified':False,
        'baseline_pdf_is_historical':True,
        'next':'Import final complete phase-graph source bodies and backward-use replacements.'})
    print(json.dumps({k:v for k,v in receipt.items() if k!='files'}))

def verify_predecessor():
    data=json.loads((STAGE/'provenance/CUMULATIVE_PREDECESSOR_MANIFEST.json').read_text(encoding='utf-8'))
    unchanged=[]; preserved=[]
    for relative, expected in data['files'].items():
        source=BASE/relative
        if row(source)!=expected:
            raise RuntimeError('Sealed baseline changed externally: '+relative)
        target=STAGE/relative
        if target.exists() and row(target)==expected:
            unchanged.append(relative)
        else:
            historical=HISTORY/relative
            if not historical.exists() or row(historical)!=expected:
                raise RuntimeError('Lost predecessor bytes: '+relative)
            preserved.append(relative)
    receipt={'status':'complete_predecessor_bytes_preserved','count':data['count'],
             'unchanged_at_original_path':unchanged,'preserved_at_historical_path':preserved,
             'baseline_mutations':0}
    save(STAGE/'provenance/PREDECESSOR_PRESERVATION_CHECK.json',receipt)
    return receipt

if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('action', choices=['initialize','verify-predecessor'])
    args=parser.parse_args()
    if args.action=='initialize': initialize()
    else:
        result=verify_predecessor()
        print(json.dumps({'status':result['status'],'count':result['count'],
                          'unchanged':len(result['unchanged_at_original_path']),
                          'preserved':len(result['preserved_at_historical_path'])}))
