"""Bounded source and artifact receipts for this disjoint mathematical lane."""
from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
SOURCES=[
 ("cqCCM",Path(r"[local]/Documents\Papors\used often\NCG\Zeta-zeros-and-prolateproofs-final-2024.pdf"),
  "Alain Connes; Caterina Consani; Henri Moscovici",
  "Zeta zeros and prolate wave operators: Semilocal adelic operators",
  "Section 3.1.1–3.1.3, PDF p.12, equations (3.2)–(3.4); Section 3.6, PDF pp.17–19, equations (3.16)–(3.22), Lemma 3.3 and Proposition 3.6; reference [6] on p.38",
  "https://alainconnes.org/wp-content/uploads/Zeta-zeros-and-prolateproofs-final-2024.pdf"),
 ("cqCM",Path(r"[local]/Documents\Papors\used often\NCG\Noncommutative Geometry, Quantum Fields and motives.pdf"),
  "Alain Connes; Matilde Marcolli", "Noncommutative Geometry, Quantum Fields and Motives",
  "Chapter 2, Section 6 and 6.1, printed pp.377–381; Proposition 2.24 and its full proof, equations (2.180)–(2.199); Section 9 pp.407–408 and 416–420, definitions 2.45–2.46, Theorem 2.47 and full annihilator proof",None),
 ("cqConnesSelecta",Path(r"[local]/Documents\Papors\used often\Connes\selecta.ps-2 Trace Formula in Noncommutative Geometry and.pdf"),
  "Alain Connes", "Trace formula in noncommutative geometry and the zeros of the Riemann zeta function",
  "89-page author PDF, Section III pp.10–15, Theorem 1 p.13, Appendix I pp.62–67; exact online byte identity verified",
  "https://alainconnes.org/wp-content/uploads/selecta.ps-2.pdf"),
 ("cqRT",Path(r"[local]/Documents\arxiv_latex\_topic_fetch\RG_flow_thermodynamics_and_heat_flow_RH\1801.05914\fmp-template.tex"),
  "Brad Rodgers; Terence Tao", "The de Bruijn–Newman constant is non-negative",
  "Section 1, source labels hoz, sas, phidef, htdef; definitions read in primary TeX lines 63–117",
  "https://arxiv.org/abs/1801.05914"),
 ("parent-mechanism",Path(r"[local]/Documents\Papors\Chatnotes\Zeta-Function-Foundation\tex\satellites\23_source_mechanism_transfer.tex"),
  "Companion research task", "Transporting the retained counterexample mechanism",
  "Complete file read; especially retained-arithmetic-extension and retained-arithmetic-matrices",None),
 ("parent-weil-tests",Path(r"[local]/Documents\Papors\Chatnotes\Zeta-Function-Foundation\tex\satellites\24_retained_weil_test_algebra.tex"),
  "Companion research task", "The retained cover as an exact Weil test algebra",
  "Complete file read after parent handoff; compact primitive, moment image, finite jet and arithmetic-jet proofs",None),
 ("companion-xi4-operator",ROOT/"sources"/"heat_task_bridge_20260908"/"connes_continuation_bridge.tex",
  "Companion research task","The common heat space and the two moving quotient coordinates",
  "Complete bridge read; final paragraph The actual fourth coefficient in the same function space supplies the unchanged four-term T_D and original incidence factor. The present fragment independently proves every new assertion about this given operator.",None),
 ("retained-bilaplacian",ROOT/"sources"/"bilaplacian_005"/"arithmetic_bilaplacian.tex",
  "Companion research task","The second Euclidean diffusion of the actual arithmetic observable",
  "Complete frozen original source read. Original Cartesian sigma, inverse-fibre curve, all gradient/Hessian contractions and all four bilaplacian coefficients independently reproduced and checked in the present fragment.",None),
 ("xi4-bilaplacian-residue",ROOT/"sources"/"bilaplacian_005"/"xi4_bilaplacian.tex",
  "Companion research task","The retained fourth coefficient and its bilaplacian residue",
  "Complete companion proof read, including Piola transport, scalar residue, four-term coefficient and negative-time asymptotic. This fragment reproduces the original residue and coefficient, then independently proves their exact actual-source quotient relations; it makes no additional asymptotic claim.",None),
 ("selecta-topology-followup",ROOT/"sources"/"topology_followup_005"/"selecta.ps-2 Trace Formula in Noncommutative Geometry and.txt",
  "Alain Connes","Trace formula in noncommutative geometry and the zeros of the Riemann zeta function",
  "Bounded inspected passages and explicit term searches did not locate the CCM entire-function topology tau. Corrected extraction metadata: 4239 LF-delimited lines, 3298 nonempty, 89 PDF pages. Three topolog matches at pp.7,29,56 (lines293,1336,2633); Bruhat–Schwartz definition p.56 lines2623–2633, Theorem III.1 proof p.62 line2875, Appendix III p.79 line3824. This is not an exhaustive proof of mathematical absence.",
  "https://alainconnes.org/wp-content/uploads/selecta.ps-2.pdf"),
 ("cqCartan",ROOT/"sources"/"cartan_006"/"modular_cartan_realform_bridge_20260719.tex",
  "Supplied project manuscript","Antiunitary Modular Descent, Cartan Radialization, and the SO(3,2)–SO(4,1) Real-Form Bridge",
  "Primary TeX lines 1–240 and 311–455: title, sector conjugation, complex-time domains, Cartan logarithm and finite-dimensional left-right standard form. Present fragment independently constructs the heat modular double and corrects the zero-logarithm slice domain.",None),
 ("cqNS2026-old",Path(r"[local]/Documents\math\output\navier_stokes_research_2026-09-08\lanes\web_bundle_audit\coordination\claimed_proof\openai_navier_stokes.pdf"),
  "OpenAI","Finite time blowup for Navier–Stokes",
  "Preserved 165-page revision: pp.1–4, Theorem 1.1, and Corollary 10.6 pp.125–126 read by bounded primary-source review. Imported source claims; complete proof not independently verified here.",
  "https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf"),
 ("cqNS2026",Path(r"[local]/Documents\math\output\navier_stokes_research_2026-09-08\downloaded_public_release\navier-stokes.pdf"),
  "OpenAI","Finite time blowup for Navier–Stokes",
  "166-page revision served with Last-Modified 2026-09-08 19:09:35 GMT: pp.1–3 read directly; Theorem 1.1 and expanded prior-work attribution. Byte hash independently recomputed; equivalence to earlier complete proof not asserted.",
  "https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf"),
 ("cqABStatement",Path(r"[local]/Documents\math\output\navier_stokes_research_2026-09-08\lanes\web_bundle_audit\coordination\claimed_proof\buckmaster_statement.pdf"),
  "Tristan Buckmaster","Public statement concerning announced forced-fluid results with Levent Alpöge",
  "Complete four-page statement read: p.1 mathematical scope and Córdoba–Martínez-Zoroa credit; p.4 explicitly does not know whether private data were used. No appropriation allegation established by this work.",
  "https://cims.nyu.edu/~tristanb/statement.pdf"),
 ("cqNSFlow",ROOT/"sources"/"flow_007"/"ns_arithmetic_flow.tex",
  "Companion heat and arithmetic research task","Exact arithmetic profiles driven by a supplied incompressible flow",
  "Complete19285-byte proof read: original S and inverse, global preterminal real flow, both timegenerators, full material viscosity, exact32pi Fourier norm constants, velocity recovery, energy/supremum equivalence and full zero-unit transport. Independently reproduced in current fragment.",None),
 ("cqNSWitness",ROOT/"sources"/"flow_007"/"ns_public_witness.tex",
  "Companion heat and arithmetic research task","Using the released Navier–Stokes construction as the arithmetic input",
  "Complete15338-byte proof read and integrated with local references, full source sums and complete transfer proofs: actual cutoff-summed source, viscosity scaling, exact original sample matrix, full remainder, profile channel, energy and terminal Koopman map. External source existence remains an explicit dependency.",None),
 ("cqNSKernel",ROOT/"sources"/"flow_007"/"heat_connection.tex",
  "Companion heat and arithmetic research task","The actual arithmetic heat function and its weighted Fourier space",
  "Primary proof source lines171–245 read: original Gaussian polynomial, Poisson parity, kernel bounds, Phi(u)=2k(2u), factors2,4,8 and fullFourier representation. Kernel and exact32pi norm proof independently reproduced here.",None),
 ("cqNS2026-actual-witness",ROOT/"sources"/"flow_007"/"navier-stokes.pdf",
  "OpenAI","Finite time blowup for Navier–Stokes",
  "166-page revision with SHA0e779481...: complete printed/PDF pages6,7,115,118,119,120,121,124,125 read directly, including sums9.21, cutoff10.4,force10.5, smooth extension10.11, energy10.13–14, sample10.20–21, viscosity10.22–23. Complete source existence/correction theorem imported; not all166 pages independently verified.",
  "https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf"),
 ("cqNSFormalDefinition",Path(r"[local]/Documents\math\output\navier_stokes_research_2026-09-08\lanes\web_bundle_audit\coordination\claimed_proof\formal_inventory\full_source\NavierStokesAndEuler-8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538\NavierStokes\R3\ProblemStatement.lean"),
  "OpenAI","NavierStokesAndEuler: whole-space problem statement",
  "Commit 8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538, lines55–62 and following solution definitions: ordinary Laplacian with term -nu Delta, compact force support, energy and initial conditions. Source read, no Lean launch or kernel-verification claim.",
  "https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/R3/ProblemStatement.lean")
]

