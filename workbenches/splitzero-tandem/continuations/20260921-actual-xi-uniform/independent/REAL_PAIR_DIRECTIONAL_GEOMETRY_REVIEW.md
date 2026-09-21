# Directional geometry: mathematical derivation and verification

The complete proof is `REAL_PAIR_DIRECTIONAL_GEOMETRY.tex`, RPD1–30 and RPD12a. It extends the actual certified root in RPZ1–19; it does not introduce new freely assigned moments or replace that root by its decimal approximation.

The exact real derivative map is

\[
\Lambda(v_z,v_x)=G_zv_z+G_xv_x.
\]

The certified invertibility of the real derivative of the vanishing factor, together with the nonzero second factor, proves that this map is an isomorphism. RPD4 gives its inverse with both signs. Its determinant is negative. RPD5 retains the complete positive definite zeroth-moment quadratic form. RPD6–7 construct the actual nearby real spectral zero curve by contraction and give both of its original-coordinate derivatives.

RPD8–19 retain every original moment, center correction and Gamma weight. They give the full straight-direction inverse spectrum at every cutoff. RPD12a also prints the actual order-two quotient map with its unchanged source quotient norm; that invertible map has a different domain from the fixed old matrix whose poles are calculated.

RPD20–22 construct every resonance vector in the original coordinates. For cutoff D there are 2D oriented positive rays and D unoriented lines. The antipodal relation is explicit, including the odd-cutoff central root. At a direction with image argument mπ/q in lowest terms, resonance occurs exactly at D=jq−1. Two cutoffs D,E share exactly gcd(D+1,E+1)−1 lines. Every magnitude remains in the arbitrary positive parameter r and in the scaling laws.

RPD23 proves the curvature correction

\[
K_D^{\mathrm{path}}=K_D(v)+\tfrac12DH_D(v)[a].
\]

RPD24–27 prove the full uniform matrix transition near a resonance line. They first retain the exact quantity H_D(v+εw)/τ in the leading corner. Only afterwards do they take limits. This order is necessary: the nonresonant inverse law is not uniform as a direction enters a resonance line. The transverse derivative is proved nonzero for every cutoff, using the exact original-coordinate vector Λ⁻¹(iΛ(v)). When ε/τ tends to a finite limit, the leading corner remains invertible even if its upper-right coefficient vanishes. When |ε|/τ tends to infinity, the single growing corner entry and the exact second exterior determinant give both singular asymptotics. The fractional-power paths are explicitly restricted to τ>0 and are not all claimed to be twice differentiable.

RPD28 specializes the full result to the original degree-three calculation. RPD29–30 prove the exact passage to the original u coordinate. A straight mixed (u,x) path introduces the acceleration (2z_*³ν_u²,0); it cannot in general be handled by multiplying a fixed-x period constant. The unit-speed fixed-x factor is |u_*|^(2p), with the additional |ν_u|^(−p) at arbitrary period speed.

The accompanying checker passes 73 exact groups containing 74 scalar identities, and 400 exact rational-angle overlap comparisons. It verifies the matrix inverse signs, quadratic determinant, original arctangent/exponential center corrections, all finite coefficient identities through degree eight, signed scaling of H and K, the curvature identity, the exact degree-three derivative and next coefficient, and weighted resonant determinants. These finite checks support the induction and analytic proofs; they are not a substitute for the all-cutoff argument.

The interval calculation propagates the saved full-series certificate's original factor derivatives. It checks the certificate's script hash and all certified inequalities before use. It proves a negative real Jacobian determinant, a positive definite quadratic form, and six distinct degree-three oriented rays, and encloses their full K3 and transverse derivative. It uses 256-bit outward arithmetic and one worker. It does not rerun the original series or claim that it has done so. The independent root calculation's separate recovery of the Jacobian from P⁻¹(I−E) gives a second propagation route.

One initial checker failure came from asking SymPy for a polynomial coefficient before expanding its factored expression. Expanding the expression fixed that checker error; none of the corresponding mathematical formulas changed. During review, the Cassini identity's range was made explicit as n≥1, while the Chebyshev identity holds for n≥0. Four equation tags were moved outside their gathered environments. The final receipt is bound to the final proof and checker hashes.

The proof uses the same bounded corpus route recorded in `REAL_PAIR_TOPIC_ROUTE.json`; no new external theorem or literature result was imported. PCL1–10, WCF1–6, RPZ1–19, RPCJ1–23 and RPAC1–15 supply the exact programme objects and prior proofs. PCL and WCF have exact pinned links in the source. The numerical arithmetic provenance is Fredrik Johansson's Arb, arXiv:1611.02831v1, inherited through the fully specified RPZ certificate. This derivation does not claim a fresh reading of that paper or of DLMF. The source-use receipt records actual reading coverage.

These are exact results on the original geometric coefficient family. They do not identify the arithmetic zeta quartet or its restricted period/unit locus.
