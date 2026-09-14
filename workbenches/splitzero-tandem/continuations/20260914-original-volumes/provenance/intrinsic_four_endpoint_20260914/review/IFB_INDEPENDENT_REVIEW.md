# Independent review of IFB1–41

Reviewer: `/root/intrinsic_four_endpoint_bridge/ifb_independent_review`.

Decision: **PASS** for the entire mathematical argument in the source pinned below. No correction is requested. This is an independent algebraic and analytic reading; it does not rely on numerical evaluation or on the author's compilation check. The source was not edited by this reviewer.

Reviewed source: `INTRINSIC_FOUR_ENDPOINT_RELATION_GRAPH.tex`, SHA256 `50fc30d31e2b6bdbf8d630f5029cf1091e10618de3e7bd3c22d229cc7ccf340a`.

Crosschecked original baseline: `../baseline_20260914/BASELINE_ORIGINAL_PACKET.tex` relative to the reviewed source's directory, SHA256 `a53703c284d816930291aa4b02373564fe8cd5cf7c93a1d0517354614f438c30`. The full baseline was read; the dependencies needed here are BSL1–4 and BSL17. No assertion that IFB independently proves the asymptotic results of the other baseline sections is made.

## IFB1–5: original source, mass, moments, and orthogonal coordinates

The packet remains the original polynomial of degree `q=e(k+1)^2`, on the original line `S=c+iy`, with `s` restricted to the existing source orders `1` and `k`. Since `k=4l+1`, `q` is divisible by four. The measure coefficient in IFB2 is correct. At `s=1`, using `M_1=sqrt(2 pi)` and `Gamma(1/2)=sqrt(pi)` gives exactly `1/(2 pi)`. At `s=k`, the Gamma recurrence contributes `4^(-l)` and

`2^(k/2-2) 4^(-l) = 2^(-3/2)`.

Thus the resulting coefficient is `M_k/(2 pi sqrt(2) Gamma(k/2))`, equal to BSL17 after inserting the density of `sigma`. Each factor of the original `|f_l(c+iy)|^2` is `y^2+(2j+1/2)^2`; no phase or source mass is lost.

The Fourier autocorrelation computation in IFB3 has the factor `2 pi`, and the substitution `y=2 xi` contributes the additional Jacobian `2`. With the coefficient from IFB2 this gives the characteristic transform `M_s(cosh w)^(-b_s)`. Rotation of Euler's integral by angle `theta sign(y)` bounds each Gamma factor by a constant times `exp(-theta |y|/2)`; squaring produces the stated bound `exp(-theta |y|)`. The small and large contour arcs vanish because `b_s/2>0` and `cos(theta)>0`. Consequently the characteristic transform is analytic on the full stated strip and gives the Laplace transform on `|t|<pi/2`. This also supplies the domination needed for every finite differentiated moment.

The product of the two generating functions in IFB4 integrates to `M_s(1-zw)^(-b_s)`: the two prefactors cancel the square-root denominators in the cosine addition identity. Comparing coefficients of `z^n w^j` yields `h_n=M_s n!(b_s)_n`. Differentiating the generating function yields the exact recurrence in IFB5 and parity. The scale agrees with BSL3: at `s=1`, `n!(1/2)_n=(2n)!/4^n`.

## IFB6–11: entire quotient Gram and relation graph

On the original evaluation line, each `u_n` equals `p_n/sqrt(h_n)` exactly. In the original `S` frame its leading coefficient is `i^(-n)/sqrt(h_n)`, so the determinant modulus in IFB7 is correct despite the translation by `c` and every phase. The fixed matrix `C_s` is invertible and is used unchanged at every endpoint.

In orthonormal coordinates the original remainder map is the matrix `C_s[I_q,V_r]`. Therefore its kernel is exactly the graph `(-V_r z,z)`, whose degree bound gives the literal relation space `chi P_(r-1)`. This proves both inclusions in IFB9, including the empty relation space at `r=0`.

Writing `w=C_s^(-1)a`, the proposed lift `(K^(-1)w,V_r^*K^(-1)w)` has image `w` and is orthogonal to every graph vector. Its squared norm is `w^*K^(-1)w`. This proves the entire positive quotient Gram, not merely its determinant. Taking its determinant and using IFB7 gives IFB11 with the full source factors and the correct inverse power of `Omega`.

