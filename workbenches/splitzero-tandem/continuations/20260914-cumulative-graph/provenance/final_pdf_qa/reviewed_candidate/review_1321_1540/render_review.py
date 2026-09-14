from pathlib import Path
import hashlib,json,subprocess
from PIL import Image, ImageOps, ImageDraw, ImageFont
import fitz

ROOT=Path(__file__).resolve().parent
PDF=Path(r'repository:\Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf')
EXPECTED='a8264bef3b1256087f99708c2d06e4bf6c45aa41669fd10679c8f352b0153252'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(PDF)==EXPECTED
(ROOT/'pages').mkdir(exist_ok=True)
(ROOT/'sheets').mkdir(exist_ok=True)
subprocess.run(['pdftoppm','-r','100','-f','1321','-l','1540','-png',str(PDF),str(ROOT/'pages'/'page')],check=True)
font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',20)
records=[]
for start in range(1321,1541,12):
    pages=list(range(start,min(start+12,1541)))
    sheet=Image.new('RGB',(1260,4*625),'#d8d8d8')
    draw=ImageDraw.Draw(sheet)
    for i,p in enumerate(pages):
        fp=ROOT/'pages'/f'page-{p}.png'
        im=Image.open(fp).convert('RGB')
        thumb=ImageOps.contain(im,(414,590))
        x=(i%3)*420+(420-thumb.width)//2; y=(i//3)*625+31
        sheet.paste(thumb,(x,y)); draw.text(((i%3)*420+8,(i//3)*625+5),f'Actual PDF page {p}',fill='black',font=font)
    target=ROOT/'sheets'/f'sheet_{pages[0]}_{pages[-1]}.png'
    sheet.save(target)
    records.append({'pages':pages,'path':str(target),'sha256':sha(target)})
assert sha(PDF)==EXPECTED
doc=fitz.open(PDF)
metrics=[]
for p in range(1321,1541):
    page=doc[p-1]
    text=page.get_text()
    metrics.append({'page':p,'page_png_sha256':sha(ROOT/'pages'/f'page-{p}.png'),'replacement_characters':text.count('\ufffd'),'width':page.rect.width,'height':page.rect.height,'footer_text':page.get_text(clip=fitz.Rect(0,785,page.rect.width,page.rect.height)).strip()})
(ROOT/'RENDER_MANIFEST.json').write_text(json.dumps({'pdf':str(PDF),'pdf_sha256':EXPECTED,'render_engine':'Poppler pdftoppm','dpi':100,'contact_sheet_cell_width':420,'sheets':records,'pages':metrics},indent=2),encoding='utf-8')
print(json.dumps({'pdf_sha256':EXPECTED,'pages':len(metrics),'sheets':len(records)}))
