from pathlib import Path
import subprocess, hashlib, json
from PIL import Image, ImageDraw, ImageFont
P=Path(__file__).parent
pdf=Path(r'repository:\Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf')
expected='a8264bef3b1256087f99708c2d06e4bf6c45aa41669fd10679c8f352b0153252'
assert hashlib.sha256(pdf.read_bytes()).hexdigest()==expected
(P/'thumbs').mkdir(exist_ok=True)
(P/'sheets').mkdir(exist_ok=True)
(P/'zooms').mkdir(exist_ok=True)
poppler=r'local:user-profile\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe'
subprocess.run([poppler,'-f','1101','-l','1320','-scale-to-x','420','-scale-to-y','-1','-png',str(pdf),str(P/'thumbs'/'page')],check=True)
font=ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf',18)
for start in range(1101,1321,12):
 pages=list(range(start,min(start+12,1321)))
 sheet=Image.new('RGB',(1680,3*626),(220,225,230)); d=ImageDraw.Draw(sheet)
 for i,page in enumerate(pages):
  pic=Image.open(P/'thumbs'/f'page-{page}.png').convert('RGB')
  x=(i%4)*420;y=(i//4)*626
  d.text((x+10,y+3),f'PDF page {page}',font=font,fill='black')
  sheet.paste(pic,(x,y+27))
 sheet.save(P/'sheets'/f'sheet_{start}_{pages[-1]}.png')
 print(f'sheet_{start}_{pages[-1]}.png',flush=True)
assert hashlib.sha256(pdf.read_bytes()).hexdigest()==expected
(P/'RENDER_MANIFEST.json').write_text(json.dumps({'pdf':str(pdf),'pdf_sha256':expected,'page_range':[1101,1320],'renderer':'Poppler pdftoppm','files':[{'path':str(f.relative_to(P)),'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in sorted(P.rglob('*.png'))]},indent=2))
