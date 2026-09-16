# Uniform exponential suppression of the original adjacent ratios

16 September 2026. Written proof contribution requiring independent review. No new Lean certificate, actual off-critical zero example, or RH conclusion is asserted.

## Source and review

Base main: `1efd53337561d8f67cf0ac1d119acdaa222644c3`. AMT1--6 were directly reread in `workbenches/splitzero-tandem/continuations/20260915-primitive-band-continuation/13_ARITHMETIC_MIXED_TRANSFER.tex`, blob `b6cfec2ac9517acc378aa02686ada6e7923ef381`.

The user supplied the complete 540-line `Pasted markdown (2)(8).md`: grouped-convolution recurrence, contraction penalties, and the exact full-action cancellation. Its recurrence proof checks out on the stated AMT inputs. Fixed arithmetic blocks 3,4,5 have a degree-linear multiplication bound; their tensor product is compressed at TOTAL degree N+1, retaining the full output face. This proves the stated bound `omega_(N+1)/omega_N <= C_mult(h)^2 (2N+floor(k/3))^2`, and the exterior benchmark gives its polynomial penalty bound O_h(1+k(m-1)). The original 4q-1 penalty coefficient count is correct. Only the prose needs clarification: d_n tends to zero; 1-d_n is close to one.

The other new transcript announces an exponential full-band candidate but contains no complete quantile proof. The argument below bypasses that unfinished proof. It requires only a lower bound for the actual relation minimum, not a sharp minimum asymptotic. The EOR source-order theorem is not an input to this continuation.

## 1. Actual source and original relation norm

Fix the complete stipulated quartet h, its multiplicity m, and amplitude v_h=2xi/h. Retain

\[
e_k=1+k(m-1),\quad q=e_k(k+1)^2,\quad c=k/2,\quad R_k=k\sqrt{\delta^2+\gamma^2},\quad\alpha=\pi/2.
\]

Every centered root of the original monic degree-q polynomial chi has modulus at most R_k. Its full multiplicities remain. Write mu_k=w_h^{*k}. AMT gives

\[
\mu_k(y)\ge\ell_{h,k}e^{-\alpha|y|}(k-2+|y|)^{-B_h},\qquad \mu_k\le A_k\sigma,
\]
\[
B_h=42+8m,\quad \ell_{h,k}=c_h\vartheta_h^{k-3}e^{-\alpha(k-3)},\quad
A_k=(C_h^{\rm tilt}/c_\Gamma)k^{p+1}M_\alpha^{k-1},\quad p=8m-9/2.
\]

All constants are the original fixed-h constants in AMT4; no source mass is normalized away. The Gamma monic norm is

\[
g_n=\sqrt{2\pi}\,n!(1/2)_n=\sqrt{2\pi}(2n)!/4^n.
\]

Let omega_n be the original arithmetic monic norm and define

\[
h_r^\chi=\inf_{P\ {m monic},\deg P=r}\int|\chi(c+iy)P(c+iy)|^2\mu_k(y)\,dy.
\]

The original source/relation determinant factorization gives

\[
\boxed{d_n:=V_n/V_{n-1}=\omega_n/h_{n-q}^\chi\quad(n\ge q).}\tag{1}
\]

Proof: V_N is the source Hankel determinant at N+1 divided by the relation Hankel determinant at N-q+1. Taking the adjacent ratio yields (1). The denominator is the norm of an original relation BEFORE its quotient value becomes represented zero. No G_(q-2) occurs. The substitution Q(y)=i^{-r}P(c+iy) is monic in y and preserves absolute values, so the following polynomial estimate uses the original coordinate through an explicit isometry, not a new arithmetic quotient.

## 2. A two-band lower bound for every monic direction

Take q>=1, 0<=r<=q, n=q+r, and set

\[
a=20n/63,\quad b=40n/21,\quad E_n=[-b,-a]\cup[a,b],\quad
 d\nu_n(y)=\frac{|y|\,dy}{\pi\sqrt{(y^2-a^2)(b^2-y^2)}}.
\]

