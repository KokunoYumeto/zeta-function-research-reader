# Independent mathematical review of MR1–18

Date: 2026-09-20.

The complete source MARKED_RESIDUE_TRANSPORT_BODY.tex, MR1–18, was read and derived independently. The final reviewed SHA256 is 57c1ffbb9e035260c62d08550a6b70393117877ce204e311d1ce3fdd6c5dbf28. The earlier draft's row-break defects were reported and corrected by the root author; they made no change to the mathematics.

**Finding:** all MR1–18 identities, source/target metric comparisons, nilpotent flags, and pointwise singular/exterior bounds are correct. They close the receiver distinction between RS27 and RD19 by an exact isometry. No cross term or complex phase is lost.

The independent script review_marked_residue_transport.py records 59 passing exact checks in MARKED_RESIDUE_TRANSPORT_REVIEW_EXACT.json. Its generic checks include all phased powers, the full inverse remainder, and inequalities on the entire stated parameter interval. Dense exact fixtures check the block congruence and its cross terms; the general congruence proof below does not rely on those fixtures.

The separate extension MARKED_RESIDUE_UNIFORM_ERROR_BODY.tex, MR19–26, SHA256 697f8faffcc218f8ab4e8f4a6dd9782b946f7e14a886be03bee30870864966b2, proves a uniform error constant and explicitly separates and bounds the two finite singular values. Its constants and every entry bound are included in the independent certificate.

## 1. Full marked receiver and inverse

The coefficient substitution \(C_a\) maps a polynomial \(p(x)\) to \(p(x+a)\). Its \((i,j)\) entry is \(\binom ji a^{j-i}\), so \(C_aC_b=C_{a+b}\), \(C_a^{-1}=C_{-a}\), and \(\det C_a=1\).

The original finite-root coefficient map is

\[
Q_r=\operatorname{diag}(C_\kappa,C_\kappa)
\begin{pmatrix}Y&0\\\Psi E&\Psi O\end{pmatrix}.
\]

Replacing \(r\) by \(x+1/2\) applies \(C_{1/2}\) to both polynomial coefficients. Since \(\kappa+1/2=c_*\), one obtains

\[
Q_x=\operatorname{diag}(C_{1/2},C_{1/2})Q_r
=\operatorname{diag}(Z,Z)
\begin{pmatrix}K&0\\E&O\end{pmatrix},
\qquad Z=C_{c_*}\Psi,
\]

where \(Y=\Psi K\) is the existing fixed-frame identity. The inverse equations for an output \((p,q)\) are

\[
\alpha=K^{-1}Z^{-1}p,\qquad
\beta=O^{-1}(Z^{-1}q-E\alpha).
\]

Substituting either these equations in the forward map or the forward map in these equations gives the identity, proving both inverse products in MR2. Its determinant is \((\det Z)^2\det K\det O=(\det\Psi)^2\det K\det O\).

