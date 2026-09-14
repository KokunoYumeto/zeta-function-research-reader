"""Record the completed local edition without changing any proof or PDF."""
from pathlib import Path
import datetime, hashlib, json, shutil

WORK=Path(__file__).resolve().parents[1]
REPO=WORK.parents[1]/'output/tau_split_zero_counterfactual_continuation_20260913'
validation=json.loads((REPO/'build/REPOSITORY_VALIDATION.json').read_text())
qa=json.loads((REPO/'build/visual_qa/FINAL_VISUAL_QA_RECEIPT.json').read_text())
pdf=REPO/'Tau_Split_Zero_Total_Counterfactual.pdf'
digest=hashlib.sha256(pdf.read_bytes()).hexdigest()
assert validation['passed'] and validation['pdf_sha256']==digest
assert qa['status']=='PASS' and qa['sha256']==digest
ts=datetime.datetime.now().astimezone().isoformat()
readme=(WORK/'total_object/README_EDITION.md').read_text(encoding='utf8')
readme=readme.replace('The18 added inputs','The22 added inputs')
readme=readme.replace('has224 pages at its current build',f"has{validation['pdf_pages']} pages in this sealed build")
readme=readme.replace('records31 proof input checks,261 labels,120 references',
                      'records35 proof input checks,272 labels,120 references')
readme=readme.replace('## Deligne and the recovered Weil II source',r'''## The attached certified finite contradiction

HCA.1–29, including19a,27a–c and29a, attaches the newly certified original Hankel forms to the same total object. The raw theta moment map is defined before the theta quotient; the reciprocal operator T_h=-(A_h-1/2)^(-2) acts on complete finite jets. Its globally convergent half-trace retains both critical and offcritical contributions and equals the original moment recurrence. Full polynomial primitives and divisor maps are proved.

The original H15 and shifted H15 are strictly positive. Exact rational endpoint comparisons give H15^(nu)>gamma_nu I in the original monomial frame, with gamma_0=(63/64)^2 6*10^(-107), gamma_1=(63/64)^2 7*10^(-111). Every offcritical separator of actual degree at most15 must have a compensating arithmetic tail greater than its negative pair contribution, with the explicit positive margins in HCA27a–c. The original negative separator has actual degree at least16; for a<=14 the cross-family comparison strengthens its nominal degree bound to at least17, retaining the possibility of a cancelled leading coefficient. This is a finite exclusion; positivity in every degree is not asserted.

Complete WBR, GF and TC proof bodies follow HCA in the manuscript. Their full calculation, source and review package is retained under companion_sources/theta_hankel. The exact attachment checker can be rerun from this repository with:

```
python total_object_sources/hankel_certificate_attachment_exact_check.py --input-dir companion_sources/theta_hankel/calculation --method-tex companion_sources/theta_hankel/originals/TC_original.tex
```

It checks1400 rational intervals,32 positive pivots and32 positive leading determinants, and the strict triangular-factor bounds. It does not rerun quadrature. The original integration and independent recurrence reviews are explicitly attributed and retained.

## Deligne and the recovered Weil II source''')
(REPO/'README.md').write_text(readme,encoding='utf8')
new=r'''## Sealed total-object edition and finite moment attachment

The final cumulative edition has248 pages,35 complete input modules,272 labels and120 references. PDF SHA8e13cfb73d11ba00ebf5ba02dfc97b510776c05d0936ebc9aff6d80db2aaac52. The three-pass XeLaTeX build and repository validation passed. Final visual receipt has the same hash;224- and247-page intermediate checks are scoped to their own versions. Root also inspected the title, full residue-boundary page and boxed derivations. Frozen109-page baseline and its archive remain unchanged.

New additive HCA source certified_hankel_attachment.tex SHA54465ACF93BBD3BB13F4670C258FBCAED7AFAB4D92DE0DFBA899617DD232DB3F constructs the exact raw-source moment observation and rational recurrence, complete reciprocal jet operator, original-unit polynomial boundary, natural divisor maps, compressed half-trace and global convergent trace. Its offpart is exactly existingT_UQ; allcritical contributions remain. It includes the full finite separator restriction with exact tail and degree, plus shifted family and same-polynomial comparisons.

The exact endpoint checker was rerun by root on the original inputs and in the portable copied repository. Both pass1400 ordered dyadic intervals,32 positive pivots,32 positive leading determinants and the offdiagonal row/column sums of L-I strictly below1/64. This proves new original-frame lower bounds gamma_0=(63/64)^2 6*10^-107 and gamma_1=(63/64)^2 7*10^-111. No quadrature was rerun here; the original validated integrations and independent integer recurrence are attributed to the coordinating calculation and retained whole.

For an actual offcritical reciprocal pair beta,barbeta, Q_nu(P_nu,N)=-2m+T_nu,N with |T_nu,N|<=C_nu^2 T_nu4^-N. If actual degree<=15, the certified positive form proves T_nu,N>2m plus the exact coefficient margin; HCA27a records the explicit beta-evaluation lower bound. HCA27b retains the shifted form on the identical original polynomial. HCA27c uses C_1^2=C_0^2/|beta| and T_1<=|beta|T_0/2 to obtain U_1<=U_0/2 and a stronger lower bound on the original unshifted tail. HCA29 proves actual negative separator degree>=16. When a=#A<=14, HCA29a proves N_*>=16-a and nominal degreeN_*+a+1>=17; actual degree may be16 when the leading affine coefficient vanishes. Its stated boundary case is retained. All these claims have full proofs, not assumed infinite positivity.

The original WBR/GF/TC proof bodies and full companion certificate/source closure are incorporated. The exact global-Q/offpart attachment is owned here and does not replace the one-object construction. The user-requested Deligne comparison, full source recovery and Weil II LaTeX locator are complete local deliverables. No exhaustive contradiction or actual offcritical zero is established; the research goal remains unfinished and its usageLimited status was not changed.

An internal progress send_message_to_thread tool call was terminated after yielding repeatedly without completion. Its delivery was not confirmed and it was not repeated. Earlier successful coordinator messages remain recorded. This has no effect on the local proof or artifact validation. No remote publication or Lean execution occurred.
'''
assert validation['pdf_pages']==248 and digest=='8e13cfb73d11ba00ebf5ba02dfc97b510776c05d0936ebc9aff6d80db2aaac52'
with (WORK/'CURRENT_CALCULATION.md').open('a',encoding='utf8') as f:f.write('\n'+new)
with (WORK/'WORK_LOG.md').open('a',encoding='utf8') as f:f.write(f'\n## {ts} — Final local edition sealed\n\n'+new)
for name in ['CURRENT_CALCULATION.md','WORK_LOG.md','USER_INPUTS_VERBATIM.md','CORRECTED_ACTIVE_GOAL.md']:
    shutil.copy2(WORK/name,REPO/'provenance'/name)
shutil.copy2(WORK/'shared_thread_audit/THIS_SESSION_USER_INPUTS_VERBATIM.md',
             REPO/'provenance/THIS_SESSION_USER_INPUTS_VERBATIM.md')
record={'recorded_at':ts,'pdf_sha256':digest,'pages':validation['pdf_pages'],
        'validation':'PASS','visual_qa':'PASS','original_interval_checker':'PASS',
        'portable_interval_checker':'PASS','proof_modules':35,'rh_endpoint_established':False,
        'goal_status_observed':'usageLimited; unchanged','publication':'none'}
(REPO/'provenance/TOTAL_OBJECT_EDITION.json').write_text(json.dumps(record,indent=2),encoding='utf8')
print(json.dumps(record,indent=2))
