# Complete conormal derivative and tensor residue proof

The complete final proof is `tex/conormal_finite_weyl.tex`, SHA256 `731b72e56eb311c456424eb917b090f7d796c34948537112322d162164b41277`. It contains every definition, theorem, identity and proof in CW.1–52. The full source text is reproduced below.

The original source witness is `sources/web_sum_connection_delivery/Tau_Sum_Connection_Control/NOTE.tex`, SHA256 `11870208e3a08df186e42629ae1a6c956faaf28f79dfce0dc2f2d44dc64b4687`. All eight sections were read. The present calculation extends its first-thickening derivative and source-unit constructions with the complete dual-number image, exact section correction, actual minimum-section change, residue functional and tensor partial-residue formulas.

## Source preservation and report locations

The first 24,487 bytes are exactly the previously reviewed CW.1–40 source, SHA256 `6ca142ec052ad110e3c58ece4d81bf87a33fc18c8533c41deb863bceb300715a`. The final extension appends CW.41, proving the full arithmetic unit's image and inverse under Phi, followed by CW.42–52, integrating the complete independently reviewed PRC.1–11 proof. No earlier CW byte, original coordinate, zero order, source factor, arithmetic unit, or map type was replaced.

The private workspace report is `work/conormal_finite_weyl_20260912.md`. Its identical portable copy, intended to accompany the source package, is `logbook/conormal_finite_weyl_20260912.md`. These paths identify the two copies; the public package is rooted at `output/split_zero_rh_tandem_2026-09-12` in the workspace. The prior CW.1–40 report is retained privately in `work/conormal_finite_weyl_review_20260912/original_cw1_40_proof_report.md`. The cumulative main TeX and publication PDF are maintained separately by the integration lane.

## Independent proof and implementation reviews

The final complete-source review reads CW.1–52 at the final hash above. Earlier separate reviews read every CW.1–40 definition and proof, the full PRC.1–11 continuation, and the exact polynomial checker. Portable audit copies express local source-file locations relative to the package. Private and package hashes are identified separately whenever that path substitution changes bytes; their mathematical review and audited source hashes are unchanged. The full audit records, with their proof chains, are:

- Package `logbook/conormal_weyl_formula_audit_20260912.md`; package SHA256 `99b319eb8165020044dacb79444ae1b43b712b0b4be2010c3e135ebb6022d675`; private audit SHA256 `99b319eb8165020044dacb79444ae1b43b712b0b4be2010c3e135ebb6022d675`.
- Package `logbook/conormal_finite_weyl_source_final_review_20260912.md`; package SHA256 `1908ca473c3caa37fb022edea6ebeb14902bfef9ff18833917f01903c0353048`; private audit SHA256 `38f96126616b6725db941ec00037c197cdb3eed77f0688debc8670411d722108`.
- Package `logbook/conormal_partial_residue_independent_audit_20260912.md`; package SHA256 `953bc7fc883a80fd06890475f74cd2d911fef2fd3da3898af419f2e2a538ef90`; private audit SHA256 `953bc7fc883a80fd06890475f74cd2d911fef2fd3da3898af419f2e2a538ef90`.
- Package `logbook/conormal_finite_weyl_integrated_final_audit_20260912.md`; package SHA256 `d246ed9aebf8ced820b8fb052fcbdabd8ff53b902c9b2c3b8e960ae4c7129d2e`; private audit SHA256 `d246ed9aebf8ced820b8fb052fcbdabd8ff53b902c9b2c3b8e960ae4c7129d2e`.

The algebraic checker is `scripts/check_conormal_finite_weyl.py`, SHA256 `307b9b879a46f56a8701e9f920a085e1a75257de8d931ae22efdff7ce8fac7a9`. Normal and optimized Python each pass 1,076 records: 991 exact identities and 85 negative controls. Their record arrays are identical. Both deliberate false-identity runs fail precisely their added 1,077th record. The four process exits are 0, 0, 1, 1. Complete receipts are `checks/conormal_finite_weyl.json`, `checks/conormal_finite_weyl_optimized.json`, `checks/conormal_finite_weyl_negative.json` and `checks/conormal_finite_weyl_negative_optimized.json`.

Those computations concern the retained original polynomial quotient, first thickening, centered operator, section projectors, full conormal unit component and dual-number algebra map in declared exact calibration fixtures. Their mathematical tests cover the original CW.1–40 identities. The appended residue continuation and Phi-unit corollary receive independent complete proof review; no new numerical arithmetic claim is inferred from the earlier fixtures. The actual arithmetic functions and units are retained in the proofs below.

## Rendering verification

An isolated wrapper using the current cumulative preamble compiled successfully in two XeLaTeX passes. Its complete nine-page PDF is retained privately at `work/conormal_finite_weyl_final_review_20260912/conormal_finite_weyl_final_review.pdf`. Every page was rendered at 110 dpi and individually inspected with the image tool. The complete final log contains no warning, overfull box, underfull box, missing glyph or unresolved reference. No rendered overlap, clipping or unreadable equation was found.

The portable hash-scoped receipt is `checks/conormal_finite_weyl_final_visual_review.json`; the private copy is `work/conormal_finite_weyl_final_review_20260912/verification_receipt.json`. The frozen earlier edition was not changed.

## Complete delivered proof

