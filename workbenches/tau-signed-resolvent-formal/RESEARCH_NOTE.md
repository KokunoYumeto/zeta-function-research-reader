# Signed source resolvents and boundaries retained at a proper support

14 September 2026. This continuation follows the current source-control chapter, equations ISM1–43, at main `331ccd30185a98bfc8fde8102cf09b9c2add4d6b`. Its exact source is `workbenches/splitzero-tandem/continuations/20260914-recursive-source-relations/tex/incoming_source_metric_control.tex`, Git blob `b23bfcba6ec2dfcf35340a7d27c6f0a3145e83ea`. The complete chapter was read, not merely its handoff. The construction builds on the original canonical source/projector and quotient-kernel implementations, including corrected PR30 head `aa6473075928b0316c49d50c163697c4ab98d004`.

The mathematical targets below are written out independently of their execution status. STATUS.md identifies the exact observed successful commit, when available. This document is not an arithmetic moment certificate.

## 1. What is retained

Keep the original scalar `G(R)={tau} disjoint-union R^bullet`, with `e=0^bullet`, the infinite arithmetic map `p_Z:G(Z)->Z`, the original theta quotient, and the original full-jet observation. The source metric is supplied by the original admitted source, not optimized over an unrelated collection of positive forms. Each canonical section is the existing `Metric.sectionMap`; its correction lies in the columns of the existing original relation map.

At the common finite source, let M be positive definite. For endpoint a in {0,1,2,3}, retain its actual relation columns B_a, coefficient columns C_a, inverse relation Gram, canonical section rho_a, quotient Gram G_a and inverse K_a. The number of relation columns may differ. Define

    P_a = rho_a K_a rho_a* M,
    Q = P_0 + P_1 - P_2 - P_3.

The inherited canonical-frame theorem proves P_a^2=P_a, P_a* M=M P_a and Tr(P_a)=q. The new `canonical_properties` composes those constructions to prove

    Tr Q=0,           Q* M=M Q.                              (SR1)

No orthogonality between different source labels is inferred. In particular the full cross term in

    Tr Q^2 = Tr(P_0-P_2)^2 + Tr(P_1-P_3)^2
             + 2 Tr((P_0-P_2)(P_1-P_3))                     (SR2)

remains present. This is the inherited `contrast_square` identity, used by the new exact regressions.

For the original inverse J with MJ=I and source perturbation E, `canonical_tangent` retains the exact identity

    Tr((JE)Q) = Tr(K_0 rho_0* E rho_0)
              + Tr(K_1 rho_1* E rho_1)
              - Tr(K_2 rho_2* E rho_2)
              - Tr(K_3 rho_3* E rho_3).                     (SR3)

Thus the signed observable is attached to the actual four source-generated quotient Grams. The analytic statement identifying these tangents with derivatives of logarithmic arithmetic volumes remains the source chapter's separately proved input; no differentiation under an arithmetic integral is claimed here.

## 2. A centered signed matrix interval in this same metric

For an M-self-adjoint operator A, write

    tr_R(A)=Re Tr(A),
    center(A)=A-tr_R(A) I/n,             n=dim(source).

For M-self-adjoint A and B, the implementation proves

    |tr_R(AB)| <= sqrt(tr_R(A^2) tr_R(B^2)).                 (SR4)

This is not imposed as a field of a certificate. `MetricFrame.ofPosDef` constructs W and W^{-1} with W*W=M and both inverse laws, using the pinned Mathlib positive-factorization theorem. Conjugation A -> W A W^{-1} carries M-self-adjoint operators to Hermitian operators and preserves every product trace. The proof then applies Hilbert–Schmidt Cauchy–Schwarz and returns to the original coordinates. The isometry changes coordinates, not the specified source form or its representatives.

If X and Y are M-self-adjoint and Q satisfies SR1, define

    E_Y=center(X-Y),        Z=tr_R(Q^2).

