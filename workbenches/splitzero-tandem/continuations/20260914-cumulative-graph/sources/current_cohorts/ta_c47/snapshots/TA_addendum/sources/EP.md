# Exact comparison of inherited EW transport with AGT and AA

13 September 2026. This add-only proof and attribution note compares the complete inherited `gamma_endpoint_window_bridge.tex` (EW.1–EW.59, including EW.35a–c and EW.46a) with the complete sealed AGT1–AGT19 and AA1–AA44 sources. All three bodies were read. No sealed source or package is changed by this note.

The inherited EW source already proves the general canonical projection and principal-angle calculation, nonlinear arcosh transport, strict positivity for the original positive polynomial moments, and the explicit signed tensor theta primitive. The later AGT calculation explicitly sharpens the chosen window by changing the pairing of the same four projections: its guaranteed scalar angle count is \(2q-1\), whereas EW.35a–c use \(2q\) at that window. The proof below establishes precisely this refinement and its attribution. Strict positivity and existence of the theta primitive are not additional results of AGT or AA relative to EW.

## 1. Exact source pins and reading scope

The base directory in this table is `source-workspace`.

| Source | Relative path | SHA-256 | Reading scope |
|---|---|---|---|
| EW | `output/tau_split_zero_counterfactual_reconstruction_20260913/original_programme/tex/gamma_endpoint_window_bridge.tex` | `400541cdcb35d44c0f7e68f5db1107df4fcf707d0be83b5a8a970d8ec9c73160` | Entire source, EW.1–59 and all prose, including appended-letter equations |
| Identical inherited reader copy | `output/tau_split_zero_counterfactual_reconstruction_20260913/original_programme/sources/reader_preparation/gamma_endpoint_window_bridge.tex` | `400541cdcb35d44c0f7e68f5db1107df4fcf707d0be83b5a8a970d8ec9c73160` | Byte equality to the fully read EW source |
| AGT | `work/tau_all_degree_angle_transport_20260913.tex` | `cc0c0c008b0532c5f120d1cea76b94e2d08153c87a694ce18775a5189c72d5f8` | Entire corrected AGT1–19 source |
| AA | `work/tau_all_degree_angle_independent_review_20260913.md` | `b0634428d69f80dedd4f68766ef9e6468c390eaac86dfe58b08c21c8fb896e03` | Entire AA1–44 proof and acceptance scope |

The EW introduction identifies its input criterion as PR 23 source revision `c720f40530eed2f5969dbabe94dfd3fddc0f507f`. That is an internal provenance statement in the read source; this comparison does not assign an independently verified publication date or external mathematical priority to it. In particular, “additional” below means additional explicit content relative to these pinned bodies. The inherited source also attributes EW.35a–c to its independent projection review. This attribution is retained.

The rational calculations EW.49–59 and their written derivations were read. Their reported checker executions were not rerun in this comparison, and their counts are not transferred to AGT or AA. The other archived EW copies and checker programs are not silently substituted for the pinned source above.

## 2. Original source, parameters, metrics and maps

Use EW's original full packet \(h\), \(g=2\xi\), integer \(k\ge1\), original line \(S=k/2+iu\), and actual cyclic relation \(\chi\) of degree \(q\ge1\). Its quotient \(\mathcal C=\mathbb C[S]/(\chi)\) and AGT/AA's \(E\) have precisely the same ordered remainder coordinates. The coefficient map

\[
I_E:\mathcal C\longrightarrow E,\qquad
\sum_{j=0}^{q-1}x_j[S^j]\longmapsto\sum_{j=0}^{q-1}x_j[S^j]
\tag{EP1}
\]

is the identity algebra isomorphism, with inverse the same coefficient map. It retains all multiplicities of \(\chi\). For the ambient source specialize EW's parameters by

\[
n=q,\qquad r=q,\qquad m_{\mathrm{EW}}=n+r=2q,
\qquad s_{\mathrm{EW}}=\min(q,r)=q,
\qquad \lambda=\tfrac14.
\tag{EP2}
\]

The symbol \(m_{\mathrm{EW}}\) is an ambient polynomial cutoff; the symbol \(m\) in AGT and AA is instead the count \(2q-1\) in a later scalar inequality. They do not denote the same integer. The exact relation between them at EP2 is \(m_{\mathrm{AGT}}=m_{\mathrm{EW}}-1\), while the ambient vector-space dimension is \(m_{\mathrm{EW}}+1=2q+1\).

