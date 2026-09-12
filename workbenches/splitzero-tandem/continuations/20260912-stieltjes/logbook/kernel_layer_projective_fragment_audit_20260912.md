# Full-fragment independent audit — projective shell comparison

Target: `output/split_zero_rh_tandem_2026-09-12/tex/kernel_layer_projective_comparison.tex`.
Auditor: the independent antidual/projective audit lane.

The full initial fragment was read from disk, from its section declaration
through the final Split-Zero lift paragraph. After the author's corrections
and additions, the entire final fragment was read again. Final-state review
is recorded below. No main TeX was edited by this auditor.

## Initial findings sent to the author

1. Two literal TeX command defects: KPC.19 had `,quad y=`, and KPC.23
   had two occurrences of `qquad` without a backslash.
2. The sentence after KPC.13 comparing coefficients with KPC.6 needs
   the qualifier `|gamma|<N`. KPC.6 lists only lower-degree terms;
   the degree-N coefficients remain the original `c_gamma`.
3. Specify the domain and codomain of the final support lift as the
   fixed-support globalizations, or a chosen constant support diagram.
   For arbitrary varying-fibre diagrams, linearity alone does not assert
   compatibility with transition maps. The displayed fixed-fibre lift
   itself is correct.

No other mathematical error was found in the initial fragment.

## Complete claims checked

- KPC.1–4: the full-jet map retains the unit and all product coordinates;
  it is used as a linear map, with its multiplication factor specified.
- KPC.5–7: the exact coefficient formula includes every lower-degree
  term; top-degree componentwise inequalities force equality of the
  two multi-indices, proving both section identities. The orthogonal
  complement statement follows from product integration and its exact
  dimension. N=0 is included with an empty lower sum.
- KPC.8–9: both maps induce the same surjection onto the explicitly
  defined associated-graded target. The intermediate kernel quotient
  is identified with the actual shell image intersected with the lower
  filtration. The saturation threshold N-1 >= k(d-1) follows from all
  retained remainder monomials and the invertible unit.
- KPC.10–12 and following paragraph: both quotient maps are well-defined
  and surjective; their kernels, paired-image quotient and full fibre
  product are exact. The universal property is explicitly linear. The
  criterion for a comparison map is kernel inclusion, and its being an
  isomorphism is equivalent to kernel equality. The independent complete
  proof is also in `work/kernel_layer_projective_independent_audit_20260912.md`.
- KPC.13: the deformation is polynomial at the parameter zero, including
  each monic leading term. Its lower coefficients have the displayed
  power of the parameter, and the associated-graded map stays fixed.
  The rank condition is exactly the determinantal condition. This
  verifies the corrected lower-coefficient qualification in finding 2.
- KPC.14–22: all inverses are typed inside the original quotient algebra.
  CRT retains ordered pairs and every local monomial. The geometric
  inverse of sigma+y, the exact ratio difference, and the preceding
  nonzero power have the displayed constants and signs. The global
  annihilator uses maximum exponents at coincident ratios, and the rank
  counts follow from the restricted polynomial kernel. The unit and
  second-coordinate power remain explicit linear isomorphisms onto
  their images; the text does not promote them to unital algebra maps.
- The initial local m=n=2 obstruction is correct. Its two nilpotent
  images have no linear coefficient in C[t]/t^3, so the exact ratio
  difference cannot map to t. The extension to all multiplicities is
  audited separately in the final-state record.
- KPC.23–28: every value, norm, jet, layer matrix and metric was checked
  directly as detailed next. The diagnostic is expressly a finite
  polynomial model and does not assert that 1/2 is an arithmetic zero.

## Direct check of the entire finite model

With masses exactly one at `1/2-i,1/2,1/2+i`, the three monic value
columns are `(1,1,1)`, `(-i,0,i)`, and `(-1/3,2/3,-1/3)`. Their
Hermitian Gram is diagonal `(3,2,2/3)`. Product polynomials of total
degree at most two are independent on the 3-by-3 grid: they belong to
the full tensor product of the two degree-at-most-two univariate
spaces, whose evaluation matrices are invertible. Thus the positive
form required at both finite stages is valid.

