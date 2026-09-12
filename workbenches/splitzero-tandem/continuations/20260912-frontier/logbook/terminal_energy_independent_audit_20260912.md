# Terminal energy recurrence: independent exact audit, 2026-09-12

This report audits and extends the terminal recurrence in the current Split-Zero arithmetic kernel calculation. It is a proof text; its finite examples and checks have the scope stated below. The original arithmetic measure is
\[
d\nu_Z(t)=|g(\tfrac12+it)/h(\tfrac12+it)|^2\,dt/(2\pi),
\quad E=\mathbb C[s]/(h),\quad A=M_s,\quad c=j_h1.
\]
Every multiplicity in the selected divisor remains in the algebra. All matrices below use the retained monomial coordinates of this algebra. Put \(d=\dim E\), let \(q_k\) be its monic vertical orthogonal polynomials, and write
\[
s q_k=q_{k+1}+b_kq_k-a_kq_{k-1},\quad
a_k=\kappa_k/\kappa_{k-1}>0,\quad b_k+\bar b_k=1.
\]
The source for these objects and the preceding full-resolvent formula is `output/split_zero_rh_tandem_2026-09-12/tex/kernel_resolvent.tex`. No existing source file was edited in this audit.

## 1. Exact matrix step and its domain

Write
\[
v_k=q_k(A)c,\qquad
K_{n-1}=\sum_{k=0}^{n-1}v_kv_k^*/\kappa_k,
\qquad n\geq d.
\]
The residue map on polynomials of degree below \(n\) is onto \(E\), so \(K_{n-1}>0\). These polynomial definitions remain valid at every selected critical centre, including centres that equal quadrature nodes. The full nilpotent matrix \(A\) is retained.

First take the domain where both \(Q_n=q_n(A)\) and \(Q_{n+1}=q_{n+1}(A)\) are invertible. It contains every off-line packet. Set
\[
R_n=Q_n^{-1}Q_{n-1},\quad r_n=R_nc,\quad
S_n=\kappa_{n-1}Q_n^{-1}K_{n-1}Q_n^{-*}.
\]
The original recurrence evaluated at \(A\), without removing any nilpotent power, gives
\[
T_n=A-b_nI+a_nR_n=Q_{n+1}Q_n^{-1},\qquad
R_{n+1}=T_n^{-1}.
\]
The polynomial kernel update is
\[
K_n=K_{n-1}+v_nv_n^*/\kappa_n.
\]
Multiply this equality on the left by \(\kappa_n Q_{n+1}^{-1}\) and on the right by \(Q_{n+1}^{-*}\), use \(v_n=Q_nc\) and \(\kappa_n=a_n\kappa_{n-1}\), and obtain the exact matrix step
\[
\boxed{S_{n+1}=T_n^{-1}(a_nS_n+cc^*)T_n^{-*}.}
\]
This proof uses the original kernel, so no uniqueness claim for a Sylvester equation is needed. In particular it does not require that the two spectra in such an equation be disjoint.

## 2. Complete scalar recurrence

Temporarily suppress the index \(n\), writing \(a=a_n\), \(b=b_n\), \(S=S_n\), \(r=r_n\), \(T=T_n\), and
\[
\langle u,v\rangle=u^*S^{-1}v,
\quad \alpha=\langle r,r\rangle,
\quad \beta=\langle c,c\rangle,
\quad \gamma=\langle c,r\rangle,
\quad t=Tc=(A-bI)c+ar.
\]
The inner product is linear in its second argument. The rank-one inverse is obtained by direct multiplication:
\[
(aS+cc^*)^{-1}
=\frac1a\left(S^{-1}-\frac{S^{-1}cc^*S^{-1}}{a+\beta}\right).
\]
Indeed multiplication by \(aS+cc^*\) leaves the identity plus a multiple of \(cc^*S^{-1}\), whose coefficient is
\(1/a-1/(a+\beta)-\beta/[a(a+\beta)]=0\).
Since \(S_{n+1}^{-1}=T^*(aS+cc^*)^{-1}T\) and \(r_{n+1}=T^{-1}c\), it follows that
\[
\boxed{\begin{aligned}
\alpha_{n+1}&=\frac{\beta}{a+\beta},\\
\gamma_{n+1}&=\frac{\langle t,c\rangle}{a+\beta},\\
\beta_{n+1}&=\frac1a\left(\langle t,t\rangle-
                         \frac{|\langle c,t\rangle|^2}{a+\beta}\right).
\end{aligned}}
\]
All three values are therefore computed with the existing inverse and the retained vector \(t\). The recurrence includes the drift \(Ac\); three scalars alone do not encode that vector.

