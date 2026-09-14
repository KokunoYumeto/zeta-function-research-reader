from pathlib import Path
import re,json,hashlib,difflib,argparse
wave=Path(__file__).resolve().parent
work=wave.parent
root=work.parent
stage=wave/'root'
stage.mkdir(exist_ok=True)
parser=argparse.ArgumentParser()
parser.add_argument('--boundary-json',default=str(wave/'boundary/CONCLUSION_REPLACEMENTS.json'))
args=parser.parse_args()
source=root/'output/split_zero_rh_tandem_2026-09-12/current_source_20260913_periodized_residue/tex/research_conclusion.tex'
raw=source.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='cec03014398811e5fa4788cb7b6f4816123c026d673a1a9a0398b7fded360e3b'
(stage/'research_conclusion_ORIGINAL.tex').write_bytes(raw)
text=raw.decode('utf-8-sig').replace('\r\n','\n')
changes=[]
def read(p):return p.read_text(encoding='utf-8-sig').replace('\r\n','\n')
def replace(key,old,new):
    global text
    old=old.replace('\r\n','\n');new=new.replace('\r\n','\n')
    assert text.count(old)==1,(key,text.count(old))
    text=text.replace(old,new)
    changes.append({'key':key,'old':old,'new':new})
anchor=r'The middle line evaluates the specified polynomial at the original \(D\); every source vector lies in \(V\).'
ins=read(wave/'support/fragments/R1_SUPPORT_INSERT.tex')
ins='\n'.join(x for x in ins.splitlines() if not x.startswith('%'))+'\n'
replace('R1 complete original proper-source correction',anchor,anchor+'\n\n'+ins)
for item in json.loads(read(wave/'metric/ENDPOINT_CONCLUSION_REPLACEMENTS.json')):
    replace(item['key'],item['old'],item['new'])
replace('R58 current finite-circle source comparison',
        read(wave/'metric/conclusion_replacements/R58_OLD.tex'),
        read(wave/'metric/conclusion_replacements/R58_NEW.tex'))
boundary=json.loads(read(Path(args.boundary_json)))['records']
for item in boundary:
    if int(item['result'][1:])<63:
        replace(item['result']+' complete current boundary result',item['old'],item['new'])
tail=r'''The arithmetic norm theorem, sharp endpoint products and upper'''
assert text.count(tail)==1
cut=text.index(tail)
old_closing=text[cut:]
text=text[:cut].rstrip()+'\n\n'
changes.append({'key':'Concluding paragraph relocated and made current','old':old_closing,'new':'Revised after R74 below; original preserved in source.'})
holonomy=read(work/'holonomy_current_results_20260913.tex')
old=r'''$2q\log(1/(1-\delta_L^2))$.'''
new=old+r'''  This bound is attached to the arithmetic
average of the canonical quotient forms.  The exact comparison
is \(G_N=\overline G_N+\mathscr D_N\), with the displayed
positive integral of original relation corrections; the
continuous equal-image complex and its cochain contraction
realizing \(\overline G_N\) are given in R64 and the full HCD
proof.  The individual phase-source comparisons have their
stronger current common-polynomial-source controls in
(HC13)--(HC14).  Their averaging retains this separate
positive correction and all of its original entries.'''
assert holonomy.count(old)==1
holonomy=holonomy.replace(old,new)
(stage/'R63_R66_ORIGINAL.tex').write_bytes((work/'holonomy_current_results_20260913.tex').read_bytes())
(stage/'R63_R66_REVISED.tex').write_text(holonomy,encoding='utf-8')
changes.append({'key':'R63 phase-source versus averaged-quotient actual maps','old':old,'new':new})
late=read(stage/'R67_R74_REVISED.tex')
for item in boundary:
    if int(item['result'][1:])>=63:
        old=item['old'].replace('\r\n','\n');new=item['new'].replace('\r\n','\n')
        assert late.count(old)==1,(item['result'],late.count(old))
        late=late.replace(old,new)
        changes.append({'key':item['result']+' complete current boundary result','old':old,'new':new})
(stage/'R67_R74_WITH_BOUNDARY.tex').write_text(late,encoding='utf-8')
text+=holonomy.rstrip()+'\n\n'+late.rstrip()+'\n\n'
text+=r'''The complete preceding proofs now carry the corrected
source kernels, full two-parameter connections, actual tensor
specializations and current signed metric controls through their
earlier dependent calculations.  The original arithmetic norm
and endpoint lower products remain in the same estimates.
The finite signed residual is explicitly constructed for each
fixed source; its constants remain the original arithmetic
spectral data as the tensor order varies.  The complete source
provenance and earlier editions accompany this revised reader.
'''
out=stage/'research_conclusion.tex'
out.write_text(text,encoding='utf-8')
diff=''.join(difflib.unified_diff(raw.decode('utf-8-sig').replace('\r\n','\n').splitlines(True),text.splitlines(True),fromfile='research_conclusion_ORIGINAL.tex',tofile='research_conclusion.tex'))
(stage/'research_conclusion.diff').write_text(diff,encoding='utf-8')
(stage/'CONCLUSION_REPLACEMENTS.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
expected=list(range(1,75))
found=[int(x) for x in re.findall(r'\\paragraph\{Result R(\d+):',text)]
assert found==list(range(38,75)),found
receipt={'original_sha256':hashlib.sha256(raw).hexdigest(),'revised_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'lines':len(text.splitlines()),'literal_replacements':len(changes),'tail_boundary_included':True,'result_paragraphs':found,'requires_final_delta_read':True,'current_metric_r58_hash':hashlib.sha256((wave/'metric/conclusion_replacements/R58_NEW.tex').read_bytes()).hexdigest(),'source':str(out)}
(stage/'CONCLUSION_MERGE_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
