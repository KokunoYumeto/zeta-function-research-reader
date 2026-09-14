from pathlib import Path
import hashlib,json,re

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
SOURCE=ROOT/'output/tau_f1_transcript_audit_2026-09-13/sources/audit_segment_U0001_U0015.md'
raw=SOURCE.read_bytes();source_text=raw.decode('utf-8');lines=source_text.splitlines()
source_hash=hashlib.sha256(raw).hexdigest()
ns=json.loads((HERE/'ns_context/opening_context_audit.json').read_text(encoding='utf-8'))
local=json.loads((HERE/'audit_local.json').read_text(encoding='utf-8'))
pb=json.loads((HERE/'physical_bridge/AUDIT.json').read_text(encoding='utf-8'))
coverage=[]
for row in ns['coverage_nodes']:
    coverage.append(dict(locator=row['locator'],node_id=row['uuid'],chain=row['chain'],line_start=row['start_line'],line_end=row['end_line'],classification=row['coverage_class'],reader='early_ns_context'))
for row in local['coverage_nodes']:
    coverage.append(dict(locator=row['locator'],node_id=row['node_id'],chain=row['chain'],line_start=row['line_start'],line_end=row['line_end'],classification=row['coverage_class'],reader='audit_early_context'))
for row in pb['turns']:
    coverage.append(dict(locator=row['turn'],node_id=row['node_id'],chain=row['chain'],line_start=row['first_line'],line_end=row['last_line'],classification=row['classification']+': '+row['description'],reader='early_physical_bridge'))
for row in coverage:
    header=lines[row['line_start']-1]
    if not(header.startswith('## '+row['locator']+' | '+row['node_id']+' | ') and header.endswith('chain '+str(row['chain']))):
        raise ValueError(('locator mismatch',row,header))
coverage.sort(key=lambda x:x['line_start'])
if len(coverage)!=51 or coverage[0]['line_start']!=1 or coverage[-1]['line_end']!=len(lines):
    raise ValueError('Incomplete coverage')
for a,b in zip(coverage,coverage[1:]):
    if a['line_end']+1!=b['line_start']: raise ValueError('Coverage gap')
for row in coverage:
    if row['locator'] in ['U0007','A0408','A0437']:
        row['segment_boundary_resolution']='A0473 subsequently supplies the signed calculation; U0010 explicitly withdraws the negative detour. No unresolved boundary inference remains.'

pb_sections={}
pbmd=(HERE/'physical_bridge/AUDIT.md').read_text(encoding='utf-8')
for m in re.finditer(r'^### (PB\d+) — ([^\n]+)\n(.*?)(?=^### PB\d+|\Z)',pbmd,re.M|re.S):
    pb_sections[m[1]]=m[3].strip()
for issue in pb['issues']:
    issue['full_passage_audit_markdown']=pb_sections.get(issue['id'],'See physical_bridge/AUDIT.md')
    issue['node_locators']=[dict(locator=r['locator'],node_id=r['node_id'],chain=r['chain']) for r in coverage if r['locator'] in issue['turns']]

for issue in ns['passages']:
    if issue['short_exact_quote'] not in source_text: raise ValueError(('NS quote not in source',issue['id']))

provenance=dict(current_source_sha256=source_hash,prior_read_source_sha256='2dc59dcf167759e7198afc474d356285d293a1e7d187a3329f7ce9f7a349ecc5',
    correction='The parent extractor disabled Windows newline translation. Exact message bodies and UUIDs are unchanged. The former source had doubled CR/LF around nine existing CR characters in U0015; the delivered source uses faithful LF extraction, 4074 lines. Full read coverage is unchanged; current headers were revalidated against every node ID and chain position.',
    current_line_system='splitlines/LF at delivered source; rg header locators agree',
    historical_powershell_read_range_physical=[2819,4083],current_physical_range=[2819,4074])