The displacement identity is
\[
AS+SA^*-S=cr^*+rc^*.
\]
Taking its trace after multiplication by \(S^{-1}\) proves the exact invariant
\[
\boxed{\operatorname{Re}\gamma_n
=\operatorname{Re}\operatorname{tr}A-d/2
=\sum_\rho m_\rho(\operatorname{Re}\rho-1/2)=:g.}
\]
For a reflection-stable divisor the summands cancel in reflected pairs, so \(g=0\). This conclusion includes the multiplicities.

For completeness the scalar step proves the same invariant locally. Multiplying the displacement identity by \(S^{-1}\) on both sides gives
\[
S^{-1}A+A^*S^{-1}-S^{-1}
=S^{-1}cr^*S^{-1}+S^{-1}rc^*S^{-1}.
\]
Its \((c,c)\) value yields
\(\operatorname{Re}\langle c,Ac\rangle=\beta/2+\beta g\).
Since \(\operatorname{Re}b=1/2\),
\(\operatorname{Re}\langle t,c\rangle=(a+\beta)g\), as required. The complete imaginary update, with no suppression of \(\operatorname{Im}b\), is
\[
\operatorname{Im}\gamma_{n+1}
=\frac{\beta\operatorname{Im}b-
       \operatorname{Im}\langle c,Ac\rangle-
       a\operatorname{Im}\gamma}{a+\beta}.
\]

## 3. Exact transverse energy and sharp one-step control

Define
\[
\Delta_n=\alpha_n\beta_n-|\gamma_n|^2\geq0,
\qquad
\epsilon_n=|g|+\sqrt{g^2+\Delta_n}.
\]
This \(\epsilon_n\) is precisely the relative weight norm at kernel index \(n-1\), and hence at the original correction index \(m=n-1-d\) where that index belongs to the source sequence. Here is the full finite-rank proof, including zero-rank and rank-one cases. Under the exact isometry \(u\mapsto S^{-1/2}u\), put \(x=S^{-1/2}c\), \(y=S^{-1/2}r\), \(U:\mathbb C^2\to E\), \(U(z_1,z_2)=xz_1+yz_2\), and \(J=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\). The transported weight is \(B=UJU^*\). Its possibly nonzero eigenvalues are those of
\[
JU^*U=\begin{pmatrix}\bar\gamma&\alpha\\\beta&\gamma\end{pmatrix},
\qquad
\det(\lambda I-JU^*U)=\lambda^2-2g\lambda-\Delta_n.
\]
Indeed at each \(\lambda\ne0\), the maps \(JU^*\) and \(\lambda^{-1}U\) give inverse maps between the corresponding eigenspaces of \(UJU^*\) and \(JU^*U\). Their products are the identities on those eigenspaces by their eigenvalue equations. The first matrix is Hermitian, so its norm is the largest absolute eigenvalue. The two displayed roots are \(g\pm\sqrt{g^2+\Delta_n}\); any extra zero leaves their largest absolute value unchanged. When both roots are zero the Hermitian matrix vanishes. Thus its norm is exactly the stated \(\epsilon_n\). This retains the original coordinates through the specified metric isometry.

