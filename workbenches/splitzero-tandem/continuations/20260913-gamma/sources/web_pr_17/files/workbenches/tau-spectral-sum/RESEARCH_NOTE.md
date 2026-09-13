# Spectral-sum descent with the relative arithmetic fibre retained

Owner-directed continuation, 12 September 2026. Draft for review; no purity or RH theorem is claimed. Base: PR #14 at `3bff1b2bd87dfa2592f65c5ccc231f6ee9541dfc`.

## 1. Original source and scope

Keep `G(R)={tau} disjoint-union {r^bullet}`, `e_R=0_R^bullet`, and the original square `G(Z)->G(C)` over `Z->C`. The first arithmetic quotient remains infinite. Fixed-label linear maps lift by `(lambda,v)->(lambda,Tv)` and fix external absence; a vanishing value remains the original labelled supported zero.

Use the existing `C_+=[V ->Theta B]`, `Q=B/Theta V`, `D=-x d/dx`, `g=2 xi`, and the actual source function `phi_*=(4 pi^2 x^4-6 pi x^2)exp(-pi x^2)`. For a finite packet h of actual zeros, including full orders, the prior analytic construction supplies F_h with Mellin transform g/h. Retain

$$T_h(P)=P(D)F_h,\quad T_h(hP)=\Theta(P(D)\phi_*),\quad J_hT_h(P)=\upsilon_h[P]_h,$$

where `upsilon_h=j_h(g/h)` is the full invertible jet, not the scalar e. These analytic range statements are inputs from the previous work, not newly Lean-certified here.

For k factors, the actual numerator is `P_M=C[s_1,...,s_k]_(degree<=M)`, the relation space is its intersection with `(h(s_1),...,h(s_k))`, and its theta realization is `B_(k,M)`. The canonical representative R_(k,M) is the unique least-norm lift with exactly these relations allowed. Its full jets, arithmetic class, Gram G and control W remain those of #14.

The supplied Kernel Layer Integration supplement agrees with the Symmetric Frontier note under `K=C_inverse`, `U=F`, `D=Omega`, `E_layer=b_M`, and `F_derivative=Omega^(-1)E_plus*`. Its sharper rank and original-layer identities are retained as source results, not counted again as new work.

## 2. An actual one-parameter pushforward and its resolution

Define

$$\iota_k:\mathbb C[S]\to E_h^{\otimes k},\qquad S\mapsto[s_1+\cdots+s_k].$$

Restriction of modules through this map is the exact quasi-coherent pushforward along the finite scheme morphism. Its adjunction maps are `f -> (l -> f(1 tensor l))` and `a tensor l -> a f(l)`. Applying G gives `p G(iota)=iota p`, with e sent to e and tau to tau; the morphism is over the same absolute pointed base. No finite field is substituted.

For the actual finite image E, with sum operator A, there is the free resolution

$$0\to\mathbb C[S]\otimes E\xrightarrow{SI-A}\mathbb C[S]\otimes E\xrightarrow{\mathrm{ev}_A}E_A\to0.$$

Its augmentation sends `P tensor v` to `P(A)v`. Injectivity follows from the highest polynomial coefficient. Exactness follows from

$$S^jv-A^jv=(SI-A)\sum_{i=0}^{j-1}S^{j-1-i}A^iv.$$

Dualizing with `C[S] dS` gives `SI-A^vee` in degrees 0,1, where `A^vee(lambda)=lambda compose A` is the algebraic transpose, not a Hermitian adjoint. Thus

$$\operatorname{Ext}^1_{\mathbb C[S]}(E_A,\mathbb C[S]dS)\cong E^\vee,$$

with `[sum S^j lambda_j dS] -> sum (A^vee)^j lambda_j` and inverse the constant class. With `C[b]^i=C^(i+b)`, the exact shifted statement is

$$R\operatorname{Hom}(E_A[-k],\mathbb C[S]dS[1])\simeq E^\vee[k].$$

