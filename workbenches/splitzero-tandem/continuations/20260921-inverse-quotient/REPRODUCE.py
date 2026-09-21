from pathlib import Path
import json,hashlib,runpy
P=Path(__file__).parent
out=P/'extracted_sources';out.mkdir(exist_ok=True)
data=(P/'RETAINED_COMPLETE_PROOF_SOURCES.tex').read_bytes()
for r in json.loads((P/'SOURCE_LEDGER.json').read_text(encoding='utf-8'))['retained_source_offsets']:
 b=data[r['offset']:r['offset']+r['length']]
 assert hashlib.sha256(b).hexdigest()==r['sha256']
 (out/r['file']).write_bytes(b)
for name in ['verify_finite_quotient.py','check_analytic_receivers.py']:
 runpy.run_path(str(P/name),run_name='__main__')