In the resolvent domain \(\beta>0\). Define the orthogonal projection, in the already specified inner product, by
\[
Pu=u-c\,\langle c,u\rangle/\beta,
\quad p=Pr,
\quad w=PAc.
\]
Direct substitution shows \(P^2=P\), \(Pc=0\), \(\langle c,Pu\rangle=0\), and \(\langle Pu,v\rangle=\langle u,Pv\rangle\). Thus
\[
\Delta_n=\beta\|p\|^2,
\qquad Pt=w+ap.
\]
Substitution of the preceding three scalar recurrences gives, with the cross term retained,
\[
\begin{aligned}
\Delta_{n+1}
&=\frac{\beta\langle t,t\rangle-|\langle c,t\rangle|^2}
        {a(a+\beta)}\\
&=\boxed{\frac{\beta}{a(a+\beta)}\|w+ap\|^2}.
\end{aligned}
\]
Consequently
\[
\boxed{\Delta_{n+1}-\Delta_n
=\frac{\beta}{a(a+\beta)}
 \left(\|w\|^2+2a\operatorname{Re}\langle w,p\rangle
                    -a\beta\|p\|^2\right).}
\]
This is the exact energy balance supplied by the recurrence. It computes the sign of the change from the actual arithmetic vectors and their current metric; it introduces no assumed sign.

Put \(\Omega_n=\beta\|w\|^2\). The triangle and reverse triangle inequalities prove the sharp estimates
\[
\boxed{
\frac{|a\sqrt{\Delta_n}-\sqrt{\Omega_n}|}{\sqrt{a(a+\beta)}}
\leq\sqrt{\Delta_{n+1}}
\leq
\frac{a\sqrt{\Delta_n}+\sqrt{\Omega_n}}{\sqrt{a(a+\beta)}}.}
\]
Equality occurs when the vectors \(w\) and \(p\) have the corresponding real collinearity and orientation, including the zero-vector cases. This specifies exactly which extra scalar drift energy controls a step; omitting it would omit part of the calculation.

## 4. Determinants and the actual source Gram

The rank-one determinant identity can be proved by extending a nonzero vector to a basis: \(I+uv^*\) induces the identity on the quotient by \(\mathbb C u\), and acts on that line with eigenvalue \(1+v^*u\). It gives
\[
\boxed{
\frac{\det S_{n+1}}{\det S_n}
=\frac{a_n^{d-1}(a_n+\beta_n)}{|\det T_n|^2},
\quad
\frac{\det K_n}{\det K_{n-1}}=1+\frac{\beta_n}{a_n}.}
\]
Here \(\det T_n=\det q_{n+1}(A)/\det q_n(A)\), with the determinants containing the complete multiplicities. For the original fixed invertible residue multiplier \(U_\varepsilon\), set
\[
G^{[n]}=U_\varepsilon^*K_{n-1}^{-1}U_\varepsilon.
\]
This is the actual original source Gram \(G_m\) at \(m=n-1-d\). Its exact volume contraction is
\[
\boxed{\frac{\det G^{[n+1]}}{\det G^{[n]}}
=\frac{a_n}{a_n+\beta_n}=1-\alpha_{n+1}.}
\]
Thus the volume contraction determines \(\alpha_{n+1}\) exactly. The separate transverse energy term in Section 3 remains in the relative weight calculation.

## 5. Exact closure in volume ratios for conjugation-and-reflection packets

The actual arithmetic construction has a stronger scalar form on every packet whose divisor contains each selected zero with its full multiplicity and is stable under both conjugation and \(\rho\mapsto1-\bar\rho\). Such packets are obtained directly by taking complete symmetry orbits of the actual zeros. No assumption about the real parts of those zeros is made.

