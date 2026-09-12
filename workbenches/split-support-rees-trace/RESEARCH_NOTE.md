# Split support, Rees defects, and the completed arithmetic trace

Research continuation, 11 September 2026.

## 1. Scope and the connected calculation

This continuation starts from the filtered comparison object of *Split support, adelic filtrations, and the comparison image*, not from a fresh scalar zero-adjunction. The fixed scalar semiring is

\[
S=G(k)=k\sqcup\{\tau\},\qquad e=0_k\in S,\qquad 0_S=\tau.
\]

Here \(k\) is a characteristic-zero coefficient field. A supported zero, the polynomial parameter origin, and a zero of an arithmetic function occur at different positions in the maps below; none is substituted for another.

The construction links five operations:

\[
\begin{aligned}
&\text{a comparison in a split-support module diagram}\\
&\longrightarrow\text{its Rees inclusion and special-fibre module}\\
&\longrightarrow\text{tensor, symmetric-power, and dual defects}\\
&\longrightarrow\text{a graded determinant and its first variation}\\
&\longrightarrow\text{completed arithmetic logarithmic derivatives and test-function traces}.
\end{aligned}
\]

The algebraic statements are proved below. The completed zeta functions and their analytic properties are established arithmetic inputs, not consequences claimed from support alone. The uniform-shift Rees family used in the arithmetic calculation is explicitly constructed here; it has not been identified with the unknown cohomological comparison for the full number-field spectral realization. The calculations do not establish RH, but they provide a scalar trace bridge and an exact amplification invariant for the proposed Weil II-style programme.

The current Zeta repository already proves the split-semimodule/linear-join-diagram equivalence in chapter 14, divisor and jet maps in chapter 15, and packet-grouped logarithmic derivatives in chapter 17. Those results are inputs and are not recounted as new discoveries.

## 2. Work above the existing common support

The source chapter 14 identifies a \(G(k)\)-semimodule with a join-semilattice \(L\), vector spaces \(V_l\), and coherent linear transports

\[
\rho_{l,m}:V_l\longrightarrow V_m\quad(l\le m).
\]

The reconstructed carrier is \(M=\bigsqcup_{l\in L}V_l\), with

\[
x\boxplus y=\rho_{l,l\vee m}x+\rho_{m,l\vee m}y,
\quad e x=0_{V_l},\quad \tau x=0_{V_{0_L}}.
\]

We retain that carrier. Suppose the vector spaces have decreasing, exhaustive, separated, left-continuous filtrations with finitely many jumps, and the transports preserve them. For a compatible family of comparison maps

\[
c_l:(V_l,F_l)\longrightarrow(W_l,G_l),
\]

put \(I_l=\operatorname{im}c_l\). The source-quotient and target-subspace filtrations are

\[
Q_l^aI_l=c_l(F_l^aV_l),\qquad
P_l^aI_l=I_l\cap G_l^aW_l.
\]

The identity of \(I_l\) gives \(Q_l^aI_l\subseteq P_l^aI_l\). A commuting square of filtered comparison maps sends both filtrations into the corresponding ones at the next support label. Hence all the Rees maps and defect quotients below are functorial over this same \(L\). For any finite dimension at a label, the calculation applies there; it does not replace the whole diagram by its top fibre.

### 2.1 A strict map already supplied by mixed support

In the user's mixed double \(D_A=G(A)^2\), retain

\[
(a,b)\star(c,d)=(ac\oplus(-1_A)bd,\ ad\oplus bc),
\]

and the amplitude map

\[
p_D(a,b)=p_A(a)+t p_A(b)\in B=A[t]/(t^2+1).
\]

The synchronization idempotent is \(E=(1,e_A)\). Multiplication by \(E\) gives a retraction

\[
r_E:D_A\longrightarrow ED_A,\qquad x\longmapsto Ex,
\]

with \(p_Dr_E=p_D\) and \(r_E|_{ED_A}=\operatorname{id}\). For every specified amplitude filtration \(F^aB\), define the lifted filtration by inverse image. Then

