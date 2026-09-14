# Independent review of QGT1–28

Scope: complete reading and analytic verification of `QUANTITATIVE_ORIGINAL_GAMMA_RETURN.tex`, using the already accepted QLG partition theorem. QLG's complete proof was not re-audited. The precise source constants and restricted-cell lower bound used by QGT were checked against QLG. GDR, LER, EIQ and WGP were inspected for their actual interfaces.

Status: **accepted against final SHA256 `0b552f80782b86651d3876ecf2dfd71a7c3f2e2c04ef005d6cadecb15d9bb629`**. The review applies to the original packet integers and density only. No independently chosen Gamma order is inserted.

## Exact source and density

QGT1–3 correctly retain `q=e(4l+2)^2=2n`, the full even moment mass, both half-lines under `t=y^2`, and the literal Heine factor `1/s!`. The domain `a>-1/2` is sufficient at zero. The determinant integral is strictly positive and all its polynomial moments are finite.

Integrating GDR3 on `[1,y]` bounds the logarithm of `r(y)=y^(1/2) exp(pi*y/2) sigma(y)` by the literal constant `D=1/16+sqrt(3)/18`. The sign and lower estimate are correct because `pi/2>D`. GDR7 proves monotonicity of `sigma` on the positive half-line, completing the bounds on `[0,1]`. QGT5's lower bound uses `(1+y)^(-1/2)` and therefore retains the finite density at zero. Its upper bound applies to every positive y.

The exact dilation in QGT7 has exponent `2as+2s(s-1)+s/2`. The three contributions are the Vandermonde exponent `2s(s-1)`, the moment and Jacobian exponent `s(2a+1)`, and the Gamma prefactor exponent `-s/2`. The remaining x-power is `a-3/4`, giving precisely the displayed alpha. The initial source contained `q^{,2as...}`; the author is removing that extraneous comma.

## Uniform partition estimate and moving shift

The upper bound uses the pointwise constant `C_+` on the whole positive domain. For the lower bound, QLG's actual quantile cells lie inside `[a_*,B_*]`. The displayed lower bound `C_*` follows from `q>=1` and monotonicity of `u/(1+u)`. Multiplication by `C_*^s` occurs on exactly those cells whose permutations cancel the original `1/s!`. Thus QGT10 and the exact difference defining QGT11 have the stated `Cs` error. There is no unproved derivative assertion about that error.

For QGT13, `n>=18l`, `n>=18`, the literal offsets `-3/4` and `-11/4`, and `eta=s^(-1/2)<1/4` put all finite difference intervals in the stated compact parameter rectangle. The rank `n+1` has beta `pi*n/(n+1)`, which remains in that rectangle. Differentiation of the exact positive integral is justified by the positive powers at zero, integrable logarithmic factors, and the exponential tail bound. Precisely `(log J)''=s^2 Var(sum log x_i)` and `g''=Var(sum log x_i)` for `g=s^(-2) log J`; the author's wording repair makes these two coefficients explicit.

The two convex secant inequalities, the error `C/s`, and the finite bound on the derivative of the equilibrium logarithmic moment give `|g'-L| <= M eta/2 + 2C/(s eta)`. Integration over length `l/s` and multiplication by `s^2` gives exactly `(M/2+2C) l sqrt(s)`. Every cancelled q-power is displayed before cancellation.

## Four blocks and the original return

The weights `1,1,2` in QGT15 reproduce the original four high blocks. Their total logarithmic coefficient is `2l[n+(n+1)+2n]=(4q+2)l`. Their error is exactly `A l(3 sqrt(n)+sqrt(n+1))`.

Substitution of the low endpoint identity gives `W=V+xi-r-epsilon`. Thus the negative Taylor remainder becomes a positive contribution to W, and QGT20's two orientations are correct. The `p^-` and `p^+` formulas in QGT21 are the complete WGP13 bounds. QGT22 retains those one-sided signs. The original source power, high power, and low power cancel as `-4lq+(4q+2)l-2l=0`.

For QGT23–24 the rank offsets are exactly `-3/4,-11/4,1/4`, with weights `1,1,2`. Their weighted absolute offsets sum to 4 and their squared-shift errors sum to `2l^2`. EIQ32 gives the rank `n+1` contribution `2(n+1)l log(1+1/n)` with the displayed positive sign. QGT25 includes every term left after subtracting the original leading coefficient; the triangle inequality is applied after the signed decomposition. QGT26 follows.

Using the exact bound `q>16l^2`, each rational term in QGT25 is bounded uniformly in m, and the whole quantity is `O(l^2+l)`. Hence QGT27 follows with constants independent of m. For fixed m>=2, q grows cubically in l, so `l/sqrt(q)` and `l^2/q` both tend to zero. QGT28 is therefore proved. At m=1, q is exactly `(4l+2)^2`; the displayed error estimate gives only a bounded quotient at the q scale. It does not prove the limit of that quotient.

## Provider pins inspected

- GDR: `642fc0b0b60a3253ad577b588b2b93d6d0aa4357cae40b69e7f45098e0c10304`.
- LER: `b3607ad6e0cd2480f917bdce057683cb8526d5243f583363eee297835403422e`.
- QLG: `52256dd3671db7944c6758ed8a2f7129b7a226a08c433b1f32449985f2137b71`.
- EIQ: `a0a0346a19d0e035a186590dbd69881cdf7a30e8fef602d47bba0932f175e731`.
- WGP: `e6122af0f0cc54028ceee5383c97070e7738d9d8ec1a5bc5481b349761e5fbfe`.

The reference to an accompanying GPR provider was flagged: no tagged GPR body was located in the current source tree. QGT already supplies the complete needed density proof from GDR, so this is a reference cleanup and does not leave a mathematical gap.

An independent subsidiary review of QGT18–28 is recorded in `FINITE_COMBINATION_CHECK.md`.

## Final correction verification

The final source was hashed and its complete difference against the preserved initial source `865dfee32fde2691f8982c5f7b345446d22fb21b42062aa920ebd779f77a092d` was read. The difference consists exactly of removal of the orphan GPR reference, replacement of the auxiliary scalar symbol h by alpha_Gamma, removal of the stray comma in QGT7, and explicit variance equalities for log J and g. Every correction is valid. No other theorem, constant, original parameter, or proof was changed. There are no outstanding proof issues in QGT1–28 within this review's stated dependency scope.