The gamma densities coincide literally under EP2. Indeed EW.5 gives

\[
c_{1/4}=2^{1-2/4}\Gamma(2/4)=\sqrt{2\pi},\qquad
r_{1/4}^{*k}(u)
=\frac{(\sqrt{2\pi})^k}{c_{k/4}}
 \frac{|\Gamma(k/4+iu/2)|^2}{2\pi}=m_0(u),
\tag{EP3}
\]

using EW.7. The gamma mass is \((2\pi)^{k/2}\), and EW.1's arithmetic density is AGT2/AA2's \(m_1=w_h^{*k}\), with mass \(\mu_h^k\). Therefore the common identity coefficient map on \(\mathcal P_{2q}\) identifies the two measures at both endpoints without a mass rescaling. Along the segment \(m_t=(1-t)m_0+tm_1\), define \(M(t)\) as its Gram in the fixed monomial frame. EW's general positive-family theorem applies with

\[
H_{m_{\mathrm{EW}}}(t)=M(t),\qquad
H_N(t)=\iota_N^*M(t)\iota_N,
\qquad \dot H_{m_{\mathrm{EW}}}=\dot M=M(1)-M(0),
\tag{EP4}
\]

where \(\iota_N:\mathbb C^{N+1}\to\mathbb C^{2q+1}\) is the original coefficient inclusion. The scalar relation \(\chi\), the monic remainder \(J_N\), and multiplication \(B_N=\times\chi\) are fixed along this same path.

EW.11 supplies

\[
K_N^{\mathrm{EW}}=J_NH_N^{-1}J_N^*,\qquad
G_N=(K_N^{\mathrm{EW}})^{-1},\qquad
R_N^{\mathrm{EW}}=H_N^{-1}J_N^*G_N,
\qquad R_N^{\mathrm{AGT}}=R_N^{\mathrm{AA}}=\iota_NR_N^{\mathrm{EW}}.
\tag{EP5}
\]

The last equality follows both by the displayed matrix formula and by uniqueness of the minimum section: the included EW vector has remainder \(x\), is orthogonal to \(B_N\mathcal P_{N-q}\), and any other lift differs by a vector in that space. The squared norm of the latter is added orthogonally, so it cannot be another minimum unless the difference is zero. Hence every \(G_N\) and \(V_N=\det G_N\) is the same original quantity. In particular, EW's \(K_N^{\mathrm{EW}}\) is the inverse quotient Gram; AGT's \(K_{ij}=G_i^{-1/2}G_jG_i^{-1/2}\) is a two-cutoff relative Gram. Their exact relation is the displayed substitution of \(G_N=(K_N^{\mathrm{EW}})^{-1}\), with this factor order preserved.

There is a further operator-type distinction requiring an explicit map. EW.30 defines a contravariant matrix

\[
Q_N^{\mathrm{EW}}
=R_NG_N^{-1}R_N^*,\qquad
\Pi_N=Q_N^{\mathrm{EW}}M
=Z_N^{\mathrm{AGT}}=N_N^{\mathrm{AA}}.
\tag{EP6}
\]

Here and below \(R_N\) on the common ambient space includes \(\iota_N\). To prove EP6, compute \(\Pi_N^2=R_NG_N^{-1}(R_N^*MR_N)G_N^{-1}R_N^*M=\Pi_N\). Its adjoint for \(M\) is itself, and its range is \(R_NE\). Thus it is exactly the orthogonal projection that AGT denotes by \(Z_N=P_N-Q_N\) and AA by \(N_N\). EW's \(Q_N^{\mathrm{EW}}\) is converted to that endomorphism by right multiplication by the original \(M\); it is not identified with AGT's relation projection \(Q_N^{\mathrm{AGT}}\).

For completeness EW's \(P_j^{\mathrm{EW}}\) is the contravariant matrix of the single monic orthogonal line. Those lines span the cutoff source, so the remaining exact conversions are

\[
P_N^{\mathrm{AGT}}=\sum_{j=0}^N P_j^{\mathrm{EW}}M,
\qquad
Q_N^{\mathrm{AGT}}=P_N^{\mathrm{AGT}}-Q_N^{\mathrm{EW}}M.
\tag{EP7}
\]

