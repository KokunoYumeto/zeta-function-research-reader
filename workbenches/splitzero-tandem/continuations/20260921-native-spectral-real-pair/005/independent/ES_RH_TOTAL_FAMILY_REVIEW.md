# Independent review of the complete eight-state ES family

The complete source `ES_RH_TOTAL_FAMILY_ROOT_BODY.tex`, EF1–25, was read and independently checked. The reviewed version has SHA256 `720a4663eaf96a319997b700bb620eab46759696231c2740eb98d6c003e83ff7`. Its stated mathematical assertions are accepted. In particular, EF6–7, the phase-dependent coefficient in EF19, both the limiting and finite-parameter metric formulas, and the complete eight-state matrices in EF25 are correct.

The signed endpoint determinant requires its sign: the exact limit is

\[
\lim_{z\to1}d^{-6}\det\Theta_L=-65536\gamma^{12}.
\]

Its absolute value is the positive constant used in EF22. The source's signed formula EF17 and its absolute-value formula EF22 are consistent.

The independent script `ES_RH_TOTAL_FAMILY_REVIEW.py` produces `ES_RH_TOTAL_FAMILY_REVIEW.json`: **45 groups / 331 exact scalar entries pass**. The proof below supplies the geometric, positivity and limiting arguments that are not consequences of a finite list of algebra checks. No rendering, packaging, publication or source discovery was performed.

## 1. The original family and all eight coefficient states

Keep the original positive parameters \(p,\gamma\), the real parameter \(0\le z\le1\), and \(\tau=1-z\). The four slots are explicitly

\[
(\mathrm M,\mathrm N,\mathrm T,\mathrm E)=(\alpha,\beta,\alpha,\chi),
\]

where

\[
\alpha=p\tau+z(1/2+i\gamma),\quad
\beta=2p\tau/5+z(1/2-i\gamma),\quad
\chi=2p\tau+z(1/2-i\gamma).
\]

At \(z=0\) this is the declared ordering \((p,2p/5,p,2p)\) of the ES tuple \((p;p,2p/5,2p)\). The reciprocal identity is exact:

\[
\frac1p+\frac1{2p/5}+\frac1{2p}
=\frac1p+\frac5{2p}+\frac1{2p}=\frac4p.
\]

The sum \(S=2\alpha+\beta+\chi=22p\tau/5+2z\) is strictly positive, so \(A_z=-1/S\) is retained and nonzero. Expansion of \(A_z(r-\alpha)^2(r-\beta)(r-\chi)\) gives cubic coefficient \(-A_zS=1\) and exactly the other coefficients in EF2. At the two endpoints this gives the displayed ES polynomial and

\[
-\frac12\big((r-1/2)^2+\gamma^2\big)^2.
\]

Set

\[
m=(\beta+\chi)/2,\quad x=r-m,\quad
d=4p\tau/5,\quad k=-p\tau/5+2i\gamma z,\quad
\kappa=k^2-d^2.
\]

Then \(h_z=A_z(x-k)^2(x^2-d^2)\), with the unchanged inverse coordinate \(r=x+m\). The factors

\[
k-d=-p\tau+2i\gamma z,\qquad
k+d=3p\tau/5+2i\gamma z
\]

