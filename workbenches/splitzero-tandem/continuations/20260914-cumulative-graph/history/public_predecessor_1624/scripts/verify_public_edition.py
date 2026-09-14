"""Verify exactly the published source/PDF/visual-QA cut, without rebuilding."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
def need(v,m):
    if not v:raise RuntimeError(m)
def read(n):return json.loads((ROOT/n).read_text(encoding='utf-8'))
def pin(n):
    p=ROOT/n;return {'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def main():
    m=read('CURRENT_SOURCE_MANIFEST.json');need(m['schema']=='public-recursive-edition-files-v1','manifest schema')
    for n,row in m['files'].items():need(pin(n)==row,'published bytes changed: '+n)
    known=set(m['files'])|{'CURRENT_SOURCE_MANIFEST.json'}
    actual={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file()}
    need(actual==known,'package file membership differs')
    pins=read('provenance/CURRENT_COMPILED_SOURCE_PINS.json')['files']
    build=read('build/CURRENT_BUILD_RECEIPT.json')
    need(len(pins)==240 and pins==build['compiled_sources'],'actual compiler closure mismatch')
    need(all(m['files'].get(n)==row for n,row in pins.items()),'compiled inputs not manifest-bound')
    d=read('PUBLIC_DERIVATION.json');pdf=d['public_reader']['path']
    need(pin(pdf)==d['public_reader']['identity'],'public reader identity')
    need(build['pdf_sha256']==d['public_reader']['identity']['sha256'],'build PDF differs')
    need(not build['source_preparation_replayed'],'historical source preparation replayed')
    for n,row in d['default_builders'].items():need(m['files'].get(n)==row,'default builder mismatch')
    qa=read('validation/PUBLIC_PDF_VISUAL_ACCEPTANCE.json')
    need(qa['status']=='PASS' and qa['pdf_sha256']==build['pdf_sha256'] and qa['final_pages']==1624 and qa['all_pages_covered'],'current PDF is not covered by final visual QA')
    for x in qa['public_evidence']:need(pin(x['path'])=={k:x[k] for k in ('bytes','sha256')},'visual evidence changed')
    import sys
    sys.dont_write_bytecode=True
    from verify_public_representations import verify as verify_lossless_representations
    representation_check=verify_lossless_representations()
    print(json.dumps({'status':'PASS','files':len(actual),'compiled_inputs':len(pins),'pdf_sha256':build['pdf_sha256'],'lossless_representations':representation_check['lossless_representations'],'fresh_mathematical_or_Lean_verification':False}))
if __name__=='__main__':main()
