# Independent proof review: the symmetric spectral sum and its two Stieltjes components

Review date: 2026-09-12. Outcome: no mathematical correction found at the reviewed source hash. The entire SSP.1–SSP.37 fragment and the complete underlying PR17 research note were read. This review independently checks the exact maps, full local orders, original unit, original measure, degree filtration and transported arithmetic weight. No author TeX, main file or frozen paper was edited by this reviewer.

## Exact source objects

| Source | SHA-256 | Reading scope |
|---|---|---|
| `tex/spectral_sum_stieltjes_pair.tex` | `54fcf2d61bb2fdd70f3c76ac3b5cf6450d225b9b5bd7991a3c84b29c33c50844` | Complete SSP.1–SSP.37 read at predecessor hash `d7ddb9061c1015a6c3c9548b05cf2a9dda85fc8bf8592fc522d39cb852cce4b7`; explicit module action and SSP.15a proof reread at `b92f4e139dcf82a49ccea16a76e89dafa21425fcd3a3d6ff487f43b9ce2653d1`; final title, squared-norm wording, nonnegative index sets and complete finite-degree primitive proof reread and checked. |
| `sources/web_pr17_spectral_sum/workbenches/tau-spectral-sum/RESEARCH_NOTE.md` | `551e3fe89b4409d5ed1eefacfaac4cb7d9c1291978127de1b4f989b272bd24a47` | Complete sections 1–7, including original relation ideal, matrix weight, full nilpotent pushforward, cochain primitives and calibration scope. |
| `tex/theta_stieltjes_pair.tex` | `15b2b20e2da43826024585431754047548237cca0ba4b495ffc156ecd62fa21b` | Complete SP.1–SP.35; original H convention, full local branch maps, V unit and half-line isometry checked as dependencies. |

No further external literature theorem is introduced in SSP. Its analytic source inputs are the already constructed actual theta packet and its stated decay; the PR17 note explicitly identifies those as prior inputs. This review does not convert that attribution into a fresh independent proof of all preceding theta analysis.

## 1. The original signs and invariant ideal

The two quadratic coordinates are retained with different domains:

\[
x_h=-(s-1/2)^2,\qquad h(s)=(-1)^D H(x_h),\qquad
Z=s_1+s_2-1,\quad x=-Z^2,\quad\Delta=(s_1-s_2)^2.
\]

Let `r=s_1−s_2`. Then `s_1=1/2+(Z+r)/2`, `s_2=1/2+(Z−r)/2`. Expanding every even monomial of `h(1/2+y)` yields exactly SSP.3 with the factor `4^(−j)` and the displayed even and odd binomial coefficients. Thus

\[
h(s_1)=A_0+rZA_1,\qquad h(s_2)=A_0-rZA_1,
\]

and at x=0,

\[
A_0(0,\Delta)=(-1)^D H(-\Delta/4),\qquad
A_1(0,\Delta)=(-1)^{D+1}H'(-\Delta/4)/2.
\]

These identities include r=0 as polynomial identities. The first polynomial has leading coefficient `4^(−D)`, not one. The alternative positive-square polynomial would be `Hplus(y)=(-1)^D H(-y)`; SSP consistently uses H and never replaces it by that other presentation silently.

Swap averaging of the original ideal gives `(H_0,Delta H_1)` in `C[S,Delta]`: an odd coefficient multiplying `r H_1` contributes its second factor r. This establishes both containments and every invariant lift, with no localization. Adjoining `x=−Z²` and putting `Q=Delta A_1` gives

\[
\mathcal E\cong \mathbb C[x,Z,\Delta]/(Z^2+x,A_0,ZQ).
\]

Before the last two relations, the module is `R⊕ZR`, where `R=C[x,Delta]`. Their arbitrary multiples have even coefficient ideal `(A_0,xQ)` and odd coefficient ideal `(A_0,Q)`. Therefore the full quotient is `B_e⊕ZB_o` with exactly SSP.6. This argument holds in nonreduced local algebras.

## 2. Both exact sequences, with full nilpotents

The maps `alpha[b]=[xb]` and `beta[a]=[a]` have their stated module and algebra types. Their composites are multiplication by x on their respective domains. The product of two pairs is `(ac−alpha(be), beta(a)e+beta(c)b)`. In particular alpha is not asserted to be a unital algebra map: its precise product identity is `alpha(b)alpha(c)=x alpha(bc)`.

Since `A_0(0,Delta)` is nonzero, the prime x does not divide A_0. If `xb=A_0c+xQe`, divisibility by x forces `c=xc_1`; then `b=A_0c_1+Qe`. This proves alpha injective in the full quotients. Beta is onto by its quotient definition. The even and odd dimensions follow from the two one-factor reflection spaces of dimension D: the even part is their two symmetric squares, of total dimension `D(D+1)`, and the odd part is their mixed tensor, of dimension `D²`.

