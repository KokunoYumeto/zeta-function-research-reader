"""Assemble the explicit whole-body AP typing maps, without source edits."""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent;OLD=R.parent/'analytic_pole_cumulative_conversion_20260913'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
jobs=[('analytic_pole',OLD/'mapping/analytic_pole_block_mapping.json',
       [R/'mapping/proof_prose_sections_1_4.json',R/'mapping/proof_prose_sections_5_7.json']),
      ('analytic_pole_review',OLD/'mapping/analytic_pole_review_math_mapping.json',
       [R/'mapping/review_prose_math.json'])]
for key,base_path,prose_paths in jobs:
    base=load(base_path);source=base['source'];raw=Path(source['path']).read_bytes()
    if len(raw)!=source['bytes'] or hashlib.sha256(raw).hexdigest()!=source['sha256']:raise RuntimeError('Accepted source changed')
    result=dict(base);result['key']=key;result['schema']='whole-body-explicit-code-and-prose-math-transcription-v2'
    result['prose_math_mappings']=[];result['component_maps']=[]
    for p in [base_path]+prose_paths:
        data=p.read_bytes();d=json.loads(data)
        if any(d['source'][name]!=source[name] for name in ['bytes','sha256']):raise RuntimeError('Incompatible complete source mapping')
        result['component_maps'].append({'path':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
        if p in prose_paths:result['prose_math_mappings'].extend(d['prose_math_mappings'])
    result['prose_math_mappings'].sort(key=lambda row:row['source_byte_start'])
    all_rows=[]
    for field in ('math_code_mappings','retained_code','display_codeblock_mappings','prose_math_mappings'):
        for row in result.get(field,[]):
            a,b=row['source_byte_start'],row['source_byte_end']
            if field=='prose_math_mappings' and raw[a:b].decode('utf-8')!=row['original']:raise RuntimeError('Incorrect original prose span')
            all_rows.append((a,b,field))
    all_rows.sort()
    for a,b in zip(all_rows,all_rows[1:]):
        if a[1]>b[0]:raise RuntimeError('Overlapping declared source spans '+str((a,b)))
    result['whole_body_scope']='Every mathematical CodeBlock, inline Code and ordinary-prose mathematical expression has its explicit original source span and complete TeX payload. Ordinary proof prose, headings, equation references and source/hash references remain. No simplification, coefficient specialization or proof selection occurs.'
    target=R/'mapping'/f'{key}_full_math_mapping.json'
    target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='')
    print(key,'prose',len(result['prose_math_mappings']),'inlineCode',len(result.get('math_code_mappings',[])),'display',len(result.get('display_codeblock_mappings',[])))
