"""Repair two source-proven degree exponents misparsed as inline footnotes."""
from pathlib import Path
import hashlib,json,re,subprocess
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parent
MATH=ROOT.parents[3]
STAGE=MATH/'work/backpropagation_20260913/cumulative_source_v1'
DELIVERY=MATH/'output/Split_Zero_Recursive_Integration_2026-09-13/repository'
SNAP=ROOT.parent/'snapshots/transcript'
def sha(b):return hashlib.sha256(b).hexdigest()
def pin(p):b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':sha(b)}
def pandoc(text,to='json',extra=()):
    return subprocess.run(['pandoc','--from=markdown+tex_math_single_backslash','--to='+to,*extra],
        input=text,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,encoding='utf-8',check=True).stdout
def nodes(node,kind):
    found=[]
    if isinstance(node,dict):
        if node.get('t')==kind:found.append(node)
        for value in node.values():found+=nodes(value,kind)
    elif isinstance(node,list):
        for value in node:found+=nodes(value,kind)
    return found
def plain(node):
    if isinstance(node,list):return ''.join(plain(v) for v in node)
    if isinstance(node,dict):
        if node.get('t')=='Str':return node['c']
        if node.get('t') in {'Space','SoftBreak'}:return ' '
        return plain(node.get('c',[]))
    return ''

root_source=SNAP/'sources/turns/A0862.md'
formation=SNAP/'ledger_publication/sources/formation.md'
ledger=SNAP/'ledger_publication/ledger.md'
converter=SNAP/'ledger_publication/build_ledger.py'
lua=SNAP/'ledger_publication/layout.lua'
source_pins=[]
for src in (root_source,formation,ledger,converter,lua):
    dst=ROOT/'original_sources'/src.name
    dst.parent.mkdir(parents=True,exist_ok=True);data=src.read_bytes()
    assert not dst.exists() or dst.read_bytes()==data
    dst.write_bytes(data);source_pins.append({'original':pin(src),'retained':pin(dst)})
original_math=root_source.read_text(encoding='utf-8')
for literal in (r'd=[K:\mathbb Q].',r'N_K(2R)=2^d.',r'q=2^dq.'):
    assert literal in original_math,literal
original=ledger.read_bytes().decode('utf-8')
raw_expressions=['N(2R)=2^[K:Q]>1','q=2^[K:Q]q']
corrected_expressions=[r'\(N(2R)=2^{[K:Q]}>1\)',r'\(q=2^{[K:Q]}q\)']
corrected=original
for old,new in zip(raw_expressions,corrected_expressions):
    assert original.count(old)==1
    assert old in formation.read_text(encoding='utf-8')
    corrected=corrected.replace(old,new,1)
inverse=corrected
for old,new in reversed(list(zip(raw_expressions,corrected_expressions))):inverse=inverse.replace(new,old,1)
assert inverse==original
(ROOT/'corrected_ledger_source_not_overwriting_original.md').write_bytes(corrected.encode('utf-8'))

# The full combined source has exactly two Note nodes, both K:Q, and the
# corrected source has no Note nodes. All full-source generated LaTeX outside
# the two formula images is the same modulo Pandoc's line wrapping.
ast_before=json.loads(pandoc(original));ast_after=json.loads(pandoc(corrected))
notes_before=nodes(ast_before,'Note');notes_after=nodes(ast_after,'Note')
assert len(notes_before)==2 and all(plain(x)=='K:Q' for x in notes_before)
assert notes_after==[]
tex_before=pandoc(original,'latex',('--lua-filter='+str(lua),))
tex_after=pandoc(corrected,'latex',('--lua-filter='+str(lua),))
(ROOT/'full_original_reconverted.tex').write_bytes(tex_before.encode('utf-8'))
(ROOT/'full_corrected_reconverted.tex').write_bytes(tex_after.encode('utf-8'))
old_tex=[r'N(2R)=2\footnote{K:Q}\textgreater1',r'q=2\footnote{K:Q}q']
new_tex=corrected_expressions
recovered_tex=tex_after
for old,new in zip(old_tex,new_tex):
    assert tex_before.count(old)==1,(old,'before generation')
    assert tex_after.count(new)==1,(new,'after generation')
    recovered_tex=recovered_tex.replace(new,old,1)
