"""Generate the reader's map without modifying the authoritative audit JSON."""
from pathlib import Path
import json,hashlib,re

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
STAGE=ROOT/'cumulative_source_v1'
def read(name):return json.loads((HERE/name).read_text(encoding='utf-8'))
pins={r['reader_path']:r for r in read('EXPECTED_FINAL_ACTIVE_PATCHES.json')['patches']}
graph=read('FINAL_ASSEMBLY_INCLUSION_GRAPH.json')['files']
def proof(path,tags):
    p=pins.get(path,graph.get(path))
    assert p is not None,path
    active=p['sha256'];accepted=p.get('accepted_source_sha256',active)
    code=f"`{accepted[:12]}`" if accepted==active else f"`{accepted[:12]}` → `{active[:12]}`"
    return f"[{tags} — {Path(path).name}](repository/{path}) ({code})"
def receipt(name,label):
    assert (HERE/name).is_file(),name
    return f"[{label}](repository/provenance/dependency_audit/{name})"
def uses(path,tags):return f"[{tags}](repository/{path})"
R='tex/research_conclusion.tex'
families=[
 ('source-correction-proper-W','1. Proper-source correction',
  r'For the original $R=s_h+\Theta T$, the correction at $W$ is $\eta_W[T]$, where $\eta_W:V/W\to\mathscr B_\Omega/\Theta W$ sends $[v]$ to $[\Theta v]_W$.',
  [('tex/tau_chain.tex','TC29a–d'),('tex/support_diagrams.tex','D9–14')],
  'TB.26, TB.37–39; '+uses(R,'R1a–c, R47 and R67')+'. Source, outer leg and coefficient mask remain independent; an empty mask retains its outer label.',
  [('DEPENDENCY_CHANGE_USE_LEDGER.json','Exact old locators'),('FINAL_ASSEMBLY_CHECK.json','Active-source check')]),
 ('finite-source-adjacent-generator','2. Finite source tower',
  r'The original generator has type $D:W_m^{\rm src}\to W_{m+1}^{\rm src}$. The lower source retains $-[D^{m+1}\phi_*]d_m$, while the full primitive retains both terminal coefficient rows.',
  [('tex/tau_boundary.tex','TB.26 and TB.35–39')],
  uses(R,'R1b–c and R67')+'. Quotient arrows use the adjacent source level; the original arithmetic Grams and two-row observation remain.',
  [('DEPENDENCY_CHANGE_USE_LEDGER.json','Source-tower record'),('FINAL_ASSEMBLY_CHECK.json','Active-source check')]),
 ('exact-u-polynomial-connection','3. Full singular-parameter connection',
  r'The literal divisions give $\Omega_u=-C(t)/u^2+B/u$ and $\Pi_u=\Pi\Omega_u$, with the degree-dependent chain term and the full two-parameter curvature.',
  [('tex/deligne_exponential_determinant_extension.tex','XD.u1–7'),('tex/deligne_split_sidebar.tex','DS70–74'),('tex/deligne_translation_bridge.tex','DT14–16')],
  uses('tex/sga_constituent_period_curvature.tex','SC.u1–7')+'; '+uses('tex/period_critical_kernel_bridge.tex','PC.u1–3')+'; '+uses('tex/period_laplacian_control_bridge.tex','LC.u1')+'; '+uses('tex/circle_critical_observation_diamond.tex','DC31–32')+'; '+uses('tex/residue_constituent_extension.tex','RCX.u1–6')+'; '+uses(R,'R52, R56–57, R59, R62 and R68–70')+'. Original metric derivatives and source commutators remain explicit.',
  [('BOUNDARY_NEW_PROOFS_REVIEW.md','Full inserted-proof review'),('TYPOGRAPHY_INDEPENDENT_CHECK.json','Presentation inverses')]),
 ('determinant-reuse-full-phase','4. Original determinant and contour phase',
  'The boundary determinant reuses XD18–19 through the proved original polynomial and contour identification, retaining ordered phases, Gamma factors and the specified primitive constant.',
  [('tex/deligne_exponential_determinant_extension.tex','XD18–19 and XD.u1–7'),('tex/marked_product_boundary_connection.tex','Complete BC proof')],
  uses('tex/sga_constituent_period_curvature.tex','Original period Gram and SC.u5–7')+'; '+uses(R,'R52–53 and R68')+'. Passing to a Gram determinant uses the explicitly stated modulus square.',
  [('BC_COMPLETE_BODY_TRANSFER_CHECK.json','Complete BC body'),('BOUNDARY_NEW_PROOFS_REVIEW.md','Connection/determinant review')]),
 ('AP-analytic-poles-u-propagation','5. Analytic pole extension',
  r'For $f=\Phi-ts$, the pole coupling is $-Q_p/u^2$, with $Q_p=\operatorname{rem}_{h-t}((f(s)-f(p))/(s-p))$. The ordinary division quotient is $1/(d+1)$, so its derivative correction is zero.',
  [('tex/actual_tau_analytic_pole_complete.tex','AP10–13, AP19–26 and APU1–23')],
  uses(R,'R69–71')+r'. Weighted residues, positively oriented loop periods, finite transport, inverse-transpose dual, full unit gauge and the specified formal endpoint all receive the same connection. The loop factor remains $2\pi i$.',
  [('AP_COMPLETE_BODY_TRANSFER_CHECK.json','Complete AP body'),('CONCLUSION_COMPLETE_BLOCK_TRANSFER_CHECK.json','Whole-result transfer')]),
 ('joint-signed-source-control','6. Original signed source comparison',
  r'The original Gamma and arithmetic forms act on the common $\mathcal P_{2q}$, with the typed relation inclusion $B_{\rm SP}=I_NB_{\rm AW}$. Their two-control minimum is retained inside the stronger family-10 minimum.',
  [('tex/AT_complete.tex','AT18–22'),('tex/AW_complete.tex','AW13a–18'),('tex/tau_signed_projection_control.tex','SP10–13')],
  uses('build/endpoint_four_volume_threshold_source.tex','FV.M1–18')+'; '+uses('tex/endpoint_restriction_join.tex','ERJ.32 and following signed refinement')+'; '+uses('tex/arithmetic_volume_upper_route.tex','AU.31a–b')+'; '+uses(R,'R44–45 and R47')+'. All four determinant signs, original masses, endpoint losses and proper-source residuals remain.',
  [('ROOT_AND_SIGNED_PROOF_REVIEW.json','Signed-operator review'),('EXPECTED_FINAL_ACTIVE_PATCHES.json','Full accepted pins')]),
 ('one-primary-inertia-scope','7. One-primary tensor boundary',
  r'The one-factor inertia calculation for $h=(s-\rho)^m$, $t=0$, is carried through every ordered tensor character. Trivial character products and additive-factor cancellation are explicitly retained.',
  [('tex/marked_product_boundary_connection.tex','Single-primary boundary proof'),('tex/tensor_primary_boundary_backpropagation.tex','BPC.1–14, BTP.1–11 and BTF.1–11'),('tex/period_critical_kernel_bridge.tex','PC30a–g')],
  uses(R,'R56 and R68')+'. The original coefficient lattice, factorial losses, reduction map and residual-collision annihilator accompany the tensor invariant calculation. Coefficient reduction and geometric inertia keep their stated domains.',
  [('DEPENDENCY_CHANGE_USE_LEDGER.json','Tensor-domain record'),('FINAL_ASSEMBLY_CHECK.json','Complete companion inclusion')]),
 ('sampled-source-signed-budget','8. Finite-circle source error',
  r'The actual continuous and sampled forms restrict from $\mathcal P_{2q+2}$ to the common $\mathcal P_{2q}$. The earlier error receives the full spectrum, five controls, nonlinear interval and finite signed residual.',
  [('tex/periodized_source_intake_proofs.tex','PSA24a–25bc'),('tex/periodized_curvature_control_bridge.tex','FC13a–b')],
  uses(R,'R58')+'; the original-metric generator comparisons in '+uses(R,'R60–61')+' retain their two degree raises. The sampled density, including its zero mode and masses, stays explicit; no Gamma substitution is used.',
  [('ROOT_AND_SIGNED_PROOF_REVIEW.json','Common-source proof checks'),('CONCLUSION_COMPLETE_BLOCK_TRANSFER_CHECK.json','Complete R58 transfer')]),
 ('actual-packet-induced-quotient','9. Induced quotient filtration',
  r'The actual quotient of $E_\rho$ by $(s-\rho)^2E_\rho$ inherits degrees $m-1,m-3$ and shift $m-2$. Its source realization uses the literal quotient of $[V\to B_\rho]$ by $[V\to B_J]$.',
  [('tex/tau_mixed_support_monodromy_filtration.tex','MW23–27'),('tex/tau_mixed_relative_extension_control.tex','MRE34–42'),('tex/tau_mixed_coefficient_face_attachment.tex','MCF47–51')],
  uses(R,'R67')+'. The low source complex, proper-source $V/W$, two-leg diagonal, and exact adjacent-level $D$ and $D-\rho$ maps are retained. No recentering is made.',
  [('DEPENDENCY_CHANGE_USE_LEDGER.json','Filtered source maps'),('FINAL_ASSEMBLY_CHECK.json','Full MW/MRE/MCF inclusion')]),
 ('five-controls-and-signed-certificate','10. Five controls and constructed signed residual',
  r'The common signed derivative receives the full-spectrum, exact trace-norm, overlap, centered Hilbert–Schmidt and angle bounds. The finite Neumann operator gives $j_L\pm e_L$, with $e_L\le\vartheta^{L+1}\sqrt{K_D(8q-6)}$.',
  [('tex/recursive_metric_transport.tex','RMT1–22'),('tex/incoming_source_metric_control.tex','ISM1–43')],
  'AT18–22, AW14–18, SP13, FV.M15–18, PSA25 and FC13; '+uses(R,'R44–45, R47, R58 and R72–74')+'. The signed interval is intersected with the additive and nonlinear intervals before substitution. Convergence is for each fixed original pair of forms; the angle entry uses the proved moment-path positivity.',
  [('ROOT_AND_SIGNED_PROOF_REVIEW.json','Complete correspondence and residual'),('FINAL_ASSEMBLY_CHECK.json','Actual proof inclusion')]),
 ('cohort-common-source-descendants','11. Arithmetic cohort and individual holonomy phases',
  r'The earlier ACM minimum and theorem receive all eligible controls. HC restricts its original phase source from degree $2q+2$ to $2q$, then carries the signed Gamma and phase intervals into the derivative-source energy budget.',
  [('tex/cohorts/cf/13_ACM.tex','ACM11a–16'),('tex/cohorts/cf/31_HC.tex','HC9–14d')],
  uses(R,'R63')+' and '+uses('tex/holonomy_hcd_complete.tex','HCD equal-image complex')+r'. The averaged quotient retains $G_N=\overline G_N+\mathscr D_N$ and its separately proved $2q$ allowance; averaging minimized quotient forms is not silently replaced by a single common-source minimum.',
  [('DEPENDENCY_CHANGE_USE_LEDGER.json','Exact cohort uses and scope'),('CONCLUSION_COMPLETE_BLOCK_TRANSFER_CHECK.json','R63–66 transfer')]),
 ('root-current-results-scope','12. Current tau pushforward and endpoint results',
  r'R67 retains the exact tensor kernel $(dC_{\rm full}^{k-1}\cap C_\lambda^k)/dC_\lambda^{k-1}$. R72 retains the admitted ordering $i\le j$ in the cross trace. R73–74 receive the complete five-control and signed nonlinear intersection.',
  [(R,'R67 and R72–74')],
  'The original source tower and mixed coefficient faces remain in the absolute-base pushforward; '+uses('tex/incoming_source_metric_control.tex','ISM38–43')+' supplies the original primitive and carrier maps. Full-source acyclicity, proper-source $V/W$ and the two-leg diagonal have their exact separate types.',
  [('ROOT_AND_SIGNED_PROOF_REVIEW.json','Independent result review'),('CONCLUSION_COMPLETE_BLOCK_TRANSFER_CHECK.json','Accepted whole blocks')]),
 ('complete-R62-proof-transfer','13. Complete quotient-curvature continuation',
  'The complete updated R62 is retained when the historical closing paragraph is relocated. Its two-parameter Hessian, ordered derivative recursion, forced-equation derivative and pure translation derivatives all remain in the cumulative result.',
  [(R,'R62'),('tex/residue_constituent_extension.tex','RCX.u1–6')],
  'The original fourth derivative and its $3R^2/u^2$ term remain the fixed-$u$ slice. The following R63–74 results are appended after the full R62 proof. The rejected truncation and its exact diff remain in provenance.',
  [('CONCLUSION_COMPLETE_BLOCK_TRANSFER_CHECK.json','22 complete-block checks'),('R62_ASSEMBLY_OMISSION.diff','Preserved rejected difference')]),
 ('active-inclusion-after-preparation','14. Actual compiled-source closure',
  'Every accepted replacement is bound to the path read by the real main file after source preparation. Presentation changes carry exact full-file forward and inverse maps, including recorded line-ending transport.',
  [('tex/main.tex','Actual cumulative main')],
  'All 41 explicitly checked source/asset paths pass. The 239 recursively included TeX files match the compiler recorder; the additional displayed verifier gives 240 recorded sources. All 4,923 historical baseline files remain unchanged. The portable rebuild retains the same sources.',
  [('FINAL_AUDIT_RECEIPT.json','Final source closure'),('DELIVERED_SOURCE_AND_PDF_CHECK.json','Portable source/PDF binding')]),
]
assert [x[0] for x in families]==[x['id'] for x in read('DEPENDENCY_CHANGE_USE_LEDGER.json')['records']]
lines=[
 '# Change/use ledger',
 '',
 'This ledger maps the fourteen revised result families to their active complete proofs and downstream uses. It accompanies the cumulative PDF and repository at the delivery root. The [detailed JSON ledger](repository/provenance/dependency_audit/DEPENDENCY_CHANGE_USE_LEDGER.json) is authoritative for exact earlier source locators, hypotheses, and full change/use records.',
 '',
 'Source pins below are the first twelve hexadecimal characters of SHA-256. An arrow gives **accepted proof source → actively typeset source**; the complete reversible transformation and both full hashes are in the [accepted active-source map](repository/provenance/dependency_audit/EXPECTED_FINAL_ACTIVE_PATCHES.json) and [presentation verification](repository/provenance/dependency_audit/TYPOGRAPHY_INDEPENDENT_CHECK.json). Unchanged downstream file pins are in the [actual inclusion graph](repository/provenance/dependency_audit/FINAL_ASSEMBLY_INCLUSION_GRAPH.json). Result numbers refer to the [current complete conclusion](repository/tex/research_conclusion.tex).',
 '',
 '| Result family and change | Earlier active proofs and accepted pins | Downstream uses and retained scope | Verification |',
 '| --- | --- | --- | --- |',
]
for ident,title,change,earlier,downstream,receipts in families:
    sites='<br>'.join(proof(path,tags) for path,tags in earlier)
    refs='<br>'.join(receipt(name,label) for name,label in receipts)
    # Markdown table delimiters must not swallow formula bars.
    cells=[f'**{title}.** {change}',sites,downstream,refs]
    lines.append('| '+' | '.join(x.replace('|',r'\|') for x in cells)+' |')
lines += ['',
 'The verified delivery contains a 1,625-page cumulative PDF. Its portable rebuild preserves all 240 recorded source files and reports zero undefined controls, missing characters, LaTeX warnings, font warnings, or overfull boxes. The [delivered-source receipt](repository/provenance/dependency_audit/DELIVERED_SOURCE_AND_PDF_CHECK.json) binds those sources to the exact PDF hash.',
 '',
 'The audit covers this explicit dependency closure and complete source transfer. The finite packet estimates retain their actual source-dependent constants and do not by themselves establish the required uniform control as the tensor order varies or complete RH. The research programme remains open at those analytic calculations.',
 '']
target=HERE/'CHANGE_USE_LEDGER.md'
target.write_text('\n'.join(lines),encoding='utf-8')
assert len(re.findall(r'^\| \*\*\d+\.',target.read_text(),re.M))==14
print(json.dumps({'path':str(target),'families':len(families),'bytes':target.stat().st_size,'sha256':hashlib.sha256(target.read_bytes()).hexdigest()}))
