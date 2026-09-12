# Historical Split-Zero transcript extraction — 12 September 2026

This continuation made progress: it recovered a complete mathematical response from the mounted SSD, preserved it with exact source locators, proved its full-jet comparison to the current arithmetic packet, and computed the generator-compatible quotient kernel. The original 40-plus-file/deep-source objective remains active; the precise remaining source coverage is recorded below.

## Source-first method and coverage

The lane first read `logbook/SPLIT_ZERO_DEEP_GOAL_2026-09-09.md`, `logbook/split_zero_inventory_20260909.md`, `work/transcript_algebra_lane_report_20260909.md`, `work/transcript_gct_lane_report_20260909.md`, and `work/split_zero_main_source_ledger.md`. It reused `work/split_zero_ssd_candidate_paths_20260909.txt` rather than rebuilding a corpus index. Bounded `rg` title/content searches then selected the Globalization Semiring Analysis and Mathematical Functor Construction transcript families. An independent Hurwitz/conormal lane examined the later proof block while this lane examined the packet ghost.

The mounted `F:` SSD is accessible. The new `sources/historical/transcript_family_inventory.json` verifies **43 existing transcript paths with 25 distinct SHA256 values** in the two selected families, including SSD originals, raw-export mirrors and Chatnotes copies. Those are file counts, not complete reads or theorem counts. Each record carries path, size, mtime, hash, line count and actual read status. All 43 candidate paths were accessible. This is not an exhaustive inventory of all SSD mathematics or all other transcript-title families.

The main newly recovered source is:

- Original: `corpus:SSD-downloads\ChatGPT-Globalization Semiring Analysis (6).md`.
- Exact mirror: `corpus:SSD-transcript-mirror\raw\F_dowloads\ChatGPT-Globalization Semiring Analysis (6).md`.
- Both SHA256: `f23aec625d03d0e21a2354fea6b9993cc0b243d67365af6656573ec588f814ed`.
- Original size: 549096 bytes; 16656 lines.
- Conversation title: **Globalization Semiring Analysis**; conversation id `6a334647-b218-83eb-a30f-58146e9138a2`.
- Response heading: original line15487; timestamp line15488, `6/24/2026, 11:13:04 AM` as exported. No timezone or message UUID is inferred.
- Complete final mathematical response body: original lines15694–16651, beginning “Cubic mixed support, ghost completion, and the critical-line obstruction.” Its title and all mathematical sections were read. The preceding draft reasoning and unrelated turns are outside the extraction.
- Retained source: `sources/historical/globalization_20260624_packet_ghost_response.md`, SHA256 `c30fe59266a56d7b677eb1f26ac641d00d1cd024cb69ef60c52fdb89df6a9454`.
- Exact ledger: `sources/historical/packet_ghost_source_ledger.json`.

All `sources/...` paths in this report are relative to the standalone package `output/split_zero_rh_tandem_2026-09-12`. Original absolute paths remain in the machine ledger.

## What the original source proves

At original lines15724–16077 the response constructs, for a root orbit O of common multiplicity m, the space `C^m tensor ell^2(O)` and the complex-linear label permutations `C e_rho=e_bar(rho)` and `S e_rho=e_(1-rho)`. It defines `Gamma=C−S`, `R=CS` and `P_-=(I−R)/2`, and proves

\[
\Gamma^*=\Gamma,\qquad\Gamma^2=4P_-,\qquad
\Gamma e_\rho=0\iff\Re\rho=\tfrac12.
\]

For an off-axis nonreal quartet the four joint `(C,S)` characters are `(1,1),(1,−1),(−1,1),(−1,−1)`, so `Gamma` has eigenvalues `−2,0,2` with multiplicities `m,2m,m`. Therefore `rank P_-=2m` and `Tr Gamma*Gamma=8m`. The original proof explicitly orders the roots `(rho,bar rho,1−rho,1−bar rho)`; that order is retained in the new proof and checks.

The source also proves that the surjection

\[
q:\mathbb C[C_2\times C_2]\to\mathbb C[u]/(u^2-1),
\quad c\mapsto u,\quad\sigma\mapsto u
\]

has exact kernel `(c−sigma) C[W]=C(c−sigma) directsum C(1−c sigma)`. Its represented image is `P_-L`, and quotienting by that image forces the two label permutations to agree. Original lines16079–16126 distinguish its supported zero from absent tau.

Original lines16128–16309 prove the general projected-Lie identity

