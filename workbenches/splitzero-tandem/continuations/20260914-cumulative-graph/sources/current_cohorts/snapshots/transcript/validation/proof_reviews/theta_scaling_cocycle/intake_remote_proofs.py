"""Copy accepted remote-owner proofs and their named source interfaces without changing bytes."""
from pathlib import Path
import hashlib,json

WORK=Path(__file__).resolve().parent
ROOT=WORK.parents[2]
OWNER=Path('F:/user/Documents/Papors/Chatnotes/Zeta-Function-Foundation/agents/zenodo_workspace_publication/integration_20260913_next/post_pr26_intake/parent_review')
OUT=ROOT/'output/tau_f1_transcript_audit_2026-09-13/dependencies/remote'
OUT.mkdir(parents=True,exist_ok=True)
specs=[
    (ROOT/'work/cumulative_next_edition_staging_20260913_v19/intake_originals/f1_scaling/ACTUAL_TAU_SCALING_AND_EXPONENTIAL_FLOW.md','f1_scaling_frobenius/ACTUAL_TAU_SCALING_AND_EXPONENTIAL_FLOW.md','209385837d3fbdc72b1f0d1164c9f6b261f312243f4427befe7148729f934029','requested accepted original, fully read; exact archived snapshot retained after owner updated its working copy'),
    (OWNER/'f1_scaling_frobenius/ACTUAL_TAU_SCALING_AND_EXPONENTIAL_FLOW.md','f1_scaling_frobenius/ACTUAL_TAU_SCALING_AND_EXPONENTIAL_FLOW_DOMAIN_CORRECTED.md','4e4cb66e3cbbff6379ae389ddaaad65045ac0ed380f17a87ac7c4241c45e6c08','owner revision explicitly corrects only the separate curve-power-map integer domain; delta verified'),
    (OWNER/'f1_twisted_dual/F1_REFLECTION_WEIGHT_TRANSPORT.md','f1_twisted_dual/F1_REFLECTION_WEIGHT_TRANSPORT.md','111f4c3ea74fa3985352d4a29a65826ee10c883c18de20230f54a7b9f15472f2','full proof read and checked'),
]
for name in ('INDEPENDENT_REVIEW.md','ROOT_ACCEPTANCE.md','check_reflection_transport.py','CHECK_NORMAL.json','CHECK_OPTIMIZED.json'):
    specs.append((OWNER/'f1_twisted_dual'/name,'f1_twisted_dual/'+name,None,'accepted supporting evidence; this intake does not rerun its checks'))
gauge_pins={
    'ACTUAL_TAYLOR_UNIT_FORMAL_GAUGE.md':'9ded2486160b76bf65f92d44b73cdd0c59a3ca7e5334f88682e10592d5a45b2f',
    'INDEPENDENT_REVIEW.md':'e32e978870e65ea375040762432a3cfe479068ebe6cfd800086a2d35d55da6d0',
    'ROOT_ACCEPTANCE.md':'ad39808a669eafba1e67793c91b4e320d9fc1426bf6194d83735227b052a0d1d',
    'check_unit_gauge.py':'8b475de68e1136e2ba8890bdf68c7b4ad7b4cc77a392d696003d6823b640d276',
    'CHECK_NORMAL.json':'c27e89d8082b3154ca7269da7d70882c7b00036e76a95aa65bb53b26382d5ebe',
    'CHECK_OPTIMIZED.json':'c27e89d8082b3154ca7269da7d70882c7b00036e76a95aa65bb53b26382d5ebe',
}
for name,pin in gauge_pins.items():
    specs.append((OWNER/'f1_unit_gauge'/name,'f1_unit_gauge/'+name,pin,'formal proof, full review and acceptance read; accepted check evidence copied without rerun'))
