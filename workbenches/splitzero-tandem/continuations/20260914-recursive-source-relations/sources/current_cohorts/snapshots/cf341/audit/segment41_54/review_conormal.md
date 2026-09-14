# Independent mathematical review of C1–C24

This review concerns `part53_54_and_conormal_proof.md`, including the subsequently added C17a–C17b and C22–C24. The reviewer read the full proof and the complete visible A1912 and A1959 passages in `output/tau_f1_transcript_audit_2026-09-13/sources/audit_segment_U0041_U0054.md`, lines 6341–7043 and 7056–7801, together with the signed-projector passage at lines 6042–6098. A separate narrow sign check agreed with the findings below. No original proof or global artifact was edited by this reviewer. Finite computational tests are being performed separately by the parent task.

The rank formulas C1–C9, C11–C14, and C18–C19 are correct. The intrinsic symmetric trace formulas C15–C17, the radical dimension C20, and the inertia C21 are correct with the stated reflection stability and the ordinary ordered residue convention. The new sum-fibre formulas C22–C24 are also correct. The original version had a missing hypothesis, an overstrong description of source representatives, an unsupported sign-cancellation statement, and an unqualified image in C17a. All four have been corrected by the parent during review, and the revised passages have been read and accepted. No unresolved numerical, multiplicity, rank, inertia, or source-map error remains in these formulas. Details and proofs follow.

## 1. Hypotheses and involution

For C1–C9 and C11–C14, take an integer k at least one and a nonempty finite packet of distinct centres with full positive integer multiplicities. The empty packet can be treated separately, but need not be introduced for the quartet calculation.

For the sesquilinear expressions and their Hermitian inertia, require

\[
\iota\rho=1-\overline\rho,\qquad
\iota Z=Z,\qquad m_{\iota\rho}=m_\rho.
\]

Then the polynomial involution

\[
f^\dagger(s)=\overline{f(1-\overline s)}
\]

satisfies \(h^\dagger=(-1)^d h\), so preserves the ideal \((h)\) and descends to \(E_h\). Its componentwise extension preserves the tensor ideal and commutes with permutations. Consequently it descends to \(B_k\). Without this hypothesis, an expression involving the value of a quotient class at \(\iota\rho\) need not be well defined. A1959 explicitly supplies reflection stability in its initial setup, and the hypothetical full quartet satisfies it. The revised proof now states this hypothesis and the descended involution.

## 2. First conormal image, kernel, and invariant domain

At a centre \(\rho\), the literal derivative is

\[
h'(\rho+z)=m_\rho z^{m_\rho-1}h_\rho(\rho+z)
 +z^{m_\rho}h'_\rho(\rho+z).
\]

The second term vanishes in the original quotient \(\mathbb C[z]/(z^{m_\rho})\). Every positive Taylor power in the first factor also vanishes after multiplication by \(z^{m_\rho-1}\). The coefficient that remains is exactly \(m_\rho h_\rho(\rho)\ne0\). The local image is therefore one dimensional, including when \(m_\rho=1\). This proves C1 without discarding any jet before differentiation.

The domain of the conormal calculation is \(I/I^2\cong E^k\), not \(E\) and not the entire thickening \(\mathcal P/I^2\). Its ordered dimension is \(kd^k\). The image of the row \(k^{-1}(h'(s_1),\ldots,h'(s_k))\) is the ideal \(\mathcal J\), and its cokernel is the literal tensor quotient in C3. Thus C4 has the correct domain dimension. The same argument on each unchanged local tuple gives C5. Multiplication by the actual unit U is invertible on E and preserves the ideal \(\mathcal J\), so it preserves this image and this kernel.

The invariant domain is

\[
(E^k)^{S_k}\cong
E_h\otimes(E_h^{\otimes(k-1)})^{S_{k-1}}.
\]

Explicitly, choose the kth coefficient. It is fixed by its stabilizer \(S_{k-1}\); set every other coefficient by any permutation carrying k to that index. Stabilizer invariance makes this assignment independent of the chosen permutation. This proves the dimension in C12 and gives the complete invariant kernel dimension

\[
d\binom{d+k-2}{k-1}
-\binom{d+k-1}{k}
+\binom{d-r+k-1}{k}.
\]

