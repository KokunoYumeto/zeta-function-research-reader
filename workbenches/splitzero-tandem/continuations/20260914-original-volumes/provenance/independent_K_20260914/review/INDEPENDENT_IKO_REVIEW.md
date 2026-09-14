# Independent review of the complete independent-order construction

**Verdict: ACCEPTED for IKO1–19.** The full source was read, and its coordinate maps, Gamma constants, fibre bijection, full product-jet Schur determinant, actual-polynomial tail estimates, original-packet transport and arithmetic transition identity were checked directly. No mathematical defect requiring a source correction was found.

Reviewed source: `INDEPENDENT_ORDER_ORIGINAL_MAPS.tex`, SHA256 `22a42086fb808c8dca688a4d34b363539e598b79d8df2510ef62f2aaf1868513`.

This review is confined to IKO1–19. The BSL interfaces used for the original parameters, fixed source, coefficient quotient, bulk comparison, tail constants and kernel/boundary frame were read directly. This does not duplicate the separate review of the full BSL/HBL baseline calculation. The macroscopic coefficient with the full deformed field is a separate proof and review; no value for that coefficient is inferred from IKO's order comparison. No source was edited, no PDF or Lean build was run, and no numerical result was used as proof.

## IKO1–3: independent order and exact translated presentation

BSL1 fixes the original packet `k=4l+1`, `l,m>=1`, `e=1+k(m-1)`, `q=e(k+1)^2` and `c=k/2`. Therefore `k+1=4l+2` is even, `q` is divisible by four, and `k/q` tends to zero at fixed original multiplicity. The choice `L=q/4` is an integer and gives exactly `K=4L+1=q+1`. It does not change the original number of roots or their primary orders.

Let `h=(K-k)/2`. The map

\[
\mathcal T_K:\mathbb C[S]\longrightarrow\mathbb C[U],
\qquad P(S)\longmapsto P(U-h)
\]

is a unital algebra isomorphism with inverse `Q(U)->Q(S+h)`. On degree at most `N`, expansion of `(U-h)^j` gives a triangular coefficient matrix with diagonal one. In particular it preserves the degree and the complete coefficient determinant. It maps the ideal `(chi)` onto `(chi_K)`, so it induces the stated quotient isomorphism and intertwines the literal remainder maps.

If `zeta` is an original root and `w` is its divided Taylor coordinate, then

\[
(\mathcal T_KP)(\zeta+h+w)=P(\zeta+w).
\]

Every divided Taylor coefficient and every primary order is therefore unchanged. The transported boundary observation is precisely `Lambda_K=Lambda Tbar_K^-1`; its kernel equals `Tbar_K(ker Lambda)` in both directions. Finally `U=S+h` takes the original line `S=c+iy` to `U=K/2+iy` with the same real coordinate and Jacobian one. These statements prove the complete coordinate dictionary used in the source calculation.

## IKO4–5: complete Gamma mass and monic norms

For each factor of the Gamma recurrence,

\[
\left|j+\frac14+\frac{iy}{2}\right|^2
=\frac14\left(y^2+(2j+\tfrac12)^2\right).
\]

The product of its `L` occurrences proves the factor `4^-L` in the displayed Gamma identity. Thus the pullback source is exactly `beta_K Phi_L(y) d sigma(y)`, with no change in `y` or omitted source constant.

The claimed characteristic function and its constant can be derived directly as follows. In the Euler product for `|Gamma(a+iy/2)|^2`, take

\[
u=\frac{we^x}{2\cosh x},\qquad
v=\frac{we^{-x}}{2\cosh x},\qquad w>0,\ x\in\mathbb R.
\]

Then `u+v=w`, `log(u/v)=2x`, and the positive Jacobian is `w/(2 cosh^2 x)`. Consequently

\[
u^{a-1}v^{a-1}\,du\,dv
=2w^{2a-1}(2\cosh x)^{-2a}\,dw\,dx.
\]

Integration of the positive `w` factor gives

\[
|\Gamma(a+iy/2)|^2
=2\Gamma(2a)\int_{\mathbb R}e^{iyx}(2\cosh x)^{-2a}\,dx.
\]

For `a>0`, the function of `x` and all its derivatives decay exponentially. It and its Fourier transform are integrable, so Fourier inversion is valid and yields

\[
\int_{\mathbb R}e^{ity}
\frac{|\Gamma(a+iy/2)|^2}{2\pi}\,dy
=2\Gamma(2a)(2\cosh t)^{-2a}.
\]

At `a=K/4`, multiplying by `beta_K 4^L` produces the constant

