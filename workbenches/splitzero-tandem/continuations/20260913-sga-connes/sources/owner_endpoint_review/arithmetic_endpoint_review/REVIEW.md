# Arithmetic endpoint intake: terminal mathematical review

Status: the original local-mass, convolution and diagonal norm estimates are accepted as written analytic proofs. The balanced-window extension is proved in `BALANCED_WINDOW_PROOF.md`. Two explicit scope clarifications below are required when integrating the ancillary quotient/transfer statements. No canonical source, frozen E artifact, remote branch or publication was changed.

## Preserved source and actual checks

The complete attached report (17,152 bytes) was read and preserved with SHA-256 `abdacca551cc7178170128c522beef8ac07d3948bf9ceea792177d0e0e8a21a8`. The original ZIP (781,925 bytes) was preserved with SHA-256 `c32ca4bebc86c6b7c7ffb58533a49b75e2140b00b31cdb6602cea6d8537ad9f6`. Its 32 regular members expand to 1,172,957 bytes. The bounded extraction checked every CRC and rejected absolute/traversing paths, symlinks, duplicate case-folded names and encryption. The original archive and extracted bytes were not edited.

All 31 manifest entries match their actual member sizes and SHA-256 values. The integration patch contains exactly 15 new regular files under `workbenches/tau-arithmetic-endpoint-bounds/`; every reconstructed patch output equals its archive member byte-for-byte, including the source-reading JSON's absent final newline. The patch was not applied to a canonical or remote tree. The local patch parser was repaired for ordinary Git single-line-hunk and absent-final-newline syntax; those were parser limitations, not source defects.

Read completely: the attached report; `NOTE.tex`; `RESEARCH_NOTE.md`; `HANDOFF.md`; `SOURCE_REVIEW.md`; `CHECKS.md`; `PROGRAMME_STATE.md`; `README.md`; both supplied Python programs; and the manifest/source-reading evidence. The reviewed executable checker imports SymPy and performs bounded local exact fixtures. Its 18 methods pass in ordinary and optimized Python with identical successful output bytes. Both deliberate failure controls exit 1 with the intended message. The fresh receipt and separate stdout/stderr captures are in `FINITE_REPLAY_RECEIPT.json` and `replay/`.

The prior Gamma and Deligne records bundled here remain attributed inherited evidence. This intake did not reassemble the external 216 MB Deligne archive, re-execute the Gamma predecessor, run Lean, compile TeX, or recheck browser-layout screenshots. None is needed to establish the new norm estimate from its stated density. No private-profile attribution was added.

## Proof audit

| Result | Actual argument checked | Scope |
| --- | --- | --- |
| NOTE (23), local zeta mass | Fixed Joukowski ellipse, nonzero anchor at 2+iT, annulus maximum principle, unit-disc derivative estimate, one-sided interval, compact completion | All real T; positive existence constant, no numerical enclosure |
| NOTE (25)-(29), arithmetic convolution envelope | Entire identity g=h v_h; gamma lower factor; polynomial h bound; positive compact minimum of w*w; threefold mass then k-3 restricted nonnegative integrals | Fixed h, every real u, k>=3; no normalization or replacement density |
| NOTE (32)-(37), monic norm estimates | Actual exponential moments, original i^j leading phase, exact monic Legendre minimum, factorial/central-binomial inequalities | Diagonal n>=k>=3; general n>=0,r>=1,k>=3,L>0 exact bound |
| NOTE (36), explicit C_h | Root of degree/mass/exponential/polynomial factors, retaining 2 from the sum of moments | Sufficient as written, intentionally nonoptimal, independent of n,k |
| NOTE (39), older threshold 2 | Diagonal norm theorem plus the supplied sinh endpoint selection and exact-quartet aggregate lower bound | Correct conditional consequence, no upper budget estimate |
| NOTE (44)-(48), relation-layer identities | Original kernel update, determinant lemma, zero jets of T-R_iF, positive Gram, canonical representative projection | Nonempty packet; i,j admitted; original boundary spaces retained |
| Balanced-window and threshold 4 | Exact bound at L=n, uniform n/2<=r<=n, exact-window product on n=q,r=q-1, monotonic overlapping volume costs | Written synthesis; requires separately reviewed original radius identity, no new Lean claim |

### Local-zeta and constant details

The ellipse semiaxes are 65/16 and 63/16; its s-plane real strip is [-55/16,71/16]. For |T|>=10 its imaginary part stays separated from zero, so the pole is outside. On sigma>=1/4, the fractional-part integral gives O(1+|T|). On the reflected strip, the functional equation and uniform gamma estimate give exponent 3/2-sigma<=79/16<5; a common exponent 6 is safe. A unit disc around [-1,1] lies inside the ellipse: the enclosing rectangle |Re z|<=2, |Im z|<=1 has `(32/65)^2+(16/63)^2<1` in its ellipse equation. Cauchy therefore gives exactly the stated derivative bound, without a lost radius factor.

The anchor radius r_*=(3+sqrt(13))/2<4 implies theta>1/3. Since c_*=1/zeta(2) lies in (0,1) and M>=1, `m>=c_*^(1/theta) M^(-(1-theta)/theta)>=c_*^3 M^-2`. The interval mass is `m^3/(8M)`, hence exponent `6*7=42`; the one-sided interval fits even at a maximum occurring at an endpoint. Positivity on the compact T interval follows from continuity and the identity theorem. No zero-spacing or RH assumption enters.