## IFB12–21: all polynomial coefficients and positive minor expansion

The four roots with signs `(±A,±B)` contribute exactly `((y-B)^2+A^2)((y+B)^2+A^2)`: each pair with opposite real coordinate contributes a minus sign, and the two signs multiply to plus. The leading phase is also consistent with `i^q=1`. Hence `vartheta=chi(c+iy)` is real, even, monic, and strictly positive for real `y`; the source weight is its literal square. IFB13–14 retain the negative middle coefficients and every multiplicity.

The coefficient recurrence IFB15 follows by expanding `y p_h`. In the term contributing to index `h`, the lowering coefficient is `(h+1)(b_s+h)`, as stated. Thus IFB16 is the full expansion of `vartheta y^j` into the orthogonal source basis, with coordinate weights `sqrt(h_h)`. On the original line these are also its coordinates in the `u_h` frame. The matrix in IFB17 sends original `S`-polynomial coefficients to the corresponding `y`-polynomial coefficients; its diagonal is `i^j`, so its determinant modulus is one.

In the high rows the column of degree `q+j` has no entry below its degree and has entry `sqrt(h_(q+j))` at that degree. The high matrix `R` is upper triangular. The column space of `L` is the exact relation graph already proved in IFB9, so `L_low R^(-1)=-V_r`, including the sign and all entries. Factoring `L=[-V_r;I_r]R` gives

`det(L^*L) = (product h_(q+j)) det(I_r+V_r^*V_r)`.

The two eliminations of the displayed block matrix prove equality with `det(I_q+V_rV_r^*)` in every rectangular dimension, preserving zero singular directions. The exterior-product expansion proves IFB20 with the exact norm ratio. Its highest-row minor is upper triangular with determinant one, and the empty minor convention is consistent at `r=0`. This is an actual sum of nonnegative terms calculated from the complete signed coefficients; positivity has not been inferred from a highest-degree approximation.

Differentiating the source transform gives the recurrence for `P_n` and moments `M_s P_n(0)`. The relation moment matrix therefore has the entries in IFB21, and extracting `M_s` from each of its `r` rows produces `M_s^r`. At `r=q+1` the largest index is `2q+2r-2=4q`, exactly as stated.

## IFB22–29: exterior measure, sum map, adjoint, and Wronskian mass

The double Vandermonde expansion gives precisely `r!` copies of the moment determinant. This cancels the literal `1/r!` and proves the mass identity with no probability normalization. Polynomial moments are integrable by the bound proved in IFB3.

The linear change to `(y_1,...,y_(r-1),Y)` has determinant one. For every fixed `Y`, the density in IFB24 is bounded by a polynomial times an exponentially decaying function of the independent coordinates, hence is integrable. Every sum fibre contains a nonempty open set of distinct coordinates, and the source and polynomial factors are strictly positive there; thus `g_r(Y)>0` for every real `Y`.

The composition map in IFB25 is an isometry by the definition of pushforward. Fibrewise Cauchy–Schwarz proves existence almost everywhere, the contraction bound, and the stated adjoint formula. Applying Fubini to the Hilbert pairing verifies the adjoint with its complex conjugations. Its kernel is exactly the zero conditional-integral subspace, so no entire exterior space is identified with the space of sum functions. The special cases `r=0,1` are treated correctly. IFB27 gives the precise translation from each constituent's natural line to the unchanged original target `rc+iR` and preserves `dY` and all masses.

For IFB28, set `f(t)=(cos t)^(-b_s)` and `z=tan t`. The moment determinant is `M_s^r det[partial_t^(i+j)(f Q_0)]`. Its columns are `f Q_j`, because the recurrence for `Q_j` retains the derivative of `f`. Factoring the common multiplier through the derivative rows gives `f^r`. Changing coordinates in the remaining Wronskian contributes `(z')^(r(r-1)/2)=(1+z^2)^(r(r-1)/2)`. Therefore the displayed divided determinant is exactly the polynomial Wronskian `det[partial_z^i Q_j]`; the total cosine exponent is `b_s r+r(r-1)`. This checks the polynomial construction directly without relying on an unproved degree statement from another provider.