This is a probability measure; y squared pushes it to the arcsine law on [a^2,b^2], with equal mass on the two half-lines. For a monic complex polynomial Q of degree r,

\[
\int\log|Q|\,d\nu_n\ge r\log\frac{\sqrt{b^2-a^2}}2.\tag{2}
\]

For each root z, symmetry turns its logarithmic integral into one half the arcsine integral of log|z^2-x|. On an interval with midpoint C and half-width D, factoring the quadratic in exp(i theta) and applying the circle Jensen formula gives log(D/2) plus nonnegative log-max root terms. Hence this integral is at least log((b^2-a^2)/4); summing proves (2). Roots on the bands are handled by logarithmic integrability or a limit.

The same arcsine substitution gives exactly

\[
\int\log|y|\,d\nu_n=\log((a+b)/2),\qquad
\int\log(d\nu_n/dy)\,d\nu_n=\log\frac2{\pi(b-a)}.\tag{3}
\]

For the entropy formula use that each of the expectations of log(x-a^2), log(b^2-x) equals log((b^2-a^2)/4).

Let

\[
E_0=\int_0^{\pi/2}\sqrt{\sin^2t+\tfrac1{36}\cos^2t}\,dt.
\]

Then int |y| dnu_n=2b E_0/pi. Here E_0<21/20 has an elementary proof. Put rho=1/6 and t0=arcsin rho. On [0,t0], the integrand minus sin t is at most rho cos t, whose integral is rho squared. On [t0,pi/2], rationalization bounds the difference by rho squared cos squared t/(2 sin t). Therefore

\[
E_0-1\le\frac1{36}+\frac1{72}[\log(6+\sqrt{35})-\sqrt{35}/6]<\frac1{20}.
\]

The last inequality uses log12<5/2 and sqrt35/6>9/10. The first seven positive Taylor terms of exp(5/2) already exceed 12, so no numerical quadrature is needed. Consequently alpha int |y| dnu_n=b E_0<=2n.

Apply probability Jensen to f/(dnu_n/dy), where f=|Q| squared times |y|^(2q) exp(-alpha|y|). Its logarithm is integrable. Equations (2)--(3) prove

\[
\begin{aligned}
\int_{E_n}|Q(y)|^2|y|^{2q}e^{-\alpha|y|}\,dy
&\ge\frac{\pi(b-a)}2\left(\frac{b^2-a^2}{4}\right)^r
\left(\frac{a+b}{2}\right)^{2q}e^{-2n}\\
&=\frac{50\pi n}{63}n^{2n}e^{-2n}(500/567)^r(100/81)^q\\
&\ge\frac{50\pi n}{63}n^{2n}e^{-2n}e^{c_*q},\qquad
c_*:=\log(50000/45927)>0.\tag{4}
\end{aligned}
\]

The last step uses r<=q and 500/567<1. An exact rational logarithm-series certificate gives

\[
0.084969826010092<c_*<0.084969826010093.
\]

This holds for ALL monic coefficient directions, including r=0. No r/q bounded away from zero, limiting quantile construction, or compressed spectral gap is assumed.

## 3. Restore the original roots, arithmetic density and mass

Assume q>=7R_k. On E_n, q<=n<=2q, every original root gives |iy-z|>=|y|-R_k. Thus

\[
|\chi(c+iy)|\ge |y|^q(1-63R_k/(20n))^q.
\]

The factor is positive and at least 1/2. Since |y|<=2n, the ORIGINAL density lower bound and (4) imply

\[
h_{n-q}^\chi\ge\ell_{h,k}(k-2+2n)^{-B_h}
(1-63R_k/(20n))^{2q}\frac{50\pi n}{63}n^{2n}e^{-2n}e^{c_*q}.\tag{5}
\]

By the original monic upper comparison and the positive-real Stirling remainder,

