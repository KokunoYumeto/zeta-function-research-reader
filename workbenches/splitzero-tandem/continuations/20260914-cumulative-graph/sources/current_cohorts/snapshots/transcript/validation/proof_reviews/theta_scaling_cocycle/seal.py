from pathlib import Path
import hashlib,json

WORK=Path(__file__).resolve().parent
ROOT=WORK.parents[2]
OUT=ROOT/'output/tau_f1_transcript_audit_2026-09-13/proofs'
outputs=[]
for suffix in ('md','tex','fragment.tex','pdf'):
    path=OUT/('theta_scaling_cocycle.'+suffix)
    data=path.read_bytes()
    outputs.append({'path':path.relative_to(ROOT).as_posix(),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
source_names=[
    'output/split_zero_rh_tandem_2026-09-12/tex/arithmetic_input.tex',
    'output/split_zero_rh_tandem_2026-09-12/sources/Tau_Base_Cohomology_2026-09-12/NOTE.md',
    'output/tau_f1_transcript_audit_2026-09-13/sources/turns/A1694.md',
    'output/split_zero_rh_tandem_2026-09-12/sources/Tau_Global_Comparison_2026-09-12/NOTE.tex',
]
sources=[]
for name in source_names:
    data=(ROOT/name).read_bytes()
    sources.append({'path':name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
record={'status':'completed','outputs':outputs,'sources':sources,
        'proof_sections':'0-9, equations 1-46 plus 28a and 43a-43c',
        'original_transcript_locator':{'turn':'A1694','node':'1fa0ebbc-f569-40c1-b7ac-b523da19a5f0','chain_position':3576},
        'validation':{'pdf_pages':18,'latex':'two-pass pdflatex, no warnings/overfull/underfull boxes',
                      'visual':'all 18 current pages inspected in contact sheets; revised pages 12 and 16 inspected individually, with unchanged gamma page 8 inspected on the prior identical rendering',
                      'text':'no Unicode replacement characters',
                      'gamma_kernel_cases':54,'decimal_precision':60,
                      'max_scaled_kernel_error':'2.13916150176476746183077201848691770770289918299790120200351e-61',
                      'mutation_controls':['lost_quartic_factor_two','negative_time_orientation_reversed']},
        'integration':'Standalone TeX requires mathrsfs/mathtools. fragment.tex contains the identical document body without preamble. Parent owns global tag renaming and cumulative-master integration.',
        'review_repairs':'Companion review resolved: P_V has the explicitly proved even-Schwartz domain; global-section infinitesimal defect uses B_D^s=Theta(phi_*ell-D b_Z+b_Z A), with full integration-by-parts proof in 43a-43c.',
        'scope':'No Lean or remote publication. Global retraction and cocycle in A1694 are credited as prior work. New proof evaluates the finite cocycle, retained unit and nilpotents, exact global-section bridge and equivariant support extension, tensor homotopies and integrated dx pairing.'}
(OUT/'theta_scaling_cocycle.manifest.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(outputs,indent=2))
