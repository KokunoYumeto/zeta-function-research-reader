"""Preserve the reviewed candidate and repair exactly three math-space commands."""
from pathlib import Path
import json,shutil,re
from prepare_successor import STAGE,HISTORY,sha,row,save,verify_predecessor

pin='bf4e1c2a6d98140e0c25b305e60074918d92ba97f7f00ba689d0c6cf2da87397'
pdf=STAGE/'Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf'
assert sha(pdf)==pin
relative='tex/cohorts/cf/33_OCQ.tex'
path=STAGE/relative
old=r''' \Theta\phi(x)&=2\sum_{n\ge1}\phi(nx),\qquad
 \mathcal MF(s)=\int_0^\infty F(x)x^s\frac{dx}{x},\qquad
 Q=\mathscr B/\Theta V,\qquad A=\mathbb C[t],\\'''
new=old.replace(r'\qquad',r'\quad')
before=path.read_bytes()
text=before.decode('utf-8')
assert text.count(old)==1
after=text.replace(old,new)
assert after.replace(new,old)==text
strip=lambda s:re.sub(r'\\q(?:quad|uad)\b','',s)
assert strip(old)==strip(new)
history=STAGE/'history/cumulative_build_candidates'/pin
capture=[pdf,path,STAGE/'CURRENT_SOURCE_MANIFEST.json',STAGE/'README_CURRENT_EDITION.md',STAGE/'README_GRAPH_SUCCESSOR.md',
 STAGE/'provenance/ASSEMBLED_SOURCE_EXPECTATIONS.json',STAGE/'provenance/CURRENT_COMPILED_SOURCE_PINS.json',STAGE/'provenance/SOURCE_BUILD_READINESS.json',STAGE/'provenance/PREDECESSOR_PRESERVATION_CHECK.json',
 *[p for p in (STAGE/'build').iterdir() if p.is_file() and (p.name.startswith('reader.') or p.name.startswith('current-xelatex-') or p.name.endswith('BUILD_RECEIPT.json'))]]
for p in capture:
 t=history/p.relative_to(STAGE);t.parent.mkdir(parents=True,exist_ok=True)
 if t.exists(): assert t.read_bytes()==p.read_bytes()
 else: shutil.copy2(p,t)
baseline_original=HISTORY/relative
if not baseline_original.exists():
 baseline_original.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(path,baseline_original)
path.write_bytes(after.encode('utf-8'))
expected_path=STAGE/'provenance/ASSEMBLED_SOURCE_EXPECTATIONS.json'
expected=json.loads(expected_path.read_text(encoding='utf-8'));expected['files'][relative]=row(path);save(expected_path,expected)
receipt={'status':'exact_reversible_three_spacing_command_transport',
 'known_defective_candidate_sha256':pin,'defect':'Physical970 OCQ.1 third-row final bracket intersects equation tag.',
 'formula_changes':0,'tag_changes':0,'line_break_changes':0,
 'operations':[{'path':relative,'before':row(history/relative),'after':row(path),'old':old,'new':new,'count':1,
 'inverse_replay':'Exact complete UTF-8 source bytes recovered; only three qquad spacing commands become quad.'}],
 'history_pdf':{'path':str(history/pdf.name),'sha256':sha(history/pdf.name)},
 'source_expectations_sha256':sha(expected_path)}
save(STAGE/'provenance/OCQ_TAG_SPACING_TRANSPORT.json',receipt)
print(json.dumps({'receipt':str(STAGE/'provenance/OCQ_TAG_SPACING_TRANSPORT.json'),'sha256':sha(STAGE/'provenance/OCQ_TAG_SPACING_TRANSPORT.json'),'source':row(path),'baseline_preservation':verify_predecessor()['count']}))
