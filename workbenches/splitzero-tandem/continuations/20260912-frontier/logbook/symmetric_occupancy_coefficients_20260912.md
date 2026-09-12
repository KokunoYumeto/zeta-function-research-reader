# Symmetric occupancy coefficients: complete finite proof and audit

Date: 2026-09-12. Bounded independent audit for the symmetric/Koszul integration.

Read in full: `output/split_zero_rh_tandem_2026-09-12/sources/web_symmetric_frontier_delivery/Tau_Symmetric_Frontier_Control/NOTE.tex`, especially Sections 5–6 and the frontier factorization in Sections 3–4. This report does not alter that source or the main paper.

## 1. Objects, full algebraic multiplicities, and exact coordinate maps

Let $E$ be a complex vector space of dimension $d\ge1$, let $A:E\to E$, and let

\[
 A_k=\sum_{j=1}^k1^{\otimes(j-1)}\otimes A\otimes1^{\otimes(k-j)}.
\]

The space here is the invariant subspace $E_k^{\mathrm{sym}}=(E^{\otimes k})^{S_k}$, with its ordinary permutation action in top degree. Its inclusion is the actual map $I_k:E_k^{\mathrm{sym}}\hookrightarrow E^{\otimes k}$ of the source. The signed chain projector of Section 5 restricts to the ordinary average in that degree. Write $A_k^{\mathrm{sym}}$ for the restriction. For $k=0$, set $E_0^{\mathrm{sym}}=\mathbb C$ and $A_0=0$.

Choose a basis $e_1,\ldots,e_d$ and retain it. For $n=(n_1,\ldots,n_d)\in\mathbb N^d$, $|n|=k$, define

\[
 v_n=\sum_{\text{distinct permutations}}e_1^{\otimes n_1}\otimes\cdots\otimes e_d^{\otimes n_d},\qquad
 D_n=\frac{k!}{\prod_i n_i!}.
\]

The vectors $v_n$ have disjoint supports in the tensor basis and form a basis of the invariant subspace. Indeed an invariant tensor has one common coefficient on each orbit. Thus

\[
 N_{d,k}:=\dim E_k^{\mathrm{sym}}=\binom{k+d-1}{d-1}.
\]

The quotient map $q:E^{\otimes k}\to\operatorname{Sym}^kE$ sends $v_n\mapsto D_n e_1^{n_1}\cdots e_d^{n_d}$. This is the exact invertible diagonal coordinate comparison with the ordinary monomial presentation, and no orbit factorial has been removed. In the source's Euclidean tensor coordinates $I_k^*I_k=\operatorname{diag}(D_n)$, so the coefficient extraction map is $L_k=\operatorname{diag}(D_n^{-1})I_k^*$.

If $Ae_j=\sum_i a_{ij}e_i$, direct counting gives the full operator, including off-diagonal directions:

\[
 A_k^{\mathrm{sym}}v_n
 =\Big(\sum_i n_i a_{ii}\Big)v_n
 +\sum_{i\ne j,\ n_j>0}(n_i+1)a_{ij}v_{n-e_j+e_i}. \tag{1}
\]

To prove the coefficient, the input orbit has $D_n$ tensors and each has $n_j$ sites of type $j$. The output orbit has $D_{n-e_j+e_i}=D_n n_j/(n_i+1)$ tensors. Equivariance makes the coefficient on all output tensors equal; dividing the number of contributions gives $n_i+1$. A diagonal site contributes $n_i a_{ii}$. Under the displayed diagonal comparison $q$, the coefficient becomes $n_j a_{ij}$, as required in the monomial presentation. These are two exactly conjugate presentations, not interchangeable coefficients in one presentation.

Let $\rho_1,\ldots,\rho_d$ be the eigenvalues of $A$, listed with algebraic multiplicity, and define

\[
 \delta_i=\Re\rho_i-\tfrac12,\qquad \Delta_i=2\delta_i=2\Re\rho_i-1.
\]

Every formula below states which convention it uses. Triangularizing $A$ and applying (1) triangularizes $A_k^{\mathrm{sym}}$; all eigenvalues, with algebraic multiplicity, are

