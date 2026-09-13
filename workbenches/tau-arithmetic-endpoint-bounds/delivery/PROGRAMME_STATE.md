# Portable programme state

Keep the original tau-base; G(Z)->Z remains the infinite arithmetic quotient.
Keep e=0^bullet and external tau distinct before applying the arithmetic map.
The source is still the original theta complex, g=2xi, the same finite packet h,
the same Taylor unit, the same cyclic sum action S=sum s_i, and the same
canonical least-norm representatives modulo the original theta relations.

## New established input

Written analytic theorem: for fixed h and all n>=k>=3,

    (omega_(h,k,2n)/omega_(h,k,n))^(1/(2n)) <= C_h n.

The proof is independent of RH: local critical-line mass from an annulus
maximum-principle argument; lower bound after three actual convolutions;
Legendre monic lower bound; exponential-moment upper bound. The constants retain
an actual compact mass and compact convolution minimum. They are not numerically
certified in this package.

## Use with the other session's endpoint criterion

On the exact-quartet window q_k,...,2q_k-1, the source norm factor is now O_h(q_k).
The remaining term is exactly

    B_k=log[V_(q_k-1)V_(q_k)/(V_(2q_k-1)V_(2q_k))].

An off-line quartet forces B_k>=2q_k asinh(delta k/(2C_h)), and therefore
liminf B_k/(q_k log k)>=2. The upper bound excluding that growth is not proved.
This is the remaining term in this endpoint criterion, not a claim that all
other global realization/trace questions have disappeared.

## Retained source maps for the volume

Two block next-relation Gram matrices compute B_k. Each block basis is
T-R_i F and has Gram Omega+F*G_i F, zero jets, an explicit quotient inverse,
and the original theta primitives. Quotient-killed relations map to e in their
receiving fibre, not external tau. In confluent-transfer coordinates only the
four matrices F_0,F_1,F_q,F_(q+1) are needed, with the source norm products
and raw-jet factorials retained.

## Reading and evidence

Main inspected: b32ca2128e0deb0eec6eafb860776a5d6a28dcbb.
Endpoint source: PR23 c720f40530eed2f5969dbabe94dfd3fddc0f507f.
Transfer source: PR24 dfcbba5cbf7fec8c9301fe242c13e741d762013e.
18 exact finite methods passed both modes; negative controls failed.
No new Lean certificate, numerical enclosure of C_h, global RH claim, or remote
write. The Deligne S20 reassembly is byte-verified; only the listed passages
were read. Old nested TeX has strictness and squared-eigenvalue errors recorded
in SOURCE_REVIEW.md; the original files are unchanged.
