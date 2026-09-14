# The actual τ-base Split-Zero program: canonical source route

Date: 2026-09-13. This is a bounded source route, with the maps needed to continue the original program. Historical source bytes are unchanged. It records seven canonical bodies, rather than a corpus reindex. The requested program takes split cohomology over the absolute base with structural zero τ, and develops the analogue of the Deligne argument there.

## 1. The primary source already constructs that program

Read this first:

`workspace:/output/split_zero_rh_tandem_2026-09-12/sources/Tau_Base_Cohomology_2026-09-12/NOTE.md`

Title: *Arithmetic cohomology over the τ-base*. Edition: delivered 2026-09-12. Bytes: 25,512. SHA-256:

`d03e71ad18f187bd89880cb8ca6fc9c5d6f260b3de8e8e5702c27db97e7b63c3`

The complete Markdown body was read in this route. Its typed companion is `NOTE.tex`, 28,353 bytes, SHA-256 `e7a494d79e01b774ad18045b1e244b28738ddf7b85aec31c58724e2fe35c3aba`. These are two presentations of the same delivered note, not independent findings.

- §1, lines 13–96, equations (1)–(8): the pointed blueprint base \(\mathbf F_{1,\tau}=\{\tau,1\}\), the literal blueprint morphism \(\jmath_R:\mathbf F_{1,\tau}\to B_R\), the structural morphism \(a_R:\operatorname{Spec}B_R\to\mathfrak b_\tau\), the ring reflection, and the distinct generic-point inclusion induced by \(\chi_R:G(R)\to\mathbb B\).
- §2, lines 98–188, equations (9)–(16): the actual four-point chart \(P\), with \(+<\eta<\sigma\), \(-<\eta<\sigma\); its structure sheaf restricts by \(G(\mathbb C)\to\mathbb B\). The full two-leg support lattice \(L=\mathcal P(\{+,-\})\) is retained. The coefficient diagram has the original \(V,V,\mathscr B,0\), with restrictions \(\Theta\) and \(J\Theta=\Theta\mathcal F\).
- §3, lines 190–288, equations (17)–(25): the projective resolution computes \(\mathsf A_\tau=R\Gamma(P,-)\). Its comparison to restriction at \(\sigma\) is the explicit derived morphism (20), including the chain homotopy. The resulting supported \(H^1\) is \(\{\tau\}\sqcup\coprod_{A\ne\varnothing}\{A\}\times Q\), with \(Q=\mathscr B/\Theta V\).
- §4, lines 290–356, equations (26)–(31): the right adjoint \(K_\tau(W)\), its signs and injective resolution, and its computed form \(S_\eta W[1]\). Dual support transports are precomposition on \(L^{\mathrm{op}}\).
- §§5–6, lines 358–499, equations (32)–(45): actual scaling on both charts, both moment representations, the full Mellin-jet observation, the residue pairing with its original skew-Hermitian orientation, and its injective equivariant morphism to \(H^{-1}R\operatorname{Hom}(\mathcal T,K_\tau(\mathcal L_1))\).
- §7, lines 501–550, equations (46)–(50): the actual product charts \(P^r\) over the underlying absolute point, external coefficient tensors with every differential sign, top cohomology \(Q^{\otimes r}\), and the product right adjoint \(S_{(\eta,\ldots,\eta)}W[r]\).

This body is the starting object for the τ-base continuation. The later polynomial-exponential and finite-metric constructions must be joined to this structural morphism, pushforward, coefficient sheaf and adjoint.

## 2. Six source bodies that retain its geometry and arithmetic arrows

### A. Original support spectrum and absolute geometry

`reference-library:/Chatnotes/split_zero_projective_monads_surcomplex/split_support_geometry_arithmetic_curve_v11.tex`

Edition stated inside file: June 2026, pre-publication Version 11. Bytes: 295,487. SHA-256:

`5fa6a55aa9d1a2e57599e206087d3d2466b25dd99fa1a90d5f86367aafab1b4d`

