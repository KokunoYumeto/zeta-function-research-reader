# Deligne's weight amplification and the actual prime-primary operators

Private independent mathematical derivation, 24 September 2026.

This note reconstructs Deligne's arguments in *La conjecture de Weil. II*, §§1.5 and 1.8, and calculates the tensor Euler products of the programme's actual prime-primary operators. The human source is Pierre Deligne, *Publications mathématiques de l'IHÉS* **52** (1980), 137–252. Grothendieck's trace formula, local monodromy theorem, and geometric-monodromy theorem retain their human attribution. They are cited inputs; this note does not claim to reprove those theories.

## 1. Source identity and what was read

The main consulted file is the local French page-record transcription:

S20_FR_record_export.tex

SHA256: d6836ae15d98f2b27eb98c9bd039a7d921679becd9fa47ff4717410289dbd351.

It is a mechanically escaped page-record transcription, **not an original author TeX source**. The historical English math-mode transcription was consulted for comparison:

032_Deligne_The_Weil_Conjecture_II_EN_source_checked_corrected.tex

SHA256: 316cbc52349cd6bc2dedbd0a493a530696d367ca0e292fc64ee3c3973327567e.

Actual reading in this derivation: French §§1.2.1–1.2.14, §§1.3.1–1.3.13, §§1.4.1–1.4.7, all of §1.5, §§1.6.1–1.6.4 and 1.6.14, §§1.7.1–1.7.6, and all of §1.8, including its final Hodge-theoretic problem. Sections not in that list have not been read completely here. English §1.5 and the displayed formulas (1.6.14.3–5) and §1.8.4 were compared. Reading all of these sections is not a claim to have read all 116 printed pages or to have reverified their external dependencies.

There are mathematical defects in the supplied copies. Most consequential here, both copies print a positive twist in (1.6.14.3). That sign is incompatible with their own convention that a Tate twist \((1)\) has weight \(-2\). Section 5 below derives the required negative twist from the equivariant nilpotent map. This derivation does not silently attribute a transcription defect to Deligne.

Other defects encountered, not used as mathematical premises: French (1.3.10)(iv) prints a finite subgroup of \(\mathbb Z\), although its proof produces a subgroup of finite index \(n\mathbb Z\), \(n\ne0\). French (1.7.5) prints a product indexed by \(j<i\) for the increasing weight filtration; the filtration prescribed by the proposition is the direct sum of generalized eigenspaces of weights \(j\le i\).

## 2. Fixed conventions and the geometric input

Let \(X_0\) be a smooth geometrically irreducible curve over \(\mathbb F_q\), let \(X=X_0\otimes_{\mathbb F_q}\overline{\mathbb F}_q\), and let \(\mathcal F_0\) be a lisse Weil sheaf with coefficients in \(\overline{\mathbb Q}_\ell\), \(\ell\nmid q\). Fix the field isomorphism \(\iota:\overline{\mathbb Q}_\ell\to\mathbb C\) used by Deligne. For a closed point \(x\), write
\[
d_x=[\kappa(x):\mathbb F_q],\qquad Q_x=N(x)=q^{d_x},
\qquad
w_{Q_x}(\alpha)=\frac{2\log|\iota\alpha|}{\log Q_x}.
\tag{DW2.1}
\]
No twist to weight zero is performed in this note. Every weight \(\beta\) remains explicit.

For a nonzero irreducible constituent \(\mathcal G_0\) of rank \(d\), its determinantal weight is the weight of \(\det\mathcal G_0\), divided by \(d\). Deligne's §§1.3.4–1.3.13 supply the following facts:

* a rank-one lisse Weil sheaf has a single pointwise \(\iota\)-weight;
* tensor products add determinantal weights;
* the determinantal weights of \(\bigwedge^a\mathcal F_0\) are the sums \(\sum_\gamma a(\gamma)\gamma\), with \(\sum_\gamma a(\gamma)=a\) and \(0\le a(\gamma)\le n(\gamma)\), where \(n(\gamma)\) is the total rank of constituents of weight \(\gamma\).

The reason for the tensor assertion is the central element in the geometric-monodromy construction of §§1.3.7–1.3.12. After passing to the semisimplification, an element \(g\) central in that algebraic group has nonzero degree \(d_g\), and on a constituent of determinantal weight \(\beta\) it acts with eigenvalues of absolute value \(q^{d_g\beta/2}\). Its eigenvalues multiply on tensors. This is geometric-monodromy information, not a consequence of the existence or uniqueness of an Euler product.

Grothendieck's trace formula, §1.4.5, is
\[
\prod_{x\in|X_0|}
 \det(1-F_xT^{d_x},\mathcal F)^{-1}
=
\prod_i\det(1-FT,H_c^i(X,\mathcal F))^{(-1)^{i+1}}.
\tag{DW2.2}
\]
The application of \(\iota\) to the coefficients is understood in subsequent complex analytic formulas and can be inserted on every determinant. On an affine curve, \(H_c^0=0\), so the full right side is
\[
\frac{\det(1-FT,H_c^1(X,\mathcal F))}
     {\det(1-FT,H_c^2(X,\mathcal F))}.
\tag{DW2.3}
\]
The absent \(H_c^0\) factor is exactly \(\det(1-FT,0)=1\); the reason for its absence is the proved vanishing for a lisse sheaf on a nonproper smooth connected curve, not a cancellation convention.