\[
J_P(x,y,z)=-P\bigl([x,Q[y,z]]+[y,Q[z,x]]+[z,Q[x,y]]\bigr),\quad Q=I-P,
\]

and the associative identity

\[
(x\star y)\star z-x\star(y\star z)
=P\bigl(xQ(yz)-Q(xy)z\bigr),\quad x\star y=P(xy).
\]

They follow by inserting `P=I−Q` and retaining the ambient Jacobi/associativity identities. The entire proofs are preserved verbatim in the selected user-owned source response; no arithmetic positivity estimate follows from these general identities alone.

Original lines16366–16452 prove the weighted packet count `one quarter sum a_O ||Gamma_O||_HS^2=2 sum_off a_O m_O` for positive weights and finite nonreal orbits. Later sections16454–16651 explicitly assume a coercive form or determinant convergence. Those later endpoint claims are retained as historical context and are **not imported as achieved theorems or substituted for missing arithmetic work**. The new paper contributes the exact generator-compatible map below instead.

## Complete new proof and the exact arithmetic relation

The full standalone proof is `tex/historical_packet_ghost.tex`, with labelled propositions/theorems. It constructs

\[
T:\mathbb C[s]/h(s)\xrightarrow{\sim}
L_Z=\bigoplus_{\rho\in Z}\mathbb C[t_\rho]/t_\rho^{m_\rho},
\quad [f]\mapsto\sum_{k<m_\rho}f^{(k)}(\rho)t_\rho^k/k!.
\]

The inverse uses the explicit Bezout–Taylor idempotents `E_rho=[a_rho h_rho]`, where `h_rho=h/(s−rho)^m` and `a_rho` is the Taylor truncation of `1/h_rho`; it maps `t_rho^k` to `E_rho(s−rho)^k`. In these coordinates the original generator is **exactly** `A=A_ss+N`, with `N e_(rho,k)=e_(rho,k+1)` up to the last nilpotent column.

The historical complex-linear permutations are denoted `C0,S0`. Natural coefficient conjugation is conjugate-linear `C=C0 K`, where `K` conjugates coefficients in the specified jet basis; natural polynomial reflection is complex-linear `S=S0 H`, where `H e_(rho,k)=(−1)^k e_(rho,k)`. Consequently `C0=C K` and `S0=S H`, with every source and target named. In particular `S A S=I−A`, while `H N=−N H`. This is the exact correction to equating a label permutation with arithmetic conjugation.

The new substantive theorem is

\[
\boxed{P_-L_Z+A(P_-L_Z)=L_{\mathrm{off}}.}
\]

Here `L_off` is the direct sum of **all** off-axis local algebras, with every original multiplicity. On each off-axis orbit the displayed sum is direct. To prove it, write

\[
A=\tfrac12 I+B+iY+N,\quad
B e_{\rho,k}=(\Re\rho-\tfrac12)e_{\rho,k},\quad
Y e_{\rho,k}=\Im\rho\,e_{\rho,k}.
\]

The involution `R=C0 S0` anticommutes with `B` and commutes with `Y,N`. Thus `P_+ A v=Bv` for `v in P_-L`. On each off-axis orbit, every diagonal entry of `B` is nonzero, and `B:P_-L→P_+L` is an isomorphism. For an arbitrary `w=w_-+w_+`, take `v=B^(-1)w_+`; then `w−Av` is in `P_-L`. If `Av` already lies in `P_-L`, `Bv=0` forces `v=0`. This proves both span and directness without omitting the nilpotent operator.

It follows that the largest quotient retaining the arithmetic generator and forcing `C0=S0` is exactly

\[
E_h\twoheadrightarrow E_{h_{\mathrm{crit}}},\qquad
\ker=(h_{\mathrm{crit}})/(h),
\]

where `h_crit` is the product of all original critical-root factors with original exponents. The proof applies even to arbitrary linear intertwining targets: their kernel must be A-invariant and contain `P_-L`, hence it must contain `L_off`. This describes exactly the arithmetic data removed by imposing the historical ghost quotient. It proves no absence of that data in the original cohomology.

The reference Hermitian weight also has exact components

\[
W_{\mathrm{ref}}=2B+N+N^*,\qquad
\frac{W_{\mathrm{ref}}-R W_{\mathrm{ref}}R}{2}=2B=c_{-+}/2,\qquad
\frac{W_{\mathrm{ref}}+R W_{\mathrm{ref}}R}{2}=N+N^*.
\]

For an actual theta-source matrix `G_E`, the CRT transport is `G_L=(T^(-1))* G_E T^(-1)`, and the exact arithmetic relation is

