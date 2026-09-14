from pathlib import Path
import subprocess, hashlib, json
from PIL import Image, ImageDraw, ImageFont
import fitz

ROOT=Path(__file__).parent
PDF=Path(r'repository:/Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf')
SHA='a8264bef3b1256087f99708c2d06e4bf6c45aa41669fd10679c8f352b0153252'
assert hashlib.sha256(PDF.read_bytes()).hexdigest()==SHA
(ROOT/'pages').mkdir(exist_ok=True)
(ROOT/'sheets').mkdir(exist_ok=True)
poppler=r'local:user-profile/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe'
subprocess.run([poppler,'-f','441','-l','660','-r','90','-png',str(PDF),str(ROOT/'pages'/'page')],check=True,stdout=subprocess.DEVNULL)
font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',18)
records=[]
for start in range(441,661,12):
    nums=list(range(start,min(start+12,661)))
    sheet=Image.new('RGB',(1260,2480),'#cccccc')
    draw=ImageDraw.Draw(sheet)
    for i,n in enumerate(nums):
        image_path=ROOT/'pages'/f'page-{n:04d}.png'
        if not image_path.exists():
            image_path=ROOT/'pages'/f'page-{n}.png'
        img=Image.open(image_path).convert('RGB')
        img.thumbnail((410,590))
        x=(i%3)*420+(420-img.width)//2
        y=(i//3)*620+27
        sheet.paste(img,(x,y))
        draw.text(((i%3)*420+12,(i//3)*620+4),f'Actual PDF page {n}',fill='black',font=font)
    path=ROOT/'sheets'/f'sheet_{nums[0]:04d}_{nums[-1]:04d}.png'
    sheet.save(path)
    records.append({'path':str(path),'pages':nums,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
doc=fitz.open(PDF)
anomalies=[]
for n in range(441,661):
    page=doc[n-1]
    bad=[]
    for block in page.get_text('dict')['blocks']:
        for line in block.get('lines',[]):
            for span in line['spans']:
                x0,y0,x1,y1=span['bbox']
                if x0 < 0 or y0 < 0 or x1 > page.rect.width or y1 > page.rect.height or '\ufffd' in span['text']:
                    bad.append({'bbox':span['bbox'],'text':span['text']})
    if bad: anomalies.append({'page':n,'findings':bad})
manifest={'pdf':str(PDF),'sha256':SHA,'pages':list(range(441,661)),'renderer':'Poppler pdftoppm 90 DPI RGB','contact_sheet_cell':[420,620],'sheets':records,'geometry_anomalies':anomalies,'page_images':[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted((ROOT/'pages').glob('*.png'))]}
(ROOT/'RENDER_MANIFEST.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(json.dumps({'sheets':len(records),'pages':len(manifest['page_images']),'anomalies':anomalies}))