\[
\beta_K 2^{2L+1-K/2}\Gamma(K/2)
=\beta_K\sqrt2\Gamma(K/2)
=(2\pi)^{K/2},
\]

since `K=4L+1`. This proves both the full mass and the characteristic function in IKO5. The moment generating function on `|t|<pi/2` follows on the stated domain: the original Gamma density has exponential rate `pi/2` up to powers, and multiplying by the finite polynomial `Phi_L` preserves integrability on every strictly smaller strip.

The proposed exponential generating function has coefficient of `y^j` in its `j`th polynomial equal to one. For small real `z,w`, the cosine addition identity gives

\[
\int (1+z^2)^{-K/4}(1+w^2)^{-K/4}
e^{y(\arctan z+\arctan w)}\,dm_{0,K}(y)
=(2\pi)^{K/2}(1-zw)^{-K/2}.
\]

Differentiation under the integral is justified by an exponential majorant within the same strip. Comparing the `z^i w^j` coefficients proves orthogonality and squared norm `(2pi)^(K/2) j!(K/2)_j`. Multiplication by `i^j` after `y=(S-c)/i` makes the resulting polynomial monic in `S` and preserves that norm, because the phase has absolute value one.

For the last equality of IKO5, the exact factor calculation is

\[
\begin{aligned}
\beta_K\gamma_j
\prod_{a=0}^{2L-1}(j+a+\tfrac12)
&=\beta_K\sqrt{2\pi}\,j!
\frac{\Gamma(j+1/2)}{\Gamma(1/2)}
\frac{\Gamma(j+K/2)}{\Gamma(j+1/2)}\\
&=(2\pi)^{K/2}\frac{j!\Gamma(j+K/2)}{\Gamma(K/2)}.
\end{aligned}
\]

The cancellation retains `Gamma(1/2)=sqrt(pi)` and the whole mass. At `L=0`, `K=1` and `beta_K=1`, giving exactly the original `sigma` source. The argument is pointwise in each finite `L`; it does not require a uniform small generating-function neighbourhood as `L` varies.

## IKO6–9: exact affine fibre inverse and full observed quotient

Every root of `chi` has imaginary part `(2b-k)gamma`, which is nonzero because the original `k` is odd. Every root `c+t_j` of `f_L` is real and distinct. Hence the two polynomials are coprime for every finite independent `L`.

In a primary divided-jet block, multiplication by `f_L` is triangular with diagonal `f_L(zeta)`. Its determinant on that block is `f_L(zeta)^e`. Multiplying the blocks gives exactly IKO6, with the displayed real and imaginary displacements and their multiplicities. No derivative factorial appears because the chosen coordinates are divided Taylor coefficients.

The forward fibre map in IKO7 is multiplication by `f_L`. Conversely, if `Q` is zero at every distinct root of `f_L`, polynomial division gives a unique `P=Q/f_L` of degree at most `N`. Its complete `chi` jets satisfy

\[
U_{f_L}\mathsf E_\chi P=\mathsf E_\chi Q
=U_{f_L}\mathsf E_\chi z.
\]

Invertibility of `U_fL` and of the complete divided Taylor map gives `J_N P=z`. This proves both surjectivity and uniqueness on the exact affine fibres, including `N=q-1` and the zero relation space. The relation injection is the actual map `P_(N-q)->P_(N+L)`, `Q->f_L chi Q`.

On those product jets, `Y=U_fL E_chi z`, so the observation in IKO8 returns exactly `Lambda z`. Its stated inverse unit is required and is present. Thus the original kernel and nilpotent jet coordinates are preserved by this map.

For any list of divided evaluations, evaluation on the monic orthogonal basis gives precisely the stated kernel Gram. Hermite interpolation modulo `chi f_L` has dimension `q+L`; because `N+L+1>=q+L`, the joint evaluation is onto. Its Gram is positive definite, as is the bottom block and its Schur complement `C_(L,N)`.

If `E` is a surjective observation on a positive source metric `H`, the minimum norm at observation `v` is `v^*(E H^-1 E^*)^-1 v`. This follows by the minimizer `H^-1 E^*(E H^-1 E^*)^-1 v` and orthogonal completion of the square. Applied to the product evaluation, the upper-left inverse block is `C_(L,N)^-1`. The exact identity `||P||_(m0K)^2=beta_K ||f_LP||_sigma^2` then gives IKO9 in the original remainder frame. In particular the coefficient maps appear on the correct sides as `E_chi^* U_fL^* C^-1 U_fL E_chi`.

At `L=0`, all bottom blocks and additional columns are empty and `beta_K=1`, so the construction returns `G_N^sigma` without a limiting argument.

## IKO10–13: mixed determinant and both finite return presentations

