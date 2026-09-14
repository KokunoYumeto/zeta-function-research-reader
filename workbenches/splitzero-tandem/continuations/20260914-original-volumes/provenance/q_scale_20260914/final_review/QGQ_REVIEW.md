# Independent review of the original m=1 quantitative bound

**Accepted.** The complete QGQ1–9 source `ORIGINAL_M_ONE_QUANTITATIVE_BOUND.tex` was read against the accepted finite combination derivation and the original summands of QGT16,21,25–26.

Source SHA256: `9803d6ddf301807a1df7b4678b325241f6785f6ac1f4778c036037607ddc7dc6`.

The original packet `q=(4l+2)^2`, `n=q/2` gives `l/sqrt(q)->1/4`. The exact displayed identity for `U/q` therefore gives `A/sqrt(2)`.

The list for D is complete. After division by q, the two surviving summands are `2Ml^2` and `4l^2 log 2`, with limits `M/8` and `(log 2)/4`. The remaining linear terms and the rank correction are O(l); the two rational source terms are O(l), O(1); the constituent orders of p-minus are `l^-1,l^-3`; those of p-plus are `l^-2,l^-4,l^-1`. The three low polynomial terms have orders `1,l^-1,l^-2`, and the bounds for K,T,E have orders `l^-5,l^-3,l^-9`. Each follows from the literal substitution `q=l^2(4+2/l)^2`; each vanishes after division by q. No summand from QGT25 is omitted.

Dividing the already proved finite QGT26 inequality by q gives QGQ3 by the limits of its nonnegative bounds. The stated limsup is correct and does not assert a limit of the centred functional. All parameters and constants are inherited from the original construction. No source modifications or further hypotheses are needed.

## Exact centre extension QGQ4–9

The complete appended proof was read. EIQ29 establishes smoothness of the same logarithmic moment, so the displayed M2 maximum exists on the already verified compact parameter rectangle. The interval joining 2 to each point in QGQ5 lies inside that rectangle. Twice integrating the second derivative gives the same absolute Taylor remainder for both signs of v. After substituting v=(d+r)/s and integrating r from 0 to l, the exact finite bound is `M2[(|d|+l)^3-|d|^3]/(6s)`. Its coefficient in QGQ5 is correct.

The three original ranks and offsets have weights 1,1,2, so their signed offset sum is -3 and the sum of their second-order shift coefficients is `2l^2`. EIQ32 supplies exactly the additional `2(n+1)l log(1+1/n)` term. Thus all terms, signs and remainder denominators in QGQ6 are correct.

QGQ7 was checked term by term by inserting QGQ6 into the literal QGT21 centre and expanding the full LER17 expression. The only terms of order l^2 are `(2 L1 - 4 log 2) l^2`. The high remainder is O(l) by its displayed finite bound and `n>=8l^2`; all other terms have the already established O(l) or smaller size. Hence QGQ8 has the exact coefficient `L1/8-log(2)/4`, derived from the original formula.

Subtracting that proved centre limit from the exact two-sided QGT22 inequality leaves only U/q in the limit. Both product errors and both low errors tend to zero after division by q. This proves QGQ9 with width `A/sqrt(2)`. The proof retains this width and does not claim convergence of the actual centred functional. No proof issues remain in QGQ1–9.

The previous QGQ1–3 source was verified at its original SHA256 `733843385298bfb71a601bbf9362053fb1618a7bfc393bbfb97f211ebe10b1e1` in the source history. The previous review and receipt are preserved byte-for-byte in `final_review/history`; this review records the extended final edition.
