# Independent proof review of GMB1–16

Reviewer: `/root/mixed_row_morphism_review`.

Outcome: **accepted in full**. The review reads every definition, displayed identity, and proof paragraph of `ORIGINAL_GAMMA_MIXED_ROW_MORPHISM.tex`, rather than selecting sample identities. No mathematical repair is requested. The accepted source SHA-256 is `32c56427cb2f62c0d41bd2f6830813a84aa01b1bff21a39fd4291e9b54f35556`.

The decisive original definitions and maps were read in HMR27–35 and BSL1–4. The full HMR source was available during this review. The original Gamma integral and orthogonal-polynomial construction were read in IKO3–5; only their existing source values `s=1` and `s=k` are used here. No auxiliary choice `K=q+1` enters any GMB identity. The independent four-endpoint graph writer was contacted to compare the incoming interface; this review certifies all GMB1–16 identities independently of completion of that other source.

## Exact source and coordinates: GMB1–4

The full source has moment generating function

\[
\int e^{ty}\,dm_{0,s}(y)=M_s(\cos t)^{-b_s},\qquad
M_s=(2\pi)^{s/2},\quad b_s=s/2,\quad |t|<\pi/2.
\]

The original polynomial generating function is

\[
F(y,z)=(1+z^2)^{-b_s/2}\exp(y\arctan z)
       =\sum_{d\geq0}p_d(y)z^d/d!.
\]

Its derivative obeys `(1+z²) ∂zF=(y−b_s z)F`. Comparing the coefficient of `z^d/d!` gives exactly

\[
p_{d+1}=yp_d-d(b_s+d-1)p_{d-1}.
\]

The generating function starts with `p_0=1,p_1=y` and has leading coefficient one in degree `d`. Integrating the product at real small `z,w` gives `M_s(1−zw)^{−b_s}`. The coefficient with degrees `i,j` vanishes for `i≠j` and equals `M_s d!(b_s)_d` for `i=j=d`. Differentiation under the integral follows from the same exponential majorant in the original source proof. Thus GMB1 retains the entire mass, the exact recurrence, and every norm. This is an algebraic verification of its source convention, not a numerical check.

On the original line `S=c+iy`, `u_d(S)=p_d(y)/sqrt(h_d)` is orthonormal and has literal leading coefficient `i^(−d)/sqrt(h_d)` in `S`. The change matrix from its first `q` columns into the original monic remainder frame is triangular; its diagonal has exactly those entries. Their product gives GMB2, including the phase `i^(−q(q−1)/2)`. All `h_d` are strictly positive because `s>0`.

At degree `D−1=q+j−1`, the original remainder map applied to the full source coefficient vector is `C_s A_j`, with `A_j=[I_q,v_0,…,v_(j−1)]`. Every column has been included. Hence `A_j A_j*=K_j>0`, and its kernel has dimension `(q+j)−q=j`. For a quotient coordinate `x`, the proposed coefficient lift `A_j* K_j^(−1)x` has remainder `x`. Its inner product with a vector `z` in `ker A_j` is `z*A_j*K_j^(−1)x=0`. Every other lift differs by that kernel vector, so the Pythagorean identity proves both its uniqueness and its minimum squared norm `x*K_j^(−1)x`. Transporting `x=C_s^(−1)e` proves GMB4 with exactly the displayed order `C_s^(−*)K_j^(−1)C_s^(−1)`.

## Original monic relation and row: GMB5–7

Put `v=v_j`, `K=K_j`, and `D=q+j`. The source vector

\[
z=(-A_j^*K^{-1}v,1)
\]

has zero original remainder, since `−A_j A_j*K^(−1)v+v=0`. The old coordinates lie in `im A_j*`, which is orthogonal to `ker A_j`; therefore this vector is orthogonal to every old relation. Its last coefficient is one, and `u_D` has leading coefficient `i^(−D)/sqrt(h_D)`. Multiplication by `i^D sqrt(h_D)` gives leading coefficient one in `S`, without changing the original remainder or orthogonality. Since `chi` is monic of degree `q`, the resulting polynomial is `chi` times a monic degree-`j` polynomial, orthogonal to lower degrees for the actual measure `|chi(c+iy)|² dm_(0,s)`. This is the relation indexed `D−1` in HMR32. If two such relations existed, their difference would belong to the old relation space and be orthogonal to itself; positivity forces zero.

