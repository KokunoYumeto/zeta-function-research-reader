# The original adjacent source step and its marked-current correction

22 September 2026. Independent verification and continuation NV1–26. The original source covariance, observation and complete minimum section are retained throughout. The finite interpolation identities first hold for every rank-one source addition. Applying the actual next monic source column then gives the stronger terminal-mass estimate and its original cutoff profile. No current sign is assigned without its actual endpoint values and trace change.

## 1. The exact minimum-map interpolation

Work in the fixed original coefficient space \(E=\mathbb C[y]/Q_k\), with its full degree-\(N\) minimum metric \(G_0=G_N\), covariance \(D_0=G_0^{-1}\), and unchanged observation \(\Lambda:E\to B\). For a source column \(u\in E\), set
\[
D(t)=D_0+tuu^*,\quad G(t)=D(t)^{-1},\quad
Q(t)=(\Lambda D(t)\Lambda^*)^{-1},\quad
L(t)=D(t)\Lambda^*Q(t),\quad0\le t\le1.
\tag{NV1}
\]
The source covariance is positive definite for every such \(t\), and \(\Lambda\) is surjective onto its actual image \(B\); hence every inverse in NV1 exists. Put \(Q_0=Q(0)\), \(L_0=L(0)\), \(P_0=L_0\Lambda\), \(u_B=P_0u\), \(u_K=(I-P_0)u\), and \(z=\Lambda u\). These are the original \(G_0\)-orthogonal observed and kernel components. For a fixed observation \(\xi\), define
\[
\beta=z^*Q_0z=\|u_B\|_{G_0}^2,\quad
\rho=z^*Q_0\xi,\quad w=|\rho|^2,\quad
Y_0=\xi^*Q_0\xi,\quad s=\frac{t}{1+\beta t}.
\tag{NV2}
\]
Multiplication of the proposed inverse by \(\Lambda D(t)\Lambda^*\) proves the rank-one inverse formula. Substitution into \(L(t)\), retaining \(u=u_B+u_K\), then proves
\[
Q(t)=Q_0-sQ_0zz^*Q_0,\qquad
L(t)=L_0+s\,u_Kz^*Q_0.
\tag{NV3}
\]
Indeed the coefficient of \(u\) is \(t-st\beta=s\), and the remaining subtraction is \(su_Bz^*Q_0\). Thus
\[
L(t)\xi=L_0\xi+s\rho u_K,\qquad
\xi^*Q(t)\xi=Y_0-sw.
\tag{NV4}
\]
These are exact maps of the original fibres. They include the entire original kernel; \(u_K\) is not an independently chosen direction.

Let \(M[p]=[yp]\) remain fixed and write
\[
M_B(t)=\Lambda ML(t),\quad
\Phi(t)=i\xi^*Q(t)\Lambda[MD(t)-D(t)M^*]\Lambda^*Q(t)\xi,
\]
\[
\tau(t)=i\operatorname{tr}\{Q(t)\Lambda[MD(t)-D(t)M^*]\Lambda^*\}.
\tag{NV5}
\]
Both currents are real. Cyclicity of trace and \(D(t)\Lambda^*Q(t)=L(t)\) give
\(\Phi(t)=-2\Im[\xi^*Q(t)M_B(t)\xi]\) and
\(\tau(t)=-2\Im\operatorname{tr}M_B(t)\).
Put \(a_K=\Lambda Mu_K\). NV3 implies
\[
M_B(t)=M_B(0)+s\,a_Kz^*Q_0,\quad
\tau(t)=\tau_0-2s\,\Im\langle u_B,Mu_K\rangle_{G_0}.
\]
Consequently, with \(\Delta\tau=\tau_1-\tau_0\),
\[
\boxed{\Delta\tau=-\frac{2}{1+\beta}
\Im\langle u_B,Mu_K\rangle_{G_0},\qquad
\tau(t)=\frac{(1-t)\tau_0+t(1+\beta)\tau_1}{1+\beta t}.}
\tag{NV6}
\]
The sign comes from \(i(A-\bar A)=-2\Im A\). This proof holds for every source column, including a column with a nonzero kernel component.

