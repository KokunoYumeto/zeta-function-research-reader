# Stable hidden-action calculation and exact source-step signs

22 September 2026. SC1–SC25. This rederives the newly supplied stable-sign continuation and carries it through the original mixed-probe receiver. The full rectangular action on the hidden kernel suffices to evaluate all three marked currents. Coherent changes of the complete metric have an error bound governed by this restricted action; the exponentially large current eigensectors need not be subtracted. The two original adjacent-cutoff paths give exact quadratic and quartic sign laws, with all coefficients retained.

## 1. Original full hidden action and the three marked currents

Keep ST1–ST3, the original fixed \(M,\Lambda,x\), and \(Mx=\omega x\). At an original metric \(G\), write \(h=P_Kx\), \(y=P_Bx\), \(Y=\|y\|_G^2\), \(r_K=\|h\|_G/\|y\|_G\). The established terminal domain gives \(Y>0\). Every adjoint is in the stated original metric, conjugate-linear in its first argument. Define
\[
\zeta=\langle y,Mh\rangle_G/Y,\qquad
\chi=\langle h,Mh\rangle_G/Y,\qquad
\xi=\omega r_K^2-\chi.
\tag{SC1}
\]
The eigenvalue equation and \(h\perp_G y\) give \(\langle y,My\rangle=\omega Y-\langle y,Mh\rangle\), and \(\langle h,My\rangle=\omega\|h\|^2-\langle h,Mh\rangle\). Hence
\[
j_G(x):=\Phi_G(\Lambda x)/Y=-2\Im\omega+2\Im\zeta.
\tag{SC2}
\]
For \(\omega=k\gamma-ik\delta\), its sign is exactly the sign of \(k\delta+\Im\zeta\). This is the original [RC32 interference identity](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/CUTOFF_CURRENT_CONNECTION.md#L283), with its complete hidden term retained.

For the physical action \(\mathscr A=kI/2+iM\), put \(z_\times=\langle h,\mathscr A y\rangle\), \(w_\times=\langle y,\mathscr A h\rangle\). Orthogonality cancels the scalar term, giving
\[
z_\times=iY\xi,\quad w_\times=iY\zeta,\quad
\overline{z_\times}w_\times/Y^2=\bar\xi\zeta.
\tag{SC3}
\]
If \(\xi=A+iB\), \(\zeta=u+iv\), the real and imaginary parts are exactly \(Au+Bv\) and \(Av-Bu\). Thus the bilinear currents and centered current have a proved common scalar receiver while retaining their different signs.

Let \(I_K\) be the complete fixed kernel frame, \(H_K=I_K^*GI_K\), \(b_K=I_K^*Gx\), \(c_K=H_K^{-1}b_K\), \(F_K=MI_K\), \(A_K=I_K^*GF_K\), \(s_K=x^*GF_K\). Then
\[
h=I_Kc_K,\quad Y=x^*Gx-b_K^*H_K^{-1}b_K,
\quad\zeta=(s_Kc_K-c_K^*A_Kc_K)/Y,
\quad\chi=c_K^*A_Kc_K/Y.
\tag{SC4}
\]
The kernel projection formula proves the first two identities. Substitution of \(y=x-I_Kc_K\) proves the last two. In particular \(F_K\) retains its full codomain \(E\); it is not replaced by its kernel-to-kernel compression.

The original source decomposition gives
\[
B_K:=\|M|_K\|_{G\to G}\le\|C\|+\epsilon\sqrt\alpha,
\quad |\zeta|\le B_Kr_K,\quad |\chi|\le B_Kr_K^2.
\tag{SC5}
\]
For \(h\in K\), \(|e^\dagger h|=|(P_Ke)^\dagger h|\le\sqrt\alpha\|h\|\). Apply the triangle inequality to \(Mh=Ch+\epsilon f(e^\dagger h)\), then Cauchy–Schwarz to SC1. Thus \(\log\max(1,B_K)=O(k\log(q+2))\) by RC25. The terminal visibility estimate TR3 bounds \(r_K\le\sqrt{\mathfrak l_{k,N}^{-1}-1}\) with \(-\log\mathfrak l=O(k\log(q+2))\). These are proved native bounds, with the original period guard.

## 2. Coherent complete-metric error, including the projection derivative

For two positive complete metrics \(G_0,G_1\), fix the same \(M,\Lambda,x,\omega\), and let
\[
S=G_0^{-1/2}G_1G_0^{-1/2},\quad
d=\tfrac12\log(\lambda_{\max}(S)/\lambda_{\min}(S)),
\quad B=B_K(G_0),\quad r=r_K(G_0).
\tag{SC6}
\]
These are finite-dimensional statements on the actual metric family. Along a differentiable positive-metric path put \(E_t=G_t^{-1}\dot G_t\); it is selfadjoint in \(G_t\). Differentiation of \(P_K=I_K(I_K^*GI_K)^{-1}I_K^*G\) gives
\[
\dot P_K=P_KE_tP_B,\quad\dot h=P_KE_ty,\quad
\dot y=-P_KE_ty,\quad\dot Y=\langle y,E_ty\rangle.
\tag{SC7}
\]
For the last equation, both vector-derivative terms vanish by \(y\perp K\). In the derivative of \(b=\langle y,Mh\rangle\), the derivative of the first vector cancels the hidden part of the metric derivative. Exactly
\[
\dot b=\langle y,E_tP_BMh\rangle
+\langle y,MP_KE_ty\rangle,
\quad |\dot\zeta|\le B_t(1+2r_t)\|E_t\|_{G_t}.
\tag{SC8}
\]
Indeed the first term has magnitude at most \(B_t r_tY_t\|E_t\|\), and the second at most \(B_tY_t\|E_t\|\). The derivative of \(1/Y_t\) contributes at most another \(B_tr_t\|E_t\|\). Both surviving actions of \(M\) have arguments in the fixed full kernel.

Let \(a_0=\tfrac12(\log\lambda_{\max}S+\log\lambda_{\min}S)\) and use the exact path \(G_t=G_0^{1/2}\exp(t(\log S-a_0I))G_0^{1/2}\), \(0\le t\le1\). Here \(a_0\) is only this paragraph's metric scalar, not the monic-profile endpoint. The endpoint is \(e^{-a_0}G_1\). Multiplying a whole metric by a positive scalar leaves its projections, SC1 and normalized current unchanged and multiplies the unnormalized current by that positive scalar. This proves the exact connecting map used for this path. Its relative eigenvalues lie in \([e^{-td},e^{td}]\), so
\[
\|E_t\|_{G_t}=d,\quad B_t\le e^{td}B,
\quad r_t^2\le e^{2td}(1+r^2)-1.
\tag{SC9}
\]
The last bound compares \(\|x\|_{G_t}^2\) and the complete minimum \(Y_t=\min_{h\in K}\|x-h\|_{G_t}^2\) using the same two relative form bounds.

Define the explicitly evaluated integral
\[
\mathcal F(d,r)=\int_1^{e^d}[1+2\sqrt{(1+r^2)s^2-1}]\,ds,
\]
\[
\mathcal F(d,r)=e^d-1+e^d\sqrt{(1+r^2)e^{2d}-1}-r
-\frac{\operatorname{arcosh}(e^d\sqrt{1+r^2})-\operatorname{arcosh}\sqrt{1+r^2}}{\sqrt{1+r^2}}.
\tag{SC10}
\]
Differentiating the second expression with respect to its upper endpoint gives the first integrand; the lower-endpoint value is zero. The formula extends to \(r=0\) by continuity. Integrating SC8 using SC9 and \(s=e^{td}\) proves
\[
\boxed{|\zeta_{G_1}-\zeta_{G_0}|\le B\mathcal F(d,r),\qquad
|j_{G_1}-j_{G_0}|\le2B\mathcal F(d,r).}
\tag{SC11}
\]
This keeps the full change in metric and projection together. It does not bound independent perturbations of eigensector coordinates by the same number.

The bilinear currents have a complete disk estimate as well. Put \(r_*=[e^{2d}(1+r^2)-1]^{1/2}\), \(\delta_\zeta=B\mathcal F(d,r)\), and
\[
\delta_\xi=2d(|\omega|+e^dB)r_*(1+r_*).
\tag{SC12}
\]
Differentiating \(r_t^2=\|h_t\|^2/Y_t\) gives \(|(r_t^2)'|\le2r_t(1+r_t)\|E_t\|\). The two vector derivatives and metric derivative of \(\langle h,Mh\rangle/Y\) give \(|\dot\chi|\le2B_tr_t(1+r_t)\|E_t\|\): each vector derivative is at most \(B_tr_tY\|E_t\|\), and the numerator metric and denominator terms total at most \(2B_tr_t^2Y\|E_t\|\). Integrating proves \(|\xi_1-\xi_0|\le\delta_\xi\). Expanding the product difference now gives
\[
|\bar\xi_1\zeta_1-\bar\xi_0\zeta_0|
\le|\xi_0|\delta_\zeta+|\zeta_0|\delta_\xi+\delta_\xi\delta_\zeta.
\tag{SC13}
\]
Its real and imaginary parts have this same radius.

For \(0\le d\le1/4\), \(\mathcal F(d,r)\le5(1+r)d\). An explicit bound suffices: in its equivalent integral over \(t\in[0,1]\), use \(e^{td}\le4/3\), \(\sqrt{e^{2td}-1}<1\), and \(\sqrt{e^{2td}r^2+e^{2td}-1}\le(4/3)r+1\). The integral is at most \([4+(32/9)r]d\le5(1+r)d\). Thus
\[
|j_1-j_0|\le10B(1+r)d.
\tag{SC14}
\]
If \((1-\eta)G_0\preceq G_1\preceq(1+\eta)G_0\), \(0\le\eta\le1/8\), then \(d\le\operatorname{arctanh}\eta\le2\eta\). An evaluated current margin \(\mu>0\) therefore retains half its margin when \(\eta\le\min\{1/8,\mu/[40B(1+r)]\}\). This is an error certificate for an evaluated center, not an assertion of a native margin. By SC5, the sufficient logarithmic precision is \(O(k\log(q+2))+\log^+(1/\mu)\).

## 3. The exact adjacent-cutoff polynomial in the original parameter

Let \(u\) be the next actual source column, and retain \(G(t)=(G^{-1}+tuu^*)^{-1}\), \(t\ge0\); the adjacent native cutoffs are \(t=0,1\). In this section \(u\) denotes that source column, not the boundary column in ST5. Define
\[
u_K=P_Ku,\quad u_B=P_Bu,\quad
a=\|u_K\|_G^2,\quad\beta=\|u_B\|_G^2,
\quad\rho=\langle u_B,x\rangle_G,\quad s=t/(1+\beta t).
\tag{SC15}
\]
Direct multiplication of inverse matrices, or the complete original [ACC4–8 proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/40a766ed3a8e0eadd9947f591803255b6eecf184/workbenches/splitzero-tandem/continuations/20260922-terminal-response/RETAINED_COMPLETE_PROOF_SOURCES.tex#L131648), gives
\[
G(t)=G-\frac{s}{1+as}Guu^*G,\qquad
h_s=h-s\rho u_K,\qquad y_s=y+s\rho u_K.
\]
\[
\langle y_s,v\rangle_{G(t)}=\langle y,v\rangle_G-s\bar\rho\langle u_B,v\rangle_G
\quad(v\in E),\qquad Y_s=Y-s|\rho|^2>0.
\tag{SC16}
\]
For the projection formula, \(x-y_s\in K\), and the displayed covector annihilates \(K\); uniqueness of the orthogonal minimum proves it. To verify the covector, expand \(y_s^*G(t)\), use \(y^*Gu=\bar\rho\), \(u_K^*Gu=a\), and cancel its \(1+as\) factor. Finally \(|\rho|^2\le\beta Y\) gives \(Y_s\ge Y/(1+\beta t)>0\).

It follows that the full unnormalized marked current is exactly \(Q(s)=q_0+q_1s+q_2s^2\), where
\[
q_0=-2\Im[\omega Y-\langle y,Mh\rangle_G],
\]
\[
q_1=-2\Im[\rho\langle y,Mu_K\rangle_G-\omega|\rho|^2+\bar\rho\langle u_B,Mh\rangle_G],
\quad q_2=2|\rho|^2\Im\langle u_B,Mu_K\rangle_G.
\tag{SC17}
\]
Insert \(My_s=My+s\rho Mu_K\) in SC16, then substitute \(My=\omega x-Mh\). This proves all three coefficients and shows every non-eigenvalue action has its argument in the original full kernel. In the literal source parameter,
\[
\Phi_{G(t)}(\Lambda x)=\frac{q_0+(2\beta q_0+q_1)t+(\beta^2q_0+\beta q_1+q_2)t^2}{(1+\beta t)^2}.
\tag{SC18}
\]
The denominator is positive. On the native step, \(s\in[0,s_1]\), \(s_1=1/(1+\beta)\). The minimum of \(Q\) is attained at an endpoint or, only when \(q_2>0\) and \(0<-q_1/(2q_2)<s_1\), at its vertex with value \((4q_0q_2-q_1^2)/(4q_2)\). This follows by differentiating the polynomial. Thus at most three real evaluations decide positivity on the complete step; apply the same rule to \(-Q\) for negativity. Coefficient radii \(\delta_i\) bound its entire interval error by \(\delta_0+s_1\delta_1+s_1^2\delta_2\). Direct differentiation also proves
\[
\left(\frac{Q(s)}{Y-s|\rho|^2}\right)''=
\frac{2[q_2Y^2+q_1Y|\rho|^2+q_0|\rho|^4]}{(Y-s|\rho|^2)^3}.
\tag{SC19}
\]
The curvature sign is constant on this complete source step, including the case of zero curvature.

## 4. All coefficients of the imaginary bilinear current

For this paragraph let \(A\) be any fixed full action, and in the programme take \(A=\mathscr A\). Put \(\eta_K=\langle u_K,h\rangle_G\). Define
\[
W_0=\langle y,Ah\rangle,\quad
W_1=-\rho\langle y,Au_K\rangle-\bar\rho\langle u_B,Ah\rangle,
\quad W_2=|\rho|^2\langle u_B,Au_K\rangle,
\]
\[
Z_0=\langle h,Ay\rangle,
\quad Z_1=\rho\langle h,Au_K\rangle+aZ_0-\bar\rho\langle u_K,Ay\rangle-\bar\eta_K\langle u,Ay\rangle,
\]
\[
Z_2=a\rho\langle h,Au_K\rangle-|\rho|^2\langle u_K,Au_K\rangle
-\rho\bar\eta_K\langle u,Au_K\rangle+a\bar\rho\langle u_B,Ay\rangle,
\quad Z_3=aW_2.
\tag{SC20}
\]
All inner products here are the initial \(G\)-products. Expanding SC16 proves \(w_\times(s)=\sum_{v=0}^2W_vs^v\). For the reverse product, direct expansion gives the covector
\[
h_s^*G(t)=\frac{h^*G+s(ah^*G-\bar\rho u_K^*G-\bar\eta_Ku^*G)+s^2a\bar\rho u_B^*G}{1+as}.
\]
Multiplying by \(A(y+s\rho u_K)\) proves \(z_\times(s)=\sum_{u=0}^3Z_us^u/(1+as)\) and every coefficient SC20. The highest coefficient of the product numerator is \(\bar Z_3W_2=a|W_2|^2\), which is real. Therefore, with
\[
I_j=\Im\sum_{u+v=j,\ 0\le u\le3,\ 0\le v\le2}\bar Z_uW_v\quad(0\le j\le4),
\]
\[
\boxed{\Im(\overline{z_\times(t)}w_\times(t))=
\frac{\sum_{j=0}^4 I_jt^j(1+\beta t)^{4-j}}{[1+(a+\beta)t](1+\beta t)^3}.}
\tag{SC21}
\]
Both denominator factors are positive. A nonzero imaginary numerator has at most four real zeros counted with multiplicity. Its sign on a finite step is determined by this actual real quartic; an identically zero numerator is retained. The real numerator retains the fifth-degree term unless that explicit coefficient vanishes.

## 5. Exact finite examples and sharpness

The following examples test the scope of the algebraic statements. They are not native-period numerical samples. First take \(G=I_3\),
\[
C=\begin{pmatrix}0&-3/5&0\\-3/5&0&-4/5\\0&-4/5&0\end{pmatrix},\quad
M=C+\tfrac{10}{3}e_2e_1^*,\quad
x=(3/10,i/2,2/5)^T,\quad v=(0,4i/5,3/5)^T,\quad K=\mathbb Cv.
\]
Multiplication gives \(Mx=-ix\), \(C=C^*\), \(\|C\|=1\), \(\|x\|^2=1/2\), \(\|h\|^2=256/625\), \(Y=113/1250\), \(\langle h,Mh\rangle=0\), and \(\langle y,Mh\rangle=-64i/625\). Thus the full eigenclass current is \(1\), whereas \(\Phi_G=-3/125\). For the unchanged \(M,K,x\), use the source column \(u=v+y\). Substitution in SC17–18 gives
\[
\Phi_{G(t)}=\frac{10(4181t-3750)}{(113t+1250)^2},
\quad t_*=3750/4181\in(0,1),\quad\Phi_{G(1)}=4310/1857769>0.
\tag{SC22}
\]
This computes a crossing with a fixed eigenclass, zero hidden self-current and unchanged first outgoing direction. It does not infer a native sign from those properties.

For two crossings take \(M=\left(\begin{smallmatrix}0&0&0\\i/2&-3i/256&0\\-67i/256&0&-3i/256\end{smallmatrix}\right)\), \(x=(0,1,1)^T\), \(K=\mathbb Ce_1\), \(u=(1,1,0)^T\). Then \(Mx=-3ix/256\), and SC18 gives \(\Phi_{G(t)}=(7t-1)(5t-3)/[64(1+t)^2]\), with zeros \(1/7,3/5\). The degree-two bound is attained. For the same \(x,K,u\), put \(A=\left(\begin{smallmatrix}0&0&0\\1&0&0\\i&0&0\end{smallmatrix}\right)\). SC20 gives \(z_\times=t^3/[(1+t)^2(1+2t)]\), \(w_\times=-t/(1+t)^2-it/(1+t)\), and
\[
\Im(\bar z_\times w_\times)=-\frac{t^4}{(1+2t)(1+t)^3}.
\tag{SC23}
\]
This attains degree four. All these substitutions are verified as exact rational identities by the accompanying script, alongside the general projection, coefficient and differential identities.

## 6. New return through the mixed probes and all four original cutoffs

At each original cutoff, MP19–24 and SC2 give the exact additional receiver
\[
\boxed{\frac{\widehat b^*\mathcal C_{\rm ord}\widehat b}{s_{\rm mix}}
=-2\Im\omega+2\Im\zeta_G,\qquad
\widehat b=Q_B^{1/2}\Lambda x/\sqrt Y.}
\tag{SC24}
\]
Here \(s_{\rm mix}=(\dim B-\operatorname{tr}A)/(q-2)\) is MP5; it is different from the source-activation parameter in SC15. Both are explicitly specified. Therefore the complete ratio on the left, recalculated from the same coherently varied metric, obeys SC11 and SC14. This carries the new stability estimate through the mixed construction without paying the norm of the large current or assigning independent perturbations to its terms. The original MP inverse still bounds errors in an independently supplied Hermitian mixed-product operator by \(1/s_{\rm mix}<6\). These two statements address their stated error models.

For each of the two original adjacent-cutoff paths, calculate the three actual coefficients SC17. Denote them \(q_i^-\) at \(q-1\to q\), \(q_i^+\) at \(2q-1\to2q\), and denote their actual source values by \(\beta_-\), \(\beta_+\). The full unnormalized four-cutoff current is exactly
\[
\boxed{\mathcal R\Phi=
2q_0^-+\frac{q_1^-}{1+\beta_-}+\frac{q_2^-}{(1+\beta_-)^2}
-2q_0^+-\frac{q_1^+}{1+\beta_+}-\frac{q_2^+}{(1+\beta_+)^2}.}
\tag{SC25}
\]
This is substitution of the literal endpoints \(t=0,1\) in SC18 with signs \(+,+,-,-\). It retains the unnormalized class and the original metric at each endpoint. The two real quartics SC21 likewise give both endpoint imaginary bilinear currents with their complete denominators. No sign of these original coefficients has been selected from magnitude bounds. The unfinished calculation is now their signed native value, with exact finite equations and coherent full-metric precision requirements already supplied.

Provenance: the stable-sign continuation supplied on22September is rederived in full above, including the three exact examples. The source-step data and complete complex currents are the original ACC1–16; the rectangular hidden-action and period bounds are the pinned RC22–44 and TR1–24 proofs linked above. The new receiver SC24 and four-cutoff formula SC25 apply them to MP19–24. Human-source provenance for the inherited arithmetic source remains in those complete published proofs. No new human literature or native-period numerical evaluation is claimed.
