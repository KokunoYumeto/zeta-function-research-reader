from pathlib import Path
import hashlib, json, fitz
from PIL import Image, ImageDraw

HERE=Path(__file__).resolve().parent
PDF=Path(r'repository:\Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf')
EXPECTED='a8264bef3b1256087f99708c2d06e4bf6c45aa41669fd10679c8f352b0153252'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(PDF)==EXPECTED
doc=fitz.open(PDF)
assert len(doc)==1625
(HERE/'pages').mkdir(exist_ok=True)
(HERE/'sheets').mkdir(exist_ok=True)
manifest={'pdf':str(PDF),'pdf_sha256':EXPECTED,'pdf_pages':len(doc),'assigned_pages':list(range(1,221)),'pages':[],'sheets':[]}
for n in range(1,221):
 p=HERE/'pages'/f'page_{n:04d}.png'
 pix=doc[n-1].get_pixmap(matrix=fitz.Matrix(2,2),alpha=False)
 pix.save(p)
 manifest['pages'].append({'page':n,'path':str(p),'sha256':sha(p),'width':pix.width,'height':pix.height})
 if n%25==0: print('rendered',n,flush=True)
for start in range(1,221,12):
 nums=list(range(start,min(221,start+12)))
 sheet=Image.new('RGB',(1800,3520),'#dddddd')
 draw=ImageDraw.Draw(sheet)
 for k,n in enumerate(nums):
  im=Image.open(HERE/'pages'/f'page_{n:04d}.png').convert('RGB')
  im.thumbnail((594,850),Image.Resampling.LANCZOS)
  x=(k%3)*600+(600-im.width)//2; y=(k//3)*880+26
  sheet.paste(im,(x,y)); draw.text(((k%3)*600+14,(k//3)*880+7),f'PDF page {n}',fill='black')
 path=HERE/'sheets'/f'sheet_{start:04d}_{nums[-1]:04d}.png'
 sheet.save(path)
 manifest['sheets'].append({'pages':nums,'path':str(path),'sha256':sha(path)})
assert sha(PDF)==EXPECTED
(HERE/'RENDER_MANIFEST.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print('complete',flush=True)
