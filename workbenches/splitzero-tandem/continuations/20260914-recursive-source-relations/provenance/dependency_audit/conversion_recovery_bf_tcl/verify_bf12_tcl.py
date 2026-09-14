"""Independent bounded BF12/TCL.2 verification; writes only beside this script."""
from pathlib import Path
from datetime import datetime, timezone
import difflib
import hashlib
import json
import re
import shutil
import subprocess

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
WORK = ROOT / 'work/backpropagation_20260913'
BF = WORK / 'cohort_staging/ledger_exponent_correction'
TCL = WORK / 'page_qa/tcl2_display_repair'
assert OUT == ROOT / 'work/backpropagation_20260913/dependency_audit/conversion_recovery_bf_tcl'
START = datetime.now(timezone.utc).isoformat()

def sha(data):
    return hashlib.sha256(data).hexdigest()

def pin(path, data=None):
    data = path.read_bytes() if data is None else data
    return {'path': str(path), 'bytes': len(data), 'sha256': sha(data)}

def save(name, data):
    path = OUT / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return pin(path, data)

def span(data, token):
    assert data.count(token) == 1, (token, data.count(token))
    start = data.index(token)
    end = start + len(token)
    return {'start_byte_0': start, 'end_byte_0_exclusive': end,
            'start_line_1': data[:start].count(b'\n')+1,
            'end_line_1': data[:end-1].count(b'\n')+1,
            'literal_utf8': token.decode('utf-8'), 'sha256': sha(token)}

def exact_replay(before, after, pairs):
    expected = before
    details = []
    for old, new in pairs:
        details.append({'before': span(before, old), 'after': span(after, new)})
        assert expected.count(old) == 1
        expected = expected.replace(old, new, 1)
    assert expected == after, 'Forward whole-file byte replay mismatch'
    inverse = after
    for old, new in reversed(pairs):
        assert inverse.count(new) == 1
        inverse = inverse.replace(new, old, 1)
    assert inverse == before, 'Inverse whole-file byte replay mismatch'
    return {'forward_whole_file_byte_equal': True, 'inverse_whole_file_byte_equal': True,
            'all_bytes_outside_replacement_spans_identical': True,
            'inverse_sha256': sha(inverse), 'replacement_count': len(pairs), 'spans': details}

def bf_block(data):
    start = data.index(b'\\subsubsection{BF12 ')
    end = data.index(b'\\subsubsection{BF13 ', start)
    return data[start:end]

applied_path = BF / 'APPLIED_LEDGER_EXPONENT_CORRECTION.json'
applied = json.loads(applied_path.read_bytes())
source_pins = []
for item in applied['source_records']:
    original = Path(item['original']['path'])
    retained = Path(item['retained']['path'])
    a, b = original.read_bytes(), retained.read_bytes()
    assert a == b
    assert sha(a) == item['original']['sha256'] == item['retained']['sha256']
    assert len(a) == item['original']['bytes'] == item['retained']['bytes']
    source_pins.append({'original': pin(original, a), 'retained': pin(retained, b),
                        'original_equals_retained_bytes': True, 'recorded_pins_verified': True})

ledger_path = BF / 'original_sources/ledger.md'
formation_path = BF / 'original_sources/formation.md'
witness_path = BF / 'original_sources/A0862.md'
ledger, formation, witness = [p.read_bytes() for p in (ledger_path, formation_path, witness_path)]
source_tokens = [b'N(2R)=2^[K:Q]>1', b'q=2^[K:Q]q']
good = [br'\(N(2R)=2^{[K:Q]}>1\)', br'\(q=2^{[K:Q]}q\)']
bad = [br'N(2R)=2\footnote{K:Q}\textgreater1', br'q=2\footnote{K:Q}q']
corrected_path = BF / 'corrected_ledger_source_not_overwriting_original.md'
corrected = corrected_path.read_bytes()
markdown_replay = exact_replay(ledger, corrected, list(zip(source_tokens, good)))
original_line = next(line for line in ledger.splitlines() if source_tokens[0] in line)
formation_line = next(line for line in formation.splitlines() if source_tokens[0] in line)
assert original_line == formation_line
source_witnesses = {'ledger': pin(ledger_path), 'formation': pin(formation_path),
                    'A0862': pin(witness_path), 'ledger_and_formation_proof_paragraph_bytes_equal': True,
                    'proof_paragraph_utf8': original_line.decode('utf-8'),
                    'source_expressions': [{'ledger':span(ledger, token), 'formation':span(formation, token)}
                                           for token in source_tokens],
                    'original_degree_and_equations': [span(witness, token) for token in
                         [br'd=[K:\mathbb Q].', br'N_K(2R)=2^d.', br'q=2^dq.', br'q=2^{[K:\mathbb Q]}q']]}

