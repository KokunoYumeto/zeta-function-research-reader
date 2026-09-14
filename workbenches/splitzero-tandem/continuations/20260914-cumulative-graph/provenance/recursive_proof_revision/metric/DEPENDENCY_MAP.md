# Propagation through the arithmetic metric and endpoint calculations

All changes are in the isolated staging tree. The immutable 821-page source, current cumulative staging, published files and earlier delivery folders have not been edited. PATCH_MANIFEST.json pins each original and revised complete proof body and its literal diff.

## Exact common source

The Gamma/arithmetic comparisons in AT, AW and SP have one specified full packet h, tensor order k, original cyclic polynomial chi of degree q at least one, and coefficient space H=P_(2q). Their ordered coordinate remains S=k/2+iy, their arithmetic density remains w_h^{*k}, and their Gamma density remains r_(1/4)^{*k}. The identity c_(1/4)=sqrt(2 pi) proves the Gamma densities coincide, with their original masses. The relation map in AT/AW has codomain P_N; the map in SP is I_N B_N with codomain H. Their relation Grams and all four projectors coincide by this exact inclusion, as proved in AT4a–b, AW13a and SP1a.

The finite-circle application retains the original sampled density and all Fourier factors, including its zero mode. Its endpoint forms are instead M^(0)=M_(2q) and M^(1)=M_(2q)(L,J). The exact restriction I_(2q,D), D=2q+2, transports the proved source inequalities while the larger degree continues to control both generator raises. It does not identify a sampled density with Gamma. PSA24a–e gives the entire determinant/projection proof for those actual two forms.

## Earlier claim → revised claim → complete proof

| Earlier locus | Earlier claim | Current claim at the same proof site | Complete proof and dependencies |
| --- | --- | --- | --- |
| AT4 | Fixed Gamma density and coefficient relation map | Exact identification of Gamma constants and the I_N B_N codomain map | Added AT4a–b; direct evaluation of c_(1/4), existing full Gamma convolution identity, direct Gram substitution |
| AT18–21 | Absolute signed correction at most 2q log kappa | At most J=integral min(S_AW,S_SP), at most L_q(D), at most (2q−1) log kappa | AT18a, AT20a–c and AT20 completely prove flags, ranks, multiplicities, source projections, eigenvalue trace bounds, common-range trace norm and original cross-trace; AT21 integrates each original eigenvalue |
| AT19 | Gamma interval with radius 2q log kappa | Same signed Gamma/arithmetic interval with radius J | Exact equality AT14–15 plus both signs of AT18; all four endpoint orientations retained |
| AT22 | Quartet lower bound with coefficient 2q, and rearranged necessary condition | Same actual quartet lower bound with radius J, then full-spectrum radius, then coefficient 2q−1; necessary condition denominator becomes 2q−1 | Original Gamma theorem unchanged, literal substitution in AT19, and division by positive 2q−1 |
| AW7 | Full spectra 0^q, 1^2, 2^(q−1) | Preserved and credited as the earlier result | Original entire AW7 proof and explicit original-metric isometry AW9–10 retained unchanged |
| AW14–17 | Full-spectrum bound and coefficient 2q−1 | Same bound preceded by actual pointwise minimum J | Existing complete AW15–17 proof retained; AW16a supplies complete actual-overlap proof and integrability; AW13a supplies exact source correspondence |
| AW18 | Actual quartet bound with L_q(D) subtracted | Same bound with J subtracted, preserving its L_q and condition-number consequences | Revised AW14 and unchanged original Gamma lower bound |
| AW11–12 | Source isometry commutator and observation defect | Preserved exactly, with its use propagated into SP | Source isometry intertwines U,W; cyclic trace proves the commutator; injection of sigma tensor eta and original kernel J prove exact observation kernel |
| SP1 | Self-adjoint metric derivative | Explicit morphism from positive relative D to signed C=(I+x(D−I))^−1(D−I), preserving eigenvalue signs | Factor the literal interpolated Gram; positivity belongs to D in M_0 |
| SP8 and SP13 | Spectra and condition-number coefficient repeated | Explicit AW7/AW14 reuse attribution, with actual overlap retained as additional information | Original SP8 flag proof plus complete earlier AW proof present in the revised cumulative source |
| SP10–13 | Actual overlap bound; condition-number consequence | Actual overlap, complete full-spectrum bound, pointwise minimum before integration; exact trace-norm integral remains independently available | Added full spectral proof SP10a–c; SP11–12 integrate the same positive relative eigenvalues; no ordering of incomparable refinements assumed |
| PSA24–25 | Four quotient determinant errors bounded separately, coefficient 2q | Same original/sampled signed four-endpoint error bounded by actual J_(L,J), then full spectrum, then (2q−1) log(beta/alpha) | Full new PSA24a–e proof inside the original finite-cutoff section: exact restriction, oriented monic determinant frame, signed derivative, both projection spectra, both complete bounds, eigenvalue integration |
| FC13 following paragraph | Four-endpoint sampling bound 2q log(beta/alpha) | J_(L,J) and full relative spectrum, then coefficient 2q−1 | FC13a explicitly transports the same original/sampled Grams and relation maps to the complete PSA24a–25 proof |
| R58 | Earlier displayed finite-circle 2q bound | Full current bound and definitions inserted into the existing R58 paragraph | Complete replacement in conclusion_replacements/R58_NEW.tex; exact old source hash and locators in R58_MAP.json; full proofs PSA24a–25 and FC13a |