Section 1.4.1 identifies
\[
H_c^2(X,\mathcal F)
=\mathcal F_{\bar\eta,\pi_1(X)}(-1).
\tag{DW2.4}
\]
The coinvariant quotient has determinantal weights among those of \(\mathcal F_0\). The Tate twist \((-1)\) multiplies geometric Frobenius by \(q\), and therefore adds exactly \(2\) to each weight. This is the source of the fixed error in the pole bound.

If all local eigenvalues have weight at most \(\beta\), the number of degree-\(n\) points is bounded by \(Cq^n\), and
\[
\sum_{n\ge1}Cq^n q^{n\beta/2}|T|^n
\tag{DW2.5}
\]
converges for \(|T|<q^{-\beta/2-1}\). The logarithmic Euler sum is bounded by the full repetition series
\[
R_{\mathcal F}\sum_{n\ge1}Cq^n
\sum_{r\ge1}\frac{(q^{n\beta/2}|T|^n)^r}{r},
\tag{DW2.6}
\]
where \(R_{\mathcal F}\) is the rank. On compact subdiscs of the displayed domain, the inner sum is bounded by a constant times its first power, uniformly in \(n\). Thus (DW2.5) proves absolute convergence of the logarithm and a holomorphic nonzero Euler product. The rank and \(C\) do not change the exponent.

## 3. The complete positivity and amplification in §1.5

Call a sheaf \(\iota\)-real when the characteristic polynomial of each \(F_x\), after applying \(\iota\), has real coefficients. Consequently every power trace \(\operatorname{tr}(F_x^r)\) is real.

Fix \(k\ge1\). For each local Frobenius \(A=F_x\),
\[
\operatorname{tr}\bigl((A^{\otimes2k})^r\bigr)
=\bigl(\operatorname{tr}(A^r)\bigr)^{2k}\ge0.
\tag{DW3.1}
\]
The reciprocal local determinant has the full formal expansion
\[
\det(1-A^{\otimes2k}U)^{-1}
=\exp\left(\sum_{r\ge1}
\frac{(\operatorname{tr}A^r)^{2k}}rU^r\right).
\tag{DW3.2}
\]
This identity follows by triangularizing \(A\), applying
\(-\log(1-z)=\sum_{r\ge1}z^r/r\) formally to every diagonal eigenvalue, and summing. Nilpotent off-diagonal entries do not change a determinant or trace; their presence is retained in the operator.

All coefficients in (DW3.2) are nonnegative. Explicitly, if \(c_0=1\) and \(c_n\) are its coefficients, differentiation gives
\[
n c_n=\sum_{r=1}^n(\operatorname{tr}A^r)^{2k}c_{n-r}.
\tag{DW3.3}
\]
Induction proves \(c_n\ge0\).

Let \(r_0\) be the largest determinantal weight of \(\mathcal F_0\). Tensor compatibility from §1.3.13 bounds all determinantal weights of \(\mathcal F_0^{\otimes2k}\) by \(2kr_0\). Equations (DW2.3–4) prove that the global rational function has no pole in
\[
|T|<R_k,\qquad R_k=q^{-kr_0-1}.
\tag{DW3.4}
\]
The numerator is a polynomial; its zeros cannot create poles. A pole in this disc is precluded by the denominator bound itself.

Here is the exact use of coefficient positivity, without the imprecise assertion that arbitrary complex poles cannot cancel. For a fixed closed point \(x\), factor the global formal series as \(P_x(T)B_x(T)\), with \(P_x\) its local reciprocal determinant and \(B_x\) the product of all other local factors. Both have nonnegative coefficients and constant coefficient \(1\). There are only finitely many closed points of bounded degree, so each formal coefficient is a finite expression. Coefficient by coefficient,
\[
0\le[T^n]P_x(T)\le[T^n](P_x(T)B_x(T)).
\tag{DW3.5}
\]
The global rational function is analytic on \(|T|<R_k\). Its Taylor coefficients therefore give an absolutely convergent series at every positive \(r<R_k\). The domination (DW3.5) proves the same for \(P_x\). Hence the local reciprocal determinant has no pole in that disc.

If \(\alpha\) is any eigenvalue of \(F_x\) on \(\mathcal F_0\), then \(\alpha^{2k}\) is an eigenvalue on its \(2k\)-fold tensor power. The polynomial factor
\[
1-\iota(\alpha)^{2k}T^{d_x}
\tag{DW3.6}
\]
has roots of absolute value \(|\iota\alpha|^{-2k/d_x}\). They are poles of the reciprocal local determinant: it has constant numerator \(1\), so local cancellation is impossible. Comparing with (DW3.4) gives
\[
|\iota\alpha|^{-2k/d_x}\ge q^{-kr_0-1},
\qquad
|\iota\alpha|\le Q_x^{\,r_0/2+1/(2k)}.
\tag{DW3.7}
\]
Equivalently,
\[
w_{Q_x}(\alpha)\le r_0+\frac1k.
\tag{DW3.8}
\]
The original \(\alpha\), point \(x\), and weight \(r_0\) are fixed as \(k\) ranges through the positive integers. Taking the infimum over \(k\) proves \(w_{Q_x}(\alpha)\le r_0\). The error is \(1/k\) in weight and \(1/(2k)\) in the exponent of the absolute value.

