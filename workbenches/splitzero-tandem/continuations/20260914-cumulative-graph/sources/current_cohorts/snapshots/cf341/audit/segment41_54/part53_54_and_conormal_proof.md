# Authoritative shared-source audit: U0053–U0054 and an exact conormal consequence

## Read coverage and authority

I read every line 6333–7810 of `output/tau_f1_transcript_audit_2026-09-13/sources/audit_segment_U0041_U0054.md`, in two complete sequential tool reads. This includes U0053, A1860, A1912, U0054, A1914, A1936 and A1959. The mathematical authority for this report is those visible messages, with the earlier signed chain projector in A1859, lines 6042–6098, additionally read in full. Later assistant-authored compilations are not premises. The full record identifiers are:

| Locator | Message/node ID | Chain | Segment lines |
|---|---|---:|---:|
| U0053 | bbd82b42-aa50-4eeb-abf3-27b7320953d3 | 3888 | 6333–6336 |
| A1860 | 275efe72-c7eb-4763-82d1-9bf3ce0e3186 | 3890 | 6337–6340 |
| A1912 | 64c5b883-17ba-441a-b5c9-bfa6ff1ef787 | 3986 | 6341–7043 |
| U0054 | 9cde09a7-2e48-4d0c-aa8b-4d54a316f9b9 | 3987 | 7044–7047 |
| A1914 | c84c5062-8d5b-45fb-8eea-c0f4c924908e | 3990 | 7048–7051 |
| A1936 | 951e58ad-9a13-43d3-847c-6b57a8616eef | 4024 | 7052–7055 |
| A1959 | ac351c92-ca3e-47a6-9014-85f239a2760e | 4075 | 7056–7810 |

The user inputs in this range, verbatim, are:

> Okay, yeah, continue.

> ok the formalizing is in progress - you work on this

They authorize continuation of the existing program. They neither assert RH false nor authorize replacing its arithmetic object by an arbitrary spectral matrix. The second message explicitly places formalization in another ongoing activity; the requested continuation here concerns the mathematics.

## What the original program actually constructs here

A1912 retains the structural square `G(Z) -> G(C)` over `Z -> C`, with the infinite arithmetic quotient, both zeros, and the absolute base. Its sum morphism is the literal ring map

\[
\iota_k:\mathbb C[S]\longrightarrow E_h^{\otimes k},\qquad
S\longmapsto s_1+\cdots+s_k.
\]

It is restriction of scalars/finite affine pushforward of the full algebra, with the actual source identity

\[
\mathcal T_h(hP)=\Theta(P(D)\phi_*),\qquad
J_h\mathcal T_h(P)=\upsilon_h[P]_h,\qquad
\upsilon_h=j_h(g/h),\quad g=2\xi.
\]

These are at lines 6410–6496. The coefficient pushforward is thus attached to theta boundaries; it is not just a change of names on a matrix. The exact symmetric-square algebra at 6497–6597 is `C[S,Delta]/(H0,Delta H1)`, with `Delta=(s1-s2)^2`, not its reduced quotient. Its two theta primitives retain the factor 1/2 and the second tensor-differential sign. Its full relative arithmetic weight at 6598–6741 retains the Jacobian, the signs `Delta=-v^2`, the original factor `(2pi)^(-1)` in each density, and the constrained image of the polynomial family. A pointwise triangular isometry carries a relative covariance term; its image is not enlarged to all sections.

A1912 lines 6742–6789 proves congruence of the same canonical control matrices through this pushforward. Lines 6790–6910 compute the finite pushforward dual by the exact resolution with differential `SI-A`; the residue formula retains the full nilpotent resolvent. Lines 6911–7016 give the Jordan ladders in actual local tensor algebras, including their arithmetic Gram after the ladder inclusion. The proof at lines 7039–7041 explicitly states that a uniform sublinear tensor excess has not been established, and the finite pushforward has not been identified with a lisse sheaf on Deligne's pencil. That is a restriction on the conclusion actually obtained here, not a reason to ignore the constructed pushforward.

A1959 proves the mass-preserving arithmetic identity

\[
\mathcal I_{h,k}+4\int\|n_k(u)\|^2du
=\frac{\mu_h^{k-1}}{k}\mathcal I_h,
\quad \mu_h=\|F_h\|_{L^2(dx)}^2.
\]

