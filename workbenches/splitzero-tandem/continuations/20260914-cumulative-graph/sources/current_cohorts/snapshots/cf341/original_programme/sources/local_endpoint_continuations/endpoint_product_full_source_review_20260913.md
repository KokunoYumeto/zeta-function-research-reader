# Independent full-source audit of the endpoint-product continuation

Date: 2026-09-13. This report accompanies the independent scalar review and its 2,453-check executable. The draft through EP.53 was read completely. The report below expands the source-to-radius, Schur, source-relation, and arithmetic-composition checks; the separate scalar report gives the full extremization proof. The final source hash and any subsequently added confluent-transfer formulas are bound in the completion record after the parent finishes those additions.

## 1. Source coordinates and the quotient

The original source uses S=c+iu, c=k/2, and the literal pairing integral conjugate(P(c+iu)) Q(c+iu) exp(theta u) m_{h,k}(u) du. All conclusions involving that source retain its original mass mu_h^k. Positivity almost everywhere makes every polynomial Gram positive definite: a nonzero polynomial has finitely many zeros on the integration line, so its nonnegative squared modulus is positive on a set of positive measure. The retained exponential moments justify every finite moment derivative with respect to a theta in the open admissible strip.

The reflection statement in EP.3 is exact. Define the conjugate-linear involution on the multivariable polynomial ring by conjugating coefficients and replacing each s_a by 1-s_a. Stability of the complete packet under rho -> 1-conjugate(rho) sends each generator h(s_a) to (-1)^{deg h} h(s_a), hence preserves their ideal. It preserves the sum-polynomial subring and sends S to k-S. Therefore it preserves the intersection ideal (chi). The transformed generator has leading coefficient (-1)^q; comparing monic generators gives conjugate(chi)(k-S)=(-1)^q chi(S). For real u this identity implies conjugate(i^{-q}chi(c+iu))=i^{-q}chi(c+iu). Thus the transported polynomial is real monic with no missing phase.

Monic polynomial division gives the kernel and surjectivity in EP.3. At N=q-1 the relation space is zero and the remainder map is the identity in the listed monomial coordinates. At N>=q the relation map is multiplication by chi from degree at most N-q. Its induced map on the leading-coefficient lines is an isomorphism only in this latter range: the leading coefficient of chi A equals the original leading coefficient of A. The draft was flagged to state N>=q explicitly for that graded assertion.

For K_N=J_N H_N^{-1} J_N^*, positivity follows from surjectivity of J_N: for nonzero quotient x, J_N^*x is nonzero and x^*K_Nx is positive. The formula R_N=H_N^{-1}J_N^*G_N gives J_NR_N=I. Since J_N B_N=0, one has B_N^*H_NR_N=0. Expanding the squared source norm of R_Nx+B_Ny gives exactly x^*G_Nx+y^*B_N^*H_NB_Ny. This proves the least-lift formula and monotonicity under enlargement of the source space. In the monic orthogonal basis, the inverse Gram is the diagonal matrix of 1/omega_j; applying the remainder map produces the full kernel sum in EP.5.

The transport Phi[P]=[P(c+iu)] has inverse [Q]->[Q((S-c)/i)]. The defining ideals correspond because chi(c+iu)=i^q widehat(chi)(u). In quotient coordinates its triangular matrix E has determinant i^{q(q-1)/2}, of modulus one. Thus the transported Gram is E^{-*}G_NE^{-1}, and its determinant equals V_N exactly. This proves the volume invariance under the stated isomorphism without changing a source density.

## 2. Complete check of the radius identity and its phase

Let Q_j=i^{-j}p_j(c+iu). These are the unique real monic orthogonal polynomials for the real positive source density. Multiplication by u is symmetric in this pairing. The coefficient of Q_{j-1} in uQ_j is omega_j/omega_{j-1}, because its inner product with Q_{j-1} equals the inner product of Q_j with uQ_{j-1}, whose leading degree-j term is Q_j. All lower terms vanish by orthogonality. Transporting the resulting recurrence back to S multiplies the lower coefficient by i^2=-1. Hence the negative lower coefficient in EP.8 is correct.

In the real coordinates put d_j=[Q_j], retaining the actual Gram G and least lift R_N. Differentiating the minimum norm at fixed quotient x eliminates the derivative of R_N because J_N R_N'=0 and R_N is orthogonal to that kernel. It gives G'=R_N^* u R_N in the source pairing. The leading coefficient of R_Nx is d_N^*Gx/omega_N: expanding R_N in the orthogonal basis gives coefficient d_j^*Gx/omega_j on Q_j.

