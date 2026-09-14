# Exact Toda dependency review for LC1–LC3

Review date: 13 September 2026. The independently delegated reviewer read LC1–LC3 completely, read the surrounding LC chapter, and checked the actual cumulative Toda chapter TVB.22–TVB.34 and TVB.37–TVB.38, including its first-degree conventions. The source definitions TVB.7 and TVB.12–TVB.14, the endpoint continuation TVB.38a–TVB.38c, and the explicit empty-quotient paragraph were also read. This review does not claim an independent audit of LC4–LC12 or of the period determinant. No primary TeX, mathematical checker, test, Lean process, or PDF build was changed or run.

## Pinned sources

| Source | SHA-256 read |
|---|---|
| work/period_laplacian_control_bridge_20260913.tex | 0799f1fbc266b25e11fec456c1d66618bdae365fe17060c9f69393a9b11c900c |
| output/split_zero_rh_tandem_2026-09-12/tex/toda_cv_exact_bridge.tex | c9629b11d4b4a173dd52bdf75fafb437883a85aba05e598c637f390386d45512 |

Verdict: the mathematical equality in LC3 is correct for the original reflection-stable source at every admitted degree, including the first degree \(N=q-1\) and the scalar case \(q=1\). The phase, factor of two in the squared trace, determinant orientation, and factor \(\alpha_{N+1}=\omega_{N+1}/\omega_N\) all agree with the cumulative Toda source.

LC1 already explicitly assumes \(q\ge1\), so another \(q=0\) exclusion is unnecessary. For a self-contained statement of the boundary typing, the chapter should state \(N\in\mathbb Z\), \(N\ge q-1\), and define the finite source kernels down to the empty sum \(K_{-1}=0\). Then \(D_{q-2}=0\) is a proved consequence of rank, not a new positive-metric convention. In particular, no \(G_{q-2}\), \(K_{q-2}^{-1}\), or \(V_{q-2}\) is introduced. The complete derivation follows.

## 1. The original source, quotient, and admitted degree

Fix the original reflection-stable cyclic polynomial \(\chi\), monic of degree \(q\ge1\), and the quotient

\[
E=\mathbb C[S]/(\chi),
\qquad A=M_S:E\longrightarrow E,
\qquad c=k/2.
\]

The original source is observed at \(S=c+iu\), with its original positive real measure, at one of the admitted fixed real tilts of the Toda chapter. Let \(p_j(S)\) be its monic orthogonal polynomials and retain the complete squared norms

\[
\omega_j=\|p_j\|_\theta^2>0,\qquad
b_j=[p_j]_\chi\in E,\qquad j\ge0.
\]

At zero tilt \(\omega_0\) is the full original source mass; at tilt \(\theta\) the Toda chapter retains \(\omega_0=M_h(\theta)^k\). No factor is divided out.

Use the original ordered quotient coordinates \(1,S,\ldots,S^{q-1}\), and define, for every integer \(j\ge-1\),

\[
K_j=\sum_{r=0}^j\frac{b_rb_r^*}{\omega_r},
\qquad K_{-1}=0_{E^*\to E}.
\]

The second expression is the empty sum. It does not involve \(\omega_{-1}\). For \(0\le j<q\), the columns \(b_0,\ldots,b_j\) are linearly independent because their representatives are monic of respective degrees \(0,\ldots,j\). If their linear combination reduced to zero, its polynomial representative would have degree below \(q\) and be divisible by monic \(\chi\), forcing that polynomial and all its coefficients in the monic basis to vanish. Thus

\[
\operatorname{rank}K_j=j+1\quad(-1\le j\le q-1).
\]

Here the rank assertion at \(j=-1\) is zero. Adding further positive source columns preserves the full rank attained at \(j=q-1\). Therefore \(K_N>0\) exactly for \(N\ge q-1\).

