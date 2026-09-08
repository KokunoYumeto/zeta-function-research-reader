"""Snapshot independently owned proof fragments; record exact integration."""
from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
pairs=[
 ('agents/nonstandard_rh/nonstandard_rh_bridge.tex','tex/nonstandard_rh_bridge.tex'),
 ('agents/fibre_complexity/fibre_complexity.tex','tex/retained_fibres.tex'),
 ('agents/invariant_transport/invariant_transport.tex','tex/invariant_transport.tex'),
 ('agents/gct_obstruction_literature/gct_obstruction_interface.tex','tex/gct_obstruction_interface.tex'),
 ('agents/material_extension/material_extension.tex','tex/material_extension.tex'),
 ('agents/shared_verifier/shared_verifier.tex','tex/shared_verifier.tex'),
 ('agents/coefficient_geometry/coefficient_geometry.tex','tex/coefficient_geometry.tex'),
 ('agents/gct_generator_block/generator_block.tex','tex/generator_block.tex'),
 ('agents/frobenius_generator_bridge/frobenius_generator_bridge.tex','tex/frobenius_generator_bridge.tex'),
 ('agents/source_character_decomposition/character_decomposition.tex','tex/character_decomposition.tex'),
 ('agents/compressed_permanent_trace/compressed_permanent_trace.tex','tex/compressed_permanent_trace.tex'),
 ('agents/full_source_generators/full_source_generators.tex','tex/full_source_generators.tex'),
 ('agents/full_source_generators/source_basis/source_basis.tex','tex/full_source_basis.tex'),
 ('agents/positive_source_geometry_obstruction/positive_source_geometry_obstruction.tex','tex/positive_source_geometry_obstruction.tex'),
 ('agents/plethysm_transport_exact/basis/integral_schur_basis.tex','tex/plethysm_integral_basis.tex'),
 ('agents/plethysm_transport_exact/plethysm_transport.tex','tex/plethysm_transport.tex'),
 ('agents/ns_scaling_bridge/ns_scaling_bridge.tex','tex/ns_scaling_bridge.tex'),
 ('agents/ym_composition_review/ym_composition.tex','tex/ym_composition.tex')]
receipt=[]
for src,dst in pairs:
    source=ROOT/src
    if not source.exists(): raise FileNotFoundError(source)
    text=source.read_text(encoding='utf-8')
    edits=[]
    if 'nonstandard_rh_bridge' in src:
        text=text.replace(
          r'\quad W_{(i,k),(j,l)}=u_{ij}u_{kl},',
          r'\quad W_{(i,k),(j,l)}=u_{ij}u_{kl}.'+'\n'+r'\]'+'\n'+r'\[')
        edits.append("Split the FRT display into two displays to avoid margin overflow; no formula changed.")
    if src=='agents/gct_generator_block/generator_block.tex':
        old=('its additional weights and all four Chevalley generators, remains\n'
             'a larger object; the quotient morphisms above relate it to $M$.')
        new=('its additional weights and all four Chevalley generators, is constructed\n'
             'explicitly in Section~\\ref{sec:full-source-generators}. Its original\n'
             '$1260$ basis vectors, all divided powers, and the $420$-dimensional\n'
             'domain with $416$-dimensional kernel give the exact quotient\n'
             'morphism to $M$. The commutator obstruction on $M$ itself remains\n'
             'the one just proved.')
        assert old in text
        text=text.replace(old,new)
        edits.append('Propagate completed full original source representation and exact interval quotient by forward reference; preserve the four-state extension obstruction.')
    if src=='agents/coefficient_geometry/coefficient_geometry.tex':
        old=('This construction does not supply maps for the other entries of an\n'
             'original GCT-IV generator block or its canonical-basis labels. The\n'
             'scheme and torsor define a proved realization of this retained scalar;\n'
             'an identification with those additional source objects requires an\n'
             'actual construction respecting their generators and relations. No such\n'
             'identification, resolution of the disputed printed matrix-entry assignment,\n'
             'nonstandard-RH conclusion, or complexity-class consequence\n'
             'is asserted by this calculation.')
        new=('The scheme and torsor realize this retained scalar with all stated\n'
             'cohomological degrees. Section~\\ref{sec:fgb} constructs actual\n'
             'additive generator functors, their integral decategorification map\n'
             'to the source interval, and a separately specified cross-path relation\n'
             'cone. Its explicit Frobenius-equivariant endpoint map uses precisely\n'
             'these cohomology groups after two-periodization; the integer grading\n'
             'and the chosen extra relation data are recorded there. Compatibility\n'
             'with canonical-basis convolution in the full original source module\n'
             'remains unproved. The source endpoint itself is resolved by the\n'
             'original action paths in Section~\\ref{sec:gct-generator-interval},\n'
             'with the full source module in Section~\\ref{sec:full-source-generators}.')
        assert old in text
        text=text.replace(old,new)
        edits.append('Propagate exact generator functors, periodized Frobenius cone map, and resolved original endpoint while preserving open canonical source geometry.')
    if src=='agents/full_source_generators/full_source_generators.tex':
        text=text.replace(r'\input{agents/full_source_generators/source_basis/source_basis.tex}',
                          r'\input{tex/full_source_basis.tex}')
        edits.append('Use the root layout snapshot of the complete source-basis proof; all mathematical content retained.')
    if src=='agents/full_source_generators/source_basis/source_basis.tex':
        old=(r'\texttt{5c5b990306c3b817d822df9f5088fdd42}\allowbreak'+'\n'+
             r'\texttt{dda146fc3449155a0b2f6202d2ed49e}.')
        new=(r'\begin{center}\small'+'\n'+
             r'\texttt{5c5b990306c3b817d822df9f5088fdd42dda146fc3449155a0b2f6202d2ed49e}'+'\n'+
             r'\end{center}')
        assert old in text
        text=text.replace(old,new)
        edits.append('Move the full unchanged source SHA-256 to its own centered line to resolve cumulative margin overflow.')
    (ROOT/dst).write_text(text,encoding='utf-8')
    receipt.append({'source':src,'target':dst,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
                    'target_sha256':hashlib.sha256((ROOT/dst).read_bytes()).hexdigest(),'edits':edits})
(ROOT/'logbook/integration.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps({'integrated':len(receipt)}))
