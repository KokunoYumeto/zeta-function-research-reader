from pathlib import Path
import fitz, hashlib, json
W=Path(__file__).resolve().parent
PDF=W.parents[2]/'output/Split_Zero_Recursive_Integration_2026-09-13/repository/Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf'
PIN='8bbd9da0d566fc5c5364a50da9b0976f9fcc21834de47822374966707b17c273'
assert hashlib.sha256(PDF.read_bytes()).hexdigest()==PIN
D=fitz.open(PDF); out=W/'first_corrected_inspection';out.mkdir(exist_ok=True)
numbers={811,1136,1137,1138}
records=[]
for n in sorted(numbers):
    p=out/f'page_{n:04d}.png'; D[n-1].get_pixmap(matrix=fitz.Matrix(2,2),alpha=False).save(p)
    records.append({'page':n,'image':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'text':D[n-1].get_text()[:200]})
(out/'RENDER_MANIFEST.json').write_text(json.dumps({'pdf_sha256':PIN,'pages':records},indent=2)+'\n')
print(json.dumps(records,indent=2))
