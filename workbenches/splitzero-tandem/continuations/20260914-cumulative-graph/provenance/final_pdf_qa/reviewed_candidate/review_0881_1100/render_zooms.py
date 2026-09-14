from pathlib import Path
import subprocess,json,hashlib
BASE=Path(__file__).parent
PDF=Path(r'repository:\Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf')
pages=[896,925,979,988,1007,1024,1047,1074,1086,1092,1100]
(BASE/'zooms').mkdir(exist_ok=True)
for p in pages:
    subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-r','144','-singlefile','-png',str(PDF),str(BASE/'zooms'/f'page-{p:04d}')],check=True)
(BASE/'ZOOM_RENDER_MANIFEST.json').write_text(json.dumps({'pages':pages,'dpi':144,'renderer':'pdftoppm','images':[{'path':str(p.relative_to(BASE)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted((BASE/'zooms').glob('*.png'))]},indent=2))
print('Rendered full-page zooms:',pages)
