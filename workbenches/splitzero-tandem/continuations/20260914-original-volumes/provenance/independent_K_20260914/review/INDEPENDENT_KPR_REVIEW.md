# Independent review of the positive macroscopic comparison return

Mathematical verdict: **PASS for the complete KPR1–16 proof.** No mathematical repair is required. This is an **exploratory comparison family**, not a canonical replacement of the original tensor source. The proof evaluates an independently chosen Gamma reference order; it does not show that the original tensor, exterior or spectral-sum construction requires that order.

User constraint relayed verbatim by root: “Don’t do any insert stuff by hand though. If it is not actually suggested by the research, then it shouldn’t be inserted by hand.” The review preserves the resulting provenance and scope. Root owns the separate intrinsic-source question; no new source factor, canonical reference change, build or publication was performed in this review.

## Exact material checked

All paths below are relative to `work/backpropagation_20260913/root/joint_schur_intake/growing_w_20260914/independent_K_20260914/`.

| Source | SHA256 |
| --- | --- |
| `INDEPENDENT_ORDER_POSITIVE_RETURN.tex`, complete KPR1–16 | `3c70d26a7a69155f911bf1932c1f77d6c73c46d940ee277338adada3ca6d5cac` |
| `INDEPENDENT_ORDER_ORIGINAL_MAPS.tex`, exact imported IKO17–19 interface | `22a42086fb808c8dca688a4d34b363539e598b79d8df2510ef62f2aaf1868513` |
| `verify_positive_log_fractions.py` | `2149927e58b48df46bb2994921ebf3fc23a6cd669161c934fadfb35cf826310a` |
| `POSITIVE_LOG_FRACTIONS.json` | `b4dbdf2a56b7f393dd6eca13489a19f035a29f456e65c2ba2d8b7e7cb9679091` |

The entire KPR proof and exact-arithmetic script were read. The original baseline source BSL13–22 and the full IKO17–19 receiving identities were read directly to check the imported limits and signs. The whole IKO proof has its separate assigned independent review, and its full transport was not re-reviewed here. The MFG proof was authored by this reviewer and was therefore assigned to a separate independent subagent; its separate review, rather than self-certification, supplies the full MFG audit.

## KPR1–3: original probability moments and the polynomial transport

The equilibrium measure for `V_0(x)=pi sqrt(x)-2 log x` is a probability with compact support `[a_*,b_*]` bounded away from zero. Its original dilation identity is `M_1=E sqrt(X)=6/pi`. All moments used are consequently finite.

The map `T_t(x)=x+t x^2` is admissible for both signs of `t` when `|t|<1/(4b_*)`: it stays positive, has derivative `1+2tx>1/2`, and its pair-difference factor `1+t(x+y)` also exceeds `1/2` on the whole support. Therefore it gives a differentiable family of admissible probabilities through the original equilibrium, with no support direction omitted.

The exact pair-energy change is `E log(1+t(X+Y))` for independent copies, so its derivative is `2M_2`. The potential derivative is `(pi/2)M_3-2M_2`. Stationarity of their difference gives `4M_2-(pi/2)M_3=0`, hence

\[
M_3=\frac8\pi M_2.
\]

Cauchy–Schwarz applied to `X^(1/4)` and `X^(3/4)` gives `M_2^2<=M_1 M_3`. Division by positive `M_2` yields `M_2<=48/pi^2`, exactly as in KPR3.

The finite geometric identity

\[
\frac1{1+x^2}=\sum_{j=0}^{7}(-1)^j x^{2j}
                 +\frac{x^{16}}{1+x^2}
\]

has strictly positive integral remainder on `(0,1)`. Its displayed eight-term integral sum multiplied by four is exactly `135904/45045>3`. This independently verifies the rational justification of `pi>3` and hence the strict upper bound `M_2<16/3`.

## KPR4–8: the actual marked field in a specified trial probability

The trial probability is the explicit dilation `X->s^2 X` of the original equilibrium, and the field retains `h_lambda(x)=integral_0^lambda log(x+4u^2)du`. Its pair energy gains `2log s`, the negative square-root potential contributes `-6(s-1)`, and the original positive logarithmic term gains `4log s`.

The exact identity

\[
\log(s^2x+4u^2)=2\log s+\log x
                    +\log(1+4u^2/(s^2x))
\]

then yields the full trial gain

\[
(6+4\lambda)\log s-6(s-1)+2\lambda\mathcal L
 +2\int_0^\lambda E\log(1+4u^2/(s^2X))\,du.
\]

This proves KPR5 with its original field intact. In particular the last positive term is retained rather than dropping the actual marking factor in favor of a pure power.

For fixed `A>0`, the second derivative of `log(1+A/x)` is `A(2x+A)/(x^2(x+A)^2)>0`. Jensen's inequality therefore gives the correct lower direction after replacing `X` by `M_2`. The inequality `log(1+v)>=v/(1+v)` has derivative remainder `v/(1+v)^2>=0`. Bounding the remaining positive denominator from above before integrating gives precisely

\[
2\int_0^\lambda E\log(1+4u^2/(s^2X))du
\ge\frac{8\lambda^3}{3(s^2M_2+4\lambda^2)}.
\]