Let `V=[A,B]` and `J=diag(I_L,-I_L)`. The definitions give exactly

\[
C_{L,N}=K_{\chi,N}+AA^*-BB^*
=K_{\chi,N}+VJV^*.
\]

Sylvester's finite determinant identity therefore gives

\[
\frac{\det C_{L,N}}{\det K_{\chi,N}}
=\det(I_{2L}+JV^*K_{\chi,N}^{-1}V).
\]

This is the determinant in IKO10, including its mixed off-diagonal entries. It is a positive real number because both original `q`-dimensional determinants are positive; positivity is not inferred by treating the `2L` matrix as a positive Hermitian matrix. The empty case gives determinant one.

At each degree, the fixed quotient has determinant `|det E_chi|^2/det K_chi,N`. The determinant of IKO9 is `beta_K^q |det E_chi|^2 |det U_fL|^2/det C_(L,N)`. Their ratio gives IKO11 exactly, including the signs of its logarithms and the exponent `q` on the source mass factor.

The four signs are `+,+,-,-` at `q-1,q,2q-1,2q`. Both `q log beta_K` and `2 log |det U_fL|` are independent of `N`, so their complete signed sums cancel and leave IKO12.

The same return can be checked directly in the original monic source/relation frame. For degree `N` and relation rank `r=N+1-q`, IKO5 gives a source determinant ratio `beta_K^(N+1) D_(L,N)`. The relation determinant ratio is `beta_K^r R_(chi,L,r)`. Therefore

\[
\log\frac{\det G_N^{(K)}}{\det G_N^\sigma}
=q\log\beta_K+\log D_{L,N}-\log R_{\chi,L,r}.
\]

The ranks are exactly `0,1,q,q+1`. The rank-zero relation determinant is one. Taking the four signs yields the negative scalar low relation term and the two positive high relation terms of IKO13. This independently checks that IKO12 and IKO13 compute the same scalar in the same original quotient frame.

## IKO14–16: full tails with the actual macroscopic polynomial

The three inequalities for `Phi_L(qz)/Phi_L(q)` follow factor by factor from `(z^2+(t_j/q)^2)/(1+(t_j/q)^2)`. They hold for the actual `Phi_L`; there is no determinant replacement by a monomial. The bulk ratio between the `chi` and power forms is `exp(psi_chi)` because the same `Phi_L` occurs in both forms. The BSL7 logarithmic ratio bounds therefore apply to their common polynomial coefficient space.

The source threshold implies `k sqrt(d+g)/q<=epsilon/2`. Pairing a displacement `zeta` with `-zeta` proves

\[
|\chi(c+iy)|^2\leq(y^2+k^2(d+g))^q.
\]

The paired reverse inequality on `1<=z<=2` gives the stated lower bound `q^(2q)(3/4)^q`; on the inner interval it gives the upper bound `q^(2q)(2epsilon^2)^q`. These are in the correct directions for the bulk denominator and inner numerator respectively.

For any source polynomial `P` of degree at most `r-1`, write `Q(z)=P(c+iqz)`. Its degree remains at most `q`. The Legendre bound from CTR40 and the Gamma upper/lower density bounds give the inner ratio at most

\[
\frac{2\epsilon r^2}{\sqrt{\cos1}}
\left[\frac43\,(2\epsilon^2)\,8^2\exp(2\pi)\right]^q.
\]

Since `epsilon=2^-10`, the bracket is exactly `(4/3) 2^-13 exp(2pi)`. Both numerator and denominator contain the full factors `Phi_L(q)`, `q^(2q)` and the Jacobian `q` before cancellation. The homogeneous power form has a stronger lower and upper comparison, so the same bound holds there. This proves IKO15 for the actual macroscopic multiplier, including rank one.

For the far tail, pairing gives the extra exponent `q/(4*64^2)` relative to `q^(2q)|z|^(2q)`. The inverse bulk lower factor adds `q log(4/3)`; their sum is less than `q/2`. The actual polynomial exponent is

\[
D=2q+2L+2r-2\leq\frac92q\leq5q
\]

for `L<=q/4` and `r<=q+1`. The proof therefore includes the full added degree `2L`.

For `z>=64`, `log(z/64)<=(z-64)/64`, so

\[
\int_{64}^{\infty}z^D e^{-qz}\,dz
\leq\frac{64^D e^{-64q}}{q-D/64},
\qquad q-D/64\geq59q/64.
\]

