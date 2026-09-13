from pathlib import Path
import hashlib,json,datetime,shutil,re
from pypdf import PdfReader
W=Path(__file__).resolve().parent;BASE=W.parent
R=BASE/'output/split_zero_rh_tandem_2026-09-12'
SRC=R/'sources/web_relation_moment_delivery/Tau_Relation_Moment_Control'
BUILD=W/'relation_moment_comparison_build_20260913'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,data):
 p=W/name;p.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8');return p
def row(p,role):return {'workspace_relative':p.relative_to(BASE).as_posix(),'role':role,'bytes':p.stat().st_size,'sha256':sha(p)}
source_manifest=json.loads((SRC/'MANIFEST.sha256.json').read_text())
for n,d in source_manifest.items():
 p=SRC/n
 if sha(p)!=d['sha256'] or p.stat().st_size!=d['bytes']:raise RuntimeError('source changed '+n)
normal=json.loads((W/'relation_moment_comparison_normal_20260913.json').read_text());optimized=json.loads((W/'relation_moment_comparison_optimized_20260913.json').read_text())
if not(normal['passed'] and optimized['passed'] and normal['methods']==optimized['methods']==10):raise RuntimeError('test scope')
for key in ['names','failures','errors','source_checker_sha256','scope']:
 if normal[key]!=optimized[key]:raise RuntimeError('mode mismatch')
for mode in ['normal','optimized']:
 log=(BUILD/('check-'+mode+'-positive.stderr.log')).read_text()
 if 'Ran 10 tests' not in log or not log.rstrip().endswith('OK'):raise RuntimeError('positive log')
 for case,msg in [('action-order','original G_i is required'),('rank-transfer','positive comparator may increase rank')]:
  if msg not in (BUILD/('check-'+mode+'-'+case+'.stderr.log')).read_text():raise RuntimeError('negative log')
execution=save('relation_moment_comparison_execution_20260913.json',{
 'schema':'relation-moment-final-execution-v1','methods_per_mode':10,'mutants_per_mode':2,
 'normal_optimization':normal['optimization'],'optimized_optimization':optimized['optimization'],
 'normal_optimized_mathematical_payload_equal':True,
 'checks_execution_evidence':'finish_relation_moment_checks_build_20260913.py actual tool execution chunk733e23: all six check jobs passed, then PDF layout check stopped on Underfull hbox; checks were not rerun for subsequent layout-only edits.',
 'build_repair_evidence':'Actual build-only commands chunks b77b72 and70a258 returned build0,warnings[],render0; final one applies explicit scalar-gap domain wording.',
 'checker_sha256':sha(W/'check_relation_moment_comparison_20260913.py'),
 'original_checker_sha256':sha(SRC/'check_relation_moments.py'),
 'raw_logs':[row(p,'actual_execution_log') for p in sorted(BUILD.glob('check-*.log'))],
 'tex_sha256':sha(W/'relation_moment_comparison_proof_20260913.tex'),
 'pdf_sha256':sha(BUILD/'relation_moment_comparison_proof_20260913.pdf')})
