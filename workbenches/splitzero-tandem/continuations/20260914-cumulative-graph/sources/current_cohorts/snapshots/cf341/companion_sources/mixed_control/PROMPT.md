# Continue the actual Deligne programme: mixed support and the singular boundary

Continue the original Split-Zero research programme over the absolute tau base. Your Marked Product / Four Endpoint continuation contains useful mathematics. This handoff preserves it, audits its exact scope, and adds calculations that let you work on the next geometric and analytic controls.

Read COMPLETE_CONTROL_WORK.tex and DELIGNE_USAGE_OVERVIEW.md before continuing. The TeX contains complete proof bodies, including the earlier AW source and your original marked-product note, with explicit reuse attribution. Read the new boundary calculation in full, especially the degree-dependent chain connection, the order-two polar term, its complete period determinant, and the actual finite-field boundary sheaf. Read the mixed coefficient-face attachment and the relative-extension calculation too. The point is to implement the intervening Deligne machinery on our objects. The final growing-family RH inequality is a downstream target; it is not a substitute for those calculations.

## Preserve the actual objects

Retain the original pointed/preaddition base, G(R), the distinct tau and supported zero e, and every original outer source label (W,S). Retain independent coefficient masks A, including the empty coefficient mask at a present outer label. Keep the slot-local leg refinement and its explicit maps separate from the outer leg index. A face inclusion A to B inserts supported zeros in the new coordinates and changes its target label. Do not take the colimit over the entire mask poset: its terminal full face would erase the retained labels.

The original arithmetic packet is h with every selected zero at its full order. Keep E_h, the entire Taylor unit upsilon_h = j_h(g/h), its inverse, the original theta spaces, Fourier sign, g = 2 xi, the seed phi_*, the Euler inverses on their proved domains, and every original source norm. The MCF module first records the original off-critical U; its final enlargement map explicitly admits the full critical-strip packet family. Use the appropriate inclusion when your h contains critical-line zeros. Do not silently treat an arbitrary polynomial fixture as an actual zero packet.

Keep the complete external family

\[
\mathcal D=\sum_i(u\partial_{s_i}+h(s_i)-t_i)\,ds_i\wedge,
\qquad
\mathcal H^k/(u,\mathbf t)\mathcal H^k=E_h^{\otimes k},
\]

and the original source map containing upsilon_h to the full tensor power. Keep the weighted cyclic inclusion eta, its quotient, the parameter defect

\[
[\chi(S)P(S)]
=\sum_i[t_iQ_i-u\partial_{s_i}Q_i],
\]

and the transverse connection map into the quotient by eta. A source section is complex-linear. The supplied free-resolution chain map gives its precise polynomial-module comparison; do not tensor a non-polynomial-linear section as though it were polynomial-linear.

## Start with the boundary calculation already completed here

Put f_t = Phi_h - ts. In the original monomial basis, divide

\[
f_t(s)s^b=(h(s)-t)q_b(s,t)+r_b(s,t).
\]

The new proof defines C_h by the remainder columns r_b and B_h by the derivative columns q_b'. It proves the exact top connection

\[
\nabla_u=\partial_u-\frac{\sum_i C_{h,i}(t_i)}{u^2}
                         +\frac{\sum_i B_{h,i}(t_i)}u,
\qquad \operatorname{Tr}B_h=d/2.
\]

It also gives the degree-j chain operator with the term (k-j)/u and proves flatness with the original t-connections. At t = 0, on the full rho-primary algebra,

\[
C_h(0)=\Phi_h(\rho)I,\qquad A_h=\rho I+N_\rho.
\]

The entire nilpotent jet still occurs in A_h. For tensor tuples, retain each labelled summand when critical-value sums coincide. The proof supplies the exact determinant of the ordered period map, including all Gamma factors, root-of-unity determinants, powers of u, and contour phases. It also supplies the exact positive comparison endomorphism between the period Gram and the original theta-source Gram. Neither form is replaced by the other.

