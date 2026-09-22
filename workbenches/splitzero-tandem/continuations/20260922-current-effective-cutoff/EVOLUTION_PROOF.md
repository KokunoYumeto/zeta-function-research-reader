# Signed-time evolution, extreme singular values, and the original hidden-source defect

22 September 2026. Independent continuation of the supplied *Original observed arithmetic-current plane*, OCP49–59. The finite arguments below are complete. The growing-degree application uses the source comparison, monic profile, two-column area and leakage estimates proved in that supplied manuscript; the exact required estimates are listed in CE20. No current of a separately marked terminal eigenclass is evaluated here.

## 1. The original spaces and their exact isometry

Retain the original simple-quartet domain \(k\equiv1\pmod4\), \(k\ge17\), \(q=(k+1)^2\), \(q_0=(k-7)^2\), \(0<\delta<1/2\), \(\gamma>2\), the admitted period and branch. Let

\[
Q_k(y)=\prod_{a,b=0}^k[y-(2b-k)\gamma+i(2a-k)\delta],\quad
E=\mathbb C[y]/Q_k,\quad M[p]=[yp],\quad \mathscr A=kI/2+iM. \tag{CE1}
\]

For every original cutoff \(q-1\le N\le2q\), let \(G=G_N\) be its complete source minimum, \(\Lambda:E\to B\) the original onto map, \(K=\ker\Lambda\), and

\[
Q_B=(\Lambda G^{-1}\Lambda^*)^{-1},\qquad
L=G^{-1}\Lambda^*Q_B,\qquad J=LQ_B^{-1/2}. \tag{CE2}
\]

Here \(E\) has inner product \(x^*Gy\), conjugate-linear in the first argument; the domain of \(J\) has the usual inner product. Direct multiplication gives

\[
\Lambda L=I_B,\quad L^*GL=Q_B,\quad J^\dagger J=I_B,
\quad J^\dagger=Q_B^{1/2}\Lambda,\quad P=JJ^\dagger=L\Lambda. \tag{CE3}
\]

Thus \(P\) is the orthogonal projection with kernel exactly \(K\). This is an isometry of the actual metric, retaining all original minimum relations. In particular

\[
U(t)=J^\dagger e^{itM}J=Q_B^{1/2}(\Lambda e^{itM}L)Q_B^{-1/2},\quad
V(t)=e^{itM_B},\quad M_B=J^\dagger MJ. \tag{CE4}
\]

Their usual norms are precisely the original \(Q_B\)-operator norms.

Let \(p_n\) be the real monic polynomials of the unchanged even source, with full squared norms \(\omega_n\). Put \(b_n=[p_n]\), \(E_N=\|b_N\|_G^2\), \(F_N=\|b_{N+1}\|_G^2\). The complete quotient representatives and parity give the original identity OCP5–7:

\[
e=b_N/\sqrt{E_N},\quad f=b_{N+1}/\sqrt{F_N},\quad
\langle e,f\rangle_G=0,\quad \|e\|_G=\|f\|_G=1,
\quad M=C+R,\quad C=C^\dagger,\quad R=\epsilon f e^\dagger,
\quad \epsilon=\sqrt{E_NF_N}/\omega_N. \tag{CE5}
\]

For completeness, the minimum representative of \(b_{N+1}\) is \(p_{N+1}-Q_k U_{N+1-q}\), where \(U_j\) is the monic polynomial for \(Q_k^2d\mu_k\); its degree is at most \(N\). Projecting multiplication by \(y\) on the actual minimum-section space leaves the degree-\(N+1\) term \([y^N]P\,p_{N+1}\). Its coefficient is \(\langle p_N,P\rangle/\omega_N\), yielding CE5. The remaining compressed multiplication is selfadjoint. Opposite parity yields \(R^2=0\), with the entire degree-\(N\) source unchanged.

Define

\[
u=J^\dagger e,\quad v=J^\dagger f,\quad
a=\|u\|^2,\quad d=\|v\|^2,\quad r=u^*v,\quad
\alpha=\|(I-P)e\|^2=1-a. \tag{CE6}
\]

