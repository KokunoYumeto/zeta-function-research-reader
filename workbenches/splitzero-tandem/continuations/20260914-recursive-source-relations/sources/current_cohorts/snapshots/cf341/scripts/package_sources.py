"""Package the complete local source repository without disposable build renders."""
from pathlib import Path
import hashlib,json,zipfile
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT.parent/'Tau_Split_Zero_Total_Counterfactual_Source.zip'
KEEP_BUILD={
 'build/BUILD_RESULT.json','build/REPOSITORY_VALIDATION.json',
 'build/visual_qa/VISUAL_QA.md','build/visual_qa/layout_metrics.json',
 'build/visual_qa/FINAL_VISUAL_QA_RECEIPT.json',
 'build/main.log', 'build/visual_qa/baseline_comparison.json',
 'build/visual_qa/check_layout.py', 'build/visual_qa/compare_baseline.py'
 ,'build/visual_qa/version_224/VISUAL_QA.md',
 'build/visual_qa/version_224/FINAL_VISUAL_QA_RECEIPT.json',
 'build/visual_qa/version_247/VISUAL_QA.md',
 'build/visual_qa/version_247/FINAL_VISUAL_QA_RECEIPT.json'
 ,'build/visual_qa/version_248/VISUAL_QA.md',
 'build/visual_qa/version_248/FINAL_VISUAL_QA_RECEIPT.json'
 ,'build/visual_qa/version_341/VISUAL_QA.md',
 'build/visual_qa/version_341/FINAL_VISUAL_QA_RECEIPT.json'
}
def main():
    records=[]
    for p in sorted(ROOT.rglob('*')):
        if not p.is_file():continue
        rel=p.relative_to(ROOT)
        if any(x in {'__pycache__','.git'} for x in rel.parts):continue
        if 'build' in rel.parts and rel.as_posix() not in KEEP_BUILD:continue
        if rel.name=='SOURCE_ARCHIVE_MANIFEST.json':continue
        data=p.read_bytes()
        records.append({'path':rel.as_posix(),'bytes':len(data),
                        'sha256':hashlib.sha256(data).hexdigest()})
    manifest={'scope':'All source/provenance/dependency files; disposable build directories omitted except named final reader receipts. Original files remain in the local repository.',
              'file_count':len(records),'uncompressed_bytes':sum(r['bytes'] for r in records),
              'files':records}
    m=ROOT/'provenance/SOURCE_ARCHIVE_MANIFEST.json'
    m.write_text(json.dumps(manifest,indent=2),encoding='utf8')
    with zipfile.ZipFile(OUT,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for row in records:z.write(ROOT/row['path'],ROOT.name+'/'+row['path'])
        z.write(m,ROOT.name+'/provenance/SOURCE_ARCHIVE_MANIFEST.json')
    with zipfile.ZipFile(OUT) as z:
        bad=z.testzip()
        if bad:raise RuntimeError('Archive integrity failure: '+bad)
    receipt={'archive':str(OUT),'bytes':OUT.stat().st_size,
             'files':len(records)+1,'sha256':hashlib.sha256(OUT.read_bytes()).hexdigest(),
             'zip_crc_check':'PASS'}
    OUT.with_suffix('.receipt.json').write_text(json.dumps(receipt,indent=2),encoding='utf8')
    print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()
