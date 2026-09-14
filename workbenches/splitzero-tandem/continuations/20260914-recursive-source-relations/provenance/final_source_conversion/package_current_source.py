"""Copy the completed current source into the requested standalone delivery.

Historical source PDFs and authored evidence remain. Only ordinary compilation
cache, current duplicate build PDF, and pixel review scratch files are omitted;
the exact omission list accompanies the repository.
"""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import zipfile

HERE=Path(__file__).resolve().parent
WORK=HERE.parent
SOURCE=HERE/'cumulative_source_v1'
OUTPUT=WORK.parent/'output/Split_Zero_Recursive_Integration_2026-09-13'
REPO=OUTPUT/'repository'

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('operation',choices=['copy','seal'])
    args=parser.parse_args()
    OUTPUT.mkdir(exist_ok=True)
    if args.operation=='copy':
        if REPO.exists():raise RuntimeError('Preserve the existing delivery repository; use its verified build or a fresh version.')
        omitted=[];records=[]
        for source in sorted(SOURCE.rglob('*')):
            if not source.is_file():continue
            name=source.relative_to(SOURCE).as_posix()
            skip=(source.suffix.lower() in ['.aux','.log','.out','.toc','.fls','.fdb_latexmk','.synctex']
                or '__pycache__' in source.parts
                or name=='build/reader.pdf'
                or name.startswith('build/qa/'))
            if skip:
                omitted.append({'path':name,'bytes':source.stat().st_size,'sha256':sha(source),'reason':'Regenerable build or page-render artifact; authored source retained.'})
                continue
            target=REPO/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,target)
            if sha(target)!=sha(source):raise RuntimeError('Copy mismatch: '+name)
            records.append({'path':name,'bytes':target.stat().st_size,'sha256':sha(target)})
        (REPO/'provenance/DELIVERY_SOURCE_COPY.json').write_text(json.dumps({'source':str(SOURCE),'copied_files':records,'omitted_regenerable_files':omitted},indent=2)+'\n',encoding='utf-8')
        print(json.dumps({'repository':str(REPO),'source_files':len(records),'omitted_build_artifacts':len(omitted)}))
        return
    build=json.loads((REPO/'build/CURRENT_BUILD_RECEIPT.json').read_text())
    pdf=REPO/build['pdf']
    if sha(pdf)!=build['pdf_sha256']:raise RuntimeError('Compiled final PDF identity changed.')
    if any(build['warnings'].values()):raise RuntimeError('Unresolved final compilation warnings.')
    qa=json.loads((OUTPUT/'validation/FINAL_PDF_VISUAL_ACCEPTANCE.json').read_text())
    if qa.get('status')!='PASS' or not qa.get('all_pages_covered') or qa['pdf_sha256']!=sha(pdf) or qa['final_pages']!=build['pages']:
        raise RuntimeError('Complete final PDF visual evidence is missing or stale.')
    conversion=json.loads((OUTPUT/'validation/FINAL_CONVERSION_ACCEPTANCE.json').read_text())
    if not conversion.get('status','').startswith('PASS'):
        raise RuntimeError('Source conversion acceptance is missing.')
    for name,row in build['compiled_sources'].items():
        p=REPO/name
        if not p.is_file() or p.stat().st_size!=row['bytes'] or sha(p)!=row['sha256']:
            raise RuntimeError('Compiled source changed before packaging: '+name)
    files={p.relative_to(REPO).as_posix():{'bytes':p.stat().st_size,'sha256':sha(p)}
           for p in sorted(REPO.rglob('*')) if p.is_file() and p.name!='CURRENT_SOURCE_MANIFEST.json'
           and p.suffix.lower() not in ['.aux','.out','.toc','.log','.fls']}
    manifest={'status':'complete-current-source-package','pdf':{'path':pdf.name,'sha256':sha(pdf),'pages':build['pages']},'files':files}
    (REPO/'CURRENT_SOURCE_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    archive=OUTPUT/'Split_Zero_Recursive_Integration_Complete_Source.zip'
    if archive.exists():raise RuntimeError('Do not overwrite the already sealed source archive.')
    with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as zipped:
        for name in sorted(files):zipped.write(REPO/name,name)
        zipped.write(REPO/'CURRENT_SOURCE_MANIFEST.json','CURRENT_SOURCE_MANIFEST.json')
    with zipfile.ZipFile(archive) as zipped:
        if zipped.testzip() is not None:raise RuntimeError('ZIP CRC verification failed.')
        if set(zipped.namelist())!=set(files)|{'CURRENT_SOURCE_MANIFEST.json'}:raise RuntimeError('ZIP membership mismatch.')
        for name,row in files.items():
            data=zipped.read(name)
            if len(data)!=row['bytes'] or hashlib.sha256(data).hexdigest()!=row['sha256']:raise RuntimeError('ZIP complete-byte mismatch: '+name)
    target=OUTPUT/'Split_Zero_Recursive_Integration.pdf';shutil.copy2(pdf,target)
    result={'repository':str(REPO),'source_manifest_sha256':sha(REPO/'CURRENT_SOURCE_MANIFEST.json'),
        'source_archive':{'path':str(archive),'sha256':sha(archive),'bytes':archive.stat().st_size,'members':len(files)+1},
        'pdf':{'path':str(target),'sha256':sha(target),'bytes':target.stat().st_size,'pages':build['pages']},
        'zip_all_complete_bytes_verified':True}
    (OUTPUT/'SOURCE_PACKAGE_RECEIPT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))

if __name__=='__main__':main()
