from pathlib import Path
import hashlib,json,datetime
base=Path(r'workspace:')
repo=base/'output/Split_Zero_Recursive_Integration_2026-09-13/repository'
reader=base/'work/backpropagation_20260913/next_phase_graph_intake/reader_v2'
audit=reader/'dependency_audit'
specs=[
('AW',repo/'tex/AW_complete.tex','Exact relation-window spectral transport on the original tau complex','Complete AW source: constructs original source isometry, complete flag spectra and relative-spectrum bound invoked by ACM6–13, ISM12 and RMT7–15.'),
('SP',repo/'tex/tau_signed_projection_control.tex','Joint trace control on the original source and relation spaces','Complete currently propagated SP source: original inverse-metric projector density, overlap trace and exact trace-norm bounds used by ACM9–11 and RMT9–10a.'),
('EP',repo/'sources/current_cohorts/ta_c47/snapshots/TA_addendum/proofs/EP.tex','Exact comparison of inherited EW transport with AGT and AA','Complete EP1–36 source, including intended EP17–25 crossed-pair count and nonlinear transport. This is not the distinct EP.1 product-optimization source.'),
('HT',repo/'tex/cohorts/cf/30_HT.tex','The off-line counterfactual inside the original holonomy construction','Complete HT1–18 source: full quartet sum module, half-density and phase maps, rank-two recurrence, exact lower boundary energy and Laplacian residual used by HC1–14.'),
]
files=[]
for key,path,title,role in specs:
    raw=path.read_bytes()
    files.append(dict(key=key,path=str(path),sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw),title=title,role=role))
at=base/'work/rh_counterfactual_20260913/total_object/propagation_metric/derived/tex/modules/AT.tex'
review=at.parents[3]/'review/ROOT_INDEPENDENT_MATH_REVIEW.json'
raw=at.read_bytes();atsha=hashlib.sha256(raw).hexdigest()
assert atsha=='438fd058f4745056945a3a747eaeb63f2b36a0f146335ed72018acdb28b93727'
review_obj=json.loads(review.read_text(encoding='utf-8-sig'))
entry=next(e for e in review_obj['entries'] if e['target']=='tex/modules/AT.tex')
assert entry['new_sha256']==atsha and entry['whole_current_body_read'] and review_obj['status']=='accepted'
obj=dict(scope='Bounded direct dependency closure of ACM/HC/RMT/ISM on reader_v2. Read-only source audit; no reader or source edits.',created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),files=files,replace_existing=[dict(key='dep04',path=str(at),sha256=atsha,bytes=len(raw),title='Arithmetic determinant transport on the original tau complex',role='Complete accepted AT containing AT21a–e required verbatim by ACM and HC; replace older dep04 reading, retain historical original bytes.',old_sha256=entry['old_sha256'],review=str(review),review_sha256=hashlib.sha256(review.read_bytes()).hexdigest())],further_direct_dependencies=[dict(key='EW',path=str(repo/'tex/gamma_endpoint_window_bridge.tex'),sha256=hashlib.sha256((repo/'tex/gamma_endpoint_window_bridge.tex').read_bytes()).hexdigest(),reason='EP is a full comparison to EW.1–59; its expanded source and section-5 positivity calculation explicitly invokes EW.17, EW.25–28 and EW.35a–c. Include complete EW to retain this full-body comparison, rather than claiming the original compared source is present when only EP is present.')],already_present={'Gamma source':'dep07, including complete orthogonality and recurrence','actual arithmetic moments and lower envelope':'dep05, dep06, dep08 and dep09 (AU)','consecutive source products and lower bound':'dep10 (CJ)','theta Euler inverse and source unit':'AI and HCA','holonomy actual phase-source sandwich':'H_NOTE H39–H41; see DIRECT_CLOSURE_AUDIT.md','full quartet cyclic polynomial':'dep02, dep03 and added HT2 with nonzero leading nilpotent coefficient proof'},not_asserted=['Whole-programme transitive closure','A new mathematical acceptance of the attached source bodies','A new PDF compilation or visual inspection'])
for key,rel,title,reason in [
    ('GR','tex/actual_tau_gamma_review_complete.tex','Complete Gamma-reference lower bound and arithmetic determinant comparison','AW18 and AT22 explicitly invoke B^Gamma >= 4q log(delta k/(2 sqrt(5))). Existing dep07 proves orthogonality/recurrence, but not that quartet lower bound. This full body proves GR9–GR33 for every retained multiplicity and order, with its complete appended Gamma derivation G1–G28.'),
    ('TVB','tex/toda_cv_exact_bridge.tex','The original Toda identity and its exact quotient-volume bridge','EW24 explicitly invokes TVB32–34a for the consecutive radius/two-loss inequality over its arbitrary window. Include the complete original TVB body for that actual additional claim. A distinct earlier CV label is not substituted without its exact map.')
]:
    path=repo/rel;raw=path.read_bytes()
    obj['further_direct_dependencies'].append(dict(key=key,path=str(path),sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw),title=title,role=reason,reason=reason))
(audit/'DIRECT_CLOSURE_FILES.json').write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'receipt':str(audit/'DIRECT_CLOSURE_FILES.json'),'files':files,'AT':obj['replace_existing'][0]},indent=2))