To obtain purity for every constituent, group the constituents by determinantal weight \(\gamma\), with total ranks \(n(\gamma)\). Their eigenvalues \(\alpha_i^\gamma\) satisfy the determinant equality
\[
\sum_{i=1}^{n(\gamma)}w_{Q_x}(\alpha_i^\gamma)=n(\gamma)\gamma.
\tag{DW3.9}
\]
Fix a nonempty group of weight \(\beta\) and put
\[
N_\beta=\sum_{\gamma>\beta}n(\gamma).
\tag{DW3.10}
\]
The exterior power \(\bigwedge^{N_\beta+1}\mathcal F_0\) is still \(\iota\)-real. Its eigenvalues are products over subsets of the original eigenvalue multiset; complex conjugation permutes that multiset and those subsets. Its largest determinantal weight is
\[
\beta+\sum_{\gamma>\beta}n(\gamma)\gamma.
\tag{DW3.11}
\]
For every \(i\), the eigenvalue
\[
\alpha_i^\beta\prod_{\gamma>\beta}\prod_{j=1}^{n(\gamma)}\alpha_j^\gamma
\tag{DW3.12}
\]
belongs to that exterior power. Applying the upper bound and subtracting the exact determinant equalities for \(\gamma>\beta\) gives
\[
w_{Q_x}(\alpha_i^\beta)\le\beta.
\tag{DW3.13}
\]
The sum of these \(n(\beta)\) inequalities is equality by (DW3.9). Every individual difference \(\beta-w_{Q_x}(\alpha_i^\beta)\) is nonnegative, and their sum is zero. Every difference is therefore zero. Thus every constituent is pointwise \(\iota\)-pure of its determinantal weight. This is the complete mechanism of §§1.5.1–1.5.3.

## 4. Boundary weights: every step of §1.8.1

Let \(j:U_0\hookrightarrow X_0\) be an open immersion with finite complement \(S_0\), and suppose \(\mathcal F_0\) is lisse and pointwise \(\iota\)-pure of weight \(\beta\) on \(U_0\). Removing a point from \(U_0\), rather than from the boundary point being examined, makes \(X_0\) affine without changing the local assertion.

The full trace formula is
\[
\begin{aligned}
&\prod_{x\in|U_0|}
\det(1-F_xT^{d_x},\mathcal F_0)^{-1}
\prod_{x\in|S_0|}
\det(1-F_xT^{d_x},j_*\mathcal F_0)^{-1}\\
&\hspace{15mm}
=\frac{\det(1-FT,H_c^1(X,j_*\mathcal F))}
{\det(1-FT,H_c^2(X,j_*\mathcal F))}.
\end{aligned}
\tag{DW4.1}
\]
The first product on the left is analytic and nonzero for
\[
|T|<q^{-(\beta+2)/2}.
\tag{DW4.2}
\]
Top cohomology depends only on the restriction to a dense smooth open, so its eigenvalues have weights \(\beta+2\). Thus the right side has no pole in (DW4.2). Dividing by the nonvanishing open product shows that the finite boundary product has no pole there. This boundary product is itself a reciprocal polynomial, so its individual determinant zeros cannot cancel one another.

For every eigenvalue \(\alpha\) at a boundary point \(x\), this proves
\[
|\iota\alpha|\le Q_x^{(\beta+2)/2},
\qquad
w_{Q_x}(\alpha)\le\beta+2.
\tag{DW4.3}
\]
At a geometric boundary point, the stalk of \(j_*\mathcal F_0\) is the inertia-invariant space \(V^I\). There is an injective, Frobenius-equivariant map
\[
(V^I)^{\otimes k}\longrightarrow(V^{\otimes k})^I.
\tag{DW4.4}
\]
It is the restriction of the tensor power of the vector-space inclusion \(V^I\hookrightarrow V\). Its image is invariant because each factor is invariant. It is injective because tensoring injections of vector spaces over a field preserves injectivity. This is the exact map behind
\[
(j_*\mathcal F_0)^{\otimes k}
\hookrightarrow j_*(\mathcal F_0^{\otimes k}).
\tag{DW4.5}
\]

The tensor sheaf on \(U_0\) has weight \(k\beta\); the boundary eigenvalue \(\alpha^k\) is carried by (DW4.4). Applying (DW4.3) to that tensor sheaf proves
\[
|\iota\alpha|^k\le Q_x^{(k\beta+2)/2},
\qquad
w_{Q_x}(\alpha)\le\beta+\frac2k.
\tag{DW4.6}
\]
Letting \(k\to\infty\) gives \(w_{Q_x}(\alpha)\le\beta\).

The error here is \(2/k\) in weight, or \(1/k\) in the absolute-value exponent. It is not the same numerical expression as (DW3.8), because §1.5 uses the even tensor power \(2k\) and its positivity argument.

Section 1.8.2 also compares zeros in (DW4.1). After the boundary bound is known, both local products are nonzero in (DW4.2); the right denominator does not vanish there. Hence the numerator does not vanish there. An eigenvalue \(\alpha\) on \(H_c^1(X,j_*\mathcal F)\) consequently satisfies \(w_q(\alpha)\le\beta+2\). This is the rough cohomological estimate, not yet the sharper weight \(\beta+1\) for cohomological degree one.

## 5. Local monodromy: §1.8.4 with every \(\beta\) retained

