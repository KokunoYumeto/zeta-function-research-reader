"""Prepare source-anchored repairs of superscript/link parser corruption."""
from pathlib import Path
import re,json,hashlib,subprocess
ROOT=Path(__file__).resolve().parent
MATH=ROOT.parents[3]
STAGE=MATH/'work/backpropagation_20260913/cumulative_source_v1'
DELIVERY=MATH/'output/Split_Zero_Recursive_Integration_2026-09-13/repository'
SNAP=ROOT.parent/'snapshots/transcript'
LUA=SNAP/'ledger_publication/layout.lua'
def sha(b):return hashlib.sha256(b).hexdigest()
def pin(p):b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':sha(b)}
def tex(source,lua=False):
    args=['pandoc','--from=markdown+tex_math_single_backslash','--to=latex']
    if lua:args+=['--lua-filter='+str(LUA)]
    return subprocess.run(args,input=source,stdout=subprocess.PIPE,stderr=subprocess.PIPE,
        text=True,encoding='utf-8',check=True).stdout
def ws_pattern(s):
    return re.compile(r'\s+'.join(re.escape(x) for x in re.split(r'\s+',s.strip())))
def tokens(s):return re.findall(r'\\[A-Za-z@]+|\\[\s\S]|[A-Za-z0-9]+|[^\s]',s)

ledger_specs=[
 ('diag(e^{-aL},e^{aL})',r'\(\operatorname{diag}(e^{-aL},e^{aL})\)',1),
 ('P_{a,b}(s)=((s−1/2−a)^2+b²)((s−1/2+a)^2+b²)',r'\(P_{a,b}(s)=((s-1/2-a)^2+b^2)((s-1/2+a)^2+b^2)\)',1),
 ('c_i:H_c^i→H^i',r'\(c_i:H_c^i\to H^i\)',1),
 ('FNF^(−1)=q^(−1)N',r'\(FNF^{(-1)}=q^{(-1)}N\)',1),
 ('N z^j=z^{j+1}',r'\(N z^j=z^{j+1}\)',1),
 ('C_qNC_q^(−1)=q^(−1)N',r'\(C_qNC_q^{(-1)}=q^{(-1)}N\)',2),
 ('C_qU_aC_q^(−1)=a^{ρ(1−1/q)}U_{a^{1/q}}',r'\(C_qU_aC_q^{(-1)}=a^{\rho(1-1/q)}U_{a^{1/q}}\)',2),
 ('H_R=L2((e^−R,e^R),dx)',r'\(H_R=\text{L2}((e^{-R},e^R),dx)\)',1),
 ('G_N^ar≤C_h^kG_N^Γ',r'\(G_N^{ar}\le C_h^kG_N^{\Gamma}\)',1),
 ('H^{−1}=E_1,H^0=E_1',r'\(H^{-1}=E_1,H^0=E_1\)',1),
 ('H^0=F,H^1=0,H^2=E/F',r'\(H^0=F,H^1=0,H^2=E/F\)',1),
 ('Π^{−*}G_NΠ^{−1}',r'\(\Pi^{-*}G_N\Pi^{-1}\)',1),
 ('B_N^0→B_N^0',r'\(B_N^0\to B_N^0\)',1)]

ledger_raw=SNAP/'ledger_publication/ledger.md'
note_raw=ROOT.parent/'ta_c47/snapshots/C47_repository/dependencies/dependencies/MATHEMATICAL_NOTE.md'
pr_raw=STAGE/'sources/web_pr_13/files/workbenches/tau-orthogonal-boundary-control/RESEARCH_NOTE.md'
groups=[
 ('ledger','tex/cohorts/transcript/LEDGER_COMPLETE.tex',ledger_raw,ledger_specs,True),
 ('structural_note','tex/cohorts/inherited/MATHEMATICAL_NOTE_COMPLETE.tex',note_raw,
  [('I^G=p^(-1)(I)',r'\(I^G=p^{(-1)}(I)\)',1)],False),
 ('pr13','build/source_pr_13.tex',pr_raw,
  [('f_j^[N](x)',r'\(f_j^{[N]}(x)\)',1)],False)]