At `t=0`, the transform has mass `M_s^r D(0)`. Comparing with IFB19 cancels precisely the same `M_s^r` in the product of source norms. IFB29 follows with the complete factorial/Pochhammer product. The empty determinant gives one at `r=0`.

## IFB30–34: original signs and positive update chain

The signs are exactly the BSL four degrees: `q-1,q,2q-1,2q`, corresponding to relation ranks `0,1,q,q+1` with signs `+,+,-,-`. Inserting IFB11 directly gives

`B = log Omega_q + log Omega_(q+1) - log Omega_1`.

Independently, the relation products in IFB30 give exponent one on `h_q`, two on `h_(q+1),...,h_(2q-1)`, and one on `h_(2q)` after subtracting the rank-one product. These cancel exactly `S_q^(s)`. The source mass exponents are respectively `2q` and `-2q`; no unexplained normalization is used.

Every `K_(s,j)` is positive definite. The rank-one determinant calculation proves `d_(s,j)>=1` and the product formula for `Omega`. Multiplying the proposed inverse by `K+vv^*` verifies IFB33; its denominator is strictly positive. The coefficients in the signed sum are one at `j=0`, two at `1<=j<q`, and one at `j=q`. Thus IFB34 is exact and nonnegative, with every interaction still present in the full inverse.

## IFB35–37: actual finite quotient recurrence

Substitution `y=(S-c)/i` sends the exact polynomial `vartheta` to `chi`, and the inverse substitution sends `chi` to `vartheta`. This proves the stated algebra isomorphism and fixes the phases. The multiplication matrix in the normalized orthogonal frame is consequently `Y_s=E_s^(-1)Y_vartheta E_s`. Dividing the original recurrence by `sqrt(h_n)` gives the off-diagonal factors `a_n=sqrt(n(b_s+n-1))`; the index and denominator in IFB37 are correct. Every denominator with `n+1>=1` is positive. Starting from the retained low frame and running through `n=2q-1` yields exactly `z_(2q)=v_q`, the last vector required by the original signed sum.

## IFB38–41: explicit coefficient minors

The positive odd-coordinate square sum is `k(k+1)(k+2)/6`; multiplying by the `(k+1)/2` choices of the other coordinate and by `2e` gives `c_(q-2)=q k(k+2)(delta^2-gamma^2)/6`. This checks the original coefficient, including its negative sign for the stated parameters. Summing the recurrence coefficients gives

`A_n=sum_(j=1)^(n-1) j(b_s+j-1)=n(n-1)(3b_s+2n-4)/6`.

Since `p_n` has coefficient `-A_n` at degree `n-2`, the coefficient of `p_(q-2)` in `vartheta` is `c_(q-2)+A_q`. For the row replacement `q -> q-2`, the first column has this value in the replacement row and vanishes in all remaining selected rows; the higher selected block is upper triangular with diagonal one. This proves IFB40 with the exact norm ratio.

For `q+1 -> q-1`, the two lowest selected rows are ordered `q-1,q`. On the first two columns their matrix is `[[0,c_(q-2)+A_(q+1)],[1,0]]`, giving the negative sign stated before squaring. Replacing both rows gives the diagonal matrix with entries `c_(q-2)+A_q` and `c_(q-2)+A_(q+1)` because the off-parity entries vanish. All remaining selected rows have zero entries in the first two columns and retain the upper triangular diagonal-one block. The four row subsets are distinct for every `r>=2`; their four norm ratios are exactly `1,x,y,xy`, proving the product lower bound IFB41. No asymptotic dominance of these terms is claimed or used.

Finally, division by the even monic `vartheta` preserves parity. Thus each `v_j` has the stated source parity and each cross-parity entry of `K` is zero. Applying the unchanged `C_s` carries the entire matrix back to the original remainder frame. This last transport is consistent with IFB11 and with the original boundary receiver; it does not remove any coordinate.

## Scope of acceptance

Every numbered claim IFB1–41 and each accompanying proof has been checked. The source establishes a finite exact calculation and positive expansion of the existing four-endpoint expression, together with its actual exterior-sum mass and fibre map. It makes no replacement `k=q`, introduces no auxiliary canonical source order, and claims no RH conclusion. No mathematical repair or additional hypothesis is needed for these results.
