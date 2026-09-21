# Original-metric heat transitions and complete mixed-family control

Complete additive derivations, 20 September 2026.

The incoming proof and summary are preserved unchanged in `inputs/`. The original spectral source is pinned at `ff251e3adc5fd78049170b8fc94c26f882df3d14`; the subsequently read derivative repair is pinned at `52274804051e325c8a6ef69c17b3958cc2caba0a`. Source-specific coverage and mathematical dependencies are in `state/SOURCE_PROVENANCE.json`. The EIQ profile remains an imported written-proof input; the finite identities are proved below.


---

# 1. The original exponential-time heat transition and the cost of weak source activation

20 September 2026. Additive continuation. All logarithms are natural.

## 1.1 Source basis and domains

The two newly supplied files are preserved unchanged under `inputs/`. The mathematical input used here is their one-factor coercivity P1–P11, joint minimum J1–J8, spectral comparison S1–S5, and, on the simple-quartet domain, V1–V6 and V13. The EIQ monic-profile theorem in V1 is an imported written source theorem; the present note does not independently prove that asymptotic. The relevant GitHub source was read at commit `ff251e3adc5fd78049170b8fc94c26f882df3d14`, file `workbenches/splitzero-tandem/continuations/20260920-original-spectral-determinant/ORIGINAL_SPECTRAL_DETERMINANT.tex`, blob `11a2154819682c01c878ffb0b886f7b704fed888`. Its SD1–SD12 specify the original companion, the selfadjoint source compression, the rank-one correction, and its singular-value bounds. SD26–SD28 keep the original metric dependence. We use those original definitions; finite identities needed below are also proved here.

The evaluated heat threshold is on the programme's stated simple quartet: fixed h, fixed delta in (0,1/2), gamma>2, k=1 mod 4, and q=(k+1)^2. This is not a claim to have exhibited an off-critical xi zero. The general covariance identities in the later parts require neither a quartet nor equal multiplicities.

Let chi be the whole original sum polynomial and let M be multiplication by y in E=C[y]/chi_y, with y=(S-k/2)/i and chi_y(y)=i^(-q)chi(k/2+iy). Let G_N be the original attained metric from the actual convolution m_k=w_h^{*k}. Write C_N for its selfadjoint physical y-compression. Then
\[
 M=C_N+R_N,\quad R_N=r_N\ell_N,\quad R_N^2=0,\quad
 C_N^{\dagger_{G_N}}=C_N,\quad \epsilon_N=\|R_N\|_{G_N}>0.
 \tag{H1}
\]
The sign is the SD2 convention. It agrees with an earlier M=A-Q convention by R=-Q; the positive scalar epsilon is unchanged.

Put r=N+1-q and s_N=r/q. We use q-1<=N<=2q, including the fourth original determinant endpoint. The finite multiplication estimate applies at degree 2q as well as at 2q-1, so one fixed constant B_h gives
\[
 \|C_N\|_{G_N}\le B_hq.
 \tag{H2}
\]
When a source moment above degree 2q is used, the supplied all-degree coercivity is applied through degree 2q+2. This retains the degree-raising column; it does not silently use a truncated multiplication form.

## 1.2 The entire allowance profile follows from the retained monic minima

Let omega_n be the squared norm of the original real monic source polynomial p_n. Let nu_j be the squared monic norm for the complete relation measure chi_y^2 m_k. Define
\[
 d_n=\omega_n/\nu_{n-q},\qquad b_{n+1}=\omega_{n+1}/\omega_n.
\]
Direct projection onto the last monic relation proves
\[
 \epsilon_{q-1}^2=b_q(1-d_q)/d_q,
\]
\[
 \epsilon_N^2=b_{N+1}(1-d_N)(1-d_{N+1})/d_{N+1}\quad(N\ge q).
 \tag{H3}
\]
Here is the full norm calculation. At cutoff N, the minimum representative of [p_(N+1)] is the difference between the monic relation of degree N+1 and p_(N+1), up to sign. Its squared norm is nu_r-omega_(N+1). The leading-coefficient functional on the minimum source has squared dual norm (1-d_N)/omega_N for N>=q, and 1/omega_(q-1) at the first cutoff. Indeed [p_N] has squared quotient norm omega_N-omega_N^2/nu_(N-q), and the leading functional is its inner product divided by omega_N. Multiplying these two norm factors gives H3. Every preceding relation is present in these orthogonal projections.

The supplied V4 gives, through r=q+1,
\[
 \log(\nu_r/\omega_{q+r})=2q\psi(r/q)+O_h(k\log^2(q+2)).
 \tag{H4}
\]
The same full-source comparisons applied to two consecutive monic affine fibres give log b_(N+1)=O_h(k log^2(q+2)). The source profile is continuous and decreasing on the required interval, with psi(1)>0. Consequently d_n is uniformly exponentially small in q on this window; both logarithms log(1-d_n) in H3 are retained and tend to zero. We obtain
\[
 \boxed{\log\epsilon_N^2=2q\psi(s_N)+O_h(k\log^2(q+2)).}
 \tag{H5}
\]
This is uniform in N. It is an asymptotic with the original profile theorem's eventual domain, not an effective numerical threshold in k.

## 1.3 An exact elliptic expression for the two heat thresholds

