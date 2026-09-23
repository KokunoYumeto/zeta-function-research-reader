# Independent proof check and exact graph-norm repair

Date: 2026-09-23. Independently read and recalculated SUPPORTED_ZERO_MASS_COMPLETION.tex, MCB1–19 and the theta-comb comparison. The checked version had MCB4 with one copy of the lower-coordinate squared norm. The precise repair and its propagation are proved here.

## GMC1. The actual graph norm

Retain the original domain and original norm:
\[
\mathcal V_0=c_{00}(\mathbb Z)\oplus\mathbb C^{L\setminus\{1_L\}},\qquad
\|(a,b)\|_0^2=\|a\|_{\ell^2}^2+\|b\|_2^2.
\]
The source operator is exactly
\[
E(a,b)=(m(a)\delta_0,b),\qquad m(a)=\sum_n a_n.
\]
This follows because original multiplication by \(e\) sends every top-supported integer point to \(e\), while fixing every lower zero-label point. In particular no lower coefficient is erased.

The literal graph norm of this operator, with this original source and target norm, is
\[
\boxed{\|(a,b)\|_{\operatorname{graph}E}^2
=\|(a,b)\|_0^2+\|E(a,b)\|_0^2
=\|a\|_2^2+2\|b\|_2^2+|m(a)|^2.}
\tag{GMC1}
\]
Therefore MCB4's single occurrence of \(\|b\|_2^2\) is an equivalent norm but is not the exact graph norm. To preserve the original formulas, retain both copies by changing its coefficient to \(2\).

The full graph embedding into \(\mathcal H_0\oplus\mathcal H_0\), where \(\mathcal H_0=\ell^2(\mathbb Z)\oplus\mathbb C^{L\setminus\{1_L\}}\), is
\[
J(a,b)=((a,b),(m(a)\delta_0,b)).
\tag{GMC2}
\]
The coordinate map \(j(a,b)=(a,b,m(a))\) is still an exact isometry if its target is equipped with
\[
\|(a,b,m)\|_{\widehat E}^2=\|a\|_2^2+2\|b\|_2^2+|m|^2.
\tag{GMC3}
\]
This target has not discarded the second \(b\): its isometry to the literal graph carrier is \((a,b,m)\mapsto((a,b),(m\delta_0,b))\).

## GMC2. Nonclosability and completion

Let \(a^{(N)}\) equal \(1/N\) at the integers \(1,\ldots,N\) and zero elsewhere. Then \(\|a^{(N)}\|_2^2=1/N\), \(m(a^{(N)})=1\), and \(E(a^{(N)},0)=(\delta_0,0)\). Thus \(E\) is unbounded and not closable in \(\mathcal H_0\): the domain vectors tend to zero and their images tend to a nonzero vector.

The completion with GMC1 is exactly
\[
\widehat{\mathcal V}_E=
\ell^2(\mathbb Z)\oplus\mathbb C^{L\setminus\{1_L\}}\oplus\mathbb C
\tag{GMC4}
\]
with norm GMC3. To prove density, truncate \(a\) to \(a^{[j]}\) and put \(d_j=m-\sum_n a_n^{[j]}\). On a finite set disjoint from that truncation, put the constant \(d_j/N_j\), with \(N_j>j^2|d_j|^2\), producing \(r^{[j]}\). Its sum is \(d_j\), and its squared norm is \(|d_j|^2/N_j<j^{-2}\). Hence \(j(a^{[j]}+r^{[j]},b)\to(a,b,m)\) in the exact norm. This proves the completion claim directly.

The closure of the original graph as a subspace of \(\mathcal H_0\oplus\mathcal H_0\) is precisely
\[
\overline{\Gamma(E)}
=\{((a,b),(m\delta_0,b)):a\in\ell^2,\ b\in\mathbb C^{L\setminus\{1_L\}},\ m\in\mathbb C\}.
\tag{GMC5}
\]
The displayed set is closed, and the density argument proves the reverse inclusion. It is a closed linear relation, not the graph of an operator on \(\mathcal H_0\), because its multivalued part at zero is
\[
\{((0,0),(m\delta_0,0)):m\in\mathbb C\}.
\tag{GMC6}
\]
The new Hilbert space GMC4 retains this full graph relation as its own state space, allowing a bounded receiving action there.

The extension is
\[
\widehat E(a,b,m)=(m\delta_0,b,m).
\tag{GMC7}
\]
It agrees with \(E\) on the dense embedded source and is idempotent. Its exact output squared norm is
\[
2|m|^2+2\|b\|_2^2
\le2(\|a\|_2^2+2\|b\|_2^2+|m|^2).
\tag{GMC8}
\]
Equality in the operator-norm bound is attained on \((0,0,1)\), so \(\|\widehat E\|=\sqrt2\). This is the required correction to the norm computation after MCB7.

The projection \(\pi(a,b,m)=(a,b)\) is bounded and onto, with kernel \(\{(0,0,m)\}\). That kernel is not \(\widehat E\)-invariant since \(\widehat E(0,0,1)=(\delta_0,0,1)\). Consequently no operator on the quotient can satisfy \(\pi\widehat E=B\pi\), bounded or otherwise: evaluating this identity on \((0,0,1)\) gives \((\delta_0,0)=B0=0\). This proves the exact failure of descent along this particular projection.

