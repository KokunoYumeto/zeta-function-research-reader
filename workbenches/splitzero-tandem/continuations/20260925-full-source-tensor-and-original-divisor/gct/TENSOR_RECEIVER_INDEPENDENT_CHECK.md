# Independent calculation of the actual rapid tensor receiver

Proof locators TRC0–TRC6. This note records the independent mathematical subtask assigned by the tensor-weight derivation task. It changes no global manuscript or workflow file. Reading coverage: ACTUAL_DEFECT_MULTIPLIER_DOMAIN.md, ADM1–ADM3; POSITIVE_SOURCE_COMPLETION_AND_SPECIALIZATION.md, CPS0–CPS4. The existing source-reading and user-input records remain in the parent task's durable logbook space. No new human-source reading is claimed.

## TRC0. Retained objects

Fix an integer \(k\ge1\), a recovered coefficient parameter \(r>1\), and the actual distinct off-line nontrivial-zero set \(I=\mathscr Z_O\). Keep the original multiplicities \(m_\rho\), \(w_\rho=1+|\Im\rho|\), and reflection \(\rho^\#=1-\overline\rho\). Put
\[
E=H_{\infty,O},\qquad p_N(x)^2=\sum_{\rho\in I}m_\rho w_\rho^{2N}|x_\rho|^2.
\]
The actual source is \(R=Q/N_O\) with its existing Fréchet quotient topology. Write \(\beta_r:R\to E\) for ADM3.4's injective continuous map. For any entire representative \(F\) of a source class,
\[
(\beta_r[F])_\rho=\delta_r(\rho)F(\rho^\#),\qquad
\delta_r(\rho)=\overline{d_r(\rho)}
=e^{i\Im\rho\log r}\bigl(r^{\Re\rho}-r^{1-\Re\rho}\bigr).
\tag{TRC0.1}
\]
Every \(\delta_r(\rho)\) on \(I\) is nonzero. ADM3.5 proves that \(\beta_r(R)\) contains every finitely supported vector. ADM3.2 retains the established finite constant
\[
C_4^2=\sum_{\rho\in\mathscr Z}m_\rho w_\rho^{-4}<\infty.
\tag{TRC0.2}
\]
The source topology is not replaced by a topology transported from \(E\).

## TRC1. The rapid tensor sequence space

For \(\boldsymbol\rho=(\rho_1,\ldots,\rho_k)\in I^k\), retain
\[
m_{\boldsymbol\rho}=\prod_{j=1}^k m_{\rho_j},\qquad
W_{\boldsymbol\rho}=\prod_{j=1}^k w_{\rho_j}.
\]
Define
\[
H_N^{(k)}=\left\{y:\ P_N(y)^2=
\sum_{\boldsymbol\rho\in I^k}m_{\boldsymbol\rho}
W_{\boldsymbol\rho}^{2N}|y_{\boldsymbol\rho}|^2<\infty\right\},
\qquad H_\infty^{(k)}=\bigcap_{N\ge0}H_N^{(k)}.
\tag{TRC1.1}
\]
Its topology is given by the increasing norms \(P_N\). It is exactly the topology given by all mixed exponents \((N_1,\ldots,N_k)\): each mixed norm is at most \(P_{\max_jN_j}\), and every \(P_N\) is one of the mixed norms. Thus the product weights in (TRC1.1) retain rapid decay separately in every coordinate.

Each \(H_N^{(k)}\) is a complete weighted Hilbert space. A sequence Cauchy in every \(P_N\) has a limit in each \(H_N^{(k)}\). Continuity of each coordinate evaluation identifies these limits as the same coordinate family, which belongs to all the spaces. This proves completeness of \(H_\infty^{(k)}\).

Let \(P_T^{[k]}\) retain exactly the tuples with \(|\Im\rho_j|\le T\) for every \(j\). Its range is finite dimensional. If a tuple is outside this range, at least one factor in \(W_{\boldsymbol\rho}\) exceeds \(1+T\). Hence
\[
P_N\bigl((1-P_T^{[k]})y\bigr)
\le (1+T)^{-1}P_{N+1}(y).
\tag{TRC1.2}
\]
The finite coordinate truncations converge in every norm, uniformly on bounded sets. In particular finite coordinate vectors are dense. This also proves compactness of each inclusion \(H_{N+1}^{(k)}\to H_N^{(k)}\), and the usual finite-projection/tail argument proves that bounded subsets of \(H_\infty^{(k)}\) have compact closure.

## TRC2. Completed projective tensor identification of the receiver

There is a canonical topological isomorphism
\[
J_k:E\widehat\otimes_\pi\cdots\widehat\otimes_\pi E
\longrightarrow H_\infty^{(k)},\qquad
J_k(x_1\otimes\cdots\otimes x_k)_{\boldsymbol\rho}
=\prod_{j=1}^k(x_j)_{\rho_j}.
\tag{TRC2.1}
\]
Here the left side means the Hausdorff completion of the algebraic \(k\)-fold projective tensor product. The result follows from an explicit inverse, without assuming a nuclear-space theorem.

Let \(\pi_N\) be the projective tensor seminorm induced by \(p_N\) in every factor. These seminorms are cofinal among projective tensor seminorms: each continuous seminorm of \(E\) is bounded by a constant times some increasing \(p_N\). On a decomposable tensor the nonnegative series factor exactly, giving
\[
P_N(J_k(x_1\otimes\cdots\otimes x_k))
=\prod_{j=1}^k p_N(x_j).
\tag{TRC2.2}
\]
Triangle inequalities followed by the defining infimum yield \(P_N(J_ku)\le\pi_N(u)\). Thus \(J_k\) extends to the completion.

Let \(e_\rho\) be the coordinate vector of value one at \(\rho\), with no rescaling; thus \(p_N(e_\rho)=\sqrt{m_\rho}w_\rho^N\). Define the proposed inverse by its full coordinate series
\[
\Psi_k(y)=\sum_{\boldsymbol\rho\in I^k}
y_{\boldsymbol\rho}
e_{\rho_1}\otimes\cdots\otimes e_{\rho_k}.
\tag{TRC2.3}
\]
Set \(S_O=\sum_{\rho\in I}w_\rho^{-4}\le C_4^2\), since every multiplicity is a positive integer. Cauchy–Schwarz gives, for every finite set \(A\subset I^k\),
\[
\begin{aligned}
\pi_N\!\left(\sum_{\boldsymbol\rho\in A}
y_{\boldsymbol\rho}e_{\rho_1}\otimes\cdots\otimes e_{\rho_k}\right)
&\le\sum_{\boldsymbol\rho\in A}|y_{\boldsymbol\rho}|
\prod_{j=1}^k\sqrt{m_{\rho_j}}w_{\rho_j}^N\\
&\le P_{N+2}(1_Ay)
\left(\sum_{\boldsymbol\rho\in A}\prod_{j=1}^kw_{\rho_j}^{-4}\right)^{1/2}\\
&\le S_O^{k/2}P_{N+2}(1_Ay).
\end{aligned}
\tag{TRC2.4}
\]
Consequently the series is absolutely Cauchy in each projective seminorm, has a limit in the completed tensor product, and satisfies
\(\pi_N(\Psi_ky)\le S_O^{k/2}P_{N+2}(y)\). It defines a continuous map.

Coordinate truncations prove \(J_k\Psi_k=1\). For a decomposable tensor, \(P_Tx_j\to x_j\) in every \(p_N\). Expand the difference of the products into its \(k\) terms, one factor difference at a time, and apply \(\pi_N\); the approximating factors stay bounded and the difference factor tends to zero. It follows that \(P_Tx_1\otimes\cdots\otimes P_Tx_k\to x_1\otimes\cdots\otimes x_k\). These are exactly the finite series defining \(\Psi_kJ_k\) on that tensor. Therefore \(\Psi_kJ_k=1\) on decomposable tensors, then on the algebraic tensor product, and then on its completion by continuity and density. This proves (TRC2.1). It proves no injectivity assertion for a tensor product formed from the different source \(R\).

## TRC3. The actual source tensor map

The continuous \(k\)-linear map
\[
(F_1,\ldots,F_k)\longmapsto
\left(\prod_{j=1}^k\delta_r(\rho_j)F_j(\rho_j^\#)\right)_{\boldsymbol\rho}
\]
induces a unique continuous linear map
\[
\beta_r^{[k]}:R\widehat\otimes_\pi\cdots\widehat\otimes_\pi R
\longrightarrow H_\infty^{(k)}.
\tag{TRC3.1}
\]
For each \(N\), continuity of the original \(\beta_r\) gives an original continuous source seminorm \(s_N\) and a finite constant \(C_N\) such that \(p_N(\beta_rF)\le C_Ns_N(F)\). Equation (TRC2.2) then bounds the displayed multilinear map by \(C_N^k\prod_js_N(F_j)\). The projective universal property gives a continuous map on the algebraic tensor product, and completeness of the target gives (TRC3.1). This argument retains the original source topology throughout.

For a tuple \(\boldsymbol\rho\), choose \(F_j\in R\) with \(\beta_rF_j=e_{\rho_j}\), using ADM3.5. The image of \(F_1\otimes\cdots\otimes F_k\) is the coordinate vector at that tuple. All finitely supported target vectors therefore occur in the image. TRC1 proves
\[
\overline{\operatorname{im}\beta_r^{[k]}}^{\,H_\infty^{(k)}}=H_\infty^{(k)}.
\tag{TRC3.2}
\]
Neither surjectivity nor injectivity of (TRC3.1) follows from this density assertion.

If \(\beta_r\ne0\), choose \(F\in R\) and \(\rho\in I\) with \((\beta_rF)_\rho\ne0\). Coordinate evaluation after \(\beta_r\) is a continuous linear functional \(\ell_\rho\) on the original source. The functional \((F_1,\ldots,F_k)\mapsto\prod_j\ell_\rho(F_j)\) extends continuously to its completed projective tensor product. Its value on the canonical tensor \(F\otimes\cdots\otimes F\) is \(\ell_\rho(F)^k\ne0\); hence that tensor survives completion. At \((\rho,\ldots,\rho)\), its image under \(\beta_r^{[k]}\) has exactly the same nonzero value. Thus
\[
\beta_r\ne0\ \Longrightarrow\ \beta_r^{[k]}\ne0
\quad\hbox{for every integer }k\ge1.
\tag{TRC3.3}
\]
This proof does not presume injectivity of any completed tensor map. If \(I\) is empty, \(E=0\), \(R=0\) by ADM3.4, and every displayed positive-order tensor receiver is zero.

## TRC4. Exact integer-cover covariance

Keep the genuine integer coefficient action \(T_n[F]=[n^sF]\). Its induced action on \(R\) is continuous, since \(N_O\) is invariant. Define
\[
U_n=T_n\widehat\otimes_\pi\cdots\widehat\otimes_\pi T_n,
\qquad
(V_ny)_{\boldsymbol\rho}=n^{\sum_{j=1}^k\rho_j^\#}y_{\boldsymbol\rho}.
\tag{TRC4.1}
\]
As \(0<\Re\rho_j^\#<1\), \(P_N(V_ny)\le n^kP_N(y)\) for integers \(n\ge1\). Its inverse is the similarly continuous diagonal coefficient operator with \(n^{-\sum_j\rho_j^\#}\). ADM3.6 in each factor proves on decomposable tensors, and then by continuity on the completion,
\[
\beta_r^{[k]}U_n=V_n\beta_r^{[k]}.
\tag{TRC4.2}
\]
The same calculation for general positive coefficient parameter \(a\) is valid; it does not describe a noninteger geometric cover.

## TRC5. Finite blocks and reflection-paired tensors

For any actual \(\lambda\in I\), let \(v_\lambda\in R\) be the class of the original full-jet isolator with value one at \(\lambda\) and zero values at every other actual zero. Then
\[
T_nv_\lambda=n^\lambda v_\lambda,\qquad
\beta_rv_\lambda=\delta_r(\lambda^\#)e_{\lambda^\#}.
\tag{TRC5.1}
\]
The first equality is exact in \(R\), since its difference has zero off-line values; all higher-jet information is retained in the known kernel \(N_O\), rather than discarded from \(Q\). For every finite tuple of actual off-line zeros,
\[
U_n(v_{\lambda_1}\otimes\cdots\otimes v_{\lambda_k})
=n^{\lambda_1+\cdots+\lambda_k}
v_{\lambda_1}\otimes\cdots\otimes v_{\lambda_k},
\]
\[
\beta_r^{[k]}(v_{\lambda_1}\otimes\cdots\otimes v_{\lambda_k})
=\left(\prod_{j=1}^k\delta_r(\lambda_j^\#)\right)
e_{(\lambda_1^\#,\ldots,\lambda_k^\#)}.
\tag{TRC5.2}
\]
The image coefficient is nonzero. Its target cover eigenvalue is exactly \(n^{\lambda_1+\cdots+\lambda_k}\), the same as its source eigenvalue. This applies also when different tuples have the same sum. Hence no source/target spectral separation is created on any such block.

Write \(\lambda=x+i\gamma\). A repeated tensor has exact eigenvalue and absolute value
\[
v_\lambda^{\otimes k}:\qquad n^{kx+ik\gamma},\qquad n^{kx}.
\tag{TRC5.3}
\]
The reflection-paired tensor uses \(\lambda^\#=1-x+i\gamma\), so
\[
v_\lambda\otimes v_{\lambda^\#}:\qquad
n^{1+2i\gamma},\qquad n.
\tag{TRC5.4}
\]
Its nonzero receiver coefficient is retained in full:
\[
\delta_r(\lambda^\#)\delta_r(\lambda)
=-e^{2i\gamma\log r}\bigl(r^x-r^{1-x}\bigr)^2.
\tag{TRC5.5}
\]
The minus sign and phase have not disappeared. For \(2j\) factors consisting of \(j\) copies of this pair, the eigenvalue is \(n^{j+2ij\gamma}\), its absolute value is \(n^j\), and its nonzero receiver coefficient is the \(j\)-th power of (TRC5.5).

Thus reflection-paired tensors have total real part \(k/2\) for even \(k\), even when every factor is off-line. Their existence, for an actual off-line zero, is compatible with the repeated tensor having total real part \(kx\ne k/2\). If the word weight is used with the convention \(|\alpha_n|=n^{w/2}\), these displayed values correspond respectively to \(w=2kx\) and \(w=k\); these are calculations of absolute values, not a proof of a geometric purity structure on the source.

## TRC6. Transfer factor caveat

The tensor product of the \(k\) original coefficient-transfer operators is exactly
\[
(nT_{1/n})^{\otimes k}=n^k(T_{1/n})^{\otimes k}.
\tag{TRC6.1}
\]
An identification of this tensor operation with a particular geometric transfer must retain the degree of that particular map. The product of \(k\) degree-\(n\) covers has degree \(n^k\). A degree-\(n\) map on one base carrying a tensor coefficient system has degree \(n\); its transfer is not justified by merely copying (TRC6.1). The finite-block matching in TRC5 uses only the specified genuine integer action \((T_n)^{\otimes k}\) and is independent of choosing either geometric interpretation. No new source metric, RH assumption, source tensor injectivity, or unproved purity assertion enters any of TRC0–TRC6.


## Publication source and dependency links

The source geometry is Alain Connes and Caterina Consani, *Schemes over F1 and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The weight-control comparison is Pierre Deligne, *La conjecture de Weil. II*, Publications mathematiques de l'IHES52 (1980),137-252, [§§3.3.11 and3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/). Deligne material was read through the identified French transcription and separately recorded peer source-page checks, not Deligne-authored TeX. These sources are not asserted to contain the new programme derivations. The [preceding complete proof and reading record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/BUILD_AND_REVIEW.md) records inherited source versions and actual inspection limits. The investigator's corrected construction remains attributed in the original text above.
