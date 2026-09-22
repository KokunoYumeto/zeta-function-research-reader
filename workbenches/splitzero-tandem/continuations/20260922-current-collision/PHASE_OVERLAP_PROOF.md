# The exact joint region of original current and native source overlap

22 September 2026. Independent derivation PO1–PO20. The native source-step curvature contains the overlap with the same second boundary vector that also enters the marked current. Their phases therefore cannot be optimized independently. This proof gives their complete feasible region, sharp combined envelopes, every degenerate case, and the exact receiver into the actual adjacent source step. No phase or sign is assigned to the marked terminal class.

## 1. The original objects and the retained phase

At one literal original cutoff \(N\), retain the complete source metric \(G_N\), observation \(\Lambda\), minimum section \(L_N\), and isometry
\[
Q_N=(\Lambda G_N^{-1}\Lambda^*)^{-1},\qquad
L_N=G_N^{-1}\Lambda^*Q_N,\qquad J=L_NQ_N^{-1/2}.
\]
The original multiplication operator and boundary vectors obey
\[
M=C+\epsilon fe^\dagger,\quad C=C^\dagger,\quad
e^\dagger f=0,\quad\|e\|=\|f\|=1,\quad\epsilon>0.
\]
These are the exact [OCP5–7](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/OBSERVED_CURRENT_PLANE.tex#L90) source classes. All daggers before observation use \(G_N\).

Put
\[
u=J^\dagger e,\quad v=J^\dagger f,\quad
a=\|u\|^2,\quad d=\|v\|^2,\quad r=u^*v=x_r+ib,\quad
D=ad-|r|^2>0.
\]
\[
g=u/\sqrt a,\qquad
h=(v-(r/a)u)/\sqrt{D/a},\qquad
W=i\epsilon(vu^*-uv^*).
\tag{PO1}
\]
The strict positivity is the original complete two-column area certificate; it is not inferred from \(a>0\) alone. The vectors \(g,h\) are orthonormal in the actual observed metric coordinates. The current vanishes on their orthogonal complement and has matrix
\[
W|_{g,h}=
\begin{pmatrix}-2\epsilon b&-i\epsilon\sqrt D\\
i\epsilon\sqrt D&0\end{pmatrix}.
\tag{PO2}
\]

For the original observed terminal unit vector \(\widehat y\), or a probe being compared under the same finite constraints, write
\[
c_g=g^*\widehat y,\quad c_h=h^*\widehat y,\quad
\mu=|c_g|^2+|c_h|^2,\quad |c_g|\le\eta,\quad
0\le\mu\le1 .
\]
The actual terminal \(\eta=\eta_N\) is the bound in [OSP38–43](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/c9df443d9e1df000dfbb083943f97197e746eb08/workbenches/splitzero-tandem/branches/identity-absorber-square/OBSERVED_SUPPORT_PROPAGATION.md#L315), carried from TR10 without changing its domain. Define
\[
j=\widehat y^*W\widehat y
=2\epsilon\sqrt D\,\Im(\overline{c_g}c_h)-2\epsilon b|c_g|^2,
\qquad
\rho=\rho_f=\frac{|v^*\widehat y|^2}{d}.
\tag{PO3}
\]
Here \(\rho\) is the actual native second-source overlap. It is not a free parameter independent of \(j\).

## 2. An exact joint phase/overlap region

Use the orthonormal basis of the same current plane
\[
v_0=v/\sqrt d=\frac{r g+\sqrt D h}{\sqrt{ad}},\qquad
n_0=\frac{\sqrt D g-\bar r h}{\sqrt{ad}}.
\tag{PO4}
\]
Direct inner products prove orthogonality and unit norms, including every complex conjugation. Put
\[
A=v_0^*\widehat y,\quad B=n_0^*\widehat y,\quad
|A|^2=\rho,\quad |B|^2=\mu-\rho,\quad
\overline A B=X+iY.
\]
Multiplying PO2 by the two columns in PO4 gives
\[
W|_{v_0,n_0}=
\begin{pmatrix}-2\epsilon b&i\epsilon\sqrt D\\
-i\epsilon\sqrt D&0\end{pmatrix}.
\]
Consequently
\[
j=-2\epsilon b\rho-2\epsilon\sqrt D\,Y,\qquad
X^2+Y^2=\rho(\mu-\rho).
\tag{PO5}
\]
This is the exact shared phase, not only a Cauchy bound.

For any proposed real pair \((j,\rho)\), define
\[
Y(j,\rho)=-\frac{j+2\epsilon b\rho}{2\epsilon\sqrt D},\qquad
R(j,\rho)=\rho(\mu-\rho)-Y(j,\rho)^2,
\]
\[
Z_{\rm mid}(j,\rho)
=\frac{D\mu+(x_r^2-b^2-D)\rho-(b/\epsilon)j}{ad},
\]
\[
Z_{\min}(j,\rho)
=Z_{\rm mid}(j,\rho)-\frac{2\sqrt D\,|x_r|}{ad}\sqrt{R(j,\rho)}
\quad\hbox{when }R(j,\rho)\ge0.
\tag{PO6}
\]
Then the complete feasible region for the mass and coordinate constraints is
\[
\boxed{
0\le\rho\le\mu,\qquad
R(j,\rho)\ge0,\qquad Z_{\min}(j,\rho)\le\eta^2.
}
\tag{PO7}
\]
All three conditions are necessary and sufficient.

Here is the full reconstruction proof. Invert PO4 on its plane to obtain
\(c_g=(rA+\sqrt D B)/\sqrt{ad}\). Therefore
\[
|c_g|^2=
\frac{D\mu+(|r|^2-D)\rho+2\sqrt D(x_rX+bY)}{ad}
=Z_{\rm mid}+\frac{2\sqrt D x_r}{ad}X.
\]
PO5 requires \(X=\pm\sqrt R\); these two possibilities give exactly the two values
\(Z_{\rm mid}\pm2\sqrt D|x_r|\sqrt R/(ad)\).
If PO7 holds and \(\rho>0\), choose \(A=\sqrt\rho\) and
\(B=(X+iY)/\sqrt\rho\), using the sign of \(X\) which gives \(Z_{\min}\).
They have the required norms and current, and \(|c_g|^2=Z_{\min}\).
The reconstructed value automatically lies between zero and \(\mu\), since PO4 is unitary. Thus no additional lower bound for \(Z_{\min}\) has been silently dropped.

If \(\rho=0\), PO7 forces \(Y=j=0\) and \(R=0\); choose \(A=0\), \(B=\sqrt\mu\). If \(\rho=\mu\), take \(B=0\), \(A=\sqrt\mu\); the current is then \(j=-2\epsilon b\mu\). If \(\mu=0\), the only feasible pair is \((0,0)\). These choices prove sufficiency at every endpoint as well.

To obtain an observed unit vector when \(\mu<1\), add a vector of norm \(\sqrt{1-\mu}\) in the orthogonal complement of the current plane. This complement is nonzero in the actual programme: [OCS32's five-orbit rank bound](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/6cf5b3aa8ff395eba6b5512b28d117334da5767b/workbenches/splitzero-tandem/continuations/20260922-cutoff-profile/RETAINED_COMPLETE_PROOF_SOURCES.tex#L11073) gives \(\dim B\ge\lfloor q/5\rfloor+\mathbf1_{5\mid k}>2\). In a separate two-dimensional model unit vectors require \(\mu=1\); the phase formulas still hold for vectors of squared norm \(\mu\).

Two useful degenerate geometries follow without dividing by \(x_r\):
\[
x_r=0:\quad |c_g|^2=Z_{\rm mid}\quad
\hbox{for both allowed signs of }X;
\]
\[
r=0:\quad
\boxed{\max\{0,\mu-\eta^2\}\le\rho\le\mu,\qquad
j^2\le4\epsilon^2D\rho(\mu-\rho).}
\tag{PO8}
\]
For general \(r\), dropping only the coordinate cap gives the exact filled ellipse
\((j+2\epsilon b\rho)^2\le4\epsilon^2D\rho(\mu-\rho)\).
With the cap, PO7 retains the necessary extra restriction. It does not replace the actual region by an independently chosen interval for each variable.

## 3. Sharp current-plus-overlap envelopes

For any real coefficient \(\theta\), the same phase-dependent expression is
\[
j+\theta\rho=\widehat y^*(W+\theta P_v)\widehat y,\qquad
P_v=vv^*/d .
\]
In the original \(g,h\) frame write
\[
W+\theta P_v=
\begin{pmatrix}A_\theta&H_\theta\\\bar H_\theta&B_\theta\end{pmatrix},
\]
\[
A_\theta=-2\epsilon b+\frac{\theta|r|^2}{ad},\quad
B_\theta=\frac{\theta D}{ad},\quad
H_\theta=\sqrt D\left(\frac{\theta r}{ad}-i\epsilon\right),\quad
\delta_\theta=A_\theta-B_\theta.
\tag{PO9}
\]
All phases remain. Exact expansion gives
\[
\det(W+\theta P_v)=-\epsilon^2D,\qquad
\Gamma_\theta
=\sqrt{\delta_\theta^2+4|H_\theta|^2}
=\sqrt{(\theta-2\epsilon b)^2+4\epsilon^2D}>0.
\tag{PO10}
\]
Thus this entire auxiliary Hermitian pencil remains indefinite on the current plane, even though its restriction to a narrow coordinate cap can have one sign. The determinant cancellation follows because
\(A_\theta B_\theta\) and \(|H_\theta|^2\) have identical quadratic and mixed \(\theta\) terms.

For \(\sigma\in\{+1,-1\}\), define
\[
z_\sigma(\theta,\mu)
=\min\left\{\eta^2,\frac{\mu}{2}
\left(1+\frac{\sigma\delta_\theta}{\Gamma_\theta}\right)\right\},
\]
\[
\mathcal M_\sigma(\theta,\mu)
=\sigma B_\theta\mu+\sigma\delta_\theta z_\sigma
+2|H_\theta|\sqrt{z_\sigma(\mu-z_\sigma)}.
\tag{PO11}
\]
The minimum is nonnegative and at most \(\mu\). The exact sharp bounds are
\[
\boxed{
-\mathcal M_-(\theta,\mu)\le j+\theta\rho
\le\mathcal M_+(\theta,\mu).
}
\tag{PO12}
\]
The numbers \(\mathcal M_\sigma\) need not be positive under a severe coordinate cap; they are the actual extrema of \(\sigma(j+\theta\rho)\), with their signs retained.

To prove PO12 put \(z=|c_g|^2\), so \(0\le z\le\min(\eta^2,\mu)\).
For this fixed \(z\), the maximum of \(\sigma(j+\theta\rho)\) is exactly
\[
\sigma B_\theta\mu+\sigma\delta_\theta z
+2|H_\theta|\sqrt{z(\mu-z)}.
\tag{PO13}
\]
If \(H_\theta\ne0\), equality is achieved by
\[
c_g=\sqrt z,\qquad
c_h=\sigma\,\frac{\overline H_\theta}{|H_\theta|}
\sqrt{\mu-z}.
\]
For \(\mu>0\), PO13 is strictly concave on \(0<z<\mu\), and its derivative vanishes uniquely at
\(\mu(1+\sigma\delta_\theta/\Gamma_\theta)/2\).
Indeed the derivative is
\(\sigma\delta_\theta+|H_\theta|(\mu-2z)/\sqrt{z(\mu-z)}\);
substitution gives zero, with the sign fixed before squaring. Truncating this maximizer by the cap proves PO11.

If \(H_\theta=0\), PO13 is affine in \(z\). By PO10, \(\delta_\theta\ne0\); hence its maximum is at \(z=0\) or the cap endpoint according to the sign of \(\sigma\delta_\theta\), exactly as PO11 states. This degeneracy can occur only when \(x_r=0\), \(b\ne0\), and \(\theta=\epsilon ad/b\). If \(\mu=0\), every expression is zero. If the chosen \(z\) is zero or \(\mu\), the vanishing amplitude makes its relative phase immaterial. These cases cover every equality and degeneracy scope.

At \(\theta=0\), one has
\(\delta_0=-2\epsilon b\), \(|H_0|=\epsilon\sqrt D\),
\(\Gamma_0=2\epsilon\sqrt{b^2+D}\). PO11–12 therefore reduce exactly to [OSP48–50](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/c9df443d9e1df000dfbb083943f97197e746eb08/workbenches/splitzero-tandem/branches/identity-absorber-square/OBSERVED_SUPPORT_PROPAGATION.md#L402), preserving the signed rank-one correction. For \(\theta\ne0\), their common phase is optimized in PO13; adding independent optimal bounds for \(j\) and \(\rho\) generally cannot attain this value.

## 4. Complete measured-mass interval receiver

The original measured-support estimate supplies
\(m_-\le\mu\le m_+\), with
\[
m_-=\max\{0,(\mathfrak s-E^{\rm supp})/d\},\qquad
m_+=\min\{1,(\mathfrak s+E^{\rm supp})/d\}.
\tag{PO14}
\]
The proof and original errors are [OSP39–41](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/c9df443d9e1df000dfbb083943f97197e746eb08/workbenches/splitzero-tandem/branches/identity-absorber-square/OBSERVED_SUPPORT_PROPAGATION.md#L325). For a general \(\theta\), replacing \(\mu\) by \(m_+\) in PO12 is not always valid: the maximum can decrease with mass on a narrow coordinate cap.

There is nevertheless an exact finite calculation using at most three candidates. Put \(h_\theta=|H_\theta|\) and \(Z=\eta^2\). For each sign \(\sigma\), start with the two candidates
\(\mathcal M_\sigma(\theta,m_-)\) and
\(\mathcal M_\sigma(\theta,m_+)\).
When \(0<Z\le m_+\), put
\[
v_{\min}=\max\{0,m_--Z\},\qquad v_{\max}=m_+-Z.
\]
On the active cap \(z=Z\), define
\[
f_{\sigma,Z}(v)=\sigma A_\theta Z+\sigma B_\theta v
+2h_\theta\sqrt{Zv}.
\]
If \(\sigma B_\theta<0\) and \(h_\theta>0\), set
\[
v_*=\min\{v_{\max},\max\{v_{\min},
h_\theta^2Z/B_\theta^2\}\}.
\]
Otherwise take the endpoint of \([v_{\min},v_{\max}]\) maximizing this displayed scalar function. This latter case is monotone when \(h_\theta>0\) and affine when \(h_\theta=0\), so its endpoint evaluation is exact. Include \(f_{\sigma,Z}(v_*)\) as the third candidate. Let \(\mathcal U_\sigma(\theta)\) be the largest included candidate. Then
\[
\boxed{
\sup_{\substack{m_-\le\mu\le m_+\\|c_g|^2\le\eta^2}}
\sigma(j+\theta\rho)=\mathcal U_\sigma(\theta).
}
\tag{PO15}
\]
The supremum is over the precise mass/coordinate information; the remaining observed norm is supplied as in PO7.

Here is a proof that no interior optimizer is missed. After optimizing the phase, put \(z=|c_g|^2\), \(v=|c_h|^2\). The feasible set is
\(z,v\ge0\), \(z\le Z\), \(m_-\le z+v\le m_+\).
The objective is
\(\sigma A_\theta z+\sigma B_\theta v+2h_\theta\sqrt{zv}\).
At a differentiable interior stationary point its two partial derivatives would give
\(A_\theta B_\theta=h_\theta^2\), contradicting the strict negative determinant PO10. Thus a maximum lies on a boundary. The two mass boundaries give PO11. The boundary \(z=Z\) gives the scalar calculation above. At \(z=0\) or \(v=0\) the function is linear in the other coordinate, so an endpoint lies on one of those previously listed boundaries. If \(Z=0\), the two mass endpoints already suffice. If \(Z>m_+\), that cap cannot bind. If \(h_\theta=0\), the entire objective is affine and its vertices are among the same candidates. Compactness proves attainment.

This prevents an unsupported monotonicity step when the source trace correction has either sign.

## 5. Receiver into the actual adjacent-source current

Use the native adjacent step and notation of [NV1–26](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/d8c76a810f18a88fb91d6f2fc52b0b3dd385ea56/workbenches/splitzero-tandem/continuations/20260922-real-words-source-steps/NATIVE_SOURCE_STEP_PROOF.md#L5), keeping the two literal paths \(q-1\to q\) and \(2q-1\to2q\). Let \(Y_0=\xi^*Q_N\xi>0\),
\(\beta_{\rm src}=z_1^*Q_Nz_1/\omega_{N+1}\),
and \(\Delta\tau=\tau_{N+1}-\tau_N\).
The same source vector satisfies
\(w=\beta_{\rm src}Y_0\rho\), with precisely the overlap in PO3.
For \(0\le t\le1\), put
\[
\lambda=\frac{(1+\beta_{\rm src})t}{1+\beta_{\rm src}t},\qquad
\theta_\lambda=
\lambda\,\frac{\beta_{\rm src}}{1+\beta_{\rm src}}\Delta\tau .
\tag{PO16}
\]
The exact source-step formula [NV8–9](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/d8c76a810f18a88fb91d6f2fc52b0b3dd385ea56/workbenches/splitzero-tandem/continuations/20260922-real-words-source-steps/NATIVE_SOURCE_STEP_PROOF.md#L84) now groups the correlated quantities:
\[
\boxed{
\frac{\Phi(t)}{Y_0}
=(1-\lambda)[j+\theta_\lambda\rho]
+\lambda\,\frac{\Phi_1}{Y_0}.
}
\tag{PO17}
\]
Here \(j=\Phi_0/Y_0\) is the endpoint current of the same normalized observed vector. The trace difference and source parameter are the actual ones, not chosen to force a sign. Substituting PO12 yields
\[
\boxed{
\lambda\frac{\Phi_1}{Y_0}-(1-\lambda)\mathcal M_-(\theta_\lambda,\mu)
\le\frac{\Phi(t)}{Y_0}
\le
\lambda\frac{\Phi_1}{Y_0}+(1-\lambda)\mathcal M_+(\theta_\lambda,\mu).
}
\tag{PO18}
\]
If only PO14's mass interval is available, replace \(\mathcal M_\sigma\) by \(\mathcal U_\sigma\) from PO15. At \(\lambda=1\), the prefactor is zero and the exact endpoint \(\Phi_1\) remains; no limiting division by \(1-\lambda\) is used. At \(\lambda=0\), the original OSP bound is recovered. These envelopes are sharp for the base mass/coordinate-constrained expression \(j+\theta\rho\). Requiring a specified second-endpoint value can impose further correlations, so no independent attainability of all full-path endpoint data is claimed.

The exact doubled-rate mass receiver also remains useful:
\[
0\le\mu-\rho
=\frac{|\sqrt D\,c_g-r c_h|^2}{ad}
\le\frac{(\sqrt D\,\eta+|r|)^2}{ad}=:E_f.
\]
Consequently
\[
\boxed{|(j+\theta\rho)-(j+\theta\mu)|\le|\theta|E_f.}
\tag{PO19}
\]
For the actual terminal class, [NV16–19](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/d8c76a810f18a88fb91d6f2fc52b0b3dd385ea56/workbenches/splitzero-tandem/continuations/20260922-real-words-source-steps/NATIVE_SOURCE_STEP_PROOF.md#L191) gives
\(E_f\le e^{-2q\psi(s_N)+O_{h,\varpi}(k\log q)}\).
On either native adjacent path,
\(|\Delta\tau|\le2\epsilon_N\sqrt{\alpha_N}
+2\epsilon_{N+1}\sqrt{\alpha_{N+1}}=e^{O(k\log q)}\),
so PO19 with \(\theta_\lambda\) has the doubled rate uniformly over the whole source step. This is an absolute error bound; it makes no division by \(\mu\) or by a signed current.

Every statement is applied separately at all four original cutoffs. If \(F_N=j_N+\theta_N\rho_N\) and PO12 gives
\(-M_{-,N}\le F_N\le M_{+,N}\), the signed return with the original \(+,+,-,-\) signs lies within the following explicit interval
\[
\boxed{
-\sum_{N\in\{q-1,q\}}M_{-,N}
-\sum_{N\in\{2q-1,2q\}}M_{+,N}
\ \le\ \mathcal R F_N\ \le\
\sum_{N\in\{q-1,q\}}M_{+,N}
+\sum_{N\in\{2q-1,2q\}}M_{-,N}.
}
\tag{PO20}
\]
The triangle/interval addition uses the four actual values; it does not identify their phases.

## 6. Source and verification scope

OSP38–51 was read in full in the published node source linked above. Its exact current correction and fixed-mass optimizer are recovered at \(\theta=0\). The new results here are the exact joint feasible region PO7, the determinant-preserving combined pencil and capped envelopes PO9–13, the complete mass-interval calculation PO15, and the common-phase native receiver PO17–19.

The exact finite checks verify all unitary coordinate changes, complex signs, determinant cancellation, stationary points, degenerate off-diagonal cases, the two possible joint-region reconstructions, and source-step regrouping. Equality examples are probes with the stated source geometry and mass constraints, not evaluations of an actual zeta zero or assertions that the original terminal probe realizes an extremum. The source’s human Gamma and elliptic citations remain those in the cited OCP/RC/OSP derivations; all additional finite phase geometry and optimization claims are proved in full here.
