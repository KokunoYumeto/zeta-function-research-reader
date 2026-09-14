from pathlib import Path
import hashlib,json,subprocess
from PIL import Image, ImageDraw, ImageFont
BASE=Path(__file__).parent
PDF=Path(r'repository:\Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf')
PIN='a8264bef3b1256087f99708c2d06e4bf6c45aa41669fd10679c8f352b0153252'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(PDF)==PIN
(BASE/'pages').mkdir(exist_ok=True)
(BASE/'sheets').mkdir(exist_ok=True)
subprocess.run(['pdftoppm','-f','881','-l','1100','-scale-to-x','420','-scale-to-y','-1','-png',str(PDF),str(BASE/'pages'/'page')],check=True)
font=ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf',20)
sheets=[]
for start in range(881,1101,12):
    pages=list(range(start,min(start+12,1101)))
    im=Image.new('RGB',(1260,2512),'#ddd')
    d=ImageDraw.Draw(im)
    for n,p in enumerate(pages):
        x=(n%3)*420; y=(n//3)*628
        d.text((x+12,y+4),f'PDF page {p}',fill='black',font=font)
        page=Image.open(BASE/'pages'/f'page-{p:04d}.png').convert('RGB')
        im.paste(page,(x,y+30))
    name=f'sheet-{pages[0]:04d}-{pages[-1]:04d}.png'
    im.save(BASE/'sheets'/name)
    sheets.append({'path':'sheets/'+name,'pages':pages,'sha256':sha(BASE/'sheets'/name)})
assert sha(PDF)==PIN
(BASE/'RENDER_MANIFEST.json').write_text(json.dumps({'pdf':str(PDF),'pdf_sha256':PIN,'renderer':'pdftoppm','pages':list(range(881,1101)),'sheets':sheets,'page_images':[{'path':str(p.relative_to(BASE)),'sha256':sha(p)} for p in sorted((BASE/'pages').glob('*.png'))]},indent=2))
print(json.dumps({'pages':220,'sheets':len(sheets),'pdf_sha256':PIN}))