manifest=dict(title='Complete early-context segment coverage U0001–U0015',source=SOURCE.relative_to(ROOT).as_posix(),provenance=provenance,
    counts=dict(nodes=51,user_turns=15,assistant_turns=36,passage_entries=34,source_lines=len(lines)),
    full_collective_read=True,individual_reader_ranges=[dict(reader='early_ns_context',range=[1,623]),dict(reader='audit_early_context',range=[624,2818]),dict(reader='early_physical_bridge',range=[2819,4074])],
    coverage=coverage,
    central_scope='The early segment contains mathematical and physical antecedents, not the later definitions of A_tau or K_tau. Continue the accepted original tau construction. No early obstruction reaches that whole program.',
    segment_boundary_resolution='U0007/A0408/A0437 were boundary-pending only in the first worker range. A0473 gives the negative branch calculation, and U0010 withdraws it as a route.',
    passage_ledgers=dict(opening=ns['passages'],central=local['passages'],physical=pb['issues']),
    complete_calculation_files=['NS_CUTOFF_THETA_SCALING.md','NS_CUTOFF_THETA_SCALING.tex','ns_context/opening_context_audit.md','physical_bridge/CALCULATIONS.md','physical_bridge/VISCOSITY_MAP.md'],
    independent_review='physical_bridge/PARENT_SCALING_REVIEW.md',
    limitations=['Full retained transcript text was read collectively; individual readers are recorded.','Every externally linked historical sandbox notebook was not acquired by this bounded lane. Scope findings concern the retained response unless a source was separately read.','The complete primary Tau_Base_Cohomology NOTE.md was read by this lane and the scaling reviewer. Its existing adjoint/residue results remain inherited source inputs, not newly claimed global positivity.','Final integration and verified PDF belong to the parent task; no remote write, shared-master edit or Lean invocation occurred.'])
