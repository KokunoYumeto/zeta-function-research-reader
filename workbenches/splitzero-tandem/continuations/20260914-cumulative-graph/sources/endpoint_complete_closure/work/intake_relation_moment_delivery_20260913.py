from pathlib import Path, PurePosixPath
import hashlib, json, zipfile, datetime
W=Path('workspace:')
R=W/'output/split_zero_rh_tandem_2026-09-12'
z=Path('corpus:research-library/Chatnotes/CHat translates and clean/Noether Multilingual/Tau_Relation_Moment_Control_2026-09-13.zip')
out=R/'sources/web_relation_moment_delivery'
sha=lambda b:hashlib.sha256(b).hexdigest()
records=[]
with zipfile.ZipFile(z) as f:
 for i in f.infolist():
  p=PurePosixPath(i.filename)
  if p.is_absolute() or '..' in p.parts or ':' in i.filename or '\\' in i.filename: raise RuntimeError(i.filename)
  if (i.external_attr>>16)&0o170000==0o120000: raise RuntimeError('symlink')
  target=out.joinpath(*p.parts)
  target.resolve().relative_to(out.resolve())
  if i.is_dir(): target.mkdir(parents=True,exist_ok=True);continue
  data=f.read(i);target.parent.mkdir(parents=True,exist_ok=True)
  if target.exists() and target.read_bytes()!=data:raise RuntimeError('existing differs')
  if not target.exists():target.write_bytes(data)
  records.append(dict(path=i.filename,bytes=len(data),sha256=sha(data)))
receipt={'schema':'relation-moment-exact-intake-v1','archive':str(z),'archive_bytes':z.stat().st_size,'archive_sha256':sha(z.read_bytes()),'members':records,'all_exact':True}
rp=W/'work/relation_moment_archive_receipt_20260913.json'
rp.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
log=W/'work/relation_moment_intake_logbook_20260913.md'
if not log.exists():log.write_text('# Relation-moment intake logbook\n\nFull user paste is retained by root in the verbatim session log. Assigned scope: independent complete source audit, exact extraction, new finite checks only, complete supplementary proof and portable closure. No main, Zenodo, global TeX, frozen release, or Lean mutation.\n',encoding='utf-8')
with log.open('a',encoding='utf-8') as f:f.write('\n'+datetime.datetime.now().isoformat()+' Exact extraction: '+str(len(records))+' files; archive SHA256 '+receipt['archive_sha256']+'.\n')
print(json.dumps(receipt,indent=2))