The right adjoint is the specified module functor `RHom_(C[S])(E_h^tensor k,-)`. This is not an assertion about pushforward on all sheaves of modules. See Stacks Tags 0AVV and 0AWZ.

The same duality has the concrete pairing

$$\langle v,[P(S)dS]\rangle=\sum_{\lambda\in\operatorname{Spec}A}\operatorname{Res}_{S=\lambda}P(S)((SI-A)^{-1}v)dS.$$

Expansion at infinity gives `sum lambda_j(A^j v)`, proving the formula and perfectness. On a length-l block,

$$(SI-A)^{-1}=\sum_{j=0}^{l-1}\frac{N^j}{(S-\lambda)^{j+1}}.$$

All poles are retained before taking the trace. The further observation is

$$\operatorname{Tr}(\psi(A))=\sum_\lambda\operatorname{Res}_{S=\lambda}\psi(S)\frac{\chi_A'(S)}{\chi_A(S)}dS.$$

Here `chi_A=det(SI-A)` is the finite characteristic polynomial, not a replacement for `g=2xi`. With `psi(S)=a^S` this is the finite trace of the same diagonal scaling correspondence; its cochain sign is `(-1)^k`.

## 3. Exact symmetric-square relation algebra

Retain the coordinate morphisms

$$S=s_1+s_2,\quad r=s_1-s_2,\quad\Delta=r^2,\qquad s_1=(S+r)/2,\quad s_2=(S-r)/2.$$

Swap fixes S and negates r. Even/odd polynomial expansion gives the filtered algebra isomorphism `Phi:C[S,Delta] -> C[s_1,s_2]^swap`, with `deg(S)=1`, `deg(Delta)=2`.

Define H0,H1 without localizing away from r=0:

$$h((S+r)/2)=H_0(S,r^2)+rH_1(S,r^2),\quad h((S-r)/2)=H_0(S,r^2)-rH_1(S,r^2).$$

Then

$$\boxed{(E_h\otimes E_h)^{S_2}\cong\mathbb C[S,\Delta]/(H_0,\Delta H_1).}$$

Proof: the original ideal in `C[S,r]` is `(H0,r H1)`. Averaging an expression `H0 a+r H1 b` under `r -> -r` gives exactly `H0 a_even+Delta H1 b_odd`. Conversely both generators lie in the original ideal. Reynolds averaging is exact over C, so the invariant quotient has precisely this ideal, including all nilpotents.

The unscaled orbit sums of `s_1^i s_2^j`, `0<=i<=j<d`, give dimension `d(d+1)/2`. The associated graded Hilbert series for the original degree filtration is

$$\sum_{0\le i\le j<d}z^{i+j}=\frac{(1-z^d)(1-z^{d+1})}{(1-z)(1-z^2)}.$$

No grading of a nonhomogeneous h is asserted.

The original primitive map is explicit:

$$H_0A_0+\Delta H_1A_1=h(s_1)\frac{A_0+rA_1}{2}+h(s_2)\frac{A_0-rA_1}{2}.$$

Its two cochain primitives use `phi_* tensor F_h` and `F_h tensor phi_*`, respectively. The second primitive has a minus sign, matched by the second tensor-differential sign. For a relation of degree M, ordered division followed by swap averaging gives `deg A0<=M-d`, `deg A1<=M-d-1`.

The unit `upsilon_h tensor upsilon_h` descends to the invariant algebra and remains in its full jet map. All finite relation quotients and the transitions `M -> M+1` commute with Phi. A class killed by the next relation maps to the receiving e-zero, never to external absence.

## 4. Push the actual norm to a matrix weight, not a scalar observation

Set

$$w_h(t)=\left|\frac{g(1/2+it)}{h(1/2+it)}\right|^2\frac1{2\pi}.$$

The exact real coordinate map is

$$u=t_1+t_2,\quad v=t_1-t_2,\quad dt_1dt_2=\tfrac12du\,dv.$$

It gives `S=1+iu`, `Delta=-v^2`. For

$$P(S,\Delta)=\sum_{a=0}^{\lfloor M/2\rfloor}\Delta^a f_a(S),\qquad\deg f_a\le M-2a,$$

define

$$\boxed{\mathsf W_{ac}(u)=\frac{(-1)^{a+c}}2\int_{\mathbb R}v^{2(a+c)}w_h((u+v)/2)w_h((u-v)/2)dv.}$$

Then the original arithmetic norm is exactly

$$\boxed{\|T_h^{(2)}\Phi P\|^2=\int_{\mathbb R}f(1+iu)^*\mathsf W(u)f(1+iu)du.}$$

Proof: substitute the coordinate map and expand the finite polynomial. Exponential moments justify Fubini. Each finite matrix W(u) is strictly positive: the integrand is the squared modulus of a nonzero polynomial in -v^2 against a density positive almost everywhere. The entire nonzero g/h has only discrete zeros on these real lines. The source exponential bound also gives convergence for each fixed u.

Its scalar entry is `(w_h*w_h)(u)`. Its other entries retain the relative-coordinate moments; they are not replaced by that scalar entry.

For general k retain `S=sum s_i`, `x_i=s_i` for i<k and `s_k=S-sum x_i`. This is a polynomial isomorphism and the real Jacobian is one. Writing `P=sum x^alpha f_alpha(S)` gives

$$\mathsf W_{\alpha\beta}(u)=\int_{\mathbb R^{k-1}}\overline{\prod_{i<k}(1/2+it_i)^{\alpha_i}}\prod_{i<k}(1/2+it_i)^{\beta_i}\prod_{i<k}w_h(t_i)w_h(u-\sum_{i<k}t_i)d^{k-1}t.$$

The outer coordinate remains `S=k/2+iu`, and `deg f_alpha<=M-|alpha|`. This supplies an all-k isometry retaining the entire filtered source. Constants in exponential-moment bounds depend on h,k and the degrees; no uniform tensor bound is inferred.

## 5. Canonical control commutes with the descent

For the explicit source-coordinate matrix C and quotient-coordinate matrix U, keep

$$M'=C^*MC,\quad J'=U^{-1}JC,\quad K'=U^{-1}K(U^{-1})^*,\quad G'=U^*GU,$$

$$A'=U^{-1}AU,\quad W'=U^*WU,\quad R'=RU.$$

These follow by substituting into `K=JM^(-1)J*` and the exact constrained-minimum formula. Thus no positive metric has been freely selected. The same isometry carries the actual next relation layer and both boundary maps Y,C_rel; their cross-pairing is unchanged.

There is a further exact base/relative map. Write `W(u)=[[m0,b],[b*,Crel]]`, with `m0>0`. Then

$$f\mapsto(f_0+m_0^{-1}bf_{\rm rel},f_{\rm rel})$$

is an isometry into the direct sum weighted by `m0` and `Crel-b* m0^(-1)b`. Its inverse is `(a,z)->(a-m0^(-1)b z,z)`. The precise image of the polynomial source is retained; the ratio need not be polynomial. Multiplication by S commutes with this map. Neither the scalar mass nor positivity of this representative norm is substituted for the arithmetic Weil pairing.

## 6. Full nilpotent fibres for every tensor degree

For an ordered tuple of roots with orders m_i, the local algebra is

$$L=\mathbb C[z_1,\ldots,z_k]/(z_i^{m_i}),\quad A=\rho_\Sigma I+N,\quad N=M_{\sum z_i},\quad D_0=\sum_i(m_i-1).$$

Let `c_r=[t^r] product_i(1+t+...+t^(m_i-1))`, `c_-1=0`. Then the complete module pushforward is

$$\boxed{\pi_*L\cong\bigoplus_{r=0}^{\lfloor D_0/2\rfloor}\left(\mathbb C[S]/(S-\rho_\Sigma)^{D_0-2r+1}\right)^{c_r-c_{r-1}}.}$$

Proof and maps: on `z_i^j` define `F_i=j(m_i-j)z_i^(j-1)` and `H_i=(2j-(m_i-1))z_i^j`. Direct calculation gives `[N,F]=H`, `[H,N]=2N`, `[H,F]=-2F`. The explicit auxiliary diagonal Gram

$$\|z^\alpha\|_0^2=\prod_i\frac{\alpha_i!(m_i-1)!}{(m_i-1-\alpha_i)!}$$

makes `F=N*`. A degree-r primitive p with Fp=0 has ladder length `w+1`, `w=D0-2r`, since

$$FN^jp=j(w-j+1)N^{j-1}p,\quad\|N^jp\|_0^2=\frac{j!w!}{(w-j)!}\|p\|_0^2.$$

Orthogonal invariant complements construct all ladders; degree counts give `c_r-c_(r-1)`. The actual module map is `[P(S)]->P(rho_Sigma+N)p` on each chosen primitive. This auxiliary Gram is related to the arithmetic one by the explicit operator `G_arithmetic^(-1)G_0`; it is used for the algebraic decomposition only. All cross-ladder entries `U*G_arithmetic U` remain in control estimates.

For an occupation list n_rho with sum k, the symmetric component has graded dimensions given by

$$\prod_\rho\prod_{j=1}^{n_\rho}\frac{1-t^{m_\rho+j-1}}{1-t^j}.$$

These are polynomial orbit-count identities, not evaluations of a rational function at roots of unity. Apply the same primitive construction to invariants, with `D0=sum n_rho(m_rho-1)` and `rho_Sigma=sum n_rho rho`. Central occupation idempotents are retained even when different occupations have the same spectral sum.

For an order-three local input taken twice, the symmetric fibre has ladders

$$1,X,X^2,X^3,X^4,\qquad p=z_1^2-z_1z_2+z_2^2,\quad X=z_1+z_2,\quad Xp=0.$$

It is `C[S]/(S-2rho)^5 direct-sum C[S]/(S-2rho)`, dimension six. This is a local algebra calculation, not an assertion that zeta has a triple zero. The full arithmetic unit commutes with A and carries the ladder coordinates to the original jets.

Each occupation trace is its full dimension times `a^(sum n_rho rho)`, with dimension `product binomial(n_rho+m_rho-1,n_rho)`. The cochain trace retains `(-1)^k`. Quotienting a top ladder vector, when explicitly requested as a module quotient, makes it the supported zero; the full pushforward itself keeps it.

## 7. Exact calibration and scope

For the declared measure `exp(-t^2/2)dt`, not the arithmetic measure, the three relative directions `1,Delta,Delta^2` give

$$\mathsf W(u)=\sqrt\pi e^{-u^2/4}\begin{pmatrix}1&-2&12\\-2&12&-120\\12&-120&1680\end{pmatrix}.$$

The unscaled coordinate columns `1,Delta+2,Delta^2+12Delta+12` turn this into `sqrt(pi)exp(-u^2/4) diag(1,8,384)`. The full two-variable mass is still `2pi`. The published core checker verifies these signs, constants, algebraic primitives, sum resolution and nilpotent blocks. The longer conversation package has a separate 24-method suite, plus independent reruns of the source 18- and 22-method suites; those are not all claimed to be tests in this smaller repository checker.

The new reduction isolates the convolution mass, the relative covariance, and full-jet interpolation on one explicit filtered image. It does not prove their required uniform sublinear tensor estimate. The finite pushforward and matrix-weight model are not asserted to be lisse sheaves on Deligne's Lefschetz pencil. They supply a precisely defined product-to-one-parameter operation to study next, with its adjoint, cohomology, arithmetic trace and original supported relations retained.

References: Stacks Tags 0AVV and 0AWZ; NIST DLMF 18.2; Deligne, La conjecture de Weil II, IHES 52 (1980), 137-252. A bounded supplied French TeX window around 3.2.11–3.2.15 was reread. Its historical line 872 contains an inconsistent numerical implication and is not used as a theorem. No complete new audit of Weil II, analytic integral certificate, Lean execution, or global novelty claim is made.