retained_active_checks = []
active_reads = []
for entry in applied['active_changes']:
    before_path, after_path = Path(entry['before']['path']), Path(entry['after']['path'])
    before, after = before_path.read_bytes(), after_path.read_bytes()
    for side, data in [('before',before),('after',after)]:
        assert sha(data) == entry[side]['sha256'] and len(data) == entry[side]['bytes']
    replay = exact_replay(before, after, list(zip(bad, good)))
    active_path = Path(entry['active'])
    current = active_path.read_bytes()
    active_reads.append((active_path,current))
    assert all(current.count(t)==1 for t in good)
    assert all(t not in current for t in bad)
    assert br'\footnote{K:Q}' not in current
    assert bf_block(current) == bf_block(after)
    current_snapshot = save('active_snapshots/'+entry['location']+'_LEDGER_COMPLETE.tex',current)
    diff = ''.join(difflib.unified_diff(after.decode('utf-8').splitlines(keepends=True),
                   current.decode('utf-8').splitlines(keepends=True),
                   fromfile='retained_bf12_only_after',tofile='active_'+entry['location']))
    diff_pin = save('active_differences/'+entry['location']+'_ledger_from_bf12_only_after.diff',diff.encode('utf-8'))
    retained_active_checks.append({'location':entry['location'],'before':pin(before_path,before),
        'after':pin(after_path,after),'exact_replay':replay,
        'current_active':pin(active_path,current),'current_snapshot':current_snapshot,
        'current_active_equals_bf12_only_after':current==after,
        'current_BF12_block_equals_bf12_only_after':True,'current_BF12_block_sha256':sha(bf_block(current)),
        'current_repaired_spans':[span(current,t) for t in good],
        'current_bad_expressions_absent':True,'active_delta_from_bf12_only_after':diff_pin,
        'active_delta_scope':'Other later changes are recorded here but are audited by the parent; no full-file equality to BF12-only state is inferred.'})
assert active_reads[0][1] == active_reads[1][1]
final_map_path=BF/'final_application/APPLIED_FINAL_CONVERTER_CORRECTIONS.json'
final_map=json.loads(final_map_path.read_bytes())
correction_chain=[]
for current_check in retained_active_checks:
    location=current_check['location']
    record=next(r for r in final_map['records'] if r['location']==location and r['path']=='tex/cohorts/transcript/LEDGER_COMPLETE.tex')
    next_before_path=BF/'final_application/before'/location/record['path']
    next_before=next_before_path.read_bytes()
    bf_after=Path(current_check['after']['path']).read_bytes()
    assert next_before==bf_after
    assert sha(next_before)==record['before_sha256']
    assert current_check['current_active']['sha256']==record['after_sha256']
    correction_chain.append({'location':location,'final_application_record':record,
        'next_before':pin(next_before_path,next_before),
        'BF12_after_equals_later_repairs_before_whole_bytes':True,
        'current_active_hash_equals_later_repairs_after_record':True,
        'BF12_block_preserved_through_later_repairs_whole_bytes':True,
        'qualification':'The chain endpoints and unchanged BF12 block are independently checked here; the parent audits the 17 intervening ledger replacement spans.'})

# Reproduce the parser and generated-body evidence with the actual retained Lua filter.
# Do not call historical scripts: they mutate active inputs.
pandoc = shutil.which('pandoc')
assert pandoc
version = subprocess.run([pandoc,'--version'],capture_output=True,check=True).stdout.decode('utf-8')
base_args = [pandoc,'--from=markdown+tex_math_single_backslash']
def convert(data,target,extra=()):
    run = subprocess.run(base_args+['--to='+target,*extra],input=data,capture_output=True,check=True)
    return run.stdout
def nodes(value, kind):
    if isinstance(value,dict):
        return ([value] if value.get('t')==kind else []) + [x for v in value.values() for x in nodes(v,kind)]
    if isinstance(value,list):
        return [x for v in value for x in nodes(v,kind)]
    return []