```tex
\section{The original conormal derivative and its finite section commutator}
\label{sec:conormal-finite-weyl}

The sum-connection source constructs differentiation on the first
thickening of the original packet ideal.  We prove its algebra map
to dual numbers, then compute the exact finite endomorphism obtained
from the original monic remainder section and from its full arithmetic
unit.  The conormal row and the section correction have different
domains; their explicit factorization, complete ranks, and residue
comparison are retained throughout.

\subsection{The first thickening and the dual-number map}

Let \(k\ge1\), and retain a nonempty packet of actual zeros with all
complete orders,
\[
 h(s)=\prod_{\rho\in\mathcal Z}(s-\rho)^{m_\rho},\quad
 d=\deg h\ge1,\quad r_0=|\mathcal Z|,\quad g=2\xi,\quad v_h=g/h.
 \tag{CW.1}
\]
Write \(h_i=h(s_i)\), and put
\[
 \begin{gathered}
 P=\mathbb C[s_1,\ldots,s_k],\quad I=(h_1,\ldots,h_k),\quad
 E=P/I,\quad E^{[2]}=P/I^2,\quad N=I/I^2,\\
 \pi:E^{[2]}\to E,\qquad
 \partial_\Sigma=\frac1k\sum_{i=1}^k\partial_{s_i},\qquad
 \delta:E^{[2]}\to E,\quad [p]\mapsto[\partial_\Sigma p].
 \end{gathered}                                                    \tag{CW.2}
\]
The derivative maps \(I^2\) into \(I\) by the product rule, so
\(\delta\) has exactly the stated type.
For each \(i\), the class of \(h_i\) maps to zero under
\(\pi\), while \(\delta[h_i]=h_i'/k\ne0\) in the retained
remainder basis.  Thus factoring \(\delta\) through \(\pi\)
would fail on this explicit class.  The full algebra map
(CW.6) below retains both its quotient value and derivative.
Monic division in each original variable gives a unique expansion
\[
 p=\sum_{\mathbf a\in\mathbb N^k}
     h_1^{a_1}\cdots h_k^{a_k}p_{\mathbf a},\qquad
 \deg_{s_i}p_{\mathbf a}<d .
 \tag{CW.3}
\]
Only finitely many terms occur.  Existence follows by repeated
one-variable division, which commutes for distinct variables.
For uniqueness, the leading monomials
\(\prod_i s_i^{da_i+b_i}\), \(0\le b_i<d\), of the
corresponding products are all distinct; comparison in a monomial
order, followed by subtraction, proves independence.
This also proves that the \(h_i\) are algebraically independent
and that \(P\) is free over \(\mathbb C[h_1,\ldots,h_k]\)
with the original remainder basis.

Consequently the original conormal coefficient map is the
\(E\)-module isomorphism
\[
 \iota_N:E^k\xrightarrow{\sim}N,\qquad
 (a_i)\longmapsto\left[\sum_i h_i\widetilde a_i\right]_{I^2},
 \quad
 \dim E=d^k,\quad \dim E^{[2]}=(k+1)d^k .
 \tag{CW.4}
\]
Changing a lift \(\widetilde a_i\) adds an element of \(I^2\).
Modulo \(I^2\), (CW.3) has exactly its constant coefficient and
its \(k\) linear \(h_i\)-coefficients, proving every assertion
in (CW.4).  In particular \(N^2=0\) in \(E^{[2]}\).
The derivative obeys
\[
 \delta(ab)=\pi(a)\delta(b)+\pi(b)\delta(a),\qquad
 \delta\iota_N(a_i)=\frac1k\sum_i h_i'a_i .
 \tag{CW.5}
\]
These identities follow before taking the indicated quotients;
the terms still containing \(h_i\) vanish only in \(E\).

\begin{theorem}[A full algebra bridge for the coefficient derivative]
Let \(B=E[\epsilon]/(\epsilon^2)\), where \(\epsilon\) is a
formal infinitesimal, and let \(\mathfrak j=(h_1',\ldots,h_k')\)
be the indicated ideal of \(E\).  There is a unital algebra map
\[
 \Phi:E^{[2]}\to B,\qquad
 a\longmapsto\pi(a)+\epsilon\delta(a).
 \tag{CW.6}
\]
The derivative induces
\(\overline\partial_\Sigma:E\to E/\mathfrak j\), and its image
and kernel are exactly
\[
 \begin{gathered}
 \operatorname{im}\Phi
   =\{q+\epsilon t:[t]_{\mathfrak j}
                         =\overline\partial_\Sigma q\},\\
 \ker\Phi=\iota_N\ker\left(E^k\xrightarrow{(a_i)\mapsto
                               k^{-1}\sum_i h_i'a_i}E\right).
 \end{gathered}                                                    \tag{CW.7}
\]
There is the exact sequence of complex vector spaces
\[
 0\longrightarrow\ker(\delta|_N)\longrightarrow E^{[2]}
 \xrightarrow{\Phi} B
 \xrightarrow{\Psi}E/\mathfrak j\longrightarrow0,\qquad
 \Psi(q+\epsilon t)=[t]_{\mathfrak j}
                              -\overline\partial_\Sigma q .
 \tag{CW.8}
\]
The map \(\Phi\) is an algebra homomorphism; \(\Psi\) is given
its displayed complex-linear type.
The complete ranks and dimensions are
\[
 \begin{aligned}
 \operatorname{rank}(\delta|_N)&=d^k-(d-r_0)^k,\\
 \dim\ker\Phi&=(k-1)d^k+(d-r_0)^k,\\
 \dim\operatorname{im}\Phi&=2d^k-(d-r_0)^k.
 \end{aligned}                                                    \tag{CW.9}
\]
\end{theorem}
\begin{proof}
Equation (CW.5) gives
\[
 \Phi(ab)=\pi(a)\pi(b)+
       \epsilon\{\pi(a)\delta(b)+\pi(b)\delta(a)\}
          =\Phi(a)\Phi(b),
\]
and \(\delta(1)=0\), proving the unital algebra claim.
Changing a representative of \(q\in E\) by \(\sum_i h_ip_i\)
changes its derivative modulo \(I\) by
\(k^{-1}\sum_i h_i'[p_i]\in\mathfrak j\).
Thus \(\overline\partial_\Sigma\) is well-defined, with its
product rule along \(E\to E/\mathfrak j\).
Every \(\Phi(a)\) consequently satisfies the condition in
(CW.7).

Conversely let that condition hold.  Take the unique original
monic remainder \(\sigma(q)\in P\), of degree below \(d\)
in every variable.  Then
\[
 t-\delta[\sigma(q)]_{I^2}
             =\frac1k\sum_i h_i'a_i
\]
for some \(a_i\in E\), by the definition of \(\mathfrak j\).
The element
\([\sigma(q)]_{I^2}+\iota_N(a_i)\) has image \(q+\epsilon t\).
This proves the image equality.  Its kernel requires
\(\pi(a)=0\), hence \(a\in N\), and then exactly the vanishing
of the row in (CW.5).  This proves the kernel statement.
The map \(\Psi\) is onto, since \(\Psi(\epsilon t)=[t]\),
and its kernel is the already computed image of \(\Phi\).
This proves (CW.8) with its exact map types.

For the ranks, retain an ordered local tensor block at centres
\(\rho_i\), of full lengths \(m_i\).  In its coordinates
\[
 L=\mathbb C[z_1,\ldots,z_k]/(z_1^{m_1},\ldots,z_k^{m_k}),
 \qquad z_i=s_i-\rho_i,
\]
write \(h(s_i)=z_i^{m_i}c_i(z_i)\), \(c_i(0)\ne0\).
Modulo the original local ideal,
\[
 h_i'=m_ic_i(0)z_i^{m_i-1},\qquad
 h_i'a_i=m_ic_i(0)z_i^{m_i-1}
                      a_i|_{z_i=0}.
 \tag{CW.10}
\]
Thus the original input constant coefficient in the \(i\)-th
variable is sent into that variable's top nilpotent direction;
all remaining variables and the factor \(m_ic_i(0)\) are retained.
The row image is the ideal spanned by monomials having at
least one exponent \(m_i-1\).  Its dimension is
\(\prod_i m_i-\prod_i(m_i-1)\).
The excluded monomials remain in the complementary vector
space and in \(E/\mathfrak j\).
Sum over every ordered tuple of centres.  The two sums are
\[
 \sum_{\rho_1,\ldots,\rho_k}\prod_i m_{\rho_i}=d^k,\qquad
 \sum_{\rho_1,\ldots,\rho_k}\prod_i(m_{\rho_i}-1)
                                  =(d-r_0)^k .
 \tag{CW.11}
\]
This proves the first line of (CW.9).  Subtract it from
\(\dim N=kd^k\) for the kernel, then subtract that kernel
from \(\dim E^{[2]}\) for the image, proving the other two.
These counts include every simple and repeated local factor.
\end{proof}

When the packet has the original reflection
\(a^\dagger(\mathbf s)=\overline{a(1-\overline{\mathbf s})}\),
its ideals are stable because \(h^\dagger=(-1)^dh\).
The derivative satisfies
\(\delta(a^\dagger)=-(\delta a)^\dagger\).
Set \((q+\epsilon t)^\dagger=q^\dagger-\epsilon t^\dagger\).
Then \(\Phi(a^\dagger)=\Phi(a)^\dagger\), by (CW.6).
This retains the sign of the infinitesimal and the original
conjugate-linear reflection.

\subsection{The original monic section and the exact finite correction}

Let \(\sigma:E\to P\) denote the multivariate monic remainder
section of (CW.3), and set \(j=[\sigma]_{I^2}:E\to E^{[2]}\).
It is complex-linear, with \(\pi j=I_E\).
Let \(S=\sum_i s_i\), and write \(Z\) and \(\widehat Z\)
for multiplication by \(S-k/2\) on \(E\) and \(E^{[2]}\),
respectively.  The original product rule gives the rectangular
operator identity
\[
 Z\delta-\delta\widehat Z=-\pi,\qquad
 \mathsf D_0=\delta j:E\to E .
 \tag{CW.12}
\]
The original finite arithmetic generator is \(A_k=Z+(k/2)I_E\).

For each \(i\), let
\(\ell_i:E\to E_{\widehat i}:=\bigotimes_{j\ne i}E_h\)
extract the coefficient of \(s_i^{d-1}\) in \(\sigma(u)\).
Let \(c_i:E_{\widehat i}\to E\) insert the constant polynomial
one in the \(i\)-th variable.  If \(k=1\), the target of
\(\ell_1\) is \(\mathbb C\), and \(c_1\) is its unit column.
These maps give the exact section defect
\[
 \begin{gathered}
 \mathsf t_Z:=\widehat Zj-jZ
       =\iota_N(c_1\ell_1,\ldots,c_k\ell_k):E\to N,\\
 [Z,\mathsf D_0]=-I_E+\mathsf J,\qquad
 \mathsf J=\delta\mathsf t_Z
       =\frac1k\sum_i M_{h_i'}c_i\ell_i .
 \end{gathered}                                                    \tag{CW.13}
\]
Indeed multiplying the original remainder by \(s_i\) creates
only its top \(s_i^d\) term outside the admitted coordinate
range.  Monic division subtracts exactly
\(h_i\sigma_{\widehat i}(\ell_i u)\).
Adding these terms for \(S-k/2\) proves the first formula.
Compose (CW.12) with \(j\) and use
\(\widehat Zj=jZ+\mathsf t_Z\); this proves the commutator
with its minus sign.  Applying (CW.5) proves its last formula.
In particular this is a specified endomorphism of the original
finite vector space, obtained by a declared section of \(\pi\).

\begin{theorem}[All projectors, eigenvalues and ranks of the section correction]
The original coordinate endomorphisms
\[
 P_i=\frac1dM_{h_i'}c_i\ell_i,\qquad
 P_i^2=P_i,\qquad P_iP_j=P_jP_i,\qquad
 \operatorname{rank}P_i=d^{k-1}
 \tag{CW.14}
\]
are commuting idempotents.  For \(T\subset\{1,\ldots,k\}\), put
\[
 P_T=\prod_{i\in T}P_i\prod_{i\notin T}(I-P_i).
 \tag{CW.15}
\]
Their pairwise products are zero when their labels differ, and
\(\sum_TP_T=I_E\).  On their ranges the full correction has
\[
 \mathsf J=\frac d k\sum_iP_i,\qquad
 \mathsf J|_{\operatorname{ran}P_T}=\frac{d|T|}{k}I .
 \tag{CW.16}
\]
For \(d>1\), its eigenvalue \(dj/k\) has multiplicity
\(\binom kj(d-1)^{k-j}\), for every \(0\le j\le k\).
For all \(d\ge1\),
\[
 \operatorname{Tr}\mathsf J=d^k,\qquad
 \operatorname{rank}\mathsf J=d^k-(d-1)^k,\qquad
 \ker\mathsf J=\bigcap_i\ker\ell_i .
 \tag{CW.17}
\]
For \(d=1\), every \(P_i=I\), \(\mathsf J=I\), and only
the \(j=k\) eigenspace is nonzero, of dimension one.
\end{theorem}
\begin{proof}
The polynomial \(h_i'\) has degree \(d-1\) and leading
coefficient \(d\).  Therefore
\[
 \ell_i M_{h_i'}c_i=dI_{E_{\widehat i}} .
 \tag{CW.18}
\]
Substitution proves \(P_i^2=P_i\).  It also proves that
\(M_{h_i'}c_i\) is injective, and hence that the rank is
\(d^{k-1}\).  Operators in distinct variables are tensor
products of their respective one-variable maps, so they commute.
The one-variable space is the direct sum of
\(\mathbb C h'\) and the polynomials of degree at most \(d-2\):
the former has nonzero top coefficient \(d\), and every
polynomial splits by subtracting that top coefficient times
\(h'/d\).  These are the image of \(P_i\) and the kernel of
\(\ell_i\), of dimensions one and \(d-1\).

Taking tensor products of these direct decompositions proves
all the identities for \(P_T\) and gives
\(\dim\operatorname{ran}P_T=(d-1)^{k-|T|}\) when \(d>1\).
On this range exactly the \(P_i\) for \(i\in T\) act as
identity, proving (CW.16).
Summing over \(|T|=j\) gives the asserted multiplicity.
Its zero space is the all-complement range, of dimension
\((d-1)^k\), proving the rank and kernel in (CW.17).
Finally
\[
 \operatorname{Tr}\mathsf J
   =\frac d k\sum_i\operatorname{rank}P_i
   =\frac d k\,k d^{k-1}=d^k .
 \tag{CW.19}
\]
For \(d=1\), the one-variable complement is zero and its image
is the entire one-dimensional space.  Only the all-image
tensor survives.  This proves the stated endpoint directly,
without assigning a positive multiplicity to a zero-dimensional
space.
\end{proof}

These are algebraic idempotents in the retained coordinates.
For any actual positive minimum metric \(G_M\), their exact
metric adjoints and coordinate transports are
\[
 P_i^{\dagger_{G_M}}=G_M^{-1}P_i^*G_M,\qquad
 \widetilde P_i=G_M^{1/2}P_iG_M^{-1/2},\qquad
 \widetilde{\mathsf J}=G_M^{1/2}\mathsf JG_M^{-1/2}.
 \tag{CW.20}
\]
The transports retain the products, ranks and algebraic spectrum.
For each \(i\), the individual \(\widetilde P_i\) is Hermitian
precisely when \(P_i^*G_M=G_MP_i\), whereas
\(\widetilde{\mathsf J}\) is Hermitian precisely when
\(\mathsf J^*G_M=G_M\mathsf J\).  None of these metric
equalities is assumed.
The same isometry carries the original weight to
\[
 G_M^{-1/2}W_MG_M^{-1/2}
    =\widetilde Z^{\,*}+\widetilde Z,\qquad
 \widetilde Z=G_M^{1/2}ZG_M^{-1/2},
 \quad W_M=A_k^*G_M+G_MA_k-kG_M .
 \tag{CW.21}
\]
It carries (CW.13) to the identical commutator with all three
operators transported.  Thus the algebraic correction and the
original Hermitian weight have an explicit common coordinate
map, with every adjoint still attached to its actual metric.

The full conormal row rank in (CW.9) and the section rank in
(CW.17) are connected by exactly
\[
 E\xrightarrow{\ (c_i\ell_i)_i\ }E^k
   \xrightarrow{\ \iota_N\ }N
   \xrightarrow{\ \delta|_N\ }E.
 \tag{CW.22}
\]
Its composite is \(\mathsf J\).
The first map retains the specific highest-coordinate
coefficients of the monic section; the full conormal row
accepts arbitrary \(k\) input coefficients.
This proves the relationship between the two ranks without
replacing one domain by the other.

\subsection{The full arithmetic unit and the original finite representatives}

Keep the complete Taylor classes
\[
 \widehat U=\left[\prod_i v_h(s_i)\right]_{I^2}\in(E^{[2]})^\times,
 \qquad U=\pi(\widehat U)\in E^\times,\qquad
 \beta_h=U^{-1}\delta\widehat U\in E.
 \tag{CW.23}
\]
Finite multivariate Hermite interpolation supplies these classes
from the entire original functions near every ordered packet
point.  Their values are nonzero at those points because the
removed orders were complete.  One can also prove invertibility
in the thickening directly: lift \(U^{-1}\) to \(b\); then
\(\widehat Ub=1+n\), \(n\in N\), and \(b(1-n)\) is the
inverse since \(N^2=0\).
Thus this thickening retains the original unit and its first
relation derivatives.

\begin{theorem}[The unit-conjugated finite Weyl identity]
Define the actual unit section and its derivative by
\[
 j_U=\widehat U\,j\,U^{-1}:E\to E^{[2]},\quad
 \pi j_U=I_E,\qquad
 \mathsf D_U=\delta j_U
            =M_{\beta_h}+M_U\mathsf D_0M_U^{-1}.
 \tag{CW.24}
\]
Then, with all multiplication operators in the original basis,
\[
 \begin{gathered}
 \mathsf t_U:=\widehat Zj_U-j_UZ
                =M_{\widehat U}\mathsf t_ZM_U^{-1}:E\to N,\\
 [Z,\mathsf D_U]=-I_E+\mathsf J_U,\qquad
 \mathsf J_U=\delta\mathsf t_U=M_U\mathsf JM_U^{-1}.
 \end{gathered}                                                    \tag{CW.25}
\]
The complete spectrum, multiplicities, ranks and trace in
(CW.16)--(CW.19) therefore hold for \(\mathsf J_U\) as well.
\end{theorem}
\begin{proof}
The section equation follows from \(\pi j=I\) and
\(\pi(\widehat U)=U\).
Apply (CW.5) to \(\widehat Uj(U^{-1}u)\).
Its two terms are
\((\delta\widehat U)U^{-1}u\) and \(U\mathsf D_0(U^{-1}u)\),
which prove (CW.24).
The multiplication maps \(\widehat Z,M_{\widehat U}\)
commute, as do \(Z,M_U^{-1}\).  This proves the formula
for \(\mathsf t_U\).
Its image lies in \(N\), so the product-rule term
\((\delta\widehat U)\pi(\mathsf t_ZM_U^{-1}u)\) vanishes
exactly.  The other term is \(U\mathsf JM_U^{-1}u\),
proving the last equality in (CW.25).
Finally \(M_{\beta_h}\) commutes with multiplication by \(Z\).
Conjugating (CW.13) by \(M_U\) proves the commutator.
Similarity gives the entire stated spectrum and its zero
space, without making an orthogonality claim.
\end{proof}

These sections have an original analytic realization.
Let
\[
 \mathcal T_h^{(k)}p=p(D_1,\ldots,D_k)F_h^{\otimes k},
 \quad
 \mathscr L_k=\frac1k\sum_i\log x_i,\quad
 R_{\rm ref}^{(k)}u=\mathcal T_h^{(k)}\sigma(U^{-1}u).
 \tag{CW.26}
\]
The original Mellin transform gives
\(\mathcal M_k\mathcal T_h^{(k)}p=(\prod_i v_h(s_i))p\).
Its thickened Taylor class is
\(\widehat U[p]_{I^2}\), so the thickened class of
\(R_{\rm ref}^{(k)}u\) is exactly \(j_Uu\).
Multiplication by \(\mathscr L_k\) differentiates this Mellin
transform by \(\partial_\Sigma\).  Hence
\[
 J^{(k)}\mathscr L_kR_{\rm ref}^{(k)}=\mathsf D_U .
 \tag{CW.27}
\]
This is the finite endomorphism of the specified original
section, with its actual logarithmic source observable.

For the actual degree-\(M\) minimum, \(M\ge k(d-1)\), retain
its original coefficient Gram \(\mathcal M_M>0\) and full
jet matrix \(\mathcal J_M\), including multiplication by \(U\).
Its numerator and source function are exactly
\[
 p_{M,u}=\mathcal M_M^{-1}\mathcal J_M^*G_Mu,\qquad
 G_M=(\mathcal J_M\mathcal M_M^{-1}\mathcal J_M^*)^{-1},
 \qquad R_Mu=\mathcal T_h^{(k)}p_{M,u}.
 \tag{CW.28}
\]
Indeed its jet is \(u\), and its coefficient vector is
\(\mathcal M_M\)-orthogonal to \(\ker\mathcal J_M\).
Every other preimage differs by such a kernel vector;
Pythagoras proves this same original constrained minimum.
Define the concrete thickened section and admitted relation by
\[
 j_Mu=\widehat U[p_{M,u}]_{I^2},\qquad
 a_M=j_M-j_U:E\to N,\qquad
 \mathsf D_M=\delta j_M=\mathsf D_U+\delta a_M.
 \tag{CW.29}
\]
The image statement follows from \(\pi j_M=\pi j_U=I_E\).
Its numerator is the original allowed relation
\(p_{M,u}-\sigma(U^{-1}u)\in I\), not an independently
chosen vector in the conormal layer.
The corresponding exact identities are
\[
 \begin{gathered}
 J^{(k)}\mathscr L_kR_M=\mathsf D_M,\qquad
 [Z,\mathsf D_M]=-I_E+\mathsf J_M^{\rm sec},\\
 \mathsf J_M^{\rm sec}
   :=\delta(\widehat Zj_M-j_MZ)
    =\mathsf J_U+[Z,\delta a_M],\qquad
 \operatorname{Tr}\mathsf J_M^{\rm sec}=d^k .
 \end{gathered}                                                    \tag{CW.30}
\]
The first follows by the same original Mellin differentiation.
For the second, compose (CW.12) with \(j_M\).
For the third, subtract (CW.25) and use
\(\delta\widehat Za_M=Za_M^{\,\delta}\), where
\(a_M^{\,\delta}=\delta a_M\), since \(\pi a_M=0\).
This gives exactly the displayed commutator difference.
Its trace is zero by the cyclic identity for finite matrices;
(CW.19) gives the final trace.
Only the specified fixed-section correction is assigned the
ranks (CW.17).  Every change to the actual minimum is retained
through the computed map \(a_M\) and its commutator.

\subsection{The one-variable residue functional and the original theta relation}

Take \(k=1\), write \(\ell:E_h\to\mathbb C\) for the
coefficient of \(s^{d-1}\), and let \(U=j_hv_h\).
The product derivative \(g'=h'v_h+hv_h'\) gives
\[
 \mathsf J_U
   =M_{j_hg'}c_1\ell M_U^{-1},\qquad
 \mathsf J_Uu=(j_hg')\,\ell(U^{-1}u),\qquad
 \operatorname{rank}\mathsf J_U=1,\quad
 \operatorname{Tr}\mathsf J_U=d .
 \tag{CW.31}
\]
The rank follows either from (CW.25) or from the nonzero
column \(j_hg'=Uh'\) and the nonzero functional.
The trace of this rank-one map is
\(\ell(U^{-1}j_hg')=\ell(h')=d\).

For the original reflection-stable packet, put
\(f^\dagger(s)=\overline{f(1-\overline s)}\).
Its residue pairing is the well-defined form
\[
 \mathscr R_{\mathcal Z}(f,u)
  =\sum_{\rho\in\mathcal Z}
      \operatorname{Res}_{s=\rho}
       \frac{\widetilde f^\dagger(s)\widetilde u(s)}{g(s)}\,ds
  =\ell(U^{-1}f^\dagger u).
 \tag{CW.32}
\]
Changing either polynomial representative by \(h\) changes
the integrand by a function holomorphic at all selected
centres: \(h^\dagger=(-1)^dh\), and \(g=hv_h\), with
\(v_h\) nonvanishing there.
To prove the last equality, take
\(p=\operatorname{rem}_h(U^{-1}f^\dagger u)\), of degree
below \(d\).  The residues of the displayed quotient equal
those of \(p/h\).  In the partial-fraction expansion of
\(p/h\), the coefficient of \(1/s\) at infinity is the
sum of its coefficients at the simple-pole terms; terms
of pole order at least two have no \(1/s\) coefficient.
Since \(h\) is monic of degree \(d\), that coefficient is
exactly the original coefficient \(\ell(p)\).
This proves (CW.32), keeping every higher local pole before
the residue is taken.
Consequently the finite correction is precisely
\[
 \boxed{\mathsf J_Uu=(j_hg')\,\mathscr R_{\mathcal Z}(1,u),
 \qquad
 \operatorname{Tr}\mathsf J_U
      =\mathscr R_{\mathcal Z}(1,j_hg')
      =\sum_{\rho\in\mathcal Z}m_\rho=d.}
 \tag{CW.33}
\]

The source map producing the same Jacobian is the original
logarithmic theta observation:
\[
 J_h(\log x\,\Theta\phi)=j_h(g')\,j_h(H_\phi),\qquad
 \mathcal M\Theta\phi=gH_\phi .
 \tag{CW.34}
\]
Differentiate the Mellin product before taking jets.
Its \(gH_\phi'\) term vanishes modulo the original \(h\);
its other term is exactly (CW.34).
For \(\phi=P(D)\phi_*\), one has \(H_\phi=P\), so the
input ranges through all original finite coefficients.
Thus this map's finite image is the full ideal \((j_hg')\),
of dimension \(r_0\) by (CW.10), rather than a selected
one-dimensional input line.
The exact connection to (CW.31) is its precomposition with
\[
 E_h\xrightarrow{\ \ell M_U^{-1}\ }\mathbb C
                   \xrightarrow{\ c_1\ }E_h.
 \tag{CW.35}
\]
The rank-one correction and the rank-\(r_0\) multiplication
map therefore use the same Jacobian with their distinct
input maps explicitly specified.
Applying (CW.32) to (CW.34) gives, with the full conjugation,
\[
 \mathscr R_{\mathcal Z}(f,j_h(g')j_hP)
  =\sum_{\rho\in\mathcal Z}
       m_\rho\overline{f(1-\overline\rho)}P(\rho).
 \tag{CW.36}
\]
Indeed the residue of \(g'/g\) at a zero of order \(m_\rho\)
is \(m_\rho\), by differentiating its local product.

There is also an exact global source map
\[
 \nu:V\to Q=\mathscr B/\Theta V,\qquad
 \nu(\phi)=q(\log x\,\Theta\phi).
 \tag{CW.37}
\]
Logarithmic multiplication preserves \(\mathscr B\), by its
defining two-sided polynomial bounds: \(|\log x|\le x+x^{-1}\)
and
\(D^j((\log x)F)=(\log x)D^jF-jD^{j-1}F\) for \(j\ge1\)
give every required bound from the original ones.
Thus this map is defined.
For the original \(D=-x\partial_x\),
\([D,\log x]=-I\) and \(D\Theta=\Theta D\).
Therefore
\[
 D_Q\nu-\nu D_V=q[D,\log x]\Theta=-q\Theta=0 .
 \tag{CW.38}
\]
For \(a>0\), let \(\Lambda_aF(x)=F(ax)\).
The identities \(\Theta\Lambda_a=\Lambda_a\Theta\) and
\((\log x)\Lambda_a-\Lambda_a(\log x)
      =-\log(a)\Lambda_a\) similarly give
\(\nu\Lambda_a=\Lambda_a\nu\).
This proves scaling equivariance on the exact source \(V\)
and target \(Q\).  Since \(J_h\Theta=0\), there is the
induced full jet map \(\overline J_h:Q\to E_h\) with
\(\overline J_hq=J_h\); its value on \(\nu\) is exactly
(CW.34).

\subsection{Supported algebra and coefficient maps}

Write \(\operatorname{pr}_0,\operatorname{pr}_\epsilon:B\to E\)
for the constant and infinitesimal coefficient maps.
The first is a unital algebra homomorphism and the second
is complex-linear, with the exact product rule
\[
 \operatorname{pr}_\epsilon(bc)
   =\operatorname{pr}_0(b)\operatorname{pr}_\epsilon(c)
       +\operatorname{pr}_0(c)\operatorname{pr}_\epsilon(b).
 \tag{CW.39}
\]
The strongest typed lift of (CW.6) is the semiring map
\[
 G(E^{[2]})\xrightarrow{\,G(\Phi)\,}G(B),\qquad
 \pi^\tau=G(\operatorname{pr}_0)G(\Phi),\qquad
 \delta^\tau=(\operatorname{pr}_\epsilon)^\tau G(\Phi).
 \tag{CW.40}
\]
Here \(G(\Phi)\) and \(G(\operatorname{pr}_0)\) fix
external \(\tau\) and send supported amplitudes to their
supported algebra images.  The map
\((\operatorname{pr}_\epsilon)^\tau\) is the stated
split-linear coefficient map; (CW.39) specifies its precise
relationship to multiplication.
Its value on the supported unit of \(B\) is the supported
zero \(e_E\).

Every vector in the algebraic kernel in (CW.7) maps under
\(G(\Phi)\) to supported zero, while external absence maps
to external absence.  A supported conormal element \(n\)
maps to \((\epsilon\delta n)^\bullet\), retaining its
coefficient derivative; constant projection gives \(e_E\).
The sections, coefficient maps, exact sequences, and original
representatives above lift at each fixed support by
\((\lambda,u)\mapsto(\lambda,Tu)\).
Thus the first thickening, its full kernel and quotient,
and the source-selected endomorphism retain their distinct
receiving fibres and the common external \(\tau\).

If \(h=1\), then \(I=P\), \(E=E^{[2]}=N=0\), and all
finite maps in (CW.2) have zero source and target.
The source function is still the original theta seed
\(F_h=\Theta\phi_*\), whose map to this arithmetic quotient
is zero.  This states that case explicitly; the projector
formulas dividing by \(d\) above have the declared domain
\(d\ge1\).

\subsection{The arithmetic unit and complete tensor partial residues}

Return to the nonempty original packet of (CW.1), with
\(d\ge1\) and \(k\ge1\).  The unit itself has the following
exact image under the algebra bridge already proved above.

\begin{corollary}[The full unit and its first relation derivative]
For the original \(\widehat U,U,\beta_h\) of (CW.23),
\[
 \begin{gathered}
 \Phi(\widehat U)=U+\epsilon\delta\widehat U
                 =U(1+\epsilon\beta_h),\\
 \Phi(\widehat U^{-1})
    =\Phi(\widehat U)^{-1}
    =U^{-1}(1-\epsilon\beta_h).
 \end{gathered}                                                    \tag{CW.41}
\]
\end{corollary}
\begin{proof}
The first identity is (CW.6) evaluated on the full thickened
unit.  The definition \(\beta_h=U^{-1}\delta\widehat U\)
gives its displayed factorization.  Since \(\epsilon^2=0\),
\((1+\epsilon\beta_h)(1-\epsilon\beta_h)=1\).
The map \(\Phi\) is unital and multiplicative, so applying
it to \(\widehat U\widehat U^{-1}=1\) proves the second
identity with its minus sign.  In particular
\(\Phi(\widehat Ua)=\Phi(\widehat U)\Phi(a)\) transports
the original arithmetic product through this same algebra map.
\end{proof}

Retain all the original complete orders, \(g=2\xi\) and
\(v_h=g/h\), and write
\[
 \begin{gathered}
 E_h=\mathbb C[s]/(h),\qquad E=E_h^{\otimes k},\qquad
 E_{\widehat i}=\bigotimes_{j\ne i}E_h,\\
 v_i=j_h(v_h)\text{ in the \(i\)-th factor},\qquad
 \gamma_i=j_h(g')\text{ in the \(i\)-th factor},\qquad
 U=\prod_i v_i .
 \end{gathered}
\]
Every \(v_i\) is the original complete invertible jet.
Let \(\ell_h:E_h\to\mathbb C\) extract the coefficient of
\(s^{d-1}\) from the unique one-variable monic remainder.
Let \(c_i:E_{\widehat i}\to E\) insert the constant polynomial
one in the \(i\)-th factor, and let
\(\ell_i:E\to E_{\widehat i}\) apply \(\ell_h\) in that
factor and identity in every other factor.
Thus \(\ell_i\) extracts the original coefficient of
\(s_i^{d-1}\), retaining every other-variable coordinate.
For \(k=1\), \(E_{\widehat i}=\mathbb C\), and \(c_i\)
is the unit column.  Let \(M_a\) denote multiplication by
the displayed element in its declared algebra.

Define the coefficient-valued partial residue map
\[
 \mathcal R_i:E\longrightarrow E_{\widehat i},\qquad
 \mathcal R_i(u)=
 \sum_{\rho\in\mathcal Z}\operatorname{Res}_{s_i=\rho}
 \frac{\widetilde u(s_1,\ldots,s_k)}{g(s_i)}\,ds_i .
 \tag{CW.42}
\]
The coefficients in the other original variables are taken
modulo their original ideals after the indicated residue.
Each residue uses the usual positively oriented complex
\(s_i\)-coordinate; the residue notation carries no
additional \(2\pi i\) factor.  Equivalently, each residue
equals \(1/(2\pi i)\) times the corresponding positively
oriented contour integral.

This map is well-defined on \(E\).  A change by \(h(s_i)p\)
in its own variable changes the integrand by \(p/v_h(s_i)\),
which is holomorphic at every selected centre because the
removed zero orders were complete.  A change by \(h(s_j)p\),
\(j\ne i\), produces that same factor \(h(s_j)\) in the
remaining coefficient algebra, hence zero in \(E_{\widehat i}\).
Linearity then covers the full original ideal.
The finite sum of coefficient residues is complex-linear
and \(E_{\widehat i}\)-linear.

The exact coefficient formula is
\[
 \boxed{\mathcal R_i=\ell_iM_{v_i}^{-1}.}                         \tag{CW.43}
\]
To prove it, let \(p_i\) be the degree-below-\(d\) remainder
in \(s_i\) of \(v_i^{-1}u\), retaining the full coefficient
algebra \(E_{\widehat i}\).  The residue in (CW.42) equals
the corresponding residue of \(p_i/h(s_i)\): the difference
in the numerator vanishes to the complete selected orders,
so division by \(h\) is locally holomorphic.
Every coefficient of \(p_i/h\) has an ordinary
partial-fraction expansion.  The coefficient of \(s_i^{-1}\)
at infinity is the sum of the finite simple-pole
coefficients; higher-pole terms contribute no \(s_i^{-1}\)
coefficient.  Since \(h\) is monic and
\(\deg_{s_i}p_i<d\), that coefficient is precisely
\(\ell_i(p_i)\).  This proof applies coefficientwise in
the finite algebra \(E_{\widehat i}\) and gives (CW.43)
with every other-variable nilpotent coefficient retained.

Define the original partial correction endomorphisms
\[
 C_i=M_{\gamma_i}c_i\mathcal R_i:E\longrightarrow E .
 \tag{CW.44}
\]
They satisfy
\[
 \boxed{\begin{gathered}
 C_i^2=dC_i,\qquad C_iC_j=C_jC_i,\\
 \operatorname{rank}C_i=d^{k-1},\qquad
 \operatorname{Tr}C_i=d^k .
 \end{gathered}}                                                  \tag{CW.45}
\]
Indeed \(g'=h'v_h+hv_h'\) gives
\(\gamma_i=v_ih_i'\) in the original \(i\)-th quotient, so
\[
 \mathcal R_iM_{\gamma_i}c_i
 =\ell_iM_{v_i}^{-1}M_{\gamma_i}c_i
 =\ell_iM_{h_i'}c_i=dI_{E_{\widehat i}} .
 \tag{CW.46}
\]
The last equality uses the literal degree \(d-1\) and
leading coefficient \(d\) of the original derivative \(h'\).
This proves the first formula in (CW.45).
It also proves that \(M_{\gamma_i}c_i\) is injective and
\(\mathcal R_i\) is onto.  The factorization (CW.44)
therefore has rank \(\dim E_{\widehat i}=d^{k-1}\).
Alternatively a specified right inverse for \(\mathcal R_i\)
is \(a\mapsto v_i s_i^{d-1}c_i(a)\), using (CW.43).
The two rectangular factors in (CW.44) have traces
\(\operatorname{Tr}_E(AB)=\operatorname{Tr}_{E_{\widehat i}}(BA)\);
apply (CW.46) to obtain \(d\,d^{k-1}=d^k\).
Operators belonging to distinct variables are tensor
products of their respective one-variable maps with
identity on the other factors.  Their compositions
therefore commute, proving the remaining identity.

These operators give precisely the correction of the
original full-unit section:
\[
 \boxed{\mathsf J_U=\frac1k\sum_{i=1}^k C_i.}                      \tag{CW.47}
\]
For proof, retain the complete thickened unit \(\widehat U\),
its residue \(U=\prod_i v_i\), and its full first derivative
\(\beta_h=U^{-1}\delta\widehat U\).
The original source-selected operator is still
\[
 \begin{gathered}
 \mathsf D_U=M_{\beta_h}+M_U\mathsf D_0M_U^{-1},
 \qquad [Z,\mathsf D_U]=-I_E+\mathsf J_U,\\
 \mathsf J_U=M_U\left(\frac1k\sum_i M_{h_i'}c_i\ell_i\right)M_U^{-1}.
 \end{gathered}                                                    \tag{CW.48}
\]
Write \(U=v_iU_{\widehat i}\), with
\(U_{\widehat i}=\prod_{j\ne i}v_j\).
The maps \(c_i,\ell_i\) are \(E_{\widehat i}\)-linear, so
the operator \(M_{U_{\widehat i}}\) commutes through
their indicated source and target actions, and its inverse
then cancels with exactly that same full other-variable unit.
Thus each summand in (CW.48) is
\[
 M_U M_{h_i'}c_i\ell_iM_U^{-1}
 =M_{v_i h_i'}c_i\ell_iM_{v_i}^{-1}
 =M_{\gamma_i}c_i\mathcal R_i=C_i .
 \tag{CW.49}
\]
This proves (CW.47).
Every \(v_i\) retains its original value, and
\(M_{\beta_h}\) remains in \(\mathsf D_U\).
It commutes with the original multiplication operator
\(Z=M_{\sum_i s_i-k/2}\), which is why it contributes
zero to that specified commutator.

For completeness, retaining all \(k\) residue variables gives
\[
 \begin{gathered}
 \mathcal R_{\mathrm{all}}:E\longrightarrow\mathbb C,\\
 \mathcal R_{\mathrm{all}}(u)=
 \sum_{\rho_1,\ldots,\rho_k\in\mathcal Z}
 \operatorname{Res}_{s_k=\rho_k}\cdots
 \operatorname{Res}_{s_1=\rho_1}
 \frac{\widetilde u(\mathbf s)}{\prod_i g(s_i)}\,
 ds_1\cdots ds_k .
 \end{gathered}                                                    \tag{CW.50}
\]
Here the formula means the ordered iterated coefficient
residues, with each original variable positively oriented.
Each variable operates on a different tensor factor, so
swapping their evaluation order gives the identical
scalar coefficient and introduces no sign.
Formula (CW.43) in each factor proves
\[
 \mathcal R_{\mathrm{all}}=\ell_h^{\otimes k}M_U^{-1},
 \qquad
 \boxed{C_1\cdots C_k(u)
 =\left(\prod_i\gamma_i\right)\mathcal R_{\mathrm{all}}(u).}
 \tag{CW.51}
\]
The map \(\ell_h^{\otimes k}:E_h^{\otimes k}\to\mathbb C\)
is the tensor product of the original one-variable
highest-coefficient functionals.
Tensoring the one-variable factorization (CW.44) proves
the second equality directly, so it keeps all repeated-root
and mixed nilpotent data before the final scalar
functional is evaluated.
The column and functional are both nonzero:
their contraction is
\[
 \begin{aligned}
 \mathcal R_{\mathrm{all}}\left(\prod_i\gamma_i\right)
 &=\prod_{i=1}^k
 \left(\sum_{\rho\in\mathcal Z}
 \operatorname{Res}_{s_i=\rho}\frac{g'(s_i)}{g(s_i)}\,ds_i\right)\\
 &=\prod_{i=1}^k\left(\sum_\rho m_\rho\right)=d^k .
 \end{aligned}                                                    \tag{CW.52}
\]
This is the rank-one full-product correction, with its
exact nonzero eigenvalue and trace \(d^k\).
Its square is \(d^k\) times itself by (CW.51)--(CW.52).
The residue of \(g'/g\) is \(m_\rho\) because
\(g(s)=(s-\rho)^{m_\rho}u_\rho(s)\) with
\(u_\rho(\rho)\ne0\); hence
\(g'/g=m_\rho/(s-\rho)+u_\rho'/u_\rho\).
This gives the complete multiplicity proof used in (CW.52).

At \(d=1\), (CW.46) gives \(C_i=I_E\) on the
one-dimensional \(E\); consequently \(\mathsf J_U=I_E\),
and (CW.51) is the same identity.
At \(k=1\), every formula reduces exactly to (CW.31)--(CW.33),
including the original residue functional
\(\mathscr R_{\mathcal Z}(1,u)\), rank one and trace \(d\).
For \(h=1\), the original arithmetic quotient is zero,
as already stated above; the positive-degree residue
coefficient formulas have the declared domain \(d\ge1\).
All repeated fibres, complete arithmetic units, and their
original source and target maps have been retained.

```
