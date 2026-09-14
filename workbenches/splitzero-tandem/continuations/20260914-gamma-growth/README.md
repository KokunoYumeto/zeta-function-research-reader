# Growth of the Complete Original Gamma Return

*Finite bounds, the leading equilibrium limit, and the arithmetic return — 14 September 2026*

Read [the accepted 37-page paper](Gamma_Growth_and_Arithmetic_Return.pdf). This cut proves finite positive bounds and the leading growth of the complete universal Gamma centre \(W_k\), then carries that result through the original signed arithmetic receiver. It prints the full preceding LET/PHT/HCT calculation and all five new WGP/RWB/EIQ/GEL/WGR proof bodies.

The leading Gamma calculation is complete at the stated scale. The original baseline \(B_k^0\) and a finer, finite \(q\)-scale Hankel or recurrence remainder remain to be evaluated. The wider programme is active; this paper does not claim its completion or a proof of the Riemann hypothesis.

## Original objects and proved growth

The growing indices are the original integers

\[
 k=4l+1,\qquad e=1+k(m-1),\qquad
 q=e(k+1)^2=2n,\qquad l,m\ge1.
\]

The source remains
\(\sigma(y)=|\Gamma(1/4+iy/2)|^2/(2\pi)\), of mass \(\sqrt{2\pi}\). The complete primary multiplicities, four endpoint roles, low scalar moment, both high parity sectors, and actual quotient, kernel, and boundary maps remain attached to the calculation. The parameters \(0<\delta<1/2\) and \(\gamma>2\) remain in the original packet and its finite source-comparison constants.

Here \(W_k\) is the complete universal centre defined by the preceding LET/PHT/HCT determinant formula and positive \(c/d\) product, including the negative low-endpoint term and all four original source products. RWB proves, for every original \(l,m\ge1\),

\[
 \frac{lq}{64}\le W_k\le6lq.
\]

It also retains the stronger finite lower bound

\[
 \begin{aligned}
 W_k\ge{}&4lq\log\frac{27}{8\pi}-4l^2-6l\log(3/2)-3l\\
 &-\frac{9l}{4q-1}-\frac{2l(l+1/4)}q.
 \end{aligned}
\]

These are proved source estimates, not conclusions inferred from floating-point exploration. Their proof uses the original Gamma logarithmic derivative, shifted reciprocal moment, and even/odd polynomial integration-by-parts identity, with the low endpoint retained.

EIQ and GEL further prove the leading limit along the original growing family:

\[
 \frac{W_k}{lq}\longrightarrow\mathcal C_\Gamma
 =2\int\log x\,d\rho_{2,\pi}(x)-4(2\log2-1)>0.
\]

The measure \(\rho_{2,\pi}\) is the explicit positive, unit-mass equilibrium measure constructed in EIQ. Its density, unique global minimizing property, support, and whole exterior inequality are supplied with complete proofs. GEL proves the literal Heine integral and the change of variables \(t=q^2x\), preserving the source mass, Jacobian, and powers, and establishes the limit by upper and lower estimates and a moving-shift argument.

The resulting equilibrium remainder is **\(o(lq)\), not a proved \(o(q)\) remainder**. It must not be confused with the separately established \(o(q)\) source-comparison error.

## Smaller-scale source products

WGP evaluates the literal four-product contribution

\[
 P_k=\log D_{l,q-1}+\log D_{l,q}
       -\log D_{l,2q-1}-\log D_{l,2q},
 \qquad
 D_{l,N}=\prod_{a=0}^{N}\prod_{j=0}^{2l-1}(a+j+1/2).
\]

Its signed expansion is

\[
 \begin{aligned}
 P_k={}&-4lq\log q-4lq(2\log2-1)-4l^2\log2\\
 &+\frac{8l^3+l}{6q}-\frac{l^4+l^2/4}{q^2}
 +E^{(3)}_{q,l}.
 \end{aligned}
\]

WGP13 gives both finite signed bounds for \(E^{(3)}_{q,l}\). The actual endpoint ranges and smaller-scale terms remain available for the next calculation; in particular, the \(-4l^2\log2\) term contributes at order \(q\) in the simple-multiplicity regime. The leading equilibrium limit is not a license to discard these terms.

## Signed arithmetic return and its remaining baseline

WGR carries the result through the exact original maps and deficits:

\[
 \Delta_k^\Gamma
 =-W_k+e_0-e_q-e_{q+1}+\delta_k^\sigma,
 \qquad
 \frac{\Delta_k^\Gamma}{kq}\longrightarrow
 -\frac{\mathcal C_\Gamma}{4}.
\]