For an admitted integer \(N\ge q-1\), put \(G=G_N=K_N^{-1}\) and \(D_j=\det K_j\). All determinants use the same \(q\)-dimensional original quotient coordinate space. In particular,

\[
D_N>0,\qquad D_{q-2}=0.
\]

For \(q=1\), this is the determinant of the one-dimensional zero matrix \(K_{-1}\), and is zero. It is not a zero-dimensional empty determinant.

The source quotient map and least-lift construction in TVB.7 and TVB.14 give precisely this kernel: in the source-orthogonal coordinates the positive source matrix is \(\operatorname{diag}(\omega_0,\ldots,\omega_N)\), and reduction has columns \(b_0,\ldots,b_N\). Thus its induced dual kernel is the displayed sum. Its inverse is the original minimum quotient metric.

## 2. The original control matrix and its phase

Retain

\[
W_0=A^*G+GA-kG,\qquad X_0=G^{-1}W_0,
\qquad
\epsilon_N=\|X_0\|_G.
\]

Since \(W_0^*=W_0\), direct multiplication gives

\[
X_0^{\dagger_G}
=G^{-1}X_0^*G
=G^{-1}W_0=X_0.
\]

Thus \(X_0\) is self-adjoint for the original positive metric. The coefficient map \(v\mapsto G^{1/2}v\) is an explicitly specified isometry from that metric to the ordinary Hermitian coefficient space. Its transported operator is

\[
H=G^{1/2}X_0G^{-1/2}=G^{-1/2}W_0G^{-1/2}.
\]

It is Hermitian, and its ordinary operator norm equals \(\epsilon_N\). This proves the equality of the norm used in LC2 and the Hermitian relative radius calculated in TVB.27.

To verify the matrix itself, the original source recurrence is

\[
Sp_j=p_{j+1}+(c+i\beta_j^{\mathrm{rec}})p_j
-\alpha_jp_{j-1},
\qquad
\beta_j^{\mathrm{rec}}\in\mathbb R,\qquad
\alpha_j=\omega_j/\omega_{j-1}>0\quad(j\ge1).
\]

At \(j=0\), the last term is zero through \(p_{-1}=0\), without evaluating \(\omega_{-1}\). This is the transport of the real monic three-term recurrence through \(S=c+iu\); the negative sign is \(i^2=-1\).

Apply reduction, insert the recurrence in \(AK_N+K_NA^*-kK_N\), and use \(2c=k\). The diagonal imaginary recurrence coefficients cancel against their adjoints. For \(j\ge1\), the coefficient of each backward off-diagonal term is \(\alpha_j/\omega_j=1/\omega_{j-1}\), cancelling the preceding forward term. Only the top pair remains:

\[
AK_N+K_NA^*-kK_N
=\frac{b_{N+1}b_N^*+b_Nb_{N+1}^*}{\omega_N}.
\]

Multiplying by \(G\) on both sides proves exactly

\[
W_0
=\frac{G(b_{N+1}b_N^*+b_Nb_{N+1}^*)G}{\omega_N}.
\]

No restriction \(N\ge q\) was used; the multiplication only requires \(G_N\), so it is valid at \(N=q-1\).

The reflection-stable annihilator satisfies

\[
\overline\chi(k-S)=(-1)^q\chi(S).
\]

The exact quotient isomorphism

\[
\Phi:E\longrightarrow\mathbb C[u]/(\widehat\chi),
\qquad [P(S)]\longmapsto[P(c+iu)],
\qquad
\widehat\chi(u)=i^{-q}\chi(c+iu)
\]

has inverse \([Q(u)]\mapsto[Q((S-c)/i)]\), and \(\widehat\chi\) is real monic. If \(E_\Phi\) denotes its coefficient matrix, the transported Gram is \(G_u=E_\Phi^{-*}GE_\Phi^{-1}\). It is a real matrix because both the transported source and the quotient polynomial have real data. Let

