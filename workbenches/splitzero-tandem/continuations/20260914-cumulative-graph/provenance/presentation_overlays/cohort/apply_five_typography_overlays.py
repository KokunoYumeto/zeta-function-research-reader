"""Five reversible presentation overlays on the active cumulative copies only."""
from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parent
ACTIVE=ROOT.parents[1]/'cumulative_source_v1'
def sha(b):return hashlib.sha256(b).hexdigest()
def pin(path):b=path.read_bytes();return {'path':str(path),'bytes':len(b),'sha256':sha(b)}
def math_and_prose_tokens(text):
    # These are the only permitted presentation changes. Every other command,
    # word, digit, sign, group, punctuation token and Unicode character stays.
    text=text.replace(r'\allowbreak{}','')
    text=re.sub(r'\\(?:qquad|quad)\b|\\;', '',text)
    return re.findall(r'\\[A-Za-z@]+|\\[\s\S]|[A-Za-z0-9]+|[^\s]',text)
def display(text,tag):
    marker=r'\tag{'+tag+'}'
    assert text.count(marker)==1
    at=text.index(marker);start=text.rfind(r'\[',0,at);end=text.index(r'\]',at)+2
    return text[start:end]
hash_value='55f7a9cce6f22b11a30321a7ba726f300a990e78c39780a43b7fdd692c7935e5'
specs=[
 ('cf/49_TP.tex','TPF.1',' N=m+1\\ge2,\\qquad p>N,\\qquad',
  ' N=m+1\\ge2,\\quad p>N,\\qquad','Reduce one two-em math separation to one em.'),
 ('cf/15_PAM.tex','PSC.6',' \\qquad\n w_{q-1}=w_{2q-1}=1,\\quad',
  ' \\quad\n w_{q-1}=w_{2q-1}=1,\\quad','Reduce one two-em separation before the unchanged weight definitions to one em.'),
 ('cf/42_CA.tex','CA18',' b_0=1,\\quad b_1=u,\\quad',
  ' b_0=1,\\; b_1=u,\\quad','Use a thick math separation between the first two unchanged recurrence initial values.'),
 ('transcript/05-proof05.tex',None,' \\quad p_{b,k}(F)=',
  ' \\; p_{b,k}(F)=','Use a thick math separation before the unchanged seminorm definition.'),
 ('ta_c47/C47_TCReview_complete.tex',None,hash_value,
  r'\allowbreak{}'.join(hash_value[i:i+8] for i in range(0,len(hash_value),8)),
  'Insert optional line-break opportunities in the unchanged 64 hexadecimal source digits.')]
before_sections=[];after_sections=[];records=[]
for rel,tag,old,new,reason in specs:
    path=ACTIVE/'tex/cohorts'/rel
    original=path.read_bytes();text=original.decode('utf-8')
    if '\r\n' in text:
        old=old.replace('\n','\r\n');new=new.replace('\n','\r\n')
    assert text.count(old)==1,(rel,'expected unique source text')
    changed=text.replace(old,new,1)
    assert changed.count(new)==1,(rel,'expected unique inverse text')
    assert changed.replace(new,old,1).encode('utf-8')==original
    assert math_and_prose_tokens(text)==math_and_prose_tokens(changed),rel
    before=ROOT/'before'/rel;after=ROOT/'after'/rel
    before.parent.mkdir(parents=True,exist_ok=True);after.parent.mkdir(parents=True,exist_ok=True)
    assert not before.exists() or before.read_bytes()==original,'Do not overwrite previous before snapshot'
    before.write_bytes(original);after.write_bytes(changed.encode('utf-8'))
    if tag:
        old_part,new_part=display(text,tag),display(changed,tag)
    elif rel.startswith('transcript'):
        marker=r'\mathscr B='
        a=text.index(marker);start=text.rfind(r'\[',0,a);end=text.index(r'\]',a)+2
        old_part=text[start:end]
        a=changed.index(marker);start=changed.rfind(r'\[',0,a);end=changed.index(r'\]',a)+2
        new_part=changed[start:end]
    else:
        old_part=re.split(r'\r?\n\r?\n',text)[1]
        new_part=re.split(r'\r?\n\r?\n',changed)[1]
    label=rel.replace('_',r'\_')
    before_sections.append(r'\subsection*{'+label+'}\n'+old_part+'\n')
    after_sections.append(r'\subsection*{'+label+'}\n'+new_part+'\n')
    records.append({'active_path':str(path),'original':pin(before),'proposed_overlay':pin(after),
        'old':old,'new':new,'reason':reason,'exact_byte_inverse':True,
        'all_nonpresentation_tokens_identical':True,
        'mathematical_and_prose_token_count':len(math_and_prose_tokens(text))})

preamble=(ACTIVE/'tex/main.tex').read_bytes().decode('utf-8').split(r'\begin{document}',1)[0]
(ROOT/'ACTIVE_PREAMBLE_SNAPSHOT.tex').write_bytes(preamble.encode('utf-8'))
for name,sections in [('before',before_sections),('after',after_sections)]:
    text=preamble+r'\begin{document}'+'\n'+r'\section*{Five source-preserving typography checks}'+'\n'+'\n'.join(sections)+r'\end{document}'+'\n'
    (ROOT/(name+'.tex')).write_bytes(text.encode('utf-8'))
(ROOT/'OVERLAY_PROPOSALS.json').write_text(json.dumps({'scope':'Exactly five active cumulative cohort files; originals and all other sources unchanged.',
    'records':records,'all_exact_inverses':True,'all_nonpresentation_tokens_identical':True,
    'active_files_modified':False,'preamble_pin':pin(ROOT/'ACTIVE_PREAMBLE_SNAPSHOT.tex')},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'proposed_overlays':len(records),'all_byte_inverses':True,'all_nonpresentation_tokens_identical':True,'active_files_modified':False}))