The polynomial \(h\) has real coefficients because conjugation permutes its roots with multiplicities. The completed zeta function satisfies \(g(\bar s)=\overline{g(s)}\); therefore on the original line \(s=1/2+it\),
\[
|g(1/2-it)/h(1/2-it)|^2=|g(1/2+it)/h(1/2+it)|^2.
\]
Thus the original measure \(\nu_Z\) is invariant under \(t\mapsto-t\). For a polynomial \(P\), write \(P^\dagger(s)=\overline{P(\bar s)}\), retaining its conjugate coefficients. The change of variable \(t\mapsto-t\) gives exactly
\[
\langle P,q_n^\dagger\rangle_{\nu_Z}
=\overline{\langle P^\dagger,q_n\rangle_{\nu_Z}}.
\]
For every \(\deg P<n\), the right side is zero. The polynomial \(q_n^\dagger\) is monic, hence uniqueness of the monic orthogonal polynomial proves \(q_n^\dagger=q_n\). This proves that every coefficient of the actual \(q_n\) is real. The same integral argument gives \(b_n=1/2\), since \(\int t|q_n(1/2+it)|^2d\nu_Z=0\).

In the original monomial coordinates, the companion matrix \(A\), the unit \(c\), all residue columns \(v_n\), and therefore \(K_n\), \(M_n\) and their inverses are real. Consequently \(\gamma_n\) is real. Reflection stability already proved \(\operatorname{Re}\gamma_n=0\); hence
\[
\boxed{\gamma_n=0,\qquad (\epsilon^{(n)})^2=\alpha_n\beta_n.}
\]
The universal update gives \(\alpha_{n+1}=\beta_n/(a_n+\beta_n)<1\), including the zero-vector case, so
\[
\boxed{(\epsilon^{(n)})^2
=a_n\frac{\alpha_n\alpha_{n+1}}{1-\alpha_{n+1}}.}
\]
For \(m=n-1-d\geq0\), define the actual consecutive volume ratios
\[
d_n=\frac{\det G_m}{\det G_{m-1}},\qquad
d_{n+1}=\frac{\det G_{m+1}}{\det G_m},
\]
where the first ratio at \(m=0\) uses the specified fixed-section metric \(G_{-1}\). The preceding determinant theorem gives \(d_n=1-\alpha_n\) and \(d_{n+1}=1-\alpha_{n+1}\). Thus the full relative weight energy on these actual symmetry packets is exactly
\[
\boxed{(\epsilon^{(n)})^2
=a_n\frac{(1-d_n)(1-d_{n+1})}{d_{n+1}}.}
\]
All constants in this identity are the original arithmetic recurrence coefficient and original theta-Gram determinants. This is an equality, not an asserted estimate or a claim of monotonicity. Together with the transverse law it gives two fully identified computations of the same arithmetic energy. It remains valid at quadrature intersections by the polynomial argument in the next section.

For an originally chosen divisor \(h_0\) without these symmetries, let \(h\) be the monic divisor obtained by completing its symmetry orbits with the actual zero multiplicities. Then \(h_0\mid h\). The exact algebra map to the original packet is
\[
\pi:\mathbb C[s]/(h)\longrightarrow\mathbb C[s]/(h_0),
\qquad [P]_h\longmapsto[P]_{h_0}.
\]
It is well defined because \((h)\subset(h_0)\), surjective because each target class has a polynomial representative, unital and multiplicative by polynomial operations, and has kernel \((h_0)/(h)\). It intertwines the original multiplication matrices and maps the unit to the unit. The two associated arithmetic measures remain separately retained: off their removable zeros they obey \(d\nu_{h_0}=|h/h_0|^2d\nu_h\), and continuation supplies the equality at removable points. Thus the symmetry completion has a proved quotient map and an explicit measure relation; it does not silently replace the original packet or its metric.

## 6. Polynomial continuation through all quadrature intersections

