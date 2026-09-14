from pathlib import Path
import json
from PIL import Image, ImageChops

q=Path(__file__).resolve().parent
mapping=json.loads((q/'baseline_page_mapping.json').read_text())
old=q/'version_247'
rows=[]
for row in mapping['page_mapping']:
    candidates=row['matching_reviewed_baseline_pages']
    if not candidates:
        continue
    new=Image.open(q/f"page-{row['page']:03}.png").convert('RGB')
    matched=False
    diffs=[]
    for page in candidates:
        previous=Image.open(old/f'page-{page:03}.png').convert('RGB')
        assert new.size==previous.size
        crop=(0,65,new.width,985)
        diff=ImageChops.difference(new.crop(crop),previous.crop(crop))
        bbox=diff.getbbox()
        if bbox is None:
            matched=True
            break
        diffs.append({'baseline_page':page,'difference_bbox_in_crop':bbox})
    rows.append({'page':row['page'],'body_raster_matches_baseline':matched,'differences':diffs if not matched else []})
report={'baseline_sha256':mapping['frozen_baseline_sha256'],'pdf_sha256':mapping['continuation_sha256'],'crop_pixels':[0,65,745,985],'compared_pages':len(rows),'identical_body_raster_pages':[r['page'] for r in rows if r['body_raster_matches_baseline']],'differing_body_raster_pages':[r for r in rows if not r['body_raster_matches_baseline']]}
(q/'body_raster_comparison.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='identical_body_raster_pages'},indent=2))