\[
\boxed{
 r_E(p_D^{-1}F^aB)=ED_A\cap p_D^{-1}F^aB.
}
\]

The inclusion from left to right uses amplitude preservation. For the converse, any point of the right side is its own preimage under the retraction. This proves supported strictness for this actual idempotent operation; it does not require a chosen section of the ordinary amplitude map. Its induced amplitude comparison is the identity of the same filtered \(B\), so its amplitude Rees defect is zero. This addresses synchronization itself, not every subsequent cohomological map.

## 3. The finite comparison module

Fix one label and write \(I\) for the finite-dimensional image, of rank \(r\ge1\). First retain integer filtration jumps, without changing any of their values. Put \(R=k[T]\), with \(\deg T=1\), and

\[
L_Q=\sum_a Q^aI\,T^{-a},\qquad
L_P=\sum_a P^aI\,T^{-a}
\subset I\otimes_k k[T,T^{-1}].
\]

These are finite free graded \(R\)-modules and \(L_Q\subseteq L_P\). Define

\[
\boxed{D_c=L_P/L_Q.}
\]

It is a finite-dimensional \(k\)-space killed by a power of \(T\). Localizing at \(T\) identifies both lattices with the same \(I\otimes k[T,T^{-1}]\). Thus

\[
D_c=0\iff Q^aI=P^aI\text{ for every }a.
\]

If the two filtration-weight lists are \((\lambda_j)\) and \((\mu_j)\), then

\[
\ell(D_c)=\sum_j\mu_j-\sum_j\lambda_j.
\]

This is the determinant-index formula proved in the predecessor. The retained finite support lift is

\[
\widetilde L_Q=M[\mathbb Z]\times_{I[\mathbb Z]}L_Q,
\qquad
\widetilde L_P=M[\mathbb Z]\times_{I[\mathbb Z]}L_P
\]

whenever \(M\to I\) is the specified compatible amplitude carrier. Supported zero coefficients remain present in \(M[\mathbb Z]\). The ordinary quotient \(D_c\) is an amplitude invariant of these maps; it is not a new externally adjoined scalar zero.

## 4. Exact composition, duality, and amplification

### Theorem 4.1: composition and duality

For nested free lattices \(L_0\subseteq L_1\subseteq L_2\), all with the same localization,

\[
0\longrightarrow L_1/L_0\longrightarrow L_2/L_0
\longrightarrow L_2/L_1\longrightarrow0.
\]

The arrows are the inclusion of classes and the quotient map. Thus lengths add exactly. The same is true of endomorphism traces for any operator preserving the three lattices.

For \(D=L_P/L_Q\), dualizing over \(R\) gives

\[
\boxed{
0\longrightarrow L_P^\vee\longrightarrow L_Q^\vee
\longrightarrow\operatorname{Ext}^1_R(D,R)\longrightarrow0.
}
\]

Indeed \(\operatorname{Hom}_R(D,R)=0\) because \(D\) is torsion and \(R\) is a domain, and both free lattices have zero first Ext. The dual defect has the same length.

There is an explicit perfect \(k\)-pairing

\[
D\times(L_Q^\vee/L_P^\vee)\longrightarrow k,
\quad([x],[\phi])\longmapsto [T^{-1}]\,\phi(x).
\]

Evaluation is taken in \(k[T,T^{-1}]/k[T]\); changing either representative adds a polynomial, whose \(T^{-1}\) coefficient is zero. In a Smith block \(T^aR\subset R\), the pairing on bases \(T^j\) and \(T^{-a+i}\), with \(0\le i,j<a\), is the anti-diagonal matrix \(\mathbf1_{i+j=a-1}\), hence is nondegenerate. If an operator restricts to an automorphism of each lattice, its action on the dual is \(\phi\mapsto\phi\circ F^{-1}\), making the pairing invariant. No positive-definiteness assertion is substituted for this bilinear duality.

### Theorem 4.2: every tensor and symmetric power retains the defect