\[
Q_j(u)=i^{-j}p_j(c+iu),\qquad d_j=[Q_j]_{\widehat\chi}.
\]

Their coefficient vectors are real and \(E_\Phi b_j=i^jd_j\). Consequently

\[
z_N:=b_N^*Gb_{N+1}
=\overline{i^N}i^{N+1}d_N^*G_ud_{N+1}
=i\,d_N^*G_ud_{N+1}.
\]

The last pairing is real. TVB.26 records its sign by

\[
\frac{z_N}{\omega_N}=i\psi_N,\qquad
\psi_N=\sigma-\ell_N'\in\mathbb R.
\]

The retained phase is \(+i\). In particular \(z_N^2=-|z_N|^2\) and \(z_N+\overline z_N=0\).

## 3. The exact squared radius, including deficient rank

Write

\[
a=b_N^*Gb_N,\qquad
d_+=b_{N+1}^*Gb_{N+1},
\qquad
x=G^{1/2}b_N,\quad y=G^{1/2}b_{N+1}.
\]

Then \(x^*x=a\), \(y^*y=d_+\), \(x^*y=z_N\), and

\[
H=\frac{yx^*+xy^*}{\omega_N}.
\]

This Hermitian operator has rank at most two. Its trace is

\[
\operatorname{Tr}H=\frac{z_N+\overline z_N}{\omega_N}=0.
\]

Expanding all four terms of its square gives

\[
\operatorname{Tr}(H^2)
=\frac{z_N^2+\overline z_N^{\,2}+2ad_+}{\omega_N^2}
=\frac{2(ad_+-|z_N|^2)}{\omega_N^2}.
\]

The Cauchy–Schwarz inequality for \(x,y\) gives \(ad_+-|z_N|^2\ge0\). A Hermitian operator of rank at most two and trace zero has either the pair of nonzero eigenvalues \(\lambda,-\lambda\), or is zero. If it has rank at most one, trace zero already forces it to be zero. The squared trace therefore proves, with all deficient-rank cases included,

\[
\boxed{\epsilon_N^2=\frac{ad_+-|z_N|^2}{\omega_N^2}.}
\]

There is no missing factor of two: \(\operatorname{Tr}(H^2)=2\epsilon_N^2\) when the nonzero pair exists, and both sides vanish otherwise.

## 4. The omitted determinant and the exact factor \(\alpha_{N+1}\)

Define on the same original quotient space

\[
\widetilde K_N
=K_{N-1}+\frac{b_{N+1}b_{N+1}^*}{\omega_{N+1}}
=K_N-\frac{b_Nb_N^*}{\omega_N}
+\frac{b_{N+1}b_{N+1}^*}{\omega_{N+1}},
\]

\[
\widetilde D_N=\det\widetilde K_N,\qquad
\Delta_N=D_{N+1}+D_{N-1}-D_N-\widetilde D_N.
\]

Only \(K_N\) is inverted below. For any invertible \(K\), block elimination of

\[
\begin{pmatrix}K&U\\-V^*&I\end{pmatrix}
\]

in the two block orders gives \(\det(K+UV^*)=\det K\det(I+V^*K^{-1}U)\). The single-column cases yield

\[
\frac{D_{N+1}}{D_N}=1+\frac{d_+}{\omega_{N+1}},
\qquad
\frac{D_{N-1}}{D_N}=1-\frac{a}{\omega_N}.
\]

The second equality is valid even when \(K_{N-1}\) is singular: the block formula uses only \(K_N^{-1}\).

For the simultaneous negative and positive update, take

\[
U=\left[-\frac{b_N}{\omega_N},
\frac{b_{N+1}}{\omega_{N+1}}\right],
\qquad
V^*=\begin{bmatrix}b_N^*\\b_{N+1}^*\end{bmatrix}.
\]

Then the complete two-column factor is

