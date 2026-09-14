from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path('workspace:')
OUT=Path(__file__).resolve().parent
LEDGER=ROOT/'work/backpropagation_20260913/cohort_staging/snapshots/transcript/ledger_publication'
scan=json.loads((OUT/'SOURCE_SCAN.json').read_text(encoding='utf-8'))
graph=json.loads((OUT.parent/'ACTIVE_TEX_SCAN.json').read_text(encoding='utf-8-sig'))
active=next(f for f in graph['roots']['stage']['files'] if f['path'].endswith('/LEDGER_COMPLETE.tex'))
tex=(LEDGER/'ledger.tex').read_text(encoding='utf-8-sig')
items=[
('formation',133,'diag(e^{-aL},e^{aL})',r'\(\operatorname{diag}(e^{-aL},e^{aL})\)'),
('formation',193,'P_{a,b}(s)=((s−1/2−a)^2+b²)((s−1/2+a)^2+b²)',r'\(P_{a,b}(s)=((s-1/2-a)^2+b^2)((s-1/2+a)^2+b^2)\)'),
('formation',377,'c_i:H_c^i→H^i',r'\(c_i:H_c^i\to H^i\)'),
('formation',479,'FNF^(−1)=q^(−1)N',r'\(FNF^{(-1)}=q^{(-1)}N\)'),
('formation',479,'N z^j=z^{j+1}',r'\(N z^j=z^{j+1}\)'),
('formation',487,'C_qNC_q^(−1)=q^(−1)N',r'\(C_qNC_q^{(-1)}=q^{(-1)}N\)'),
('formation',487,'C_qU_aC_q^(−1)=a^{ρ(1−1/q)}U_{a^{1/q}}',r'\(C_qU_aC_q^{(-1)}=a^{\rho(1-1/q)}U_{a^{1/q}}\)'),
('formation',530,'C_qNC_q^(−1)=q^(−1)N',r'\(C_qNC_q^{(-1)}=q^{(-1)}N\)'),
('formation',530,'C_qU_aC_q^(−1)=a^{ρ(1−1/q)}U_{a^{1/q}}',r'\(C_qU_aC_q^{(-1)}=a^{\rho(1-1/q)}U_{a^{1/q}}\)'),
('typed',241,'H_R=L2((e^−R,e^R),dx)',r'\(H_R=\mathrm{L2}((e^{-R},e^R),dx)\)'),
('late',137,'G_N^ar≤C_h^kG_N^Γ',r'\(G_N^{\mathrm{ar}}\le C_h^kG_N^\Gamma\)'),
('late',243,'H^{−1}=E_1,H^0=E_1',r'\(H^{-1}=E_1,H^0=E_1\)'),
('late',270,'H^0=F,H^1=0,H^2=E/F',r'\(H^0=F,H^1=0,H^2=E/F\)'),
('late',324,'Π^{−*}G_NΠ^{−1}',r'\(\Pi^{-*}G_N\Pi^{-1}\)'),
('late',376,'B_N^0→B_N^0',r'\(B_N^0\to B_N^0\)'),
]
assert len(items)==len(active['superscript_commands'])==15
proposals=[]
for num,((slug,line,raw,replacement),old_active) in enumerate(zip(items,active['superscript_commands']),1):
    src=next(f for f in scan['files'] if f['slug']==slug and f['role']=='packaged')
    original=next(f for f in scan['files'] if f['slug']==slug and f['role']=='original')
    lines=(ROOT/src['path']).read_text(encoding='utf-8-sig').splitlines()
    assert raw in lines[line-1],(slug,line,raw)
    cmd=['pandoc','--from=markdown+tex_math_single_backslash','--to=latex','--wrap=none','--lua-filter='+str(LEDGER/'layout.lua')]
    old_tex=subprocess.run(cmd,input=raw.encode('utf-8'),capture_output=True,check=True).stdout.decode('utf-8').strip()
    regex=r'\s+'.join(re.escape(piece) for piece in old_tex.split())
    matched=[{'line':tex.count('\n',0,m.start())+1,'column':m.start()-tex.rfind('\n',0,m.start()),'exact_old_tex_phrase':m.group()} for m in re.finditer(regex,tex)]
    # Pandoc adds typographic escapes context-sensitively; retain standalone conversion and exact old active line if full expression matching fails.
    new_ast=json.loads(subprocess.run(['pandoc','--from=markdown+tex_math_single_backslash','--to=json'],input=replacement.encode('utf-8'),capture_output=True,check=True).stdout)
    assert new_ast['blocks'][0]['c'][0]['t']=='Math'
    assert len(new_ast['blocks'][0]['c'])==1
    rec={'id':f'SUP{num:02d}','classification':'false Markdown superscript formed by pairing separate mathematical caret operators','slug':slug,'packaged_path':src['path'],'original_path':original['path'],'source_sha256':src['sha256'],'source_line':line,'source_column':lines[line-1].index(raw)+1,'exact_original_phrase':raw,'exact_original_line':lines[line-1],'active_path':active['path'],'active_source_line':old_active['line'],'exact_old_active_source_line':old_active['source_line'].rstrip('\r'),'standalone_old_tex_phrase':old_tex,'frozen_ledger_tex_matches':matched,'proposed_inline_math':replacement,'proposal_parse':'one InlineMath node, zero Note and Superscript nodes'}
    if slug=='typed':rec['notation_note']='The ledger source spells the space L2; proposal preserves those literal characters with \\mathrm{L2}. Recasting it as L^2 would require an explicitly documented source-typography correction; transcript witness is being checked separately.'
    if '^(−1)' in raw:rec['notation_note']='Original parenthesized inverse exponent is retained as {(-1)}; no sign or exponent simplification.'
    proposals.append(rec)
