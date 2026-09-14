# Independent finite-combination check

Date: 2026-09-14. Scope: QGT18–28 against WGP13 and LER17–23, including their definitions. The QGT source was not edited. The density and convex-secant arguments are outside this check and are being checked independently by the parent reviewer.

**Result:** No concrete algebraic error was found in QGT18–28. The finite centres, signs, copied constants, and distinction between fixed `m >= 2` and `m = 1` are correct. The preceding high-block estimate QGT17 is used as input; its proof is covered by the parent's separate review.

## Exact signed combination

Use the actual original packet `q = [1 + (4l+1)(m-1)](4l+2)^2 = 2n`, with `l,m >= 1`. Write `g = 2 log 2 - 1`. WGP13 and LER18 say exactly

\[
P_k=-4lq\log q+p^{\rm c}_{q,l}+\delta_{q,l},\qquad
-p^-_{q,l}\le\delta_{q,l}\le p^+_{q,l},
\]
\[
\log(\mu_{q+l}/\mu_q)=F_{q,l}-K_{q,l}+r_{q,l}+\varepsilon_{q,l},\quad
-T_{q,l}\le r_{q,l}\le0,\quad |\varepsilon_{q,l}|\le E_{q,l}.
\]

Substituting these and QGT17 in QGT18 gives the exact identity

\[
W_k=\mathcal V^{\rm c}_{q,l}+\delta_{q,l}+\xi_{q,l}-r_{q,l}-\varepsilon_{q,l}.
\]

Consequently the lower error is `-p^- - U - E`, and the upper error is `p^+ + U + T + E`, as in QGT22. Replacing `p^c + delta` by the exact finite sum `P-tilde` gives QGT20. In particular `K` enters the centre positively, and the one-sided low Taylor error enters the upper endpoint positively. The logarithmic coefficient cancels exactly as `-4lq + (4q+2)l - 2l = 0`; the remaining low logarithm is `-2l log(4/pi)`.

## Copied constants and weighted centre

In WGP13, `A3 = 8l^4 + 2l^2` and `A4 = (192l^5 + 80l^3 - 2l)/15`. Therefore

\[
p^-_{q,l}=\frac l{6q}+\frac{8l^3+l}{12q^3},\qquad
p^+_{q,l}=\frac{l^2}{3q^2}+\frac{8l^4+2l^2}{6q^4}
+\frac{7(192l^5+80l^3-2l)}{1440q^3}.
\]

These are exactly QGT21. Its cubic Taylor contribution is negative: `-A3/(8q^2) = -(l^4+l^2/4)/q^2`.

For the low endpoint, the literal sums over `j = 0,...,2l-1` of `(j+1/2)^r`, divided respectively by `2q`, `-8q^2`, `24q^3`, and `64q^4`, give

\[
\frac{l^2}{q},\quad
-\frac{l(16l^2-1)}{48q^2},\quad
\frac{l^2(8l^2-1)}{48q^3},\quad
T_{q,l}=\frac{l(768l^4-160l^2+7)}{7680q^4}.
\]

The last expression is the positive bound for the magnitude of the negative fourth-order remainder. The LER17 constant `E = 51l/(16q^5)` and LER20 bound `0 < K <= 3l/(32q^3)` are retained correctly.

For QGT23–24 the three starting shifts are exactly `d = -3/4, -11/4, 1/4`, at ranks `n,n+1,n`, with weights `1,1,2`. The rank `n+1` shift follows from `q-3/4 = 2(n+1)-11/4`. The weighted sums are

\[
n+(n+1)+2n=2q+1,\qquad
\frac34+\frac{11}4+2\frac14=4,\qquad
\frac{1+1+2}{2}=2.
\]

The beta dilation contributes exactly `2(n+1)l log(1+1/n)`. Hence the error in QGT24 is `M(2l^2+4l)` with the displayed sign of that dilation.

To verify every term of QGT25, write the QGT24 remainder as `rho`, with `|rho| <= M(2l^2+4l)`. Subtracting `lq C_Gamma`, where `C_Gamma = 2 L_0 - 4g`, gives exactly

\[
\begin{aligned}
W_k-lq\mathcal C_\Gamma={}&\rho+\xi+\delta+l\mathcal L_0
+2(n+1)l\log(1+1/n)-4l^2\log2\\
&+\frac{8l^3+l}{6q}-\frac{l^4+l^2/4}{q^2}
-2l\log(4/\pi)-\frac{l^2}{q}\\
&+\frac{l(16l^2-1)}{48q^2}
-\frac{l^2(8l^2-1)}{48q^3}
+K-r-\varepsilon.
\end{aligned}
\]

The triangle inequality gives precisely `U + D` in QGT25–26. All its displayed summands are nonnegative for `l >= 1`.

## Endpoint distinction

The inequality `q >= (4l+2)^2 >= 16l^2` makes `D = O(l^2+l)` uniformly in `m`. In detail, the two leading contributions are `2Ml^2` and `4l^2 log 2`; the dilation is at most `2(n+1)l/n <= 4l`; the remaining nontrivial rational scales are `l^3/q = O(l)`, `l^4/q^2 = O(1)`, `l^5/q^3 = O(l^-1)`, `l^2/q = O(1)`, `l^3/q^2 = O(l^-1)`, and `l^4/q^3 = O(l^-2)`. All smaller displayed rational terms obey the same asserted bound. LER20 gives `K = O(l^-5)`, while `T = O(l^-3)` and `E = O(l^-9)`. QGT16 gives `U = O(l sqrt(q))`. This proves the scale asserted in QGT27.

For each fixed `m >= 2`, the exact packet satisfies

\[
\frac{q}{l^3}\longrightarrow64(m-1)>0.
\]

Thus `l/sqrt(q) -> 0` and `l^2/q -> 0`. Dividing the finite QGT26 inequality by `q` proves QGT28 for these original packets.

For `m = 1`, retain exactly `q=(4l+2)^2` and `n=q/2`. The bounds themselves have the explicit limits

\[
\frac{\mathcal U_{q,l}}q
=A\frac l{\sqrt q}\left(\frac3{\sqrt2}+\sqrt{\frac12+\frac1q}\right)
\longrightarrow\frac A{\sqrt2},
\qquad
\frac{\mathcal D_{q,l}}q\longrightarrow\frac M8+\frac{\log2}{4}.
\]

For the second equality, `l^2/q -> 1/16`; only the terms `2Ml^2` and `4l^2 log 2` survive division by `q`. Every other term vanishes by the finite estimates above. Therefore QGT26 proves the finite conclusion

\[
\limsup_{l\to\infty}
\left|\frac{W_k-lq\mathcal C_\Gamma}{q}\right|
\le\frac A{\sqrt2}+\frac M8+\frac{\log2}{4}
\quad(m=1).
\]

These are limits of the explicit bounds, **not a claimed limit of the actual centred Gamma functional**. They support the source's explicit statement that this estimate does not identify the actual `m=1` quotient limit.

## Incidental source issue and handoff

During the read, QGT7 contained a stray comma in `q^{,2as+2s(s-1)+s/2}`. The immediately following derivation and QGT11 show the intended exponent. This was reported to the parent reviewer, who confirmed that the main agent is repairing it. It is outside QGT18–28 and no change was made here.