cannot vanish on the interval: vanishing of their imaginary part requires \(z=0\), when their real parts are nonzero. Thus \(\kappa\ne0\) throughout. Localizing \(\mathbb C[z]\) at \(S\kappa\) makes both factors units. Dividing successively by the unit-leading quartic relation and by the monic relation \(t^2-h_z'\) gives the free basis

\[
1,r,r^2,r^3,t,tr,tr^2,tr^3.
\]

Its rank is eight at both endpoints as well as every intermediate parameter. This does not assert that the fibres are reduced; the upper double root persists throughout.

## 2. Complete projector coefficients and inverse

Write \(a_0=k^2+d^2\). Direct expansion proves the polynomial identity

\[
e_U=\frac{(x^2-d^2)(3k^2-d^2-2kx)}{\kappa^2},\quad
e_L=\frac{(x-k)^2(a_0+2kx)}{\kappa^2},\quad e_U+e_L=1.
\]

At \(x=k+\varepsilon\), the first factor times the displayed first-order reciprocal is \(1\) modulo \(\varepsilon^2\). Modulo \(x^2-d^2\), the product

\[
(a_0-2kx)(a_0+2kx)=a_0^2-4k^2d^2=\kappa^2
\]

proves the other congruence. Coprimality therefore proves the idempotent and orthogonality relations on the full nonreduced quotient, including \(d=0\).

Expanding \(e_U,e_U(x-k),e_L,e_Lx\) and reducing by

\[
x^4=2kx^3-\kappa x^2-2kd^2x+k^2d^2
\]

gives exactly all sixteen entries of EF6. The following four functionals give their full inverse:

\[
f\longmapsto
\big(f(k),f'(k),[1](f\bmod(x^2-d^2)),[x](f\bmod(x^2-d^2))\big).
\]

In cubic coefficients their matrix is

\[
M=\begin{pmatrix}
1&k&k^2&k^3\\0&1&2k&3k^2\\
1&0&d^2&0\\0&1&0&d^2
\end{pmatrix}.
\]

Applying these rows to the four displayed projector columns yields \(I_4\). Subtracting the first row from the third and the second from the fourth makes the determinant the bottom-right minor

\[
\det\begin{pmatrix}-\kappa&-k^3\\-2k&d^2-3k^2\end{pmatrix}
=\kappa^2.
\]

Thus \([P_U\ P_L]^{-1}=M\) and \(\det[P_U\ P_L]=\kappa^{-2}\). This explicitly verifies both products and the determinant in EF7.

The complete binomial maps \(C_{-m}\) and \(C_m\) substitute \(x=r-m\) and \(r=x+m\) and compose to the identity. They therefore prove EF8, including its inverse and its original centre. Its exact column order is upper even, lower even, upper odd, lower odd, each pair in its displayed basis. In particular, the lower inclusion is the rectangular matrix \(\operatorname{diag}(C_{-m}P_L,C_{-m}P_L)\); it has rank four because each \(P_L\) has rank two.

Applying the unchanged original maps \(F_U,F_W\) preserves this injection, with \(T_A\oplus T_A\) between the two images. All original metrics are induced by this precise inclusion.

## 3. Both local algebras and all residue corrections

Differentiation before quotienting gives the upper relation

\[
t^2=2A_z\kappa\varepsilon\pmod{\varepsilon^2},
\]

and the lower relation

\[
t^2=u x+v\pmod{x^2-d^2},\quad
u=2A_z(k^2+d^2),\quad v=-4A_zkd^2.
\]

This proves EF9 with its full derivative constants. In the upper cofactor

\[
g(\varepsilon)=A_z(\kappa+2k\varepsilon+\varepsilon^2),
\]

the first two coefficients are \(g_0=A_z\kappa\) and \(g_1=2A_zk\). The coefficient of \(\varepsilon\) in \((b_0+b_1\varepsilon)/g\), modulo \(\varepsilon^2\), is

\[
\frac{b_1}{A_z\kappa}-\frac{2kb_0}{A_z\kappa^2}.
\]

This proves EF10 without discarding the derivative of the cofactor. In the lower quotient, the exact inverse of \(A_z(x-k)^2\) is

\[
\frac{k^2+d^2+2kx}{A_z\kappa^2}.
\]

Multiplication by \(b_0+b_1x\), followed by its coefficient of \(x\), gives EF11. Its two-by-two cross determinant is

\[
\frac{4k^2d^2-(k^2+d^2)^2}{A_z^2\kappa^4}
=-\frac1{A_z^2\kappa^2},
\]

so the full lower residue determinant is \(1/(A_z^4\kappa^4)\). The upper residue has the same determinant. Their complete eight-dimensional direct product has determinant \(1/(A_z^8\kappa^8)\), and is perfect throughout this family, including its final two nilpotent blocks. The independent checker calculates the complete cross Gram directly from the original quartic residue and confirms both off-primary blocks are zero.

At the ES endpoint \(g_{0,E}=3p/22\) and \(g_{1,E}=1/11\), so \(g_{1,E}/g_{0,E}=2/(3p)\). For the continuous choice \(c^2=g_{0,E}/g_0\), the map \(\varepsilon_E\mapsto\varepsilon\), \(t_E\mapsto ct\) preserves both relations and has the stated inverse. The complete unit

\[
w_E=c^3\left(1+\left(\frac{g_{1,E}}{g_{0,E}}-\frac{g_1}{g_0}\right)\varepsilon_E\right)
\]

satisfies \(\Lambda_U(\phi f)=\Lambda_E(w_Ef)\): on \(t_E\varepsilon_E\), both sides are \(c/g_0=c^3/g_{0,E}\); on \(t_E\), both sides are \(-cg_1/g_0^2\). The two even basis vectors have zero residue. This proves the identity on the entire algebra and the inverse unit follows from \(\varepsilon_E^2=0\). The endpoint coefficient is \(2/(3p)+i/\gamma\), with the retained sign in EF12.

## 4. All four actual lower inverse branches

For \(z<1\), \(d>0\) and both lower roots are simple. At \(x=\epsilon d\), differentiation gives

\[
h_z'(m+\epsilon d)=2A_z\epsilon d(\epsilon d-k)^2.
\]

The four nonzero values

\[
t_{\epsilon,\sigma}=\sigma(\epsilon d-k)\sqrt{2A_z\epsilon d},
\qquad \epsilon,\sigma\in\{1,-1\},
\]

therefore give every lower sign/root state, with the exact square-root choices stated in EF13. The root \(\epsilon=-1\) is the N slot and \(\epsilon=1\) is the E slot. The two signs remain distinct.

Insertion into the original FS13 inverse gives exactly EF14, retaining all four coordinate polynomials and every coefficient. Its projection is the original polynomial target because FS13 composed with the original polynomial is FS4. The persistent upper primary algebra has \(t^4=0\), so its open \(t\ne0\) is empty; it supplies no extra finite affine branch.

As \(z\to1\), the displayed square roots give

\[
\frac{t_{\epsilon,\sigma}}{\sqrt d}
\longrightarrow\sigma(-2i\gamma)\sqrt{-\epsilon}.
\]

Here \(\sqrt{-1}=i\) for \(\epsilon=1\) and \(\sqrt1=1\) for \(\epsilon=-1\), as fixed in EF13. In the original source vector, multiplying \(t^{-1}\) by \(\sqrt d\) gives the reciprocal of this limit. Every other coordinate tends to zero after the same multiplication: \(r,A_z,B_z\) are bounded and \(t=O(\sqrt d)\) in their complete expressions. This proves the vector limit in EF15. Fixed linearity and norm continuity prove the two original-metric limits, whose four common magnitudes are \(\|\Phi e_1\|/(2\gamma)\) and \(\|\Psi e_1\|/(2\gamma)\). Their different complex phases have not been identified.

## 5. The complete lower inverse and its signed endpoint

In the unchanged lower basis, set

\[
X_d=\begin{pmatrix}0&d^2\\1&0\end{pmatrix},\quad
H_d=uX_d+vI,\quad D_d=v^2-u^2d^2=-4A_z^2d^2\kappa^2.
\]

Since \(X_d^2=d^2I\), multiplication immediately proves

\[
H_d^{-1}=\frac{vI-uX_d}{D_d},\qquad
H_d^{-2}=\frac{(v^2+u^2d^2)I-2uvX_d}{D_d^2}.
\]

Multiplication by \(t\) has blocks \(\left(\begin{smallmatrix}0&H_d\\I&0\end{smallmatrix}\right)\). Cubing and multiplying by two gives EF16, and block multiplication proves both inverse products in EF17. The determinant is

\[
\det\Theta_L=2^4(\det H_d)^3
=16D_d^3=-1024A_z^6d^6\kappa^6.
\]

Multiplying the full residue Gram by this matrix gives the trace Gram EF18, with determinant \(-1024A_z^2d^6\kappa^2\). Alternatively its entries follow from \(\operatorname{Tr}(1)=4\) and zero traces of \(x,t,tx\), with every product reduced by the two original relations.

There is no inversion of the complete eight-dimensional trace here. The upper trace has rank one throughout. The lower trace has rank four for \(z<1\), and rank one at \(z=1\); hence the complete trace has ranks five and two, respectively. In the exact EF8 order, upper even, lower even, upper odd, lower odd, its complete matrix is

\[
\operatorname{diag}\left(4,0,4,4d^2,0,0,
\begin{pmatrix}4v&4ud^2\\4ud^2&4vd^2\end{pmatrix}\right).
\]

This proves the displayed trace order in EF25. Its residue cross matrix is precisely \(\operatorname{diag}(J_U,J_L)\), already calculated in Section 3; squaring its determinant gives the stated eight-state residue determinant. The independent checker additionally derives every trace entry from the whole-algebra functional \(\operatorname{Tr}(R+tV)=4R(k)+2R(d)+2R(-d)\) and compares all 64 entries in this order. That functional counts both the upper multiplicity and the sign extension, and remains valid at \(d=0\).

The exact expressions after multiplying the inverse blocks by \(d^2\) are regular at the endpoint because \(A_z\kappa\ne0\). In particular,

\[
d^2H_d^{-2}
=\frac{((k^2+d^2)^2+4k^2d^2)I+4k(k^2+d^2)X_d}
       {4A_z^2\kappa^4}.
\]

Substituting \(A_z\to-1/2\), \(k\to2i\gamma\), \(X_d\to N_2\), and \(\kappa\to-4\gamma^2\) gives

\[
\lim d^2H_d^{-1}=\frac{N_2}{4\gamma^2},\qquad
\lim d^2H_d^{-2}=\frac{I-2iN_2/\gamma}{16\gamma^4}.
\]

This proves every coefficient and the phase in EF19. The first block has rank one; the second is invertible, so \(K_L\) has rank three. The forward limit has just the lower-left block \(8\gamma^2N_2\) and has rank one. The signed determinant limit is

\[
-1024\left(-\tfrac12\right)^6(-4\gamma^2)^6
=-65536\gamma^{12}.
\]

## 6. Explicit evaluation of every endpoint constant

The inclusion in EF20 is injective through \(z=1\), so its Gram \(G_L(z)\) is positive and continuous, with positive endpoint \(G_*\). Both parity blocks have the same retained metric \(G_*\). Put

\[
\rho=(G_*)_{11}(G_*^{-1})_{00}>0.
\]

These indices are zero-based in the lower basis \((1,x)\). For \(N=N_2=e_1e_0^{\mathsf T}\), its squared operator norm is exactly \(\rho\): the squared norm of its image vector is \((G_*)_{11}\), and that of its input coordinate functional is \((G_*^{-1})_{00}\). Equivalently,

\[
\operatorname{tr}(G_*^{-1}N^*G_*N)=\rho.
\]

The off-diagonal blocks of \(K_L\) act between orthogonal parity spaces. Its positive singular constants are therefore the union of the positive singular constants of

\[
\frac{N}{8\gamma^2},\qquad
\frac{I-2iN/\gamma}{32\gamma^4}.
\]

The first has the single positive value \(\sqrt\rho/(8\gamma^2)\). For \(V=I-2iN/\gamma\), the determinant is one. Expanding its metric square gives

\[
\begin{aligned}
\operatorname{tr}(G_*^{-1}V^*G_*V)
&=2-\frac{2i}{\gamma}\operatorname{tr}N
  +\frac{2i}{\gamma}\operatorname{tr}(G_*^{-1}N^*G_*)
  +\frac4{\gamma^2}\operatorname{tr}(G_*^{-1}N^*G_*N)\\
&=2+\frac{4\rho}{\gamma^2}.
\end{aligned}
\]

Both linear traces vanish by cyclic invariance and \(\operatorname{tr}N=0\). Its two positive singular values have product one and squared sum \(2+4\rho/\gamma^2\). Solving these two equations, retaining the positive roots, yields

\[
\sqrt{1+\rho/\gamma^2}\pm\frac{\sqrt\rho}{\gamma}.
\]

After the unchanged block factors, all three endpoint constants are exactly the multiset in EF23. No ordering among these three expressions is asserted before sorting; the largest depends on the actual parameters and metric.

The forward rank-one limit has positive singular value

\[
\eta=8\gamma^2\sqrt\rho.
\]

The product of the two shear constants is \(1/(1024\gamma^8)\), so

\[
c_1c_2c_3=\frac{\sqrt\rho}{8192\gamma^{10}},\qquad
\frac{c_1c_2c_3}{\eta}=\frac1{65536\gamma^{12}}.
\]

There is an independent adjugate verification. In the four-dimensional lower basis,

\[
\operatorname{adj}K_L
=-\frac1{8192\gamma^{10}}e_3e_0^{\mathsf T}.
\]

The unique nonzero third-exterior singular value of \(K_L\) has squared norm

\[
\operatorname{tr}\big(\Gamma_*^{-1}(\operatorname{adj}K_L)^*
              \Gamma_*\operatorname{adj}K_L\big)
=\frac{\rho}{2^{26}\gamma^{20}}.
\]

This is exactly the cubic invariant \(a_3=c_1^2c_2^2c_3^2\) in EF21. The checker proves these identities with a general complex Hermitian matrix

\[
G_*=\begin{pmatrix}g_a&g_b+ig_c\\g_b-ig_c&g_d\end{pmatrix},
\]

before imposing its positivity conditions. Thus the calculation preserves complex off-diagonal metric entries; it does not substitute a diagonal or Euclidean metric.

## 7. Every finite-parameter singular value and exterior norm

For each \(z<1\), use precisely \(G=G_L(z)\) and the two maps \(F=H_d,H_d^2\). The positive metric square

\[
G^{-1}F^*GF
\]

is similar to the positive Hermitian matrix \((G^{1/2}FG^{-1/2})^*(G^{1/2}FG^{-1/2})\). Its trace is \(a_F\), and its determinant is \(|\det F|^2=b_F\). Therefore the two positive singular squares are

\[
\lambda_{F,\pm}=\frac{a_F\pm\sqrt{a_F^2-4b_F}}2.
\]

For \(H_d\), \(b_F=|D_d|^2\); for \(H_d^2\), it is \(|D_d|^4\). Both are positive. The two orthogonal parity blocks of the exact inverse are \(\tfrac12H_d^{-1}\) and \(\tfrac12H_d^{-2}\), with the same metric on source and target. Their singular values are precisely

\[
\frac1{2\sqrt{\lambda_{H,+}}},\quad
\frac1{2\sqrt{\lambda_{H,-}}},\quad
\frac1{2\sqrt{\lambda_{H^2,+}}},\quad
\frac1{2\sqrt{\lambda_{H^2,-}}}.
\]

This proves EF24 as an exact finite-parameter formula. Sorting these four positive values and multiplying the largest \(j\) gives each exact inverse exterior norm. For full rank, the product is

\[
\frac1{16|D_d|^3}
=\frac1{1024|A_z|^6d^6|\kappa|^6},
\]

which agrees with EF22 and includes all metric factors through their exact cancellation in the determinant of an endomorphism with the same source and target metric.

For the endpoint limits, the isometric Euclidean representations using \(\Gamma_L(z)^{1/2}\) vary continuously, because the positive Grams converge to a positive Gram. The rank-three limit of \(d^2\Theta_L^{-1}\) supplies three growing values \(c_jd^{-2}\). The largest forward singular value tends to \(\eta>0\), so the remaining inverse value tends to \(\eta^{-1}\). Products give every limit in EF22. This uses both the inverse and forward limits; the inverse rank-three limit alone would not determine the fourth value.

## Review scope and provenance

The full EF1–25 body and the column-order correction in EF8 were read. The exact original source and local residue identities used in the review are FS4, FS13, FS21–25 and RD2, RD9–12, already read in the preceding independent review. The original ES marking and polynomial provenance remain the ES reader and Tao citation in the root source; this review introduces no alternative origin or attribution. No additional human paper was claimed as read.

The script checks generic polynomial/rational formulas before endpoint substitution, then checks the interpolation, the entire upper residue correction, the complete phase-dependent limiting matrix, and general complex Hermitian metric identities. It also reconstructs the original polynomial and verifies all four coordinates of its composition with the generic finite signed-root inverse, covering every branch in EF14. The additional finite-parameter spectral fixture is an exact rational interior family member with a dense complex Hermitian metric, evaluated through characteristic polynomials without numerical root tolerances. The written argument above proves the arbitrary-metric assertion; that fixture does not replace it.

These results describe the complete specified ES-to-formal-quartet family and its exact original receiver maps. They do not identify the formal endpoint roots with arithmetic zeta zeros, invert the persistent upper nilpotent trace block, or produce an order jump of the original linear conductor.
