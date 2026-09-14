# Coherent-comparison review log

## Assignment and source scope

Parent assignment, verbatim: "Review coherent-comparison math directly with counterfactual_algebra once written. He proves β:M→N=O/(g) is universal among maps to finite coherent analytic targets because K is divisible meromorphic module; claims Hom(M,ω)=0 but Ext1 contains nontrivial kernel Ext1(K,ω) ≅ (Ohat/O)ds per meromorphic basis via telescope. Audit analytic local-ring vs completion distinctions, all proper-label/source transitions, actual source sheaf gluing and retained dilation; need strongest exact map into true tau cohomology/purity, not just one failed map. Own continuation2/coherent_review. Check derived-dual computation independently."

The original full-source constructions BK, DP, PL and authoritative source A1427 have been read in TeX/Markdown. The author is writing `../coherent_comparison/original_coherent_comparison.tex`; review will read that file when present. No target file will be edited.

Current independent findings:

1. The original full-source balanced comparison sheafifies and its canonical splitting is the original g-torsion summand, obtained because multiplication by the exact entire g is invertible on the meromorphic kernel at every stalk.
2. Ordinary coherent-target universality is valid stalkwise and glues using this actual sheaf epimorphism. The proper-label kernel is instead the full extension by O tensor_A(V/W), as proved in DP.6–8 and the actual PL.1–15 example. It must not inherit the full-source universality without that term.
3. The telescope Ext calculation is valid in analytic stalk-module categories. Completion enters only as a computed target quotient, never as replacement of the original analytic O-module or source functions.
4. A stalk Ext group for this noncoherent source is not automatically the stalk of internal sheaf Ext against the analytic canonical sheaf. The exact global coherent derived summand is obtained directly from the split map to O/(g). The exact alternative sheaf realization of the local Ext group has target i_{s*}(omega_s), a noncoherent skyscraper target, by stalk/skyscraper derived adjunction.
5. New strongest local continuation: the completion exact sequence canonically identifies Ext¹(K,omega)=Hom_F(K,completed omega/omega). This quotient is an F-vector space. For D=RHom(-,omega[1]), the derived bidual on K is vector-space evaluation and is injective. The ordinary dual vanishing therefore does not erase any class from the true local derived bidual. The natural positive evaluation sign has been independently verified, including comparison with an injective target and the finite N double-dual resolution.

The above findings have been sent to parent and author. The independent nested reviewer has accepted the stalk/skyscraper bridge, telescope extension, and natural bidual map under `stalk_sheaf_bridge/`. The full author OCQ.1–35 proof has been reviewed and accepted in `OCQ_REVIEW.md`.

The requested new standalone companion is `derived_coherent_bidual.tex`, DC.1–23, final source SHA256 `2efb32e03d456ae889b13e046600ecec7a3b7d3d9f7948c1de06e7dd83ea48af`. It proves the global canonical splitting and split coherent-derived summand, the exact completion dual and injective local derived bidual, the precise point-supported sheaf bridge, and the true original tau complex with its full degree-zero source and reciprocal dilation. Its clean five-page LuaLaTeX wrapper is `DERIVED_COHERENT_BIDUAL_MAIN.tex`.

Root and the independent reviewer found a wording ambiguity in the first companion draft: the diagonal source was the kernel of the first projection, whereas the full map to the analytic g-complex has the larger degree-zero kernel ker H plus that diagonal. This has been fully repaired by DC.20–22, which prove the whole exact chain kernel, its actual surjectivity witnesses, and H⁰=V_plus, H¹=K. The support ending also explicitly identifies the one-leg subcomplexes inside the joint-face decomposition, so no diagonal H⁰ is added to a one-leg face. Root has received this final repair and source hash.

Existing complete user-input provenance remains in `../../shared_thread_audit/segment16_28/user_inputs_verbatim.md` and the parent session's durable provenance log. No mathematical counterexample to RH is asserted; the actual divisor h|2xi and its complete jets remain the counterfactual input.