The cokernel of alpha is `R/(A_0,x)`. The exact substitution `Delta=−4x_h`, with inverse `x_h=−Delta/4`, identifies it with `A_H=C[x_h]/H`. It preserves each local order and yields `rho_0[a]=[a(0,−4x_h)]`.

For the second sequence, finite dimensionality of `R/(A_0,Q)` supplies a nonzero annihilator in x alone and one in Delta alone. A common irreducible divisor of A_0 and Q would divide both annihilators. Over C their irreducible factors are respectively `x−a` and `Delta−b`, so such a common divisor cannot exist. Thus A_0 and Q are coprime. If `Qp=A_0c+xQe`, coprimality forces `A_0 | p−xe`, proving the exact colon calculation

\[
(A_0,xQ):Q=(A_0,x).
\]

It follows that `R/(A_0,x)→ker beta`, `[p]↦[Qp]`, is both well-defined and bijective. Composing the polynomial-variable isomorphism gives precisely

\[
\iota_0[q]=[Qq(-\Delta/4)].
\]

The exact sequences are sequences of `C[x,Delta]`-modules with action on A_H given by `x↦0`, `Delta↦−4x_h`. The full class Q must be formed before the coefficient ring is specialized. Multiplication by `Z=S−1` is `[[0,−alpha],[beta,0]]`. Hence its kernel is `(iota_0 A_H,0)` and its cokernel is A_H through rho_0 on the even component; neither statement removes nilpotents.

The additional ideal-multiplication formula SSP.15a also checks. Since `xQ=0`, one has `Q²=Q Q(0,Delta)` in B_e. Its coefficient transported by `Delta=−4x_h` is exactly

\[
\mathfrak c_H=2(-1)^D x_hH'(x_h)\pmod H.
\]

Thus `iota_0(q)iota_0(t)=iota_0(mathfrak c_H qt)`. This gives the exact algebra correspondence from the inherited kernel ideal to the module A_H equipped with product `q star t=mathfrak c_H qt`; it does not silently equip the module injection with the ordinary unital product. In particular the derivative's vanishing and nilpotent coefficients at repeated roots remain in the multiplication law.

## 3. Exact original unit on the defect

SP's full unit is `V(x_h)=(-1)^D Phi(x_h)/H(x_h)` modulo H. Its product in the original tensor quotient is `V(x_1)V(x_2)`, with

\[
x_1=-(Z+r)^2/4,\qquad x_2=-(Z-r)^2/4.
\]

Reflection in both original variables fixes this product, so it gives `(u_e,0)` in the parity decomposition. Its inverse remains the original product inverse, proving invertibility of U_e and U_o. Multiplication proves the intertwiners with alpha and beta.

The specialization `Z=0, Delta=−4x_h` is the original equation `s_2=1−s_1`, followed by the reflection-invariant quotient. It sends both x_1 and x_2 to x_h, hence sends the full unit to `V(x_h)^2` in A_H. This proves the rho_0 intertwiner with all Taylor coefficients. In the kernel, `xQ=0` gives `u_e Qp=Q u_e(0,Delta)p`, proving the identical full V² action through iota_0. No value at a root replaces the Taylor class.

## 4. Orbit cardinalities and full coordinate maps

SSP.20 uses literal orbit sums. A diagonal tensor column has squared Euclidean coordinate length one; a column with two distinct basis vectors has squared length two. Therefore `L=(I*I)^(−1)I*` is an exact left inverse of the invariant inclusion I and `IL=(1+swap)/2`. Since `T⊗T` commutes with swap, the two SSP.21 formulas are mutual inverses.

The symmetric-square determinant exponent is `d+1`: after triangularization, each diagonal entry of T occurs in one diagonal tensor twice and in its `d−1` mixed tensors once. The final ordering can change its sign only. Thus `|det T_s|=|det T|^(d+1)=1`. The parity basis dimensions and odd coefficient identification agree with the quotient modules above. This establishes the coordinate congruence without dividing any tensor vector by its Hilbert length.

## 5. Actual vector measure, inverse map and original degree

The PR17 coordinate Jacobian is `dt_1dt_2=du dv/2`, and the original vertical line gives `S=1+iu`, `Delta=−v²`. Substitution therefore yields exactly

\[
\mathsf W_{ac}(u)=\frac{(-1)^{a+c}}2
\int v^{2(a+c)}w_h((u+v)/2)w_h((u-v)/2)\,dv,
\quad w_h(t)=|v_h(1/2+it)|^2/(2\pi).
\]

Every finite quadratic form is the integral of the squared modulus of a nonzero polynomial in `−v²` against a positive density off a discrete set. This proves strict positivity. Evenness of w_h proves matrix evenness. The actual decay supplies convergence and Fubini for every fixed finite degree; no uniform estimate in degree or tensor order is inferred.

