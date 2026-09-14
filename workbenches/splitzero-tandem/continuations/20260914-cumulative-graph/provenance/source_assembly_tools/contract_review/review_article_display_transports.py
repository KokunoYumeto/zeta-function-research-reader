"""Independent read-only replay of five display transports; writes only audit evidence."""
from pathlib import Path
from collections import Counter
import ast, datetime, hashlib, json, re

ROOT = Path(r'workspace:')
OUT = Path(__file__).parent
STAGE = ROOT/'work/backpropagation_20260913/cumulative_graph_successor_v2'
SCRIPT = ROOT/'work/backpropagation_20260913/cumulative_graph_successor_support/repair_article_display_widths.py'
RECEIPT = STAGE/'provenance/ARTICLE_DISPLAY_WIDTH_TRANSPORTS.json'

def sha(data):
    return hashlib.sha256(data).hexdigest()

def decomment(s):
    return re.sub(r'(?<!\\)%[^\n]*','',s)

def tokens(s):
    return re.findall(r'\\[A-Za-z@]+|\\.|[^\\\s]',s)

def presentation_projection(s):
    """Only erase the exact enumerated layout constructs, never algebraic tokens."""
    s=s.replace(r'\begin{gathered}','').replace(r'\end{gathered}','')
    return [t for t in tokens(s) if t not in (r'\quad',r'\qquad',r'\\','&')]

def balanced_arguments(s, command):
    result=[]
    for m in re.finditer(r'\\'+command+r'\*?\s*\{',decomment(s)):
        start=m.end(); depth=1; pos=start
        while depth and pos<len(s):
            if s[pos]=='{' and s[pos-1]!='\\': depth+=1
            elif s[pos]=='}' and s[pos-1]!='\\': depth-=1
            pos+=1
        if depth: raise AssertionError('unclosed '+command)
        result.append(s[start:pos-1])
    return result

raw_receipt=RECEIPT.read_bytes()
receipt=json.loads(raw_receipt)
history=STAGE/'history/cumulative_build_candidates'/receipt['candidate_pdf_sha256']
tree=ast.parse(SCRIPT.read_text(encoding='utf-8-sig'))
script_changes=next(ast.literal_eval(n.value) for n in tree.body
                    if isinstance(n,ast.Assign) and any(isinstance(x,ast.Name) and x.id=='changes' for x in n.targets))
receipt_changes=[(x['path'],x['old'],x['new']) for x in receipt['operations']]
assert script_changes==receipt_changes
assert len(receipt_changes)==5

interpretations={
 'tex/phase_graph_v2/dep01.tex':'The six definitions/equalities keep F=S G^(-1/2), F*F=I_d, J_0=G^(-1/2)JG^(-1/2), X=A I_d+iJ_0, C_0=G^(1/2)CG^(-1/2), and L=X-C_0 in exactly that order. Two separator quads become row breaks. No factor, exponent, sign, coordinate or equality changes.',
 'tex/phase_graph_v2/dep08.tex':'One row break is inserted after the complete left-hand fractional power and before the existing <= token. The full factorial, b exponent, sum M_h(b)^k+M_h(-b)^k, exponential alpha_0(L+k-3), polynomial power B_h, denominator c_h vartheta_h^(k-3) mathfrak l_n(L), and outer power 1/(2r) retain all tokens and order.',
 'tex/phase_graph_v2/RMT.tex':'The function H_a, its derivative and its inverse retain every original token. The inverse expression moves to the second row; the separator qquad is removed there. Domain z>0 remains attached to that inverse expression; the surrounding B>0 hypothesis is outside the replaced span and byte-identical.',
 'tex/phase_graph_v2/PGD.tex':'The outer boxed argument remains intact. The complete pair of preceq comparisons, c_k=1+k^2 A^2, E_(k,N)=k^2 F_k L_N D_N/a_k, and restrictions k>=3 and N>=0 retain all tokens in order. Only outer spacing/separator controls become three gathered rows.',
 'tex/research_conclusion.tex':'The negative squared norm remains on the same side of the equality with all inverse square-root and ordered matrix factors unchanged. The closing norm power and comma are retained, followed by a new aligned row containing the unchanged definition Z_(2q)^mix=(D_mix,f_(2q)). The added ampersand is an alignment marker; it introduces no mathematical term.'
}
evidence=[]
for op in receipt['operations']:
    relative=op['path']
    before_path=history/relative
    after_path=STAGE/relative
    before=before_path.read_bytes()
    after=after_path.read_bytes()
    old=op['old'].encode('utf-8')
    new=op['new'].encode('utf-8')
    before_text=before.decode('utf-8')
    after_text=after.decode('utf-8')
    checks={
        'before_hash_matches_receipt':sha(before)==op['before']['sha256'],
        'before_size_matches_receipt':len(before)==op['before']['bytes'],
        'after_hash_matches_receipt':sha(after)==op['after']['sha256'],
        'after_size_matches_receipt':len(after)==op['after']['bytes'],
        'unique_old_span_in_predecessor':before.count(old)==1,
        'unique_new_span_in_current':after.count(new)==1,
        'forward_full_bytes':before.replace(old,new)==after,
        'inverse_full_bytes':after.replace(new,old)==before,
        'nonlayout_tex_tokens_same_in_exact_order':presentation_projection(op['old'])==presentation_projection(op['new']),
        'all_ordered_tag_arguments_unchanged':balanced_arguments(before_text,'tag')==balanced_arguments(after_text,'tag'),
        'all_ordered_label_arguments_unchanged':balanced_arguments(before_text,'label')==balanced_arguments(after_text,'label'),
        'all_ordered_reference_arguments_unchanged':balanced_arguments(before_text,'ref')==balanced_arguments(after_text,'ref'),
    }
    assert all(checks.values()),(relative,checks)
    offset_before=before.find(old)
    offset_after=after.find(new)
    start_display=after_text.rfind(r'\[',0,after_text.find(op['new']))
    end_display=after_text.find(r'\]',after_text.find(op['new']))+2
    whole_display=after_text[start_display:end_display]
    old_layout=Counter(t for t in tokens(op['old']) if t in (r'\quad',r'\qquad',r'\\','&'))
    new_layout=Counter(t for t in tokens(op['new']) if t in (r'\quad',r'\qquad',r'\\','&'))
    evidence.append({
        'path':relative,
        'before_file':str(before_path.relative_to(ROOT)).replace('\\','/'),
        'after_file':str(after_path.relative_to(ROOT)).replace('\\','/'),
        'before':{'sha256':sha(before),'bytes':len(before),'offset':offset_before,'line':before[:offset_before].count(b'\n')+1},
        'after':{'sha256':sha(after),'bytes':len(after),'offset':offset_after,'line':after[:offset_after].count(b'\n')+1},
        'checks':checks,
        'mathematical_control_and_character_token_count':len(presentation_projection(op['old'])),
        'complete_preserved_token_sequence':presentation_projection(op['old']),
        'before_layout_controls':dict(old_layout),
        'after_layout_controls':dict(new_layout),
        'gathered_pairs_added':op['new'].count(r'\begin{gathered}')-op['old'].count(r'\begin{gathered}'),
        'old':op['old'],'new':op['new'],
        'complete_current_display':whole_display,
        'display_tags':balanced_arguments(whole_display,'tag'),
        'display_labels':balanced_arguments(whole_display,'label'),
        'interpretation':interpretations[relative]
    })

