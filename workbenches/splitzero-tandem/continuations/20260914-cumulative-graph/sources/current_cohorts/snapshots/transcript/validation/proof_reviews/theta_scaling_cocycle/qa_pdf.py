from pathlib import Path
import json
from PIL import Image,ImageOps,ImageDraw
import fitz

WORK=Path(__file__).resolve().parent
ROOT=WORK.parents[2]
PDF=ROOT/'output/tau_f1_transcript_audit_2026-09-13/proofs/theta_scaling_cocycle.pdf'
pages=sorted(WORK.glob('page-*.png'))
for start in range(0,len(pages),6):
    sheet=Image.new('RGB',(1650,1480),'#dedede')
    draw=ImageDraw.Draw(sheet)
    for offset,path in enumerate(pages[start:start+6]):
        img=Image.open(path).convert('RGB')
        img.thumbnail((540,710))
        x=(offset%3)*550+(550-img.width)//2
        y=(offset//3)*740+25
        sheet.paste(img,(x,y))
        draw.text((x,y-18),f'Page {start+offset+1}',fill='black')
    sheet.save(WORK/f'contact_{start//6+1}.png')
doc=fitz.open(PDF)
records=[]
for n,page in enumerate(doc):
    text=page.get_text()
    records.append({'page':n+1,'characters':len(text),
                    'tags':[tag for tag in ('(10)','(21)','(28a)','(36)','(41)','(44)','(46)') if tag in text]})
    if '\ufffd' in text:
        raise RuntimeError(f'Unicode replacement character on page {n+1}')
if len(pages)!=len(doc):
    raise RuntimeError('Not all pages rendered')
(WORK/'pdf_text.txt').write_text('\n\f\n'.join(p.get_text() for p in doc),encoding='utf-8')
(WORK/'pdf_page_records.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
print(json.dumps(records,indent=2))
