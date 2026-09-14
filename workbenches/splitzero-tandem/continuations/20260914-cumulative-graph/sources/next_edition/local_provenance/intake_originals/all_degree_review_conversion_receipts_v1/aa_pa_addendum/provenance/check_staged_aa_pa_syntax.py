"""Compile the three actually staged whole wrappers; keep output in this lane."""
from pathlib import Path
import hashlib,json,re,shutil,subprocess
ROOT=Path(__file__).resolve().parent
STAGE=ROOT.parent/'cumulative_next_edition_staging_20260913_v19'
READER=STAGE/'reader'
RECORD=STAGE/'ALL_DEGREE_REVIEW_CONVERSION_STAGE.json'
OUT=ROOT/'syntax_aa_pa_staged'
assert not OUT.exists()
record=json.loads(RECORD.read_text(encoding='utf-8'))
assert len(record['readable_routes'])==3
for row in record['readable_routes']:
    raw=(READER/row['whole_wrapper']).read_bytes()
    assert len(raw)==row['bytes'] and hashlib.sha256(raw).hexdigest()==row['sha256']
baseline=ROOT.parent/'cumulative_deligne_build_20260913_v18/tex/main.tex'
preamble=baseline.read_text(encoding='utf-8').split(r'\begin{document}',1)[0]
master=preamble+'\n\\begin{document}\n'+''.join(
    '\\input{'+row['whole_wrapper']+'}\n' for row in record['readable_routes'])+'\\end{document}\n'
OUT.mkdir();tex=OUT/'staged_syntax.tex';tex.write_text(master,encoding='utf-8',newline='')
cmd=[shutil.which('xelatex'),'-interaction=nonstopmode','-halt-on-error','-file-line-error',
     '-output-directory='+OUT.as_posix(),tex.as_posix()]
p=subprocess.run(cmd,cwd=READER,capture_output=True)
(OUT/'engine_output.log').write_bytes(p.stdout+b'\n'+p.stderr)
log=(OUT/'staged_syntax.log').read_text(encoding='utf-8',errors='replace')
result={'schema':'staged-all-degree-whole-source-syntax-check-v1',
    'source_stage_receipt_sha256':hashlib.sha256(RECORD.read_bytes()).hexdigest(),
    'selected_whole_wrappers':[r['whole_wrapper'] for r in record['readable_routes']],
    'exit_code':p.returncode,'overfull_boxes':re.findall(r'Overfull \\hbox[^\n]*',log),
    'missing_glyphs':re.findall(r'Missing character[^\n]*',log),
    'undefined_controls':'Undefined control sequence' in log,
    'latex_errors':re.findall(r'^.*(?:LaTeX Error:|^! ).*$',log,re.M),
    'pdf_created':(OUT/'staged_syntax.pdf').is_file(),'visual_acceptance':False,
    'scope':'All three complete rebased wrappers compiled from their actual staged paths. Every compiler output remains in the source-conversion lane; no existing reader file is changed. No final cumulative PDF or visual acceptance is claimed.'}
dest=OUT/'SYNTAX_RECEIPT.json';dest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert not any((result['exit_code'],result['overfull_boxes'],result['missing_glyphs'],result['undefined_controls'],result['latex_errors'])),json.dumps(result)
print(json.dumps({'receipt':str(dest),'bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),**result}))