ast_before = json.loads(convert(ledger,'json'))
ast_after = json.loads(convert(corrected,'json'))
notes_before,notes_after = nodes(ast_before,'Note'),nodes(ast_after,'Note')
assert len(notes_before)==2 and notes_after==[]
assert all(n=={'t':'Note','c':[{'t':'Para','c':[{'t':'Str','c':'K:Q'}]}]} for n in notes_before)
math_after = nodes(ast_after,'Math')
assert all(sum(n['c']==[{'t':'InlineMath'},t.decode('utf-8')[2:-2]] for n in math_after)==1 for t in good)
generated_before_native = convert(ledger,'latex',('--lua-filter='+str(BF/'original_sources/layout.lua'),))
generated_after_native = convert(corrected,'latex',('--lua-filter='+str(BF/'original_sources/layout.lua'),))
# The original correction script used subprocess text=True, whose Windows
# stdout decoding replaces CRLF by LF. Retain both native stdout and the
# exact returned text bytes; do not silently assert native pipe equality.
generated_before = generated_before_native.replace(b'\r\n',b'\n')
generated_after = generated_after_native.replace(b'\r\n',b'\n')
assert b'\r' not in generated_before and b'\r' not in generated_after
assert generated_before.replace(b'\n',b'\r\n') == generated_before_native
assert generated_after.replace(b'\n',b'\r\n') == generated_after_native
native_generated_pins = [save('independent_generated/'+n,b) for n,b in
                  [('original_native_stdout.tex',generated_before_native),('corrected_native_stdout.tex',generated_after_native)]]
generated_pins = [save('independent_generated/'+n,b) for n,b in
                  [('original.tex',generated_before),('corrected.tex',generated_after)]]
recorded_generated = applied['full_combined_ledger_conversion_check']
for key, data in [('original_generated',generated_before),('corrected_generated',generated_after)]:
    assert data == Path(recorded_generated[key]['path']).read_bytes()
    assert sha(data) == recorded_generated[key]['sha256'] and len(data) == recorded_generated[key]['bytes']
restored_generated = generated_after
for old,new in reversed(list(zip(bad,good))):
    assert generated_before.count(old)==1 and generated_after.count(new)==1
    restored_generated=restored_generated.replace(new,old,1)
lex = lambda data: re.findall(rb'\\[A-Za-z@]+|\\[\s\S]|[A-Za-z0-9]+|[^\s]',data)
assert lex(restored_generated)==lex(generated_before)
generated_diff=''.join(difflib.unified_diff(generated_before.decode('utf-8').splitlines(keepends=True),
                     restored_generated.decode('utf-8').splitlines(keepends=True),
                     fromfile='original_generated',tofile='inverse_corrected_generated'))
generated_diff_pin=save('independent_generated/inverse_generated_line_wrap.diff',generated_diff.encode('utf-8'))
parser_check={'pandoc_executable':pandoc,'pandoc_version':version.splitlines()[0],
    'parser_arguments':base_args,'lua_filter':pin(BF/'original_sources/layout.lua'),
    'original_Note_nodes':notes_before,'corrected_Note_nodes':notes_after,
    'corrected_math_nodes':[n for n in math_after if n['c'][1] in [t.decode('utf-8')[2:-2] for t in good]],
    'native_stdout_pins':native_generated_pins,'independent_generated_pins':generated_pins,
    'native_stdout_line_endings':'CRLF at every line ending; exact inverse to the original script text-stream LF representation verified',
    'native_stdout_CRLF_counts':[generated_before_native.count(b'\r\n'),generated_after_native.count(b'\r\n')],
    'original_script_text_stream_generated_equals_recorded_bytes':True,
    'inverse_generated_bytes_equal':restored_generated==generated_before,
    'inverse_generated_nonwhitespace_tex_token_sequence_equal':True,
    'inverse_generated_line_wrap_diff':generated_diff_pin,
    'qualification':'The two exact active-file repairs are whole-byte reversible. Fresh full-body Pandoc conversion additionally changes line wrapping; only its TeX token sequence after inverse repair is equal.'}

tcl_map_path=TCL/'TCL2_REVERSIBLE_DISPLAY_MAP.json'
tcl_map=json.loads(tcl_map_path.read_bytes())
tcl_before_path,tcl_after_path=TCL/'before_49_TP.tex',TCL/'after_49_TP.tex'
tcl_before,tcl_after=tcl_before_path.read_bytes(),tcl_after_path.read_bytes()
assert sha(tcl_before)==tcl_map['before_sha256']
assert sha(tcl_after)==tcl_map['after_sha256']
old_fragment,new_fragment=[tcl_map[k].encode('utf-8') for k in ['old_fragment','new_fragment']]
fragment_replay=exact_replay(tcl_before,tcl_after,[(old_fragment,new_fragment)])
environment_pairs=[(br'\begin{split}',br'\begin{aligned}'),(br'\end{split}',br'\end{aligned}')]
fragment_tokens=exact_replay(old_fragment,new_fragment,environment_pairs)
old_formula=old_fragment[old_fragment.index(b'\n')+1:old_fragment.rindex(br' \end{')]
new_formula=new_fragment[new_fragment.index(b'\n')+1:new_fragment.rindex(br' \end{')]
assert old_formula==new_formula
old_interior=old_fragment[old_fragment.index(br'\begin{split}')+len(br'\begin{split}'):old_fragment.index(br'\end{split}')]
new_interior=new_fragment[new_fragment.index(br'\begin{aligned}')+len(br'\begin{aligned}'):new_fragment.index(br'\end{aligned}')]
assert old_interior==new_interior
environment_whole_file_spans=[]
for old,new in environment_pairs:
    spans={}
    for side,data,fragment,token in [('before',tcl_before,old_fragment,old),('after',tcl_after,new_fragment,new)]:
        start=data.index(fragment)+fragment.index(token)
        spans[side]={'start_byte_0':start,'end_byte_0_exclusive':start+len(token),
                     'start_line_1':data[:start].count(b'\n')+1,'literal_utf8':token.decode('utf-8')}
    environment_whole_file_spans.append(spans)
