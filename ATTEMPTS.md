# Zeta research: what we tried and why

Reconstruct published results about the Riemann zeta function and connect them, by explicit formulas rather than metaphor, to three named inputs: the CUE (circular unitary ensemble) characteristic-polynomial literature; the cubic polynomial map F:C^3→C^3 discussed by Tao, Speyer and Poplett; and the corrected finite-time Navier–Stokes reconstruction published as a companion reader. The broader motivation was to determine exactly what arithmetic information these interfaces carry and whether any route reaches a criterion relevant to the Riemann hypothesis (RH).

## What the named objects are

The central analytic object is the Riemann zeta function ζ(s), together with its completed critical-line function Xi(t)=ξ(1/2+it). The adjacent random-matrix input is the CUE characteristic polynomial—CUE means the circular unitary ensemble, the Haar-random unitary-matrix model—and its derivative moments, specifically A. Grover, F. Mezzadri and N. Simm, *Higher order derivative moments of CUE characteristic polynomials and the Riemann zeta function*, arXiv:2604.03051v1; the user also identified the Easy Riders channel as a public source for that programme.

The geometric input is the explicit cubic map F:C³→C³ written in the reader: F1=(1+xy)³w+y²(1+xy)(4+3xy), F2=y+3x(1+xy)²w+3xy²(4+3xy), and F3=2x−3x²y−x³w. The reader cites Terry Tao’s 21 July 2026 exposition, David Speyer’s 20 July 2026 exposition, and J. Poplett’s *Local Fidelity, Global Alias* research note for this map.

The fluid input is the corrected 208-page *Finite Time Blowup for Navier–Stokes* reconstruction: a velocity field uν(x,t), pressure pν, positive viscosity ν>0, zero initial velocity, smooth compactly supported forcing, and the nonlinear transport terms retained. Its public companion edition is [Zenodo 10.5281/zenodo.22678406](https://doi.org/10.5281/zenodo.22678406); the reader preserves the source attribution and states that independent analytical/Lean validation is unfinished.

These routes are interfaces between named objects, not claims that ζ, a CUE polynomial, F, and uν are identical. Each entry below names the actual map or transform used and says what was and was not obtained. “Typed” here means that the map’s domain, codomain and formula are stated.

These five short accounts describe the selected routes in the [frozen 411-page reader](https://zenodo.org/records/22678086/files/01-main-reader.pdf), not the whole project. Route rationales are reconstructed from the written arguments; they are not quotations of the original motivation. The full calculations and human-source references remain in the reader.

## Keep the branches, then transport the equations

We aimed to test whether the explicit Tao–Speyer–Poplett cubic map can be carried into fluid and arithmetic coordinates without losing inverse branches. An inverse fibre is the set of input points with one fixed output under F, so its geometry gives a concrete place to calculate exactly what a projection forgets. We started from the displayed F1,F2,F3 formulas and constructed the cubic inverse chart, rank-degenerate exceptional fibres, incompressible trajectories and diffusion operators after changing coordinates. This gave exact maps and an escaping trajectory in the retained pullback metric. That metric is incomplete; this route did not itself produce a classical Euclidean Navier–Stokes singularity or an off-critical zeta zero. The later work therefore also uses the actual released fluid field.

## Test the negative coefficient in the complete Weil form

We aimed to determine whether the coefficient-level negative signal survives in a quadratic Weil-form test relevant to RH. The Weil form here is the explicit quadratic functional used in a Weil-type positivity criterion. The retained coefficient acts on the actual theta input (a Gaussian-weighted theta series) whose Fourier transform is Xi. We evaluated the complete Weil form, retaining pole, gamma and prime-power terms, cross terms and infinite-tail bounds. The recorded certified value is positive, approximately 2.0984855607004 × 10⁻¹¹. This particular input is not a negative Weil witness. The calculation neither proves global Weil positivity nor settles RH; the negative linear coefficient remains a different, explicitly related calculation.

## Transport the actual concentrating swirl into arithmetic

We aimed to propagate the corrected Navier–Stokes reconstruction's actual velocity and angular momentum into zeta Mellin coordinates (integral coordinates indexed by the complex exponent s), rather than infer its behaviour from an analogy. The published construction has an explicitly defined concentrating component, while angular momentum admits explicit dilation and Mellin maps involving ζ(s). We kept the named field uν, pressure, force, positive viscosity, both nonlinear fluxes and the projection remainder; constructed the arithmetic map and inverse, then examined the fixed-axis derivative. The written calculation obtains a directly growing arithmetic derivative and an equal genuine Mellin residue at s = −1. This is a precise transported signal, not an off-critical zeta zero. Independent verification of the imported complete source existence theorem is unfinished.

## Recover data hidden by trivial-zero cancellation

We aimed to find where higher radial information goes when a zeta factor cancels its Mellin pole. The cancellation occurs at the zeta factor's trivial zeros (the negative even integers). A cancelled pole need not mean that the input coefficient has disappeared. We expanded the full Mellin product at negative integers and retained the local zeta factors. Odd Taylor coefficients are recovered from residues; even coefficients from regular values divided by the nonzero derivative of the multiplier. This recovers the complete Taylor sequence, not an arbitrary smooth germ from that sequence alone. Flat remainders (nonzero functions invisible to every Taylor coefficient at the expansion point) remain in the full invertible transform; no new nontrivial zeta zero is obtained.

## Make the higher radial source data constructive

We aimed to extend the axis calculation beyond its first derivative without replacing the complete corrected field. The preceding second-coefficient cancellation suggested finite source dependence at each fixed radial degree. We derived the coupled coefficient recursion (a recurrence determining the next radial coefficient from earlier ones) with pressure, viscosity and cutoff terms, then carried it into residue/value coordinates. The written induction gives vanishing above correction order n > m and a finite algorithm for every fixed Taylor degree. This is not convergence of the uncut series or an autonomous finite-dimensional fluid system. The full functions, nonlinear fluxes and flat remainders remain necessary.

## Full work and source locations

[Read the main manuscript](https://zenodo.org/records/22678086/files/01-main-reader.pdf) · [Exact complete source archive](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/490a7ac7ef693702e9d92ba1e933a440d8f55b9b/zenodo_collection_20260909_main411/07-complete-mathematical-sources.zip) · [Machine-readable accounts and per-section hashes](ATTEMPTS.json)

The machine records identify the exact archive members and section/equation labels. This pass adds research history and navigation, not a new proof review or a prescribed next-calculation queue. Later results may extend these frozen accounts.