For x>0, the exact measure is `dLambda(x)=W(sqrt x)dx/sqrt x`. Adding the matrix quadratic forms at u and −u cancels the mixed terms in `A(u²)+iu B(u²)`. The substitution x=u² proves the unitary map from `L²(Lambda)⊕L²(x Lambda)` and the stated inverse. Applying the same identity to `u f` proves the exact multiplication domain in SSP.28. The common point x=0 has no atom in this Hilbert measure; the algebraic x=0 defect is separately retained by the exact sequences, not removed by that almost-everywhere statement.

For every relative direction a, the expansion of `S^j=(1+Z)^j` gives SSP.30 with every binomial coefficient and the sign from `Z²=−x`. The permitted even and odd powers are exactly `2a+2j≤M` and `2a+2j+1≤M`. A negative odd bound is the zero polynomial subspace in the declared ambient vector Hilbert space. This proves SSP.29 and preserves all relative directions and original weighted degrees.

## 6. The actual minimum, rectangular block and original primitive

The source Gram matrices in SSP.31 follow directly from the vector monomials `Delta^a x^j` and `Z Delta^a x^j` under the proved Hilbert isometry. Their full residue columns include u_e and beta(u_e); no evaluation scalar is used. Each is a positive finite Gram matrix. Original orbit monomials with exponents below d span the quotient at degree `M≥2(d−1)`. Averaging by reflection preserves that degree, so each parity jet map is onto, including `D=1,M=2`.

For an onto map J with source Gram M, `M^(−1)J*(JM^(−1)J*)^(−1)y` is a preimage orthogonal to ker J. Pythagoras proves that its norm is the unique minimum metric. Applying this to the actual parity source yields SSP.32–33. Swap preserves the full source norm and target, so uniqueness identifies this symmetric minimum with the original full constrained minimum on a symmetric target. This establishes the stated source representative as well as the target metric.

The transported generator is `I+[[0,−alpha],[beta,0]]`. Its identity parts cancel exactly the `−2G` in the original weight. Direct multiplication gives upper block `beta*G_o−G_e alpha`. Congruence by the two positive metric square roots gives the displayed rectangular relative block B. Its singular vectors give the eigenvalue pairs `+sigma,−sigma`; its remaining kernel has dimension `D(D+1)+D²−2rank B`. The explicit unitary in the proof transports these entire eigenvalues to the original relative weight. Thus the difference D of parity dimensions and every additional zero eigenvalue are retained.

An original full local eigenvector at rho survives as a nonzero symmetric square with eigenvalue `2rho`; its relative Rayleigh quotient is exactly `4 Re(rho)−2`, establishing SSP.36 with the original factor four.

Finally, substitution in SSP.37 gives an even relation `A_0a+xQb` by taking `A=a,B=−Zb`, and an odd relation `Z(A_0a+Qb)` by `A=Za,B=b`. The two tensor differential signs match the two original primitive coefficients. The final degree proof was also checked: ordered division by the two monic polynomials gives coefficients of degree at most `M−d` and zero final remainder in the basis with both exponents below d. Swap averaging gives `B_1,B_2=swap(B_1)` of that same degree; then `A=B_1+B_2` and `B=(B_1−B_2)/r` are even in r and have degree at most `M−d` and `M−d−1`, respectively. Divisibility of the odd numerator by r is a polynomial identity, not localization. The stated algebra maps have algebraic G-lifts; alpha and iota_0 retain their module types and fixed-label linear lifts. No unsupported algebra-homomorphism type is assigned to either linear injection.

## 7. Independent repeated-root witness

As a declared algebra calibration, take `H(x_h)=(x_h+1)^2`. Then `h(1/2+z)=(z²−1)²`, D=2, and the exact formulas become

\[
A_0=((\Delta-x-4)^2-4x\Delta)/16,\quad
A_1=(\Delta-x-4)/4,\quad
Q=\Delta(\Delta-x-4)/4.
\]

On the original mixed roots `z_1=1+u`, `z_2=−1+v`, with `u²=v²=0`, direct expansion gives

\[
x=-2uv,\quad \Delta=4+4(u-v)-2uv,\quad
Q=4(u-v)-8uv,\quad Q(0,\Delta)=4(u-v)-10uv.
\]

Thus premature specialization changes the full class by exactly `2uv`. Moreover

\[
Q(\Delta-4)=-32uv\ne0,\qquad Q(\Delta-4)^2=0.
\]

This exhibits the length-two kernel predicted by A_H and its nonzero mixed nilpotent. In B_o, Q vanishes by its defining relation whereas `Q(0,Delta)=Delta²/4−Delta` does not vanish; hence the prematurely specialized expression does not even define the asserted kernel generator. A separate exact symbolic calibration by the independent audit agent records this witness and all ideal reductions. The example is not an assertion about any actual zero of zeta.

**Final scope:** SSP.1–SSP.37 is mathematically consistent at the exact reviewed hash. The review proves the relevant coordinate and module compatibilities rather than treating different presentations as unrelated. It supplies no new asymptotic norm theorem or RH conclusion beyond the finite spectral inequality explicitly proved in SSP.36.