Compression gives

\[
C_B=J^\dagger CJ=C_B^*,\quad R_B=\epsilon vu^*,\quad
\epsilon_B=\|R_B\|=\epsilon\sqrt{ad},\quad z=\operatorname{tr}R_B=\epsilon r,
\quad R_B^2=zR_B. \tag{CE7}
\]

The Gram \(\mathcal C=\begin{pmatrix}a&r\\\bar r&d\end{pmatrix}\) obeys \(0\preceq\mathcal C\preceq I_2\). Since \(e\perp f\), \(r=-\langle(I-P)e,(I-P)f\rangle\), so \(|r|\le\sqrt\alpha\). If the complete two-column certificate supplies \(\det\mathcal C\ge\Theta>0\), then

\[
\epsilon\sqrt\Theta\le\epsilon_B\le\epsilon,
\quad |z|\le\epsilon\sqrt\alpha,
\quad |z|/\epsilon_B\le\sqrt{\alpha/\Theta}. \tag{CE8}
\]

No separate norm lower bounds can replace this determinant certificate.

## 2. A finite noncommuting propagator estimate at both signed times

For a bounded \(C\), a rank-one \(R\) with \(\|R\|=\varepsilon\) and \(R^2=zR\), set, for \(T\ge0\),

\[
D(T;\varepsilon,z,c)=c e^{T|z|}
\left[T+\frac{\varepsilon^2T^3}{6(1+T\varepsilon)}\right],\qquad c\ge\|C\|. \tag{CE9}
\]

Whenever \(D<1\), every \(|t|\le T\) satisfies

\[
\frac{\|e^{it(C+R)}-I-itR\|}{1+|t|\varepsilon}
\le e^{T|z|}\left[\frac D{1-D}+\frac{T|z|}{2}\right]. \tag{CE10}
\]

**Proof.** It suffices first to take \(t\ge0\). The identity \(R^j=z^{j-1}R\) for \(j\ge1\) yields

\[
e^{itR}=I+f_t(z)R,\quad f_t(z)=(e^{itz}-1)/z,
\quad f_t(0)=it,
\quad |f_t(z)-it|\le \tfrac12 t^2|z|e^{T|z|}. \tag{CE11}
\]

Differentiate \(e^{i(t-s)R}e^{is(C+R)}\) and integrate, obtaining exactly

\[
e^{it(C+R)}-e^{itR}=i\int_0^t e^{i(t-s)R}C e^{is(C+R)}ds. \tag{CE12}
\]

No interchange of \(C\) and \(R\) occurs. Let \(M_T=\sup_{0\le s\le T}\|e^{is(C+R)}\|/(1+s\varepsilon)\), finite by continuity. The exact scalar integral is

\[
\int_0^t\frac{(1+(t-s)\varepsilon)(1+s\varepsilon)}{1+t\varepsilon}ds
=t+\frac{\varepsilon^2t^3}{6(1+t\varepsilon)}. \tag{CE13}
\]

The right side is increasing in \(t\ge0\). Hence \(M_T\le e^{T|z|}+DM_T\); substitute \(M_T\le e^{T|z|}/(1-D)\) in CE12, then add CE11. For negative \(t\), apply the same proof to \(-C,-R\), whose rank-one trace is \(-z\) and whose norms are unchanged. This proves CE10 for both signs. The coarser bound \(D\le c e^{T|z|}(T+\varepsilon T^2/6)\) recovers OCP53.

Apply CE10 to the full space and its actual compression. Put \(c=2(N+1)\sqrt{u_0/\ell_0}\), where \(\ell_0\|P\|_\sigma^2\le\|P\|_{\mu_k}^2\le u_0\|P\|_\sigma^2\) holds through degree \(N+1\), retaining the absolute source masses. The exact Gamma recurrence has off-diagonal orthonormal coefficients \(\sqrt{n(n-1/2)}\le n\), so multiplication on degree at most \(N\) has norm at most \(2(N+1)\). Taking the ratio of these two actual source inequalities, then compressing orthogonally, proves \(\|C\|,\|C_B\|\le c\).