The old degree-at-most-one basis has norms `(9,6,6)` and jets `(1,0,0)`.
Consequently `K1=1/9`, `G1=9`, and the minimum is `R1 u=u`.
The original packet sum acts by `A=1`. Its boundary is
`(s1+s2-1)u`, in the span of `s1-1/2,s2-1/2`, proving `C1=0`
and `W1=0` directly.

For the next shell `(2,0),(1,1),(0,2)`, the norms are `(2,4,2)` and
jets `(2/3,0,2/3)`. Subtracting the minimum of each jet gives the
actual layer vectors

\[
e_{20}=(s_1-1/2)^2,\quad e_{11}=(s_1-1/2)(s_2-1/2),\quad
e_{02}=(s_2-1/2)^2.
\]

Their Gram is exactly

\[
H=\begin{pmatrix}6&0&4\\0&4&0\\4&0&6\end{pmatrix}
=\operatorname{diag}(2,4,2)+U^*9U,
\quad U=(2/3,0,2/3).
\]

Its three eigenvalues are `10,4,2`. The kernel update is
`K2=1/9+2/9+2/9=5/9`, giving `G2=9/5`.

There is also a direct minimum witness, independent of inversion of
the updated kernel. Solving the displayed 2-by-2 outer block gives

\[
H^{-1}U^*G_1=(3/5,0,3/5)^T,\quad
Y_1=-\tfrac35(e_{20}+e_{02}),
\]
\[
R_2u=\left[1+\tfrac35\{(s_1-1/2)^2+(s_2-1/2)^2\}\right]u.
\]

Its values are `-1/5` at the four grid points with both centred
coordinates nonzero, `2/5` at the four with exactly one nonzero, and
`1` at the central point. Therefore

\[
\|R_2(1)\|^2=4/25+16/25+1=9/5.
\]

The full jet remains one. The Gram loss is exactly `9-9/5=36/5`, and
`||Y1||^2=(9/25)(6+8+6)=36/5`, agreeing with the original layer
Pythagorean identity. A nonzero metric loss together with a zero
derivative layer is therefore verified without an inferred rank rule.

## Final-state record

Final source SHA-256:
`D5265F886180DB33933BE8DEB5D286A53C7AE4DFDB440F97DF4ED6B6CFB677E8`.

The entire final source was independently reread from disk after the
author's additions. All three initial findings are resolved: the TeX
spacing commands have their backslashes; the deformation coefficient
statement explicitly treats lower degrees and separately retains the
leading coefficient; the final support lift specifies its two carriers,
addition and scalar action, including the external and supported zeros.

The new generator identity KPC.22a follows in the original algebra from
`s1+s2=s2(1+zeta)`; its domain-quotient compatibility follows by multiplying
a multiple of the complete minimal polynomial by `1+Z`. Its example with
two distinct diagonal centre pairs correctly proves the stated failure of
invariance of the ratio subalgebra while the adjacent-shell map remains
explicit.

The complete local/global algebra-retraction proof was checked. When one
local multiplicity is one, the displayed finite inverse or linear formula
recovers the other coordinate inside the ratio algebra. When both exceed
one, each nilpotent coordinate image must have zero linear coefficient in
the target of length `m+n-1`, preventing a retraction. Globally, the
squarefree selection of one ordered pair for each ratio defines a unital
algebra retraction. In the repeated case, KPC.22b has exact length
`2M-1`; the target's proved idempotent property forces selection of one
local factor, its constant ratio forces equal centres, and its multiplicity
`m<=M<2M-1` forces the same vanishing of linear coefficients. This is a
complete obstruction and retains the original ratio embedding.

The added direct minimum proof KPC.28a is correct. Its three classes of
grid values have the displayed counts and squared norm. The odd-coordinate
pairings vanish, and each remaining square-coordinate pairing is the
stated zero three-value sum. The five independent zero-jet vectors exhaust
the degree-at-most-two kernel, so Pythagoras establishes the unique minimum
at the exact norm `9/5`.

Final audit status: **no outstanding mathematical corrections** in the
entire fragment at the stated SHA-256. This is a mathematical source audit;
the author owns the separate compilation and rendering checks. No execution
of Lean or claim of a new analytic certificate is made by this report.
