# Independent review of the original coherent comparison

## Verdict

Accepted: OCQ.1–OCQ.35 have no blocking mathematical defect. The final reviewed TeX is `../coherent_comparison/original_coherent_comparison.tex`, 585 lines, SHA256 `fd662634929885a44b911aa556e0b5b723abf434d38d1c6a49710303859d7a85`.

The source's qualification about Ext is essential and correctly present: its Ext computations concern modules over the analytic local ring, not an unproved identification with stalks of sheaf Ext for the noncoherent source. The global ordinary Hom factorization is separately proved using an actual sheaf epimorphism. Proper labels retain their exact relation quotient and its extension obstruction, and the original residue map lands in the computed tau right-adjoint target with the original dilation character.

The new companion `derived_coherent_bidual.tex` contains a stronger continuation requested by the parent and accepted by the author: the global canonical g-splitting, a basis-free local Ext formula, the injectivity of the natural local derived bidual, and the actual two-leg tau cochain decomposition preserving degree zero and the reciprocal minus-leg dilation. It is separate from the reviewed OCQ source.

## Coverage and authoritative sources

The following paths are relative to the shared repository root.

* Full OCQ.1–35 draft read, followed by the final small wording/provenance and wrapping changes identified by the author. Current hash above.
* Full `work/rh_counterfactual_20260913/shared_thread_audit/turns/A1427.md`, 544 lines, SHA256 `387c1705fc86561db1793ce2cde44172e1f428da8d9ccac18d2e1ee7889c9d05`.
* `work/rh_counterfactual_20260913/shared_thread_audit/turns/A1523.md`, lines 97–510 read directly, covering the exact four-point chart, both source restrictions, actual tau cohomology complex, right-adjoint complex, reciprocal second-leg dilation and finite residue map. Full record has 619 lines and SHA256 `518924c41a5edaa4ac598eb81d4e21caf018b33b45b6f0a79bfb083202b4b58a`. No assertion of full-record reading is made in this review.
* Full `work/rh_counterfactual_20260913/shared_thread_audit/segment29_40/original_balanced_kernel.tex`, 396 lines, SHA256 `8beb9dba80a6d64b9e20b0bde6d4636208c29ad062d2746feaddb5ddfb4efc01`; a truncated tool window was completed by the explicit lines 216–275 reread.
* Full `work/rh_counterfactual_20260913/shared_thread_audit/derived_packet_comparison.tex`, 185 lines, SHA256 `7299f71b048f2075fd3691c579605f40cde2e0e0077c88cba583a0aad267b178`.
* Full `work/rh_counterfactual_20260913/shared_thread_audit/proper_label_spectral_kernel.tex`, 216 lines, SHA256 `56b96792c1a9eb352a9c2989d6737ececb858dac06190ae9065c9fdca415dc33`.
* Full preceding `balanced_independent_review.md`, whose repaired proper-label findings are consistent with the current BK, DP and PL modules.

## Checks of the coherent comparison

1. **Original sheaf construction and gluing.** The presheaf `O(U) tensor_A Q` has the required restriction maps and sheafification has stalk `O_s tensor_A Q`, because tensor products commute with filtered colimits. Mellin balancing follows from `M DF=s MF`; theta boundaries map to multiples of the unchanged entire function `g=2xi`. The nowhere-zero Gaussian transform `sqrt(pi) exp(s^2/4)` supplies local lifts, hence a genuine sheaf epimorphism.

2. **The meromorphic field is the analytic one.** At a point, `O=C{z}` and `F=O[1/z]`. A nonzero analytic germ is a full analytic unit times a power of z. BK.18 therefore makes every such germ invertible on K, giving the unique F-action. Neither this construction nor the nonzero original Gaussian witness is a formal completion.

3. **Canonical torsion splitting.** OCQ.6 uses the actual function g, including its full local unit. Since gM lies in K, the formula `p_K=(g|K)^(-1)g` makes sense, and `p_T=1-p_K` projects onto `M[g]`. Its kernel is exactly K. The map `b|M[g]` is an isomorphism onto `O/(g)`. The companion proves these local formulas are also unique sheaf maps and glue globally.

