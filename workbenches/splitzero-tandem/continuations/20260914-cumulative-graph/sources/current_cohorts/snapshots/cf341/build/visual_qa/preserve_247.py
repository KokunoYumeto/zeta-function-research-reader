from pathlib import Path
import json, hashlib, shutil
q=Path(__file__).resolve().parent
pdf=q.parents[1]/'Tau_Split_Zero_Total_Counterfactual.pdf'
expected='6aa8f6a5e9ea44c03a4e6544e5a8a5b5714f093a7d626fb07f2e10c1d4973543'
assert hashlib.sha256(pdf.read_bytes()).hexdigest()==expected
snapshot=q/'version_247'
snapshot.mkdir(exist_ok=True)
for p in list(q.iterdir()):
    if p.is_file() and (p.name.startswith(('page-', 'text-', 'contact-')) or p.name in ['layout_metrics.json','baseline_page_mapping.json','boxed_detail_index.json']):
        shutil.copy2(p,snapshot/p.name)
shutil.copy2(pdf,snapshot/pdf.name)
receipt={'status':'PARTIAL_VISUAL_REVIEW_SUPERSEDED_BY_PENDING_REVISION', 'sha256':expected, 'pages':247, 'all_pages_rendered_at_dpi':90, 'all_page_geometry_check':'PASS', 'new_or_changed_pages':[1,3]+list(range(225,248)), 'full_size_individual_pages_reviewed':[1,3]+list(range(225,241)), 'remaining_pages_at_pause':list(range(241,248)), 'visual_defects_in_reviewed_pages':[], 'reason_for_pause':'Parent is adding a proved HCA refinement; resume by exact page comparison against the revised PDF.'}
(snapshot/'PARTIAL_VISUAL_QA_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
