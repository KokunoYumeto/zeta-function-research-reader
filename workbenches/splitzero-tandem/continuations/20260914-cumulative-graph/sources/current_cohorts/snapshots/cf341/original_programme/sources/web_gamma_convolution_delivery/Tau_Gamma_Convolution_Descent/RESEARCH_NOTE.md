---
title: "An exact gamma pushforward for the arithmetic Toda control"
subtitle: "Original split support, convolution coefficients, retained relative fibres, and certified-tail interfaces"
date: "13 September 2026"
---

# 1. Scope and the inspected collaboration state

This is a mathematical continuation of **Tau Toda Volume Control** and **Tau Exterior Trace Amplification**. It retains their arithmetic source, quotient, scaling action, full packet multiplicities, and canonical minimum-norm metric. The new calculation links those objects to the gamma reference that is already in the repository. The gamma orthogonal polynomials and their general convolution identities are classical. The contribution here is the explicit arithmetic coefficient transform, its source and quotient maps, its quantitative bounds, and the resulting exact substitution into the existing Toda/exterior estimate.

The GitHub read was pinned to main `fa4be32f87a9a90f3c02a07f7790dea95a1e7b0f`. The separate formalization was read at PR #22 head `811210d24b80813a08972ca23f919db015383137`. At that inspected revision the PR explicitly said strict verification was still in progress. No successful certificate for that revision is inferred here. Its invariant-filtration trace budget is retained as the other session's result, not presented as a new deduction of this note.

The main-branch gamma source read was `workbenches/splitzero-tandem/continuations/20260912-stieltjes/tex/theta_gamma_reference.tex`, equations TG.2--TG.14. It already constructs the exact one-factor gamma measure, its constants, its monic polynomials and its arithmetic multiplier. We extend that specified reference through the sum pushforward at every tensor degree.

There is no new RH proof or arithmetic asymptotic assertion here. Theorems below have written proofs. The checker supplies finite exact regression evidence, not analytic interval certification and not Lean execution. No inherited file or other-session branch is modified.

# 2. The original arithmetic source and its split maps

Retain

$$
G(R)=\{\tau_R\}\sqcup\{r^\bullet:r\in R\},\qquad e_R=0_R^\bullet,
$$

with the original maps

$$
\begin{array}{ccc}
G(\mathbb Z)&\xrightarrow{G(j)}&G(\mathbb C)\\
p_{\mathbb Z}\downarrow&&\downarrow p_{\mathbb C}\\
\mathbb Z&\xrightarrow{j}&\mathbb C.
\end{array}                                                    \tag{1}
$$

The target of the first quotient is infinite. Its structural base is the same absolute pointed base $\mathfrak b_\tau$. The supported scalar and the external absorber have not changed.

The source complex is

$$
C_+=[V\xrightarrow{\Theta}\mathscr B],\quad
Q=\mathscr B/\Theta V,\quad D=-x\partial_x,
$$

where $V$ consists of the original even Schwartz functions with both original moments zero, and $\mathscr B$ has the original rapid decay at both multiplicative ends with all $D$-derivatives. Keep

