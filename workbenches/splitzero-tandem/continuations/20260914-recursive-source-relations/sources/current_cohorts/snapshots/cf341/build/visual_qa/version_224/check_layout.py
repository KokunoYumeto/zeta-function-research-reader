from pathlib import Path
from collections import defaultdict
import hashlib, json, math, re
import pdfplumber
from PIL import Image, ImageOps, ImageDraw

root = Path(__file__).resolve().parents[2]
out = Path(__file__).resolve().parent
pdf = root / 'Tau_Split_Zero_Total_Counterfactual.pdf'
rows = []
with pdfplumber.open(pdf) as doc:
    for n, page in enumerate(doc.pages, 1):
        chars = [c for c in page.chars if c.get('text', '').strip()]
        bad = []
        missing = []
        duplicates = []
        seen = {}
        collisions = []
        grid = defaultdict(list)
        for i, c in enumerate(chars):
            x0, x1, y0, y1 = c['x0'], c['x1'], c['top'], c['bottom']
            if x0 < -0.5 or y0 < -0.5 or x1 > page.width + 0.5 or y1 > page.height + 0.5:
                bad.append({'text':c['text'], 'bbox':[x0,y0,x1,y1]})
            if '\ufffd' in c['text'] or '(cid:' in c['text']:
                missing.append({'text':c['text'], 'bbox':[x0,y0,x1,y1]})
            key=(c['text'], round(x0,2), round(y0,2), round(x1,2), round(y1,2))
            if key in seen:
                duplicates.append({'text':c['text'], 'bbox':[x0,y0,x1,y1]})
            seen[key]=i
            nearby=set()
            for gx in range(math.floor(x0/15), math.floor(x1/15)+1):
                for gy in range(math.floor(y0/15), math.floor(y1/15)+1):
                    nearby.update(grid[(gx,gy)])
            for j in nearby:
                d=chars[j]
                iw=max(0,min(x1,d['x1'])-max(x0,d['x0']))
                ih=max(0,min(y1,d['bottom'])-max(y0,d['top']))
                area=min((x1-x0)*(y1-y0), (d['x1']-d['x0'])*(d['bottom']-d['top']))
                if area > 1 and iw*ih/area > 0.92 and c['text'] != d['text']:
                    collisions.append({'text':[d['text'],c['text']], 'bbox':[min(x0,d['x0']),min(y0,d['top']),max(x1,d['x1']),max(y1,d['bottom'])]})
            for gx in range(math.floor(x0/15), math.floor(x1/15)+1):
                for gy in range(math.floor(y0/15), math.floor(y1/15)+1):
                    grid[(gx,gy)].append(i)
        body=[c for c in chars if 60 < c['top'] < 790]
        bbox=[min(c['x0'] for c in chars),min(c['top'] for c in chars),max(c['x1'] for c in chars),max(c['bottom'] for c in chars)] if chars else None
        bodybbox=[min(c['x0'] for c in body),min(c['top'] for c in body),max(c['x1'] for c in body),max(c['bottom'] for c in body)] if body else None
        text=page.extract_text() or ''
        (out / f'text-{n:03}.txt').write_text(text, encoding='utf-8')
        rows.append({'page':n, 'width':page.width, 'height':page.height, 'cropbox':page.cropbox, 'chars':len(chars), 'bbox':bbox, 'body_bbox':bodybbox, 'outside_crop':bad, 'missing_glyph_candidates':missing, 'duplicate_chars':duplicates, 'high_overlap_candidates':collisions})

logs=(root/'build'/'main.log').read_text(encoding='utf-8', errors='replace')
report={'pdf':str(pdf), 'sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(), 'pages':len(rows), 'page_results':rows, 'log_layout_warnings':[line for line in logs.splitlines() if re.search(r'Missing character|Overfull|Underfull|Undefined|undefined references|undefined citations',line)]}
(out/'layout_metrics.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
imgs=sorted(out.glob('page-*.png'))
for start in range(0,len(imgs),9):
    sheet=Image.new('RGB',(1260,1845),'#dddddd')
    draw=ImageDraw.Draw(sheet)
    for k,path in enumerate(imgs[start:start+9]):
        thumb=Image.open(path).convert('RGB')
        thumb.thumbnail((408,578))
        x=(k%3)*420+(420-thumb.width)//2
        y=(k//3)*615+24
        sheet.paste(thumb,(x,y))
        draw.text(((k%3)*420+10,(k//3)*615+6),f'PDF PAGE {start+k+1}',fill='black')
    sheet.save(out/f'contact-{start+1:03}-{min(start+9,len(imgs)):03}.png')
print(json.dumps({'pages':len(rows),'rendered_pages':len(imgs),'outside_crop_pages':[r['page'] for r in rows if r['outside_crop']],'missing_glyph_pages':[r['page'] for r in rows if r['missing_glyph_candidates']],'duplicate_pages':[r['page'] for r in rows if r['duplicate_chars']],'overlap_pages':[{ 'page':r['page'],'count':len(r['high_overlap_candidates'])} for r in rows if r['high_overlap_candidates']],'dense_pages':sorted([{'page':r['page'],'chars':r['chars']} for r in rows],key=lambda r:r['chars'],reverse=True)[:18],'log_layout_warnings':report['log_layout_warnings']},indent=2))
