# PR27: scoped Hochschild comparison and Laplacian review

Review date: 2026-09-13. Repository: `KokunoYumeto/zeta-function-research-reader`. Immutable reviewed head: `a4a87844c257485ae6d669f5b3eb6d96b9e8b8d8`.

## Outcome

No merge-blocking mathematical error was found in the two assigned notes. They are suitable to merge as written within their stated research-note scope, subject to the separate PR-wide source, formal, and CI review. This is not approval of an RH proof, a uniform arithmetic estimate, or an unrestricted identification of the full and critical spectral objects. In particular, the explicit loss of off-critical generalized blocks is correct, not an omitted obstacle.

The literal zero-mode problem identified in the primary publication is real. The proposed augmented object and Gaussian averaging repair are mathematically sound in the specified local smooth-flat topology. The numerical-range parabola is also valid in the original Gram metric, without diagonalizability.

## Exact read extent and evidence

Read completely, including qualifications and references:

- [HOCHSCHILD_COMPARISON.md at the reviewed head](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/a4a87844c257485ae6d669f5b3eb6d96b9e8b8d8/workbenches/tau-specialization-curvature-formal/HOCHSCHILD_COMPARISON.md), 430 physical lines plus final newline.
- [LAPLACIAN_PARABOLA.md at the reviewed head](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/a4a87844c257485ae6d669f5b3eb6d96b9e8b8d8/workbenches/tau-specialization-curvature-formal/LAPLACIAN_PARABOLA.md), 85 physical lines plus final newline.

The local copies under `pr27_review/source` were compared as complete strings against the pinned raw GitHub versions; both matched. Their SHA-256 hashes are respectively:

```text
0f5707281ee46ec411b1af5d25361cf23bb88c3689a0f3cd75f7fac5b951be13
f127b4ed560fbe5215d24a9337a70be4ae316f518ac0f2d05f2919f4ae491fdb
```