\[
 \lambda_n=\sum_i n_i\rho_i,\qquad |n|=k. \tag{2}
\]

Triangularization does not discard the off-diagonal action: it is exactly (1) after the induced invertible tensor coordinate map. Consequently

\[
 \det(zI-A_k^{\mathrm{sym}})=\prod_{|n|=k}\left(z-\sum_i n_i\rho_i\right). \tag{3}
\]

For the actual quotient $E=\mathbb C[t]/h$, the exact comparison to local coordinates is the Chinese remainder map

\[
 [P]\longmapsto\left(\sum_{j=0}^{m_\rho-1}\frac{P^{(j)}(\rho)}{j!}\varepsilon_\rho^j\right)_\rho,
 \qquad E\xrightarrow{\sim}\bigoplus_\rho\mathbb C[\varepsilon_\rho]/\varepsilon_\rho^{m_\rho}.
\]

Its inverse is unique Hermite interpolation of degree less than $d$. Multiplication by $t$ becomes multiplication by $\rho+\varepsilon_\rho$, hence the original raising convention $N_\rho e_j=e_{j+1}$, with $N_\rho e_{m_\rho-1}=0$, is retained.

## 2. Occupancy moments, including both edge cases

Use the convention $\binom{a}{b}=0$ for integers $a\ge0,b>a$, and put

\[
 B_1=\binom{k+d-1}{d},\qquad B_2=\binom{k+d-1}{d+1}.
\]

For every $i$, and every distinct $i,j$,

\[
 \sum_{|n|=k}n_i=B_1,\qquad
 \sum_{|n|=k}n_i(n_i-1)=2B_2,\qquad
 \sum_{|n|=k}n_in_j=B_2. \tag{4}
\]

Proof: the ordinary generating series of the first sum is

\[
 \left(\sum_{r\ge0}r q^r\right)(1-q)^{-(d-1)}=q(1-q)^{-(d+1)}.
\]

The factorial second moment has series $2q^2(1-q)^{-(d+2)}$. The mixed moment has series $q^2(1-q)^{-(d+2)}$. Extracting $q^k$ yields (4). These equalities follow directly by differentiating the geometric series as formal series, so require no convergence assertion.

Writing $S_1=\sum_i\delta_i$ and $S_2=\sum_i\delta_i^2$, expansion of the square now gives the exact formulas

\[
 \sum_{|n|=k}n\cdot\delta=B_1S_1, \tag{5}
\]

\[
 \boxed{\sum_{|n|=k}(n\cdot\delta)^2
 =\binom{k+d-1}{d+1}S_1^2+\binom{k+d}{d+1}S_2.} \tag{6}
\]

Indeed $\sum n_i^2=2B_2+B_1$, while the mixed terms have coefficient $B_2$. Combining them gives $B_2S_1^2+(B_1+B_2)S_2$, and Pascal's identity gives (6). In particular

\[
 \frac1{N_{d,k}}\sum_{|n|=k}(n\cdot\delta)^2
 =\frac{k(k-1)}{d(d+1)}S_1^2+\frac{k(k+d)}{d(d+1)}S_2. \tag{7}
\]

Equation (7) records an exact arithmetic mean and leaves the original sum and its factor $N_{d,k}$ in (6). For $d=1$, the sum has the single value $k\delta_1$ and the two coefficients in (6) add to $k^2$. For $k=1$, (5) and (6) give $S_1,S_2$. For $k=0$, all displayed moments vanish and the space has dimension one. No denominator is singular in any of these cases.

For the doubled convention $\Delta=2\delta$, the first moment doubles and the second moment is four times (6).

## 3. Grouping distinct roots preserves their multiplicity weights and nilpotents

Let $\mathcal R$ be the set of distinct eigenvalues and let $m_\rho$ be their algebraic multiplicities. Grouping individual occupancies by $\ell_\rho=\sum_{i:\rho_i=\rho}n_i$ gives the weight

\[
 w(\ell)=\prod_{\rho\in\mathcal R}\binom{\ell_\rho+m_\rho-1}{m_\rho-1}. \tag{8}
\]

