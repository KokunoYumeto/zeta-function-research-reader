# Whole-proof review of the joint-Schur resolvent application

Reviewed on 2026-09-14: the complete `JOINT_SCHUR_RESOLVENT_APPLICATION.tex`, JRA1–JRA29, including every proof paragraph and the formal-source provenance paragraph. Accepted source SHA-256:

`718c3a5ed81a81acc02a808e64fc18d20b9be95f8d71d9766914ae4d7348d063`.

The entire mathematical body was read, followed by rereading the three exactness repairs described below. The earlier label prefix JSR was changed throughout to JRA to avoid collision with the independent receiving calculation. This was a mathematical source review; no PDF build, Lean run, numerical substitution, or historical CI replay was performed.

## Original source and quotient maps: JRA1–JRA11

The stated packet has distinct grid nodes, all nonreal because `k=4l+1` is odd. The new real nodes are distinct and disjoint from that grid. The Chinese remainder construction therefore gives the claimed joint-map surjectivity at `M=N+l`, for the declared range `N>=q-1`. Its positive source covariance has the two stated positive Schur complements. The adjoints and inverse orders in both complements and in `G_N^0=C_k M_f^* S_M^{-1} M_f` are correct.

The original monic-tail covariance update is `K_M=K_N+U_N Omega_N^{-1} U_N^*`. Consequently `X_N=Omega_N^{-1} U_N^* G_N U_N` is self-adjoint for **Omega_N**, and `Y_N=A_M^{-1} C_M^* G_M C_M` is self-adjoint for **A_M**. These are the metrics used in JRA12. They must not be interchanged with their inverses. The spectrum assertions follow from the displayed positive congruences, including `A_M(I-Y_N)=L_M>0`.

The raw Hermite formula in JRA6 is now the explicit direct sum of lower triangular node blocks, including every derivative order below `e`. Its entries `binom(r,s) f^(r-s)(lambda)` follow directly from differentiating the product. The change from divided to raw jets is `D=diag(r!)`, with `F_raw=D F_div D^{-1}`. The repaired formula explicitly makes different-node entries and upper triangular entries zero.

The Gamma constant agrees exactly with the incoming source: since `k=4l+1`, `4^l 2^(1-k/2)=sqrt(2)`, so JRA7 is also `C_k=(2pi)^(k/2)/(sqrt(2) Gamma(k/2))`. In particular its `k=5` value is `16pi^2/3`. The holomorphic ratio and its real-line modulus retain the `4^{-l}` factor.

For the crucial sign, write `c0=q log C_k+2 log|det M_f|`. JRA8 gives

\[
\log V_N^0=c_0+\log V_{N+l}^{\sigma}
                 -\log\det(I-Y_N).
\]

Subtracting this from `log V_N^sigma`, and then using JRA9, gives exactly

\[
\log V_N^\sigma-\log V_N^0
=-c_0+\log\det(I+X_N)+\log\det(I-Y_N).
\]

Thus the four coefficients `(1,1,-1,-1)` in JRA11 have the correct sign, and the constant cancels. This agrees with the incoming note's `R_k^0-R_k^sigma = B_k^sigma-B_k^0`. No minus sign is missing from the `I-Y_N` determinant.

## Exact block construction and finite constants: JRA12–JRA20

The direct sum has dimension `n=8l`, with `l>=1` explicitly stated, so the nonempty index required by PR31's spectral theorem is satisfied. Both copies at endpoint `r` carry sign `epsilon_r`. Hence `Q^2=I`, `Tr Q=0`, and `Tr Q^2=8l`. The determinant character multiplies both determinants at each endpoint before applying that endpoint's sign; this is the required typed scalar comparison, with no assertion that this Q is the original larger-source canonical projector contrast.

JRA15 now constructs W as the direct sum of positive square roots of the eight original metric blocks. The subsequent block unitary construction therefore commutes with Q. Its metric equation `F^*F=M` and both inverse equations are correct, and it supplies simultaneous spectral coordinates for every rational function used in JRA17.

The lower constant `mu=min(1,min_r det(I-Y_Nr))` is valid. Every eigenvalue of `I-Y_N` belongs to `(0,1]`; its product is at most each individual eigenvalue. The upper constant `nu=1+sum_r Tr X_Nr` bounds the plus blocks since a nonnegative eigenvalue is at most the sum of the eigenvalues, and it bounds the minus blocks since their eigenvalues are at most one. This proves `0<mu<=b_i<=nu`, `mu<=1<=nu`, and `0<=theta=(nu-mu)/(nu+mu)<1`.