Let the Smith exponents of \(L_Q\subseteq L_P\) be \(a_1,\ldots,a_r\), all nonnegative. For \(m\ge1\), the tensor-power inclusion has Smith exponents

\[
a_{i_1}+\cdots+a_{i_m}\quad(1\le i_j\le r).
\]

Its defect therefore has length

\[
\boxed{\ell D_{\otimes m}=m r^{m-1}\ell D_c.}
\]

The symmetric-power inclusion has one exponent

\[
\alpha_1a_1+\cdots+\alpha_ra_r
\]

for each \(\alpha\in\mathbb N^r\) with \(\sum_i\alpha_i=m\). Consequently, writing \(r_m=\binom{m+r-1}{r-1}\),

\[
\boxed{
\ell D_{\mathrm{Sym}^m}=\binom{m+r-1}{r}\ell D_c,
\qquad
\frac{\ell D_{\mathrm{Sym}^m}}{r_m}=\frac m r\ell D_c.
}
\]

For exterior powers, \(1\le j\le r\),

\[
\boxed{\ell D_{\wedge^j}=\binom{r-1}{j-1}\ell D_c.}
\]

Proof: the invertible changes of basis used in the Smith form induce invertible maps on each displayed functor. For the diagonal inclusion, the tensor, monomial, and wedge bases give exactly the exponents written above. Each \(a_i\) occurs \(m r^{m-1}\) times in the tensor total and \(\binom{r-1}{j-1}\) times in the wedge total. In the symmetric total, symmetry makes each coordinate contribute \(m r_m/r=\binom{m+r-1}{r}\). No factorial-scaled choice of symmetric basis is used.

### Corollary 4.3: a sublinear per-rank estimate forces strictness

Suppose the **same symmetric-power comparison** satisfies

\[
\ell D_{\mathrm{Sym}^m}\le r_m b_m\quad\text{for every }m\ge1,
\qquad b_m/m\longrightarrow0.
\]

Then \(D_c=0\). In fact, the exact formula yields \(\ell D_c/r\le b_m/m\) for every \(m\), and taking the limit forces the nonnegative integer \(\ell D_c\) to vanish. The hypothesis includes bounds of the form \(b_m=C\log r_m+B\).

This is an exact amplification-to-vanishing theorem. Chen--Moriwaki provide logarithmic-rank errors for their own casting comparisons; those errors are not silently reassigned to this different comparison. To use this corollary on a given arithmetic map, its actual symmetric-power defect must receive the stated bound. Here the invariant and its exact growth are calculated, rather than assumed to vanish.

For finite real filtrations, retain the ordered exponent algebra of the predecessor and the actual degree difference \(\Delta=\sum\mu_j-\sum\lambda_j\). Symmetric-power weight sums give the same identity \(\Delta_m=\binom{m+r-1}{r}\Delta\). These are real degree differences, not a claimed finite module length over a dense non-Noetherian monoid algebra.

## 5. A trace can forget the defect while a graded trace recovers it

Let \(F\) preserve the two integer filtrations. Its induced \(R\)-linear operator commutes with \(T\) and acts on \(D_c\). For every positive integer \(n\), define finite Laurent polynomials

\[
\begin{aligned}
A_Q(z,F^n)&=\sum_d z^d\operatorname{Tr}(F^n\mid(L_Q/TL_Q)_d),\\
A_P(z,F^n)&=\sum_d z^d\operatorname{Tr}(F^n\mid(L_P/TL_P)_d),\\
\Theta_D(z,F^n)&=\sum_d z^d\operatorname{Tr}(F^n\mid(D_c)_d).
\end{aligned}
\]

The grading is literally the exponent of \(T\), so a filtration weight \(\lambda\) gives a free generator of degree \(-\lambda\).

### Theorem 5.1: the boundary-character identity

\[
\boxed{A_P(z,F^n)-A_Q(z,F^n)=(1-z)\Theta_D(z,F^n).}
\]