\[
I+V^*GU=
\begin{pmatrix}
1-a/\omega_N&z_N/\omega_{N+1}\\
-\overline z_N/\omega_N&1+d_+/\omega_{N+1}
\end{pmatrix},
\]

so

\[
\frac{\widetilde D_N}{D_N}
=\left(1-\frac a{\omega_N}\right)
\left(1+\frac{d_+}{\omega_{N+1}}\right)
+\frac{|z_N|^2}{\omega_N\omega_{N+1}}.
\]

Subtracting these three determinant ratios in the precise order defining \(\Delta_N\) gives

\[
\begin{aligned}
\frac{\Delta_N}{D_N}
&=\left(1+\frac{d_+}{\omega_{N+1}}\right)
+\left(1-\frac a{\omega_N}\right)-1\\
&\quad-\left[
\left(1-\frac a{\omega_N}\right)
\left(1+\frac{d_+}{\omega_{N+1}}\right)
+\frac{|z_N|^2}{\omega_N\omega_{N+1}}\right]\\
&=\frac{ad_+-|z_N|^2}{\omega_N\omega_{N+1}}.
\end{aligned}
\]

Therefore

\[
\boxed{
\alpha_{N+1}\frac{\Delta_N}{D_N}
=\frac{\omega_{N+1}}{\omega_N}
\frac{ad_+-|z_N|^2}{\omega_N\omega_{N+1}}
=\epsilon_N^2.}
\]

This is LC3, with its original norm ratio and both consecutive norm factors. The proof is valid for all \(N\ge q-1\), including \(N=0\) when \(q=1\).

## 5. The positive source-minor map and the regular-degree losses

For a finite column set \(L\), Cauchy–Binet on the original orthogonal source gives

\[
\det\left(\sum_{j\in L}\frac{b_jb_j^*}{\omega_j}\right)
=\sum_{\substack{J\subseteq L\\|J|=q}}
\frac{|\det B_J|^2}{\prod_{j\in J}\omega_j}.
\]

In the four terms defining \(\Delta_N\), a subset containing neither of \(N,N+1\) has coefficient \(1+1-1-1=0\); a subset containing exactly one has coefficient zero; a subset containing both has coefficient one. Hence for \(q\ge2\),

\[
\Delta_N=
\sum_{\substack{I\subseteq\{0,\ldots,N-1\}\\|I|=q-2}}
\frac{|\det B_{I\cup\{N,N+1\}}|^2}
{\omega_N\omega_{N+1}\prod_{i\in I}\omega_i}\ge0.
\]

This formula is valid at \(N=q-1\). For \(q=1\), the determinant is additive in its scalar column contributions, and the four terms cancel to \(\Delta_N=0\); a subset of size \(-1\) is not introduced.

The source wedge subspace

\[
\mathcal E_N=(\bigwedge^{q-2}\mathcal P_{N-1})
\wedge p_N\wedge p_{N+1}
\]

and the map \(\Lambda_N=(\bigwedge^qT_{N+1})|_{\mathcal E_N}\) from TVB.31 retain each original source norm. With the original coordinate wedge \(e_C\), the adjoint vector has coefficient

\[
\frac{\overline{\det B_{I\cup\{N,N+1\}}}}
{\omega_N\omega_{N+1}\prod_{i\in I}\omega_i}
\]

on the source wedge indexed by \(I\). Its norm is therefore exactly

\[
\|\Lambda_N^*e_C\|_\theta^2=\Delta_N.
\]

The original unscaled alternating tensor image has squared norm \(q!\Delta_N\), as TVB.31 states. LC3 uses the exterior-source determinant norm \(\Delta_N\); it does not silently replace it by the tensor-image norm.

For \(N\ge q\), both \(D_{N-1}\) and \(D_N\) are positive. The regular ratios

\[
\delta_N=D_{N-1}/D_N,\qquad
\delta_{N+1}=D_N/D_{N+1}
\]

