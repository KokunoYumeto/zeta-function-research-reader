# Independent proof check of both cutoff singular rates

The complete source **REAL_PAIR_CUTOFF_MATRIX.tex**, RCM1–17, was read and independently re-derived. Reviewed SHA256: 409b03d303b95f20f82db10956eb9062997b7244b87e62162a4200b95beea19a.

No mathematical correction is needed within the source's stated quantifiers: the geometric parameter is fixed and invertible, the cutoff tends to infinity, and the growing source order obeys the displayed condition. The source does not interchange this limit with an approach to the singular parameter. It also does not claim an intermediate-rank asymptotic from the determinant alone.

The analytic input agrees with the independently completed **REAL_PAIR_UNIFORM_COEFFICIENTS.tex**, RUC1–30. RCM uses the same actual factorization \(g=U(t-\alpha)(t-\beta)\), retains the full reciprocal \(F=1/U\), and includes the unit derivative at a double root. The following calculation gives explicit versions of its determinant-error constants and verifies the matrix and Gamma conclusions.

## Uniform coefficient and full-matrix decomposition

The contour formula RCM3 is exact: partial fractions in the contour variable yield \(F(t)/q(t)\) at \(t\) and the negative interpolation quotient at the two roots. At a repeated root, the limit is the corresponding derivative residue. Coefficient extraction gives the same fixed radius and constant for every \(n\):

\[
|e_n|\le C_RR^{-n},\qquad C_R=M_R/(R-r_0)^2.
\]

The distinction between this coefficient estimate and a bounded remainder matrix is retained. Since \(R<1\), the matrix estimate contains \(R^{-D}\). The source prints that term rather than calling the matrix remainder bounded.

For negative integer indices, the principal coefficient is minus the divided difference of \(F(z)z^{k-1}\) at \(k=-n\ge1\). Differentiating along the segment between the roots gives

\[
|P_{-k}|\le C_1r_0^{k-1}
 +\mathbf1_{k\ge2}(k-1)C_0r_0^{k-2}.
\]

Summation of the two geometric derivative series gives exactly

\[
K_-=\frac{C_1}{1-r_0}+\frac{C_0}{(1-r_0)^2}.
\]

Thus the full-matrix identity \(T_D(h)=\mathcal P_D+\mathcal E_D-\mathcal L_D\) has the correct minus sign on every lower diagonal. The two full outer products have rank at most two. At coalescence the coefficient is affine in the row/column index difference, so it still has two generating vectors. There is no use of the false assertion that an upper-triangular pole matrix itself has rank two.

## The first singular rate

The exact adjacent identities are

\[
\alpha P_n-P_{n-1}=F(\beta)\beta^{-n-1},\qquad
\beta P_n-P_{n-1}=F(\alpha)\alpha^{-n-1}.
\]

Both survive coalescence with their derivative terms cancelling. Choosing the right-hand root of smaller modulus \(r\) and retaining both error coefficients gives precisely RCM11:

\[
(1+r_0)\max(|h_n|,|h_{n-1}|)
\ge m_Fr^{-n-1}-C_R(r_0+R)R^{-n}.
\]

The printed threshold RCM12 makes the error at most half the main term. In particular it is valid at every sufficiently large cutoff, not merely on a subsequence of noncancelling top coefficients. Each of the two coefficients is an actual matrix entry. Conversely RCM6 and the error estimate bound the norm by a polynomial in \(D\) times \(r^{-D-2}\). Taking \(D\)-th roots proves

\[
\lim_{D\to\infty}\sigma_1(T_D(h))^{1/D}=r^{-1}.
\]

This proof also works when the two roots have equal modulus, when the roots coincide, and when one principal coefficient vanishes at infinitely many indices.

## The exact Hankel corner and its complete error constants

Let \(s_r=\max(|\alpha|,|\beta|)\), \(J=|F(\alpha)F(\beta)|>0\), and

\[
A=C_0+2r_0C_1.
\]

For \(D\ge2\), the actual upper-right two-by-two minor is