One must not obtain this kernel by subtracting C11 from \(k\dim B_k\): that would use the wrong domain. The proof does not make this mistake.

The conormal permutation action also has an explicit lift to the signed original cochain action. For polynomial lifts \(P_i\), use the degree \(k-1\) primitive

\[
\mathcal K(P_1,\ldots,P_k)=
\sum_{i=1}^k(-1)^{i-1}P_i(D_1,\ldots,D_k)
\bigl(F_h^{\otimes(i-1)}\otimes\phi_*\otimes
F_h^{\otimes(k-i)}\bigr).
\]

The tensor differential on the ith source leg contributes the same \((-1)^{i-1}\), so its boundary is the positive sum of the original relation terms. Under a permutation \(\pi\), the Koszul sign on a tensor with its degree-zero factor at i is

\[
\operatorname{sgn}(\pi)(-1)^{i+\pi(i)}.
\]

The extra sign in the signed projector changes the coefficient \((-1)^{i-1}\) to \((-1)^{\pi(i)-1}\). Therefore the signed primitive action is precisely simultaneous variable/index permutation on the conormal coefficients. Choosing the unique lifts of degree less than d in each variable makes this coefficient lift equivariant. This supplies the direct cochain morphism underlying the invariant-domain calculation; no dimension or sign correction is needed.

## 3. C6 retains the entire arithmetic unit

The correct source object in C6 is the entire function

\[
U(\mathbf s)=\prod_i v_h(s_i),\qquad v_h=g/h,
\]

before taking jets. Although the notation U is also used for its class in E, no derivative of a quotient class is being assumed. For every product-rule term, the unique derivative \(\partial_{s_i}\) either hits \(h(s_i)\) or does not. If it does not, no other derivative can remove that factor, because \(h(s_i)\) depends on no other variable. That term belongs to I. This covers derivatives landing on P, on any Taylor coefficient of U, or on both across different variables. The sole surviving term is

\[
U P\prod_i h'(s_i).
\]

