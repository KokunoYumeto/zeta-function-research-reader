# Complex phase coherence of the original terminal current

22 September 2026. This is a continuation of RC35–44 and CE1–29. The exact original terminal class has exponentially balanced current-sign weights. Here the eigenclass equation controls their complex amplitudes, with a doubled exponential rate for the phase-coherence deficit. All estimates use the original observation projection; the argument does not optimize over substitute projections.

## 1. Original object and proved domain

Keep \(k\equiv1\pmod4\), \(k\ge17\), \(q=(k+1)^2\), \(q_0=(k-7)^2\), the original simple quartet \(0<\delta<1/2,\gamma>2\), admitted period and branch. In the physical coordinate \(S=k/2+iy\), the coefficient algebra, multiplication and terminal cardinal are
\[
E=\mathbb C[y]/Q_k,\qquad M[p]=[yp],\qquad
x=v_+(S)=\frac{\chi_k(S)}{(S-k\rho)\chi_k'(k\rho)},\quad
\rho=\tfrac12+\delta+i\gamma,\quad
Mx=\omega x,\quad\omega=k\gamma-ik\delta.
\tag{TR1}
\]
For every original cutoff \(q-1\le N\le2q\), retain the entire source metric \(G_N\), original onto map \(\Lambda\), full invariant kernel \(K=\ker\Lambda\), and
\[
Q_B=(\Lambda G_N^{-1}\Lambda^*)^{-1},\qquad
L=G_N^{-1}\Lambda^*Q_B,\qquad P=L\Lambda.
\tag{TR2}
\]
The adjoint is in the stated metric, with inner products conjugate-linear in the first argument. CE2–3 prove that \(P\) is the \(G_N\)-orthogonal projection onto \(K^\perp\); \(\Lambda:(K^\perp,G_N)\to(B,Q_B)\) is an isometry with inverse \(L\). Consequently every calculation below on \(y=Px\) is a calculation of the original observed class \(\Lambda x\), with its actual minimum norm.

The terminal nonvanishing and quantitative norm comparison are used precisely on the period domain of RC37–42: \(\gamma\ge1000\delta\), the retained five-orbit requirement, and \(|\varpi|\ge R_{\rm corner}\), with the actual finite \(R_{\rm corner}\) of RC37–38. Its proof uses the original coefficient \(C_Av_+=a_{88}v_-\), not a selected replacement column. Write
\[
\theta=\frac{\|Px\|_{G_N}^2}{\|x\|_{G_N}^2},\qquad
\theta_K=1-\theta,\qquad
\theta\ge\mathfrak l_{k,N}>0,\qquad
-\log\mathfrak l_{k,N}=O_{h,\varpi}(k\log(q+2)).
\tag{TR3}
\]
The complete finite formula for \(\mathfrak l_{k,N}\) and its conductor/reverse-lift proof are RC40–42; no other period domain is inferred here.

Retain the full even-source monic classes \(b_N,b_{N+1}\) and their norms \(E_N,F_N,\omega_N\). Put
\[
e=b_N/\sqrt{E_N},\qquad f=b_{N+1}/\sqrt{F_N},\qquad
\epsilon=\sqrt{E_NF_N}/\omega_N,\qquad
M=C+\epsilon f e^\dagger,\quad C=C^\dagger,\quad e\perp f,\quad
\|e\|=\|f\|=1.
\tag{TR4}
\]
This is the exact original action CE5/OCP5–7. The degree-\(N+1\) class is represented by its complete degree-\(N\) minimum, so the cutoff has not changed. Set
\[
c=2(N+1)\sqrt{u_0/\ell_0},\quad \|C\|\le c,\quad
D=|\omega|+c,\quad
u=Pe,\quad v=Pf,\quad
a=\|u\|^2,\quad d=\|v\|^2,\quad r=\langle u,v\rangle,
\]
\[
\mathcal C=\begin{pmatrix}a&r\\\bar r&d\end{pmatrix},\quad
\mathfrak d=ad-|r|^2,\quad
\alpha=\|(I-P)e\|^2=1-a.
\tag{TR5}
\]
The notation here is exactly \(u_0=u_k,\ell_0=\ell_k\), the original complete source constants of RC22/RD4 through degree \(2q+2\); thus the actual source-comparison ratio is retained. On the eventual finite guards proved in the conductor calculation,
\[
0\prec\mathcal C\preceq I_2,\quad
\mathfrak d\ge\Theta_N>0,\quad |r|^2\le\alpha(1-d)\le\alpha.
\tag{TR6}
\]
For the last inequality, \(e\perp f\) gives \(r=-\langle(I-P)e,(I-P)f\rangle\), then apply Cauchy–Schwarz to these actual hidden vectors.
Since the larger eigenvalue of \(\mathcal C\) is at most one, its smaller eigenvalue is at least its determinant; consequently \(a,d\ge\Theta_N\).

## 2. The terminal equation constrains a complex coordinate

Let \(A=\langle e,x\rangle\), \(B=\langle f,x\rangle\). From TR1 and TR4,
\[
\epsilon A f=(\omega-C)x,\qquad
\epsilon|A|\le D\|x\|.
\tag{TR7}
\]
This is a vector equation before observation. After the complete original projection,
\[
\langle e,Px\rangle=A-\langle(I-P)e,(I-P)x\rangle.
\]
Hence
\[
\frac{|\langle e,Px\rangle|}{\|Px\|}
\le\frac{D/\epsilon+\sqrt{\alpha\theta_K}}{\sqrt\theta}.
\tag{TR8}
\]
The conductor lower bound TR3 is what makes the denominator quantitative. It is not omitted.

Define the exact orthonormal pair in the original observed space by
\[
g=\frac{u}{\sqrt a},\qquad
h=\frac{v-(r/a)u}{\sqrt{\mathfrak d/a}}.
\tag{TR9}
\]
The subtraction is the actual projection of \(v\) on \(u\). Direct multiplication with TR5 proves \(\langle g,h\rangle=0\) and both norms equal one. In particular no cross phase has been discarded. Let
\[
\widehat y=\frac{Px}{\|Px\|},\qquad
c_g=\langle g,\widehat y\rangle,\qquad
c_h=\langle h,\widehat y\rangle,\qquad
y_0=\widehat y-c_gg-c_hh.
\]
Then \(y_0\) is orthogonal to both \(g,h\), and
\[
\boxed{|c_g|\le\eta_N:=
\min\left\{1,\frac{D/\epsilon+\sqrt{\alpha\theta_K}}{\sqrt{a\theta}}\right\}.}
\tag{TR10}
\]
Indeed \(P^\dagger=P\) and \(P\widehat y=\widehat y\), so \(\langle g,\widehat y\rangle=\langle e,Px\rangle/(\sqrt a\|Px\|)\); apply TR8. TR10 controls the entire complex coordinate, not only its imaginary part.

Using \(\theta\ge\mathfrak l_{k,N}\), \(a\ge\Theta_N\), and the completed source estimates RC25,
\[
\log\epsilon=q\psi(t_N)+O_{h,\varpi}(k\log q),\quad
-\log\Theta_N=O_{h,\varpi}(k\log q),\quad
\alpha\le e^{-2q\psi(t_N)+O_{h,\varpi}(k\log q)},\quad
\log D=O_h(k+\log q),
\]
\[
t_N=(N+1-q)/q,
\]
we obtain, uniformly on all original cutoffs and the stated period domain,
\[
\boxed{\eta_N\le
\exp[-q\psi(t_N)+O_{h,\varpi}(k\log q)].}
\tag{TR11}
\]
The profile \(\psi\) is the original monic profile in RC8/OCP31, not the heat profile \(J\); their exact relation is RC7–10.

There is a geometric consequence in the original metric. If
\(\mathcal H_N=\{b\in K^\perp:\langle Pe,b\rangle=0\}\), then
\[
\operatorname{dist}_{G_N}(\widehat y,\mathcal H_N)=|c_g|\le\eta_N.
\tag{TR12}
\]
This is a complex hyperplane, with exactly defined orthogonal projection \(I-gg^\dagger\) on \(K^\perp\). It contains the original zero-current line generated by \(h\) and the entire zero eigenspace of the current. Equation TR12 does not assert that \(\widehat y\) has a nonzero component along \(h\).

More precisely, this exact hyperplane is a maximal totally isotropic subspace for the original Hermitian current form:
\[
\boxed{\mathcal H_N=\operatorname{span}_{\mathbb C}\{h\}\oplus\ker W,\quad
\langle z,Wz'\rangle=0\quad(z,z'\in\mathcal H_N),\quad
\dim_{\mathbb C}\mathcal H_N=\dim B-1.}
\tag{TR12a}
\]
The current matrix TR13 has zero \(h,h\) entry and is zero on the orthogonal complement of \(g,h\), proving the stated vanishing of the complete restricted form. Its two nonzero eigenvalues have opposite signs, so the induced nondegenerate form on \(K^\perp/\ker W\) has signature \((1,1)\). A totally isotropic subspace of that two-dimensional quotient has dimension at most one: dimension two would be the whole space and would force the nondegenerate form to vanish. Every totally isotropic subspace of the original space therefore has dimension at most \(1+\dim\ker W=\dim B-1\), attained by \(\mathcal H_N\). Its quotient \(\mathcal H_N/\ker W\) is the exactly specified isotropic line generated by the class of \(h\). The operator itself does not vanish on \(h\): TR13 gives \(Wh=-i\epsilon\sqrt{\mathfrak d}\,g\ne0\). Thus the space records vanishing of the restricted current form, while retaining the nonzero action into its complementary direction.