The polynomial

\[
uR_Nx-R_NTx-(Q_{N+1}-R_Nd_{N+1})d_N^*Gx/\omega_N
\]

has degree at most N and zero remainder. Pairing it with R_N, using R_N^*Q_{N+1}=0, gives

\[
G'=GT-Gd_{N+1}d_N^*G/\omega_N.
\]

Taking the trace after multiplication by G^{-1} gives (log V_N)'=Tr T-d_N^*Gd_{N+1}/omega_N. The quotient data and Gram are real in these coordinates, so the displayed scalar is real. Since Phi b_j=i^j d_j, the cross term in the original coordinates is b_N^*G_Nb_{N+1}=i omega_N phi_N. This proves every phase and sign in EP.9.

For the rank-one updates, subtracting the last term from K_N gives

\[
\det K_{N-1}=\det K_N\left(1-b_N^*G_Nb_N/\omega_N\right).
\]

Its left-to-right determinant ratio is V_N/V_{N-1}=delta_N. Adding the next term to K_N similarly gives det K_{N+1}/det K_N=delta_{N+1}^{-1}. Thus both formulas EP.6 follow with their stated orientations.

Substitute the complete recurrence in A K_N+K_N A^*. Every negative lower term -b_{j-1}b_j^*/omega_{j-1} cancels the preceding positive upper term, with its adjoint canceling likewise. The diagonal recurrence terms sum to 2cK_N because their imaginary parts are conjugates. The only remaining upper pair is (b_{N+1}b_N^*+b_Nb_{N+1}^*)/omega_N. Multiplication by G_N on both sides and congruence by G_N^{-1/2} gives exactly the relative defect in EP.10.

Write x=G_N^{1/2}b_N, y=G_N^{1/2}b_{N+1}. Then x^*y=i omega_N phi_N is purely imaginary and

\[
\operatorname{Tr}(xy^*+yx^*)=0,
\]

\[
\operatorname{Tr}(xy^*+yx^*)^2
=2\|x\|^2\|y\|^2+2\operatorname{Re}((x^*y)^2)
=2\|x\|^2\|y\|^2-2\omega_N^2\phi_N^2.
\]

The Hermitian matrix has rank at most two and trace zero. If it has nonzero eigenvalues, they are an opposite pair; its squared radius is half its squared trace norm in the displayed expansion. At q=1 the defect is identically zero and no second eigenvalue is introduced. Substituting EP.6 proves epsilon_N^2+phi_N^2=(omega_{N+1}/omega_N)(1-delta_N)(delta_{N+1}^{-1}-1). Thus the identity used by the scalar optimization is derived from the original source and quotient.

## 3. Scalar statements and quantitative loss

EP.12-EP.18 and EP.21-EP.31 agree with the complete independent scalar proof R1-R18. The independent executable checks exact rational identities, fixed-budget perturbations, fixed-endpoint perturbations, and phase thresholds; its checks do not presume arithmetic realization of the scalar extremizers. Its receipt binds both unmodified runs and ten deliberate formula-mutation runs.

The extra quadratic loss EP.20 is also valid. With t in (0,1), every v_j=-log d_j and their mean lies in (0,-log t]. For f(v)=log(1-exp(-v)), one has

\[
-f''(v)=\frac{e^{-v}}{(1-e^{-v})^2}\ge\frac{t}{(1-t)^2}.
\]

Indeed e^{-v}>=t, and z/(1-z)^2 is increasing on (0,1), with derivative (1+z)/(1-z)^3>0. Integrating the derivative twice about the mean gives the tangent inequality with negative remainder -t(v-mean)^2/(2(1-t)^2). Summing cancels the linear terms. This proves the stated lower bound on the exact loss, with coefficient and sign intact. At s=1 its variance is zero. At any unit interior contraction the product vanishes and the logarithmic expression is omitted, as the draft requires.

The computational root equation EP.31 follows by exponentiating EP.25, with no approximation. The actual endpoint ratio R need not be rational. The draft was flagged to restrict integer-product equality checks to rational R and to describe the general arithmetic case through certified rational enclosures R_-<=R<=R_+. Because B(x), and hence R(x), is strictly increasing, these bounds transport to corresponding root bounds. The exact equation remains true for arbitrary real R>=1.