links=[]
for num,(raw,replacement,active_line) in enumerate([
    ('q_k=[1+k(m−1)](k+1)²',r'\(q_k=[1+k(m-1)](k+1)^2\)',8275),
    ('L_{h,k}=2δ[1+k(m−1)](k+1)floor((k+1)²/4)',r'\(L_{h,k}=2\delta[1+k(m-1)](k+1)\operatorname{floor}((k+1)^2/4)\)',8276),
],1):
    src=next(f for f in scan['files'] if f['slug']=='late' and f['role']=='packaged')
    original=next(f for f in scan['files'] if f['slug']=='late' and f['role']=='original')
    source_line=(ROOT/src['path']).read_text(encoding='utf-8-sig').splitlines()[83]
    assert raw in source_line
    old_tex=subprocess.run(['pandoc','--from=markdown+tex_math_single_backslash','--to=latex','--wrap=none','--lua-filter='+str(LEDGER/'layout.lua')],input=raw.encode('utf-8'),capture_output=True,check=True).stdout.decode('utf-8').strip()
    regex=r'\s+'.join(re.escape(piece) for piece in old_tex.split())
    matches=[{'line':tex.count('\n',0,m.start())+1,'column':m.start()-tex.rfind('\n',0,m.start()),'exact_old_tex_phrase':m.group()} for m in re.finditer(regex,tex)]
    assert len(matches)==1
    new_ast=json.loads(subprocess.run(['pandoc','--from=markdown+tex_math_single_backslash','--to=json'],input=replacement.encode('utf-8'),capture_output=True,check=True).stdout)
    assert len(new_ast['blocks'][0]['c'])==1 and new_ast['blocks'][0]['c'][0]['t']=='Math'
    links.append({'id':f'LINK{num:02d}','classification':'false Markdown hyperlink: adjacent bracket factor and parenthesis factor parsed as link label and target','packaged_path':src['path'],'original_path':original['path'],'source_sha256':src['sha256'],'source_line':84,'source_column':source_line.index(raw)+1,'exact_original_phrase':raw,'exact_original_line':source_line,'active_path':active['path'],'active_source_line':active_line,'standalone_old_tex_phrase':old_tex,'frozen_ledger_tex_matches':matches,'proposed_inline_math':replacement,'proposal_parse':'one InlineMath node, zero Link/Note/Superscript nodes','preservation_note':'The mathematical [1+k(m−1)] factor and adjacent (k+1) factor must both remain visible. floor is retained as an operator word with its original parenthesized argument; no evaluation or normalization.'})