Proof-read windows: lines 376–484 (original scalar pair embedding and universal maps); 593–666 (idempotent localization); 2235–2362 (prime ideals, generic-point suspension, stalks and contracted blueprint); 3374–3496 (cycle determinants and their precise local-system morphism); 5940–6005 (denominator/Frobenius transition); 8153–8191 (Mellin character calculation); 8493–8675 (internal split globalization, split arithmetic/scaling sites).

Durable theorem locators are `thm:generic-suspension`, `cor:split-stalks`, `thm:blueprint-presentation`, `thm:denominator-frobenius`, `thm:internal-split-functor`, and `thm:split-arithmetic-site`. In particular \(D(e)=\{P_\tau\}\), \(G(R)_{P_\tau}=\mathbb B\), and \(\operatorname{Spec}R\) is the closed subspace \(V(e)\). Internalization is the functor \(A\mapsto1\amalg A\), and inverse image at a topos point gives \(x^*\operatorname{Spl}(A)=G(x^*A)\). Frobenius fixes the external τ while retaining the supported tropical zero. The spherical absolute stalk \(\mathbf F_1[T^{H_+}]\) and the semiringed split site are linked by the stated coefficient interfaces; their definitions remain separate in the source.

Version control: `v11 (1).tex` is 286,614 bytes with hash `1c41e1d7f61ec2ba2f514ab6db9d3d73d2dedca3fdc56df5fe0ea9b729e21fed`; `v11910.tex` is 290,245 bytes with hash `8443cc0401b18d373939d992f0a2f5384ee2fa1130f059753d5f3972eec5052d`. They are distinct historical editions, not byte duplicates or interchangeable citations. This route uses the 295,487-byte version and its own line locators.

### B. Earlier proof compendium, including the Boolean section

`reference-library:/Chatnotes/globalization nte/proof_compendium_both_files.md`

Bytes: 148,684. SHA-256:

`c118bbb31e4ea4ebcf32538bf63d522a7e4d239cc4425ded0d6a3a8e271a2e00`

The companion source-route reviewer read B.12 at line 1151, B.20–21 at lines 1367–1401, expanded Theorems 8.2–8.3 near 2542–2593, the Boolean section at 3365–3449, restriction/stalk maps at 3473–3605, and the semimodule projector/fibre description at 3610–3776. The exact section is \(s:\mathbb B\to G(R)\), \(0\mapsto\tau,1\mapsto e\), preserving zero, addition and multiplication, with \(\chi s=1\) and \(s\chi(x)=ex\); its multiplicative identity maps to e. Retain that arrow with its declared type.

The compendium's uncontracted monoid-semiring presentation at lines 3843–3907 omits the relation \([\tau]=0\). The exact repair is present in source A and in the primary τ-base note: use the contracted monoid semiring or add that relation. The old relations alone admit the augmentation sending every monomial, including \([\tau]\), to 1 in \(\mathbb B\), while sending the empty sum to 0. This proves precisely why the additional relation is required. No historical source was edited.

### C. Sheaf, Boolean geometry and full jet support source

`reference-library:/Chatnotes/globalization nte/shefy/zeta_split_zero_professional_preprint (1).tex`

Bytes: 61,288. SHA-256:

`d13832b31fd0ffcfde6187956bc09d0245073c1f08444491852b4b8477825238`

The companion reviewer read lines 286–509 (sheafification and affine Boolean realization), 520–717 (Artin ideal-chain and Boolean-cube adjoint retraction), 720–913 (full original jets, derivative coefficients and pointed support sections), and 915–1035 (the actual compactification tail sequence). The tail term \(\prod V/\bigoplus V\) is retained with its exact global quotient map. The complete companion route is `workspace:/work/f1_shefy_source_route_20260913.md`; its reading claims belong to that reviewer, not to an implied complete reread here.

### D. Literal theta sheaf and extension-by-zero comparison

`workspace:/output/split_zero_rh_tandem_2026-09-12/sources/Tau_Base_Cohomology_2026-09-12/sources/Split_Support_Actual_Comparison__CONTINUATION.tex`

Edition: original comparison delivered 2026-09-11, preserved as a dependency of the 2026-09-12 τ-base package. Bytes: 35,860. SHA-256:

`98e8aaa63b1f7ee4661c043cd985ca274646b749f36d23d2ec46cbc4b0737dc5`

Read §§3–4, lines 316–480, and §6, lines 648–744. The two-chart space \(X_\theta\) has the explicit Čech differential \(E_\chi\phi-r_-\psi\). The extension-by-zero comparison is \(c^0\phi=(\phi,0)\), \(c^1F=F\), inducing the identity on \(Q_\chi\). Every original coefficient/support fibre is carried through \(W_l\otimes\mathcal T_\chi\) and \(W_l\otimes Q_\chi\), with the original transition maps. §6 proves full finite Mellin-jet surjectivity, including a compactly supported right inverse, and retains every nilpotent in equation (6.1).

### E. Current complete category and supported cohomology morphisms

`workspace:/output/split_zero_rh_tandem_2026-09-12/tex/support_diagrams.tex`

Bytes: 8,127. SHA-256:

`7586ac17247456a55bdacfcf8b46c196c29eafd3b57846a71792e918704e069b`

The complete body was read. D1–D5 prove the equivalence between join-indexed linear diagrams and \(G(R)\)-semimodules, allowing changing support indices and nonzero bottom fibres. D6 proves the internal quotient against arbitrary split-linear targets. D7 is the exact kernel of the induced cohomology map. D8 gives the inclusion from the categorical kernel to the all-support pullback \(M\times_N eN\), with both domains explicit. These are the exact arrows for carrying the τ-base sheaf and arithmetic quotients without deleting supported zeros.

### F. Current arithmetic source and packet quotient with full unit

`workspace:/output/split_zero_rh_tandem_2026-09-12/tex/arithmetic_input.tex`

Bytes: 14,644. SHA-256:

`a50b0fb587b644c4ea94dba45b2b423d038f2bfbe7fef188543939ba850e58d2`

Read its opening and A1–A13, lines 1–302. The coefficient square and absolute pointed base appear at lines 1–19. A1–A3 retain \(D=-x\partial_x\), \(\Theta\phi=2\sum_{n\ge1}\phi(nx)\), the Fourier convention, the Gaussian source, and \(g=2\xi\). A7–A10 prove the full \(h(D)\) quotient square, the actual arithmetic kernel/cokernel sequence, and the packet section containing the original unit \(j_h(h/g)\). A11–A13 retain the nonzero extension coefficient and its equivariant roof. This file is the arithmetic continuation of primary equations (38)–(43), not a replacement of the τ-base space.

## 3. Exact τ-point arrows, with the base and restriction both retained

Write \(S=G(R)\), and retain its multiplicative pointed monoid \(M_S\). The map \(\iota:\{\tau,1\}\to M_S\), \(\tau\mapsto\tau,1\mapsto1_R^\bullet\), preserves multiplication, zero and unit. It is unique because those two images are required. Adding only the empty-sum relation at τ makes it a blueprint morphism to the full blueprint of S. Contravariant inverse image sends every proper prime to \(\{\tau\}\): every such prime contains τ and excludes 1. This proves the structural map to the absolute base point. None of the additive relations of R, its primes, or its quotient map has been removed.

The separate algebra map \(\chi:S\to\mathbb B\) gives the open generic point \(P_\tau\) of the original spectrum. Its exact effect on any S-semimodule M is

\[
\mathbb B\otimes_S M\ \cong\ eM,
\qquad b\otimes m\longmapsto b\cdot em.
\]

Here \(eM\) is a Boolean semimodule under its original addition; 0 acts by the global zero and 1 by identity. To prove balancing, if \(a=\tau\), then both \(\chi(a)b\cdot em\) and \(b\cdot e(am)\) are zero. If \(a=r^\bullet\), then \(ea=e\), so both are \(b\cdot em\). Additivity in m follows from distributivity of e; additivity in b follows from \(em+em=em\). The inverse is \(l\mapsto1\otimes l\). Its first composite is \(el=l\). Its other composite sends \(1\otimes m\) to \(1\otimes em=\chi(e)\otimes m=1\otimes m\); the b=0 generators vanish. These identities prove both inverses and naturality in M.