## 4. Schur endpoint coordinates

Let A=H_{n-1} and write the source block as [[A,C],[C^*,D]]. The determinant-one triangular coordinate map Q=[[I,-A^{-1}C],[0,I]] satisfies Q^*H_mQ=diag(A,W), W=D-C^*A^{-1}C. It also satisfies J_mQ=[J_{n-1},F], with the F in EP.32. Thus inverse congruence gives K_{n+j-1}=K_{n-1}+F_jW_j^{-1}F_j^* for each prefix, and the determinant identity yields R_j=det(W_j+Z_j)/det W_j. All W_j are positive definite because they are restrictions of W>0.

Identify a 1-by-1 matrix with its sole scalar entry explicitly. Then write w=(W_1)_{11}, e=w+(Z_1)_{11}, p=det W_r, s=det W_{r+1}, H_-=det(W_r+Z_r), H_+=det(W_{r+1}+Z_{r+1}). Successive source determinant ratios give omega_n=w and omega_m=s/p. Direct substitution now gives

\[
U=\frac{s}{pw},\quad
\alpha=\frac we,\quad
\beta=\frac{H_-s}{pH_+},\quad
t=\frac{ep}{wH_-},
\]

\[
U\frac{V_n}{V_m}=\frac{H_+}{pe},\qquad
\mathcal B=\log\frac{H_-H_+w}{pse}.
\]

For example R_1=e/w, R_r=H_-/p, and R_{r+1}=H_+/s. Thus V_n/V_m=R_{r+1}/R_1, while exp(B)=R_r R_{r+1}/R_1. These substitutions verify every numerator and denominator in EP.35. At r=1, p=w and H_-=e, so t=1, and the separate one-step expression is used. At n=q the base source has exactly q monomials and no boundary columns; J_{q-1}=I, hence G_{q-1}=H_{q-1}, as stated.

## 5. Determinants and the receiving relation

In degree N, the coefficient matrix formed from the q quotient monomials followed by chi,S chi,...,S^{N-q}chi has diagonal entries all one. Replacing its quotient columns by R_N subtracts boundary combinations and leaves determinant one. The resulting columns are source-orthogonal across the two blocks. Consequently det H_N=det G_N det(B_N^*H_NB_N), proving V_N=D_{N+1}/B_{N-q+1}. Orthogonal monic triangularization similarly gives omega_N=D_{N+1}/D_N. Their literal quotient is Lambda_N=B_{N-q+1}/D_N; the cancellation in EP.37-EP.38 has the correct indices.

For the multidegree relation layer let T have columns p_{i+1},...,p_j, F their remainders, and b=T-R_iF. The remainder of each column is zero. Each column is orthogonal to D_i because its first summand is orthogonal to P_i and its second summand is orthogonal to D_i. Its highest degree is i+a with coefficient one. Thus the j-i columns are independent. Since dim D_j-dim D_i=j-i and D_i is a positive subspace of D_j, dim(D_j intersect D_i^perp)=j-i, proving that b is an isomorphism onto the stated relation layer. Orthogonality of T and R_i gives its Gram Omega+F^*G_iF.

The kernel sum adds F Omega^{-1}F^* to K_i. The determinant identity then proves EP.45, using the positive semidefinite matrix Omega^{-1/2}F^*G_iF Omega^{-1/2}. In the window (q,2q) it has size q by q, so its largest eigenvalue exists even when all eigenvalues are zero. The draft was flagged to define lambda_max using this full matrix, since the preceding displayed list included only positive eigenvalues.

The representative formula EP.47 has the positive sign shown. Indeed b^*R_i=-F^*G_i, so subtracting the orthogonal projection of R_i onto the new relation layer is

\[
R_i-b(b^*b)^{-1}b^*R_i
=R_i+b(\Omega+F^*G_iF)^{-1}F^*G_i.
\]

The image remains a lift of the same quotient because J_jb=0. It is orthogonal to both old and new relations and hence equals R_j by the already proved uniqueness.