## 2. The marked current and its exact quadratic receiver

Expand \(\xi^*Q(t)M_B(t)\xi\) using NV3:
\[
\xi^*Q_0M_B(0)\xi
+s[\rho\,\xi^*Q_0a_K-\bar\rho\,z^*Q_0M_B(0)\xi]
-s^2w\,z^*Q_0a_K.
\]
Taking \(-2\Im\) shows that \(\Phi(t)=q_0+q_1s+q_2s^2\), with
\[
q_0=\Phi_0,\qquad
q_2=2w\Im\langle u_B,Mu_K\rangle_{G_0}
=-(1+\beta)w\Delta\tau.
\]
Since \(s(1)=1/(1+\beta)\), the endpoint \(\Phi_1\) determines the remaining coefficient. The exact receiver into [SC17–18](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/4ba9285b66af58a6d58fc502a494c1fb45ca5b79/workbenches/splitzero-tandem/continuations/20260922-support-transport/STABLE_HIDDEN_ACTION_AND_SIGN_STEPS.md#L136) is therefore
\[
\boxed{\begin{aligned}
q_0&=\Phi_0,\\
q_1&=(1+\beta)(\Phi_1-\Phi_0)+w\Delta\tau,\\
q_2&=-(1+\beta)w\Delta\tau.
\end{aligned}}
\tag{NV7}
\]
For the terminal eigenclass these are precisely SC17's coefficients, because the complete source step and \(u_B,u_K,\rho\) are identical. The derivation above also proves the polynomial identity without an eigenclass hypothesis.

Returning to the original source coordinate \(t\) gives
\[
\boxed{\Phi(t)=
\frac{(1-t)\Phi_0+t(1+\beta)\Phi_1}{1+\beta t}
+\frac{t(1-t)w\,\Delta\tau}{(1+\beta t)^2}.}
\tag{NV8}
\]
Thus the additional marked-current term is determined by the actual trace change and the observed source overlap. It does not disappear when the minimum section moves.

The coordinate
\[
\lambda=(1+\beta)s=\frac{(1+\beta)t}{1+\beta t}
\]
is a strictly increasing bijection of \([0,1]\), with inverse
\(t=\lambda/(1+\beta-\beta\lambda)\). In this coordinate
\[
\tau=(1-\lambda)\tau_0+\lambda\tau_1,\qquad
\boxed{\Phi=(1-\lambda)\Phi_0+\lambda\Phi_1
+\lambda(1-\lambda)\frac{w\,\Delta\tau}{1+\beta}.}
\tag{NV9}
\]
This is an exact change of the interpolation parameter, with its inverse supplied; no original metric or source column has been changed.

Since \(\lambda(1-\lambda)\) has maximum \(1/4\), the absolute deviation from the weighted endpoint chord is
\[
\boxed{\max_{0\le t\le1}
\left|\Phi(t)-\frac{(1-t)\Phi_0+t(1+\beta)\Phi_1}{1+\beta t}\right|
=\frac{w|\Delta\tau|}{4(1+\beta)}.}
\tag{NV10}
\]
It is attained at \(\lambda=1/2\), equivalently \(t=1/(\beta+2)\). If \(w\Delta\tau=0\), the deviation is zero throughout and this point is still a maximizer. The signed deviation at that point is \(w\Delta\tau/[4(1+\beta)]\). Cauchy–Schwarz in the original \(Q_0\) metric proves
\[
w\le\beta Y_0,\qquad
\frac{w|\Delta\tau|}{4(1+\beta)}
\le\frac{\beta}{1+\beta}\frac{Y_0|\Delta\tau|}{4}.
\tag{NV11}
\]
This retains a factor stronger than the bound \(Y_0|\Delta\tau|/4\).

If \(\beta=0\), positivity of \(Q_0\) implies \(z=0\), so \(w=0\), \(u_B=0\), and NV3 gives \(Q(t)=Q_0,L(t)=L_0\). Both currents are constant and NV6–11 hold without division by \(\beta\). Likewise \(\xi=0\) makes all marked currents and \(w,Y_0\) zero. No normalized terminal overlap is used in either edge case.

The sign of \(\Delta\tau\) also has a finite consequence: the current polynomial in \(\lambda\) is concave for \(\Delta\tau>0,w>0\), and convex for \(\Delta\tau<0,w>0\). Its second derivative is exactly \(-2w\Delta\tau/(1+\beta)\). The three-value SC17 criterion is preserved. In particular positive endpoints remain positive when the trace increases, and negative endpoints remain negative when the trace decreases. The other cases require the actual vertex or its bound NV10; no endpoint sign is inferred.

## 3. The original next-source column and recurrence

Now specialize to the actual source addition, without substituting a different column:
\[
u=\frac{b_{N+1}}{\sqrt{\omega_{N+1}}},\quad b_j=[p_j],\quad
D(t)=G_N^{-1}+t\frac{b_{N+1}b_{N+1}^*}{\omega_{N+1}}.
\tag{NV12}
\]
For completeness, let \(V_N:\mathbb C^{N+1}\to E\) have all columns \(b_j/\sqrt{\omega_j}\), \(0\le j\le N\). The domain norm is exactly the coefficient norm in the original orthonormal polynomial basis. Its kernel consists of every degree-at-most-\(N\) polynomial divisible by \(Q_k\); these are the complete original relations. Since \(N\ge q-1\), the map is surjective. For an original class \(x\), its minimum coefficient vector is \(V_N^*(V_NV_N^*)^{-1}x\): it maps to \(x\), is orthogonal to \(\ker V_N\), and subtracting it from any other preimage leaves a vector in that kernel. Its squared norm is \(x^*(V_NV_N^*)^{-1}x\). Thus \(G_N=(V_NV_N^*)^{-1}\), with no omitted relation. Adding the one next column proves \(D(1)=G_{N+1}^{-1}\) in NV12.

The two native adjacent paths used for the original four-cutoff return are \(N=q-1\to q\) and \(N=2q-1\to2q\). Their endpoint source and terminal estimates are therefore entirely within the four original cutoffs. The finite identities apply wherever the same complete source construction is defined; the quantitative terminal statements here are asserted on these two paths.

The original even source has the exact monic recurrence
\[
Mb_{N+1}=b_{N+2}+\frac{\omega_{N+1}}{\omega_N}b_N.
\]
The zero middle coefficient follows by integrating the odd function \(y|p_{N+1}(y)|^2\) against the even source; the lower coefficient follows by testing against \(p_N\), using the leading coefficient one in the reverse recurrence. The relation-quotient map carries this polynomial identity to the same classes \(b_j\).

Let \(z_j=\Lambda b_{N+j}\), \(j=0,1,2\). The original boundary decomposition [OCP5–7](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/OBSERVED_CURRENT_PLANE.tex#L90) gives
\[
MD_0-D_0M^*=
\frac{b_{N+1}b_N^*-b_Nb_{N+1}^*}{\omega_N}.
\]
Insert NV12 and the exact recurrence. Its \(b_N,b_{N+1}\) contribution subtracts \(t\) times this boundary pair. Thus the complete unmetricized observed skew current is
\[
\boxed{\Lambda[MD(t)-D(t)M^*]\Lambda^*
=(1-t)\frac{z_1z_0^*-z_0z_1^*}{\omega_N}
+t\frac{z_2z_1^*-z_1z_2^*}{\omega_{N+1}}.}
\tag{NV13}
\]
All signs are fixed by the displayed order. Both endpoints share the actual next-source column \(z_1\). In the native edge case \(\beta=0\), \(z_1=0\), so NV13 vanishes and both observed currents are zero, strengthening their general constancy.

The original source identity and its map to the quotient are fully retained in the cited OCP proof. Human orthogonal-polynomial provenance is T. H. Koornwinder, R. Wong, R. Koekoek, R. F. Swarttouw and W. P. Reinhardt, [DLMF Chapter18](https://dlmf.nist.gov/18), with the Gamma comparison and its original recurrence read as [18.22.8](https://dlmf.nist.gov/18.22.E8). The recurrence for the arithmetic measure used here has just been derived from its parity and monic orthogonality; it is not asserted to be the Gamma recurrence itself.

## 4. The actual terminal mass controls the peak correction

Retain the full terminal domain of [RC35–44](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/CUTOFF_CURRENT_CONNECTION.md#L315): the original simple quartet, admitted five-orbit period with the stated finite corner radius, and \(\gamma\ge1000\delta\). Take the same terminal cardinal \(x\), \(\xi=\Lambda x\). Then \(Y_0>0\). In the actual source isometry \(J=L_0Q_0^{-1/2}\), retain ST5 and ST13–14:
\[
e=b_N/\sqrt{E_N},\quad f=b_{N+1}/\sqrt{F_N},\quad
u_e=J^\dagger e,\quad v_f=J^\dagger f,
\]
\[
a=\|u_e\|^2,\ d=\|v_f\|^2,\ r=u_e^*v_f,\ 
\mathfrak d=ad-|r|^2,\quad
g=u_e/\sqrt a,\quad h=(v_f-(r/a)u_e)/\sqrt{\mathfrak d/a}.
\]
\[
\widehat y=Q_0^{1/2}\xi/\sqrt{Y_0},\quad
c_g=g^*\widehat y,\ c_h=h^*\widehat y,\quad
\mu=|c_g|^2+|c_h|^2,\quad
\mathfrak s=\widehat y^*(u_eu_e^*+v_fv_f^*)\widehat y.
\tag{NV14}
\]
The support parameter \(\mu\) is the combined mass in the actual two current directions; components in their orthogonal complement remain in the unit norm of \(\widehat y\). The complete area certificate gives \(\mathfrak d\ge\Theta_N>0\), so \(d>0\). The phase-coherent terminal equation gives \(|c_g|\le\eta_N\), with the exact finite \(\eta_N\) in [TR10](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/40a766ed3a8e0eadd9947f591803255b6eecf184/workbenches/splitzero-tandem/continuations/20260922-terminal-response/TERMINAL_COHERENCE_PROOF.md).

Since \(Q_0^{1/2}z_1=\sqrt{F_N}\,v_f\), the native source parameters are exactly
\[
\beta=\frac{F_N}{\omega_{N+1}}d,\qquad
w=\beta Y_0\rho_f,\qquad
\rho_f:=\frac{|v_f^*\widehat y|^2}{d}.
\tag{NV15}
\]
Thus the marked source overlap is not replaced by its largest possible value.

The unit vector \(v_f/\sqrt d\) has coordinates
\((r,\sqrt{\mathfrak d})/\sqrt{ad}\) in the \(g,h\) plane. Its orthogonal unit complement has coordinates
\((\sqrt{\mathfrak d},-\bar r)/\sqrt{ad}\).
Taking the squared component of \(\widehat y\) on this complement proves
\[
\boxed{0\le\mu-\rho_f
=\frac{|\sqrt{\mathfrak d}\,c_g-r c_h|^2}{ad}
\le E_f:=\frac{(\sqrt{\mathfrak d}\,\eta_N+|r|)^2}{ad}.}
\tag{NV16}
\]
The complex conjugations are fixed by the two displayed unit vectors; replacing \(r c_h\) by \(\bar r c_h\) generally changes the quantity. Because
\(|r|^2\le\alpha(1-d)\), \(ad\ge\Theta_N\), and
\(\alpha,\eta_N^2\le e^{-2q\psi(s_N)+O_{h,\varpi}(k\log q)}\), the error in NV16 has this same doubled exponential rate. It requires no lower bound on \(\mu\).

There is a sharper direct receiver from the measured support itself:
\[
\rho_f=\frac{\mathfrak s-a|c_g|^2}{d},\qquad
\boxed{\max\{0,(\mathfrak s-a\eta_N^2)/d\}
\le\rho_f\le\min\{1,\mathfrak s/d\}.}
\tag{NV17}
\]
The identity follows by adding the two boundary-column squared overlaps in the definition of \(\mathfrak s\). It improves a mass-free correction bound even when the terminal support is very small.

The native source parameter has its own proved growth. Put
\(\vartheta=E_N/\omega_N\), \(\epsilon=\sqrt{E_NF_N}/\omega_N\), and \(r_\omega=\omega_{N+1}/\omega_N\). Then
\[
\beta=\frac{\epsilon^2d}{\vartheta r_\omega}.
\]
OCP5 gives \(\vartheta\ge1/2\) eventually and \(\vartheta\le1\); RC25 gives \(d\ge\Theta_N\), \(\log\epsilon=q\psi(s_N)+O(k\log q)\), and \(-\log\Theta_N=O(k\log q)\). The full source comparison in [RC22–25](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/CUTOFF_CURRENT_CONNECTION.md#L222) gives
\[
\frac{\ell_k}{u_k}(N+1)(N+1/2)
\le r_\omega\le
\frac{u_k}{\ell_k}(N+1)(N+1/2).
\]
Taking logarithms therefore proves, at every original cutoff,
\[
\boxed{\log\beta=2q\psi(s_N)+O_{h,\varpi}(k\log q),\qquad
t_{\rm peak}=\frac1{\beta+2}
=e^{-2q\psi(s_N)+O_{h,\varpi}(k\log q)}.}
\tag{NV18}
\]
The variable \(t_{\rm peak}\) is the original covariance-step fraction, not the arithmetic evolution time.

Set \(\kappa_{\rm term}=\beta\rho_f/(1+\beta)\). NV16 yields the signed and quantitative terminal receiver
\[
0\le\mu-\kappa_{\rm term}
=(\mu-\rho_f)+\frac{\rho_f}{1+\beta}
\le E_f+\frac1{1+\beta}.
\]
Thus
\[
\boxed{
\Phi(t_{\rm peak})-\tfrac12(\Phi_0+\Phi_1)
=\frac{Y_0\Delta\tau}{4}\,\kappa_{\rm term},
\qquad
\left|\Phi(t_{\rm peak})-\tfrac12(\Phi_0+\Phi_1)
-\frac{Y_0\Delta\tau}{4}\mu\right|
\le\frac{Y_0|\Delta\tau|}{4}
\left(E_f+\frac1{1+\beta}\right).
}
\tag{NV19}
\]
At the peak the weighted endpoint chord is exactly the midpoint, by NV9. The coefficient error in parentheses has the doubled exponential rate. If \(\Delta\tau=0\), both sides of the error bound are zero; division by the trace change is never required.

This also gives an absolute normalized-current error on the two original adjacent paths. At each endpoint the exact trace is \(\tau_N=-2\epsilon_N\Im r_N\), so
\[
|\Delta\tau|\le
2\epsilon_N\sqrt{\alpha_N}
+2\epsilon_{N+1}\sqrt{\alpha_{N+1}}
\le e^{O_{h,\varpi}(k\log q)}.
\]
Multiplying this bound into NV19 shows that its error divided by \(Y_0\) is at most \(e^{-2q\psi(s_N)+O_{h,\varpi}(k\log q)}\). Both endpoint leakages and both complete source metrics remain in the finite bound; no signed trace value has been evaluated.

The source step's quadratic coefficient receives the same mass estimate:
\[
\boxed{
q_2=-(1+\beta)\beta Y_0\rho_f\Delta\tau,\qquad
\left|\frac{q_2}{(1+\beta)^2}
+Y_0\mu\Delta\tau\right|
\le Y_0|\Delta\tau|
\left(E_f+\frac1{1+\beta}\right).
}
\tag{NV20}
\]
The scaling on the left is exactly the coefficient of \(\lambda^2\) in NV9. This preserves the original SC17 coefficient and gives its native terminal-mass receiver rather than assuming a current-sector occupation.

## 5. The exact source-step sign cone

Write \(A=\Phi_0\), \(B=\Phi_1\) and
\(\kappa=w\Delta\tau/(1+\beta)\). The same original current is
\[
F(\lambda)=A(1-\lambda)+B\lambda+\kappa\lambda(1-\lambda).
\]
It is nonnegative on the complete source step if and only if
\[
\boxed{A\ge0,\quad B\ge0,\quad
\kappa\ge-(\sqrt A+\sqrt B)^2.}
\tag{NV21}
\]
Necessity of the endpoint signs follows by evaluation. For the interior divide by the positive number \(\lambda(1-\lambda)\):
\[
\frac{F(\lambda)}{\lambda(1-\lambda)}
=\frac A\lambda+\frac B{1-\lambda}+\kappa.
\]
For \(A,B>0\), completing a square gives
\[
\frac A\lambda+\frac B{1-\lambda}
-(\sqrt A+\sqrt B)^2
=\frac{[\sqrt A(1-\lambda)-\sqrt B\,\lambda]^2}
{\lambda(1-\lambda)}.
\]
Its infimum is \((\sqrt A+\sqrt B)^2\), attained at
\(\lambda_*=\sqrt A/(\sqrt A+\sqrt B)\). If \(A=0,B>0\), the infimum is \(B\), approached as \(\lambda\downarrow0\); the case \(B=0,A>0\) is the opposite endpoint. If \(A=B=0\), it is zero identically. These cases prove both directions of NV21, including every zero-endpoint limit. Strict positivity on the closed step requires \(A,B>0\) and a strict third inequality.

Equivalently the exact coefficient matrix
\[
\boxed{\mathcal C_{\rm step}=
\begin{pmatrix}
A&(A+B+\kappa)/2\\
(A+B+\kappa)/2&B
\end{pmatrix}}
\tag{NV22}
\]
is copositive: its quadratic form is nonnegative for every vector with nonnegative real coordinates. Indeed at \((x,y)=(1-\lambda,\lambda)\) it equals \(F(\lambda)\), and every nonzero nonnegative vector is a positive multiple of such a vector. This proves an exact map between the original covariance path and this two-dimensional cone, with no change to its source column or endpoint metrics.

When \(A,B>0\), the boundary \(\kappa=-(\sqrt A+\sqrt B)^2\) has
\[
F(\lambda)=[\sqrt A(1-\lambda)-\sqrt B\,\lambda]^2,
\quad
\boxed{t_*=\frac{\sqrt A}{\sqrt A+(1+\beta)\sqrt B}.}
\tag{NV23}
\]
This is the actual source coordinate corresponding to \(\lambda_*\). Below the boundary, evaluation at that same \(t_*\) is strictly negative. When one endpoint is zero, a violation of NV21 produces a negative value arbitrarily near the corresponding endpoint by the explicit interior formula above. Thus failure of the cone inequality identifies the exact sign-changing source paths rather than declaring the interpolation unrelated to the sign problem.

Applying NV21 to \(-F\) gives the complete nonpositive cone:
\[
\boxed{A\le0,\quad B\le0,\quad
\kappa\le(\sqrt{-A}+\sqrt{-B})^2.}
\tag{NV24}
\]
In NV21–24 the coefficient is the original \(\kappa=w\Delta\tau/(1+\beta)\). For the native terminal source it is also \(Y_0\kappa_{\rm term}\Delta\tau\), with the full doubled-rate mass estimate NV19. Hence these are exact necessary and sufficient endpoint-and-trace tests for the actual marked source path. They do not assert which cone contains a native path before its endpoint data and trace change are evaluated.

## 6. Adjacent dual-number fibres and native source curvature

At each of the two actual endpoints \(i=N,N+1\), use that endpoint's own consecutive source vectors \(e_i,f_i\), full source metric \(G_i\), minimum isometry \(J_i\), and observed columns \(u_i=J_i^\dagger e_i\), \(v_i=J_i^\dagger f_i\). Write
\[
a_i=\|u_i\|^2,\quad d_i=\|v_i\|^2,\quad r_i=u_i^*v_i,\quad
\mathfrak d_i=a_id_i-|r_i|^2\ge\Theta_i>0.
\]
Here \(a_i\) is source support retention, not either scalar endpoint value of the function \(\psi\).
For a complex deformation parameter \(\sigma\), [DF3–12](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/4ba9285b66af58a6d58fc502a494c1fb45ca5b79/workbenches/splitzero-tandem/continuations/20260922-support-transport/OBSERVED_DEFORMATION_AND_CURRENT.md#L22) gives
\[
F_{B,i}(\sigma)=(\epsilon_i v_i+\sigma u_i)u_i^*,\quad
F_{B,i}(\sigma)^2=(a_i\sigma+\epsilon_i r_i)F_{B,i}(\sigma).
\]
Multiplication proves this identity directly. Its collision is
\(\sigma_{*,i}=-\epsilon_i r_i/a_i\). In the original orthonormal current frame,
\(F_{B,i}(\sigma_{*,i})=\epsilon_i\sqrt{\mathfrak d_i}\,h_ig_i^*\).
It is square-zero and nonzero because \(\epsilon_i>0\) and \(\mathfrak d_i>0\); positivity of \(a_i\) alone would not prove nonzero nilpotence. The support-plane algebra at that parameter is therefore faithfully the dual-number algebra, with its actual nonzero generator just displayed.

The selfadjoint part of the full endpoint action contributes zero trace current. Its rank-one boundary part gives
\(\tau_i=-2\epsilon_i\Im r_i=2a_i\Im\sigma_{*,i}\).
Define the weighted adjacent collision displacement
\(\chi_{\rm coll}=a_{N+1}\Im\sigma_{*,N+1}-a_N\Im\sigma_{*,N}\).
Then the exact original source receiver is
\[
\boxed{\Delta\tau=2\chi_{\rm coll},\qquad
q_2=-2(1+\beta)w\,\chi_{\rm coll}.}
\tag{NV25}
\]
No endpoint is compared in the other's metric. This identity uses the two actual trace scalars, each computed from its own minimum section.

The native peak and the complete path curvature become
\[
\boxed{\begin{aligned}
\Phi(t_{\rm peak})-\tfrac12(\Phi_0+\Phi_1)
&=\frac{Y_0\kappa_{\rm term}}2\,\chi_{\rm coll},\\
\frac{d^2\Phi}{d\lambda^2}
&=-\frac{4w}{1+\beta}\,\chi_{\rm coll}.
\end{aligned}}
\tag{NV26}
\]
Both formulas follow by substituting NV25 into NV9 and NV19. Thus the adjacent imaginary displacement of the dual-number fibre, with its actual support weights, controls the complete original marked-current curvature. NV19 retains the doubled-rate terminal-mass approximation to \(\kappa_{\rm term}\); NV21–24 receive \(\kappa=2w\chi_{\rm coll}/(1+\beta)\) without a sign assumption. The complex deformation parameter \(\sigma\), covariance coordinate \(t\), and its exact parameter map \(\lambda(t)\) remain distinct and explicitly related by these equations.

## 7. Source scope and checks

The full [SC1–25 proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/4ba9285b66af58a6d58fc502a494c1fb45ca5b79/workbenches/splitzero-tandem/continuations/20260922-support-transport/STABLE_HIDDEN_ACTION_AND_SIGN_STEPS.md#L136) and [ST1–20 proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/4ba9285b66af58a6d58fc502a494c1fb45ca5b79/workbenches/splitzero-tandem/continuations/20260922-support-transport/SUPPORT_SPECTRUM_AND_TERMINAL_MASS.md#L113) accompany the current local edition. Both links use the verified public support-transport edition pin; their complete source dependencies remain retained with that edition. NV1–11 rederive all finite interpolation statements directly, including their minimum maps and edge cases. NV12–20 use the actual native source column and proved original source/terminal estimates, with the public predecessor locators given above.

The checker constructs covariance sums from actual consecutive monic Gamma polynomials in an auxiliary four-root quotient, with its complete relations and cutoff minima. It verifies the native recurrence, unmetricized skew current, every interpolation and trace coefficient, and the moving minimum maps exactly. These finite matrices test the formulas; they are not observations of a hypothetical zeta zero or replacements for the original five-orbit map in the proof. Separate exact complex two-column checks test NV16's phase and the support-mass receiver. No numerical evidence is used to select an actual terminal sign.