They follow by decomposing a polynomial in the complete monic orthogonal family and then subtracting its minimum-section component. Every factor \(M\) remains in the written map.

Set \(C=M^{-1}\dot M\), the AGT4/AA21 operator. The map \(v\mapsto M^{1/2}v\) is an isometry from \((\mathcal P_{2q},M)\) to its displayed Euclidean coefficient space, and

\[
M^{1/2}CM^{-1/2}=M^{-1/2}\dot M M^{-1/2},\qquad
\mathfrak o_H(\dot H)=c_{\max}(C)-c_{\min}(C).
\tag{EP8}
\]

The trace also has the exact original-coordinate conversion

\[
\operatorname{Tr}(Q_N^{\mathrm{EW}}\dot M)
=\operatorname{Tr}(\Pi_N C).
\tag{EP9}
\]

Indeed \(\Pi_N C=Q_N^{\mathrm{EW}}MM^{-1}\dot M\). Thus EW.31–32 and AGT4/AA23 have identical signed determinant derivatives. The positive relative operators \(M(0)^{-1}M(1)\) and \(M(0)^{-1/2}M(1)M(0)^{-1/2}\) are conjugate by \(M(0)^{1/2}\), so EW.34 and AGT/AA use exactly the same positive relative eigenvalues and \(\kappa\).

## 3. Existing angle proof and the exact changed pairing

The equation-level crosswalk is as follows.

| Inherited EW statement | AGT statement | AA statement | Mathematical scope |
|---|---|---|---|
| EW.1–7 and EW.3–4 | AGT1–3 | AA1–5 | Same source at EP2–4, full packet, unit, exact quotient and masses |
| EW.25–27 and proof of EW.28 | AGT5–8 | AA6, AA8–16 | Same canonical projection, Gram cosines, all common directions, and signed \(2\times2\) projection blocks |
| EW.31–32 | AGT4 | AA21–24 | Same four signed derivatives after EP6–9 |
| EW.28 rank bound and EW.35a concavity | AGT9–11, AGT15–16 | AA17–26 | Later crossed pairing gives \(2q-1\) instead of EW.35a's \(2q\) at \(n=r=q\) |
| EW.35b–c | AGT14, AGT17–19 | AA32–37 | Same integration and inverse-cosh construction, with that changed count |
| EW.46a and its proof | AGT12–13 | AA27–31 | Strict positivity already proved; later direct involution proof supplies another calculation at the selected cutoffs |
| EW.46–48, with EW.3 | AGT paragraph after AGT8 | AA38–44 | Same exact theta primitive; AA adds expanded division details and the explicit energy matrix coordinate |

To establish the shared angle calculation without presuming a change of presentation is an identity, put \(L_i=R_iE\). EW.26 proves \(R_j=\Pi_jR_i\) for \(i\le j\), since both vectors have remainder \(x\) and their difference is in the relation space orthogonal to \(L_j\). Thus

\[
R_i^*MR_j=G_j,\qquad
G_i-G_j=(R_i-R_j)^*M(R_i-R_j).
\tag{EP10}
\]

For isometries \(F_i=R_iG_i^{-1/2}\), the two cross matrices in AGT7 and AA9 are actual adjoints:

\[
F_j^*MF_i=G_j^{1/2}G_i^{-1/2},\qquad
F_i^*MF_j=G_i^{-1/2}G_j^{1/2},\qquad
K_{ij}=G_i^{-1/2}G_jG_i^{-1/2}.
\tag{EP11}
\]

Their squared singular values are the eigenvalues \(c_a^2\in(0,1]\) of \(K_{ij}\). If \(x_a\in L_i\) are orthonormal eigenvectors for the squared projection restriction and \(y_a=\Pi_jx_a/c_a\), then \(y_a\) form an orthonormal basis of \(L_j\), with \(\langle x_a,y_b\rangle=c_b\delta_{ab}\). For \(c_a=1\), equality in orthogonal Pythagoras gives \(x_a=y_a\in L_i\cap L_j\), and conversely every common vector contributes eigenvalue one. For \(s_a=\sqrt{1-c_a^2}>0\), put \(z_a=(y_a-c_ax_a)/s_a\). Computing these inner products gives orthonormal, mutually orthogonal two-dimensional planes, on which

\[
(\Pi_i-\Pi_j)|_{\operatorname{span}(x_a,z_a)}
=\begin{pmatrix}s_a^2&-s_ac_a\\-s_ac_a&-s_a^2\end{pmatrix}.
\tag{EP12}
\]

