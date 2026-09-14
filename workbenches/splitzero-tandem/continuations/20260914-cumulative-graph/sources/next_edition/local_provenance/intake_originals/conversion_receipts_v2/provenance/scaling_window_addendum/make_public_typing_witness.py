"""Project complete mathematical notation maps without machine locators.
The local original-byte inverse remains a separately classified artifact.
"""
import copy,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
for key in ('f1_reflection','f1_scaling'):
    receipt=json.loads((ROOT/'receipts'/f'{key}.json').read_text(encoding='utf-8'))
    mapping=json.loads((ROOT/'mapping'/f'{key}_math_mapping.json').read_text(encoding='utf-8'))
    keep={k:copy.deepcopy(v) for k,v in mapping.items() if k not in ('source','retained_code','typed_markdown')}
    if 'typed_markdown' in mapping:
        keep['typed_markdown_before_publication_projection']={k:v for k,v in mapping['typed_markdown'].items() if k!='path'}
    keep['schema']='complete-public-mathematical-notation-transcription-v1'
    keep['source']={k:mapping['source'][k] for k in ('bytes','sha256')}
    keep['complete_public_source']={'path':Path(receipt['public_source']['path']).relative_to(ROOT).as_posix(),
                                  'bytes':receipt['public_source']['bytes'],'sha256':receipt['public_source']['sha256']}
    literal_rows=[]
    for row in mapping['retained_code']:
        item=copy.deepcopy(row);original=item.pop('original')
        item['original_literal_sha256']=hashlib.sha256(original.encode()).hexdigest()
        item['public_literal']=original.removeprefix('workspace:/')
        item['machine_prefix_removed']=item['public_literal']!=original
        literal_rows.append(item)
    keep['retained_code']=literal_rows
    keep['public_projection_scope']='The complete mathematical Code-to-Math map is retained. Source identity is pinned by SHA-256 and byte length. Machine-specific absolute source locators are omitted; their original-byte inverse remains local provenance. The mathematical source objects, formula payloads and notation decisions are not projected away.'
    if 'notes' in keep and isinstance(keep['notes'],str):keep['notes']=keep['notes'].replace('workspace:/','')
    raw=(json.dumps(keep,ensure_ascii=False,indent=2)+'\n').encode()
    if b'Users' in raw or b'C:/Users/' in raw or b'C:\\Users\\' in raw:raise RuntimeError('Private machine locator remains in public notation witness')
    path=ROOT/'public_provenance'/f'{key}_typing.json';path.parent.mkdir(exist_ok=True)
    if path.exists() and path.read_bytes()!=raw:raise RuntimeError('Refusing public notation witness mutation')
    path.write_bytes(raw)
    print(json.dumps({'key':key,'path':str(path),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}))
