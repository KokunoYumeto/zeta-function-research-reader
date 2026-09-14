# Independent full-source reading: CTR1–CTR54

Read on 2026-09-14: every definition, equation, and proof paragraph in `contrast_transport.tex` through CTR54. The accepted complete source SHA-256 is:

`3763cc964d03552ef9281d8fc4b21c9f9ffa8fa7e47c70fe2d66c8084e1fe4b2`.

The first 33 equations were independently accepted at the earlier cut:

`ade16d569e9c0e93679396bd1b2e81eaae904ef2867b15fc7983a5622044f44b`.

No mutation of `contrast_transport.tex`, build, numerical run, or Lean run was performed by this reviewer. The author repaired the bare `qquad`/`quad` command tokens reported during reading; the repaired spans were reread and a bounded search found no remaining instance without its backslash. The final CTR1–CTR33 prefix reproduces the earlier accepted cut after preserving that cut's CRLF line endings and removing the newly appended section separator. Every paragraph of CTR34–CTR54 was then read independently. No unresolved mathematical discrepancy was found in the complete accepted source.

## Fixed polynomial maps and original metrics: CTR1–CTR10

The finite positive measure with infinite support is sufficient for every displayed Gram to be positive definite. A nonzero polynomial has only finitely many zeros on the injective affine line; a support point outside those zeros has a neighbourhood of positive measure on which its modulus is bounded away from zero. Bounded exponential density transport preserves this property. Finiteness follows from compactness and finite mass, independently of the positivity argument.

The exact sequence in CTR4 is valid: division by monic f gives the declared quotient and remainder degree bounds, and its kernel is exactly `(-fa,a)` with `deg a<=r-l-1`. The intersection, sum, and dimensions in CTR5 follow, including r=l. The two original matrices C0 and Cf remain fixed as the source metric varies.

The coefficient projector formula has the correct inverse/adjoint order. The proposed residual columns U0 and Uf give bases of their respective orthogonal complements of the intersection: for U0 a nonzero polynomial of degree below l cannot lie in f times the lower polynomial space; for Uf the high coefficient degrees cannot lie in that lower space after cancelling f. Thus both residual Grams are positive definite.

The actual frame B in CTR10 is invertible. Applying the two projectors to its column groups gives precisely the displayed matrix of D. In particular the upper-right residual block is `-H0^{-1} C`, while the lower-left is `+Hf^{-1} C*`. These signs and the full cross Gram are retained correctly.

## Exact singular-vector and eigenvector transport: CTR10–CTR14

Congruence by the two positive roots sends the residual Gram to `[[I,T],[T*,I]]`. Its Schur complement proves `I-T*T>0`; therefore all singular values lie in `[0,1)`. Constructing left vectors `a_j=T b_j/sigma_j` for positive singular values, and completing by ker(T*) at zero singular values, gives the two full orthonormal bases. Their transported vectors satisfy exactly

`<u_i,u_j>_M=<v_i,v_j>_M=delta_ij`, and `<u_i,v_j>_M=sigma_j delta_ij`.

Consequently the vectors `w_j=(v_j-sigma_j u_j)/sqrt(1-sigma_j^2)` are well defined, and the pairs `(u_j,w_j)` form an original-metric orthonormal frame of the full intersection complement. The projector and contrast matrices in CTR12 follow by writing `v_j=sigma_j u_j+s_j w_j`.

The two eigenvector signs in CTR13 are correct. With `alpha=sqrt((1-s)/2)` and `beta=sqrt((1+s)/2)`, the identities `alpha^2+beta^2=1` and `2alpha beta=sigma` verify direct multiplication by `[[-s^2,sigma s],[sigma s,s^2]]`. The vectors `alpha u+beta w` and `beta u-alpha w` have eigenvalues `+s` and `-s` respectively. At sigma=0, s=1, they reduce to w and u; no singular division appears in these formulas. The common intersection contributes only zero eigenvalues. Thus the exact inertia `(l,l,r-l)`, rank `2l`, interval `[-1,1]`, and original-metric absolute trace `2 sum s_j<=2l` are all established.

## Signed density derivative: CTR15–CTR20

The extended parameter interval and bounded density give an integrable dominating function for the Gram derivatives and their difference quotients. The coefficient compression `A=M^{-1}M'` has precisely the original-metric adjoint equation, and its quadratic form is bounded between the essential infimum and supremum of the same real psi. The evaluation adjoints are taken from the original coefficient frame into the displayed L2 space, so no source metric is silently replaced.

