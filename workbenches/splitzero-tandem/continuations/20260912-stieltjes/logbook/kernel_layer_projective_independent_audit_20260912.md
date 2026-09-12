# Independent projective-shell algebra audit — 12 September 2026

This is the bounded independent verification requested by the kernel-layer
source auditor. It checks the local and global ratio algebra, the exact
relation between monic and homogeneous shells, and the common quotient
and paired image. It does not edit the cumulative TeX or source delivery.
The parent source audit's three-atom example was read directly in
`work/kernel_layer_source_audit_20260912.md`.

## 1. Exact local ratio and every multiplicity

Let

\[
h(s)=\prod_{\rho\in Z}(s-\rho)^{m_\rho},\quad
0\notin Z,\quad
E=\mathbb C[s_1,s_2]/(h(s_1),h(s_2)),\quad z=s_1s_2^{-1}.
\]

The invertibility of `s_2` follows from `gcd(s,h)=1`, with its inverse
given by any Bezout identity. CRT retains all ordered local factors

\[
E\simeq\prod_{(\rho,\sigma)\in Z^2}
R_{\rho,\sigma},\qquad
R_{\rho,\sigma}=\mathbb C[x,y]/(x^{m_\rho},y^{m_\sigma}),
\]

where `s_1=rho+x`, `s_2=sigma+y`. Write `m=m_rho`, `n=m_sigma`.
The exact local difference is

\[
\delta=z-\rho/\sigma
=\frac{\sigma x-\rho y}{\sigma(\sigma+y)}.
\]

The denominator is a unit with constant term `sigma^2`. Every monomial
of degree `m+n-1` vanishes in `R_(rho,sigma)`, so
`delta^(m+n-1)=0`. At degree `q=m+n-2`, only the term with exponents
`m-1,n-1` survives. Consequently

\[
\delta^{m+n-2}
=\binom{m+n-2}{m-1}
 \frac{\sigma^{m-1}(-\rho)^{n-1}}{\sigma^{2(m+n-2)}}
 x^{m-1}y^{n-1}\ne0.
\]

All constants are nonzero over `C`; the displayed monomial is a member
of the quotient basis. This includes `m=n=1`: the exponent on the left
is zero, its value is `1`, and the nilpotency index of `delta=0` is one.
Thus the exact local minimal polynomial of `z` is
`(T-rho/sigma)^(m+n-1)`.

For completeness, if a polynomial has first nonzero Taylor coefficient
at degree `j` about `rho/sigma`, evaluation gives `delta^j` times a unit.
It is zero exactly when `j>=m+n-1`. This proves the whole local
annihilator ideal, beyond the displayed two powers.

The nonzero-centre assumption is material. If the numerator centre is
zero, while the denominator centre remains nonzero, the difference is
`x/(sigma+y)` and its nilpotency index is `m`, losing the `n-1` term.
If the denominator centre is zero, the declared ratio need not exist.
Neither exception occurs for the stated domain.

## 2. Global minimal polynomial and the algebra embedding

Let `Rho` be the set of distinct ratios of ordered centres and put

\[
L_r=\max_{\rho/\sigma=r}(m_\rho+m_\sigma-1),\qquad
\mu_z(T)=\prod_{r\in\mathrm{Rho}}(T-r)^{L_r}.
\]

A polynomial annihilates `z` precisely when it annihilates it in every
local factor. Its annihilator ideal is therefore the intersection of
the local principal ideals. Coincident ratio factors contribute their
maximum exponent; distinct factors are coprime and contribute their
product. Hence evaluation induces the exact unital algebra embedding

\[
\iota_z:\mathbb C[T]/(\mu_z)\hookrightarrow E,
\qquad [f]\longmapsto f(z),
\]

with image `C[z]`. In particular the diagonal pairs all contribute to
the ratio `1`; their exponents must not be counted additively.

If `D_z=deg(mu_z)`, the powers `1,z,...,z^(D_z-1)` are independent:
a dependence would be an annihilating polynomial of smaller degree.
Division by the monic `mu_z` expresses every later power in their span.
Thus the homogeneous shell map

\[
\mathbb C[T]_{\le N}\longrightarrow E,
\qquad f\longmapsto s_2^Nf(z)
\]

