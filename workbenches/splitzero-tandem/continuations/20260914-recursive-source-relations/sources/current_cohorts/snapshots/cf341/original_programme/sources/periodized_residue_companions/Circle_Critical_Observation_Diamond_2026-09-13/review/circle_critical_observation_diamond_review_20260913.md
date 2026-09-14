# Independent complete-source review of DC1–30

Reviewer: /root/deligne_sidebar_review/circle_critical_algebra_review

Date: 13 September 2026

Status: accepted after the source corrections described below. No mathematical defect remains in the reviewed DC1–30 source. This is a written mathematical review of the exact observation diamond and its period transport. It makes no claim to have proved RH or an arithmetic upper estimate.

## Exact source and reading scope

The reviewed source is:

workspace:/work/circle_critical_observation_diamond_20260913.tex

Final accepted SHA256:

f3ec0cb1fa1f3213281029787849688346afd3dc08ec6ef36f9308022bee7fe1

Final source size: 26386 bytes.

I read the entire actual source, including every definition, displayed equation DC1–30, proof paragraph, endpoint statement, and the concluding supported Split-Zero maps. This final complete read followed complete reads of the DC1–28 draft and the first DC1–30 revision. The final complete read used the actual file after the author announced the hash above; acceptance is tied to these bytes, rather than to an earlier derivation or an abstract description of the result.

The two dependency pins in the source were independently checked against the actual files:

- Periodized source NOTE.tex, SHA256 acf63a56d5f50cfaa23f57ee52a66df261ec241ce13fd81ccac39a3bbbddd3ff.
- Period-critical bridge, SHA256 7a7733e0d6910398b6de716604a82ef5287a55002e1874327490a70ccc3dd414.

For this review I also read the actual dependency passages containing the original Fourier convention, logarithmic generator, Fourier coefficients and amplitude identity (P8–18 and P26–26b); the positive-weight circle quotient and support modification (P53–58); and the critical derivative retraction, original local units, period equation and tensor injection/retraction (the relevant PC12–36 passages). This was a targeted check of those dependencies. The complete-source read claimed here is the DC source; this review does not claim a fresh complete read of all P1–64 or all PC1–41.

An additional independent algebra check was delegated to /root/deligne_sidebar_review/circle_critical_algebra_review/local_divisor_diamond_check before the draft was read. That derivation independently confirmed the fibre-product signs, local exponents, factorization directions, weighted-image typing, and squarefree extra-circle decomposition. Its task was an algebraic derivation; it is not represented as another complete DC source read.

## DC1–5: full cyclic multiplicities and the actual critical image

The maximum over ordered tuples is the exact nilpotence calculation. On a tuple block the term of degree D=sum_i(m_i-1) has coefficient D!/product_i(m_i-1)! on the sole top monomial. The coefficient is nonzero over C; every higher power vanishes. Taking the maximum only over literally equal sums therefore gives the stated full ambient multiplicity. Restricting the tuples to critical roots gives exponents r_lambda between zero and m_lambda and the divisor a of chi.

The original nonempty packet is explicitly retained, so q=deg chi is at least one and the later top-coefficient functional is defined.

The source retains the exact type-changing map iota_1 and its tensor inverse. In particular eta_k=M_(upsilon_h tensor k) alpha_k equals eta_h tensor k composed with bar-alpha_k with its stated codomain. The tensor arithmetic unit is not asserted to be a scalar unit in the sum-cyclic quotient.

The actual critical image is W_a=im C. The inverse of j_a has the correct domain W_a: R_c tensor k first takes this image into im alpha_c,k, where alpha_c,k inverse is defined. The identity R_c tensor k C=alpha_c,k pi_a proves both sides of the inverse. This uses the actual continuous retraction in PC32, so it does not assume preservation of arbitrary exact sequences by completion.

The local derivative factors i^(-j)/j! and inverse units with identity e_c are retained. The multiplication identity on the original critical ideal is epsilon_c upsilon_c=e_c. The result concerns finite-dimensional R-modules and requires no multiplication on the ambient critical quotient.

The source quotient map now has its full name and type q_B:B→B/Theta V, avoiding a collision with the integer q=deg chi.

## DC6–8: original circle amplitude, quotient and zero target

The Fourier sign agrees with the original transform: the source generator becomes k/2+iu, and the circle basis is L^(-1/2) exp(-2 pi i n r/L). Therefore the coefficient is exactly L^(-1/2) beta_n P(S_n), with S_n=k/2+2 pi i n/L.