pdf=BUILD/'relation_moment_comparison_proof_20260913.pdf';pages=PdfReader(pdf).pages
if len(pages)!=8:raise RuntimeError('page count changed')
log=(BUILD/'relation_moment_comparison_proof_20260913.log').read_text(errors='replace')
bad=[x for x in log.splitlines() if any(t in x for t in ['Overfull','Underfull','Missing character','undefined','LaTeX Warning','pdfTeX warning'])]
if bad:raise RuntimeError(bad)
qa=save('relation_moment_comparison_visual_20260913.json',{'schema':'actual-pdf-visual-review-v1','pages':8,'all_pages_actually_viewed':True,'terminal_pages_4_through_8_viewed_after_final_gap_domain_edit':True,'pages_1_through_3_unchanged_by_that_edit':True,'resolution_dpi':100,'pdf_sha256':sha(pdf),'tex_sha256':sha(W/'relation_moment_comparison_proof_20260913.tex'),'tex_warnings':bad,'findings':'All eight pages readable; no clipping, overlap, broken symbols, or displaced equation tags. Final page retains source provenance.','images':[row(p,'actual_reviewed_page_image') for p in sorted((BUILD/'qa').glob('page-*.png'))]})
corrections=save('relation_moment_source_corrections_20260913.json',{'schema':'relation-moment-source-corrections-v1','raw_sources_unchanged':True,'source_note_sha256':sha(SRC/'NOTE.tex'),'source_markdown_sha256':sha(SRC/'RESEARCH_NOTE.md'),'corrections':[
 {'locator':'NOTE.tex:499 / RESEARCH_NOTE.md:330','original':'the volume is zero','corrected':'Vi/Vj=1, Vi=Vj>0, and log(Vi/Vj)=0','proof':'RM.1-4'},
 {'locator':'NOTE.tex section8 equations26-28','original_scope':'i<=j inherited from section3','corrected_scope':'i<j and r=j-i>=1 for window minimum/powers; operator maps retain i=j','proof':'RM.3-4 and section5 final paragraph'},
 {'locator':'NOTE.tex section5 equality paragraph','original':'integrand strictly positive except at x=a,b','corrected':'complete remainder strictly positive away from the two nodes; bare integral remains positive','proof':'RM.12-16'},
 {'locator':'NOTE.tex section8 beforeequation30','original':'positive lower budget','corrected':'positive logarithmic budget2q log(D_h k)>0 means D_h k>1, implyingt1>0; the inequality alsoholds wheneveractualt1>0','proof':'complete independent review section7'}],
 'unproved_source_small_o_example':'Preserved as raw source motivation; no arithmetic upper estimate or conditional replacement is added to the cumulative claimed results.'})
attribution=save('relation_moment_primary_attribution_20260913.json',{'schema':'primary-literature-attribution-v1','date':'2026-09-13','publisher_url':'https://www.tandfonline.com/doi/abs/10.1080/03081088408817634','publisher_direct_fetch':'403; search-indexed publisher abstract inspected','author_bibliography':'https://www.math.uwaterloo.ca/~hwolkowi/henry/reports/ABSTRACTS.html','author_hosted_article':'https://www.math.uwaterloo.ca/~hwolkowi/henry/reports/PAPER17.pdf','actual_access':'Author bibliography entry and author-hosted19-page article opened; abstract/introduction and retrieved section3 passages identify best bounds for dimension, trace,trace-square. No claim to read every page or inaccessible theorem number.','citation':'Grone, Johnson, Marques de Sa, Wolkowicz, Improving Hadamard\'s inequality, Linear and Multilinear Algebra16(1984),305-322,doi10.1080/03081088408817634','secondary_support':'https://dlmf.nist.gov/3.3 (official NIST interpolation page inspected)','new_proof':'RM.11-19 independently proves complete inequality and remainder; no full copyrighted article copied into public closure.'})
inputs=W/'relation_moment_inputs_20260913';inputs.mkdir(exist_ok=True)
for src,dest in [(W/'arithmetic_volume_upper_route_20260913.tex','Arithmetic_Volume_Upper_Route.tex'),(W/'arithmetic_volume_upper_inputs_20260913/Arithmetic_Endpoint_Bounds_NOTE.tex','Arithmetic_Endpoint_Bounds_NOTE.tex')]:
 target=inputs/dest
 if target.exists() and target.read_bytes()!=src.read_bytes():raise RuntimeError('dependency differs')
 if not target.exists():shutil.copyfile(src,target)
with (W/'relation_moment_intake_logbook_20260913.md').open('a',encoding='utf-8') as f:
 f.write('\n'+datetime.datetime.now().isoformat()+' Complete newNOTE/MD/checker/handoff/source metadata/build scripts read, all36 manifest entries and9patchpayloads verified. Incoming22-method suites normal/-O passed; cross-pairing mutants rejected both. Originalrestriction19 notrerun. NewRM.1-35proof complete, tennewmethods normal/-O passed, original-Gi omission and invalidranktransfer mutants rejected both. All8PDFpages inspected. Layout-only rebuilds fixed duplicateanchors/hashline andfinalq1gapwording withoutrepeatingtests. Fullindependentsource andsupplementreviews read. Comparator AU.1-14includingallAU.10-13 source read completely; exactB42+2degh=42+8m retained. Parentowns completePR25source/fullanalyticconsecutiveprerequisites. No newLean/globalR/main/Zenodomutation.\n')