The scalar direction cancels because Tr Q=0. The new `signed_interval`, and then `canonical_interval` on the constructed source columns, prove

    tr_R(YQ)-sqrt(tr_R(E_Y^2) Z)
       <= tr_R(XQ)
       <= tr_R(YQ)+sqrt(tr_R(E_Y^2) Z).                     (SR5)

The center tr_R(YQ) is signed. Replacing it by its absolute value would erase the cancellation that ISM27 uses.

## 3. Construct the finite resolvent and its literal remainder

In any ring, for H,T and integer L>=0, set

    S_L(H,T)=(I+H+...+H^L)T.

Whenever (I-H)X=T, the new ring theorem proves

    X-S_L(H,T)=H^(L+1)X.                                   (SR6)

The proof is the finite identity `(sum_{r<n} H^r)(I-H)=I-H^n`, proved by induction. It uses no commutation of Q with H or X. Both the constant term and the exponent L+1 are essential. At H=0, the finite sum is exactly T, even for L=0.

If H and X are self-adjoint for M and commute with each other, their product H^(L+1)X is also M-self-adjoint. The implementation proves this product and power calculation and derives self-adjointness of S_L from SR6. It does not presume that the signed source contrast Q commutes with either operator. `canonical_resolvent_interval` substitutes SR6 into SR5 with the actual canonical Q.

For the ISM endpoint construction, keep

    D=M_0^{-1}M_1,             B_x=(1-x)I+xD,
    X_x=B_x^{-1}(D-I),         a_x=(lambda_min(x)+lambda_max(x))/2,
    H_x=I-B_x/a_x,             T_x=(D-I)/a_x.

These satisfy the literal equation `(I-H_x)X_x=T_x`. Their self-adjointness and simultaneous spectral coordinates concern the original metric M_x=(1-x)M_0+xM_1. The scalar endpoint construction below proves the required bounds on those specified spectral values; the code does not assert a new arithmetic identification of M_0 or M_1.

## 4. Carry the spectral error back to the original matrices

Let b_i>0 be the complete endpoint spectrum of D, including multiplicity. On 0<=x<=1, retain

    lambda_i(x)=1-x+x b_i,
    gamma_i(x)=(b_i-1)/lambda_i(x),
    h_i(x)=1-lambda_i(x)/a_x.

The scalar theorems prove

    lambda_i(x)>=min(1,b_i)>0,
    |gamma_i(x)|<=|b_i-1|/min(1,b_i),
    |h_i(x)|<=theta=(b_max-b_min)/(b_max+b_min)<1.            (SR7)

Every inequality is proved for the fixed positive endpoint pair and all x in its closed unit interval. It is not uniform over changing packets or tensor orders.

`SplitZeroSpectralResidual` accepts the simultaneous diagonalization as explicit equations for an original-metric isometry F:

    F H F^{-1}=diag(h_i),       F X F^{-1}=diag(gamma_i).

It proves the conjugation identities, including powers, scalar centering and all traces. Therefore the actual matrix remainder R_L=H^(L+1)X has diagonal values delta_i=h_i^(L+1) gamma_i, and the actual centered matrix error E_L satisfies

    tr_R(E_L^2)=sum_i delta_i^2-(sum_i delta_i)^2/n.         (SR8)

This equality is a transported matrix calculation, not a replacement of the residual by an independently selected diagonal matrix. The diagonalizing equations are required inputs; this contribution does not construct the entire generalized-eigenvalue solver for arbitrary endpoint matrices.

Set K=sum_i (|b_i-1|/min(1,b_i))^2. The finite scalar variance theorem and SR7 give

    tr_R(E_L^2)<=theta^(2L+2) K.

The new `signed_error` composes this spectral calculation with SR4 and scalar cancellation to prove

    |tr_R(XQ)-tr_R(S_L(H,T)Q)|
       <=theta^(L+1) sqrt(K tr_R(Q^2)).                     (SR9)

