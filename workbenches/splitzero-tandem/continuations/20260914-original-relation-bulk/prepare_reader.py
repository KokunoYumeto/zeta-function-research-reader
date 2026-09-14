"""Prepare only accepted pinned mathematical sources for the reader.

Usage: python prepare_reader.py ACCEPTED_SOURCE_PINS.json
The JSON object must have accepted=true and a sections list containing
name, path, sha256, title. This does not compile or edit author sources.
"""
from pathlib import Path
import json, hashlib, shutil, re, sys, difflib
HERE=Path(__file__).resolve().parent

def sha(data): return hashlib.sha256(data).hexdigest()

if len(sys.argv)!=2:
    raise SystemExit('Pass the root-accepted source pin JSON; no source preparation has run.')
pins_path=Path(sys.argv[1])
pins=json.loads(pins_path.read_text(encoding='utf-8-sig'))
if pins.get('accepted') is not True:
    raise SystemExit('The mathematical source pins have not been accepted.')
sections=pins['sections']
if not sections or len({s['name'] for s in sections})!=len(sections):
    raise SystemExit('Empty or duplicated source section names.')
records=[]
for s in sections:
    p=Path(s['path']); data=p.read_bytes()
    if sha(data)!=s['sha256']:
        raise SystemExit(f'Pin mismatch: {p.name}')
    name=s['name']
    if Path(name).name!=name or not name.endswith('.tex'):
        raise SystemExit('Source name must be a plain .tex filename.')
    text=data.decode('utf-8-sig')
    if r'\begin{document}' in text:
        text=text.split(r'\begin{document}',1)[1]
        if r'\end{document}' not in text:
            raise SystemExit(f'No document terminator: {name}')
        text=text.rsplit(r'\end{document}',1)[0]
        text=re.sub(r'\\maketitle\s*','',text,count=1)
        text=re.sub(r'\\tableofcontents\s*','',text,count=1)
    text=text.strip()+'\n'
    original=HERE/'provenance'/'math_sources'/name
    prepared=HERE/'sources'/name
    original.parent.mkdir(parents=True,exist_ok=True)
    prepared.parent.mkdir(parents=True,exist_ok=True)
    if original.exists() and original.read_bytes()!=data:
        raise SystemExit(f'Existing source provenance differs; preserve history before replacing {name}.')
    original.write_bytes(data)
    prepared.write_text(text,encoding='utf-8',newline='\n')
    diff=''.join(difflib.unified_diff(data.decode('utf-8-sig').splitlines(True),text.splitlines(True),fromfile='author/'+name,tofile='sources/'+name))
    diffpath=HERE/'provenance'/'display_changes'/(name+'.diff')
    diffpath.parent.mkdir(parents=True,exist_ok=True)
    diffpath.write_text(diff,encoding='utf-8')
    records.append({'name':name,'author_sha256':sha(data),'prepared_sha256':sha(prepared.read_bytes()),'author_bytes':len(data),'prepared_bytes':prepared.stat().st_size,'operations':['Extract complete document body, if the author source is a standalone document.','Remove only its own maketitle and tableofcontents commands; the combined volume provides both.','Store UTF-8 with LF line endings.'],'display_diff':diffpath.relative_to(HERE).as_posix()})
    if p.read_bytes()!=data:
        raise SystemExit(f'Author source changed during preparation: {name}')
wrapper=HERE/'Original_Relation_Bulk_Control.tex'
base=wrapper.read_text(encoding='utf-8-sig').split('% BEGIN ACCEPTED SECTIONS',1)[0]+'% BEGIN ACCEPTED SECTIONS\n'
parts=[]
for s in sections:
    parts.append('\\readerpart{'+s['title']+'}\n\\input{sources/'+s['name']+'}\n')
wrapper.write_text(base+''.join(parts)+'\\end{document}\n',encoding='utf-8',newline='\n')
receipt={'accepted_pin_sha256':sha(pins_path.read_bytes()),'sections':records,'wrapper_sha256':sha(wrapper.read_bytes()),'compiled':False}
(HERE/'SOURCE_PREPARATION_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'prepared_sections':len(records),'receipt':'SOURCE_PREPARATION_RECEIPT.json','compiled':False}))