Counting both tails and bounding `2r-2<=2q` gives exactly the coefficient printed in IKO. Its exponential bracket is greater than `20`: the displayed elementary estimates give the stronger lower bound `64-8-30-4-1/2=43/2`. The inequality `log(131/32)<2` follows already from `exp(2)>1+2+2=5>131/32`. Since `r<=2q`, the remaining prefactor is at most `512q/(59 sqrt(cos 1))`. Thus the derived `exp(-20q)` bound is contained in the retained `kappa_F` with `exp(-19q)`.

For both full forms, positivity and these two tail inequalities imply

\[
0\leq t_H=\log\det\left(I_r+(H^B)^{-1/2}(H^I+H^F)(H^B)^{-1/2}\right)
\leq r\log(1+\kappa_{I,r}+\kappa_F)=L_r.
\]

The bulk density ratio has each generalized eigenvalue between `exp(b_-)` and `exp(b_+)`. Adding the two full tail corrections, with their opposite signs, gives IKO16:

\[
rb_- -L_r\leq\eta_{L,r}\leq rb_++L_r.
\]

## IKO17: exact original-packet transport and its order

Let `eta_(L,r)=log det A_(chi,L,r)-log det A_(0,L,r)`. The difference of the actual relation ratios has the exact identity

\[
\log R_{\chi,L,r}-\log R_{0,L,r}
=\eta_{L,r}-\eta_{0,r}.
\]

Here the second `0` in `eta_(0,r)` refers to `L=0`, while `A_(0,L,r)` uses the homogeneous relation polynomial; the displayed definitions fix this indexing unambiguously. Substitution in IKO13 gives the signs `+,+,-` at ranks `q,q+1,1` printed in IKO17.

Each difference of the two errors is bounded in absolute value by `r(b_+-b_-)+2L_r`. Summing the three ranks gives `q+(q+1)+1=2q+2`, hence the exact stated finite bound. No rank or tail contribution is dropped.

At fixed original `d,g,m`, the BSL constants obey

\[
|a_k|=\frac{k(k+2)(g-d)}{3e(k+1)^2}\leq\frac{g-d}{3e},
\]

\[
d_\chi\leq\frac{2(d+g)^2}{3e^3 k^2\epsilon^4},\qquad
b_+-b_-=|a_k|(\epsilon^{-2}-64^{-2})+2d_\chi=O(1/e).
\]

The inner and far bases give exponentially small tail constants, including the polynomial rank factors. Therefore the total finite bound is `O(q/e)`. Dividing by `q^2` gives `O(1/(eq))->0`. This proves the asserted `o(q^2)` transport on `L=q/4` while retaining every original root and the complete multiplying polynomial. It does not evaluate the separate homogeneous macroscopic coefficient.

## IKO18–19: invariant arithmetic combination and observed transition

The fixed arithmetic relation is `B_ar=B_sigma+delta_sigma`. Since `T_(k;L)=B^(K)-B_sigma` by its actual four-endpoint definition, substitution gives exactly

\[
B_{\rm ar}=B^{(K)}-T_{k;L}+\delta_\sigma.
\]

Subtracting two independent orders gives IKO19. Subtraction of three such equalities gives the additive cocycle identity with no additional constant. Thus a new value of the Gamma order changes the baseline and comparison return together, through the explicit finite source and relation determinants; their stated arithmetic combination is invariant.

When `L_b>=L_a`, write `g=f_(L_b)/f_(L_a)`. It is a genuine polynomial with the indicated distinct real roots and a unit on every original `chi` primary block. Multiplication by `g`, with inverse division on its zero-product-jet fibre, is exactly the IKO7 construction relative to source `m_(0,K_a)`. The full norm factor in that transition is `beta_(K_b)/beta_(K_a)`, since

\[
\|P\|_{m_{0,K_b}}^2
=\frac{\beta_{K_b}}{\beta_{K_a}}\,\|gP\|_{m_{0,K_a}}^2.
\]

Its observation returns the same original `Lambda` by the inverse quotient germ as in IKO8. This confirms the transition's exact source map, including its positive constant; the source density definitions already retain that constant even though the final cocycle involves only the cancelled four-endpoint quotient sum.

For each order, BSL20 gives the kernel/boundary determinant product in the same original coefficient frame. Its full frame determinant has signed coefficient zero over the four endpoints. Applying this identity at the two orders transports their combined signed sum and their exact difference through the original observed kernel and boundary factors. Individual factor changes are defined by their actual restricted and quotient metrics; no individual factor is assigned the entire combined comparison value.

The claimed comparable independent order is therefore constructed on the original packet. The mathematical scope of this acceptance is the exact maps, source/norm identities, determinant presentations, full-tail transport and invariant arithmetic transition. The accompanying deformed-equilibrium and product calculations supply their own macroscopic coefficients in the disjoint author/reviewer lanes.