notes=[]
formation=next(f for f in scan['files'] if f['slug']=='formation' and f['role']=='packaged')
for i,occ in enumerate(formation['occurrences'],1):
    notes.append({'id':f'NOTE{i:02d}','classification':'field-degree exponent, not a genuine footnote','source_path':formation['path'],'source_sha256':formation['sha256'],'source_line':occ['line'],'source_column':occ['column'],'raw_marker':'^[K:Q]','original_line':occ['line_text'].rstrip('\r'),'proposed_exact_exponent':r'2^{[K:Q]}','reason':'The bracketed field degree [K:Q] is the exponent of the base 2 in N(2R)=2^[K:Q]>1 and q=2^[K:Q]q. The same line uses the power in the absorption argument; there is no note text or note reference.'})
receipt={'status':'read-only proposals; no active edits; no PDF build','coverage':{'manifest_entries':12,'packaged_markdown_files':12,'original_markdown_files':12,'missing_files':[],'hash_mismatches':[],'inline_caret_bracket_occurrences_per_corpus':2,'genuine_footnotes':0,'false_pandoc_note_nodes':2,'false_pandoc_superscript_nodes':15,'false_pandoc_formula_links':2},'mechanism':'build_ledger.py invokes Pandoc --from=markdown+tex_math_single_backslash, retaining default inline_notes and superscript extensions. Pandoc parses bare ^[K:Q] as Note and un-delimited pairs of ^ as Superscript before layout.lua visits Str/Code/Math. It also parses adjacent [1+k(m−1)](k+1) mathematical factors as a hyperlink to k+1. Actual AST probes of all 12 Markdown files reproduce exactly two Notes, fifteen Superscripts and the two formula Links. Every proposed expression parses as a single InlineMath node.','footnote_candidates':notes,'superscript_proposals':proposals,'formula_link_proposals':links,'inputs':{'source_scan_sha256':hashlib.sha256((OUT/'SOURCE_SCAN.json').read_bytes()).hexdigest(),'parser_probe_sha256':hashlib.sha256((OUT/'PARSER_PROBE.json').read_bytes()).hexdigest(),'parent_active_scan_sha256':hashlib.sha256((OUT.parent/'ACTIVE_TEX_SCAN.json').read_bytes()).hexdigest(),'frozen_ledger_tex_sha256':hashlib.sha256((LEDGER/'ledger.tex').read_bytes()).hexdigest()}}
(OUT/'CLASSIFICATION_AND_PROPOSALS.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
md=['# Source-faithful ledger conversion audit','',receipt['status']+'.','',receipt['mechanism'],'','All 24 source files exist and match their manifest hashes and bytes. Exactly two raw `^[K:Q]` occurrences are field-degree exponents; no genuine source footnotes were found.','']
for p in proposals:
    md += [f"## {p['id']}: {p['slug']}:{p['source_line']}",'',f"Original path: `{p['original_path']}`",f"Source SHA-256: `{p['source_sha256']}`",'',f"Original: `{p['exact_original_phrase']}`",'',f"Old active TeX line {p['active_source_line']}: `{p['exact_old_active_source_line']}`",'',f"Proposed: `{p['proposed_inline_math']}`",'']
    if p.get('notation_note'):md += [p['notation_note'],'']
for p in links:
    md += [f"## {p['id']}: late:84",'',f"Original path: `{p['original_path']}`",f"Source SHA-256: `{p['source_sha256']}`",'',f"Original: `{p['exact_original_phrase']}`",'',f"Old TeX: `{p['standalone_old_tex_phrase']}`",'',f"Proposed: `{p['proposed_inline_math']}`",'',p['preservation_note'],'']
(OUT/'CLASSIFICATION_AND_PROPOSALS.md').write_text('\n'.join(md),encoding='utf-8')
for p in proposals:print(p['id'],p['slug'],p['source_line'],p['proposed_inline_math'],'frozen matches',len(p['frozen_ledger_tex_matches']))
print('proposal receipt SHA256',hashlib.sha256((OUT/'CLASSIFICATION_AND_PROPOSALS.json').read_bytes()).hexdigest())
