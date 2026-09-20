from pathlib import Path
import json,hashlib
from PIL import Image,ImageOps,ImageDraw
import fitz
B=Path(__file__).resolve().parent
O=B/'output/pdf'
pdf=O/'REAL_PAIR_005.pdf'
doc=fitz.open(pdf)
pages=sorted((O/'rendered005').glob('page-*.png'))
assert len(pages)==len(doc)
rows=[]
for i,p in enumerate(doc):
    rows.append({'page':i+1,'external_links':[x['uri'] for x in p.get_links() if 'uri' in x]})
for start in range(0,len(pages),6):
    canvas=Image.new('RGB',(1260,1220),'#dddddd')
    for j,p in enumerate(pages[start:start+6]):
        left,top=(j%3)*420,(j//3)*610
        canvas.paste(ImageOps.contain(Image.open(p),(410,575)),(left+5,top+25))
        ImageDraw.Draw(canvas).text((left+8,top+5),'Page '+str(start+j+1),fill='black')
    canvas.save(O/f'contact_{start//6+1}.png')
verified=json.loads((B/'PROGRAMME_CITATION_TARGETS_005.json').read_text(encoding='utf-8'))['verified_targets']
links=[u for p in rows for u in p['external_links']]
assert all(v['url'] in links for v in verified)
out={'pages':len(doc),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
     'verified_programme_links_present':True,'page_links':rows,
     'rendering':'Every page rendered by Poppler at 90 dpi; contact sheets prepared for inspection.'}
(O/'PAGE_LINK_AUDIT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='page_links'},indent=2))
