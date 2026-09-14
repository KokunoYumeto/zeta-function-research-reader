from pathlib import Path
import fitz, hashlib, json
from PIL import Image, ImageDraw, ImageFont
root=Path(r'workspace:\work\backpropagation_20260913\page_qa\review_0661_0880')
pdf=Path(r'repository:\Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf')
expected='a8264bef3b1256087f99708c2d06e4bf6c45aa41669fd10679c8f352b0153252'
assert hashlib.sha256(pdf.read_bytes()).hexdigest()==expected
font=ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf',20)
sheets=[]
for start in range(661,881,12):
    pages=list(range(start,min(881,start+12)))
    sheet=Image.new('RGB',(1260,4*624),'#c8c8c8')
    d=ImageDraw.Draw(sheet)
    for j,n in enumerate(pages):
        p=root/f'page-{n:04d}.png'
        im=Image.open(p).convert('RGB');im.thumbnail((414,588))
        x=(j%3)*420+(420-im.width)//2;y=(j//3)*624+30
        d.text(((j%3)*420+8,(j//3)*624+4),f'Actual page {n}',fill='black',font=font)
        sheet.paste(im,(x,y))
    dest=root/f'sheet_{start:04d}_{pages[-1]:04d}.png';sheet.save(dest)
    sheets.append({'path':str(dest),'pages':pages,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()})
doc=fitz.open(pdf)
geometry=[]
for n in range(661,881):
    pg=doc[n-1];data=pg.get_text('dict');spans=[s for b in data['blocks'] if 'lines' in b for l in b['lines'] for s in l['spans']]
    anomalies=[{'text':s['text'],'bbox':s['bbox']} for s in spans if s['bbox'][0]<30 or s['bbox'][2]>pg.rect.width-20 or s['bbox'][1]<15 or s['bbox'][3]>pg.rect.height-15 or '\ufffd' in s['text'] or '\u25a0' in s['text']]
    geometry.append({'page':n,'size':list(pg.rect),'anomalies':anomalies,'first_spans':[s['text'] for s in spans[:3]],'last_spans':[s['text'] for s in spans[-3:]]})
(root/'SHEETS.json').write_text(json.dumps(sheets,indent=2))
(root/'GEOMETRY.json').write_text(json.dumps(geometry,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps({'sheets':len(sheets),'pages':220,'anomalous_pages':[x['page'] for x in geometry if x['anomalies']]}))