Fix a boundary point \(s\), set \(Q=N(s)\), and let \(V=\mathcal F_{\bar\eta}\) for the corresponding henselian trait. Grothendieck's quasi-unipotence theorem allows a finite cover on which inertia is unipotent, with
\[
\rho_I(\sigma)=\exp(t_\ell(\sigma)N),
\qquad
N:V(1)\longrightarrow V.
\tag{DW5.1}
\]
A finite ramification change multiplies the chosen logarithm \(N\) by a nonzero scalar, leaving its monodromy filtration unchanged. With compatible Frobenius lifts, a residue extension of degree \(f\) changes \(Q\) to \(Q^f\) and eigenvalues to their \(f\)-th powers; it leaves the numerical weight (DW2.1) unchanged. Changes of lift can multiply eigenvalues by roots of unity, which have complex absolute value one and therefore leave these weights unchanged. These exact changes justify the reduction.

Let \(F\) be geometric Frobenius. Equivariance of the map in (DW5.1), including the \(Q^{-1}\) action on the Tate line, is
\[
FN=Q^{-1}NF,\qquad FNF^{-1}=Q^{-1}N.
\tag{DW5.2}
\]
The monodromy filtration \(M\) is centered at zero and satisfies
\[
N M_i(1)\subset M_{i-2},
\qquad
N^j:\operatorname{Gr}_j^M V(j)
\xrightarrow{\;\sim\;}\operatorname{Gr}_{-j}^M V.
\tag{DW5.3}
\]
Write \(P_{-j}\) for the primitive kernel at index \(-j\), \(j\ge0\). It is a subquotient of \(\ker N=V^I\). The boundary estimate gives
\[
|\iota\alpha|\le Q^{\beta/2}
\quad\text{for each eigenvalue on }P_{-j}(V).
\tag{DW5.4}
\]