This has eigenvalues \(s_a,-s_a\); every remaining direction has eigenvalue zero. Taking determinants in EP11 yields \(\log(V_i/V_j)=\sum_a-\log c_a^2\). These are precisely the calculations already written in the complete EW.26–28 proof.

EW also proves that at most \(\min(q,j-i)\) of the angles move. Indeed \(L_i\) is already orthogonal to the relation columns up through degree \(i\). The extra \(j-i\) independent monic boundary columns impose at most \(j-i\) linear equations on \(L_i\), and their joint kernel is exactly \(L_i\cap L_j\). Hence the common-subspace dimension is at least \(q-(j-i)\) if positive. This exact rank bound includes all common vectors, and for \(i=j\) all angles are zero.

At EP2, the original loss and derivative are

\[
B=\log\frac{V_{q-1}V_q}{V_{2q-1}V_{2q}}
=\mathscr L_{n=q,r=q},\qquad
B'=\operatorname{Tr}((\Pi_{q-1}+\Pi_q-\Pi_{2q-1}-\Pi_{2q})C).
\tag{EP13}
\]

EW.33–35a use the pairs \((q-1,2q-1)\) and \((q,2q)\). Each has gap \(q\), hence its displayed estimate uses up to \(q\) moving angles and a list of length \(2q\). AGT instead uses

\[
(q-1,2q),\qquad(q,2q-1),
\tag{EP14}
\]

whose gaps are \(q+1\) and \(q-1\). EW's already proved rank bound gives \(q\) and \(q-1\) moving slots respectively. In AGT9 the latter is also proved directly by placing both \(q\)-dimensional spaces in the common \(2q-1\)-dimensional hyperplane. It is the same incidence bound. The reordered sum in EP13 is exactly unchanged. One zero angle from the full second list can therefore be omitted from the scalar sum, retaining every original vector space and every other zero contribution, for a count \(2q-1\).

For a self-adjoint \(C\) with width \(w=c_{\max}-c_{\min}\), each positive/negative spectral pair in EP12 contributes to the trace by \(s_a(\langle v_a,Cv_a\rangle-\langle w_a,Cw_a\rangle)\), in absolute value at most \(s_aw\), since both Rayleigh quotients are in the same interval. Summing gives the shared angle estimate. For \(f(x)=\sqrt{1-e^{-x}}\), its full second derivative is

\[
f''(x)=-\frac{e^{-x}}{2\sqrt{1-e^{-x}}}
-\frac{e^{-2x}}{4(1-e^{-x})^{3/2}}
=-\frac{e^{-x}(2-e^{-x})}{4(1-e^{-x})^{3/2}}<0.
\tag{EP15}
\]

The two displayed formulas in EW/AGT and AA are therefore identical. Concavity extends to zero by continuity, and finite Jensen on any retained list of \(a\) slots with total cost \(B\) gives

\[
|B'|\le a\sqrt{1-e^{-B/a}}\,w.
\tag{EP16}
\]

EW.35a gives this with \(a=2q\) at EP2, while AGT16/AA26 give it with \(a=2q-1\). The general theorem and concavity method predate the latter specialization in the pinned source graph.

## 4. Full general-window consequence of the crossed pairing

The same refinement can be expressed directly in EW's general domain \(n\ge q\ge1\), \(r\ge1\), \(m_{\mathrm{EW}}=n+r\). Retain its exact \(\mathscr L=\log(V_{n-1}V_n/(V_{n+r-1}V_{n+r}))\). Use the two nested pairs

\[
(n-1,n+r),\qquad(n,n+r-1),\qquad
a(q,r)=\min(q,r+1)+\min(q,r-1).
\tag{EP17}
\]

For \(r=1\) the second pair is identical, contributes its full list of unit cosines, and contributes zero moving slots. In every case \(a(q,r)\ge1\). The two gap rank bounds just proved show that their nonzero angle costs fit in \(a(q,r)\) slots. Append zero scalar terms if there are fewer. Their sum is the same original \(\mathscr L\), because the two log determinant ratios telescope to the four original endpoints. The trace signs are also the same. The preceding spectral-pair estimate and EP15 therefore prove

\[
|\mathscr L'|\le a(q,r)\sqrt{1-e^{-\mathscr L/a(q,r)}}\,
\mathfrak o_H(\dot H).
\tag{EP18}
\]

