# Fixed-kernel mass, sharp dyadic contraction, and original determinant recovery

This is an independent derivation for the 022 intake. It retains the original observation, word, source metric, zero-energy space and full kernel. The input is the complete `inputs/KERNEL_MEMORY_MASS.md` and Section 2 of `PROOF.md` in the supplied arithmetic-probe package. Their core mass and two-sided extrapolation statements are valid. The additional results below are the lower contraction, a tighter upper matrix using the same samples, a stronger finite defect constant, and a direct original-boundary covariance receiver. No native period value is assigned.

The finite elimination is the Feshbach–Schur construction of Geneviève Dusson, Israel Michael Sigal and Benjamin Stamm, [arXiv:2105.02058v1, Theorem 1.2](https://arxiv.org/abs/2105.02058v1), with original author TeX lines 398–489 read. The complete finite identities used here are proved below. The existing [020 exact-memory proof RM1–23](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/13ca9b136fcdae48df7454bd9bf99e1ef22dd03c/workbenches/splitzero-tandem/continuations/20260922-original-growth-resolvent/ORIGINAL_RESOLVENT_MEMORY_PROOFS.md) and [original resolvent proof PR19–22](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/13ca9b136fcdae48df7454bd9bf99e1ef22dd03c/workbenches/splitzero-tandem/continuations/20260922-original-growth-resolvent/RECEIVED_RESOLVENT_PROOFS.md) retain their attributions. The sealed 021 providers are [MR1–29, full matrix recovery](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/e40b46fde72c245dd79ef5691f59c21d6cbf0c75/workbenches/splitzero-tandem/continuations/20260922-original-observation-recovery/MATRIX_RECOVERY_PROOFS.md) and [SD1–54, scalar recovery and original determinant receiver](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/e40b46fde72c245dd79ef5691f59c21d6cbf0c75/workbenches/splitzero-tandem/continuations/20260922-original-observation-recovery/SCALAR_RECOVERY_PROOFS.md). Their exact source identities are recorded in the ledger.

## 1. Complete original spaces and the mass identity

Let \(E=\mathbb C^q\), \(G=G^*>0\), and let the original onto observation be \(\Lambda:E\to B=\mathbb C^n\). Let \(I_K:\mathbb C^m\to E\) be the fixed full column frame of \(K=\ker\Lambda\), where \(m=q-n\). For the unchanged word \(T:E\to E\), set
\[
 H=G^{-1}T^*GT,\quad V=\ker T,\quad \nu=\operatorname{rank}T,\quad
 Q=(\Lambda G^{-1}\Lambda^*)^{-1},\quad L=G^{-1}\Lambda^*Q,
 \quad H_K=I_K^*GI_K.
 \tag{KM1}
\]
All adjoints between physical spaces use \(G\). A star on a coordinate matrix is its conjugate transpose. The actual isometries are \(J_B=LQ^{-1/2}\), \(J_K=I_KH_K^{-1/2}\). Multiplication gives \(\Lambda L=I\), \(L^*GL=Q\), \(J_K^*GJ_K=I\), and \(J_B^*GJ_K=0\). Thus these maps give an orthogonal decomposition with inverse \([J_B,J_K]^*G\); the original \(G,Q,H_K\) have not been replaced.

Put \(Z=K\cap V\), \(t=\dim Z\), \(K_+=K\ominus_GZ\), and \(p=m-t\). Choose once a \(G\)-isometry \(J_+:\mathbb C^p\to K_+\). In a fixed frame \([I_Z,I_1]=I_KS\), the metric on \(K/Z\) is
\[
 H_{\rm quot}=H_{11}-H_{01}^*H_{00}^{-1}H_{01};
 \qquad x\longmapsto I_1x-I_ZH_{00}^{-1}H_{01}x
 \tag{KM2}
\]
is its isometry into \(K_+\). This follows by completing the full \(G\)-square in the \(I_Z\) coefficient. No arbitrary block of the source metric is deleted.

Define
\[
 A=J_+^*GHJ_+>0,\quad C=J_+^*GHJ_B,\quad B_0=J_B^*GHJ_B,
 \quad Y(z)=Q^{1/2}\Lambda z(zI+H)^{-1}LQ^{-1/2}.
\]
The zero block \(Z\) is annihilated by \(H\) and has no energy cross term. Inverting the remaining full block of \(zI+H\) gives
\[
 F(z):=zY(z)^{-1}=zI+B_0-C^*(zI+A)^{-1}C,
 \quad W_B=F'(0)=I+C^*A^{-2}C,
 \quad W_K=I+A^{-1}CC^*A^{-1}.
 \tag{KM3}
\]
These formulas follow also by solving the lower equation
\((zI+A)a+Cb=0\) and substituting into the upper equation. In original observed value coordinates, \(F\) is the congruence of \(zQ\mathscr Y(z)^{-1}\), where \(\mathscr Y=\Lambda z(zI+H)^{-1}L\); its multiplication order is fixed. Sylvester elimination in \(\left(\begin{smallmatrix}I&U\\-V&I\end{smallmatrix}\right)\) proves \(\det(I+UV)=\det(I+VU)\). Consequently \(\det W_B=\det W_K\), with the distinct numbers of unit eigenvalues retained.

Write \(P=P_{V^{\perp_G}}^G\), \(H_+=H|_{V^{\perp_G}}\), and
\[
 \Gamma=J_+^*GPJ_+,\quad R=PJ_+,\quad U=R\Gamma^{-1/2}.
\]
Here \(0<\Gamma\preceq I_p\): \(PJ_+x=0\) would put \(J_+x\) in \(K_+\cap V=0\). Moreover \(U^*GU=I\). Put \(A_0=U^*GH_+U\). Since \(H\) annihilates \(V\),
\(A=\Gamma^{1/2}A_0\Gamma^{1/2}\) and
\(A^2+CC^*=\Gamma^{1/2}U^*GH_+^2U\Gamma^{1/2}\).
It follows that
\[
 W_K=\Gamma^{-1/2}(I+\mathcal E^*\mathcal E)\Gamma^{-1/2},
 \quad \mathcal E=(I-UU^{\dagger_G})H_+UA_0^{-1},
 \quad \operatorname{rank}\mathcal E\le d_0:=\min(p,\nu-p).
 \tag{KM4}
\]
Indeed insert \(I=UU^{\dagger_G}+(I-UU^{\dagger_G})\) between the two \(H_+\) factors. This proves the mass identity including every off-diagonal positive-energy term.

For actual positive spectral bounds \(lI\preceq_G H_+\preceq_G uI\), functional calculus gives \(H_+^2\preceq(l+u)H_+-luI\). Compress by \(U\), then use
\[
 (l+u)x-lu\le \frac{(l+u)^2}{4lu}x^2
 \quad\text{because}\quad
 \frac{((l+u)x-2lu)^2}{4lu}\ge0.
\]
The result is
\[
 \Gamma^{-1}\preceq W_K\preceq
 \frac{(l+u)^2}{4lu}\Gamma^{-1},\qquad
 0\le\log\det W_B+\log\det\Gamma
 \le d_0\log\frac{(l+u)^2}{4lu}.
 \tag{KM5}
\]
The upper constant is the classical Kantorovich constant, here derived directly. To attain it, choose a unit vector in a two-dimensional positive space with eigenvalues \(l,u\), giving the \(l\)-eigenspace weight \(u/(l+u)\) and the \(u\)-eigenspace weight \(l/(l+u)\). Then its compressed energy is \(2lu/(l+u)\) and its mass ratio is exactly the displayed constant. Adding any zero component to that kernel vector supplies a prescribed angle in \((0,1]\); choosing its orthogonal-complement observation gives the complete original setup.

The memory space \(\mathcal M=\operatorname{span}\{A^jCb:0\le j<p\}\) is reducing for \(A\); its complement is annihilated by \(C^*\). For an eigenvector \(x\) in that complement, \(HJ_+x=J_+Ax\) has positive eigenvalue, so \(J_+x\in V^{\perp_G}\). Hence \(\Gamma x=x\). By spectral decomposition,
\[
 \Gamma=\Gamma_{\mathcal M}\oplus I_{\mathcal M^\perp}.
 \tag{KM6}
\]
The \(t\) original zero-angle directions are still \(Z\); they are not unit directions. This is the exact connection to MR8 and MR11. A memory reduction removes only unit positive angle factors and keeps the actual metric of its chosen frame.

## 2. The common filtered kernel mass

For \(\sigma>0\), define \(H_\sigma=H(\sigma I+H)^{-1}\). This is the energy of the specified operator \(T_\sigma=T(\sigma I+H)^{-1/2}\) in the same \(G\); it is not identified with the original polynomial word. Its zero space is \(V\), and therefore \(\Gamma\) is unchanged. The full scalar functional identity, including eigenvalue zero, gives
\[
 Y_\sigma(s)=\frac{sI+Y(\sigma s/(1+s))}{1+s},\qquad s>0.
 \tag{KM7}
\]
Indeed both sides on an energy \(\lambda\) equal \(s(\sigma+\lambda)/(s\sigma+(s+1)\lambda)\). Observation by the same \(J_B\) proves the matrix formula.

Choose an isometric complement to \(U\) inside \(V^{\perp_G}\) and write the original inverse energy, in this one fixed decomposition, as
\[
 H_+^{-1}=
 \begin{pmatrix}\mathcal A&\mathcal B^*\\
 \mathcal B&\mathcal C\end{pmatrix},\qquad
 aI\preceq H_+^{-1}\preceq bI,\quad a=1/u,\quad b=1/l.
\]
The complement may be empty. The lower block of
\((I+\sigma H_+^{-1})(H_\sigma)=I\) gives
\((H_\sigma)_{21}(H_\sigma)_{11}^{-1}
=-\sigma(I+\sigma\mathcal C)^{-1}\mathcal B\).
Substitution into KM4 proves
\[
 W(\sigma)=\Gamma^{-1/2}
 [I+\mathcal B^*\sigma^2(I+\sigma\mathcal C)^{-2}\mathcal B]
 \Gamma^{-1/2}.
 \tag{KM8}
\]
All \(W(\sigma)\) act in the same \(J_+\) coordinates. In a different fixed frame \(J_+S\), their operators are \(S^{-1}W(\sigma)S\), their metric is \(P_S=S^*S\), and their quadratic forms are \(S^*W(\sigma)S\). Determinants of these forms must be divided by \(\det P_S\). A different frame at each \(\sigma\) does not define the linear combinations below.

Differentiation of the scalar rational function gives
\[
 W'(\sigma)=2\sigma\Gamma^{-1/2}
 \mathcal B^*(I+\sigma\mathcal C)^{-3}\mathcal B\Gamma^{-1/2}\succeq0.
 \tag{KM9}
\]
The limits are \(\Gamma^{-1}\) at zero and the original unfiltered mass at infinity. No commutation of \(\mathcal B\) with \(\mathcal C\) is used.

There is a stronger finite block constraint than the separate norm bounds in the input. From
\((H_+^{-1})^2\preceq(a+b)H_+^{-1}-abI\), its lower-right block gives
\[
 \mathcal B\mathcal B^*\preceq(bI-\mathcal C)(\mathcal C-aI).
 \tag{KM10}
\]
For every nonnegative scalar function \(\phi\) on \([a,b]\), the nonzero eigenvalues of \(\mathcal B^*\phi(\mathcal C)\mathcal B\) equal those of
\(\phi(\mathcal C)^{1/2}\mathcal B\mathcal B^*\phi(\mathcal C)^{1/2}\). Thus
\[
 \|\mathcal B^*\phi(\mathcal C)\mathcal B\|
 \le\max_{a\le c\le b}(b-c)(c-a)\phi(c).
 \tag{KM11}
\]
This is sharp: for any \(c\in[a,b]\), the matrix
\(\left(\begin{smallmatrix}a+b-c&\sqrt{(b-c)(c-a)}\\
\sqrt{(b-c)(c-a)}&c\end{smallmatrix}\right)\)
has eigenvalues \(a,b\), and realizes equality for the one-dimensional kernel/complement. This construction is in the positive energy space; any added zero component of the kernel only introduces the unchanged outer \(\Gamma\) congruence.

For \(\phi(c)=\sigma^2/(1+\sigma c)^2\), differentiation locates the maximum at
\(c=(a+b+2\sigma ab)/(2+\sigma(a+b))\). Substitution yields
\[
 \Gamma^{-1}\preceq W(\sigma)\preceq
 \left[1+\frac{\sigma^2(b-a)^2}
 {4(1+\sigma a)(1+\sigma b)}\right]\Gamma^{-1}
 \preceq\left[1+\frac{(\sigma/l)^2}{4(1+\sigma/l)}\right]\Gamma^{-1}.
 \tag{KM12}
\]
The last inequality also follows by maximizing with \(a=0\). It uses only the proved floor \(l\), and for \(0<\sigma\le l\) its multiplier is at most \(9/8\), improving the input's \(5/4\).

## 3. Dyadic weights and their exact positive error

Let \(r\ge1\), \(s_i=2^{-i}\sigma\), \(0\le i<r\), and define
\[
 w_i=\frac{(-1)^{r-1}\prod_j s_j}
 {(\sum_j s_j^{-1})s_i^2\prod_{j\ne i}(s_i-s_j)},\qquad
 R_r(\sigma)=\sum_{i=0}^{r-1}w_iW(s_i).
 \tag{KM13}
\]
For distinct nodes the coefficient of \(x^{r-1}\) in their Lagrange interpolant is
\([s_0,\ldots,s_{r-1}]f=\sum_i f(s_i)/\prod_{j\ne i}(s_i-s_j)\).
It vanishes on powers below \(r-1\). Partial fractions of
\(\prod_i(z+s_i)^{-1}\), followed by differentiation at \(z=0\), give
\([s_0,\ldots,s_{r-1}]x^{-2}
=(-1)^{r-1}(\sum_i s_i^{-1})/\prod_i s_i\).
Consequently
\[
 \sum_iw_i=1,\qquad\sum_iw_i s_i^j=0\quad(2\le j\le r).
 \tag{KM14}
\]
The missing first moment is intentional: the mass error starts at order two.

For completeness, with \(\rho=1/2\) and \(j=r-1-i\), direct factoring gives
\[
 |w_i|=\frac{1-\rho}{1-\rho^r}
 \frac{\rho^{j(j+3)/2}}
 {\prod_{a=1}^{j}(1-\rho^a)\prod_{a=1}^{r-1-j}(1-\rho^a)}.
\]
The finite identity
\(\prod_{a=0}^{n-1}(1+x\rho^a)
=\sum_{j=0}^n\rho^{j(j-1)/2}
\frac{\prod_{a=1}^n(1-\rho^a)}
{\prod_{a=1}^j(1-\rho^a)\prod_{a=1}^{n-j}(1-\rho^a)}x^j\)
follows by induction on \(n\): multiply by \(1+x\rho^n\) and combine adjacent coefficients. Apply it with \(n=r-1,x=\rho^2\). Then
\[
 A_r:=\sum_i|w_i|=\prod_{j=2}^{r}\frac{1+2^{-j}}{1-2^{-j}}<3.
 \tag{KM15}
\]
Indeed \(\log A_r=2\sum_{j=2}^r\operatorname{arctanh}(2^{-j})
\le(32/15)\sum_{j=2}^\infty2^{-j}=16/15\).
To certify \(16/15<\log3\) without a decimal assertion, use
\(\log3=2\sum_{n\ge0}(1/2)^{2n+1}/(2n+1)>1+1/12=13/12>16/15\).

The same partial-fraction identity at \(z=c^{-1}\), differentiated once, proves
\[
 \begin{split}
 R_r(\sigma)&=\Gamma^{-1/2}
 [I+\mathcal B^*\Psi_r(\mathcal C;\sigma)\mathcal B]\Gamma^{-1/2},\\
 \Psi_r(c;\sigma)&=
 \frac{c^{r-1}(\prod_i s_i)\sum_i(1+cs_i)^{-1}}
 {(\sum_i s_i^{-1})\prod_i(1+cs_i)}>0\quad(c>0).
 \end{split}
 \tag{KM16}
\]
Explicitly, \(\sum_iw_i s_i^2/(1+cs_i)^2\) is the ratio of the divided differences of \((1+cx)^{-2}\) and \(x^{-2}\); both have sign \((-1)^{r-1}\), and their evaluated ratio is KM16. The continuous endpoint value at \(c=0\) is used when needed. This proves positivity despite the alternating weights.

Write \(s=\sigma/l\le1\) and
\(J_r=2^{-r(r-1)/2}/(2^r-1)\). Since
\(\prod_i s_i/(\sum_i s_i^{-1})=J_r\sigma^{r+1}\), the input's bound is
\(\delta_r=rJ_rs^{r+1}\). KM10 gives the sharper bounds
\[
 \begin{split}
 \epsilon_r(a,b,\sigma)&=
 \max_{a\le c\le b}(b-c)(c-a)\Psi_r(c;\sigma),\\
 \epsilon_r(a,b,\sigma)&\le
 \widehat\delta_r:=
 J_r\left(\frac r{r+1}\right)^{r+1}s^{r+1},\\
 \Gamma^{-1}&\preceq R_r(\sigma)
 \preceq(1+\epsilon_r)\Gamma^{-1}.
 \end{split}
 \tag{KM17}
\]
To prove the second line, bound the sum in KM16 by \(r\), the denominator product below by one, and \((b-c)(c-a)\le(b-c)c\). The maximum of \(c^r(b-c)\) is
\(b^{r+1}r^r/(r+1)^{r+1}\), attained at \(c=rb/(r+1)\).
KM11 proves the first line is itself the sharp finite constant for the class with the specified positive spectral bounds when both the kernel image and its positive-energy complement have positive dimension. When \(d_0=0\), the defect is identically zero. Its maximization is over a displayed continuous rational function on a compact interval; no unknown native angle occurs. For \(r=1\), use the explicit, stronger KM12 value. Every determinant error has at most \(d_0\) contributing eigenvalues, by the rank of \(\mathcal B\).

## 4. Both contractions and a sharper interval from the same masses

Put \(S_r(x)=\sum_{i=0}^{r-1}(1+2^{-i}x)^{-1}\). Cancellation of the dyadic products in KM16 gives the continuous ratio
\[
 h_r(x):=\frac{\Psi_r(c;\sigma/2)}{\Psi_r(c;\sigma)}
 =2^{-(r+1)}\frac{1+x}{1+2^{-r}x}\frac{S_r(x/2)}{S_r(x)},
 \qquad x=c\sigma.
 \tag{KM18}
\]
To prove its monotonicity on \([0,1]\), set
\(p_i=(1+2^{-i}x)^{-1}/S_r(x)\),
\(u_i=2^{-i}x/(1+2^{-i}x)\), and
\(H_r(x)=-xS_r'(x)/S_r(x)=\sum p_i u_i\).
Differentiation with respect to \(\log x\) gives
\(p_i'=p_i(H_r-u_i)\), \(u_i'=u_i(1-u_i)\), and therefore
\[
 \frac{dH_r}{d\log x}
 =\mathbb E(u)-2\mathbb E(u^2)+(\mathbb E(u))^2\ge0,
 \tag{KM19}
\]
because \(0\le u_i\le1/2\). Thus
\(d\log(S_r(x/2)/S_r(x))/d\log x=H_r(x)-H_r(x/2)\ge0\).
The other nonconstant factor in KM18 is increasing. Endpoint continuity proves
\[
 \chi_r:=2^{-(r+1)}\le h_r(x)\le
 \theta_r:=\frac{S_r(1/2)}{(2^r+1)S_r(1)}<1 .
 \tag{KM20}
\]
Both are sharp scalar endpoint bounds. For available spectral bounds \(a,b\), replace them by
\(\chi=h_r(a\sigma)\), \(\theta=h_r(b\sigma)\); \(b\sigma\le1\).
Even when a nonzero coupling cannot occur exactly at an endpoint eigenvalue of the full inverse energy, KM11's two-dimensional energies approach it, so the endpoint constants cannot be uniformly improved for the nonzero error ratio.

In particular
\(\theta_1=4/9,\theta_2=44/175,\theta_3=212/1593\).
Also \(S_r(x/2)/S_r(x)\le4/3\) on \([0,1]\): it is the weighted mean of
\((1+2^{-i}x)/(1+2^{-i-1}x)\le4/3\).
Hence \(\theta_r\le4/[3(2^r+1)]\). Functional calculus and the unchanged congruence give, writing \(A_\Gamma=\Gamma^{-1}\), \(E=R_r(\sigma)-A_\Gamma\), \(E'=R_r(\sigma/2)-A_\Gamma\),
\[
 0\preceq\chi E\preceq E'\preceq\theta E,\qquad
 D:=R_r(\sigma)-R_r(\sigma/2)\succeq0.
 \tag{KM21}
\]
No simultaneous diagonalization of the kernel masses is asserted.

The input's lower matrix is valid. Its upper matrix can be improved:
\[
 L_r=R_r(\sigma/2)-\frac{\theta}{1-\theta}D,\qquad
 U_r^\sharp=R_r(\sigma/2)-\frac{\chi}{1-\chi}D,
 \qquad L_r\preceq A_\Gamma\preceq U_r^\sharp
 \preceq R_r(\sigma/2).
 \tag{KM22}
\]
Indeed \(D=E-E'\), and KM21 gives
\(\chi D/(1-\chi)\preceq E'\preceq\theta D/(1-\theta)\).
Only the same \(r+1\) masses at \(2^{-i}\sigma\), \(0\le i\le r\), occur.
Their exact interval difference is
\[
 U_r^\sharp-L_r=\beta D,\qquad
 \beta=\frac{\theta-\chi}{(1-\theta)(1-\chi)}.
 \tag{KM23}
\]
The earlier upper matrix corresponds to using only \(E'\succeq0\); KM22 also uses the lower contraction.

For an available defect bound \(\epsilon\) at \(\sigma\), define
\[
 \alpha=\frac{\theta-\chi}{1-\theta}\epsilon,\qquad
 \zeta=\frac{\theta-\chi}{1-\chi}\epsilon.
\]
Then
\[
 (1-\alpha)A_\Gamma\preceq L_r\preceq A_\Gamma
 \preceq U_r^\sharp\preceq(1+\zeta)A_\Gamma.
 \tag{KM24}
\]
One may decrease \(\zeta\) to the minimum with
\((\theta-\chi)\epsilon' /[\theta(1-\chi)]\), where \(\epsilon'\) is a bound at \(\sigma/2\). This follows by replacing \(E\) by \(E'/\theta\) in \(E'-\chi E\). For all the universal choices here, \(\alpha<1\). At \(r=1,\sigma=l\), KM12 and KM20 give
\(\epsilon\le1/8\), \(\alpha\le7/160\), and \(\zeta\le7/216\).
For \(r\ge2\), the weaker input estimates already give
\(\theta\epsilon/(1-\theta)\le4/33<1\), since
\(\theta\le4/15\), \(\delta_r\le1/3\).
For the latter, \(\delta_2=1/3\) and
\(\delta_{r+1}/\delta_r
=((r+1)/r)2^{-r}(2^r-1)/(2^{r+1}-1)<1\).
Thus the strict positivity claimed by the input is proved, and KM24 improves it.

All exact determinant and exterior bounds keep the original metric. They are
\[
 \log\det L_r\le-\log\det\Gamma\le\log\det U_r^\sharp,\qquad
 \log\det U_r^\sharp-\log\det L_r
 =\log\det(I+\beta L_r^{-1/2}DL_r^{-1/2}).
 \tag{KM25}
\]
The last positive matrix has at most \(d_0\) nonunit eigenvalues. Therefore its logarithm is at most
\(\beta\operatorname{tr}(L_r^{-1}D)\), and at most
\(d_0\log[1+\beta\operatorname{tr}(L_r^{-1}D)/d_0]\) when \(d_0>0\), by concavity of the scalar logarithm. It is also at most
\(d_0\log[(1+\zeta)/(1-\alpha)]\).
For each \(1\le j\le p\), min–max places the ordered eigenvalue of \(A_\Gamma\) between those of \(L_r,U_r^\sharp\); multiplying its first \(j\) eigenvalues gives the complete rank-\(j\) inverse exterior interval. Rank zero has determinant one. Rank beyond \(p\) does not define an inverse on the original zero-angle directions.

## 5. Noisy masses in the same complete metric

For each \(0\le i\le r\), let \(\widetilde W_i=\widetilde W_i^*\) be an approximation to \(W(2^{-i}\sigma)\) in the single frame of KM8, with
\[
 -\eta_iW(2^{-i}\sigma)\preceq
 \widetilde W_i-W(2^{-i}\sigma)\preceq
 \eta_iW(2^{-i}\sigma).
 \tag{KM26}
\]
This is an explicit error interface, not a conclusion from scalar sample rounding. A Hermitian part may be taken before certifying the interface. Put \(w_{-1}=w_r=0\), and
\[
 c_i(t)=\frac{w_{i-1}-t w_i}{1-t}\quad(0\le i\le r),\qquad
 \kappa_i=1+\frac{(2^{-i}\sigma/l)^2}{4(1+2^{-i}\sigma/l)},\quad
 e_t=\sum_{i=0}^{r}|c_i(t)|\eta_i\kappa_i .
\]
Then \(\sum c_i(t)=1\), and the exact matrix \(X_t=\sum c_i(t)W_i\) is
\(L_r\) for \(t=\theta\), \(U_r^\sharp\) for \(t=\chi\), and the incoming upper matrix for \(t=0\). Multiplying each two-sided error by its signed coefficient and using KM12 proves
\[
 -e_tA_\Gamma\preceq\widetilde X_t-X_t\preceq e_tA_\Gamma .
 \tag{KM27}
\]
This retains heterogeneous errors and each actual sample's filter constant. The signs of adjacent \(w_i\) alternate, so direct summation gives
\(\sum_i|c_i(t)|=A_r(1+t)/(1-t)\) for \(0\le t<1\).
For common \(\eta_i\le\eta\),
\(e_t\le(9/8)\eta A_r(1+t)/(1-t)<(27/8)\eta(1+t)/(1-t)\).
Using \(5/4\) instead recovers the input's \(15\eta/4\) and its stated lower-error constant, so those enclosures are valid.

On \(e_\chi<1\) and \(\widetilde L_r>0\), the certified matrices
\[
 L_{\rm cert}=\frac{\widetilde L_r}{1+e_\theta},
 \qquad U_{\rm cert}=\frac{\widetilde U_r^\sharp}{1-e_\chi}
 \quad\text{satisfy}\quad
 0<L_{\rm cert}\preceq A_\Gamma\preceq U_{\rm cert}.
 \tag{KM28}
\]
Indeed \(\widetilde L_r\preceq(1+e_\theta)A_\Gamma\) and
\(\widetilde U_r^\sharp\succeq(1-e_\chi)A_\Gamma\).
A sufficient fully explicit lower positivity guard is \(e_\theta<1-\alpha\), by KM24. If the less noisy upper matrix \(R_r(\sigma/2)\) is preferable, use \(t=0\) in the upper certificate; its guard is \(e_0<1\). One may retain whichever certified upper determinant is smaller. No ordered matrix minimum is assumed.

The exact rank \(d_0\) bounds the analytic extrapolation defect. It does not bound arbitrary errors in KM26. For example, if \(\mathcal B=0\) and \(\Gamma=I_p\), every exact mass is \(I_p\), whereas the permitted approximation \((1+\eta)I_p\) has determinant error \(p\log(1+\eta)\), although \(d_0\) may be zero. A smaller noise rank is used only when the actual perturbation is supported on a proved common subspace. This preserves the input's separate statement about errors restricted to the recovered memory.

The ordinary determinant interval from KM28 is
\[
 \log\det\widetilde L_r-p\log(1+e_\theta)
 \le-\log\det\Gamma\le
 \log\det\widetilde U_r^\sharp-p\log(1-e_\chi).
 \tag{KM29}
\]
For coefficient forms in metric \(P_S\), subtract \(\log\det P_S\) from both endpoints. At a zero-dimensional positive quotient all terms are empty and equal zero; no positivity guard is needed for an empty matrix.

## 6. Exact finite fixtures and the common-frame requirement

For the supplied auxiliary data
\[
 G=I_3,\quad T=\operatorname{diag}(0,1,2),\quad
 I_K=(5,2,1)^{\mathsf T},\quad
 \Lambda=\begin{pmatrix}-2&5&0\\-1&0&5\end{pmatrix},
\]
one has \(H_K=30\), \(P=\operatorname{diag}(0,1,1)\), and \(\Gamma=5/30=1/6\). The positive projected unit vector is \((2,1)/\sqrt5\). Its inverse-energy compression complement has
\(\mathcal C=2/5\) and \(|\mathcal B|^2=9/100\).
Consequently
\[
 W(\sigma)=6+\frac{27}{50}\frac{\sigma^2}{(1+2\sigma/5)^2},
 \quad \det W_B(\infty)=75/8,\quad
 \det W_B(\infty)\det\Gamma=25/16.
 \tag{KM30}
\]
The last number is KM5's sharp value for \(l=1,u=4\). This computes every metric factor of the example, rather than assigning \(I_K\) unit length.

At \(r=3,\sigma=l=1\), \(w=(1/21,-4/7,32/21)\), \(\theta=212/1593\), and \(\chi=1/16\). Direct rational substitution gives
\[
 R_3(1)=1992825/332024,\quad R_3(1/2)=7968825/1328096,
 \quad L_3=1572060375/262014368.
 \tag{KM31}
\]
Thus the incoming \(L_3<6<R_3(1/2)\) is correct, as is its ratio
\(48910877/48908545\). The strict logarithmic bound follows from
\(\log(1+x)<x\) at \(x=2332/48908545>0\).
The strengthened upper value is the exact rational
\[
 U_3^\sharp=\frac{16R_3(1/2)-R_3(1)}{15}
 =\frac{284595}{47432},
 \qquad L_3<6<U_3^\sharp<R_3(1/2).
 \tag{KM32}
\]
These are declared auxiliary data, not native period evaluations.

Observed masses have the same nonunit spectra separately, but their frame does not intertwine the whole family with KM8. In the original observed coefficient form,
\[
 \mathfrak W_B(\sigma)
 =Q+X_\sigma^*E_{\sigma,KK}^{-1}H_KE_{\sigma,KK}^{-1}X_\sigma,
 \quad X_\sigma=I_K^*GH_\sigma L,\quad
 E_{\sigma,KK}=I_K^*GH_\sigma I_K,
\]
the same fixture gives
\[
 \det[\mathfrak W_B(1)-\mathfrak W_B(1/2)]=-1/3136,\quad
 \det[(4\mathfrak W_B(1/2)-\mathfrak W_B(1))/3
       -\mathfrak W_B(0)]=-4/11025.
 \tag{KM33}
\]
A Hermitian two-square matrix with negative determinant has opposite-sign eigenvalues. These exact differences therefore disprove observed-frame monotonicity and the proposed substitution into the kernel extrapolation. The connecting map is retained: each mass is \(I+XX^*\) or \(I+X^*X\) for its own \(X=A_\sigma^{-1}C_\sigma\). Sylvester gives its equal nonunit spectrum, but \(X\) varies with \(\sigma\). It does not supply a single simultaneous conjugacy.

[Sealed 021 MR1–11](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/e40b46fde72c245dd79ef5691f59c21d6cbf0c75/workbenches/splitzero-tandem/continuations/20260922-original-observation-recovery/MATRIX_RECOVERY_PROOFS.md#L7) reconstructs the full relevant energy and its actual realization metric from \(2m+1\) original response matrices; no derivatives are needed. The canonical anchored energy scale there is restored before applying \(\sigma\): if \(\bar H=H/R\), use \(\bar\sigma=\sigma/R\), since
\(\bar H(\bar\sigma+\bar H)^{-1}=H(\sigma+H)^{-1}\).
On that recovered metric space, perform the explicit block calculation KM8 in one fixed memory frame. KM6 restores the remaining unit angles; KM2 restores the zero intersection as its attained quotient. Thus increasing \(r\) uses no additional original response samples after complete realization. This uses MR's exact reconstruction, not an assumption that separately diagonalized observed masses share a kernel basis.

The actual common realization metric can be computed from MR's selected matrices, not merely named. Use its notation
\(A_*=\mathcal L_0^{-1}\mathcal S_0\),
\(C_{1,*}=\mathcal L_0^{-1}B_L\), and \(B_R\).
Let \(h\) be the recovered memory rank and put
\(\mathcal C_*=[C_{1,*},A_*C_{1,*},\ldots,A_*^{h-1}C_{1,*}]\).
The spanning proof in MR3 makes its rank \(h\). Choose \(h\) independent columns \(\mathcal C_0\), and select the same indices in the block matrix
\([M_{i+j}]_{i,j=0}^{h-1}\), where \(M_j=B_RA_*^jC_{1,*}\), obtaining \(\mathcal H_0\). Then
\[
 P_*=\mathcal C_0^{-*}\mathcal H_0\mathcal C_0^{-1}>0,\qquad
 C_*=(I+A_*)^{1/2}C_{1,*},\qquad
 B_0=Z(1)+C_{1,*}^*P_*C_{1,*}.
 \tag{KM33a}
\]
For proof, with MR's scaled kernel energy \(\bar A=A/R\), its actual basis map \(Y_0\) satisfies
\(A_*=Y_0^{-1}\bar A Y_0\),
\(C_{1,*}=Y_0^{-1}C_1\), \(B_R=C_1^*Y_0\).
Consequently \(\mathcal H_0=\mathcal C_0^*Y_0^*Y_0\mathcal C_0\), which proves \(P_*=Y_0^*Y_0\) exactly. Its positive square root in \(C_*\) is functional calculus for the \(P_*\)-selfadjoint \(A_*\), equivalently the conjugate of \((I+\bar A)^{1/2}\), and therefore introduces no independently selected kernel frame. The identity for \(B_0\) follows from \(Z(1)=B_0-C_1^*C_1\). In MR's physical energy scale \(R\), the recovered original operator is
\[
 H_{\rm rec}=R\,G_{\rm rec}^{-1}E_{\rm rec},\qquad
 G_{\rm rec}=\operatorname{diag}(Q,P_*),\quad
 E_{\rm rec}=
 \begin{pmatrix}B_0&C_*^*P_*\\P_*C_*&P_*A_*\end{pmatrix}.
 \tag{KM33b}
\]
The map \((b,a)\mapsto Lb+J_+Y_0a\) pulls the physical metric and energy back to these displayed matrices. Filtering \(H_{\rm rec}\) and using this same \(P_*\) at every node gives the required masses. The missing reducing positive kernel space contributes the exact identity by KM6, and the missing \(Z\) contributes only the actual zero quotient. For \(h=0\), the memory blocks and their Gram are empty; no inverse of a zero-size selected minor is requested. This proves the source-to-fixed-frame map needed by the extrapolation in full.

## 7. Original arithmetic bounds and native determinant transfer

Retain the original simple-quartet family and physical coordinate \(s=k/2+iy\), so \(y=-i(s-k/2)\), together with the complete operator \(M_k\), polynomial word \(T_k=D_k(M_k)\), full observation \(\Lambda\), both source regions and all four cutoffs
\[
 N\in\{q-1,q,2q-1,2q\},\qquad
 q=(k+1)^2,\quad d=(k-7)^2,\quad
 \nu=\Delta=16k-48,\quad m=8k-16.
 \tag{KM34}
\]
The sealed 021 definitions and transversality give \(K\cap\ker T_k=0\), hence \(p=m\) and \(d_0=\Delta-m=8k-32\). The return operator is
\(\mathcal R f_N=f_{q-1}+f_q-f_{2q-1}-f_{2q}\).
No invariant condition defining \(I_K\) is removed.

Here is a finite energy floor expressed in original data. In the complete root-value coordinates, let \(G_N^{\rm val}\) be the actual source metric, let \(g_-I\preceq G_N^{\rm val}\preceq g_+I\) for all four cutoffs, and set \(\kappa_g=\max(1,g_+/g_-)\). The original word is the full diagonal matrix with entries \(D_k(\omega)\), including all \(d\) zeros. Put \(t_*=\min_{D_k(\omega)\ne0}|D_k(\omega)|\), a finite positive number specified by the retained root data. Then
\[
 \lambda_{\min}^+(T_k^{\dagger_G}T_k)\ge t_*^2/\kappa_g.
 \tag{KM35}
\]
To prove this, the Euclidean representative of the physical word is
\(G^{1/2}T_kG^{-1/2}\). For every positive singular index, multiplication on the left and right by invertible matrices bounds its singular value below by the product of their smallest singular values and the corresponding singular value of \(T_k\). This follows from min–max, or from the distance of \(Tx\) to the image of the preceding singular subspace. Its squared bound is \(g_-/g_+\) times that of the diagonal word. Thus no zero mode is counted as positive. On the original proved root-separation bound \(|\omega-\omega'|\ge2\delta\) for the factors of \(D_k(\omega)\), \(t_*\ge(2\delta)^d\), giving the supplied
\(l_*=\kappa_g^{-1}(2\delta)^{2d}\).

The source's complete finite constants are retained:
\[
 g_-=\ell_k/A_{\rm all},\quad g_+=u_kB_{\rm all},\quad
 A_{\rm all}=\frac{qe^2}{\sqrt{2\pi}}(2q+1)^{3/2}(4q+1)^{R_k+1},
\]
\[
 B_{\rm all}=q\sqrt{2\pi}e^{8q}
 \left(\frac{2q+R_k}{2\delta k}\right)^{2(q-1)},\qquad
 R_k=k\sqrt{\delta^2+\gamma^2}.
 \tag{KM36}
\]
Here \(\ell_k,u_k\) are the full-mass arithmetic/Gamma comparison constants, not word-energy eigenvalues. The mass calculation uses any certified floor, including KM35 directly. It requires no positive-energy equilibrium asymptotic. These original evaluation/interpolation constants enter only through their proved comparison and are not claimed as a new source estimate in this lane.

Let \(\pi_\partial:E\to\mathbb C^\Delta\) be the original full boundary root-value map, whose kernel is \(V\). Put
\[
 C_{\partial,N}=\pi_\partial G_N^{-1}\pi_\partial^*,\quad
 G_N^\partial=C_{\partial,N}^{-1},\quad
 J_\partial=\pi_\partial I_K,\quad
 B_{\partial,N}=J_\partial^*G_N^\partial J_\partial.
 \tag{KM37}
\]
The minimum of \(x^*G_Nx\) at fixed \(\pi_\partial x=b\) is \(b^*G_N^\partial b\): solve the Lagrange equation to obtain the section
\(G_N^{-1}\pi_\partial^*G_N^\partial\).
Its image is \(V^{\perp_G}\). Applying this to \(I_Ka\) shows
\(B_{\partial,N}=I_K^*G_NP_{V^{\perp_G}}I_K\).
Therefore, exactly in the original fixed coefficient volume,
\[
 \Gamma_N=H_{K,N}^{-1/2}B_{\partial,N}H_{K,N}^{-1/2},\quad
 \log\det H_{K,N}
 =\log\det B_{\partial,N}+\log\det A_{\Gamma,N}.
 \tag{KM38}
\]
This is [SD38's full boundary minimum](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/e40b46fde72c245dd79ef5691f59c21d6cbf0c75/workbenches/splitzero-tandem/continuations/20260922-original-observation-recovery/SCALAR_RECOVERY_PROOFS.md#L391), now connected to evaluated mass intervals; it is not a substitution of a raw boundary block.

Let \(\lambda_N\le\log\det A_{\Gamma,N}\le\upsilon_N\) be any interval from KM25 or KM29, with all metric-volume corrections included. If the original boundary covariance is evaluated, set \(b_N=\log\det[J_\partial^*C_{\partial,N}^{-1}J_\partial]\). Then
\[
 \begin{split}
 \mathcal R b_N+\lambda_{q-1}+\lambda_q-\upsilon_{2q-1}-\upsilon_{2q}
 &\le\mathcal K_k:=\mathcal R\log\det H_{K,N}\\
 &\le\mathcal R b_N+\upsilon_{q-1}+\upsilon_q-\lambda_{2q-1}-\lambda_{2q}.
 \end{split}
 \tag{KM39}
\]
Its exact width is \(\sum_N(\upsilon_N-\lambda_N)\); the boundary comparison width is absent because its actual determinant factor has been retained and evaluated. This is a finite original-data calculation, with a specified covariance and a specified fixed map at every cutoff. It does not insert an assumed value of \(b_N\).

When only the provider's comparison is available, retain
\(a_\partial I\preceq G_N^\partial\preceq b_\partial I\) and the source nesting \(G_{N+1}^\partial\preceq G_N^\partial\), with
\[
 \omega_k=\log(b_\partial/a_\partial),\quad
 a_\partial=\ell_k/A_{2q}^\partial,\quad b_\partial=u_kB_k^\partial,
\]
\[
 A_{2q}^\partial=\frac{\Delta e^2}{\sqrt{2\pi}}
 (2q+1)^{3/2}(4q+1)^{R_k+1},\quad
 B_k^\partial=\Delta\sqrt{2\pi}
 \left(\frac{2\Delta+R_k}{2\delta}\right)^{2(\Delta-1)} .
 \tag{KM40}
\]
Restriction by the fixed injective \(J_\partial\) preserves these bounds relative to \(J_\partial^*J_\partial\). Each low-to-high determinant drop belongs to \([0,m\omega_k]\). Summing the two paired drops gives
\(0\le\mathcal Rb_N\le2m\omega_k\). Hence KM39 recovers precisely HB16, with its upper endpoint enlarged by \(2m\omega_k\). Under the retained provider bound \(\omega_k=O_{h,\varpi}(k\log q)\), this width is \(o(kq)\). This fact does not evaluate the remaining coefficient.

The boundary-data version also has a finite noise certificate. Suppose the actual covariance calculation gives
\((1-\varepsilon_N)C_{\partial,N}\preceq\widetilde C_{\partial,N}
\preceq(1+\varepsilon_N)C_{\partial,N}\), with \(0\le\varepsilon_N<1\). Inversion, then restriction by \(J_\partial\), gives
\[
 (1-\varepsilon_N)\widetilde B_{\partial,N}
 \preceq B_{\partial,N}\preceq
 (1+\varepsilon_N)\widetilde B_{\partial,N},
 \quad
 \widetilde B_{\partial,N}=J_\partial^*\widetilde C_{\partial,N}^{-1}J_\partial.
\]
Therefore the original kernel determinant has the fully measured per-cutoff interval
\[
 \log\det\widetilde B_{\partial,N}
 +m\log(1-\varepsilon_N)+\lambda_N
 \le\log\det H_{K,N}\le
 \log\det\widetilde B_{\partial,N}
 +m\log(1+\varepsilon_N)+\upsilon_N .
 \tag{KM41}
\]
Apply the original four signs to these endpoints. Its width is
\(\sum_N[\upsilon_N-\lambda_N+
m\log((1+\varepsilon_N)/(1-\varepsilon_N))]\).
The midpoint is a certified estimator with half this width as absolute error. Both the finite covariance tolerance and the mass tolerance occur explicitly; no metric is assigned an unevaluated favorable sign.

At an intersection \(t>0\), use the fixed \(S,I_Z,I_1\) of KM2 and
\(B_{11}=I_1^*GP_{V^{\perp_G}}I_1\). The nonzero generalized angle matrix is \((B_{11},H_{\rm quot})\), since the lower-right block of \((S^*H_KS)^{-1}\) is \(H_{\rm quot}^{-1}\). Thus the exact complete extension is
\[
 \log\det H_K=
 \log\det H_{00}+\log\det B_{11}
 +\log\det A_\Gamma-2\log|\det S|.
 \tag{KM42}
\]
This rederives [SD50](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/e40b46fde72c245dd79ef5691f59c21d6cbf0c75/workbenches/splitzero-tandem/continuations/20260922-original-observation-recovery/SCALAR_RECOVERY_PROOFS.md#L530). KM25 and KM29 approximate the positive quotient factor only; the actual metric of \(Z\) is retained in \(H_{00}\). A fixed \(S\)-factor cancels under four signs, but \(H_{00}\) does not generally cancel. For \(T=0\), the positive quotient is empty, and KM42 still retains the full original kernel metric.

## 8. Connections to the scalar and endpoint receivers

The [scalar identity SD25–28](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/e40b46fde72c245dd79ef5691f59c21d6cbf0c75/workbenches/splitzero-tandem/continuations/20260922-original-observation-recovery/SCALAR_RECOVERY_PROOFS.md#L249) has a useful additional measured consequence. With
\(a_{\rm sc}=\lim_{z\downarrow0}z^{-(\nu-p)}\det\mathscr Y(z)>0\),
let \(U\) be the actual isometry of KM4 and choose a complement in \(V^{\perp_G}\). In those coordinates write
\[
 H_+=\begin{pmatrix}A_0&D^*\\D&E_0\end{pmatrix},\quad
 \Sigma=E_0-DA_0^{-1}D^*>0.
\]
Full Schur elimination gives
\(\det H_+=\det A_0\det\Sigma\), while
\(\det A=\det\Gamma\det A_0\).
The full resolvent determinant obtained by eliminating the observation/kernel blocks is
\(z^{\nu-p}\det(zI_p+A)/\det(zI_\nu+H_+)\).
Consequently
\[
 a_{\rm sc}=\frac{\det\Gamma}{\det\Sigma},\qquad
 -\log a_{\rm sc}-\upsilon_N
 \le\log\det\Sigma\le
 -\log a_{\rm sc}-\lambda_N .
 \tag{KM43}
\]
This evaluates the exact complementary-energy determinant to the measured mass accuracy once the scalar leading coefficient is computed. Its dimension is \(\nu-p\), not \(p\). For an empty complement, \(\det\Sigma=1\) and KM43 becomes equality with the scalar angle receiver. At repeated scalar cancellations the reduced leading coefficient is unchanged; no root multiplicity is omitted.

[Sealed MR9–11](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/e40b46fde72c245dd79ef5691f59c21d6cbf0c75/workbenches/splitzero-tandem/continuations/20260922-original-observation-recovery/MATRIX_RECOVERY_PROOFS.md#L144) proves that the positive endpoint spectrum of
\(Y_*=\Lambda P_V^GL\) has the same nonunit factors as \(\Gamma_K=J_K^*GP_{V^\perp}J_K\), including their actual isometric eigenvector map; all extra positive factors are units. Hence its positive determinant equals \(\det\Gamma\). KM25, KM29 and MR's independently certified endpoint interval can be intersected as scalar intervals: take the largest lower endpoint and the smallest upper endpoint. SD's complete scalar angle intervals can be intersected in the same way. This procedure is valid because each interval contains the same proved number, not because their errors are independent. An empty intersection signals an invalid input enclosure or inconsistent source data.

Mass alone cannot set the fixed original coefficient volume. For an explicit transverse example take
\[
 T=\operatorname{diag}(0,1),\quad\Lambda=(1,0),\quad I_K=e_2,
 \quad G_s=\operatorname{diag}(1,s),\quad s>0.
 \tag{KM44}
\]
For every \(s\), \(Q=1\), \(L=e_1\), \(\mathscr Y(z)=1\), \(\Gamma=1\), and all observed and kernel masses are the identity. Nevertheless \(H_K=s\), and the boundary projection \(\pi_\partial=(0,1)\) has \(C_\partial=1/s\) and \(B_\partial=s\). The positive one-dimensional metric cone \(\{s>0\}\) is the exact defect space of these fixed response data; KM38 is its connecting map back to the native determinant. Thus KM39 uses specified boundary data rather than assuming that fixed mass data determine this missing metric factor.

The native unresolved coefficient can now be enclosed directly. If the full interval from KM39 or KM41 is \([L_{\mathcal K},U_{\mathcal K}]\), then
\(\mathcal K_k/(kq)\) belongs to
\([L_{\mathcal K}/(kq),U_{\mathcal K}/(kq)]\) on the original \(k>0\) family. The exact lower-root receiver [RG50–54](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/13ca9b136fcdae48df7454bd9bf99e1ef22dd03c/workbenches/splitzero-tandem/continuations/20260922-original-growth-resolvent/GROWTH_PROOFS.md) retains
\(|\mathcal K_k-\log\mathcal A_{k,v}+G_0+G_1|\le\mathcal E_k\).
It follows by interval addition that
\[
 L_{\mathcal K}-\mathcal E_k
 \le\log\mathcal A_{k,v}-G_0-G_1
 \le U_{\mathcal K}+\mathcal E_k.
 \tag{KM45}
\]
The full original projected rows, both gains, all roots, source regions, and the earlier analytic status are unchanged. The finite error can shrink as the specified original matrices are evaluated more accurately. Nothing here supplies their unevaluated period-dependent entries or closes the Riemann hypothesis.

## 9. Verification and source use

The exact checker uses rational and Gaussian-rational arithmetic, tests the entire metric transport, and rejects observed-frame substitution, omission of the middle kernel metric in the mass, and unsupported noise-rank reduction. Its finite fixtures supplement the complete analytic proofs; they are not native arithmetic evaluations. Both normal and optimized runs use explicit failure gates. The source ledger records the exact input bytes, the prior MR/SD proof bytes and bounded original-author TeX reading. The sealed 021 files are never edited by this derivation.