has image dimension `min(N+1,D_z)`, because multiplication by `s_2^N`
is invertible. Its kernel consists exactly of the degree-at-most-`N`
multiples of `mu_z`. Multiplying the image by the original arithmetic
unit `U=upsilon_h tensor upsilon_h` preserves these linear facts. The
map `f -> U s_2^N f(z)` is a linear map; the factors `U s_2^N` do not
make it a unital algebra morphism. The algebra embedding is the
explicit `iota_z` above.

The original summed generator has a precise adjacent-shell action:

\[
M_{s_1+s_2}\bigl(U s_2^Nf(z)\bigr)
=U s_2^{N+1}(1+z)f(z).
\]

This is valid in the original quotient algebra, for every retained
nilpotent component. It is well-defined on the shell kernel because
`mu_z | f` implies `mu_z | (1+T)f`. The ratio subalgebra by itself is
not being assumed invariant under the summed generator. For example,
distinct diagonal centre pairs have the same ratio `1` and different
sums `2rho`, so the sum cannot be a function of the ratio on those
reduced fibres.

## 3. Exact monic-to-homogeneous comparison

Let `H_N` be the vector space of homogeneous polynomials of degree `N`
in `s_1,s_2`. For the actual monic orthogonal polynomials `p_j`, define

\[
T_N(s_1^j s_2^{N-j})=p_j(s_1)p_{N-j}(s_2),\qquad
L_N=T_N-\operatorname{incl}_{H_N}.
\]

Each product has its displayed leading monomial and all other terms
of total degree at most `N-1`. Therefore
`L_N:H_N -> P_(<=N-1)` is an exact linear map. For `N=0` it is zero,
with `P_(<=-1)={0}`. If `J` is the original full remainder map followed
by the original arithmetic unit, then

\[
A_{\rm orth}=JT_N,
\quad A_{\rm hom}=J\operatorname{incl}_{H_N},
\quad A_{\rm orth}-A_{\rm hom}=JL_N.
\]

The complete filtered polynomial space is preserved by the monic
triangular change of basis. Its single-shell image under `J` retains
the correction `JL_N`; no assertion about equality of those images
follows merely from monicity.

The parent audit's finite counterexample checks exactly. Give equal
positive mass to the three points `s=1/2-i,1/2,1/2+i`. Then

\[
p_0=1,\qquad p_1=s-\tfrac12,\qquad
p_2=(s-\tfrac12)^2+\tfrac23.
\]

Their sampled values are respectively `(1,1,1)`, `(-i,0,i)`, and
`(-1/3,2/3,-1/3)`, whose Hermitian cross inner products vanish. With
`h=s-1/2`, unit `1`, `k=2`, `N=1`, both orthogonal shell columns have
zero jet, whereas both homogeneous columns have jet `1/2`. Thus
`rank A_orth=0`, `rank A_hom=1`. This is a finite polynomial model
counterexample to the general shell-replacement claim. It does not
identify `1/2` as an actual zero of `g` or substitute this discrete
measure for the original arithmetic measure.

## 4. The common quotient and the full paired image

The following statements apply to any two linear maps
`a:H->I_a`, `b:H->I_b`, with their codomains taken to be their images.
Write `K_a=ker a`, `K_b=ker b` and

\[
Q=H/(K_a+K_b),\qquad
\Gamma=\operatorname{im}(a,b)\subset I_a\oplus I_b.
\]

The induced maps

\[
q_a:I_a\twoheadrightarrow Q,\ a(v)\mapsto[v],\qquad
q_b:I_b\twoheadrightarrow Q,\ b(v)\mapsto[v]
\]

are well-defined because their respective kernels are in `K_a+K_b`.
Their kernels are precisely

\[
\ker q_a=a(K_b),\qquad \ker q_b=b(K_a).
\]

For example `[v]=0` means `v=u+w` with `u in K_a`, `w in K_b`, and
then `a(v)=a(w)`; the converse is immediate. The quotient has the exact
universal property of a common quotient relative to the given domain
maps: if `f:I_a->T`, `g:I_b->T` satisfy `fa=gb`, this common map on
`H` kills both kernels and factors uniquely through `Q`. This is a
vector-space universal property. Neither shell map is presumed to be
an algebra homomorphism, so no quotient-algebra structure is asserted.

The map `(a,b)` has kernel `K_a intersect K_b`, proving

\[
H/(K_a\cap K_b)\simeq\Gamma.
\]

