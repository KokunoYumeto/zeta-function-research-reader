# Independent complete proof review of the Toda–CV bridge

Date: 2026-09-13. Scope: a full reading and independent derivation of the
standalone `toda_cv_exact_bridge_20260912.tex`, including the actual source
spaces, analytic strip, unit and quotient maps, both determinant sequences,
operator curvature, retained complex phase, positive minors, degree endpoint,
and the spectral-coupling join. This is a written mathematical review. It
does not report Lean execution, a new replay of the delivered Toda suite, an
arithmetic asymptotic bound, or an RH proof.

Final source SHA256:
`97652a43445708c0e6d2a959f45aed8a4f2a7f73f9cd4b6cd57e67b8fedb408e`.
Final source size: **45,985 bytes**.

Status: **accepted after complete source reading and independent derivation**.
Every TVB.1–44 proof, the additional TVB.34a–b and TVB.38a–c maps,
and the last domain clarifications were read. No unresolved mathematical
defect remains in this bounded bridge.

## Sources and reading scope

The bridge was read consecutively in full, not by selecting its displayed
formulas. The review additionally read the original arithmetic definitions
and proofs A1–A7 in the cumulative `tex/arithmetic_input.tex`, the direct
spectral-coupling join `sources/web_toda_parent_join/PARENT_EXACT_JOIN.md`,
and the original exterior proof through E18 in
`work/exterior_trace_equality_continuation_20260912.tex`.

The parent-join source SHA256 is
`71e275a8543448e57bcfafc5ead8cf3c7f98d594ae994582d1180999d98c6370`.
The exterior source SHA256 is
`313c321537673bf629e10a673daaacd5d74d234efcaadee0210a8c56909a921e`.

Two source-typing repairs were requested from the author during review:
explicit standalone definitions and construction of the theta/Mellin source,
and the precise analytic Taylor-jet map defining `[v_h]_h`. These are
completeness repairs to the text, not changes to the determinant or curvature
formulas. Both are closed in the accepted source. The final seed Mellin
domain and the nonempty Sylvester unit sphere are also explicit there.

## 1. Original arithmetic measure, jet unit, and tensor source

Write the original nonempty packet as
\(h(s)=\prod_\rho(s-\rho)^{m_\rho}\), retaining every actual complete zero
order. Then \(v_h=g/h\) is entire. At each selected root, its constant
Taylor coefficient is nonzero: if
\(g=(s-\rho)^{m_\rho}a_\rho(s)\) and
\(h=(s-\rho)^{m_\rho}b_\rho(s)\), both local factors have nonzero value,
and \(v_h(\rho)=a_\rho(\rho)/b_\rho(\rho)\ne0\).
The analytic-jet map sends an entire function to its Taylor polynomials
modulo each \((s-\rho)^{m_\rho}\), followed by the inverse Chinese-remainder
isomorphism into \(\mathbb C[s]/(h)\). Thus the notation
\(\upsilon_h=[v_h]_h\) has an exact algebraic target. A truncated Taylor
series with nonzero constant coefficient has a unique multiplicative
inverse, recursively determined by its product with the original series.
This proves \(\upsilon_h\) is a unit, with all higher Taylor coefficients
retained; it does not replace the unit by its constant coefficient.

For \(I=(h(s_1),\ldots,h(s_k))\), the map
\(\mathbb C[S]\to\mathbb C[s_1,\ldots,s_k]/I\), \(S\mapsto\sum_i s_i\),
has a nonzero kernel because its target is finite dimensional. Its unique
monic least-degree kernel polynomial \(\chi\) generates the whole kernel:
division by \(\chi\) leaves a lower-degree remainder in the same kernel,
and minimality forces this remainder to vanish. Consequently
\[
 \eta:\mathbb C[S]/(\chi)\longrightarrow
       (E_h^{\otimes k})^{\mathfrak S_k},\qquad
 \eta[P]=\upsilon_h^{\otimes k}[P(s_1+\cdots+s_k)]
\]
is injective. The first map has kernel exactly \((\chi)\); its product with
the displayed tensor unit is invertible; and both the sum polynomial and
the unit tensor are permutation invariant. These verify kernel, target,
and invariance separately.

The exact Mellin convention is
\(\mathcal MF(s)=\int_0^\infty F(x)x^s\,dx/x\), and the theta convention
is \(\Theta\phi(x)=2\sum_{n\ge1}\phi(nx)\). For the original Gaussian
polynomial
\(\phi_0=(4\pi^2x^4-6\pi x^2)e^{-\pi x^2}\), direct integration on
\(\Re s>-2\) gives
\[
 \mathcal M_+\phi_0(s)
 =\pi^{-s/2}\{2\Gamma(s/2+2)-3\Gamma(s/2+1)\}
 =\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2).
\]
At \(s=0\), the last product has the removable value supplied by the
preceding gamma expression, which is holomorphic on \(\Re s>-2\).
The factor two in theta then gives \(\mathcal M\Theta\phi_0=g\), not
\(g/2\). The source has value zero at zero, and its integral on the real
line is zero since its even half-line integral is the displayed expression
at \(s=1\). Euler differentiation preserves these conditions: its value
at zero remains zero, and integration by parts gives
\(\int D\phi=\int\phi\). It preserves evenness and Schwartz decay too.