## 3. Canonical phases in the two current eigenspaces

In \(K^\perp\), the original centered Hermitian current is
\[
W=i\epsilon(vu^\dagger-uv^\dagger).
\]
Its exact matrix in the retained pair \(g,h\) is
\[
W\big|_{\operatorname{span}\{g,h\}}=
\epsilon\begin{pmatrix}-2\Im r&-i\sqrt{\mathfrak d}\\
i\sqrt{\mathfrak d}&0\end{pmatrix},
\qquad W y_0=0.
\tag{TR13}
\]
Substitute \(u=\sqrt a\,g\) and
\(v=(r/\sqrt a)g+\sqrt{\mathfrak d/a}\,h\) to prove this directly. Thus
\[
\lambda_+=\epsilon[-\Im r+\sqrt{\mathfrak d+(\Im r)^2}]>0,\qquad
\lambda_-=\epsilon[-\Im r-\sqrt{\mathfrak d+(\Im r)^2}]<0.
\]
Put \(\lambda_p=\lambda_+\), \(\lambda_n=-\lambda_-\), and
\[
A_*=\sqrt{\frac{\lambda_p}{\lambda_p+\lambda_n}},\qquad
B_*=\sqrt{\frac{\lambda_n}{\lambda_p+\lambda_n}},\qquad
w_+=-iA_*g+B_*h,\qquad
w_-=iB_*g+A_*h.
\tag{TR14}
\]
These are an orthonormal eigenpair for \(W\): the characteristic equation is
\(\lambda^2+2\epsilon(\Im r)\lambda-\epsilon^2\mathfrak d=0\),
so substituting TR14 in TR13 verifies both equations. Their phases are fixed by positive real \(h\)-components. This definition uses the original real-\(y\) monic phases in TR4 and the exact Gram map TR9; it is not an arbitrary identification of two eigenvector phases.