The primitive tensor formula contains a direct summand
\[
P_{-j}(V)\otimes P_{-j}(V)(-j)
\longrightarrow P_0(V\otimes V).
\tag{DW5.5}
\]
This is the \(j'=j''=j\), total primitive index zero, summand in (1.6.14.4). Its twist is essential. A direct Jordan-string check is available: take a length-\(j+1\) string \(Nv_r=v_{r-1}\), \(Nv_0=0\). The vector
\[
\Omega=\sum_{r=0}^j(-1)^r v_r\otimes v_{j-r}
\tag{DW5.6}
\]
has degree zero and is killed by \(N\otimes1+1\otimes N\). On the degree-zero basis \(b_r=v_r\otimes v_{j-r}\), the functional \(b_r\mapsto(-1)^r\) annihilates the image of \(N\) from degree two, since that image is spanned by \(b_{r-1}+b_r\). It evaluates \(\Omega\) to \(j+1\ne0\). Thus this primitive component is nonzero. The total \(j\) inverse steps up the two strings contribute the twist \((-j)\). The general primitive-multiplicity formula is Deligne's (1.6.14.4).

The tensor sheaf has weight \(2\beta\). If \(\alpha\) occurs on \(P_{-j}(V)\), then \(\alpha^2Q^j\) occurs in (DW5.5). Applying (DW5.4) to the tensor sheaf yields
\[
|\iota\alpha|^2Q^j\le Q^\beta,
\qquad
|\iota\alpha|\le Q^{(\beta-j)/2}.
\tag{DW5.7}
\]
The primitive dual formula is
\[
P_{-j}(V^\vee)\simeq P_{-j}(V)^\vee(j).
\tag{DW5.8}
\]
Its eigenvalue corresponding to \(\alpha\) is \(\alpha^{-1}Q^{-j}\). The dual sheaf has weight \(-\beta\), so (DW5.7) applied to it gives
\[
|\iota\alpha|^{-1}Q^{-j}\le Q^{(-\beta-j)/2},
\qquad
|\iota\alpha|\ge Q^{(\beta-j)/2}.
\tag{DW5.9}
\]
Together, the inequalities prove
\[
|\iota\alpha|=Q^{(\beta-j)/2}
\quad\text{on }P_{-j}(V).
\tag{DW5.10}
\]

Here is the sign check needed to recover all the graded pieces. A primitive string contributes to \(\operatorname{Gr}_i^M V\) when \(j\ge|i|\) and \(j\equiv i\pmod2\). Put \(r=(i+j)/2\). On this component,
\[
N^r:\operatorname{Gr}_i^M V(r)\longrightarrow P_{-j}(V)
\tag{DW5.11}
\]
is the equivariant isomorphism. Therefore its exact untwisted-domain form is
\[
\operatorname{Gr}_i^M V
\simeq
\bigoplus_{\substack{j\ge|i|\\j\equiv i\ (2)}}
P_{-j}(V)\left(-\frac{i+j}{2}\right).
\tag{DW5.12}
\]
The eigenvalue on the corresponding graded piece is \(\alpha Q^{(i+j)/2}\). Its absolute value, with every factor retained, is
\[
Q^{(\beta-j)/2}Q^{(i+j)/2}
=Q^{(\beta+i)/2}.
\tag{DW5.13}
\]
This proves the asserted weight \(\beta+i\) of \(\operatorname{Gr}_i^M V\). The positive sign printed in the consulted copies of (1.6.14.3) would instead give \(Q^{(\beta-i-2j)/2}\), contradicting (DW5.11) and the theorem. Formula (DW5.12) is independently derived, rather than silently copied.

## 6. What the remainder of §1.8 establishes

The propagation statements have precise content beyond the tensor estimate.

In (1.8.5), a lisse sheaf carries a finite filtration \(W\) by lisse subsheaves whose graded pieces are pointwise pure of weight \(a\). On each \(\operatorname{Gr}_a^W V\), (DW5.13), with its center shifted from zero to \(a\), gives the relative monodromy isomorphisms
\[
N^j:\operatorname{Gr}_{a+j}^M\operatorname{Gr}_a^W V(j)
\xrightarrow{\sim}
\operatorname{Gr}_{a-j}^M\operatorname{Gr}_a^W V.
\tag{DW6.1}
\]
The Frobenius weight filtration exists by (1.7.5); equation (DW5.2) lowers weights by two. Consequently that weight filtration satisfies both defining properties of the relative monodromy filtration. Uniqueness of the latter, (1.6.13), identifies the two. This uses a proved uniqueness theorem for a filtration with specified maps; it is not uniqueness of the scalar zeta function.

Statements (1.8.6–7) restrict to curves transverse to a smooth boundary divisor. The tame nearby local system \(\mathcal F_0[D_0]\) retains its \(\mathbb Z_\ell(1)\)-action. Formula (DW6.1) gives its relative monodromy filtration and the asserted weights. The construction of \(\mathcal F_0[D_0]\) and transverse restriction are inputs from §1.7.8; that construction has not been rederived in this note.

In (1.8.8), the stalk of \(j_*\mathcal F_0\) is obtained from \(\ker N\) by taking invariants under the finite residual inertia group. All primitive indices in \(\ker N\) are nonpositive. Therefore boundary weights are \(\beta+i\) with \(i\le0\). Taking a subspace of invariants cannot introduce new eigenvalues. The divisor version is the same calculation on the tame nearby local system.

Corollary (1.8.9) extends the upper bound and mixedness to \(j_*\) for arbitrary finite-type schemes. Its proof uses the following actual injective maps, each preserving the pointwise upper-weight conclusion:

1. For an extension \(0\to\mathcal F'_0\to\mathcal F_0\to\mathcal F''_0\to0\), left exactness gives \(0\to j_*\mathcal F'_0\to j_*\mathcal F_0\to j_*\mathcal F''_0\).
2. A supported sheaf embedded in \(i_*i^*\mathcal F_0\) reduces the assertion to its support closure.
3. For a finite surjective map \(\epsilon:X'_0\to X_0\), the pullback-detection map is \(j_*\mathcal F_0\hookrightarrow\epsilon_*j'_*\epsilon^*\mathcal F_0\).
4. Restriction to a dense open gives \(j_*\mathcal F_0\hookrightarrow(jk)_*k^*\mathcal F_0\).
5. With \(X_0\) normal, lisse \(\mathcal F_0\), boundary immersion \(i\), and a dense boundary open \(k\), there is an injection \(i^*j_*\mathcal F_0\hookrightarrow k_*k^*i^*j_*\mathcal F_0\). On a geometric stalk, it follows from the factorization of the injection to a generic stalk through the displayed target, using connectedness of the appropriate strict henselian open.

Induction on the dimension of the support and these reductions bring the boundary calculation to the smooth tame-divisor case (1.8.8). This is Deligne's reduction; the underlying reduction theory is not reproved here.

Corollary (1.8.10) starts with a lisse sheaf pure of weight \(\beta\) on a dense open. Both it and its dual inject into their \(j_*j^*\). The upper bound for the sheaf is \(\beta\), and for its dual is \(-\beta\). If \(\alpha\) occurs on the sheaf, the two inequalities are
\[
|\iota\alpha|\le Q^{\beta/2},
\qquad
|\iota\alpha|^{-1}\le Q^{-\beta/2}.
\tag{DW6.2}
\]
They give equality, so purity extends across the original lisse locus.

For (1.8.11), normality ensures that restriction of an irreducible lisse sheaf to a dense open remains irreducible. An \(\iota\)-mixed irreducible sheaf is pure on some such open; (1.8.10) extends its purity. A Jordan–Hölder filtration then gives successive lisse pure constituents.

For (1.8.12), on a connected normal scheme the finite collection of constituent weights is visible on every stalk, so purity at one stalk forces all constituents to have that weight. On a general connected scheme, pullback to the normalization shows that the locus pure of that fixed weight contains every irreducible component through each of its points. It is therefore open and closed, and connectedness propagates it globally. This is purity propagation after mixedness and the preceding theorems are known, not a rule allowing one ungraded support point to assert a weight.

Statement (1.8.13) permits the analogous purity and integral-weight formulations. Statements (1.8.14–15) compare the result with W. Schmid's asymptotic Hodge theory and formulate a problem about good variations of mixed Hodge structure. They are not an additional proof that arbitrary filtered local systems have the required relative monodromy filtration.

## 7. The exact primary-jet tensor action in the programme

Let \(\rho=\beta+i\gamma\) be an actual nontrivial zero of the original \(\zeta(s)\), of multiplicity \(m\), and suppose for the calculation that \(\beta\ne1/2\). The full distinct orbit is
\[
\mathcal O_\rho=\{\rho,\overline\rho,1-\rho,1-\overline\rho\}.
\tag{DW7.1}
\]
The original functional equation, with every factor retained, is
\[
\zeta(s)=2^s\pi^{s-1}\sin(\pi s/2)\Gamma(1-s)\zeta(1-s).
\tag{DW7.1a}
\]
The multiplier is holomorphic and nonzero in \(0<\Re s<1\). Complex conjugation commutes with \(\zeta\), initially by its Dirichlet series and then by unique meromorphic continuation. Therefore these two exact maps give the same multiplicity \(m\) at all four points. The original zeta has no real zero in \(0<s<1\): the convergent alternating Dirichlet series there is strictly positive, while \(1-2^{1-s}<0\), and their quotient is \(\zeta(s)\). Positivity follows by pairing consecutive terms \((2a-1)^{-s}-(2a)^{-s}>0\) and retaining the first positive pair; convergence is the alternating-series criterion. Thus \(\gamma\ne0\), and all four points in (DW7.1) are distinct. Formula (DW7.1a) is used only on its stated strip for multiplicity preservation; it does not discard its exceptional points globally.

The programme's primary space and operators are
\[
V_\rho=\bigoplus_{\omega\in\mathcal O_\rho}\mathbb C[\epsilon_\omega]/(\epsilon_\omega^m),
\qquad
W_p|_{V_\omega}
=p^\omega\sum_{j=0}^{m-1}\frac{(\log p)^j}{j!}N_\omega^j,
\quad
N_\omega v=\epsilon_\omega v.
\tag{DW7.2}
\]
The letter \(\epsilon_\omega\) is a spectral jet coordinate, not the source presence \(\tau\). The vector-space zero in these coefficient modules is not an identification of source \(Z_1\) with \(Z_0\).

The full \(d\)-fold tensor space of one block is
\[
V_\omega^{\otimes d}
\simeq
\mathbb C[\epsilon_1,\ldots,\epsilon_d]/
(\epsilon_1^m,\ldots,\epsilon_d^m),
\tag{DW7.3}
\]
and the tensor operator is exactly
\[
W_p^{\otimes d}
=p^{d\omega}\exp\left((\log p)\sum_{a=1}^dN_a\right).
\tag{DW7.4}
\]
All terms of the exponential of degree \(>d(m-1)\) vanish. When \(m>1\), the power of degree \(d(m-1)\) is nonzero: its coefficient of \(\epsilon_1^{m-1}\cdots\epsilon_d^{m-1}\) is
\[
\frac{(d(m-1))!}{((m-1)!)^d}\ne0.
\tag{DW7.5}
\]
Thus the nilpotency index of \(\sum N_a\) is exactly \(d(m-1)+1\). None of this tensor structure is discarded when taking determinants below.

For \(r\ge1\),
\[
\operatorname{tr}(W_p^r|V_\rho)
=m\sum_{\omega\in\mathcal O_\rho}p^{r\omega}
=2m\bigl(p^{r\beta}+p^{r(1-\beta)}\bigr)
\cos(r\gamma\log p).
\tag{DW7.6}
\]
This is real. Consequently the reciprocal determinant for the \(2k\)-fold tensor representation has nonnegative coefficients, by precisely (DW3.1–3):
\[
\det(1-UW_p^{\otimes2k})^{-1}
=\exp\left(
\sum_{r\ge1}\frac{
\left[2m(p^{r\beta}+p^{r(1-\beta)})
\cos(r\gamma\log p)\right]^{2k}}rU^r
\right).
\tag{DW7.7}
\]
This proves an exact transfer of Deligne's local coefficient-positivity step. It does not yet import his independent geometric bound on the global poles.

## 8. The complete global tensor Euler product is computable

Put \(B=\max(\beta,1-\beta)\), and define the actual tensor Euler product
\[
\mathcal L_k(s)=
\prod_p\det(1-p^{-s}W_p^{\otimes2k}|V_\rho^{\otimes2k})^{-1}.
\tag{DW8.1}
\]
It converges absolutely for \(\Re s>1+2kB\). Each of the finitely many eigenvalues in a local tensor determinant has absolute value at most \(p^{2kB}\). For \(\delta=\Re s-2kB>1\), the full logarithmic sum is bounded by
\[
(4m)^{2k}\sum_p\sum_{r\ge1}\frac{p^{-r\delta}}r
\le
\frac{(4m)^{2k}}{1-2^{-\delta}}\sum_{n\ge2}n^{-\delta}<\infty.
\tag{DW8.1a}
\]
The tensor rank \((4m)^{2k}\) is finite for every \(k\).

For an ordered tuple \(\boldsymbol\omega=(\omega_1,\ldots,\omega_{2k})\in\mathcal O_\rho^{2k}\), define
\[
\sigma(\boldsymbol\omega)=\sum_{a=1}^{2k}\omega_a.
\tag{DW8.2}
\]
The associated tensor block has dimension \(m^{2k}\). In the monomial basis of (DW7.3), ordered by total degree, its exponential nilpotent factor is triangular with all diagonal entries \(1\). Every diagonal eigenvalue is therefore \(p^{\sigma(\boldsymbol\omega)}\), with all \(m^{2k}\) occurrences retained. Thus
\[
\det(1-p^{-s}W_p^{\otimes2k})
=
\prod_{\boldsymbol\omega\in\mathcal O_\rho^{2k}}
(1-p^{\sigma(\boldsymbol\omega)-s})^{m^{2k}}.
\tag{DW8.3}
\]
The finite product over tuples can be interchanged with the absolutely convergent prime product, giving the exact original-zeta identity
\[
\boxed{\displaystyle
\mathcal L_k(s)=
\prod_{\boldsymbol\omega\in\mathcal O_\rho^{2k}}
\zeta\bigl(s-\sigma(\boldsymbol\omega)\bigr)^{m^{2k}}.}
\tag{DW8.4}
\]
Both sides therefore have the meromorphic continuation specified by the right side. This uses the original \(\zeta\), with its original pole at \(1\); no completion, Gamma factor, or endpoint factor has been inserted or removed.

The real point
\[
s_k=1+2kB
\tag{DW8.5}
\]
is a genuine pole of order
\[
h_k=m^{2k}\binom{2k}{k}.
\tag{DW8.6}
\]
Here is a proof including exclusion of every possible cancellation. Let \(\omega_+=B+i\gamma'\), \(\omega_-=B-i\gamma'\) be the two points in the orbit with maximal real part, where \(\gamma'\ne0\). A tuple has real part \(2kB\) exactly when all its entries are \(\omega_+\) or \(\omega_-\). Its imaginary part is zero exactly when there are \(k\) of each. There are \(\binom{2k}{k}\) such ordered tuples. They contribute the factor
\[
\zeta(s-2kB)^{\,m^{2k}\binom{2k}{k}}.
\tag{DW8.7}
\]
Every other tuple has either \(\Re(s_k-\sigma)>1\), or \(\Re(s_k-\sigma)=1\) and \(\Im(s_k-\sigma)\ne0\). The original \(\zeta\) is holomorphic and nonzero at all these points. For completeness, the classical Hadamard–de la Vallée-Poussin nonvanishing argument is reproduced here, rather than claimed as new. It uses the Euler product and the known single pole at \(1\):
\[
3+4\cos\theta+\cos2\theta=2(1+\cos\theta)^2\ge0
\tag{DW8.8}
\]
implies, for \(u>1\) and real \(v\),
\[
\zeta(u)^3|\zeta(u+iv)|^4|\zeta(u+2iv)|\ge1.
\tag{DW8.9}
\]
Indeed taking logarithms expands the left logarithm as
\[
\sum_p\sum_{r\ge1}\frac{p^{-ru}}r
\left[3+4\cos(rv\log p)+\cos(2rv\log p)\right]\ge0.
\tag{DW8.10}
\]
If \(\zeta(1+iv)\) had a zero of order \(a\ge1\) with \(v\ne0\), its factor in (DW8.9) would be \(O((u-1)^{4a})\), while \(\zeta(u)^3=O((u-1)^{-3})\) and the last factor stays bounded as \(u\downarrow1\). The left side would tend to zero, contradicting (DW8.9). In \(\Re s>1\), the Euler product itself proves nonvanishing. Thus every factor other than (DW8.7) is finite and nonzero at \(s_k\), proving the pole and its exact order.

This proves more than an abstract list of potential properties: the entire tensor Euler function, its domain, its continuation, a forced global pole, and that pole's multiplicity are constructed from the actual primary orbit. It does not create or assert the existence of an off-critical zero. It calculates exactly the consequence for an actual zero if its real part differs from \(1/2\).

There is also an exact global coefficient consequence. Write
\[
\det(1-UW_p^{\otimes2k})^{-1}
=\sum_{a\ge0}c_{p,k}(a)U^a.
\tag{DW8.7a}
\]
Equation (DW7.7) proves \(c_{p,k}(a)\ge0\) and \(c_{p,k}(0)=1\). For \(n=\prod_pp^{a_p}\), define the finite product
\[
A_k(n)=\prod_pc_{p,k}(a_p).
\tag{DW8.7b}
\]
The absolutely convergent Euler expansion gives
\[
\mathcal L_k(s)=\sum_{n\ge1}A_k(n)n^{-s},
\qquad A_k(n)\ge0,\qquad \Re s>1+2kB.
\tag{DW8.7c}
\]
Its abscissa of convergence is exactly \(1+2kB\). If it converged at a real \(\sigma_0<1+2kB\), nonnegativity would make the series absolutely convergent there and locally uniformly convergent on \(\Re s>\sigma_0\), by domination with its value at a smaller intermediate real parameter. It would define a holomorphic function near \(s_k\), equal to (DW8.4) on a nonempty right half-plane and hence throughout the connected domain away from poles. That contradicts the pole already proved at \(s_k\). Convergence to the right was proved in (DW8.1a).

The pole is invariant under every prime-action-preserving isomorphism. Indeed if an invertible \(T:V_\rho\to V'\) satisfies \(TW_p=W'_pT\) for every prime, then \(T^{\otimes2k}\) conjugates their tensor operators. Every determinant in (DW8.1), their Euler product, and the continuation (DW8.4) agree exactly. Neither \(s_k\) nor \(h_k\) changes.

A quotient has a different exact formula. For a subspace \(K\subset V_\rho\) invariant under all \(W_p\), and \(Q=V_\rho/K\), a basis adapted to \(K\) gives
\[
\det(1-UW_p|V_\rho)
=\det(1-UW_p|K)\det(1-UW_p|Q).
\tag{DW8.7d}
\]
The tensor filtration on \(V_\rho^{\otimes2k}\) has associated graded the direct sum, over all words of length \(2k\) in the letters \(K,Q\), of their ordered tensor products. Triangularity gives the corresponding product formula for all the tensor determinants. Thus a quotient does not make removed spectral contributions vanish by isomorphism: the contributions persist in the kernel and the mixed tensor terms. Those terms must be retained to recover the original global object.

For comparison with Deligne, a weight-one input has expected tensor weight \(2k\); the geometric top-cohomology error \(+2\) would place the furthest allowed pole at the exponent \(k+1\). The exact displacement in the constructed tensor object is
\[
s_k-(k+1)=k(2B-1).
\tag{DW8.11}
\]
For the off-critical orbit under examination it is positive and grows linearly with \(k\). The computed positivity does not erase it. The determinant/cohomology control that supplies \(k+1\) in Deligne's argument has not been proved for these operators merely by reconstructing the original zeta function.

One must also not assign the quartet's average determinant weight to every irreducible constituent. The joint representation of all \(W_p\) has one-dimensional semisimple characters \(p\mapsto p^\omega\), with weights \(2\Re\omega\). Their maximum is \(2B\). Applying only a constituent-weight statement with the weights already visible in this representation would return \(2B\), not \(1\). The full determinant and its average weight are exactly
\[
\det(W_p|V_\rho)=p^{m\sum_{\omega\in\mathcal O_\rho}\omega}=p^{2m},
\qquad
\frac{2\log|\det(W_p|V_\rho)|}{(4m)\log p}=1.
\tag{DW8.12}
\]
That average does not identify the constituent weights.

## 9. The exact monodromy-comparison defect

Write \(J_\rho=\mathbb C[\epsilon_\rho]/(\epsilon_\rho^m)\) for the single spectral primary block of length \(m\), retaining \(V_\rho\) for the four-block direct sum. On \(J_\rho\), (DW7.2) gives
\[
W_pN_\rho W_p^{-1}=N_\rho.
\tag{DW9.1}
\]
Deligne's geometric local-monodromy relation, at norm \(p\), is instead (DW5.2). The exact defect is
\[
C_p=W_pN_\rho-p^{-1}N_\rho W_p
=(1-p^{-1})W_pN_\rho.
\tag{DW9.2}
\]
Because \(W_p\) is invertible, its rank is \(m-1\) when \(m>1\). Thus this defect is nonzero for every prime \(p\) on a nontrivial spectral jet block.

In particular, an invertible linear map intertwining both the same \(W_p\) and the same \(N_\rho\) with a norm-\(p\) Weil-monodromy representation would carry (DW9.1) and (DW5.2) to the same operators. Subtraction gives \((1-p^{-1})N=0\), hence \(N=0\), contrary to \(m>1\). This proves failure of that specific two-operator identification; it does not say the two frameworks have no relation.

There are exact surviving comparisons:

* The quotient \(J_\rho\to J_\rho/N_\rho J_\rho\) is equivariant for every \(W_p\), and its target has scalar \(p^\rho\) and nilpotent zero. This quotient has dimension one and therefore does **not** preserve the original multiplicity \(m\).
* On the full vector space with basis \(1,\epsilon,\ldots,\epsilon^{m-1}\), define \(S_p(\epsilon^j)=p^{-j}\epsilon^j\), and \(F_p^{\rm geom}=p^\rho S_p\). Then \(F_p^{\rm geom}N_\rho(F_p^{\rm geom})^{-1}=p^{-1}N_\rho\), and \(F_a^{\rm geom}F_b^{\rm geom}=F_{ab}^{\rm geom}\) for positive \(a,b\). This constructs a complex representation satisfying the Weil-monodromy operator relation, with the same nilpotent and the same scalar action on \(J_\rho/N_\rho J_\rho\). It is not asserted to be an arithmetic lisse sheaf.

The latter construction has full eigenvalues \(p^{\rho-j}\), \(0\le j<m\), whereas the original \(W_p\) has eigenvalue \(p^\rho\) with multiplicity \(m\). Thus it is not a hidden isomorphism replacing \(W_p\); its characteristic polynomial and weight data have changed in an explicitly displayed way. Its role is to identify exactly what extra grading a comparison would have to supply and exactly what original spectral data that supply alters.

Neither (DW9.2) nor this construction uses an addition on \(\tau\), a parity assignment to \(\tau\), or an identification of source support with the coefficient zero. The obstruction occurs in the actual coefficient operators and survives attachment of unchanged support labels.

## 10. What has and has not transferred

The transferred calculations are exact tensor eigenvalue multiplication, preservation of all spectral jets, the even-tensor coefficient positivity, the complete tensor Euler product (DW8.4), its forced pole and exact multiplicity, and the monodromy-comparison defect and its two explicit receiving maps.

The source of Deligne's contradiction is the combination of these tensor operations with an independently proved pole bound whose additive error is independent of tensor degree. It comes from geometric top cohomology, its Tate factor, and determinantal-weight control. It does not come from renaming the zero object or from uniqueness of the arithmetic reconstruction.

For the actual programme orbit, the directly constructed global object gives the explicit pole (DW8.5). Thus the current computation specifies the precise object to which any stronger geometric comparison must apply. The scalar zeta identification remains established; this note does not reopen it, assert RH, assert a disproof, or claim that the required geometric bound has already been transferred.