For the cochain formula, the equality chi(sum s_a)=sum_a h(s_a)Q_a belongs to the exact kernel ideal and is obtained by division by the monic h(s_a) in all variables. Applying the commuting D_a gives the same identity of differential operators on the source tensor. In the a-th summand the one degree-zero entry phi_0 is preceded by a-1 degree-one source entries, so the tensor differential contributes (-1)^{a-1}; this cancels the prefactor in EP.48. Its differential is therefore the original V_{h,k}(chi kappa) with positive sign. The quotient image is the receiving fibre's supported zero, while the external absence is preserved by its separately stated map.

## 6. Arithmetic consequence and dependency precision

I read the complete independent arithmetic analytic review, which in turn retains the raw analytic source and proves its constant. Its literal C_h agrees with EP.40, including the factor-two estimate for the two Laplace moments inside the leading constant 64. The product continuation uses that proved theorem as a source dependency; the scalar checker is not presented as its proof.

For the exact quartet, the exterior allowance L is positive at all k>=1, and q_k>=k. On n=r=q_k with k>=3, every radius identity gives f_j>0 because epsilon_{q+j}>=L>0. Consequently all d_0,...,d_q are strictly below one, and every logarithm in EP.42 is defined. The exact product gives

\[
\log\frac{V_q}{V_{2q}}
=\log K-\log U-\log(1-d_0)-\log(1-d_q)
 -2\sum_{j=1}^{q-1}\log(1-d_j).
\]

At every index, epsilon_{q+j}^2+phi_{q+j}^2>=L^2(1+phi_{q+j}^2/L^2), while log U<=2q log(C_hq). Substitution proves precisely EP.42. The contraction penalties are nonnegative and in fact strictly positive. Dividing the first term by q log k and using L/q>=delta k/2 yields 2+2 log(delta/(2C_h))/log k, whose limit is two. This proves the stated lower-limit threshold for log(V_q/V_{2q}). The actual phase terms and contraction penalties remain in the stronger finite inequality.

The determinant lower bound Lambda_{2q}/Lambda_q>=L^{2q} follows independently by raising EP.38 to the positive power 2q and using L<=E_*. For the relation matrix, its determinant is at most (1+lambda_max)^q because each of its q eigenvalues is at most lambda_max. Combining with V_q/V_{2q}>=(L/(C_hq))^{2q}, and taking positive q-th roots, yields lambda_max>=(L/(C_hq))^2-1. This proves EP.46 also when the latter bound is negative, because the full matrix is positive semidefinite.

The signed boundary formula is exact:

\[
\mathcal B-2\log(V_n/V_m)
=\log\frac{V_{n-1}V_m}{V_nV_{m-1}}
=\log(\beta/\alpha).
\]

No lower bound on this signed term follows solely from the two-volume threshold. The separate monotonicity inequality EP.50 is valid: subtracting twice the central log ratio gives log(V_{q-1}/V_q)+log(V_{2q-1}/V_{2q})>=0. Its norm input belongs to the stated balanced-window continuation, which must remain a bound source dependency for any stronger arithmetic conclusion made there.

## 7. Literal-mass Gaussian calibration checked by hand

For the mass-seven Gaussian, reduction modulo u^2+1 gives the first six Hermite columns

\[
b_0=(1,0)^T,\ b_1=(0,1)^T,\ b_2=(-2,0)^T,
b_3=(0,-4)^T,\ b_4=(10,0)^T,\ b_5=(0,26)^T.
\]

With omega_j=7j!, their kernel sum gives

\[
K_1=\operatorname{diag}(1/7,1/7),\quad
K_2=\operatorname{diag}(3/7,1/7),\quad
K_3=\operatorname{diag}(3/7,11/21),
\]

\[
K_4=\operatorname{diag}(43/42,11/21),\quad
K_5=\operatorname{diag}(43/42,93/70).
\]

Inversion proves G_2,G_3,G_4 and all five volumes in EP.52, including V_5=(42/43)(70/93)=980/1333. The relative defect for diagonal G is the congruence of i(GT-T^TG), giving squared radius (g_0+g_1)^2/(g_0g_1). Substitution gives 16/3,400/99,4225/946. The norm endpoint ratio is omega_5/omega_2=5!/2!=60. The endpoint ratios compute to alpha=1/3, beta=110/279, and t=54/473. These calculations independently reproduce EP.52-EP.53 without assigning a quotient Gram.

