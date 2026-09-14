# Parallel formalization handoff: all-holonomy source descent

13 September 2026. New analytic/algebraic continuation; no Lean execution is claimed. Read against GitHub main `789339c2daff74167224a7bdd665879910c168fc`. Do not modify another session's workbench or silently replace any original source interface.

## Inputs retained

Use the existing SplitZero scalar, original internal quotient, fixed-index reconstruction, and actual relation map. In a coefficient fibre, keep a surjective J:P_N -> E, an injective B with range ker J, the original positive source Gram M, and C=M^{-1}J*(JM^{-1}J*)^{-1}. The arithmetic specialization uses E=C[S]/chi, B=multiplication by the literal chi, original source V_h,k, the complete Taylor unit in eta, and g=2xi. Do not substitute chi^r for the contracted higher ideal.

The marked base retains G(Z)->Z with infinite target. On each label, f lifts as (ell,v)->(ell,fv); an original relation goes to (ell,0), external absence to tau. Fourier integrals are performed in coefficient fibres and then lifted, not postulated as operations on arbitrary semimodule totals.

## Highest-priority finite targets

1. **Exact quotient-mean defect (H24–H28).** For positive matrices M_j and weights a_j>0 summing to 1, let M=sum a_j M_j. Let C,C_j be the canonical right inverses of the SAME J and G,G_j their Grams. Construct X_j=(B*M_j B)^{-1}B*M_j C. Prove C-C_j=B X_j and G=sum a_j G_j+sum a_j X_j*(B*M_j B)X_j. This uses actual relation columns, not an assumed error term.

2. **Sharp quadratic comparison (H32–H38).** From mean M and (1-eta)M<=M_j<=(1+eta)M, eta<1, derive (1-eta^2)G<=sum a_jG_j<=G. The proof first establishes the inverse chord with its exact scalar remainder, then averages K_j=J M_j^{-1}J*, then uses positivity of [[K_j,I],[I,G_j]]. The constant is sharp. A general asymmetric version is ab/(a+b-1), under aM<=M_j<=bM, 0<a<=1<=b.

3. **Equal-jet descent complex (H29–H31).** P_eq={(P_j):JP_j independent of j}. The diagonal [B->P] -> [B^m->P_eq] has average as a left inverse. Its complement is [B^0 --I--> B^0], B^0=sum-zero tuples. Give both inverse coordinate maps and the identity contraction. Preserve the degree shift and support labels. At finite polynomial cutoff multiplication by S maps degree N to N+1; do not package it as an endomorphism of the truncated source.

4. **Finite cyclic cover (H18–H23).** Retain 1/m and sqrt(m) in projectors and the isometry. On Laurent coordinate rings use z->w^m, with full rank-m module and the z factor when character products wrap past m. All projectors sum to the identity; none is relabelled as the scalar e. This gives an exact algebraic target independently of the analytic integral.

5. **Metric-to-residue coefficient transfer (H57–H61).** For fixed nonzero proper invariant F, c_F(M) is the quotient norm of [1] times the restricted dual-residue norm. Under aG<=H<=bG, prove (a/b)c_F(G)<=c_F(H)<=(b/a)c_F(G). Apply a=1-eta^2,b=1. This controls a coupling; it does not reverse into a global volume estimate.

6. **Endpoint error.** From aG_N<=H_N<=bG_N at all four original endpoints, prove absolute four-volume error <=2q log(b/a). Use a=1-eta^2,b=1 for the exact phase mean, or the explicitly supplied finite quadrature/truncation factors. The threshold-four argument is inherited and not reproved as a new theorem.

## Written analytic additions

- All-phase Bloch–Zak transform and explicit inverse (H11–H17) on the original half-density tensor source, retaining every relative variable and the zero Fourier mode.
- Uniform phase Gram estimate from the original weighted correlation matrices (H39–H41).
- Holomorphic Schur extension of the quotient metric and exponentially convergent trapezoid quadrature (H49a–H49g). This is a holomorphic coefficient extension, not a Hermitian Gram at complex phase. The bound includes all inversions and the original source conditioning.
- Uniform shifted-frequency tail with J-1, not J (H50–H52).
- Fixed-phase completed quotient and its explicit full-jet kernel. Completing those phase quotients and then taking their direct integral yields zero almost everywhere; this is not the finite full-jet descent complex or the original strong-Schwartz quotient.

These are complete written proofs in NOTE.md/NOTE.tex. The finite Python tests do not certify their analytic convergence or the arithmetic weighted integrals.

## What the source corrections change

The uploaded dated correction resolves Weil II's final citation as Roman (I.8.11), pointing to Weil I. Retain strict <2, the tensor square of the same eigenvalue, and the lisse/mixed hypotheses. The supplied split sidebar gives disjoint inverse images of absence and of supported zero. The translation note retains its exponential scalar and the marked arithmetic fibre a=0. The new pasted residue note supplies exact rank-one transverse motion; that result is inherited, not claimed as new here.

## Quantitative boundary

No bound on the growth of the original weighted-source constants kappa_{a,N} or H_{p,N} is proved. No upper bound contradicting the quartet volume threshold is proved. What is new is an exact recovery of the source using all phases, an explicitly supported gluing norm, its sharp quadratic relative bound, and a finite exponentially convergent calculation of the phasewise quotient mean. The same support, quotient, operator and metric remain in each formula.

## Executed verification

22 exact finite methods passed normally and under python -O with identical JSON records. Three formula-negative controls failed in each mode. The predecessor ZIP's 33 manifest entries verified; its 16-method checker passed both modes. No new Lean build. Browser inspection checked native MathML at desktop and mobile widths; no external scripts or bundled fonts.