For a finite graded free module, the degreewise trace series is its fibre trace polynomial divided by \(1-z\). This follows either by the sequences for multiplication by \(T\), or by an adapted basis and the upper triangular action on its weight blocks. Applying additivity of trace to \(0\to L_Q\to L_P\to D_c\to0\) proves the identity. This proof also covers nonsemisimple \(F\).

At \(z=1\), the difference is zero for every \(n\). Its derivative retains the full ungraded defect trace:

\[
\boxed{
-\left.z\frac{\partial}{\partial z}(A_P-A_Q)\right|_{z=1}
=\operatorname{Tr}(F^n\mid D_c).
}
\]

For \(F=I\), this is exactly \(\ell D_c\). Higher derivatives retain higher degree moments of \(D_c\); keeping \(\Theta_D\) retains the trace on every graded component.

The derived special-fibre sequence is

\[
0\to\operatorname{Tor}_1^R(D_c,k)\to L_Q/TL_Q
\to L_P/TL_P\to D_c/TD_c\to0.
\]

The cancellation at \(z=1\) is thus explained by the actual kernel and cokernel maps. It is not a claim that these spaces individually vanish.

### Theorem 5.2: determinant form, with its sign

Define, as a formal series in \(u\),

\[
\boxed{
\mathcal B_c(u,z)=
\frac{\prod_d\det(1-u z^d F\mid(L_Q/TL_Q)_d)}
     {\prod_d\det(1-u z^d F\mid(L_P/TL_P)_d)}.
}
\]

Then \(\mathcal B_c(u,1)=1\), but

\[
\boxed{
\left.z\partial_z\log\mathcal B_c(u,z)\right|_{z=1}
=-u\partial_u\log\det(1-uF\mid D_c)^{-1}.
}
\]

Proof: the determinant logarithm gives

\[
\log\mathcal B_c(u,z)=
\sum_{n\ge1}\frac{u^n}{n}
\bigl(A_P(z^n,F^n)-A_Q(z^n,F^n)\bigr).
\]

Insert Theorem 5.1. Differentiating \((1-z^n)\Theta_D(z^n,F^n)\) at \(z=1\) yields \(-n\operatorname{Tr}(F^n|D_c)\), proving the formula. The minus sign is determined by the displayed order of numerator and denominator.

## 6. Put the actual arithmetic norms into the determinant calculation

Take the uniform comparison

\[
L_Q=k[T]\otimes V,\qquad
L_P=T^{-a}k[T]\otimes V,\qquad a\in\mathbb Z_{>0}.
\]

Its defect has length \(a\dim V\). For an operator \(F\) on \(V\),

\[
\mathcal B_{a,F}(u,z)=\frac{\det(1-uF)}{\det(1-u z^{-a}F)}.
\]

Let \(\mathfrak p\) be a finite prime of a number field, \(Q=N\mathfrak p\). Use the exact parameter map

\[
(s,\varepsilon)\longmapsto(u,z)=(Q^{-s},Q^{-\varepsilon}),
\quad Q^{-s}=\exp(-s\log Q),
\]

with the real positive \(\log Q\). If

\[
L_{\mathfrak p}(s,F)=\det(1-Q^{-s}F)^{-1},
\]

then

\[
\boxed{
\mathcal B_{a,F}(Q^{-s},Q^{-\varepsilon})
=\frac{L_{\mathfrak p}(s-a\varepsilon,F)}{L_{\mathfrak p}(s,F)}.
}
\]

Consequently,