def digest(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda:f.read(1<<20),b""):
            h.update(block)
    return h.hexdigest()

records=[]
private=[]
for key,path,authors,title,locator,url in SOURCES:
    records.append({"id":key,"authors":authors,"title":title,"sha256":digest(path),
                    "bytes":path.stat().st_size,"read_locator":locator,"url":url,
                    "evidence":"primary content read; routing metadata was not used as mathematical evidence"})
    private.append({"id":key,"absolute_path":str(path)})

online = json.loads((ROOT/"sources"/"topology_followup"/"online_primary_receipt.json").read_text(encoding="utf-8"))
for edition in online:
    if edition["id"] not in ("ccm_v1_tex", "ccm_v2_tex"):
        continue
    member = edition if edition["id"] == "ccm_v1_tex" else edition["members"][0]
    records.append({"id":edition["id"],
        "authors":"Alain Connes; Caterina Consani; Henri Moscovici",
        "title":"Zeta zeros and prolate wave operators: Semilocal adelic operators",
        "url":edition["url"], "container_sha256":edition["sha256"],
        "primary_tex_sha256":member.get("tex_sha256",member.get("sha256")),
        "read_locator":("Primary TeX lines 683–704, Proposition 3.9" if edition["id"] == "ccm_v1_tex"
                        else "mainc2m24fine.tex lines 668–689, Proposition 3.6"),
        "evidence":"Primary mathematical clauses read directly; topology unspecified in both editions",
        "retrieved_utc":edition["retrieved_utc"]})