are then positive and at most one. Substitution in Section 4 gives the complete original phase formulas

\[
\epsilon_N^2=
\alpha_{N+1}(1-\delta_N)(\delta_{N+1}^{-1}-1)-\psi_N^2,
\]

\[
\frac{\widetilde D_N}{D_N}
-\frac{\delta_N}{\delta_{N+1}}
=\frac{\psi_N^2}{\alpha_{N+1}}.
\]

Writing \(v_N=-\log\delta_N\), \(s_N=(v_N+v_{N+1})/2\), and \(t_N=(v_{N+1}-v_N)/2\), the product in the first formula equals

\[
(1-e^{-v_N})(e^{v_{N+1}}-1)
=\sinh^2s_N-(e^{t_N}-\cosh s_N)^2.
\]

This proves TVB.32–TVB.34, including the two retained nonnegative losses. Equality in the resulting upper bound requires both \(\psi_N=0\) and \(e^{t_N}=\cosh s_N\); multiplying the second equation by \(2\sqrt{\delta_N\delta_{N+1}}\) gives precisely \(\delta_N(2-\delta_{N+1})=1\). These logarithmic formulas have domain \(N\ge q\). LC3 uses the determinant form, which remains meaningful at the first degree without taking a logarithm of \(D_{q-2}=0\).

## 6. The first admitted degree \(N=q-1\)

Let \(B=[b_0,\ldots,b_{q-1}]\). Its determinant is one because the columns are monic and triangular in the original remainder coordinates. Thus

\[
K_{q-1}=B\operatorname{diag}(\omega_j^{-1})B^*,
\qquad
B^*G_{q-1}B=\operatorname{diag}(\omega_j),
\qquad
D_{q-1}=\prod_{j=0}^{q-1}\omega_j^{-1}.
\]

Expand the complete original relation:

\[
\chi=p_q+\sum_{j=0}^{q-1}\gamma_jp_j,\qquad
\gamma_j=\frac{\langle p_j,\chi\rangle_\theta}{\omega_j}.
\]

Reduction gives \(b_q=-\sum_{j<q}\gamma_jb_j\). The orthogonality just proved yields

\[
a=\omega_{q-1},\qquad
z_{q-1}=-\gamma_{q-1}\omega_{q-1},\qquad
d_+=\sum_{j<q}|\gamma_j|^2\omega_j.
\]

The source norm of the entire relation is

\[
\nu_0=\|\chi\|_\theta^2
=\omega_q+\sum_{j<q}|\gamma_j|^2\omega_j.
\]

Combining the formula for \(z_{q-1}\) with the retained phase \(z_{q-1}=i\omega_{q-1}\psi_{q-1}\) gives the exact sign \(\gamma_{q-1}=-i\psi_{q-1}\). Therefore Section 3 becomes

\[
\epsilon_{q-1}^2
=\frac{\sum_{j=0}^{q-2}|\gamma_j|^2\omega_j}{\omega_{q-1}}
=\frac{\nu_0-\omega_q}{\omega_{q-1}}-\psi_{q-1}^2.
\]

The singular predecessor is already accounted for by \(D_{q-2}=0\). The omitted determinant and the determinant difference are

\[
\frac{\widetilde D_{q-1}}{D_{q-1}}
=\frac{|\gamma_{q-1}|^2\omega_{q-1}}{\omega_q}
=\frac{\psi_{q-1}^2}{\alpha_q},
\]

\[
\frac{\Delta_{q-1}}{D_{q-1}}
=\frac{\sum_{j=0}^{q-2}|\gamma_j|^2\omega_j}{\omega_q}.
\]

Multiplication of the last formula by \(\alpha_q=\omega_q/\omega_{q-1}\) gives exactly the endpoint radius. This is a direct boundary derivation of both equalities in LC3.

The source projection

\[
\mathsf P_{q-2}\chi=\sum_{j=0}^{q-2}\gamma_jp_j
\]

