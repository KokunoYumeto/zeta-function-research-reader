from pathlib import Path
from PIL import Image, ImageDraw
import json
q=Path(__file__).resolve().parent
mapping=json.loads((q/'baseline_page_mapping.json').read_text())
nums=[n for n in mapping['new_or_changed_pages'] if n>95]
for start in range(0,len(nums),9):
    batch=nums[start:start+9]
    sheet=Image.new('RGB',(1260,1845),'#dddddd'); draw=ImageDraw.Draw(sheet)
    for k,n in enumerate(batch):
        im=Image.open(q/f'page-{n:03}.png').convert('RGB'); im.thumbnail((408,578))
        x=k%3*420+(420-im.width)//2; y=k//3*615+24
        sheet.paste(im,(x,y)); draw.text((k%3*420+10,k//3*615+6),f'PDF PAGE {n}',fill='black')
    sheet.save(q/f'changed-remainder-341-{start//9+1:02}.png')
print(json.dumps({'pages':nums,'sheets':(len(nums)+8)//9},indent=2))
