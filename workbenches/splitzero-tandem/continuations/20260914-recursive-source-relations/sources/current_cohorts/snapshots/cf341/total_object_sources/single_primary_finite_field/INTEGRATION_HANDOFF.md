# SPF integration handoff

Ready includable file: single_primary_finite_field.tex.

- 29 equations tagged SPF.1–SPF.29; 30 unique labels; 13 resolved internal equation references.
- No preamble. Uses standard article sectioning, amsmath, amssymb, and ordinary text commands.
- Five-page draft-mode compile at A4, 11pt, 23mm margins. Final log has no LaTeX warnings, undefined references, overfull boxes, or underfull boxes. The expected pdfdraftmode notice reports that no output PDF was created. Parent owns combined PDF production.
- SHA256: 538b2da5adf307b54396e46f0848a49c63f0d81072844d191768016255c4fd53.
- Independent review: review/character_review.md. Character, projector, Frobenius, Gauss, constant, field-extension, inertia, and nilpotent-logarithm conventions passed. Reviewer-suggested explicit ramification-index proof is integrated.
- Exact validation: check_single_primary.py and EXACT_CHECKS.json. All 1,872 original-phase trace cases pass integer reduction modulo cyclotomic polynomials; all tested nontrivial Gauss sums satisfy G conjugate(G)=p exactly. Tests supplement the full symbolic proof.
- Primary references and checked locations: SOURCE_REVIEW.md. The author-hosted Katz PDF hash is 8711424f8edb14f38c0e61606ef49d6efc67d5a93ac9f5bd9fa3e13b7c7d9ffe. The downloaded book and text under sources/ are a local research cache, not inputs required to compile the proof module.

## Exact objects and results for assembly

The finite-field datum is the specified ring map from the original coefficient ring containing rho, 1/n!, and every coefficient of the full Taylor class upsilon_h=j_h(g/h) and its inverse in the retained m-dimensional remainder basis. The entire source map is s=y+rho, and the phase remains y^n/(nu)+c/u with c=−(−rho)^n/n. No unit is removed or substituted into the phase.

Over the explicit splitting constant field with n dividing Q−1:

F = Lpsi(c/u) tensor direct sum over chi^n=1, chi≠1 of A_(−G(chi,psi)) tensor K_(chi inverse)(1/(nu)).

Equivalently the summand is A_(−chi(n)G(chi,psi)) tensor K_chi(u). These are isomorphisms of sheaves, proved by power-map projectors and source-coordinate isomorphisms, not just matching traces.

The actual rank is n−1=m. It is pure of weight one by the exact Gauss absolute-square proof, with no half Tate twist. At the original geometric inertia group I_0 its invariant space is zero for c=0 and c≠0. Its Swan conductor is 0 when c=0 and n−1 otherwise. The cover u=v^n, z^p−z=bc/v^n retains and then trivializes the Artin–Schreier factor, and makes the full geometric inertia action trivial. Thus the unipotent logarithm is exactly N=0 while the original invariant space remains zero.

Use ordinary inertia and boundary terminology. This module asserts no new support concept and no complex arithmetic zeta-zero construction.
