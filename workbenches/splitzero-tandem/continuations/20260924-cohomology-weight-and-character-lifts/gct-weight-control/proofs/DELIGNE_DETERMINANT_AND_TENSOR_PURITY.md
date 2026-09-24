# Determinant weights, all tensor powers, and pointwise purity

24 September 2026. Reconstruction DP0–DP9 of the determinant/tensor purity mechanism in Pierre Deligne, *La conjecture de Weil. II*, §§1.3–1.5. The dominant-pullback and étale-extension assertions1.3.13(i),1.3.14–15 and the general nonsemisimple1.3.8 are addressed in the separate monodromy-group supplement; they are not claimed proved in this file. This derivation retains the source arithmetic data. It does not assert that a new coefficient object on the programme base has already been constructed.

## DP0. Source, conventions, and the exact input

The entire current French transcription, printed pages137–252, was read. The witness is `output/Deligne_Weil_II_S20_LaTeX/typed_latex/S20_FR_record_export.tex`, SHA256 `d6836ae15d98f2b27eb98c9bd039a7d921679becd9fa47ff4717410289dbd351`. It is a local transcription, not author TeX; the source-reading ledger records its provenance and discrepancies. The passages reconstructed here are printed pages156–165, §§1.3.1–1.5.3, together with definitions1.1–1.2. No original PDF comparison is claimed.

Let \(q=p^f\), with \(p\ne\ell\) primes. Let \(X_0\) be a smooth geometrically connected curve over \(\mathbb F_q\), and \(X=X_0\times_{\mathbb F_q}\overline{\mathbb F}_q\). A geometric point \(\bar x\) gives the exact Weil-group sequence
\[
1\longrightarrow\pi_1(X,\bar x)\longrightarrow W(X_0,\bar x)
 \xrightarrow{\deg}\mathbb Z\longrightarrow0.
\tag{DP0.1}
\]
The generator is **geometric** Frobenius. At a closed point \(x\), set \(d_x=[k(x):\mathbb F_q]\) and \(N(x)=q^{d_x}\); \(F_x\) has degree \(d_x\). These integers and fields are source data of Deligne's theorem. They are not arithmetic placed on \(\tau\langle Z_1;\text{no }Z_2\rangle\).

A lisse Weil sheaf \(\mathcal F_0\) is represented by a finite-dimensional continuous representation of (DP0.1), defined over a finite extension of \(\mathbb Q_\ell\) on the geometric subgroup. Fix Deligne's coefficient embedding \(\iota:\overline{\mathbb Q}_\ell\to\mathbb C\). For \(a\ne0\), write
\[
w_{q}(a)=\frac{2\log|\iota a|}{\log q},\qquad
w_{N(x)}(a)=\frac{2\log|\iota a|}{d_x\log q}.
\tag{DP0.2}
\]
These weights are logarithms of actual Frobenius eigenvalue moduli. They are not distances between a support and a stalk. A Tate twist \((r)\) multiplies \(F_x\) by \(N(x)^{-r}\), and subtracts \(2r\) from its weight.

The established source inputs used below are global function-field class field theory, the finite-field Picard variety, the representation theory of reductive algebraic groups, Grothendieck's trace formula, and Poincaré duality for curves. We give the deductions from these inputs, including every weight and determinant step. We do not claim to reprove the entire upstream SGA theory.

## DP1. Rank-one geometric monodromy and its exact character

Let \(\chi:W(X_0,\bar x)\to E^\times\) be rank one, with \(E/\mathbb Q_\ell\) finite. Deligne1.3.1 identifies the geometric part of the abelianized Weil group, by class field theory, with degree-zero idèle classes allowing ramification at the finite boundary \(S=\overline X_0-X_0\). The map to the unramified degree-zero divisor-class group has kernel a quotient of
\[
\prod_{v\in S}\mathcal O_v^\times.
\tag{DP1.1}
\]
Each local unit group has finite residue-unit quotient and pro-\(p\) principal units. The unramified quotient is \(\operatorname{Pic}^0(\overline X_0)(\mathbb F_q)\), a finite set because the variety is of finite type over a finite field. Consequently the geometric abelian image is finite-by-pro-\(p\).

The image of \(\pi_1(X,\bar x)\) under \(\chi\) is also compact in \(E^\times\). Compactness makes its valuation image a finite subgroup of \(\mathbb Z\), hence zero. It lies in \(\mathcal O_E^\times\), which has an open pro-\(\ell\) subgroup. A group that is both pro-\(p\) and pro-\(\ell\) is trivial when \(p\ne\ell\): every finite quotient has order both a power of \(p\) and a power of \(\ell\). Taking the open subgroups in the two descriptions therefore shows that the compact image is finite.

