"""Build the assembled cumulative successor and verify actual input closure.

This authoring wrapper deliberately requires the new source-stage expectation
manifest.  It never replays historical source conversion.  It pins the actual
FLS inputs only after the ordinary three-pass fixed-source compiler finishes,
then compares every input byte and membership with the accepted assembly.
"""
from pathlib import Path
import hashlib, json, subprocess, sys

ROOT=Path(__file__).resolve().parents[1]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    expected=json.loads((ROOT/'provenance/ASSEMBLED_SOURCE_EXPECTATIONS.json').read_text(encoding='utf-8'))
    for name,item in expected['files'].items():
        path=ROOT/name
        if not path.is_file() or path.stat().st_size!=item['bytes'] or digest(path)!=item['sha256']:
            raise RuntimeError('Assembled source differs before compilation: '+name)
    result=subprocess.run([sys.executable,str(ROOT/'scripts/build_current_reader.py'),'--record-source-pins'],cwd=ROOT)
    if result.returncode:
        raise SystemExit(result.returncode)
    actual=json.loads((ROOT/'provenance/CURRENT_COMPILED_SOURCE_PINS.json').read_text(encoding='utf-8'))
    if actual['files']!=expected['files']:
        raise RuntimeError('Actual FLS inputs differ from the source-stage closure.')
    build=json.loads((ROOT/'build/CURRENT_BUILD_RECEIPT.json').read_text(encoding='utf-8'))
    receipt={'status':'three_pass_cumulative_build_and_exact_input_closure_verified',
             'compiled_input_count':len(actual['files']),
             'source_expectations_sha256':digest(ROOT/'provenance/ASSEMBLED_SOURCE_EXPECTATIONS.json'),
             'actual_source_pins_sha256':digest(ROOT/'provenance/CURRENT_COMPILED_SOURCE_PINS.json'),
             'build_receipt_sha256':digest(ROOT/'build/CURRENT_BUILD_RECEIPT.json'),
             'pdf_sha256':build['pdf_sha256'],'pages':build['pages'],'warnings':build['warnings'],
             'visual_review':'Not implied by this build; review rendered pages separately.'}
    (ROOT/'build/GRAPH_SUCCESSOR_BUILD_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in receipt.items() if k!='warnings'}))

if __name__=='__main__':
    main()
