"""Verify exact compiled inputs and complete source/body provenance for H."""
from pathlib import Path
import hashlib,json,re
W=Path(__file__).resolve().parents[1]
R=W/'output/split_zero_rh_tandem_2026-09-12'
G=R/'release_20260912g'
def read(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def need(ok,msg):
    if not ok: raise RuntimeError(msg)
build=read(R/'build/build_receipt.json')
old=read(G/'build/build_receipt.json')
notes=read(R/'build/source_receipt.json')
need(build['status']=='compiled' and notes==build['source_notes'],'Build/source disagreement')
need(len(build['tex_inputs'])==39 and len(notes)==18,'Unexpected complete edition membership')
need(sha(R/'Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf')==build['pdf_sha256'],'Unpinned PDF')
checks=[]
for path,pin in build['tex_inputs'].items():
    actual=sha(R/path)
    need(actual==pin,'Unbuilt input '+path)
    row={'path':path,'sha256':actual,'matches':True}
    if path in old['tex_inputs'] and path not in ('tex/main.tex','tex/research_conclusion.tex'):
        need(actual==old['tex_inputs'][path],'Inherited proof changed '+path)
        row['inherited_g_proof_byte_identical']=True
    checks.append(row)
sources=[]
oldnotes={n['source']:n for n in old['source_notes']}
for note in notes:
    src=R/note['source']; converted=R/note['converted']
    need(sha(src)==note['sha256'],'Original source changed '+note['source'])
    need(converted.is_file() and converted.stat().st_size>0,'Empty appendix')
    need(note.get('staging_manifest_verified') is True,'Source staging not verified')
    row={'path':note['source'],'sha256':sha(src),'bytes':src.stat().st_size,
         'original_preserved':True,'converted':note['converted'],'converted_sha256':sha(converted)}
    if note['source'] in oldnotes:
        earlier=oldnotes[note['source']]
        need(note['sha256']==earlier['sha256'] and note['converted']==earlier['converted'],'Changed inherited source locator')
        need(sha(converted)==sha(G/earlier['converted']),'Inherited complete converted appendix changed')
        row['inherited_g_complete_appendix_byte_identical']=True
    else:
        need(note.get('all_math_spans_preserved_exactly', note.get('all_prepared_math_spans_preserved_exactly')) is True,'New source full math preservation missing')
        row['build_conversion_receipt']=note
    sources.append(row)
rows=read(R/'sources/local_toda_continuations/FRAGMENT_TRANSFORMATIONS.json')
need(len(rows)==3,'Missing full authored source')
body_checks=[]
for row in rows:
    original=R/row['original']; fragment=R/row['fragment']
    need(sha(original)==row['source_sha256'] and sha(fragment)==row['fragment_sha256'],'Authored source/fragment pin changed')
    source=original.read_text(encoding='utf-8'); body=fragment.read_text(encoding='utf-8')
    if '\\begin{document}' in source:
        pre,sourcebody=source.split('\\begin{document}',1)
        sourcebody,tail=sourcebody.split('\\end{document}',1)
        need(not tail.strip(),'Unaccounted original trailer')
        transformed=sourcebody.replace('\\maketitle','',1)
        transformed=re.sub(r'\\(section|subsection)(?=\*?[\[{])',lambda m:'\\'+{'section':'subsection','subsection':'subsubsection'}[m[1]],transformed)
        need(transformed in body,'Complete original body not retained')
        pattern=r'\\\[(.*?)\\\]|\\\((.*?)\\\)|\$(.*?)\$'
        need(re.findall(pattern,sourcebody,re.S)==re.findall(pattern,body,re.S),'Authored math spans changed')
        for line in pre.splitlines():
            if line.startswith('\\newcommand'):
                match=re.fullmatch(r'\\newcommand\{(\\[A-Za-z]+)\}(\{.*\})',line)
                need(match is not None,'Unaccounted original macro')
                need('\\def'+match[1]+match[2] in body,'Original macro not defined locally')
    else:
        need(original.read_bytes()==fragment.read_bytes(),'Byte-identical fragment changed')
    body_checks.append({**row,'complete_body_verified':True,'all_mathematical_spans_preserved':True})
original_conclusion=(G/'tex/research_conclusion.tex').read_text(encoding='utf-8')
need((R/'tex/research_conclusion.tex').read_text(encoding='utf-8').startswith(original_conclusion),'G conclusion not retained completely')
result={'status':'all source and input identities verified','pdf_sha256':build['pdf_sha256'],
        'pages':build['pages'],'proof_fragments':38,'complete_source_appendices':18,
        'checks':checks,'sources':sources,'authored_complete_body_checks':body_checks,
        'inherited_conclusion_retained_completely':True,
        'scope':'Exact compiled-source and complete-body provenance checks. Mathematical acceptance is documented by the complete independent written reviews; this script makes no formal proof or asymptotic claim.'}
out=R/'build/source_audit_20260913h.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':result['status'],'pages':build['pages'],'proofs':38,'sources':18,'sha256':sha(out)}))
