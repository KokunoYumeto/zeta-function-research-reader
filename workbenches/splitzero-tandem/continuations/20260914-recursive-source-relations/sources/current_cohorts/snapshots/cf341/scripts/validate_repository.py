"""Read-only integrity, reference and PDF checks for the assembled reader."""
from pathlib import Path
import hashlib,json,re
import fitz
ROOT=Path(__file__).resolve().parents[1]

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    manifest=json.loads((ROOT/'provenance/PROOF_INPUT_MANIFEST.json').read_text(encoding='utf8'))
    integrity=[]
    for row in manifest:
        original=ROOT/row['original_copy']; included=ROOT/row['included_copy']
        integrity.append({'prefix':row['prefix'],
          'original_match':sha(original)==row['source_sha256'],
          'included_match':sha(included)==row['included_sha256']})
    continuation=json.loads((ROOT/'provenance/CONTINUATION_INPUT_MANIFEST.json').read_text(encoding='utf8'))
    for row in continuation['entries']:
        integrity.append({'prefix':row['code'],'original_match':
            sha(ROOT/row['original_copy'])==row['source_sha256'] if 'original_copy' in row
            else row['source_sha256']==row['included_sha256'],
            'included_match':sha(ROOT/row['included'])==row['included_sha256']})
    labels=[];references=[];inputs=[]
    for p in sorted((ROOT/'tex').rglob('*.tex')):
        t=p.read_text(encoding='utf8')
        labels += [(m,p.name) for m in re.findall(r'\\label\{([^}]+)\}',t)]
        references += [(m,p.name) for m in re.findall(r'\\(?:ref|eqref|pageref|autoref)\{([^}]+)\}',t)]
        inputs += [((ROOT/'tex'/m).is_file(),m) for m in re.findall(r'\\input\{([^}]+)\}',t)]
    names=[x[0] for x in labels]
    duplicates=sorted({s for s in names if names.count(s)>1})
    missing=[x for x in references if x[0] not in names]
    pdf=ROOT/'Tau_Split_Zero_Total_Counterfactual.pdf'
    doc=fitz.open(pdf); outside=[]; replacement=[]; blank=[]
    for index,page in enumerate(doc):
        txt=page.get_text()
        if '\ufffd' in txt:replacement.append(index+1)
        if len(txt.strip())<15:blank.append(index+1)
        for block in page.get_text('dict')['blocks']:
            if 'lines' not in block:continue
            for line in block['lines']:
                for span in line['spans']:
                    box=fitz.Rect(span['bbox'])
                    if box.x0 < -0.5 or box.y0 < -0.5 or box.x1>page.rect.width+0.5 or box.y1>page.rect.height+0.5:
                        outside.append({'page':index+1,'text':span['text'],'bbox':list(box)})
    log=(ROOT/'build/main.log').read_text(encoding='utf8',errors='replace')
    errors=[line for line in log.splitlines() if any(x in line for x in ['Overfull','Missing character','undefined references','multiply defined'])]
    report={'pdf_pages':len(doc),'pdf_sha256':sha(pdf),'proof_integrity':integrity,
            'label_count':len(names),'reference_count':len(references),'duplicate_labels':duplicates,
            'missing_references':missing,'missing_inputs':[m for ok,m in inputs if not ok],
            'out_of_page_text':outside,'replacement_glyph_pages':replacement,'blank_pages':blank,
            'compiler_layout_or_reference_errors':errors,
            'scope':'New compiled reader only. Visual inspection reported separately. Original historical receipts not rerun.'}
    report['passed']=all(x['original_match'] and x['included_match'] for x in integrity) and not any([
          duplicates,missing,report['missing_inputs'],outside,replacement,blank,errors])
    (ROOT/'build/REPOSITORY_VALIDATION.json').write_text(json.dumps(report,indent=2),encoding='utf8')
    print(json.dumps(report,indent=2))
    if not report['passed']:raise SystemExit(1)
if __name__=='__main__':main()
