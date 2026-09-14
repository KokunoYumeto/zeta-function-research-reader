from pathlib import Path
import subprocess,hashlib,json
root=Path(__file__).parent
pdf=Path(r'repository:/Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf')
poppler=r'local:user-profile/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe'
pages=[453,460,471,472,486,512,535,540,569,585,619,625,642,650,660]
(root/'zooms').mkdir(exist_ok=True)
rows=[]
for n in pages:
    out=root/'zooms'/f'page-{n:04d}'
    subprocess.run([poppler,'-f',str(n),'-l',str(n),'-r','150','-singlefile','-png',str(pdf),str(out)],check=True,stdout=subprocess.DEVNULL)
    p=out.with_suffix('.png')
    rows.append({'page':n,'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'dpi':150})
(root/'ZOOM_MANIFEST.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
print(len(rows))
