# A uniform inverse bound for the original period observation

19 September 2026. This treats the original AKS7–10 observation at a fixed admitted simple quartet, actual fixed nonzero period and original branch. It gives a bound uniform in tensor degree for recovery on the observation image. The observation kernel is retained. It does not declare recovery of that kernel, a small native angular loss, or a proper-source isometry.

## 1. The precise polynomial map underlying the actual observation

Keep the exact invertible one-factor matrix

    H=F^(-1) Pi U E_prim,
    D=diag(zeta,zeta^2,zeta^3,zeta^4), zeta^5=1,
    Q(x)=Q_0(H^(-1)x), Q_0(t)=t_1 t_4-t_2 t_3.

Let A=C[x_1,x_2,x_3,x_4], A_k its homogeneous degree-k part, and A_k^D its weight-zero part. Substitution

    x=H t,   t=(ZW,Z,W,1)^T

gives the literal map Theta_k:A_k -> C[Z,W]_(<=k,<=k). Its kernel is Q A_(k-2). This is the actual AKS coefficient map. In the original invariant monomial frame and biform monomial frame the matrix of Theta_k restricted to A_k^D is B_k^T, with B_k exactly AKS8. The ordinary transpose is retained because this is the coefficient dual of the observation.

Use coefficient l1 and l2 norms only in this intermediate computation. They will be explicitly returned to the original output Gram and arithmetic source below.

For a biform monomial Z^a W^b, put n=max(0,a+b-k) and choose the exact homogeneous lift

    t_1^n t_2^(a-n) t_3^(b-n) t_4^(k-a-b+n).

The four exponents are nonnegative and sum to k. Substitute t=H^(-1)x. This defines a linear lift L_k of every biform of bidegrees <=k. With

    h_- = max(1,max_i sum_j |(H^(-1))_(ij)|),

its coefficient norm satisfies

    ||L_k f||_1 <= h_-^k ||f||_1.                       (U1)

This lift includes all original one-factor period and arithmetic-unit factors through H.

## 2. One fixed polynomial module controls all degrees

Introduce S=C[X_1,X_2,X_3,X_4] with X_i=x_i^5. The polynomial ring A is a free S-module on the 625 monomials x^r, 0<=r_i<5. Its invariant part is the free S-submodule on the 125 r with sum i r_i=0 modulo five. These counts follow by fixing three residues and solving uniquely for the fourth.

Multiplication by the fixed quadratic Q is an S-linear 625 by 625 polynomial matrix. Its entries have X-degree at most one. Form the fixed module map

    M:S^125 direct_sum S^625 -> S^625,
    M(f,g)=f+Qg.                                         (U2)

The homogeneous weight of X_i is five and the basis weight of x^r is |r|; the second source summand has its additional degree-two shift. Its image is exactly A^D+QA, in every degree, without using a moving minor.

Compute a reduced homogeneous module Groebner basis g_1,...,g_s for image M, in a fixed monomial order, and retain polynomial lifts h_j with M h_j=g_j. This is a single finite calculation at the fixed actual coefficients of Q; it is not performed independently at every k. The ordinary polynomial-module division algorithm constructs these lifts. Termination follows from the strict increase of the leading-monomial submodule and Dickson's lemma for N^4; a finite antichain argument proves that lemma by induction on the number of variables.

Normalize each g_j to leading coefficient one by its actual nonzero coefficient. Since there are only finitely many comparisons between a leading term and a tail term in these g_j, choose positive integer variable weights w_i and integer basis offsets beta_r realizing all those strict monomial-order comparisons. Such a choice can be made explicitly: for lexicographic comparisons of the bounded exponents appearing here use successive powers of an integer larger than the maximum exponent difference, and put the basis-position weights at the corresponding priority. Add one constant to all offsets so that they are nonnegative.

Let

    W=max w_i,
    B=max beta_r,
    C=max(2,1+max_j sum of absolute coefficients of tail(g_j)),
    H_0=max(1,max_j ||h_j||_1).

Every reduction of a monomial multiple of g_j lowers the integer score w.alpha+beta_r by at least one. For a degree-k input the score is at most W k/5+B. A recursive division, extended linearly from monomials, therefore gives a representation f=M R_k f plus its normal form, with

    ||R_k f||_1 <= H_0 C^(W k/5+B+1) ||f||_1            (U3)

on the image of M. To prove the bound, at each rewrite retain its explicit lift h_j and replace the leading term by the tail; a path has length at most the score. The sum of absolute coefficients at a branching step is at most C-1. Induction on the score bounds the total lift coefficient mass by H_0 C^(score+1). Coefficient cancellation only decreases the l1 norm. Every relation and lift is homogeneous in the specified degree, so its degree-k output has the original grading.

