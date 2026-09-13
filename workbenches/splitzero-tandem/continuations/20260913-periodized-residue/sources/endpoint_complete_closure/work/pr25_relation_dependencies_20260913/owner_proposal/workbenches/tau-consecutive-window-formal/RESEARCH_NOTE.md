# Consecutive losses and the arithmetic endpoint threshold

## Source, scope, and notation

This add-only continuation starts from main 7ea0a49945390eae14d3160a5730858899768b5f. The source is the owner's arithmetic endpoint note dated 2026-09-13 and the previously supplied exact Toda and exterior formulas. NORM_REVIEW.md audits its analytic proof and establishes the comparable-window extension used below. Those analytic results have written proofs, not a new Lean certificate. The Lean files prove the finite propagation independently of assuming RH, normality of the arithmetic action, or an estimate for the quotient volume.

Keep the original packet h, g=2xi, theta source, full Taylor unit, canonical representatives R_N, and arithmetic cyclic module C[S]/chi_(h,k). Write q=dim C. The norms omega_N are the unscaled monic source norms; V_N=det G_N are its canonical quotient volumes. The phase is phi_N=sigma-partial_theta log V_N. Lambda_N below is omega_N/V_N, NOT the global theta retraction denoted Lambda in earlier notes.

## 1. Exact consecutive product

For N>=q the existing identity is

    epsilon_N^2+phi_N^2
      =(omega_(N+1)/omega_N)(1-delta_N)(delta_(N+1)^(-1)-1),
    delta_N=V_N/V_(N-1) in (0,1].

Rearrange it as

    (epsilon_N^2+phi_N^2) Lambda_N
       =Lambda_(N+1)(1-delta_N)(1-delta_(N+1)).       (1)

For n>=q and r>=1, multiplication and cancellation of positive Lambda-values gives

    product_(j<r)(epsilon_(n+j)^2+phi_(n+j)^2)
      = (omega_(n+r)V_n)/(omega_n V_(n+r))
        (1-delta_n)(1-delta_(n+r))
        product_(0<j<r)(1-delta_(n+j))^2.            (2)

Every interior contraction occurs twice. This is an exact phase-retaining identity; the Lean theorem exact_product proves its general algebraic form. In particular,

    min_(j<r) epsilon_(n+j)
       <= [(omega_(n+r)V_n)/(omega_n V_(n+r))]^(1/(2r)). (3)

The finite minimum exists. Equation (3) follows by bounding each factor 1-delta by one, comparing the product with the minimum's 2r-th power, and taking a nonnegative root. This proof does not require Jensen or the earlier four-endpoint hyperbolic-sine bound. It need not be sharper when contractions are small.

The local coarse bound epsilon_N^2 Lambda_N<=Lambda_(N+1) also holds at N=q-1. Use the separate first-degree identity

    epsilon_(q-1)^2+phi_(q-1)^2=(nu_0-omega_q)/omega_(q-1),
    V_q/V_(q-1)=omega_q/nu_0.

It follows that epsilon_(q-1)^2 Lambda_(q-1)<=Lambda_q. No inverse at degree q-2 is introduced. Thus (3) and the lower-allowance consequence below apply to windows starting at q-1, although the exact two-contraction identity (2) is used only from q onward.

## 2. The actual spectral lower allowance forces each single block

The existing original-Gram exterior/trace theorem gives L_(h,k)<=epsilon_N for every admitted N. Iterating the coarse local inequality proves

    L_(h,k)^(2r) Lambda_n <= Lambda_(n+r).          (4)

If the actual norm bound gives omega_(n+r)/omega_n<=C^(2r), then

    (L_(h,k)/C)^(2r) V_(n+r)<=V_n.                 (5)

For L>0,C>0 this is

    log(V_n/V_(n+r)) >= 2r log(L_(h,k)/C).          (6)

The formal propagation, norm comparison, and log conversion have separate declarations, so the analytic premise is explicit.

For the exact hypothetical quartet, retain

    q_k=[1+k(m-1)](k+1)^2,
    L_(h,k)>=delta*k*q_k/2, delta>0.