Choose a positive integer \(h\) killing this finite image. Then \(\chi^h\) is trivial on the kernel of degree, so
\[
\chi(w)^h=b^{\deg w}
\tag{DP1.2}
\]
for some \(b\ne0\). Choose \(c\) with \(c^h=b\), and put \(\varepsilon(w)=\chi(w)c^{-\deg w}\). Direct substitution gives \(\varepsilon(w)^h=1\). Thus
\[
\boxed{\chi(w)=c^{\deg w}\varepsilon(w),\quad
\varepsilon^h=1,\quad
|\iota\chi(F_x)|=|\iota c|^{d_x}.}
\tag{DP1.3}
\]
In particular rank one is pointwise \(\iota\)-pure of weight \(w_q(c)\). No choice of an individual prime or closed point is used to create the degree map; it is the full source sequence (DP0.1).

For an irreducible rank-\(n\) constituent \(\mathcal G_0\), apply (DP1.3) to \(\det\mathcal G_0\). Its determinant weight is
\[
\beta(\mathcal G_0)=\frac1n w_q(c_{\det\mathcal G_0}).
\tag{DP1.4}
\]
If \(\alpha_1(x),\ldots,\alpha_n(x)\) are its eigenvalues with their multiplicities, then
\[
\sum_{j=1}^n w_{N(x)}(\alpha_j(x))=n\beta(\mathcal G_0)
\tag{DP1.5}
\]
at **every** closed point. This is an equality about the product of eigenvalues; individual equality has not yet been obtained.

The convention for a constant twist defined over \(\mathbb F_p\) is important. If its Frobenius scalar is \(b\), it multiplies the determinant at \(x\) by
\[
b^{n[k(x):\mathbb F_p]}=b^{n f d_x}.
\tag{DP1.6}
\]
This multiplication by \(f\), not division by \(f\), follows from the degree of the residue-field extension. The available transcription's1.3.6 exponent is inconsistent with1.2.7; equation(DP1.6) derives the correction while retaining the original scalar and field.

## DP2. The central element that controls determinant weights

Replace \(\mathcal F_0\) by its semisimplification for this paragraph only: determinants and constituent weights are unchanged, and no extension is removed from later trace formulas. Let \(G^0\) be the Zariski closure of geometric monodromy on its fibre. A degree-one lift \(w\) normalizes \(G^0\). The group
\[
G=G^0\rtimes_{\operatorname{Int}(\rho(w))}\mathbb Z
\tag{DP2.1}
\]
receives the Weil group and all its tensor constructions. Its identity component \(G^{00}\) is reductive. Indeed its unipotent radical is characteristic in \(G^{00}\), hence normal in \(G\). The invariant subspace in an irreducible \(G\)-module is nonzero by unipotence and \(G\)-stable by normality, hence is the whole module. The radical therefore acts trivially on the semisimple faithful fibre, and is trivial.

We recall the rest of Deligne1.3.9's argument because reductivity alone is insufficient. The connected central torus \(T_1\subset G^{00}\) acts through a finite set of characters on the faithful fibre. These characters generate its character group; conjugation permutes them, so after a finite-index restriction conjugation acts trivially on \(T_1\). The outer automorphisms of a reductive group that act trivially on its connected centre form a finite group (the finite root-datum automorphisms). A further finite-index restriction therefore makes the degree action inner. After changing its lift by an element of \(G^{00}\), this restriction is \(G^{00}\times\mathbb Z\). The associated finite cover and constant-field extension retain a smooth curve, and rank-one result(DP1.3) applies there.

The maximal torus quotient of \(G^{00}\) is isogenous to \(T_1\). Every character of that quotient would give a rank-one Weil character with finite geometric image by(DP1.3). Its geometric image is also Zariski dense by construction. A finite subset cannot be Zariski dense in a positive-dimensional torus. Therefore the torus quotient is trivial and \(G^{00}\) is semisimple. Its centre is finite.

Choose a positive power of the degree-one lift \(w\) whose conjugation is inner on \(G^{00}\) and trivial on the finite group \(G^0/G^{00}\). Correct it by an element \(h_0\in G^{00}\), obtaining \(y=h_0w^m\) that centralizes \(G^{00}\). For each representative \(h\) of \(G^0/G^{00}\), the commutator \([y,h]\) lies in \(G^{00}\) because the component action is trivial; it centralizes \(G^{00}\) because \(y\) does. Thus it lies in the finite centre \(Z(G^{00})\). Also \([y,w]\) lies in \(G^{00}\), by the expression \(y=h_0w^m\), and centralizes \(G^{00}\), so it lies in that same finite centre. Since \(y\) centralizes this finite centre, a common positive power kills all these commutators. That power centralizes \(G^{00}\), the representatives of \(G^0/G^{00}\), and \(w\), which together generate \(G\). We obtain
\[
z\in Z(G),\qquad m=\deg(z)>0.
\tag{DP2.2}
\]
This proves finite **index**, not finiteness, of the image of \(Z(G)\to\mathbb Z\). Its kernel is contained in the finite centre of \(G^0\). The contradictory wording “finite subgroup of Z” in the available1.3.10(iv) is not used.