The coordinate relation is chi(S)=(S-1/2)^2-1, since its image on S=1/2+iu is -(u^2+1). The matrix E=[[1,1/2],[0,i]] is exactly the substitution on coefficients; G^S=E^*G^uE and |det E|=1 follow directly. Reflection of the literal even Gaussian sends theta to -theta through the same diagonal parity change in source and quotient monomials, so V_N(theta) is even. At zero tilt its derivative vanishes, and Tr T=0, proving phi_N=0. Thus the computed defect and the product radius identity concern the same allowance.

## 8. Corrections communicated before finalization

Five precision repairs were sent to the parent, without editing its source: explicitly extract the scalar entries of W_1 and Z_1; define lambda_max on the full matrix including zeros; describe the nonzero opposite eigenvalue pair without forcing two entries at q=1; restrict the graded line isomorphism to N>=q; and distinguish rational endpoint input from rational enclosures of a general real endpoint input. These do not change the claimed scalar optimizer, radius formula, determinant bridges, or arithmetic lower threshold. Their final insertion and the new confluent-transfer section are to be checked against the final source bytes.

## 9. Complete confluent-transfer addition EP.38a-EP.38k

The entire newly added section was subsequently read. Under reflection stability, psi=i^{-q}chi(c+iu) is real monic of degree q, and Pi=psi^2 has degree d=2q. The full derivative map at each distinct root zeta_a, with orders zero through r_a-1 for r_a=2 ell_a, has kernel (Pi): vanishing of those derivatives is precisely divisibility by each (u-zeta_a)^{r_a}, and their pairwise coprimality makes their product divide the polynomial. Leibniz's formula supplies each binomial coefficient for multiplication of raw jets. Differentiating u f supplies the block formula zeta_a v_e+e v_{e-1}; no divided-derivative convention has been introduced.

The substitution derivative is exactly d_u^e P(c+iu)=i^e P^{(e)}(c+iu). At u=zeta_a=(lambda_a-c)/i this becomes i^e P^{(e)}(lambda_a). Since Phi(chi^2)=i^{2q}Pi, it induces the quotient isomorphism in EP.38b. These calculations preserve all factorials and phases.

For the raw Vandermonde, order the monic columns by successive polynomials

\[
P_{a,e}(u)=\prod_{b<a}(u-\zeta_b)^{r_b}(u-\zeta_a)^e,
\quad 0\le e<r_a.
\]

Their degrees run through zero,...,d-1 and their leading coefficients are one, so their coefficient transformation has determinant one. Every derivative row belonging to b<a vanishes on a column P_{a,e}. Within the diagonal block a, the derivatives of orders below e vanish, and the e-th derivative equals e! product_{b<a}(zeta_a-zeta_b)^{r_b}. Thus the jet matrix is triangular across blocks with these diagonal values. Multiplying first over e and then over a yields product_a product_e e! times product_{b<a}(zeta_a-zeta_b)^{r_ar_b}, exactly EP.38d in its stated node order. At a=0 the orthogonal column basis has determinant-one monic coefficient transform, so det F_0=det V; equality of matrices is not needed.

For any a>=0, suppose a linear combination Q of Q_a,...,Q_{a+d-1} has zero full jets. Then Q=Pi H, with deg H<a. If a=0, the degree already forces Q=0. Otherwise source orthogonality gives <H,Q>=0. Since Pi=psi^2 is nonnegative and positive away from finitely many real points,

\[
0=\langle H,Q\rangle=\int\Pi(u)|H(u)|^2d\mu_\theta(u)
\]

forces H=0 and hence Q=0. Thus F_a is invertible. The quotient in EP.38e exists by its zero full jets, is monic of degree a, and is orthogonal for Pi dmu_theta to every polynomial of degree below a. Its unique real monic representative is the one displayed.

To compute its literal norm, pair its numerator Pi widehat(Q)_a with widehat(Q)_a. The terms Q_{a+d} and Q_{a+j} with j>0 are orthogonal to every degree-a polynomial, while <widehat(Q)_a,Q_a>=omega_a because both polynomials are monic degree a. Therefore nu_a=-(z_a)_0 omega_a>0, checking the minus sign in EP.38f. The original relation polynomial chi(S)i^a widehat(Q)_a((S-c)/i) is monic degree a+q; its value on the source line is i^{a+q} psi(u)widehat(Q)_a(u). Its squared norm is exactly nu_a because the squared modulus of the phase is one and psi is real here.

The shifted column matrix [e_1,...,e_{d-1},z_a] has determinant (-1)^{d-1}(z_a)_0. Since d is the even integer 2q, this is -(z_a)_0=nu_a/omega_a. Multiplying successive determinant ratios proves