## Source-metric arrows retained in neighboring calculations

R50's positive relation cost is Z=(K_j−K_i)G_i on E; it retains its trace and square trace and the full q-dimensional Hermite majorant. The signed window difference A=U−W acts on H=P_(2q), has trace zero, and is paired with C=M^−1 dot M. It cannot be substituted for Z in the positive-cost majorant. The exact connection is the original quotient section R_N=M_N^−1 J_N^*G_N, satisfying J_NR_N=I and R_N^*M_NR_N=G_N; on its range the common source projection is R_NG_N^−1R_N^*M_N=P_N−Q_N. The determinant derivative is Tr((P_N−Q_N)C), which is the formula used before forming the four signed terms. This identity is proved in AT6–12 and PSA24c–d. Thus the original two-trace estimate stays valid and can be combined with the updated signed endpoint bound through their common unchanged quotient determinants.

R60/FC8–13 concerns the residue operator e_0 ell and an invariant constituent inside E. Its normalized rank-two trace has eigenvalues 1,−1,0 and its original dimension-free spectral-spread bound remains unchanged. The source embedding C_N in FC7 is the exact metric map to H; the revised FC13a explicitly records this map and keeps the residue bound distinct from the source-window bound without discarding their relation.

R61/FC24–29 concerns the two quotient forms G,H and the actual arithmetic generator A+tR−k/2. Its isometry S=(G^−1H)^(1/2):(E,H)→(E,G) and exact error S X_H S^−1−X_G=Z+Z^{dagger_G}, Z=[S,T]S^−1, remain unchanged. AW's T^iso instead acts on the common polynomial source and intertwines its two window operators. The revised SP proof retains the complete observation defect of T^iso; it does not transport a false arithmetic intertwining assertion into R61.

## Integration instructions

Replace the five complete proof files under staged/ at their matching successor-reader roles, rather than appending duplicate chapters. For the original 821-path PSA and FC chapters this means their existing tex/ paths. The source snapshot records AT/AW under tex/next_edition/, but the verified active successor master routes are tex/AT_complete.tex and tex/AW_complete.tex: apply those two revised bodies to the active routes. For SP use the current source role that includes tau_signed_projection_control_20260913.tex, preserving the original delivery as history. The builder must use its actual input graph rather than infer an active path from the historical snapshot path.

The parent owns all R-paragraph assembly and cumulative manifests. Apply R58_NEW.tex only by matching its exact original block and source hash from R58_MAP.json. The endpoint child supplies separate complete replacements for the older four-volume chapter and its central restriction/upper-bound consequences; those are not duplicate AT/AW sources.

## Second propagation: complete RMT result through the same earlier sites