The identity norm(beta_n)^2=2 pi m_h,k(2 pi n/L) gives the exact squared coordinate weight nu_n=(2 pi/L)m_h,k(2 pi n/L). No coefficient vector or weight is normalized. The scalar-to-vector map is an isometry for this specified weighted norm.

The quotient proof divides a vector vanishing at retained atoms by chi away from those atoms and approximates it in the original weighted space with weight |chi|^2 nu. The exponential-moment density argument in the dependency applies after this polynomial weight. Multiplication by chi returns convergence in the original norm. Thus the relation closure is exactly the vanishing subspace, and the quotient norm is the displayed finite weighted sum.

Distinct frequencies give squarefree b dividing chi. The displayed interpolation inverse of j_b has nonzero denominators and attains every finite retained coordinate vector. Its kernel is exactly K_b.

The empty retained set is explicitly handled: b=1, W_b=0, the interpolation sum is zero, and the squared norm of j_b[1] is zero. The final source says that sum is positive exactly for a nonempty retained set.

For k=1, the support restriction is preserved. The new full-order argument proves that it removes no sampled selected root: after dividing g and h by the same exact factor (s-rho)^m, the quotient v_h(rho)=g_rho(rho)/h_rho(rho) is nonzero. The exact sampled weight is |v_h(rho)|^2/L. This argument requires no positivity at unrelated lattice atoms.

## DC9–15: joint image, common quotient and exact signs

All gcds and lcms are monic. The maps f_a=pi_d^a j_a inverse and f_b=pi_d^b j_b inverse undo precisely the specified observation embeddings; their common composite is the original reduction pi_d. They are defined on the actual images, not unspecified ambient spaces.

For compatible representatives with Y-X=dT, the draft's Bezout convention is u a'+v b'=1. The formula P=X+a u T then gives P-Y=-b v T. This verifies the two residues with the exact displayed signs. Two solutions differ by a multiple of both a and b, hence by l. This proves surjectivity, injectivity and well-definedness of the induced isomorphism E_l→W_vee.

The difference map E_a plus E_b→E_d is onto because either reduction onto E_d is onto. Its kernel is the joint image. Transport through j_a and j_b retains the original weights.

The kernel identities K_a intersection K_b=K_l and K_a+K_b=K_d follow respectively from divisibility and Bezout. The kernel sequence uses z→(z,-z) and (x,y)→x+y; those signs are consistent.

The universality statement now explicitly uses linear maps. Their common composite vanishes on K_a+K_b, so the factor through E_d exists and is unique. Surjectivity of the original maps proves the two required factorization equalities. Intertwining of the induced map follows from the same surjectivity. This proves the precise source-compatible common-quotient assertion.

## DC16–21: every local cofactor and both factorization directions

At lambda the retained coordinate is x=S-lambda and the action remains lambda+x. For each divisor s the literal factorization s(lambda+x)=x^e s_lambda_unit(x) is retained. The local kernel injection multiplies by the full x^e s_lambda_unit(x). Multiplication by the recursively inverted unit and cancellation of x^e proves injectivity; the image is the exact local kernel ideal.

This verifies the min/max quotient lengths and all complementary kernel lengths, including exponents zero and m_lambda. It does not replace the original global ideal injection by an unweighted multiplication map.

The circle observer factors through the critical observer exactly when b divides a. Necessity follows by applying a factorization to the class of a, and sufficiency is j_b pi_b^a j_a inverse. The reverse factorization exists exactly when a divides b. Uniqueness is only asserted on the actual image, where surjectivity proves it. The reverse direction therefore requires all retained critical exponents to be at most one and all corresponding roots to be sampled.

The residue-generated ideals [a]_b E_b and [b]_a E_a in DC20 have unambiguous domains even when neither polynomial divides the other. Their dimensions are deg b-deg d and deg a-deg d. The first is also the ideal generated by d in E_b, and the second is the ideal generated by d in E_a.

At a sampled root absent from a, the original CRT idempotent is killed by C and has the exact single circle value of DC21, with squared norm nu_n. At a shared root the circle retains the constant critical jet; the other r_lambda-1 critical jets are in C(K_b). Any excess ambient multiplicity m_lambda-r_lambda stays in both K_a and K_l there. At unsampled roots all surviving critical jets are in C(K_b). These cases exhaust the local possibilities.