By NORM_REVIEW.md, both windows (n,r)=(q_k,q_k) and (q_k-1,q_k) have norm factors at most C_h q_k. Indeed q_k-1>=k for k>=3, and r is between n/2 and 2n. The first window uses only regular local degrees; the second begins at the separately checked first degree. Let D_h=delta/(2C_h)>0. Then

    log(V_(q_k)/V_(2q_k)) >= 2q_k log(D_h k),
    log(V_(q_k-1)/V_(2q_k-1)) >= 2q_k log(D_h k).  (7)

Therefore the source's SAME four-volume budget satisfies the stronger implication

    B_(h,k)=log[V_(q_k-1)V_(q_k)/(V_(2q_k-1)V_(2q_k))]
       >=4q_k log(D_h k),
    liminf B_(h,k)/(q_k log k)>=4.                 (8)

The source's threshold 2 remains correct but is not optimal after retaining the adjacency of the exact radius equations. This is a new deduction, not a correction falsely attributed to its original proof. No upper estimate below 4 is claimed. Either one-block upper limsup below 2 would already suffice for contradiction, while a total upper limsup below 4 would also suffice. Multiplicities remain in q_k.

## 3. Relation-layer meaning

For the original block (i,j), put F=[b_(i+1),...,b_j], Omega=diag(omega_(i+1),...,omega_j). The supplied map b=T-R_iF is an isomorphism onto D_j intersect D_i-perp, with Gram Omega+F*G_iF, and original quotient value zero. Hence

    V_i/V_j=det(I+Omega^(-1)F*G_iF).

Take the nonnegative generalized eigenvalues lambda_a of (F*G_iF,Omega), counted with all q multiplicities including zeros. Indeed Omega is positive definite, while F*G_iF is positive semidefinite and can have a kernel. The two blocks (q-1,2q-1) and (q,2q) each have q source coordinates. Equations (7) imply, for each block separately,

    product_(a=1..q)(1+lambda_a)>=(D_h k)^(2q),
    geometric_mean(1+lambda_a)>=(D_h k)^2,
    (1/q) sum_a lambda_a>=(D_h k)^2-1.             (9)

The arithmetic-geometric mean inequality proves the last line. This does NOT force every lambda_a to grow. Their multiplicity and rank profile remain. On the split lift the actual final quotient sends each retained relation to the receiving label's supported zero, not to external tau. Its source Gram is measured before that map.

Zero eigenvalues genuinely occur in the stated quartet family. At theta=0 the full quartet gives an even source measure. At even tensor degree k, q_k=[1+k(m-1)](k+1)^2 is odd. In u coordinates the original cyclic polynomial has reflection-symmetric roots with their full orders, hence psi(-u)=(-1)^q psi(u). The monic orthogonal source polynomials obey Q_j(-u)=(-1)^j Q_j(u), and reduction modulo the odd psi preserves parity. In the first block (q-1,2q-1), the q columns Q_q,...,Q_(2q-1) contain (q+1)/2 odd polynomials, but the odd part of C[u]/psi has dimension (q-1)/2. Thus F is singular and at least one of its q generalized eigenvalues is zero. The coordinate map S=k/2+iu and its nonzero column factors i^j preserve this rank calculation; no source unit or phase is removed. Keeping that zero in (9) preserves the determinant product and the arithmetic-geometric mean inequality because every 1+lambda_a is still strictly positive. This does not weaken either block budget or the limiting threshold four.

## 4. Constant and source accounting

No measure is normalized. The original mass omega_0=mu_h^k remains, and its effect is in the explicit constants of NORM_REVIEW.md. The Taylor multiplier and its derivative are not omitted. The norm leading-coefficient quotient is not identified with the arithmetic quotient. No complementary arithmetic block, nilpotent direction, or cochain sign is removed.

The analytic proof and the asymptotic consequence (8) are written mathematics. The new Lean run, when successful, certifies the finite local/product/forcing interfaces named in AuditConsecutiveWindow.lean; it does not certify the complex-analytic zeta argument, the arithmetic integrals, or a new weight theorem. Consult the PR for the exact completed run rather than treating this source note as an execution receipt.