Let \(D_F=D(T;\epsilon,0,c)\), \(D_B=D(T;\epsilon_B,z,c)\), and suppose both are less than one. Define

\[
A_F=\frac{1+T\epsilon}{1+T\epsilon_B}\frac{D_F}{1-D_F},\qquad
A_B=e^{T|z|}\left[\frac{D_B}{1-D_B}+\frac{T|z|}{2}\right]. \tag{CE14}
\]

For each signed time \(t=\pm T\), contraction by \(J^\dagger,J\) gives the finite inequalities

\[
\|U(t)-I-itR_B\|\le(1+T\epsilon_B)A_F,\qquad
\|V(t)-I-itR_B\|\le(1+T\epsilon_B)A_B. \tag{CE15}
\]

The factor \((1+T\epsilon)/(1+T\epsilon_B)\le\Theta^{-1/2}\) is retained; it need not be one. In particular 

\[
\|U(t)-V(t)\|\le(1+T\epsilon_B)(A_F+A_B). \tag{CE16}
\]

## 3. Exact finite shear, and the forward/backward singular receiver

Set \(x=T\epsilon_B\), \(h=|z|/\epsilon_B\le1\), and

\[
S(x)=\frac{\sqrt{x^2+4}+x}{2}. \tag{CE17}
\]

On the span of \(u,v\), a unitary frame places \(R_B/\epsilon_B\) into \(\begin{pmatrix}\zeta&\sqrt{1-|\zeta|^2}\\0&0\end{pmatrix}\), where \(\zeta=z/\epsilon_B\). To construct the frame, take its first vector along the range of \(R_B\), and choose the phase of the second to make the off-diagonal entry nonnegative. The rank-one norm identity fixes that entry. Its distance from \(\begin{pmatrix}0&1\\0&0\end{pmatrix}\) is at most \(2h\): the diagonal difference is \(h\), and \(1-\sqrt{1-h^2}\le h\). Directly computing the two eigenvalues of the shear's Gram gives \(S(x)\) and \(S(x)^{-1}\) as its singular values. Consequently

\[
\left|\frac{\|U(\pm T)\|}{S(x)}-1\right|\le\eta_F:=2A_F+2h,
\qquad
\left|\frac{\|V(\pm T)\|}{S(x)}-1\right|\le\eta_B:=2A_B+2h. \tag{CE18}
\]

Indeed \(S(x)\ge\max\{1,x\}\), so \((1+x)/S(x)\le2\) and \(x/S(x)\le1\).

The exact inverse is \(V(T)^{-1}=V(-T)\), because both are exponentials of the same original compressed generator. If \(\eta_B<1\), CE18 proves

\[
\begin{aligned}
(1-\eta_B)S(x)&\le\sigma_{\max}(V(T))\le(1+\eta_B)S(x),\\
\frac1{(1+\eta_B)S(x)}&\le\sigma_{\min}(V(T))\le\frac1{(1-\eta_B)S(x)},\\
(1-\eta_B)^2S(x)^2&\le\operatorname{cond}_{Q_B}(e^{iT\Lambda ML})
\le(1+\eta_B)^2S(x)^2.
\end{aligned} \tag{CE19}
\]

Here condition number means the product of the operator norm and inverse operator norm in the original metric. The finite error is explicit. No inverse identity for the observed full operator \(U(T)\) has been used; CE26 below gives its exact inverse defect.

One may retain the small complex trace without any shear replacement: on the two-dimensional active span the squared singular values of \(I+itR_B\) are the roots of

\[
w^2-\bigl(2+t^2\epsilon_B^2-2t\Im z\bigr)w+|1+itz|^2=0.
\]

All other singular values are one. This follows from the Frobenius norm and determinant of its displayed two-by-two matrix and preserves the sign of \(t\Im z\).

## 4. Application to every original cutoff, with the required input displayed