\[
\mathcal H_D=h_{D-1}^2-h_Dh_{D-2}.
\]

The full principal coefficient has the exact identity

\[
P_{D-1}^2-P_DP_{D-2}
=\frac{F(\alpha)F(\beta)}{(\alpha\beta)^{D+1}}.
\]

Its sign follows by reversing the sign of the determinant \(P_nP_{n+2}-P_{n+1}^2\) at \(n=D-2\). It remains valid at repeated nonzero roots. Expansion of the exact coefficients gives

\[
\begin{aligned}
|\mathcal H_D-(P_{D-1}^2-P_DP_{D-2})|
\le{}&2|P_{D-1}||e_{D-1}|+
 |P_D||e_{D-2}|+|P_{D-2}||e_D|\\
&+|e_{D-1}|^2+|e_De_{D-2}|.
\end{aligned}
\]

Using \(|P_n|\le A(n+1)r^{-n-2}\), \(|e_n|\le C_RR^{-n}\), and \(r<R\), each of the three mixed errors is bounded by its corresponding multiplicity in

\[
4AC_R(D+1)r^{-D-2}R^{-D+2}.
\]

The two pure remainder errors together are bounded by \(2C_R^2R^{-2D+2}\). Division by the principal modulus \(J(rs_r)^{-D-1}\) gives the explicit relative bound

\[
\left|
\frac{\mathcal H_D}{F(\alpha)F(\beta)(\alpha\beta)^{-D-1}}-1
\right|
\le K_1(D+1)(s_r/R)^D+K_2(rs_r/R^2)^D,
\]

where the complete constants are

\[
K_1=\frac{4AC_RR^2s_r}{rJ},\qquad
K_2=\frac{2C_R^2R^2rs_r}{J}.
\]

Both bases are strictly less than one. These constants are finite at the fixed invertible parameter, including a repeated nonzero root. The factor \(1/r\) shows why this particular fixed-point estimate should not be declared uniform as a root goes to zero. RCM explicitly avoids making that claim. The separate real-slice result RUC20–21 gives a uniform local threshold when the two root moduli are equal.

An explicit fixed-point threshold can also be supplied. Let

\[
a_1=\log(R/s_r)>0,\qquad a_2=\log(R^2/(rs_r))>0.
\]

Since \((D+1)e^{-a_1D/2}\le1+2/(a_1\exp(1))\), the bound is at most \(1/2\) for all

\[
D\ge\max\left\{2,\
\left\lceil\frac2{a_1}\log^+\!\left(4K_1\left(1+\frac2{a_1\exp(1)}\right)\right)\right\rceil,\
\left\lceil\frac1{a_2}\log^+(4K_2)\right\rceil\right\}.
\]

Each term on the right-hand side of the relative-error bound is then at most \(1/4\). This proves RCM14 quantitatively and yields a nonzero corner at every sufficiently large cutoff.

## The second and third singular rates

The absolute value of the corner minor is bounded above by \(\sigma_1\sigma_2\), because it is a matrix entry of the second exterior map in orthonormal coordinate frames. The preceding determinant asymptotic and the first singular-rate limit imply

\[
\liminf_{D\to\infty}\sigma_2(T_D(h))^{1/D}\ge s_r^{-1}.
\]

If \(r<s_r\), subtract the rank-one outer product attached to the smaller root. For the remaining root \(c\), \(|c|=s_r<1\), the two vectors satisfy

\[
\|(c^i)_{i=0}^D\|\le(1-s_r^2)^{-1/2},\qquad
\|(c^{-j})_{j=0}^D\|\le s_r^{-D}(1-s_r^2)^{-1/2}.
\]

Thus its rank-one matrix has norm at most its exact residue amplitude times \(s_r^{-D}/(1-s_r^2)\). Adding \(K_-\) and \(C_RR^{-D}/(1-R)\) bounds the complete residual. Its exponential rate is at most \(s_r^{-1}\), since \(s_r<R\). The kernel of the subtracted rank-one map has codimension at most one. The minimum–maximum characterization applied on that kernel bounds \(\sigma_2\) by this residual norm.