(HERE/'audit.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(HERE/'read_coverage.json').write_text(json.dumps({k:manifest[k] for k in ['source','provenance','counts','full_collective_read','individual_reader_ranges','coverage']},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

out=['# Complete early-context audit: U0001–U0015','',
'Every retained turn in this segment is covered: **51 nodes, comprising 15 user turns and 36 assistant turns**, across delivered source lines **1–4074**. The full read was collective, divided into three disjoint contiguous ranges. Exact node IDs and chain positions were checked again against the delivered source.','',
f'Current source SHA256: `{source_hash}`. The former read-source SHA256 was `2dc59dcf167759e7198afc474d356285d293a1e7d187a3329f7ce9f7a349ecc5`; the parent corrected Windows newline translation without changing message text or UUIDs. The physical reader originally read PowerShell logical lines 2819–4083, covering all delivered LF lines 2819–4074.','',
'## Findings that matter for the current tau continuation','',
'1. **The negative detour was expressly withdrawn.** A0473 completes the negative polynomial-branch calculation requested near U0007/U0008; U0010 asks to omit it and use the released fluid proof. Its unconstructed finite-energy extension is not an active redo target.','2. **The exact arithmetic sign was repaired, not left unresolved.** A0618 gives the source scalar `sum_v W_v(g*g*)`, its nonpositive RH direction, its original factor `1/2`, its actual local-factor unitary, and `Q_previous = -sum_v W_v`. The previous finite positive values were never positive witnesses for the source scalar.','3. **The actual cutoff map had an unfinished action comparison.** A0618 proves admissibility for `(D_r^2-1/4)(chi a_u)` but stops before proving its arithmetic action or class. The completed supplementary appendix below now provides the original theta map, full nilpotent jets, right-adjoint residue evaluation and exact scaling behavior.','4. **Pure transported dilation has a precisely scoped obstruction.** It leaves the entire test autocorrelation unchanged, hence leaves every original prime and archimedean contribution unchanged. This does not describe the full actual NS evolution, which has changing profiles, interactions and cutoffs. Its time-dependent transport creates an explicitly computed additional force.','5. **The finite heat model and numerical packet search have limited scope.** A0598 labels its five-state example as auxiliary and its 18-packet arithmetic search as uncertified. Neither closes the original analytic calculation or rejects its remaining directions.','6. **A0706 materially repairs the earlier physical substitution.** A0656 gives exact modular scattering but does not complete the requested NS/horizon chain. A0706 subsequently supplies several explicit maps. The remaining physical endpoint and full arithmetic-kernel realization gaps do not obstruct the later A_tau/K_tau construction.','',
'The late accepted program remains `A_tau = RΓ(P,-)`, its separate `res_sigma`, `K_tau`, and the actual theta quotient with all support labels. None of the early finite-family, compact-error, physical-clock or endpoint arguments proves failure of that entire program.','',
'## Completed calculation supplied for integration','',
'[Full proof in Markdown](NS_CUTOFF_THETA_SCALING.md) and [editable LaTeX fragment](NS_CUTOFF_THETA_SCALING.tex) give the exact map from the A0618 test to the original theta complex. The proof includes the factor `1/2` between early Ephi and Theta, all cutoff derivative terms, unchanged physical viscosity, the unequal actions on the two theta legs, every actual-zero nilpotent jet, the K_tau residue evaluation, unchanged autocorrelation, and the complete force produced by a varying scale.','',
'The [independent review](physical_bridge/PARENT_SCALING_REVIEW.md) read the complete proof and complete Tau Base source. It found no algebraic correction. Its two notation/scope clarifications were applied. The integration owner separately read and checked the proof.','',
'Additional bounded contextual calculations are retained in [the opening audit](ns_context/opening_context_audit.md), [the physical calculations](physical_bridge/CALCULATIONS.md), and [the viscosity/clock map](physical_bridge/VISCOSITY_MAP.md). These remain subordinate to the late tau construction.','',
'## Passage-by-passage ledgers','',
'- [Opening U0001–U0007 ledger](ns_context/opening_context_audit.md): 28 nodes, 8 passage entries, all lines 1–623. Its boundary-pending strain exchange is resolved by A0473 and U0010 as stated above.','- [Central U0008–U0012 ledger](AUDIT_LOCAL.md): 15 nodes, 12 passage entries, all lines 624–2818. Every quotation was checked against the exact retained node.','- [Physical U0013–U0015 ledger](physical_bridge/AUDIT.md): 8 nodes, 14 passage entries, all delivered lines 2819–4074.','',
'The complete structured union is [audit.json](audit.json); [read_coverage.json](read_coverage.json) records provenance and all node classifications. Historical source pins inside the worker files remain as read receipts; the current source hash above controls delivered-source lookup.','',
'## Complete coverage table','',
'| Turn | Exact node | Chain | Lines | Classification |','|---|---|---:|---:|---|']
for r in coverage:
    status=r['classification']
    if 'segment_boundary_resolution' in r: status+='; answered by A0473, then route withdrawn by U0010'
    out.append(f'| {r["locator"]} | `{r["node_id"]}` | {r["chain"]} | {r["line_start"]}–{r["line_end"]} | {status} |')
out+=['','## Acquisition and audit limits','',
'The source acquisition itself belongs to the parent task. This lane read every assigned retained user/assistant text, including displays and original order; it did not silently substitute a latest ZIP. Historical linked sandbox notebooks and external articles were not all independently acquired here. When an early response reports proofs inside those packages, the ledger preserves that distinction. Newly completed proofs are identified separately. No motive judgement, remote publication, shared-master edit or Lean run occurred.']
(HERE/'AUDIT.md').write_text('\n'.join(out)+'\n',encoding='utf-8')

pins=[]
for p in sorted(HERE.rglob('*')):
    if p.is_file() and p.name not in ['MANIFEST.json'] and '__pycache__' not in str(p):
        pins.append(dict(path=p.relative_to(HERE).as_posix(),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
(HERE/'MANIFEST.json').write_text(json.dumps(dict(source_sha256=source_hash,files=pins),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(nodes=len(coverage),passages=34,current_source_lines=len(lines),source_sha256=source_hash,all_node_headers_verified=True,coverage_gap_count=0),indent=2))