On any irreducible \(G\)-module \(V\), the central element \(z\) is a scalar \(u\) by Schur's lemma. The determinant character extends(DP1.3) from the Weil group to \(G\): its \(h\)-th power is trivial on geometric monodromy, hence on its Zariski closure \(G^0\). Writing \(g=g_0w^d\) gives \(\chi(g)^h=b^d\); choosing \(c^h=b\) yields \(\varepsilon(g)=\chi(g)c^{-d}\) with \(\varepsilon(g)^h=1\). Thus evaluation at \(z\), whether or not it is itself in the Weil-group image, is legitimate. If \(V\) has rank \(r\), this gives
\[
u^r=c^{m}\varepsilon(z),\qquad
|\iota u|^r=|\iota c|^{m},\qquad
\boxed{|\iota u|=q^{m\beta(V)/2}.}
\tag{DP2.3}
\]
This proves1.3.12's central-character criterion with the rank and degree factors intact.

Tensor products multiply eigenvalues of \(z\). Thus their determinant weights add. In an exterior power, a triangular basis for the action of \(z\) shows that every eigenvalue is a product of the chosen number of diagonal eigenvalues. If the constituent weight \(\gamma\) occurs in total rank \(n(\gamma)\), the determinant weights of \(\bigwedge^a\mathcal F_0\) are
\[
\sum_\gamma a(\gamma)\gamma,
\quad 0\le a(\gamma)\le n(\gamma),\quad
\sum_\gamma a(\gamma)=a.
\tag{DP2.4}
\]
For nonsplit sheaves, a composition filtration induces the tensor and exterior filtrations, and the same eigenvalue products give the weights of their graded constituents. Hence these conclusions do not require splitting extensions in the original sheaf.

## DP3. The complete curve trace identity and its poles

For any lisse sheaf \(\mathcal V_0\) on the curve, write \(V\) for its geometric fibre and \(\Pi=\pi_1(X,\bar x)\). The complete formulas are
\[
H^0(X,\mathcal V)=V^\Pi,
\quad
H_c^0(X,\mathcal V)=
\begin{cases}V^\Pi,&X\text{ proper},\\0,&X\text{ not proper},\end{cases}
\quad
H_c^2(X,\mathcal V)=V_\Pi(-1).
\tag{DP3.1}
\]
The last equality follows from Poincaré duality with
\(H^0(X,\mathcal V^\vee(1))\); in particular the \((-1)\) and the resulting factor \(q\) are retained. These invariant and coinvariant spaces come from geometric-constant subobjects or quotients. If every determinant weight of \(\mathcal V_0\) is at most \(b\), eigenvalues on \(H_c^0\) have weight at most \(b\), and those on \(H_c^2\) have weight at most \(b+2\).

Grothendieck's trace formula, Deligne1.4.5, gives
\[
L(\mathcal V_0,t)
=\prod_{x\in|X_0|}\det(1-F_x t^{d_x}\mid\mathcal V_{\bar x})^{-1}
=\frac{\det(1-Ft\mid H_c^1(X,\mathcal V))}
{\det(1-Ft\mid H_c^0(X,\mathcal V))
 \det(1-Ft\mid H_c^2(X,\mathcal V))}.
\tag{DP3.2}
\]
This begins as a formal series identity. For each coefficient only finitely many closed points contribute. Every cohomology group, sign, and multiplicity remains in(DP3.2). On an affine smooth connected curve, \(H_c^0=0\) by(DP3.1), so its determinant is exactly1; this is a proved vanishing, not a discarded term.

When eigenvalue weights at closed points are at most \(b\) and dimension is \(d\), the Euler product converges absolutely for
\[
|t|<q^{-b/2-d}.
\tag{DP3.3}
\]
Indeed a finite decomposition into quasi-finite maps to affine space bounds the number of degree-\(n\) closed points by \(Cq^{dn}\). The absolute logarithmic expansion is bounded by a constant times \(\sum_{n\ge1}q^{dn}q^{nb/2}|t|^n\), after summing repetitions geometrically on a smaller closed disc. This converges. This argument is Deligne1.4.6; it records how arithmetic point counts enter the analytic function.

