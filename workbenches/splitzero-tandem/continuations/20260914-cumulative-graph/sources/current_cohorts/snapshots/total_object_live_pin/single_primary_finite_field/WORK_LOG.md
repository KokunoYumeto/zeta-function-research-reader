# Single-primary finite-field calculation log

This scoped module belongs to the ongoing Bloch-/Split-Zero programme. It computes the actual compact-support sheaf of the specified single-primary phase; it does not construct an arithmetic RH zero or assert a verdict about RH. Parent owns global packaging and session provenance.

## Delegated task, verbatim

> Bounded finite-field part ONLY. Actual h(s)=(s−rho)^m, n=m+1, t=0, Phi(0)=0 ->Phi(s)=((s−rho)^n−(−rho)^n)/n=y^n/n+c with c=−(−rho)^n/n. Originalfinite ring includesrho,1/n!, fullunit/inverse g/h coefficients. For specified specialization kappa=F_Q charp>n, compute actual sheaf F=R^1 pi_! L_psi(Phi(s)/u) onGm_u. Derive explicit geometric Kummer/Gauss decomposition and inertiaat u=0, afteradjoining nthroots finiteconstantfieldextension ifneeded. Need actualV^I=0, finitecoverunipotentlogN=0 preserving c/u ASfactor; handlec=0 specialization separately. UseONLYprimarysourcesverifywithweb (Deligne/Katz/Stacks originalsource). Full proofs exactcharacters/signs/Gauss factors and mark no arithmeticRHzero construction. Own work/rh_counterfactual_20260913/total_object/single_primary_finite_field/; parentroot ownspackaging; I complexPascalperiod/monodromy/source. Produce includableTeX section/subsection no preamble (prefixSPF) +sourcecitationsreview. IMPORTANT Frobeniustrace conventions compute −Gauss and inverseKummer on a=1/(n u), then rewrite on u keep nconstant. Need independentlyboundedreasoning no generalallpacketStokes.

## Plan and current calculation

1. Fix geometric Frobenius and finite-field character conventions by trace functions.
2. Translate s to y=s−rho without changing Phi or dropping c.
3. Compute the finite power-map direct image, including its trivial summand at zero; prove the trivial summand contributes no compact-support cohomology.
4. Compute every nontrivial Kummer summand geometrically by w=az and identify its one-dimensional compact-support cohomology and exact negative Gauss Frobenius.
5. Retain the factor chi(n) on passing from a to u; prove the full extension-field trace identity.
6. Compute inertia for c=0 and c≠0 and give a finite cover trivializing it, with unipotent logarithm exactly zero.
7. Include elementary Gauss absolute-value proof, finite-field numerical checks, primary-source verification, and independent review.

Initial formula derived for checking: F = Lpsi(c/u) tensor direct sum over nontrivial chi^n=1 of A_{−G(chi,psi)} tensor K_{chi inverse}(1/(n u)). Equivalently the constant eigenvalue is −chi(n)G(chi,psi) multiplying Kchi(u).

An independent character/inertia reviewer is assigned in the review subdirectory. No original/global TeX is being edited by this scoped agent.

## Completed mathematics and checks

- Wrote SPF.1–29 in single_primary_finite_field.tex: specified coefficient map and exact primitive; support-preserving translation; full power-map projectors including the zero stalk; one-dimensional compact-support groups; inverse Kummer and negative Gauss factors; all finite-extension traces; separate c=0 and c≠0 inertia proofs; finite cover retaining AS factor; exact N=0; elementary pure-weight-one calculation.
- All 1,872 original-phase finite-field trace cases passed exact reduction over integer cyclotomic polynomials, together with exact Gauss absolute-square identities. No floating point and no Lean process.
- Primary sources verified: Katz author-hosted book; Stacks tags 0A3J and 03PK. Bibliographic and source details in SOURCE_REVIEW.md.
- Independent reviewer confirmed projector, inverse-character signs, Gauss sign, chi(n), extension-field descent, Swan1, invariant vanishing, and finite-cover logarithm. Adopted reviewer improvement proving ramification index e=p directly from p v_E(z)=−e.
- Five-page draft-mode TeX compilation has no mathematical typesetting warnings or overfull/underfull boxes. Parent owns PDF production, so no output PDF was created here.

## Final source wording correction

Parent requested, verbatim:

> One precise sourcewordingfix beforefinalintegration: SPF.1 'including ... every coefficient of original unit g/h and its inverse' could mean entireinfiniteanalyticfunction. Replaceby 'every coefficient of the full Taylor class upsilon_h=j_h(g/h) and its inverse in the retained m-dimensional remainder basis'; no changeactualproof. Confirmthisnewhash stable. I fullyread SPF1–29 andallmathaccepted inclroot/projector/Frob/Gauss/inertia. Ensure sourceURLcitationsread availableSOURCE_REVIEW (I'llread).

Applied that exact finite Taylor-class wording in SPF.1 and propagated it to the source review and integration handoff. The mathematical formulas and tests are unchanged.
