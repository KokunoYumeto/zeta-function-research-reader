"""Sequential exact checks and PDF build. No network or sibling imports."""
from pathlib import Path
import subprocess,sys,json,datetime
ROOT=Path(__file__).resolve().parents[1]
scripts=[
 'scripts/check_bridges.py',
 'agents/fibre_complexity/check_fibre_complexity.py',
 'agents/fibre_complexity/audit/check_audit.py',
 'agents/invariant_transport/verification/check_invariant_transport.py',
 'agents/invariant_transport/check_supplement.py',
 'agents/nonstandard_rh/check_nonstandard_coefficient.py',
 'agents/audit_root_bridges/check_root_bridges.py',
 'agents/gct_obstruction_literature/multiplicity_scope/check_plethysm.py',
 'agents/gct_obstruction_literature/check_interface.py',
 'agents/material_extension/check_material_extension.py',
 'scripts/check_integral_coefficient.py',
 'agents/gct_generator_block/check_generator_block.py',
 'agents/full_source_generators/reproduce_full_source.py',
 'agents/full_source_generators/source_basis/check_sign_witnesses.py',
 'agents/full_source_generators/source_basis/check_ssyt_bijection.py',
 'agents/full_generator_audit/independent_matrix_audit.py',
 'agents/full_generator_audit/check_raw_integral_map.py',
 'agents/full_generator_audit/check_source_graph.py',
 'agents/full_generator_audit/check_specialization.py',
 'agents/source_character_decomposition/check_character.py',
 'agents/source_character_decomposition/independent_check/check_character.py',
 'agents/source_character_decomposition/check_actual_projectors.py',
 'agents/character_projector_audit/check_projectors_independently.py',
 'scripts/check_quantum_tensor_symmetry.py',
 'agents/quantum_tensor_audit/check_tensor_independently.py',
 'agents/quantum_tensor_audit/small_braid/check_small_braid.py',
 'agents/positive_source_geometry_obstruction/check_positive_cover.py',
 'agents/positive_source_geometry_obstruction/audit/check_signs.py',
 'agents/positive_source_geometry_obstruction/audit/check_cover_relations.py',
 'agents/plethysm_transport_exact/basis/check_integral_schur_basis.py',
 'agents/plethysm_transport_exact/check_plethysm_transport.py',
 'agents/plethysm_transport_exact/audit/check_independently.py',
 'agents/plethysm_transport_exact/audit/mixed_prime/check_mixed_prime.py',
 'agents/ns_scaling_bridge/check_ns_scaling_bridge.py',
 'agents/ns_scaling_bridge/source_audit/check_bridge_independently.py',
 'agents/positive_source_geometry_obstruction/ns_bridge_audit/check_conic_connection.py',
 'agents/positive_source_geometry_obstruction/ns_bridge_audit/profile_review/check_profiles.py',
 'scripts/check_ns_schur_path.py',
 'agents/ns_schur_path_audit/check_endpoint_germ.py',
 'agents/ns_schur_path_audit/tableau_audit/check_tableaux.py',
 'agents/ns_schur_path_audit/tableau_audit/check_path_algebra.py',
 'agents/ym_composition_review/check_composition.py',
 'agents/ym_composition_review/coefficient_audit/check_coefficients.py',
 'agents/ym_composition_review/domain_audit/check_domains_independently.py',
 'agents/ym_composition_review/domain_audit/hilbert_complexification/cubic_check/check_cubic_weights.py',
 'agents/ym_composition_review/coefficient_audit/weight_identity/check.py',
 'scripts/check_permanent_projection.py',
 'scripts/check_permanent_obstructions.py',
 'agents/compressed_permanent_trace/check_compressed_trace.py',
 'agents/compressed_permanent_trace/audit/check.py',
 'agents/shared_verifier/check_shared_verifier.py',
 'agents/coefficient_geometry/check.py',
 'agents/frobenius_generator_bridge/check_frobenius_generator_bridge.py',
 'scripts/integrate_fragments.py',
 'scripts/build_reader.py',
 'scripts/seal_records.py',
 'scripts/check_fragment.py']
receipt=[]
for relative in scripts:
    path=ROOT/relative
    if not path.exists():
        raise FileNotFoundError(path)
    process=subprocess.run([sys.executable,'-X','utf8',str(path)],cwd=path.parent,
                           stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    output=process.stdout.decode('utf-8',errors='replace')
    receipt.append({'script':relative,'exit_code':process.returncode,'output':output})
    (ROOT/'checks/reproduction_progress.json').write_text(json.dumps(
        {'runs':receipt,'complete':False},indent=2),encoding='utf-8')
    if process.returncode:
        print(output); raise SystemExit(process.returncode)
(ROOT/'checks/reproduction.json').write_text(json.dumps(
 {'timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
  'execution':'one sequential Python process at a time; no Lean','runs':receipt,
  'all_passed':all(x['exit_code']==0 for x in receipt)},indent=2),encoding='utf-8')
print(json.dumps({'runs':len(receipt),'all_passed':True}))
