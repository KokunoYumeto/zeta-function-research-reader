# Final independent review of the combined restriction

Reviewed `output/tau_split_zero_counterfactual_reconstruction_20260913/tex/combined_restriction.tex` in full, together with the full HC module, the relevant actual-source definitions in AT, and an independent source-bounded review of CR2/CR5/CR6 against AT and AW. The four prior corrections in `tex/reconstruction.tex` were also checked. No source file was edited.

## Verdict

The mathematical inequalities CR1–CR6 are correct on the stated actual counterfactual quartet and original common source. The full cyclic length `q=[1+k(m−1)](k+1)^2`, every relative eigenvalue and its index, the sign of the commutator trace, and the orientation of the four determinant factors are retained. The final section correctly refrains from asserting a verified nonempty instance of the refined interval.

Two text corrections were sent to the root:

1. Replace “the source isometry does not commute with the arithmetic observation” by “the source isometry does not preserve the arithmetic observation.” The two operators do not have composable domains in both orders. The strict nonpreservation has an exact witness below.
2. Near R.8 in the introductory reconstruction, qualify “the resulting proved bounds are compatible” as a statement about the **coarse scalar upper and lower bound functions**. The refined common-source interval CR3 retains actual unevaluated relative eigenvalues and envelope determinants. Its nonemptiness at an off-line packet has not been verified. The combined chapter itself already states this distinction correctly.

## 1. The bounds are on the same arithmetic object

AT2–AT6 define the polynomial source `P_N=C[S]_(<=N)`, its literal remainder map modulo the original full cyclic sum polynomial, the same quotient `E=C[S]/(chi)`, and canonical quotient Grams for the two specified measures. The arithmetic density is exactly `w_h^(convolution k)`, with `w_h(u)=|(g/h)(1/2+iu)|²/(2pi)`. The Gamma reference retains its mass `(2pi)^(k/2)` and all displayed factors. Interpolating these two densities changes neither the remainder map nor the arithmetic observation into `Q^(tensor k)`.

Both densities are positive almost everywhere and have every finite moment. Their moment matrices are positive definite, and the remainder map is onto for `N>=q−1`. Thus every quotient determinant used by CR1 is positive. Increasing the polynomial degree enlarges each affine remainder fibre; minimization therefore decreases the quotient Gram. The two volume ratios in CR1's arithmetic product are at least one, proving `B_ar>=0` exactly. No normalization of a source mass or replacement of a coefficient frame is involved.

## 2. HC supplies precisely the three scalar/envelope entries used in CR3

HC5 proves the exact identity

`B_ar=4q log(D_h k)+R_k`, `R_k>=0`,

with `D_h` fixed by HC3 from the actual packet. The full residual includes the contraction penalties, phase terms, norm saving, comparable-window saving, and full-multiplicity boundary saving; none is omitted in CR's invocation of the lower bound.

HC8 proves `B_ar<=Uhat_k` by applying the actual remainder map at the two needed degrees `2q−1` and `2q`, including the additional last-degree estimate. HC15 proves `B_ar<=U_(nu,k)` by pointwise domination of the original lower-envelope measure and minimizing over the identical affine remainder fibres. The latter upper expression includes its actual two low-degree arithmetic determinants, not freely chosen constants.

Consequently the lower entries `0` and `4q log(D_h k)` and the upper entries `Uhat_k` and `U_(nu,k)` all constrain the same `B_ar`. Taking their maximum/minimum introduces no independent choice of data.

## 3. The relative spectrum and CR2 indices are exact

All spectral comparisons take place in `H=P_(2q)`, of dimension `2q+1`. The relative operator `D_*=M_(2q)(0)^−1 M_(2q)(1)` is positive and self-adjoint in the `M_(2q)(0)` metric; equivalently it is similar to the ordinary positive Hermitian matrix obtained by conjugating with `M_(2q)(0)^(1/2)`. It is not being asserted to be Euclidean-Hermitian without that transport.

The full window spectrum in AW is `0` with multiplicity `q`, `1` with multiplicity two, and `2` with multiplicity `q−1`. Pairing its increasing/decreasing rearrangements with the ordered actual interpolation eigenvalues gives the exact upper-minus-lower expression

`c_(q+2)(t)−c_q(t)+2 sum_(j=1)^(q−1)(c_(2q+2−j)(t)−c_j(t))`.

Here `c_j(t)=(b_j−1)/(1−t+t b_j)`, and direct integration from zero to one gives `log b_j`. Thus the stated

`L_q=log(b_(q+2)/b_q)+2 sum_(j=1)^(q−1)log(b_(2q+2−j)/b_j)`

has exactly the correct indices and multiplicities. Every ratio is at least one because the b's are sorted positive eigenvalues. AW14 therefore supplies `|Delta|<=L_q` on the actual common source. These b's are not a separately chosen diagonal arithmetic model.

