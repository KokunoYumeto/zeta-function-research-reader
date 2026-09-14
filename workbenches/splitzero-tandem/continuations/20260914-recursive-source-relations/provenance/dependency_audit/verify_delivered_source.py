"""Add portable delivery/PDF binding without changing the earlier stage receipt."""
from pathlib import Path
import hashlib,json,argparse,datetime

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
WORKSPACE=ROOT.parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--repository',type=Path,default=WORKSPACE/'output/Split_Zero_Recursive_Integration_2026-09-13/repository')
args=parser.parse_args()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8'))
stage=read(ROOT/'cumulative_source_v1/provenance/CURRENT_COMPILED_SOURCE_PINS.json')['files']
delivery=read(args.repository/'build/CURRENT_BUILD_RECEIPT.json')
assert delivery['compiled_sources']==stage
for rel,pin in stage.items():assert sha(args.repository/rel)==pin['sha256'],rel
pdf=args.repository/delivery['pdf']
assert sha(pdf)==delivery['pdf_sha256']
assert not delivery['source_preparation_replayed']
assert all(not v for v in delivery['warnings'].values())
result={'status':'PASS: portable rebuild uses every accepted compiled source unchanged',
 'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'repository':str(args.repository),'compiled_sources_checked':len(stage),
 'source_manifest_identical_to_accepted_stage':True,
 'pdf':{'path':str(pdf),'sha256':sha(pdf),'bytes':pdf.stat().st_size,'pages_from_build_receipt':delivery['pages']},
 'stage_audit_receipt':{'path':str(HERE/'FINAL_AUDIT_RECEIPT.json'),'sha256':sha(HERE/'FINAL_AUDIT_RECEIPT.json')},
 'delivery_build_receipt':{'path':str(args.repository/'build/CURRENT_BUILD_RECEIPT.json'),'sha256':sha(args.repository/'build/CURRENT_BUILD_RECEIPT.json')},
 'warning_counts':{k:len(v) for k,v in delivery['warnings'].items()}}
(HERE/'DELIVERED_SOURCE_AND_PDF_CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
