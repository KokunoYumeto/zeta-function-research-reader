"""Verify every recorded presentation transport against byte-retained originals."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
ROOT=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((ROOT/'SOURCE_MANIFEST.json').read_text())
checks=[]
for e in manifest['files']:
    p=ROOT/e['original'];assert sha(p)==e['sha256'],e['key']
    original=p.read_bytes().decode('utf-8-sig').replace('\r\n','\n')
    body=original
    for op in e['transports']:
        if op['kind']=='full_document_body':
            pre,body=body.split('\\begin{document}',1)
            body,post=body.rsplit('\\end{document}',1)
            assert pre==op['preamble'] and post==op['postamble'],e['key']
        elif op['kind']=='title_moved_to_chapter':
            assert body.count(op['token'])==1
            body=body.replace(op['token'],'')
        elif op['kind']=='literal_presentation':
            assert body.count(op['old'])>=op['count'],(e['key'],op)
            body=body.replace(op['old'],op['new'],op['count'])
        else:raise ValueError(op['kind'])
    prepared=ROOT/e['body']
    assert prepared.read_text(encoding='utf-8')==body,e['key']
    assert sha(prepared)==e['body_sha256'],e['key']
    checks.append({'key':e['key'],'original_sha256':sha(p),'body_sha256':sha(prepared),'operation_count':len(e['transports']),'exact_replay':True})
receipt={'utc':datetime.now(timezone.utc).isoformat(),'source_manifest_sha256':sha(ROOT/'SOURCE_MANIFEST.json'),'source_count':len(checks),'all_original_bytes_pinned':True,'all_transports_replayed_exactly':True,'checks':checks}
(ROOT/'SOURCE_TRANSPORT_VERIFICATION.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'source_count':len(checks),'all_transports_replayed_exactly':True}))