The count has the exact elementary form

\[
a(q,r)=
\begin{cases}
2\min(q,r)-1=2q-1,&r=q,\\
2\min(q,r),&r\ne q.
\end{cases}
\tag{EP19}
\]

For \(r<q\), the two terms are \(r+1,r-1\); for \(r=q\), they are \(q,q-1\); and for \(r>q\), both are \(q\). This proves all cases, including \(q=r=1\). In particular the explicit improvement is available for every \(n\ge q\) when \(r=q\), while AGT states it at \(n=q\). This paragraph is an add-only consequence derived here from EW.28 and its transport proof, and is not attributed as an extra assertion already present in the AGT body.

For any positive integer \(a\), define the exact increasing map and its inverse by

\[
\Psi_a(B)=2\operatorname{arcosh}(e^{B/(2a)}),\qquad
\Psi_a^{-1}(v)=2a\log\cosh(v/2),\qquad B,v\ge0.
\tag{EP20}
\]

The real branch is \(\operatorname{arcosh}(z)=\log(z+\sqrt{z^2-1})\) for \(z\ge1\). Differentiating \(\cosh(\Psi_a(B)/2)=e^{B/(2a)}\) gives \(\Psi_a'(B)=[a\sqrt{1-e^{-B/a}}]^{-1}\) for \(B>0\). For possible zero losses along a general positive \(C^1\) family, apply the derivative to \(\Psi_a(\mathscr L+\varepsilon)\). EP18 bounds the absolute derivative by

\[
\mathfrak o_H(\dot H)
\sqrt{\frac{1-e^{-\mathscr L/a}}{1-e^{-(\mathscr L+\varepsilon)/a}}}
\le\mathfrak o_H(\dot H).
\tag{EP21}
\]

Integrate and let \(\varepsilon\downarrow0\) by continuity. For the original straight positive segment, put \(D=(H^{(0)})^{-1}H^{(1)}\). It is self-adjoint positive for \(H^{(0)}\), and every positive relative eigenvalue \(b\) gives exactly \(c_b(t)=(b-1)/(1-t+tb)\). Since its derivative with respect to \(b\) is \((1-t+tb)^{-2}>0\), the same extreme \(b\)'s determine the width throughout the path. Its integral is

\[
\int_0^1\mathfrak o_{H(t)}(\dot H)\,dt
=\int_0^1\frac{d}{dt}\log\frac{1-t+tb_{\max}}{1-t+tb_{\min}}\,dt
=\log\kappa.
\tag{EP22}
\]

Thus the crossed-pair general-window consequence is

\[
|\Psi_{a(q,r)}(\mathscr L^{(1)})-
  \Psi_{a(q,r)}(\mathscr L^{(0)})|\le\log\kappa.
\tag{EP23}
\]

It holds including zero loss for every such positive matrix pair. At \(n=r=q\), it is AGT14/AA35; with \(a=2s_{\mathrm{EW}}\), EP20 is exactly EW's \(\Phi_s\), and the proof is EW.35b's existing integration argument. This identifies both the inherited map and its changed parameter rather than giving a new name to the inherited result.

The endpoint interval is equally the same exact inverse construction. Put \(A_0=\operatorname{arcosh}(e^{\mathscr L^{(0)}/(2a)})\) and \(d=\tfrac12\log\kappa\). Equation EP23 is equivalent to

\[
2a\log\cosh(\max\{0,A_0-d\})
\le\mathscr L^{(1)}\le2a\log\cosh(A_0+d).
\tag{EP24}
\]

Exponentiating and writing \(z_0=e^{A_0}\), \(z_-=\max\{1,z_0/\sqrt\kappa\}\), \(z_+=\sqrt\kappa\,z_0\) gives

\[
\left(\frac{z_-+z_-^{-1}}2\right)^{2a}
\le\mathscr R^{(1)}\le
\left(\frac{z_++z_+^{-1}}2\right)^{2a}.
\tag{EP25}
\]

For \(a=2s\), the exponent \(2a=4s\) is exactly EW.35c. The replacement \(a=2q-1\) is therefore a coefficient refinement of that inherited endpoint certificate. The original source-norm factor \(U=\omega_{n+r}/\omega_n\) remains present in EW.20's actual endpoint \(U^{1/(2r)}\sinh(\mathscr L/(2r))\); AGT's estimate concerns its four-volume argument and does not replace the complete EW endpoint construction.

The improvement is strict at the level of these scalar constraints for distinct positive losses. To prove it, for fixed \(B>0\) let \(F_a(B)=a\sqrt{1-e^{-B/a}}\) and set \(x=B/a>0\). Direct differentiation gives

\[
\frac{\partial F_a(B)}{\partial a}
=\frac{2-(2+x)e^{-x}}{2\sqrt{1-e^{-x}}}>0.
\tag{EP26}
\]

The numerator is positive because \(e^x>1+x/2\) for \(x>0\): the difference has value zero at zero and derivative \(e^x-1/2>0\). Therefore \(F_{2q-1}(B)<F_{2q}(B)\). Since \(\Psi_a'(B)=1/F_a(B)\), for \(0<B_0<B_1\)

\[
\Psi_{2q-1}(B_1)-\Psi_{2q-1}(B_0)
>\Psi_{2q}(B_1)-\Psi_{2q}(B_0).
\tag{EP27}
\]

Integration proves this inequality; continuity gives the non-strict comparison when endpoints coincide or a zero endpoint is admitted. Thus the \(2q-1\) constraint implies the inherited \(2q\) constraint and is tighter for a nonzero change of positive losses. No claim of sharpness for actual arithmetic measures or any bound uniform in growing \(k,q,n\) is inferred from this comparison.

## 5. Strict positivity: prior theorem and alternate later proof

EW.46a already proves \(\mathscr L>0\) for every admitted nonempty actual positive polynomial window. Its proof uses the actual real-\(u\) moment form. Here is its full link to the later one.

Let \(\pi_j\) be its real monic orthogonal polynomials, with positive squared norms \(\omega_j\). The matrix of multiplication by real \(u\) is self-adjoint. Degree and orthogonality imply

\[
u\pi_j=\pi_{j+1}+b_j\pi_j+a_j\pi_{j-1},\qquad
b_j\in\mathbb R,\quad a_j=\omega_j/\omega_{j-1}>0
\quad(j\ge1).
\tag{EP28}
\]

Indeed the coefficient against \(\pi_l\), \(l\le j-2\), vanishes by moving \(u\) to \(\pi_l\), whose degree is at most \(j-1\). The coefficient of \(\pi_{j-1}\) is \(\langle\pi_{j-1},u\pi_j\rangle/\omega_{j-1}=\omega_j/\omega_{j-1}\), since the leading coefficient of \(u\pi_{j-1}\) against \(\pi_j\) is one. The diagonal coefficient is real by self-adjointness. The \(j=0\) equation lacks its last term.

On the original \(S=c+iu\) line, the exact monic phase map \(p_j(S)=i^j\pi_j((S-c)/i)\) has modulus-one factor and retains \(\omega_j\). Multiplying EP28 by its full factor gives

\[
Sp_j=p_{j+1}+(c+ib_j)p_j-a_jp_{j-1}.
\tag{EP29}
\]

If nonconstant \(\chi\) divided consecutive \(p_j,p_{j+1}\), EP29 and \(a_j\ne0\) force divisibility of \(p_{j-1}\), and descending induction forces divisibility of \(p_0=1\), impossible. The two residual monomial columns at degrees \(N,N+1\), after projecting away \(\mathcal P_{N-1}\), are \(p_N\) and \(p_{N+1}+zp_N\), with \(z=\langle p_N,S^{N+1}\rangle/\omega_N\). Their quotient residual map \(F_2\) cannot vanish, or both consecutive \(p\)'s would have zero remainder and be divisible by \(\chi\). Thus \(F_2^*G_{N-1}F_2\) is nonzero positive semidefinite. EW.17 then gives \(V_{N-1}/V_{N+1}>1\), because the determinant of identity plus a nonzero positive semidefinite matrix is strictly greater than one. Multiplying the exact overlapping factors gives

\[
\frac{V_{n-1}V_n}{V_{n+r-1}V_{n+r}}
=\prod_{j=0}^{r-1}\frac{V_{n+j-1}}{V_{n+j+1}}>1.
\tag{EP30}
\]

This is precisely EW.46a. It applies to every positive measure along the AGT convex moment path as well, since that measure remains positive on nonzero polynomials and has every needed moment. Consequently AGT/AA's strict positivity statement already follows from the inherited proof.

AGT12–13 and AA28–30 give a different direct proof for the specific first pair in EP14. If \(B=0\), all its angles vanish, and \(L_{q-1}=L_{2q}\). The first space is \(\mathcal P_{q-1}\); the second is orthogonal to \(\chi\mathcal P_q\). Thus \(1\perp\chi\mathcal P_q\). For \(\chi(S)=\sum_{j=0}^q a_jS^j\), define the full antilinear involution

\[
\chi^{\#_k}(S)=\sum_{j=0}^q\overline{a_j}(k-S)^j.
\tag{EP31}
\]

It has degree \(q\), leading coefficient \((-1)^q\overline{a_q}\), and equals \(\overline{\chi(S)}\) on \(S=k/2+iu\), because \(\overline S=k-S\). Hence \(1\perp\chi\mathcal P_q\) would imply \(0=\langle1,\chi\chi^{\#_k}\rangle=\int|\chi(k/2+iu)|^2m_t(u)\,du>0\). This contradiction is a shorter alternate proof at the chosen cutoffs. Its exact involution calculation is additional proof detail relative to EW's recurrence proof; the strict positivity conclusion is already inherited, in a broader window domain.

## 6. The theta primitive is the same original cochain

EW.46's coefficient \(\kappa_x\) and AA7's \(X_{ij}x\) are equal under EP5. To prove this with its full coefficient metric, put \(\mathsf H_j=B_j^*MB_j\), using the original inclusion of \(B_j\) in the common source. Then

\[
X_{ij}=\mathsf H_j^{-1}B_j^*MR_i:E\to\mathcal P_{j-q},\quad
R_i-R_j=B_jX_{ij},\quad
G_i-G_j=X_{ij}^*\mathsf H_jX_{ij}.
\tag{EP32}
\]

The orthogonal projection onto the relation space is \(B_j\mathsf H_j^{-1}B_j^*M\). Applying it to \(R_i\) gives \(R_i-R_j\), by EP10. This proves the second equality and then its Gram energy. For the empty relation domain the maps are its unique zero maps and no nonzero inverse is needed. Monic division makes multiplication by \(\chi\) injective, so both the EW relation \(R_ix-R_jx=\chi\kappa_x\) and EP32 force \(\kappa_x=X_{ij}x\). In AA the name \(H_j\) denotes \(\mathsf H_j\) here; EW's name \(H_j\) denotes the full source Gram from EP4. EP32 specifies the exact relationship and avoids identifying those two forms.

Retain the original \(D=-x\partial_x\), \(\mathcal MF_h=g/h\), and seed

\[
\phi_0=\phi_*=(4\pi^2x^4-6\pi x^2)e^{-\pi x^2},\qquad
h(D)F_h=\Theta\phi_0.
\tag{EP33}
\]

EW explicitly supplies the same successive divisions as AA40. Start with \(F_0=\chi(s_1+\cdots+s_k)\), and divide successively in the fixed order \(s_1,\ldots,s_k\): \(F_{j-1}=h(s_j)L_j+F_j\), \(\deg_{s_j}F_j<\deg h\). The polynomial \(h(s_j)\) is monic with complex coefficients, so each division is unique over the ring in the other variables and does not increase an earlier restricted degree. The final remainder is in the tensor monomial basis of \(E_h^{\otimes k}\). It has zero quotient image because \(\chi\) annihilates the original sum operator on the unit; thus that remainder is zero. Therefore

\[
\chi(\textstyle\sum s_j)=\sum_{j=1}^k h(s_j)L_j(\mathbf s).
\tag{EP34}
\]

EW's \(Q_j\) and AA's \(L_j\) are the same coefficient polynomials if the same stated successive-division order is used. This follows inductively from the uniqueness of each monic division; every \(F_{j-1}\) is then the same polynomial in the two constructions. In particular no simple-root replacement is made and every full-order nilpotent relation remains in EP34.

For the one-leg complex \([V\xrightarrow{\Theta}\mathscr B]\) in degrees zero and one, both sources consequently write the identical degree-\(k-1\) cochain

\[
\mathcal P_\chi(P)=\mathcal K_\chi(P)
=\sum_{j=1}^k(-1)^{j-1}L_j(\mathbf D)P(\textstyle\sum D_i)
\bigl(F_h^{\otimes(j-1)}\otimes\phi_0\otimes F_h^{\otimes(k-j)}\bigr).
\tag{EP35}
\]

The only factor on which the tensor differential acts in the \(j\)-th summand is \(\phi_0\) in degree zero. There are exactly \(j-1\) preceding degree-one factors, so the differential contributes \((-1)^{j-1}\), cancelling the written coefficient. Polynomial \(D_i\)'s have degree zero and commute with the differential through \(D\Theta=\Theta D\). Equations EP33–34 then give, term by term,

\[
d\mathcal P_\chi(P)
=P(\textstyle\sum D_i)\sum_jh(D_j)L_j(\mathbf D)F_h^{\otimes k}
=\mathcal V_{h,k}(\chi P).
\tag{EP36}
\]

This is EW.47–48 and AA42–43, with the same seed, signs, coefficients, and factor \(g=2\xi\). Substituting \(P=\kappa_x=X_{ij}x\) gives precisely the same boundary of the change of canonical representative. For \(k=1\), the cyclic annihilator is the original monic \(h\), the division gives \(L_1=1\), and the identity reduces to EP33 with the polynomial factor \(P(D)\).

EW.3 and AGT1/AA44 also preserve the exact same full-unit observation \(\eta[P]=[g/h]_h^{\otimes k}P(s_1+\cdots+s_k)\). The further supported cohomology observation is the previously supplied \(\sigma_h^{\otimes k}\eta\). The one-leg inclusion used in AA maps \(\phi\mapsto(\phi,0)\) into the original two-leg complex and is the identity in degree one, so the original difference differential still sends this pair to \(\Theta\phi\). It therefore carries EP35–36 to the original tau-base complex with no sign change. At every retained support label \(A\), the map \((A,v)\mapsto(A,fv)\), \(\tau\mapsto\tau\), sends a zero coefficient to the represented zero at \(A\) and external absence to external absence. This exact support rule is already stated after EW.48.

The explicitly displayed additional coordinate in AA7/AA44 is the energy \(X_{ij}^*\mathsf H_jX_{ij}\) in EP32 and its simultaneous presentation with the primitive. That energy is already an immediate orthogonal Pythagoras consequence of EW.11 and EW.26, as proved in EP10 and EP32. It must not be described as a new existence theorem for a theta primitive or a new connection of the angles to cohomology. Its metric is \(M(t)\) along the interpolation, and the ordinary original arithmetic norm at \(t=1\); the two are related by the specified segment, not silently identified at other parameters.

## 7. Attribution text and cumulative integration scope

The following paragraph is suitable for R74 and the cumulative text:

> The inherited endpoint-window calculation already proves the canonical principal-angle comparison, nonlinear arcosh transport, strict positivity for the actual polynomial moments, and the signed tensor theta primitive (EW.25–28, EW.35a–c, EW.46a–48). The later AGT/AA calculation independently rederives these structures and sharpens the selected window \(n=r=q\): crossing the same four projection terms changes the guaranteed moving-angle count from \(2q\) to \(2q-1\), yielding the corresponding stronger arcosh bound. Its direct reflected-polynomial positivity proof and explicit relation-energy coordinates provide additional proof detail. The original masses, full jets, theta primitive, and tau support remain those of the inherited construction.

If the add-only general-window consequence EP17–25 is included, append:

> Applying the same crossed pairing to the inherited arbitrary-window theorem gives the count \(\min(q,r+1)+\min(q,r-1)\). It improves the earlier count \(2\min(q,r)\) by one exactly when \(r=q\), for every \(n\ge q\). This is an explicit refinement derived from EW's rank bound and transport argument.

These attribution statements replace any implication that AGT or AA first supplied an all-degree principal-angle method, first obtained nonlinear arcosh transport, first proved strict moment positivity, or first constructed the tensor theta primitive. The original source has broader retained content: arbitrary windows, the norm factor \(U\), coefficient-to-Gram maps, rational enclosures, and zero-loss positive-matrix families. That content remains part of the cumulative program; the selected-window refinement does not supersede it. The preserved global analytic limitation is the absence here of a uniform growing-packet bound on the original relative Gram or its \(\kappa\). Neither source claims such a bound from the finite transport formula alone.

The companion receipt pins the compared bodies and this add-only note. The mathematical derivations above are written proofs. No numerical, Lean, remote-publication, or sealed-package mutation is claimed by this comparison.