Primary source: Alain Connes and Caterina Consani, *Hochschild homology, trace map and zeta-cycles*, Proceedings of Symposia in Pure Mathematics 105 (2023), printed pp. 83-101, [DOI](https://doi.org/10.1090/pspum/105/01896), [author-hosted published offprint](https://alainconnes.org/wp-content/uploads/Hochschild-homology-trace-map-and-%CE%B6-cycles-2023.pdf). Read all nineteen pages as extracted text, including proofs and references. Independently rendered and visually inspected complete printed pp. 89-92, 94-95, and 100. In particular, the two Section 5 problems below are present in the printed pages, not extraction artifacts. The offprint SHA-256 is `1560e179de4c73fc605a5e5b0ce7dd67cbc1249964f91a8a686116daec36212e`.

The PDF skill was read and used for extraction/rendered-page verification. The reference PDF and PNGs remain in a private temporary directory outside this review/deliverable tree; none was added to the repository. This review did not inspect the uploaded proceedings volume, the chapter's separately cited books/papers, or independently reprove their global spectral-realization theorems. No local Lean was run, no remote writes were made, and no additional worker was spawned.

## 1. Exact trace, half-density, and Gaussian seed

The citation in H4-H7 is accurate: Proposition 3.1 concerns the inclusion-induced image; Lemma 3.2(ii) and Proposition 3.3 give the trace constant on that image (printed pp. 87-90). The note correctly avoids identifying every sector of Hochschild homology with even Schwartz functions. [Primary source, Sections 3-3.1](https://alainconnes.org/wp-content/uploads/Hochschild-homology-trace-map-and-%CE%B6-cycles-2023.pdf)

Here is the actual constant check. For the representative `(1_Zhat tensor f)U(1)` and positive real idele coordinate `u`, the finite component forces the rational summation variable to be a nonzero integer. Evenness then yields

\[
\operatorname{Tr}j(f)(u)=\sum_{n\ne0}f(nu)=2\sum_{n>0}f(nu)=\Theta f(u).
\]

Consequently `E=(1/2)U Theta`, not `U Theta`. For `UF(u)=u^(1/2)F(u)`,

\[
\|UF\|^2_{L^2(du/u)}=\int_0^\infty u|F(u)|^2\frac{du}{u}
=\|F\|^2_{L^2(du)}.
\]

This is the positive-half-line isometry used in H7. Extending an even function to the full line doubles its squared norm; the note explicitly retains that separate convention.

With `D=-x d/dx`, direct differentiation gives

\[
Dg_0=2\pi x^2g_0,\quad D^2g_0=(4\pi^2x^4-4\pi x^2)g_0,
\quad (D^2-D)g_0=(4\pi^2x^4-6\pi x^2)g_0.
\]

Using the half-line Mellin transform `MF(s)=integral F(x)x^(s-1) dx`, its Gaussian transform is `(1/2)pi^(-s/2)Gamma(s/2)`. Integration by parts multiplies by `s` for each `D`. Thus

\[
M\phi_*(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2),\qquad
M\Theta\phi_*(s)=2\zeta(s)M\phi_*(s)=2\xi(s).
\]

This validates H8-H11 without changing the seed or its coefficient. Lemma 4.1(iii), printed pp. 90-91, supplies the stated bijection `D^2-D:S_even -> V`. Its continuous inverse follows from the Frechet open mapping theorem because the two moment conditions are continuous and define a closed subspace. The operator commutes with `D`, and `F D=(1-D)F` makes `D^2-D` Fourier-equivariant. H12-H13 therefore are genuine two-term-complex isomorphisms; the ordered-leg cycle is transported rather than discarded. [Primary source, Lemma 4.1](https://alainconnes.org/wp-content/uploads/Hochschild-homology-trace-map-and-%CE%B6-cycles-2023.pdf)

## 2. Closure and the full-to-critical map

H14-H15 retain the correct closure arrow. Independently of any retraction, the kernel of `B/Theta V -> B/closure(Theta V)` is exactly `closure(Theta V)/Theta V`. If the prior continuous retraction `Lambda Theta=1` is available, `Theta Lambda` is a continuous idempotent with range `Theta V`; this proves closedness. I checked this implication, not the earlier global-retraction theorem itself.

For H16-H20, let `y=log x`. The defining strong-Schwartz seminorms of `B` control all derivatives of `exp(y/2)F(exp y)` with arbitrary polynomial weights. This gives continuity of the plus-sign Mellin restriction into `S(R)`. For `phi in V`, the analogous factor `exp(y/2)phi(exp y)` has exponentially decaying derivatives at negative infinity, using `phi(x)=O(x^2)`, and decays at positive infinity. Hence its Fourier transform is Schwartz. The factorization

\[
J_{\rm crit}\Theta\phi(t)=2\zeta(1/2+it)M\phi(1/2+it)
\]

places the image in the target relation space, so `Gamma` really descends; continuity also kills the closure of the source relation space. Integration by parts and change of variables give precisely multiplication by `1/2+it` and `a^(it)` for the displayed normalized dilation. The note deliberately uses the opposite Fourier sign from the chapter's initial transform; it does not silently drop this reversal.

The full realization uses the closed strong-Schwartz quotient and retained jets; the critical realization uses a different closed Schwartz ideal quotient. Those primary claims appear in Proposition 4.2 and Theorem 5.4/Remark 5.5. [Primary source, pp. 91-92 and 98-100](https://alainconnes.org/wp-content/uploads/Hochschild-homology-trace-map-and-%CE%B6-cycles-2023.pdf)

### Exact finite kernel, including multiplicity

For an off-critical `rho`, `q_rho(t)=1/(1/2+it-rho)` is smooth with polynomially bounded derivatives. Both it and its inverse multiplier preserve Schwartz space and the closed zeta relation space. Thus `M_(1/2+it)-rho` is invertible on the target quotient. Intertwining annihilates an entire generalized source block: if `(A-rho)^m v=0`, then the invertible target operator's `m`th power kills `Gamma sigma_Z v`, forcing that vector to vanish. This argument does not assume an eigenbasis.

For `rho=1/2+i gamma`, every derivative evaluation below the zero's multiplicity is continuous and vanishes on the ideal and its closure. The recovery functional has exactly the phase and factorial in H23:

\[
\Xi_\rho[f]=\sum_{j<m}\frac{i^{-j}}{j!}f^{(j)}(\gamma)\epsilon^j,
\qquad
\Xi_\rho\Gamma[F]=\sum_{j<m}\frac{(MF)^{(j)}(\rho)}{j!}\epsilon^j.
\]

Indeed, the `j`th real derivative of `MF(1/2+it)` contributes `i^j`. Given the expressly retained prior identity `J_Z sigma_Z=1`, these evaluations supply a left inverse on the direct sum of critical blocks. Combining this with the off-critical calculation proves exactly `ker(Gamma sigma_Z)=E_(Z,off)`. The argument neither assumes RH nor asserts global injectivity of `Gamma`.

## 3. Raw zero mode and the proposed repair

Printed p. 94 asserts the raw source families are smooth sections at zero; p. 95 explicitly gives their zeroth coefficient as `L^(-1/2) zeta(1/2) psi(0)`. The incompatibility is literal. Printed p. 100 also has `L -> 0` in a limit that requires `L -> infinity`. Both were visually verified. [Primary source, Proposition 5.2 proof and Theorem 5.4 proof](https://alainconnes.org/wp-content/uploads/Hochschild-homology-trace-map-and-%CE%B6-cycles-2023.pdf)

The note's counterexample is exact: `a_(phi*)=zeta(1/2)Mphi*(1/2)=xi(1/2)`. For real `0<s<1`, the alternating eta series paired in consecutive terms is strictly positive, while `1-2^(1-s)<0`; therefore `zeta(s)<0`. Gamma has no zero here, so `xi(1/2)` is nonzero. No extra condition in `V` cancels this Mellin value. Raw smooth extension at `L=0` therefore fails.

The replacement `H#=M_nonzero,flat direct-sum O` is explicit and retains the zero line. Reconstruction adds `L^(-1/2)a e_0` in normalized Fourier coordinates, which corresponds to the constant function `a/L` on a circle of length `L`. These two different exponents are correct. Covering transfer has coefficient `sqrt(n) xi_hat(nL,nj)`; at `j=0` this sends the reconstructed zero mode to `L^(-1/2)a(nL)`, proving the claimed action on the renormalized coordinate.

### Heat-limit proof audit

For every fixed Schwartz seminorm `p_(p,q)`, the normalized dilation in H38 satisfies a bound of the form

\[
p_{p,q}(e^{-r/2}\phi_*(e^{-r}\,\cdot))\le C_{p,q}e^{C'_{p,q}|r|}.
\]

The Gaussian is integrable against every such exponential for fixed positive `T`. Thus the integral converges in Schwartz space, differentiation is legitimate there, and parity plus both continuous moment constraints survive. This proves `phi_T in V` without claiming uniformly bounded source seminorms as `T` grows.

The dilation identity for `E` is exact. In logarithmic coordinates it becomes translation, so Gaussian convolution yields

\[
h_T(s)=e^{-Ts^2}h(s),\qquad h(s)=\widehat{E\phi_*}(s),\quad h_T(0)=h(0)=\xi(1/2).
\]

For `n!=0`, the periodized coefficient is `L^(-1/2)h_T(2 pi n/L)`. On `0<L<=M`, its frequency has magnitude at least `2 pi/M`. Each of `m` derivatives in `L` introduces only finitely many terms with at most `m` powers of `T`, powers of frequency and `L^(-1)`, and derivatives of `h`. Split the exponential into `exp(-Ts^2/2)exp(-Ts^2/2)`. The first factor gives `exp(-2 pi^2 T/M^2)`; with `T>=1`, the second absorbs all remaining frequency powers, including those from flat weights `L^(-N)`. Using `L^(-1)=|s|/(2 pi |n|)` and further decay makes the squared sum over nonzero integers convergent. This justifies H40, its stated polynomial factor `(1+T)^m`, all derivatives at zero, and convergence in every local flat-section seminorm.

It follows that `(0,xi(1/2))` is in the closed source-generated module. Multiplication by arbitrary local smooth functions yields the full zero-line sheaf. Finally, if a closed submodule `N subset M direct-sum O` contains `0 direct-sum O`, then subtracting that component from every element shows `N=(N intersect M) direct-sum O`; its projection to `M` is closed. This proves the last quotient assertion, not merely an algebraic approximation to it.

This repair validates the retained-zero-line/nonzero-mode quotient construction as a written argument. It does not retroactively make the unmodified raw-section assertion true. The critical Schwartz quotient and the explicit map `Gamma` do not depend on accepting that raw assertion.

## 4. Original metric, Laplacian defect, and the parabola

H27 follows from `D_times U=U D-(1/2)U`, preserving `G=R*R` and the factor `2 E K`. Applying the same isometry to every representative along a relation curve preserves its complete Gram curve, not just one norm.

For real `k`, expansion with `W=A*G+GA-kG`, `L=A^2-kA`, and `B=A-kI/2` gives

\[
L^*G-GL=A^*W-WA,\qquad GL=WA-A^*GA
=WB-B^*GB-\tfrac{k^2}{4}G.
\]

No commutator with a restriction-loss operator was set to zero. Rank at most two of `W` gives rank at most four for the displayed adjoint defect, but supplies no small norm by itself. The jet polynomial is exactly

\[
L|_{E_\rho}=\rho(\rho-k)I+(2\rho-k)N+N^2.
\]

When `2rho-k!=0`, the nilpotent part factors as `N((2rho-k)I+N)` with commuting invertible second factor, preserving the kernels of every power and thus Jordan lengths. Exact positive-metric self-adjointness would force semisimplicity; the notes do not assume it. The chapter itself labels its Hodge dictionary heuristic and retains multiple-zero Jordan behavior. [Primary source, pp. 91 and 100](https://alainconnes.org/wp-content/uploads/Hochschild-homology-trace-map-and-%CE%B6-cycles-2023.pdf)

For P2, `C=G^(-1)W` is self-adjoint in the actual `G`-inner product and `||C||_G<=epsilon`. Normalize `||v||_G=1`, set `r=||Bv||_G`, and `a+ib=<v,CBv>_G`. Then `a^2+b^2<=epsilon^2 r^2` and the exact energy identity yields `x=Re z=a-r^2-k^2/4`, `Im z=b`. Completing the square gives the first bound. For the second, direct expansion gives

\[
\epsilon^2\left(\frac{\epsilon^2-k^2}{4}-x\right)-b^2
=(a-\epsilon^2/2)^2+\epsilon^2r^2-a^2-b^2\ge0.
\]

Thus P3 controls the full numerical range, including `epsilon=0`, rather than merely diagonal/eigenvalue data. Every eigenvector gives an eigenvalue in that same numerical range, even if the operator has nontrivial Jordan blocks. For positive finite error, negative real part does not imply a real spectrum, so the note correctly does not infer the primary source's RH-equivalent negative-real-spectrum conclusion.

For a positive tensor weight `k` and an actually present character `k rho`, dividing by `k^2` gives the stated enclosure for the fixed scalar `rho(rho-1)` with error `epsilon_k/k`. A separately proved limit of that ratio to zero would force its imaginary part to vanish (and real part at most `-1/4`). The notes expressly do not prove the limit.

## Remaining dependencies and final disposition

This review accepts as explicit prior inputs, rather than revalidating, the original supported coefficient construction, continuous global retraction, finite packet inclusion/right-inverse identity, original rank-two source formula, and actual arithmetic tensor tower. The correctness of the comparison implications checked above does not certify those earlier inputs. Formal-source scope and actual CI success remain with the parallel PR review.

Within the assigned scope, there are no required corrections. Keep the distinctions already present in the text: coefficient-fibre maps versus semiring completion; supported zero versus absence; a closure quotient versus an unproved closed image; full generalized blocks versus reduced eigenlines; an explicit original-metric defect versus a chosen Hodge adjoint; and a conditional error-ratio limit versus a proved arithmetic bound. With those existing qualifications intact, the two notes are mathematically suitable to merge as written.
