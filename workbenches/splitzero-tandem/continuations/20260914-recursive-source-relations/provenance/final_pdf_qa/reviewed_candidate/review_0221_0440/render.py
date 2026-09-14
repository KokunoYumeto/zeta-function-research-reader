from pathlib import Path
import hashlib, json, subprocess, time
from PIL import Image, ImageDraw, ImageFont
O=Path(r'workspace:\work\backpropagation_20260913\page_qa\review_0221_0440')
pdf=Path(r'repository:\Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf')
pin='a8264bef3b1256087f99708c2d06e4bf6c45aa41669fd10679c8f352b0153252'
assert hashlib.sha256(pdf.read_bytes()).hexdigest()==pin
(O/'pages').mkdir(exist_ok=True)
subprocess.run([r'local:user-profile\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe','-f','221','-l','440','-scale-to-x','840','-scale-to-y','-1','-png',str(pdf),str(O/'pages/page')],check=True)
font=ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf',20)
rows=[]
for start in range(221,441,12):
    pages=list(range(start,min(start+12,441)))
    sheet=Image.new('RGB',(1260,4*624),'#d0d0d0'); d=ImageDraw.Draw(sheet)
    for j,p in enumerate(pages):
        src=O/f'pages/page-{p:04}.png'
        im=Image.open(src).convert('RGB'); im.thumbnail((420,594))
        x=(j%3)*420;y=(j//3)*624
        d.text((x+8,y+3),f'PDF page {p}',font=font,fill='black')
        sheet.paste(im,(x,y+28))
    dst=O/f'sheet_{start:04}_{pages[-1]:04}.png';sheet.save(dst)
    rows.append({'file':dst.name,'pages':pages,'sha256':hashlib.sha256(dst.read_bytes()).hexdigest()})
    print(dst.name,flush=True)
assert hashlib.sha256(pdf.read_bytes()).hexdigest()==pin
(O/'RENDER_MANIFEST.json').write_text(json.dumps({'pdf':str(pdf),'pdf_sha256':pin,'range':[221,440],'renderer':'Poppler pdftoppm PNG width 840; contact thumbnails 420','sheets':rows,'pages':[{'page':p,'file':f'pages/page-{p:04}.png','sha256':hashlib.sha256((O/f'pages/page-{p:04}.png').read_bytes()).hexdigest()} for p in range(221,441)]},indent=2),encoding='utf-8')
print('RENDER_COMPLETE',flush=True)
