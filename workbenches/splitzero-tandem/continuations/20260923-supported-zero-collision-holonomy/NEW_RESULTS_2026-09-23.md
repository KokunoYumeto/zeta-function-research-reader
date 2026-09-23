# New mathematics — 23 September 2026

The new proofs extend the original Rodgers–Tao heat family and the full split-support construction. The attached reader retains the preceding 40-page argument in full; the added calculations begin at page 41. Every occurrence of m refers to the order of an actual real zero under consideration. No multiple zero is asserted to exist.

## SZ-20260923-122 — The complete conductor and discriminant of an original heat collision

For an actual real zero of H_0 of order m, the original algebra A=C{t}[xi]/W embeds in its integral closure B with B/A isomorphic to the direct sum over k=0,...,m-1 of C{t}/(t^floor(k/2)). Its length is floor((m-1)^2/4). The exact full-unit conductor, special-fibre map and full support spectra are evaluated. The discriminant has leading coefficient 2^(m(m-1)/2) times the product j^j, order m(m-1)/2, and next coefficient m(m-1)(2d-c^2).

Complete proof: [HC1-19, HC27-30](HEAT_COLLISION_CONDUCTOR.tex). SZ-20260923-121, EP1-21: the original energy finite part now determines the first regular discriminant coefficient.

## SZ-20260923-123 — The trace-invisible endpoint is a derived cotangent group with a perfect pairing

For the full relative algebra, Omega=A/(W_xi) dxi has length m(m-1)/2. Tor_1(Omega,C)=(xi) in C[xi]/xi^m, and Omega tensor C=A_0/(xi^(m-1)) dxi. The torsion linking form lambda(ab/W_xi) mod C{t} is perfect; at the endpoint lambda_0(ab) pairs (xi) perfectly with A_0/(xi^(m-1)).

Complete proof: [HC20-26](HEAT_COLLISION_CONDUCTOR.tex). RD27-28a of the pinned collision-residue proof: endpoint duality is carried through the whole original time family.

## SZ-20260923-124 — Actual heat holonomy, reflected-trace defect and arithmetic commutator

The connection is partial_t+(W_xixi/W_xi+2U_xi/U) partial_xi, with the complete original analytic unit. Its monodromy is M=V^-1 P V. For r=floor(m/2), upper-half-plane transport has exact Hermitian defect 2 V_+^* Pi_- V_+, rank r. The squared commutator norm with arithmetic scaling is 8 sum_a sin^2(L(theta_a,+-theta_a,-)/4); its t^2 coefficient is -16 L^2 FP(E) -(L^4/3)m(m-1)(2m-3).

Complete proof: [HH1-38; HC30](HEAT_COLLISION_HOLONOMY.tex). SZ-20260923-120-121: the full residue-to-Weil receiver and original finite energy now enter one evaluated two-action calculation. Deformed fibres are not assigned the arithmetic Weil meaning of t=0.

## SZ-20260923-125 — The full supported fixed locus and the original two-prime action

On each complete endpoint jet, nonresonant scaling fixes zero amplitude; nonzero resonant scaling fixes the entire socle line. Every zero-support label remains fixed. On any finite packet of actual zeta zeros, ker(T_2-I) intersect ker(T_3-I)=0 and the supported common fixed set is exactly the whole lattice L. The original compact-test dilation preserves the complete Weil form; the two scalar prime characters and the finite nilpotent logarithm retain every zero location and jet.

Complete proof: [PFH1-7 and HH39-43](PRIME_FIXED_SUPPORT_RECEIVER.tex). HH39-43 extends the scalar supported-zero fixed locus; PFH uses and cites the retained TP1-6 joint prime receiver.

Human sources are Brad Rodgers and Terence Tao’s [original heat-flow paper](https://arxiv.org/abs/1801.05914v5), Alain Connes and Caterina Consani’s [multiplicity-sensitive spectral construction](https://arxiv.org/abs/2207.10419) and [complete archimedean Weil form](https://arxiv.org/abs/2006.13771v1). The reader gives the exact author-source equations; SOURCE_READING_AND_USE.json records versions and actual reading coverage. Hermite conventions are credited to the named DLMF chapter authors.

The remaining arithmetic question is the complete Weil form on the original global tests. The new formulas evaluate local transport, cotangent and support data; they do not assign positivity to the degenerate trace by discarding its radical.
