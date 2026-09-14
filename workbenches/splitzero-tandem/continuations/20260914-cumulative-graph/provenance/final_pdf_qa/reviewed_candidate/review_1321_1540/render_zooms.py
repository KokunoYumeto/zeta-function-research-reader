from pathlib import Path
import subprocess,json,hashlib
ROOT=Path(__file__).resolve().parent
PDF=Path(r'repository:\Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf')
pages=[1352,1368,1398,1466,1506,1523]
(ROOT/'zooms').mkdir(exist_ok=True)
records=[]
for p in pages:
    prefix=ROOT/'zooms'/f'page-{p}'
    subprocess.run(['pdftoppm','-r','200','-f',str(p),'-l',str(p),'-singlefile','-png',str(PDF),str(prefix)],check=True)
    fp=prefix.with_suffix('.png')
    records.append({'page':p,'path':str(fp),'dpi':200,'sha256':hashlib.sha256(fp.read_bytes()).hexdigest()})
(ROOT/'ZOOM_MANIFEST.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
print(json.dumps({'zooms':len(records)}))
