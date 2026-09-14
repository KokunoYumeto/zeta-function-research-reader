"""Independent read-only source/replay audit of the nineteen parser repairs.

Writes only the additive receipt beside this script. Original and proposed
files, raw Markdown sources and the earlier bound audit remain untouched.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re

HERE = Path(__file__).resolve().parent
WAVE = HERE.parent
BASE = WAVE.parents[1]
SCAN = WAVE / 'cohort_staging/ledger_exponent_correction/independent_scan'
STAGE = WAVE / 'cumulative_source_v1'
DELIVERY = BASE / 'output/Split_Zero_Recursive_Integration_2026-09-13/repository'
def sha(b): return hashlib.sha256(b).hexdigest()
def readj(p): return json.loads(p.read_text(encoding='utf-8'))
def pin(p): return {'path': str(p), 'sha256': sha(p.read_bytes()), 'bytes': p.stat().st_size}

# These nineteen results were read against the complete original source lines
# independently of the proposal-replay program. Parenthesized inverse powers,
# L2, the floor argument, all brackets, signs and both factors are retained.
accepted = {
 'SUP01': r'\(\operatorname{diag}(e^{-aL},e^{aL})\)',
 'SUP02': r'\(P_{a,b}(s)=((s-1/2-a)^2+b^2)((s-1/2+a)^2+b^2)\)',
 'SUP03': r'\(c_i:H_c^i\to H^i\)',
 'SUP04': r'\(FNF^{(-1)}=q^{(-1)}N\)',
 'SUP05': r'\(N z^j=z^{j+1}\)',
 'SUP06': r'\(C_qNC_q^{(-1)}=q^{(-1)}N\)',
 'SUP07': r'\(C_qU_aC_q^{(-1)}=a^{\rho(1-1/q)}U_{a^{1/q}}\)',
 'SUP08': r'\(C_qNC_q^{(-1)}=q^{(-1)}N\)',
 'SUP09': r'\(C_qU_aC_q^{(-1)}=a^{\rho(1-1/q)}U_{a^{1/q}}\)',
 'SUP10': r'\(H_R=\mathrm{L2}((e^{-R},e^R),dx)\)',
 'SUP11': r'\(G_N^{\mathrm{ar}}\le C_h^kG_N^\Gamma\)',
 'SUP12': r'\(H^{-1}=E_1,H^0=E_1\)',
 'SUP13': r'\(H^0=F,H^1=0,H^2=E/F\)',
 'SUP14': r'\(\Pi^{-*}G_N\Pi^{-1}\)',
 'SUP15': r'\(B_N^0\to B_N^0\)',
 'LINK01': r'\(q_k=[1+k(m-1)](k+1)^2\)',
 'LINK02': r'\(L_{h,k}=2\delta[1+k(m-1)](k+1)\operatorname{floor}((k+1)^2/4)\)',
 'inherited_paired_caret_exponents': r'\(I^G=p^{(-1)}(I)\)',
 'pr13_bracket_exponent_and_argument_as_link': r'\(f_j^{[N]}(x)\)',
}

ledger = readj(SCAN/'originals/CLASSIFICATION_AND_PROPOSALS.json')
local = readj(SCAN/'LINK_AND_LOCAL_PROPOSALS.json')
proposals = {}
for p in ledger['superscript_proposals'] + ledger['formula_link_proposals']:
    q = dict(id=p['id'], path=p['active_path'], old=p['standalone_old_tex_phrase'],
             new=p['proposed_inline_math'], source=BASE/p['packaged_path'],
             line=p['source_line'], phrase=p['exact_original_phrase'],
             source_sha256=p['source_sha256'])
    proposals[q['id']] = q
for p in local['confirmed_conversion_proposals']:
    q = dict(id=p['id'], path=p['active_relative_path'], old=p['old_tex'],
             new=p['proposed_tex'], source=Path(p['source']['path']),
             line=p['source_line'], phrase=p['source_exact_phrase'],
             source_sha256=p['source']['sha256'])
    proposals[q['id']] = q
assert set(proposals) == set(accepted)
source_checks=[]
for ident, p in proposals.items():
    raw = p['source'].read_bytes()
    assert sha(raw) == p['source_sha256'], ident
    source_line = raw.decode('utf-8-sig').splitlines()[p['line']-1]
    assert p['phrase'] in source_line, ident
    assert p['new'] == accepted[ident], ident
    source_checks.append({'id': ident, 'source': pin(p['source']), 'line': p['line'],
                          'exact_line': source_line, 'original_phrase': p['phrase'],
                          'accepted_tex': accepted[ident], 'pass': True})

replay = readj(SCAN/'PROPOSAL_REPLAY_RECEIPT.json')
assert replay['proposal_count'] == replay['edit_count'] == 19
file_checks=[]
seen=[]
for r in replay['files']:
    rel=r['path']
    before_path=SCAN/'reviewed_active_inputs'/rel
    after_path=SCAN/'proposed_scratch_outputs'/rel
    before_raw=before_path.read_bytes(); after_raw=after_path.read_bytes()
    assert sha(before_raw)==r['reviewed_input_sha256'], rel
    assert sha(after_raw)==r['scratch_output_sha256'], rel
    before=before_raw.decode('utf-8'); after=after_raw.decode('utf-8')
    edits=sorted(r['edits'], key=lambda e:e['old_start'])
    cursor=0; pieces=[]; unchanged=[]
    for e in edits:
        ident=e['id']; seen.append(ident); p=proposals[ident]
        assert p['path']==rel and e['old']==p['old'] and e['new']==accepted[ident]
        assert e['old_start']>=cursor and before[e['old_start']:e['old_end']]==e['old']
        prefix=before[cursor:e['old_start']]
        pieces += [prefix,e['new']]
        unchanged.append(sha(prefix.encode('utf-8')))
        cursor=e['old_end']
    pieces.append(before[cursor:]); unchanged.append(sha(before[cursor:].encode('utf-8')))
    assert ''.join(pieces).encode('utf-8')==after_raw, rel
    restored=after
    for e in sorted(edits,key=lambda e:e['new_start'],reverse=True):
        assert restored[e['new_start']:e['new_end']]==e['new']
        restored=restored[:e['new_start']]+e['old']+restored[e['new_end']:]
    assert restored.encode('utf-8')==before_raw, rel
    bindings=[]
    for root in (STAGE,DELIVERY):
        active=(root/rel).read_bytes()
        bindings.append({'root':str(root),'sha256':sha(active),'equals_reviewed_correction':active==after_raw})
    file_checks.append({'path':rel,'before':pin(before_path),'after':pin(after_path),
                        'edit_count':len(edits),'exact_forward_bytes':True,'exact_inverse_bytes':True,
                        'untouched_span_sha256':unchanged,'bindings':bindings})
assert len(seen)==19 and set(seen)==set(accepted)

# Existing history is checked in place; it is never refreshed with new hashes.
history=HERE/'history/pre_conversion_fidelity_20260913'
preserved=readj(history/'PRESERVED_FILES.json')
for r in preserved: assert sha((history/r['file']).read_bytes())==r['sha256'],r['file']
ledger_path=HERE/'CHANGE_USE_LEDGER.md'; readable=ledger_path.read_bytes()
assert sha(readable)=='878632304f272bc9de6b87471727c18b05939280c7e97072ecf52bf0531da0b2'
assert br'D-\rho' in readable
assert not [c for c in readable.decode('utf-8') if ord(c)<32 and c!='\n']
result={
 'status':'PASS: nineteen exact original-source conversion repairs and independent byte replay',
 'utc':datetime.now(timezone.utc).isoformat(),
 'scope':'Source-conversion fidelity only. Two earlier BF12 corrections and TCL.2 are separately bound; this receipt does not declare a PDF layout pass or a new proof of the historical mathematics.',
 'proposal_count':19,'file_count':len(file_checks),'source_checks':source_checks,'file_checks':file_checks,
 'all_active_stage_and_delivery_bytes_match':all(b['equals_reviewed_correction'] for r in file_checks for b in r['bindings']),
 'historical_audit_files_checked_unchanged':len(preserved),'readable_ledger':pin(ledger_path),
 'evidence':[pin(SCAN/'PROPOSAL_REPLAY_RECEIPT.json'),pin(SCAN/'originals/CLASSIFICATION_AND_PROPOSALS.json'),pin(SCAN/'LINK_AND_LOCAL_PROPOSALS.json')],
}
(HERE/'CONVERSION_NINETEEN_INDEPENDENT_CHECK.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['status','proposal_count','file_count','all_active_stage_and_delivery_bytes_match','historical_audit_files_checked_unchanged']},indent=2))
print('receipt_sha256',sha((HERE/'CONVERSION_NINETEEN_INDEPENDENT_CHECK.json').read_bytes()))
