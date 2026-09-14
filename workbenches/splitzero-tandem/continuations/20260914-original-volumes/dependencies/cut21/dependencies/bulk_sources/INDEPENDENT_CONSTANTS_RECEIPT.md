# Exterior polynomial constants: independent calculation

Full proof: independent_constants.tex, equations IBC1–IBC33.

The original degree is retained as
q = (1 + k(m−1))(k+1)^2, with k = 4l+1. The proof retains the
translated argument c+iy, every root, and every multiplicity.

The proposed coefficient
p2 = q k(k+2)(delta^2−gamma^2)/3
and the proposed finite remainder
q tau^2/[2(1−tau)]
are correct on the stated exterior domain tau < 1.

The proof also supplies the exact fourth- and sixth-order signed
coefficients, finite rootwise logarithmic remainder bounds, exact fourth
and sixth absolute moments, and the resulting sharper enclosures.
The Gamma offset second and fourth power sums are proved in both l
and k. An additional integral calculation gives one-sided Gamma
remainder bounds for every real nonzero y.

An independent algebra agent derived the fourth-order coefficient and
both offset sums, with agreement. Symbolic checks confirm seven
polynomial identities. Supplementary 90-digit checks cover 24 exterior
cases, including equal squared offsets, a zero offset, negative y,
different signs, and multiplicities from m=1,2.
The proof does not rely on these checks.

The independent agent then read all 328 source lines and accepted the
coefficients and finite estimates. Its one domain wording correction was
applied: the definition of the logarithm explicitly excludes zero
evaluations. The exterior inequality guarantees this exclusion throughout
the exterior theorem.

The source SHA256 and machine-check details are recorded in
INDEPENDENT_CONSTANTS_CHECK.json.
No sealed input, build, global reader, or publication was modified.

## Delegated task provenance

The parent supplied this bounded task verbatim:

> Independent bounded calculation alongside my source/Gram work. For original χ(c+x)=Π_{a,b=0}^k[x−(2a−k)δ−i(2b−k)γ]^e, k=4l+1,e=1+k(m−1),q=e(k+1)², d=δ²,g=γ²: prove exact exterior log(|χ(c+iy)|²/|y|^(2q))=p2/y²+E, p2=q k(k+2)(d−g)/3 and claimed |E|≤q τ²/[2(1−τ)],τ=k²(d+g)/y²<1. Check signs, all powers/multiplicities; derive exact p4 and strongest useful finite improved remainder if immediate. Also compute Σ_{j<l}(2j+1/2)², fourth powers for f. Write full proof NEW root/joint_schur_intake/next_bulk_density/independent_constants.tex and brief receipt. No current sealed inputs/build/publication edits.

The chosen proof uses the convergent logarithm on the exterior disk,
the exact central reflection of the finite root grid, and direct finite
moment identities. Each remainder comparison is written and proved.