The complete RMT1–18 source has now been fully read, copied with its exact pin under dependencies/, and applied in the same five earlier chapters. The generic two-Gram J bound and its full proof remain. On the actual original continuous or positive atomic moment measures only, write a=2q−1 and A(x)=a sqrt(1−exp(−B(x)/a)) d(x). Then J^(3)=integral min(S_AW,S_SP,A) is inserted before J in AT18, AW14, PSA25, FC13a and R58, and replaces the radius in AT19/22 and AW18. SP13a–c gives the corresponding actual-moment application while preserving its preceding generic positive-Gram statements.

The strict positivity needed for the nonlinear coordinate is proved on those actual measures: B=0 makes the two crossed minimum sections agree, putting 1 perpendicular to chi P_q; the reflected polynomial chi^{#_k} then forces integral |chi|^2=0, contradicting the positive Gram. The full original angle calculation, including both q-angle lists and their designated zero entry, remains in RMT and EP. No nonlinear claim for arbitrary positive coefficient matrices has been inserted.

AT19a and PSA25a insert the actual simultaneous nonlinear endpoint interval with radius I=integral min(d,S_AW/[a sqrt(1−exp(−B/a))],S_SP/[a sqrt(1−exp(−B/a))]). AW22 and AW23 now use I and I/2 in their existing q=1 nonlinear formulas, respectively, retaining the previous log-condition-number bound as a consequence. The exact map H_a(B)=2 arcosh exp(B/(2a)), derivative and inverse are written at each application.

This dependency is acyclic. RMT uses AT's early determinant derivative, AW15–17 and the complete EP angle proof. It does not use the newly strengthened AT final theorem. RMT_DEPENDENCY.json records the precise complete source and applicability. The independent reviews of the earlier two-bound cut remain as historical verification; a separate full delta review covers this recursive application.

## Final propagation: five controls and the constructed signed interval

The current v4 final-signed manifest supersedes the three-entry cut without deleting that cut. Every actual-moment J radius now retains five entries: AW full spectrum, exact trace norm, SP overlap, centered Hilbert–Schmidt variance, and the original full-angle bound. Every nonlinear I radius retains the corresponding four generic numerators and the angle-derived diameter. The generic two-Gram derivations remain written in full, and the new trace-norm/variance proofs are included at the earlier AT, AW, SP and PSA claim sites.

The complete ISM1–43 and RMT1–22 sources were fully read. The finite Neumann polynomial is constructed explicitly in AT19ba–c, AW17aa–c, SP13ea–c and PSA25ba–c: its original relative operator, midpoint scalar, commuting finite geometric sum, exact centered remainder and integrated signed center j_ell and error e_ell are all given. The error satisfies the proved fixed-source bound theta^(ell+1) sqrt(K_D(8q−6)). The finite series index ell_N preserves the original circle length L, derivative order p, exponential source parameter a, tensor order k and quotient degree q.

The actual earlier intervals AT19 and AT19a, AW18 and AW23, SP13c, PSA25a, FC13b and R58 intersect the previous absolute/nonlinear bounds with B_0+j_ell−e_ell and B_0+j_ell+e_ell. These are exact integrals; no claim of numerical integration without enclosure is made. AW22 keeps the complete five-entry I radius, and AW23 combines its nonlinear endpoint with the signed interval by explicit proof dependency. AT22 also carries the signed Gamma lower-bound branch. The five-entry and signed construction never removes either original arithmetic endpoint loss.

The exact ISM canonical projector equality Pi_N=P_N−Q_N is used with the original coefficient inclusion I_N B_N. Its primitive and proper-source residual remain the full tensor differential calculation; no proper-W boundary is declared zero merely from its full-source remainder. The earlier endpoint child supplies FV.M13–14 with the exact tensor kernel and one-leg V/W map.

## Averaged quotient scope retained

The bounded full reading of HCD9–16 and R63 confirms the exact arrow from constant-source complex to continuous common-image source by repetition. The latter minimum section is theta↦C_theta x, its quotient metric is Gbar=integral G_theta, and G−Gbar is the integral of the original relation correction norms, with both weighted cross terms retained. These additional relation fields vary with cutoff. No simultaneous finite P_2q source form realizing all four averaged quotient Grams and their original flags has been constructed in this pass. The averaged quotient 2q bound therefore remains; the eligible phasewise common-source bound is separately propagated in the HC patch. This is an exact applicability restriction, not a claim that the further bridge cannot be constructed.