The conclusion that a sampled root absent from a has a mixed or off-critical realizing tuple is an immediate consequence of the definition of a. The draft asserts no existence of such a root.

## DC22–27: same period transport and exact action defects

The unchanged period matrix has the original potential, rays, u, and increasing-power basis. Its invertibility and equation Pi'=-Pi(A+t e_0 ell)/u are the stated PC dependencies.

The final source explicitly uses four formal observation roles with assigned divisors a,b,d,l. Thus equal divisor polynomials do not identify W_a, W_b, E_d or W_vee, or their specified maps. This matters at endpoints and when a=b=d=l.

The kernel identity ker(T_s Pi inverse)=Pi K_s and the holomorphic right inverse are valid. For the zero target the right inverse is the unique zero map. The intersection and sum identities follow by the same invertible transport.

For B_t=Pi A Pi inverse, the entire diagram intertwines the R-actions exactly. For A_t_per=Pi(A+t e_0 ell)Pi inverse, direct multiplication gives

T_s,t A_t_per-M_s T_s,t
=t T_s(e_0) ell Pi inverse.

The source retains all four actual target vectors, including C(e_0), its raw unit-weighted derivative recovery, and the unscaled circle vector with its original norm.

For every monic v dividing chi with degree below q, the ideal basis v,Sv,...,S^(q-deg v-1)v is independent by leading degrees and spans by division by chi/v. Its final leading coefficient is one, proving ell|K_v is onto. Thus the restricted defect has rank one exactly when t is nonzero, deg s>0 and deg v<q. Its range and kernel are precisely the two subspaces in DC27. In that case the kernel dimension is q-deg v-1.

The endpoint statements are correct: v=chi gives zero domain; t=0 gives zero defect; s=1 gives zero target and zero defect. In particular the own-kernel defect has rank one exactly for t nonzero and 0<deg s<q.

The proof also correctly covers crossed kernels and keeps their original observation images. Factorization at even one period parameter is equivalent to original factorization because Pi is invertible. The common reductions take the two defects to the same common defect, and the joint defect is their ordered pair.

## DC28–30: extra circle source and differential equation

Since b is squarefree, b_new=b/d is coprime to a and l=a b_new. The two coordinate cases in DC28 exhaust the sampled roots and are disjoint. At a shared root, evaluating j_a inverse is well defined because a vanishes there. Thus DC28 gives an actual-image module isomorphism W_vee→W_a plus W_new.

The metric statement preserves the entire shared weighted evaluation sum. It does not claim that the module isomorphism removes that term or preserves an arbitrarily assigned direct-sum metric.

In DC29 every a(S_n) denominator on a new root is nonzero. The interpolation denominators are nonzero by distinctness. Multiplication by a puts the class in K_a; interpolation gives the exact prescribed values at new roots and zero at shared roots. The source lift is the original V_h,k P_z, with its original cohomology inclusion sigma_h tensor k eta_k.

The empty-new-set lift is zero. For a nonempty new set the displayed polynomial already has degree at most deg a+deg b_new-1=deg l-1, hence below q. Its original coefficients a(S_n)^(-1) remain present.

For k=1 a sampled root of chi=h is itself critical, so b divides a and W_new=0. This agrees with the full-order positivity calculation after DC8.

Finally, differentiating Pi inverse gives (Pi inverse)'=(A+t e_0 ell)Pi inverse/u. Multiplication by u T_s and the original intertwining identity yield exactly DC30 with its positive right-hand sign and unchanged u and t. The common and joint equations commute with the fixed reductions by the already proved identities.

The concluding supported maps retain the specified support and send killed represented coefficients to supported zero; tau is explicitly retained. Every coefficient-kernel assertion is backed by the inclusions and maps proved in the source.

## Corrections resolved and review boundary

The final read confirmed all requested repairs: empty circle norm; typed original quotient q_B; explicit linearity in universality; nonempty packet and q at least one; unambiguous residue-generated ideals; and four formal target roles when divisors coincide. The final k=1 positivity paragraph was read in full and checked directly.

All DC1–30 claims and their proofs are accepted for the exact source hash recorded above. I did not edit the author's TeX. This review performed no tests, Lean runs, PDF builds, numerical experiments, remote writes, or publication actions. Those activities are not evidence claimed by this review.
