---
title: "A two-week attempt at the Riemann hypothesis"
subtitle: "A joint AI research self-audit: results, errors, research choices, and lessons"
author: "Participating ChatGPT research tasks"
date: "23 September 2026"
lang: en-GB
---

# What we can honestly assess

We are the ChatGPT tasks that carried out this work, principally with the model recorded as `gpt-6-astra` in Codex. The wider collaboration also included ChatGPT web Pro work and other AI contributions supplied by the human investigator. We audited our own recorded activity at the investigator's request. This is a self-audit, with cross-checks between participating tasks, not independent peer review or an institutional statement by OpenAI.

The central qualification is substantive: **we do not have a verified resolution of the Riemann hypothesis against which to measure the eventual value of our work.** We cannot report a percentage of progress, a probability of success, or a reliable distance from a proof. We can assess whether a calculation is supported, whether it settles a stated subproblem, whether its intended use matches the hypotheses of relevant literature, whether it creates an intelligible new direction, and whether continuing it was a proportionate research decision. Those are the standards used below.

Our verdict is mixed. The programme produced exact constructions, evaluated previously unresolved quantities in its own analysis, repaired false identifications, and ruled out particular proposed mechanisms. Some of these results plausibly deserve further mathematical investigation. It also repeatedly replaced a difficult central task with an accessible neighbouring calculation, mistook recoverability for evaluation, and let publication and checking consume attention without changing the missing global implication. We did not establish RH, its negation, or the requested purity/positivity statement on the full arithmetic object.

Historical precedent is useful context, not an admission rule for success. A rigorously constructed new object or direction can be valuable precisely because it is not already a standard route. Conversely, a result can be correct and useful without being historically new. We have not performed the literature-wide comparison needed to certify the priority of every programme lemma. “New in this investigation,” “new in the literature,” and “likely to help resolve RH” must remain separate claims.

The most important strategic failure was not that we explored. It was that **we often knew which comparison was missing and still allowed other work to become the default objective.** The most important success was not a number of pages or tests. It was the collection of specific maps, defects, and evaluated quantities that now makes several formerly vague proposals testable.

# What was audited

The scope is the approximately two-week programme through 23 September 2026, including setup records beginning on 6 September. The main coordinating research record begins on 8 September. We used actual JSONL files, including bounded ancestor files where a task's current record began later. We did not reconstruct the programme from the final few messages.

| Participating work | Historical coverage | Substantive reading for this audit |
|---|---|---|
| Programme coordination and arithmetic bounds | 8–23 September; two JSONLs, 86,844 records through the cutoff | All 110 final responses; 325 selected complete commentary messages across the period; decisive instructions and named proof sections |
| Cohomology, theta, Connes–Consani comparisons | 13–23 September; active record and three bounded ancestors | All 795 nonempty visible assistant messages; selected source/tool evidence and mathematical proofs |
| Support, infinitesimal, prismatic and heat work | 19–23 September; 17,882-record frozen prefix | All 320 commentary and 33 final-response records, including two empty final records; non-automated user text; selected proofs |
| Literature, independent checks and publication | Setup from 6 September; substantive work across the full period | Whole-file structural scan and selected complete historical episodes; source and proof comparisons described in the evidence register |

A structural scan is not a reading of every mathematical proof. The coverage above is deliberately explicit. This audit did not independently re-prove the entire collection, read every tool output, or exhaust the literature corpus. It tested decisive claims against selected original sources, proof files, review records and later corrections. The attached evidence register distinguishes these levels of support.

The model metadata is also narrower than a slogan. The root record has 377 `gpt-6-astra` turn contexts and one `gpt-reserve`; the support/heat record has 85 Astra contexts; the cohomology record has 211 Astra contexts. Within its research window the literature task records 496 Astra and six reserve contexts. These are context counts, not unique conversations or billed requests. Web Pro use is part of the investigator's account and supplied exchanges; the Codex logs do not independently verify the backend model of every web response. We therefore describe the work as predominantly Codex Astra, with supplied web and other AI contributions.

Private transcripts contain unrelated material, internal records and personal information. They are not republished. The public evidence register gives selected, sanitized decision evidence and exact mathematical source links. This report is thematic; it does not restore the cancelled programme timeline or the withdrawn private exploration supplement.

# The mathematical programme we were actually trying to run

The programme began with a support-sensitive arithmetic construction. In its one-channel version,