## DP4. Even tensor powers give positive coefficients, without a positive form

All local and global L-functions in DP4–DP5 are complex series after coefficientwise application of \(\iota\). This includes the determinant on the left of(DP4.1).

Suppose that \(\mathcal F_0\) is \(\iota\)-real: the local polynomial \(\iota\det(1-F_x u\mid\mathcal F_{\bar x})\) has real coefficients at every closed point. Newton identities show that \(\iota\operatorname{Tr}(F_x^j\mid\mathcal F_{\bar x})\) is real for each \(j\ge1\). For a positive integer \(k\), set \(\mathcal V_0=\mathcal F_0^{\otimes 2k}\). The exact local logarithm is
\[
\log\det(1-F_x t^{d_x}\mid\mathcal V_{\bar x})^{-1}
=\sum_{j\ge1}\frac{
 \bigl(\iota\operatorname{Tr}(F_x^j\mid\mathcal F_{\bar x})\bigr)^{2k}}
 {j}\,t^{j d_x}.
\tag{DP4.1}
\]
The trace identity used here is \(\operatorname{Tr}(A^{\otimes 2k})=(\operatorname{Tr}A)^{2k}\), proved by multiplying diagonal entries in a tensor basis. Every coefficient on the right is nonnegative. Exponentiating a series with nonnegative coefficients and zero constant term gives nonnegative coefficients and constant term1, because each coefficient of \(\sum_{r\ge0}h^r/r!\) is a sum of nonnegative products.

Consequently each local factor \(L_{x,k}(t)\) has nonnegative Taylor coefficients. The product of all other factors also has nonnegative coefficients and constant term1. Coefficientwise,
\[
0\le[t^n]L_{x,k}(t)\le[t^n]L(\mathcal F_0^{\otimes2k},t).
\tag{DP4.2}
\]
For any finite \(n\), the assertion follows from the finite product of points of degree at most \(n\), so there is no convergence assumption hidden in this formal inequality.

This is positivity of power-series coefficients obtained from **real traces at every closed point and every repetition**. No positive inner product on the sheaf has been assumed, and no reflection-positivity assertion about the programme has been inserted.

## DP5. Pole control implies each eigenvalue inequality

For the zero sheaf there are no eigenvalues or constituents, so the assertions are vacuous. Assume the sheaf has positive rank before taking a largest determinant weight.

Let \(r\) be the largest determinant weight of \(\mathcal F_0\). By(DP2.4), every constituent of \(\mathcal F_0^{\otimes2k}\) has determinant weight at most \(2kr\). Remove a closed point different from the particular point \(x\) being tested, making the curve affine. The restriction retains the local eigenvalues at \(x\) and its determinant weights: the fundamental group of the nonempty open curve surjects onto that of the original normal curve, so constituents stay irreducible with the same determinant characters.

Equations(DP3.1–2) show that the global rational function has no pole in
\[
|t|<R_k,\qquad R_k=q^{-(2kr+2)/2}.
\tag{DP5.1}
\]
This uses the full possible \(H_c^2\) denominator. Cancellation with the numerator can only remove poles, so it cannot invalidate the asserted disc. The Taylor series of this rational function converges at every \(0\le t<R_k\). Equation(DP4.2) and nonnegativity then make the local factor's Taylor series converge there too. It therefore has radius at least \(R_k\).

If \(\alpha\) is any eigenvalue of \(F_x\) on \(\mathcal F_{\bar x}\), then \(\alpha^{2k}\) is an eigenvalue on the tensor power, including its multiplicity. The reciprocal local determinant has a pole at every solution of
\[
t^{d_x}=(\iota\alpha)^{-2k},
\quad\text{each of modulus }|\iota\alpha|^{-2k/d_x}.
\tag{DP5.2}
\]
Its numerator is1, so these poles cannot be cancelled locally. Radius at least \(R_k\) implies
\[
|\iota\alpha|^{2k/d_x}\le q^{(2kr+2)/2},
\qquad
w_{N(x)}(\alpha)\le r+\frac1k.
\tag{DP5.3}
\]
The same fixed eigenvalue satisfies(DP5.3) for every positive integer \(k\). If its weight exceeded \(r\) by \(e>0\), an integer \(k>1/e\) would contradict(DP5.3). Thus
\[
\boxed{w_{N(x)}(\alpha)\le r.}
\tag{DP5.4}
\]
This is Deligne1.5.2 with the analytic coefficient-domination step supplied in full. It uses all tensor powers to obtain an exact conclusion, not a finite numerical sample.