In source E's coordinates \(M=\coprod_lV_l\), this projection is exactly \((l,v)\mapsto(l,0)\). Its fibre over \((l,0)\) is the original \(V_l\), and the transition arrows are the original \(\rho_{lk}\). Applying the same calculation to the reconstructed cohomology object gives its label semilattice and its original cohomology fibres. The full diagram remains upstream of this comparison.

The primary construction uses the structural pushforward \(R\Gamma(P,-)\). Its exact comparison with the preceding generic-point restriction is already equations (19)–(20). Explicitly, the resolution

\[
0\to P_\eta\xrightarrow{v\mapsto(v,-v)}P_+\oplus P_-\to\mathbf E\to0
\]

is exact at each of the four stalks. Applying \(\operatorname{Hom}(-,F)\) gives \([F_+\oplus F_-\xrightarrow{r_+-r_-}F_\eta]\). The two degree-zero maps to \(F_\sigma\) differ by \(r_{\eta\sigma}(r_+-r_-)\), giving the homotopy with its displayed sign. Thus this is a proved map between the structural τ-base cohomology and the privileged support stalk; the construction does not replace the former by the latter.

## 4. The same arithmetic action survives the complete route

Source D uses \(R_aF(x)=F(ax)\); the primary τ-base note uses \(U_aF(x)=F(x/a)\). Their exact morphism is \(U_a=R_{a^{-1}}\). Retain each source's own coordinates. Substituting \(y=ax\) gives

\[
\mathcal M(R_aF)(s)=a^{-s}\mathcal MF(s).
\]

The target action commutes with \(D=-x\partial_x\). On the two source legs its lift is \((R_a,a^{-1}R_{a^{-1}})\), since Fourier scaling gives \(\mathcal F R_a=a^{-1}R_{a^{-1}}\mathcal F\). The original theta series commutes with dilation term by term; its established Schwartz estimates justify the sum. These identities prove a cochain endomorphism of the actual two-leg complex, fixing the support masks and the τ-base.

At the full jet \(s=\rho+z\), \(z^{m_\rho}=0\), its induced operator is

\[
a^{-\rho}\sum_{j=0}^{m_\rho-1}\frac{(-\log a)^j}{j!}N_\rho^j,
\qquad N_\rho(z^j)=z^{j+1}.
\]

This follows by Taylor multiplication of the exact entire factor \(a^{-s}\), retaining every coefficient. It is precisely source D equation (6.1), while inversion of a gives primary equation (40). The functorial support lift is \((A,v)\mapsto(A,R_av)\); τ maps to τ. Consequently the original τ-base pushforward, its dualizing right adjoint, and the finite jet/scaling realization form one explicit research route. A bound proved or disproved for an extra chosen family must be transported through these actual arrows before it says anything about this program.

## Reading and duplication record

The primary Markdown and source E were read completely. Source F was read through A13; source D through the windows stated above; source A through its stated theorem windows. The compendium and shefy windows were independently read by the companion reviewer. This note claims no fresh Lean, numerical, browser or remote execution. SHA identities were recomputed locally for all seven selected files.

The broad v2–v11 sequence in the support-geometry folder is edition history. Source D is a verified byte duplicate of `workspace:/output/split_zero_rh_tandem_2026-09-12/sources/Split_Support_Actual_Comparison_2026-09-11/CONTINUATION.tex`: both have 35,860 bytes and SHA-256 `98e8aaa63b1f7ee4661c043cd985ca274646b749f36d23d2ec46cbc4b0737dc5`. It is an explicit dependency, not another mathematical result. The present route uses the named retained original and current TeX with their exact hashes, never a same-title assumption.

The complete companion review was read after delivery. Its final SHA-256 is `0ea2b0d8cab72ebab08d4fd28a24f3c800cc2b53bdca48a5d6aac4ce48d418a0`. It contains the full proofs of the pointed-monoid base retraction, the semiring-spectrum inclusion in the monoid spectrum, and the missing-zero-relation repair, alongside the two original-source reading windows.