For the physical cubic receiver \(C_W f=f(S'-c_*)\), one has \(C_W C_{c_*}p=p\). Hence \(C_W Z=\Psi\), \(C_W ZK=Y\). Applying \(L^{-1}=T_A^{-1}\) gives \(C_U Z=\Phi\), \(C_U ZK=X\). These equations prove the two components of

\[
\mathcal J_U=\mathcal C_UQ_x,\qquad
\mathcal J_W=\mathcal C_WQ_x,\qquad
(T_A\oplus T_A)\mathcal J_U=\mathcal J_W.
\]

All coefficient maps and their inverses are therefore between the stated original spaces; the marked quartet remains fixed while \(w\) varies.

## 2. The metric identity retains every mixed entry

Let \(G_{U,x}\) be the actual source Gram from RS24 in the independent cubic receiver. Because \(C_UZ=\Phi\),

\[
Z^*G_{U,x}Z=\Phi^*\langle\, ,\,\rangle_U\Phi=G_U,
\qquad K^*G_UK=G_X.
\]

Multiplying the complete block matrices gives

\[
Q_x^*\operatorname{diag}(G_{U,x},G_{U,x})Q_x
=
\begin{pmatrix}
G_X+E^*G_UE&E^*G_UO\\
O^*G_UE&O^*G_UO
\end{pmatrix}.
\]

This equals the original marked source Gram from RW19. In particular the off-diagonal entries are not zero by assumption. The same multiplication, with the target identities \(C_W Z=\Psi\), \(C_W ZK=Y\), gives the target formula in MR4.

For any invertible \(Q\), set \(H=Q^*G_8Q\), \(A_Q=Q^{-1}AQ\). Then

\[
\begin{aligned}
H^{-1}A_Q^*HA_Q
&=Q^{-1}G_8^{-1}Q^{-*}
 Q^*A^*Q^{-*}Q^*G_8Q Q^{-1}AQ\\
&=Q^{-1}G_8^{-1}A^*G_8AQ.
\end{aligned}
\]

Thus the squared singular-value operators are similar. Each is itself similar, via the positive square root of its metric, to its Hermitian positive semidefinite adjoint product. This proves equality of all singular values, including multiplicities. Exterior norms are products of the largest singular values in orthonormal wedge bases, so they are equal as well. This proves MR6–7 for every parameter \(w>0\), not only in the limit.

## 3. Phase-sensitive powers and exact flags

Put \(V=\operatorname{span}(v_1,v_2)\), with

\[
v_1=(g,0,1,0)^{\mathsf T},\qquad
v_2=(0,g,0,1)^{\mathsf T}.
\]

The columns of \(N\) are \(v_1,v_2,-gv_1,-gv_2\). They give rank two and image \(V\). Since \(N^2=0\), the kernel is also \(V\). The invertible matrix \(X_0\) commutes with \(N\), so \(H_0=-2X_0N\) has the same image and kernel. Moreover \(H_0N=NH_0=H_0^2=0\).

Set

\[
\mathscr L=c
\begin{pmatrix}
0&H_0/(32g^2)\\
(gI+N)/(32g^3)&0
\end{pmatrix},
\qquad c=(1+i)/\sqrt2.
\]

Since \(H_0(gI+N)=gH_0=(gI+N)H_0\),

\[
\mathscr L^2=\frac{c^2}{2^{10}g^4}\operatorname{diag}(H_0,H_0).
\]

Multiplying once more gives

\[
\mathscr L^3=\frac{c^3}{2^{15}g^6}
\begin{pmatrix}0&0\\H_0&0\end{pmatrix}.
\]

The original critical multiplier is

\[
\Theta_0=\frac2c\begin{pmatrix}0&0\\H_0&0\end{pmatrix}.
\]

Because \(c^4=-1\), it follows that
\(\mathscr L^3=-\Theta_0/(2^{16}g^6)\). A fourth multiplication vanishes. This verifies the sign and all powers of \(g\) in MR9.

The matrix \(gI+N\) has inverse \(g^{-1}I-g^{-2}N\). Reading the two parity components therefore gives

\[
\begin{array}{c|c|c}
j&\operatorname{im}\mathscr L^j&\ker\mathscr L^j\\\hline
1&V\oplus\mathbb C^4&0\oplus V\\
2&V\oplus V&V\oplus V\\
3&0\oplus V&V\oplus\mathbb C^4\\
4&0&\mathbb C^4\oplus\mathbb C^4.
\end{array}
\]

The ranks are \(6,4,2,0\), as claimed. These are algebraic flags; no unproved orthogonality of their subspaces is asserted.

For \(u_j=(e_j,0)\), direct multiplication gives \(H_0e_0=-2v_2\), \(H_0e_1=2gv_1\). The last nonzero vectors \(\mathscr L^3u_0,\mathscr L^3u_1\) are independent. Applying \(\mathscr L^3,\mathscr L^2,\mathscr L\) successively to any relation between the eight chain vectors forces the coefficients at each level to vanish. This proves that MR11 gives two full chains.

An additional exact determinant check fixes their scaling: in the column order used after MR11,

\[
\det(\mathscr L^3u_0,\mathscr L^2u_0,\mathscr Lu_0,u_0,
     \mathscr L^3u_1,\mathscr L^2u_1,\mathscr Lu_1,u_1)
=-\frac1{2^{56}g^{22}}.
\]

The independent checker also verifies that the matrix of \(\mathscr L\) in this unchanged chain basis has two length-four nilpotent blocks. This determinant is a verification of the displayed vectors, not a change to their phases.

Conjugation by \(Q_x\) proves every image and kernel identity in MR12. The identity \(\mathcal J_UQ_x^{-1}=\mathcal C_U\) then gives their physical return. For any collection of chain vectors, its Gram equality follows immediately by inserting the proved congruence of section 2.

## 4. Exact remainder

The proposed inverse \(X_w^{-1}\) in MR15 passes both matrix products. Write \(a=g-w\), \(p=(g+w)^2\). The upper-right block of the inverse multiplier before its phase is

\[
\frac{X_w+aX_w^{-1}}{16gw},
\]

and its lower-left block is \(-X_w^{-2}/(32gw)\). Subtracting the two residue blocks \(H_0/(32g^2w)\) and \((gI+N)/(32g^3w)\) gives exactly the six nonzero entries of \(A_w\) and four nonzero entries of \(B_w\) in MR14.

The generic symbolic check verifies the entire eight-by-eight identity

\[
\Theta_w^{-1}-\mathscr L/w
=c\begin{pmatrix}0&A_w\\B_w&0\end{pmatrix}
\]

over the rational function field with the unchanged complex constant \(c\). Thus the result includes all entries and is not inferred from a determinant. Its denominators are powers of \(g\) and \(g+w\); both remain nonzero at \(w=0\), since \(g>0\).

## 5. Pointwise singular and exterior bounds

For a four-dimensional block \(A\), its squared Hilbert–Schmidt norm in \(G_0\) is \(\operatorname{tr}(G_0^{-1}A^*G_0A)\). Orthogonality of the two independent cubic summands makes the squared Hilbert–Schmidt norm of the eight-dimensional off-diagonal block the sum of the two such traces. This proves the formula for \(e(w)\). The original forward multiplier has blocks \(2H_w^2/c\) and \(2H_w/c\), so the formula for \(b(w)\) follows with both factors 4.

For each index, the singular-value variational formula and the triangle inequality give

\[
|\sigma_j(A)-\sigma_j(B)|\le\|A-B\|.
\]

Apply this to \(w\Theta_w^{-1}\) and \(\mathscr L\). Their difference has operator norm at most \(we(w)\). The first six singular values of \(\mathscr L\) are \(c_1,\ldots,c_6\); the last two are zero. This proves all upper bounds and the first six lower bounds in MR17.

The smallest singular value of the inverse equals \(1/\sigma_1(\Theta_w)\). Since \(\sigma_1(\Theta_w)\le b(w)\), both its seventh and eighth singular values are at least \(1/b(w)\). These are the remaining lower bounds in MR17. The norm \(b(w)\) is strictly positive because \(\Theta_w\) is invertible for \(w>0\).

All factors in the products in MR18 are nonnegative. Multiplying the first \(r\) singular-value intervals gives the bounds for \(r\le6\). Multiplying the first six and then one or two of the last intervals gives the bounds for \(r=7,8\). The full determinant supplies the exact rank-eight identity. This verifies MR18 on the entire stated interval \(w>0\), even where a truncated lower factor is zero.

## 6. Uniform extension and exact scope

MR19–26 are proved in the separate extension source. On \(0<w\le g\), their uniform remainder bound is

\[
\|\Theta_w^{-1}-\mathscr L/w\|
\le \sqrt{\operatorname{tr}G_0\operatorname{tr}G_0^{-1}}\,
\sqrt{\frac9{256}+\frac3{256g^2}+\frac1{4g^4}
             +\frac3{16g^6}+\frac9{512g^8}}.
\]

The exact entry inequalities used for this bound and the bound on \((H_w-H_0)/w\) were independently certified. Clearing their positive denominators after substituting \(g=w+u\), \(u\ge0\), leaves polynomials in \(u,w\) with nonnegative coefficients. The endpoint \(u=0\) is included by continuity; this check only proves the stated inequalities and changes no original operator or coordinate.

The extension's explicit threshold ensures that six singular values exceed \(1/\eta_2\), while the two specified reciprocal values are at most \(1/\eta_2\). This proves their ordered indices. The reciprocal estimate then gives the exact linear error constants in MR25. Multiplication gives the uniformly positive bounds MR26.

These calculations concern the completed trace-to-residue multiplier and its exact original source and marked returns. The original conductor remains the same fixed isomorphism. No new assertion about its vanishing order or an arithmetic endpoint is introduced by this review.
