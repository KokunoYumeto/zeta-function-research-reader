# Independent review of the cubic product delta and signed growth receiver

Mathematical verdict: **PASS** for the added WGP12–14 and the complete WGR1–15. No equation or inequality defect was found. Two local exposition clarifications were sent to the author and then installed and checked: the inherited boundary map domains and section identity are now explicit, and the whole parameter-dependent Gamma receiving interval is now correctly described as using the original source constants. The final checked receiver source pin is `9b42c91c8cbc5e8a01aaf130f9d5d5ac3855880bfe85dd72c8ac6add2bfb5479`.

This bounded review did not repeat the accepted WGP1–11 review, edit either proof source, build a PDF, run Lean, or publish anything. The entire new `signed_growth_receiver.tex` was read. The earlier full JSR20–21 provider, its JSR13–15 signed identities and WRC3–5 interval were inspected directly. GCR41–44 was also read to verify the exact kernel/boundary map inherited by WGR7–8. The GEL18–19 interface was read with its fixed-packet hypotheses; the complete GEL analytical argument is handled by its independently assigned review rather than re-reviewed here.

## Source pins at this review

Paths are relative to `work/backpropagation_20260913/root/joint_schur_intake/`.

| Source | SHA256 |
| --- | --- |
| `growing_w_20260914/original_product_expansion.tex`, added WGP12–14 only | `e6122af0f0cc54028ceee5383c97070e7738d9d8ec1a5bc5481b349761e5fbfe` |
| `growing_w_20260914/signed_growth_receiver.tex`, WGR1–15 | `b52e4ad0b1bfef2cc0424b655a89184f4fec7a558fe2cb9e8fc86bb423a81824` |
| `growing_w_20260914/signed_growth_receiver.tex`, final checked clarification delta | `9b42c91c8cbc5e8a01aaf130f9d5d5ac3855880bfe85dd72c8ac6add2bfb5479` |
| `growing_w_20260914/equilibrium/GAMMA_ENSEMBLE_LEADING_RETURN.tex`, GEL18–19 interface | `2014e7fefdcd963b70b00fb89d597e24c0826582a2541dd1ff44d63051979fc1` |
| `next_bulk_density/future_hankel/receiving/SIGNED_RETURN_RECEIVER.tex` | `2d353afa6e5f0ed9f8ac9756356447b2d0538e30a6688154ca4dc8cd1ddbfb5c` |

The accepted RWB1–27 proof and its separate complete review supply the finite bounds used here. The GEL pin records the source interface inspected, not an independent certification here of its entire analytical proof.

The final local delta uses `B_obs=im Lambda` for the boundary target, avoiding a collision with the already defined positive high-error constant `B`. It prints `Lambda:E->B_obs`, `K=ker Lambda`, `I_K:K->E`, `S_*:B_obs->E`, `Lambda S_*=I_B_obs`, and the coefficient isomorphism `[I_K,S_*]:K direct-sum B_obs->E`. The text after WGR11 now says “an evaluated bound with the original source constants.” Both changes were read directly and resolve the two precision comments without altering the reviewed mathematics.

## Added cubic product terms, WGP12–14

The installed refinement agrees with the complete derivation in `REVIEW_PRODUCT.md`. The exact integral remainder has the stated negative sign in `log(1+u)` and therefore the positive sign `+Q_4` after the original negative product sum. The finite fourth-power sum is correct:

\[
A_4=\frac{192l^5+80l^3-2l}{15}.
\]

Its newly added induction proof is valid: the difference of `2N^5/5+2N^3/3-N/15` between `N+1` and `N` is `N^4+(N+1)^4`, and both the finite sum and its polynomial value start at zero when `N=0`.

The inverse-cube midpoint deficit lies in `[0,1/(2q)]`; the inverse-fourth-power midpoint sum is at most `7q/24`. Consequently `0<=Q_4<=7A_4/(96q^3)`. The cubic contribution is exactly

\[
-\frac{A_3}{3q^3}\frac{3q}{8}
=-\frac{l^4+l^2/4}{q^2}.
\]

All five signed terms in the exact WGP14 error agree with the integral calculation. The lower and upper WGP13 bounds follow by retaining their respective negative and positive terms. They give `O(l^-1)` at `m=1` and `O(l^-2)` at fixed `m>=2`; because `q=(4l+2)^2` at `m=1`, the older WGP10 error is `-1/256+O(l^-1)`. The original source products, their two endpoint ranges and the opposite arithmetic receiving sign are preserved.