4. **Ordinary coherent targets.** The finite-module elementary divisor argument proves `intersection z^n E=0`. Every image of the divisible K is divisible, hence lies in that intersection. This proves both universal factorization through b and `Hom(M,E)=E[g]`, with the specified inverse. Conversely every nonzero divisible target submodule admits a nonzero O-linear map from F by choosing a compatible divisible chain. The chosen F-coordinate of the explicit nonzero K witness then produces a map that does not factor through b. Thus the stated largest target class is correct.

5. **Noncoherence and all quotients.** A finite O-module cannot contain the nonzero witness in every `z^nM`, so M and K are nowhere coherent. The global Hom-sheaf factorization follows from its actual stalkwise vanishing on K and the sheaf quotient property. Every coherent local quotient of M comes from an ideal `(z^r)` containing `(g)`, with `0<=r<=m`; the full removed kernel and its multiplicity are correct. The global ideal sheaves are the corresponding effective subdivisors of the actual divisor of g.

## Checks of the derived calculation

The free telescope differential is exactly `d(e_n)=e_n-z e_{n+1}`, with quotient map `e_n -> z^(-n)`. Its last nonzero coefficient proves injectivity; reduction to the final basis vector proves exactness. Applying Hom gives `Delta(a)_n=a_n-z a_{n+1}` with the correct sign.

The sum `S(c)=sum z^n c_n mod E` converges only in the explicitly specified completion. For `c=Delta a`, finite partial sums telescope to `a_0-z^(N+1)a_{N+1}`, so the image is zero modulo E. If this formal sum is an analytic germ, the formula in OCQ.18 has analytic numerator of zero order at least n and therefore gives an actual analytic germ after division by `z^n`. This proves the kernel claim. Constant coefficient sequences supply all formal series; the finite torsion formula in OCQ.19 handles all finite modules. No exchange of analytic and formal convergence is used.

The free direct-sum resolution of an F-basis of K yields the stated product of completion quotients, and Ext vanishes above one. OCQ.22 follows from the canonical splitting and the literal resolution by g. The hyper-Ext argument has only its p=1 column, so the exact finite-length characterization of bounded finite derived targets is correct. The basis is nonempty by the actual Gaussian witness; that point is needed for the reverse implication and is present.

The nonsplit extension OCQ.25 has relations `e_n-z e_{n+1}=n! ds`. The injection of omega and quotient by it are checked directly. A splitting would give analytic germs with `a_n-z a_{n+1}=n!`, hence a convergent Taylor germ with factorial coefficients. That is impossible. Pullback along the chosen meromorphic coordinate of the original K keeps this extension nonzero on the embedded F-line, so it cannot come from the finite N summand. Its target is the coherent module `omega[1]` in the declared analytic stalk-module derived category.

The second independent review in `stalk_sheaf_bridge/REVIEW.md` reproduced these telescope, extension, and analytic-versus-formal calculations. Its companion `BIDUAL_REVIEW.md` verifies the natural derived bidual sign, including comparison with an injective target.

## The exact global derived replacement and new bidual result

For the noncoherent K, there is no automatic isomorphism between stalk-module Ext and the stalk of internal sheaf Ext against `omega_X`. The author correctly declines that inference. The companion instead proves the actual global split summand

`R sheafHom(M,omega_X) = (omega_X/g omega_X)[-1] direct-sum R sheafHom(K,omega_X)`.

For the full local module K it also proves canonically

`Ext^1_O(K,omega) = Hom_F(K,completed omega/omega)`.

The completion quotient is an F-vector space: z-surjectivity follows by removing the constant coefficient, and z-injectivity follows by analytic division of a germ with zero constant term. Hom and positive Ext from any F-vector space into completed omega vanish by the explicit formal telescope solution. The connecting map is therefore canonical and is represented by a literal pullback of the completion sequence.

For `D_omega=RHom(-,omega[1])`, the natural bidual is the positive evaluation map

`k -> (f -> f(k))`.