# Every preserved character/control token, including braces and relation signs,
# is compared in its original order. Only the listed layout tokens are projected
# out for that separate check; byte inverse equality above reconstructs EVERYTHING.
all_current_stable=all(sha((STAGE/e['path']).read_bytes())==e['after']['sha256'] for e in evidence)
assert all_current_stable
report={
 'status':'PASS',
 'audit_completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'scope':'Five source display-line transports; no TeX execution or source mutations.',
 'source_receipt':str(RECEIPT.relative_to(ROOT)).replace('\\','/'),
 'source_receipt_sha256':sha(raw_receipt),
 'repair_script':str(SCRIPT.relative_to(ROOT)).replace('\\','/'),
 'repair_script_sha256':sha(SCRIPT.read_bytes()),
 'script_literal_changes_exactly_match_receipt':True,
 'operation_count':5,
 'before_and_after_hashes_match':True,
 'full_byte_forward_and_inverse_replay_all_five':True,
 'ordered_nonlayout_tex_tokens_equal_all_five':True,
 'all_tag_label_reference_arguments_preserved':True,
 'stage_sources_stable_on_final_reread':all_current_stable,
 'projection_definition':r'Remove only exact \begin{gathered}, \end{gathered}, whitespace, \quad, \qquad, \\, and alignment & from the changed fragments; retain every other TeX control/character token including braces, signs, ordered factors, exponents, punctuation and constants. This is a finite lexical comparison, with no algebraic simplification or formula rewrite.',
 'layout_semantics':'The installed amsmath.sty lines 1525-1539 defines gathered with a displaystyle math cell (line 1534). All four gathered additions occur inside existing display math; PGD remains inside the original boxed argument. The conclusion already uses aligned and adds only one row break and ampersand before its original Z definition. No macro declaration spans one of the inserted row boundaries.',
 'tocdepth_review':'Separate independent tocdepth_state_independent_review.json/.md in this directory.',
 'operations':evidence,
 'limitations':['This verifies exact source transport and its layout-only nature, not PDF layout quality or mathematical theorem truth.','The second three-pass build is owned by the parent and was not invoked or interrupted.']
}
(OUT/'article_display_width_independent_review.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
md=['# Independent display-width transport review','',
    'PASS. All five current source files match their recorded after hashes. Each archived predecessor matches its before hash. Applying the recorded replacement reconstructs the entire current file; applying its inverse reconstructs the entire archived predecessor byte for byte. The source repair script was parsed as data, never imported or executed, and its five literal replacements exactly match the receipt.','',
    'After erasing only the explicitly listed layout constructs, every other TeX control/character token is identical in its original order. This retains all signs, constants, ordered factors, exponents, grouping braces and punctuation. Every tag, label and reference argument in each complete file is unchanged. The JSON contains full old/new fragments, full current displays, exact preserved token sequences, byte offsets, hashes and every check.','',
    '| Source | Current line | Display tag | Preserved tokens | Inverse bytes |',
    '|---|---:|---|---:|---|']
for e in evidence:
    md.append('| '+e['path']+' | '+str(e['after']['line'])+' | '+', '.join(e['display_tags'])+' | '+str(e['mathematical_control_and_character_token_count'])+' | exact |')
md+=['','## Per-display assessment','']
for e in evidence:
    md.extend(['### '+e['path'],'',e['interpretation'],''])
md+=['## Scope and layout semantics','',
      report['projection_definition'],'',
      report['layout_semantics'],'',
      'No TeX was run. No stage, predecessor, reader or repair-script source was modified. All five current files remained unchanged on the final hash reread. The second build and PDF quality checks remain with the parent. The tocdepth wrapper has a separate independent receipt in this directory.','']
(OUT/'article_display_width_independent_review.md').write_text('\n'.join(md),encoding='utf-8')
print(json.dumps({'status':'PASS','operations':5,'full_byte_inverse_all':True,'math_token_order_all':True,'tags_preserved_all':True,'files_stable':all_current_stable,'reports':['article_display_width_independent_review.json','article_display_width_independent_review.md']},indent=2))