local_specs=[
    ('output/split_zero_rh_tandem_2026-09-12/sources/Tau_Base_Cohomology_2026-09-12/NOTE.md','Tau_Base_Cohomology_NOTE.md','d03e71ad18f187bd89880cb8ca6fc9c5d6f260b3de8e8e5702c27db97e7b63c3'),
    ('output/split_zero_rh_tandem_2026-09-12/tex/arithmetic_input.tex','arithmetic_input.tex','a50b0fb587b644c4ea94dba45b2b423d038f2bfbe7fef188543939ba850e58d2'),
    ('work/deligne_split_sidebar_20260913.tex','deligne_split_sidebar_20260913.tex','8601c882177ecbf64a374bded1641573f7cbba4d950dd8786e23d15b64307384'),
    ('work/deligne_exponential_determinant_extension_20260913.tex','deligne_exponential_determinant_extension_20260913.tex','4a6b6c237ca3cff29abceba6cb5f8285e080b080c5f923f0e09d6f130a30dfe8'),
    ('output/split_zero_rh_tandem_2026-09-12/sources/web_deligne_exponential_delivery/Tau_Deligne_Exponential_Comparison/RESEARCH_NOTE.md','Tau_Deligne_Exponential_RESEARCH_NOTE.md','c2246c9f6046347bbd246890db88b1676b1a53487d66583a13b5883528bc0402'),
    ('output/split_zero_rh_tandem_2026-09-12/tex/deligne_translation_bridge.tex','deligne_translation_bridge.tex','7dc6c73941a3ea30b141e7fb1110d6fb7b688af8a9c79a996acce31f9086611d'),
    ('output/split_zero_rh_tandem_2026-09-12/tex/deligne_primary_source_correction.tex','deligne_primary_source_correction.tex','b12bf0c1ff1175de1099075f0da66cf51996acc43b2acc5d0ed01523dc05c001'),
    ('output/split_zero_rh_tandem_2026-09-12/tex/split_zero_carriers.tex','split_zero_carriers.tex','49ed53151068f726e5e392a36d076c95e4e050e163c204d85fd3b179a4a25805'),
    ('output/split_zero_rh_tandem_2026-09-12/sources/endpoint_complete_closure/output/Deligne_Split_Cohomology/primary_source_evidence/DELIGNE_PRIMARY_REVIEW_20260913.md','DELIGNE_PRIMARY_REVIEW_20260913.md',None),
]
for source,dest,pin in local_specs:
    specs.append((ROOT/source,'source_interfaces/'+dest,pin,'named source interface copied in full; see review for actual reread scope'))
records=[]
for source,relative,pin,status in specs:
    data=source.read_bytes()
    digest=hashlib.sha256(data).hexdigest()
    if pin is not None and digest!=pin:
        raise RuntimeError(f'Pinned input changed: {source.name}; got {digest}, expected {pin}')
    dest=OUT/relative
    dest.parent.mkdir(parents=True,exist_ok=True)
    if dest.exists() and dest.read_bytes()!=data:
        raise RuntimeError(f'Refusing to replace a different retained dependency: {relative}')
    dest.write_bytes(data)
    if dest.read_bytes()!=data:
        raise RuntimeError('Byte comparison failed: '+relative)
    try:
        source_locator=source.relative_to(ROOT).as_posix()
    except ValueError:
        source_locator='remote-owner accepted parent_review/'+source.relative_to(OWNER).as_posix()
    records.append({'path':relative,'source':source_locator,'bytes':len(data),'sha256':digest,'pinned_input_verified':pin is not None,'byte_identical':True,'scope':status})
manifest={'status':'retained without source edits','files':records,
          'qualification':'The requested 209385 original requires an integer exponent for the separate curve power map in section 6. The owner corrected that exact domain in current revision 4e4cb6, also retained byte-for-byte. Theta dilation remains defined for every positive real parameter.',
          'unit_direction':'The raw one-packet residue identity is R_g(f,h)=S_h(f^dagger,epsilon h), epsilon=j_h(h/g)=upsilon^{-1}; upsilon=j_h(g/h) belongs to the specified inclusion coordinates.',
          'formal_gauge':'Accepted UG1-19 carries the actual direct unit by a proved coefficientwise formal localization/gauge quasi-isomorphism and retains the inverse unit in UG19. Analytic evaluation of its pole contraction at nonzero complex u is not established by the formal proof.',
          'review':'REMOTE_PROOF_CONNECTION_REVIEW.md',
          'publication':'No remote publication; copies are local dependency retention. Accepted supporting check records are preserved, not reported as newly executed.'}
(OUT/'REMOTE_INTAKE_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'copied_files':len(records),'bytes':sum(x['bytes'] for x in records),'all_pins_match':True,'all_byte_comparisons_match':True},indent=2))
