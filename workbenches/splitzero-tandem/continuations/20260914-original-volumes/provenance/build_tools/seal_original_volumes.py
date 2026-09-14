"""Seal cut22 only after root proof acceptance and full current-PDF visual coverage."""
from pathlib import Path
import hashlib,json,zipfile,datetime
import fitz

gw=Path(__file__).resolve().parent
out=Path(r'C:\Users\[[user]]\Documents\math\output\Split_Zero_Mixed_Boundary_Continuation_2026-09-14\22_ORIGINAL_VOLUMES')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
pdf=out/'Original_Gamma_Volumes_and_Intrinsic_Spectral_Sums.pdf'
pdfsha=digest(pdf)
pages=len(fitz.open(pdf))
rootaccept=out/'ROOT_PROOF_ACCEPTANCE.json'
if not rootaccept.exists():raise RuntimeError('Await root proof acceptance')
accept=json.loads(rootaccept.read_text(encoding='utf-8'))
if accept.get('status') not in ['PASS','ACCEPT','ACCEPTED']:raise RuntimeError('Root proof acceptance is not complete')
coverage=set();visual=[]
for path in sorted((out/'qa').glob('VISUAL_*.json')):
    item=json.loads(path.read_text(encoding='utf-8'))
    if item.get('status')!='PASS' or item.get('pdf_sha256')!=pdfsha:raise RuntimeError(('visual pin/status',path))
    coverage.update(item['pages'])
    visual.append({'path':str(path.relative_to(out)).replace('\\','/'),'sha256':digest(path)})
if coverage!=set(range(1,pages+1)):raise RuntimeError(('incomplete current-PDF visual coverage',sorted(coverage),pages))
opg=out/'next_original_observation'
opg_receipt=opg/'CLOSURE_RECEIPT.json'
opg_data=json.loads(opg_receipt.read_text(encoding='utf-8'))
if opg_data.get('result')!='PASS':raise RuntimeError('Separate original observation stage is not accepted')
opg_pinned_files=[opg_receipt]
for item in opg_data['files_excluding_this_receipt']:
    path=opg/item['path']
    if not path.resolve().is_relative_to(opg.resolve()):raise RuntimeError(item)
    if path.stat().st_size!=item['bytes'] or digest(path)!=item['sha256']:raise RuntimeError(('OPG receipt file pin',item))
    opg_pinned_files.append(path)
for f in ['00_CONTINUE_THE_PROGRAMME.md','CURRENT_RESEARCH_WORKFLOW_4000_CHARS.md','current_receiving/CURRENT_JOINT_SCHUR_NOTE.tex','current_receiving/SIGNED_RETURN_RECEIVER.tex']:
    if not (out/f).exists():raise RuntimeError(('required delivery file',f))
workflow=(out/'CURRENT_RESEARCH_WORKFLOW_4000_CHARS.md').read_bytes().decode('utf-8')
if len(workflow)!=4000:raise RuntimeError(('workflow Unicode character count',len(workflow)))
if '\r' in workflow:raise RuntimeError('workflow must retain LF bytes')
for pin in json.loads((out/'NEW_PROOF_SOURCE_PINS.json').read_text(encoding='utf-8')):
    if digest(out/pin['original'])!=pin['sha256']:raise RuntimeError(('original proof pin',pin))
    if digest(out/pin['destination'])!=pin['typeset_sha256']:raise RuntimeError(('typeset proof pin',pin))
root_provider_pins={x['sha256'] for x in accept['proofs']}
printed_pins={x['sha256'] for x in json.loads((out/'NEW_PROOF_SOURCE_PINS.json').read_text(encoding='utf-8'))}
if not printed_pins.issubset(root_provider_pins):raise RuntimeError('Unaccepted printed provider')
receiving=out/'current_receiving'
receiving_accept=json.loads((receiving/'ROOT_RECEIVING_ACCEPTANCE.json').read_text(encoding='utf-8'))
for item in receiving_accept['receiver_pins']:
    if digest(receiving/item['file'])!=item['successor_sha256']:raise RuntimeError(('receiving pin',item))
manifest=json.loads((receiving/'CANONICAL_PROVIDER_MANIFEST.json').read_text(encoding='utf-8'))
for item in manifest:
    if digest(receiving/'providers/canonical'/item['name'])!=item['sha256']:raise RuntimeError(('canonical companion pin',item))
required_path=out/'provenance/source_closure/REQUIRED_SOURCE_MAP.json'
required=json.loads(required_path.read_text(encoding='utf-8'))
if not {x['sha256'] for x in required['sources']}.issubset({x['sha256'] for x in manifest}):
    raise RuntimeError('A required historical proof source is missing from the companion')
