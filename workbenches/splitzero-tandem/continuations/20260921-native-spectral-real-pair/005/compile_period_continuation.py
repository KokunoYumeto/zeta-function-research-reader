from pathlib import Path
import subprocess,hashlib,json,re
B=Path(__file__).resolve().parent;O=B/'texcheck_period_061';O.mkdir(exist_ok=True)
passes=[]
for j in [1,2]:
    p=subprocess.run(['pdflatex','-draftmode','-interaction=nonstopmode','-halt-on-error',
      '-output-directory='+str(O),'FABLE_TO_ORIGINAL_CONDUCTOR.tex'],cwd=B,
      stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=180)
    (O/f'compile_pass{j}.txt').write_bytes(p.stdout)
    passes.append({'pass':j,'exit_code':p.returncode})
    if p.returncode:print(p.stdout.decode('utf-8',errors='replace')[-7000:]);raise SystemExit(p.returncode)
log=(O/'FABLE_TO_ORIGINAL_CONDUCTOR.log').read_text(encoding='utf-8',errors='replace')
missing=re.findall(r'LaTeX Warning: (?:Citation|Reference).*undefined',log)
assert not missing,missing
out={'passes':passes,'principal_sha256':hashlib.sha256((B/'FABLE_TO_ORIGINAL_CONDUCTOR.tex').read_bytes()).hexdigest(),
 'unresolved_citations_or_references':missing,'overfull_boxes':log.count('Overfull'),
 'duplicate_destination_warnings':log.count('destination with the same identifier'),
 'pdf_generated':False,'scope':'Draft source compilation; no PDF layout claim. All three new scientific figures rendered and visually inspected separately.'}
(O/'COMPILATION_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
