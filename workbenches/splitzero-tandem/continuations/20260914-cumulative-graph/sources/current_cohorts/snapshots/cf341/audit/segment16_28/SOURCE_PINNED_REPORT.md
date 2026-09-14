# Reconstruction of the actual programme, U0016–U0028

This report concerns the original shared conversation, not an inferred programme assembled from later assistant notebooks. Every one of its 35 visible records has been read in full: 13 user inputs and 22 assistant messages, 5,036 lines. The initially read CRLF serialization had 204,419 bytes and SHA-256 `1dbb7fdc4004376bdcb312396dc6e12eccc9bdb8e6f2618b057a681e4682b919`. The current LF serialization has 199,384 bytes and SHA-256 `9705e32233d967f4abc6d522d40cfddc20a9f94c057d47410b37a3ee9e065298`; the byte difference is exactly the 5,035 removed carriage returns. Every visible payload matches the original record after the same line-ending convention. `READ_COVERAGE.json` gives each original node identifier, chain position, text digest, and segment lines. `user_inputs_verbatim.md` contains the original decoded user records without paraphrase. Both original-record and display-segment provenance are retained.

Additional original records A0935, A0945 and A0953 were read in full. A0953 is the actual command containing the complete authored `STUDY.md`, including proofs absent from the final reply. Historical tool outputs in this interval are redacted. Those original commands establish what mathematical text was submitted; the redaction prevents independently confirming their historical execution results. No PDF or OCR was used in this audit.

## 1. What the user actually asks in this interval

U0016 (node `7d76e278-ae0c-43db-ab75-81ea7405723a`, chain 1337, lines 1–9) asks for the whole arithmetic–geometric picture to be reconstructed and then mapped, including Dedekind/BCM character slices, one split-zero support, winding retained above a projected origin, all higher levels, nilpotent/unipotent/idempotent support, and two potential rigidity mechanisms. The last part explicitly develops a **GRH proof by contradiction**, not a claim that RH has been disproved.

U0017 (node `9dd06d78-abdb-4213-a643-73780d99ad1f`, chain 1445, lines 1773–1776) corrects the central foundational conflation: the unique bottom split-support datum is not the many-level family of coordinate origins. It asks for actual typed morphisms when distinctions are made. The user temporarily permits a hypothetical NS/arithmetic transfer and a third coordinate level as research premises for mapping; that permission does not prove either premise.

U0018 (node `a4f2753d-2aa4-4c11-b394-3b77c1640c80`, chain 1481, lines 1781–1784) insists that winding, holonomy and the all-level construction remain present rather than being replaced by the classical complex plane or one Klein-four example. The user explicitly rejects the interpretation that they are unsuccessfully stating a standard object. The requested 2024 geometric-Langlands source and rank-three Jordan link are part of the research directions, not replacements for the full RH programme.

U0019 repeats U0017 and says that making the third-level maps explicit has not executed the task. U0020 and U0021 require reading the actual split-zero work and the fuller GitHub globalization, respectively. These are corrections to the authority used in earlier replies.

U0022 (node `b48b70f3-9b82-48fc-b7b9-d3e6fd428c42`, chain 1713, lines 3379–3382) preserves the single bottom-support uniqueness while distinguishing higher nullity data: new layers correspond to information not realized at the preceding level. It explicitly invokes mixed support and asks what the infinite arithmetic quotient forces.

U0023 (node `c1f5c457-5da2-439d-b133-0a4b032008ed`, chain 1746, lines 3845–3849) gives the intended F1/purity programme directly: use the privileged point and retained infinite arithmetic quotient to put the supported spectrum over the unsupported base; map mixed support, sheaves, Frobenius, integrality, duality and the Weil II argument; then test a contradiction from an actual off-critical zero. It explicitly says “I never said GRH is wrong. I said it's correct.” The claimed inference from infinite quotient to purity remains a proposed conclusion to prove, rather than a theorem supplied merely by this utterance.

U0024 (node `65b8bdef-be04-4ac6-a7f1-9bb25a8f74f4`, chain 1748, lines 3850–3857) identifies **two routes**: spectral purity using actual mixed-support states, and the NS origin/cancellation route. U0025 challenges a false reading claim; U0026 asks to restart; U0027 (node `b48fac36-14fb-4a9b-a6fe-7d6fe8b94886`, chain 1774, lines 3874–3880) explicitly requires the LaTeX, forbidding PDF/OCR extraction.