If \(r=s_r\), the bound \(\sigma_2\le\sigma_1\), combined with the lower bound, gives the same limit. This covers the repeated-root case without a singular separated-residue representation. Therefore

\[
\lim\sigma_2^{1/D}=s_r^{-1},\qquad
\lim\|\bigwedge^2T_D(h)\|^{1/D}=(rs_r)^{-1}.
\]

Subtracting the entire rank-at-most-two principal matrix and restricting to its kernel gives \(\sigma_3\le K_-+C_RR^{-D}/(1-R)\). Hence its upper exponential rate is \(R^{-1}\), exactly as claimed. This is an upper rate, not an assertion that no further spectral roots occur beyond the chosen contour.

## The original Gamma condition and its precise scope

The actual old inverse is \(B_{D,s}^{-1}=D_\rho^{-1}T_D(h)D_\rho\), with both physical frames orthonormal in their original measures. Multiplication by these two diagonal matrices bounds every singular value between \(\kappa_{D,s}^{-1}\sigma_j(T_D(h))\) and \(\kappa_{D,s}\sigma_j(T_D(h))\). This is the condition number, not its square, because the two factor norms have product \(\max\rho_j/\min\rho_j\). The corresponding second exterior comparison has the square of that condition number.

At \(s=1\), monotonicity gives \(\kappa=\rho_D\), and the exact induction used in RQT15 yields \(\log\kappa\le\frac14\log(4D+1)\). For \(s\ge2\), monotonicity reverses, and

\[
\kappa_{D,s}^2=\prod_{j=1}^D\left(1+\frac{s/2-1}{j}\right).
\]

Taking logarithms and integrating \(1/(1+t)\le1\) for \(t\ge0\) gives

\[
\log\kappa_{D,s}\le\tfrac12(s/2-1)H_D.
\]

Thus \(s_D\log(D+1)/D\to0\) is a sufficient condition for \(\kappa^{1/D}\to1\), which transfers all three singular-rate statements. It includes the original source sequence \(s_D=a_{{\rm amp},D}=O(\sqrt D)\).

The qualifier matters: \(D=\Theta(a_{\rm amp}^2)\), or more generally \(a_{\rm amp}=O(\sqrt D)\), implies the stated condition. An upper bound \(D=O(a_{\rm amp}^2)\) by itself does not. For example \(D=a_{\rm amp}\) obeys that upper bound but does not satisfy the sufficient condition proved here. RCM correctly states its result on the sequences satisfying the required relation and should retain that wording. This observation does not invalidate any claim currently made in RCM.

## The full unit in the remaining logarithmic sum

On the fixed invertible parameter locus under discussion, the actual order is zero. The old matrix therefore has determinant \(g_0^{D+1}\); both Gamma diagonal factors cancel exactly in that determinant even when \(s\) varies. Consequently

\[
\frac1D\sum_{j=1}^{D+1}\log\tau_{j,D}
=-\frac{D+1}{D}\log|g_0|.
\]

The first two terms converge after division by \(D\) to \(-\log r\) and \(-\log s_r\). Since \(g_0=U(0,p)\alpha\beta\), subtraction gives

\[
\lim_{D\to\infty}\frac1D\sum_{j=3}^{D+1}\log\tau_{j,D}
=-\log|U(0,p)|.
\]

The sign and constant are exact. The unit has not been set equal to one. The conclusion remains valid for every source-order sequence covered by RCM16. It does not claim that the individual remaining singular values have a common limit or that every intermediate exterior rank has been evaluated. It also does not apply this old order-zero determinant on the order-one or order-two strata without changing the source.

## Verification record

Independent exact symbolic calculations checked 14 instances of the displayed relative-error factor identities and seven signed corner determinants for cutoffs two through eight. The derivations above prove the identities for all cutoffs; these finite checks only corroborate the factors and signs. No new root certificate was run. No original source, frozen edition, or shared mathematical proof was edited during this review.