## DP6. Exterior powers and determinant equality force every constituent to be pure

For each determinant weight \(\beta\), let \(n(\beta)\) be the total rank of the corresponding constituents, and \(\alpha_i^\beta\), \(1\le i\le n(\beta)\), their local eigenvalues at a fixed \(x\), counted with multiplicity. From(DP1.5),
\[
\sum_i w_{N(x)}(\alpha_i^\gamma)=n(\gamma)\gamma
\quad\text{for every }\gamma.
\tag{DP6.1}
\]
Fix an occurring \(\beta\), and put \(N_\beta=\sum_{\gamma>\beta}n(\gamma)\). The largest determinant weight of \(\bigwedge^{N_\beta+1}\mathcal F_0\) is
\[
r_\beta=\beta+\sum_{\gamma>\beta}n(\gamma)\gamma
\tag{DP6.2}
\]
by(DP2.4): choose every higher-weight eigenvalue, then one at weight \(\beta\). Exterior powers preserve the reality of the characteristic polynomial because their eigenvalues are products and complex conjugation permutes the original eigenvalue multiset. Hence DP5 applies to this exterior power. Its eigenvalue
\[
\alpha_i^\beta\prod_{\gamma>\beta}\prod_j\alpha_j^\gamma
\tag{DP6.3}
\]
has weight at most \(r_\beta\). Subtract the equalities(DP6.1) for \(\gamma>\beta\). This gives \(w_{N(x)}(\alpha_i^\beta)\le\beta\) for each \(i\). Their sum is exactly \(n(\beta)\beta\) by(DP6.1). If any individual inequality were strict, this sum would be strictly smaller. Therefore
\[
\boxed{w_{N(x)}(\alpha_i^\beta)=\beta
\quad\text{for every }x,\beta,i.}
\tag{DP6.4}
\]
This completes the deduction of Deligne1.5.1. No chosen eigenvalue or constituent has been dropped.

## DP7. The full real companion and its retained scalar

For a pointwise pure sheaf of integer weight \(n\), the source real companion is
\[
\mathcal F_0\oplus\mathcal F_0^\vee(-n).
\tag{DP7.1}
\]
At \(x\), an eigenvalue \(a\) is paired with \(N(x)^n/a\). Since \(|\iota a|^2=N(x)^n\), that second complex eigenvalue equals \(\overline{\iota a}\). This proves reality and preserves the same weight; the Tate factor is essential.

For arbitrary real \(\beta\) in the category of Weil sheaves, let \(\mathcal L_{\beta}\) be the constant Weil line whose geometric \(\mathbb F_q\)-Frobenius is the scalar \(\iota^{-1}(q^\beta)\). Its value at \(x\) is \(N(x)^\beta\), and its weight is \(2\beta\). Then the exact companion is
\[
\mathcal F_0\oplus(\mathcal F_0^\vee\otimes\mathcal L_\beta).
\tag{DP7.2}
\]
The proof is the same equality \(N(x)^\beta/a=\overline a\) after \(\iota\). The scalar need not be an \(\ell\)-adic unit, which is why Weil sheaves, rather than only étale sheaves, occur here. This construction starts with proved pointwise purity; it is not an argument establishing purity of an arbitrary sheaf merely by adjoining a dual.

## DP8. What this calculation actually supplies to weight control

The proved chain is:
\[
\begin{gathered}
\text{rank-one geometric finiteness}
\longrightarrow\text{determinant weights and tensor rules}\\
\longrightarrow\text{all-even-power coefficient positivity}
\longrightarrow\text{global pole control}\\
\longrightarrow\text{pointwise constituent purity}.
\end{gathered}
\tag{DP8.1}
\]
Every arrow has been calculated above. The curve's \(H_c^2\) Tate twist supplies the \(+2\); all powers make its contribution \(1/k\), and the exact determinant sum supplies equality. This is one genuine weight-control mechanism. The later source proof uses the local monodromy filtration and a Lefschetz pencil to pass from pointwise sheaf purity to cohomological purity. Those steps have their own complete reconstructions;(DP8.1) does not replace them.

## DP9. Named external inputs and reading limits

The rank-one argument uses Deligne1.3.1's explicitly cited global class-field isomorphism and the Picard variety. The central-element argument uses the root-datum description of automorphisms of a connected reductive group cited in1.3.10. The cohomological trace identity and duality are the theorems recalled in1.4.1–1.4.5. Their exact statements used here are displayed, and the ensuing deductions are proved. A complete reconstruction of the weight argument does not mean that these foundational theories have all been independently rebuilt. The wider full-source reading is recorded in `DELIGNE_FULL_READING_LOG.md`.