For explicit identification, one can choose `c_h^(1)=c_h^(0)c_zeta exp(-pi/2)2^(-2d)` and `c_h=b_h c_h^(1)`. The factors `b_h`, `vartheta_h`, and `M_h(+b),M_h(-b)` stay actual positive quantities. The original whole density remains in every norm. The entire identity, not an unevaluated division, handles selected critical-line zeros.

The diagonal constant in NOTE (36) is sufficient: after including the factor 2 from the two moments, the combinatorial factor is at most `32n*((2n+1)/n)^(1/(2n))<=64n`; the remaining mass factors are bounded by the stated square root. No missing factor 2 requires correction.

### Relation-layer map audit

For `b=T-R_i F`, original orthogonality gives `b*R_i=-F*G_i` and `b*b=Omega+F*G_iF`; consequently the plus sign in the representative update is correct. The columns lie in `D_j intersect D_i^perp`, have zero original jets, and their top-degree coefficient map is triangular with diagonal one. Removing those top coefficients from an arbitrary new relation leaves an old relation; orthogonality then proves surjectivity. This verifies the map, not only a dimension count. The determinant in (44) has positive eigenvalues through its similarity to `I+Omega^(-1/2)F*G_iF Omega^(-1/2)`; no unsupported claim of Euclidean Hermitian positivity is made for `I+Omega^-1F*G_iF` itself.

## Required integration clarifications, with exact correction

1. Immediately after (13), change the leading-coefficient multiplication sentence to start **“For n>=q, multiplication by the monic chi carries ...”**. Retain the separate statement that at n=q-1 the relation space is zero. Without this restriction, the literal asserted isomorphism would identify the zero source `P_-1/P_-2` with the one-dimensional target `P_(q-1)/P_(q-2)`. This is an endpoint-domain clarification, not a change to the valid norm proof.

2. In Section 8 before (41), explicitly retain PR24's dagger-stability prerequisite `bar(chi)(k-S)=(-1)^q chi(S)`. With c=k/2 and `psi(u)=i^(-q)chi(c+iu)`, the relation weight is `|chi(c+iu)|^2=psi(u)^2` under this prerequisite. The induced quotient map is `[P(S)] -> [P(c+iu)]`; raw derivative order d contributes `i^d`. The exact symmetric quartet satisfies this prerequisite. For an arbitrary packet, the analytic norm theorem still holds, but one must not silently assert the specialized squared-polynomial transfer identity. Apply the same qualification to the handoff's transfer item D. This matches the separate PR24 reviewer correction and retains all raw factorial and norm-product factors.

The source's threshold 2 is not false: it follows from the older, weaker sinh bound. A next-cut integrated account should retain its provenance while presenting the new threshold 4 as the strengthened join, with the exact-window input and balanced-window proof cited. No mathematical correction to the core mass/norm theorem was found.

## Integration-ready result map

- Incorporate the full actual-density local-mass proof and threefold envelope into the analytic-source section, preserving NOTE (23)-(34), original mass mu_h^k, and k>=3.
- Retain the diagonal theorem and its literal C_h; add `BALANCED_WINDOW_PROOF.md` BW1-BW3 for every balanced source window.
- Join the separately reviewed exact radius-product theorem, with phase retained, to BW5 on the same canonical metrics. On n=q,r=q-1, use norm endpoint 2q-1 and radius indices q,...,2q-2.
- Present the central two-volume bound and the exact identity `B_k=2C_k+log(V_(q-1)/V_q)+log(V_(2q-1)/V_(2q))`; conclude the four-volume liminf at least 4.
- Retain the source-to-leading-coefficient and source-to-arithmetic-quotient diagrams as different maps, with clarification 1. Retain relation-layer block costs (44)-(48), and add clarification 2 before the PR24 determinant coordinate specialization.
- Mark the missing next analytic input precisely: an upper four-volume budget with normalized limsup strictly below 4, or a corresponding central two-volume upper estimate. Positivity, fixed transfer width, or finite fixtures alone do not provide it. This is not an RH proof.

## Primary literature checked

The needed published identities were checked directly at [DLMF 25.4.2](https://dlmf.nist.gov/25.4.E2) (zeta functional equation), [DLMF 5.11.9](https://dlmf.nist.gov/5.11.E9) (gamma asymptotic, explicitly uniform on bounded real strips), [DLMF 18.3](https://dlmf.nist.gov/18.3) (Legendre norm and leading coefficient), and [DLMF 18.5](https://dlmf.nist.gov/18.5) (Rodrigues representation). The elementary integral formula and annulus maximum-principle argument were checked as written derivations. Deligne is not an input to the new inequality; inherited transcription comparisons were not relabelled as this intake's independent primary-source audit.

## Independent parent synthesis review

The complete parent `FOUR_VOLUME_THRESHOLD.md`, SHA-256 `9ff55c84d74db85306e7a68c70fe7b08d8e642e8ac1a3e6137649f68e102fc3a`, was read independently. Its literal constant, envelope amplitude c_h, original phase, exact multiplicities, every endpoint index, zero-contraction treatment, overlap identity and verification boundary are correct. No required correction to that exact file was identified. The norm constant is not numerically enclosed, and the analytic source realization and radius identity remain their explicitly stated upstream inputs.