Here \(e_0\) is the low scalar comparison error, \(e_q,e_{q+1}\) are the two high relation errors, and \(\delta_k^\sigma\) is the original arithmetic correction. Its asymmetric allowances are retained. The simple-multiplicity \(5/7\) estimate and the different fixed-\(m\ge2\) constants are used in their separate regimes; they vanish after division by \(kq\).

WGR10–11 contain the complete finite arithmetic and HC intervals. WGR15 and the current receiving application retain the baseline/arithmetic and residual/baseline difference limits, including the necessary condition

\[
 \liminf\frac{B_k^0}{kq}\ge\frac{\mathcal C_\Gamma}{4}.
\]

This does not evaluate the original baseline. The remaining calculation must use \(B_k^0\) at its actual four degrees and the unchanged nonnegative residual

\[
 R_k=B_k^{\rm ar}-4q\log(D_hk),
\]

with its original source and constant \(D_h\). The negative leading Gamma contribution alone is not an endpoint conclusion for that residual.

The other remaining task is a finite \(q\)-scale correction for the Gamma Hankel ratios or positive recurrence around the explicit equilibrium. It must retain \(n=q/2\), shifts \(a=q,\ldots,q+l\), the size-\(n+1\) occurrence, both odd blocks, the low moment, and every surviving product term. The required remainder needs its own proof; differentiating an uncontrolled free-energy error does not supply it.

## Complete proofs and receiving sources

The [editable main file](Gamma_Growth_and_Arithmetic_Return.tex) assembles the preceding full calculation and these five complete new bodies:

| Proof | Reading role |
| --- | --- |
| [WGP1–14](sources/growth/WGP.tex) | Literal four-product expansion and finite signed remainder. |
| [RWB1–27](sources/growth/RWB.tex) | Original-source recurrence estimates and finite positive \(W_k\) bounds. |
| [EIQ1–33](sources/growth/EIQ.tex) | Explicit positive-axis equilibrium, global minimizer, and exterior inequality. |
| [GEL1–19](sources/growth/GEL.tex) | Original Gamma determinant integral and proved leading limit, including the supplementary numbered statements. |
| [WGR1–15](sources/growth/WGR.tex) | Exact signed growth transfer into arithmetic, baseline, and HC relations. |

The complete [author originals](originals/growth/), [prepared sources](sources/), [earlier dependencies](dependencies/), and [theorem crosswalk](THEOREM_CROSSWALK.md) accompany the paper. The crosswalk and this guide locate the mathematics; neither replaces its definitions or proofs.

The [current receiving guide](current_receiving/README.md) identifies the full [NOTE successor](current_receiving/CURRENT_JOINT_SCHUR_NOTE.tex) and [JSR successor](current_receiving/SIGNED_RETURN_RECEIVER.tex). The complete [GRI1–7 application](current_receiving/spans/GROWTH_RECEIVING_BODY.tex) is embedded once in each successor. It installs the finite evaluated interval, equilibrium coefficient, signed limit, and necessary baseline/residual relations. The five full proof providers and earlier maps remain in [providers](current_receiving/providers/).

The [receiving receipt](current_receiving/FULL_RECEIVING_RECEIPT.json) records 19 precise reversible updates, whole-file lineage, provider pins, and preservation of the entire [67-file cut-20 receiving predecessor](current_receiving/predecessors/cut20/). Its recorded integration checks are inherited evidence, not a new whole-source review performed for this guide. The evaluated interval contains the earlier exact-\(W\) interval, so the existing four-entry exact-input intersection is unchanged; no pointwise finite tightening is claimed.

## Acceptance and edition scope

The [completed acceptance record](BUILD_AND_PROOF_ACCEPTANCE.json) records full mathematical reading of all five new proofs, accepted independent complete reviews with final repairs checked, and visual acceptance of all 37 actual pages. The [delivery receipt](provenance/owner_delivery/DELIVERY_RECEIPT.json) identifies the accepted artifact. These are owner-recorded results, not fresh proof, archive, PDF, build, or Lean checks for this public guide. No Lean result is claimed by the cut.

The [current source pins](CURRENT_SOURCE_PINS.json) bind the unchanged PDF, complete proof bodies, and current receivers. The [public derivation ledger](PUBLIC_DERIVATION.json) maps every named owner source to its public copy or documented private-text exclusion. [Historical locator notes](source-records/README.md) explain receipt aliases and retained original hashes.

Earlier sealed readers retain their historical source cuts and PDF bytes. This is the separate Gamma-growth successor, with complete current receiving sources and the remaining baseline and finer-remainder work stated explicitly.