The fixed-pair radius converges to zero; `exists_stopping_degree` proves a finite L exists for each positive requested tolerance. Its constants remain source-dependent. The source's sharper `8q-6` estimate for its nested projector geometry and the integration of pointwise errors can be used in the written continuation. They are not relabelled as new declarations in this five-module contribution. In particular there is no new uniform arithmetic endpoint estimate and no claim that auxiliary purity supplies one.

## 5. A full-source boundary can remain nonzero at a proper source

Let D,E be the original coefficient diagrams on the same support semilattice, f:D->E an original natural linear map, and B,C their original stable relation submodules. Assume f(B_i) is contained in C_i. Define

    K_i=f_i^{-1}(C_i),
    residual_i=K_i/B_i,
    qf_i:D_i/B_i -> E_i/C_i.

Here B_i in the denominator is its actual restricted inclusion into K_i. The existing `Homology.quotientKernelEquiv` identifies residual_i with ker(qf_i). The new module assembles these literal fibres into diagrams and constructs both natural maps and both inverse laws:

    residualDiagram <-> kernelDiagram.                    (SR10)

The transports are restrictions and quotients of the original transports. Their naturality follows from the given commuting square for f. No transport is assumed injective. Thus this construction applies even when enlarging support kills a previously retained class.

Its inclusion into the original small quotient satisfies the exact G(R)-linear square

    residualInclusion o q_residual
       = q_B o inclusion_K.                                (SR11)

Its exact total image is

    y in image(residualInclusion)
       iff qf(y)=e qf(y).                                   (SR12)

The right side is zero in the receiving support fibre. It is not qf(y)=tau. `proper_residual` separately proves that x notin B_i and f_i(x) in C_i give a nonzero small quotient class whose full comparison is its receiving fibre zero. At a nonbottom outer label, the theorem `present_empty_residual` retains `((i,empty),0) != tau`.

For the source chapter, f is the inclusion of the declared proper top source into the full top source, B_i is the admitted proper boundary image and C_i the full boundary image. Then SR10 is precisely

    (C_i intersect image(proper source))/B_i
       -> kernel(proper quotient -> full quotient),

with the pullback presentation used when the inclusion is not identified with a set inclusion. The actual tensor theta primitive and its ordered Koszul signs remain the written source data producing the full boundary; their membership in the smaller admitted boundary is not assumed. The previous checked boundary-socle, synchronization and conormal modules are imported jointly rather than replaced.

## 6. Execution and non-overlap

The new exact checker constructs non-diagonal complex source forms, full polynomial relation columns, repeated-root calibration polynomials, actual canonical sections and all four projectors. Its examples are explicitly not actual zeta packets. It checks the L+1 remainder, the centered spectral variance, source-mass scaling, mixed cross terms, scalar endpoints, proper-source kernel classes and the present-empty-face distinction. Five false formulas are required to fail; Python optimization does not remove any test.

The branch preserves main331 and corrected PR30 ancestry. The recovered suites have nine and eight methods, not the erroneous eleven/fifteen in the older summary. The corrected historical record is retained without rewriting PR30. STATUS.md reports observed counts and exact CI pins. No publication, main merge, other-branch update, analytic theta integral or general six-functor/derived-tensor theorem is part of this contribution.

## References

KokunoYumeto. (2026). *Recursive source-relations continuation: Incoming source metric control* (ISM1–43; Git revision 331ccd30185a98bfc8fde8102cf09b9c2add4d6b). zeta-function-research-reader. The mathematical source for SR1–SR12 is the pinned chapter, not its publication metadata.

The mathlib Community. (2026). *Mathlib: Matrix order, positive-definite matrices, and inner-product inequalities* (Git revision fabf563a7c95a166b8d7b6efca11c8b4dc9d911f). Primary implementation references: `Mathlib/Analysis/Matrix/Order.lean`, `Mathlib/LinearAlgebra/Matrix/PosDef.lean`, and `Mathlib/Analysis/InnerProductSpace/Basic.lean`.