Write
\[
z_+=\langle w_+,\widehat y\rangle=iA_*c_g+B_*c_h,\qquad
z_-=\langle w_-,\widehat y\rangle=-iB_*c_g+A_*c_h,
\quad p_\pm=|z_\pm|^2.
\tag{TR15}
\]
The two exact complex amplitude identities are
\[
\boxed{A_*z_+-B_*z_-=ic_g,\qquad
B_*z_++A_*z_-=c_h.}
\tag{TR16}
\]
They follow from \(A_*^2+B_*^2=1\). In particular TR10 proves
\[
|A_*z_+-B_*z_-|\le\eta_N.
\]
Unlike a difference of squared magnitudes, this inequality controls the relative complex phase. It also remains valid when one or both amplitudes vanish.

Let
\[
\delta_N^{\rm tr}=\frac{|\Im r|}{\sqrt{\mathfrak d+(\Im r)^2}}
\le\sqrt{\alpha/\Theta_N}.
\]
Since
\[
|A_*-B_*|=\frac{|A_*^2-B_*^2|}{A_*+B_*}
=\frac{\delta_N^{\rm tr}}{A_*+B_*}
\le\delta_N^{\rm tr},\qquad A_*+B_*\le\sqrt2,
\]
TR15 gives the finite, unweighted coherent-amplitude estimate
\[
\boxed{|z_+-z_-|\le
\sqrt2\,\eta_N+\delta_N^{\rm tr}.}
\tag{TR17}
\]
Here \(|c_h|\le1\) is enough; no positive lower bound on the active current-plane mass is assumed.