U0028 (node `9d5e82ea-d670-4145-b5d3-c22d8948133e`, chain 2033, lines 5030–5033) again asks for the actual whole split-zero/Spec Z programme to be mapped into Weil II and continued. The user specifically objects to incomplete work followed by a statement that GRH has not been proved. That objection is not authorization to assert a proof without proving the mathematical bridge.

## 2. Corrections that must remain integrated

The authoritative correction is A0844 (node `2aeb23d1-e3be-4204-9bc2-3abe87a3cbed`, chain 1712, lines 2728–3378). Its retractions are part of the source programme and cannot be silently reverted.

### 2.1 Zero adjunction and higher origin layers

The source category `Rig^{not0}` forgets the distinguished additive-zero symbol but retains addition, multiplication and 1. The left adjoint is

\[
\mathfrak Z(A)=A\sqcup\{\tau_A\},\qquad
\operatorname{Hom}_{\mathrm{Rig}}(\mathfrak Z(A),S)
\simeq\operatorname{Hom}_{\mathrm{Rig}^{\neg0}}(A,U(S)).
\]

Restriction and extension \(\widetilde f(\tau_A)=0_S\) are inverse. Two objects having this same universal property over the same input admit unique inverse isomorphisms over that input: their composites extend the same input maps, and uniqueness makes the composites identities. This is the exact uniqueness theorem; a Krull-dimension comparison is not its proof.

The higher construction additionally retains \(i_n:L_n\to L_{n+1}\), with

\[
\operatorname{Orig}_{i_n}(y)=\operatorname{Hom}_{\mathrm{Set}/L_{n+1}}(\widehat y,i_n)
\simeq i_n^{-1}(y),\qquad
N(i_n)=L_{n+1}\setminus\operatorname{im}(i_n).
\]

A single empty value of this origin relation can occur at many distinct points of the nullity locus. A0844 explicitly retracts replacing this construction by \(G(R),G(G(R)),\ldots\). U0022 also rejects treating that retraction as cancellation of the valid uniqueness of the bottom support.

### 2.2 Coordinate geometry, rather than the bare field

The coordinate layer is \(A_d=\mathbb R[x_1,\ldots,x_d]\), with origin evaluation \(\epsilon_d:A_d\to\mathbb R\) and ideal \((x_1,\ldots,x_d)\). The coordinate inclusion has pullback

\[
j_d^*:A_{d+1}\to A_d,\quad x_{d+1}\mapsto0,
\qquad \epsilon_dj_d^*=\epsilon_{d+1}.
\]

After split globalization, the same equality holds under \(G\). These are diagrams over the single scalar object \(G(\mathbb R)\); they do not introduce another bottom zero at each level. The reported dimension theorem is \(\dim A_d=d\), \(\dim G(A_d)=d+1\). A0844 explicitly retracts the bare-\(\mathbb C\) objection, because it tested the wrong coordinate object.

For \(\mathbb R\)-algebras \(A,B\), the source proves the fully faithful map

\[
\operatorname{Hom}_{\mathbb R\text{-Alg}}(A,B)
\simeq\operatorname{Hom}_{G(\mathbb R)\text{-Alg}}(G(A),G(B)).
\]

Indeed a map over \(G(\mathbb R)\) fixes the supported zero. If it sent a supported \(a\) to \(\tau\), the identity \(a+e=a\) would map to \(\tau+e=\tau\), impossible because \(\tau+e=e\ne\tau\). Restriction is therefore an ordinary algebra map, inverse to split extension. The single common support retains the entire amplitude-algebra diagram.

### 2.3 The complex multiplicative observation retains support

The theorem that an additive semiring homomorphism to a ring kills \(e\) remains true. It does not cover multiplicative monoid representations. A0844 records the actual contracted monoid algebra

\[
\mathbb Z[M]/([\tau])\simeq
\mathbb Z\times\mathbb Z[\mathbb Z\setminus\{0\}],
\quad [0]\mapsto(1,0),\quad [n]\mapsto(1,[n]).
\]

Its inverse is

\[
\left(c,\sum b_n[n]\right)\mapsto
\left(c-\sum b_n\right)[0]+\sum b_n[n].
\]