\[
\omega_n\le A_kg_n\le2\pi\sqrt{2n}A_kn^{2n}e^{-2n}e^{1/(24n)}.\tag{6}
\]

Divide (6) by (5). For a uniform bound, -log(1-x)<=2x shows that the root-factor logarithmic cost is at most 63R_k/5. Define the explicit finite certificate

\[
U_{h,k}^{\rm ctr}=\frac{63\sqrt2 A_k}{25c_h\sqrt q}
\vartheta_h^{-(k-3)}(k-2+4q)^{B_h}
\exp\left(\alpha(k-3)+\frac{63}5R_k+\frac1{24q}-c_*q\right).
\]

Then

\[
\boxed{0<d_n\le U_{h,k}^{\rm ctr}\quad(q\le n\le2q).}\tag{7}
\]

It is still a true, possibly uninformative, bound when U_ctr>=1. At fixed actual h and full multiplicity,

\[
\log U_{h,k}^{\rm ctr}=-c_*q+O_h(k+\log q).
\]

All original masses, the full amplitude, convolution order and primary multiplicities are retained. The reference bands are only integration subsets. No quotient was replaced by the monomial quotient. The period observation is not needed for this bound.

## 4. The penalties are exponentially small

Keep exactly the original endpoint multiplicities:

\[
P_-=-\log(1-d_{2q-1})-2\sum_{n=q}^{2q-2}\log(1-d_n),
\]
\[
P_+=-\log(1-d_q)-\log(1-d_{2q})-2\sum_{n=q+1}^{2q-1}\log(1-d_n).
\]

Their combined coefficient count is 4q-1. If U_ctr<1,

\[
\boxed{0\le P_-+P_+\le-(4q-1)\log(1-U_{h,k}^{\rm ctr})
\le\frac{(4q-1)U_{h,k}^{\rm ctr}}{1-U_{h,k}^{\rm ctr}}.}\tag{8}
\]

Hence P_-+P_+=O_h(q exp(-c_*q/2)), improving the submitted O_h(e_k). For finite use intersect (8) with the submitted polynomial allowance; retain the older bound where either new guard fails.

The complete exact receiver remains

\[
J_k^{\rm action}=\mathcal B_k^{\rm ar}+\mathcal W_k^{\rm ar}-P_--P_+.
\]

Thus J_action=B_ar+W_ar plus a nonpositive exponentially small error. The separate monic-window comparison W_sigma-E_hi<=W_ar<=W_sigma+E_lo still has error O_h(k+log q); that error has NOT become exponentially small.

The submission's exact Gamma window and finite enclosure check out:

\[
W_q^\sigma=2\log\frac{(4q)!}{(2q)!}-4q\log2+\log\frac{2q-1}{2(4q-1)},
\]
\[
C(q)-\log2-\left(\frac1{16q}+\frac1{4q-2}\right)\le W_q^\sigma\le C(q)-\log2,
\quad C(q)=4q\log q+(8\log2-4)q.
\]

The new action enclosure replaces the old penalty allowance by the minimum of the old bound and (8). It does not evaluate a further coefficient of B_ar or of a separate allocation.

## 5. This also controls the minimum, not only the action mean

At the original untilted source, total parity gives

\[
\epsilon_{q-1}^2=b_q(1-d_q)/d_q,\qquad
\epsilon_N^2=b_{N+1}(1-d_N)(1-d_{N+1})/d_{N+1}\quad(N\ge q),
\]

where b_n=omega_n/omega_(n-1). This is total parity, not an assertion that the mixed kernel and boundary pairings vanish separately.

AMT's lower monic comparison gives

\[
b_n\ge\frac{a_k}{A_kD_n}n(n-1/2),\quad
D_n=[1+4(n+21+4m)^2]^{21+4m}.
\]

Let b_low=(a_k/(A_kD_(2q)))q(q-1/2). Equation (7) proves, for U_ctr<1,