Thus the constants in (U3) are fixed finite functions of a single explicitly specified polynomial module and its actual coefficient field. They do not assert a bound uniform over changing periods. No degree-dependent nonzero minor is assigned a lower bound.

## 3. A right inverse on the original invariant image

Take f in image(Theta_k|A_k^D). The lift L_k f differs from an invariant lift by a multiple of Q, so L_k f belongs to image M. Apply (U3) and retain its invariant component p. Then Theta_k p=f and

    ||p||_2 <= R_k ||f||_2,
    R_k=H_0 C^(W k/5+B+1) h_-^k (k+1).                 (U4)

Here ||f||_1<=(k+1)||f||_2 because the biform frame has (k+1)^2 entries. In particular log R_k=O_actual(k).

This constructs a linear right inverse for B_k^T on its full image. Therefore its nonzero singular values, and those of B_k, are at least R_k^(-1). The equality of the nonzero singular values of a complex matrix and its ordinary transpose follows immediately by transposing its singular-value factorization. Zero singular values are retained as the actual observation kernel.

The forward coefficient map also has exponential norm. Substitution by H has l1 norm at most h_+^k, where h_+=max(1,max_i sum_j |H_(ij)|). The number of degree-k monomials is binom(k+3,3), so ordinary l1/l2 comparison gives an upper bound polynomial in k times h_+^k. Hence the condition number on the nonzero coefficient singular values is exp(O_actual(k)).

## 4. Restore the actual inherited output norm

The original Fourier matrix satisfies F*F=5(I+11*), with eigenvalues five and twenty-five. Its k-fold tensor therefore has squared singular values between 5^k and 25^k. In the unscaled symmetric-word coefficient frame, the identity tensor Gram is diag(k!/nu!). These factors lie between one and 4^k, by the multinomial theorem. Restriction to weight-zero coordinates preserves the inequalities. Thus AKS10's exact output Gram G_0 obeys

    5^k I <= G_0 <= 100^k I.                            (U5)

No multinomial coefficient has been inserted twice: (U5) is precisely the coefficient-of-(bar x F*F y)^k Gram given in AKS10.

In root-value coordinates v_(a,b)=P(lambda_(a,b)), the actual observation is j Lambda_k P=F_0 B_k v. On its image it therefore has a right inverse into the quotient of the root-value space by ker B_k of norm at most

    5^(-k/2) R_k.                                       (U6)

For example, use the actual least-squares inverse of F_0 on its image followed by the Moore–Penrose inverse of B_k. Equations (U4)–(U5) give the bound; the inverse is not merely asserted to exist. The recovered vector is determined only modulo the actual kernel of the original observation.

## 5. Restore the original arithmetic norm, uniformly in the cutoff

Let q=(k+1)^2, c=k/2, R=k sqrt(delta^2+gamma^2), d_*=2 min(delta,gamma)>0. All original root separations are at least d_*. The exact Lagrange lift of a root-value vector is

    P_v(S)=sum_lambda v_lambda chi(S)/[(S-lambda)chi'(lambda)].

On S=c+iy,

    |P_v(c+iy)|^2
       <= q d_*^(-2(q-1)) (|y|+R)^(2q-2) ||v||_2^2.

Choose eta=pi/4. The elementary exponential-series bound t^n<=n! eta^(-n)e^(eta t), and the actual convolution identity for M_h(eta), give

    ||P_v||_(m_k)^2 <= B_(h,k)||v||_2^2,
    B_(h,k)=2q (2q-2)! (eta d_*)^(-2q+2)
                 exp(eta R) M_h(eta)^k.                (U7)

Evenness gives integral exp(eta|y|) m_k(y)dy <=2 M_h(eta)^k. All source masses remain in (U7).

For every original cutoff N>=q-1, the canonical minimum norm of [P_v] is no greater than this specific representative norm. Combining (U6) and (U7) gives a right inverse on the actual period image with

    ||R_(k,N)||_(period -> arithmetic quotient)
       <= sqrt(B_(h,k)) 5^(-k/2) R_k,
    log ||R_(k,N)|| <= O_(h,u)(q log(q+2)),              (U8)

uniformly over every such N. This recovers the quotient by ker Lambda_k, not the lost kernel. It holds at the fixed actual period, including its full unit and branch.

The bound is large and is not a small action allowance. It does answer the formerly unquantified degree-uniform recovery question for this specified observation: the cost is explicitly bounded, with no unexamined growing minor. Neither (U6) nor (U8) gives the native angular exponents or identifies the period quotient metric with the independent PRD source metric.