The original two-column and profile proofs OCP29–35 supply, uniformly for \(q-1\le N\le2q\), with \(s_N=(N+1-q)/q\),

\[
\begin{gathered}
\log\epsilon_N=q\psi(s_N)+O(k\log^2(q+2)),\qquad
0\le-\log\Theta_N=O(k\log^2(q+2)),\\
\alpha_N\le\exp[-2q\psi(s_N)+O(k\log^2(q+2))],\qquad
\log c_N=O(k\log^2(q+2)),\\
\det\mathcal C_N\ge\Theta_N>0.
\end{gathered} \tag{CE20}
\]

These are the precise inputs to the following propagation, including the full complex area estimate. The present note proves their consequences, not an independent replacement for the conductor argument. The original elliptic profile is

\[
1+s=\frac{E(\sqrt{1-r_s^2})}{r_sK(\sqrt{1-r_s^2})},\qquad
\psi(s)=s\log\frac{\sqrt{1-r_s^2}}{E(\sqrt{1-r_s^2})}
+\log\frac{1+r_s}{E(\sqrt{1-r_s^2})},
\]

with its endpoint limit at \(s=0\). Its endpoint values are \(a_0=\log(4/\pi)\) and \(a_1=\psi(1)>0\). It is decreasing, has logarithmically bounded derivative near zero, and bounded derivative near one, as retained in OCP31. Write \(L_k=k\log^2(q+2)=o(q)\). To propagate sharper inherited source bounds without concealing them in this coarser allowance, define the actual finite cost

\[
\mathfrak E_k=1+\max_N\left\{
|\log\epsilon_N-q\psi(s_N)|,\ -\log\Theta_N,\ \log^+c_N,
\ \log^+\bigl(\alpha_Ne^{2q\psi(s_N)}\bigr)\right\}. \tag{CE20a}
\]

Here \(\log^+x=\max\{0,\log x\}\) for \(x>0\), with \(\log^+0=0\). This is an explicitly specified scalar of the original finite data, not a new assumption. CE20 proves \(\mathfrak E_k=O(L_k)\). In particular, for the original source cost \(\mathcal L_k=\log(u_0/\ell_0)\), the multiplication contribution is exactly \(\log c_N=\log(2(N+1))+\mathcal L_k/2\). Every occurrence of \(O(L_k)\) in the propagation estimates CE21–23 can be replaced by \(O(\mathfrak E_k+\log q)\). Thus a proved sharper upper bound on the same source and area scalars transfers directly; no evolution argument is repeated.

For each fixed \(b>a_0/2\), take the same physical time \(T=e^{-bq}\) at every cutoff. CE8 and CE20 give

\[
\log\epsilon_{B,N}=q\psi(s_N)+O(L_k),\quad
|z_N|=e^{O(L_k)},\quad h_N\le e^{-q\psi(s_N)+O(L_k)}.
\]

Moreover \(D_F,D_B\le e^{-bq+O(L_k)}+e^{(a_0-2b)q+O(L_k)}\), and the full-to-observed factor in CE14 is \(e^{O(L_k)}\). Therefore for every positive \(c_b<\min\{b,2b-a_0,a_1\}\), all finite guards eventually hold and

\[
\eta_F+\eta_B\le e^{-c_bq+O_{h,\varpi,b}(L_k)}. \tag{CE21}
\]

Since \(\log S(e^w)-\max\{w,0\}\) is bounded uniformly on the real line, CE18–19 prove the new original-metric extreme singular laws

\[
\begin{aligned}
\log\|U(e^{-bq})\|&=q(\psi(s_N)-b)_++O_{h,\varpi,b}(L_k),\\
\log\sigma_{\max}(V(e^{-bq}))&=q(\psi(s_N)-b)_++O_{h,\varpi,b}(L_k),\\
\log\sigma_{\min}(V(e^{-bq}))&=-q(\psi(s_N)-b)_++O_{h,\varpi,b}(L_k),\\
\log\operatorname{cond}_{Q_{B,N}}(e^{ie^{-bq}\Lambda ML_N})
&=2q(\psi(s_N)-b)_++O_{h,\varpi,b}(L_k).
\end{aligned} \tag{CE22}
\]