The squared norm of `z` is

\[
1+v^*K^{-1}A_jA_j^*K^{-1}v=1+v^*K^{-1}v=1+t_j.
\]

Thus the monic relation norm is exactly `a_(D−1)=h_D(1+t_j)`. For a polynomial `P` of degree less than `q`, its source coordinates at degree `D−1` are `(C_s^(−1)[P],0_j)`. The inner product of the old lift term with this vector is `v*K^(−1)C_s^(−1)[P]`; the inner product of `u_D` with `P` is zero. The inner product is conjugate linear in its first variable, so the conjugate of the orientation scalar is `i^(−D)sqrt(h_D)`. This yields exactly

\[
\alpha_{D-1}=-i^{-D}\sqrt{h_D}\,v^*K^{-1}C_s^{-1}.
\]

Both the minus sign and the conjugated phase in GMB6 are necessary and correct.

Multiplication verifies the displayed rank-one inverse formula. Inserting it into GMB4 gives

\[
G_{D-1}-G_D=C_s^{-*}K^{-1}vv^*K^{-1}C_s^{-1}/(1+t_j)
             =\alpha_{D-1}^*\alpha_{D-1}/a_{D-1}.
\]

The phases have product one and the full norm factors cancel only at this displayed quotient. The determinant of the rank-one update to `K` is `1+t_j`, so GMB7 is also valid for `v_j=0`; no division by `t_j` occurs.

## Exact observation and retained kernel: GMB8–12

`R_s=Lambda C_s` is the matrix of the unchanged original observation, and is surjective because both `Lambda` and `C_s` have their stated ranks. On a nonzero boundary space, `M=R_s K R_s*` is positive definite: for `b≠0`, the injection `R_s*` gives `(R_s*b)*K(R_s*b)>0`. Thus `xi=w*M^(−1)w` is nonnegative. With `w=R_s v`, the vector `r=v−KR_s*M^(−1)w` lies in `ker R_s`. The displayed complement is orthogonal for the `K^(−1)` metric because `r*R_s*=0`. Its squared norm is `w*M^(−1)w=xi`, proving `t=xi+r*K^(−1)r`, including `0≤xi≤t`.

The restriction of `C_s` is a bijection from `ker R_s` onto `ker Lambda`; this follows from `R_s=Lambda C_s` in both directions using `C_s^(−1)`. Thus the kernel in the formula is the original kernel with its actual coefficient embedding.

At the new degree, `S_D=G_D^(−1)Lambda*Q_D` satisfies `Lambda S_D=1` and `I*G_DS_D=0`. The sum map `[I,S_D]:ker Lambda ⊕ B_obs → E_chi` is bijective, since the unique kernel component of `e` is `e−S_D Lambda e`. In these coefficient frames the Gram is `diag(H_D^ker,Q_D)`; conjugating its inverse back proves GMB12 with the original ordered products. In particular no common eigenbasis or commuting square roots are assumed.

For boundary rank zero, `R_s` and the boundary matrices are empty, `w` is empty, `xi=0`, and `r=v`. For kernel rank zero, `R_s` is invertible, the formula for `r` gives zero, and therefore `xi=t`. In these cases the corresponding inverse and determinant are the unique empty inverse and determinant one. All identities GMB8–12 remain defined.

## Both mixed contractions: GMB13

For the notation in the source, `d=1+t`, `h=h_D`, and `N=M+ww*`. From GMB4 one gets

\[
G_D^{-1}=C_s(K+vv^*)C_s^*,\quad
Q_D=N^{-1},\quad
S_D=C_s(K+vv^*)R_s^*N^{-1}.
\]

The row calculation is

\[
v^*K^{-1}(K+vv^*)R_s^*=(1+t)v^*R_s^*=d\,w^*.
\]

Also `N^(−1)w=M^(−1)w/(1+xi)`, verified by multiplication. Substituting these two formulas gives