There is an exact extension of every scalar formula above even where a selected critical centre makes \(Q_n\) or \(Q_{n+1}\) singular. It does not require a resolvent. At each stage use
\[
\langle u,v\rangle_{n,\mathrm{pol}}
=\kappa_{n-1}^{-1}u^*K_{n-1}^{-1}v,
\quad C=v_n,\quad R=v_{n-1},\quad
t=(A-b_nI)C+a_nR=v_{n+1}.
\]
Define \(\alpha=\langle R,R\rangle_{n,\mathrm{pol}}\), \(\beta=\langle C,C\rangle_{n,\mathrm{pol}}\), and \(\gamma=\langle C,R\rangle_{n,\mathrm{pol}}\). Wherever \(Q_n\) is invertible, the typed map
\[
Q_n:(E,\langle\ ,\ \rangle_{S_n^{-1}})
\longrightarrow(E,\langle\ ,\ \rangle_{n,\mathrm{pol}})
\]
is an isometry and sends \(c\) to \(C\), \(r_n\) to \(R\), because
\(\kappa_{n-1}^{-1}Q_n^*K_{n-1}^{-1}Q_n=S_n^{-1}\).
At the exceptional fibres the polynomial definitions themselves are retained. Applying the rank-one inverse formula directly to
\(K_n=K_{n-1}+CC^*/\kappa_n\), and using \(\kappa_n=a_n\kappa_{n-1}\), proves the same three scalar recurrences in Section 2, with \(c,r\) replaced by \(C,R\) and all pairings interpreted in the polynomial metric. In particular they require only the positive denominator \(a_n+\beta_n\), and remain meaningful when \(\beta_n=0\).

The Christoffel displacement identity
\[
AK_{n-1}+K_{n-1}A^*-K_{n-1}
=\kappa_{n-1}^{-1}(CR^*+RC^*)
\]
proves the identical trace invariant and the identical energy formula. For \(\beta>0\), Section 3 applies with
\(Pu=u-C\langle C,u\rangle/\beta\), \(p=PR\), and \(w=PAC\).
For \(\beta=0\), positivity gives \(C=0\). Then \(\gamma=0\), \(K_n=K_{n-1}\), the current displacement form vanishes, and \(t=a_nR\). The scalar step gives exactly
\[
\alpha_{n+1}=0,\quad\gamma_{n+1}=0,
\quad\beta_{n+1}=a_n\alpha_n,
\quad\Delta_n=\Delta_{n+1}=0.
\]
The next displacement form also vanishes because its second vector is \(C=0\). Every determinant formula for \(K\) and \(G\) remains valid with determinant ratio one. Thus every centre and every permitted jet has an explicit formula, including this exceptional case.

## 7. Strict increase in a reflected positive moment model

A separate exact computation in `work/terminal_energy_monotonicity_20260912.md` supplies a counterexample to decreasing energy inferred from positivity, vertical support, the recurrence, and reflection alone. Its measure is the positive probability measure of \(s=1/2+it\), where \(t\) is centred Gaussian with variance \(1/16\). Its reflected packet is
\[
h(s)=(s-3/4)(s-1/4)=s^2-s+3/16,
\quad A=\begin{pmatrix}0&-3/16\\1&1\end{pmatrix},
\quad c=\binom10.
\]
The exact evaluation isomorphism is
\[
T:E\longrightarrow\mathbb C^2,
\quad u_0+u_1s\longmapsto(u_0+3u_1/4,u_0+u_1/4),
\quad T=\begin{pmatrix}1&3/4\\1&1/4\end{pmatrix},
\]
and satisfies \(TA=\operatorname{diag}(3/4,1/4)T\), \(Tc=(1,1)^t\). The kernels in that coordinate system are
\[
TK_3T^*=\begin{pmatrix}20/3&-2/3\\-2/3&20/3\end{pmatrix},
\qquad
TK_4T^*=\begin{pmatrix}65/6&7/2\\7/2&65/6\end{pmatrix}.
\]
The exact relative energies satisfy
\[
\epsilon_{N=3}^2=25/99,
\qquad\epsilon_{N=4}^2=4225/15136,
\qquad
\epsilon_{N=4}^2-\epsilon_{N=3}^2=39875/1498464>0.
\]
These are the original correction levels \(m=1\) and \(m=2\) for \(d=2\), so the strict increase lies within that indexing range. This is a generic vertical moment example with an explicitly stated measure. It does not assert an increase for the arithmetic measure \(\nu_Z\). The exact map to the arithmetic calculation is the common construction \((\nu,h)\mapsto(E,A,c,\{q_k,\kappa_k,K_k\})\), whose recurrence and scalar identities have been proved above for each measure separately. The special arithmetic coefficients remain in the exact drift and energy formula, ready for the arithmetic estimate.

