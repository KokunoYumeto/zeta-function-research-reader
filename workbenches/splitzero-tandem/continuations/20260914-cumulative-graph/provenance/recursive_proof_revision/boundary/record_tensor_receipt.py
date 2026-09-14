"""Read-only source pinning and final provenance receipt for the tensor lane."""
from pathlib import Path
import hashlib
import json
import re

base = Path(__file__).resolve().parent
work = base.parents[1]
source = work/'rh_counterfactual_20260913/total_object/tensor_primary_boundary_control.tex'
old = work/'cumulative_next_edition_staging_20260913_v19/reader/tex/period_critical_kernel_bridge.tex'
files = [base/'fragments/tensor_primary_update.tex',
         base/'fragments/PC30_coefficient_insertion.tex',
         base/'fragments/single_primary_conclusion_update.tex']

def pin(p):
    data = p.read_bytes()
    text = data.decode('utf-8-sig')
    return {'path': str(p), 'sha256': hashlib.sha256(data).hexdigest(),
            'bytes': len(data), 'lines': len(text.splitlines()),
            'equation_tags': re.findall(r'\\tag\{([^}]+)\}', text)}

src_pin = pin(source)
assert src_pin['sha256'] == '692b5fe8b3434974df0a38ff905d5d1bd456ffba3374c508cfed84df47d61f88'
pins = [pin(p) for p in files]
log = (base/'compile/tensor_update_review.log').read_text(encoding='utf-8', errors='replace')
issues = [line for line in log.splitlines() if re.search(r'(^!|Overfull|Underfull|undefined|LaTeX Warning|Package .*Warning)', line)]
assert not issues, issues
checks = json.loads((base/'receipts/PC30_EXACT_CHECKS.json').read_text())
assert checks['status'] == 'PASS'
assert all(checks['source_sha256'][p['path'].split('\\')[-1]] == p['sha256'] for p in pins[:2])
receipt = {
    'scope': 'Complete TP/TPF/TCL reading and mathematical backward/forward propagation fragments',
    'source': src_pin,
    'old_pc30_source': pin(old),
    'delivered_sources': pins,
    'source_read_coverage': 'Every source line, TP.1--40, TPF.1--55, TCL.1--37; no source body omitted.',
    'compile': {'mode': 'LuaLaTeX draftmode', 'pages': 11, 'issues': issues,
                'log_sha256': hashlib.sha256((base/'compile/tensor_update_review.log').read_bytes()).hexdigest(),
                'pdf_produced': False, 'visual_qa_claimed': False},
    'checks': {'local_cases': checks['local_case_count'],
               'residual_collision_cases': checks['residual_collision_case_count'], 'status': 'PASS'},
    'sealed_or_live_sources_modified': False,
    'program_complete': False,
}
(base/'receipts/TENSOR_PRIMARY_PROPAGATION.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
table = '\n'.join(f"| {Path(p['path']).name} | {p['lines']} | `{p['sha256']}` |" for p in pins)
text = f'''# Full tensor-primary reading and propagation receipt

The lane read every line of the complete stable source `{source}`: {src_pin['lines']} lines, {src_pin['bytes']} bytes, SHA256 `{src_pin['sha256']}`. The reading covered TP.1–40, TPF.1–55 and TCL.1–37, including every proof paragraph, source dependency paragraph, convention and exceptional case. Reads were bounded consecutive blocks, not a search-only or equation-only intake.

The prior source neighborhood was then read directly in `{old}`, the entire PC28–PC34 neighborhood. The preserved PC30 formula is the characteristic-zero cyclic sum polynomial with the maximum primary nilpotent exponent over ordered tuples having exactly equal sums. Its existing proof retains the top multinomial coefficient. No historical source or working cumulative source was edited by this lane.

## Complete source reading

TP.1–12: checked the original primitive c=−(−rho)^(m+1)/(m+1), unchanged ordered top form and tensor complex, exact Pascal substitutions and inverses, contracting remainder decomposition, Gamma constants, contour orientation and remote connector estimates, period determinant, connection, analytic monodromy and all character projectors. The finite-cover logarithm concerns the covered local system; the unremoved exponential controls the actual connection. The invariant stalk here is the ordinary local-system stalk.

TP.13–22: checked the original arithmetic multiplication sum, every retained multinomial nilpotent coefficient, exact conjugated arithmetic action and its connection commutator, outgoing character shift, nonzero departure criterion, full compressed exponential with every return power, and its exact nonrepresentation defect. Scalar compression does not erase its outgoing arrow.

TP.23–29: read the complete Taylor unit and inverse recurrence, connection derivative defect, actual theta/Mellin-jet maps, the full-unit conjugate projector U_k Q_0 U_k^(-1), source period observation Pi_k U_k^(-1), compressed-unit inverse and representative remainder correction. No positive Taylor coefficient is discarded.

TP.30–40: read the original terminal monomial, exact n-divisibility invariant subsequence, complete period vector, original quartet-unit ratio and MAI/PAM scalar, dilation discrepancy, full rank proof using the explicitly auxiliary adjoint form, and the two-factor alternating eigenline. The auxiliary form proves algebraic rank and does not become the theta norm. External absence and represented zeros at existing support labels remain different entries of the original carrier.

TPF.1–11: read the actual coefficient specialization, full phase denominator restrictions, original constant-field extension and geometric Frobenius convention, all ordered character lines and every negative Gauss constant, source-preserving Kunneth map, tensor sign, and extension-field trace formula. Tensor degree stays an integer except in its specified multiplication of the coefficient-field element c.

TPF.12–24: checked the original Kummer/Artin–Schreier cover, inertia quotient and inverse deck signs, full tame and wild averages, rank counts, all c=0 versus p-divides-k cases, inertia image orders, Swan one on every nontrivial additive line, and zero logarithm after the actual finite cover. The original-inertia projector is zero when kc is nonzero; it is the tame projector exactly when the wild factor vanishes.

TPF.25–35: read original-base Frobenius tuple permutation, complete source descent through intermediate power maps, exact orbit-field Gauss scalar rather than an arbitrary root choice, cyclic orbit basis and characteristic polynomial, weight k of every nonzero invariant orbit, and all gcd/Mobius orbit counts. The denominator N is retained under the smaller-order character descent.

TPF.36–55: checked terminal deck-pullback versus inverse deck operator signs, primitive character label and orbit length, exact terminal inertia conditions, all factorial-specialization restrictions, coefficient algebra targets, shared cyclotomic integral representation and both actual base changes, complete Gauss-line reconstruction, and multiplicity-one quadratic Gauss identity. The scalar comparison retains its exact intertwining defect; no characteristic-p scalar is multiplied into a characteristic-zero l-adic line.

TCL.1–20: read the exact local coefficient ring and its specified map, original coordinate substitutions and full unit/inverse, complete original cyclic map, primitive vectors and pivot splitting, r! image lattice, rational saturation, full coordinate matrix, integer p-factorial depths, target cokernel with its free complementary summand, every reduced lattice chain, image and source nilpotency indices, exact Tor resolution/sign and terminal coefficient. No DVR structure, universal prime specialization or module-length assertion is inferred.

TCL.21–32: read the actual injection Z/p^L into the retained coefficient quotient, extension/contraction and all ideal laws on the principal subchain, original G_C_L coefficient morphism, represented zeros versus absence, annihilator labels and coefficient vectors, and simultaneous depth/character maps through the same cyclic inclusion and Tor sequence. An annihilator label never replaces its vector.

TCL.33–37: checked the original quartet CRT polynomial divided-difference identity proving inversion of each rational prime at most the tensor degree, the exact directed coefficient union containing Q, the nonextension of a local prime to that fully split stage, and the infinite surviving reduced character-zero subsequence with original nonzero precursor p W_p retained. The missing global specialization is not called a vanishing image of a vector.

## Proved backward and forward updates

The complete companion `tensor_primary_update.tex` supplies BPC.1–14, BTP.1–11 and BTF.1–11 with proofs. It carries the old cyclic exponent through the actual factorial image, saturation, quotient and Tor map, and carries the old single-primary boundary calculation forward through the full ordered tensor projector, original source unit, wild cancellation, orbit Frobenius and coefficient-stage restriction.

The direct insertion `PC30_coefficient_insertion.tex` belongs immediately after the original full PC30 proof and immediately before the paragraph beginning “Let chi_c,k”. PC30 itself is preserved. PC30a–e proves the exact unequal-order tuple version: D=sum(m_i−1), actual image r! U V_r, saturation, quotient, reduced kernel and the distinct source/image nilpotence indices. PC30f–g then proves the exact polynomial for newly colliding residual sums, with global prime bound p>m_rho for every retained primary order. The product is only over attained residual centres, and the empty carrier has psi=1 and zero source/image. The full geometric-inverse proof establishes the local minimal polynomial before the product/lcm calculation. The specialized kernel is (psi)/(bar-chi), on precisely the existing coefficient-map domain.

The replacement `single_primary_conclusion_update.tex` updates the old closing paragraph with a short proved tensor continuation. It retains the one-factor vanishing as k=1, gives the source-unit conjugate projector and exact tensor invariant/Swan cases, and explicitly identifies the saturated-lattice quotient separately from the full tensor cokernel. It references the complete proofs in the companion and the PC30 insertion.

The phase and coefficient domains are explicit. Factorial algebra uses p>m, or p>max m_i for an unequal tuple. The sheaf phase additionally requires the actual inverse of m+1 and every other original inverse. For m=1,p=2, the supplied coefficient-only map has K=0 and unit image, but has no extension across 1/2. A universal existence claim for characteristic-2 specialization of all original analytic coefficients is not made.

## Validation and ownership

The independent coefficient reviewer read TCL.1–20 and TCL.33–37, all new BPC.1–14 and BTF.8–11 proofs, the entire PC30a–g insertion with its original neighborhood, and the direct single-primary conclusion. The reviewer requested and verified explicit rho in the coefficient ring, global prime bounds, empty-carrier conventions, exact quotient targets, and literal TeX repairs. Detailed receipts are adjacent in `coefficient_review.md`, `tensor_primary_update_review.md`, and `PC30_and_final_coefficient_review.md`; the final source pins are below.

The three complete files compile together in 11 draft-mode pages, with no TeX error, warning, undefined reference, overfull box or underfull box in the final log. Only the expected backend notice that draft mode produces no PDF is present. No visual-QA claim is made and no PDF was produced by this lane.

The independent exact arithmetic script passes {checks['local_case_count']} unequal-order local cases and {checks['residual_collision_case_count']} global residual-collision cases. These checks supplement the symbolic proofs. They use explicitly chosen finite polynomial test data and do not assign their coefficient values to the original theta source.

| Source | Lines | SHA256 |
|---|---:|---|
{table}

The parent owns insertion into revised old-source copies and cumulative-book integration. The original 800-plus-page sources, sealed tensor source and web handoff folders remain unchanged. The broader mathematical programme is not marked complete by these local deliverables. `fix_tensor_update.py` is the historical one-pass repair record, not the build entrypoint; the read-only pinning script and the draft compile wrapper are the current validation entries.
'''
(base/'receipts/TENSOR_PRIMARY_FULL_READ.md').write_text(text, encoding='utf-8')
print(json.dumps({'source_lines': src_pin['lines'], 'source_tags': len(src_pin['equation_tags']),
                  'delivered': [{k: p[k] for k in ('path', 'sha256', 'lines')} for p in pins],
                  'compile_issues': issues}, indent=2))