lex=lambda s:re.findall(r'\\[A-Za-z@]+|\\[\s\S]|[A-Za-z0-9]+|[^\s]',s)
assert lex(recovered_tex)==lex(tex_before),'Nonlocal full-source conversion effect'

rel=Path('tex/cohorts/transcript/LEDGER_COMPLETE.tex')
source_hash='514033f1c772997e2b13a1cd095f84a631a92162f0d5711ab3795dcfb97c77c3'
records=[];prepared=[]
for label,base in [('stage',STAGE),('delivery',DELIVERY)]:
    active=base/rel;raw=active.read_bytes();text=raw.decode('utf-8')
    assert sha(raw)==source_hash,(label,'unexpected active input pin')
    changed=text;occurrences=[]
    for old,new,raw_expr in zip(old_tex,new_tex,raw_expressions):
        assert changed.count(old)==1
        pos=changed.index(old)
        occurrences.append({'old_tex':old,'correct_tex':new,'source_expression':raw_expr,
            'old_active_line':text[:text.index(old)].count('\n')+1,
            'source_ledger_line':original[:original.index(raw_expr)].count('\n')+1,
            'source_formation_line':formation.read_text(encoding='utf-8')[:formation.read_text(encoding='utf-8').index(raw_expr)].count('\n')+1})
        changed=changed.replace(old,new,1)
    restored=changed
    for old,new in reversed(list(zip(old_tex,new_tex))):restored=restored.replace(new,old,1)
    assert restored.encode('utf-8')==raw
    assert r'\footnote{K:Q}' not in changed
    before=ROOT/'before'/label/'LEDGER_COMPLETE.tex';after=ROOT/'after'/label/'LEDGER_COMPLETE.tex'
    before.parent.mkdir(parents=True,exist_ok=True);after.parent.mkdir(parents=True,exist_ok=True)
    assert not before.exists() or before.read_bytes()==raw
    before.write_bytes(raw);after.write_bytes(changed.encode('utf-8'))
    records.append({'location':label,'active':str(active),'before':pin(before),'after':pin(after),
        'exact_fullbody_inverse':True,'occurrences':occurrences,
        'all_other_body_bytes_unchanged':True})
    prepared.append((active,changed.encode('utf-8')))

# Evidence from the actual source fixes the intended exponent. There is no
# global parser reinterpretation or guessed replacement of genuine footnotes.
for active,data in prepared:active.write_bytes(data)
receipt={'utc':datetime.now(timezone.utc).isoformat(),'status':'confirmed source conversion correction applied',
    'source_records':source_pins,'cause':'Pandoc markdown enables inline_notes; raw 2^[K:Q] produced a Note node K:Q, then a numbered footnote instead of an exponent.',
    'exact_original_mathematics':{'d':r'd=[K:\mathbb Q]',
        'norm':r'N_K(2R)=2^d','finite_positive_value':r'q=2^d q',
        'source_note':'A0862 defines the number-field degree and derives both equations from the original arithmetic ideal norm; ledger retains its abbreviated K:Q spelling.'},
    'full_combined_ledger_conversion_check':{'source_inline_note_count':2,'source_note_payloads':[plain(x) for x in notes_before],
        'corrected_note_count':0,'only_two_exact_math_images_changed_in_full_generated_body':True,
        'all_other_generated_body_tokens_identical':True,
        'exact_original_markdown_recoverable':True,
        'original_generated':pin(ROOT/'full_original_reconverted.tex'),
        'corrected_generated':pin(ROOT/'full_corrected_reconverted.tex')},
    'active_changes':records,'active_source_paths_modified':2,'mathematical_editorial_changes':False,
    'historical_raw_sources_and_old_editions_unchanged':True,'full_pdf_compile_performed':False}
(ROOT/'APPLIED_LEDGER_EXPONENT_CORRECTION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'active_files_corrected':2,'occurrences_per_file':2,
    'new_active_sha256':sha(prepared[0][1]),'full_body_inverse':True,'full_generated_body_nonlocal_change':False,
    'receipt_sha256':pin(ROOT/'APPLIED_LEDGER_EXPONENT_CORRECTION.json')['sha256']}))