\[
W_L=(T^{-1})^*W_E T^{-1}
=G_LW_{\mathrm{ref}}+[A_L^*,G_L].
\]

Both metric-commutator and nilpotent contributions remain present. The manuscript gives the full expansion proving this equality.

Finally the quotient induces an endomorphism map on the exact descent algebra

\[
\mathcal D=\{X\in\operatorname{End}_{\mathbb C}L_Z:X(L_{\mathrm{off}})\subseteq L_{\mathrm{off}}\},
\quad\mathcal D\twoheadrightarrow\operatorname{End}_{\mathbb C}L_{\mathrm{crit}},
\quad\ker=\operatorname{Hom}_{\mathbb C}(L_Z,L_{\mathrm{off}}).
\]

Every target endomorphism lifts by acting on the critical direct summand and vanishing on the off-axis summand. Applying `G` gives the exact semiring morphism sending `Gamma^bullet` to supported `e`, while `tau` remains `tau`; the restricted descent domain prevents an invalid quotient of the entire endomorphism ring.

## Verification and review

`work/check_historical_packet_ghost_20260912.py` and its standalone copy `scripts/check_historical_packet_ghost.py` execute **43 exact rational-complex calibration checks**, all passed. These use an off-axis quartet with multiplicity2, critical pair with multiplicity3, and exceptional real off-axis pair with multiplicity2. They verify original-coordinate CRT matrices, full nilpotent generators, exact involution signs, weight components, half-rank ghost spaces and their complete one-step arithmetic saturation. They do not test or prove arithmetic zero locations. The checker uses explicit exceptions, so optimization does not remove checks; both normal and `python -O` runs passed43/43.

An independent proof reviewer verified CRT, conjugate-linearity, reflection signs, arbitrary-target universal quotient and all nilpotent columns. Their repairs were integrated: explicit transported-A notation; eigenvalue multiplicities `m,2m,m`; the eta product identity continued analytically before dividing only on real `0<s<1`; and the endomorphism descent domain. The eta argument includes normal convergence of paired differences `s integral_(2n−1)^(2n) x^(−s−1) dx`, retaining the nonreal zeros of `1−2^(1−s)` as removable points of the quotient expression rather than incorrectly excluding only `s=1`.

## Comparison with prior Chatnotes and remaining source scope

Targeted literal searches for “critical packet ghost,” “Ghost-free descent criterion,” “Packet anomaly spectrum,” and “Positive packet-anomaly” in the core `split_zero_projective_monads_surcomplex` TeX/Markdown, the local `transcripts` tree, and the current standalone TeX found no matching complete argument before this addition. The earlier September9 reports already knew the tesserine coordinate map and period/Frobenius finite kernel, but did not contain the packet-ghost group quotient or its A-invariant saturation theorem. This is evidence for a previously unintegrated result in those checked locations, not a global priority assertion or proof of absence from every other directory.

The companion report `work/historical_hurwitz_lane_20260912.md` independently recovers the later marked Laurent/conormal proof block and proves its full multiplicity extension. It gives the exact isomorphism `U↦omega exp(log(p)(X−1/2))` on each local jet, an explicit truncated-log inverse, all conjugate-reciprocal jet coefficients, and the collision image/codimension when two spectral labels differ by `2pi i/log p`. It also proves an inverse to every Hurwitz zero-motion coefficient and reconstructs the whole compact input measure by original-scale Bernstein weights. These are actionable additions for the active CUE/Hurwitz owner and the present Tau packet. The report includes every proof and source hash; it was sent to the parent for integration.

The final audited version strengthens that Hurwitz result to **every nontrivial zero, including multiple zeros**: H10–H13 construct the complete local cluster polynomial by contour integrals and recursively recover every input moment using its coefficient germ. The final report has603 lines and SHA256 `df6385b14a3684f562bdc2fc684c8c42765d7bb8068d1bd529938b62991e6a9b`. Its J19–J20 now give the explicit collision map and exact sequence, rather than calling a cokernel a kernel. The agent is preparing a complete TeX fragment and exact source excerpts in its disjoint lane for the root's next reader build.

Remaining archive work is concrete: the two-family inventory contains25 distinct accessible hashes; this lane fully read selected response bodies from two editions, not all25 full transcripts. Other family members may contain later sections, altered exports or omitted attachments and must be compared at content/response level before claiming exhaustive source integration. The existing Sep9 full-file/main-manuscript audit remains evidence for its own stated scope; it is not inflated by this report. No source access blocker was encountered here, and none is claimed.