The original fixed real/imaginary phase and the vanishing cross integral `integral conjugate(a_h) a_h' = 0` establish the identity, including the exact 1/k. This is lines 7158–7330. The full relative matrix derivative at 7331–7444 is

\[
\partial_u(j_uc)=j_u(c'+\Gamma_uc)+N_uc,
\quad N_u^*N_u=\mathsf T-\tfrac14\mathsf W'\mathsf W^{-1}\mathsf W',
\]

with the additional `C^{-1}C'` term under a moving frame. The actual operator dictionary at 7445–7506 is

\[
\mathscr U_kD^{(k)}=(k/2+iu)\mathscr U_k,
\quad\partial_u\mathscr U_k=i\mathscr U_k\mathscr L_k,
\quad\mathscr L_k=k^{-1}\sum_i\log x_i,
\quad[D^{(k)},\mathscr L_k]=-1.
\]

Consequently the Fisher identity estimates a specified conjugate observable. The graph of both derivative pieces maps by addition, inverse Mellin–Fourier transform, and the original jets into the arithmetic tensor packet. The map is explicit, but the scalar Fisher identity alone does not bound all the columns of the original interpolation matrix. A1959 expressly records this limit at 7782–7784.

The relation derivative in A1959 lines 7507–7633 is genuinely defined before the internal quotient:

\[
\mathcal P=\mathbb C[s_1,\ldots,s_k],\quad
I=(h(s_1),\ldots,h(s_k)),\quad E=\mathcal P/I,
\]
\[
I/I^2\simeq E^k,\qquad
\delta_S:I/I^2\longrightarrow E,\qquad
(a_i)\longmapsto\frac1k\sum_i h'(s_i)a_i.
\]

The domain is the conormal part of the original `P/I^2`; the derivative is induced by `(1/k)sum partial_si`, which sends `I^2` into `I`. The arithmetic unit is retained in lines 7634–7722:

\[
U=\prod_i(g/h)(s_i),\qquad
J^{(k)}\mathscr L_k\mathcal T_h^{(k)}\!\left(\sum_i h(s_i)P_i\right)
=\frac Uk\sum_i h'(s_i)[P_i]_I.
\]

This exact map is the starting point for the calculation below. The derivative of the original relation is not discarded when the relation itself maps to its supported zero.

## New calculation: the entire conormal image of an actual zero packet

Let Z be the finite actual packet in the transcript, with all its distinct centres and full positive multiplicities. For the residue and Hermitian trace calculations retain the transcript's reflection stability: `iota(rho)=1-conjugate(rho)` permutes Z and `m_(iota rho)=m_rho`. Its conjugate-linear involution is `f†(s)=conjugate(f(1-conjugate(s)))`; since `h†=(-1)^d h`, it descends to `E_h` and componentwise to its tensor powers. The rank calculations alone do not need this involution. Write

\[
h(s)=\prod_{\rho\in Z}(s-\rho)^{m_\rho},\quad
d=\sum_{\rho\in Z}m_\rho,\quad r=|Z|,
\quad E_h=\mathbb C[s]/(h).
\]

No factor of h is removed. Denote by `e_rho` the full Chinese-remainder idempotent of `E_h`. The exact CRT map sends a polynomial class to its classes modulo `(s-rho)^{m_rho}`; its inverse is multiplication by these idempotents followed by summation. At the rho component use the named local coordinate `z=s-rho`. Let

\[
h_\rho(s)=h(s)/(s-\rho)^{m_\rho}.
\]

Its value `h_rho(rho)` is nonzero. Before reduction the derivative is

\[
h'(\rho+z)=m_\rho z^{m_\rho-1}h_\rho(\rho+z)
 +z^{m_\rho}h_\rho'(\rho+z).
\]

In `C[z]/(z^{m_rho})`, the second displayed term maps to zero and the first equals `m_rho h_rho(rho)z^{m_rho-1}`. This explicitly records the killed term and every original scalar. Therefore the ideal `(h')` on this factor is the line generated by `z^{m_rho-1}`. For `m_rho=1` this line is the whole one-dimensional factor. We have proved

\[
\dim(h')E_h=r,\qquad
\dim E_h/(h')=d-r.
\tag{C1}
\]

For the ordered k-fold packet put `E=E_h^{tensor k}`. The image of `delta_S` is exactly

\[
\mathcal J=(h'(s_1),\ldots,h'(s_k))E.
\tag{C2}
\]

Containment follows from its displayed row. For the reverse inclusion, a term `h'(s_i)b` is the image of the vector with ith entry `kb` and all other entries zero. This retains the original 1/k instead of dropping it. There is the exact quotient morphism

\[
E/\mathcal J\xrightarrow{\sim}(E_h/(h'))^{\otimes k},
\quad [a_1\otimes\cdots\otimes a_k]\longmapsto
[a_1]\otimes\cdots\otimes[a_k].
\tag{C3}
\]

To prove its kernel, choose any basis of `(h')E_h` and extend it to a basis of `E_h`. The tensor basis decomposes into those tensors with at least one ideal-basis factor and those with none. The former span exactly the sum of the k ideals in (C2); the latter project bijectively onto a basis of the target. The basis is used only to prove the named quotient map, and it does not replace the arithmetic Gram or the original polynomial coordinates. Equations (C1)–(C3) imply

\[
\operatorname{rank}\delta_S=d^k-(d-r)^k,
\qquad
\dim\ker\delta_S=(k-1)d^k+(d-r)^k.
\tag{C4}
\]

The full local version, for an ordered tuple `(rho_1,...,rho_k)`, has image dimension

\[
\prod_i m_{\rho_i}-\prod_i(m_{\rho_i}-1)
\tag{C5}
\]

inside the unchanged local algebra `C[z_1,...,z_k]/(z_i^{m_rho_i})`. Indeed the quotient in (C3) replaces each local vector-space dimension by `m_rho_i-1`. This includes every repeated-root direction rather than passing to residue values.

The actual coefficient `U` in A1959 is an invertible element of E. Multiplication by U is therefore an automorphism with explicit inverse multiplication by `U^{-1}`. Since an ideal is invariant under multiplication by a unit, the actual arithmetic observation `U delta_S` has precisely the same image (C2) and kernel as `delta_S`. These are rank calculations for the original arithmetic source relation map, including its unit, not merely ranks of an unrelated polynomial map.

## The full mixed derivative and its arithmetic trace

Let

\[
\mathsf J_k=\prod_{i=1}^k g'(s_i)\in E,
\qquad g=2\xi.
\]

A1959 lines 7743–7764 gives the exact source identity

\[
\left[\partial_{s_1}\cdots\partial_{s_k}
\left(U P\prod_i h(s_i)\right)\right]_I
=\mathsf J_k[P]_I.
\tag{C6}
\]

The product rule proves this without suppressing terms: every term in which some derivative misses its corresponding h retains an undifferentiated `h(s_i)` and therefore belongs to I; exactly the one term hitting every h survives. Its coefficient is `U product_i h'(s_i)=product_i g'(s_i)` in E because `g'=h'(g/h)+h(g/h)'`. The term involving h has thus been recorded before the quotient.

The actual unit `v_h=g/h` is nonzero at every centre. On the rho factor,

\[
g'(\rho+z)=m_\rho u_\rho(0)z^{m_\rho-1}\quad\bmod z^{m_\rho},
\quad u_\rho(z)=g(\rho+z)/z^{m_\rho},
\quad u_\rho(0)\ne0.
\tag{C7}
\]

Thus `M_(g')` has rank one at each centre, and the tensor-product multiplication map in (C6) has

\[
\operatorname{rank}M_{\mathsf J_k}=r^k,
\qquad \dim\ker M_{\mathsf J_k}=d^k-r^k.
\tag{C8}
\]

Its image on an ordered tuple is the line with the original coefficient

\[
\left(\prod_i m_{\rho_i}u_{\rho_i}(0)\right)
z_1^{m_{\rho_1}-1}\cdots z_k^{m_{\rho_k}-1}.
\tag{C9}
\]

The map may land in the nilradical when a multiplicity exceeds one, but the original perfect residue pairing still detects (C9). Concretely, the ordered residue contraction is

\[
\mathscr R_k(f,\mathsf J_k u)
=\sum_{\boldsymbol\rho\in Z^k}
\left(\prod_i m_{\rho_i}\right)
\overline{f(1-\overline{\boldsymbol\rho})}u(\boldsymbol\rho).
\tag{C10}
\]

Here `mathscr R_k` means the ordinary ordered iterated residue in the fixed order `s_1,...,s_k`, with no additional Koszul factor. Equation (C10) is repeated application of the actual simple-pole residue of `g'/g`, whose coefficient is the full `m_rho`. It is also the ordinary multiplication trace on the full ordered algebra. Formula (C10) proves the exact map between the conormal/Jacobian observation and the trace; no assertion that a nilpotent is irrelevant is used. The cohomological supertrace has its separate factor `(-1)^k`. A differently signed tensor evaluation must be related by its explicit sign multiplication; no automatic cancellation is claimed here.

## Restriction to the actual signed symmetric cochain image

The original idempotent in A1859 lines 6054–6078 is

\[
\mathsf S_k=\frac1{k!}\sum_{\pi\in S_k}\operatorname{sgn}(\pi)T_\pi,
\quad T_\pi=\operatorname{sgn}(\pi)P_\pi
\text{ in top degree}.
\]

Its top-degree action is therefore the ordinary Reynolds projector
`R_k=(1/k!)sum P_pi`. We use the exact image `B_k=(E_h^{tensor k})^{S_k}`, including full nilpotents. Simultaneous permutation of variables and conormal indices makes `delta_S` equivariant. Averaging a preimage proves that its invariant image is `J^{S_k}`. This argument uses the same 1/k! as the actual chain idempotent. Taking invariants in (C3) is exact: if an invariant quotient vector has a lift, averaging that lift gives an invariant lift. It follows that

\[
\operatorname{rank}(\delta_S\text{ on invariant conormals})
=\binom{d+k-1}{k}-\binom{d-r+k-1}{k}.
\tag{C11}
\]

Here `binom(k-1,k)=0` when `d-r=0`, since the kth symmetric power of the zero vector space is zero for `k>=1`. To verify the dimensions, a basis of a t-dimensional vector space gives an unscaled orbit-sum basis of its kth tensor invariants indexed by nonnegative t-tuples summing to k; placing k identical marks among t slots gives `binom(t+k-1,k)`. This is a vector-space basis calculation, not a metric replacement.

The invariant conormal domain has dimension

\[
d\binom{d+k-2}{k-1}.
\tag{C12}
\]

Indeed an invariant tuple of k coefficients is determined by its kth coefficient, which must be invariant under the permutations of the first k-1 tensor positions. The other coefficients are recovered by permutation; independence of the chosen permutation is exactly this stabilizer invariance. This constructs the isomorphism to `E_h tensor Sym^{k-1}(E_h)` and proves (C12). Subtracting (C11) gives the complete invariant kernel dimension.

The mixed Jacobian is permutation invariant. Its image is the kth tensor power of the r-dimensional image `(g')E_h`; the same averaging proves surjectivity after taking invariants. Therefore

\[
\operatorname{rank}(M_{\mathsf J_k}|_{B_k})=\binom{r+k-1}{k}.
\tag{C13}
\]

These are exact maps on the original signed symmetric cochain image, not on the unsigned cochain average that kills repeated degree-one vectors.

## Intrinsic symmetric trace: the exact comparison of its multiplicities

It is necessary to keep both trace maps, with their actual comparison. Let an occupation vector be `n=(n_rho)_(rho in Z)`, with every `n_rho>=0` and `sum n_rho=k`. Define `e_n` to be the unscaled sum of the full ordered CRT idempotents whose ordered tuples have those occupations. Products of distinct summands vanish, so `e_n^2=e_n`, and these are the full orthogonal idempotents of B_k. The associated local factor is the invariant tensor product of the original local algebras. Its dimension is

\[
D_{\boldsymbol n}=\prod_{\rho\in Z}
\binom{m_\rho+n_\rho-1}{n_\rho}.
\tag{C14}
\]

For proof, one chosen ordering has stabilizer `product_rho S_(n_rho)`. An invariant tuple of local components is determined by that component and its stabilizer invariance. The latter is `tensor_rho (C[z]/z^{m_rho})^{tensor n_rho,S_(n_rho)}`. Applying the orbit-sum dimension argument separately proves (C14), and also constructs the isomorphism without changing local variables.

The component has nilpotent ideal of zero constant terms: in the full ordered local algebra the ideal `(z_1,...,z_k)` has a power equal to zero, hence so does its intersection with the invariant factor. Every element with nonzero constant is invertible by the finite geometric series in this ideal. Thus this is a local algebra, with residue field C and dimension (C14). Multiplication by `a=c+n`, n nilpotent, has trace `D_n c`: multiplication by n is nilpotent, hence has zero trace (triangularize its successive kernels). We obtain the intrinsic symmetric trace form

\[
\mathcal T_k^{\rm sym}(f,u)=\operatorname{Tr}_{B_k}M_{f^\dagger u}
=\sum_{\boldsymbol n}D_{\boldsymbol n}
\overline{f(\iota\boldsymbol n)}u(\boldsymbol n),
\quad\iota\rho=1-\bar\rho.
\tag{C15}
\]

It is also, by the image/kernel decomposition of the Reynolds projector,

\[
\mathcal T_k^{\rm sym}(f,u)
=\operatorname{Tr}_{E_h^{\otimes k}}(R_kM_{f^\dagger u}).
\tag{C16}
\]

Indeed `M_(f†u)` commutes with `R_k`, and `R_kM` equals M on its image B_k and zero on its kernel. This is the exact operator joining the ordered tensor trace and the actual symmetric cohomology trace.

The unprojected ordered trace in (C10), restricted to invariant inputs, has the different weight

\[
O_{\boldsymbol n}=\frac{k!}{\prod_\rho n_\rho!}
\prod_\rho m_\rho^{n_\rho}.
\]

The exact further map between the two arithmetic forms is multiplication by

\[
B=\sum_{\boldsymbol n}\frac{D_{\boldsymbol n}}{O_{\boldsymbol n}}e_{\boldsymbol n},
\qquad
\mathcal T_k^{\rm sym}(f,u)=\mathscr R_k(f,\mathsf J_k B u).
\tag{C17}
\]

Every ratio is a specified positive nonzero rational number, and the inverse replaces each ratio by its reciprocal. The equation follows by comparing the two literal finite sums. Thus the symmetric intrinsic trace is reached by the same actual theta mixed derivative, followed by its explicitly displayed coefficient map B. No orbit factor or local multiplicity has been normalized away.

For precision, this contraction has the exact induced isomorphism

\[
B_k/\operatorname{rad}\mathcal T_k^{\rm sym}
\xrightarrow{\sim}\operatorname{im}(M_{\mathsf J_k}|_{B_k}),
\qquad[u]\longmapsto\mathsf J_k B u.
\tag{C17a}
\]

The local formula (C7) shows that multiplication by the full mixed Jacobian kills exactly those classes whose constant term is zero on every ordered tuple. Restricting to invariants gives exactly the nilpotent ideal of B_k, already computed from its local factors. Multiplication by B preserves that ideal and is invertible. Its kernel is therefore precisely the trace radical, and surjectivity onto the stated invariant image follows from invertibility of B. The image here has dimension (C13); it is the invariant part of the ordered image (C8), not the full ordered image. This proves (C17a), with its exact kernel, rather than identifying its two spaces without a map.

An explicit original source representative for its value is obtained as follows. Choose the unique full CRT polynomial representative P of `Bu`, of degree less than d in each of the unchanged variables; for invariant u this representative is invariant by uniqueness and the permutation invariance of h. Then

\[
F_{u,k}:=\left(\prod_{i=1}^k\log x_i\right)
P(D_1,\ldots,D_k)(\Theta\phi_*)^{\otimes k}
\quad\text{satisfies}\quad J^{(k)}F_{u,k}=\mathsf J_k B u.
\tag{C17b}
\]

Indeed the undifferentiated source on the right has Mellin transform `P product_i g(s_i)=U P product_i h(s_i)`. Each log multiplication differentiates its specified Mellin variable, so (C6) gives precisely (C17b). These source functions and their logarithmic multiples remain in the given rapidly decreasing test spaces by the bounds defining those spaces. The undifferentiated expression is an original theta tensor boundary, for example using the first source leg `phi_*` with the other theta legs and the same polynomial operator. The mixed derivative is taken before that relation is quotiented. For m>1 its observed jet may be trace-radical, even while its residue contraction in (C17) is nonzero; (C17a) and (C17b) retain exactly which map is being used.

## Consequence for the actual RH counterfactual, with every multiplicity

Suppose the counterfactual supplies an actual quartet

\[
Z=\{\tfrac12+\delta+i\gamma,\tfrac12-\delta+i\gamma,
\tfrac12+\delta-i\gamma,\tfrac12-\delta-i\gamma\},
\quad0<\delta<\tfrac12,\quad\gamma>0,
\]

with the common full multiplicity m supplied by the original reflection and conjugation. This paragraph does not assert that such a zero exists. It computes what the negation of RH would force on the original objects just proved. Put the first and second centres in one reflection pair, and the third and fourth in the other. Then d=4m and r=4, so

\[
\operatorname{rank}\delta_S=(4m)^k-(4(m-1))^k,
\qquad\operatorname{rank}M_{\mathsf J_k}=4^k,
\tag{C18}
\]

and on the actual signed symmetric image,

\[
\operatorname{rank}\delta_S^{\rm sym}
=\binom{4m+k-1}{k}-\binom{4(m-1)+k-1}{k},
\qquad\operatorname{rank}M_{\mathsf J_k}^{\rm sym}
=\binom{k+3}{3}.
\tag{C19}
\]

The trace radical is exactly the nilpotent ideal. To prove this, a zero-constant element is orthogonal to everything by (C15). Conversely, if its value at occupation n is nonzero, pairing against `e_(iota n)` gives the nonzero scalar `D_(iota n)` times that value or its conjugate. The radical therefore has dimension

\[
\binom{4m+k-1}{k}-\binom{k+3}{3}.
\tag{C20}
\]

On a two-element reflection orbit of occupations n and iota n, the literal Gram in the idempotent basis is

\[
\begin{pmatrix}0&D_{\boldsymbol n}\\D_{\boldsymbol n}&0\end{pmatrix},
\quad
D_{\boldsymbol n}=\prod_{i=1}^4\binom{m+n_i-1}{n_i}>0,
\]

since matched multiplicities make `D_n=D_(iota n)`. The vectors `e_n+e_(iota n)` and `e_n-e_(iota n)` have values `+2D_n` and `-2D_n`, respectively. The basis and both factors two have been retained. A fixed occupation gives the positive one-dimensional Gram `D_n`.

A fixed occupation must have `n_1=n_2` and `n_3=n_4`. There are no such occupations for odd k. For k=2l, choosing `n_1=n_2=a` and `n_3=n_4=l-a`, with `0<=a<=l`, gives exactly l+1. Let

\[
b_k=\binom{k+3}{3},\qquad
f_k=\begin{cases}0&k\text{ odd},\\k/2+1&k\text{ even}.\end{cases}
\]

Counting each nonfixed orbit twice proves the complete inertia, including the entire radical:

\[
\boxed{\begin{aligned}
n_+(\mathcal T_k^{\rm sym})&=(b_k+f_k)/2,\\
n_-(\mathcal T_k^{\rm sym})&=(b_k-f_k)/2,\\
n_0(\mathcal T_k^{\rm sym})&=\binom{4m+k-1}{k}-b_k.
\end{aligned}}
\tag{C21}
\]

These negative directions are nonradical. Each of their negative trace values is the pairing with the explicit original theta mixed-derivative observation `mathsf J_k B f` in (C6) and (C17). This states the exact map: it does not assert that an idempotent f is itself in the Jacobian image, which would fail for repeated roots. The class f survives the nilradical quotient and the actual signed symmetric projector; its mixed-derivative observation remains available before the corresponding source relation is quotiented to its supported zero. Formula (C21) supplies a growing family of exact nonzero arithmetic directions that every claimed purity comparison for the RH counterfactual must control. It establishes no off-line zeta zero and no unconditional positivity contradiction: neither assertion occurs in the authoritative source, and neither was used in this calculation.

## The relative fibres at the expected sum weight still retain negative directions

The sum pushforward in A1912 retains the occupation idempotents even when their sum eigenvalues coincide. On the quartet label ordering just specified, its eigenvalue at occupation n is exactly

\[
\lambda_{\boldsymbol n}
=\frac k2+\delta(n_1-n_2+n_3-n_4)
 +i\gamma(n_1+n_2-n_3-n_4).
\tag{C22}
\]

To verify this with nilpotents, restrict multiplication by `S=sum s_i` to one ordered CRT factor, where it is the displayed scalar plus multiplication by `sum z_i`. The latter has a power equal to zero, since all monomials of total degree above `k(m-1)` vanish. Passing to stabilizer invariants retains this action and its scalar; it does not set the nilpotent to zero. This proves the full generalized eigenvalue statement on the occupation factor.

For k=2l, let `B_bal` be the direct summand defined by the sum of all full idempotents with `n_1+n_3=l` and `n_2+n_4=l`. It is a specified algebra direct summand of B_k, invariant under both reflection and the sum operator. Its eigenvalues all have real part k/2 by (C22). There are exactly `(l+1)^2` such occupations: independently distribute l among the two right centres and l among the two left centres. Exactly l+1 of them are reflection-fixed, as in (C21). Its trace form therefore has

\[
n_-(\mathcal T_k^{\rm sym}|_{B_{\rm bal}})=\frac{l(l+1)}2,
\qquad
n_+(\mathcal T_k^{\rm sym}|_{B_{\rm bal}})=\frac{(l+1)(l+2)}2,
\tag{C23}
\]

and radical dimension `sum_(balanced n) D_n-(l+1)^2`, with the same literal weights (C14). This is proved by the same explicit two-idempotent Gram blocks, now on this exact invariant direct summand. It is not a new positivity assumption.

Already at k=2 the two distinct occupations `(1,0,0,1)` and `(0,1,1,0)` both have the actual sum eigenvalue 1. Their full idempotents remain different, and

\[
\mathcal T_2^{\rm sym}
(e_{(1,0,0,1)}-e_{(0,1,1,0)},
 e_{(1,0,0,1)}-e_{(0,1,1,0)})=-2m^2.
\tag{C24}
\]

For m>1 the local nilpotent sum operators remain attached; no assertion that the idempotents are eigenvectors is needed. Equation (C24) is exactly why the original program's relative algebra cannot be replaced by the list of sums alone. It is an actual counterfactual consequence inside A1912's constructed pushforward. It does not say that an upper bound on the entire tensor image would be insufficient: the same whole image also retains repeated extreme eigenlines of real part `k(1/2+delta)`. Rather, it specifies the additional negative relative directions that remain even in its expected-real-part summand, with their exact source and trace maps (C17a)–(C17b).

The negative count can be located on each exact sum fibre. For an integer `q` with `-l<=q<=l`, the fibre whose eigenvalue is `l+2i gamma q` consists of the full occupation factors

\[
\boldsymbol n=(a,b,l-a,l-b),\quad
0\le a,b\le l,\quad a+b=l+q.
\]

There are `N_q=l+1-|q|` such pairs: when `q>=0`, a runs from q to l; when `q<=0`, a runs from 0 to l+q. Reflection exchanges a and b, so its fixed count is `f_q=1` if `l+q` is even and zero otherwise. This also equals one precisely when N_q is odd. The exact nonradical inertia of that particular sum fibre is consequently

\[
n_- =\left\lfloor\frac{l+1-|q|}{2}\right\rfloor,
\qquad
n_+ =\left\lceil\frac{l+1-|q|}{2}\right\rceil,
\tag{C25}
\]

with its unchanged nilpotent radical of dimension `sum_(a+b=l+q)D_(a,b,l-a,l-b)-N_q`. The proof is the full Gram-block argument above restricted by the literal spectral projector which sums these occupation idempotents. Thus the persistent negative directions are established inside individual exact sum fibres, not only in a union of fibres with the same real part.

## Limits of this result, stated as facts about the computed maps

The conormal rank, complete inertia, and source representatives are proved above on the actual counterfactual packet. The Fisher identity has its precise source-to-jet morphism, but the source does not prove an operator bound of its full relative connection in the packet's canonical interpolation norm. Accordingly the displayed 1/k alone supplies no sign restriction eliminating (C21). This report adds an exact restriction any actual counterexample must satisfy, while retaining the absolute-base, source, conormal, cohomological-sign and arithmetic-unit constructions already present in the original thread.