Each factor counts compositions of $\ell_\rho$ into its $m_\rho$ labelled eigenvalue slots. Therefore (3) becomes exactly

\[
 \det(zI-A_k^{\mathrm{sym}})
 =\prod_{\sum_\rho\ell_\rho=k}\left(z-\sum_\rho\ell_\rho\rho\right)^{w(\ell)}. \tag{9}
\]

Coincident sums from different $\ell$'s multiply their factors and add their multiplicities. In (5)–(6), replace $S_1,S_2$ by $\sum_\rho m_\rho\delta_\rho$ and $\sum_\rho m_\rho\delta_\rho^2$, respectively. The left sides can equivalently be written as sums over $\ell$, each with weight (8).

The canonical generalized eigenspace decomposition $E=\bigoplus_\rho E_\rho$ induces

\[
 E_k^{\mathrm{sym}}\cong\bigoplus_{\sum\ell_\rho=k}\bigotimes_\rho(E_\rho^{\otimes\ell_\rho})^{S_{\ell_\rho}}. \tag{10}
\]

An explicit map takes the tensor of within-root invariant tensors and sums over the distinct placements of its root blocks in the $k$ positions; its inverse extracts the coefficient in one fixed root-block arrangement. Thus no extra factorial is silently inserted. In each block of (10), $A_k^{\mathrm{sym}}$ is the scalar $\sum\ell_\rho\rho$ plus the sum of the induced nilpotents. Formula (1) gives all coefficients of that nilpotent operator.

For the actual cyclic local factors $\mathbb C[\varepsilon_\rho]/\varepsilon_\rho^{m_\rho}$, its nilpotency index on the block labelled $\ell$ is exactly

\[
 1+L,\qquad L=\sum_\rho\ell_\rho(m_\rho-1). \tag{11}
\]

Proof: give a tensor $\varepsilon_{\rho_1}^{j_1}\otimes\cdots\otimes\varepsilon_{\rho_k}^{j_k}$ grade $\sum j_i$. The nilpotent sum raises grade by one; no grade exceeds $L$. Its power $L+1$ is therefore zero. Let $v_{\mathrm{bottom}}$ be the unscaled orbit sum with $\ell_\rho$ copies of each local $e_0$. Let $v_{\mathrm{top}}$ have $\ell_\rho$ copies of each $e_{m_\rho-1}$. Multinomial expansion of the commuting $k$ raising operators gives

\[
 N_k^Lv_{\mathrm{bottom}}
 =\frac{L!}{\prod_\rho((m_\rho-1)!)^{\ell_\rho}}v_{\mathrm{top}}\ne0. \tag{12}
\]

Every nonzero summand has precisely $m_\rho-1$ raises in each factor of type $\rho$, and both endpoint root-placement orbits have the same size. This proves the coefficient as well as the index, including $L=0$. This asserts the maximal block length, not that the whole block in (10) is one Jordan block.

## 4. Trace series and its exact relation to the source cycle formula

For $a>0$, retain the literal generator $U(a)=\exp((\log a)A)$. Its eigenvalues are $a^{\rho_i}=\exp((\log a)\rho_i)$. Triangularity and the orbit basis prove

\[
 \operatorname{Tr}(U(a)^{\otimes k}|E_k^{\mathrm{sym}})
 =\sum_{|n|=k}a^{\sum_i n_i\rho_i},
\]

and therefore, as a formal power series in $q$,

\[
 \boxed{\sum_{k\ge0}q^k\operatorname{Tr}(U(a)^{\otimes k}|E_k^{\mathrm{sym}})
 =\det(I-qU(a))^{-1}
 =\prod_\rho(1-qa^\rho)^{-m_\rho}.} \tag{13}
\]

Nilpotent coefficients remain in (1), (10)–(12); the trace forgets them because a triangular matrix has trace equal to the sum of its diagonal entries. The map to this observation, with its information loss, is explicit.

Taking the formal logarithm of the product in (13), using $-\log(1-x)=\sum_{j\ge1}x^j/j$, gives