\[
\alpha S_D=-i^{-D}\sqrt h\,d\,w^*N^{-1},\qquad
\nu=h d^2\xi/(1+\xi).
\]

The full inverse decomposition gives

\[
\beta+\nu=\alpha G_D^{-1}\alpha^*=h(t+t^2)=hdt.
\]

Exact subtraction then yields

\[
\beta=hd\frac{t-\xi}{1+\xi},\quad
\frac\beta a=\frac{t-\xi}{1+\xi},\quad
a+\beta=\frac{h d^2}{1+\xi},\quad
\frac\nu{a+\beta}=\xi.
\]

Thus both factors in GMB13 and their product are correct, with positivity supplied by the already proved `0≤xi≤t`. Restricting the GMB7 update to the original `I` makes the kernel determinant ratio `1+beta/a`. The determinant product identity from the bijection `[I,S_D]` (or HMR30–33) then makes the boundary determinant ratio `(1+t)/(1+beta/a)=1+xi`. The coefficient frame determinant is the same at both degrees because any two right inverses differ by a kernel column and hence by a triangular change of determinant one. This verifies the identification with the original individual BRU factors, rather than only their combined product.

At zero boundary rank these are `1+t` and `1`; at zero kernel rank they are `1` and `1+t`. If `v=0`, both are one and all contractions vanish. No excluded degeneracy is concealed.

## Four exact endpoints and finite recurrence: GMB14–16

For the complete quotient determinant, the log increment at row `D−1=q+j−1` is `log(1+t_j)`. Expanding

\[
(\log\det G_{q-1}-\log\det G_{2q-1})
+(\log\det G_q-\log\det G_{2q})
\]

by successive increments gives weight one at row `q−1`, weight two at every row `q,…,2q−2`, and weight one at row `2q−1`. Under `D−1=q+j−1`, these are `j=0`, `1≤j≤q−1`, and `j=q`. This proves precisely `W_q` and all three formulas in GMB15. Applying the same telescoping to the individually verified kernel and boundary factors gives their signed endpoint volumes, with no reversal of a sign and no missing row.

Multiplication by `S` on the original remainder algebra is the literal companion operator `T_chi`. Therefore `Y_chi=(T_chi−cI)/i` represents multiplication by `(S−c)/i`. Starting from `[1]` and `Y_chi[1]`, the GMB1 recurrence proves by induction that `r_d=p_d(Y_chi)[1]`. Division by `sqrt(h_d)` gives `[u_d]`; hence the low columns are exactly `C_s` and the higher columns exactly `C_s v_j`. All coefficients and multiplicities of `chi` enter the same companion operator, and the formula does not replace a polynomial by its leading term. Every inverse needed afterward was proved to exist. Thus GMB16 is a finite explicit algorithm for the precise objects proved above.

## Scope and provenance

This acceptance concerns the exact Gamma source-to-remainder-to-observation morphism and its complete mixed rows. It neither claims a new arithmetic source nor assigns a new Gamma order. The source orders are exactly `{1,k}`. The actual packet order, centre, polynomial, full observation, and kernel are preserved. The full intrinsic exterior construction can feed these finite matrices through its existing exact Gram identities; an incoming graph source must preserve the same masses, bases, and ranks. Any future additional estimate on `t_j` or `xi_j` requires its own proof; GMB makes no unproved estimate of that kind.

Pinned sources:

- GMB1–16 source: `32c56427cb2f62c0d41bd2f6830813a84aa01b1bff21a39fd4291e9b54f35556`.
- HMR source, decisive HMR27–35 read: `e645576fff6e7c32af8bd02ee36a46972f486c369eab009444c98fe437aef6b2`.
- BSL source, BSL1–4 source definitions and following coordinate convention read: `a53703c284d816930291aa4b02373564fe8cd5cf7c93a1d0517354614f438c30`.
- IKO source, IKO3–5 source integral and polynomial proof read at `s=1,k`: `ca441951613a7c9041133e56f57f8469535a052294303e6e1f7e30106e5e2633`.

No numerical experiment, finite-dimensional sample, or successful compilation is used as the proof of any accepted identity.
