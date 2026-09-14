"""Exact complete bodies required by the current TWA/TW/FPK claims."""
from pathlib import Path
import hashlib,json
here=Path(__file__).resolve().parent
math=Path(r'C:\Users\[[user]]\Documents\math')
specs=[
('dependency_TWA.tex','work/backpropagation_20260913/root/signed_receiving_successor/TWA.tex','7e23d48f9f251bd0a065547226f76a21751a25a8bab87a237b5d1028cdff0b90','Complete accepted source, identical to the cut21 dependency copy; current use is original baseline/HC identity TWA5--10 and source/arithmetic transition.'),
('dependency_TW.tex','work/rh_counterfactual_20260913/continuation2/arithmetic_tail/arithmetic_tail_windows.tex','e2abf620498569e6fe6bd767d7ba68576960aef20ee30a6bf282aa16ee27640c','Full TW1--21 including TW15a,b; original source window comparison used by TWA.'),
('dependency_BT_BI.tex','work/rh_counterfactual_20260913/continuation2/arithmetic_tail/boundary_tilt_full.tex','3c7785c28e7c713cddfacf405b261b62c8d1dfb5016764089a5b1aa7f8da49ca','Full BT1--23 and its internal BI1--26 proof; TW2 uses BT12--16 and TW4 uses BT9--10, with original-line Gamma bound proved by BI.'),
('dependency_ARITHMETIC_ENDPOINT_NOTE.tex','work/backpropagation_20260913/base_source_plan_v1/files/sources/web_arithmetic_endpoint_delivery/Tau_Arithmetic_Endpoint_Bounds/NOTE.tex','f776e7934f026342f48732a74f14d57470b8aae1cef76ebdee5f831bd49dedf8','Full source; needed lower-envelope proof in sections3--4 equations14--29, retaining stated classical functional equation and strip Gamma estimate.'),
('dependency_CJ.tex','work/backpropagation_20260913/cumulative_source_v1/tex/consecutive_first_window_join.tex','483651e205bfc7b8a11e2aa67f2da9410843cc4a0fd8f2cfebab3623e4db329a','Full CJ.1--22; TW20 uses CJ.1--14.'),
('dependency_HC.tex','work/rh_counterfactual_20260913/total_object/propagation_metric/compile/tex/modules/HC.tex','d96317fca97a4c99d1856f3cdc7688d085ea8d3ec82d345e77ae3684c8e17e9b','Full source retained; current TWA uses HC2. Later holonomy claims are outside this bounded transitive review scope.'),
('dependency_EP.tex','work/backpropagation_20260913/cumulative_source_v1/tex/endpoint_product_sharpening.tex','a0fe9271049d9ca5224c411ce1df5c9033189e60f495cc45361c551dc10e4668','Full source retained; EP.1--11 proves CJ.8 regular radius and EP.41 proves CJ.11 original spectral trace. Later balanced-window sections are outside this closure question.'),
('dependency_FPK.tex','work/rh_counterfactual_20260913/continuation2/fixed_packet_kernel/fixed_gamma_full_jet_asymptotic.tex','fb64e10661cfe211b5466fef341a87d6b881768c13b0863d9fcf78c2201217e4','Full FPK source; current original Gamma fixed-packet construction with all sources and finite jets.'),
('dependency_TG.tex','work/rh_counterfactual_20260913/shared_thread_audit/segment29_40/sources/theta_gamma_reference.tex','a379a1e19de4ce885680e14bda466a37b4c1eb25228c19b931d573f58be167f9','Full source; required TG.7--14 fully proved. Later KL/Hardy/LMS claims are outside the needed audited scope.'),
('dependency_AT.tex','work/rh_counterfactual_20260913/total_object/propagation_metric/compile/tex/modules/AT.tex','438fd058f4745056945a3a747eaeb63f2b36a0f146335ed72018acdb28b93727','Full original AT source supplied by FPK transitive review.'),
('dependency_GC.tex','output/tau_split_zero_counterfactual_reconstruction_20260913/original_programme/tex/gamma_exact_coefficient_join.tex','6830ccf4e3a24beae858ae38d46a254c1af350d47741178d63a830b796d005aa','Full source; required GC10--13 proves the actual original tensor Gamma convolution used in AT4.'),
('dependency_A.tex','output/tau_split_zero_counterfactual_reconstruction_20260913/original_programme/tex/arithmetic_input.tex','a50b0fb587b644c4ea94dba45b2b423d038f2bfbe7fef188543939ba850e58d2','Full source; A1--10 gives the original source and section used in FPK final source realization paragraph.'),
('dependency_CC.tex','output/tau_split_zero_counterfactual_reconstruction_20260913/original_programme/tex/cyclic_sum_conormal.tex','1182806be9a6e1ecde9b594a195a8cd3fa17b7259540fcd5617d044d06b05e79','Full source; CC1--6 proves the exact collided sum and unit injection used in FPK final source realization paragraph.'),
]
entries=[]
for name,relative,pin,scope in specs:
    source=math/relative
    actual=hashlib.sha256(source.read_bytes()).hexdigest()
    assert actual==pin,(name,actual,pin)
    entries.append({'name':name,'source':str(source),'sha256':pin,'typeset':False,
                    'proof_scope':scope,'provenance':'Bounded current-claim dependency audit by mixed_row_morphism_review and its FPK closure subreview; full bodies copied, no acceptance inferred for unrelated later sections.'})
(here/'TRANSITIVE_PROVIDER_MANIFEST.json').write_bytes((json.dumps(entries,indent=2)+'\n').encode('utf-8'))
print(json.dumps({'complete_transitive_bodies':len(entries),'all_source_pins_match':True},indent=2))