tcl_current=[]
for entry in tcl_map['active_copies']:
    path=Path(entry['root'])/entry['active_path']
    current=path.read_bytes()
    active_reads.append((path,current))
    assert current==tcl_after
    label='stage' if '/work/' in path.as_posix() else 'delivery'
    tcl_current.append({'location':label,'active':pin(path,current),
        'snapshot':save('active_snapshots/'+label+'_49_TP.tex',current),
        'equals_retained_after_bytes':True,'repaired_fragment':span(current,new_fragment)})

unchanged=[]
for path,data in active_reads:
    at_end=path.read_bytes()
    unchanged.append({'path':str(path),'start_sha256':sha(data),'end_sha256':sha(at_end),
                      'unchanged_during_audit':data==at_end})
assert all(x['unchanged_during_audit'] for x in unchanged), 'Concurrent active file change; rerun snapshot audit'

receipt={'audit':'Independent BF12 exponent and TCL.2 display conversion recovery',
    'started_utc':START,'finished_utc':datetime.now(timezone.utc).isoformat(),
    'status':'PASS for the narrowly scoped source conversion and display transformations',
    'scope':'Two BF12 expression restorations and TCL.2 split-to-aligned display wrapper only. No mathematical proof revision is proposed or made. No PDF, compiler-output, or other-conversion-repair certification is made.',
    'audit_script':pin(Path(__file__)),
    'evidence_records':{'BF12_applied_record':pin(applied_path),'TCL2_display_map':pin(tcl_map_path),
                        'later_converter_application':pin(final_map_path)},
    'BF12':{'original_source_pin_checks':source_pins,'source_mathematical_witnesses':source_witnesses,
            'corrected_markdown':pin(corrected_path),'exact_markdown_replay':markdown_replay,
            'retained_and_current_active_checks':retained_active_checks,
            'stage_delivery_ledger_bytes_equal_at_read':True,'independent_parser_reproduction':parser_check,
            'correction_chain_into_current_active':correction_chain,
            'mathematical_scope':'Both corrected exponents are the source degree [K:Q], with the original N(2R), q, >1, and multiplication placement preserved. The source explicitly identifies d=[K:\\mathbb Q], N_K(2R)=2^d, and q=2^dq. This receipt checks fidelity to those source statements and exact edit closure; it does not re-prove or endorse every claim of the full ledger.'},
    'TCL2':{'before':pin(tcl_before_path,tcl_before),'after':pin(tcl_after_path,tcl_after),
            'whole_file_exact_fragment_replay':fragment_replay,
            'within_fragment_environment_token_replay':fragment_tokens,
            'whole_file_environment_token_spans':environment_whole_file_spans,
            'mathematical_formula_bytes_equal':True,'formula_bytes':len(old_formula),
            'formula_sha256':sha(old_formula),'formula_utf8':old_formula.decode('utf-8'),
            'entire_environment_interior_including_adjacent_whitespace_bytes_equal':True,
            'entire_environment_interior_bytes':len(old_interior),
            'entire_environment_interior_sha256':sha(old_interior),
            'active_copies':tcl_current,'visual_acceptance':'Not assessed; PDF rendering excluded from this audit.'},
    'concurrency':{'active_inputs_double_read':unchanged,
                   'qualification':'Pins bind the bytes observed between the reported audit timestamps. The parent must bind final compiler inputs and delivery to its final build after concurrent work settles.'}}
(OUT/'BF12_TCL2_INDEPENDENT_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':receipt['status'],'receipt':pin(OUT/'BF12_TCL2_INDEPENDENT_RECEIPT.json'),
                  'BF12_active_sha256':retained_active_checks[0]['current_active']['sha256'],
                  'BF12_active_equals_bf12_only_after':retained_active_checks[0]['current_active_equals_bf12_only_after'],
                  'TCL2_active_sha256':sha(tcl_after),'active_inputs_unchanged_during_audit':True}))
