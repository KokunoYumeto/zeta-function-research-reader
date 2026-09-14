from pathlib import Path
import datetime, json

ROOT=Path(__file__).resolve().parents[1]
SESSION=Path(r'local:user-profile\.codex\sessions\2026\09\13\rollout-2026-09-13T07-00-56-01a09923-cfae-7353-82d0-a47f6c90e839.jsonl')
records=[]
for line in SESSION.read_text(encoding='utf-8').splitlines():
    row=json.loads(line)
    p=row.get('payload',{})
    if row.get('type')=='response_item' and p.get('role')=='user':
        body='\n'.join(c.get('text','') for c in p.get('content',[]) if c.get('type') in ('input_text','text'))
        records.append((row.get('timestamp',''),body))
out=['# All user-channel inputs in this session, verbatim\n',
     'Internal coordinator envelopes, if present, are recorded as transport provenance and are not new human instructions.\n']
for i,(ts,body) in enumerate(records,1):
    out.append(f'\n## Record {i} — {ts}\n\n'+body+'\n')
(ROOT/'shared_thread_audit/THIS_SESSION_USER_INPUTS_VERBATIM.md').write_text(''.join(out),encoding='utf-8')
with (ROOT/'USER_INPUTS_VERBATIM.md').open('a',encoding='utf-8') as f:
    f.write('\nCurrent bounded session audit: '+str(len(records))+' records in shared_thread_audit/THIS_SESSION_USER_INPUTS_VERBATIM.md. Latest literal requests are retained there, including total-object construction, exhaustive contradiction logic, and Deligne-proof recollection.\n')
ts=datetime.datetime.now().astimezone().isoformat()
with (ROOT/'WORK_LOG.md').open('a',encoding='utf-8') as f:
    f.write('\n## '+ts+' — Total-object correction and construction\n\n'
      'The user repeatedly corrects the deliverable: explicitly assemble one total counterfactual object from every actual programme definition and exclusion, rather than another collection of restrictions. The active goal remains unfinished; get_goal reported usageLimited, and no goal status was changed. Durable workflow is corrected here without replacing the goal.\n\n'
      'Prior continuation2 proof inputs OCQ/DC, QT/VR, BT/BI/TW, FPK/LC/FKG and CA/AGT are complete and independently reviewed. The new cumulative PDF was not yet assembled. The frozen109-page repository is unchanged. The previous README replacement failed before either README or log mutation; no successful edit is claimed.\n\n'
      'New concrete root: for every monic p whose roots are off the critical line in the open strip, use the original Koszul complex V -> B directsum V -> B, maps (Theta,p(D)) and (p(D),-Theta). Its H1 is Q[p(D)] and its H2 is Q/p(D)Q; p(D) is NOT onto the original spaces. Directed maps are explicit. The actual source subspace B_off is the inverse image in B of the union of these torsion kernels. The single dg tensor algebra of [V -> B_off], together with its original two-leg tau realization and balanced Mellin arrow, will carry the complete source, full tensor, cyclic, conormal, norm, phase and comparison maps.\n\n'
      'Every possible offcritical zero maps to a nonzero full jet via the exact original Euler inverse, and conversely finite offcritical torsion detects a zero of g. This exhaustive map is part of the construction. Full coherent kernel K and tau diagonal remain attached and are not incorrectly used as RH detectors. Partial-divisor units are not assumed invertible; full-order packet charts are explicitly delimited. Divisor transport goes through full joint tensor algebras, because it need not preserve canonical sum-cyclic subspaces.\n\n'
      'The user also requests the exact Deligne contradiction mechanism recorded. The primary 1974 paper has been browsed at numdam, sections3.2–3.7 and7.1–7.3: cohomological pole exclusion, positivity preventing a nearer local pole, tensor amplification, and the final fixed-half-exponent error squeezed by product varieties. Exact exponents will be recorded with source locators. No assertion of RH proof/disproof follows from current progress.\n')
print(json.dumps({'user_channel_records':len(records),'recorded_at':ts}))