has squared original source norm equal to the numerator in the first radius formula. Its reduction is \(\sum_{j=0}^{q-2}\gamma_jb_j\), whereas the complete relation reduces to zero. TVB.38b–TVB.38c give the exact conjugate-linear isomorphism from this projection source to the endpoint wedge source, with norm multiplier \(D_{q-1}/\omega_q\). Thus the positive endpoint expression is attached to a specified source and map; it is not a discarded leading coefficient.

## 7. The scalar quotient and the excluded empty quotient

For \(q=1\), the admitted degrees are \(N\ge0\). Every pair \(b_N,b_{N+1}\) lies in the same one-dimensional quotient, so its two-vector Gram determinant is zero:

\[
ad_+-|z_N|^2=0.
\]

The reflection phase still gives trace zero, and hence \(X_0=0\). Thus \(\epsilon_N=0\) at every admitted degree, exactly as in TVB.38. The determinant difference also vanishes by scalar additivity, so both sides of LC3 are zero.

At the first degree \(N=0\), the convention is explicitly \(K_{-1}=0\) as a one-dimensional zero matrix and \(D_{-1}=0\). The endpoint expansion \(\chi=p_1+\gamma_0p_0\) retains its top coefficient and omitted determinant. The lower projection is the zero source \(\mathcal P_{-1}=0\), its sum is empty, and the endpoint radius is zero. Neither \(\nu_{-1}\) nor a predecessor quotient metric is needed.

The LC chapter already excludes \(q=0\) by its displayed hypothesis \(q=\deg\chi\ge1\). This is appropriate for its nonzero constant class and highest-remainder-coefficient functional. The separate empty-quotient paragraph of the Toda chapter has \(\chi=1\), \(E=0\), the unique zero least lift and control, and the empty Gram determinant \(V_N=1\). The source quotient map is the zero map from the original source to \(E=0\), with the whole source its relation kernel. These are its exact boundary objects. They do not justify extending the positive-dimensional rule \(D_{q-2}=0\) to \(q=0\); an empty determinant is one and the index \(q-2=-2\) would lie outside the source-kernel convention used here.

## 8. Concrete self-contained addition recommended to the author

No change to the mathematical formula LC3 is required. The following explicit domain and kernel definitions make its boundary meaning visible within the LC chapter:

~~~tex
N\in\mathbb Z,\qquad N\ge q-1,\qquad
K_j=\sum_{r=0}^{j}\frac{b_rb_r^*}{\omega_r}\quad(j\ge-1),
\qquad K_{-1}=0.
~~~

The accompanying text should specify that the last sum is empty at \(j=-1\), that \(D_j=\det K_j\) is always taken on the original \(q\)-dimensional quotient, and that independence of the first \(q-1\) monic columns proves \(D_{q-2}=0\). Define \(\widetilde K_N=K_{N-1}+b_{N+1}b_{N+1}^*/\omega_{N+1}\) and \(\widetilde D_N=\det\widetilde K_N\) directly next to \(\Delta_N\) if the LC chapter is to be independently readable.

These additions make explicit what the currently cited Toda chapter already proves. All primary source formulas reviewed here remain unchanged; this review pin applies to the source editions listed above.

## 9. Follow-up source inspection

The author subsequently supplied the cumulative LC source with SHA-256 11acd1f4437984c94ef21c961973d83445ad4fcc81f9935398e25e4cff111fa2. This reviewer read that complete source. In its LC1–LC3 portion, the original monicity, the integer condition \(N\ge q-1\), the complex deformation parameter, the empty source sum \(K_{-1}=0\), the omitted kernel, and the rank proof of \(D_{q-2}=0\) are now explicit. The formula LC3 and its trace phase are unchanged. The recommended boundary clarification is therefore implemented and verified at that source edition. The separate newly appended LC13–LC16 constituent comparison is handled in the dedicated constituent-comparison review.