## 4. CR3, CR4 and CR6 follow with their stated orientations

From `Delta=B_ar−B_Gamma` and `|Delta|<=L_q` one obtains `B_Gamma−L_q<=B_ar<=B_Gamma+L_q`. Combining with HC's bounds gives exactly CR3. Subtracting the same `B_Gamma` from every entry gives CR4; its lower entry `−B_Gamma` is required because `B_ar>=0` does not imply `Delta>=0`.

For CR6, combine `B_Gamma−L_q<=B_ar` with each of the two arithmetic upper bounds. This gives `L_q>=B_Gamma−Uhat_k` and `L_q>=B_Gamma−U_(nu,k)`. Combine `max(0,4q log(D_h k))<=B_ar` with `B_ar<=B_Gamma+L_q` to get the remaining lower bound on L_q. Adding `L_q>=0` produces the stated maximum. No reverse inequality or positivity of Delta is inferred.

## 5. CR5 preserves the full common source and the correct commutator sign

The original operators `U(t),W(t),C(t),T(t)` act on the same `H=P_(2q)`. AW constructs `T` with `T* M(t) T=M(t)` and `U=T W T^−1`. In the ordinary finite trace,

`Tr((U−W)C)=Tr(TWT^−1 C−WC)=Tr(WT^−1 CT−WC)=Tr(WT^−1[C,T])`.

The sign is therefore `[C,T]=CT−TC`, as printed. AT15 is the four-window logarithmic variation from reference parameter zero to arithmetic parameter one, so integration in CR5 has the correct orientation and equals `B_ar−B_Gamma`. The identity does not change a source metric, quotient class, or local arithmetic factor by declaration.

The observation map has type `O:H->Q^(tensor k)`. Thus `OT` is defined, but `TO` is not. The wording must be nonpreservation, not noncommutation. AW12 gives `ker O=F2=chi P_q` and `ker(OT)=P_(q−1)^perp` in the actual M(t) inner product.

Strict nonpreservation can be proved on these exact spaces. Write `chi(S)=sum_(j=0)^q a_j S^j` and define

`chi_dagger(S)=sum_(j=0)^q conjugate(a_j)(k−S)^j`, `v=chi chi_dagger`.

Then v is in `P_(2q)` and in `F2`, so `O(v)=0`. On the retained line `S=k/2+iu`, `chi_dagger(S)=conjugate(chi(S))`. Therefore

`<1,v>_t=integral |chi(k/2+iu)|² m_t(u) du>0`.

The integral is finite by the full moments and strictly positive because the density is positive almost everywhere and chi is nonzero. Since `1` belongs to `P_(q−1)`, v is not orthogonal to that space, so `OT(v)!=0`. This proves the isometry changes the arithmetic observation, rather than merely noting that its computed defect might change it.

## 6. The compatibility scope is correct in the combined chapter

HC9–HC11 prove positive separation only for the coarse scalar upper/lower functions. With fixed packet constants, `q>2k`, all indicated lower-order upper-bound terms are nonnegative, and `D_h<1`. Hence `Uhat_k>max(0,4q log(D_h k))`. Dividing the separation by q² gives the stated limit `2((pi/2)D+log 256)>0`.

That calculation neither produces actual moments of an off-line quartet nor verifies the refined max/min comparison numerically at one. CR3 has additional unevaluated actual quantities, so an assertion that the coarse functions leave room does not certify the nonemptiness of the refined interval for a hypothetical or actual instance. The combined chapter explicitly says this. The introductory reconstruction should use equally specific wording near R.8.

## 7. Previous reconstruction fixes verified

- The restriction after R.3 is now explicitly `A_tau(T)->T_sigma[0]=0`, with the homotopy fibre correctly identified.
- The R.5 scope now says nonzero polynomial, excluding the invalid zero-polynomial finite-jet reading. Nonzero constants give a trivial exact sequence.
- R.7 now declares its retained finite coefficient space, sum operator, representative map, original L² measure, differential, Gram, and boundary map; the shared notation for boundary and Schwartz space is explicitly disambiguated.
- R.8 now gives `k>=2`, the exact cyclic length q, positive determinant volumes, and the two original window definitions. The stronger HC/CR estimates correctly start at `k>=3`.

## Final reread after the root corrections

Both requested text corrections have now been made and verified. The combined chapter says the isometry does not preserve the observation and includes the full explicit witness as CR7. I read that new section: its polynomial, unchanged sum line, strict positive integral, kernel comparison, and supported-zero interpretation agree with the proof above. The conclusion is correctly limited to this particular source isometry not descending through the original relation quotient.

The introduction near R.8 now explicitly limits numerical compatibility to the coarse scalar bound functions and says the refined common-source interval retains unevaluated quantities. This resolves the possible overstatement. No mathematical correction remains requested. The original objects, counterfactual status, and full arithmetic conditions remain intact.