Denote the complete elliptic integrals by K(u), E(u), with modulus u in (0,1), and put u'=sqrt(1-u^2). The supplied equilibrium endpoint equations and profile derivative are
\[
 1+s=E(u)/(u'K(u)),\qquad \psi'(s)=\log(u/E(u)),\qquad \psi(0)=\log(4/\pi).
 \tag{H6}
\]
The parameter map in H6 is invertible: its derivative is
\[
 \frac{(K-E)(E-u'^2K)}{u\,u'^3K^2}>0.
\]
Both factors in the numerator are positive by the defining elliptic integrals. Its range is (0,infinity) after subtracting one. The two derivative formulas E'=(E-K)/u and K'=E/(u u'^2)-K/u follow by differentiation of their defining integrals.

Integration by parts in H6 gives the complete closed expression
\[
 \boxed{\psi(s)=s\log\frac{u_s}{E(u_s)}+
                   \log\frac{1+u_s'}{E(u_s)},\quad
       1+s=\frac{E(u_s)}{u_s'K(u_s)}.}
 \tag{H7}
\]
For a direct verification, differentiate the right side: the coefficient of du/ds is
((1+s)K/E-1)/u-u/(u'(1+u'))=0. Its limit at zero is log(4/pi). Thus this is the same profile, through its exact inverse parameter map.

Let a_0=psi(0), a_1=psi(1). Then
\[
 a_0=\log(4/\pi),\qquad
 a_1=\log\frac{u_1(1+u_1')}{E(u_1)^2},\qquad
 E(u_1)=2u_1'K(u_1).
 \tag{H8}
\]
The exact rational enclosure in `checks/heat_checks.py` proves
\[
 \boxed{0<a_1<1/8<a_0.}\tag{H9}
\]
For completeness, the enclosure uses u_1 in (987/1000,988/1000). Write z=u^2 and c_n=(binom(2n,n)/4^n)^2. The series
K=(pi/2)sum c_n z^n and E=(pi/2)(1-sum_(n>=1)c_n z^n/(2n-1)) have omitted positive tails bounded by c_(J+1)z^(J+1)/(1-z) and this quantity/(2J+1). At J=512 the rational squared inequalities E_series^2 versus 4(1-z)K_series^2 prove the root bracket. Using 333/106<pi<355/113 and 154/1000<u_1'<161/1000 then proves
1<u_1(1+u_1')/E(u_1)^2<9/8.
Finally log(9/8)<1/8 and exp(1/8)<=8/7<4/(355/113). The checker separately derives the stated loose pi bounds from Machin's alternating arctangent series.

Non-interval high-precision evaluations, not native moment evaluations, are
\[
 u_1\simeq0.9871005293061829185,\quad
 a_1\simeq0.06651895202027391967,\quad
 a_0\simeq0.24156447527049044469.
\]

## 1.4 The exact finite heat sandwich retains the large singular value and the whole root trace

Let the singular values of M in G_N be s_1>=...>=s_q. The two triangle inequalities and restriction to ker ell_N give
\[
 |s_1-\epsilon_N|\le B_hq,\qquad s_j\le B_hq\quad(j\ge2).
 \tag{H10}
\]
Set R_k=k sqrt(delta^2+gamma^2). For every tau>=0 the full holomorphic trace, with the entire primary structure, is
\[
 Z_{hol,N}(\tau)=\operatorname{Tr}e^{-\tau M^2}
 =\sum_{a,b=0}^k e^{-\tau[(2b-k)\gamma-i(2a-k)\delta]^2}.
 \tag{H11}
\]
For repeated-primary analogues each term receives its actual multiplicity. This trace identity follows from upper triangular primary blocks; it does not delete the operator's nilpotent terms.

Define the original heat gap
\[
 D_N(\tau)=\Re Z_{hol,N}(\tau)-\operatorname{Tr}e^{-\tau M^{\dagger_{G_N}}M}.
\]
Put h_k(tau)=q tau R_k^2 exp(tau R_k^2). H10 and |exp(z)-1|<=|z|exp(|z|) prove the unconditional finite interval
\[
 \boxed{\begin{aligned}
 1-e^{-\tau(\epsilon_N-B_hq)_+^2}-h_k(\tau)
 &\le D_N(\tau)\\
 &\le1-e^{-\tau(\epsilon_N+B_hq)^2}
       +h_k(\tau)+(q-1)\tau B_h^2q^2.
 \end{aligned}}\tag{H12}
\]
Thus no limiting argument about small singular values is used to drop a logarithmic tail. All q-1 bounded singular directions and the full arithmetic-root trace have displayed errors.

For sigma>0 take tau_k(sigma)=exp(-2 sigma q). Combining H5 and H12 yields
\[
 \boxed{D_N(\tau_k(\sigma))\longrightarrow
        1_{\{\psi(s)>\sigma\}}}\quad\text{as }s_N\to s,
        \quad\psi(s)\ne\sigma.\tag{H13}
\]
The convergence is uniform on closed regions with positive sigma and |psi(s_N)-sigma| bounded below. Its unresolved layer has width O_h(k log^2(q)/q) in sigma. H12, with the actual epsilon_N, remains the finite statement inside that layer. A value at the threshold is not assigned.

At the FOUR ORIGINAL cutoffs (q-1,q,2q-1,2q), with signs (+,+,-,-), this gives
\[
 \boxed{\mathcal R D_N(e^{-2\sigma q})\longrightarrow
 2\,1_{\{a_1<\sigma<a_0\}}\quad(\sigma>0,\ \sigma\notin\{a_0,a_1\}).}
 \tag{H14}
\]
In particular the fully specified heat scale satisfies
\[
 \boxed{\mathcal R D_N(e^{-q/4})\longrightarrow2.}\tag{H15}
\]
This is a trace in the original full canonical arithmetic module. It has not been assigned to its observation quotient or to a full-Weil quadratic form.

With the original action weights w_(q-1)=w_(2q-1)=1 and w_N=2 in between,
\[
 \frac1{2q}\sum_Nw_N D_N(e^{-2\sigma q})\longrightarrow
 I(\sigma):=|\{s\in[0,1]:\psi(s)>\sigma\}|.
 \tag{H16}
\]
H12 bounds this family by 1+o(1) for fixed sigma>0, uniformly in N, and the shrinking transition set has vanishing measure; this proves H16. For sigma=1/8 the inverse in H7 gives I(1/8) approximately 0.3299435897584082 (non-interval diagnostic).
The original coefficient satisfies the exact limiting-profile identity C_B=4 int_0^infty I(sigma)d sigma. This is Fubini on the positive function psi, not an interchange of an uncontrolled finite heat integral at sigma=0. More explicitly the outlier proxy 1-exp(-epsilon_N^2 exp(-2q sigma)) has integral
(log epsilon_N^2+EulerGamma+E_1(epsilon_N^2))/(2q), where E_1(z)=int_z^infty exp(-u)du/u. This keeps its full tail. H12 records separately what differs between that proxy and the complete arithmetic heat gap.

## 1.5 Introduce the source stiffness by an exact source isometry

Retain the actual scalar source X_N, the supplied tensor section Y, and their orthogonal normal map Z=(I-P_X)R. In the notation of the input,
\[
 H_Z=Z^*Z,\quad F_Z=\operatorname{value}(Z),\quad
 \Omega_N=F_ZH_Z^+F_Z^*,\quad
 G_N^J=(G_N^{-1}+\Omega_N)^{-1}.
\]
For alpha>0 give X_N plus im Z the specified norm ||x||^2+alpha^(-1)||z||^2. The map (x,z)->(x,z/sqrt(alpha)) is an isometry onto the ordinary orthogonal sum; its value map becomes J_X x+sqrt(alpha)J_Z z'. Therefore the attained metric is exactly
\[
 \boxed{G_N(\alpha)=(G_N^{-1}+\alpha\Omega_N)^{-1}.}\tag{H17}
\]
At alpha=1 this is the actual physical joint minimum. At alpha=0 the normal source is absent and the metric is G_N. At intermediate alpha the penalty is displayed, not represented as the unchanged physical norm.

Let K_N=G_N^(1/2)Omega_N G_N^(1/2), and let lambda_j>=1 be the eigenvalues of I+K_N. The pasted proof supplies
\[
 |\log\lambda_j-2(j-1)\ell_k|\le E_{h,k},\quad
 \ell_k=\log(q/k),\quad E_{h,k}=O_h(q),
 \tag{H18}
\]
including finite bounds for E and every zero correction direction.

For a fixed theta>=0 choose alpha_k=exp(-2 theta q). Put a=2 theta q and Delta_N(alpha)=log det G_N-log det G_N(alpha). The complete identity is
\[
 \Delta_N(1)-\Delta_N(e^{-a})=qa-\sum_j\log[1+(e^a-1)/\lambda_j].
 \tag{H19}
\]
Let J_0=min(q,ceil((a+E_(h,k))/(2 ell_k))). Since every lambda_j>=1, the first J_0 summands on the right are at most a. The remaining ones are bounded by a geometric series using H18. Thus, for a>0,
\[
 \boxed{0\le\Delta_N(e^{-a})-\Delta_N(1)+qa
 \le aJ_0+(1-e^{-2\ell_k})^{-1}.}\tag{H20}
\]
For a=0 the left expression is identically zero. In particular, uniformly at the original cutoffs,
\[
 \boxed{\Delta_N(e^{-2\theta q})
 =\Delta_N(1)-2\theta q^2+O_{h,\theta}(q^2/\ell_k).}\tag{H21}
\]
Using the input's V13, with its original EIQ and rectangle conventions,
\[
 \boxed{\begin{aligned}
 \Delta_N(e^{-2\theta q})
 =q^2[\ell_k-\tfrac32-E_\square-2\mathfrak F(s_N)-2\theta]
 +O_{h,\theta}(q^2/\ell_k+kq\log^2(q+2)).
 \end{aligned}}\tag{H22}
\]
Both errors are o(q^2) on the simple-quartet family. The extra term -2 theta q^2 cancels under the SAME four endpoint signs, so
\[
 \boxed{\mathcal R\Delta_N(e^{-2\theta q})=C_Bq^2+o_h(q^2).}\tag{H23}
\]
This calculation also applies to the original observation quotient on the five-orbit codimension m=8k-16 domain: compression interlacing bounds the difference from the full determinant by at most m log lambda_q=O_h(kq log(q/k))=o(q^2). The observation, its kernel, and its period have not been changed.

## 1.6 Weak activation collapses the heat gap in a proved two-scale region

For 0<alpha<=1, simultaneous diagonalization of I+alpha K and I+K gives
\[
 G_N^J\preceq G_N(\alpha)\preceq\alpha^{-1}G_N^J.
 \tag{H24}
\]
The exact input J3 gives ||M||_(G_N^J)<=C_h k exp(W_k/2), W_k=O_h(k log^2 q)=o(q). Hence
\[
 \|M\|_{G_N(e^{-2\theta q})}^2
 \le C_h^2k^2\exp(2\theta q+W_k).
\]
On the explicit parameter region 0<=theta<sigma,
\[
 \boxed{D_N^{(\alpha_k)}(e^{-2\sigma q})\longrightarrow0}\tag{H25}
\]
uniformly in N. Indeed both exponentials differ from identity in absolute trace by at most q tau ||M||^2 exp(tau||M||^2), which tends to zero. For the original observation, its minimum lift is an isometry and its quotient map a contraction, so the same statement holds for its OWN centered minimum-section compression. This retains the changing action through its exact minimum section; it does not assert that the observed action is fixed.

A fully specified pair of scales is
\[
 \boxed{\alpha_k=e^{-q/8},\qquad\tau_k=e^{-q/4}.}\tag{H26}
\]
Here theta=1/16 and sigma=1/8. The canonical signed full heat gap tends to 2 by H15; the penalized-joint signed gap tends to zero by H25; and the exact source change costs
\[
 \Delta_N(\alpha_k)=q^2[\ell_k-\tfrac32-E_\square-2\mathfrak F(s_N)-\tfrac18]+o(q^2),
\]
with four-endpoint return still C_B q^2+o(q^2). Thus the changed heat behavior is accompanied by its evaluated, non-negligible full metric correction.

## Scope

The heat plateau and weak-activation coefficient are new deductions from the stated inputs. The arbitrary-source covariance and phase formulas in the following parts are finite and do not use EIQ. The individual original observed-current sign, its period-dependent angle, and the separate PRD proper-source minimum are not evaluated by H15 or H25. Their exact moving-section matrices, with both leakage blocks retained, are the next part's objects.


---

# 2. Exact curvature, section motion, and principal angles for the complete mixed minimum

## 2.1 Return from the original maps to one explicit orthonormal block frame

Fix any of the actual finite source data: positive G, positive semidefinite Omega=F_Z H_Z^+ F_Z^*, an onto original observation Lambda:E->B, and its actual kernel inclusion I:K->E. No invariance of K under the arithmetic action is imposed. Write q=dim E, m=dim K, r=q-m, and
\[
 H=I^*GI,\quad Q=(\Lambda G^{-1}\Lambda^*)^{-1},\quad
 L=G^{-1}\Lambda^*Q.
\]
The exact coordinate map and inverse are
\[
 F=[I H^{-1/2},\ L Q^{-1/2}],\qquad F^{-1}=F^*G.
 \tag{M1}
\]
Thus F^*GF=I_q and Q^(1/2)Lambda F=[0,I_r]. Put
\[
 K_0=F^{-1}\Omega(F^{-1})^*
 =\begin{pmatrix}U&V\\V^*&W\end{pmatrix}\succeq0.
 \tag{M2}
\]
The covariance and metric of H17 become I+tK_0 and (I+tK_0)^(-1). This is a proof of the coordinate identification, including its inverse and both original metrics.

Define, for all t>=0,
\[
 D_t=I_r+tW,\quad Q_t=D_t^{-1},\quad
 X_t=tV D_t^{-1},
\]
\[
 E_t=I_m+tU-t^2V D_t^{-1}V^*,\quad H_t=E_t^{-1}.
 \tag{M3}
\]
Block inversion gives all original subquotient maps in these coordinates:
\[
 \boxed{L_t=\binom{X_t}{I_r},\quad
 P_t=\begin{pmatrix}I_m&-X_t\\0&0\end{pmatrix},\quad
 T_t^*G_tT_t=\operatorname{diag}(H_t,Q_t),\quad
 T_t=\begin{pmatrix}I_m&X_t\\0&I_r\end{pmatrix}.}\tag{M4}
\]
The original minimum section is F L_t Q^(1/2); the original kernel metric is H^(1/2) H_t H^(1/2); the original observed metric is Q^(1/2)Q_tQ^(1/2). These formulas are used only on the indicated actual value spaces.

## 2.2 The mixed curvature is a sum of two complete positive Grams

Differentiate the finite matrices in M3:
\[
 X_t'=V D_t^{-2},\qquad
 E_t''=-2X_t'D_t(X_t')^*.
 \tag{M5}
\]
Positive semidefiniteness of K_0 gives ker W subset ker V and U-VW^+V^*>=0. Hence
\[
 E_t=I_m+t(U-VW^+V^*)+tVW^+(I+tW)^{-1}V^*,
\]
\[
 E_t'=U-VW^+V^*+VW^+(I+tW)^{-2}V^*\succeq0.
 \tag{M6}
\]
The pseudoinverse here is the inverse on W's positive range. It was not applied to a missing value direction.

Let
\[
 f_K(t)=\log\det E_t,
\quad \mathcal E(t)=\operatorname{Tr}[H_t X_t'D_t(X_t')^*].
\]
The latter is exactly the Hilbert--Schmidt squared norm of L_t' as a map from (B,Q_t) to the original kernel (K,H_t). The derivative has range in the kernel, since the bottom block of L_t is constant. Matrix differentiation now proves
\[
 \boxed{-f_K''(t)
 =\operatorname{Tr}[(E_t^{-1/2}E_t'E_t^{-1/2})^2]
   +2\mathcal E(t).}\tag{M7}
\]
This is an equality, not the omission of a mixed derivative from a positive estimate. In original coordinates f_K is exactly
log det(I^*G I)-log det(I^*G(t)I).

Integrating by parts, using f_K(0)=0, gives the finite energy identity
\[
 \boxed{\begin{aligned}
 2\int_0^T t\mathcal E(t)dt
 +\int_0^T t\operatorname{Tr}[(E_t^{-1/2}E_t'E_t^{-1/2})^2]dt
 =f_K(T)-T f_K'(T).
 \end{aligned}}\tag{M8}
\]
In particular
\[
 2\int_0^T t\mathcal E(t)dt\le f_K(T).
 \tag{M9}
\]
Both sides keep the original norm of the section derivative. Very small normal Grams have not been inverted independently of their value maps.

Concavity of E_t and E_0=I imply E_t-tE_t'>=I. Therefore
\[
 \boxed{0\le t f_K'(t)\le m.}\tag{M10}
\]
Equivalently this follows from the exact derivative of
f_K=log det(I+tK_0)-log det(I+tW), by compression interlacing. It bounds the entire kernel response by its actual dimension for every t, not just at the endpoint.

Using the input's full logarithmic spectrum and original m=8k-16 observation,
\[
 f_K(1)\le m[2(q-1)\log(q/k)+E_{h,k}].
\]
Consequently
\[
 \boxed{\int_0^1t\mathcal E(t)dt
 \le m(q-1)\log(q/k)+\tfrac m2E_{h,k}
 =O_h(kq\log(q/k)).}\tag{M11}
\]
This is control of the whole moving minimum section. Its right side is smaller than the q^2 log(q/k) full comparison scale by a factor O(k/q). It does not say every individual current component is small or has a chosen sign.

## 2.3 Simultaneous positive covariance directions

Orthogonalize the entire actual normal source first, retaining its full Gram and value map. Penalizing separately chosen orthogonal normal groups gives covariance
C(t)=I+sum_i t_i K_i, K_i>=0, t_i>=0.
This defines the allowed multi-parameter family by an exact source map. It is not a declaration that several unorthogonalized sources have zero cross Gram.

Write C in blocks A(t),B(t),D(t), and set X=BD^(-1), E=A-BD^(-1)B^*. Denote block derivatives of K_i by U_i,V_i,W_i. Then
\[
 X_i=(V_i-XW_i)D^{-1},\qquad
 E_i=[I,-X]K_i[I,-X]^*\succeq0,
\]
\[
 E_{ij}=-X_iDX_j^*-X_jDX_i^*.
\]
Thus
\[
 \boxed{-\partial_i\partial_j\log\det E
 =\operatorname{Tr}(E^{-1}E_iE^{-1}E_j)
 +2\Re\operatorname{Tr}(E^{-1}X_iDX_j^*).}\tag{M12}
\]
As a real symmetric matrix in i,j, the right side is the sum of two positive Gram matrices. The first is the Gram of the Hermitian matrices E^(-1/2)E_iE^(-1/2); the second is twice the real Hilbert--Schmidt Gram of E^(-1/2)X_iD^(1/2). This proves joint concavity and controls every mixed direction, with its actual complex cross terms. Restriction to an affine ray gives M8.

## 2.4 The exact principal angles keep the covariance cross block

Compare the original observation subspace im L_0 with im L_t, both measured in G_t. Since L_0=L_t-(X_t,0)^T, its Gram is
Q_t+X_t^*H_tX_t, and its pairing with L_t is Q_t. Therefore the nontrivial squared cosines are the eigenvalues of
\[
 [I_r+Q_t^{-1/2}X_t^*H_tX_tQ_t^{-1/2}]^{-1}.
 \tag{M13}
\]
There are at most m nontrivial angles. In terms of the covariance cross correlation
\[
 Z_t=(I+tU)^{-1/2}tV(I+tW)^{-1/2},
\]
these cosines are 1-s_j(Z_t)^2, with the remaining cosines equal to one. This follows by substituting E=(I+tU)^(1/2)(I-Z_tZ_t^*)(I+tU)^(1/2); the eigenvalue relation is rho^2/(1-rho^2) for the squared tangents. Thus
\[
 \boxed{-\sum_j\log\cos^2\theta_j(t)
 =\log\det(I+tU)-\log\det E_t.}\tag{M14}
\]
The principal-angle cost is not f_K itself; M14 records their exact relation. In particular metric drift can change angles even after the section X_t has nearly stabilized.

For the actual fixed class x=(u,b), the full finite identity is
\[
 \boxed{x^*G_tx=(u-X_tb)^*H_t(u-X_tb)+b^*Q_tb.}\tag{M15}
\]
The observed fraction is the second term divided by the whole expression. All phases in u-X_tb remain. The source's previously unresolved canonical angle is not assigned a value from a determinant.

## 2.5 Every action block and its return

Let the original arithmetic operator in M1 coordinates be
A= [[a,b_0],[c,d]]. Its full matrix in the moving minimum-section frame is
\[
 \boxed{T_t^{-1}AT_t=
 \begin{pmatrix}
 a-X_tc & b_0+aX_t-X_td-X_tcX_t\\
 c & d+cX_t
 \end{pmatrix}.}\tag{M16}
\]
Here c is exactly the original kernel leakage, with the coordinate transports in M1. The observed action changes by cX_t; the reverse block is quadratic in X_t and cannot be dropped. Differentiation gives [T_t^(-1)AT_t, [[0,X_t'],[0,0]]], so the full action remains conjugate to the original one.

The intrinsic Hilbert--Schmidt action speed obeys
\[
 \|(d+cX_t)'\|_{HS,Q_t}^2
 \le\|c\|_{H_t\to Q_t}^2\mathcal E(t).
 \tag{M17}
\]
This controls the action response by the actual leakage and M8, not by an assumed invariance of the kernel. The leakage factor has not been set to one or assigned a native asymptotic by this inequality.

For any z off the relevant finite spectra, the exact observed characteristic determinant is
\[
 \det(zI-d-cX_t)
 =\det(zI-d)\det[I_m-X_t(zI-d)^{-1}c].
 \tag{M18}
\]
After multiplication by the original denominators this is a polynomial identity valid across removable factors. It has a small m-dimensional correction, but it does not assert that only m eigenvalues move.

## 2.6 A fully evaluated mixing example

Take K_0=[[9,3],[3,1]], m=r=1. Then
\[
 Q_t=(1+t)^{-1},\quad X_t=3t/(1+t),\quad
 E_t=(1+10t)/(1+t),\quad
 \mathcal E(t)=9/[(1+10t)(1+t)^2].
\]
Equation M8 becomes the exact integral identity with right side
log((1+10T)/(1+T))-9T/[(1+10T)(1+T)]. This is nonnegative and includes both positive integrals. This declared matrix example is not a native period calculation.


---

# 3. A positive-coefficient polynomial for the complete original spectral determinant

The older general-family proof Q2 gives a Cauchy--Binet polynomial for a restricted Gram. This part applies that identity to BOTH sides of the unchanged arithmetic operator in the actual covariance path. The result is a full regularized spectral determinant, rather than a replacement Gram determinant. The connecting maps are explicit below.

## 3.1 Full original metric and arithmetic matrix

Keep the original fixed endomorphism M and the actual source path
G(t)=(G_0^(-1)+t Omega)^(-1), t>=0. Set K=G_0^(1/2)Omega G_0^(1/2), and choose a unitary U with U^*KU=diag(kappa_1,...,kappa_q), kappa_i>=0. Define
\[
 M_0=U^*G_0^{1/2}M G_0^{-1/2}U,\quad
 c_i(t)=1+t\kappa_i,\quad D(t)=\prod_i c_i(t).
 \tag{P1}
\]
The exact isometry from the ORIGINAL metric G(t) to the standard metric is
\[
 S_t=\operatorname{diag}(c_i^{-1/2})U^*G_0^{1/2},\qquad
 S_t^{-1}=G_0^{-1/2}U\operatorname{diag}(c_i^{1/2}).
\]
Consequently the original M becomes
T_t=diag(c_i^(-1/2))M_0 diag(c_i^(1/2)). Its adjoint and every singular value are transported by this isometry. This proof does not replace the arithmetic spectrum by the spectrum of K.

For a>0 define the full positive spectral determinant
F(a,t)=log det(aI+M^(dagger_G(t))M).
Then
\[
 \boxed{\det(aI+M^{\dagger_{G(t)}}M)=P(a,t)/D(t),}\tag{P2}
\]
where
\[
 \boxed{\begin{aligned}
 P(a,t)=\sum_{s=0}^q a^{q-s}
 \sum_{|I|=|J|=s}
 |\det(M_0)_{I,J}|^2
 \prod_{i\notin I}c_i(t)\prod_{j\in J}c_j(t).
 \end{aligned}}\tag{P3}
\]
The empty minor equals one. Every matrix minor in P3 contains its full complex cross terms before its absolute square is taken.

Proof: det(aI+T^*T)=sum_s a^(q-s)Tr wedge^s(T^*T). In coordinate exterior bases the trace is the sum of the squared absolute values of every s-by-s minor of T. Its row and column diagonal factors give
|det T_IJ|^2=|det M_0,IJ|^2(prod_J c_j)/(prod_I c_i).
Multiplication by D(t) proves P3. Each term contains exactly q factors c_i, counting repetitions, because |I|=|J|. Therefore
\[
 \boxed{P(a,t)=\sum_{j=0}^q\sum_{n=0}^q p_{jn}a^jt^n,
 \quad p_{jn}\ge0.}\tag{P4}
\]
There are at most (q+1)^2 collected coefficients, even though P3 displays many minors. Multiplicities, zero covariance directions, and complex phases are retained.

The two exact endpoint identities are
\[
 P(a,0)=\det(aI+M^{\dagger_{G_0}}M),\qquad
 P(0,t)=|\det M|^2D(t).
 \tag{P5}
\]
In particular the full root determinant at a=0 is independent of the metric by a proved cancellation, in agreement with GitHub SD6. It has not been estimated by discarding small singular directions.

## 3.2 A finite coefficient algorithm without a covariance eigensolve

Formula P3 establishes coefficient positivity. The polynomial itself can also be computed in the original normalized matrix coordinates, using C(t)=I+tK and A_C(t)=adj(C(t)). For q>=2,
\[
 \boxed{P(a,t)=
 \frac{\det[aA_C(t)+M_0^*A_C(t)M_0]}
      {\det C(t)^{q-2}}.}\tag{P6}
\]
This is an exact polynomial division. To verify it, G=C^(-1)=A_C/det C, so
 det(aI+M^(dagger_G)M)=det(aG+M^*GM)/det G.
Substitute the two expressions for G and multiply by det C. P3 proves the division has zero remainder and degree at most q in t. In P6 M_0 may be taken in any G_0-isometric frame; no diagonal K is required. For q=1 the scalar operator is metric independent and P(a,t)=(a+|M|^2)D(t).

Alternatively, interpolation at q+1 distinct positive t values and q+1 distinct positive a values determines the polynomial exactly. Numerical use of this algorithm still needs an error enclosure; coefficient positivity is not permission to ignore cancellation in an unstable interpolation implementation.

## 3.3 Simultaneous scales have an O(log q) complete determinant remainder

For a,t>0 set
\[
 L(a,t)=\max_{p_{jn}>0}[\log p_{jn}+j\log a+n\log t].
\]
Then
\[
 \boxed{0\le F(a,t)-[L(a,t)-\log D(t)]
 \le2\log(q+1).}\tag{P7}
\]
Proof: P is a sum of at most (q+1)^2 nonnegative terms, one attaining exp L. This retains every phase inside p_(jn). It is not an absolute-value replacement of entries of M or of the current.

Thus every scaling path a=exp(u), t=exp(v) is controlled by a finite maximum of affine functions in (u,v), with the displayed uniform remainder. On the four original endpoints, at the SAME a and t, and signs (+,+,-,-),
\[
 \boxed{\left|\mathcal R F-
 \mathcal R[L-\log D]\right|\le4\log(q+1).}\tag{P8}
\]
Indeed each endpoint error is in [0,2log(q+1)]; two occur with each sign. This is a correlated error interval, not four independently selected favorable values.

No coefficient asymptotic is assigned without evaluating its actual minors. The finite diagram in P7 is the exact remaining coefficient problem for simultaneous regularizer and source-activation scales, with an error below order q.

## 3.4 Uniform logarithmic curvature budget and finite oscillation

Fix a>0 and write x=log t. The constant coefficient of P(a,t) is positive. Its logarithmic derivatives are
\[
 \partial_x\log P=\sum_n n\pi_n(x),\quad
 \partial_x^2\log P=\operatorname{Var}_{\pi(x)}(n),
\]
where pi_n is the actual positive coefficient weight p_n(a)e^(nx)/P. Likewise
\[
 \partial_x\log D=\sum_i\frac{e^x\kappa_i}{1+e^x\kappa_i},\qquad
 \partial_x^2\log D=\sum_i\frac{e^x\kappa_i}{(1+e^x\kappa_i)^2}.
\]
Consequently
\[
 \boxed{|\partial_xF|\le q,\qquad
 \int_{-\infty}^{\infty}|\partial_x^2F|\,dx\le2q.}\tag{P9}
\]
For the integral, each log polynomial has increasing slope from zero to its degree. Their second derivatives are nonnegative and integrate to at most q each; take their difference. This is a total-variation bound on logarithmic curvature, independent of the original matrix condition numbers. It is not a claim that F itself is monotone.

Stationary points solve P_tD-PD_t=0. This real polynomial has degree at most 2q-2: when both degrees are q their highest term cancels; otherwise their degree sum is at most 2q-1. Therefore F is either constant or has at most 2q-2 positive stationary points, counted with multiplicity. This proves a finite oscillation bound across the whole positive source-activation axis.

## 3.5 Return to the exact GitHub arithmetic determinant and its source change

For each original cutoff N, apply P2 to its ACTUAL M, G_N and Omega_N. Since D_N(t)=det(I+tK_N), the exact endpoint relation is
\[
 \boxed{F_N(a,t)-F_N(a,0)
 =\log\frac{P_N(a,t)}{P_N(a,0)}-\Delta_N(t).}\tag{P10}
\]
Here Delta_N(t) is precisely the full mixed-source metric cost calculated in H19–H23, not the arithmetic root determinant. At t=0 the original rank-one formula SD5 and the complete action receiver SD13 apply, with both boundary resolvent energies retained. Equation P10 is their exact handoff to the new metric. At t>0 a rank-one selfadjoint correction is not assumed for the new metric.

On the simple-quartet family and a=tau_0 q^2 with fixed tau_0>0,
\[
 \log\det(I+M^{\dagger_{G_N}}M/a)=O_h(q).
 \tag{P11}
\]
To prove it, SD12 bounds all but the top singular value by B_h q, and H5 gives log epsilon_N=O_h(q), uniformly; thus the top contribution is O(q) and the remaining q-1 contributions are bounded constants each. For the actual joint metric, input J3 gives instead
\[
 0\le\log\det(I+M^{\dagger_{G_N^J}}M/a)
 \le q\log[1+C_h^2k^2e^{W_k}/a]
 =O_h(kq\log^2q)=o(q^2).
 \tag{P12}
\]
Insert P11–P12 and the supplied V13 into P10 at t=1. The SPECTRAL numerator acquires the fully evaluated leading return
\[
 \boxed{\begin{aligned}
 \log\frac{P_N(a,1)}{P_N(a,0)}
 =q^2[\log(q/k)-\tfrac32-E_\square-2\mathfrak F(s_N)]
 +O_h(kq\log^2(q+2)).
 \end{aligned}}\tag{P13}
\]
Its four-endpoint return is C_Bq^2+o(q^2). Thus the large metric determinant cost is accompanied by a matching numerator cost in the full arithmetic spectral determinant. Neither is removed from the original action while its counterpart is held fixed.

These are proved comparisons of the same arithmetic endomorphism. They do not equate eigenvalues of M with generalized eigenvalues of the metric pair, and they do not infer an observed-current sign from the nonnegative spectral coefficients.

## 3.6 The next order-q spectral correction is evaluated at the same two scales

Define, without altering the source metric,
\[
 \mathcal F_N(\tau,t)=\log\det(I+\tau M^{\dagger_{G_N(t)}}M).
\]
Thus F_N(a,t)=q log a+mathcal F_N(1/a,t). The scalar q log a cancels in the two-metric comparison and in the four-cutoff return because the dimension and scalar are the same.

For the CANONICAL metric, H10 gives the following finite estimate on its explicit domain epsilon_N>B_hq:
\[
 \boxed{\left|\mathcal F_N(\tau,0)
 -\log(1+\tau\epsilon_N^2)\right|
 \le2\log\frac{\epsilon_N}{\epsilon_N-B_hq}
 +(q-1)\tau B_h^2q^2.}\tag{P14}
\]
For the top direction, the derivative of log(1+tau exp(2x)) in x is in [0,2]. Apply it between log s_1 and log epsilon_N and use H10. The q-1 other nonnegative logarithms are at most tau B_h^2q^2 each. This proves P14 without an assumption about their lower singular scales. Before the stated finite guard, the two bounding singular values in H10 still give direct one-sided logarithmic bounds.

For tau=exp(-2sigma q), sigma>0, the right side tends to zero uniformly in the original cutoff window. Write H5 as log epsilon_N^2=2q psi(s_N)+e_N, with |e_N|=O_h(k log^2 q). The elementary inequality
0<=log(1+exp u)-u_+<=log 2 therefore gives
\[
 \boxed{q^{-1}\mathcal F_N(e^{-2\sigma q},0)
 =2(\psi(s_N)-\sigma)_++O_h(k\log^2q/q).}\tag{P15}
\]
This limit is continuous at the threshold and needs no deleted threshold point. It is uniform in N and in sigma on compact subsets of (0,infinity). In particular the complete four-cutoff logarithmic spectral return is
\[
 \boxed{q^{-1}\mathcal R\mathcal F_N(e^{-2\sigma q},0)
 \longrightarrow4[(a_0-\sigma)_+-(a_1-\sigma)_+].}\tag{P16}
\]

For alpha_k=exp(-2theta q) on 0<=theta<sigma, H24 gives
0<=mathcal F_N(exp(-2sigma q),alpha_k)
<=q exp(-2sigma q)||M||_(G_N(alpha_k))^2 ->0,
uniformly. Combining this with the EXACT P10, not an asymptotic for its individual large terms, proves
\[
 \boxed{\begin{aligned}
 \mathcal R\left[
 \log\frac{P_N(e^{2\sigma q},e^{-2\theta q})}{P_N(e^{2\sigma q},0)}
 -\Delta_N(e^{-2\theta q})\right]
 =-4q[(a_0-\sigma)_+-(a_1-\sigma)_+]+o_h(q).
 \end{aligned}}\tag{P17}
\]
At the explicit scales theta=1/16 and sigma=1/8,
\[
 \boxed{\mathcal R\left[
 \log\frac{P_N(e^{q/4},e^{-q/8})}{P_N(e^{q/4},0)}
 -\Delta_N(e^{-q/8})\right]
 =\bigl[\tfrac12-4\log(4/\pi)\bigr]q+o_h(q).}\tag{P18}
\]
The coefficient is approximately -0.4662579010819618. Its negativity refers to this displayed difference of the spectral numerator and the COMPLETE source-metric cost. It does not remove the still-present C_B q^2 leading four-cutoff return of either component. No unproved order-q expansion of Delta_N itself is claimed. P18 evaluates the correlated smaller combination directly through the original arithmetic operator, all its singular directions, and the exact source-activation map.

## 3.7 An explicit projective realization of the scalar family and every mixed curvature

The positive polynomial also gives a concrete geometric map, not just an analogy with a period construction. Let u,v be complex coordinates, put a=|u|^2 and t=|v|^2, and keep the finite coefficient set in P4. On u!=0 define
\[
 \Phi_M(u,v)=[\sqrt{p_{jn}}\,u^jv^n]_{p_{jn}>0},\qquad
 \Psi(v)=[\sqrt{d_n}\,v^n]_{d_n>0},\quad D(t)=\sum_nd_nt^n.
 \tag{P19}
\]
These are actual regular maps to finite projective spaces: coefficients are fixed complex constants, every coordinate is a monomial, the numerator has the nonzero coordinate u^q because p_(q,0)=1, and the denominator has d_0=1. For the original invertible companion, p_(0,0)=|det M|^2>0, so Phi extends over u=0 as well. No statement about extension over all points at infinity is presumed.

Let bold Phi and bold Psi denote these specific coordinate lifts, not arbitrary rescalings. Their squared norms satisfy the exact identities
\[
 \|\boldsymbol\Phi_M(u,v)\|^2=P(|u|^2,|v|^2),\quad
 \|\boldsymbol\Psi(v)\|^2=D(|v|^2).
\]
Consequently
\[
 \boxed{F(|u|^2,|v|^2)
 =\log\|\boldsymbol\Phi_M(u,v)\|^2
  -\log\|\boldsymbol\Psi(v)\|^2.}\tag{P20}
\]
With the convention omega_FS=i partial barpartial log(sum |Z_j|^2), this gives
\[
 \boxed{i\partial\bar\partial F
 =\Phi_M^*\omega_{FS}-\Psi^*\omega_{FS}.}\tag{P21}
\]
For an elementary verification, differentiation of log||f||² in a complex tangent direction gives
(||f||²||df||²-|f*df|²)/||f||⁴. This is nonnegative by Cauchy--Schwarz. Applying the formula to each displayed lift proves P21 and its full mixed entries. The spectral determinant's curvature is a DIFFERENCE of these two retained positive forms; it is not declared positive by retaining only the numerator.

In real logarithmic coordinates x=log a,y=log t, the numerator Hessian is exactly the covariance matrix of the two integer exponents (j,n) in the probability weights p_(jn) exp(jx+ny)/P. The denominator subtracts the variance of n in d_n exp(ny)/D from its yy entry. Thus all mixed terms, their possible signs, and the cancellation responsible for P9 have explicit coefficient expressions. The finite dominance regions in P7 are the associated affine comparisons of these same monomials; their error is already controlled uniformly.

This projective realization recovers the SCALAR spectral determinant and its parameter curvature through P20--P21. The original source, arithmetic operator, kernel, class and complex current are still the separately displayed matrices and maps in M1--M18 and C1--C4. No claim that Phi is an admissible Hodge period map, or a faithful replacement of those arithmetic objects, is made.


---

# 4. Exact projected-current polynomials and the growing activation response

## 4.1 Every original projected-current phase is a rational function with a positive denominator

Use the explicit original-to-orthonormal map M1, retaining the actual observation. In this frame set S=[0,I_r], C_t=I_q+tK_0, D_t=S C_t S^*, Q_t=D_t^(-1), G_t=C_t^(-1), L_t=C_t S^*Q_t, and P_t=I-L_tS. Let A be the original arithmetic matrix transported by M1 and x the unchanged original class in this frame. Put b=Sx. Define the COMPLETE mixed pair
\[
 z(t)=\langle P_tx,A(I-P_t)x\rangle_{G_t},\qquad
 w(t)=\langle(I-P_t)x,AP_tx\rangle_{G_t}.
 \tag{C1}
\]
The original complex current is built from overline(z)w; no real part is taken until its prescribed final sign test.

Let d_0=det C_t, d_1=det D_t, C^#=adj C_t, D^#=adj D_t. Define the scalar polynomial
\[
 U(t)=b^*D^\# S A C_tS^*D^\#b.
\]
Then the exact numerator formulas are
\[
 p_z(t)=d_1x^*C^\#A C_tS^*D^\#b-d_0U(t),
\]
\[
 p_w(t)=d_1b^*D^\#S A x-U(t).
 \tag{C2}
\]
They satisfy
\[
 \boxed{z(t)=\frac{p_z(t)}{d_0(t)d_1(t)^2},\qquad
 w(t)=\frac{p_w(t)}{d_1(t)^2}.}\tag{C3}
\]
Proof: L_t^*G_t=Q_t S and P_t^*G_t=G_tP_t=G_t-S^*Q_tS. Substituting these two identities directly in C1 gives C2–C3. Thus both moving projections, both complex pairings, and their entire product are retained.

The adjugate degree bounds give
\[
 \deg p_z\le q+2r-1,\qquad \deg p_w\le2r-1.
\]
On the whole nonnegative real t axis, d_0,d_1>0. Therefore
\[
 \boxed{\Re(\overline{z(t)}w(t))
 =\frac{\Re(\overline{p_z(t)}p_w(t))}{d_0(t)d_1(t)^4},
 \quad\deg\Re(\overline{p_z}p_w)\le q+4r-2.}\tag{C4}
\]
The overline in the numerator conjugates coefficients while t is real. The result is a real polynomial. It is identically zero exactly on its coefficient-vanishing locus; on every other finite-data stratum it has at most q+4r-2 positive zeros, counted with multiplicity. This is a linear-in-q bound for all possible sign changes along the actual covariance path. When r=0, or b=0, both currents vanish directly.

All numerator coefficients are finite expressions in the original metric, actual normal-source covariance, original observation and class. They are not assigned signs by this statement. In particular a numerical sign decision requires native coefficient enclosures that separate zero; the polynomial-degree argument is not such a numerical evaluation.

For several covariance parameters C=I+sum t_i K_i, the same formulas have total degree at most q+4r-2 and denominators positive throughout the nonnegative orthant. Thus the complete projected-current sign regions are specified by one explicit real polynomial inequality on that parameter space. The dependence of its coefficients on a period or arithmetic moments is retained separately; it is not presumed polynomial in an unexamined period coordinate.

## 4.2 Exact example showing why the phases cannot be assigned from volume monotonicity

Use the actual finite matrices
K_0=[[9,3],[3,1]], A=[[0,1],[1,0]], x=(0,1)^T and S=(0,1).
They give
\[
 \boxed{\Re(\overline z w)=
 \frac{9t^2(1+2t-8t^2)}{(1+t)^4(1+10t)}.}\tag{C5}
\]
It is positive at t=1/4, zero at t=1/2, and negative at t=3/4. Meanwhile the source determinant log det(I+tK_0)=log(1+10t) is increasing. Every value follows by substitution in the full C1, not a sign chosen independently for two factors. This is a declared auxiliary matrix family, not an xi packet.

## 4.3 The effective number of changed metric directions is evaluated

Return to the actual common-multiplicity quartet, for which the pasted proof establishes
|log lambda_j-2(j-1)ell_k|<=E_(h,k), E_(h,k)=O_h(q), ell_k=log(q/k).
Let
\[
 \mathsf K_N=G_N^{1/2}\Omega_NG_N^{1/2},\qquad
 d_N(t)=\operatorname{Tr}[t\mathsf K_N(I+t\mathsf K_N)^{-1}].
 \tag{C6}
\]
This is the derivative of the ACTUAL mixed metric cost with respect to log t. It counts each covariance direction with its exact response between zero and one.

For b>=0 put t_k(b)=exp(-2bq ell_k). For any L>0, define
\[
 h_{k,L}=\frac{E_{h,k}+L+\log2}{2q\ell_k}.
\]
Then
\[
 \boxed{\left|q^{-1}d_N(t_k(b))-(1-b)_+\right|
 \le h_{k,L}+2/q+e^{-L}.}\tag{C7}
\]
Proof: the j-th response is p_j=t(lambda_j-1)/(1+t(lambda_j-1)). For (j-1)/q<=b-h the numerator is at most exp(-L). For (j-1)/q>=b+h, lambda_j>=2 and lambda_j-1>=lambda_j/2, giving 1-p_j<=exp(-L). Count the uniform grid outside the intervening band. The grid endpoints cost at most 2/q. This proves the estimate for all b, including b=0,1.

Taking L=log q gives uniform error O_h(1/log(q/k)) and
\[
 \boxed{q^{-1}d_N(t_k(b))\longrightarrow(1-b)_+.}\tag{C8}
\]
For the original observation, its response d_(B,N) is obtained by compressing K_N with the exact coisometry in the pasted O2. Equivalently it is Tr[tW(I+tW)^(-1)] in M2. Formula M10 gives
\[
 \boxed{0\le d_N(t)-d_{B,N}(t)\le m}\tag{C9}
\]
at every t>=0. On m=8k-16 this is o(q), uniformly over the entire activation axis. Thus the observed quotient has the same effective-dimension law, with its actual rank normalization, without a generic-orientation assumption.

There is also a full curvature measure on the logarithmic activation scale:
\[
 d\nu_{k,N}(b)=2\ell_k\sum_jp_j(b)(1-p_j(b))\,db.
 \tag{C10}
\]
It is nonnegative, its total mass on the real line is rank(K_N)/q, and it converges weakly to uniform probability measure on [0,1]. Its distribution functions are controlled by C7, and the input rank lower bound makes its mass tend to one. This is weak convergence of the complete response measure; no pointwise limiting density inside an unresolved spectral layer is claimed. The observed covariance has the same limit. The difference of the two curvature measures need not be positive; C9 does not assert that it is.

## 4.4 How the two new scales are connected

C8 uses t=exp(-2bq log(q/k)); H21 uses t=exp(-2theta q). The latter is the specific moving value b=theta/log(q/k), approaching zero in C8. H19–H20 evaluate its next q^2 term directly, rather than substituting a moving b into a mere pointwise limit. Thus the weak-activation coefficient -2theta q^2 and the effective-dimension limit are connected by the exact eigenvalue formula, with all small and zero covariance directions present.

The arithmetic heat transition uses tau=exp(-2sigma q) on the unchanged multiplication M, whereas C6 is a response of the actual metric-correction operator. The exact spectral polynomial P2–P3 relates the two through the original metric and arithmetic minors. No arithmetic eigenvalue is replaced by a covariance eigenvalue.

## 4.5 Resulting finite family-control statement

For every fixed native input and every k, the source-activation path has: an explicit source isometry; the full observed and kernel minima; an exact positive Gram identity for all mixed curvatures; an integrated kernel-sized section-motion budget; exact principal-angle factors; all four action blocks; a positive spectral polynomial with degree at most q in each scale; and a current sign polynomial of degree at most q+4r-2. These are direct algebraic and analytic calculations on the displayed original maps.

The comparison with the user's Deligne/BBT goal is at this level of explicit finite-family and boundary control. Bakker--Brunebarbe--Tsimerman's mixed-period-map result concerns admissible mixed period maps and their associated-graded images. Such a period-map identification is not supplied here. The equations above prove the family control actually used, without assigning a Hodge or Frobenius interpretation to an unconstructed map.


---

# 5. The newest finite derivative repair enters through the full arithmetic units

## 5.1 Precisely which later GitHub result was read

During this continuation the repository advanced from `ff251e3adc5fd78049170b8fc94c26f882df3d14` to its child `52274804051e325c8a6ef69c17b3958cc2caba0a`. The newly read file is `workbenches/splitzero-tandem/continuations/20260920-gamma-and-finite-derivative/FINITE_DERIVATIVE_REPAIR.tex`, blob `d84cc1ac47df9f2d74b60c73d464f56034bc3261`. Its complete text and result index were read. The separate full Gamma-inequality proof was not independently reread here; its Taylor-cutoff consequence is imported exactly as attributed in the derivative repair. No complete implementation or actual native xi derivative evaluation was run.

That source retains the original auxiliary entire function F(z)=sum c_(2j)z^(2j), its derivative bound F_m, and coefficient bound |c_(2j)|<=pi^j/(2^(j+1)j!). Its admissible absolute tolerance is the ORIGINAL minimum
\[
 \widetilde E_m=\min(4F_m,E_m),
\]
not the inconsistent maximum at a later printed occurrence. The corrected selection uses the overlapping strict tests F_m<E_m for zero output and E_m<2F_m for a computed derivative. At least one passes throughout the positive parameter domain, including equality E_m=F_m or E_m=2F_m. The finite computed index set need not be an initial interval. These are retained source results, not new discoveries attributed to this continuation.

For its actual Taylor polynomial P_J and |p|<=1, the source proves the full tail bound
\[
 |F^{(m)}(p)-P_J^{(m)}(p)|<m!\,(2\pi)^J/J!\quad(J\ge12).
 \tag{U1}
\]
The derivative's full finite coefficient-evaluation constant is
\[
 K_m=\sum_{\substack{0\le j<J\ \ 2j\ge m}}
 \frac{(2j)!}{(2j-m)!}
 \left[1+(2j-m)\frac{(22/7)^j}{2^{j+1}j!}\right].
 \tag{U2}
\]
Coefficient and point errors at most epsilon produce evaluation error at most epsilon K_m. The Taylor truncation and finite evaluation budgets remain separate, with their original constants. The source's six-step Gamma identity and rational H(2006)<H(2000) check were also replayed in the small auxiliary checker; they replace no native moment or period evaluation.

## 5.2 The actual local unit needs derivatives through order 2m-1

Keep the original g=2xi, full divisor h, root rho of complete multiplicity m, and h_rho=h/(s-rho)^m. In the original divided-jet coordinate z=s-rho put
\[
 b_j=[z^j]h_\rho(\rho+z),\qquad
 f_j=\frac{g^{(m+j)}(\rho)}{(m+j)!},\quad0\le j<m.
 \tag{U3}
\]
Since the original multiplicity is complete, b_0!=0 and f_0!=0. The FULL unit jet u=j_(z^m)(g/h) is the finite recurrence
\[
 \boxed{u_0=f_0/b_0,\qquad
 u_j=b_0^{-1}\left(f_j-\sum_{i=1}^j b_i u_{j-i}\right).}\tag{U4}
\]
Indeed g(rho+z)=z^m(f_0+f_1z+...), h(rho+z)=z^m(b_0+b_1z+...), and coefficient comparison after cancelling the SAME z^m proves U4. This exact cancellation uses the original full multiplicity, not a small approximate denominator at rho.

Thus a length-m unit requires derivatives g^(m),...,g^(2m-1), not just g through order m-1. The derivative repair in Section 5.1 is part of a finite zeta-evaluation input method; the conversion from its auxiliary F derivatives to these g derivatives still retains the original Riemann--Siegel, Gamma, and product-rule factors. Those conversion data and certified roots/periods are not supplied numerically in this task. We do not identify F^(j) with xi^(j), or assign values from the auxiliary Taylor bound alone.

The physical unit matrix is exactly
\[
 U_{jl}=u_{j-l}\ (j\ge l),\qquad U_{jl}=0\ (j<l).
\]
Its inverse is the same lower triangular coefficient map associated with
\[
 v_0=u_0^{-1},\qquad
 v_j=-u_0^{-1}\sum_{i=1}^j u_i v_{j-i}.\tag{U5}
\]
It commutes with multiplication by rho+z, since both are polynomial multiplications modulo z^m. Every higher unit derivative is present in that identity and in the metric (U^(-1))^* D U^(-1).

## 5.3 Exact unit-inverse and metric error bounds

The following formulas specify finite certificate domains rather than treating rounded input matrices as exact. Let Uhat be a certified invertible centre for a unit matrix, with ||Uhat^(-1)||<=B. Divided-coefficient enclosures of radii e_j give
\[
 \|U-Uhat\|\le E:=\sum_{j=0}^{m-1}e_j,
\]
because each lower shift has norm at most one. On the explicitly testable domain r=BE<1, the convergent finite-dimensional Neumann inverse and its resolvent identity give
\[
 \boxed{\|U^{-1}\|\le\frac{B}{1-r},\qquad
 \|U^{-1}-Uhat^{-1}\|\le\frac{B^2E}{1-r}.}\tag{U6}
\]
To prove it, factor U=Uhat(I+Uhat^(-1)(U-Uhat)); the perturbation norm is at most r. Its geometric inverse series gives the first bound. The exact identity U^(-1)-Uhat^(-1)=U^(-1)(Uhat-U)Uhat^(-1) gives the second. A usable B itself is the sum of the absolute coefficients of the exact finite inverse U5 at Uhat, with their interval upper bounds.

For the retained positive jet Gram D and physical H=U^(-*) D U^(-1), Hhat=Uhat^(-*) D Uhat^(-1), the full bound is
\[
 \boxed{\|H-Hhat\|
 \le\|D\|B^3E\frac{2-r}{(1-r)^2}.}\tag{U7}
\]
This follows by writing X^*DX-Y^*DY=(X-Y)^*DX+Y^*D(X-Y), using X=U^(-1),Y=Uhat^(-1), and both bounds in U6. Cross terms have not been dropped.

For a relative certificate, set
\[
 a=\sqrt{\operatorname{cond}D}\,\frac{r}{1-r}.
\]
On the explicit certificate domain a<1,
\[
 \boxed{(1-a)^2Hhat\preceq H\preceq(1+a)^2Hhat.}\tag{U8}
\]
In fact U^(-1)Uhat=I+T with ||T||<=r/(1-r). The D-relative norm of T is at most a. Apply the triangle inequality and its reverse to (I+T)x in D, then pull back by Uhat^(-1). This specifies both coordinate maps and proves the claimed original-frame order.

## 5.4 Ordered tensoring and the same full minima

For factorwise relative bounds U8, tensor products give the complete ordered Gram enclosure
\[
 \left(\prod_i(1-a_i)^2\right)\bigotimes_iHhat_i
 \preceq\bigotimes_iH_i
 \preceq
 \left(\prod_i(1+a_i)^2\right)\bigotimes_iHhat_i.\tag{U9}
\]
This is a positive matrix inequality on the ENTIRE tensor coefficient space, not a monomialwise bound. Restriction by the actual cyclic injection or minimization in the same specified affine value fibres preserves both scalar factors. When an approximate unit is used to label values, the change of labels is explicitly Uhat^(-1)U in each factor and its ordered tensor product; the observation and class must be transported by that same map before comparing their metrics. A metric bound alone is not permission to change the arithmetic value constraint.

For a fixed q-dimensional attained quotient, U9 yields a logarithmic determinant error at most
\[
 2q\max\left\{-\sum_i\log(1-a_i),\ \sum_i\log(1+a_i)\right\}.
 \tag{U10}
\]
An actual projected-phase calculation must additionally propagate the matrix/map uncertainties through the full numerator C2. For a certified real-coordinate box of its primitive entries, the polynomial Phi=Re(conj(p_z)p_w) satisfies the explicit bound
\[
 |\Phi(v)-\Phi(v_0)|\le\sum_j r_j\sup_{v\ \mathrm{in\ box}}|\partial_j\Phi(v)|.\tag{U11}
\]
Expand each derivative polynomial and bound its monomials by the coordinate-box maxima. The fundamental theorem of calculus on the line from v_0 to v proves U11. A centre value larger in absolute value than this radius certifies its sign; otherwise the result remains an interval containing zero. There is no promised termination at an exact phase zero and no automatic transfer of the derivative bound U1 into a native-current sign.

This gives the newest derivative repair a precise place in the programme: certified g derivatives enter the full unit recurrence U4, then U6--U10 retain their effects on the original tensor and quotient metrics, while U11 handles the complete phase polynomial. It is a finite error-composition result. No native derivatives, roots, moments or periods have been invented or numerically evaluated here.
