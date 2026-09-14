# Exact comparison review: announced arithmetic-tail proof

Date: 2026-09-13. This file records the independent calculations, subsequently checked against the complete BT and TW drafts. `FINAL_REVIEW.md` identifies the exact editions and additions reviewed.

The fixed object is the actual complete hypothetical quartet, with full common order m≥1, h of degree 4m, g=2xi, w_h(u)=|(g/h)(1/2+iu)|²/(2pi), and m_(h,k)=w_h^{*k}, k≥3. The original mass is mu_h^k. Put alpha=pi/2, B=42+8m, M=B/2=21+4m, and p=8m−9/2. The fixed reference density is sigma(u)=|Gamma(1/4+iu/2)|²/(2pi), whose mass is sqrt(2pi).

## 1. Lower scalar comparison

The original endpoint proof, NOTE (23)–(29), retains the full g/h multiplier and establishes

\[
m_{h,k}(u)\ge c_h\vartheta_h^{k-3}e^{-\alpha(|u|+k-3)}(k-2+|u|)^{-B}.
\]

Take positive constants c_Gamma,C_Gamma for the two-sided bound sigma(u) between c_Gamma and C_Gamma times e^(−alpha|u|)(1+|u|)^(−1/2). For t=|u| and k≥3,

\[
k-2+t\le(k-2)(1+t),\qquad (1+t)^B\le2^{B/2}(1+t^2)^{B/2},\qquad(1+t)^{1/2}\ge1.
\]

Consequently the announced constant is correct:

\[
a_k=\frac{c_h\vartheta_h^{k-3}e^{-\alpha(k-3)}}{C_\Gamma 2^{B/2}(k-2)^B},
\qquad m_{h,k}(u)\ge a_k\frac{\sigma(u)}{(1+u^2)^M}.
\]

No lower bound on pointwise zeta values was inserted. The original local integral bound and the actual three-factor convolution supply the strictly positive envelope.

## 2. Upper scalar comparison and retained boundary mass

The completely reviewed boundary calculation BT14 establishes the actual bound

\[
e^{\alpha|u|}w_h(u)\le C_h(1+|u|)^{-p},\qquad p=8m-9/2>1.
\]

Here C_h is the fully explicit C_h^tilt from BT12, with its compact and tail terms retaining the entire quartet denominator. Thus v(u)=e^(alpha u)w_h(u) is integrable, has literal mass M_h(alpha), and obeys v(u)≤C_h(1+|u|)^(−p). The convolution hyperplane x_1+...+x_k=u is covered by the k sets where |x_j|≥|u|/k. On each set bound the selected v(x_j) by C_h(1+|u|/k)^(−p), and integrate every other factor over the entire real line. Nonnegativity gives

\[
v^{*k}(u)\le C_h k(1+|u|/k)^{-p}M_h(\alpha)^{k-1}
\le C_h k^{p+1}(1+|u|)^{-p}M_h(\alpha)^{k-1}.
\]

For u≥0, v^{*k}(u)=e^(alpha u)m_(h,k)(u). The actual quartet is stable under conjugation, so w_h and m_(h,k) are even; this gives the same bound with |u| on the entire line. Since p≥1/2,

\[
m_{h,k}(u)\le A_k\sigma(u),\qquad A_k=\frac{C_h}{c_\Gamma}k^{p+1}M_h(\alpha)^{k-1}.
\]

The exponent k−1 belongs to the actual tilted mass, not a probability normalization. The boundary integrability requires p>1; this holds even at m=1, when p=7/2.

## 3. Polynomial multiplication and Cauchy duality

Inherited TG.11–14 give the real monic reference polynomials b_j and their exact squared norms

\[
\gamma_j=\sqrt2\,j!\Gamma(j+1/2),\qquad
u b_j=b_{j+1}+j(j-1/2)b_{j-1}.
\]

Thus e_j=b_j/sqrt(gamma_j) satisfies

\[
u e_j=\sqrt{(j+1)(j+1/2)}e_{j+1}+\sqrt{j(j-1/2)}e_{j-1},
\]

with the second term absent at j=0. On the degree≤N polynomial space, the raising and lowering weighted shifts have norm at most N+1 separately. The triangle inequality therefore proves ||uP||_sigma≤2(N+1)||P||_sigma. Iterating on the successive spaces P_(N+j) yields

\[
\|u^jP\|_\sigma\le[2(N+M)]^j\|P\|_\sigma,\qquad0\le j\le M.
\]

The binomial theorem, with no cross terms because the multiplier is scalar and real, gives