records=[];proposals=[]
for role,rel,source,specs,use_lua in groups:
    original=source.read_bytes().decode('utf-8-sig')
    source_copy=ROOT/'parser_repair_sources'/source.name
    if source_copy.exists() and source_copy.read_bytes()!=source.read_bytes():
        source_copy=ROOT/'parser_repair_sources'/(role+'_'+source.name)
    source_copy.parent.mkdir(exist_ok=True);source_copy.write_bytes(source.read_bytes())
    corrected=original
    # Start the ledger conversion from the already corrected exact exponent
    # source when checking the newly found, additional 15 superscript defects.
    if role=='ledger':
        for old,new in [('N(2R)=2^[K:Q]>1',r'\(N(2R)=2^{[K:Q]}>1\)'),
                        ('q=2^[K:Q]q',r'\(q=2^{[K:Q]}q\)')]:corrected=corrected.replace(old,new)
    before_source=corrected
    term_records=[]
    for raw,new,count in specs:
        assert original.count(raw)==count,(role,raw,'original count',original.count(raw))
        old_tex=tex(raw,use_lua).strip()
        new_tex=tex(new,use_lua).strip()
        assert new_tex==new,(role,new,new_tex)
        locations=[{'source_line':original[:m.start()].count('\n')+1,
                    'source_column':m.start()-original.rfind('\n',0,m.start()),
                    'source_exact_expression':m[0]} for m in re.finditer(re.escape(raw),original)]
        term_records.append({'original_expression':raw,'correct_math_tex':new,'old_generated_tex':old_tex,
            'expected_occurrences':count,'source_locations':locations})
        corrected=corrected.replace(raw,new)
    # Entire source-converter output changes only at the exact formula images.
    gen_before=tex(before_source,use_lua);gen_after=tex(corrected,use_lua)
    recovered=gen_after
    for t in term_records:
        assert recovered.count(t['correct_math_tex'])==t['expected_occurrences']
        recovered=recovered.replace(t['correct_math_tex'],t['old_generated_tex'])
    assert tokens(recovered)==tokens(gen_before),(role,'nonlocal generated body effect')
    conv_dir=ROOT/'full_parser_conversion'/role;conv_dir.mkdir(parents=True,exist_ok=True)
    for name,body in [('source_before.md',before_source),('source_corrected.md',corrected),
                      ('generated_before.tex',gen_before),('generated_corrected.tex',gen_after)]:
        (conv_dir/name).write_bytes(body.encode('utf-8'))

    for location,base in [('stage',STAGE),('delivery',DELIVERY)]:
        path=base/rel;raw_bytes=path.read_bytes();body=raw_bytes.decode('utf-8')
        changed=body;patches=[]
        for term in term_records:
            matches=list(ws_pattern(term['old_generated_tex']).finditer(changed))
            assert len(matches)==term['expected_occurrences'],(role,term['original_expression'],len(matches))
            for match in reversed(matches):
                old=match[0];new=term['correct_math_tex']
                patches.append({'offset':match.start(),'old':old,'new':new,
                    'old_active_line':body[:body.find(old)].count('\n')+1,
                    'source_expression':term['original_expression']})
                changed=changed[:match.start()]+new+changed[match.end():]
        restored=changed
        for term in reversed(term_records):
            old_images=[p['old'] for p in reversed(patches) if p['source_expression']==term['original_expression']]
            assert len(old_images)==term['expected_occurrences']
            for old in old_images:restored=restored.replace(term['correct_math_tex'],old,1)
        # Independent replacement order can change for duplicated identical
        # formulas only through their whitespace. Verify exact restoration by
        # direct reversible opcodes as the authoritative whole-body inverse.
        import difflib
        opcodes=[]
        for tag,a,b,c,d in difflib.SequenceMatcher(a=body,b=changed,autojunk=False).get_opcodes():
            if tag!='equal':opcodes.append({'old_start':a,'old_end':b,'new_start':c,'new_end':d,
                                           'old':body[a:b],'new':changed[c:d]})
        exact=changed
        for op in reversed(opcodes):exact=exact[:op['new_start']]+op['old']+exact[op['new_end']:]
        assert exact.encode('utf-8')==raw_bytes,(role,'full body inverse')
        out_before=ROOT/'parser_before'/location/rel;out_after=ROOT/'parser_after'/location/rel
        out_before.parent.mkdir(parents=True,exist_ok=True);out_after.parent.mkdir(parents=True,exist_ok=True)
        assert not out_before.exists() or out_before.read_bytes()==raw_bytes
        out_before.write_bytes(raw_bytes);out_after.write_bytes(changed.encode('utf-8'))
        rec={'role':role,'location':location,'active_path':str(path),'before':pin(out_before),'after':pin(out_after),
             'source':pin(source),'source_terms':term_records,'patches':patches,'exact_inverse_opcodes':opcodes,
             'fullbody_inverse_exact':True,'full_converter_generated_body_other_tokens_identical':True,
             'active_file_changed':False}
        records.append(rec)
    proposals+=term_records
(ROOT/'PARSER_CORRECTION_PROPOSALS.json').write_text(json.dumps({'scope':'Exact source-anchored corrections of 15 swallowed ledger superscripts, one inherited note superscript and one PR13 truncation-index hyperlink.',
    'records':records,'unique_source_expressions':len(proposals),'confirmed_occurrences_per_repository':17,
    'active_mutations_performed':False,'raw_historical_sources_changed':False,
    'presentation_dictionary':{'−':'-', '²':'^2','ρ':r'\rho','Π':r'\Pi','Γ':r'\Gamma','→':r'\to','≤':r'\le',
        'diag':'operatorname{diag}','L2':'text{L2}; original literal name retained without changing it to L^2',
        '^(-1)':'^{(-1)}; original exponent parentheses retained'}},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'files_prepared':len(records),'occurrences_per_repository':17,'exact_fullbody_inverses':True,
    'all_full_generated_body_other_tokens_unchanged':True,'active_files_changed':False}))
