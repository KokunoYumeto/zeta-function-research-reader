"""Render the complete reader and make contact sheets for visual review."""
from pathlib import Path
import fitz
from PIL import Image, ImageOps, ImageDraw

B=Path(__file__).resolve().parent
src=B/'output/pdf/ACTUAL_XI_UNIFORM_CONDUCTOR.pdf'
out=B/'output/pdf/rendered011'; out.mkdir(exist_ok=True)
doc=fitz.open(src)
pages=[]
for i,page in enumerate(doc):
    target=out/f'page-{i+1:02}.png'
    page.get_pixmap(matrix=fitz.Matrix(1.15,1.15),alpha=False).save(target)
    pages.append(target)
for start in range(0,len(pages),4):
    sheet=Image.new('RGB',(1200,1680),'#dce2e6')
    draw=ImageDraw.Draw(sheet)
    for j,p in enumerate(pages[start:start+4]):
        im=Image.open(p).convert('RGB')
        im.thumbnail((580,790))
        x=(j%2)*600+(600-im.width)//2
        y=(j//2)*840+30
        sheet.paste(im,(x,y))
        draw.text(((j%2)*600+12,(j//2)*840+8),f'Page {start+j+1}',fill='black')
    sheet.save(out/f'contact-{start//4+1:02}.png')
text='\n'.join(p.get_text() for p in doc)
(out/'reader-text.txt').write_text(text,encoding='utf-8')
assert 'Levent' in doc[0].get_text()
assert 'Alp' in doc[0].get_text()
print({'pages':len(doc),'levent_mentions':text.count('Levent'),'contact_sheets':(len(pages)+3)//4})