The exact inverse used to construct \(F_h\) is
\[
 S_\rho F(x)=x^{-\rho}\int_x^\infty F(y)y^{\rho-1}\,dy.
\]
It is defined on the zero Mellin moment at \(\rho\). On that domain the
upper integral is the negative lower integral. If
\(\sigma=\Re\rho\), a bound \(|F(y)|\le C y^{-M}\) at infinity gives
\(|S_\rho F(x)|\le Cx^{-M}/(M-\sigma)\) for \(M>\sigma\). A bound
\(|F(y)|\le C y^M\) at zero gives
\(|S_\rho F(x)|\le Cx^M/(M+\sigma)\) for \(M+\sigma>0\).
The equation \(D S_\rho F=\rho S_\rho F+F\) supplies all Euler derivative
estimates recursively. Thus this inverse preserves the original strong
Schwartz target. Its homogeneous kernel is \(cx^{-\rho}\), whose required
decay at both ends forces \(c=0\). Mellin integration by parts then gives
\(\mathcal M S_\rho F=\mathcal MF/(s-\rho)\), with the removable value
retained. Iterating through every root and its complete order defines the
unique \(F_h\) with \(h(D)F_h=\Theta\phi_0\) and \(\mathcal MF_h=g/h\).
Every intermediate inverse is defined because the remaining Mellin factor
has the corresponding zero. This establishes the original source map
\(\mathcal VP=P(D_1+\cdots+D_k)F_h^{\otimes k}\).

Mellin–Plancherel on \(\Re s=1/2\) gives one factor \(dt/(2\pi)\) per
tensor coordinate, hence the density is exactly
\(\prod_iw_h(t_i)\,d^kt\) with
\(w_h(t)=|v_h(1/2+it)|^2/(2\pi)\). The map
\[
 (y_1,\ldots,y_{k-1},u)\longmapsto
 (y_1,\ldots,y_{k-1},u-\textstyle\sum y_i)
\]
has determinant one. Reordering its input as \((u,y)\) contributes
\((-1)^{k-1}\). Absolute integration retains unit density Jacobian and
gives the convolution \(m_k=w_h^{*k}\), so the mass is \(\mu_h^k\).
No probability normalization or change in the arithmetic unit is involved.

## 2. Analytic strip and its exact Hilbert comparisons

The alternating Dirichlet partial sums are bounded by one, so Abel
summation gives \(|\eta(s)|\le |s|/\Re s\) in \(\Re s>0\). On the
line \(\Re s=1/2\), the denominator of
\(\zeta=\eta/(1-2^{1-s})\) has modulus at least \(\sqrt2-1\).
Rotation of the gamma ray through
\(\operatorname{sgn}(t)\varphi\), \(0<\varphi<\pi/2\), gives
\[
 |\Gamma(1/4+it/2)|
 \le\Gamma(1/4)(\cos\varphi)^{-1/4}e^{-\varphi|t|/2}.
\]
The sign of the rotation is essential: the factor
\(e^{i\operatorname{sgn}(t)\varphi(1/4+it/2)}\) has modulus
\(e^{-\varphi|t|/2}\). The small arc vanishes since its radial real
exponent is \(1/4>0\), and the large arc vanishes since
\(\cos\varphi>0\). The gamma formula therefore supplies its stated
bound without an omitted phase or an asymptotic equality.

For sufficiently large \(|t|\), monicity gives a positive constant
\(C_h\) with \(|h(1/2+it)|\ge C_h(1+|t|)^d\). The two factors in
\(s(s-1)\) and the preceding linear zeta bound yield
\[
 w_h(t)\le C_{h,\varphi}(1+|t|)^{6-2d}e^{-\varphi|t|}.
\]
On compact intervals the division by complete zero orders is removable,
so no local singularity is hidden in this estimate. For any
\(r<\pi/2\), choose \(r<\varphi<\pi/2\). Multiplication by
\(e^{\theta t}\) for \(|\Re\theta|\le r\), and by any fixed polynomial,
leaves an integrable majorant. This proves all stated derivatives and their
local uniform convergence. Tensor absolute integrability permits Fubini,
and thus \(Z(\theta)=M_h(\theta)^k\) on the same complex strip.

The nonzero entire \(v_h\) has a discrete zero set on the line. Its squared
modulus is positive almost everywhere; the convolution fibre integrand is
positive off the finite union of the inverse images of that discrete set.
Consequently every nonzero polynomial has positive original and tilted
norm. All finite source and relation Gram matrices in the proof are
therefore positive definite.

For real \(\theta\), the scalar map
\(f\mapsto e^{\theta u/2}f\) is an onto isometry from
\(L^2(e^{\theta u}m_k\,du)\) to \(L^2(m_k\,du)\), with inverse using
the negative exponent. It commutes with multiplication by \(c+iu\).
The tensor map multiplies by \(e^{\theta\sum t_i/2}\) and has the same
inverse on the original Mellin Hilbert space. Its restriction to
\(\mathcal VP\) agrees with the scalar map by the sum-fibre formula.
This makes the target of every tilted alternating tensor norm explicit;
the theta-zero norm remains the original tensor source norm.

## 3. Polynomial source relation and the full boundary primitive

Set \(n=N+1\), \(m=N-q+1\), and \(\mathcal P_j=\mathbb C[S]_{\le j}\)
with \(\mathcal P_{-1}=0\). For \(N\ge q-1\), monic division proves
\[
 0\to\mathcal P_{m-1}\xrightarrow{M_\chi}\mathcal P_N
       \xrightarrow{T_N}C\to0.
\]
The leading degree proves injectivity of \(M_\chi\), the kernel of
reduction is the displayed multiple space, and the first \(q\) monomials
prove surjectivity. Successive monic division in the retained order
\(s_1,\ldots,s_k\) gives actual polynomials \(Q_i\) satisfying
\(\chi(S)=\sum_i h(s_i)Q_i\). The tensor remainder vanishes because
\(\chi\) belongs to the contraction ideal.