\[
 \exp\left(\sum_{j\ge1}\frac{q^j}{j}\operatorname{Tr}(U(a)^j)\right). \tag{14}
\]

For cycle counts $c_j\ge0$, $\sum j c_j=k$, the coefficient in (14) is $\prod_j\operatorname{Tr}(U^j)^{c_j}/(j^{c_j}c_j!)$. There are $k!/\prod_j j^{c_j}c_j!$ permutations with those cycle counts: choose the labelled elements of each cycle, divide by each cycle's cyclic rotations and by permutations of cycles of identical length. Hence (14) is exactly the source's $1/k!$ cycle sum, including that factor. The cohomological sign is the original $(-1)^k$; the complementary supertrace is the difference from the full tensor supertrace, exactly as in source (6.7).

## 5. Comparison with ordered full tensor powers

The ordered tensor basis has $d^k$ entries. Its occupancy $n$ has weight $k!/\prod n_i!$, rather than weight one. For $k\ge1$, counting one or two specified tensor positions proves

\[
 \sum_{i_1,\ldots,i_k}(\delta_{i_1}+\cdots+\delta_{i_k})
 =k d^{k-1}S_1,
\]

\[
 \sum_{i_1,\ldots,i_k}(\delta_{i_1}+\cdots+\delta_{i_k})^2
 =k d^{k-1}S_2+k(k-1)d^{k-2}S_1^2. \tag{15}
\]

For $k=1$, the last term is zero. For $k=0$, both sums are zero. Grouped by distinct roots, its occupancy weight is $k!\prod_\rho m_\rho^{\ell_\rho}/\prod_\rho\ell_\rho!$. Its action trace is $(\sum_\rho m_\rho a^\rho)^k$.

The typed comparison is the inclusion $I_k$, the commuting permutation projector, and the complementary invariant subspace, not an identification of these two differently weighted sums. In a reflection-stable packet $S_1=0$, (7) and (15) give arithmetic means $k(k+d)S_2/[d(d+1)]$ and $kS_2/d$, respectively. These moment identities alone do not compare the two arithmetic relative-control constants.

## 6. Exact rank and inertia lower bounds for the original metric

Let $G\succ0$ be the source's actual symmetric Gram matrix and let

\[
 W=(A_k^{\mathrm{sym}})^*G+GA_k^{\mathrm{sym}}-kG.
\]

Define the exact congruence coordinates $H=G^{-1/2}WG^{-1/2}$, $B=G^{1/2}A_k^{\mathrm{sym}}G^{-1/2}$. These are invertible coordinate maps retaining $G,W,A_k^{\mathrm{sym}}$; they do not substitute a new metric. Then $H=B^*+B-kI$. Unitary Schur triangularization $U^*BU=T$, with diagonal $(\lambda_n)$, gives diagonal entries $2n\cdot\delta$ in $U^*HU$. Consequently

\[
 \operatorname{Tr}H=2B_1S_1,
\]

\[
 \operatorname{Tr}(H^2)
 =4\sum_{|n|=k}(n\cdot\delta)^2+2\sum_{i<j}|T_{ij}|^2
 \ge4\left[\binom{k+d-1}{d+1}S_1^2+\binom{k+d}{d+1}S_2\right]. \tag{16}
\]

Every Schur off-diagonal term is explicitly retained in (16). If $r=\operatorname{rank}H>0$ and $\epsilon=\|H\|_{\mathrm{op}}$, its $r$ nonzero eigenvalues each have square at most $\epsilon^2$. Thus

\[
 \boxed{\epsilon\ge\frac2{\sqrt r}\sqrt{\binom{k+d-1}{d+1}S_1^2+\binom{k+d}{d+1}S_2}.} \tag{17}
\]

Let $r_+,r_-$ be its positive and negative inertia and let $H_+,H_-$ be the positive and negative parts. For any subset of Schur coordinate indices, let $P$ be its orthogonal projection. Then $\operatorname{Tr}(PH)\le\operatorname{Tr}(PH_+)\le\operatorname{Tr}H_+$. Choosing precisely those indices with $n\cdot\delta>0$ proves

