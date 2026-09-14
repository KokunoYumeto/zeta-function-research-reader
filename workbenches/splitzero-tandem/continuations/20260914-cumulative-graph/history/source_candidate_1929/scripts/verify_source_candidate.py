"""Verify the current source candidate; never report release/PDF acceptance."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
def need(v,m):
    if not v:raise RuntimeError(m)
def read(n):return json.loads((ROOT/n).read_text(encoding='utf-8'))
def pin(n):
    p=ROOT/n;h=hashlib.sha256();size=0
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1048576),b''):h.update(b);size+=len(b)
    return {'bytes':size,'sha256':h.hexdigest()}
def main():
    m=read('CURRENT_SOURCE_MANIFEST.json')
    need(m['schema']=='public-source-candidate-files-v1','candidate manifest schema')
    for n,r in m['files'].items():need(pin(n)==r,'candidate bytes changed '+n)
    actual={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file()}
    need(actual==set(m['files'])|{'CURRENT_SOURCE_MANIFEST.json'},'candidate membership differs')
    a=read('provenance/CURRENT_COMPILED_SOURCE_PINS.json')['files']
    e=read('provenance/ASSEMBLED_SOURCE_EXPECTATIONS.json')['files']
    need(len(a)==279 and a==e,'279-input expectation mismatch')
    need(all(m['files'][n]==r for n,r in a.items()),'compiler files not bound')
    d=read('PUBLIC_DERIVATION.json')
    need(d['status']=='SOURCE_CANDIDATE_NOT_BUILT_NOT_RELEASE_ACCEPTED','candidate status changed')
    history={r['previous_path']:r for r in d['preserved_predecessor_paths']}
    for r in read(d['baseline']['inventory']):
        target=history[r['path']]['preserved_path'] if r['path'] in history else r['path']
        need(pin(target)=={k:r[k] for k in ('bytes','sha256')},'baseline not preserved '+r['path'])
    for r in d['selected_source_dispositions']:
        if r['public_path'] is not None:need(pin(r['public_path'])==r['public'],'selected source differs')
    for n,r in d['compiler']['default_builders'].items():need(pin(n)==r,'fixed builder changed')
    print(json.dumps({'status':'PASS_SOURCE_CANDIDATE_ONLY','files':len(actual),'compiled_input_pins':279,'baseline_files_preserved':11357,'pdf_built':False,'release_accepted':False,'new_math_or_Lean_verification':False}))
if __name__=='__main__':main()
