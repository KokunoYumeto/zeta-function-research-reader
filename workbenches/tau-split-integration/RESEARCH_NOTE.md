# SplitZero integration of residue and period comparisons

13 September 2026. Base: reviewed main `789339c2daff74167224a7bdd665879910c168fc`. The four new modules use the original scalar `G`, `LinearDiagram.Total`, `HomOver`, Codex's `ReindexedHom`, `Relations.quotientDiagram`, and the internal quotient universal property. No replacement scalar, total carrier, or definition of homology is introduced. The actual execution checkpoint belongs in `STATUS.md`; mathematical arguments below do not themselves claim a successful Lean run.

## 1. The original support-changing quotient square

Let `D,E` be the existing coefficient diagrams on join-semilattices with bottom, `f : SupportMap L K`, and `a : HomOver D E f`. Let `B,C` be the original transport-stable relation submodules, and require `a_i(B_i) subset C_{f(i)}`.

`descendOver` constructs quotient fibre maps by the existing `Submodule.mapQ` and proves their naturality by lifting a quotient representative and applying the original naturality square. The resulting total map is linear over the original `G(R)` and obeys

\[
\begin{array}{ccc}
\mathfrak R_L(D)&\xrightarrow{\widetilde a}&\mathfrak R_K(E)\\
q_B\downarrow&&\downarrow q_C\\
\mathfrak R_L(D/B)&\xrightarrow{\overline a}&\mathfrak R_K(E/C).
\end{array}
\tag{I1}
\]

Its exact receiving-boundary criterion is

\[
\overline a(i,[x])=(f(i),0)\iff a_i x\in C_{f(i)}.
\tag{I2}
\]

If `x` is outside `B_i`, the source class is not `(i,0)`. If `f(i)` is nonbottom, the output is not global absence, even when (I2) holds. This qualification is explicit: preserving joins and bottom need not imply reflecting bottom, and the original reconstruction permits a nontrivial bottom coefficient fibre. No injectivity of arbitrary transports is assumed.

The adapter from Codex's `SupBotHom`-based `ReindexedHom` to `HomOver` has literally the same total map. The existing terminal amplitude observation commutes with fixed-index natural maps. The original scalar square `G(R) -> G(S)` over `R -> S` is retained through `Maps.reflection_natural`.

## 2. Preserve the original quotient and the further observation kernel separately

Let `J : Hom D E` kill `B`. The existing `Relations.descend` constructs

\[
\overline J:\mathfrak R_L(D/B)\longrightarrow\mathfrak R_L(E),
\qquad(i,[x])\longmapsto(i,J_i x).
\tag{I3}
\]

The family `K_i=ker J_i` is transport-stable: `J_j D(h)x=E(h)J_i x`. The code constructs a further quotient

\[
\mathfrak R_L(D/B)\longrightarrow\mathfrak R_L(D/K)
\tag{I4}
\]

whose composite with `q_B` is `q_K`. The coefficient kernel added by this observation is `K_i/B_i`, not a newly declared zero object. A non-boundary `x` in `K_i` is recorded as a nonzero original quotient class before (I3) sends it to the receiving supported zero.

For the arithmetic programme, the full `ker j_E` of a finite jet observation on the infinite strong-Schwartz source must not be identified with its original theta boundary module. Exactness can identify those spaces on a specified finite polynomial presentation; it does not do so on the entire source automatically. Period invertibility preserves `ker j_E`; it does not prove that kernel trivial.

## 3. Representative and coefficient defects both remain

Assume only fibrewise sections `r_i:E_i -> D_i` with `J_i r_i=1`. Define

\[
\Delta_h(v)=D(h)r_i v-r_jE(h)v,\qquad h:i\le j.
\tag{I5}
\]

The code proves