\[
\boxed{
\left.\partial_\varepsilon\log\mathcal B_{a,F}\right|_0
=-a\frac{L_{\mathfrak p}'(s,F)}{L_{\mathfrak p}(s,F)}
=a\log Q\sum_{n\ge1}\operatorname{Tr}(F^n)Q^{-ns}.
}
\]

The prime norm produces the factor \(\log Q\); it has not been replaced by an unweighted count.

For an Artin representation, use exactly \(V^{I_{\mathfrak p}}\) and Frobenius on those inertia invariants. Since finite-group invariants in characteristic zero are exact, the same uniform comparison restricts there. Thus no ramified Euler factor is dropped. The construction is compatible with direct sums, and hence with character decompositions and their multiplicities.

### 6.1 A finite arithmetic check including ramification

For \(\mathbb Q(i)/\mathbb Q\), use the permutation representation on the two embeddings. The local determinant is

\[
\begin{cases}
(1-u)^2,&p\equiv1\pmod4,\\
1-u^2,&p\equiv3\pmod4,\\
1-u,&p=2.
\end{cases}
\]

At \(p=2\), inertia invariants have basis \((1,1)\), and the induced Frobenius is the identity. For the inert case the matrix is \(\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\); its odd power traces vanish and its even power traces are two. The prime-two factor is therefore included by the same formula, not inserted afterward without a representation.

## 7. Complete the trace, including all archimedean and discriminant terms

For a number field \(K\), retain its absolute discriminant \(D_K\), real-place count \(r_1\), and complex-place count \(r_2\). Define

\[
\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2),\qquad
\Gamma_{\mathbb C}(s)=2(2\pi)^{-s}\Gamma(s),
\]

\[
\Lambda_K(s)=|D_K|^{s/2}
\Gamma_{\mathbb R}(s)^{r_1}
\Gamma_{\mathbb C}(s)^{r_2}\zeta_K(s).
\]

These factors are explicit. Form the meromorphic family

\[
\boxed{\mathscr B_{K,a}(s,\varepsilon)
=\frac{\Lambda_K(s-a\varepsilon)}{\Lambda_K(s)}.}
\]

In a zero- and pole-free neighborhood it is holomorphic in \(\varepsilon\) near zero and has value one there. Its finite-prime part is the convergent product of the preceding uniform Rees comparisons when both real parts exceed one. Its continuation is supplied by the established completed Dedekind function.