\[
 2\sum_n(n\cdot\delta)_+\le\operatorname{Tr}H_+\le r_+\max(0,\lambda_{\max}H).
\]

Applying this to $-H$ proves its negative analogue. Summing yields

\[
 \boxed{\epsilon\ge\frac2r\sum_{|n|=k}|n\cdot\delta|.} \tag{18}
\]

If $r=0$, then $H=0$, all the departures in its Schur diagonal are zero, and the inequalities before division remain the valid statements. In particular each repeated eigenline $v^{\otimes k}$ gives the source's sharper pointwise witness $\epsilon\ge2k\max_i|\delta_i|$ for $k>0$.

The source's symmetric frontier has dimension $s=p_{\le k}(M+1)$. Its displayed factorization is a congruence/compression of the Hermitian block matrix

\[
 \begin{pmatrix}0&\Omega^{-1}\\\Omega^{-1}&0\end{pmatrix},\qquad\Omega\succ0,
\]

which has exactly $s$ positive and $s$ negative eigenvalues: the invertible map $(x,y)\mapsto(x+y,x-y)$, retaining its factors of two in the quadratic form, gives positive and negative definite diagonal blocks. A pullback cannot increase either inertia, because any positive-definite subspace maps injectively into one on which the original form is positive. Therefore

\[
 r\le\min(N_{d,k},2s),\qquad r_+\le s,\qquad r_-\le s. \tag{19}
\]

Combining (17)–(19) gives valid finite constraints on exactly the source's symmetric metric. For example, if $s>0$,

\[
 \epsilon\ge\sqrt{\frac2s\left[\binom{k+d-1}{d+1}S_1^2+\binom{k+d}{d+1}S_2\right]},\qquad
 \epsilon\ge\frac1s\sum_{|n|=k}|n\cdot\delta|. \tag{20}
\]

For a packet stable under $\rho\mapsto1-\bar\rho$ with full multiplicities, $S_1=0$, and the occupancy involution reverses every departure. Thus the positive and negative departure sums are each half the absolute sum. The positive and negative one-sided bounds are each at least that absolute sum divided by $s$, whenever that sum is nonzero. No same-packet reflection assertion is used for an arbitrary packet.

These are lower bounds and exact combinatorial constraints. They do not prove an arithmetic upper bound sublinear in $k$, do not infer a missing estimate from dimension reduction, and do not assert that trace/characteristic data determine the retained nilpotent matrices.

## 7. Reproducible finite checks and scope

Checker: `work/check_symmetric_occupancy_20260912.py`. It uses exact rational/integer arithmetic and explicit runtime failures, never Python `assert`. It checks all $1\le d\le6,0\le k\le7$ occupancy moments, grouped repeated-root characteristic multiplicities, full ordered-tensor moments, direct tensor enumeration of the unscaled orbit action, and raising nilpotent endpoint coefficients including single-dimensional and degree-zero nilpotent edges.

Executed commands:

```
python work/check_symmetric_occupancy_20260912.py
python -O work/check_symmetric_occupancy_20260912.py
python work/check_symmetric_occupancy_20260912.py --deliberate-failure
python -O work/check_symmetric_occupancy_20260912.py --deliberate-failure
```

The first two each pass 938 finite checks with exit 0. The last two replace the original orbit coefficient $n_i+1$ by the monomial coefficient $n_j$; both fail with exit 1 at the direct orbit-action comparison. These are finite checks, not 938 theorems and not arithmetic or analytic certificates. The complete proofs of the formulas are Sections 1–6 above.

## 8. Formatting repair and independent main-fragment review

The formatting repair used raw bytes: the original report had five carriage-return bytes inside the intended command $\rho$ and one backspace byte inside the intended command $\binom$. Those commands have been restored. All 145 original inline mathematical spans now use dollar delimiters; the 33 display pairs remain intact. No control bytes other than line feeds remain. Missing backslashes on $\qquad$, $\sum$, $\prod$, $\operatorname{Tr}$ and $\epsilon$ were repaired. Mathematical content was not changed. The checker and its existing execution receipt were left untouched; consequently the receipt's old report hash identifies the pre-repair report and must not be presented as the final report hash.