The exact inverse, rather than a perturbation claim about the smallest singular value of a large shear, proves the third line. It also covers the transition \(\psi(s_N)=b\).

The four original signs are \(+,+,-,-\) at \(N=q-1,q,2q-1,2q\). At \(b=1/8\), the certified inequalities \(a_1<1/8<a_0\) and \(a_0/2<1/8\) give

\[
\begin{aligned}
\mathcal R\log\sigma_{\max}(V(e^{-q/8}))
&=[2\log(4/\pi)-1/4]q+O_{h,\varpi}(L_k),\\
\mathcal R\log\sigma_{\min}(V(e^{-q/8}))
&=-[2\log(4/\pi)-1/4]q+O_{h,\varpi}(L_k),\\
\boxed{\mathcal R\log\operatorname{cond}_{Q_{B,N}}(e^{ie^{-q/8}\Lambda ML_N})
=[4\log(4/\pi)-1/2]q+O_{h,\varpi}(L_k).}
\end{aligned} \tag{CE23}
\]

The profile arguments are exactly \(0,1/q,1,1+1/q\); no cutoff is merged with its neighbour. Integrating the endpoint derivative bound makes the lower displacement \(O(\log q)\), and the upper displacement costs \(O(1)\), both already inside \(O(L_k)\). The condition-number coefficient is twice the incoming norm coefficient, approximately \(0.4662579010819617787641475662531776980\).

For the uncentered physical action \(\mathscr A=kI/2+iM\), the scalar \(e^{kT/2}\) multiplies both observed evolutions. It cancels in the condition number at each cutoff and cancels exactly from the four-cutoff logarithmic norm and singular-value returns. The arithmetic unit is therefore retained.

## 5. The complete hidden-source defect and its connecting equations

The second-order difference is exactly

\[
U(t)-V(t)=-\tfrac12t^2\mathcal D+O(t^3),\qquad
\mathcal D=J^\dagger M(I-P)MJ. \tag{CE24}
\]

The statement is a finite-dimensional Taylor expansion at each fixed original cutoff. Its remainder is not being promoted to a uniform growing-degree estimate. Expanding the original \(C+R\) gives

\[
\boxed{\mathcal D=J^\dagger C(I-P)CJ
+J^\dagger C(I-P)RJ+J^\dagger R(I-P)CJ-zR_B.} \tag{CE25}
\]

Indeed \(J^\dagger R(I-P)RJ=J^\dagger R^2J-R_B^2=-zR_B\). This retains the hidden excursion and calculates its apparent quadratic rank-one contribution exactly. In the original data,

\[
\|\mathcal D\|\le c^2+c\epsilon\bigl[\sqrt{a(1-d)}+\sqrt{d(1-a)}\bigr]+|z|\epsilon_B.
\]

The two mixed bounds follow by substituting \(R=\epsilon f e^\dagger\), with \(\|(I-P)f\|=\sqrt{1-d}\), \(\|(I-P)e\|=\sqrt{1-a}\). Under CE20 this entire upper bound is \(\exp[q\psi(s_N)+O(L_k)]\), rather than the unproved estimate obtained by treating two factors of \(\epsilon\) independently.

There is also an exact all-time inverse defect:

\[
\boxed{U(-t)U(t)=I_B-J^\dagger e^{-itM}(I-P)e^{itM}J.} \tag{CE26}
\]

It follows by inserting \(P=JJ^\dagger=I-(I-P)\) between the two exponentials. In particular \(U(-t)U(t)=I-t^2\mathcal D+O(t^3)\), consistently with CE24. This identifies the exact map preventing the intrinsic inverse identity from being assigned to the measured full evolution.

Write \(M_{BK}=J^\dagger M|_K\), \(M_{KB}=(I-P)MJ\), \(M_{KK}=(I-P)M|_K\). The coupled source equations yield the exact Volterra identity, for \(t\ge0\),