The shifted target model has differential `-projection` in degrees -1 and 0. The Hom complexes have only degree-zero terms for an F-vector source, so the evaluation sign is positive. Comparison to an injective resolution verifies this is the natural derived map. Nonzero F-linear functionals into the nonzero completion quotient separate K, proving injectivity. The finite N summand has its literal finite-free bidual isomorphism, preserving g. Thus ordinary analytic dual vanishing is not a reason to erase any original class from the true local derived bidual.

The exact alternative global target of the local Ext calculation is the point-supported sheaf `i_{s*}omega_s`. Stalk evaluation is exact and left adjoint to the exact skyscraper functor, yielding both global and internal derived adjunctions. This target is explicitly noncoherent on X. It is not mislabeled as the coherent analytic canonical sheaf.

## Original tau cohomology, residue and dilation

OCQ.26–30 match the actual A1523 residue comparison. Division by the exact g gives `omega/g omega -> g^(-1)omega/omega`; the local dual basis contains the full unit `u(z)` before cancellation. Residue is well-defined on both quotient arguments and its matrix on the displayed bases is the identity. The reflected germ `f^dagger(s)=conjugate f(1-conjugate s)` is well-defined because `g^dagger=g` and the finite actual zero set is reflection stable.

The finite Mellin-jet map is onto on the original target function space. Consequently the residue composite into `Hom_C(Q,C)` is injective. Its target acquires the original one-dimensional character L1. Precomposition with `R_{1/a}` and multiplication by a sends the differential representative to `a^(1-s)` times itself; this agrees exactly with `(a^s f)^dagger`. The g-prime insertion gives the original trace with multiplicity `m_rho`; no assertion that this nilpotent-killing trace is the perfect residue pairing is made.

The companion explicitly retains the full original tau complex, including its degree-zero diagonal source. Give V_plus the action t=D and V_minus the action t=1-D. Fourier is an A-linear isomorphism V_minus to V_plus. The coordinate map `(phi,psi) -> (phi-hat(psi),hat(psi))` identifies the balanced two-leg complex with the balanced single-theta complex plus V_plus in degree zero; the inverse is `(u,v) -> (u+v,hat(v))`. Thus H^1 is the original M=N direct-sum K, and H^0 is retained rather than silently removed.

The original A1523 actions are `R_a` on the plus leg and overlap, and `a R_{1/a}` on the minus leg. Fourier intertwines these actions, so the full cochain decomposition is equivariant. The balanced chain map to `[O --g-> O]` is `(H_phi, Mellin F)`, and its degree-one map is beta. Canonical splitting commutes with dilation, giving the complete `a^rho exp((log a)N_rho)` action on the actual full nilpotent packet.

## Proper labels and support

The exact sequences in OCQ.32 agree with DP.6 and PL.12–14. A finite-target map from M_W factors through b_W exactly when it vanishes on the full relation quotient L_W. The pushout obstruction in OCQ.33 has the correct sign and its splitting is equivalent to extending the prescribed map from L_W. For W contained in W-prime, both transition kernels are the same balanced `W-prime/W`, with the original theta arrow identifying them.

The actual proper-label PL example is therefore retained, not contradicted by the full-source universal quotient. The full source's meromorphic invertibility is never transferred to K_W. A dilation at a proper label is transported from W to R_a W, as already proved in DP; no additional invariance of W is assumed here.

The support lift sends `(S,v)` to `(S,f(v))` and external tau to tau. A killed vector remains at its supported zero, while only external tau has image external tau. These explicit maps connect the analytic calculation back to the original support fibres. No off-line zero or purity bound is deduced from the universal quotient or the derived-dual computation.

## Validation receipt

The companion has 23 uniquely named DC equation tags and a direct standalone LuaLaTeX wrapper. Its current five-page build is clean, with no warning or overflow diagnostic after correcting one equation line wrap. Root and the independent checker identified an ambiguous reference to the diagonal kernel; the final text now gives the full chain kernel `[ker H direct-sum V_plus -> ker Mellin]`, its exact maps, and its two cohomology modules. The final support paragraph also explicitly restricts the joint-face decomposition to the plus-only and minus-only subcomplexes, rather than transporting the full diagonal to a single leg. Mathematical source inspection, rather than finite sampling, verifies its formulas. No Lean, Lake, or Elan session was started. The author-owned OCQ file was not changed by this reviewer.
