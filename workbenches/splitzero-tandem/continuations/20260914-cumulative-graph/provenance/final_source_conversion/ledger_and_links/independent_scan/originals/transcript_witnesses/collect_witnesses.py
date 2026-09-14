"""Bounded, read-only transcript witness extraction; writes only beside this script."""
from pathlib import Path
import hashlib
import json

ROOT = Path(r'workspace:')
OUT = Path(__file__).resolve().parent
BASE = ROOT / 'work/backpropagation_20260913/cohort_staging'
LEDGERS = BASE / 'snapshots/transcript/ledger_publication/sources'
TURNS = BASE / 'snapshots/transcript/sources/turns'
PROBE = OUT.parent / 'PARSER_PROBE.json'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def rel(path):
    return path.relative_to(ROOT).as_posix()

def snippet(name, start, end):
    path = TURNS / name
    lines = path.read_text(encoding='utf-8-sig').splitlines()
    return {'path': rel(path), 'sha256': sha(path), 'start_line': start,
            'end_line': end, 'exact_lines': lines[start-1:end]}

specs = [
 ('formation',479,71,'A0961.md',[(591,594),(611,628)],
  'Exponent-boundary witness found. Transcript uses FNF^{-1}=q^{-1}N without literal parentheses around -1; ledger contains FNF^(−1)=q^(−1)N. No parenthesis removal is proposed by this receipt.'),
 ('formation',479,148,'A0961.md',[],
  'UNMATCHED in selected transcript A0961. Ledger explicitly attributes N z^j=z^{j+1} and U_a to Original Tau_Base (40), not to A0961. No external Tau_Base source was searched within this bounded task.'),
 ('formation',487,286,'A0961.md',[],
  'UNMATCHED in selected transcript A0961. The ledger labels this a concrete surviving derivation, and line 532 identifies GERM_GRADING_AND_THETA_LIFT.md as the complete new proof. No C_q appears in the selected transcript.'),
 ('formation',487,313,'A0961.md',[],
  'UNMATCHED in selected transcript A0961. C_q U_a C_q^(−1)=a^{ρ(1−1/q)}U_{a^{1/q}} is audit-authored continuation according to ledger lines 528–532; no transcript quotation is asserted.'),
 ('formation',530,340,'A0961.md',[],
  'UNMATCHED in selected transcript A0961. Repeated audit-authored C_q N C_q inverse relation; ledger line 532 supplies its separate proof-file provenance.'),
 ('formation',530,367,'A0961.md',[],
  'UNMATCHED in selected transcript A0961. Repeated audit-authored C_q U_a C_q inverse relation; ledger line 532 supplies its separate proof-file provenance.'),
 ('typed',241,41,'A1167.md',[(502,509)],
  'Exponent-boundary witness found. Transcript uses I_R=(e^{-R},e^R), then mathcal H_R=L^2(I_R,dx). Ledger uses H_R=L2((e^−R,e^R),dx); changing L2 to L^2 or H to mathcal H is a notation restoration beyond only fencing the two e exponents.'),
 ('late',137,227,'A2129.md',[(565,574)],
  'Exponent-boundary witness found with a literal notation discrepancy: transcript G_N\\preceq C_h^kG_N^\\Gamma has no ar superscript; ledger G_N^ar≤C_h^kG_N^Γ adds ar and uses ≤. This receipt does not authorize removing the ledger ar label or changing its relation sign.'),
 ('late',243,102,'A2330.md',[(188,204)],
  'Exponent-boundary witness found: H^{-1}=E_1 and H^0=E_1 in the chosen infinity frame. The source keeps the intrinsic kernel line factor immediately afterward.'),
 ('late',270,301,'A2368.md',[(79,86)],
  'Exponent-boundary witness found: source has mathbb H^0(X,mathcal K_{F,m})=F, mathbb H^1(...)=0, mathbb H^2(...)=E/F. Ledger abbreviates the symbol and its arguments.'),
 ('late',324,383,'A2444.md',[(538,547)],
  'Exponent-boundary witness found: source exact transport is Pi^{-*}G_N Pi^{-1}; ledger uses Unicode Π and minus signs with braces.'),
 ('late',376,181,'A2559.md',[(285,301)],
  'Exponent-boundary witness found: source complement is [B_N^0 xrightarrow{I} B_N^0] and explicitly contracts by the identity. Ledger abbreviates the displayed arrow label.'),
]

probe = json.loads(PROBE.read_text(encoding='utf-8-sig'))
unique = {}
for doc in probe['records']:
    for node in doc['selected_nodes']:
        if node['node_type'] == 'Superscript':
            for raw in node['raw_matches']:
                unique[(doc['slug'], raw['line'], raw['column'])] = raw
