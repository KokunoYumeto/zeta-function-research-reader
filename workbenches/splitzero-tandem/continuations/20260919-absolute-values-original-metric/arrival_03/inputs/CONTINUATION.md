# The logarithmic arithmetic tail at the next surviving scale

19 September 2026. Additive continuation of the original signed arithmetic–Gamma calculation.

## 1. Result and analytic dependencies

Retain the fixed complete packet, its multiplicity \(m_0\), the full amplitude \(2\xi/h\), and the original sequence
\[
 k\equiv1\pmod4,\qquad e=1+k(m_0-1),\qquad q=e(k+1)^2.
\]
Set
\[
 d=4m_0-2,\quad c_*=\frac{\log2}{\pi},\quad
 I_h=\int_0^{\pi/2}\left(\frac{M_h'(\theta)}{M_h(\theta)}\right)^2d\theta,
\]
\[
 \mathcal C_\Gamma=2\mathcal L(2,\pi)-8\log2+4>0.
\]
Here \(\mathcal L\) has precisely the incoming EIQ/GEL normalization.

Using the quantitative central, averaged-tail, and relation-free-energy estimates stated in the incoming signed-value note, the following finer conclusion holds:
\[
 \boxed{\delta_{k,1}^{\rm ar}
 =-d\mathcal C_\Gamma q+c_*I_hk^2
   +\frac{\mathcal C_\Gamma}{2}\frac q{\log q}
   +o_h(q/\log q).}                                      \tag{ST1}
\]
More explicitly, with \(L=\log q\), on an eventual fixed-packet domain,
\[
 \begin{split}
 \left|\delta_{k,1}^{\rm ar}+d\mathcal C_\Gamma q-c_*I_hk^2
                    -\frac{\mathcal C_\Gamma q}{2L}\right|
 \le C_h\bigg[&\frac{q(1+\log L)^2}{L^2}+q^{199/200}L^2
       +\sqrt{qL}+\frac{k^2}{L^3}+kL^2
       +1+\frac{k^4}{q^2}\bigg].                         \tag{ST2}
 \end{split}
\]
Every term on the right is \(o_h(q/L)\). In particular the remainder is bounded by
\[
 C_hq\left[\frac{(1+\log\log q)^2}{(\log q)^2}
                  +q^{-1/200}(\log q)^2\right].       \tag{ST2a}
\]
The statement concerns the order-one Gamma reference, not a substituted order-\(k\) reference.

The new argument is the determinant transport of the retained logarithmic tail factor, together with a uniform small change of the rational-weight exponent. It does not differentiate an \(o(q)\) error. The quantitative incoming analytic estimates are recorded explicitly in Section 3. Their moving-potential and free-energy appendices have the same attributed, not independently certified, status as in the preceding integration. The present proof establishes the deductions from those estimates; it does not claim a new independent proof of those appendices.

## 2. Unchanged objects and determinant accounting

Write
\[
 w_h(y)=\frac{|(2\xi/h)(1/2+iy)|^2}{2\pi},\qquad m_k=w_h^{*k},
 \qquad \sigma(y)=\frac{|\Gamma(1/4+iy/2)|^2}{2\pi},
 \quad M_\sigma=\sqrt{2\pi}.
\]
The full relation polynomial remains
\[
 \chi_k(S)=\prod_{a,b=0}^k
 [S-k/2-(2a-k)\delta-i(2b-k)\gamma]^e,
 \qquad Q_k(y)=i^{-q}\chi_k(k/2+iy).
\]
All roots and primary orders remain. Let \(H_N[\mu]\) be the Gram of polynomials of degree at most \(N\), in the original monic coefficient convention, and let \(H_N^{\rm rel}[\mu]\) be the Gram of
\[
 \mathcal R_N=Q_k\mathcal P_{N-q}.
\]
A negative polynomial-degree bound denotes the zero space, whose determinant is one. The original quotient satisfies
\[
 \det G_N[\mu]=\frac{\det H_N[\mu]}{\det H_N^{\rm rel}[\mu]}.
                                                               \tag{ST3}
\]
The coordinate change between \(S\) and \(y\) has the same fixed factors at both measures, so those factors cancel in each measure comparison. This does not change an individual unpaired Gram determinant.

For \((N_0,N_1,N_2,N_3)=(q-1,q,2q-1,2q)\) and \(\varepsilon=(1,1,-1,-1)\),
\[
 \mathcal B_k[\mu]=\sum_{i=0}^3\varepsilon_i\log\det G_{N_i}[\mu],
 \qquad \delta_{k,1}^{\rm ar}=\mathcal B_k[m_k]-\mathcal B_k[\sigma].
\]
For a scalar \(A>0\), each quotient Gram is multiplied by \(A\); consequently
\[
 \mathcal B_k[A\mu]-\mathcal B_k[\mu]
       =(q+q-q-q)\log A=0.                              \tag{ST4}
\]
The scalar cancellation is used only on this full return.

Put
\[
 \alpha=\pi/2,\quad \mathfrak M=M_h(\alpha),\quad
 b=(\log M_h)'(\alpha),\quad C_k=[-kb,kb],
\]
and retain the literal outer-only density
\[
 \omega_k(y)=\begin{cases}\sigma(y),&y\in C_k,\\
                  \mathfrak M^{-k}m_k(y),&y\notin C_k.
             \end{cases}
\]
Then exactly
\[
 \delta_{k,1}^{\rm ar}=\delta_k^{\rm out}+\delta_k^{\rm cen,end},
 \quad \delta_k^{\rm out}=\mathcal B_k[\omega_k]-\mathcal B_k[\sigma].
                                                               \tag{ST5}
\]
The central endpoint changes the density on \(C_k\) while holding the actual exterior fixed.

## 3. Quantitative inputs actually used

The incoming central endpoint estimate, equation (30) of the value note, is
\[
 \delta_k^{\rm cen,end}=c_*I_hk^2+
 O_h\left(\frac{k^2}{\log^3(q+2)}+k\log^2(q+2)+1+\frac{k^4}{q^2}\right).
                                                               \tag{IN1}
\]
Its error is already smaller than the scale in (ST1).

Write \(c_\zeta=2\gamma_{\rm E}-\log(2\pi)\), where \(\gamma_{\rm E}\) is Euler's constant, not the ordinate of the packet. The averaged tail estimate, equation (13) of the value note, is
\[
 \int_T^{2T}\left|
 \frac{\mathfrak M^{-k}m_k(y)}{
   \frac{k}{\sqrt\pi\mathfrak M}(\log y+c_\zeta)
      (1+y^2)^{-d}\sigma(y)}-1\right|dy
       \le C_hT^{199/200},\qquad q^{9/10}\le T\le128q.
                                                               \tag{IN2}
\]
This is an averaged estimate, not a pointwise replacement of zeta. The negative tail follows from evenness. Its source proof uses the short-interval mean-square-error estimate of Ivić (2009, equation (2.1) and the immediately following statement for \(E\)); that primary statement was checked, but (IN2) remains the supplied convolution estimate.

The consolidation supplies fixed positive constants \(c_-,c_+\) such that, after enlarging the fixed-packet threshold,
\[
 c_-k^{-1/2}(1+y^2)^{-M_*}
 \le \frac{\omega_k(y)}{\sigma(y)}\le c_+k^{p+1},
 \quad M_*=21+4m_0,\quad p=8m_0-\tfrac92.                \tag{IN3}
\]
Indeed it proves these bounds for the residual factor \(\psi_k\) in
\(\mathfrak M^{-k}m_k=\psi_ke^{-W_k}\sigma\). Outside \(C_k\), \(W_k=0\); inside, \(\omega_k/\sigma=1\). Thus its constants may be enlarged to cover \(\omega_k\). This is the polynomial comparison for the outer-only density. It would be incorrect to apply it to the unsplit central suppression.

The final analytic input is the uniform relation free-energy estimate (18) in the value note. For \(n=q,q+1\), define
\[
 D_{k,n}(t)=\det\operatorname{Gram}_{(1+y^2)^{qt}\sigma}
                  (Q_k,yQ_k,\ldots,y^{n-1}Q_k).
\]
Its stated estimate and convex-secant consequence give, for each fixed integer \(j\ge1\),
\[
 \log\frac{D_{k,n}(-j/q)}{D_{k,n}(0)}
   =-2jn\log q-jq\mathcal L(2,\pi)+O_{h,j}(\sqrt{q\log q}).
                                                               \tag{IN4}
\]
The use at \(j=d-1,d,d+1\) changes only this auxiliary comparison exponent. It does not change \(m_0\), \(\chi_k\), or the arithmetic source. The source's uniform estimate is on a fixed neighborhood of \(t=0\), so it covers all these three fixed values of \(j\).

No use is made of the old coarse allowance for discarding \((\log|y|+c_\zeta)/(\log q+c_\zeta)\). That is exactly the factor evaluated below.

## 4. Two Gamma estimates with their normalizations checked

### 4.1 Complex evaluation and a fixed Taylor kernel

The original monic polynomials and squared norms are
\[
 \sum_{n\ge0}\frac{p_n(z)}{n!}t^n
    =(1+t^2)^{-1/4}e^{z\arctan t},\qquad
 \gamma_n=M_\sigma n!(1/2)_n.
                                                               \tag{ST6}
\]
This is the original specialization of the Meixner–Pollaczek generating function (NIST DLMF, §18.23.7), not a rescaled source convention.

For \(D\ge1\), use the Cauchy circle \(\rho=D/(D+1)\). The estimates
\[
 \rho^{-n}\le e\ (n\le D),\quad
 |\arctan t|\le\tfrac12\log(2D+1),\quad
 |1+t^2|^{-1/4}\le(1-\rho^2)^{-1/4},
\]
combined with \(n!/(1/2)_n\le2n+1\), imply
\[
 K_D^\sigma(z,\bar z)
 \le \frac{e^2}{M_\sigma}(D+1)^2\sqrt{2D+1}\,(2D+1)^{|z|}.
                                                               \tag{ST7}
\]
The ratio bound follows from the central binomial coefficient being at least the average of the \(2n+1\) binomial coefficients in that row.

If \(P\in y^r\mathcal P_{D-r}\), the maximum principle applied to \(P(z)/z^r\) on the radius-\(2T\) disk gives
\[
 \int_{-T}^T|P(y)|^2\sigma(y)dy
 \le \zeta_{D,T,r}\|P\|_\sigma^2,
\]
\[
 \boxed{\zeta_{D,T,r}
   =e^2(D+1)^2\sqrt{2D+1}\,(2D+1)^{2T}4^{-r}.}          \tag{ST8}
\]
The whole central mass, not a pointwise value at zero, is bounded. The coefficient factor \(M_\sigma\) from its integration cancels the reciprocal mass in (ST7).

### 4.2 A real-line diagonal bound from the actual Poisson kernel

Let \(\lambda=1/4\), \(x=y/2\), and let \(p_n^{(\lambda)}(x;\pi/2)\) be normalized in the measure
\[
 d\mu_\lambda(x)=\frac{2^{2\lambda}}{2\pi}
                   |\Gamma(\lambda+ix)|^2dx.
\]
Koelink and Van der Jeugt (1997, Proposition 2.1, equations (2.8)–(2.9)) give, for \(0<t<1\),
\[
 v_t(x,x)=\frac{(1+t)^{2ix}(1-t)^{-2\lambda-2ix}}{\Gamma(2\lambda)}
 {}_2F_1\left(\lambda+ix,\lambda+ix;2\lambda;
                     -\frac{4t}{(1-t)^2}\right).
\]
Since the density transforms under \(y=2x\),
\[
 \sum_{n\ge0}t^n\frac{p_n(y)^2\sigma(y)}{\gamma_n}
                   =\tfrac12\mu_\lambda'(x)v_t(x,x).
                                                               \tag{ST9}
\]
Euler's integral for \({}_2F_1\) cancels the factor
\(|\Gamma(\lambda+ix)|^2\) exactly. On putting
\(R=4t/(1-t)^2\), taking absolute values leaves
\[
 \frac{2^{-3/2}}{\pi}(1-t)^{-1/2}
 \int_0^1s^{-3/4}(1-s)^{-3/4}(1+Rs)^{-1/4}ds.
\]
For \(R\ge8\), split at \(1/R\) and \(1/2\). The three integrals are at most
\(8R^{-1/4}\), \(2R^{-1/4}\log R\), and \(8R^{-1/4}\), respectively. Hence (ST9) is at most
\[
 \frac{16+2\log R}{4\pi t^{1/4}}.
\]
Choose \(t=D/(D+1)\). All summands in (ST9) are nonnegative and \(t^{-D}\le e\), so
\[
 \boxed{K_D^\sigma(y,y)\sigma(y)
 \le \frac{e\,2^{1/4}}{4\pi}
       [16+2\log(4D(D+1))]
 \le20\log(D+2),\qquad D\ge1.}                         \tag{ST10}
\]
Thus the bound used in the transport has been checked with the original Jacobian and mass. It is not obtained by substituting a fixed-\(y\) oscillatory asymptotic at growing \(y\).

The orthonormal recurrence also gives
\[
 \|yP\|_\sigma\le2(D+1)\|P\|_\sigma\qquad(\deg P\le D).
                                                               \tag{ST11}
\]
Iteration bounds polynomially weighted tails outside \(128q\), for degrees at most \(2q\), by a polynomial in \(q\) times \(256^{-q}\). In detail, for a fixed integer \(J\ge0\) and \(q\ge J+1\),
\[
 \int_{|y|>128q}(1+y^2)^J|P(y)|^2\sigma(y)dy
 \le128^J q^{2J}256^{-q}\|P\|_\sigma^2,
 \qquad\deg P\le2q.                                   \tag{ST12}
\]
For \(J=0\) this follows by inserting \((|y|/(128q))^{2q}\). For general \(J\), use \((1+y^2)^J\le2^J|y|^{2J}\) there and apply (ST11) \(q+J\) times, bounding each multiplication factor by \(8q\). Every tail integral is retained in this inequality.

## 5. The logarithmic factor is a small real change of exponent

For real \(a\ge0\), define the auxiliary measure
\[
 \tau_a(y)=(1+y^2)^{-a}\sigma(y).
\]
Set
\[
 L=\log q,\quad L_c=L+c_\zeta,\quad
 \epsilon_q=\frac1{2L_c},\quad a_q=d-\epsilon_q,
\]
\[
 A_q=\frac{kL_c}{\sqrt\pi\mathfrak M}\,q^{-1/L_c},\qquad
 T_q=\frac q{L^6},\quad B_q=128q,\quad
 \mathfrak A_q=\{T_q\le|y|\le B_q\}.
                                                               \tag{ST13}
\]
All subsequent uses impose the explicit eventual guards
\[
 L_c\ge L/2>0,\quad \epsilon_q\le1/2,\quad
 T_q\ge\max\{q^{9/10},kb,1\},\quad
 \frac{6\log L+\log128}{L_c}\le\frac12.
                                                               \tag{ST14}
\]
They hold on the original fixed-packet sequence. No packet or period is moved as \(k\) changes.

For \(y\in\mathfrak A_q\), let \(x=\log(|y|/q)\). The slow-factor ratio is exactly
\[
 s_q(y)=
 \frac{\frac{k}{\sqrt\pi\mathfrak M}(\log|y|+c_\zeta)\tau_d(y)}
      {A_q\tau_{a_q}(y)}
 =\left(1+\frac{x}{L_c}\right)
    \exp\left[-\frac{x}{L_c}
        -\frac{\log(1+y^{-2})}{2L_c}\right].             \tag{ST15}
\]
Consequently,
\[
 -\eta_q\le\log s_q(y)\le0,
 \quad \eta_q=\frac{(6\log L+\log128)^2}{L_c^2}
                   +\frac1{2L_cT_q^2}
       =O\left(\frac{(1+\log L)^2}{L^2}\right).         \tag{ST16}
\]
Here \(|\log(1+z)-z|\le z^2\) for \(|z|\le1/2\). Extend \(s_q=1\) outside \(\mathfrak A_q\), and put \(\nu_q=s_q\tau_{a_q}\). Then the full forms, including every affine minimum, satisfy
\[
 e^{-\eta_q}\tau_{a_q}\preceq\nu_q\preceq\tau_{a_q}.
                                                               \tag{ST17}
\]
For a polynomial subspace of dimension \(n\), its logdet error is therefore at most \(n\eta_q\). Charging this uniform error by dimension, rather than by an additional diagonal-kernel bound, is essential to the finer scale.

## 6. Transport the averaged arithmetic error through the full determinants

### 6.1 Polynomial comparisons and one common subspace

Let \(\mu_q=\omega_k/A_q\), and let \(\mu_q^{\rm cut}\) equal \(\mu_q\) on \(\mathfrak A_q\) and \(\tau_{a_q}\) outside it. This is only an explicitly estimated intermediate density.

The pointwise envelope (IN3), Jensen's inequality, and (ST11) imply polynomial norm comparisons on all polynomials of degree at most \(2q\), simultaneously for
\(\mu_q,\mu_q^{\rm cut},\nu_q,\tau_{a_q}\): there is a fixed integer \(B=B_h\) and an eventual threshold such that
\[
 q^{-B}\|P\|_\sigma^2\le\|P\|_\xi^2\le q^B\|P\|_\sigma^2.
                                                               \tag{ST18}
\]
For clarity, the lower bound follows from
\[
 \int(1+y^2)^{-M}|P|^2\sigma\ge
 [1+4(2q+1)^2]^{-M}\|P\|_\sigma^2
\]
for each fixed \(M\ge0\), obtained by Jensen under
\(|P|^2\sigma/\|P\|_\sigma^2\). The upper bounds are immediate from (IN3) and the bounded deterministic ratio, together with the fact that \(A_q\) and its reciprocal are bounded by fixed powers of \(q\). Constants are absorbed by enlarging the threshold, not by changing a measure. One may take, for example,
\(B=2M_*+\lceil p\rceil+2d+20\), after imposing the corresponding inequalities on the fixed envelope constants and \(A_q\). Increasing this fixed integer also bounds the pointwise arithmetic ratio on \(\mathfrak A_q\) between \(q^{-B}\) and \(q^B\).

Take \(D=2q\), and choose
\[
 r_q=\left\lceil
 \frac{\log\{e^2(D+1)^2\sqrt{2D+1}(2D+1)^{2T_q}\}
       +(4B+4d+60)L}{\log4}\right\rceil.
                                                               \tag{ST19}
\]
Then
\[
 \zeta_{D,T_q,r_q}\le q^{-(4B+4d+60)},\quad
 r_q=O_h(T_qL+L)=O_h(q/L^5).
\]
Also require \(r_q+d\le q\), an eventual guard. For any one of the actual source or relation subspaces \(\mathcal S\subset\mathcal P_{2q}\), set
\[
 \mathcal S^\circ=\mathcal S\cap
             (y+i)^d y^{r_q}\mathbb C[y].
\]
Its codimension in \(\mathcal S\) is at most \(r_q+d\). This construction imposes fixed linear polynomial conditions before changing any metric. The original relation subspace still contains its entire factor \(Q_k\); that factor is not replaced.

On \(\mathcal S^\circ\), write \(P=(y+i)^dR\). Then \(R\) is a polynomial divisible by \(y^{r_q}\), and
\[
 \|P\|_{\tau_{a_q}}^2
     =\int |R|^2(1+y^2)^{\epsilon_q}\sigma(y)dy.
                                                               \tag{ST20}
\]
This is an exact isometry on the indicated image, not an assertion that polynomial division acts on every original polynomial.

### 6.2 The inner region and the remote tail

On \(|y|<T_q\), the complete difference of the two densities in
\(\|P\|_{\mu_q}^2-\|P\|_{\mu_q^{\rm cut}}^2\), after (ST20), is bounded above in absolute value by a fixed power of \(q\) times \(|R|^2\sigma\). Equation (ST8) and the choice (ST19) pay that power. On \(|y|>128q\), (IN3), (ST20), and (ST12), with a fixed exponent at most \(d+1\), give a polynomial in \(q\) times \(256^{-q}\).

The lower norm comparison (ST18) pays the relative denominator. Therefore, after a further explicit eventual guard on that exponentially decreasing tail,
\[
 (1-q^{-20})G_{\mathcal S^\circ}[\mu_q^{\rm cut}]
 \preceq G_{\mathcal S^\circ}[\mu_q]
 \preceq(1+q^{-20})G_{\mathcal S^\circ}[\mu_q^{\rm cut}].
                                                               \tag{ST21}
\]
The corresponding logdet error is at most \(4q^{-19}\).

Factor both full Grams through the exact sequence
\[
 0\longrightarrow\mathcal S^\circ\longrightarrow\mathcal S
       \longrightarrow\mathcal S/\mathcal S^\circ\longrightarrow0.
                                                               \tag{ST22}
\]
The quotient carries its full Schur minimum. Applying (ST18) to every representative of the same quotient value bounds its logdet change by
\(2B(r_q+d)L\). The fixed coordinate determinant in this factorization is identical at the two measures and cancels. Thus the whole inner region has a retained error
\[
 O_h((r_q+d)L)=O_h(q/L^4),                              \tag{ST23}
\]
not zero. All cross Grams are included through (ST22).

### 6.3 Exceptional arithmetic intervals in the actual minima

On \(\mathfrak A_q\) define
\[
 a_k(y)=
 \frac{\omega_k(y)}{
   \frac{k}{\sqrt\pi\mathfrak M}(\log|y|+c_\zeta)\tau_d(y)},
\]
and put \(a_k=1\) off that annulus. Then exactly
\(\mu_q^{\rm cut}=a_k\nu_q\). Summing (IN2) over dyadic intervals, and using evenness, gives
\[
 E_q:=\int_{\mathfrak A_q}|a_k-1|dy\le C_hq^{199/200}.
                                                               \tag{ST24}
\]
There is no extra logarithmic number of intervals: their lengths to the power \(199/200\) form a geometric sum.

The pointwise polynomial lower and upper envelopes give
\(|\log a_k|\le BL\) on the annulus after increasing \(B\). On the set \(|a_k-1|\le1/2\), use \(|\log a_k|\le2|a_k-1|\). The complementary set has measure at most \(2E_q\). Consequently
\[
 \int_{\mathfrak A_q}|\log a_k|dy\le(2+2BL)E_q.         \tag{ST25}
\]
Small-density intervals have therefore been bounded rather than removed.

Under the isometry (ST20), the reference on the image polynomial subspace is
\[
 d\lambda_q=s_q(y)(1+y^2)^{\epsilon_q}\sigma(y)dy.
\]
It is at least \(e^{-\eta_q}\sigma\) on the whole line; on the annulus its ratio to \(\sigma\) is bounded above by an absolute constant under (ST14). The variational evaluation-kernel inequality and (ST10) therefore give
\[
 K_{\mathcal S^\circ}^{\nu_q}(y,y)\nu_q(y)\le C L,
                         \qquad y\in\mathfrak A_q.    \tag{ST26}
\]
The expression denotes the density-weighted kernel. The factors \(|y+i|^{2d}\) in the kernel and the measure are precisely those of (ST20).

For any finite-dimensional polynomial subspace \(V\), in a frame orthonormal for \(\nu\), the exact inequalities are
\[
 \int\log a\,K_V^\nu d\nu
 \le\log\frac{\det G_V[a\nu]}{\det G_V[\nu]}
 \le\int(a-1)K_V^\nu d\nu.                            \tag{ST27}
\]
The lower inequality is Jensen applied to the complete squared-determinant integral for the Gram determinant. The upper inequality is
\(\log\det A\le\operatorname{Tr}(A-I)\). Neither replaces a full Gram by its diagonal determinant.

Applying (ST24)–(ST27) to \(\mathcal S^\circ\) yields
\[
 \left|\log\frac{\det G_{\mathcal S^\circ}[\mu_q^{\rm cut}]}
                         {\det G_{\mathcal S^\circ}[\nu_q]}\right|
          \le C_h q^{199/200}L^2.                     \tag{ST28}
\]
The same quotient in (ST22) contributes at most another
\(2B(r_q+d)L\), by (ST18).

### 6.4 Reassemble all eight original spaces

Finally, (ST17) gives
\[
 \left|\log\frac{\det G_\mathcal S[\nu_q]}
                         {\det G_\mathcal S[\tau_{a_q}]}\right|
        \le(2q+1)\eta_q.
\]
Combining this with (ST21)–(ST28), and then using (ST3) at all four endpoints, proves
\[
 \boxed{\mathcal B_k[\omega_k]-\mathcal B_k[\tau_{a_q}]
 =O_h\left(
      \frac{q(1+\log L)^2}{L^2}
          +q^{199/200}L^2+\frac q{L^4}\right).}         \tag{ST29}
\]
The scalar \(A_q\) cancels by (ST4) only after the source/relation and four-endpoint accounting. Every term in (ST29) is \(o_h(q/L)\).

## 7. Evaluate the moving rational exponent without differentiating an error

### 7.1 Integer source exponents

For each fixed integer \(j\ge1\), the monic frame
\[
 1,y,\ldots,y^{j-1},\ (y+i)^j,y(y+i)^j,\ldots,y^{N-j}(y+i)^j
\]
has coefficient determinant one. Its last block in \(\tau_j\) is exactly the Gamma Gram through degree \(N-j\). The remaining block is the attained jet quotient of rank \(j\). Its logdet is \(O_j(\log(N+2))\): an upper bound uses the fixed low-degree representatives; a lower bound follows by bounding the \(j\) evaluation derivatives at \(-i\) using (ST7), a fixed Cauchy circle, and
\[
 \|P\|_\sigma^2\le[1+4(N+1)^2]^j\|P\|_{\tau_j}^2.
\]
The jet map on the fixed low-degree representative frame is a fixed invertible matrix. Hence its full minimum eigenvalues are bounded above and below by fixed powers of \(N+2\).

This proves
\[
 \log\det H_N[\tau_j]
       =\sum_{n=0}^{N-j}\log\gamma_n+O_j(\log(N+2)),
\]
\[
 f_N(j):=\log\frac{\det H_N[\tau_j]}{\det H_N[\sigma]}
       =-j\log\gamma_N+O_j(\log(N+2)),                 \tag{ST30}
\]
where \(\gamma_N=\sqrt{2\pi}(2N)!/4^N\). The last equality uses only a fixed number of consecutive norm ratios, each with logarithm \(O(\log N)\).

### 7.2 Convex secants on the actual positive determinant

For every fixed polynomial subspace \(V\),
\[
 f_V(a)=\log\det G_V[(1+y^2)^{-a}\sigma]
\]
is convex in real \(a\). Indeed the full Gram determinant is an integral of
\(\exp[-a\sum_i\log(1+y_i^2)]\) against a nonnegative squared-determinant density; its second logarithmic derivative is a variance. All integrals exist for bounded \(a\) because of the Gamma decay.

For a convex function \(f\), integer \(d\), and \(0\le\epsilon\le1\),
\[
 -\epsilon[f(d+1)-f(d)]\le f(d-\epsilon)-f(d)
                  \le-\epsilon[f(d)-f(d-1)].           \tag{ST31}
\]
Therefore, if the three integer values are \(j\ell+O(E)\), the middle moving value is
\((d-\epsilon)\ell+O(E)\), with a constant uniform in \(\epsilon\). The sharper increment error is \(O(\epsilon E)\).

Apply this before taking any signed combination. Equations (ST30) and (ST31) give, uniformly for \(a=d-\epsilon\), \(0\le\epsilon\le1/2\),
\[
 f_N(a)=-a\log\gamma_N+O_h(\log q),
              \qquad N\in\{q-1,q,2q-1,2q\}.           \tag{ST32}
\]
The same argument applied to the full relation determinants and (IN4) gives, for \(n=q,q+1\),
\[
 f_{k,n}^{\rm rel}(a)
  =-2anL-aq\mathcal L(2,\pi)+O_h(\sqrt{qL}).           \tag{ST33}
\]
The low rank-one relation has logarithmic comparison \(O_h(L)\), directly from Jensen and (ST11); the empty relation contributes zero. The signed return itself is not assumed convex.

### 7.3 Cancellation at the original endpoints

Stirling's formula in (ST32), keeping its \(O(\log q)\) endpoint remainder, gives the full source contribution
\[
 4aq\log q+(8a\log2-4a)q+O_h(\log q).
\]
The relation contribution, with its subtraction in (ST3) and the original four signs, is
\[
 -4aq\log q-2aq\mathcal L(2,\pi)+O_h(\sqrt{q\log q}).
\]
Thus uniformly in the indicated interval of auxiliary exponents,
\[
 \boxed{\mathcal B_k[\tau_a]-\mathcal B_k[\sigma]
       =-a\mathcal C_\Gamma q+O_h(\sqrt{q\log q}).}     \tag{ST34}
\]
At \(a=a_q=d-1/(2L_c)\),
\[
 \mathcal B_k[\tau_{a_q}]-\mathcal B_k[\sigma]
 =-d\mathcal C_\Gamma q+\frac{\mathcal C_\Gamma q}{2(L+c_\zeta)}
          +O_h(\sqrt{qL}).                            \tag{ST35}
\]
The exact known constant \(c_\zeta\) has been retained. Replacing its denominator by \(L\) now costs \(O_h(q/L^2)\); no coefficient at that still-finer scale is assigned.

## 8. Combine, extract the coefficient, and classify the scalar sign

Substitute (ST29) and (ST35) into (ST5), and then use (IN1). This proves (ST2) and (ST1). For example, after dividing their remainders by \(q/L\), the potentially slow terms are
\[
 \frac{(1+\log L)^2}{L},\qquad q^{-1/200}L^3,\qquad
 \frac{k^2}{qL^2},\qquad\frac{kL^3}{q},\qquad
 \frac{L^{3/2}}{\sqrt q},
\]
all tending to zero because \(q\ge(k+1)^2\) and \(\log q=O_{m_0}(\log k)\). This is an asymptotic statement on fixed-packet domains; the slow power-saving term is not asserted numerically small at practical degrees.

The previously evaluated coefficient is
\[
 d_0(h)=\begin{cases}-2\mathcal C_\Gamma+c_*I_h,&m_0=1,\\
                 -(4m_0-2)\mathcal C_\Gamma,&m_0\ge2.
          \end{cases}
\]
On the simple stratum \(q-k^2=2k+1=o(q/L)\). On every fixed higher stratum \(k^2=o(q/L)\). Therefore
\[
 \boxed{\lim_{k\to\infty}\frac{\log q}{q}
           [\delta_{k,1}^{\rm ar}-q\,d_0(h)]
          =\frac{\mathcal C_\Gamma}{2}>0.}             \tag{ST36}
\]
In units of \(q/\log k\), the coefficients are
\[
 \boxed{\lim_{k\to\infty}\frac{\log k}{q}
           [\delta_{k,1}^{\rm ar}-q\,d_0(h)]
 =\begin{cases}\mathcal C_\Gamma/4,&m_0=1,\\
                \mathcal C_\Gamma/6,&m_0\ge2.
   \end{cases}}                                       \tag{ST37}
\]
The difference between the two cases comes from the actual dimension, not from a different tail coefficient.

For a simple packet at the cancellation value
\[
 I_h=\frac{2\pi\mathcal C_\Gamma}{\log2},
\]
(ST36) resolves the formerly undecided scalar sign:
\[
 \delta_{k,1}^{\rm ar}\sim\frac{\mathcal C_\Gamma}{2}\frac q{\log q}>0.
                                                               \tag{ST38}
\]
Together with the leading coefficient, this gives the eventual scalar sign classification: negative for fixed \(m_0\ge2\); for \(m_0=1\), negative below the displayed threshold and positive at or above it. It is a classification in the actual fixed-source integral \(I_h\), not a numerical computation of an unspecified xi packet.

The former \(O(q\log\log q/\log q)\) slow-factor allowance is thus replaced by an evaluated \(+\mathcal C_\Gamma q/(2\log q)\) term and a smaller remainder. In particular a term of size \(q\log\log q/\log q\) is excluded in this scalar remainder after subtracting its already evaluated leading pieces.

## 9. Exact return to the programme

The unchanged receiver is
\[
 J_k=\mathcal B_k[\sigma]+\delta_{k,1}^{\rm ar}
       +W_k^{\rm mono}-P_{k,-}-P_{k,+}.
\]
The substitution is exactly
\[
 \begin{split}
 J_k={}&\mathcal B_k[\sigma]-d\mathcal C_\Gamma q+c_*I_hk^2
      +\frac{\mathcal C_\Gamma q}{2\log q}\\
     &+W_k^{\rm mono}-P_{k,-}-P_{k,+}+R_{h,k},
 \end{split}                                                   \tag{ST39}
\]
where \(R_{h,k}\) has the bound (ST2). This does not assign a \(q/\log q\) coefficient to the complete action while its independent native part still has an \(O_h(q)\) remainder. On the previously treated simple-quartet action lane, its positive \(C_Bq^2\) contribution is unchanged. Nor does it evaluate the native angular flags or substitute a degree-\(k+4\) metric for the proper degree-\(k\) source.

## References and source register

Ivić, A. (2009). On the mean square of the Riemann zeta-function in short intervals. *Publications de l'Institut Mathématique, 85*(99), 1–17. arXiv:0803.0132. Equation (2.1) and its stated \(E(x+U)-E(x)\) counterpart were checked directly.

Koelink, H. T., & Van der Jeugt, J. (1997). *Bilinear generating functions for orthogonal polynomials* (Report 97-03). Universiteit van Amsterdam. arXiv:q-alg/9704016. Proposition 2.1 supplies the Poisson formula; the bound (ST10) above includes its independent normalization and integral estimate.

National Institute of Standards and Technology. (n.d.). *Digital Library of Mathematical Functions*. Sections 15.6.1 and 18.23.7. Euler's hypergeometric integral and the Meixner–Pollaczek generating function.

Split-Zero programme. (2026, September 18). *Evaluated signed arithmetic–Gamma correction* [Supplied research note; original file `Pasted markdown(20260918-223501).md`]. Equations (13), (18)–(19), and (30) are the specific analytic dependencies; equations (14)–(15) and the fixed-integer source step are rederived here as needed.

Split-Zero programme. (2026, September 18). *Consolidation and localization* [Supplied continuation preserved in `Pasted text (2)(20260918-232526).txt`]. The whole-line residual-factor and outer-only bounds are equations (13), (18)–(19) of that continuation. The new source is not inferred from missing text.

Split-Zero programme. (2026, September 19). *Marked arithmetic integration* [Preceding additive package]. Its mathematical state and analytic-input qualifications are retained. The exact preceding ZIP is included unchanged in this package.

Finite diagnostics in the accompanying script test normalization, the slow-factor identity, the error scales, convex secants, the original signed source coefficients, and complete Schur/mass accounting. They do not constitute numerical xi-packet data or independent certification of (IN1), (IN2), or (IN4).