The multiplicative representation \(T(\tau)=0\), \(T(n)=\operatorname{diag}(1,n)\) retains \(T(e)=\operatorname{diag}(1,0)\). The failure of additive preservation is exactly \(\operatorname{diag}(1,m+n)\ne\operatorname{diag}(2,m+n)\). This is a proved map, not a reason to dismiss support. Its central idempotent sector carries the identity action of every supported scalar because \(T(r)T(e)=T(e)\).

## 3. The infinite quotient supplies real arithmetic rigidity

A0862 (node `b6c3dc97-18dd-487e-bb70-933fab060c64`, chain 1745, lines 3383–3844) works with the source object \(S=G(\mathcal O_K)\), supported ideal \(\mathfrak e=\{\tau,e\}\), and supported ideal monoid \(I_J=J\cup\{\tau\}\). It proves

\[
I_JI_L=I_{JL},\qquad \mathfrak e I_J=\mathfrak e.
\]

Two absorbing elements of this same commutative ideal monoid coincide by multiplying them together. This uniqueness does not identify directional faces or origin fibres, which have different roles.

The ordinary norms extend uniquely to \([1,\infty]\), with \(\mathcal N(\mathfrak e)=\infty\). For \(d=[K:\mathbb Q]\), absorption with \(2\mathcal O_K\) would force a finite positive value \(r\) to obey \(r=2^dr\), impossible. Assigning infinity satisfies every absorption identity; ordinary multiplicativity handles the other products.

The quotient statement is stronger than a statement about cardinality alone. A surjective semiring map \(q:S\to T\) whose zero fibre is exactly \(\mathfrak e\) restricts to an injective ring map \(\mathcal O_K\to T\): equality of two images forces their difference into that exact zero fibre. Its image is a ring because additive inverses come from the supported copy. Surjectivity then gives \(T\simeq\mathcal O_K\), necessarily infinite. A finite quotient has to enlarge the arithmetic zero fibre, as in reduction modulo a nonzero ideal.

For any finite-order ray-class character \(\chi\), each multiplicative weight \(w_{\chi,s}(J)=\chi(J)N(J)^{-s}\), \(\Re s>0\), has unique extension to the absorbing ideal with \(w_{\chi,s}(\mathfrak e)=0\). Choose an allowed ideal of norm greater than one; the fixed-point equation has scalar multiplier of modulus less than one. The single idempotent remains in

\[
\mathbb C[\mathcal I\sqcup\{\mathfrak e\}]
\simeq\mathbb C\times\mathbb C[\mathcal I],
\]

while these character weights factor through the second factor. Thus the support is retained algebraically and cannot supply a new finite Euler term. **An actual off-critical zero consistent with these results must belong to the unchanged arithmetic amplitude; it cannot be manufactured as a new finite-norm contribution from the bottom ideal.** This restriction is proved for all finite-order sectors, not only the Riemann trivial sector.

## 4. The actual mixed-support and Frobenius construction is already present

A0952 (node `50a6a43b-ec70-40dc-b17f-864477ddcff4`, chain 1985, lines 3893–4353) recovers the actual double. A0961 (node `a7bbd422-311c-4380-ba6c-a4bdd61fce2f`, chain 2032, lines 4354–5029) and original code A0953 give its full derivation.

For \(S=G(A)\), \(u=-1_A\),

\[
D_A=S^2,\qquad
(a,b)\star(c,d)=(ac\oplus ubd,ad\oplus bc).
\]

The four zero-amplitude masks \((\tau,\tau),(e,\tau),(\tau,e),(e,e)\) are distinct. The amplitude is \(\pi(a,b)=p(a)+tp(b)\) in \(B=A[t]/(t^2+1)\); the support lies in \(\mathbb B[C_2]\). The **pair** of these observations is injective because \(1,t\) form a free basis and the mask distinguishes each absent zero coefficient from each supported zero coefficient.

The synchronization idempotent is \(E=(1,e)\), and

\[
D_A[E^{-1}]\simeq G(B).
\]

