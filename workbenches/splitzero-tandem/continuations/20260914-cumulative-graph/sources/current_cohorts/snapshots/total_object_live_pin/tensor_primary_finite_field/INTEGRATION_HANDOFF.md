# TPF integration handoff

Ready includable source: tensor_primary_finite_field.tex.

- TPF.1–55, 56 unique labels, 31 internal references. Standard sectioning and amsmath/amssymb; no preamble or external macro dependencies.
- Eleven-page draft-mode compile at A4, 11pt, 23mm margins. No LaTeX warnings, unresolved references, overfull boxes, or underfull boxes. The only expected tool notice is pdfdraftmode; no output PDF was created.
- Final source SHA256: 5c2fa0e144f74aea4f21604e986a36fd8b5f37ee4e8235a36a605b49eba32b95.
- Exact validation: check_tensor_primary.py and EXACT_CHECKS.json.
- Primary source verification: SOURCE_REVIEW.md, including the verified relative compact-support Kunneth theorem and explicit researcher-hosted primary URL.
- Independent reviews: review/tensor_review.md, review/terminal_character_review.md, and review/common_model_m1_review.md. The final reviewer independently confirmed the final source hash and sealed TPF.36–55.

## Contents for assembly

TPF.1–11: actual ordered k-fold source on the same u-line, full sheaf decomposition, all Gauss constants and Frobenius signs.

TPF.12–24: original inertia representation, exact tame and full projectors, all character multiplicities, finite image orders, Swan, and finite-cover logarithm. The tensor can cancel its original wild character when p divides k.

TPF.25–35: original-base invariant Frobenius, character permutation chi→chi^Q0, actual smaller-field source maps, exact cycle constants, pure weight k, and gcd/Mobius orbit counts.

TPF.36–43: terminal label chi_* inverse, exact terminal orbit and invariant criterion, typed characteristic-p scalar specialization in the full nilpotent remainder module. Scalar reduction is only asserted on a marked stage admitting the specified alpha; a stage inverting p has no such specialization.

TPF.44–50: common cyclotomic integral deck module, exact idempotents, two base changes, and canonical reconstruction with the actual Gauss lines and their Frobenius. No field map between characteristic p and characteristic zero is inferred.

TPF.51–55: m=1 exception with all quadratic Gauss factors and no factorial loss; exact basis-independent scalar comparison between finite Frobenius and the original complex arithmetic dilation for every chosen nonzero map of the resulting one-dimensional complex spaces.

No global source edits or RH verdict were made by this scoped agent.