The claimed primitive of \(\mathcal V(\chi P)\) has its \(i\)th summand
\[
 (-1)^{i-1}Q_i(D_1,\ldots,D_k)P(D_1+\cdots+D_k)
 (F_h^{\otimes(i-1)}\otimes\phi_0\otimes F_h^{\otimes(k-i)}).
\]
It belongs to cochain degree \(k-1\). All factors preceding \(\phi_0\)
have degree one; hence the tensor differential introduces another
\((-1)^{i-1}\). Their product is one and its differential is exactly
the \(i\)th term \(h(D_i)Q_i(D)P(\sum D_i)F_h^{\otimes k}\).
Euler differentiation preserves each stated source and commutes with
theta. Summing proves the full boundary formula with its original signs
and domains. Conversely the full jet of an admitted polynomial source is
\(\eta T_NP\), whose zero set is exactly the same kernel by injectivity
of \(\eta\). A nonzero boundary retains positive source norm before
reduction; its zero observation is the proved jet map.

The Laplace map satisfies
\(\mathscr L(SP)=(c+i\partial_\theta)\mathscr L(P)\) by the dominated
derivative calculation. Since complex conjugation on the source line
sends \(c+iu\) to \(c-iu\), the relation norm is precisely
\[
 Z_\chi=\overline\chi(c-i\partial_\theta)
                 \chi(c+i\partial_\theta)Z.
\]
Both polynomial factors, both derivative signs, and their positive Gram
interpretation are necessary and agree with TVB.10.

## 4. Monic determinants and the determinant-line map

The coefficient matrix \(E_j\) for \(S^a=(c+iu)^a\) has entries
\((E_j)_{ba}=\binom ab c^{a-b}i^b\) for \(b\le a\) and zero otherwise.
It is triangular, with determinant \(i^{j(j-1)/2}\). Thus the original
\(S\)-monomial Gram equals \(E_j^*H_jE_j\), where
\(H_j=[Z^{(a+b)}]\), and its determinant multiplier is
\(\overline{\det E_j}\det E_j=1\). The relation-weight Gram has the
same coordinate matrix and multiplier. This proves that the Hankel
determinants \(\mathfrak D_j,\mathfrak B_j\) retain the original monic
coordinates and mass. Monic Gram elimination then gives
\(\omega_j=\mathfrak D_{j+1}/\mathfrak D_j\) and
\(\nu_j=\mathfrak B_{j+1}/\mathfrak B_j\), with
\(\omega_0=Z=M_h^k\).

In fixed quotient coordinates the right inverse
\[
 R_N=M_N^{-1}J_N^*G_N,\qquad
 K_N=J_NM_N^{-1}J_N^*,\qquad G_N=K_N^{-1}
\]
satisfies \(J_NR_N=I\). For \(B\in\ker J_N\),
\(\langle B,R_Nx\rangle=B^*J_N^*G_Nx=0\). Every other lift is
\(R_Nx+B\), giving the exact norm
\(x^*G_Nx+\|B\|^2\). This proves both minimality and uniqueness.

The source basis consisting first of \(1,S,\ldots,S^{q-1}\), then of
\(\chi,\chi S,\ldots,\chi S^{m-1}\), has triangular transition
determinant one from the original source monomials. Replacing the first
block by the corresponding minimum lifts adds only relation columns and
again has determinant one. Its orthogonal-block Gram has determinant
\(\det G_N\,\mathfrak B_m\). Therefore
\[
 V_N=\det G_N=\mathfrak D_{N+1}/\mathfrak B_m,
 \qquad D_N^{\rm CV}=\det K_N=V_N^{-1}.
\]
This is also the explicit determinant-line map
\(\det C\otimes\det\mathcal P_{m-1}\to\det\mathcal P_N\), taking
the quotient wedge first and the multiplication-by-\(\chi\) wedge
second. Reversing these blocks contributes \((-1)^{qm}\); there is no
unspecified orientation. The unscaled alternating tensor sum applied to
\(n\) source vectors has squared norm \(n!\det(\operatorname{Gram})\):
expand its two permutation sums and group by their relative permutation.
There are \(n!\) copies of the determinant, proving the stated factorial
and the target cochain degree \(kn\).

## 5. Both Toda equations and the operator curvature

