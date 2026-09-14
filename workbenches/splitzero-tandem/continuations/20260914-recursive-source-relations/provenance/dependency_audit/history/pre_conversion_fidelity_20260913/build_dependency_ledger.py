"""Assemble reviewed change/use records and discover literal theorem uses."""
from __future__ import annotations
import hashlib,json,re
from pathlib import Path

HERE=Path(__file__).resolve().parent
W=HERE.parents[2]
BASE=W/'output/split_zero_rh_tandem_2026-09-12/current_source_20260913_periodized_residue'
STAGE=W/'work/cumulative_next_edition_staging_20260913_v19/reader'

def loc(path,token,occurrence=1):
    p=Path(path)
    if not p.is_absolute(): p=BASE/path
    text=p.read_text(encoding='utf-8-sig')
    hits=[m for m in re.finditer(re.escape(token),text)]
    if len(hits)<occurrence: raise ValueError((str(p),token,occurrence))
    m=hits[occurrence-1]
    return {'path':str(p),'line':text.count('\n',0,m.start())+1,'token':token,
            'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}

def use(path,token,relation,status='reviewed-proof-context'):
    return {**loc(path,token),'relation':relation,'review_status':status}

records=[
 {'id':'source-correction-proper-W','lane':'support',
  'old':loc('tex/tau_chain.tex','\\tag{TC29}'),
  'refinement':'For R=s_h+Theta T, sigma_R,W-sigma_h,W=eta_W[T]; generator defect takes Q_W to Q_Wprime when DW is contained in Wprime; dilation takes W to R_a W. Global quotient and metrics retain their old values.',
  'revised_labels':['TC29a','TC29b','TC29c','TC29d','D11','D14'],
  'uses':[use('tex/tau_boundary.tex','\\tag{TB.26}','Actual adjacent orthogonal representative change'),
          use('tex/research_conclusion.tex','\\tag{R1}','Opening current arithmetic comparison must state proper-source residual'),
          use('tex/research_conclusion.tex','Result R47','Full remainder kernel statement stays valid; proper-source extension must retain residual'),
          use('tex/support_diagrams.tex','\\tag{D8}','Bottom categorical kernel and all-label fibre kernel remain separate exact constructions')],
  'discovered_issue':'New metric FV.M12 initially applied full-source vanishing to every arbitrary W. Repaired and independently accepted in FV.M13-14: kernel is (d C_full^(k-1) intersect C_lambda^k)/d C_lambda^(k-1); one-factor specialization is V/W with its original Theta map.'},
 {'id':'finite-source-adjacent-generator','lane':'support',
  'old':loc('tex/tau_boundary.tex','W_{m+1}=\\operatorname{span}'),
  'refinement':'D induces Q_Wm to Q_Wm+1, not a fixed-level endomorphism. Mod W_m the original full boundary retains -[D^(m+1)phi_*]d_m; both d_m,d_m+1 remain in the full primitive.',
  'revised_labels':['TB.37','TB.38','TB.39'],
  'uses':[use('tex/tau_boundary.tex','\\tag{TB.35}','Full source primitive fixes residual sign'),
          use('tex/tau_boundary.tex','\\tag{TB.36}','Two-row arithmetic observability remains stronger than one transition'),
          use('tex/research_conclusion.tex','\\tag{R1}','Preserve original Grams and boundary formula while refining quotient domains')]},
 {'id':'exact-u-polynomial-connection','lane':'boundary',
  'old':loc('tex/deligne_exponential_determinant_extension.tex','\\tag{XD12}'),
  'refinement':'Omega_p=-C_p(t)/u^2+B_p/u and Pi_u=Pi Omega_p, with degree-correct chain maps, full constants, and all nilpotents.',
  'revised_labels':['XD.u1','XD.u2','XD.u3','XD.u4','XD.u5','XD.u6','XD.u7','DS70','DS71','DS72','DS73','DS74','PC.u1','PC.u2','PC.u3','SC.u1','SC.u2','SC.u3','SC.u4','SC.u5','SC.u6','SC.u7'],
  'uses':[use('tex/deligne_split_sidebar.tex','\\tag{DS68}','Original family and source deformation receive u connection'),
          use('tex/deligne_translation_bridge.tex','\\tag{DT.3}','Full scalar/Pascal gauge must carry u derivative'),
          use('tex/period_critical_kernel_bridge.tex','\\tag{PC18}','Observation C Pi^-1 gets -C Omega Pi^-1'),
          use('tex/period_laplacian_control_bridge.tex','\\tag{LC12}','Original metric congruence and derivative must include u'),
          use('tex/circle_critical_observation_diamond.tex','\\tag{DC30}','All four quotient/critical/circle maps get u equation; fixed diamond maps commute'),
          use('tex/residue_constituent_extension.tex','(LC12a)','Original source forcing must retain its full primitive'),
          use('tex/research_conclusion.tex','Result R52','Current result reports new connection and reuse of original determinant'),
          use('tex/research_conclusion.tex','Result R56','Critical/tensor kernel observations retain new two-parameter defect'),
          use('tex/research_conclusion.tex','Result R57','Laplacian transport retains unchanged source metric'),
          use('tex/research_conclusion.tex','Result R59','Four circle diamond observations acquire same u equation'),
          use('tex/research_conclusion.tex','Result R62','Constituent/quotient curvature and current scope advance together')]},
 {'id':'determinant-reuse-full-phase','lane':'boundary',
  'old':loc('tex/deligne_exponential_determinant_extension.tex','\\tag{XD19}'),
  'refinement':'BC full ordered determinant equals prior XD determinant after the exact original polynomial/contour identification; its computation is reused, with u connection added.',
  'uses':[use('tex/sga_constituent_period_curvature.tex','(XD18)--(XD19)','Squared Gamma constant and period Gram remain exact'),
          use('tex/research_conclusion.tex','Result R52','Attribution and all oriented Gamma factors'),
          use('tex/research_conclusion.tex','Result R53','Squared determinant loses phase only through explicitly taking modulus')]},
 {'id':'AP-analytic-poles-u-propagation','lane':'boundary',
  'old':loc(STAGE/'sources/next_edition/analytic_pole_conversions_v2/build/analytic_pole/endpoint_analytic_pole_source.tex','\\tag{AP10}'),
  'refinement':'For r_p=(s-p)^-1, f=Phi-ts, Q_p=rem_(h-t)((f-f(p))/(s-p)), nabla_u r_p=-Q_p/u^2-f(p)r_p/u^2. Full block Omega_ext=[[Omega_pol,-Q/u^2],[0,-diag(f(p))/u^2]]. The ordinary quotient is constant 1/(d+1), hence its derivative correction vanishes.',
  'uses':[use(STAGE/'sources/next_edition/analytic_pole_conversions_v2/build/analytic_pole/endpoint_analytic_pole_source.tex','\\tag{AP11}','W_u=-diag(f(p))W/u^2 gives exact weighted-residue horizontality'),
          use(STAGE/'sources/next_edition/analytic_pole_conversions_v2/build/analytic_pole/endpoint_analytic_pole_source.tex','\\tag{AP19b}','Entire polynomial-plus-loop period matrix has u derivative Pi_ext Omega_ext'),
          use(STAGE/'sources/next_edition/analytic_pole_conversions_v2/build/analytic_pole/endpoint_analytic_pole_source.tex','\\tag{AP22}','Dual uses inverse-transpose connection and same residue injection'),
          use(STAGE/'sources/next_edition/analytic_pole_conversions_v2/build/analytic_pole/endpoint_analytic_pole_source.tex','\\tag{AP26}','Formal endpoint maps remain separately typed; no evaluating formal contraction at nonzero u')],
  'review_status':'Derived directly in this audit; boundary lane supplied complete APU1-23 proof. Independent complete-body transfer to the active AP wrapper passed; mathematical owner and separate reader accepted the full extension.'},
 {'id':'joint-signed-source-control','lane':'metric',
  'old':loc(STAGE/'tex/next_edition/AT_complete.tex','\\tag{AT18}'),
  'refinement':'At original common source P_2q and original Gamma/arithmetic masses, J=integral min(S_AW,S_SP) bounds signed correction; J<=L_q<=(2q-1)log kappa. B_SP=I_N B_AW fixes the relation-map codomain.',
  'revised_labels':['AT18a','AT18','AT19','AT20a','AT20b','AT20c','AT22','AW13a','AW14','AW16a','AW18','SP1a','SP10a','SP10b','SP10c','SP13'],
  'uses':[use('build/endpoint_four_volume_threshold_source.tex','\\label{endpoint-four_volume_threshold','Finite four-volume expression receives exact two-sided signed budget'),
          use('tex/endpoint_restriction_join.tex','\\tag{ERJ.32}','Actual return eigenvalue products and inverse-power budgets inherit bound'),
          use('tex/arithmetic_volume_upper_route.tex','\\tag{AU.31}','Central upper estimate meets signed source control'),
          use('tex/research_conclusion.tex','Result R44','Four-volume costs preserve all four signed terms'),
          use('tex/research_conclusion.tex','Result R45','Original central upper/lower comparison incorporates finite budget'),
          use('tex/research_conclusion.tex','Result R47','Return spectrum and inverse powers incorporate refined budget')],
  'restrictions':['q>=1; k>=1; actual original packet h with full zero orders',
                  'T=M_x^-1(M1-M0) is self-adjoint with signs retained; M0^-1M1 is positive in M0',
                  'No uniform amplified-degree estimate follows from finite J',
                  'AW7/AW14 spectral and final condition-number results are reused; SP contributes actual overlap refinement']},
 {'id':'one-primary-inertia-scope','lane':'boundary',
  'old':loc(W/'work/rh_counterfactual_20260913/total_object/single_primary_boundary_control.tex','\\tag{SPF.1}'),
  'refinement':'Single-primary h=(s-rho)^m at t=0 has no inertia invariants in one factor; tensor products retain character products, including trivial products and additive-factor cancellation.',
  'uses':[use('tex/period_critical_kernel_bridge.tex','\\tag{PC30}','Original integral and cyclic tensor image receive explicit PC30a-g coefficient lattice, factorial cokernel and specialization'),
          use(W/'work/backpropagation_20260913/root/R67_R74_ORIGINAL.tex','Result R68','Original product period image receives full tensor character invariants and transverse connection, retaining one-factor vanishing only in its exact specialization')],
  'restrictions':['No transfer of one-factor vanishing to arbitrary tensor degree',
                  'Arithmetic coefficient reduction in characteristic p retains factorial cokernel; it is not the l-adic coefficient field',
                  'Arithmetic spectral N and geometric boundary inertia N are related only through explicitly proved maps']},
 {'id':'sampled-source-signed-budget','lane':'metric',
  'old':loc('tex/periodized_source_intake_proofs.tex','\\tag{PSA25}'),
  'refinement':'The actual original/sampled source forms restrict from degree D=2q+2 to H=P_2q; their signed four-endpoint error is bounded by the same pointwise-minimum construction, then by (2q-1)log(beta/alpha). The sampled form is not identified with Gamma.',
  'revised_labels':['PSA24a','PSA24b','PSA24c','PSA24d','PSA24e','PSA25','FC13a'],
  'uses':[use('tex/research_conclusion.tex','Result R58','Earlier 2q bound is replaced at its existing result site'),
          use('tex/research_conclusion.tex','Result R60','Dimension-free residue constituent estimate remains on its original metric'),
          use('tex/research_conclusion.tex','Result R61','Sampling commutator and generator estimate retain degree-two raises')],
  'review_status':'Owner supplied complete current proof and separate independent review; audit checked exact domain/dependency mapping.'},
 {'id':'actual-packet-induced-quotient','lane':'support',
  'old':loc(W/'work/tau_mixed_relative_extension_control_20260913.tex','\\tag{MRE10}'),
  'refinement':'For E_rho and J_rho=(s-rho)^2E_rho, the actual length-two quotient inherits degrees m-1,m-3 and center shift m-2. Its original-source realization is the exact quotient of [V->B_rho] by its subcomplex [V->B_J], with central spaces defined as q-preimages. Proper-W kernels remain.',
  'revised_labels':['MW23','MW24','MW25','MW26','MW27','MRE34','MRE35','MRE36','MRE37','MRE38','MRE39','MRE40','MRE41','MRE42','MCF47','MCF48','MCF49','MCF50','MCF51'],
  'uses':[use(W/'work/backpropagation_20260913/root/R67_R74_ORIGINAL.tex','Result R67','Absolute tau pushforward carries filtered original-source preimages and adjacent-level maps, retaining proper-W residual')],
  'review_status':'Full MCF47-51 proof read and accepted here; complete MW/MRE proof reviewed by support filtration lane and its independent checker.',
  'restrictions':['No actual repeated zero existence asserted',
                  'Induced filtration is not silently recentered',
                  'Lowest source-complex filtration keeps [V->Theta V], not a literal zero complex',
                  'D-rho uses (D-rho)W contained in Wprime; D uses DW contained in Wprime']},
 {'id':'five-controls-and-signed-certificate','lane':'metric-root',
  'old':loc(W/'work/backpropagation_20260913/recursive_metric_transport.tex','\\tag{RMT10a}'),
  'refinement':'The exact trace norm, actual overlap majorant, full relative spectrum, centered Hilbert-Schmidt bound and nonlinear angle bound act on the same signed derivative. Their pointwise minimum controls both original B and H_a(B)=2 arcosh(exp(B/(2a))), a=2q-1. The finite Neumann signed center J_L with residual epsilon_L gives a further interval for the same correction and is intersected before downstream substitution.',
  'revised_labels':['RMT10a','RMT10b','RMT13','RMT14','RMT16','RMT17','RMT18','RMT19','RMT20','RMT21','RMT22','ISM31','ISM32','ISM33','ISM34','ISM35','ISM36','ISM37'],
  'uses':[use(STAGE/'tex/next_edition/AT_complete.tex','\\tag{AT18}','Earlier absolute correction at its original proof site'),
          use(STAGE/'tex/next_edition/AW_complete.tex','\\tag{AW14}','Full-spectrum bound keeps five-control refinement'),
          use(W/'work/tau_signed_projection_control_20260913.tex','\\tag{SP13}','Earlier signed projection endpoint receives new minimum and nonlinear interval'),
          use('tex/research_conclusion.tex','Result R44','Four-volume quantity is the same B endpoint'),
          use('tex/research_conclusion.tex','Result R45','Central arithmetic upper/lower consequences retain original endpoint losses'),
          use('tex/research_conclusion.tex','Result R47','Original return spectrum and inverse-power consequences'),
          use('tex/research_conclusion.tex','Result R58','Apply to actual original/sampled moment path only with its established positive Gram'),
          use(W/'work/backpropagation_20260913/incoming_pr29_metric/incoming_source_metric_control.tex','\\tag{ISM12}','Earlier source-error coefficient 2q must receive current eligible refinement'),
          use(W/'work/backpropagation_20260913/incoming_pr29_metric/incoming_source_metric_control.tex','\\tag{ISM42}','New signed certificate carries exact arbitrary declared-source residual')],
  'review_status':'RMT10a through RMT22 and complete ISM1-37,40-43 contexts read here. Finite Neumann residual, original weighted operator correspondence, fixed-source convergence and nonlinear endpoint intersection independently accepted. Root R67/R72 scope repairs requested separately; metrics owner propagates all eligible old sites.',
  'restrictions':['Keep all 2q geometric angle entries; designated zero is displayed, and all additional zero contributions stay in the a=2q-1 scalar list.',
                  'Strict B positivity uses actual original-line moment Gram, not arbitrary positive coefficient form.',
                  'Signed residual convergence is at a fixed source; no uniform k estimate inferred.',
                  'Five-control minimum does not discard a smaller exact trace norm or signed center.']},
 {'id':'cohort-common-source-descendants','lane':'metric',
  'old':loc(W/'work/backpropagation_20260913/cohort_staging/snapshots/cf341/tex/continuation/ACM.tex','\\tag{ACM11}'),
  'refinement':'Replace the original two-control minimum at ACM11 and its theorem ACM13 with all eligible common-source controls and the finite signed interval; the same arithmetic canonical B endpoint is retained.',
  'uses':[use(W/'work/backpropagation_20260913/cohort_staging/snapshots/cf341/tex/continuation/ACM.tex','\\tag{ACM13}','Original aggregate theorem must carry the refined bound at its original statement'),
          use(W/'work/backpropagation_20260913/cohort_staging/snapshots/cf341/tex/modules/HC.tex','\\tag{HC14}','For each actual phase source, restrict the D=2q+2 Gram to common P_2q and improve its original 2q source-error bound'),
          use(W/'work/backpropagation_20260913/cohort_staging/snapshots/cf341/tex/modules/HC.tex','\\tag{HC13}','Phasewise source refinement carries to the existing return budget')],
  'review_status':'Complete original and new ACM11a-16, HC9-14d proof contexts independently read. Final ACM SHA2ca5d662b84804295f3172f2a1a46518cda56b918a70648129293d88da8272c5 and HC SHAe73bd05ee517cb07bc0ed37b293aa33e51b1f3c2ca8aacc80678b1dd7e8d4b94 accepted and actively included. Averaged-quotient proof remains unchanged.',
  'restrictions':['The averaged quotient Gram is an average of already minimized forms; it has not been proved to be the minimum quotient of one averaged source form.',
                  'Do not apply common-source projector formulas to that averaged quotient without an exact new source realization. Its separately proved estimate remains in scope.']},
 {'id':'root-current-results-scope','lane':'root',
  'old':loc(W/'work/backpropagation_20260913/root/R67_R74_ORIGINAL.tex','Result R67'),
  'refinement':'The current tau pushforward must retain every independent support kernel and carry finite Neumann signed bounds through R72-74. Exact proper-support residual is defined for compared top representatives in C_lambda^k; full-source acyclic low tail and proper-W residual are both retained. Cross-trace T_ij uses admitted degrees i<=j.',
  'uses':[use(W/'work/backpropagation_20260913/root/R67_R74_ORIGINAL.tex','Result R72','Canonical projector equality, signed secants, cross trace and finite residual'),
          use(W/'work/backpropagation_20260913/root/R67_R74_ORIGINAL.tex','Result R73','All five original-source controls replace the earlier spectral estimate at its result site'),
          use(W/'work/backpropagation_20260913/root/R67_R74_ORIGINAL.tex','Result R74','Computed signed interval is intersected with the nonlinear endpoint interval before propagation')],
  'review_status':'Root replacement source and exact replacement script fully read; secant signs, scalar cases, nonlinear derivative/inverse, and signed residual accepted. All three scope repairs reread and accepted at root revised SHA13288392b5cc9a19b7099e347a6d55b5b4790da58476e1b0385ea41bb648c921. Final carrier repair in ISM43 fully read and accepted at SHAce4b0968607fd06d7203ca498e66ce3dbe78e93e8eb3fe9079a106fa188ae0d8.'},
 {'id':'complete-R62-proof-transfer','lane':'assembly-root',
  'old':loc(W/'work/backpropagation_20260913/dependency_audit/rejected_conclusion_4e4eb1bd665d.tex','Result R62'),
  'refinement':'Remove only the exact six-line historical closing paragraph. Retain the full newly proved quotient Hessian, ordered u/t recursion, forced-equation derivative and pure-translation derivatives before appending R63-74.',
  'uses':[use('tex/research_conclusion.tex','Result R62','Whole earlier result is refined in place and all derivative descendants must remain present')],
  'review_status':'Complete-block validation rejected the first assembled 4e4... source because an old-ending truncation removed 76 lines of new proof. Root repaired the exact operation. Corrected complete source a310d094... and typeset active dc9852c... pass the full22-block test; rejected bytes and exact diff preserved.',
  'restrictions':['A source hash or successful compilation alone does not prove all accepted result blocks survived assembly.',
                  'The only removed text is the exact historical closing paragraph; no revised proof continuation is discarded.']},
 {'id':'active-inclusion-after-preparation','lane':'assembly',
  'old':loc(W/'work/cumulative_actual_tau_draft_inputs_20260913_v20/DRAFT_MASTER.tex','\\input{tex/AT_complete.tex}'),
  'refinement':'Bind accepted revised bytes to actual compiled routes after proof preparation; AT/AW supplied next_edition paths map to tex/AT_complete.tex and tex/AW_complete.tex in main. Overlays must survive rebuild.',
  'uses':[],
  'restrictions':['Historical 821 baseline is immutable; 4,923 files pinned independently.',
                  'Each proposed active patch requires both exact hash equality and recursive inclusion from actual main.',
                  'Archived source witnesses do not satisfy the active mathematical update.']}
]

def main():
    data={'schema':'reviewed-recursive-change-use-ledger-v1','scope':'Bounded theorem-level closure for three accepted propagation lanes; not a claim that every proof in 821 pages was reread.',
          'records':records}
    (HERE/'DEPENDENCY_CHANGE_USE_LEDGER.json').write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    tags=set()
    for row in records:
        tags.update(row.get('revised_labels',[]))
    candidates=[]
    for p in sorted((BASE/'tex').glob('*.tex')):
        lines=p.read_text(encoding='utf-8-sig').splitlines()
        for i,line in enumerate(lines):
            matches=[t for t in tags if t in line]
            if matches:
                candidates.append({'path':str(p),'line':i+1,'tokens':matches,'context':'\n'.join(lines[max(0,i-2):i+3]),'status':'lexical-candidate-only'})
    (HERE/'LEXICAL_CHANGE_USE_CANDIDATES.json').write_text(json.dumps(candidates,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({'reviewed_records':len(records),'lexical_candidates':len(candidates)}))

if __name__=='__main__': main()
