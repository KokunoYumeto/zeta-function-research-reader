# Independent review of the original four-product expansion

Verdict: **PASS. No mathematical repair required for WGP1–11.**

This is a bounded mathematical review of the complete proof fragment, its original product endpoints, signed finite error, and its exact interface to the existing positive Gamma recurrence. It does not certify a growing-degree value of the recurrence and does not claim any build, visual review, Lean execution, or publication. The reviewed source was not edited.

## Exact source state

All paths below are relative to `work/backpropagation_20260913/root/joint_schur_intake/`.

| Source | SHA256 |
| --- | --- |
| `growing_w_20260914/original_product_expansion.tex` | `cf98ada94f65e81ca7edd11dd51e3c38d5fb5a12397b0e0d1264d70cf86a69a2` |
| `future_hankel/independent_contiguous.tex` | `e01021c3b9b659cd897cc95179391b3bde0de63397405426fef2cda420e81196` |
| `future_hankel/PARITY_AND_TODA_TRANSPORT.tex` | `3b5914ff3d99e18f881fc59a372787dadfe1e1ef8aa9ebeefebb62d6a6a9991d` |
| `next_bulk_density/future_hankel/LOW_ENDPOINT_TRANSPORT.tex` | `a31250b693b9e687481bc7bfa7638707013930c4bfb9b6a8f39c201779d02a44` |

The entire WGP fragment was read. The comparison used the HCT definitions and HCT33–37, PHT20–23, and LET19–21, including the full source mass and the distinction between the source products and the moment determinants.

## Endpoint and scalar-coordinate checks

1. WGP1 agrees with the literal source products in LET19 and PHT20. Since the indices in `D_{l,N}` are inclusive, the quotient `D_{l,q-1}/D_{l,2q-1}` leaves precisely `a=q,...,2q-1` in the denominator. The other quotient leaves precisely `a=q+1,...,2q`. There are `q` terms in each range. WGP2 therefore has the correct minus sign and both endpoints.

2. On the second range, `b=a-1` gives `a+j+1/2=b+j+3/2=q(x_b+(j+1)/q)`, whereas the first range gives `b+j+1/2=q(x_b+j/q)`. Across the two ranges and `2l` values of `j`, there are `4lq` factors. WGP3 consequently retains exactly `4lq log q`. The original integer parameters ensure positive integral `q` and even `q=2n`; no independent continuous replacement of the packet degree occurs.

## Midpoint bound and its signed applications

For each cell, both displayed integral Taylor formulas are correct, including the reversed integration limits for negative displacement. Integrating the absolute bound `||F''|| u^2/2` over a cell gives `||F''||/(24 q^3)`. Summing over `q` cells and multiplying by `q` proves WGP4, with denominator `24q`.

The integral remainder `F(x_b+u)-F(x_b)-uF'(x_b)` has the sign of `F''` when it has constant sign. Thus the signed error `sum F(x_b)-q integral F` has the *opposite* sign. The prose immediately after WGP4 states the resulting midpoint inequalities correctly. Its use in WGP5 is unambiguous and correct.

The three integrals are respectively `2 log 2-1`, `log 2`, and `1/2`. Their second derivative bounds on the literal interval `[1,2]` are `1`, `2`, and `6`. Accordingly:

- the concave logarithm has nonnegative midpoint excess at most `1/(24q)`;
- the convex reciprocal has nonnegative midpoint deficit at most `1/(12q)`;
- the convex inverse square has nonnegative midpoint deficit at most `1/(4q)`.

These are exactly all signs and constants of WGP5.

## Taylor sums and finite error

WGP6 follows by integrating the exact rational identity `1/(1+u)=1-u+u^2/(1+u)`. It holds for every nonnegative `u`; the upper bound for its remainder does not require `u<1`.

Writing `N=2l`, the shifted power sums are

\[
\sum_{j=0}^{N-1}(j+(j+1))=N^2,
\quad
\sum_{j=0}^{N-1}(j^2+(j+1)^2)=\frac{2N^3+N}{3},
\quad
\sum_{j=0}^{N-1}(j^3+(j+1)^3)=\frac{N^4+N^2}{2}.
\]

They yield WGP7 exactly. In particular the coefficient of `sum x_b^{-2}` is `(8l^3+l)/(3q^2)` after the Taylor factor `1/2`; the entire nonnegative Taylor remainder enters with a minus sign because the original logarithm sum is negative. WGP8 is exact.

WGP9 uses the exact cubic numerator sum and `sum x_b^{-3} <= q`. Both the number of remainder summands, `4lq`, and the powers of `q` are correct.

Let `A=(8l^3+l)/(3q^2)`. Substitution of WGP5 into WGP8 gives exactly

\[
\mathcal E=-4l\varepsilon_0
 +\frac{4l^2}{q}\varepsilon_1-A\varepsilon_2-\mathcal R.
\]