Independently reviewed the actual main fragment at output/split_zero_rh_tandem_2026-09-12/tex/symmetric_spectral_cost.tex, including all of SS.14 and SS.18–SS.28. The current formulas in those locations agree with the independently derived calculations above. No mathematical correction was found in this bounded review:

Reviewed main-fragment SHA256: BE671BBCB439EB8D58CAC41A2A2AF94CBA6A205A04A8E32342B046B68A23AE1A.

- SS.14 retains the raising convention and coefficient $h_\ell!/\prod_\rho((m_\rho-1)!)^{\ell_\rho}$. Its endpoints are nonzero and the nilpotency index is exactly $h_\ell+1$, including $h_\ell=0$.
- SS.18 has $a_k+b_k=\binom{k+d}{d+1}$ multiplying $\sigma_2$ and $b_k$ multiplying $\sigma_1^2$.
- SS.19 uses the precise original-metric quantity $\mathfrak d_M^s=\operatorname{Tr}(G^{-1}(A^s)^*GA^s)-\sum|\lambda_n|^2$. Under $T=G^{1/2}A^sG^{-1/2}$ this is the sum of squared moduli of the strictly upper-triangular Schur entries. Consequently the factor on it in $\operatorname{Tr}((S_M^s)^2)$ is exactly two, while the offset-square sum has factor four.
- SS.20 follows by subtracting $Nk^2\sigma_1^2/d^2$ from SS.18. The coefficient identity $b_k-Nk^2/d^2=-Nk(k+d)/(d^2(d+1))$ proves the centered formula, also for $d=1$ and $k=1$.
- SS.21 gives the complementary occupancy weight $k!/\prod n_i!-1$. The commuting permutation projector gives the exact direct sum of the two invariant operators, and commutation with the same Gram makes that direct sum orthogonal for the arithmetic metric.
- SS.22–SS.24 retain the negative cross term. Vanishing of the quadratic form on each of $\ker Y_M^s$ and $\ker C_M^s$ proves both inertia bounds. The trace-norm estimate gives $\mathcal D_k^s\le\sqrt{\tau_M^s\chi_M^s}$ and $\mathcal D_k^s\le r_M^s\epsilon_M^s$ with their displayed constants.
- SS.25 restricts the reflection assertion to a same-packet involution with full orders. I checked the cited CT.16a matrices and their resulting generalized-eigenvalue map: $u\mapsto C_{h,k}\bar u$ carries $\lambda$ to $-\lambda$. With $2p_M^s$ nonzero eigenvalues, SS.19 gives exactly $p_M^s(\epsilon_M^s)^2\ge 2Nk(k+d)\sigma_2/[d(d+1)]+\mathfrak d_M^s$.
- SS.26 follows from $|n\cdot\delta|^2\le k\delta_*|n\cdot\delta|$. Its reflected specialization cancels exactly one factor $k$. The repeated-eigenline bound is $\epsilon_M^s\ge2k\delta_*$, and SS.14 proves strictly positive Schur departure whenever some $m_\rho>1$.
- SS.27 has the correct inequality direction: $\pi^{1/r}\le r^{-1}\sum_j(1-t_j)=1-\tau/r$ gives $\tau\le r(1-\pi^{1/r})$. The formula is explicitly restricted to $r>0$ and the zero-rank case is handled without division.
- SS.28 follows from $(\mathcal D_k^s)^2/\chi_M^s\le\tau_M^s\le-\log\pi_M^s$. Its denominators are positive under the stated $\mathcal D_k^s>0$. The asserted divergence of $\sum_M\tau_M^s$ follows because convergence would imply eventual $t_j\le\tau_M^s\le1/2$ and hence $-\log(1-t_j)\le2t_j$, contradicting determinant decay. The cited JD.8–JD.9 state and prove the full source density and Gram limit; restriction by the bounded permutation projector gives the invariant version used here.

This second review covers the finite coefficients, the nilpotent calculation, the exact metric manipulations, and the specified dependence on CT.16a and JD.8–JD.9. It does not claim an independent reproof of all earlier infinite-dimensional analytic inputs.