\[
\int |P|^2(1+u^2)^M\sigma\,du
=\sum_{j=0}^M\binom Mj\|u^jP\|_\sigma^2
\le D_N\|P\|_\sigma^2,
\quad D_N=[1+4(N+M)^2]^M.
\]

For P≠0, Cauchy–Schwarz now gives

\[
\|P\|_\sigma^4
\le\left(\int\frac{|P|^2\sigma}{(1+u^2)^M}\,du\right)
\left(\int|P|^2\sigma(1+u^2)^M\,du\right)
\le D_N\|P\|_\sigma^2\int\frac{|P|^2\sigma}{(1+u^2)^M}\,du.
\]

Divide by the positive sigma norm; the zero polynomial satisfies the conclusion as well. Together with the two scalar bounds, this proves the full finite comparison

\[
\frac{a_k}{D_N}\|P\|_\sigma^2\le\|P\|_{m_{h,k}}^2\le A_k\|P\|_\sigma^2
\quad(P\in\mathcal P_N).
\]

Equivalently, in any identical polynomial coordinate basis, a_k H_N^sigma/D_N≤H_N^ar≤A_k H_N^sigma. This is not obtained by reversing an infimum or using a test polynomial in the wrong direction.

## 4. Original monic spaces and uniform errors

The original variable is S=k/2+iu. On the affine space of degree-n monic polynomials in S, P(S)↦i^(−n)P(k/2+iu) is a bijection to the affine space of degree-n monic polynomials in u and preserves absolute values. Its inverse is Q(u)↦i^n Q((S−k/2)/i). On lower-degree vector spaces the underlying substitution is an algebra isomorphism; the degree-dependent monic phase is not represented as one linear algebra homomorphism across all degrees.

Take minima of the already proved inequalities on that identical affine monic space. This proves

\[
\boxed{a_k\gamma_n/D_n\le\omega_{h,k,n}\le A_k\gamma_n.}
\]

The displayed constants give |log a_k|+|log A_k|=O_h(k+log k), while log D_n=O_h(log(n+1)). Since log k≤k for k≥3, the valid uniform conclusion is

\[
\log\omega_{h,k,n}=\log\gamma_n+O_h(k+\log(n+1)),\qquad k\ge3,\ n\ge0.
\]

At n=0 this compares the literal original mass mu_h^k to gamma_0=sqrt(2pi). No density has been divided by its mass.

## 5. Literal q-windows and exact finite inequalities

For every n≥0 and r≥1,

\[
\frac{a_k}{A_kD_{n+r}}\frac{\gamma_{n+r}}{\gamma_n}
\le\frac{\omega_{h,k,n+r}}{\omega_{h,k,n}}
\le\frac{A_kD_n}{a_k}\frac{\gamma_{n+r}}{\gamma_n}.
\]

All logarithmic comparison errors are therefore explicit. For r=q=(1+k(m−1))(k+1)^2 and n=q−1,q, their logarithms divided by 2q tend to zero. The exact reference recurrence gives

\[
\gamma_{n+q}/\gamma_n=\prod_{j=1}^q(n+j)(n+j-1/2).
\]

After taking the 2q-th root and dividing by q, its logarithm tends by the monotone Riemann sum for log(1+x) to integral_0^1 log(1+x)dx=log(4/e). Hence the proposed literal-window limit is valid. This conclusion concerns those q-length windows; the estimate alone does not prove consecutive recurrence asymptotics. For general n/q→theta>0, the corresponding constant is exp((theta+1)log(theta+1)−theta log theta−1).

## 6. The exact common-quotient consequence

For the identical full remainder map modulo the original degree-q relation chi, the source polynomial identity preserves all jets. Minimizing on each identical affine fibre gives

\[
\frac{a_k}{D_N}G_N^\sigma\preceq G_N^{ar}\preceq A_kG_N^\sigma.
\]

Thus, writing T_N^sigma=V_N^ar/V_N^sigma,

\[
(a_k/D_N)^q\le T_N^\sigma\le A_k^q.
\]

For the same four literal volumes this yields

\[
-q\{2\log(A_k/a_k)+\log D_{q-1}+\log D_q\}
\le\mathcal B_k^{ar}-\mathcal B_k^\sigma
\le q\{2\log(A_k/a_k)+\log D_{2q-1}+\log D_{2q}\}.
\]

This is an O_h(q(k+log q)) bound derived through the actual observation map. The reference here is the fixed one-factor sigma of mass sqrt(2pi); it is not the inherited AT Gamma convolution with parameter k/4 and mass (2pi)^(k/2).
