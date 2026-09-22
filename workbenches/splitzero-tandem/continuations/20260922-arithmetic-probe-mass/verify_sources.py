from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent
d=json.loads((P/'SOURCE_LEDGER.json').read_text(encoding='utf-8'))
b=(P/'RETAINED_COMPLETE_PROOF_SOURCES.tex').read_bytes()
for x in d['retained_source_offsets']:
 if hashlib.sha256(b[x['offset']:x['offset']+x['length']]).hexdigest()!=x['sha256']:
  raise ArithmeticError(x['file'])
for x in json.loads((P/'MANIFEST.json').read_text(encoding='utf-8'))['files']:
 f=P/x['file']
 if f.stat().st_size!=x['bytes'] or hashlib.sha256(f.read_bytes()).hexdigest()!=x['sha256']:
  raise ArithmeticError(x['file'])
print('Verified every source block and every manifested file.')