\[
J_j\Delta_h=0,\qquad
\Delta_{h'h}=D(h')\Delta_h+\Delta_{h'}E(h).
\tag{I6}
\]

The first uses naturality of `J` and the two section identities. The second adds and subtracts the actual intermediate representative `D(h')r_jE(h)v`, retaining both transport compositions.

To identify the first defect with an original theta boundary, the stronger input `Delta_h(v) in B_j` is required. `section_natural_mod` then proves naturality in the original quotient. Equality of finitely many jets alone is not substituted for this input.

For an actual natural coefficient action `A`, its source lift is

\[
\widehat A_i=r_iA_iJ_i,
\quad J_i\widehat A_i=A_iJ_i,
\quad
D(h)\widehat A_i x-\widehat A_jD(h)x
=\Delta_h(A_iJ_i x).
\tag{I7}
\]

It kills `ker J_i`. With the original-boundary witness just specified, `quotientLiftOperator` constructs a natural action on `D/B`. Its reconstructed total obeys

\[
\overline J\,\overline{\widehat A}
=\widetilde A\,\overline J.
\tag{I8}
\]

Source sections are not assumed natural to obtain this conclusion.

The residue insertion for different cyclic packet algebras need not itself be natural under arbitrary packet injections. The general code therefore also accepts arbitrary fibrewise operations `a_i` and records

\[
C_h=E(h)a_i-a_jE(h),\qquad \widehat a_i=r_i a_iJ_i,
\]
\[
\boxed{D(h)\widehat a_i-\widehat a_jD(h)
=\Delta_h a_iJ_i+r_j C_hJ_i.}
\tag{I9}
\]

Expansion and additivity of `r_j` prove (I9). Both terms have stated source and target types. `coefficientDefect_of_natural` proves `C_h=0` only for a genuine natural action; the simpler equation (I7) is that case. No global supported-linear map is manufactured from a non-natural family by merely adding labels.

## 4. The residue insertion and the original theta lift

In the specified cyclic algebra `E=C[S]/chi`, let `ell` be the top-remainder residue functional. `residueInsertion` is the existing linear-map construction

\[
\mathcal R(v)=\ell(v)1_E.
\tag{I10}
\]

For the actual inclusion `inc:F -> E` and quotient `pi:E -> E/F`, the code proves

\[
\pi\mathcal R\,\mathrm{inc}=(\pi1_E)\otimes(\ell\,\mathrm{inc}).
\tag{I11}
\]

This follows by applying linearity of `pi` to `ell(inc v) * 1_E`. Given a specified vector with residue one, every scalar multiple of `1_E` is obtained by scaling that vector; `residue_image_line` checks both directions of the image description. The preceding written perfect-residue-pairing argument supplies nonzero factors for a nonzero proper invariant cyclic constituent. That whole cyclic nonvanishing proof and the analytic period-curvature theorem are not relabelled as new Lean results here.

The source operation at degree `N` remains exactly `r_N R j_E`, as in the supplied exponential family. Formula (I9) controls its comparison with other source degrees or packets. On the original cochain source, `j_E d=0` makes it vanish on theta boundaries. Across the same fixed packet, the known original-boundary representative comparison supplies (I7) modulo the existing quotient.

## 5. Period coordinates transport the whole support diagram

For specified fibrewise linear equivalences `Phi_i:E_i ~= W_i`, construct

\[
W(h)=\Phi_j E(h)\Phi_i^{-1}.
\tag{I12}
\]

The adjacent inverse factors cancel in the identity and composition laws. The resulting forward and backward maps are natural, and `periodTotalEquiv` proves both inverse laws and linearity over the original `G(R)` on reconstructed totals. It preserves the support label, fibre zero, and global absence.

The original action is conjugated through the same maps, and its total intertwining square is checked. Through the original boundary quotient the key equality is

\[
\boxed{\widetilde\Phi\,\overline J=\overline{\Phi J}.}
\tag{I13}
\]

The proof lifts a class using the established quotient surjection, applies the universal quotient formula to both sides, and evaluates the identical coefficient maps. In particular `ker(Phi_i J_i)=ker J_i`. Neither this equality nor the equivalence replaces the infinite arithmetic quotient by a finite packet.

The fixed-coefficient-ring formalization takes analytic period invertibility as an explicit input. The coefficient base-change square is a separate reused ring-map theorem, not a new general six-functor or Frobenius comparison. The original metric at period coordinates remains `Phi_i^{-*}G_iPhi_i^{-1}`; it is not silently the coordinate Euclidean metric. Theta mass, Taylor units, full nilpotent jets, and cross-pairings remain in the objects supplying `J,r,A,Phi`.

## 6. Concurrent GitHub work and reference intake

The PR27 collaboration comment concerning circle periodization was read. Its additional Hilbert-completion observation has a kernel containing unsampled primary blocks and higher jets at sampled roots; it is not the original strong-Schwartz quotient or the Schwartz critical-line quotient. Sections 2 and 5 preserve exactly the place for that further kernel. This branch does not claim to have rerun that analytic development or formalized its sampling theorem.

The EGA editable archive and Deligne French TeX supplied with this request remain reference inputs. This code continuation does not republish them or claim a new full reading. The dated Deligne primary-source correction remains separately retained; the new transcript is not silently used to reverse that correction.

## 7. Verification contract

`SPLIT_INTEGRATION_TARGETS.json` enumerates 47 definitions/theorems. The workflow checks the original scalar and dependency blobs, unchanged Lean and Mathlib pins, and rejects replacement scalar declarations and proof escapes. It traverses and strictly compiles the actual local import closure, including reconstruction, homology, internal quotients, Codex support changes, joint synchronization homotopies, the conormal tower, and Laplacian identities. The new combined import and exact-target audit are followed by the inherited derived audit.

The existing fail-closed parser is reused. Missing, duplicate, unexpected, and forbidden-axiom reports are deliberately tested in normal and optimized Python. A separate Lean control must reject `e=tau` at the actual equality, not due to a missing import or identifier. The observed result, source commit, and failure history are recorded in `STATUS.md`, not inferred from these proof scripts.

No existing mathematical file, publication source, or dependency pin is modified. The branch remains an add-only continuation against its recorded main base; concurrent corrections require explicit review rather than an unrecorded replacement.