\[
\boxed{U(t)-V(t)=-\int_0^t\int_0^s
e^{i(t-s)M_B}M_{BK}e^{i(s-r)M_{KK}}M_{KB}U(r)\,dr\,ds.} \tag{CE27}
\]

To prove it, put \(H(t)=(I-P)e^{itM}J\). Then \(U'=iM_BU+iM_{BK}H\), \(H'=iM_{KB}U+iM_{KK}H\), with \(U(0)=I,H(0)=0\). Solve the second equation by differentiating its variation-of-constants expression and substitute into the first. All finite-dimensional integrals converge. CE27 retains every original kernel coordinate and all mixed actions; its value at the diagonal origin is exactly CE24.

The hidden propagator itself has the finite bound

\[
\|e^{itM_{KK}}\|\le e^{|t|\epsilon\sqrt{\alpha(1-d)}}. \tag{CE28}
\]

For a solution \(x'=iM_{KK}x\), its squared norm has derivative bounded in absolute value by \(2\|R_{KK}\|\|x\|^2\), since \(C_{KK}\) is selfadjoint and \(\|R_{KK}\|=\epsilon\sqrt{\alpha(1-d)}\). Integrating this scalar differential inequality proves CE28 for both signs. The complete memory integrand has the original finite bound

\[
\|M_{BK}e^{itM_{KK}}M_{KB}\|
\le e^{|t|\epsilon\sqrt{\alpha(1-d)}}
\bigl(c+\epsilon\sqrt{d\alpha}\bigr)
\bigl(c+\epsilon\sqrt{a(1-d)}\bigr). \tag{CE29}
\]

This follows by writing both original mixed blocks explicitly. CE28–29 do not assume that the kernel is invariant. They give the actual hidden object and its maps which control the failure of the measured full operator to be a group.

## 6. Provenance and exact scope

The supplied full TeX [*Original observed arithmetic-current plane*](OBSERVED_CURRENT_PLANE.tex), OCP1–7, OCP19–35 and OCP49–59, defines the original data and contains the conductor proof supplying CE20. The present derivation independently proves CE9–19 and CE24–29; CE22–23 are new applications of the signed-time bounds. Root integration must retain the full supplied proof alongside this note and its original author citations. Its two-column certificate must be checked on the actual original source; this note has not checked that part in place of the root calculation.

The retained [kernel-pencil proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/9104d852c6bc5b79e6fc4588c403128a40b7fda3/workbenches/splitzero-tandem/continuations/20260922-arithmetic-probe-mass/PENCIL_PROOFS.md), PEN14–27, describes the original canonical sections. The present isometry CE2–3 and full-kernel excursion CE24–29 preserve those sections and the entire minimum.

Human source used for the coefficient recurrence: T. H. Koornwinder, R. Wong, R. Koekoek, R. F. Swarttouw and W. P. Reinhardt, *Orthogonal Polynomials*, NIST DLMF, [18.22.8](https://dlmf.nist.gov/18.22.E8) and [18.23.7](https://dlmf.nist.gov/18.23.E7). Their original TeX is retained in `human_sources/18.22.E8.tex` and `human_sources/18.23.E7.tex`. Substituting \(\lambda=1/4,\phi=\pi/2,x=y/2\) and multiplying \(P_n\) by \(n!\) gives \(\pi_{n+1}=y\pi_n-n(n-1/2)\pi_{n-1}\) and the generating function used in the source. The complete mass and norms remain the source's \(h_n=\sqrt{2\pi}\,n!(1/2)_n\). The elliptic profile retains B. C. Carlson's DLMF Chapter 19 conventions cited by the source. The elementary exponential, Duhamel and singular-value calculations used here are all proved above.

Neither the positive/negative operator signature nor the large singular values determine the current of the separately marked arithmetic eigenclass. That remains a different, actual matrix evaluation on its prescribed vector; no sign has been assigned to it by this continuation.