\[
\det F_a/\det V=\prod_{j=0}^{a-1}\nu_j/\omega_j
=\mathfrak B_a/\mathfrak D_a.
\]

The final identity follows from monic orthogonal triangularization of the source and the relation Gram, in the original coordinates. The relation transformation carries its explicit unit-modulus i^q factor, so it changes no determinant norm. Substitution with a=N-q+1 gives EP.38h and the two-transfer determinant ratio EP.38i; the source norm band has q-1 factors and is empty when q=1. Its positivity follows from the proved equality to Lambda_m/Lambda_n, retaining the complex Vandermonde phase in each uncanceled expression.

Multiplication by u in the full jet space is X_Pi. Conjugating it by F_a gives T_a, and the shifted basis gives T_{a+1}=K_a^{-1}T_aK_a. The source recurrence at index a+d-1 yields the stated last-column z_a because the previous column is e_{d-2}. The index is defined since d>=2. For j>=1, differentiation of orthogonality gives partial_theta Q_j=-(omega_j/omega_{j-1})Q_{j-1}: all lower pairings vanish and the pairing with Q_{j-1} equals -omega_j. At j=0 the derivative is zero; the draft was flagged to say this explicitly instead of formally introducing omega_{-1}.

The norm derivative is partial_theta log omega_j=a_j^{(0)}. In F_a', internal derivatives shift a column into the preceding column and therefore have zero matrix trace. The first column contributes only -(omega_a/omega_{a-1})v_{a-1}e_0^T for a>=1. Consequently

\[
\partial_\theta\log\det F_a
=-\frac{\omega_a}{\omega_{a-1}}e_0^TF_a^{-1}v_{a-1},
\]

with the term omitted at a=0. Differentiating EP.38h proves the positive last term in EP.38j. A local logarithm of det F_a suffices; its constant node-dependent phase drops from the derivative because det F_a/det V is positive. This supplies the phase through the same original source jets.

For a positive Gamma reference using exactly the same Pi and raw derivative rows, divide the two copies of EP.38g. The common Vandermonde cancels literally, giving det F_a/det F_a^Gamma=Y_a/X_a. The volume formula similarly gives V_N/V_N^Gamma=X_{N+1}/Y_{N-q+1}. No relation between different node orders or different jet conventions is assumed.

The largest polynomial in F_a for a=N-q+1 has degree a+d-1=N+q. Monic orthogonal projection to obtain that polynomial uses moments through degree 2(N+q)-1. The invariant endpoint Gram at degree m uses moments only through 2m. The determinant formula proves the cancellation in the invariant, while retaining the possibly larger input needed for individual raw entries; it does not erase those entries or declare them unrelated.

### Exact general norm-transfer correction

For a non-reflection-stable chi the valid positive norm multiplier is Pi=conjugate(psi)psi. This changes the doubled original jet ideal, not the original relation polynomial. Define

\[
\chi^\dagger(S)=(-1)^q\overline\chi(k-S).
\]

It is monic of degree q and satisfies

\[
\Phi(\chi^\dagger)=i^q\overline\psi,
\qquad \Phi(\chi^\dagger\chi)=i^{2q}\overline\psi\psi.
\]

Indeed conjugate(psi)(u)=(-i)^{-q}conjugate(chi)(c-iu), and multiplying by i^q gives (-1)^q conjugate(chi)(c-iu), exactly the substituted chi^dagger. Therefore the full norm-jet isomorphism is

\[
\mathbb C[S]/(\chi^\dagger\chi)
\xrightarrow{\ [P]\mapsto[P(c+iu)]\ }
\mathbb C[u]/(\overline\psi\psi),
\]

with the same inverse substitution and derivative phases i^e. Its nodes are the combined roots of psi and conjugate(psi), with orders added at overlaps. The relation multiplier remains chi; its original norm is the positive form |psi|^2 dmu_theta. The positivity, division, norm, and determinant proofs above therefore give the general norm transfer through this exact changed jet ideal. The radius proof retains its explicitly stated reflection condition. This correction was sent to the parent before final source binding; applying EP.38b unchanged with chi^2 in the general case would have been false.

## 10. Final spectral expansion and balanced-window EP.50a-EP.50f