$$
\Theta\phi(x)=\sum_{n\ne0}\phi(nx),\qquad
 g(s)=2\xi(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
$$

Fix a nonempty finite packet $h(s)=\prod_\rho(s-\rho)^{m_\rho}$ of actual zeros, with every selected order complete. For reflection statements require the same dagger stability as the source. Write

$$
v_h=g/h,\quad \mathcal MF_h=v_h,\quad
w_h(t)=\frac{|v_h(1/2+it)|^2}{2\pi},\quad \mu_h=\int w_h(t)\,dt.       \tag{2}
$$

The cyclic tensor source and its maps remain

$$
\mathcal V_{h,k}P=P(D_1+\cdots+D_k)(F_h^{\otimes k}),\quad
C_{h,k}=\mathbb C[S]/\chi_{h,k},\quad A=M_S,
$$

$$
J^{(k)}\mathcal V_{h,k}=\eta_{h,k}\pi_\chi,\qquad
q^{(k)}\mathcal V_{h,k}=\sigma_h^{\otimes k}\eta_{h,k}\pi_\chi,          \tag{3}
$$

where $S=s_1+\cdots+s_k$ and
$\eta_{h,k}[P]=\upsilon_h^{\otimes k}P(A_k)1$, with
$\upsilon_h=j_h(g/h)$. All local units remain in this map.

At polynomial degree $N$, the original relation map is

$$
M_\chi:\mathcal P_{N-q}\longrightarrow\mathcal P_N,\quad P\mapsto\chi P,
\qquad q=\deg\chi,                                                   \tag{4}
$$

and its image under $\mathcal V_{h,k}$ consists of the already constructed theta boundaries. Every norm construction below concerns this same map and its quotient. Its squared-norm weight $|\chi|^2$ does not mean that the next conormal ideal is $(\chi^2)$: that ideal remains the exact pullback of the original $I^r$.

For $h=1$, the analytic source (2) still exists, but the finite arithmetic quotient is the zero module. Its split lift has $e$ and $\tau$. No nonzero packet or Gram inverse is inferred from that analytic branch.

# 3. Carry the repository's gamma reference through every tensor power

For a fixed real $\lambda>0$ define exactly

$$
r_\lambda(t)=\frac{|\Gamma(\lambda+it/2)|^2}{2\pi},\qquad
 d\sigma_\lambda(t)=r_\lambda(t)dt,\qquad
 c_\lambda=2^{1-2\lambda}\Gamma(2\lambda).                           \tag{5}
$$

The repository proves, by the beta integral and Fourier inversion,

$$
\int e^{iyt}d\sigma_\lambda(t)=c_\lambda(\cosh y)^{-2\lambda}.
                                                                    \tag{6}
$$

Its factor $2$ comes from $t=2u$ in the beta integral. Thus $c_\lambda$, rather than $1$, is the mass. Fourier uniqueness for finite measures gives the all-tensor identity

$$
\boxed{
 r_{\lambda,k}:=r_\lambda^{*k}
 =\kappa_{\lambda,k}r_{k\lambda},\qquad
 \kappa_{\lambda,k}=\frac{c_\lambda^k}{c_{k\lambda}}
 =2^{k-1}\frac{\Gamma(2\lambda)^k}{\Gamma(2k\lambda)}.
}                                                                   \tag{7}
$$

In particular the mass of the sum measure is $c_\lambda^k$.
For $\lambda=1/4$ this reads

$$
\boxed{
 r_{1/4,k}(u)=
 \frac{2^{k-1}\pi^{k/2}}{\Gamma(k/2)}
 \frac{|\Gamma(k/4+iu/2)|^2}{2\pi},\qquad
 \int r_{1/4,k}=(2\pi)^{k/2}.
}                                                                   \tag{8}
$$

The literal coordinate map is $(t_1,\ldots,t_k)\mapsto u=\sum_i t_i$; $u$ is not replaced by an average or a rescaled variable. The original arithmetic scaling coordinate is still $S=k/2+iu$.

For real $|\theta|<\pi/2$, analytic continuation of (6) gives

$$
Z_{\lambda,k}^{\Gamma}(\theta)
 :=\int e^{\theta u}r_{\lambda,k}(u)du
 =c_\lambda^k(\cos\theta)^{-2k\lambda}.                            \tag{9}
$$

The exponential integrability follows either from the original beta-contour estimate or the gamma vertical-strip bound. This justifies all finite differentiated moment integrals used below.

# 4. The sum projection and its complete polynomial complement

Define actual Hilbert spaces

$$
\mathcal H_k=L^2(\mathbb R^k,\prod_i d\sigma_\lambda(t_i)),\qquad
\mathcal H_\Sigma=L^2(\mathbb R,r_{\lambda,k}(u)du).
$$

Their isometric inclusion is

$$
U_\Sigma:\mathcal H_\Sigma\to\mathcal H_k,\qquad
(U_\Sigma f)(\mathbf t)=f(t_1+\cdots+t_k).                           \tag{10}
$$

For $k\ge2$, its adjoint has the explicit disintegration formula

$$
(C_\Sigma F)(u)=\frac{1}{r_{\lambda,k}(u)}
\int_{\mathbb R^{k-1}}
F(t_1,\ldots,t_{k-1},u-\sum_{i<k}t_i)
\prod_{i<k}r_\lambda(t_i)\,r_\lambda(u-\sum_{i<k}t_i)\,d^{k-1}t.
                                                                    \tag{11}
$$

Its denominator is the actual fibre mass. Fubini proves $C_\Sigma U_\Sigma=1$ and $C_\Sigma=U_\Sigma^*$. For $k=1$ both maps are the identity. Put $P_\Sigma=U_\Sigma C_\Sigma$ and retain

$$
F\longmapsto(C_\Sigma F,(1-P_\Sigma)F),\qquad
(f,n)\longmapsto U_\Sigma f+n.                                      \tag{12}
$$

These are inverse Hilbert isometries onto
$\mathcal H_\Sigma\oplus\ker C_\Sigma$. The second component is not discarded.
At each original support label $\ell$, their reconstructed maps are
$(\ell,F)\mapsto(\ell,C_\Sigma F)$ and
$(\ell,F)\mapsto(\ell,(1-P_\Sigma)F)$. A nonzero normal vector has first image
$(\ell,0)$, while its second image retains that vector. Both maps send external
absence to external absence; their paired inverse is still (12). Norm and
Gram observations have their actual quadratic types, not the type of a linear
quotient: $\operatorname{Gram}:\operatorname{Hom}_{\mathbb C}(E,\mathcal H)
\to\operatorname{Herm}(E)$, $R\mapsto R^*R$.

## 4.1 Exact action on every product-polynomial degree

Let $b_n^{(\lambda)}(t)$ be the repository's monic gamma polynomial, with

$$
\sum_{n\ge0}\frac{b_n^{(\lambda)}(t)}{n!}z^n
=(1-iz)^{-\lambda+it/2}(1+iz)^{-\lambda-it/2}.
$$

Set $\alpha=2\lambda$. Its complete norm and recurrence are

$$
\|b_n^{(\lambda)}\|^2=c_\lambda n!(\alpha)_n,\qquad
b_{n+1}^{(\lambda)}=t b_n^{(\lambda)}-n(n+\alpha-1)b_{n-1}^{(\lambda)}.
                                                                    \tag{13}
$$

The polynomials are not divided by their norms. Multiplying the $k$ generating functions proves the literal addition formula

$$
b_n^{(k\lambda)}(\sum_i t_i)
=\sum_{n_1+\cdots+n_k=n}\frac{n!}{\prod_i n_i!}
                         \prod_i b_{n_i}^{(\lambda)}(t_i).         \tag{14}
$$

For a multi-index $\mathbf n$, put $n=\sum_i n_i$. The exact sum projection is

$$
\boxed{
C_\Sigma\left(\prod_i b_{n_i}^{(\lambda)}(t_i)\right)
 =\frac{\prod_i(\alpha)_{n_i}}{(k\alpha)_n}\,b_n^{(k\lambda)}(u).
}                                                                   \tag{15}
$$

**Proof.** Pair the product against (14), in the actual product measure. Orthogonality makes the answer zero unless the sum degree is $n$, and at degree $n$ the answer is
$c_\lambda^k n!\prod_i(\alpha)_{n_i}$. The squared norm of the sum polynomial is $c_\lambda^k n!(k\alpha)_n$. Their quotient gives (15).

These tests identify the whole conditional projection, not merely its finite polynomial moments: the gamma sum measure has exponential moments, so its polynomials are dense in $L^2$. To verify that last statement, an $L^2$ vector orthogonal to all polynomials defines a finite measure whose Fourier transform is analytic on a strip by Cauchy--Schwarz and exponential integrability. All derivatives at zero vanish; analytic uniqueness and uniqueness of Fourier transforms give the zero vector.

The retained normal polynomial is

$$
n_{\mathbf n}=\prod_i b_{n_i}^{(\lambda)}(t_i)
 -\frac{\prod_i(\alpha)_{n_i}}{(k\alpha)_n}
                    b_n^{(k\lambda)}(\sum_i t_i).
$$

Its exact squared norm is

$$
\boxed{
\|n_{\mathbf n}\|^2
=c_\lambda^k\left[
\prod_i n_i!(\alpha)_{n_i}
 -\frac{n!\prod_i(\alpha)_{n_i}^2}{(k\alpha)_n}
\right].
}                                                                   \tag{16}
$$

Thus every degree, every factorial, and the relative component have an explicit map and norm. This is the classical Meixner--Pollaczek addition mechanism, applied with the source's exact scale and masses; it is not a claim to have discovered a new general family of orthogonal polynomials.

# 5. Insert the complete arithmetic multiplier, not a substituted gamma measure

Define the complex amplitude and its squared modulus by

$$
A_{h,\lambda}(t)
=\frac{v_h(1/2+it)}{\Gamma(\lambda+it/2)},\qquad
B_{h,\lambda}(t)=|A_{h,\lambda}(t)|^2,
\qquad w_h=B_{h,\lambda}r_\lambda.                                 \tag{17}
$$

The entire quotient $g/h$ supplies values at the selected zeros. No pole is inserted into the multiplier at those locations. The full complex amplitude, not only its modulus, remains in the source comparison

$$
P\longmapsto
\prod_i\frac{\Gamma(\lambda+it_i/2)}{\sqrt{2\pi}}
 A_{h,\lambda}(t_i)\,P(k/2+i\sum_i t_i).
                                                                    \tag{18}
$$

This is the original Mellin image of $\mathcal V_{h,k}P$.

The scalar multiplier on the sum line is

$$
B_{h,\lambda;k}=C_\Sigma(B_{h,\lambda}^{\otimes k}).
$$

The exact pushforward identity is

$$
\boxed{
 m_{h,k}(u)=w_h^{*k}(u)=r_{\lambda,k}(u)B_{h,\lambda;k}(u).
}                                                                   \tag{19}
$$

This is a norm observation of the original source; it does not project the original finite arithmetic module or change its trace. The maps in (3), including the full unit in $\eta$, remain attached to every polynomial. The full field $B_{h,\lambda}^{\otimes k}$ is recoverable from (12), so its relative complement is retained too.

## 5.1 A bounded multiplier for every full quartet

For $\lambda=1/4$, the original formula is

$$
A_{h,1/4}(t)=
\frac{-\pi^{-1/4}(t^2+1/4)e^{-it\log\pi/2}\zeta(1/2+it)}{h(1/2+it)}.
                                                                    \tag{20}
$$

The minus sign and phase are still in (18). The elementary continuation formula

$$
\zeta(s)=\frac{s}{s-1}-s\int_1^\infty\{x\}x^{-s-1}dx
$$

gives, on this line,

$$
|\zeta(1/2+it)|\le1+2\sqrt{t^2+1/4}\le2(1+|t|).
$$

Let $d=\deg h\ge3$ and take
$T_h=\max(1,2\max_\rho|\rho-1/2|)$. For $|t|\ge T_h$,
$|h(1/2+it)|\ge(|t|/2)^d$, and direct substitution gives

$$
B_{h,1/4}(t)\le\frac{25\,2^{2d}}{\sqrt\pi}|t|^{6-2d}.
$$

Consequently the finite, specified constant

$$
C_h=\max\left\{
\sup_{|t|\le T_h}|A_{h,1/4}(t)|^2,
\frac{25\,2^{2d}}{\sqrt\pi}T_h^{6-2d}
\right\}
$$

satisfies $0\le B_{h,1/4}\le C_h$. The compact supremum uses the analytic quotient, not the expression with a removable denominator left untreated. A full nonreal quartet has $d=4m\ge4$, so this applies to the entire packet used in the exterior amplification, with constants allowed to depend on that fixed packet.

The positive integral in (11) now proves

$$
\boxed{
0<B_{h,1/4;k}(u)\le C_h^k\quad(k\ge2),\qquad
0\le m_{h,k}(u)\le C_h^k r_{1/4,k}(u).
}                                                                   \tag{21}
$$

Strict positivity for $k\ge2$ follows because the one-factor multiplier only vanishes at a discrete set; its excluded hyperplanes have zero fibre measure. For $k=1$ retain its actual isolated zeros.

## 5.2 The other packet sizes and the empty analytic source

For a chosen reference below, $C_h$ always denotes an explicitly specified upper bound for that reference's $B_{h,\lambda}$. An explicit alternate reference is available without changing the arithmetic source. For integer $L\ge0$,

$$
A_{h,1/4+L}(t)
=\frac{A_{h,1/4}(t)}{\prod_{j=0}^{L-1}(j+1/4+it/2)}.                \tag{22}
$$

Its product is a known nonvanishing gamma-shift factor on the integration line. Taking $L\ge\max(0,3-d)$ makes its squared modulus bounded by the same compact/tail argument. Equations (17)--(19) connect both references to the identical original $w_h$; no coordinate or original mass is reassigned.

For the actual seed $h=1$, choosing $L=3$ gives the explicit all-real estimate

$$
\boxed{
B_{1,13/4}(t)\le1024/\sqrt\pi.
}                                                                   \tag{23}
$$

Indeed the gamma-shift denominator is
$4^{-3}(t^2+1/4)(t^2+25/4)(t^2+81/4)$, and
$|\zeta(1/2+it)|\le4\sqrt{t^2+1/4}$. The remaining fraction is bounded by one since
$(t^2+1/4)^2\le(t^2+25/4)(t^2+81/4)$.

This is an analytic estimate for a nonzero seed. Its finite spectral quotient is still zero, as required by the merged correction.

# 6. Exact arithmetic coefficients at every tensor degree

Use a reference for which $B=B_{h,\lambda}$ is bounded, as constructed above. Define its actual coefficients

$$
c_{h,j}=\frac{\int b_j^{(\lambda)}(t)w_h(t)dt}
                 {c_\lambda j!(\alpha)_j},\qquad
\mathcal A_h(z)=\sum_{j\ge0}(\alpha)_j c_{h,j}z^j.                  \tag{24}
$$

The series is used coefficientwise; no convergence radius for this formal series is stipulated. Each coefficient is an actual one-factor arithmetic integral. Define

$$
d_{h,k,n}=[z^n]\mathcal A_h(z)^k.
$$

Then the complete $L^2(r_{\lambda,k}du)$ expansion is

$$
\boxed{
B_{h,\lambda;k}(u)
=\sum_{n\ge0}\frac{d_{h,k,n}}{(k\alpha)_n}
                                     b_n^{(k\lambda)}(u).
}                                                                   \tag{25}
$$

**Proof.** Pair $B^{\otimes k}$ with the finite addition formula (14). Each one-factor pairing is $c_\lambda j!(\alpha)_j c_{h,j}$. The multinomial coefficient cancels the displayed factorials and gives

$$
\int B_{h,\lambda;k} b_n^{(k\lambda)}r_{\lambda,k}
=c_\lambda^k n! [z^n]\mathcal A_h(z)^k.
$$

Divide by the exact norm $c_\lambda^k n!(k\alpha)_n$. Completeness gives (25). No exchange of an infinite product of formal series with an integral was needed: every coefficient used a finite polynomial identity.

At degree zero,

$$
c_{h,0}=\mu_h/c_\lambda,\qquad
 d_{h,k,0}=(\mu_h/c_\lambda)^k,
$$

so (25) recovers exactly $\int m_{h,k}=\mu_h^k$.

The retained relative residual is

$$
\mathcal N_{h,k}=B^{\otimes k}-U_\Sigma B_{h,\lambda;k}.
$$

Its whole norm is calculated by Pythagoras:

$$
\boxed{
\|\mathcal N_{h,k}\|^2
=\left(\int B(t)^2d\sigma_\lambda(t)\right)^k
-c_\lambda^k\sum_{n\ge0}\frac{n!}{(k\alpha)_n}|d_{h,k,n}|^2.
}                                                                   \tag{26}
$$

The difference is nonnegative because it is the norm of the explicitly retained vector. It is not set to zero by calling the sum map a pushforward.

## 6.1 Finite exactness and approximation errors

Let $B_L=\sum_{j=0}^L c_{h,j}b_j^{(\lambda)}$ and
$B_{k,L}=C_\Sigma(B_L^{\otimes k})$. Projection contraction and the tensor telescoping identity give

$$
\boxed{
\|B_{h,\lambda;k}-B_{k,L}\|
\le k\|B\|^{k-1}\|B-B_L\|.
}                                                                   \tag{27}
$$

These norms have the respective original reference measures. The proof uses $\|B_L\|\le\|B\|$ and expands the tensor difference into $k$ terms. Both sides retain the full mass factors.

More strongly, the moments of $B_{k,L}r_{\lambda,k}$ against every polynomial of degree at most $L$ are **exactly** those of $m_{h,k}$, since coefficient $n\le L$ in (25) uses only $c_{h,j}$ with $j\le n$.

It follows that the entire degree-$N$ source Gram, and its degree-$N$ relation Gram, are determined exactly by $c_{h,0},\ldots,c_{h,2N}$. The relation integrands are also degree at most $2N$. Their tensor dependence is the explicit finite coefficient power in (24), not a fresh $k$-dimensional integral.

A truncated $B_{k,L}$ need not be nonnegative pointwise. Its relationship to the true positive metric is the exact finite-moment equality just proved when $L\ge2N$, or the error estimate (27) and Cauchy--Schwarz for the specified polynomial tests when $L<2N$. Positivity is not inferred from a plotted truncated density.

## 6.2 Actual seed coefficients, and their tensor cross term

The supplied numerical driver evaluates the original theta seed on $x\ge1$,
using its inversion symmetry. With $L=D-1/2$, the even spectral moments are
$\mu_{2r}=2\int_1^\infty |L^rf_0(x)|^2dx$. It constructs their source
polynomials by $q_0(z)=4z^2-6z$ and
$q_{r+1}=2z(q_r-q_r')-q_r/2$, and integrates the integer double sums using
upper incomplete gamma integrals. This is a numerical check, not a validated
interval computation.

For $h=1$ and the bounded-multiplier reference $\lambda=13/4$, the 50-digit,
cutoff-6 and 70-digit, cutoff-8 calculations agree in the displayed values:

| Quantity | Numerical value |
|:--|--:|
| $\mu_0$ | $1.279007247846485140479533592267$ |
| $\mu_2$ | $13.055549302570558435392684658123$ |
| $\mu_4$ | $383.274341717364242554407237479131$ |
| $\mu_6$ | $17946.5273016052076235667646919834$ |
| $c_{h,0}$ | $0.201056688692785865809916163220$ |
| $c_{h,2}$ | $0.007645442999486401188133851481$ |
| $c_{h,4}$ | $-0.000030516920803762043746724840$ |

The reference mass is $c_{13/4}=6.361426004587219292629853548733\ldots$,
so it has not been assigned the actual mass $\mu_0$ or the value one.
The negative fourth expansion coefficient is retained; a positive density
need not have positive coefficients in this orthogonal basis.

For every even arithmetic multiplier, the first tensor terms from (25) are
exactly

$$
\begin{aligned}
d_{h,k,2}&=k c_{h,0}^{k-1}(\alpha)_2c_{h,2},\\
d_{h,k,4}&=k c_{h,0}^{k-1}(\alpha)_4c_{h,4}
 +\binom{k}{2}c_{h,0}^{k-2}\bigl((\alpha)_2c_{h,2}\bigr)^2.
\end{aligned}
$$

Both terms in the fourth coefficient remain. These are coefficients of the
exact arithmetic source norm; the empty packet still supplies no nonzero
finite spectral quotient. Agreement of two numerical truncations is not a
bound on their shared truncation or rounding error.

# 7. Feed the result into the two original Toda determinants

Put $\alpha_k=2k\lambda$. The full gamma source determinants are explicit:

$$
\boxed{
\mathfrak D_n^\Gamma(\theta)
=c_\lambda^{kn}
\prod_{j=0}^{n-1}j!(\alpha_k)_j
(\cos\theta)^{-n(\alpha_k+n-1)}.
}                                                                   \tag{28}
$$

At $\theta=0$ this is the product of the monic norms from (13) and (7). One direct proof for all real $\theta$ starts with $\mathfrak D_0^\Gamma=1$ and $\mathfrak D_1^\Gamma=c_\lambda^k\cos^{-\alpha_k}\theta$. Apply the already-proved Hankel--Toda identity recursively; the second derivative of the logarithm of the right side is $n(\alpha_k+n-1)\sec^2\theta$. Substitution proves the next determinant with all constants. Strict positivity makes the recurrence division valid.

In particular

$$
\omega_n^\Gamma(\theta)
=c_\lambda^k n!(\alpha_k)_n(\cos\theta)^{-(\alpha_k+2n)},\qquad
 a_n^\Gamma(\theta)=n(n+\alpha_k-1)\sec^2\theta.                     \tag{29}
$$

The arithmetic source determinant is the previous $\mathfrak D_n$. The reference relation determinant is

$$
\mathfrak B_n^\Gamma(\theta)
=\det\left[\partial_\theta^{i+j}
 \left\{\overline\chi(k/2-i\partial_\theta)
       \chi(k/2+i\partial_\theta)
       Z_{\lambda,k}^\Gamma(\theta)\right\}\right]_{i,j<n}.         \tag{30}
$$

It is the Gram of the **same** multiplication map $M_\chi$. This is an explicit finite expression in gamma constants, $\cos\theta$, $\tan\theta$, and the original coefficients of $\chi$.

Define positive scalar corrections, including the empty-index value one,

$$
X_n=\mathfrak D_n/\mathfrak D_n^\Gamma,\qquad
Y_n=\mathfrak B_n/\mathfrak B_n^\Gamma.
$$

The source--boundary determinant theorem now factors as

$$
\boxed{
V_N=V_N^\Gamma\,T_N,\qquad
 V_N^\Gamma=\frac{\mathfrak D_{N+1}^\Gamma}{\mathfrak B_{N-q+1}^\Gamma},\qquad
 T_N=\frac{X_{N+1}}{Y_{N-q+1}}.
}                                                                   \tag{31}
$$

This retains the entire arithmetic correction in both numerator and denominator. It is not an assertion that the arithmetic quotient metric equals the reference metric.

## 7.1 The representative map between the two metrics

Use the same finite polynomial source. Let $B_\chi$ be the injective matrix of its original relation columns, and let $R_N^\Gamma$ be the least-norm lift for the gamma observation. Let $M_h$ be the actual arithmetic source Gram. Then the actual lift is

$$
\boxed{
R_N=R_N^\Gamma-
B_\chi(B_\chi^*M_hB_\chi)^{-1}B_\chi^*M_hR_N^\Gamma.
}                                                                   \tag{32}
$$

For an empty boundary block the correction is the zero map. The proof is direct: the correction is an old relation, so the quotient remains the identity; multiplication by $B_\chi^*M_h$ gives zero. These two properties characterize the arithmetic least-norm lift.

Applying $\mathcal V_{h,k}$ to (32) supplies the original theta primitive of the difference. In the reconstructed support carrier, the difference maps to the supported zero in its fibre. It does not disappear from the source metric or from its boundary primitive. The comparison keeps the complete unit in (3).

## 7.2 A genuine source-side upper bound

From (21), for every admitted polynomial,

$$
\|P\|_h^2\le C_h^k\|P\|_\Gamma^2.
$$

Evaluate this inequality on $R_N^\Gamma u$ and then minimize on the arithmetic side. This proves

$$
\boxed{
G_N\preceq C_h^kG_N^\Gamma,\qquad
0<T_N\le C_h^{kq}.
}                                                                   \tag{33}
$$

The second assertion is the determinant inequality in dimension $q$. It has the quotient dimension, rather than the full polynomial-source dimension, in its exponent. The corresponding source estimate is $0<X_n\le C_h^{kn}$, and similarly $0<Y_n\le C_h^{kn}$.

These are one-sided estimates. They do not bound the consecutive ratio $T_{N-1}/T_{N+1}$, which is the quantity required by the Toda upper bound. Its exact map to that estimate is the following.

# 8. The current upper-control expression, with all reference costs exposed

Define

$$
Q_N=\frac{X_{N+2}X_N}{X_{N+1}^2},\qquad
\mathcal R_N^\Gamma=\frac{V_{N-1}^\Gamma}{V_{N+1}^\Gamma}.
$$

At the original observation $\theta=0$, (29)--(31) give

$$
\boxed{
a_{N+1}=(N+1)(N+\alpha_k)Q_N,\qquad
\mathcal R_N=\mathcal R_N^\Gamma\frac{T_{N-1}}{T_{N+1}}.
}                                                                   \tag{34}
$$

The preceding exact phase identity is also retained through

$$
\ell_N'=\partial_\theta\log V_N^\Gamma+\partial_\theta\log T_N.
$$

Thus its finite upper bound becomes exactly

$$
\boxed{
\epsilon_{h,k,N}\le
\sqrt{(N+1)(N+\alpha_k)Q_N}\,
\frac{\mathcal R_N^\Gamma T_{N-1}/T_{N+1}-1}
 {2\sqrt{\mathcal R_N^\Gamma T_{N-1}/T_{N+1}}}.
}                                                                   \tag{35}
$$

The nonnegative numerator uses the original monotonicity of the actual quotient minimum, not a presumed monotonicity of $T_N$. When this inequality is coarse, the inherited equality with the volume-imbalance square and the phase square remains the sharper calculation.

For the full quartet one can keep $\lambda=1/4$, so $\alpha_k=k/2$. The gamma source recurrence is now explicit at every degree; the remaining arithmetic dependence is in $Q_N$ and the relative source--boundary correction $T_{N-1}/T_{N+1}$. The reference relation term still contains the full spectral annihilator $\chi$. It is not bounded by pretending its roots are on the integration line.

The exterior theorem remains

$$
L_{h,k}\le\epsilon_{h,k,N},\qquad
L_{h,k}=2\delta[1+k(m-1)](k+1)
          \left\lfloor\frac{(k+1)^2}{4}\right\rfloor.
$$

Neither (33) nor (35) proves a subcubic bound. Equation (35) identifies exactly which degree-to-degree arithmetic corrections must be controlled next. All entries of those finite determinants can now be generated by the all-$k$ coefficient transform (25), with the source--boundary comparison map (32) retained.

# 9. A proved all-degree tail estimate for the actual arithmetic moments

The multiplier bound gives more than a change of coordinates. For $a,b>0$ with $a+b<\pi/2$, every integer $r\ge0$ and $T\ge0$,

$$
\boxed{
\int_{|u|>T}|u|^r m_{h,k}(u)du
\le
2 C_h^k c_\lambda^k\,r!\,a^{-r}
 e^{-bT}(\cos(a+b))^{-2k\lambda}.
}                                                                   \tag{36}
$$

**Proof.** For $x\ge0$, $x^r\le r!a^{-r}e^{ax}$. On the indicated tail, $1\le e^{b(x-T)}$. Apply (21) and integrate. Since the reference density is even,

$$
\int e^{(a+b)|u|}r_{\lambda,k}(u)du
\le Z_{\lambda,k}^\Gamma(a+b)+Z_{\lambda,k}^\Gamma(-a-b).
$$

Equation (9) gives (36). This estimate retains the original mass and the complete tensor cost. It is a theorem with specified constants, not a claim that a floating-point quadrature has validated them numerically.

For a source or relation moment whose integrand is a polynomial $P(u)=\sum_j p_ju^j$, sum $|p_j|$ times (36). In particular this controls every entry of a degree-$N$ source and relation Gram, including the full $|\chi|^2$ factor. It is then combined with an independently certified compact-interval quadrature and the existing matrix inverse/error inequalities; it does not certify that quadrature by itself.

This is an explicit tail interface for the actual arithmetic input at all degrees and tensor powers. For the empty analytic seed, (23) gives a completely stated bound without locating any zeta zero. For a nonempty packet the compact constant in $C_h$ must be enclosed using the actual analytic quotient.

# 10. What has and has not been concluded

The constructed chain is

$$
\text{original split-supported polynomial source}
\longrightarrow\text{full gamma product fibre with arithmetic amplitude}
\longrightarrow\text{sum density and retained relative component}
\longrightarrow\text{exact all-tensor arithmetic coefficients}
\longrightarrow\text{the same source--boundary Toda determinant ratio}.
$$

The finite coefficient projection, polynomial degree, all masses, all gamma factors, the arithmetic unit, and the original theta primitives are explicit. The same finite quotient is used throughout; an existing relation becomes $e$ only under its original quotient map, while the source norm and all derivative data remain available before that map. No new scalar-zero adjunction is performed at a tensor or relation level.

There is now a proved bound for the full arithmetic sum density, explicit closed-form reference determinants at every tensor degree, an exact finite coefficient algorithm, and a rigorous moment-tail bound. There is not yet a uniform small bound for the consecutive arithmetic determinant correction. The upper-estimate problem is sharpened to that specific comparison rather than being claimed solved by gamma convolution or by positivity of individual source Grams.

# References and exact source roles

* Repository main at `fa4be32f87a9a90f3c02a07f7790dea95a1e7b0f`, `tex/theta_gamma_reference.tex` in the 20260912-stieltjes continuation, TG.2--TG.14: original one-factor gamma reference, arithmetic amplitude, constants and polynomial norms. Only the stated TeX window was read in this review; no complete reader audit is claimed.
* PR #22 head `811210d24b80813a08972ca23f919db015383137`, `workbenches/tau-exterior-trace-formal/RESEARCH_NOTE.md`: current exterior and filtration formalization work, with its separate verification scope. Its reported in-progress status is not promoted to a completed certificate.
* Delivered `Tau_Toda_Volume_Control/NOTE.tex`: original source and relation determinants, quotient metric, phase derivative and finite upper inequality. Its supplied manifest was independently checked here.
* NIST Digital Library of Mathematical Functions, §§18.22 and 18.23: classical Meixner--Pollaczek recurrence and generating function. The formulas here retain the repository's original $t/2$ scale and all factorials.
* Koelink, H. T., and Van der Jeugt, J. (1998). Convolutions for orthogonal polynomials from Lie and quantum algebra representations. *SIAM Journal on Mathematical Analysis*, 29(3), 794--822. arXiv:q-alg/9607010. Background for the classical addition/convolution mechanism, not a claim that this article treats the present arithmetic quotient.

The proofs in this note establish the stated specialized maps directly. The regression checker tests finite exact polynomial and matrix consequences; it does not replace the analytic proofs or establish the outstanding uniform estimate.
