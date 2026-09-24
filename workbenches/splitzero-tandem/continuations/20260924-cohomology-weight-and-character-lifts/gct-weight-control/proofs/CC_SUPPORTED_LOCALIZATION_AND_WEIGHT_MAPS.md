# The supported localization maps of the original-zeta sheaf

Complete derivation, 24 September 2026. Proof locators CSL0–CSL10.

## CSL0. Construction stage and sources

The supporting datum is \(\tau\langle Z_1;\text{no }Z_2\rangle\). Its comparison with the unique generic point uses the complete chart reconstruction CG1–CG3, after the complete arithmetic has been recovered. All vector spaces, sums, scalar factors and quotient operations in this note occur in the coefficient sheaf over that support. None is an arithmetic operation on \(\tau\), a metric on it, or a definition of the earlier counting process. The two chart summation maps remain separately labelled.

The corrected argument and relevant verbatim passages were recalled before this calculation; PC04 in the private prerequisite ledger records that reading. In particular, the retracted addition at \(\tau\) is not used, and fixed support is not substituted for trivial action on its stalk.

The original author source is Alain Connes and Caterina Consani, *Schemes over \(\mathbb F_1\) and zeta functions*, [arXiv:0903.2024v3](https://arxiv.org/abs/0903.2024v3), §5. Its unchanged author file is `sources/CC_0903_2024_v3/author_source/announc3.tex`. Root read lines1376–1667 in full, including the sheaf, both restriction maps, the Fourier proof and the localization sequence. The source archive is retained unchanged. The spectral comparison below uses the complete construction in `CC_SHEAF_ORIGINAL_ZETA_COHOMOLOGY.md` and S1–S7 in `GLOBAL_MELLIN_SYNTHESIS.md`; the former proves the exact finite-unit sector of the adelic sheaf and the latter its closed summation image. These are named derivations, not original-author claims.

The weight comparison is with Pierre Deligne, *La conjecture de Weil. II*, [§3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/), as reconstructed in DC1–DC8 of `DELIGNE_INVARIANT_CYCLE_QUOTIENT.md`. The present calculation gives the actual supported-cohomology maps of the CC coefficient sheaf. It does not replace Deligne's inertia and geometric duality terms with similarly named analytic spaces.

## CSL1. Exact sheaf and unshifted actions

Let \(X=\{x_+,\eta,x_-\}\), with opens
\[
\varnothing,\quad U=\{\eta\},\quad
U_+=\{x_+,\eta\},\quad U_-=\{x_-,\eta\},\quad X.
\tag{CSL1.1}
\]
The notation \(x_+,x_-\) distinguishes the two closed chart points from the integer zero and from \(\tau\). In the author's notation these are \(0,\infty\); that is a chart notation, not an equation identifying \(\tau\) with zero.

There is an exact topological comparison with the later signed CC construction: send its points \((+,\eta,-)\) to \((x_+,\eta,x_-)\). The open sets of CC.tex lines499–505 are exactly (CSL1.1), so this map and its inverse are continuous. The underlying map of the full involution exchanges the two closed points and fixes the generic point. Therefore this homeomorphism intertwines the underlying involutions, and pullback transports the coefficient sheaf below to that space, with its stalks and all cohomology unchanged. The original signed stalk formulas remain \(\alpha^*T=\epsilon T^{-1}\) and \(\alpha^*J=\epsilon J\), with \(J^2=\epsilon\). The topological pullback is not asserted to be a comparison of the two structure sheaves or an action of those full signed stalk generators on the new coefficient sheaf. Its domain is precisely the underlying topological space, which is sufficient for the sheaf and support calculations being made here.

Let \(S\) be the even real Schwartz space with complex coefficients and with both moments zero:
\[
S=\{f\in\mathcal S(\mathbb R):f(-v)=f(v),\ f(0)=0,\ \int_{\mathbb R}f(v)\,dv=0\}.
\tag{CSL1.2}
\]
Set \(V_+=S\oplus\mathbb C^2\), \(V_-=S\oplus\mathbb C^2\). Denote the additional coordinates by \((c_0,c_1)\), retaining the value and integral labels. The overlap is
\[
A=\{a\in C^\infty(\mathbb R_{>0}):
\sup_{u>0}(u^N+u^{-N})|(u\partial_u)^j a(u)|<\infty
\text{ for every }N,j\ge0\}.
\tag{CSL1.3}
\]
The exact comparison with S1's centred source is the topological isomorphism
\[
\mathcal T:\mathcal A\longrightarrow A,\qquad
(\mathcal T k)(u)=2u^{-1/2}k(u),\qquad
\mathcal T^{-1}a(u)=\tfrac12u^{1/2}a(u).
\tag{CSL1.4}
\]
Multiplication by either displayed power shifts each seminorm by at most one integer weight; Leibniz's formula gives a finite sum of derivative seminorms. Thus both maps are continuous and preserve exactly the stated spaces.

Define
\[
\Sigma f(u)=2\sum_{n\ge1}f(nu),\qquad
Ra(u)=u^{-1}a(u^{-1}),\qquad
r_+(f,c_0,c_1)=\Sigma f,\quad r_-(h,d_0,d_1)=R\Sigma h.
\tag{CSL1.5}
\]
These are the original CC restriction maps in the finite-unit sector. The factor2 comes from both signs in \(\mathbb Q^\times\); it is not discarded. Poisson summation gives, for general even Schwartz \(h\),
\[
\Sigma\widehat h(u)
=u^{-1}\Sigma h(u^{-1})+u^{-1}h(0)-\int_{\mathbb R}h(v)\,dv.
\tag{CSL1.6}
\]
Here \(\widehat h(t)=\int h(v)e^{-2\pi ivt}\,dv\). Therefore on \(S\)
\[
R^2=1,\qquad \widehat{\widehat h}=h,\qquad
R\Sigma h=\Sigma\widehat h.
\tag{CSL1.7}
\]
The two omitted terms in the restricted identity are zero by the two specified moment conditions; their formula and their independent endpoint coordinates are retained. The convergence and continuity of \(\Sigma:S\to A\) follow by Schwartz summation at infinity and (CSL1.6) at zero, with logarithmic derivatives. Its injectivity also has an elementary proof: for \(\Re s>1\),
\[
\int_0^\infty\Sigma f(u)u^s\frac{du}{u}
=2\zeta(s)\int_0^\infty f(v)v^s\frac{dv}{v}.
\tag{CSL1.8}
\]
If \(\Sigma f=0\), the nonvanishing Euler product on this half-plane makes the second Mellin transform zero there. Fourier uniqueness on any vertical line in that half-plane gives \(f=0\) on the positive axis, and evenness gives \(f=0\) on \(\mathbb R\).

For \(a>0\), retain the unshifted actions
\[
\begin{aligned}
T_a b(u)&=b(u/a),\\
\rho_+(a)(f,c_0,c_1)&=(f(\cdot/a),c_0,ac_1),\\
\rho_-(a)(h,d_0,d_1)&=(a h(a\cdot),ad_0,d_1).
\end{aligned}
\tag{CSL1.9}
\]
Direct substitution shows \(r_\pm\rho_\pm(a)=T_a r_\pm\) and
\[
T_aR=aRT_{a^{-1}},\qquad
\widehat{a h(a\cdot)}(v)=\widehat h(v/a).
\tag{CSL1.10}
\]
Thus these are actions on the specified sheaf. No \(a^{-1/2}\) character has been used to replace them.

## CSL2. The whole Cech complex and its topology

Each of \(U_+,U_-,U\) has a point whose only neighbourhood in that open is the whole open. Sections there are the corresponding stalk functor, hence exact. These opens are acyclic for every sheaf of vector spaces. The Cech complex for this two-open cover therefore computes ordinary sheaf cohomology:
\[
D^0=V_+\oplus V_-,\qquad D^1=A,\qquad
d(v_+,v_-)=r_+v_+-r_-v_-.
\tag{CSL2.1}
\]
This sign convention is fixed below. Let
\[
J=\Sigma(S),\qquad C=\overline J^{\,A},\qquad
Q_{\rm alg}=A/J,\qquad Q_H=A/C,\qquad N=C/J.
\tag{CSL2.2}
\]
By (CSL1.7), \(r_+(V_+)=r_-(V_-)=J\), so the sum of the chart images is exactly \(J\), without a doubling of its arithmetic spectrum. Hence
\[
H^1(X,\Omega)=Q_{\rm alg},\qquad H^j(X,\Omega)=0\ (j\ge2),
\quad 0\longrightarrow N\longrightarrow Q_{\rm alg}
\longrightarrow Q_H\longrightarrow0.
\tag{CSL2.3}
\]
The last arrow is precisely Hausdorffization for the quotient locally convex topology. The construction of this sequence does not presuppose \(J=C\). CSL10 now proves that equality by applying the complete inverse-source theorem.

Injectivity of \(\Sigma\) and (CSL1.7) give the full zeroth cohomology:
\[
H^0(X,\Omega)=
\{((\widehat h,c_0,c_1),(h,d_0,d_1)):
h\in S,\ c_0,c_1,d_0,d_1\in\mathbb C\}.
\tag{CSL2.4}
\]
In particular, all four labelled endpoint lines remain in the kernel. The restriction to \(U\) has image \(J\), and its kernel consists exactly of these four lines.

## CSL3. One closed support and an actual lifting map

Let \(Y_+=\{x_+\}\). Its complement is \(U_-\). The complex with support on \(Y_+\) is represented by
\[
K_+=[V_+\xrightarrow{r_+}A]
\quad\text{in degrees }0,1.
\tag{CSL3.1}
\]
To prove this, use the localization cone of the chain map
\(D\to V_-[0]\), \((v_+,v_-)\mapsto v_-\). Its degree0 is \(V_+\oplus V_-\), its degree1 is \(A\oplus V_-\), and its differential is
\((v_+,v_-)\mapsto(r_+v_+-r_-v_-,v_-)\).
Changing degree1 coordinates to \((b+r_-v_-,v_-)\) splits it as (CSL3.1) plus the contractible identity complex on \(V_-\). This explicitly proves the claimed quasi-isomorphism.

Consequently
\[
H^0_{Y_+}(X,\Omega)=\mathbb C\oplus\mathbb C[1],\qquad
H^1_{Y_+}(X,\Omega)=Q_{\rm alg},\qquad H^j_{Y_+}=0\ (j\ge2),
\tag{CSL3.2}
\]
where \(\mathbb C[1]\) means the character \(a\mapsto a\), not a cohomological shift. The map \(K_+\to D\) is \(v\mapsto(v,0)\) in degree0 and the identity on \(A\) in degree1. It induces the identity
\[
H^1_{Y_+}(X,\Omega)\xrightarrow{\sim}H^1(X,\Omega).
\tag{CSL3.3}
\]

The connecting map from \(H^0(U_-,\Omega)\) into this supported \(H^1\) is zero. This is proved by the continuous equivariant lift
\[
\ell_-:V_-\longrightarrow H^0(X,\Omega),\qquad
(h,d_0,d_1)\longmapsto
((\widehat h,0,0),(h,d_0,d_1)).
\tag{CSL3.4}
\]
Its restriction to \(U_-\) is the identity. Equation (CSL1.10) proves equivariance, and the Fourier transform is continuous in the Schwartz topology. Thus the exact lifting is actually constructed, including the endpoint data. Its mechanism is Poisson summation and Fourier transform; it is not presented as a new proof of weight separation.

For \(Y_-=\{x_-\}\), the analogous supported complex is \([V_-\xrightarrow{r_-}A]\). Under the fixed sign of (CSL2.1), its map to \(D\) is \(v\mapsto(0,v)\) in degree0 and multiplication by \(-1\) in degree1. Both support choices are thereby retained with their correct sign.

## CSL4. Both closed supports and the diagonal/difference sequence

Put \(Y=\{x_+,x_-\}\), whose complement is the generic open \(U\). A complex representing \(R\Gamma_Y(X,\Omega)\) is
\[
K^0=V_+\oplus V_-,\quad K^1=A\oplus A,\quad
d_K(v_+,v_-)=(r_+v_+,r_-v_-).
\tag{CSL4.1}
\]
Here is an explicit localization-cone proof. Represent the restriction to \(U\) by the chain map \(D\to A[0]\) which is \(r_+\) on the first summand of \(D^0\). Choosing \(r_-\) instead gives a homotopic map: their difference is the differential (CSL2.1). The shifted cone has differential
\[
(v_+,v_-)\longmapsto
(r_+v_+-r_-v_-,\ r_+v_+)
\quad\text{in }A\oplus A.
\tag{CSL4.2}
\]
The invertible degree1 change \((k,b)\mapsto(b,b-k)\), with inverse \((b_+,b_-)\mapsto(b_+-b_-,b_+)\), gives (CSL4.1). Its map to \(D\) is the identity in degree0 and
\((b_+,b_-)\mapsto b_+-b_-\) in degree1. The boundary from \(A\) into supported degree1 is \(b\mapsto(b,b)\).

It follows, with all maps specified, that the complete nonzero portion of the localization sequence is
\[
0\to\mathbb C^4\to H^0(X,\Omega)\xrightarrow{\Sigma\widehat{\phantom h}}A
\xrightarrow{\beta}Q_{\rm alg}\oplus Q_{\rm alg}
\xrightarrow{\pi}Q_{\rm alg}\to0,
\tag{CSL4.3}
\]
where the middle map on the graph (CSL2.4) sends it to \(\Sigma\widehat h\), and
\[
\beta(b)=([b],[b]),\qquad \pi([b_+],[b_-])=[b_+-b_-].
\tag{CSL4.4}
\]
Exactness can also be checked without derived notation. The kernel of \(\beta\) is \(J\). If \([b_+]=[b_-]\), the pair is diagonal and in its image. Every class is the image of \(([b],0)\), and all earlier kernels have already been computed in (CSL2.4). This proves each arrow of (CSL4.3).

After factoring out \(J\) in the middle, one obtains
\[
0\longrightarrow Q_{\rm alg}\xrightarrow{q\mapsto(q,q)}
Q_{\rm alg}\oplus Q_{\rm alg}
\xrightarrow{(q_+,q_-)\mapsto q_+-q_-}Q_{\rm alg}
\longrightarrow0.
\tag{CSL4.5}
\]
This row is split by \(q\mapsto(q,0)\). Hausdorffization here gives exactly the same row with \(Q_H\) in all three places: this follows directly from the explicit maps and the closed subspaces \(C\), \(C\oplus C\), rather than from a general exactness claim about Hausdorffization.

## CSL5. The mirror sign on cochains and its retained action

The mirror exchanges \(x_+,x_-\) and fixes \(\eta\), since the generic point is unique. A carried exchanged \(Z_2\)-label at that fixed point would have to equal its flip, which is impossible for either of its two states. This derives the relevant absence of that label at \(\tau\langle Z_1;\text{no }Z_2\rangle\). It does not make the stalk involution the identity.

On the sheaf the mirror swaps the two chart sections and uses \(R\) on the overlap. The induced map on the ordered Cech complex is
\[
w_D^0(v_+,v_-)=(v_-,v_+),\qquad w_D^1(b)=-Rb.
\tag{CSL5.1}
\]
Indeed,
\(d(v_-,v_+)=\Sigma h-R\Sigma f=-R(\Sigma f-R\Sigma h)\).
The minus sign is the orientation sign from reversing the ordered cover; omitting it would not give a chain map. This does not change the author's assertion of spectral symmetry, but it fixes the actual action under our displayed identification of \(H^1\).

On (CSL4.1) the induced map is
\[
w_K^0(v_+,v_-)=(v_-,v_+),\qquad
w_K^1(b_+,b_-)=(Rb_-,Rb_+).
\tag{CSL5.2}
\]
The identity \(Rr_-=r_+\), with the two chart labels exchanged, verifies the chain-map identity. Consequently (CSL4.5) is equivariant with mirror \(R\) on its first term, \((q_+,q_-)\mapsto(Rq_-,Rq_+)\) on its middle term, and \(-R\) on its last term. Its continuous arithmetic- and mirror-equivariant section is
\[
s(q)=\tfrac12(q,-q).
\tag{CSL5.3}
\]
The calculation is exact: \(\pi s(q)=q\), while
\(w_Ks(q)=\tfrac12(-Rq,Rq)=s(-Rq)\).
The scalar \(1/2\) is in the already constructed complex coefficient field. It has no interpretation as halving \(\tau\).

## CSL6. Exact comparison with the original-zeta receiver

Use the raw Mellin map
\[
\mathcal M_0b(s)=\int_0^\infty b(u)u^s\frac{du}{u}.
\tag{CSL6.1}
\]
From (CSL1.4) and S1,
\[
\mathcal M_0\mathcal T=2\mathcal M,\qquad
\mathcal M_0T_a=a^s\mathcal M_0,\qquad
\mathcal M_0R b(s)=\mathcal M_0b(1-s).
\tag{CSL6.2}
\]
All integrals converge absolutely in every fixed strip; the inverse is
\[
b(e^x)=\frac{e^{-cx}}{2\pi}\int_{\mathbb R}
(\mathcal M_0b)(c+it)e^{-itx}\,dt
\quad(c\in\mathbb R).
\tag{CSL6.3}
\]
The estimates and contour shifts are those of S1 with the exact change (CSL6.2). Thus \(\mathcal M_0\) is a topological isomorphism \(A\to\mathcal B\).

Let \(\mathcal I\) be the closed ideal of full-order vanishing at every original nontrivial zero, with its original multiplicity. S5 gives \(\mathcal M_0 C=\mathcal I\), so
\[
Q_H\xrightarrow{\sim}\mathcal Q=\mathcal B/\mathcal I,
\qquad[b]\longmapsto[\mathcal M_0b].
\tag{CSL6.4}
\]
Under this exact isomorphism, the entire supported row (CSL4.5) is the diagonal/difference row of the actual \(\mathcal Q\), with the same full multiplicities and quotient topology. It is not an unrestricted product of jets or an algebraic direct sum.

For the retained source function
\[
f_0(v)=\frac\pi2v^2(2\pi v^2-3)e^{-\pi v^2},
\]
the complete auxiliary transform is
\[
\mathcal M_0\Sigma f_0(s)
=\frac{s(s-1)}4\pi^{-s/2}\Gamma(s/2)\zeta(s)=2F_0(s).
\tag{CSL6.5}
\]
Its endpoint values are \(1/4\) at both0 and1. At each negative even integer, with \(r\ge1\), its retained cancellation value is
\[
(2F_0)(-2r)
=\frac{r(2r+1)(-1)^r\pi^r}{r!}\zeta'(-2r)
=\frac{(1+2r)(2r)}4\pi^{-(1+2r)/2}
\Gamma((1+2r)/2)\zeta(1+2r)\ne0.
\tag{CSL6.6}
\]
These are values of the transform; the original \(\zeta\) still has its pole at1 and trivial zeros at \(-2r\). Its unit and prime-power repetitions remain in
\[
\zeta(s)=1+\sum_{n\ge2}n^{-s}
=\prod_p(1-p^{-s})^{-1},\qquad
-\frac{\zeta'(s)}{\zeta(s)}
=\sum_p\sum_{m\ge1}(\log p)p^{-ms}
\quad(\Re s>1).
\tag{CSL6.7}
\]
All these arithmetic labels belong to the recovered complete arithmetic, not to the primitive support.

## CSL7. What the computed action says about weights

On an actual original-zero block at \(\rho\) of multiplicity \(m_\rho\), multiplication by \(s\) is \(\rho I+N_\rho\), where \(N_\rho^{m_\rho}=0\). Consequently the unshifted action in every \(Q_H\) term above is
\[
T_a=a^\rho\sum_{j=0}^{m_\rho-1}
\frac{(\log a)^j}{j!}N_\rho^j.
\tag{CSL7.1}
\]
It follows from the original strip \(0<\Re\rho<1\), for \(a>1\), that its character weight \(2\log_a|a^\rho|\) lies in \((0,2)\). The kernel, middle terms and quotient of (CSL4.5) have these same character weights. The diagonal and difference are explicit nonzero equivariant maps; they are not forced to vanish by separated weights.

The endpoint kernel has the separately computed weights. In \(V_+\), value has character1 and integral has character \(a\); in \(V_-\), value has character \(a\) and integral has character1. Thus the four endpoint lines have weights \(0,2,2,0\), in that order. This follows from (CSL1.9), not from a weight assigned to a support point.

This weight computation states the exact analytic character action. It does not assert that these spaces are finite-dimensional \(\ell\)-adic cohomology, that their characters are algebraic Weil numbers, or that an arithmetic weight filtration has been imported without a comparison.

## CSL8. The precise comparison with Deligne's localization cross

In Deligne's theorem, the top obstruction group and the inertia term are
\[
O_i=H^{2N-i-1}(X_s,E)^\vee(-N),\qquad
K_i=H^{i-1}(X_{\bar\eta},E)_I(-1),
\tag{CSL8.1}
\]
and the obstruction to specialization is
\[
\operatorname{im}(\partial_i)/\partial_i j_i(K_i).
\tag{CSL8.2}
\]
DC3–DC6 derives the Tate factors from tame inertia and the dualizing complex of the smooth total space. Those operations give the weights \(\le i\) on the classes and \(\ge i+1\) on the obstruction receiver. They are additional geometric maps, not consequences of the name “localization.”

For the CC sheaf calculated here, the exact specialization-like map actually constructed by removing one closed point is (CSL3.3). It is an isomorphism, with inverse the identity on the displayed quotient. The restriction lift (CSL3.4) is explicit. For removal of both closed points, the exact receiver and its maps are (CSL4.3)–(CSL4.5), and the equivariant section is (CSL5.3). These are genuine applications of localization to this coefficient sheaf, and every map has now been calculated on its source.

In particular, neither supported calculation produces an uncomputed Tate shift: the character identity (CSL7.1) determines its action. The constructed comparison to the Mellin receiver is (CSL6.4), not an identification with (CSL8.1). A geometric extension carrying an additional normal direction can have a different dualizing or inertia term; the preceding calculation makes no claim against such an extension. Its exact current contribution is the original-zeta cohomological receiver, its support maps, its Fourier lift, and its mirror-equivariant split supported row. It does not certify completion of the requested Deligne weight-lifting application.

## CSL9. All comparison arrows and retained information

The following commuting formulas describe the full receiver used here:
\[
\begin{aligned}
\mathcal M_0\circ r_+&=2\,\mathcal M\circ\mathcal E,\\
\mathcal M_0\circ r_-&=2\,(F(s)\mapsto F(1-s))\circ\mathcal M\circ\mathcal E,\\
\overline{\mathcal M_0}^{\oplus2}\circ\beta
&=\operatorname{diag}\circ\overline{\mathcal M_0},\\
\overline{\mathcal M_0}\circ\pi
&=\operatorname{diff}\circ\overline{\mathcal M_0}^{\oplus2},\\
\overline{\mathcal M_0}^{\oplus2}\circ s(q)
&=\tfrac12(\overline{\mathcal M_0}q,-\overline{\mathcal M_0}q).
\end{aligned}
\tag{CSL9.1}
\]
The first two formulas act on the Schwartz component and send each explicitly retained endpoint summand to zero. The last three use the quotient of \(\beta\) by its kernel \(J\), followed by the stated Hausdorffization. Hence their domains and codomains are exactly the displayed \(Q_H\) spaces. Every original-zero jet survives in \(\mathcal Q\); CSL10 calculates the separately retained closure difference as \(N=C/J=0\). The support remains \(\tau\langle Z_1;\text{no }Z_2\rangle\), while the full coefficient action, both charts and their orientation sign remain visible.


## CSL10. Exact image, strict maps, and the calculated comparison kernel

The complete proof SSI0–SSI9 in `EXACT_SCHWARTZ_SUMMATION_IMAGE.md` constructs a continuous inverse to
\[
\mathcal M_0\Sigma:S\xrightarrow{\sim}\mathcal I.
\tag{CSL10.1}
\]
Its independently checked proof ESI0–ESI9 is retained in `EXACT_SCHWARTZ_IMAGE_INDEPENDENT_CHECK.md`. With \(F=\mathcal M_0b\), the inverse has the full formula
\[
f_F(x)=\frac1{2\pi}\int_{\mathbb R}
\frac{F(2+it)}{2\zeta(2+it)}x^{-2-it}\,dt\quad(x>0).
\tag{CSL10.2}
\]
The pole-cleared strip estimate, contour residues and smooth even extension in SSI4–SSI6 prove \(f_F\in S\), continuity in all Schwartz seminorms, and \(\Sigma f_F=b\). Its even derivatives at zero are exactly \((2r)!F(-2r)/(2\zeta'(-2r))\); both vanishing moments and every nontrivial multiplicity are proved there. Thus the inverse does not discard the trivial-zero data of the original function.

It follows, on the actual spaces already used in CSL2, that
\[
J=\mathcal M_0^{-1}\mathcal I=C,\qquad N=0,
\qquad Q_{\mathrm{alg}}\xrightarrow{\sim}Q_H\xrightarrow{\sim}\mathcal Q.
\tag{CSL10.3}
\]
Each map is a homeomorphism with the quotient topologies. Both chart restrictions are strict onto \(J\): the plus chart has right inverse \(b\mapsto(\Sigma^{-1}b,0,0)\), and the minus chart has right inverse \(b\mapsto(\widehat{\Sigma^{-1}b},0,0)\). Poisson summation proves the second identity. The Čech differential has right inverse from its image \(b\mapsto((\Sigma^{-1}b,0,0),0)\), so its image is closed and its ordinary first cohomology is already Hausdorff.

Therefore the one-point localization maps and the two-point diagonal/difference row of CSL3–CSL5 are maps on the actual original-zero quotient without any extra closure operation. Their signs, common arithmetic action and section \(q\mapsto\tfrac12(q,-q)\) are unchanged. This is the vanishing of the exact comparison kernel \(N\), not a deduction that the source has pure weight or that the independently calculated localization row is Deligne's cross.