The subsequently added finite spectral proof after EP.41 was read completely. In a tensor local algebra the highest nonzero power of z_1+...+z_k has degree k(m_0-1) and coefficient [k(m_0-1)]!/[(m_0-1)!]^k on the one top monomial. It is nonzero in characteristic zero. All higher powers vanish by the exponent bound in at least one variable. The local annihilator order is therefore exactly 1+k(m_0-1).

For each count pair 0<=a,b<=k, a contingency table of the four sign combinations exists because its upper-left entry can be any integer between max(0,a+b-k) and min(a,b). The interval is nonempty: a+b-k<=a and <=b since a,b<=k, and both a and b are nonnegative. Thus all (k+1)^2 centres occur. Their real and imaginary coordinates distinguish them because delta,gamma>0. The least common multiple of the local annihilators has the stated degree q_k.

The Schur triangularization can order eigenvalues with positive real part first by choosing those eigenvectors successively in the usual inductive upper-triangular construction. Conjugation by G_N^{1/2} gives the Euclidean representative of A-cI. The Hermitian sum is exactly the relative defect already proved to have the opposite nonzero pair. Its trace on the coordinate subspace for the positive-real diagonal entries is twice their total real part. In an eigenbasis of the Hermitian sum, this compressed trace equals epsilon_N <Pe_+,e_+>-epsilon_N <Pe_-,e_-><=epsilon_N. This proves the exterior bound directly, with all local multiplicities retained. Summing the positive terms 2a-k yields floor((k+1)^2/4): for even k=2l the sum is 2(1+...+l)=l(l+1); for odd k=2l+1 it is 1+3+...+(2l+1)=(l+1)^2. Those are exactly the respective floor values. This independently verifies the formula and inequality for L_{h,k}.

The entire retained `endpoint_product_dependencies_20260913/FOUR_VOLUME_THRESHOLD.md` was read. Its balanced norm constant is exactly the one in EP.50b. To check its factors directly, combine the upper endpoint at n+r with the original lower envelope and the exact Legendre norm at n, as in the analytic review. Use

\[
(2(n+r))!\le(4n)^{2(n+r)},\quad
M_h(b)^k+M_h(-b)^k\le2M_*^k,
\]

\[
\mathfrak l_n(n)\ge\frac{2n^{2n+1}}{(2n+1)4^n},\quad
\vartheta_h^{-(k-3)}\le K_h^k,
\quad K_h=\max(1,\vartheta_h^{-1}).
\]

After the positive 2r-th root, the factorial, Legendre, and literal factor two give precisely

\[
4n\,8^{n/r}\left(\frac{2n+1}{c_hn}\right)^{1/(2r)}.
\]

Indeed the powers of four are 4^{3n+2r} before the root, and the powers of n are n^{2r-1}; the remaining factor (2n+1)/c_h is retained inside the root. The other factors are

\[
b^{-(n+r)/r}(M_*K_h)^{k/(2r)}
 e^{\pi(n+k-3)/(4r)}(2n)^{B_h/(2r)}.
\]

For n>=k>=3 and n/2<=r<=n, these are bounded respectively using n/r<=2, (n+r)/r<=3, k/(2r)<=1, (n+k-3)/(4r)<=1, and (2n+1)/n<=3. Thus the first constant is at most 256 max(1,3/c_h), the mass factor is at most M_*K_h, and the exponential factor is at most exp(pi). The function log(2n)/n decreases for n>=3 because its derivative is (1-log(2n))/n^2<0. Hence (2n)^{B_h/(2r)}<=6^{B_h/3}. The b factor is at most max(1,b^{-3}), both when b<=1 and when b>1. Their product proves exactly EP.50a-EP.50b with the stated literal constant.

On the exact-quartet window n=q_k,r=q_k-1, all these conditions hold: q_k>1, q_k>=k>=3, and q_k-1>=q_k/2. Apply the already proved exact product and L bound at these q_k-1 indices. Every radius is positive, so all contractions appearing in EP.50c are strictly below one. The same logarithmic calculation as Section 6 gives the stated endpoint terms, the factor two on every interior contraction, and the phase sum with upper index q-2.

The full four-volume logarithm equals twice this central cost plus log(V_{q-1}/V_q)+log(V_{2q-1}/V_{2q}). The two extra terms are nonnegative. Therefore its lower bound is at least

\[
4(q_k-1)\left[\log k+\log(\delta/(2C_h^{\rm bal}))\right].
\]