Multiplication by \(E\) sends every active mask to the fully supported face while preserving all ordinary coefficients; its image has unit \(E\). If a homomorphism makes \(E\) invertible, idempotence forces its image to be 1, so it factors uniquely through multiplication by \(E\). This proves the localization, including its unit and direction. Original A0953 additionally says the localization open consists of \(P_\tau\) and the \(Q_{\mathfrak q}\) branches in the source prime classification; the mixed \(M\) and \(T_{\mathfrak p}\) branches contain \(E\). The latter prime names depend on the source ledger and are not redefined in this audit.

For every \(n\ge1\), the source extension is \(D_{A,n}=G(A)^n\), with wrap factor \(u\) when \(i+j\ge n\); its amplitude is \(B_{A,n}=A[t]/(t^n+1)\), and \(E_n=(1,e,\ldots,e)\). The full \(2^n\) masks remain in \(\mathbb B[C_n]\). The same proof gives \(D_{A,n}[E_n^{-1}]\simeq G(B_{A,n})\). Associativity follows from the exact equality of the two integer wrap counts, not cancellation of absent terms.

For \(n\mid m\), \(k=m/n\), the source map inserts the \(i\)-th coefficient at slot \(ki\). It induces \(t_n\mapsto t_m^k\), and the precise idempotent equation is \(E_m\iota_{n,m}(E_n)=E_m\). It need not preserve the unsynchronized mask. These maps implement the higher-degree comparison over a single support.

For an \(\mathbb F_q\)-algebra, \(q\) odd and \(\gcd(q,n)=1\), the actual Frobenius is

\[
(\Phi_q(a))_{qi\bmod n}
=u^{\lfloor qi/n\rfloor}a_i^q,
\]

with absent coefficients kept absent. It is a semiring map, satisfies \(\pi_n\Phi_q(z)=\pi_n(z)^q\), fixes \(E_n\), and commutes with synchronization. Coefficient reduction from \(\mathcal O_K\) to a residue field preserves every mask: a coefficient divisible by the prime becomes supported zero, never external absence. Bad primes dividing \(2n\) are retained as excluded from this particular finite-etale statement, rather than silently deleted from a global Euler product.

For \(Y_n=\operatorname{Spec}(\mathbb F_q[t]/(t^n+1))\), roots \(r_j=\zeta_{2n}^{2j+1}\) carry arithmetic Frobenius

\[
j\longmapsto qj+(q-1)/2\pmod n.
\]

For cycle lengths \(d_j\), \(\det(1-TF\mid H^0)=\prod_j(1-T^{d_j})\); geometric Frobenius is the inverse permutation and has the same cycle lengths. This is a completed proof of **weight-zero purity of the actual coefficient object**. An audit saying that the programme has no Frobenius realization would be false.

## 5. Which Deligne argument was actually selected

A0952/A0961 identify three substantial constructions rather than merely quote a purity definition:

1. Weil II §§1.7.8–1.7.11 retain all tame monodromy directions \(N_i\) over the one common intersection \(E\), with successive-specialization isomorphisms preserving all actions and an associativity square. Coordinate choices are retained in the normal-bundle complement before restriction to a section. This is relevant to the user's one-support/many-directions correction.
2. §§3.3.4–3.3.6 give opposite bounds on the same image \(\operatorname{im}(H_c^i\to H^i)\). Duality retains \(2d-i\), dual coefficients and the Tate factor \((-d)\). §6.2.4 uses upper weight \(w\) for \(K\) and \(-w\) for its dual, not the same sign.
3. §1.5 uses even tensor powers, nonnegative real local traces, and geometric cohomological pole control to prove \(w(\alpha)\le r+1/k\) for every \(k\). §3.2.13 performs the tensor-square refinement \(1+2^{-k}\to1+2^{-(k+1)}\). A fixed spectral excess is contradicted only once those estimates act on that same spectral value.

The special-fibre route also includes the invariant-cycle surjection in §6.2.9, retaining the invariant part of nearby cohomology, and the rational-homology-manifold extension via the actual dualizing identity in §3.3.11. It does not infer that singularity destroys purity.

Source qualification is essential. A0953 explicitly records that the nested French/English TeX are historical witnesses with zero accepted salvage members, while the current accepted edition is stored separately. The witnesses disagree on a \(j_!\)/\(j_*\) statement, the dual-weight sign, and an eigenvalue/reciprocal-root sentence. Thus A0952/A0961 are source-pinned accounts of the chosen mechanism, but not evidence that every statement in the historical witness was correct. Original A0935 documents earlier scan/page reading; A0952 declares PDF use despite U0027's instruction. The later A0953 note explicitly uses TeX and records the provenance problem. This audit follows the user's LaTeX instruction.