\[
\boxed{\min_{q-1\le N\le2q-1}\epsilon_N
\ge\sqrt{b_{\rm low}}\frac{1-U_{h,k}^{\rm ctr}}{\sqrt{U_{h,k}^{\rm ctr}}}.}\tag{9}
\]

The first endpoint has only one factor 1-d_q and gives at least this bound. Since log b_low=O_h(k+log q),

\[
\liminf\frac1q\log\min_{q-1\le N\le2q-1}\epsilon_N\ge c_*/2.
\]

For the original exterior benchmark L_hk=delta q(k+1)/2 on k=4l+1,

\[
\boxed{\liminf\frac1q\log\frac{\min_{q-1\le N\le2q-1}\epsilon_N}{L_{h,k}}
\ge c_*/2>0.}\tag{10}
\]

Conditional on the original arithmetic packet/source inputs, every canonical allowance in THIS window is exponentially larger than the polynomial benchmark. This is stronger than the earlier geometric-mean obstruction. It does not identify the arithmetic spectrum with the allowance, negate RH, or prove that the whole tau programme fails.

## 6. Extension to any fixed proportional window

For any fixed C>1 choose small fixed rho>0 and let

\[
H(rho)=1+rho^2+\frac{rho^2}{2}
\left[\log\frac{1+\sqrt{1-rho^2}}{rho}-\sqrt{1-rho^2}\right].
\]

The preceding integral proof gives E(rho)<=H(rho). Use b=2n/H(rho), a=rho b. The exponential cost is <=2n and the two normalized factors are (1+rho)/H(rho), sqrt(1-rho^2)/H(rho). For q<=n<=Cq the gap is at least c_C(rho)q, where

\[
c_C(rho)=2\log(1+rho)+(C-1)\log(1-rho^2)-2C\log H(rho).
\]

As H(rho)-1=O(rho^2 log(1/rho)), c_C(rho)=2rho+O_C(rho^2 log(1/rho))>0 for sufficiently small rho. The band has inner radius a fixed positive constant times n, so the actual root and density costs remain O_(h,C)(k+log q). This proves the analogous exponential bound for every fixed C, and the minimum-allowance conclusion follows as above. Constants depend on C. No uniform assertion is made for C growing with k.

A mere replacement of 2q by another fixed multiple therefore does not repair this canonical small-allowance strategy. A further RH-directed estimate needs a genuinely different admitted degree scaling or another same-class comparison. The exact mixed objects remain useful, but a cancelled allocation cannot be improved while its correlated action budget is held fixed.

## Verification and scope

The local executable checker uses exact rational and Gaussian-rational arithmetic for the rate certificate, Gamma norms/orthogonality and generating ODE, all 3/4/5 partitions k=3..101, the complete top face, original quotient ratios, three actual canonical reference constructions, parity, and the weighted action product. Its reference mass is seven, not silently one. Separate 180-digit tests of monic exponential-weight minima and Gamma-window bounds are explicitly NON-INTERVAL diagnostics.

Normal and Python -O executions completed with byte-identical success records. All four false-formula controls were rejected in both modes. An initial combined shell batch timed out during the controls; the controls were subsequently rerun in separate modes and all eight expected errors recorded. No timeout is called a proof failure or a passing execution.

No new Lean run, independent second-reader approval, actual zeta packet, actual-period integral, or full cumulative-source audit is claimed. The infinite theta quotient, represented-zero/absence distinction, mixed supports, full arithmetic units and multiplicities are unchanged. The proof requires the explicit original AMT density envelopes and standard positive-real Stirling bounds. It does not assume the desired exterior upper estimate.

Primary literature: NIST Digital Library of Mathematical Functions, sections 18.23.7 and 18.19 (the Meixner--Pollaczek generating function and normalization), 5.11.1/5.11(ii) (positive-real Stirling remainder), and 19.2 (elliptic-integral conventions). The two Jensen calculations are included above; no novelty claim is made for those classical ingredients.