Division by q_k log k gives the threshold four, since q_k tends to infinity. The relation matrix for the central interval has size q-1, so padding its eigenvalue list to that full size and applying the same determinant bound yields exactly EP.50f. No upper estimate for the growing arithmetic relation matrix follows from these lower bounds; the exact source and relation maps in Sections 4-5 identify the quantity that remains to be estimated.

## 11. Complete primary-checker audit

The full `endpoint_product_check_20260913.py` was read. It derives the source monic polynomials by exact rational orthogonal projection, computes original S-coordinate moment Grams and monic division matrices, forms K_N and G_N by the stated constrained minimum, and calculates the phase from the differentiated source Gram. The Gaussian q=2, Gaussian q=1, and positive asymmetric atomic q=2 fixtures therefore reach the radius identities through source data. The atomic measure has nineteen distinct real support points with positive integer weights; every polynomial degree used for its norm checks is below nineteen, so its positive Gram assertions are valid. Its nonzero phase makes removal of the phase term a concrete formula mutation.

The window checks multiply the independently calculated radii, build the source Schur block and each prefix, compare every endpoint coordinate, and separately compute the source-relation determinant ratio from multiplication by chi. The raw-jet tests use repeated first derivative jets at both roots of u^2+1 and also a literal second-derivative calibration that detects removal of the factorial. They check divisibility, transformed monic relation norm, determinant product, and the two-transfer window. Those are finite auxiliary checks; they do not evaluate an arithmetic zero packet or C_h.

The root certificate bisects the monotone algebraic equation for the budget optimizer with rational endpoints and ninety iterations, then encloses the positive 2r-th root. Its map F_max(x) is increasing on (0,1/2): the numerator increases there and both positive denominator factors decrease. Thus the outer two root calculations give a valid enclosure of the final bound. The decimal midpoint is explicitly described as orientation only, while the rational endpoints are retained in the certificate.

The retained replay has fourteen runs, each executing 415 checks. The normal and optimized unmodified runs have no failures. Each of six formula mutants rejects in both modes: mass, six failures; interior multiplicity, thirteen; beta orientation, twenty-five; Schur ratio, twenty-six; phase, five; raw factorial, two. The binding script verifies every recorded result hash, actual checker hash, count, mode, mutation, and full equality of the paired normal/optimized check and certificate records. This review did not rerun the primary checker; it reviewed the executed records and the complete code. The separate independent scalar checker was actually run by this review lane in both modes and all five of its concrete mutations.

## 12. Final rational display, source pin, and completed corrections

The final addition EP.54 and the verification paragraph were read. Its budget input is R=630509/1080 and its original norm ratio is U=60, both equal to the independently computed mass-seven window values. The primary result retains

\[
x_- =\frac{1074648601054021601908361577}{2475880078570760549798248448},
\quad
x_+ =\frac{537324300527010800954180789}{1237940039285380274899124224}.
\]

Let R(x)=(1+2x)(1+x)^4/((1-2x)(1-x)^4) and F(x)=(2x)^6/((1-4x^2)(1-x^2)^2). Both are strictly increasing on (0,1/2), as their positive numerator factors increase and their positive denominator factors decrease. The binding script independently evaluates the exact Fraction inequalities R(x_-)<=630509/1080<=R(x_+), together with

\[
\left(\frac{719736229856370310835738215}{2^{88}}\right)^6
\le60F(x_-),\qquad
60F(x_+)\le
\left(\frac{719736229856370310835738217}{2^{88}}\right)^6.
\]

They imply the displayed EP.54 by the positive-root monotonicity. The decimal is explicitly orientation only. These recorded integer/rational comparisons verify the actual printed bounds directly rather than treating the decimal as a certificate.

All seven communicated repairs were directly checked in the final source: the 1-by-1 Schur entries, the full eigenvalue list, the q=1 rank-zero wording, the N>=q graded map, rational enclosures for real R, the j=0 theta derivative, and the non-reflection doubled ideal chi chi^dagger. The complete reviewed source through EP.54, including EP.38a-EP.38k and EP.50a-EP.50f, is pinned to SHA-256 `b4f9481976ad03bb8e321464f937d3777af15581241ece1f78aaa5c56e49b924` in the full-source review receipt. The source is not edited by this reviewer. The binding receipt distinguishes mathematical proof review, source/result hash checks, exact rational certificate checks, and the separate finite checker executions.