The exact identity
\[
p_++p_--2\Re(z_+\overline{z_-})=|z_+-z_-|^2
\]
and TR11 yield the completed stronger receiver
\[
\boxed{0\le p_++p_--2\Re(z_+\overline{z_-})
\le(\sqrt2\,\eta_N+\delta_N^{\rm tr})^2
\le\exp[-2q\psi(t_N)+O_{h,\varpi}(k\log q)].}
\tag{TR18}
\]
Thus the real part of the sign-sector coherence equals half their combined weight up to a nonnegative error of the doubled exponential order. The phase \(\arg(z_+/z_-)\) is not defined at zero amplitude; TR18 is the globally valid statement. It strengthens RC44, which bounded only \(|p_+-p_-|\) at the single exponential order.

For clarity, the preceding weight estimate follows from this stronger one: since \(|z_++z_-|\le\sqrt{2(p_++p_-)}\le\sqrt2\),
\[
|p_+-p_-|
=|\Re((z_+-z_-)\overline{(z_++z_-)})|
\le\sqrt2\,|z_+-z_-|
\le 2\eta_N+\sqrt2\,\delta_N^{\rm tr}.
\tag{TR19}
\]
This derivation preserves all zero directions and does not divide by either sign-sector weight.

## 4. A quantitatively isolated residual current

The normalized current on the original terminal class is
\[
j_N=\frac{\Phi_N(\Lambda x)}{\|\Lambda x\|_{Q_B}^2}
=\langle\widehat y,W\widehat y\rangle.
\]
Using TR13 gives the exact expression and error estimate
\[
j_N=2\epsilon\sqrt{\mathfrak d}\,
\Im(\overline{c_g}c_h)-2\epsilon(\Im r)|c_g|^2,
\]
\[
\boxed{\left|j_N-
2\epsilon\sqrt{\mathfrak d}\Im(\overline{c_g}c_h)\right|
\le2\epsilon|r|\eta_N^2
\le\exp[-2q\psi(t_N)+O_{h,\varpi}(k\log q)].}
\tag{TR20}
\]
Indeed \(\epsilon=e^{q\psi+O(k\log q)}\), \(|r|\le\sqrt\alpha\le e^{-q\psi+O(k\log q)}\), and \(\eta_N^2\le e^{-2q\psi+O(k\log q)}\). The diagonal trace correction is therefore absolutely exponentially small. The leading term can remain subexponential: multiplication by \(\epsilon\) reverses the single exponential size of \(c_g\). Neither TR18 nor TR20 evaluates the sign of this retained imaginary product. It is an actual original-metric pairing, with its exact scale and negligible trace term now determined.

All these estimates hold separately at \(N=q-1,q,2q-1,2q\), whose unchanged arguments are \(0,1/q,1,1+1/q\). No individual sign or four-cutoff signed-current value is obtained by treating the positive upper bounds as signed values.

## 5. Independent check of the response-amplification dictionary

The source physical convention is \(b_n^S=i^n b_n\). Thus, with \(F_{13}=\langle b_N^S,x\rangle\), \(F_{23}=\langle b_{N+1}^S,x\rangle\), one has
\[
F_{13}=i^{-N}\sqrt{E_N}\,A,\qquad
F_{23}=i^{-(N+1)}\sqrt{F_N}\,B,\qquad
\mathfrak c_{N,\lambda}
=\frac{\overline{F_{13}}F_{23}}{\omega_N\|x\|^2}
=-i\epsilon\,\frac{\bar A B}{\|x\|^2}.
\tag{TR21}
\]
This verifies the imaginary factor in the real-\(y\) coordinate. NCE9–13 prove for this exact terminal eigenclass
\(\Re\mathfrak c_{N,\lambda}=k\delta\) and
\(|\Im\mathfrak c_{N,\lambda}|<k\gamma\). In particular
\[
k\delta\le|\mathfrak c_{N,\lambda}|<|\omega|.
\]
Both denominators are nonzero. Define the original dimensionless responses
\[
\mathfrak A=\frac{\|x\|^2}{|A|^2},\qquad
\mathfrak B=\frac{\|x\|^2}{|B|^2}.
\]
The exact phase dictionary TR21 and the eigenclass estimate TR7 prove
\[
\boxed{\mathfrak A\mathfrak B
=\frac{\epsilon^2}{|\mathfrak c_{N,\lambda}|^2},\quad
\frac{\epsilon^2}{D^2}\le\mathfrak A
\le\frac{\epsilon^2}{(k\delta)^2},\quad
1\le\mathfrak B\le\frac{D^2}{|\mathfrak c_{N,\lambda}|^2}
\le\frac{D^2}{(k\delta)^2}.}
\tag{TR22}
\]
For the upper bound on \(\mathfrak A\), use \(\mathfrak B\ge1\), which is Cauchy–Schwarz with the original unit vector \(f\). For its lower bound use TR7. Then divide the exact product by that lower bound to bound \(\mathfrak B\). The precise source estimate \(\log(u_0/\ell_0)=O_h(k+\log q)\) gives
\[
\log\mathfrak B=O_h(k+\log q),\qquad
\log\mathfrak A=2q\psi(t_N)+O_{h,\varpi}(k\log q).
\tag{TR23}
\]
These independently verify the root's separate leading amplification rates.