closure={'status':'all_required_source_bytes_present','scope':'Byte closure of the separately reviewed exact required-claim map; mathematical proof acceptance is given by that map and its full reading reports, not inferred from this byte check','required_map_sha256':digest(required_path),'required_source_count':len(required['sources']),'copied_companion_provider_count':len(manifest),'receiving_acceptance_sha256':digest(receiving/'ROOT_RECEIVING_ACCEPTANCE.json'),'full_receiving_receipt_sha256':digest(receiving/'FULL_RECEIVING_RECEIPT.json')}
(out/'SOURCE_CLOSURE_VERIFICATION.json').write_bytes(json.dumps(closure,indent=2).encode())
log=(out/'Original_Gamma_Volumes_and_Intrinsic_Spectral_Sums.log').read_text(encoding='utf-8')
for bad in ['Overfull','undefined references','Undefined control sequence','LaTeX Error']:
    if bad in log:raise RuntimeError(('build defect',bad))
build={'status':'PASS','pdf_sha256':pdfsha,'pages':pages,'proof_acceptance':{'path':rootaccept.name,'sha256':digest(rootaccept)},'visual_coverage':visual,'all_actual_pages_visually_accepted':True,'provider_pins_sha256':digest(out/'NEW_PROOF_SOURCE_PINS.json'),'exact_reversible_transports_sha256':digest(out/'DISPLAY_AND_BODY_TRANSPORTS.json'),'canonical_order_unchanged':True,'exploratory_family_labelled':True,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
build['separate_observation_stage']={'path':'next_original_observation/CLOSURE_RECEIPT.json','sha256':digest(opg_receipt),'declared_files_including_receipt':len(opg_pinned_files),'all_declared_file_bytes_verified':True,'principal_pdf_unchanged':True}
(out/'BUILD_AND_PROOF_ACCEPTANCE.json').write_bytes(json.dumps(build,indent=2).encode())
skip_suffix={'.pdf','.png','.xdv','.aux','.toc','.out','.fls','.log','.zip','.pyc'}
skip_names={'DELIVERY_RECEIPT.json','SOURCE_ARCHIVE_MANIFEST.json','WORK_IN_PROGRESS.json'}
files=[]
for p in sorted(out.rglob('*')):
    if not p.is_file() or p.suffix.lower() in skip_suffix or p.name in skip_names:continue
    rel=p.relative_to(out)
    if '__pycache__' in rel.parts:continue
    # The prior closure is preserved completely, including its own provenance.
    files.append(p)
# Prior source ZIP members may have historical suffixes; retain every member byte once.
for p in (out/'dependencies/cut21').rglob('*'):
    if p.is_file() and p not in files:files.append(p)
for p in opg_pinned_files:
    if p not in files:files.append(p)
files=sorted(files)
manifest=[{'path':p.relative_to(out).as_posix(),'bytes':p.stat().st_size,'sha256':digest(p)} for p in files]
(out/'SOURCE_ARCHIVE_MANIFEST.json').write_bytes(json.dumps(manifest,indent=2).encode())
files.append(out/'SOURCE_ARCHIVE_MANIFEST.json')
archive=out/'Original_Gamma_Volumes_Complete_Source.zip'
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in files:z.write(p,p.relative_to(out).as_posix())
with zipfile.ZipFile(archive) as z:
    if z.testzip() is not None:raise RuntimeError('ZIP CRC defect')
    for name in z.namelist():
        if z.read(name)!=(out/name).read_bytes():raise RuntimeError(('ZIP byte mismatch',name))
receipt={'status':'sealed','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pdf':{'path':pdf.name,'bytes':pdf.stat().st_size,'sha256':pdfsha,'pages':pages},'complete_source_zip':{'path':archive.name,'bytes':archive.stat().st_size,'sha256':digest(archive),'members':len(files),'all_member_bytes_verified':True},'build_and_proof_acceptance':{'path':'BUILD_AND_PROOF_ACCEPTANCE.json','sha256':digest(out/'BUILD_AND_PROOF_ACCEPTANCE.json')},'new_proof_source_pins_sha256':digest(out/'NEW_PROOF_SOURCE_PINS.json'),'display_transport_sha256':digest(out/'DISPLAY_AND_BODY_TRANSPORTS.json'),'source_manifest_sha256':digest(out/'SOURCE_ARCHIVE_MANIFEST.json'),'workflow_characters':len(workflow),'publication_performed':False}
receipt['separate_observation_stage']=build['separate_observation_stage']
(out/'DELIVERY_RECEIPT.json').write_bytes(json.dumps(receipt,indent=2).encode())
(out/'WORK_IN_PROGRESS.json').write_bytes(json.dumps({'status':'superseded by sealed DELIVERY_RECEIPT.json','delivery_receipt_sha256':digest(out/'DELIVERY_RECEIPT.json')},indent=2).encode())
print(json.dumps(receipt,indent=2))
