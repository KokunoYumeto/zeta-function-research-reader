# Independent proof review of the exact arithmetic generating join

Date: 13 September 2026. This is a direct proof review of the generating join relayed by the Zeta owner. It uses the literal arithmetic density and gamma reference in the delivered `Tau_Gamma_Convolution_Descent/NOTE.tex`, SHA256 `7cf984d87de405b815250b44454c4ee27c8ab46574da245b377ebc6e49327fa2`. That complete source was read in the preceding independent review. This report edits no source or shared integration file. It addresses the generating identity, its branches, convergence, derivative interchange, coefficients, and tensor partition-function quotient; finite metric-error estimates are outside this assignment.

The proposed identities pass with their stated domains and original masses. The formal arithmetic series in source (24) is the Taylor series of the holomorphic function constructed below on `|z|<1`. No global nonvanishing assertion about that complex function is needed.

## 1. Original measures and the analytic moment transform

Fix a positive real reference parameter `lambda` for which the already-proved arithmetic multiplier bound holds. Retain

\[
r_\lambda(t)=\frac{|\Gamma(\lambda+it/2)|^2}{2\pi},\qquad
c_\lambda=2^{1-2\lambda}\Gamma(2\lambda),\qquad
w_h(t)=B_{h,\lambda}(t)r_\lambda(t),\qquad
0\le B_{h,\lambda}(t)\le C_h<\infty.
\]

The nonzero arithmetic density is positive almost everywhere; its total mass is `mu_h=integral w_h(t)dt>0`. In particular, neither `mu_h` nor `c_lambda` is assigned the value one. Define on the complex strip

\[
\mathcal S=\{\theta\in\mathbb C:|\operatorname{Re}\theta|<\pi/2\},
\qquad M_h(\theta)=\int_{\mathbb R}e^{\theta t}w_h(t)\,dt.
\]

For each `0<=eta<pi/2`, the exact gamma moment formula proves

\[
\int_{\mathbb R}e^{\eta|t|}w_h(t)\,dt
\le C_h\int_{\mathbb R}(e^{\eta t}+e^{-\eta t})r_\lambda(t)\,dt
=2C_hc_\lambda(\cos\eta)^{-2\lambda}.
\]

Thus the integral defining `M_h` converges locally uniformly on `S`. Its derivatives can also be taken under the integral. Indeed, on a compact set with `|Re(theta)|<=eta`, choose `eta'` with `eta<eta'<pi/2` and put `delta=eta'−eta>0`. For each integer `j>=0`, the exponential-series inequality gives