records = []
for slug,line,col,turn,ranges,note in specs:
    path = LEDGERS / f'{slug}.md'
    lines = path.read_text(encoding='utf-8-sig').splitlines()
    raw = unique[(slug,line,col)]
    assert lines[line-1] == raw['exact_raw_line']
    headings = [(i+1,s) for i,s in enumerate(lines[:line]) if s.startswith(('## ','### '))]
    heading_line,heading = headings[-1]
    records.append({'id':f'{slug}:{line}:{col}', 'ledger_path':rel(path),
                    'ledger_sha256':sha(path), 'ledger_line':line,
                    'raw_token':raw['exact_raw_token'], 'exact_ledger_line':lines[line-1],
                    'nearest_heading_line':heading_line,'nearest_heading':heading,
                    'selected_turn':rel(TURNS / turn), 'selected_turn_sha256':sha(TURNS / turn),
                    'status':'witness_found_with_notation_recorded' if ranges else 'unmatched_in_selected_transcript',
                    'witnesses':[snippet(turn,a,b) for a,b in ranges], 'finding':note})

searches = []
for turn, needles in [('A0961.md',['C_q','C_{q}','U_a','U_{a}','N z^j']),
                      ('A2129.md',['G_N^ar','G_N^{ar}',r'G_N^{\mathrm{ar}}'])]:
    path = TURNS / turn
    lines = path.read_text(encoding='utf-8-sig').splitlines()
    searches.append({'path':rel(path),'sha256':sha(path),'line_count':len(lines),
                     'literal_needles':{needle:[i+1 for i,s in enumerate(lines) if needle in s] for needle in needles}})

receipt = {'scope':'Read-only witness extraction from selected transcript turns and three ledger Markdown sources; all twelve ledger records were inspected in PARSER_PROBE.json. No active edits or PDF work.',
           'probe_path':rel(PROBE),'probe_sha256':sha(PROBE),
           'unique_flagged_superscript_occurrences':len(unique),
           'local_record_count':len(records),'records':records,'bounded_negative_searches':searches,
           'formation_subset_receipt':'formation_subset/FORMATION_TRANSCRIPT_WITNESSES.json supplies formation:133:128, formation:193:53, formation:377:39',
           'unmatched_ids':[r['id'] for r in records if r['status']=='unmatched_in_selected_transcript'],
           'notation_caution':'Transcript witnesses support the semantic exponent boundaries; preserve the exact ledger object labels, parentheses, constants, and relation symbols unless the parent separately records a source-restoration decision.'}
(OUT / 'LOCAL_WITNESSES.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
subset_path = OUT / 'formation_subset/FORMATION_TRANSCRIPT_WITNESSES.json'
subset = json.loads(subset_path.read_text(encoding='utf-8-sig'))
combined = records[:]
for record,col in zip(subset['records'],[128,53,39]):
    line = record['ledger']['first_line']
    combined.append({'id':f'formation:{line}:{col}',
                     'status':'witness_found_with_notation_recorded',
                     'detail':record,'detail_receipt_path':rel(subset_path),
                     'detail_receipt_sha256':sha(subset_path)})
assert len(combined) == len(unique) == 15
assert set(r['id'] for r in combined) == {f'{s}:{l}:{c}' for s,l,c in unique}
ledger_hashes = [{'path':doc['packaged_path'],'expected_sha256':doc['source_sha256'],
                  'observed_sha256':sha(ROOT / doc['packaged_path'])} for doc in probe['records']]
assert all(r['expected_sha256']==r['observed_sha256'] for r in ledger_hashes)
for record in records:
    assert sha(ROOT / record['selected_turn']) == record['selected_turn_sha256']
    for witness in record['witnesses']:
        lines = (ROOT / witness['path']).read_text(encoding='utf-8-sig').splitlines()
        assert lines[witness['start_line']-1:witness['end_line']] == witness['exact_lines']
for item in subset['original_files']:
    assert sha(Path(item['path'])) == item['sha256']
final_receipt = {
    'scope':receipt['scope'],
    'method':'One record per unique path/line/column false Superscript occurrence. Selected turn files derive from nearest finding headings/episode IDs; formation line 530 explicitly points back to BF22. A witness means exponent boundaries are supported, not that the condensed ledger string literally matches the transcript.',
    'provenance_path':rel(OUT.parent.parent / 'USER_INPUTS_VERBATIM.md'),
    'probe_path':rel(PROBE),'probe_sha256':sha(PROBE),
    'occurrences':15,'transcript_witness_found':10,'unmatched_in_selected_transcript':5,
    'records':sorted(combined,key=lambda r:r['id']),
    'explicit_unmatched_ids':receipt['unmatched_ids'],
    'bounded_negative_searches':searches,
    'ledger_hash_verification':ledger_hashes,
    'all_12_ledger_hashes_match_parser_probe':True,
    'transcript_hashes_and_snippets_rechecked':True,
    'local_receipt_path':rel(OUT/'LOCAL_WITNESSES.json'),
    'local_receipt_sha256':sha(OUT/'LOCAL_WITNESSES.json'),
    'formation_subset_receipt_path':rel(subset_path),
    'formation_subset_receipt_sha256':sha(subset_path),
    'notation_caution':receipt['notation_caution']
}
final_path = OUT / 'TRANSCRIPT_WITNESS_RECEIPT.json'
final_path.write_text(json.dumps(final_receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'receipt':rel(final_path),'sha256':sha(final_path),
                  'records':15,'matched':10,'unmatched':receipt['unmatched_ids']},ensure_ascii=False))