`K0=mu^{-2} Tr(B-I)^2` retains the original direct-sum matrices. The trace is `sum_r Tr(X_Nr^2+Y_Nr^2)=sum_i(b_i-1)^2`, even though their displayed original-coordinate matrices need not be Hermitian in the Euclidean metric. The constructed metric isometry establishes this equality and its nonnegativity.

For `a_t=1+t(d-1)`, `d=(mu+nu)/2`, the inequality `t/a_t<=1/d` is equivalent to `t<=1`. All denominators stay positive, giving `|h_i(t)|<=theta` and `sum_i gamma_i(t)^2<=K0`. The equation `(I-H_t) X_t^res=T_t` and the literal finite sum give the residual with exponent `L+1`, exactly as stated. Its matrices commute because they are rational functions of the same original B, rather than because of an assumed observable commutation theorem.

## Centered error, integration and stopping: JRA21–JRA25

The complete centered variance includes the subtracted mean square and equals a sum of squares. Its upper bound is `theta^(2L+2) K0`. Scalar cancellation follows from `Tr Q=0`, and weighted Cauchy–Schwarz gives the displayed factor `sqrt(8l V_L(t))`. The fixed isometry preserves every product trace. The calculation therefore supplies all inputs to the generic PR31 signed-error theorem; it also proves this application directly.

The identity `log b = integral_0^1 (b-1)/(1+t(b-1)) dt` holds at `b=1` by the zero integrand. The positive lower denominator `mu` makes the finitely many integrands continuous. Thus JRA23 integrates the actual pointwise estimate over the entire unit interval with its full signed center.

For JRA24, the substitution `u=1+(d-1)t` gives

\[
I_j(d)=(d-1)^{-j-1}\int_1^d
       \sum_{a=0}^j(-1)^a\binom ja u^{-a-1}\,du.
\]

The `a=0` integral is `log d`. For `a>=1` it is `(1-d^{-a})/a`. This proves the stated closed formula, including `0<d<1`: both the integral orientation and the signed power of `d-1` are retained. For `d=1`, direct integration gives `1/(j+1)`. No singular-case formula is used at `d=1`.

The stopping degree JRA25 is sufficient with the stated residual exponent. For `A=sqrt(8l K0)>eta`, the chosen `L` satisfies `theta^L A<=eta`, and hence also `theta^(L+1) A<=eta`. For `A<=eta`, `L=0` suffices. If `A=0`, the isometry and sum of eigenvalue squares give `B=I`; if `theta=0`, `mu=nu=1` gives the same conclusion. These separate cases correctly avoid taking logarithms of zero. The rule is finite for each specified positive source pair and does not assert a degree-uniform estimate.

## Receiving maps and final interval: JRA26–JRA29

The interval intersection in JRA26 contains the same signed return by the two independently stated bounds; the application makes no false universal width-improvement claim. JRA27 is the canonical minimum on the original relation fibre, with the displayed Gram inverse order obtained by completing the square. Its degree `q-1` zero-dimensional case is expressly retained. JRA28 is the exact multiplication intertwining on the inherited weighted cyclic inclusion, and the accompanying labelled-set transport does not assign unproved multiplicative structure to arbitrary coefficient maps.

JRA29 now explicitly states that `[a_k,b_k]` encloses `delta_k^sigma`. Adding this interval to the proved signed-return interval gives the two displayed endpoints with the correct signs. The original arithmetic interval, Gamma-moment finiteness, and original tensor/cyclic algebra remain identified as inherited source results. This review checks their use and the exact receiving substitution; it does not re-prove the entire earlier arithmetic determinant programme.

## Repairs and acceptance

Three specification clarifications were requested and are present in the accepted hash: the explicit block construction of W; the complete node-block/zero-entry formula for raw jets; and the explicit statement `delta_k^sigma in [a_k,b_k]`. All equation identifiers now use JRA consistently. No unresolved mathematical discrepancy was identified in JRA1–JRA29. The sign, original metrics, finite constants, closed integral formula, and stopping rule are accepted in the stated fixed-packet scope.
