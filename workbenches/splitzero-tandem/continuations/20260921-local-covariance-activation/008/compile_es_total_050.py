"""Compile cumulative TeX without generating a PDF; retain full diagnostic logs."""
from pathlib import Path
import subprocess,hashlib,json,re
B=Path(__file__).resolve().parent
O=B/'texcheck_es_total_050';O.mkdir(exist_ok=True)
passes=[]
for j in [1,2]:
    p=subprocess.run(['pdflatex','-draftmode','-interaction=nonstopmode','-halt-on-error',
                      '-output-directory='+str(O),'FABLE_TO_ORIGINAL_CONDUCTOR.tex'],
                     cwd=B,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=180)
    (O/f'compile_pass{j}.txt').write_bytes(p.stdout)
    text=p.stdout.decode('utf-8',errors='replace')
    passes.append({'pass':j,'exit_code':p.returncode})
    if p.returncode:
        print(text[-6500:]);raise SystemExit(p.returncode)
log=(O/'FABLE_TO_ORIGINAL_CONDUCTOR.log').read_text(encoding='utf-8',errors='replace')
missing=re.findall(r'LaTeX Warning: (?:Citation|Reference).*undefined',log)
if missing:raise ValueError(missing)
report={'passes':passes,'principal_sha256':hashlib.sha256((B/'FABLE_TO_ORIGINAL_CONDUCTOR.tex').read_bytes()).hexdigest(),
 'unresolved_citations_or_references':missing,'overfull_boxes':log.count('Overfull'),
 'duplicate_destination_warnings':log.count('destination with the same identifier'),
 'pdf_generated':False,'scope':'Source compilation only. No PDF layout claim; scientific figures are separately rendered and visually inspected.'}
(O/'COMPILATION_RECEIPT.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))