allfiles=[]
for p in sorted(SRC.rglob('*')):
 if p.is_file():allfiles.append(row(p,'unchanged_original_delivery'))
names=['relation_moment_archive_receipt_20260913.json','relation_moment_replay_receipt_20260913.json','relation_moment_independent_review_20260913.md','relation_moment_comparison_independent_review_20260913.md','relation_moment_comparison_proof_20260913.tex','check_relation_moment_comparison_20260913.py','relation_moment_comparison_normal_20260913.json','relation_moment_comparison_optimized_20260913.json','relation_moment_comparison_execution_20260913.json','relation_moment_comparison_visual_20260913.json','relation_moment_source_corrections_20260913.json','relation_moment_primary_attribution_20260913.json','relation_moment_intake_logbook_20260913.md','intake_relation_moment_delivery_20260913.py','replay_relation_moment_20260913.py','finish_relation_moment_checks_build_20260913.py','seal_relation_moment_intake_20260913.py']
for n in names:allfiles.append(row(W/n,'intake_proof_or_actual_evidence'))
for folder in [W/'relation_moment_replay_20260913',inputs]:
 for p in sorted(folder.rglob('*')):
  if p.is_file():allfiles.append(row(p,'actual_replay_or_complete_math_dependency'))
for p in sorted(BUILD.rglob('*')):
 if p.is_file() and p.suffix in ['.pdf','.png','.log']:allfiles.append(row(p,'pdf_build_actual_evidence'))
manifest={'schema':'relation-moment-intake-final-v1','status':'complete-local-mathematics-source-intake','archive':json.loads((W/'relation_moment_archive_receipt_20260913.json').read_text())['archive_sha256'],'proof_labels':'RM.1-35','pdf_pages':8,'source_methods_each_mode':22,'source_mutants_each_mode':1,'supplement_methods_each_mode':10,'supplement_mutants_each_mode':2,'raw_original_unchanged':True,'full_original_note_read':True,'full_original_markdown_read':True,'full_written_independent_reviews_read':True,'inherited_restriction_methods_rerun':False,'new_lean':False,'arithmetic_quadrature':False,'root_owned_pr25_scope':'Root separately validates completefirst-degree/consecutive/normenvelope source anditsnonnegativecostcorrection. Thisintakedoesnotinfer thoseproofs fromthissourcecitation.','portable_jobs':[
 {'script':'sources/web_relation_moment_delivery/Tau_Relation_Moment_Control/check_relation_moments.py','modes':['normal','optimized'],'positive_args':['--json','{output}/relation-moments.json','--calibration','{output}/relation-moments-calibration.json'],'expected_methods':22,'negative_args':['--negative-control'],'negative_expected_exit':1},
 {'script':'work/check_relation_moment_comparison_20260913.py','modes':['normal','optimized'],'dependency_args':['--source-checker','{root}/sources/web_relation_moment_delivery/Tau_Relation_Moment_Control/check_relation_moments.py'],'positive_args':['--json','{output}/relation-moment-comparison.json'],'expected_methods':10,'negative_cases':[['--negative-control','action-order'],['--negative-control','rank-transfer']],'negative_expected_exit':1}],
 'required_existing_closures':['arithmetic_volume_upper_manifest_20260913.json','arithmetic_endpoint_intake_manifest_20260913.json','root-owned currentPR25complete sourceandcorrection'],
 'file_count':len(allfiles),'files':allfiles}
mp=save('relation_moment_intake_manifest_20260913.json',manifest)
print(json.dumps({'manifest_sha256':sha(mp),'files':len(allfiles),'proof_sha256':sha(W/'relation_moment_comparison_proof_20260913.tex'),'pdf_sha256':sha(pdf),'review_sha256':sha(W/'relation_moment_comparison_independent_review_20260913.md')}))