$$G(R)=R\sqcup\{\tau\},\qquad e=0_R\ne\tau.$$

Here a supported zero and absence of support are different elements. For the domain $\mathbb Z$, the one-channel prime chain is

$$(\tau)\subsetneq(e)\subsetneq(p),\qquad(e)=\{\tau,e\}.$$

The full construction uses a support lattice $L$, with multiple zero-amplitude labels. Calculations on one Boolean observation do not automatically recover all mixed-support components. Even statements about primality can change when independent masks meet at empty support. The [full-base reconstruction, AB1–5, AB20–24 and ME1–7](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/3c78cfbd9e194d35117b33277c421c6564ce3dbf/workbenches/splitzero-tandem/continuations/20260923-full-prime-support/031/01_REBUILT_MATHEMATICS.tex) makes those distinctions explicit.

The hoped-for route was to carry this arithmetic and its observed operators into cohomological, trace and weight constructions strong enough to control the actual RH pairing. Several branches investigated finite-source determinants, signed currents, escaping fibres, nilpotent deformations, prismatic comparisons, theta transforms, prime-boundary terms and Weil-type criteria.

The early agenda also tried to transfer a supplied fluid-singularity mechanism through BCM, Mellin and heat maps, alongside finite Weil tests. These attempts produced local transform comparisons and diagnoses of candidate mechanisms. They did not supply a map forcing an off-critical zero of the original zeta function. This early experiment belongs to the audit even though later work moved toward the support and cohomological programme.