If \(\beta_K=\|(I-P)f\|^2\), the original response ratios NCE14 are
\[
U=\frac{\langle e,(I-P)x\rangle}{A},\qquad
V=\frac{\langle f,(I-P)x\rangle}{B}.
\]
The physical unit factors in TR21 cancel in each respective ratio. Cauchy–Schwarz on the two actual hidden vectors and TR22 yield
\[
\boxed{|U|\le\sqrt{\mathfrak A\alpha\theta_K}
\le\frac{\epsilon\sqrt{\alpha\theta_K}}{|\mathfrak c_{N,\lambda}|},
\quad
|V|\le\sqrt{\mathfrak B\beta_K\theta_K}
\le\frac{D\sqrt{\beta_K\theta_K}}{|\mathfrak c_{N,\lambda}|}.}
\tag{TR24}
\]
The first displayed upper bound for \(\mathfrak A\) in TR22 was deliberately weaker than its exact \(\epsilon^2/|\mathfrak c|^2\) upper bound; using the latter proves TR24. No individual response or its sign is inferred from these magnitude bounds.

## 6. Proof provenance and remaining calculation

The exact original action, metric isometry and evolution are proved in [CE1–8 of the sealed 026 EVOLUTION_PROOF.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/EVOLUTION_PROOF.md#L18). The terminal conductor coefficient, reverse lift and norm comparison are [RC35–42](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/CUTOFF_CURRENT_CONNECTION.md#L315), with the [exact period domain at RC37–39](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/CUTOFF_CURRENT_CONNECTION.md#L332). [RC25](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/CUTOFF_CURRENT_CONNECTION.md#L222) supplies the complete source rates used in TR11, TR18, TR20 and TR23. These sealed files remain unchanged; this derivation is a new successor.

The earlier underlying proofs are public in the pinned source bank:

- [OB1–15](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/6cf5b3aa8ff395eba6b5512b28d117334da5767b/workbenches/splitzero-tandem/continuations/20260922-cutoff-profile/RETAINED_COMPLETE_PROOF_SOURCES.tex#L127618): complete terminal observation comparison.
- [OC50–74](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/6cf5b3aa8ff395eba6b5512b28d117334da5767b/workbenches/splitzero-tandem/continuations/20260922-cutoff-profile/RETAINED_COMPLETE_PROOF_SOURCES.tex#L127917): exact original large-period domain.
- [NCE10–21](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/6cf5b3aa8ff395eba6b5512b28d117334da5767b/workbenches/splitzero-tandem/continuations/20260922-cutoff-profile/RETAINED_COMPLETE_PROOF_SOURCES.tex#L109682): physical source phases, even spectral measure, strict scalar-current interval and response map.
- [FW7](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/6cf5b3aa8ff395eba6b5512b28d117334da5767b/workbenches/splitzero-tandem/continuations/20260922-cutoff-profile/RETAINED_COMPLETE_PROOF_SOURCES.tex#L120043): complete original source comparison through degree \(2q+2\).

The independent additions here are the complex hyperplane estimate TR10–12, its exact maximal-isotropic geometry TR12a, the canonical sign-eigenbasis calculation TR13–17, the doubled-rate coherence theorem TR18, and the exponentially small absolute trace correction TR20. The finite proof uses only the stated exact original operators and elementary inner-product algebra; no external theorem has been silently used. The inherited source-polynomial and Gamma identities retain the human citations in the complete CE/OCP proofs: T. H. Koornwinder, R. Wong, R. Koekoek, R. F. Swarttouw and W. P. Reinhardt (DLMF Chapter 18); R. A. Askey and R. Roy (DLMF Chapter 5); and the elliptic profile B. C. Carlson (DLMF Chapter 19).

What remains is the signed value of
\(2\epsilon\sqrt{\mathfrak d}\Im(\overline{c_g}c_h)\)
on the original terminal class and actual period-dependent projection. The proved complex constraint does not set it to zero. Its sign cannot be selected from the exponentially balanced weights, and no RH conclusion is made.