At the stated `lambda=1/4` and `s=7/6`, use `M_2<16/3`. The denominator comparison is `(7/6)^2(16/3)+1/4=811/108`, and the resulting fraction is `9/1622`. Both numerical coefficients were recomputed directly. A weak lower inequality at this step is valid even though the moment comparison is strict. The variational supremum is at least this trial value, proving KPR8.

The admissible trial is used to estimate the comparison field. It supplies no assertion that the original research construction chooses its independent order or adds that marking factor to its canonical source.

## KPR9–11: logarithmic moment input and the exact source correction

The previously proved identity and lower estimate are

\[
2\mathcal L-4(2\log2-1)=\mathcal C_\Gamma
\ge4\log(27/(8\pi)).
\]

Combining the logarithms gives `mathcal L/2>=log(27/(2pi))-1`. The positive integral for `22/7-pi` implies the strict inequality `mathcal L/2>log(189/44)-1`. This verifies the factor `1/2` and all constants in KPR9.

The exact primitive in MFG20 is `A(z)=z^2 log(z)/2-3z^2/4`. Substituting the four values `5/2,3/2,2,1` into twice its signed difference gives

\[
Q(1/4)=\frac{25}{4}\log(5/2)-\frac94\log(3/2)
                      -4\log2-\frac32.
\]

Subtracting this from KPR8 and then applying the strict KPR9 bound yields exactly the five logarithms and constant `-1/2+9/1622` in KPR11. The negatively signed logarithm is `log(5/2)`, with coefficient `-25/4`; this sign is preserved in the subsequent rational enclosure.

## KPR12–14: independent exact rational verification

For `r=(x-1)/(x+1)` with `x>1`, integrating the positive geometric series of `2/(1-t^2)` gives

\[
S_{20}(r)<\log x<S_{20}(r)+\frac{2r^{41}}{41(1-r^2)}.
\]

The first omitted power is exactly `41`; every later denominator is at least `41`, so the tail estimate is correct and has positive denominator. All five rational `r` values in KPR13 are correct.

The script was read and its asserted inequalities match these written inputs. Independently of that script and its output, this reviewer executed a separate BigInt fraction calculation for all ten table comparisons. Every comparison passed. The signed table substitution reproduced exactly

\[
\frac{9279677}{40550000000},\qquad
\frac{9279677}{40550000000}-\frac1{5000}
       =\frac{1169677}{40550000000}>0.
\]

That separate execution also checked `135904/45045>3`. Its record is `KPR_TABLE_INDEPENDENT_CHECK.json`. An earlier independent calculation applied the same twenty-term series without rounding the individual logarithms to `10^-8`; the resulting stronger lower rational bound and its positive gap above `1/5000` are retained in `QUARTER_SIGN_INDEPENDENT_RATIONAL.json`. Neither check uses numerical quadrature or a finite-matrix experiment.

Consequently the exact conclusion

\[
\Psi(1/4)>\frac{9279677}{40550000000}>\frac1{5000}>0
\]

is proved by the written variational and moment arguments together with the explicit finite rational sums.

## KPR15–16: original-packet comparison and simultaneous baseline change

The imported MFG theorem concerns the actual `f_L` and gives the homogeneous limit at `L=q/4`. The exact original-packet transport IKO17 has absolute error at most

\[
(2q+2)(b_+-b_-)+2(L_q+L_{q+1}+L_1)=O(q/e)=o(q^2).
\]

It uses the same original polynomial in both numerator and denominator forms. Therefore its comparison transfers the coefficient `Psi(1/4)` to the return of the original packet under this exploratory reference order, as KPR15 states. Because `q` is divisible by four, the exact admissible order is `K=4(q/4)+1=q+1`; the final `+1` is retained.

For the baseline, IKO12 and IKO18 give the exact equalities

\[
\mathcal B_k^{(q+1)}=\mathcal B_k^\sigma+\mathfrak T_{k;q/4},
\qquad
\mathcal B_k^{\rm ar}=\mathcal B_k^{(q+1)}
                    -\mathfrak T_{k;q/4}+\delta_k^\sigma.
\]

The original-packet theorem BSL16 gives `B_sigma/q^2->C_B`. The old arithmetic source estimate gives `delta_sigma/(kq)->0`; since `k/q->0` on the original packet, this implies `delta_sigma/q^2->0`. Thus the three KPR16 limits are respectively `C_B+Psi(1/4)`, `-Psi(1/4)`, and `C_B`. Every sign is consistent with the exact finite identity, and the positive return is accompanied by the change of its own reference baseline.

The inherited BSL20 frame identity retains the original kernel and boundary summands and the full common determinant factor. Its factor cancels only with the prescribed four endpoint signs. The combined mixed equality therefore receives the same transition law; KPR does not assign the combined coefficient separately to each kernel or boundary summand.

The result proves a positive return within an evaluated comparison family and its exact relation to the invariant arithmetic quantity. It does not derive the independent reference order from the original spectral-sum or exterior operation. That provenance question remains root's distinct current task, in accordance with the user's explicit constraint.
