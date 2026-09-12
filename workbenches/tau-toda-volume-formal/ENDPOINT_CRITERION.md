# Sharper endpoint-only criterion and the scope of exterior iteration

This is a mathematical continuation of the supplied Toda and exterior notes. The general Jensen argument and exterior-multiplicity count below have written proofs; they are not additional Lean declarations. The norm-ratio product and overlapping-volume telescope are included in the finite formalization target list. No arithmetic asymptotic bound is claimed.

## 1. Eliminate the supremum over recurrence coefficients

Retain a nonempty fixed packet and tensor degree k, cyclic dimension q, the actual positive monic norm sequence omega_N, the actual quotient volume V_N=det G_N, and the source's exact control allowance epsilon_N. Choose consecutive admitted degrees N=n,...,n+r-1 with n>=q and integer r>=1. Put

    B_(n,r)=log( V_(n-1) V_n / (V_(n+r-1) V_(n+r)) ),
    A_(n,r)=(omega_(n+r)/omega_n)^(1/(2r)).

These are four endpoint quotient volumes and two endpoint polynomial norms of the existing family. Since V is positive and nonincreasing, B_(n,r)>=0. The source's finite upper bound implies

    min_(0<=j<r) epsilon_(n+j)
      <= A_(n,r) sinh(B_(n,r)/(2r)).                 (E1)

Unlike the preceding maximum-recurrence criterion, E1 needs no pointwise upper bound for every recurrence coefficient in the window.

### Complete proof

For N=n+j set

    x_j=(1/2)log(V_(N-1)/V_(N+1))>=0,
    A_j=sqrt(omega_(N+1)/omega_N)>0.

The existing local estimate is epsilon_(n+j)<=A_j sinh(x_j). If any x_j=0, the nonnegative allowance at that step is zero, and E1 follows. Otherwise all x_j>0. The function f(x)=log(sinh x) has

    f''(x)=-1/sinh(x)^2<0.

Finite Jensen therefore gives

    product_j sinh(x_j) <= sinh((sum_j x_j)/r)^r.

Let E be the minimum of the nonnegative allowances. Multiplication of the local bounds gives

    E^r <= product_j epsilon_(n+j)
        <= (product_j A_j) product_j sinh(x_j).

The actual products telescope:

    product_j A_j=(omega_(n+r)/omega_n)^(1/2),
    2 sum_j x_j=log( V_(n-1) V_n / (V_(n+r-1) V_(n+r)) ).

Taking the nonnegative r-th root proves E1. A finite minimum is attained, so E1 selects an actual original degree N inside the specified window. No favorable metric is selected independently, and its original theta representative, quotient and full jets remain attached.

The recurrence product is `VolumeWindow.norm_ratio_product`; the second telescope is `VolumeWindow.overlapping_log_telescope`, applied to V(j)=V_(n-1+j). The Jensen and nonnegative-root assembly is this written proof rather than a claim about an unimplemented exterior/analytic declaration.

## 2. Every input is an endpoint of the two original determinant sequences

The source's omega_j=D_(j+1)/D_j gives

    A_(n,r)=[D_(n+r+1) D_n/(D_(n+r) D_(n+1))]^(1/(2r)).

The four V-values in B are evaluated by V_N=D_(N+1)/B_(N-q+1), with the source's literal relation determinant B. All indices are nonnegative because n>=q. No negative-index determinant or inverse of a rank-deficient earlier kernel is used. The common mass factors cancel only in these displayed ratios; the source norm omega_0=mu_h^k has not been reset.

For the original quartet,

    q_k=[1+k(m-1)](k+1)^2,
    L_(h,k)>=delta*k*q_k/2.

The exterior theorem gives L_(h,k)<=epsilon_N at every admitted N. Thus E1 yields

    L_(h,k) <= A_(n,r) sinh(B_(n,r)/(2r)).          (E2)

A proof that the right side is o(k*q_k) along admitted n=n(k), r=r(k) would exclude that fixed off-line quartet. One sufficient set of estimates is

    r(k)>=c_h q_k,  A_(n,r)=O_h(q_k),
    B_(n,r)=o_h(q_k log k),

for c_h>0. Indeed B/(2r)=o(log k), so sinh(B/(2r))<=exp(o(log k))=k^(o(1)), and the ratio to k*q_k tends to zero. These are candidate arithmetic estimates, not consequences of the formal telescope, positivity, the Toda equation, or Deligne's finite-field hypotheses.

The weighted endpoint criterion is sharp as an abstract sequence inequality: equality can occur when all x_j are equal and every A_j sinh(x_j) equals the same allowance. For arbitrary recurrence sequences the bound is never larger, and potentially strictly smaller, than the bound obtained by replacing A_(n,r) by the largest A_j.

## 3. A useful boundary on further exterior amplification

The supplied single exterior theorem is correct. It must not be reused with a rank-two hypothesis that no longer holds after exterior powering.

Suppose the original self-adjoint control H has spectrum

    (+epsilon, 0 repeated q-2 times, -epsilon),  epsilon>0.

On the actual p-th exterior power, 1<=p<=q, the additive control has +epsilon and -epsilon each with multiplicity

    r_p=binomial(q-2,p-1),

and zero with multiplicity binomial(q-2,p)+binomial(q-2,p-2). This follows by the unscaled wedge basis: select the positive direction but not the negative, the negative but not the positive, or both/neither. In particular its operator norm is at most epsilon: it equals epsilon for 1<=p<=q-1 and is zero for p=q. Its rank is 2r_p, not generally two.

Apply an s-th exterior power to that whole space, whose dimension is D_p=binomial(q,p). Its largest absolute additive-control eigenvalue is exactly

    epsilon*min(s,r_p,D_p-s),  0<=s<=D_p.

Proof: select positive eigenvectors first, zero eigenvectors next, and negative eigenvectors only when the degree forces them. There are r_p available positive directions and r_p negative ones. This attains the stated piecewise maximum; reversing the choices attains its negative. At s=D_p the sum is zero. For example q=4,p=2 gives spectrum (+epsilon,+epsilon,0,0,-epsilon,-epsilon), and the next exterior square has allowance 2epsilon.

This does not weaken the original determinant-line amplification or remove its nilpotent arithmetic action. It identifies the precise cost of iterating the operation on the entire exterior space, and prevents a spurious second cost-free amplification. The source's chosen determinant line has its own one-dimensional action and must remain distinguished from the complete first exterior power.

## 4. Collaboration boundary

The formal work carries the exact source/quotient determinant and the two loss terms into the original-Gram trace certificate. The analytic collaborator can now estimate the two endpoint quantities in E1, or retain the exact phase and imbalance when the coarse upper bound is too large. The six-part Deligne archive and uploaded ZIP test suites were not opened in this execution environment; the source statements used here came from the complete pasted notes. The current GitHub correction and original source maps are unchanged.