Let \(\psi=\Gamma'/\Gamma\). The first variation is exactly

\[
\begin{aligned}
J_{K,a}(s)
&:=\left.\partial_\varepsilon\log\mathscr B_{K,a}\right|_0\\
&=-a\left[
\frac12\log|D_K|
+r_1\left(\frac12\psi(s/2)-\frac12\log\pi\right)
+r_2\left(\psi(s)-\log(2\pi)\right)
+\frac{\zeta_K'(s)}{\zeta_K(s)}\right].
\end{aligned}
\]

For \(\Re s>1\), its last term can be written with every prime ideal:

\[
-a\frac{\zeta_K'}{\zeta_K}(s)
=a\sum_{\mathfrak p}\sum_{n\ge1}
\log N\mathfrak p\,(N\mathfrak p)^{-ns}.
\]

The \(\Gamma_{\mathbb C}\) factor 2 cancels between two identical ratio factors; its presence in \(\Lambda_K\) is retained. Nothing in this construction assigns the defect length \(a\) to an actual arithmetic zero. The length indexes the comparison family, while the first variation reads the existing arithmetic divisor.

### 7.1 The higher datum lies over a supported zero

Set \(\mathscr C_{K,a}=\mathscr B_{K,a}-1\). Let \(U\) avoid the divisor of \(\Lambda_K\), and let \(A\) be the algebra of holomorphic germs near \(U\times\{0\}\). The first-jet ring map is

\[
j^1:A\longrightarrow\mathcal O(U)[\eta]/(\eta^2),
\quad f\longmapsto f(s,0)+\eta\partial_\varepsilon f(s,0).
\]

It is multiplicative by the product rule. Applying the same split functor gives

\[
G(A)\xrightarrow{G(j^1)}G(\mathcal O(U)[\eta]/\eta^2)
\xrightarrow{G(\eta\mapsto0)}G(\mathcal O(U)).
\]

For the supported germ \(\mathscr C_{K,a}\), the first arrow gives

\[
\boxed{-a\eta\,\Lambda_K'(s)/\Lambda_K(s),}
\]

and the second gives the supported zero, not \(\tau\). This is a concrete way in which evaluation at the common origin forgets arithmetic information that a retained first jet recovers. The nilpotent coefficient algebra is a higher amplitude object over the same scalar support; its zero ideal is not asserted to be prime in every coefficient ring.

At a zero or pole \(\rho\) of order \(m_\rho\), with pole orders negative,

\[
\operatorname{Res}_{s=\rho}J_{K,a}(s)=-a m_\rho.
\]

This follows by writing \(\Lambda_K(s)=(s-\rho)^{m_\rho}u(s)\), where \(u(\rho)\ne0\). Thus the jet extends meromorphically and recovers location and multiplicity, not just the common zero value.

## 8. Exact passage to an arithmetic test-function trace

Let \(f\in C_c^\infty(\mathbb R_{>0})\),

\[
h(s)=\int_0^\infty f(x)x^{s-1}\,dx,
\qquad f^\sharp(x)=x^{-1}f(x^{-1}).
\]

Then \(h(1-s)=\mathcal M(f^\sharp)(s)\). For any positively oriented contour avoiding the completed divisor,

\[
-\frac1{2\pi i}\int_C h(s)J_{K,a}(s)\,ds
=a\sum_{\rho\text{ inside }C}m_\rho h(\rho).
\]

This is the residue theorem applied to the first jet just constructed. It needs no claim about where the nontrivial zeros lie.

The completed Dedekind function has its two poles at 0 and 1 and satisfies \(\Lambda_K(s)=\Lambda_K(1-s)\). Moving the contour to the two vertical lines \(c\) and \(1-c\), with \(c>1\), gives

\[
\boxed{
\sum_{\rho\text{ nontrivial}}h(\rho)
=h(0)+h(1)-\frac1{2\pi i a}
\int_{c-i\infty}^{c+i\infty}
[h(s)+h(1-s)]J_{K,a}(s)\,ds.
}
\]

The sum counts multiplicity. Mellin transforms of the stated test functions decay faster than every power vertically in a fixed strip. The order-one completed function's paired logarithmic-derivative expansion supplies polynomial bounds along a sequence of horizontal lines avoiding its zeros; these make the horizontal integrals vanish. Equivalently, for \(K=\mathbb Q\), the current repository's normally convergent packet expansion and the standard explicit formula justify the same passage. The sum and vertical integrals converge in these test-function spaces. This is an application of those established analytic facts, not a new proof of them.

Substitute the calculated \(J\). With

\[
\mathcal G_K(f)=\frac1{2\pi i}\int_{c-i\infty}^{c+i\infty}
[h(s)+h(1-s)]
\left[r_1\frac{\Gamma_{\mathbb R}'(s)}{\Gamma_{\mathbb R}(s)}
+r_2\frac{\Gamma_{\mathbb C}'(s)}{\Gamma_{\mathbb C}(s)}\right]ds,
\]

Mellin inversion gives the full identity

\[
\boxed{
\begin{aligned}
\sum_\rho h(\rho)
={}&h(0)+h(1)+\log|D_K|f(1)+\mathcal G_K(f)\\
&-\sum_{\mathfrak p,n\ge1}\log N\mathfrak p
\left[f((N\mathfrak p)^n)+(N\mathfrak p)^{-n}f((N\mathfrak p)^{-n})\right].
\end{aligned}
}
\]

For a compactly supported \(f\), the last sum has only finitely many nonzero terms. Both poles, the discriminant term, every finite prime ideal, and the archimedean integral have been retained. This completes the scalar trace identification for the constructed first variation. It does not identify the constructed uniform-shift comparison with a compact-support-to-ordinary cohomological map for the number field.

For \(K=\mathbb Q\), \(\xi(s)=\tfrac12s(s-1)\Lambda_{\mathbb Q}(s)\). The exact ratio identity is

\[
\frac{\xi(s-a\varepsilon)}{\xi(s)}
=\frac{(s-a\varepsilon)(s-a\varepsilon-1)}{s(s-1)}
\mathscr B_{\mathbb Q,a}(s,\varepsilon).
\]

Its first variation is \(-a\xi'/\xi\). In chapter 17's actual packet coordinates it is

\[
-a\sum_O m_O\frac{P_O'(s)}{P_O(s)}
=-a\sum_O m_O\sum_{\rho\in O}\frac1{s-\rho},
\]

with that chapter's compact-uniform grouping. This is the direct integration point with the existing Zeta workbench, rather than another construction of the same packet decomposition.

## 9. What has been obtained and what is to be tested next

The common support is retained in a diagram of filtered modules. Actual support synchronization is strict. More general comparison defects have exact composition, duality, and all-power growth laws. Their ungraded determinant can be identically one while the grading derivative recovers every defect trace. Coupling that grading to the actual ideal norm reconstructs completed arithmetic logarithmic derivatives and their test-function trace, with no missing finite or infinite place.

There are now two concrete measurements to carry on the same arithmetic comparison: the all-power Rees defect \(D_{\mathrm{Sym}^m}\), and the completed first-variation trace \(J_{K,a}\). The first has a proved linear-per-rank growth law; a genuinely sublinear estimate on that very family forces strictness. The second is already expressed in the existing prime and packet formulas. No bound on the former has been deduced from the latter in this note, and no positivity of the full Weil pairing is asserted.

For the Weil II-directed route, strictness and the two opposite weight bounds remain separate calculations joined by the image map. The work here advances the strictness/trace interface. It does not replace the two-sided purity argument by support uniqueness, nor use a generic NS endpoint assertion as a proof of an arithmetic estimate.

## 10. Source and verification record

The source basis is recorded in README.md with pinned repository paths and hashes. The predecessor's complete LaTeX was read locally. Current Zeta chapters 14, 15, 17, and selected interfaces of 19 were read as TeX; the relevant local archive copies match the pinned Git blob identities. The mathematical input from Chen--Moriwaki is the attached book and the predecessor's retained formulas. The supplied Deligne TeX excerpts were reread, with their pre-existing historical-transcription qualifications retained. No new PDF or OCR extraction was used for this continuation.

The executable checks use exact rational arithmetic and symbolic polynomials, with explicit failures instead of Python assert statements. They exercise support synchronization, composition and Smith indices, tensor/symmetric/exterior multiplicities, dual residue pairings, graded traces, determinant derivatives, ramified and unramified local factors, and jet/divisor identities. They verify finite instances of the displayed general proofs, not RH, the whole Chen--Moriwaki book, Deligne's proof, or the upstream NS manuscript. Novelty and an independent mathematical audit are not claimed.

### References

- Huayi Chen and Atsushi Moriwaki, *Positivity in Arakelov Geometry over Adelic Curves: Hilbert-Samuel Formula and Equidistribution Theorem*, Progress in Mathematics 355, 2024. In particular §§2.5, 3.1, 3.2, 4.1 and 5.5. DOI: 10.1007/978-3-031-61668-6. Related preprint: arXiv:2207.02033.
- Pierre Deligne, *La conjecture de Weil. II*, Publications Mathématiques de l'IHÉS 52 (1980), 137–252. The relevant supplied TeX passages are §§3.3.4–3.3.6 and 6.2.4–6.2.6.
- James W. Cogdell, *On Artin L-functions*, especially the intrinsic inertia-invariant Euler factors, archimedean factors, and additivity/induction discussion. User-supplied text.
- Alain Connes, Caterina Consani and Henri Moscovici, *Zeta Spectral Triples*, arXiv:2511.22755, §3 for the explicit formula and its test-function conventions.
- KokunoYumeto, Zeta research reader, chapters 14, 15 and 17 at commit `42d00e359b16d52ca71568ce5e3db5341949d929`; *Split support, adelic filtrations, and the comparison image*, conversation attachment, 11 September 2026. These are research inputs, not assertions of an independently audited endpoint theorem.
