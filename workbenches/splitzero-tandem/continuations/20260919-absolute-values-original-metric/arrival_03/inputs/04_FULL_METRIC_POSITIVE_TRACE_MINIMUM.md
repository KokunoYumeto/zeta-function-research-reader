# Exact minimum of the full-packet positive weight trace

19 September 2026. This extends the archive's TC18/TC21 operator-norm optimization to the positive trace relevant to the positive-primary exterior benchmark. The earlier operator-norm infimum is not claimed again as a new result.

Retain the original full packet of tensor order k=4l+1,

    lambda_(a,b)=k/2+(2a-k)delta+i(2b-k)gamma,
    e=1+k(m0-1), q=e(k+1)^2,
    A=multiplication by S on E=C[S]/chi_k.

For a positive definite metric G in the original coordinates set

    H_G=G^(-1/2)(A*G+GA-kG)G^(-1/2),
    T_+(G)=Tr((H_G)_+).

The exact result is

    min_(G>0) T_+(G) = delta q(k+1)/2 = L_(h,k).         (M1)

This is attained with all complete nilpotent primary blocks retained.

## 1. Lower bound on the original packet

Take a complete A-invariant flag, including all generalized vectors, and orthonormalize it in G. The resulting triangular matrix for A has the original lambda's, each repeated e times, on its diagonal. The corresponding Hermitian weight matrix has diagonal values

    2(2a-k)delta.

The trace of its positive part is at least the sum of its positive diagonal entries: for the coordinate projection P onto those entries, Tr(PH)<=Tr(PH_+)<=Tr(H_+). These inequalities follow by inserting positive square roots, not from commuting P and H.

Because k is odd, the positive rows are a=(k+1)/2,...,k. Thus the sum is

    e(k+1) 2delta sum_(a=(k+1)/2)^k (2a-k)
      = e(k+1) 2delta ((k+1)/2)^2
      = delta q(k+1)/2.

This is the same spectral lower-bound argument underlying the archive's TC24–25, now applied to the positive trace without imposing the canonical rank-two condition.

## 2. An attaining metric with the full primary structure

Let C be the exact confluent CRT map from the original polynomial coordinates to the coefficient lists in (S-lambda)^r, 0<=r<e. Divided derivatives are used, so these are literal coefficients. Then

    C A C^(-1)=direct_sum_lambda (lambda I_e+J_e),

where J_e has ones on its first subdiagonal.

Put t=delta/2 and D_e=diag(1,t,...,t^(e-1)). Define the original-coordinate metric

    G_*=C* [direct_sum_lambda D_e^2] C.                (M2)

The displayed CRT map followed by the D_e blocks is an exact isometry from (E,G_*) to the ordinary coordinate sum. In that frame the Hermitian weight block is

    2(2a-k)delta I_e+t(J_e+J_e*).

Its eigenvalues are explicitly

    2(2a-k)delta+delta cos(j pi/(e+1)), 1<=j<=e.         (M3)

The sine vectors prove this tridiagonal diagonalization directly. Since |2a-k|>=1, every eigenvalue has the sign of 2a-k. The nilpotent correction has zero trace in each block. Hence summing (M3) over the positive blocks attains (M1), with no nilpotent direction removed.

Its positive and negative ranks are both q/2. The total trace is zero, and Tr|H_(G_*)|=2L_(h,k).

## 3. Realize the metric by an actual finite polynomial section

Use the original arithmetic polynomial source through N=2q-1, its Gram H_N, remainder J_N, and canonical minimum section

    R_min=H_N^(-1)J_N* G_min,
    G_min=(J_N H_N^(-1)J_N*)^(-1).

The complete relation space chi_k P_(q-1) has dimension q. Let B be an H_N-orthonormal column frame of precisely that relation space. Thus J_N B=0 and B*H_N R_min=0.

Choose the explicit positive scalar

    alpha=1+||G_*^(-1/2)G_min G_*^(-1/2)||,
    P=alpha G_*-G_min >0,

and set

    R=R_min+B P^(1/2).                                  (M4)

Then, exactly,

    J_N R=I_E,
    R*H_N R=alpha G_*.

The scale does not change H_G's spectrum. This realizes the minimum (M1) in the actual finite arithmetic polynomial presentation. Composing (M4) with the original theta-polynomial source map retains the same arithmetic quotient class. The correction is a complete original chi_k relation.

At a smaller proper source W, the archive's TC29a–d gives its nonzero possible residual: the correction changes the proper-source class by the corresponding class of its primitive in V/W. No vanishing of that proper-source residual is claimed. The construction therefore does not replace the independent PRD source metric.

## 4. Why the scalar canonical allowance is not transported unchanged