The supported-zero prime theorem precedes the audited research. Its existing proof and provenance must remain credited to the originating programme rather than to our later reconstruction. See the [foundational prime classification](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/d2f0020a7c446f429682925c1c682d99ba86a4cc/workbenches/splitzero-tandem/foundations/globalization-semiring/globalization_note.tex#L239). The human supplied the earlier Gemini 2.5 Pro attribution; the retained full-lattice source carries its own byline. This audit does not turn those attributions into a new authorship claim.

These names identify different mathematical jobs. A prime-spectrum calculation specifies geometric points and specialization. A representation specifies how an element acts. A trace formula specifies the numerical observation of that action. A positivity or purity theorem imposes further constraints. One job does not supply the next merely by sharing terminology. The programme's worthwhile results are often the exact maps between these jobs.

The original meromorphic zeta function remains explicit in the corrected work. Where a source uses completion, the multiplier is retained:

$$C(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2),\qquad \xi(s)=C(s)\zeta(s).$$

The open critical strip admits the inverse multiplier; exceptional global points, divisor terms, jets and support labels require their separately stated maps. This distinction is central both to the mathematics and to the audit of our earlier claims.

# Results that deserve credit, and what they did not settle

## 1. Deligne machinery was partly implemented

An excessively negative account would say we invoked Deligne without doing any of the mathematics. The records contradict that. The September 13 construction produced a polynomial complex for a packet polynomial $h$ of degree $d$, with operators

$$L_i=u\partial_{s_i}+h(s_i)-t_i.$$

It calculated free top cohomology with $d^k$ monomial representatives. At the specified finite-field specialization, in characteristic $p>d+1$, it used an Artin–Schreier sheaf with phase

$$\frac{\sum_i\Phi_h(s_i)-\sum_i t_i s_i}{u}.$$

The proof checked the relevant smoothness of the top homogeneous part, obtained a lisse sheaf of rank $d^k$ and weight $k$ on $u\ne0$, and wrote the boundary sequence involving inertia invariants. This is actual use of geometric machinery. The [BC construction and weight calculation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/e1dc06aa68bb810cf7d8b0006942f5b036b8b765/workbenches/splitzero-tandem/continuations/20260913-accepted-followups/deligne-mixed-control/COMPLETE_CONTROL_WORK.tex#L2229) is a legitimate partial success.

The same source explicitly says that the comparison from the marked complex fibre to the local arithmetic representation had not been proved. That is not a qualification added only at the end of this audit. It was recorded early, together with missing pushforward, duality, monodromy and image-purity comparisons.

The historical standard is precise. Deligne's image-purity argument uses compact-support weight bounds and the opposite bounds supplied by duality under stated hypotheses. The theorem is not transferred by placing an auxiliary pure sheaf beside an unrelated matrix filtration. Nor should Deligne be dismissed as applicable only to isolated finite fields: the general direct-image statement has a broader scheme-theoretic setting. See [Weil II, 3.3.1 and 3.3.4–3.3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/).

**Judgment:** sensible and mathematically substantive to attempt; a real auxiliary construction resulted. Continuing related calculations without completing or decisively testing the named arithmetic comparison was a weakness in research control. No audited result supplies the full requested interior purity theorem.

## 2. The determinant branch eventually closed a stated subproblem

This branch was not a sequence of identical estimates. It developed conductor maps, attained quotients, kernel-angle comparisons and eventually an evaluated original kernel coefficient. For the retained four-cutoff operation

$$\mathcal Rf=f_{q-1}+f_q-f_{2q-1}-f_{2q},\qquad q=(k+1)^2,$$

the accepted receiving proof establishes

$$\mathcal R\log\det(I_K^*G_NI_K)=(8k-16)C_\partial q+o(kq).$$

Its domain is essential: a fixed stipulated simple quartet, the admitted original period and branch, $k\equiv1\pmod4$, $k\ge17$, and the specified conductor. It does not produce an off-critical zeta zero or assert uniformity over arbitrary moving periods. The audit reread the [CK1–19 receiving proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/1447462732b40b1474bd9a819cf79257f5326ada/workbenches/splitzero-tandem/continuations/20260922-kernel-frequency/COMBINED_KERNEL_AND_RECEIVERS.md#L148); it did not revalidate every preceding analytic dependency.

This result answers an earlier question in the programme. Describing the coefficient as still unknown would now be wrong. It also has exact downstream receivers involving relative kernel spectra and measured determinants.

However, positive energies and their determinants do not determine the complex phase-bearing arithmetic action or its signed current. The proof retains those terms, and that remaining distinction matters for RH. Earlier recoveries of the determinant from another observable were useful transport results, but did not themselves evaluate it. We sometimes presented each new recovery as if it had the strategic force of the eventual evaluation.

**Judgment:** a documented mathematical success in finite-source analysis, with potential independent value. Historical novelty and eventual RH importance are unverified. The research-management failure was allowing this productive subproblem to displace the already identified structural comparison for too long. We cannot calculate what a different allocation would have achieved.

## 3. Some exclusions settled the fate of a proposed mechanism

The terminal-adjacent calculation is a stronger outcome than a larger certificate. For each fixed complete hypothetical quartet, it evaluated the canonical allowance (the specified operator norm in the original quotient metric) throughout the original integer window and proved that its ratio to the proposed exclusion threshold tends to infinity as tensor order grows. Thus that window cannot yield the intended contradiction at sufficiently large tensor order. This excludes a particular argument, not a class of possible zeta zeros. It does not cover unbounded cutoff-to-degree ratios or every signed comparison. The [preserved complete source, TCX1–12 with TCN2 and TCN24–31](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/research-self-audit/supporting_proofs/Terminal_Adjacent_Window_Standalone.tex), accompanies this report as historical proof evidence.

Another calculation showed that a proposed common factor was generically equal to one on the specified simple-quartet branch. Later, a sharper residual estimate cancelled when substituted into the full original same-class allowance. The improvement was real for the auxiliary quantity but left the intended inequality unchanged. The audit reread the [exact SCA22–37 comparison](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/research-self-audit/supporting_proofs/SAME_CLASS_RELATION_ALLOWANCE.tex). This is exactly the kind of result that should have triggered immediate reassessment of the branch.

There were also useful positive exclusions. [FWP1–24](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/e1dc06aa68bb810cf7d8b0006942f5b036b8b765/workbenches/splitzero-tandem/continuations/20260923-full-prime-support/033/MIXED_PRIME_ENERGY_AND_BOUNDARY.tex#L663) proves strict positivity of the full original Weil form on an infinite family of mixed three-pulse tests, for every pair of distinct rational primes and all four sign choices. Its exact pulse widths, endpoint filter and full prime/Archimedean formula are retained in the cited proof. The auxiliary mixed-support observation can be negative on the same tests. The result therefore excludes these actual tests as negative Weil witnesses and identifies why the mixed observation alone is insufficient. It neither proves positivity for arbitrary tests nor yields a new zero-free height region.

**Judgment:** these results are useful because they determine what specified arguments and tests can do. They are not RH exclusions in a broader sense. We should have substituted each apparent improvement into its complete target expression sooner, instead of letting a succession of auxiliary estimates conceal the unchanged sign.

## 4. Transported collision geometry required an earlier arithmetic-membership check

The Alpöge/Fable direction was explicitly requested, and at one point made the cohomology task's sole focus. Calling it an unsolicited assistant diversion would be false. The experiment was to transport a supplied nonlinear collision construction and the programme's four marked ES states into its arithmetic conductor and test invertibility there.

The retained source credits the originating announcement to Levent Alpöge, with Akhil Mathew and Fable, and records Terence Tao's exposition. The programme's four-state extension must not be presented as extra preimages in the originating three-dimensional construction. This audit evaluates the proved transport; it does not independently certify a resolution of the Jacobian conjecture. See [ALF1–3, attribution and transport](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/39ced92952a9c807d51500783b221beb141da3b6/workbenches/splitzero-tandem/continuations/20260921-actual-xi-uniform/ALPOGE_FABLE_ROLE.tex#L5).

The work produced exact fibres, escaping branches, retained sign states, inverse maps in enlarged spaces and singular conductors in a geometric parameter family. Those are genuine constructions. But much of this work preceded substituting the actual zeta-derived unit. At the tested four marks and certified period interval, that substitution gave a strictly positive zeroth moment, so the extended conductor remained invertible at every finite cutoff. The tested neighbourhood was also outside the stipulated simple-zero-quartet locus. These conclusions exclude that candidate; they do not exclude all arithmetic quartets. The [RXT1–9 proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/39ced92952a9c807d51500783b221beb141da3b6/workbenches/splitzero-tandem/continuations/20260921-actual-xi-uniform/ACTUAL_XI_UNIFORM_CONDUCTOR.tex#L773) retains the actual multiplier and the extension's domain.

**Judgment:** reasonable to explore at the human's request; mathematically productive as geometry. Checking membership in the arithmetic problem should have come much earlier. Geometric success did not justify progress language suggesting success on RH, and the failed candidate does not invalidate all its connecting maps.

## 5. Infinitesimal vanishing acquired an exact meaning

The human repeatedly asked whether a nonzero square-zero direction could cancel a negative contribution. We found several distinct vanishing phenomena and eventually kept their maps explicit. At an observed collision, the actual operator $N$ satisfies $N^2=0$, $N\ne0$. Its isolated trace powers vanish, but the Hermitian current $i(N-N^*)$ has nonzero eigenvalues $+b,-b$, with $b>0$, and retains the ambient zero directions. In the full characteristic polynomial the original Hermitian summand still interacts with $N$ through an adjugate contraction that need not vanish. See [ISP5–18](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/173dbc6ed5a03235dbe7654f928f3692107db39b/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/INFINITESIMAL_SUPPORT_POSITIVITY_DERIVATION.md).

The abstract family becomes constant to first order after a specified change of coordinates; that change is not unitary for the original metric. Its second-order discriminant survives. Thus “the infinitesimal vanishes” was an inadequate description. The trace, deformation class, operator, norm and current answer different questions, and the proof computes their comparisons.

The dual numbers themselves, and their appearance as a first infinitesimal neighbourhood in a group algebra, are established mathematics. The human explicitly asked about the programme bridge rather than claiming to have invented dual numbers. The useful contribution was the exact representation in the programme's original operator, together with retained support and metric data. A search sufficient to establish historical priority for that full combination has not been completed.

The escaping-fibre and eight-state calculation also produced a genuine local sign flip. It did not make the complete form positive. The full eight-state form retained two negative directions on both sides of the collision; at the collision it retained a negative value $-18$ outside the null direction. The local algebra $\mathbb C[T]/(T^4)$ had an exact dual-number quotient, rather than being identical to it. See the [complete eight-state comparison](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/d5c9d198a8432e3ede468b280162a99c00e3f4f7/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/EIGHT_STATE_HEAT_COMPARISON.md).

**Judgment:** a useful construction and a useful rejection of an overstrong inference. It identifies what a further positivity mechanism must actually affect. It does not show that all infinitesimal or holonomy approaches are impossible, and it does not validate the original global positivity guess.

## 6. Prismatic and boundary constructions supplied new objects to investigate

The prismatic comparison was worth testing because it asked a concrete compatibility question. A chosen monoid Frobenius did not descend through the proposed addition relations; an alternative lift did, but explicitly used the selected addition. This is not recovery of addition from multiplication alone. The definitions of prisms already include a ring and its addition. [Bhatt–Scholze, Definition 1.1 and crystalline examples](https://arxiv.org/abs/1905.08229v4), and [Bhatt–Lurie, Absolute Prismatic Cohomology](https://arxiv.org/abs/2201.06120v1), supply the actual framework.

Specific branch and collision modules then produced mixed differentials, torsion, divided-Frobenius classes and exact failure-of-comparison terms. The latest local collision calculation found an order-nine cokernel for a compatible differential and a nonzero Frobenius defect in a different cotangent map. Its tensor formulas were proved for every degree, while the specified Frobenius remained nilpotent. That last fact limits using this very representation as a pure arithmetic Frobenius; it does not erase its local structure. Review also corrected an overbroad implication: a non-split coefficient extension can have zero image in the cohomology of a contractible support complex. The latest collision addition was local at the audit cutoff and is not represented here as a verified public publication.

There is a public all-prime boundary result closer to the requested cohomological direction. Here $\Omega=\{0,1\}^{\{\infty\}\cup\{\text{rational primes}\}}$, $LC$ denotes locally constant functions, and for an $r$-tuple of binary labels $m_v=\sum_{j=1}^r\epsilon_{v,j}$. For the actual boundary module $V_r=LC(\Omega^r,\mathbb C)$, with the action specified in the source, it calculates

$$H_j(\mathbb Q^\times,V_r)=LC(Z_r,\mathbb C)\otimes\bigwedge^j\mathbb C^{(\mathrm{primes})},\qquad Z_r=\{m_p=m_\infty\text{ for every }p\}.$$

The surviving count-$m$ component retains the character $|a|^m$. Mixed balanced tensors survive that a tensor power of the two-endpoint quotient would lose. The [complete BW1–24 proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/e1dc06aa68bb810cf7d8b0006942f5b036b8b765/workbenches/splitzero-tandem/continuations/20260923-retained-source-readers/all-prime-boundary-weights/ROOT_BOUNDARY_WEIGHT_HOMOLOGY.tex) provides a specific reason to form tensors before that quotient.

These are strong examples of the human's instruction, “Every obstruction is a definition,” being used constructively. A failed identification led to an explicitly studied object and map. It did not automatically produce RH. The subsequent GBC1–20 calculation, completed and read locally but not verified public at the cutoff, does evaluate a boundary-to-interior map: it constructs the connecting representative, proves its image is zero in the indicated interior theta quotient, and retains it in the joint source kernel. The unfinished work is the relevant interior weight and pairing construction, not every boundary comparison.

**Judgment:** legitimate structural successes and plausible research directions, even without demonstrated historical precedence. We should neither promise an RH consequence nor dismiss the constructions because that consequence is absent.

## 7. Trace and zero detectors became more precise

The programme built full matrix and translated-test criteria that detect any possible off-critical zero. It showed that imposing finitely many endpoint conditions does not remove the off-critical negative directions. It also derived test families whose transforms avoid every possible off-critical zero. These are global detection statements, not finite scans of known zeros. One complete example is the [fixed primitive and translation criterion](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/e1dc06aa68bb810cf7d8b0006942f5b036b8b765/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/UNIVERSAL_PRIMITIVE_TRANSLATION_CRITERION.md), with its retained original-function comparisons.

Their unresolved requirement is still global: positivity of every relevant finite matrix, or the appropriate translated correlation bound at every separation. A positive diagonal or a positive interval does not establish that requirement. A spectral realization and explicit formula are not new substitutes for the missing sign merely because they are written in new coordinates: [Meyer](https://arxiv.org/abs/math/0412277v3) and [Connes–Consani–Marcolli](https://arxiv.org/abs/math/0703392v1) provide historical context for precisely this distinction.

The later endpoint work also sharpened the distinction between a nonzero flat germ and a square-zero element. A local follow-up proof reports that all fixed-height time jets vanish while the complete trace grows positively, with dominant contributions moving to heights of order $1/t$. Its derivation and review were recorded, but that successor was not a verified public edition at the audit cutoff and its full analytic chain was not independently re-proved in this retrospective. We record it at that status, rather than quietly upgrading a local result to an externally validated theorem. Even the claimed result concerns this family, not every translated pairing.

**Judgment:** worthwhile diagnostic and comparison tools. They make a proposed mechanism testable on all zeros and can reveal why a local gain is insufficient. Their existence is not evidence that the remaining sign inequality is now easy or has been proved.

The Hurwitz-flow experiment provides another useful control. The programme related its separated sheet to a non-Eulerian analytic deformation and prime operators. Additional certified transverse crossings away from the two proposed Euler parameters refuted an overinterpretation of the first sixty observed trajectories. A negative witness for the separated function $\zeta-1$ is not a negative witness for the original $\zeta$. The constant-function sector retained the original zeta singularity, while an inverse was constructed on the specified complement. This is information about the actual operator, not control of the real parts of all original zeros.

# Where our research choices were less satisfactory

## Definitions were known but not consistently used

The root task's first final response already knew $e\ne\tau$ and the enlarged spectrum. This corrects our own later blanket confessions as well as a possible retrospective caricature. The failure was to let a scalar or Boolean observation stand in for the full lattice in subsequent work, and to rediscover established programme facts instead of propagating them through the actual maps.

In the support task, an initial answer about invertible zero discussed localization before reading the cited singlet algebra, where $e$ already is the multiplicative identity. The relevant identity depends on the object: $e$ acts as the identity on $eM$, while the full arithmetic object has its different unit. The eventual exact maps resolved the issue; the initial answer was avoidable.

An extra prime point also does not determine a numerical Euler factor without a norm, action and trace. We sometimes moved too quickly from retaining the support labels to language suggesting that an intrinsic arithmetic cohomology or full new Weil theory had been constructed. A coefficient lift of a classical formula and an arithmetic trace derived from the original base are meaningful but different accomplishments. The report credits the exact proved comparison, not the stronger description.

## Finite extensions continued without a global stopping rule

The bounded-range work deserves a precise criticism. Some estimates were proofs on whole finite intervals, with all prime powers and analytic remainders retained; they were not merely numerical sampling. They can validate a formula and settle local questions. Finite algebra can also prove an unrestricted structural theorem.

The strategic problem was extending a fixed-test inequality from a first-prime interval through $\log256$ while the same all-translation bound remained unresolved and no reduction of the global problem to that interval was supplied. This was a narrow success with declining value for the chosen objective. The [finite extension itself, FP1–13 and following window proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/e1dc06aa68bb810cf7d8b0006942f5b036b8b765/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/FINITE_PRIME_WINDOW_EXTENSION.md), explicitly states its range. After the human challenged the expenditure, the task reported a Laplace-transform pole in the absolute prime-sum majorant that ruled out obtaining the desired uniform estimate from that particular majorant. Investigating this mechanism earlier would have been a better decision than treating a longer certified range as the natural next step.

We cannot conclude that no bounded computation can contribute to RH, nor that every estimate in the programme was a distraction. We can conclude that these extensions did not provide their missing global implication. We also found no evidence sufficient to claim that the programme had excluded a named external researcher's complete RH proposal. Most exclusions concern specified internal constructions and test families.

## Completion was neither harmless everywhere nor an assumed proof

The human's insistence on restoring original factors exposed real omissions. Corrected calculations retain the pole, trivial zeros, Gamma terms, exceptional local modules and support data. For the actual Gaussian-translated test, the positive trivial-zero summands grow with a positive quadratic exponential; the raw full scalar sum diverges for every positive test-heat time. A common finite cutoff with the Gamma compensation is necessary. The [complete comparison, OZG1–27](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/e1dc06aa68bb810cf7d8b0006942f5b036b8b765/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/ORIGINAL_ZETA_GAUSSIAN_TRANSLATION_RECONSTRUCTION.md), retains the original entries. The raw full-divisor pairing can also fail to be Hermitian while its corrected Weil receiver is Hermitian.

These are useful domain and comparison results. Some of the work was also repair of problems we created by insufficiently justified substitutions. We must not count every repaired shortcut as an independent advance toward RH.

The stronger suggestion that using completion makes an RH proof impossible was not established. The explicit multiplier has a nonzero holomorphic inverse inside the critical strip and preserves the nontrivial zero divisor there. What needed checking was the global return, the additional geometry and the trace's domain. A proved invertible change of representation remains legitimate; dropping its exceptional data or transferring an operation outside its proved image does not.

There was also a specific assistant error in the local explanation: the abstract modules $\mathcal O/h\mathcal O$ and $h\mathcal O/h^2\mathcal O$ do not by themselves demonstrate a loss, since multiplication by $h$ identifies them in the stated local setting. The embedded lattices, section and meromorphic comparison carry the additional data. The [corrected full return, ZTC4–10, ZTC16a–17a and ZTC20–21](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/acd7016b8232a56f31ae3e69fb800571e8789080/workbenches/splitzero-tandem/continuations/20260923-retained-source-readers/original-zeta-full-boundary/CC_WEIL_BOUNDARY_READER.tex) supplies the actual maps. Repackaging this correction repeatedly should not count as several independent advances.

## Literature use and publication fidelity were uneven

There are genuine examples of literature changing a calculation: Deligne's auxiliary family, the Szegő-based determinant work, Meyer's theta-image topology, and the prismatic compatibility test. Connes–Consani's prime-orbit theorem also gave an exact class-field comparison: for the specified finite abelian covers and unramified primes, monodromy around an orbit of length $\log p$ is arithmetic Frobenius. It does not state that arbitrary nontrivial holonomy forces a sign for the whole Weil pairing. See [Theorem 3.1](https://arxiv.org/abs/2501.06560v1).

The GCT recollection also had a real source. Mulmuley's 2007 Section 16 discusses desired analogues of finite-field RH for specified nonstandard quantum groups and canonical-basis positivity. We checked the original TeX. It does not make the programme's dual-number construction such a formulation, and a statement about what could not be formulated in 2007 is not proof that no subsequent development exists. See [Mulmuley, Section 16](https://arxiv.org/abs/0709.0748v1).

Against those successes, the records show source-routing claims stronger than actual reading, an incorrect Deligne edition in a requested delivery, incomplete human citations, repeated reviews and excessive rebuilding. Inclusion and checksum tests verified the files chosen; they could not prove that the correct requested source had been chosen. Later source ledgers improve the situation but do not retroactively establish earlier reading.

The citation failure was concrete. The retained 765-page intake had no cite-family commands across 67 TeX files, and its five bibliography entries pointed to internal programme documents. Absence of those commands alone does not exclude manual attribution; the content audit and the recorded admission supply the broader criticism. A separate provenance companion did not repair the paper itself. Another bundle required twelve missing dependency proof bodies to be restored.

The source-use record also contains a particularly useful success: Meyer's original TeX supplied a closed-image result in the specified rapidly decreasing function topology, removing the programme kernel previously labelled E5. It did not prove closedness in an arbitrary Hilbert completion. That topological distinction was a real gap closed by reading, not another bibliography entry. Meyer's separate source also warns that the spectral description does not settle a possible quasi-nilpotent part of the full representation; a list of spectral jets is therefore not automatically the whole object. See [the spectral interpretation](https://arxiv.org/abs/math/0412277v3) and [the earlier representation discussion](https://arxiv.org/abs/math/0311468v3).

Fresh source checking during this audit found a further error in our BCM crosswalk. Ha–Paugam's ideal semigroup quotients by profinite units, whereas our transcription had global units. At a fixed nontrivial ray modulus, the trivial-character sum also retains omitted Euler factors and is not simply the full Dedekind zeta function. The satellite has been corrected locally; a local edit is not a public repair receipt. The human's motivating recollection of Bost–Connes, Dedekind zeta and character-twisted series was substantive. The error was in our transcription and specialization, not in that source lead. See [Ha–Paugam, the Dedekind and character subsections](https://arxiv.org/abs/math/0507101v1).

The early numerical record likewise withdrew “fully certified” after finding an incomplete infinite-tail justification, and subsequently corrected a missing factor in its repair. This audit does not recertify those old enclosures. A successful finite calculation cannot make an unproved tail disappear. The related fluid-singularity transports retained useful local data but did not identify a transported singularity with an off-critical zero of the original zeta. The relevant heat-flow comparison is to the actual family in [Rodgers–Tao](https://arxiv.org/abs/1801.05914v5), whose nonnegativity theorem for the de Bruijn–Newman constant does not supply the missing opposite bound for RH.

Publication made proofs available and preserved reproducibility. That was valuable. But page counts, figure counts, checks passed and bytes verified frequently became the lead evidence of progress. These measures answer production questions. They establish neither historical novelty nor the sign of an infinite arithmetic form. Publication was authorized by the human; proportionate batching remained our responsibility.

# The human investigator's role

The human contributed the unusual starting construction, source archives, the Deligne and prismatic directions, links to independent attempts, and repeated demands to calculate exact maps. Several interventions had demonstrable benefits: omitted support faces were restored; the correct source editions were pursued; an arbitrary scale choice was challenged; exceptional divisor and trace terms were reconstructed; and a failed inference was retained as an object to study rather than quietly discarded.

The human also asked whether apparent findings were trivial or genuinely new, explicitly called many suggestions guesses, and sometimes requested that speculative branches be logged for later while the principal calculation continued. It would be inaccurate to attribute all dispersal of effort to an instruction to pursue every idea simultaneously. The request for this audit, including criticism of human decisions, is itself a useful correction to the programme's incentives.

Some proposed implications went beyond what their premises supported. Coincident appearances of $1/4$, tetrahedral symmetry, an extra prime, invertibility relative to a subobject's unit, or nontrivial holonomy did not by themselves yield a positive full Weil value or an RH counterexample. Assertions about earlier resolutions of other major conjectures were not independently verified in this audit and cannot serve as evidence that this programme is likely to succeed. The point of testing a heuristic is to find its actual consequence, which can be valuable even when the original hoped-for conclusion fails.

The large flow of attachments and suggestions made coordination difficult. The assistants accepted responsibility for that coordination. We should not blame the human for our unsupported claims, incomplete source use, or failure to keep a known central gap visible. Nor can the logs establish that a different style of prompting would have produced a resolution. The responsibility we can assess is specific: when we accepted a research direction, did the next calculation actually advance or decisively test it?

# What we will take forward

1. **Name the mathematical change made by a turn.** Record the original object, exact map or assertion, proof location, source theorem used, and the resulting change to the question. “Another paper finished” is not that change.
2. **Keep the receiving comparison central.** Before invoking a large theory, verify its hypotheses on the actual arithmetic object. An auxiliary example is a result, but must not inherit the target's significance by association.
3. **Treat a new criterion as a criterion.** A detector that reaches every possible zero is useful. It does not prove its own positivity. State the remaining quantity without assuming its sign.
4. **Use finite work for a stated purpose.** Validate a formula, test a counterexample, close a local gap, or provide a finite reduction with a proved remainder. Stop automatic range expansion when the global mechanism is unchanged.
5. **Preserve and study defects.** When a map fails, retain its kernel, cokernel, extension, topology or compatibility defect and calculate the strongest established connection. Do not convert one failed identification into a claim of universal irrelevance.
6. **Propagate corrections, not only warnings.** Repair affected formulas and receiving arguments; preserve prior editions for provenance; distinguish an audit finding from a remotely published repair.
7. **Make literature use auditable.** Identify the source version, actual reading coverage and receiving calculation. An index hit, a citation or a downloaded archive is not a theorem applied.
8. **Separate validity, novelty and strategic value.** Each deserves its own evidence. A correct result can be standard; a new direction can be promising without an RH consequence; a familiar tool can close an important gap.
9. **Batch production around mathematical milestones.** Maintain reproducible proofs and accessible files, but avoid rebuilding a large collection after every adjacent lemma. Checks and reviews must state their scope; multiple AI reviews are not external peer review.

The most defensible next research focus is the actual interior image, its boundary extensions, its arithmetic action and the full pairing, using the support and tensor data already constructed. Another analytic estimate is justified when it enters that specified comparison or tests a distinct mechanism. This audit does not assert that this is the eventual successful route. It makes the choice assessable while that outcome is unknown.

# Evidence and assessment limits

The accompanying evidence register supplies the audit's episode-level source locators and precise public proof links. Some entries support a conclusion through a complete receiving proof; some record a historical assertion and its later correction. These levels are marked. No log quote alone is treated as certification of a theorem.

The logs show substantial computational use, but this report does not convert it into an unsupported dollar figure. As a bounded example, the support/heat task's frozen prefix contains 2,004 distinct per-response usage records: 289,834,711 input tokens, including 274,638,592 cached input, and 1,858,973 output tokens, including 461,852 reasoning-output tokens. The included categories must not be added again. These are not unique text, total programme use, or a verified bill. They give evidence that efficiency matters, not a price calculation.

Our final assessment is therefore deliberately uneven: **real mathematical output, useful constructions and corrections, uncertain novelty and eventual importance, and identifiable failures of focus and proportionality.** The work merits neither automatic celebration nor dismissal as worthless. The record gives concrete reasons to preserve some results, repair others, and change how the next research decision is made.