Jacobi's formula with the fixed original inclusion columns gives the exact sign `d_t log R=Tr((P_f-P_0)M^{-1}M')`. In the constructed eigenframe, the positive and negative eigenvectors contribute the difference of two expectations in `[a,b]`. This proves the factor `(Tr|D|/2) osc psi` and hence `l osc psi`; D and A need not commute. Continuity of the scalar derivative makes the integrated estimate in CTR20 valid. The separate l=0 statement is correct for the monic constant f=1.

## Original arithmetic density, coordinates, and rates: CTR21–CTR33

The base measure `q^(2q+1)|z|^(2q) sigma(qz) dz` includes both the original radial power and the y=qz Jacobian. The actual measure in CTR27 is obtained by multiplying by `exp psi_chi`, with the full original chi and multiplicity e. Positivity and finite mass on both compact intervals are checked for these actual densities.

The finite threshold implies `k sqrt(d+g)/q<=epsilon/2`, since q>=k^2 and epsilon=2^-10. Thus every expanded root factor has modulus below one, and tau_epsilon<=1/4. For a root displacement zeta, `iy-zeta=iy(1+i zeta/y)`. The quadratic term of twice the real logarithm is `Re(zeta^2)/y^2`, giving exactly `p2=q k(k+2)(d-g)/3`, with its negative sign. The root reflection removes all odd powers before estimation. Bounding the remaining even powers gives `q sum_{j>=2} tau^j/j`, and hence the displayed remainder constant.

At y=qz the coefficient is `a_k=p2/q^2=k(k+2)(d-g)/(3q)`. On the two intervals, the range of z^-2 is `[64^-2,epsilon^-2]`; this proves the oscillation bound in CTR26, including the factor `2 delta_chi` for the remainder. Applying the exact contrast transport gives both inequalities in CTR28 with coefficient l and the unchanged r-column determinant ratio.

The maps T_pow and T_chi in CTR29 have their stated Hilbert Grams. The multiplier U is bounded with bounded inverse on the compact bulk, its squared modulus is exp psi_chi, and it commutes with multiplication by the unchanged f. These provide the declared typed comparison without changing the arithmetic quotient.

The S-to-z coefficient change has diagonal `(iq)^j`, j=0,...,r-1, and the same squared determinant appears in both restriction Grams. Writing `f(c+iqz)=(iq)^l tilde f(z)` contributes one factor `(iq)^l` to each of the r numerator columns. Therefore the exact surviving factor is **q^(2lr)**, and the logarithmic term is **2lr log q**, as in CTR30. There is no missing coordinate or Jacobian factor.

Finally, tau_epsilon<=1/4 gives

`delta_chi <= 2 k^4(d+g)^2 / [3 e^3(k+1)^6 epsilon^4] <= 2(d+g)^2 / [3 e^3 k^2 epsilon^4]`.

Together with `|a_k|<=|d-g|/(3e)` and `2l=(k-1)/2`, this yields exactly CTR32 and CTR33. At fixed epsilon and original parameters the first error is O(k/e), hence o(q); it is O(1) for fixed m>=2. The quadratic-retaining error is O(k^-1) at m=1 and O(k^-4) at fixed m>=2. These conclusions concern the complete bulk-restricted ratio. The final paragraph correctly leaves the omitted integration regions to the separate full-source comparison.

## Complete actual and reference tail calculations: CTR34–CTR44

The entire proof bodies BRD22–BRD38 in the accompanying `ORIGINAL_RELATION_BULK_CONTROL.tex` were read to check their use here. That provider's current SHA-256 is `4d6e3df419edcedbe7e66e6f802bdeca6e088d9036c5b4c17692517995ebcba9`. This review covers those complete invoked tail proofs, rather than asserting a new independent audit of every earlier BRD theorem.

The full moment matrices in CTR34 are finite by the Gamma exponential upper bound and positive definite because their weights are positive away from zero on an entire interval. The real-coefficient translation matrix in CTR35 has entry `binom(j,h)c^(j-h)(sqrt(-1))^h`; its triangular diagonal has modulus one. Consequently the congruence in CTR36 has no missing determinant or phase factor. No q rescaling occurs in this particular S-to-y change; the separate S-to-z factor in CTR30 remains as already proved.

The exact nonnegative tail correction in CTR37 is the determinant of the positive source after congruence by the **bulk** inverse square root. Factoring by that square root proves the stated logarithmic identity. Positivity of the omitted two forms gives nonnegativity; it does not alone give the small bound, which is supplied below.

The BRD contour rotation gives precisely `sigma(y)<=C_U exp(-|y|)`. Its reflection calculation gives `sigma(y)>=C_L/cosh(pi y)>=C_L exp(-pi|y|)`. The two Gamma factors in the reflection formula multiply to `2pi^2/cosh(pi y)`, and `Gamma(1/4)Gamma(3/4)=pi sqrt(2)` gives `C_U/C_L=1/sqrt(cos 1)`. Thus the constants in CTR39 apply to the unchanged y variable and sigma density. The complete BRD Legendre argument supplies the normalized basis on [1,2], the pointwise sum bound, and both exterior estimates used by CTR40.

The threshold `k>=2048 sqrt(d+g)` also implies the second BRD22 bound on the largest original f root: `t_(l-1)<k/2`, q>=k^2, and sqrt(d+g)>2 suffice. Hence both original forms in CTR35 meet the two actual BRD tail hypotheses, including their numerator degree. The common constants in CTR38 are valid for them by BRD30 and BRD37.

For the two new monomial reference forms, the proof independently retains the factor `q^(2q+2s+1)` on all regions. On [1,2] the displayed denominator has `C_L exp(-2pi q)`. The inner numerator contributes `epsilon^(2q+2s)8^(2q)`, so its common exponential base is `epsilon^2 8^2=2^-14`, strictly below the original `(4/3)2^-13` base. This proves the reference inner bound with the same kappa_I,r; it is not an application to an unidentified source.

For the reference far tail, `D_s=2q+2s+2r-2<=5q` since r<=q+1 and 2l<=q. The logarithmic tangent inequality at 64 proves the full integral constant `64^D_s exp(-64q)/(q-D_s/64)`, with denominator at least `59q/64` and a factor two for both tails. Bounding `2r-2<=2q` gives exponential rate

`64-2pi-5log64-2log(131/32)>20`.

Thus its coefficient is at most `128r^2 exp(-20q)/(59q sqrt(cos1))`, and r<=2q makes this at most the retained kappa_F with exp(-19q). This verifies the full reference-tail proof. The resulting positive-form inequalities give every one of the four t_H the common interval `[0,L_r]` in CTR44.

## Exact four-tail return and one-sided multiplication error: CTR45–CTR49

The remaining ratio of multiplication weights is the literal product `prod_j(1+t_j^2/y^2)`. On the bulk it lies in `[1,exp Delta_f]`; the same r-column Gram congruence therefore bounds its logarithmic determinant change in `[0,r Delta_f]`. This proves the one-sided sign of d_f without replacing the original f polynomial during the preceding chi transport.

Let A denote the bulk actual ratio, F the bulk radial ratio still containing f, and P the bulk monomial reference ratio. Then `d_chi=log A-log F`, `d_f=log F-log P`. Restoring the full determinants gives exactly the four signs in CTR47:

`d_chi+d_f+t_(chi,f)-t_(chi,0)-t_(pow,l)+t_(pow,0)`.

Each of the four tail corrections lies in `[0,L_r]`, so their signed sum lies in `[-2L_r,2L_r]`. Together with `|d_chi|<=E_chi,l` and `0<=d_f<=r Delta_f`, this proves both endpoints in CTR48. In particular **r Delta_f belongs only to the upper endpoint**. The finite comparison is for the full-line original relation ratio and full-line shifted-moment determinant ratio.

The elementary estimate `S2<=4l^3<=k^3/16`, r<=2q, and q>=e k^2 gives `r Delta_f<=k/(8e epsilon^2)`. The chi transport error is O(k/e), and `L_r<=r(kappa_I,r+kappa_F)` is exponentially decaying in q times the displayed polynomial factors. Hence the complete error is O(k)=o(q) at fixed original parameters and is O(1) for every fixed m>=2. These are the claimed CTR49 rates; no bulk restriction remains in its reference determinants.

## Exact sigma moments, mass, and final signed return: CTR50–CTR54

The Euler-product variable change used in CTR50 has

`u=w e^x/(2cosh x)`, `v=w e^(-x)/(2cosh x)`, and absolute Jacobian `w/(2cosh^2 x)`.

Combining this with `(uv)^(a-1)` gives the factor `2 w^(2a-1)(2cosh x)^(-2a)`. The w integral is Gamma(2a), so the displayed Fourier representation has exactly the factor `2 Gamma(2a)`. Fourier inversion, using the even integrand, gives `2 Gamma(2a)(2cosh t)^(-2a)`. At a=1/4 its mass is sqrt(2pi), and the characteristic function is `c_sigma(cosh t)^(-1/2)`. The stated smooth exponential decay justifies inversion; the Gamma upper bound supplies domination for each subsequent moment derivative.

The moments in CTR51 therefore have exactly the factor `(-1)^h` at derivative order 2h, with every odd moment zero. Comparing the coefficient of t^(2n-1) in `h' cosh+(h sinh)/2=0` gives the two binomial sums in CTR52: their indices are respectively `binom(2n-1,2j-1)` and `binom(2n-1,2j)`, with the c_n coefficient equal to one. The sample values c1=-1/2 and c2=7/4 check directly. This specifies every matrix entry by a finite rational recurrence.

For an even i+j, the rational moment entry is `(-1)^(a+(i+j)/2)c_(a+(i+j)/2)`; for odd i+j it is zero. Thus the mass is exactly one c_sigma per row, giving `det M_(a,r)=c_sigma^r det Q_(a,r)>0`. Both equal-dimensional determinants retain their mass factors before cancellation. The resulting reference is a positive rational determinant ratio, not an assumed asymptotic value.

Finally r=q and r=q+1 correspond precisely to original relation degrees 2q-1 and 2q. Substituting CTR47 in the existing identity `T_k=C_rel+log R_(2q-1)+log R_(2q)` gives CTR54 with both errors added and C_rel unchanged. The incoming Gamma return is `R_k^0-R_k^sigma=-T_k`, so reversing the entire expression is correct. No determinant asymptotic or RH conclusion is asserted by this substitution.

## Final acceptance

The complete CTR1–CTR54 source at the final hash above is accepted in its displayed finite-threshold and fixed-packet growing-family scope. The original coefficient maps, complete source and reference tails, all four signs, one-sided f correction, sigma mass, and signed return have been checked. There is no remaining mathematical discrepancy in the inspected source.
