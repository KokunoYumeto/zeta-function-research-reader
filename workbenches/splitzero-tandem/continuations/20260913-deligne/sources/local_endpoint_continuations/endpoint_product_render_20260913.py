"""Render the final standalone PDF and make contact sheets for inspection."""
import hashlib,json,subprocess
from pathlib import Path
from PIL import Image,ImageOps,ImageDraw
from pypdf import PdfReader
base=Path(__file__).resolve().parent
pdf=base/'endpoint_product_sharpening_20260913.pdf'
qa=base/'endpoint_product_pdf_qa_20260913'
qa.mkdir(exist_ok=True)
subprocess.run(['pdftoppm','-r','100','-png',str(pdf),str(qa/'page')],check=True,capture_output=True)
pages=sorted(qa.glob('page-*.png'))
count=len(PdfReader(pdf).pages)
if len(pages)!=count:raise RuntimeError('Rendered-page count mismatch')
contacts=[]
for start in range(0,count,4):
    canvas=Image.new('RGB',(1400,2040),'#d5d5d5')
    for j,path in enumerate(pages[start:start+4]):
        im=Image.open(path).convert('RGB');im.thumbnail((680,970))
        x=(j%2)*700+(700-im.width)//2;y=(j//2)*1020+25
        canvas.paste(im,(x,y));ImageDraw.Draw(canvas).text(((j%2)*700+20,(j//2)*1020+5),f'Physical PDF page {start+j+1}',fill='black')
    path=qa/f'contact-{start+1:02d}-{min(start+4,count):02d}.jpg'
    canvas.save(path,quality=94);contacts.append(path.name)
def pin(path):return {'file':path.name,'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
receipt={'schema':'endpoint-product-pdf-render-v1','pdf':pin(pdf),'page_count':count,'pages':[pin(p) for p in pages],'contacts':[pin(qa/p) for p in contacts],'visually_reviewed':False}
(qa/'render_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'page_count':count,'contacts':contacts,'pdf_sha256':receipt['pdf']['sha256']}))
