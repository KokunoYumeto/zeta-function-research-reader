"""Verify complete revised result blocks in the actual cumulative conclusion."""
from pathlib import Path
import hashlib,json,re,argparse

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
parser=argparse.ArgumentParser()
parser.add_argument('--active',type=Path,default=ROOT/'cumulative_source_v1/tex/research_conclusion.tex')
args=parser.parse_args()
def txt(p):return p.read_text(encoding='utf-8-sig')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def block(s,n):
    start=s.index(r'\paragraph{Result R'+str(n)+':')
    tail=s[start:]
    found=re.search(r'\n\\paragraph\{Result R\d+:',tail[1:])
    return tail[:found.start()+1] if found else tail

current=txt(ROOT/'root/research_conclusion.tex')
active=txt(args.active)
presentation_inverse=[]
manifest=ROOT/'cohort_staging/typesetting_root_conclusion/OVERLAY_PROPOSALS.json'
if manifest.is_file():
    layout=json.loads(txt(manifest))
    if args.active.resolve()==Path(layout['active_source']).resolve():
        assert sha(args.active)==layout['proposed_after']['sha256']
        for e in reversed(layout['records']):
            old=e['old_display'].replace('\r\n','\n');new=e['new_display'].replace('\r\n','\n')
            assert active.count(new)==1
            active=active.replace(new,old,1)
            presentation_inverse.append({'old':old,'new':new})
        assert active==current,'Complete conclusion inverse differs from accepted source'
checks=[]
replacements=json.loads(txt(ROOT/'root/CONCLUSION_REPLACEMENTS.json'))
relocation=next(r['old'] for r in replacements if r['key']=='Only the exact historical closing paragraph is relocated')
for row in replacements:
    if row['key']=='Only the exact historical closing paragraph is relocated':continue
    # The assembler changes the blank separator after R62 when it appends R63.
    # Keep its entire mathematical/prose block, excluding only terminal LFs.
    new=row['new'].rstrip('\n')
    if row['key']=='R62 complete current boundary result':
        # The only deliberately relocated text is the exact historical closing
        # paragraph. The entire new Hessian/recursion continuation must remain.
        assert new.count(relocation)==1
        new=new.replace(relocation,'').strip('\n')
        actual_r62=block(active,62).strip('\n')
        current_r62=block(current,62).strip('\n')
        checks.append({'key':row['key'],'entire_mathematical_and_prose_block_preserved':actual_r62==new and current_r62==new,'exact_historical_paragraph_relocated':relocation,'pass':actual_r62==new and current_r62==new})
        continue
    checks.append({'key':row['key'],'complete_current_occurrences':current.count(new),
                   'complete_active_occurrences':active.count(new),
                   'pass':current.count(new)==1 and active.count(new)==1})
root_tail=txt(ROOT/'root/R67_R74_REVISED.tex')
for n in [67,72,73]:
    b=block(root_tail,n).rstrip()
    checks.append({'key':f'Entire independently accepted R{n}',
                   'complete_active_occurrences':active.count(b),'pass':active.count(b)==1})
# R74 is the last original tail block, also retained in full before the final
# cumulative concluding paragraph; its complete exact text includes all windows.
b=block(root_tail,74).rstrip()
checks.append({'key':'Entire independently accepted R74','complete_active_occurrences':active.count(b),'pass':active.count(b)==1})
hol=txt(ROOT/'root/R63_R66_REVISED.tex').rstrip()
checks.append({'key':'Entire R63-R66 original source with precise averaging refinement',
               'complete_active_occurrences':active.count(hol),'pass':active.count(hol)==1})
result={'active_path':str(args.active),'active_sha256':sha(args.active),
        'root_candidate_sha256':sha(ROOT/'root/research_conclusion.tex'),
        'active_presentation_inverse':presentation_inverse,
        'checks':checks,'pass':all(r['pass'] for r in checks)}
(HERE/'CONCLUSION_COMPLETE_BLOCK_TRANSFER_CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'pass':result['pass'],'checks':len(checks),'failures':[r['key'] for r in checks if not r['pass']]}))
if not result['pass']:raise SystemExit(1)