## WGR1–4: original coordinates, source errors and signed Gamma return

The polynomial `f(S)=prod_(j<l)(S-c-2j-1/2)` agrees with the earlier original displacement `t_j=2j+1/2`. The polynomial `chi`, its multiplicity, `E=C[S]/(chi)`, and the original source line are unchanged.

For the coefficient map from the `S` monomial frame into the `y` monomial frame, the binomial formula is exactly

\[
J_{hj}=\binom jh c^{j-h}i^h.
\]

It is triangular with diagonal `i^j`, so its determinant has modulus one. Its Gram congruence `J^* M J` consequently does not introduce any determinant power of `q`. The moment index in WGR2 is the literal exponent of `y`, and the two high relation indices `q+r-1` give exactly `2q-1` and `2q` at `r=q,q+1`.

The original full-source estimates give `e_0 in [-a_0,b_0]` and `e_q+e_(q+1) in [-A,B]` with precisely the displayed definitions. In the earlier WRC notation, `A=b_k^+` and `B=b_k^-`; no sign is exchanged in translating notation. The finite threshold is exactly the inherited one, and the fixed-packet orders quoted in WGR3 agree with LET and CTR.

Substitution into the original relation identity gives

\[
\mathfrak T_k=W_k-e_0+e_q+e_{q+1},
\qquad
\mathcal H_k=-W_k+e_0-e_q-e_{q+1}.
\]

These are the same WRC3 and JSR14–15 identities, retaining the negative original low relation logarithm in `T`.

## WGR5–6: evaluated interval and containment

Both entries in the maximum defining `w^-` are proved lower bounds from RWB; `w^+=6lq` is its proved upper bound. This is valid for all original packet integers, while the return to the original `chi` metric uses the additional stated source threshold.

In `H=-W+e_0-(e_q+e_(q+1))`, independent substitution of the lower and upper values gives exactly

\[
-w^+-a_0-B\le\mathcal H_k\le-w^-+b_0+A.
\]

At a fixed exact `W`, the earlier WRC5 endpoints are `-W-a_0-B` and `-W+b_0+A`. Since `w^-<=W<=w^+`, the new lower endpoint is no greater and its upper endpoint no smaller. Thus the claimed containment is correct: the value of this new interval is its explicit growing-family evaluation, not a narrower enclosure of a known exact finite `W`.

The constants `A,B,a_0,b_0` retain the original source parameters. The source independence belongs to `W` and its bounds `w^-,w^+`, not to the entire interval after adding those errors. The author was sent this precise wording clarification.

## WGR7–9: exact quotient, retained kernel and boundary

The inverse quotient formula is used at the original four indices, all satisfying `N>=q-1`; the remainder map is onto there. It consequently defines a positive definite metric on the same `E` for either source.

The inherited exact sequence, verified directly in GCR41–44 and JSR13, is

\[
0\longrightarrow K=\ker\Lambda
\mathop{\longrightarrow}^{I_K}E
\mathop{\longrightarrow}^{\Lambda}B=\operatorname{im}\Lambda
\longrightarrow0.
\]

The coefficient section `S_*:B->E` satisfies `Lambda S_*=I_B`. These are the types and section identity requested as an explicit local clarification next to WGR7.

For a positive quotient metric `G`, set `Q=(Lambda G^-1 Lambda^*)^-1` and `L=G^-1 Lambda^* Q`. Then

\[
\Lambda L=I_B,\qquad I_K^*GL=0,\qquad L^*GL=Q.
\]

Indeed the first identity is the definition of `Q`, the second follows from `Lambda I_K=0`, and the last is `Q(Lambda G^-1 Lambda^*)Q=Q`. The section difference `S_*-L` takes values in `K`. Thus changing `[I_K,S_*]` to `[I_K,L]` is triangular with identity diagonal. The latter frame has block diagonal Gram `diag(H_K,Q)`, so

\[
\det H_K\det Q=|\det[I_K,S_*]|^2\det G.
\]

This proves WGR8 including its determinant direction and complex modulus square. The common frame factor cancels between the two sources. The same proof works when either summand has dimension zero using determinant one for its empty factor.