For either real positive weight, let \(Q_j\) be its real monic orthogonal
polynomial in \(u\), with squared norm \(h_j\). Degree, orthogonality and
the leading coefficient yield
\[
 uQ_j=Q_{j+1}+b_j^{\rm rec}Q_j+a_jQ_{j-1},
 \qquad a_j=h_j/h_{j-1}>0\ (j\ge1),\quad a_0=0.
\]
Differentiate \(\langle Q_i,Q_j\rangle=0\). For \(i\le j-2\), all
terms except \(\langle Q_i,\partial_\theta Q_j\rangle\) vanish by
degree. For \(i=j-1\), the measure-derivative term is
\(\langle Q_{j-1},uQ_j\rangle=h_j\), so that coefficient is \(-a_j\).
Consequently \(\partial_\theta Q_j=-a_jQ_{j-1}\) and
\(h_j'=b_j^{\rm rec}h_j\). Differentiating
\(h_jb_j^{\rm rec}=\langle Q_j,uQ_j\rangle\) gives two polynomial
terms \(-2a_jh_j\), and the measure term
\(h_j(a_{j+1}+(b_j^{\rm rec})^2+a_j)\). Subtracting
\(h_j'b_j^{\rm rec}\) proves
\((b_j^{\rm rec})'=a_{j+1}-a_j\). Summing this equality telescopes,
so the second logarithmic derivative of the first \(n\) norms is
\(a_n\). In original coordinates this is exactly
\[
 (\log\mathfrak D_n)''=\omega_n/\omega_{n-1},\qquad
 (\log\mathfrak B_m)''=\nu_m/\nu_{m-1}.
\]
Their zeroth determinants are one and have zero logarithmic derivatives.
Thus \(\ell_N''=\alpha_{N+1}-\beta_m\), including \(m=0\) with
\(\beta_0=0\). Multiplying by the determinant squared gives the
Hankel–Toda equation with coefficient exactly one.

All finite Gram entries and their inverses depend smoothly on real
\(\theta\), by positivity and the analytic strip just proved. Hence
the lift can be differentiated in the fixed polynomial space. Put
\(X=(S-c)/i\); it is the original selfadjoint multiplication by \(u\)
on its polynomial domain. Differentiating \(T_NR_N=I\) proves
\(R_N'x\in\mathcal D_N\). Differentiating its pairing with every
fixed boundary polynomial gives
\[
 R_N'=-P_{\mathcal D_N}XR_N=-I_N.
\]
The derivative is therefore the actual boundary already represented by
the displayed cochain primitive. Differentiating its original norm,
including the varying measure, gives
\[
 G_N'=R_N^*XR_N,\qquad
 G_N''=R_N^*X^2R_N-2R_N^*XP_{\mathcal D_N}XR_N.
\]
Since the minimum-lift projector is \(R_NG_N^{-1}R_N^*\) and its
orthogonal direct sum with \(P_{\mathcal D_N}\) is \(P_N\), subtraction
of \(G_N'G_N^{-1}G_N'\) gives
\[
 G_N''-G_N'G_N^{-1}G_N'=O_N^*O_N-I_N^*I_N,
 \qquad O_N=(1-P_N)XR_N.
\]
This verifies TVB.18 as an equality of fixed-coordinate Hermitian forms,
not just the equality after taking its trace.
Its exact linear target is the antidual consisting of conjugate-linear
functionals: the form operator sends \(x\) to
\(y\mapsto\langle O_Ny,O_Nx\rangle_\theta\), which is complex-linear
in \(x\) and conjugate-linear in \(y\). The coefficient Euclidean
pairing identifies this antidual with the written matrix coordinates.

## 6. Exact individual curvature costs

The polynomial \(\chi r_m\) is monic of degree \(N+1\), is a relation,
and is orthogonal to \(\mathcal D_N\). Subtracting the monic source
polynomial \(p_{N+1}\) leaves a degree-at-most-\(N\) vector orthogonal
to \(\mathcal D_N\), whose reduction is \(-b_{N+1}\). Uniqueness of
the minimum lift therefore proves
\[
 \chi r_m=p_{N+1}-R_Nb_{N+1},\qquad
 \nu_m=\omega_{N+1}+b_{N+1}^*G_Nb_{N+1}.
\]
The two summands in this norm are orthogonal because \(p_{N+1}\) is
orthogonal to the whole source \(\mathcal P_N\).

The coefficient of \(p_N\) in \(R_Nx\) is
\(b_N^*G_Nx/\omega_N\). The leading coefficient of \(X\) as an
\(S\)-polynomial is \(-i\). Thus
\[
 O_Nx=-i\,p_{N+1}\,b_N^*G_Nx/\omega_N.
\]
To compute the inner component, pair with the orthogonal relation basis
\(\chi r_j\). For \(j\le m-2\), \(X\chi r_j\) is an old boundary
and hence pairs to zero with \(R_Nx\). At \(j=m-1\), its top
coefficient is \(-i\) times \(\chi r_m\). Moving \(X\) across the
pairing conjugates that coefficient to \(+i\), while the previous
identity gives \(\langle\chi r_m,R_Nx\rangle=-b_{N+1}^*G_Nx\).
Consequently
\[
 I_Nx=-i\,\chi r_{m-1}\,b_{N+1}^*G_Nx/\nu_{m-1}
\]
for \(m\ge1\), and \(I_N=0\) when \(m=0\). This checks the sign
in the full map, which would be invisible in its squared norm.

Writing \(a=b_N^*G_Nb_N\), \(d_+=b_{N+1}^*G_Nb_{N+1}\), the two
traces are \(\omega_{N+1}a/\omega_N^2\) and \(d_+/\nu_{m-1}\).
The rank-one determinant identities below give
\(a/\omega_N=1-\delta_N\),
\(\delta_N=\omega_N/\nu_{m-1}\), and
\(d_+=\nu_m-\omega_{N+1}\). Thus the costs are exactly
\[
 \alpha_{N+1}(1-\delta_N),\qquad
 \beta_m-\alpha_{N+1}\delta_N.
\]
Both are nonnegative and retain their shared term
\(\alpha_{N+1}\delta_N\). Their difference is the scalar curvature;
identifying the two positive costs individually with \(\alpha\) and
\(\beta\) would discard this shared term. At \(N=q-1\), the included
top column has leverage one, the outer cost is \(\alpha_q\), and the
inner cost is zero. The written scalar convention for \(\delta^{\rm end}\)
is a zero determinant ratio and uses no inverse of \(K_{q-2}\).

## 7. Rank-one determinant and inverse updates

The orthogonal source basis gives
\(K_N=\sum_{j\le N}b_jb_j^*/\omega_j\). Its first \(q\) monic
remainder columns are a triangular basis, so \(K_N>0\) exactly in
the admitted range. Block elimination of the matrix with blocks
\(K,U,-V^*,I\) proves
\(\det(K+UV^*)=\det K\det(I+V^*K^{-1}U)\).
For the added column and removed last column it yields
\[
 D_{N+1}^{\rm CV}/D_N^{\rm CV}=1+d_+/\omega_{N+1},\qquad
 D_{N-1}^{\rm CV}/D_N^{\rm CV}=1-a/\omega_N.
\]
Since \(D_j^{\rm CV}=V_j^{-1}\), these are precisely TVB.23; the
identities with \(\nu_{m-1},\nu_m\) follow independently from the
complete determinant-line quotient. Direct multiplication verifies
\[
 G_{N+1}=G_N-
 \frac{G_Nb_{N+1}b_{N+1}^*G_N}{\omega_{N+1}+d_+}.
\]
Its denominator is the positive original relation norm \(\nu_m\).
All original source norms remain in the denominators.

## 8. Real quotient correspondence and the retained cross phase

Reflection preserves the tensor ideal, sends \(S\) to \(k-\bar S\),
and therefore sends its monic generator to the same generator with
leading sign: \(\bar\chi(k-S)=(-1)^q\chi(S)\). It follows that
\(\widehat\chi(u)=i^{-q}\chi(c+iu)\) is real and monic. The maps
\[
 [P(S)]\mapsto[P(c+iu)],\qquad
 [Q(u)]\mapsto[Q((S-c)/i)]
\]
are inverse algebra isomorphisms because they carry \((\chi)\) to
\((\widehat\chi)\) by the explicit scalar unit \(i^q\). Their
coefficient matrix is the previously specified \(E_q\).
Thus \(A\) transports to \(cI+iT\), the Gram to
\(E_q^{-*}G_NE_q^{-1}\), and the kernel to \(E_qK_NE_q^*\).
The determinant is unchanged because \(|\det E_q|=1\). This exact
coordinate map preserves the original quotient and its norm.

Let \(Q_j(u)=i^{-j}p_j(c+iu)\). It is real monic, and with
\(d_j=[Q_j]\) one has \(E_qb_j=i^jd_j\). In these explicitly
transported coordinates all source moments, remainder maps and Grams
are real. Write \(\sigma=\operatorname{Tr}T\in\mathbb R\).
The top coefficient of the minimum lift is
\(d_N^*G_Nx/\omega_N\). Subtracting its top boundary from
\(XR_N-R_NT\) leaves an old boundary. Pairing with the minimum lift
and using \(R_N^*(Q_{N+1}-R_Nd_{N+1})=-G_Nd_{N+1}\) gives
\[
 R_N^*XR_N-G_NT
 =-G_Nd_{N+1}d_N^*G_N/\omega_N.
\]
Taking the trace after multiplication by \(G_N^{-1}\) proves
\(\ell_N'=\sigma-d_N^*G_Nd_{N+1}/\omega_N\). Transporting back
introduces the exact factor \(\overline{i^N}i^{N+1}=i\), hence
\[
 z_N:=b_N^*G_Nb_{N+1}=i\omega_N\psi_N,
 \qquad\psi_N=\sigma-\ell_N'.
\]
No evenness of the arithmetic weight was assumed: reflection stability
of the packet supplies a real quotient, while a non-even weight or a
nonzero tilt may retain a nonzero \(\psi_N\).

## 9. Rank-two relative operator and omitted determinant

The real three-term recurrence transports back to
\(Sp_j=p_{j+1}+(c+ib_j^{\rm rec})p_j-\alpha_jp_{j-1}\).
In \(AK_N+K_NA^*-kK_N\), the imaginary diagonal parts cancel and
the interior neighboring terms cancel because
\(\alpha_j/\omega_j=1/\omega_{j-1}\). Only the endpoint remains:
\[
 AK_N+K_NA^*-kK_N
 =(b_{N+1}b_N^*+b_Nb_{N+1}^*)/\omega_N.
\]
Multiplying by \(G_N\) on both sides yields the original relative
Hermitian form. With \(x=G_N^{1/2}b_N\), \(y=G_N^{1/2}b_{N+1}\),
its Euclidean Hermitian realization is
\((xy^*+yx^*)/\omega_N\). Its trace is zero since
\(z_N=i\omega_N\psi_N\), consistently with
\(2\Re\operatorname{Tr}A-kq=0\). Its rank is at most two, and
expanding its square gives
\[
 \operatorname{Tr}H_N^2
 =\{2ad_++2\Re(z_N^2)\}/\omega_N^2
 =2(ad_+-|z_N|^2)/\omega_N^2.
\]
Thus its nonzero eigenvalues are \(+\epsilon_N,-\epsilon_N\), where
\[
 \epsilon_N^2=(ad_+-|z_N|^2)/\omega_N^2
 =\alpha_{N+1}(1-\delta_N)(\delta_{N+1}^{-1}-1)-\psi_N^2.
\]
The first formula already holds at the first admitted degree.

For the actual omitted-column kernel,
\(\widetilde K_N=K_N-b_Nb_N^*/\omega_N+b_{N+1}b_{N+1}^*/\omega_{N+1}\),
the same determinant lemma gives the two-by-two determinant
\[
 \widetilde D_N/D_N^{\rm CV}
 =(1-a/\omega_N)(1+d_+/\omega_{N+1})
       +|z_N|^2/(\omega_N\omega_{N+1}).
\]
The positive sign before the cross modulus comes from the one negative
column update. No inverse of \(\widetilde K_N\) is used; singular
omitted-direction kernels are included. Subtracting the four determinants
gives
\[
 \epsilon_N^2=\alpha_{N+1}\Delta_N/D_N^{\rm CV},\qquad
 \widetilde D_N/D_N^{\rm CV}-\delta_N/\delta_{N+1}
       =\psi_N^2/\alpha_{N+1}.
\]
The first derivative records the sign of the phase, and the omitted
determinant records its square through this exact map.

## 10. Positive minors and their original source vector

Cauchy–Binet, equivalently determinant multilinearity grouped by
distinct column sets, proves
\[
 \det\left(\sum_{j\in L}b_jb_j^*/\omega_j\right)
 =\sum_{J\subseteq L,\ |J|=q}|\det B_J|^2/\prod_{j\in J}\omega_j.
\]
The increasing order of columns fixes every minor orientation. This
identity requires no nonsingularity of the sum. In the four determinants
forming \(\Delta_N\), column sets containing neither of \(N,N+1\)
have coefficient \(1+1-1-1=0\); those containing exactly one have
coefficient zero; those containing both have coefficient one. Hence
\[
 \Delta_N=
 \sum_{I\subseteq\{0,\ldots,N-1\},\ |I|=q-2}
 \frac{|\det B_{I\cup\{N,N+1\}}|^2}
 {\omega_N\omega_{N+1}\prod_{i\in I}\omega_i}.
\]
For \(q=1\), no one-element set can contain both indices, so this
quantity is zero.

The actual source space
\(\mathcal E_N=(\bigwedge^{q-2}\mathcal P_{N-1})\wedge p_N\wedge p_{N+1}\)
has the orthogonal wedge basis with full product norms appearing in the
denominator. The map \(\Lambda_N=\bigwedge^qT_{N+1}|_{\mathcal E_N}\)
sends each basis wedge to its oriented determinant times the fixed
quotient wedge \(e_C\). Since the inner product is conjugate-linear in
its first argument, the adjoint \(\Lambda_N^*e_C\) has coefficient
the **conjugate** determinant divided by its source squared norm.
This proves the stated formula for \(\zeta_N\), as well as
\[
 \|\zeta_N\|_\theta^2=\Delta_N,\qquad
 \Lambda_N\zeta_N=\Delta_Ne_C.
\]
The unscaled alternating tensor image has squared norm \(q!\Delta_N\)
in the specified tensor observation. At \(q=1\) the zero source and
zero map correctly represent the absent pair of columns.

## 11. Both exact losses, equality conditions, and volume coordinates

Put \(v_N=-\log\delta_N\),
\(s_N=(v_N+v_{N+1})/2\), and \(t_N=(v_{N+1}-v_N)/2\).
Then
\[
 (1-e^{-v_N})(e^{v_{N+1}}-1)
 =2e^{t_N}\cosh s_N-e^{2t_N}-1
 =\sinh^2s_N-(e^{t_N}-\cosh s_N)^2.
\]
Substitution into the retained rank-two radius proves TVB.32 with both
losses and their original coefficient \(\alpha_{N+1}\). Since this
coefficient is strictly positive, equality in the resulting upper bound
holds exactly when \(\psi_N=0\) and \(e^{t_N}=\cosh s_N\).
Multiplying the latter equality by
\(2\sqrt{\delta_N\delta_{N+1}}\) gives
\(\delta_N(2-\delta_{N+1})=1\). The positive-minor equality follows
by substituting \(\epsilon_N^2/\alpha_{N+1}=\Delta_N/D_N^{\rm CV}\).

The exact original volume expressions are
\[
 e^{t_N}=V_N/\sqrt{V_{N-1}V_{N+1}},\qquad
 \cosh s_N=(V_{N-1}+V_{N+1})/(2\sqrt{V_{N-1}V_{N+1}}).
\]
They prove TVB.34a and show that equality requires the arithmetic
midpoint \(2V_N=V_{N-1}+V_{N+1}\) and the actual cross term \(z_N=0\).
An additional geometric midpoint condition alone supplies no such
equality; both midpoint equations force
\((\sqrt{V_{N-1}}-\sqrt{V_{N+1}})^2=0\).

For a direct check of every inverse-volume denominator, put
\(a=D_-\), \(b=D_0\), \(c=D_+\), \(e=\widetilde D_N\). Then
\(\Delta_N=a+c-b-e\), and the omitted determinant gives
\[
 eb-ac=b^2|z_N|^2/(\omega_N\omega_{N+1}).
\]
The left side of the second TVB.34b equality expands to
\(b(a+c)^2/(4ac)-a-c+e\). Its stated right side expands to the
same expression because the terms \(ac/b\) cancel exactly. Both
remaining right terms are nonnegative. Equality is therefore
\(b=2ac/(a+c)\) and \(e=ac/b=(a+c)/2\), yielding
\(\Delta_N=e-b\). In particular, at these admitted degrees zero
phase corresponds to the positive omitted determinant \(e=ac/b\).

## 12. Exterior trace bound and exact two-step telescope

Transport the original metric isometrically by \(G_N^{1/2}\), and let
\(P\) be the orthogonal projector onto the image of the full generalized
right-half-plane subspace of \(A\). In this orthogonal decomposition,
the transformed \(A\) is upper triangular; its selected diagonal block
has precisely the selected eigenvalues with their algebraic
multiplicities. Consequently
\[
 \operatorname{Tr}(PH_N)
 =\sum_{\Re\lambda>k/2}\ell_\lambda(2\Re\lambda-k)=L.
\]
The \(+\epsilon_N\) eigenline contributes at most \(\epsilon_N\)
to this trace, while the \(-\epsilon_N\) eigenline contributes a
nonpositive number. Hence \(L\le\epsilon_N\) on this same minimum
metric at every fixed real tilt. No unproved orthogonality of the CRT
spectral projector enters this argument.

Combining with the exact upper bound, and using \(s_N\ge0\), proves
\[
 \log(V_{N-1}/V_{N+1})
 \ge2\operatorname{arsinh}(L/\sqrt{\alpha_{N+1}}).
\]
For \(N=N_0+2j\), every intermediate volume cancels in the sum of the
logarithms, leaving exactly
\(\log(V_{N_0-1}/V_{N_0+2r-1})\). The last Toda coefficient is
\(\alpha_{N_0+2r-1}\), in agreement with the written summand index
\(N_0+2j+1\). All quantities share the same packet, \(k\), and tilt;
no estimate on changing degrees or on a limiting determinant is inferred.

## 13. First admitted degree and its conjugate-linear source correspondence

At \(N=q-1\), the first \(q\) monic remainder columns form a basis
with determinant one. In that basis
\(b_i^*G_{q-1}b_j=\delta_{ij}\omega_j\). For the full original
expansion
\(\chi=p_q+\sum_{j<q}\gamma_jp_j\), reduction gives
\(b_q=-\sum_{j<q}\gamma_jb_j\). Therefore
\[
 a=\omega_{q-1},\quad z=-\gamma_{q-1}\omega_{q-1},\quad
 d_+=\sum_{j<q}|\gamma_j|^2\omega_j=\nu_0-\omega_q.
\]
The already proved phase identity yields
\(\gamma_{q-1}=-i\psi_{q-1}\). Substituting in the direct rank-two
formula removes only the explicitly displayed last squared term:
\[
 \epsilon_{q-1}^2
 =\frac{\sum_{j<q-1}|\gamma_j|^2\omega_j}{\omega_{q-1}}
 =\frac{\nu_0-\omega_q}{\omega_{q-1}}-\psi_{q-1}^2.
\]
This uses no preceding-volume inverse. The actual source projection
\(\mathsf P_{q-2}\chi\) has the displayed norm and the actual jet
\(\eta\sum_{j<q-1}\gamma_jb_j\); the full relation instead has zero
jet with the complete cochain primitive already proved. This is an exact
map between the two source observations.

Let \(D=D_{q-1}^{\rm CV}=\prod_{j<q}\omega_j^{-1}\). In the endpoint
minor omitting column \(j<q-1\), expansion of \(b_q\) leaves only
\(-\gamma_jb_j\). Moving \(b_j\) from the last position to its
position \(j\) requires \(q-1-j\) transpositions; including the
preceding minus gives the exact sign \((-1)^{q-j}\gamma_j\).
For the resulting source wedge \(e_j\),
\(\|e_j\|_\theta^2=\omega_q/(D\omega_j)\). The map
\[
 \mathcal H\!\left(\sum_{j<q-1}a_jp_j\right)
 =\sum_{j<q-1}(-1)^{q-j}\overline{a_j}
                 \frac{\omega_jD}{\omega_q}e_j
\]
is conjugate-linear. Its proposed inverse follows by conjugating each
coefficient and multiplying by \(\omega_q/(\omega_jD)\), with the
same sign. Orthogonality gives its exact squared-norm multiplier \(D/\omega_q\).
The minor-adjoint formula consequently proves
\[
 \zeta_{q-1}=\mathcal H(\mathsf P_{q-2}\chi),\qquad
 \Delta_{q-1}=(D/\omega_q)\|\mathsf P_{q-2}\chi\|_\theta^2.
\]
The alternating tensor multiplier remains \(q!\). The separate omitted
top coefficient gives
\(\widetilde D_{q-1}=D|\gamma_{q-1}|^2\omega_{q-1}/\omega_q\).
All original coefficients, signs, and norm factors are accounted for.

For \(q=1\), the lower projection, minor space, and conjugate-linear
map are zero; the scalar relative operator is trace zero and hence
\(\epsilon_N=0\) at every admitted degree. The top-coefficient formula
still records the entire omitted determinant. Moreover consecutive source
orthogonal polynomials have no common root: their recurrence with
\(\alpha_j>0\) propagates a common root back to \(p_0=1\), a
contradiction. Thus, for any nonzero quotient, \(b_N\) and
\(b_{N+1}\) cannot both vanish. At \(N\ge q\),
\(K_{N+1}-K_{N-1}\) is a nonzero positive semidefinite update of a
positive-definite matrix. Conjugation by \(K_{N-1}^{-1/2}\) gives
eigenvalues all at least one, with at least one strictly larger; therefore
\(D_{N+1}^{\rm CV}>D_{N-1}^{\rm CV}\) and \(\mathcal R_N>1\).
In particular the volume upper bound is strictly positive and strictly
above \(\epsilon_N=0\) for \(q=1,N\ge1\).

## 14. Empty quotient

When \(h=1\), one has \(\chi=1\), \(q=0\), and \(C=0\). The
original source and its positive measure remain defined. Multiplication
by one identifies the relation source with the whole source, so
\(\mathfrak B_{N+1}=\mathfrak D_{N+1}\), while the quotient determinant
is the empty determinant \(V_N=1\). Its minimum lift, curvature, and
relative control are the unique zero maps. The two Toda coefficients
are equal and their difference vanishes. No nonexistent positive-
dimensional inverse is required. In the support lift of this actual zero
vector space, represented zero is the supported point \(e\), and the
separate absolute point \(\tau\) is retained and maps to itself.

## 15. Spectral-coupling join, TVB.39–44

Fix \(N\ge q\) and the same original metric \(G_N\), with \(L>0\).
Then \(\epsilon_N>0\). In the original metric write
\(\mathcal H_N=A^{\sharp}+A-kI\); this is isometrically conjugate
to the Euclidean Hermitian matrix used above. Let \(P\) be the
\(G_N\)-orthogonal projection onto the complete positive spectral
subspace, and put \(C_N=PA(1-P):V_+^{\perp_G}\to V_+\). Invariance
of \(V_+\) gives \((1-P)AP=0\), hence
\(PA^{\sharp}(1-P)=0\) and therefore
\(P\mathcal H_N(1-P)=C_N\).
The complement is nonzero: if the selected subspace were all of \(C\),
then \(L=\operatorname{Tr}\mathcal H_N=0\), contrary to \(L>0\).
Thus both factors of the Sylvester Hom space have positive dimension,
and its Hilbert-Schmidt unit sphere used below is nonempty.

Choose the two \(G_N\)-unit eigenvectors of \(\mathcal H_N\) at
\(\pm\epsilon_N\), and let \(E:\mathbb C^2\to C\) be their
isometric injection with the explicitly inherited original metric. Put
\(M=E^{\sharp}PE=\left(\begin{smallmatrix}a&c\\\bar c&b\end{smallmatrix}\right)\).
For every \(z\), \(z^*Mz=\|PEz\|_G^2\) and
\(z^*(I-M)z=\|(1-P)Ez\|_G^2\). Thus \(0\le M\le I\), and
the two determinants are nonnegative. Direct spectral expansion gives
\(L=\epsilon_N(a-b)\), while the off-diagonal block norm gives
\[
 \|C_N\|_{\mathrm{HS},G_N}^2
 =\epsilon_N^2(a+b-a^2-b^2+2|c|^2).
\]
Subtracting this and \(L^2\) from \(\epsilon_N^2\) leaves
\[
 \epsilon_N^2-L^2
 =\|C_N\|_{\mathrm{HS},G_N}^2
   +\epsilon_N^2\{\det M+\det(I-M)\}.
\]
Adding the already proved two-loss equation therefore gives, on precisely
the same original metric,
\[
 \alpha_{N+1}\sinh^2s_N-L^2
 =\alpha_{N+1}(e^{t_N}-\cosh s_N)^2+\psi_N^2
 +\|C_N\|_{\mathrm{HS},G_N}^2
 +\epsilon_N^2\{\det M+\det(I-M)\}.
\]
All four terms are nonnegative. Retaining the phase and coupling while
dropping just the other two gives
\[
 \log\mathcal R_N\ge
 2\operatorname{arsinh}
 \left(\frac{\sqrt{L^2+\psi_N^2+\|C_N\|_{\mathrm{HS},G_N}^2}}
 {\sqrt{\alpha_{N+1}}}\right).
\]
The underlying maps also hold at any declared fixed real tilt; the
parent note specializes to \(\theta=0\). Neither form supplies a
uniform lower bound for the coupling or an asymptotic upper estimate.

For the precise projector comparison, write the original orthogonal
block matrix as \(A=\left(\begin{smallmatrix}B&C_N\\0&D^{\rm op}\end{smallmatrix}\right)\)
and the CRT spectral idempotent as
\(Q=\left(\begin{smallmatrix}I&X_N\\0&0\end{smallmatrix}\right)\).
Its commutation relation is exactly
\(BX_N-X_ND^{\rm op}=C_N\). The map on the original
\(\operatorname{Hom}(V_+^{\perp_G},V_+)\) has inverse
\[
 Y\longmapsto\int_0^\infty e^{-tB}Y e^{tD^{\rm op}}\,dt.
\]
The real spectral separation is strictly positive. Expanding each
finite generalized eigenspace exponential as its original scalar
exponential times its full terminating nilpotent polynomial proves
convergence. Differentiation gives the inverse equation with the upper
boundary term zero; an intertwiner in the kernel would produce a
constant integrand tending to zero, proving injectivity. Its actual
positive smallest singular value therefore controls
\(\|Q-P\|_{\mathrm{HS},G_N}=\|X_N\|_{\mathrm{HS},G_N}\) through
\(\|C_N\|\), with no uniform value substituted for that singular value.
This is the exact morphism between the two projectors used by the join.

The join's eigenline construction uses \(L>0\), and its volume ratios
use \(N\ge q\). The first admitted degree remains governed by TVB.38
and its complete source map. At \(L=0\), the direct Toda identity is
available without asserting two nonzero eigenlines when \(\epsilon_N=0\).

## Final-hash closure

The author's bounded source was read completely at SHA256
`9d38489ac9e7e2f529266403ace0f69641e4da6ef7a8cf46f64179ab572c1c71`,
including the complete original-source construction and TVB.39–44 join.
The last two domain sentences were then read at the final source SHA256
`97652a43445708c0e6d2a959f45aed8a4f2a7f73f9cd4b6cd57e67b8fedb408e`:
the seed Mellin integral has domain \(\Re s>-2\), and the selected
subspace's orthogonal complement is nonzero when \(L>0\), making the
Sylvester Hom unit sphere nonempty. These sentences have the full
supporting derivations in Sections 1 and 15 above.
An exact byte-level check reversed only those two edits in the final
source and reconstructed SHA256
`9d38489ac9e7e2f529266403ace0f69641e4da6ef7a8cf46f64179ab572c1c71`.
Thus the final source has no other unseen delta from the complete read.

The standalone source now explicitly supplies the source spaces, theta
factor two, both Euler-inverse tails, exact Hermite remainder and its
unit inverse, tilted tensor target, and antidual. The operator curvature
retains both positive costs and their common term. The endpoint retains
its conjugate-linear source map and all original coefficient norms.
The four-loss identity is proved on the same original metric, with the
full projector-to-coupling Sylvester isomorphism and its original
nilpotent factors. The \(q=0\), \(q=1\), \(N=q-1\), and \(L=0\)
cases use their stated maps and never a nonexistent inverse or eigenline.

Acceptance is for exactly the displayed final source hash and this
bounded mathematics. Source-package replay, numerical calibration,
cumulative typesetting, visual QA, and remote publication each have
their own receipts. No numerical fixture is used in place of any
derivation above; no Lean run or asymptotic arithmetic estimate is
claimed by this review.