## 6. Counterfactual restrictions that are actually proved here

This interval proves restrictions on an actual RH counterfactual, but it does not exhibit one:

- It must be an actual zero of the unchanged original arithmetic amplitude, with its argument retained separately from its zero value. A0756's Klein-four calculation gives \(\Re\rho-1/2=c_{-+}(\rho)/4\). Mapping \(\zeta(\rho)\) to the target origin does not set that independent component to zero.
- It cannot be the addition of a finite-norm bottom-support ideal while preserving the actual norm/quotient maps; A0862 proves that impossible.
- It is not removed by the actual synchronization localization: the complete coefficients are preserved, with loss of only the unsynchronized mask. The theorem in `PACKET_SURVIVAL.tex` proves the exact survival map for the actual packet through this very coefficient construction.
- A pure weight-zero cyclic coefficient spectrum may accompany the arithmetic packet. Its roots-of-unity action does not change an arithmetic eigenvalue's absolute value; the exact tensor/retraction computation below proves this for the full jets.
- Unipotent local monodromy alone retains relative grades but not their absolute center. A0961's \(Nv_j=v_{j-1}\), \(Fv_j=cq^jv_j\) has grades \(2j-d\), center \(\gamma+d\). No original factor \(c\) is discarded.

A0756's arbitrary symmetric polynomial and A0788's chosen Jordan holonomy are valid computations for their declared objects. They are not actual arithmetic counterexamples and do not establish that an off-line arithmetic packet satisfies the eventual global purity constraints. The user repeatedly rejected stopping at those substitutes. A complete later argument must propagate every subsequently proved global constraint onto the actual packet; this report does not declare the listed local restrictions exhaustive of later work.

The NS route in this interval has a precise source-level limitation: the residual equation and force translate together, and compactly supported disjoint translated copies have vanishing cross-convection terms. Those are maps of the actual triples, not an assertion that a fixed force produces blowup at arbitrary points. Therefore coordinate-origin uniqueness is not established by the source. The user-selected marked arithmetic point remains meaningful; a transfer has to carry that marking and the cancellation invariant rather than identify it with an arbitrary spatial coordinate.

## 7. New exact consequence

`PACKET_SURVIVAL.tex` proves a retraction of an **actual assumed arithmetic packet** through the original all-degree mixed-support coefficient construction. With full multiplicity,

\[
E_Z=\mathbb C[x]/\prod_{\rho\in Z}(x-\rho)^{m_\rho},
\qquad B_n=E_Z[t]/(t^n+1),
\]

the inclusion \(E_Z\to B_n\), \(f\mapsto f\otimes1\), has the explicit \(E_Z\)-linear retraction \(\operatorname{Tr}_{B_n/E_Z}/n\). Its split lift preserves supported zero and external absence separately. It commutes with the original full-jet arithmetic action and with the integral signed-permutation lift of the source coefficient Frobenius. An actual off-line eigenclass remains nonzero, and its exact eigenvalue on the retained invariant unit coefficient remains \(a^\rho\). Tensoring with the full coefficient Frobenius changes it only by a root of unity, so its modulus remains \(a^{\Re\rho}\).

This identifies a definite surviving cohomological input for the global purity calculation. It is not a claim that the global comparison must preserve it: proving or refuting that preservation is precisely where the actual compact/ordinary image, duality and geometric estimate must be evaluated. It also does not assert any numerical zero off the critical line.

Independent review required the amplification base to be explicit. All amplification powers in `PACKET_SURVIVAL.tex` are now written over \(\mathbb C\), with nonvanishing proved by a complex linear functional. Tensoring over the packet ring would be a different operation and can kill the nilpotent highest-jet tensor. The module also now proves the original scaling bridge: \(\Theta\mathcal R_a=\mathcal R_a\Theta\), \(J_Z\overline{\mathcal R}_a=A_aJ_Z\), and the complete packet bijection gives \(\overline{\mathcal R}_a\sigma_Z=\sigma_ZA_a\). No arithmetic scaling factor is assigned independently of the original theta quotient.