The original normalized source comparison gives nonnegative source, quotient, kernel and boundary determinant deficits. With the actual dimensions kept, the coefficient `q log A_k` splits into `dim(K)log A_k+dim(B)log A_k`, and the just-proved determinant identity gives `b_N^K+b_N^B=b_N`. The inherited Schur comparison gives `b_N<=Xi_(k,N)`. Thus WGR9 is the exact JSR20 interval: the two low deficits enter negatively, the two high deficits positively. It also applies to the individual retained kernel and boundary deficits with their corresponding superscripts.

No kernel is chosen anew and no cohomology direction is killed by the estimate. The product-jet observation from JSR13 remains `(0,Y)->Lambda Ejet^-1 U_f^-1 Y`, sending `(0,U_f Ejet v)` to the same original `Lambda v`.

## WGR10–11: arithmetic and HC finite bounds

The original equality is `B_ar=B_0+H+delta_sigma`. Adding the interval `delta_sigma in [-a^-,a^+]` to WGR6 gives precisely the two endpoints of WGR10. Replacing `a^-` and `a^+` by their respective larger `D^-` and `D^+` preserves the outer enclosure with the stated signs.

Subtracting the unchanged `4q log(D_h k)` gives the original residual. Its previously proved independent nonnegativity allows the lower endpoint to be replaced by its maximum with zero, and does not change the upper endpoint. This proves WGR11 on the combined original source and HC thresholds. The source threshold for WGR3 does not replace the earlier HC threshold; the text retains both.

## WGR12–13: actual fixed-packet arithmetic growth

The full original JSR17–21 source was inspected directly. Its simple-multiplicity branch gives `delta_sigma/(kq)=O_h((log k/k)^(5/7))`. For each fixed `m>=2`, its lower and upper asymptotic constants at scale `q log k` are exactly `-(64m+245)` and `128m+490`. A finite lower liminf and upper limsup imply eventual boundedness at that scale; multiplication by `log k/k` then gives `delta_sigma/(kq)->0`. This argument uses an eventual two-sided bound, not a presumed exact limit.

The Gamma errors from WGR3 also vanish after division by `kq`. Since `l/k->1/4`, RWB23 gives

\[
\liminf\frac{W_k}{kq}\ge\log\frac{27}{8\pi},
\]

while RWB27 gives `limsup W_k/(kq)<=3/2`. In the exact identity `Delta_Gamma=-W_k+e_0-e_q-e_(q+1)+delta_sigma`, all other divided terms tend to zero. Reversing the signs gives every bound in WGR13. Its strictly negative limsup proves eventual strict negativity for fixed original parameters, without asserting either an exact finite threshold for that negativity or a limit not yet supplied by GEL.

## WGR14–15: proved GEL limit and baseline consequence

The GEL18 interface inspected here states `W_k/(lq)->C_Gamma` for fixed original multiplicity and packet sequence, with the complete original parity and low-moment factors retained. GEL18a gives its analytic interval `4log(27/(8pi))<=C_Gamma<=6`. The receiving argument uses exactly that fixed-packet scope.

Multiplying the supplied limit by `l/k->1/4` and adding the already proved vanishing terms from WGR3 and WGR12 gives `Delta_Gamma/(kq)->-C_Gamma/4`. This proves WGR14's sign, factor and use of the GEL result. The independent GEL analytical audit remains the evidence for that provider theorem; nothing here assumes a sharper error term from it.

The remaining consequences are direct exact differences:

\[
\frac{B_0-B_{\rm ar}}{kq}=-\frac{\Delta_\Gamma}{kq}
\longrightarrow\frac{C_\Gamma}{4},
\]

\[
\frac{R_k-B_0}{kq}
=\frac{\Delta_\Gamma}{kq}-\frac{4\log(D_hk)}k
\longrightarrow-\frac{C_\Gamma}{4}.
\]

Here `D_h>0` is fixed on the original packet. Because `R_k>=0`, one has `B_0/(kq)>=(B_0-R_k)/(kq)` at every admitted degree. Taking the liminf proves the stated necessary lower bound `liminf B_0/(kq)>=C_Gamma/4`.

This is a necessary baseline estimate following from a nonnegative residual and an evaluated difference. It does not set either baseline or residual equal to zero. The text also correctly retains the distinction between the proved `o(lq)` GEL remainder and the finer unproved `o(q)` control that would require additional calculation. No unsupported RH consequence is claimed.