There is also a complete decomposition
\[
(a,b,m)=(a-m\delta_0,0,0)+(m\delta_0,b,m),
\tag{GMC9}
\]
where the first term is in the kernel of \(\widehat E\) and the second is in its range. The projection is generally not orthogonal; its norm \(\sqrt2\) quantifies that fact without changing its idempotence.

## GMC3. Every original zero label

Let \(q=|L\setminus\{1_L\}|\). For \(\sigma<1_L\), MCB9 is the exact formula
\[
\widehat E_\sigma(a,b,m)=(0,b',0),\qquad
b'_\nu=m\mathbf1_{\nu=\sigma}
+\sum_{\substack{\lambda<1_L\\\sigma\wedge\lambda=\nu}}b_\lambda.
\tag{GMC10}
\]
The top mass is zero in the output because no top-supported atom remains. Its lower coefficients retain all original fibers of the meet map. The case \(\sigma=1_L\) is GMC7.

An exact operator-norm computation is available. Set
\[
k_{\sigma,\nu}=
\#\{\lambda<1_L:\sigma\wedge\lambda=\nu\}.
\]
Use coordinates \(\widetilde b=\sqrt2\,b\) for the sole purpose of computing the original weighted norm GMC3; the actual formulas still use \(b\). The output lower coordinate in these norm coordinates is
\[
\sqrt2\,b'_\nu
=\sqrt2\,m\mathbf1_{\nu=\sigma}
+\sum_{\sigma\wedge\lambda=\nu}\widetilde b_\lambda.
\]
Rows have disjoint input supports, including the mass coordinate which occurs only at row \(\sigma\). Their squared row norms are \(k_{\sigma,\nu}+2\mathbf1_{\nu=\sigma}\). Orthogonality of these rows therefore gives
\[
\boxed{\|\widehat E_\sigma\|^2
=\max_{\nu<1_L}
\left(k_{\sigma,\nu}+2\mathbf1_{\nu=\sigma}\right).}
\tag{GMC11}
\]
The ignored \(a\)-coordinate cannot enlarge the norm. Equality is attained by an input proportional to a row of maximal norm, with \(a=0\). In particular the bottom-label action has squared norm \(q+2=|L|+1\).

On the finite embedded source, these operators are literal multiplication by \(z_\sigma\). Therefore associativity and \(z_\sigma z_\lambda=z_{\sigma\wedge\lambda}\) give
\[
\widehat E_\sigma\widehat E_\lambda
=\widehat E_{\sigma\wedge\lambda}
\tag{GMC12}
\]
first on that source, then everywhere by density and boundedness. The representation of the meet semilattice is faithful: apply the operators to the embedded point \((\delta_1,0,1)\), which is sent to the distinct original point \(z_\sigma\) in each case. No identification of two labels is needed.

For nonzero \(k\in\mathbb Z\), \(P_ka\) places \(a_n\) at \(kn\). Since \(n\mapsto kn\) is injective, \(\|P_ka\|_2=\|a\|_2\), and
\[
\widehat M_k(a,b,m)=(P_ka,b,m)
\tag{GMC13}
\]
is an isometry for GMC3. Its finite-source mass is unchanged. Composition and its mixed products with GMC10 reproduce original point multiplication by density. No claim that the sum of two operator matrices equals the operator of semiring addition is needed or implied.

## GMC4. Gaussian frame constants

Retain \(k_T(x)=(4\pi T)^{-1/2}e^{-x^2/(4T)}\) and the Fourier convention \(e^{-2\pi i x\xi}\). For finite sequences,
\[
\int_{\mathbb R}k_T(x-n)k_T(x-m)\,dx
=(8\pi T)^{-1/2}e^{-(n-m)^2/(8T)}.
\tag{GMC14}
\]
Completing the square in the full product of the two kernels gives this constant directly:
\((x-n)^2+(x-m)^2=2(x-(n+m)/2)^2+(n-m)^2/2\);
the integral of the remaining Gaussian is \(\sqrt{2\pi T}\), multiplied by \((4\pi T)^{-1}\).

For \(A_Ta=\sum_na_nk_T(x-n)\), let \(P_a(\theta)=\sum_na_ne^{-2\pi i n\theta}\). Periodization of the Fourier Gaussian gives
\[
\|A_Ta\|_2^2=
\int_{-1/2}^{1/2}W_T(\theta)|P_a(\theta)|^2\,d\theta,
\quad
W_T(\theta)=\sum_{j\in\mathbb Z}e^{-8\pi^2T(\theta+j)^2}.
\tag{GMC15}
\]
Indeed unfolding its \(n-m\) Fourier coefficient gives exactly GMC14. All interchanges for a finite polynomial are justified by the uniformly summable Gaussian tails. The \(j=0\) term gives the lower bound on the interval, and \(|\theta+j|\ge |j|-1/2\) bounds the other terms:
\[
e^{-2\pi^2T}\le W_T(\theta)
\le1+2\sum_{j\ge1}e^{-8\pi^2T(j-1/2)^2}=U_T.
\tag{GMC16}
\]
Parseval for finite exponentials therefore gives exactly the MCB16 bounds. They extend to \(\ell^2\) by completion; the lower bound proves injectivity and closed range. The inverse norm on that range is at most \(e^{\pi^2T}\). No Fourier factor is missing.

## GMC5. Heat state with the corrected original graph norm

Keep the output norm as the ordinary direct-sum norm of \(L^2(\mathbb R;\mathbb C^L)\oplus\mathbb C\), and retain the unchanged formula
\[
\mathbb H_T(a,b,m)=
\left(A_Ta\,v_{1_L}+k_T\sum_{\lambda<1_L}b_\lambda v_\lambda,\ m\right).
\tag{GMC17}
\]
Set \(\kappa_T=(8\pi T)^{-1/2}\). The exact squared output norm is
\[
\|A_Ta\|_2^2+\kappa_T\|b\|_2^2+|m|^2.
\tag{GMC18}
\]
Relative to the corrected exact input norm GMC3, explicit constants are
\[
c_T=\min\{e^{-2\pi^2T},\kappa_T/2,1\},\qquad
C_T=\max\{U_T,\kappa_T/2,1\}.
\tag{GMC19}
\]
Thus
\[
c_T\|(a,b,m)\|_{\widehat E}^2
\le\|\mathbb H_T(a,b,m)\|^2
\le C_T\|(a,b,m)\|_{\widehat E}^2.
\tag{GMC20}
\]
These prove a bounded isomorphism onto a closed image, with forward norm at most \(\sqrt{C_T}\) and inverse norm at most \(1/\sqrt{c_T}\). The factor \(1/2\) in the lower-label comparison is exactly the second copy of \(b\) retained in the literal graph norm.

The transported \(e\)-action is unchanged:
\[
\mathbb H_T\widehat E(a,b,m)=
\left(mk_Tv_{1_L}+k_T\sum_{\lambda<1_L}b_\lambda v_\lambda,\ m\right).
\tag{GMC21}
\]
It is a bounded idempotent on the closed heat image. A valid bound is
\(\|\mathbb H_T\widehat E\mathbb H_T^{-1}\|
\le\sqrt{2C_T/c_T}\).
All other arithmetic actions transport through the same exact isomorphism, preserving their product relations. This does not assert that their heat-image operators are ordinary pointwise multiplication.

Convolution by \(k_U\) is bounded on \(L^2\) with norm at most one, as its Fourier multiplier has modulus at most one. On finite sources \(k_U*k_T=k_{T+U}\), retaining both Gaussian prefactors. Density and the bounded maps give
\[
(k_U*,\mathrm{id})\mathbb H_T=\mathbb H_{T+U}.
\tag{GMC22}
\]
This proves MCB19 after the graph-norm correction, with the same physical \(T,U\).

## GMC6. Exact common domain with the tempered theta source

The whole integer comb has coefficients all equal to one, so it is not an \(\ell^2\) source and has no finite total mass. Its symmetric finite truncations have mass \(2N+1\). Their \(e\)-images are \((2N+1)\delta_0\) in the top coordinate, which do not converge even as distributions: any compact test of value one at zero has pairing \(2N+1\). Thus the completed finite-mass action does not extend to this comb by those truncations.

Finite atomic sources form an exact common domain. If \(\iota\) is LH2, \(j\) is the graph embedding, and \(\operatorname{pr}_{\rm fun}\) forgets only the newly retained mass coordinate of the heat output, the comparison is the explicit identity
\[
\operatorname{pr}_{\rm fun}\mathbb H_Tj(v)=\mathcal H_T\iota(v),
\qquad v\in\mathcal V_0.
\tag{GMC23}
\]
Every coefficient agrees by the finite Gaussian sum. Stating this projection makes the different codomains exact: \(\mathbb H_Tj(v)\) has an additional mass coordinate, while \(\mathcal H_T\iota(v)\) is the labelled function alone. The marked zero in the tempered comb remains separately retained by LH's pair and is not assigned a nonexistent finite total comb mass.

## Required changes and conclusion

The only mathematical correction to the checked formulas is the literal graph norm and its propagated norm constants:

* MCB4: replace \(\|b\|_2^2\) by \(2\|b\|_2^2\), or explicitly retain both \(b\)-coordinates in the literal graph embedding GMC2.
* MCB5: specify the weighted norm GMC3.
* The MCB7 output-norm sentence: use \(2|m|^2+2\|b\|_2^2\).
* MCB17's quantitative comparison: use GMC19–20 against the exact input graph norm.
* The common-domain statement can be made fully typed by GMC23.

MCB1–3, MCB6's density construction, all operator formulas MCB7–11, Gaussian identities MCB12–16, the heat transport formulas MCB17–19, and the theta-comb exclusion otherwise check. The stronger relation description, exact lattice-action norms, and exact heat comparison above are derived from the original formulas.