\[
|t|^j|e^{\theta t}|
\le j!\delta^{-j}e^{\eta'|t|}.
\]

The preceding gamma bound integrates this majorant. Consequently `M_h` is holomorphic on `S` and

\[
M_h^{(j)}(\theta)=\int_{\mathbb R}t^je^{\theta t}w_h(t)\,dt
\]

there. This analytic statement keeps the original spectral variable `t` and its mass.

## 2. Principal logarithms and arctangent on the unit disc

Let `D={z in C:|z|<1}` and use the principal logarithm `Log`, with its value zero at one. For `z=x+iy in D`,

\[
\operatorname{Re}(1+iz)=1-y>0,\qquad
\operatorname{Re}(1-iz)=1+y>0,
\]

and

\[
\operatorname{Re}(1+z^2)=1+x^2-y^2\ge1-|z|^2>0.
\]

All three principal logarithms are therefore holomorphic on the whole disc. Define the branch of arctangent inherited from zero by

\[
\phi(z)=\arctan z
=\frac{\Log(1+iz)-\Log(1-iz)}{2i}.
\]

Then `phi(0)=0` and direct differentiation gives `phi'(z)=1/(1+z^2)`. The two exact logarithmic identities needed below are

\[
\Log(1+iz)+\Log(1-iz)=\Log(1+z^2),
\]

\[
\Log(1-iz)-\Log(1+iz)=-2i\phi(z).
\]

For the first identity, exponentiating both sides gives the same nonzero holomorphic function `(1+iz)(1−iz)=1+z^2`; their difference is a continuous integer multiple of `2pi i` on a connected disc and vanishes at zero. The second identity is the defining formula. This proves that no branch-dependent additive constant is lost.

For an explicit range bound, set

\[
W(z)=\frac{1+iz}{1-iz}
=\frac{1-|z|^2+2ix}{|1-iz|^2}.
\]

It has positive real part. The difference `Log(1+iz)−Log(1−iz)` is therefore `Log W(z)` on the disc, by the same continuous-branch argument at zero. It follows that

\[
\operatorname{Re}\phi(z)
=\tfrac12\Arg W(z)
=\tfrac12\arctan\!\left(\frac{2x}{1-|z|^2}\right),
\]

where the last real arctangent takes its value in `(-pi/2,pi/2)`. For `|z|<=r<1`, the denominator is positive and

\[
|\operatorname{Re}\phi(z)|
\le\tfrac12\arctan\!\left(\frac{2r}{1-r^2}\right)
=\arctan r<\pi/4.
\]

The equality in the last step follows because `2 arctan r` lies in `[0,pi/2)` and has tangent `2r/(1−r^2)`. It includes `r=0`; equality in the bound is attained at the real points `z=±r`. Thus the proposed compact-disc bound is exact, rather than a qualitative boundedness assertion.

The exponential identity `exp(2i phi(z))=W(z)` also proves `tan(phi(z))=z` directly: the identity
`tan(w)=(exp(2iw)−1)/(i(exp(2iw)+1))` reduces its right side to `z`. Its denominator is nonzero here because `W(z)+1=2/(1−iz)`. For real `theta` with `|theta|<pi/4`, `tan theta in (-1,1)` and the branch range above gives `phi(tan theta)=theta`.

## 3. The exact gamma polynomial generating function

Retain the source's monic gamma polynomials, with their original factorials:

\[
\mathcal G_\lambda(z,t)
:=\sum_{n\ge0}\frac{b_n^{(\lambda)}(t)}{n!}z^n
=(1-iz)^{-\lambda+it/2}(1+iz)^{-\lambda-it/2}.
\]

The powers use the principal logarithms just fixed. Substituting the two logarithmic identities of section 2 gives exactly

\[
\begin{aligned}
\mathcal G_\lambda(z,t)
&=\exp\left[-\lambda\{\Log(1-iz)+\Log(1+iz)\}
+\frac{it}{2}\{\Log(1-iz)-\Log(1+iz)\}\right]\\
&=\exp\{-\lambda\Log(1+z^2)+t\phi(z)\}\\
&=(1+z^2)^{-\lambda}e^{t\arctan z}.
\end{aligned}
\]

In particular, the exponent is `+t arctan z`. The factor `it/2` multiplied by `−2i arctan z` gives `+t arctan z`; it does not give its negative or an extra factor two. For example, this yields `b_1(t)=t` and `b_2(t)=t^2−2lambda`, consistent with the original monic recurrence.

For `|z|<=r<1` and real `t`, section 2 gives the pointwise bound

\[
|\mathcal G_\lambda(z,t)|
=|1+z^2|^{-\lambda}e^{t\operatorname{Re}\phi(z)}
\le(1-r^2)^{-\lambda}e^{(\arctan r)|t|}.
\]

Since `arctan r<pi/4<pi/2`, this majorant is integrable against the original arithmetic measure by section 1. More explicitly,

\[
\int_{\mathbb R}|\mathcal G_\lambda(z,t)|w_h(t)\,dt
\le2C_hc_\lambda
\left(\frac{1+r^2}{1-r^2}\right)^\lambda.
\]

The identity `cos(arctan r)=(1+r^2)^(−1/2)` accounts for the last constant. It supplies a compact-disc dominating function before an integral or derivative is interchanged.

## 4. Construction, holomorphy, and every coefficient

Define the actual arithmetic generating function on `D` by

\[
\mathcal A_h(z)=\frac1{c_\lambda}
\int_{\mathbb R}\mathcal G_\lambda(z,t)w_h(t)\,dt.
\]

The preceding locally uniform integrable majorant proves that this is holomorphic. Substitution of the exact expression for `G_lambda` proves the proposed join without a formal-series interchange:

\[
\boxed{
\mathcal A_h(z)=c_\lambda^{-1}(1+z^2)^{-\lambda}
M_h(\arctan z),\qquad |z|<1.
}
\]

The composition is defined because `|Re arctan z|<pi/4`, inside the analytic strip for `M_h`. The complex power remains the principal one inherited from zero.

For complete derivative justification, fix `0<=r<R<1`. Cauchy's derivative formula applied to `G_lambda(.,t)` on the circle of radius `R−r` about any `z` with `|z|<=r` gives

\[
|\partial_z^n\mathcal G_\lambda(z,t)|
\le\frac{n!}{(R-r)^n}(1-R^2)^{-\lambda}
e^{(\arctan R)|t|}.
\]

All points of that circle have modulus at most `R`, and the right side is integrable against `w_h`. Fubini in Cauchy's integral formula, or dominated differentiation with this explicit majorant, therefore proves

\[
\mathcal A_h^{(n)}(z)
=c_\lambda^{-1}\int_{\mathbb R}
\partial_z^n\mathcal G_\lambda(z,t)w_h(t)\,dt.
\]

At zero the polynomial generating function gives `partial_z^n G_lambda(0,t)=b_n^(lambda)(t)`. With the source's coefficient definition

\[
c_{h,n}=\frac{\int b_n^{(\lambda)}(t)w_h(t)\,dt}
{c_\lambda n!(2\lambda)_n},
\]

the exact coefficient identity is thus

\[
\boxed{
\mathcal A_h^{(n)}(0)
=c_\lambda^{-1}\int_{\mathbb R}b_n^{(\lambda)}(t)w_h(t)\,dt
=n!(2\lambda)_n c_{h,n}.
}
\]

Taylor's theorem for a holomorphic function on the disc now proves

\[
\boxed{
\mathcal A_h(z)=\sum_{n\ge0}(2\lambda)_n c_{h,n}z^n,
\qquad |z|<1.
}
\]

This is the source's formerly coefficientwise-defined series, now with absolute and locally uniform convergence throughout the open unit disc. The derivative at zero contains `n!`; the coefficient of `z^n` does not. No infinite product of formal series has been moved through the original integral.

The compact bound also gives, for each `0<R<1`, the concrete coefficient estimate

\[
|(2\lambda)_n c_{h,n}|
\le2C_h\left(\frac{1+R^2}{1-R^2}\right)^\lambda R^{-n}
\]

by Cauchy's coefficient formula. This is a fixed-disc bound, not a tensor-degree asymptotic estimate.

## 5. Inverting the join on its stated real domain

Take real `theta` with `|theta|<pi/4`. Then `z=tan theta` belongs to the real interval `(-1,1)`, `arctan(tan theta)=theta`, and `1+tan^2 theta=sec^2 theta>0`. The forward identity gives

\[
\mathcal A_h(\tan\theta)
=c_\lambda^{-1}(\sec^2\theta)^{-\lambda}M_h(\theta)
=c_\lambda^{-1}(\cos\theta)^{2\lambda}M_h(\theta).
\]

Here all displayed real powers use positive real bases; the equality follows from the same branches fixed on the disc. Solving for the moment transform proves

\[
\boxed{
M_h(\theta)=c_\lambda(\sec\theta)^{2\lambda}
\mathcal A_h(\tan\theta),\qquad
\theta\in\mathbb R,\quad |\theta|<\pi/4.
}
\]

For real `z in (-1,1)`, its integral expression has a strictly positive real kernel and a nonzero nonnegative arithmetic density. Thus `A_h(z)>0`. Comparison with the gamma density also gives `A_h(z)<=C_h`: at `theta=arctan z`,

\[
M_h(\theta)\le C_h c_\lambda(\cos\theta)^{-2\lambda},
\qquad
\mathcal A_h(z)=c_\lambda^{-1}(\cos\theta)^{2\lambda}M_h(\theta).
\]

The original source mass is visible at zero:

\[
\mathcal A_h(0)=\mu_h/c_\lambda=c_{h,0}.
\]

It is not one in general. Complex zeros elsewhere in the disc are not excluded by this positive real-interval statement. No complex logarithm of `A_h` is used in the proved identities.

## 6. Every tensor degree and the gamma quotient

For each positive integer `k`, retain the literal arithmetic sum density `m_(h,k)=w_h^{*k}` in the unscaled sum coordinate `u=t_1+...+t_k`, and define

\[
Z_{h,k}(\theta)=\int_{\mathbb R}e^{\theta u}m_{h,k}(u)\,du.
\]

For complex `theta` in the strip `S`, the absolute integral after returning to the product variables is

\[
\int_{\mathbb R^k}\left|e^{\theta(t_1+\cdots+t_k)}\right|
\prod_{i=1}^k w_h(t_i)\,d^kt
=M_h(\operatorname{Re}\theta)^k<\infty.
\]

Fubini is therefore applicable and proves `Z_(h,k)(theta)=M_h(theta)^k`. On the real subinterval `|theta|<pi/4`, the exact gamma sum formula is

\[
Z_{\lambda,k}^{\Gamma}(\theta)
=c_\lambda^k(\cos\theta)^{-2k\lambda}>0.
\]

Raising the already-proved inverse join to the integer power `k` and dividing by this exact denominator proves

\[
\boxed{
\frac{Z_{h,k}(\theta)}{Z_{\lambda,k}^{\Gamma}(\theta)}
=\mathcal A_h(\tan\theta)^k,
\qquad k\ge1,\quad\theta\in\mathbb R,\quad |\theta|<\pi/4.
}
\]

At zero this ratio is `(mu_h/c_lambda)^k`, agreeing with both original convolution masses. For the pure gamma reference `w_h=r_lambda`, the same proof yields `A_h(z)=1` on the real interval and therefore on the whole connected disc by holomorphic uniqueness. This supplies an independent check on the prefactor `1/c_lambda` and the exponent `−lambda`.

Since `A_h` has a convergent Taylor series on the disc, each integer tensor power has the convergent series whose degree-`n` coefficient is the finite sum

\[
[z^n]\mathcal A_h(z)^k
=\sum_{n_1+\cdots+n_k=n}\prod_{i=1}^k(2\lambda)_{n_i}c_{h,n_i}.
\]

This is exactly the all-tensor arithmetic coefficient in the delivered source. The proof keeps each Pochhammer symbol, the original masses and the original sum coordinate. It does not replace a source or relation determinant by its zeroth partition function.

## Disposition and scope

The proposed analytic generating join, real inverse and all-tensor partition-function quotient are correct on the stated domains. The compact-disc range bound is `|Re arctan z|<=arctan r`, the integrated generating function is dominated by the explicit gamma exponential-moment majorant above, and all derivatives may be interchanged with the original arithmetic integral. The coefficient derivative is exactly `n!(2lambda)_n c_(h,n)`.

This upgrades the source's formal one-factor coefficient series to a holomorphic function on `|z|<1`, connected by an exact map to the actual arithmetic moment transform. It does not assert that finitely many coefficients recover that function at a nonzero tilt, that its complex logarithm is globally defined, or that the outstanding consecutive arithmetic determinant correction is uniformly small.

## Exact standalone-chapter audit: GC.24–GC.30

The final actual chapter `work/gamma_exact_coefficient_join_20260913.tex` was read at SHA256 `270d7f89e6ac2b147fdbdb5d223125b3744239d43c5485c53740c47ed8d223ec`, 40,111 bytes. The reviewed block is the complete text at lines 355–472, including the complex inverse continuation between GC.29 and GC.30. The specific dependency passages GC.6, GC.13–GC.14 and GC.21–GC.23 were also inspected in the preceding revision. This source pin identifies the entire file; the approval in this appendix concerns the stated block and the implications of the inspected dependencies, not unreviewed chapters elsewhere in that file. The preceding reviewed revision was SHA256 `ef6a252b14d386b8fc063d22d1fbd0c9868b63fe66f25a88c7b2efc00e4ab8dc`, 40,074 bytes. The entire stated block was re-read in the final revision, and its only change is the precise kernel-naming clarification at lines 417–419, approved below.

### Every positive reference parameter

The actual chapter strengthens the initial bounded-reference formulation of this review to every real `lambda>0`. This is valid: the chapter uses its arithmetic estimate GC.6, independently of boundedness of `B_(h,lambda)`. On the integration line that estimate gives for every `0<beta<pi/4`

\[
w_h(t)=\frac{|v_h(1/2+it)|^2}{2\pi}
\le K_{\beta,h}e^{-2\beta|t|}.
\]

For a fixed compact subdisc `|z|<=R<1`, put `a=arctan R<pi/4` and choose `beta` with `a/2<beta<pi/4`. The product of `w_h` with the generating kernel majorant is at most a fixed constant times `exp(−(2beta−a)|t|)`, which is integrable. The same argument applies to every derivative majorant from the Cauchy formula, since all its additional displayed factors are independent of `t`. The bound proves the required analytic integration for every positive `lambda`; no bounded multiplier is being assumed in GC.24. It also yields analyticity of `M_h` on `|Re theta|<pi/2` by choosing `beta>|Re theta|/2` locally on that strip.

### Cauchy bound with its precise kernel and constants

For `0<=r<R<1`, each circle `|zeta−z|=R−r` with `|z|<=r` lies in `|zeta|<=R`. Cauchy's formula gives exactly

\[
\partial_z^n\mathcal G_\lambda(z,t)
=\frac{n!}{2\pi i}\int_{|\zeta-z|=R-r}
\frac{\mathcal G_\lambda(\zeta,t)}{(\zeta-z)^{n+1}}\,d\zeta.
\]

The contour length `2pi(R−r)` cancels the `2pi` and one denominator power. Using GC.28 on the contour proves

\[
|\partial_z^n\mathcal G_\lambda(z,t)|
\le n!(R-r)^{-n}(1-R^2)^{-\lambda}
e^{\arctan(R)|t|}.
\]

After integration against the original arithmetic density, the corresponding bound for the generating function's derivative is

\[
|\mathcal A_h^{(n)}(z)|
\le\frac{n!}{c_\lambda}(R-r)^{-n}(1-R^2)^{-\lambda}
\int_{\mathbb R}e^{\arctan(R)|t|}w_h(t)\,dt<\infty.
\]

This confirms the exact factorial, radius and mass constants. The final chapter explicitly names the kernel derivative `|partial_z^n G_lambda(z,t)|` at lines 417–419. This installs the requested clarification and removes the earlier phrase “its integrated modulus.” The displayed bound and its constants remain unchanged and correct.

### The stronger complex inverse strip

Define the connected open strip

\[
\mathcal S_0=\{\theta\in\mathbb C:|\operatorname{Re}\theta|<\pi/4\}.
\]

For `theta=x+iy` in this strip, direct expansion of sine and cosine gives

\[
|\sin\theta|^2=\tfrac12\{\cosh(2y)-\cos(2x)\},\qquad
|\cos\theta|^2=\tfrac12\{\cosh(2y)+\cos(2x)\}.
\]

Since `cos(2x)>0`, the second expression is strictly positive and exceeds the first. Consequently

\[
|\tan\theta|^2
=\frac{\cosh(2y)-\cos(2x)}{\cosh(2y)+\cos(2x)}<1.
\]

The numerator is nonnegative, including its zero at the origin. Thus `tan` is holomorphic on `S_0` with values in the unit disc. The function `phi(tan theta)` is holomorphic on `S_0`, agrees with `theta` on a neighbourhood of zero by the inverse branch already fixed, and therefore equals `theta` throughout `S_0` by the identity theorem.

For the power identity, retain the chapter's analytic logarithm `L_c(theta)` of `cos theta` with value zero at zero. On the larger strip `|Re theta|<pi/2`, one has `Re cos theta=cos(x)cosh(y)>0`; hence this logarithm is also the principal logarithm there. Since `tan theta` is in the unit disc on `S_0`, the logarithm `Log(1+tan^2 theta)` is the same analytic logarithm used in GC.24. The holomorphic function

\[
J(\theta)=\Log(1+\tan^2\theta)+2L_c(\theta)
\]

satisfies `exp J(theta)=(1+tan^2 theta)cos^2 theta=1`. It is a continuous integer multiple of `2pi i` on the connected strip and vanishes at zero. Hence `J=0` everywhere on `S_0`. Substitution in GC.24 proves the complex inverse with its exact branch:

\[
M_h(\theta)=c_\lambda e^{-2\lambda L_c(\theta)}
\mathcal A_h(\tan\theta),\qquad\theta\in\mathcal S_0.
\]

The gamma partition function in GC.13 is `c_lambda^k exp(−2k lambda L_c(theta))`, which is nonzero on this strip. Complex Fubini, already justified by the finite absolute integral `M_h(Re theta)^k`, gives `Z_(h,k)=M_h^k`. Therefore

\[
\frac{Z_{h,k}(\theta)}{Z_{\lambda,k}^\Gamma(\theta)}
=\mathcal A_h(\tan\theta)^k,\qquad\theta\in\mathcal S_0,
\]

exactly as asserted in the actual chapter. Possible complex zeros of `A_h` do not obstruct this equality; the proof never takes its logarithm.

### GC.30 and the finite triangular coefficient map

Expand the monic polynomial in the original variable as `b_n^(lambda)(t)=sum_(j=0)^n b_(n,j)t^j`, with `b_(n,n)=1`. Each summand is integrable against `w_h`, and the moment derivative formula proved above gives

\[
\frac1{c_\lambda}\int b_n^{(\lambda)}(t)w_h(t)\,dt
=\frac1{c_\lambda}\sum_{j=0}^n b_{n,j}M_h^{(j)}(0).
\]

The left side is `n!(alpha)_n c_(h,n)`, where `alpha=2lambda`, by GC.29. This proves the first equality in GC.30. The Taylor expansion of the holomorphic integer power `A_h(z)^k` proves its second equality, including the factor `1/n!`; its degree-`n` coefficient is precisely the finite sum GC.22.

The invertibility assertion also follows without dropping the diagonal constants. Given the coefficient values through degree `n`, recover the moments recursively by

\[
M_h(0)=c_\lambda c_{h,0},\qquad
M_h^{(n)}(0)=c_\lambda n!(\alpha)_n c_{h,n}
-\sum_{j=0}^{n-1}b_{n,j}M_h^{(j)}(0),\quad n\ge1.
\]

Every diagonal multiplier `c_lambda n!(alpha)_n` is strictly positive for `lambda>0`. Conversely the finite polynomial formula gives each coefficient from these moments. This is the exact invertible triangular map claimed in the chapter.

**Final exact-block disposition:** GC.24–GC.30 and the intervening complex inverse statement pass at the final pinned source revision. The derivative-kernel clarification is installed and verified; this block has no outstanding review correction. No source edits were made by this reviewer.