The unreduced identity \(g'=v_hh'+v_h'h\) then gives C6 after reduction. This is valid with the full entire U, and the proof does not need or assume that its higher jets vanish.

There is also a precise lift-independence check. A derivative of total order k sends \(I^{k+1}\) into I: every differentiation lowers the number of retained relation factors by at most one. Replacing a lift of U or P by an element of I changes the expression multiplied by \(\prod_i h(s_i)\) by an element of \(I^{k+1}\). Hence the resulting jet is independent of these lifts. If desired, the notation can explicitly distinguish the entire U from its class in E; the displayed equality itself needs no change.

The operator here corresponds to \(\prod_i\log x_i\). It is not the first common derivative \(\mathscr L_k=k^{-1}\sum_i\log x_i\) estimated by the scalar Fisher identity. The proof's final limitation correctly does not infer a bound for this mixed derivative from that scalar estimate.

## 4. Ordered residue, symmetric trace, and the genuine sign correction

Fix the ordinary ordered residue form explicitly:

\[
\mathscr R_k^{\rm ord}(f,v)=
\sum_{\boldsymbol\rho\in Z^k}
\operatorname{Res}_{s_1=\rho_1}\cdots
\operatorname{Res}_{s_k=\rho_k}
\frac{f^\dagger(\mathbf s)v(\mathbf s)}{
\prod_i g(s_i)}\,ds_1\cdots ds_k.
\]

Use this fixed order and the literal multiplier \(\mathsf J_k=\prod_i g'(s_i)\). Repeated one-variable residue evaluation gives C10 with its full coefficient \(\prod_i m_{\rho_i}\). Multiplication by an element on the full local ordered algebra has trace equal to its constant value times \(\prod_i m_{\rho_i}\), proving the trace equality directly.

The original paragraph following C10 asserted that a Koszul evaluation factor

\[
\varepsilon_k=(-1)^{k(k-1)/2}
\]

automatically cancels against a second factor supplied by the contraction. This is not established by the cited source and is not true of the literal degree-zero multiplication \(M_{\mathsf J_k}\). If another explicitly defined pairing is \(\mathscr R_k^{\rm gr}=\varepsilon_k\mathscr R_k^{\rm ord}\), the precise comparison is

\[
\operatorname{Tr}_E M_{f^\dagger u}
=\varepsilon_k\mathscr R_k^{\rm gr}(f,\mathsf J_k u),
\qquad
\mathcal T_k^{\rm sym}(f,u)
=\varepsilon_k\mathscr R_k^{\rm gr}(f,\mathsf J_k B u).
\]

For k=2 and f=u=1, the ordered value is \(d^2\), while this graded value is \(-d^2\), so the second sign cannot be omitted. The revised proof now defines the ordered residue convention and removes the asserted automatic cancellation. The cohomological supertrace factor \((-1)^k\) is a separate map already identified in A1912. The signed projector has its own rigorously proved cancellation of two permutation signs; that does not prove this different residue cancellation. The final revised convention is correct.

## 5. Symmetric local dimensions and the central coefficient B

For an occupation n, restriction to one ordered component identifies the invariant occupation factor with

\[
\bigotimes_{\rho\in Z}
\left((\mathbb C[z]/z^{m_\rho})^{\otimes n_\rho}
\right)^{S_{n_\rho}}.
\]

An invariant tensor in each factor is determined by its monomial-orbit coefficients. Its dimension is the binomial factor in C14. Its ideal of zero constant terms is nilpotent: in a chosen ordered component every monomial of total degree greater than \(\sum_\rho n_\rho(m_\rho-1)\) vanishes. The invariant intersection therefore has a vanishing power as well. A nonzero constant gives an inverse by a finite geometric series. This proves locality, identifies the residue field, and proves the trace formula C15.

The Reynolds projector is the actual top-degree image of the signed cochain projector. For f,u in \(B_k\), multiplication by \(f^\dagger u\) commutes with it. Therefore the ordered vector space decomposes into its image and kernel, and C16 follows with no orbit scalar.

The two literal trace weights are

\[
D_n=\prod_\rho\binom{m_\rho+n_\rho-1}{n_\rho},
\qquad
O_n=\frac{k!}{\prod_\rho n_\rho!}\prod_\rho m_\rho^{n_\rho}.
\]

Thus \(B=\sum_n(D_n/O_n)e_n\) is an invertible central element of \(B_k\); its inverse is obtained by reciprocating those same coefficients. Reflection stability also gives \(D_{\iota n}=D_n\), \(O_{\iota n}=O_n\), and \(B^\dagger=B\). Comparing the finite sums proves C17. No replacement of D by O, or omission of an orbit factor, is permissible; the proof retains both correctly.

## 6. C17a–C17b and the exact meaning of a source representative

On an ordered component, multiplication by \(\mathsf J_k\) is its nonzero original socle coefficient times the constant-value map. It kills precisely the maximal ideal. On \(B_k\), its kernel is precisely the direct product of the zero-constant ideals, namely the trace radical. The correct induced isomorphism is

\[
B_k/\operatorname{rad}\mathcal T_k^{\rm sym}
\xrightarrow{\sim}
\operatorname{im}\bigl(M_{\mathsf J_k}|_{B_k}\bigr),
\qquad [u]\longmapsto\mathsf J_kBu.
\]

The restriction on the codomain is necessary. The previously defined ordered image has dimension \(r^k\), whereas this invariant image has dimension \(\binom{r+k-1}{k}\). Writing only \(\operatorname{im}M_{\mathsf J_k}\) without specifying its restricted domain creates a dimension/type mismatch. Equivalently the codomain is \((\operatorname{im}(M_{\mathsf J_k}:E\to E))^{S_k}\). The revised C17a now contains the restriction explicitly, and its proof identifies the dimension of that invariant image. This issue is resolved.

C17b is correct. Choose the unique polynomial P of degree less than d in every original variable representing Bu. Permutation invariance follows from uniqueness. The original source

\[
F_{u,k}=\left(\prod_i\log x_i\right)
P(D_1,\ldots,D_k)(\Theta\phi_*)^{\otimes k}
\]

has Mellin transform equal to the mixed derivative of \(UP\prod_i h(s_i)\), so its full jets are exactly \(\mathsf J_kBu\). The undifferentiated source is a theta tensor boundary using its first degree-zero leg and the remaining theta legs, with positive tensor-differential sign; averaging its primitive by the actual signed chain idempotent gives a primitive in the selected chain image. This is a source-level construction rather than a declaration about an abstract matrix.

For the common multiplicity m greater than one, the Jacobian image is contained in the nilpotent ideal of \(B_k\), hence in the radical of its intrinsic trace form. Therefore \(w=\mathsf J_kBu\) is not itself a negative vector for that trace form, even when u is. The precise nonzero statement is

\[
\mathcal T_k^{\rm sym}(u,u)
=\mathscr R_k^{\rm ord}(u,w).
\]

For \(u=e_n-e_{\iota n}\) on a nonfixed reflection orbit this common value is \(-2D_n\). The parent has corrected the prose after C21 to state this map explicitly. It now preserves both the negative nonradical class and its actual mixed-derivative observation without identifying their different roles.

## 7. Quartet inertia and limits

For four distinct centres with the common full multiplicity m, \(\iota\) exchanges positions 1 and 2 and exchanges positions 3 and 4. There are \(b_k=\binom{k+3}{3}\) occupation idempotents. A fixed occupation satisfies \(n_1=n_2\) and \(n_3=n_4\); it exists only for even k, with exactly \(k/2+1\) choices. Each fixed idempotent contributes the positive coefficient \(D_n\); each two-element orbit contributes the literal matrix

\[
\begin{pmatrix}0&D_n\\D_n&0\end{pmatrix}.
\]

Its unscaled sum and difference have values \(2D_n\) and \(-2D_n\), respectively. The remaining full-jet directions are exactly the nilpotent radical of dimension \(\binom{4m+k-1}{k}-b_k\). This proves C20–C21, including m=1. For odd k the positive and negative counts agree; multiplying by the separate supertrace sign therefore leaves the count of each unchanged in this particular quartet calculation.

No part of this rank or inertia calculation assumes RH, purity, an off-line zero, a lisse comparison, or a bound on the full canonical interpolation operator. The hypothetical quartet is the stated input for the counterfactual calculation. The source identities attach its derivative observations to the original theta relations. They do not supply the missing control estimate. The proof accurately states that limitation.

## 8. Further check of C22–C24: negative directions inside exact sum fibres

The literal sum of the quartet coordinates on occupation n is

\[
\lambda_n=\frac{k}{2}
+\delta(n_1-n_2+n_3-n_4)
+i\gamma(n_1+n_2-n_3-n_4),
\]

as in C22. The local sum operator is \(\lambda_n+M_{\sum_i z_i}\); its nilpotent part has power zero no later than \(k(m-1)+1\). Passing to the invariant occupation factor preserves this action. No statement that its idempotent is an eigenvector is needed.

For k=2l, the balanced summand consists of occupations

\[
n=(a,b,l-a,l-b),\qquad 0\le a,b\le l.
\]

Their eigenvalues have real part l. This is a direct sum over potentially different imaginary parts, as the proof explicitly states. Reflection exchanges a and b, giving \((l+1)^2\) occupations and exactly l+1 fixed occupations. Its negative and positive counts are therefore respectively \(l(l+1)/2\) and \((l+1)(l+2)/2\), verifying C23 with the full local weights.

There is a more refined exact-fibre verification. At

\[
\lambda=l+2i\gamma q,\qquad -l\le q\le l,
\]

the occupations have \(a+b=l+q\). Their number is

\[
N_q=l+1-|q|.
\]

There is one reflection-fixed occupation exactly when l+q is even, and none otherwise. Consequently this individual scalar-sum fibre has

\[
n_-=\left\lfloor\frac{N_q}{2}\right\rfloor,
\qquad
n_+=\left\lceil\frac{N_q}{2}\right\rceil,
\qquad
n_0=\sum_{n:\lambda_n=\lambda}D_n-N_q.
\]

This follows from the same literal Gram blocks on its full occupation factors, so the negative directions persist within exact sum fibres and not just within their union. For l=1 and q=0, the two occupations are \((1,0,0,1)\) and \((0,1,1,0)\), both with sum 1 and weight \(m^2\). Their difference has value \(-2m^2\), exactly C24. The original A1912 warning about retaining separate occupation factors when sums coincide is respected.