There is now a genuine sheaf-level step on the finite-field branch. With the stated good coefficient specialization and u nonzero, Weil II 3.7.3 makes the rank-d^k, weight-k compact-support family lisse. On each fixed-t punctured u-curve, the supplied calculation constructs

\[
0\longrightarrow j_!\mathcal F
\longrightarrow j_*\mathcal F
\longrightarrow i_*(V^I)\longrightarrow0
\]

and applies 1.8.4 and 1.8.8 to that actual representation. Thus the invariant boundary stalk is mixed of weights at most k. Its actual inertia, graded multiplicities, and comparison with the original marked coefficient fibre still need calculation. Continue from this proved boundary result.

## The next calculation: compute this family's local boundary data

Work first on the one-factor original family at u = 0 with t retained, then at its marked t = 0 fibre. Calculate its local extension using the full connection above. Determine the exponential blocks, ramification and local monodromy; calculate the Stokes maps where the complex realization requires them. Use the retained critical values and multiplicities, including collisions, rather than imposing simple critical points or distinct critical-value sums. The scalar leading u-pole does not remove the primary nilpotent in the t-connection.

Start with explicit original primary blocks and their coupling, proving every coordinate map and its inverse when you use local coordinates. Keep the critical-value exponential factors and their exact equal-modulus rays. Do not identify B_h alone with a residue determining all local monodromy: the order-two C_h term is present. On the finite-field realization, construct the compactified phase and compute its actual inertia and monodromy filtration at u = 0. Use the relevant stationary-phase and ramification results with their complete hypotheses and prove their application to this phase.

Carry the calculation through the ordered external product. Prove the induced maps on the full tensor fibre and then on eta and its retained quotient. Include the transverse map and cyclic parameter defect above. Show how the calculated boundary maps act on every independent mixed face and on the receiving supported zeros. The original theta source must remain connected by the explicit chain maps and their nonzero source homotopies.

## Build mixed-extension, tensor and dual control on those maps

Use Weil II 1.6–1.8 at its actual types. The MW module already supplies the centered nilpotent filtration on the original spectral jets, its tensor compatibility with all coefficients, its dual signs, and an exact reconstruction of the original arithmetic dilation from additional Tate-scaling matrices. The accompanying relative-extension proof supplies the induced subobject and quotient filtrations of the specified length-two jet extension and its exact Tate map. This local calculation does not assert that an actual double zeta zero exists.

Use these computations as input. Determine the actual relative filtration for the boundary representation just constructed. Do not identify its inertia logarithm with the spectral multiplication N_rho without constructing the intertwiner. The centered spectral filtration by itself need not be strict on extensions; the attached example calculates the defect and repairs the filtration on its subobject and quotient explicitly. Keep those shifted maps when enlarging to general mixed extensions.

Construct and calculate the localization sequence or triangle, its connecting maps, and the dual comparison on the original mixed diagram. For proper W, retain the actual (V/W)^A kernel and the surviving Euler/dilation primitive classes. For duality, preserve the reversed support arrows, original bottom fibres, tensor-adjoint signs, and source pairings. The previously completed full-support dual and theta-scaling cocycle remain dependencies, not work to discard and restart.

After these local calculations, use the actual compact-support pushforward and image machinery in Weil II 3.3, and its mixed/pure-complex formulation in 6.1–6.2. State the realized functor and calculate its image, kernel and cone. Include the constituent control used in 1.3–1.5 and the boundary/vanishing-cycle input used in 3.1–3.2 where the map reaches them. Merely naming the six operations supplies no control; an explicit finite calculation through the available maps does.

## Feed the calculated terms into the same arithmetic estimate

Retain the common source P_(2q), the same J_N and original relation multiplication B_N, and the four endpoint signs. Here q means degree chi; use a distinct symbol for a finite-field cardinality when both appear.

The SP proof reproduces the earlier AW common-source identity and spectral control, and adds an explicit overlap refinement:

\[
F'(x)=\operatorname{Tr}\bigl(T_x(\mathcal R_x-\mathcal P_x)\bigr),
\qquad
T_x=M_x^{-1}\dot M.
\]

The two positive operators have rank q+1 and trace 2q, with eigenvalues 1, 2 of multiplicity q-1, and 1. Their scalar evaluation density includes the exact factor M_x^{-1}. Their common range and projection overlap give

\[
|\Delta_{h,k}|
\leq\frac12\int_0^1
\bigl(\lambda_{\max}T_x-\lambda_{\min}T_x\bigr)
\|\mathcal R_x-\mathcal P_x\|_1\,dx
\leq(2q-1)\log\frac{r_{\max}}{r_{\min}},
\]

where r_min and r_max belong to the original endomorphism
(M_Gamma)^(-1) M_ar. Use the stronger overlap integral as well as the last bound. Their proofs preserve the original masses and every relation cross-pairing.

The spectra and the final (2q−1) log condition-number estimate already occur in AW7 and AW14 of the accompanying full relation-window spectral-transport proof. On the identical original polynomial source, with x=t and frequency y=u_AW, its operators satisfy R_SP=U_AW, P_SP=W_AW and T_SP=C_AW; this follows directly from their projector formulas and Q_(q−1)=0. The reader includes this exact correspondence. AW's separate source isometry T is retained with its own type. Reuse AW13's stronger bound with the full ordered relative spectrum, AW11's commutator expression and AW12's observation defect. SP8/SP10 add the explicit projection-overlap and common-range refinement. Compare these evaluated bounds on the same original Grams; neither refinement is asserted to dominate the other in every case.

Calculate what the new boundary and mixed-extension data contribute to these exact operators, their overlap, and the cyclic restriction of the period comparison. Determine the dependence on h and k from the original arithmetic moments and source formulas. A finite constant is useful progress but must retain its calculated dependence. A full-period determinant alone does not determine singular values on the rectangular cyclic image. Compute that image and its correction.

Continue a calculable local case to completion and then extend the proved construction. Do not replace the missing estimate by a hypothesis saying that the estimate holds. If a proposed map fails, give its actual defect and build the strongest exact corrected map, extension, or comparison available. Such a calculation does not close the programme.

## Return complete mathematics and keep the work connected

Give complete definitions, domains, codomains, constants, signs and proofs in cumulative LaTeX, with an updated readable PDF and exact source handoff. Update every earlier statement affected by a corrected map. Clearly identify reused results and newly completed calculations.

The repository is https://github.com/KokunoYumeto/zeta-function-research-reader . Check its current mathematical source and incoming work before claiming an item new. The final live Git-remote check for this handoff returned main baef5c29f2bc36101eb74e7fe95c2d8c9e44bb8c and PR29 head 55f656ed738b8a33a777c58ff45005c0680afc20. Refresh those references if additional work has arrived; a frozen reader description is not the current mathematical source.

PR29 is now merged. Read its complete workbenches/tau-arithmetic-metric-transfer/RESEARCH_NOTE.md and workbenches/tau-residue-rigidity/ARITHMETIC_VARIATION.md and ADAPTIVE_VARIATION.md. This handoff audit read all three. Reuse their canonical secants, relation-valued metric derivatives, adaptive slope enclosures and convergent signed trace-power certificates. Those certificates combine the four endpoint signs and cancel the common logarithmic scale before bounding the remainder. They provide existing finite calculations to sharpen with the new common-source projection-overlap bound; do not present their reconstruction as a new result. Retain their original arithmetic Grams, degree ranges and residue-pairing maps when applying the boundary calculation.

The local Zeta, counterfactual-integration, and transcript-audit tasks have been notified. Continue with their explicit maps and new calculations. The counterfactual owner is integrating the coefficient-face diagram and the actual Weil II dyadic bootstrap separately. Report the next established local control and the calculations it enables. Do not jump from an unfinished boundary comparison to either an RH conclusion or a claim that the F1/tau programme has failed.