## Audit outcome and next exact calculation

The proposed matrix step is correct. The complete scalar recurrence, determinant update, trace invariant, exceptional-fibre continuation and sharp transverse energy bounds are proved above. A monotone decrease does not follow from the displayed general hypotheses, as the exact reflected example demonstrates. For the actual arithmetic measure the next retained quantities are
\[
\Omega_n=\beta_n\|P_nAv_n\|_{n,\mathrm{pol}}^2,
\qquad
\operatorname{Re}\langle P_nAv_n,P_nv_{n-1}\rangle_{n,\mathrm{pol}},
\]
with the zero-vector fibre handled explicitly in Section 6. Their exact combination, rather than an assumed sign, is the fully computed change of the relative weight energy. On the complete conjugation-and-reflection packets of Section 5, the same energy is also the exact expression in two consecutive actual volume ratios.

The new cumulative source `tex/kernel_terminal_continuation.tex`, equations KT.1–KT.18, was independently checked against this report. Its formulas agree, including the imaginary conjugations, complete multiplicity determinants and zero-vector fibre. The audit requested the precise rank wording “at most two nonzero generalized eigenvalues,” because rank zero and rank one are permitted.

Reproducible exact calibration is in `work/check_terminal_energy_recurrence_20260912.py`: four explicitly stated Gaussian moment packets, including one repeated off-line complex centre, two simple critical quadrature nodes, and a repeated critical centre. It checks 16 consecutive steps, of which three have singular `q_n(A)` and one has `beta_n=0`. Ordinary and optimized Python each pass **288 exact checks**, including the universal scalar recurrences, imaginary update, exact transverse increment, isometry, matrix step and both determinant laws. The counterexample checker separately passes **88 exact checks** in ordinary and optimized Python. These checks supplement the proofs and assert no arithmetic asymptotic estimate. Copies of both scripts and all four receipts are in the current output package's `checks/terminal_energy_monotonicity.*` and `checks/terminal_energy_recurrence.*` files.

The separate `checks/terminal_volume_energy.py` and its two receipts add **66 exact checks in each Python mode** for the volume-energy equality of Section 5, retaining all earlier calibration files. They calculate the generalized eigenvalue energy and the consecutive determinant ratios independently on reflected-pair, critical-node-pair and repeated-critical-jet packets, including the fixed-section endpoint. The fully written nine-atom counterexample is now the companion fragment `tex/terminal_energy_counterexample.tex`, with every moment through degree ten and the actual finite-measure fifth norm `114/16^5` explicitly proved.

The subsequently added complete theorem KT.28 in `tex/kernel_terminal_continuation.tex` was read independently and agrees with Section 5, including the coefficient `kappa_(d+m+1)/kappa_(d+m)`, the determinant indexing, the original `G_-1` endpoint, reality of every retained matrix, and zero-column cases. The companion counterexample fragment was independently read in full; its pinned SHA256 is `9AFCD1DA3A2E6B2B1DC1D40F510FDB6B8AFDB6FC7B12286127187F6BD3BBD007`. No mathematical correction remains in these audited portions. Compilation and visual QA belong to the cumulative build and are not asserted here.
