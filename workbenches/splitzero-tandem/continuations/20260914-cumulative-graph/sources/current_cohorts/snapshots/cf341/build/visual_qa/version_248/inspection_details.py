from pathlib import Path
from PIL import Image, ImageDraw
import json
import pdfplumber

Q=Path(__file__).resolve().parent
D=json.loads((Q/'baseline_page_mapping.json').read_text())
changed=set(D['new_or_changed_pages'])
middle=sorted(p for p in changed if 54<p<159)
for start in range(0,len(middle),9):
    nums=middle[start:start+9]
    sheet=Image.new('RGB',(1260,1845),'#dddddd'); draw=ImageDraw.Draw(sheet)
    for k,n in enumerate(nums):
        im=Image.open(Q/f'page-{n:03}.png').convert('RGB'); im.thumbnail((408,578))
        x=k%3*420+(420-im.width)//2; y=k//3*615+24
        sheet.paste(im,(x,y)); draw.text((k%3*420+10,k//3*615+6),f'PDF PAGE {n}',fill='black')
    sheet.save(Q/f'changed-middle-{start//9+1}.png')

crops=[]
with pdfplumber.open(Q.parents[1]/'Tau_Split_Zero_Total_Counterfactual.pdf') as doc:
    for n,page in enumerate(doc.pages,1):
        if n not in changed: continue
        vertical=[l for l in page.lines if abs(l['x1']-l['x0'])<0.6 and l['bottom']-l['top']>9]
        pairs=[]
        for a in vertical:
            for b in vertical:
                if b['x0']-a['x0']>20 and abs(a['top']-b['top'])<1 and abs(a['bottom']-b['bottom'])<1:
                    horizontal=[l for l in page.lines if l['x0']<=a['x0']+1 and l['x1']>=b['x0']-1 and (abs(l['top']-a['top'])<1 or abs(l['top']-a['bottom'])<1)]
                    if len(horizontal)>=2: pairs.append([a['x0'],a['top'],b['x0'],b['bottom']])
        if not pairs: continue
        im=Image.open(Q/f'page-{n:03}.png').convert('RGB'); scale=im.width/page.width
        for i,box in enumerate(pairs,1):
            crop=im.crop((max(0,int((box[0]-9)*scale)),max(0,int((box[1]-8)*scale)),min(im.width,int((page.width-38)*scale)),min(im.height,int((box[3]+8)*scale))))
            crops.append((n,i,box,crop))

sheet=Image.new('RGB',(1000,1700),'#dddddd'); draw=ImageDraw.Draw(sheet); y=10; sn=1
records=[]
for n,i,box,crop in crops:
    if y+crop.height+25>1680:
        sheet.crop((0,0,1000,y)).save(Q/f'boxed-details-{sn:02}.png'); sn+=1
        sheet=Image.new('RGB',(1000,1700),'#dddddd'); draw=ImageDraw.Draw(sheet); y=10
    draw.text((10,y),f'PDF PAGE {n} / BOX {i}',fill='black'); y+=20
    sheet.paste(crop,(10,y)); records.append({'page':n,'box':box,'detail_sheet':sn}); y+=crop.height+15
sheet.crop((0,0,1000,y)).save(Q/f'boxed-details-{sn:02}.png')
(Q/'boxed_detail_index.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
print(json.dumps({'middle_changed_pages':middle,'detected_boxed_expressions':len(crops),'boxed_detail_sheets':sn},indent=2))
