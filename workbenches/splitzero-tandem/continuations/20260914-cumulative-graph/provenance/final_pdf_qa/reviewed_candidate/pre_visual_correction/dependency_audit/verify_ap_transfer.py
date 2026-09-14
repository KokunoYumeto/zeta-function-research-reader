"""Verify the entire revised AP proof inside its pre-existing reader wrapper.

The two inherited body-level transforms are proved from old raw and old
prepared bytes, then applied literally to the revised raw body. This does
not discard formulas or compare only mathematical token summaries.
"""
import argparse,difflib,hashlib,json
from pathlib import Path

HERE=Path(__file__).resolve().parent
W=HERE.parents[2]
OLD=W/'work/cumulative_actual_tau_draft_inputs_20260913_v21'
RAW=OLD/'source_snapshot/sources/next_edition/analytic_pole_conversions_v2/build/analytic_pole/endpoint_analytic_pole_source.tex'
PREPARED=OLD/'proof_bodies/AP/actual_tau_analytic_pole_complete.tex'
REVISED=HERE.parent/'boundary/revised/sources/next_edition/analytic_pole_conversions_v2/build/analytic_pole/endpoint_analytic_pole_source.tex'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def text(p):return p.read_text(encoding='utf-8-sig')

def verify(assembly):
    raw=text(RAW); prepared=text(PREPARED); revised=text(REVISED)
    rawlines=raw.splitlines(keepends=True)
    start=prepared.index('\\subsubsection{Actual Taylor-unit gauge:')
    # Only the documented outer local-group closures follow the original body.
    suffix='\n\\endgroup\n\n\n\\endgroup\n'
    if not prepared.endswith(suffix):
        raise ValueError('Unexpected original AP wrapper suffix')
    oldbody=prepared[start:-len(suffix)]
    # Preserve the exact terminal newline convention used in the original body.
    if not oldbody.endswith('\n'):oldbody+='\n'
    oldbodylines=oldbody.splitlines(keepends=True)
    ops=difflib.SequenceMatcher(None,rawlines,oldbodylines,autojunk=False).get_opcodes()
    changes=[]
    for tag,a,b,c,d in ops:
        if tag=='equal':continue
        before=''.join(rawlines[a:b]); after=''.join(oldbodylines[c:d])
        if not before or revised.count(before)!=1:
            raise ValueError(('Original literal transform not uniquely found in revised AP',tag,a,b))
        changes.append({'old_line':a+1,'old':before,'new':after})
        revised=revised.replace(before,after,1)
    if len(changes)!=2:
        raise ValueError(('Expected two inherited transforms',len(changes)))
    target=Path(assembly)/'tex/actual_tau_analytic_pole_complete.tex'
    active=text(target)
    presentation_inverse=[]
    manifest=HERE.parent/'cohort_staging/typesetting_boundary/OVERLAY_PROPOSALS.json'
    if manifest.is_file():
        for row in json.loads(text(manifest))['records']:
            if Path(row['active_path']).resolve()==target.resolve():
                if sha(target)!=row['after']['sha256']:
                    raise ValueError('Active AP typography hash differs from recorded derivation')
                before=row['old_display'];after=row['new_display']
                if active.count(after)!=1:raise ValueError('AP presentation inverse is not unique')
                active=active.replace(after,before,1)
                expected=text(Path(row['before']['path']))
                if active!=expected:raise ValueError('Complete AP inverse differs from accepted wrapper')
                presentation_inverse.append({'old':before,'new':after,'before_sha256':row['before']['sha256'],'after_sha256':row['after']['sha256']})
    count=active.count(revised)
    result={'raw_original':{'path':str(RAW),'sha256':sha(RAW)},
            'prepared_original':{'path':str(PREPARED),'sha256':sha(PREPARED)},
            'revised_raw':{'path':str(REVISED),'sha256':sha(REVISED)},
            'active':{'path':str(target),'sha256':sha(target)},
            'inherited_literal_transforms':changes,
            'active_presentation_inverse':presentation_inverse,
            'complete_revised_body_occurrences':count,
            'pass':count==1}
    (HERE/'AP_COMPLETE_BODY_TRANSFER_CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    return result

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('assembly',type=Path);args=ap.parse_args()
    result=verify(args.assembly)
    print(json.dumps({'pass':result['pass'],'complete_revised_body_occurrences':result['complete_revised_body_occurrences'],'active':result['active']},indent=2))
    if not result['pass']:raise SystemExit(1)
