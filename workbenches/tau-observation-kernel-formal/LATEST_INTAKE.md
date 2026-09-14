# Concurrent original-kernel continuation and exact source join

14 September 2026. While the new finite proofs were being checked, main advanced from `5a2fa7d6fc2db3133601dccbeed77785792be5d4` to `8fd2157e8b41783224b42781699432d824ec0c15`. The complete commit comparison was read. It modifies six publication/index files and adds the flat `20260914-original-kernel-web` source package; it does not alter an inherited Lean source or workflow. The branch integration preserves those exact changes and both parent histories. It does not merge this contribution into main.

## Reading scope

At the earlier main revision, the complete OPG1–26 and OPR1–5 bodies and NEXT_RECEIVING_INTERFACE were read. At the new main revision, the complete `00_CONTINUE_HERE.md`, all 771 lines of `04_CYCLIC_SECTORS.tex`, and `12_VALIDATION.md` were read. Their Git blobs are respectively `b89cd22db659923f5ef1312e437cb3030a99695c`, `a467c6180cd65ddfc19e40a4eb69805bafd06b47`, and `4a364c0e54b12b55426dde17927128bc58275949`. The other newly mirrored full TeX bodies are preserved, but this is not a claim to have independently audited their entire analytic proofs, source-only builds or reported validation.

The current handoff says the remaining analytic target is the absolute common original-kernel contribution `F_K^(1)/(kq)`, after the stated baseline, Gamma and source-difference results. In particular this continuation does not continue to advertise those earlier source differences as the current unsolved step. Their complete arithmetic verification remains with the analytic source lane.

## The new finite code applies to the precise OCS matrices

OCS17–19 construct the literal observation matrix

    mathfrakA_(nu;(a,b,D)) = i^D D! c_(nu;abD),
    L H = F_0 mathfrakA,

where H is the original primary basis map and F_0 is the injective unscaled zero-charge tensor-coordinate map. The full period matrix, arithmetic unit, symmetrization multiplicities, i^D and D! remain in these entries. No orthonormality of the Fourier frame is asserted: its Gram is N(I+11*), as calculated in OCS4.

OCS37–39 retain the original action J through YH=HJ and form

    mathfrakO = [mathfrakA; mathfrakA J; ...; mathfrakA J^(q-1)].

The already supplied OCS39 identifies `K_inf=H ker(mathfrakO)`. Our ObservedIterates module formalizes this finite-kernel and invariant-quotient mechanism, including its support maps. It does not claim to originate the observed-iterate construction.

The additional ResidueObservation result computes that kernel by the original perfect residue pairing. Use the actual coordinate rows of `mathfrakA H^(-1)` as the lambda_mu in OK4 (equivalently, choose coordinates on im(L) and compose Lambda). Composing with the explicit injective F_0 does not change any of the iterated kernels. The action A and Y=(A-kI/2)/i have the same finite observed-iterate kernel by their invertible triangular binomial change. Thus OK5–7 apply to these exact OCS rows. They reduce the permanently invisible part to the common annihilator, and, in the written polynomial corollary, to `gcd(chi,a_mu)`. The raw kernel and the invariant kernel remain distinct even when a later source calculates the raw kernel's dimension.

This identifies a finite test of which original primary socle lines the actual observation sees. It does not assert that the actual period rows pass that test, bound a reconstruction condition number, or evaluate the common original-kernel volume. The new observation-norm identity retains OPR's corrected kernel vector and the actual source metric for that next analytic calculation.

## Preservation and certification

The observed successful implementation `8e78bc7c240b04d297ade6afdadfd863e0c6db7b` predates this documentation/source-intake reconciliation. The reconciliation changes none of its Lean, runner, finite-checker, workflow or used dependency blobs. Its certificate is stated at that exact implementation; a later run is not claimed before observation. The mirrored analytic source has its own written-proof and validation scope, not inherited Lean certification.