Bounding the three negative terms separately gives

\[
\mathcal E\ge-\frac l{6q}
 -\frac{8l^3+l}{12q^3}-\frac{8l^4+2l^2}{3q^2},
\]

and retaining just the positive term gives `E <= l^2/(3q^2)`. The main quadratic term is `A q/2=(8l^3+l)/(6q)`. This proves every coefficient and one-sided sign in WGP10.

For `m=1`, `q=(4l+2)^2`, so the stated error is `O(1)` and `-4l^2 log 2` contributes on the `q` scale, with its coefficient unchanged. For each fixed integer `m>=2`, `q` has order `l^3`; the negative remainder terms have orders `l^-2`, `l^-6`, and `l^-2`, while the positive bound has order `l^-4`. The stated `O(l^-2)` follows.

## Exact recurrence and receiving signs

The `H_j^(a)` and `c_j^(a)` definitions agree with HCT1 and HCT9, including all original Gamma mass factors. HCT37 supplies, for each shift `s`, two copies of `log c_j^(q+s)` for `j<n`, one `log c_n^(q+s)`, and two copies of `log c_j^(q+s+1)` for `j<n`. PHT22 subtracts exactly `log c_0^(q+s)` from the low endpoint.

Consequently the coefficient sum per shift is `2n+1+2n-1=4n=2q`. Substituting `log c=lambda+2 log q` gives exactly `4q log q` per shift and `4lq log q` in total. This cancels the explicitly retained scale term from the original products. The resulting expression is precisely WGP11, with both high ranks, both odd blocks and the low correction retained.

PHT23 identifies this result with the literal `W_k` in LET19. LET20 places `W_k` in `mathfrak T_k` with coefficient `+1`, and LET21 places it in the arithmetic receiver with coefficient `-1`. Thus the WGP10 error interval transfers as `[-E^-,E^+]` into `W_k`, and as `[-E^+,E^-]` into the corresponding arithmetic contribution. The final receiving-sign sentence is correct.

## Optional proved refinement, if constant-scale precision becomes useful

The existing WGP10 is sufficient for its stated scope. A cubic refinement resolves its `O(1)` remainder at `m=1` while keeping exactly the same endpoints. Here is a complete derivation, supplied as optional mathematics rather than a requested repair.

For `u>=0`, integrate

\[
\frac1{1+u}=1-u+u^2-\frac{u^3}{1+u}
\]

to obtain

\[
\log(1+u)=u-\frac{u^2}{2}+\frac{u^3}{3}-r_4(u),
\qquad r_4(u)=\int_0^u\frac{t^3}{1+t}\,dt,
\qquad 0\le r_4(u)\le u^4/4.
\]

Set `A3=8l^4+2l^2` and

\[
A_4=\sum_{j=0}^{2l-1}\big(j^4+(j+1)^4\big)
=\frac{192l^5+80l^3-2l}{15}.
\]

The last equality follows by telescoping fifth powers or expanding the standard finite fourth-power sum; with `N=2l` the same polynomial is `2N^5/5+2N^3/3-N/15`.

Apply WGP4 to `x^-3`: its second derivative is `12x^-5`, so

\[
\sum_bx_b^{-3}=3q/8-\varepsilon_3,
\qquad 0\le\varepsilon_3\le1/(2q).
\]

Convexity of `x^-4` and the literal integral `integral_1^2 x^-4 dx=7/24` also give `sum_b x_b^-4 <= 7q/24`. The nonnegative quartic integral remainders therefore have sum `Q4` satisfying

\[
0\le Q_4\le\frac{A_4}{4q^4}\sum_bx_b^{-4}
\le\frac{7A_4}{96q^3}.
\]

The exact product expansion becomes

\[
\begin{aligned}
P_k={}&-4lq\log q-4lq(2\log2-1)-4l^2\log2
 +\frac{8l^3+l}{6q}-\frac{l^4+l^2/4}{q^2}+E^{(3)},\\
E^{(3)}={}&-4l\varepsilon_0
 +\frac{4l^2}{q}\varepsilon_1
 -\frac{8l^3+l}{3q^2}\varepsilon_2
 +\frac{A_3}{3q^3}\varepsilon_3+Q_4.
\end{aligned}
\]

Every sign follows from the negative outer sum in WGP3. In particular

\[
-\frac l{6q}-\frac{8l^3+l}{12q^3}
\le E^{(3)}\le
\frac{l^2}{3q^2}+\frac{A_3}{6q^4}+\frac{7A_4}{96q^3}.
\]

This has error `O(l^-1)` at `m=1` and `O(l^-2)` at every fixed `m>=2`. For `m=1`, the exact original `q=(4l+2)^2` implies the original WGP10 error satisfies `E=-1/256+O(l^-1)`. No endpoint or source factor has been discarded in this refinement. Its arithmetic contribution still carries the coefficient `-1` prescribed by LET21.