claims=[
 ("CQ-001","Polynomial trace image is exactly C[s]Xi, with the actual closure retained","proved_from_primary_polynomial_degrees","sec:cq-source"),
 ("CQ-002","Source S spectrum is the nontrivial zeta-zero parameters","imported_primary_theorem","eq:cq-source-spectrum"),
 ("CQ-003","Entire functions of order at most one admit an all-complex-time invertible heat map with coefficient -1/4","proved","thm:cq-heat"),
 ("CQ-004","Actual source topology and closed image transport to a homeomorphic quotient","proved_without_identifying_source_topology","eq:cq-Qt"),
 ("CQ-005","Original s spectrum is retained by B_t=s-(t/2)D","proved_using_imported_source_spectrum","thm:cq-moving"),
 ("CQ-006","Full associative transported product is sum (-t/2)^n f^(n)g^(n)/n!","proved_with_convergence","eq:cq-star"),
 ("CQ-007","Actual transported trace image has no common point-evaluation zero at every nonzero t","proved_without_identifying_source_topology","sec:cq-moving"),
 ("CQ-008","Derivative correspondence has full domain and exact fibres [D^k f]+(D^kN+N)/N","proved","eq:cq-relation"),
 ("CQ-009","Correlated source jet quotient is Q_ar plus explicitly topologized residual copies","proved","eq:cq-jetextension"),
 ("CQ-010","Compact-open and growth closures both equal Xi E, with continuous entire division proved by a Jensen–Poisson bound","proved_with_retained_growth_constants","thm:cq-equalclosures"),
 ("CQ-011","Compact analytic divisor quotient has original-coordinate spectrum and all local multiplicity jets","proved","thm:cq-compact"),
 ("CQ-012","D, D² and all nonzero heat times fail frozen invariance in explicit compact and growth topologies","proved_without_simple_zero_or_RH_assumption","thm:cq-obstruction"),
 ("CQ-013","Source/analytic comparison is a continuous span with exact kernels; sum quotient only asserted algebraically from each endpoint","proved","eq:cq-span"),
 ("CQ-014","Two-sheet source extension retains trace kernel and exact r and s spectra","proved","eq:cq-rspec"),
 ("CQ-015","Punctured-cover connection, commutator and maximal holomorphic iterated domains at branch are explicit","proved","eq:cq-branchdomain"),
 ("CQ-016","Z_t(0)>0 for every real t, so actual real heat divisor avoids s=0","proved_from_retained_positive_kernel","sec:cq-cover"),
 ("CQ-017","Compact tests enter the arithmetic quotient via Fourier transform with exact heat G_t=e^(tu²/4) and coordinate T_t=-iD_u+itu/2","proved_with_exact_ingress_kernels","eq:cq-testheat"),
 ("CQ-018","Transported test differential factors and root inverse have exact weighted-moment images and integral inverses","proved","eq:cq-testinverse"),
 ("CQ-019","All derivative relation domains in Xi E have exact multiplicity and local-unit Taylor constraints; finite ambiguity projections have dimension min(k,m)","proved_including_k_greater_than_m","eq:cq-Ik"),
 ("CQ-020","Analytically transported relation is the principal ideal Z_t star_t E, with explicit continuous inverse","proved","eq:cq-starideal"),
 ("CQ-021","Every heated finite Hermite trace has a unique rapidly decreasing-at-infinity Moebius inverse and exact Mellin poles","proved_with_absolute_convergence_and_domains","eq:cq-moebius-inverse"),
 ("CQ-022","For every nonzero heat time some finite Hermite seed has a Moebius inverse unbounded at the origin","proved_without_assuming_simple_zeros","eq:cq-moebius-pole"),
 ("CQ-023","Compact quotient has its exact jet-image topology and full product completion; growth quotient is complete and comparison inverse is discontinuous","proved_with_explicit_Cauchy_sequence_and_seminorm_bounds","thm:cq-jet-topology"),
 ("CQ-024","Actual source coordinate has exact algebraic kernel/cokernel and division-splitting formulas","proved_without_identifying_source_topology","eq:cq-source-kercoker"),
 ("CQ-025","Source D and heat-generator invariance are equivalent; one forward nonzero heat inclusion forces every coordinate shift algebraically onto","proved_exact_implications_not_asserted_inclusions","eq:cq-source-D-equivalence"),
 ("CQ-026","Full even Schwartz trace has all original zeta-zero multiplicity jets; its order-at-most-one intersection lies in Xi E","proved_with_actual_Mellin_half_plane_and_zero_conditions","eq:cq-fulltrace-jets"),
 ("CQ-027","Arithmetic principal-parts map has kernel Xi E, exact finite images, completed topology and retained spectral blocks","proved_with_all_local_units_factorials_and_powers_of_i","eq:cq-principalparts"),
 ("CQ-028","Every finite derivative-ambiguity image is precisely the arithmetic principal parts of pole order at most min(k,m)","proved","eq:cq-principal-ambiguity"),
 ("CQ-029","Even Schwartz Mellin transform is a homeomorphism onto the specified meromorphic finite-strip space, with exact inverse and all Taylor residues","proved_with_contour_orientation_and_all_seminorm_estimates","eq:cq-Mellin-isomorphism"),
 ("CQ-030","Schwartz trace intersection has exact zeta-divided Mellin membership, all origin Taylor data and analytic closures Xi E","proved_with_all_trivial_zero_residues","eq:cq-exact-Schwartz-trace-image"),
 ("CQ-031","Xi exp(as) has an original even Schwartz preimage exactly for |Re a|<pi/4; unique input and source scaling generator are explicit","proved_including_both_boundary_lines","eq:cq-exponential-Schwartz-domain"),
 ("CQ-032","Arithmetic meromorphic numerator space is homeomorphic to the original entire growth space and carries the exact all-time zeta heat connection","proved_with_full_cross_terms_and_source_quotient_transport","eq:cq-meromorphic-heat"),
 ("CQ-033","Zeta heat cancels all apparent higher poles and has exact entire-time numerator jets and principal-part evolution","proved_with_actual_multiplicities_and_local_units","eq:cq-meromorphic-principal-evolution"),
 ("CQ-034","Heat retains a Schwartz arithmetic input on exactly the calculated zero-jet and strip domain, proper at every nonzero time","proved_with_unique_inverse_Mellin_reconstruction","eq:cq-meromorphic-Schwartz-heat-equivalence"),
 ("CQ-035","Specified source Sobolev trace annihilator is the closed span of critical-line log-monomial characters with strict weighted degree bound","imported_primary_theorem_with_direct_cutoff_verification","eq:cq-sobolev-source-annihilator"),
 ("CQ-036","Compact tests map densely to the source Sobolev cokernel with exact truncated-real-jet kernel and retained iD1-to-s sign","proved_from_explicitly_imported_annihilator","thm:cq-sobolev-ingress"),
 ("CQ-037","Actual unnamed source quotient and Sobolev quotient have a common test-space comparison with exact two kernels; adelic even-input trace is exactly twice the original trace","proved_with_norm_one_idele_representatives","eq:cq-sobolev-source-span"),
 ("CQ-038","The full even-derivative and all-time heat cores of Xi E are zero; no nonzero invariant linear subspace exists inside this analytic relation","proved_with_actual_multiplicities_period_groups_and_retained_Hadamard_product","eq:cq-persistent-core-zero"),
 ("CQ-039","For every set of heat times with a finite accumulation point, the intersection of the inverse transported analytic relations is zero","proved_by_entire_time_jets_and_zero_core","eq:cq-accumulating-heat-times"),
 ("CQ-040","Each nonzero entire input returns to the analytic relation or original Schwartz trace intersection only at a closed discrete set of times","proved_without_RH_or_simple_zero_assumption","eq:cq-Schwartz-discrete-returns"),
 ("CQ-041","The original four-term xi4 coefficient is nonzero, commutes exactly with heat, and has discrete arithmetic return times with all incidence cases retained","proved_from_complete_Fourier_multiplier_and_positive_value_at_zero","eq:cq-xi4-arithmetic-return-times"),
 ("CQ-042","The retained Cartesian bilaplacian has all four computed coefficients and exact scaled residue 36h'(0)+(15/16)h''(0), with the original xi4 shifts and incidence retained","proved_by_full_polynomial_chain_rule_and_exact_curve_limits","eq:cq-retained-spatial-residue"),
 ("CQ-043","The bilaplacian residue on every actual source class has full complex ambiguity; its zero-residue quotient with the explicit quotient topology is homeomorphic to the actual source quotient","proved_without_source_continuity_assumption","eq:cq-source-residue-reduced-quotient"),
 ("CQ-044","Every finite origin jet is realized by an explicit original polynomial trace; its complete section, quotient topology and growth decomposition are proved","proved_with_reciprocal_Xi_coefficients_and_all_factorials","eq:cq-origin-jet-section"),
 ("CQ-045","At every nonzero complex heat time, the actual transported polynomial traces realize every finite derivative jet at any single point","proved_with_full_normal_order_correction_and_nonzero_polynomial_obstruction","eq:cq-moving-finite-jet-image"),
 ("CQ-046","The original fixed spatial residue has full complex ambiguity on every actual moving quotient at every complex time, with a finite trace section and exact quotient topology","proved_including_time_zero_and_all_finite_jet_pivot_sections","eq:cq-all-times-residue-source-quotient"),
 ("CQ-047","The transported spatial residue has its convergent derivative series and heat-conjugate source quotient homeomorphism","proved_with_original_heat_sign_and_quotient_topology","eq:cq-transported-spatial-residue"),
 ("CQ-048","The generator parity JKJ=epsilon K determines the full complex-time reflection, with exact spectral domains and the zero Cartan logarithm slice stated on the whole Hilbert space","proved","eq:cq-cartan-parity"),
 ("CQ-049","The retained heat multiplier has a modular double with explicit standard closed real subspace, canonical Tomita involution and negative-time domains","proved_with_graph_and_polar_decomposition","eq:cq-standard-real-heat-space"),
 ("CQ-050","The exact conjugate moving source quotients carry the antilinear reversal and the Fourier ingress diagram with both exact kernels","proved_without_source_topology_identification_or_Hilbert_quotient_assumption","eq:cq-actual-quotient-test-diagram"),
 ("CQ-051","Positive Euclidean viscosity is intertwined with the threefold original heat multiplier at t=-4nu theta, retaining Fourier constants and the inverse domain","proved_with_closed_L2_domains","eq:cq-viscosity-Fourier-intertwiner"),
 ("CQ-052","The retained spatial section gives the exact continuous splitting and compressed diffusion (1/4)D²+4D","proved_with_original_Cartesian_polynomial","eq:cq-spatial-compression"),
 ("CQ-053","The complete diffusion leakage has kernel exactly constants and the correctly typed derivative commutator vanishes exactly on affine entire inputs","proved_with_full_Taylor_coefficients","eq:cq-spatial-commutator"),
 ("CQ-054","The spatial second diffusion returns the exact missed component (36s²+32)D²+24sD, and the scalar viscous residual retains all original coefficients","proved_by_full_Cartesian_differentiation","eq:cq-spatial-second-feedback"),
 ("CQ-055","The original full spatial target has exact inverse differential and the smooth compactly supported incompressible input has a proved real volume-preserving flow with inverse and support control","proved_with_original_coordinates_and_orientation","eq:cq-NS-flow-support"),
 ("CQ-056","The actual arithmetic profiles retain a full fibre inverse, both timegenerators, all momentum/Hessian terms, and the complete material metric Laplacian","proved_with_all_heat_coefficients_and_viscosity","eq:cq-NS-material-viscous-residual"),
 ("CQ-057","The two original arithmetic Fourier profiles have exact positive32pi derivative norm integrals and inverse velocity recovery transferring L2energy and spatial supremum together","proved_with_full_four_term_multiplier","eq:cq-NS-exact-velocity-recovery"),
 ("CQ-058","The cited public Theorem1.1 gives actual arithmetic temporal defects with bounded jointL2 norm and unbounded spatial-supremum norm, at explicit Newman time zero","proved_transfer_using_explicitly_imported_public_existence","eq:cq-NS-public-arithmetic-blowup"),
 ("CQ-059","The actual cutoff-summed public witness and unchanged viscosity map give a whole arithmetic profile combination with its original swirl remainder and explicit quantitative lower bound","proved_transfer_from_read_public_source_equations","eq:cq-nw:profileblowup"),
 ("CQ-060","The actual force bound gives a Lipschitz terminal arithmetic profile, a measure-preserving almost-everywhere terminal flow and a strong Koopman isometry with exact adjoint range projection","proved_without_terminal_surjectivity_assumption","eq:cq-nw:terminalrate"),
 ("CQ-061","The translated heat source quotient has exact spectral conjugacy; its Xi profile class is zero and temporal defect class is v[Xi'] with an explicit scalar kernel","proved_without_frozen_descent_assumption","eq:cq-flow-source-beta"),
 ("CQ-062","The common quotient by N intersect XiE has continuous maps with exact kernels to source and analytic quotients and a complemented velocity line recovered by original residue/multiplicity","proved_with_join_topology_and_complete_division_kernel","eq:cq-flow-meet-projection"),
 ("CQ-063","The full logarithmic connection is flat off its actual divisor; its temporal residues recover velocity and preserve the exact energy and supremum comparison","proved_with_full_analytic_unit_and_divisor_orientation","eq:cq-flow-temporal-residue"),
 ("CQ-064","The actual published swirl sample produces residue m_lambda sqrt(nu) tau^(-1/2-h)(e0+R*) with explicit diverging lower bound and bounded spatial residue energy","proved_transfer_of_actual_imported_witness_with_full_remainder","eq:cq-actual-witness-residue-growth"),
 ("CQ-065","The translated modular double retains the actual real flow shifts and reverses the heat parameter with exact source and conjugate-source quotient maps","proved_with_all_complex_parameter_signs","eq:cq-flow-translated-cartan"),
 ("CQ-066","A single frozen heat inclusion and any actual source eigenvector force arbitrarily long generalized chains; the separate Sobolev block is explicitly finite","proved_algebraic_incompatibility_without_asserting_missing_source_block","eq:cq-source-surjective-chain"),
 ("CQ-067","An explicit continuous principal-part Weyl model has the actual zero spectrum and geometric multiplicity one while every spectral shift is onto; actual source inverse at zero yields only the displayed saturation","proved_with_full_resolvent_and_counterexample_scope","eq:cq-source-model-spectrum"),
 ("CQ-I01","The public manuscript Theorem1.1 is the imported existence input for the new actual-witness arithmetic propagation; two PDF revisions and the source pin are recorded distinctly","imported_public_source_theorem_not_independently_verified_here","sec:cq-public-NS-source"),
 ("CQ-U01","Identification of named source topology with compact-open or explicit growth topology","not_established_in_inspected_sources","sec:cq-source"),
 ("CQ-U02","D or D² invariance of the actual frozen source closure with unnamed topology","not_decided; exact obstruction and source-independent transport proved","sec:cq-analytic"),
 ("CQ-U03","Off-critical zeta zero, negative full Weil value, or RH endpoint","not_claimed","sec:cq-source"),
 ("CQ-U04","The bounded inspected passages and explicit term searches in Connes Selecta did not locate the CCM entire-function topology tau; actual page and extraction locators were corrected and verified","bounded_audit_no_identification_found_not_universal_absence_proof","sec:cq-source")
]
now=datetime.now(timezone.utc).isoformat()
(ROOT/"sources"/"provenance.json").write_text(json.dumps({"schema_version":1,"recorded_utc":now,
 "sources":records,"routing":"Existing literature_index_entrypoint.json and query_corpus.py used with bounded queries. No index rebuilt.",
 "topology_audit":"CCM author proof p.19 and both primary arXiv TeX editions name the Hadamard topological ring without seminorms or convergence criterion; CM Proposition 2.24 proves polynomial image and discusses multiple realizations, without specifying that topology. Following CM Section 9 and Connes's original paper supplies a specified weighted Hilbert cokernel and a proved common-test morphism, without identifying the topology on the entire-function ring. The bounded Selecta inspection locates the adele topological-ring phrase, weighted Hilbert norms, and Bruhat–Schwartz inductive-limit topology. Explicit term searches and inspected passages did not locate the CCM entire-function topology tau; this is not an exhaustive absence proof. Corrected extraction counts and verified page locators are in checks/ns_cartan_006/topology_locator_correction.md. CM theorem p.408 has a multiplicity-fraction discrepancy; its proof and the original Connes theorem agree with the directly verified strict degree bound. Bounded primary audits are retained privately; no final publisher byte-identity claim.",
 "redistribution":"Primary texts and private paths are not dependencies of the shareable manuscript."},indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
(ROOT/"sources"/"private_source_paths.json").write_text(json.dumps(private,indent=2)+"\n",encoding="utf-8")
(ROOT/"claims.json").write_text(json.dumps({"schema_version":1,"recorded_utc":now,
 "claims":[dict(zip(("id","claim","proof_status","tex_locator"),c)) for c in claims],
 "checks":"checks/verification_receipt.json","all_new_mathematical_claims_have_written_proofs":True,
 "imported_arithmetic_input_is_explicit":True},indent=2)+"\n",encoding="utf-8")
print(json.dumps({"source_receipts":len(records),"claims":len(claims)}))
