# Concrete next-cut correction proposal for PR #24

This proposal targets only the two files named in `PROPOSED_CORRECTION.patch`, based on PR head `dfcbba5cbf7fec8c9301fe242c13e741d762013e`. It has not been applied remotely or to the current publication.

## Source prerequisite and the actual map

Retain the original packet, centre c=k/2, complete root orders, arithmetic measure, and k>=1. State the exact source prerequisite

    conjugate(chi)(k-S)=(-1)^q chi(S).

Here conjugation applies to polynomial coefficients. This holds for the complete reflection-stable quartet packets used by the intended target. It does not follow merely from choosing an arbitrary finite packet of zeros.

The actual coordinate map is `Psi(P)(u)=P(c+iu)`. The stated prerequisite gives real monic `psi=i^(-q)Psi(chi)` and `Pi=psi^2`. It therefore induces the quotient isomorphism

    C[S]/chi^2 -> C[u]/Pi,
    [P] -> [P(c+iu)],

because `Psi(chi^2)=i^(2q)Pi`. At each original root lambda_a, with shifted root zeta_a=(lambda_a-c)/i, its raw full-jet map is

    (d_u^d Psi(P))(zeta_a)=i^d P^(d)(lambda_a),
    0<=d<2 ell_a.

These are the coordinates used by F_a and its factorial Vandermonde; no derivative division, root order, phase unit, or actual conormal map is changed. Without the prerequisite, the doubled-original-root presentation is not asserted.

## Positive asymmetric phase fixture

Keep the nodes t_j=j-9, j=0,...,18, but use

    w_j=(10+t_j)*(2+(j*j+3*j) mod 7).

Every weight is positive because 1<=10+t_j<=19. The multiplier breaks the original fixture's reflection symmetry. The proposed public test checks all of the following on the same directly calculated quotient Gram:

- the extra transfer solve equals the full logarithmic volume derivative;
- `phi=sigma-d_theta log V_N` is explicitly nonzero;
- the two norm gaps, with `-phi^2` retained, equal the computed control radius squared;
- the separate volume-imbalance square and phase square give that same radius squared.

At q=2, n=2, N=3, the exact phase is

    -74546106783325497234077749 / 44411209934630298438578438.

The test therefore fails if the phase is silently zeroed or removed. It is an exact atomic calibration, not a representation of a zeta packet or a numerical enclosure of arithmetic moments.

## Verification and unchanged scope

The proposed checker passes all eight methods normally and under `python -O`. Both success records are identical; both deliberate-failure controls exit 1. The original public checker also passed its separate fresh replay, and its downloaded bytes remain unchanged. `PROPOSED_CORRECTION_RECEIPT.json` records source and proposed SHA-256 hashes.

No new general-packet construction, Lean theorem, asymptotic bound, or assertion about zero locations is included. The original canonical source/relation calculation and the exact endpoint/Gamma interface remain those reviewed in `REVIEW.md`.
