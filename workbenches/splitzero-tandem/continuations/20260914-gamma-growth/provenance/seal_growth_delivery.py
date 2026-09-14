"""Seal this completed mathematical cut; do not rebuild historical editions."""
from pathlib import Path
import datetime,hashlib,json,shutil,zipfile
work=Path(__file__).resolve().parent
outer=Path(r'C:\Users\[[user]]\Documents\math\output\Split_Zero_Mixed_Boundary_Continuation_2026-09-14')
out=outer/'21_GAMMA_GROWTH'
utc=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def record(p):return {'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)}

receiving=work/'receiving'
receipt=receiving/'FULL_RECEIVING_RECEIPT.json'
if not receipt.exists():raise SystemExit('Wait for completed actual receiving sources and receipt')
shutil.copytree(receiving,out/'current_receiving',dirs_exist_ok=True)
for p in work.glob('REVIEW*.md'):shutil.copy2(p,out/'provenance'/p.name)
eqreview=work/'equilibrium'/'review'/'INDEPENDENT_GEL_EIQ_REVIEW.md'
shutil.copy2(eqreview,out/'provenance'/eqreview.name)
shutil.copy2(work/'equilibrium'/'review'/'FINAL_REVIEW_RECEIPT.json',out/'provenance'/'FINAL_GEL_REVIEW_RECEIPT.json')
shutil.copy2(work/'CONTINUE_THE_PROGRAMME.md',out/'00_CONTINUE_THE_PROGRAMME.md')
shutil.copy2(work/'WORKFLOW_DRAFT.md',out/'CURRENT_RESEARCH_WORKFLOW_4000_CHARS.md')
for filename in ['build_growth_paper.py','seal_growth_delivery.py']:
    shutil.copy2(work/filename,out/'provenance'/filename)

readme='''# Growth of the complete original Gamma return

The current paper is `Gamma_Growth_and_Arithmetic_Return.pdf` (37 pages), with its editable cumulative source `Gamma_Growth_and_Arithmetic_Return.tex`. The continuation is `00_CONTINUE_THE_PROGRAMME.md`.

It prints the preceding full LET/PHT/HCT calculation and the complete new WGP/RWB/EIQ/GEL/WGR proofs. The original Gamma source, mass, four endpoint roles, primary multiplicities and actual quotient/kernel/boundary maps are retained. The exact finite bounds lq/64 <= W <= 6lq, the proved positive leading equilibrium integral, and the arithmetic limit Delta_Gamma/(kq) -> -C_Gamma/4 are proved in full. The leading remainder is o(lq); the finite q-scale Hankel calculation remains the next mathematical task. The original P product has the sharper WGP13 signed expansion through its constant-scale term.

`current_receiving` contains the actual complete NOTE/JSR successors, full new proof providers and reversible edits. `dependencies` contains the complete earlier source providers. `originals/growth` retains byte-exact new mathematical sources; `sources/growth` has only the recorded display reflows needed for the paper. All source transports and accepted mathematical reviews are included. The 4,000-character workflow is current.

Build this paper from this folder with `xelatex -interaction=nonstopmode -halt-on-error Gamma_Growth_and_Arithmetic_Return.tex`, twice. It uses standard amsmath/amsfonts, hyperref, fontspec and installed Cambria, Calibri and Consolas fonts. No Lean result is claimed. Floating-point exploration is kept explicitly separate in provenance; the mathematical signs and limits do not depend on those values.

Historical cuts18,19,20 remain unchanged in their original folders. The previous publication owner reports cuts18–20 published at DOI10.5281/zenodo.22754516. This folder is a new local successor; its publication is handed to the same owner separately.
'''
(out/'README.md').write_text(readme,encoding='utf-8')
crosswalk='''# New results and their original receivers

| Complete proof | Original object | Exact receiving site |
|---|---|---|
| WGP1–14 | Literal four D products, both endpoints | LET19/PHT20 and GEL17a,b |
| RWB1–12 | Original Gamma density and even/odd polynomial maps | HCT13 coefficients, original low moment |
| RWB13–27 | Whole positive W product | LET20–21, WRC5–7, WGR5–13 |
| EIQ1–33 | Square-root/log potential on the actual positive axis | GEL7–9, exact equilibrium logarithmic integral |
| GEL1–19 | Original Gamma Hankel determinants, full mass/Jacobian | LET19–20, WGR14–15 |
| WGR1–15 | Original quotient, kernel, boundary and arithmetic deficits | Current NOTE/JSR finite arithmetic and HC sites |

Every mathematical statement appears with its full proof in the TeX. This crosswalk locates it; it does not replace the definitions or proof. The evaluated W interval contains the interval using exact W, so no unproved finite tightening is claimed. The new analytic gain is its finite magnitude and proved leading coefficient on the original growing family.
'''
(out/'THEOREM_CROSSWALK.md').write_text(crosswalk,encoding='utf-8')

pdf=out/'Gamma_Growth_and_Arithmetic_Return.pdf'
assert sha(pdf)=='2b365ad5761a36c6e1d523fd22b28b27b1001443bc8bb2639c68c3a5156c71d4'
v1=json.loads((out/'qa'/'VISUAL_01_18.json').read_text())
v2=json.loads((out/'qa'/'VISUAL_19_37.json').read_text())
identity=json.loads((out/'qa'/'REFLOW_PAGE_IDENTITY.json').read_text())
assert all(f'page-{i:02}.png' in identity['same'] for i in range(19,38))
oldqa=out/'history'/'before_low_display_reflow'/'qa'
for i in range(19,38):assert (out/'qa'/f'page-{i:02}.png').read_bytes()==(oldqa/f'page-{i:02}.png').read_bytes()
proofpins=json.loads((out/'NEW_PROOF_SOURCE_PINS.json').read_text())
for pin in proofpins:
    assert sha(Path(pin['source']))==pin['sha256']
    assert sha(Path(pin['destination']))==pin['typeset_sha256']
reviews=[work/'REVIEW_PRODUCT.md',work/'REVIEW_RECURRENCE.md',work/'REVIEW_RECEIVER.md',eqreview]
validation={
 'utc':utc,'pdf':record(pdf),'pages':37,
 'mathematical_acceptance':'Root read all complete WGP/RWB/EIQ/GEL/WGR proofs; independent complete mathematical reviews accepted, with final literal repairs checked.',
 'reviews':[record(p) for p in reviews],
 'visual_acceptance':'PASS: all37 actual pages visually reviewed. Finalpages2–5 reinspected after low-display placement repair; allother33 rendered PNGs verified byte-identical to the actually inspected prior render. No pending defects.',
 'visual_receipts':[record(out/'qa'/'VISUAL_01_18.json'),record(out/'qa'/'VISUAL_19_37.json'),record(out/'qa'/'REFLOW_PAGE_IDENTITY.json')],
 'receiving':record(receipt),'proofs':proofpins,'lean':'No Lean/Lake/Elan execution in this cut',
 'scope':'W finite positive and exact leading limit; entire signed arithmetic transfer. No o(q) Hankel remainder or programme completion asserted.'}
(out/'BUILD_AND_PROOF_ACCEPTANCE.json').write_text(json.dumps(validation,indent=2),encoding='utf-8')

archive=out/'Gamma_Growth_Complete_Source.zip'
exclude_suffix={'.aux','.log','.fls','.out'}
files=[]
for p in sorted(out.rglob('*')):
    if not p.is_file():continue
    rel=p.relative_to(out)
    if rel.parts[0]=='qa':continue
    if rel.parts[:2]==('history','before_low_display_reflow'):continue
    if p==archive or p.name in ['DELIVERY_RECEIPT.json','SOURCE_ARCHIVE_MANIFEST.json']:continue
    if p.suffix in exclude_suffix:continue
    files.append(p)
members=[{'path':p.relative_to(out).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files]
(out/'SOURCE_ARCHIVE_MANIFEST.json').write_text(json.dumps(members,indent=2),encoding='utf-8')
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in files:z.write(p,p.relative_to(out).as_posix())
    z.write(out/'SOURCE_ARCHIVE_MANIFEST.json','SOURCE_ARCHIVE_MANIFEST.json')
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    for item in members:
        data=z.read(item['path']);assert hashlib.sha256(data).hexdigest()==item['sha256']
        assert data==(out/item['path']).read_bytes()
    count=len(z.infolist())
final={'utc':utc,'status':'Complete local mathematical cut, wider programme active','pdf':record(pdf),'pages':37,'archive':record(archive),'archive_members':count,'member_validation':'CRC and every complete uncompressed member exact-byte verified against stable source tree','acceptance':record(out/'BUILD_AND_PROOF_ACCEPTANCE.json'),'receiving':record(out/'current_receiving'/'FULL_RECEIVING_RECEIPT.json'),'prompt':record(out/'00_CONTINUE_THE_PROGRAMME.md'),'workflow':record(out/'CURRENT_RESEARCH_WORKFLOW_4000_CHARS.md'),'next':'Original B0 baseline and finite q-scale Hankel/recurrence remainder, then original mixed-cohomology receiver.'}
(out/'DELIVERY_RECEIPT.json').write_text(json.dumps(final,indent=2),encoding='utf-8')
print(json.dumps(final,indent=2))