The canonical moment sequence has weight rank at most two and trace zero. Its positive trace equals its positive eigenvalue epsilon_N. That is the exact reason the archive's aggregate bound takes the scalar form epsilon_N>=L_(h,k).

For a general positive metric with positive rank r_+,

    L_(h,k)<=T_+(G)<=r_+ ||H_G||.

For the attaining metric (M2), r_+=q/2, not one. In the simple stratum its operator norm is 2k delta, while its positive trace remains L_(h,k). Using the smaller operator norm as though it were the canonical rank-two positive trace would change the quantity in the closing inequality.

Thus the full-packet trace threshold cannot be improved below L_(h,k) by any positive source metric or finite polynomial representative family. This is an optimization result on the unchanged full arithmetic packet; it does not evaluate the original projected kernel or boundary allocation, where the actual projection and both leakage terms remain.


## 5. Complete characterization of every attaining metric

Let E_+ and E_- be the original sums of all complete primary spaces with Re(lambda)>k/2 and Re(lambda)<k/2, respectively. They have dimension q/2. Write B_+=A|E_+-kI/2 and C_-=kI/2-A|E_-. Both have strictly positive real spectrum. The complete minimizing set in (M1) consists exactly of the following metrics:

    G(E_+,E_-)=0,
    B_+* G_++G_+ B_+ >=0,
    C_-* G_-+G_- C_- >=0.                              (M5)

Here G_+,G_- are the actual restrictions of G; no primary direction has been removed.

For necessity, orthonormalize E_+ and its G-orthogonal complement. In this frame B=A-kI/2 has block matrix [[B_+,C],[0,B_-]], and its Hermitian part is [[H_+,C],[C*,H_-]]. The trace on the projection P onto E_+ is exactly L_(h,k). Equality in Tr(PH)<=Tr(H_+) can hold only when P contains every positive eigendirection and annihilates every negative eigendirection: diagonalizing H, each omitted positive or admitted negative eigenvalue contributes a strictly positive loss. P may choose an arbitrary subspace of the zero eigenspace, but it therefore still commutes with H. Thus C=0, H_+>=0 and H_-<=0. The G-orthogonal complement is now A-invariant; its spectrum is precisely the negative half, so uniqueness of the complete spectral decomposition identifies it with E_-. This proves (M5). Conversely, (M5) block-diagonalizes the full Hermitian weight into its nonnegative and nonpositive parts; its positive trace is exactly the original spectral sum.

Every metric in (M5) has an explicit Lyapunov parametrization. Choose positive semidefinite Q_+,Q_- with

    intersection_(j=0)^(q/2-1) ker(Q_+^(1/2) B_+^j)={0},
    intersection_(j=0)^(q/2-1) ker(Q_-^(1/2) C_-^j)={0}.

Then set

    G_+=integral_0^infinity exp(-t B_+*) Q_+ exp(-t B_+) dt,
    G_-=integral_0^infinity exp(-t C_-*) Q_- exp(-t C_-) dt. (M6)

The integrals converge because all real parts are positive and their complete Jordan exponential factors have only polynomial growth. Differentiating the integrands proves the two Lyapunov equations in (M5). A vector has zero G-norm exactly when Q^(1/2)exp(-tB)v vanishes identically; its Taylor coefficients, together with Cayley–Hamilton, prove the stated finite intersection test. Thus (M6) is positive definite on exactly the displayed domain. Conversely, integrate the derivative of exp(-tB*)Gexp(-tB) to recover (M6) from every metric in (M5).

These integrals can be evaluated as finite rational block expressions. In the full CRT coordinates, write the relevant positive-real-part blocks as B_alpha=b_alpha I+N_alpha, with all original nilpotent signs retained. Then the (alpha,beta) block is

    G_(alpha,beta)=sum_(r,s=0)^(e-1)
       [(-1)^(r+s)(r+s)! /
        (r!s!(conj(b_alpha)+b_beta)^(r+s+1))]
       (N_alpha*)^r Q_(alpha,beta) N_beta^s.              (M7)

The denominators have positive real part; no zero denominator or primary reduction is introduced. Formula (M7) allows all cross terms within each spectral half. Conjugating by the original confluent CRT matrix returns every metric to the original polynomial frame. The scaling and section construction (M4) then realizes every such minimizing metric, up to a positive scalar, in the original finite polynomial source.

The classification does not impose the stronger condition that each primary block be G-orthogonal to every other primary block. Only the positive/negative halves must be orthogonal, and the complete semidefinite Lyapunov conditions remain. In particular it retains minimizing metrics whose Hermitian weight has additional zero eigenvalues inside a spectral half.