Moreover the paired image is the exact fibre product

\[
\Gamma=I_a\mathbin{\times}_Q I_b.
\]

One inclusion follows from `q_a a=q_b b`. Conversely suppose
`q_a(a(u))=q_b(b(v))`. Write `u-v=w_a+w_b`, with `w_a in K_a`,
`w_b in K_b`. Then `w=u-w_a=v+w_b` satisfies
`a(w)=a(u)` and `b(w)=b(v)`, proving the converse. This also proves
the exact sequence

\[
0\longrightarrow\Gamma\longrightarrow I_a\oplus I_b
 \xrightarrow{\ (x,y)\mapsto q_a(x)-q_b(y)\ }Q
 \longrightarrow0.
\]

The first and second projections of `Gamma` have respective kernels
`{0} direct_sum b(K_a)` and `a(K_b) direct_sum {0}`. A linear map
`T:I_a->I_b` satisfying `Ta=b` exists exactly when `K_a subset K_b`;
it is then unique. This condition is proved by evaluating on `K_a`
in one direction and by representative-independence in the other.
Without it, the paired image still gives the complete exact relation.

`Q` need not be an ambient intersection of the two images. For example,
on `H=C^2`, `a(u,v)=u`, `b(u,v)=v`, both image spaces are `C`, but
`K_a+K_b=H`, so `Q=0`. Nor should `Gamma` be called the graph of a
function from `I_a` unless the displayed kernel condition holds.

For the actual monic comparison one has additionally

\[
\Gamma=\{(A_{\rm hom}v,A_{\rm hom}v+JL_Nv):v\in H_N\}.
\]

Thus the invertible ambient shear `(x,y)->(x,x+y)` sends
`im(A_hom,JL_N)` exactly to the paired shell image. This retains the
entire lower-degree correction as an explicit morphism.

## 5. Optional stronger algebra-retraction result

For a local factor with nonzero centres, the inclusion of its ratio
subalgebra `C[delta]` is an algebra retract precisely when
`min(m,n)=1`. If `m=1`, then `x=0` and
`y=rho z^-1-sigma`, so the ratio subalgebra is the whole local algebra.
If `n=1`, then `y=0` and `x=sigma z-rho`, with the same conclusion.

If `m,n>=2`, put `L=m+n-1` and identify `C[delta]` with
`C[t]/t^L` by `delta -> t`. In any proposed algebra retraction,
the images of `x` and `y` have zero constant term because they are
nilpotent. Their linear coefficients must also be zero: a nonzero
linear coefficient of the image of `x` would give a nonzero coefficient
of `t^m` in its `m`-th power, since `m<L`; the same argument uses `n<L`
for `y`. The exact rational expression for `delta` then has zero linear
coefficient under the map, contradicting its required image `t`.

For the global algebra `E_h tensor E_h`, the ratio-subalgebra inclusion
has a unital algebra retraction if and only if `h` is squarefree.
If squarefree, `E=C^(Z^2)` and `C[z]=C^Rho`; choosing one ordered pair
for each ratio gives a retraction by evaluation at those chosen pairs.

For the converse let `M=max m_rho>=2`. The ratio-`1` factor of the
ratio algebra is `C[t]/t^(2M-1)`. Compose a proposed retraction with
its projection to this factor. A unital homomorphism from the product
of the local factors of `E` into this local target selects exactly one
factor: the orthogonal source idempotents must map to orthogonal
idempotents of a local ring, each `0` or `1`, whose sum is `1`.
Because `z` has target constant term `1`, the selected ordered pair
has ratio `1`, hence identical centre and equal multiplicity `m<=M`.
Its two nilpotent coordinates have nilpotency exponent `m<2M-1`.
The preceding linear-coefficient argument again makes the image of
`z-1` have zero linear coefficient, contradicting its required image
`t`. This proves the obstruction while retaining the explicit ratio
embedding and adjacent-shell generator map.

## Audit outcome

The requested local exponent, global maximum rule, common quotient,
induced image maps, and paired-image comparison are correct with the
types and nonzero-centre hypotheses displayed above. The substantive
exceptions to avoid are: treating a shell unit multiple as a unital
algebra embedding; treating the common quotient as the ambient
intersection; treating the paired relation as a function without the
kernel inclusion; or using the homogeneous shell rank for the original
orthogonal shell without its retained lower-degree map.
