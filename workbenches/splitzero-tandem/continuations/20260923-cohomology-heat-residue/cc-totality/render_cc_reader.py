from pathlib import Path
import fitz,json
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parent
out=root/'rendered_cc_reader';out.mkdir(exist_ok=True)
doc=fitz.open(root/'FULL_LATTICE_CC_READER.pdf')
assert len(doc)>0,'PDF has no pages; wait for the active compiler before rendering.'
paths=[];outside=[]
for i,page in enumerate(doc):
    p=out/f'page-{i+1:03}.png'
    page.get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).save(p)
    paths.append(p)
    for b in page.get_text('dict')['blocks']:
        if b.get('type')!=0:continue
        for line in b['lines']:
            for span in line['spans']:
                x0,y0,x1,y1=span['bbox']
                if x0<0 or y0<0 or x1>page.rect.width or y1>page.rect.height:
                    outside.append(dict(page=i+1,text=span['text'],bbox=span['bbox']))
contacts=[]
for offset in range(0,len(paths),6):
    canvas=Image.new('RGB',(1240,2650),'#c9cdd3');draw=ImageDraw.Draw(canvas)
    for j,path in enumerate(paths[offset:offset+6]):
        im=Image.open(path).convert('RGB');im.thumbnail((590,840))
        x=15+(j%2)*620;y=28+(j//2)*880
        canvas.paste(im,(x,y));draw.text((x,y-18),f'Page {offset+j+1}',fill='black')
    contact=out/f'contact-{offset//6+1:02}.png';canvas.save(contact);contacts.append(str(contact))
receipt=dict(pages=len(doc),contacts=contacts,outside_page_text=outside,
    inspection='Rendering completed; human-visible model inspection recorded separately after image review.')
(out/'RENDER_RECEIPT.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps({'pages':len(doc),'contacts':len(contacts),'outside_page_text':outside}))
