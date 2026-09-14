# Independent selected-source review: SGA 5 trace and DLMF gamma product

Date: 2026-09-13. Scope: the source and types behind the residue/trace operation used in `Tau_SGA_Trace_Period_Control`, and the precise gamma product used in its period determinant. This review does not replay the package's finite checks or establish a new proof of its determinant. The parent task owns those calculations and cumulative integration.

## Finding

SGA 5, Exposé III, printed pages 127–129, does state the required residue–multiplication-trace compatibility as (6.8.5), constructs the class through the conormal differential, and gives its adjoint trace maps. The packet preserves the essential source qualification. The source assumes a noetherian base and separated schemes of finite type. Its ambient smooth morphism need not be proper for (6.8.5); the finite flat composite is proper. The package's extension to an arbitrary commutative coefficient ring must therefore rest on its direct finite-free calculation, as its source review already states.

The DLMF gamma product is an exact match, with the packet's integer \(d=q+1\ge2\). No correction to that product is needed.

## Files and provenance

The supplied packet is at:

`output/split_zero_rh_tandem_2026-09-12/sources/web_sga_trace_period_delivery/Tau_SGA_Trace_Period_Control/`

The entire `SOURCE_REVIEW.md` and the SGA 5 row of `checks/source-inventory.json` were read. The expected English master is `02e_SGA5_English_Master(1).tex`, 799289 bytes, 15818 lines, SHA-256 `e87647513be376d904bf4ad418ce942ac40e0d74890baace284fb73fba76f6d2`. That row declares no input dependencies and records prior selected reading ranges 2140–2269, 3060–3098, 3630–3678, 3850–3925, and 4020–4282. These are the packet's earlier reading claims, not line ranges independently reread in this review. The exact English master was not located in the bounded intake paths, including Downloads, the task-local sources, and the named Noether Multilingual directory. Accordingly this review does not attest to the bytes or translation of that master.

The independently inspected original French source is the preexisting local scan:

`local-profile/Documents/Papors/OS/SGA5.pdf`

- Size: 59033040 bytes; 496 PDF pages.
- SHA-256: `79bd542454ca2a5b3ac60488b14d3d91af9c7f8e68fa5acc0c48cf6068a89ad5`.
- The printed page number is the one-based PDF page number minus 12 in the examined portion.
- Visually read in full: printed pages 120–130 and 136–137, corresponding to one-based PDF pages 132–142 and 148–149. The actual load-bearing interval is printed pages 127–129, PDF pages 139–141. Printed 130 was read to check the following transition; no conclusion about the full subsequent theorem 6.10 is claimed.
- The table of contents on one-based PDF page 11 was visually read to identify Exposé III and its attribution: A. Grothendieck, written up by L. Illusie.
- Read-only Poppler renders are in `work/sga_trace_period_primary_evidence_20260913/`. Their file hashes are bound in the companion JSON. Text extraction on both available scans yielded form-feed-only output in the sample; the findings below come from rendered pages, not OCR.

A second local scan, `local-profile/Documents/Papors/OS/SGA5 (1).pdf`, has 62025563 bytes and SHA-256 `b256ebd072a8c68209518412a263c9289c6f1854a346733d86f885930d5fe6ca`. It was inventoried, but the first scan above was the visual reading witness. The [public SGA 5 scan index](https://wstein.org/sga/sga5/index.html) was opened and identifies the scans as made by Vincent Maillot. Its linked PDF exceeded the browsing tool's content-size limit. This review does not claim a bytewise comparison between the remote download and either local scan.

## The coherent category in III §6

Printed page 120 starts the coherent-sheaf appendix. In this section \(S\) is noetherian; the \(S\)-schemes considered are separated and of finite type. \(D(X)\) is the derived category of \(\mathcal O_X\)-modules. Section 6.1 records the exceptional inverse image

\[
f^!:D^+(Y)\longrightarrow D^+(X),
\]

with transitivity. For proper \(f\), its duality/adjunction isomorphism has the form

\[
Rf_*R\mathcal Hom_X(E,f^!F)
\simeq R\mathcal Hom_Y(Rf_*E,F),
\tag{III 6.1.1}
\]

with the coherent/boundedness qualifications displayed in the source. Here \(R\) is written explicitly on direct images to make the derived types visible; the source convention suppresses it in several formulas. For smooth \(f:X\to Y\) of pure relative dimension \(d\), the displayed isomorphism is

\[
Lf^*L\otimes_{\mathcal O_X}\Omega^d_{X/Y}[d]
\xrightarrow{\sim}f^!L.
\tag{III 6.1.2}
\]

When \(f\) is also proper, the counit gives

\[
\operatorname{Tr}_f:
Rf_*(Lf^*L\otimes\Omega^d_{X/Y}[d])\longrightarrow L.
\tag{III 6.1.3}
\]

Printed pages 120–122 explicitly warn that there is no generally satisfactory coherent subcategory stable under all six operations. A complex is perfect relative to \(S\) when it has finite Tor-dimension relative to \(S\) and coherent cohomology. The notation is \(D(X)_{\mathrm{parf}/S}\). This category is not in general closed under either derived tensor product or derived internal Hom. The particular internal-Hom stability stated on page 121 assumes that its first argument is absolutely perfect and its second argument is relatively perfect.

For external products, \(X_1,X_2\) are required to be Tor-independent over \(S\):

\[
\operatorname{Tor}^{\mathcal O_S}_i(\mathcal O_{X_1},\mathcal O_{X_2})=0
\qquad(i>0).
\]

Section 6.3 retains the corresponding Tor-independence and relative-perfection hypotheses for its Künneth arrows; the exceptional-pullback Künneth isomorphism has the additional finite-Tor-dimension/boundedness conditions in that paragraph. Sections 6.4–6.7 retain their own finite Tor-dimension, proper-support, and Tor-independence hypotheses. In particular the coherent correspondence formula cannot be imported solely by replacing the coefficient symbol in an étale formula. The finite residue construction in §6.8 has the explicit smooth/regular-immersion factorization below; no general six-functor closure is needed for the packet's elementary coefficient extraction.

## The actual class and residue in III §6.8

The data on printed page 127 are

\[
f:X\longrightarrow S\quad\text{smooth of pure relative dimension }N,
\qquad i:Y\hookrightarrow X\quad\text{regular of codimension }d,
\qquad g=f\circ i.
\]

Write \(I=\ker(\mathcal O_X\to i_*\mathcal O_Y)\) and retain the source's conormal notation

\[
N_{Y/X}=I/I^2.
\]

The purity isomorphism in (6.8.2) is

\[
\mathcal Ext^r_{\mathcal O_X}(\mathcal O_Y,\Omega^d_{X/S})=0
\quad(r\ne d),
\]

\[
\mathcal Ext^d_{\mathcal O_X}(\mathcal O_Y,\Omega^d_{X/S})
\simeq
\mathcal Hom_{\mathcal O_Y}
\bigl(\Lambda^dN_{Y/X},\Omega^d_{X/S}|_Y\bigr).
\]

It induces the global isomorphism

\[
\operatorname{Ext}^d_{\mathcal O_X}(\mathcal O_Y,\Omega^d_{X/S})
\simeq H^0\!\left(Y,
\mathcal Hom_{\mathcal O_Y}(\Lambda^dN_{Y/X},\Omega^d_{X/S}|_Y)\right).
\tag{III 6.8.3}
\]

The differential is the actual map

\[
I/I^2\longrightarrow\Omega^1_{X/S}|_Y,
\qquad [h]\longmapsto d_{X/S}h|_Y.
\]

It is well-defined because \(d(I^2)\subset I\Omega^1_{X/S}\). Its \(d\)-fold exterior power is an element of the right-hand side of (6.8.3). Its inverse image is the class

\[
\operatorname{cl}_{X/S}(Y)
\in\operatorname{Ext}^d_{\mathcal O_X}(\mathcal O_Y,\Omega^d_{X/S}).
\tag{III 6.8.1}
\]

Now suppose \(g\) is finite and flat; the source then has \(d=N\). The duality identification gives the line module

\[
g^!\mathcal O_S\simeq
(\Lambda^N N_{Y/X})^\vee\otimes_{\mathcal O_Y}\Omega^N_{X/S}|_Y.
\]

A global section \(\omega\) of this module is a morphism \(\mathcal O_Y\to g^!\mathcal O_S\). Its adjoint is a morphism \(g_*\mathcal O_Y\to\mathcal O_S\). The source defines

\[
\operatorname{Res}_{Y/S}(\omega)
=\bigl(\text{that adjoint morphism}\bigr)(1).
\]

This is a morphism of coherent algebraic coefficient modules. It has no complex conjugation or Hermitian form built into its definition.

There are two separate equations on printed page 128:

1. If the ambient \(f\) is proper, then the map from the Ext group to \(H^N(X,\Omega^N_{X/S})\), followed by its cohomological trace, gives

   \[
   \operatorname{Res}_{Y/S}(\omega)=\operatorname{Tr}_f(i_*\omega).
   \tag{III 6.8.4}
   \]

2. With no properness assumption on the ambient \(f\), and still with \(g\) finite flat, the source states

   \[
   \boxed{\operatorname{Res}_{Y/S}
   \bigl(y\operatorname{cl}_{X/S}(Y)\bigr)
   =\operatorname{Tr}_{Y/S}(y)}.
   \tag{III 6.8.5}
   \]

   Here \(y\in H^0(Y,\mathcal O_Y)\), and \(\operatorname{Tr}_{Y/S}(y)\) is the classical trace of multiplication by \(y\) on the finite locally free module \(g_*\mathcal O_Y\). The finite morphism \(g\) itself is proper, so the adjunction defining this residue is available even when \(X\to S\) is affine and nonproper.

The exact adjoint statement is that \(\operatorname{Tr}_{Y/S}:g_*\mathcal O_Y\to\mathcal O_S\) corresponds to

\[
\mathcal O_Y\longrightarrow g^!\mathcal O_S,
\qquad 1\longmapsto\operatorname{cl}_{X/S}(Y).
\]

For \(F\in D(S)_{\mathrm{coh}}\), (6.8.6) is the resulting class-multiplication arrow

\[
Lg^*F\longrightarrow g^!F
\simeq Lg^*F\otimes^{L}_{\mathcal O_Y}g^!\mathcal O_S.
\]

Its adjoint, (6.8.7) at the top of printed page 129, is

\[
g_*Lg^*F\simeq F\otimes^L_{\mathcal O_S}g_*\mathcal O_Y
\xrightarrow{\mathrm{id}_F\otimes\operatorname{Tr}_{Y/S}}F.
\]

These are the exact morphisms supplied by the passage, rather than merely a comparison of ranks or a similarity between trace expressions.

## The source's proof qualification and a printed conormal typo

Equation (6.8.5) is followed by an explicit qualification: its compatibility is not demonstrated in the cited location, [8] III 9 R6; the case \(N=1\) is treated in Raynaud, *Anneaux locaux henséliens*, VII 1, Lecture Notes in Mathematics 169, Springer, 1970. Printed page 136 identifies [8] as Hartshorne, *Residues and duality*, Lecture Notes in Mathematics 20, Springer, 1966. This review verifies that the qualification and references are printed; it does not claim to have independently read Raynaud VII 1 or Hartshorne III 9 R6. The packet's direct one-variable proof is therefore material and should remain complete.

There is also a source typography issue on printed page 128. The map on the second displayed line uses \(N_{Y/X}\), in agreement with the definition and (6.8.2)–(6.8.3) on page 127. Three subsequent occurrences in the prose and line-module displays are printed \(N_{Y/S}\). The mathematical line module in this construction must use \(N_{Y/X}=I/I^2\). This is established directly from the displayed Hom in (6.8.3): for a locally free rank-\(d\) module \(N\),

\[
\mathcal Hom(\Lambda^dN,\Omega^d_{X/S}|_Y)
\simeq(\Lambda^dN)^\vee\otimes\Omega^d_{X/S}|_Y,
\]

with \(N=N_{Y/X}\). No \(N_{Y/S}\) is defined by this regular immersion, and \(Y\to S\) is not assumed to be an immersion. The high-resolution witness is `sga5_printed128_top_zoom.png`. Preserve \(N_{Y/S}\) if literally transcribing the print, and annotate the required \(N_{Y/X}\) reading; do not silently describe the original print as already consistent. Without the missing English master this review cannot determine whether its translation preserves or corrects those three source tokens.

## Exact dictionary to the packet's one-variable object

For the packet's retained monic \(H\in R[S]\) of positive degree \(q\), the affine factorization is

\[
\operatorname{Spec}B\xrightarrow{i}\mathbb A^1_R
\xrightarrow{f}\operatorname{Spec}R,
\qquad B=R[S]/(H),\qquad g=f\circ i.
\]

The monic polynomial is a non-zero-divisor in \(R[S]\): the highest nonzero coefficient of any nonzero polynomial \(P\) remains the highest nonzero coefficient of \(HP\), shifted by \(q\). Thus \(i\) is a regular codimension-one immersion. Division by the monic \(H\) makes \(B\) free with its retained ordered basis \(1,S,\ldots,S^{q-1}\), so \(g\) is finite flat, without requiring distinct roots. The ambient map is smooth of relative dimension one. These are the actual smoothness, regularity, and flatness inputs, not assumptions about a semisimple root decomposition.

The generator of \(I/I^2\) is \([H]\), and the source differential is exactly

\[
[H]\longmapsto H'(S)\,dS\pmod H.
\]

Writing the dualizing generator as the Hom sending \([H]\mapsto dS\), the class is \(H'\) times that generator. Therefore in the packet's coefficient-residue trivialization \(\lambda_H\), the source's formula is exactly

\[
\operatorname{Tr}_R(m_y)=\lambda_H(yH')
\qquad(y\in B).
\]

No factor \(2\pi i\), sign choice at infinity, division by \(H'\), or root-distinctness assumption enters the algebraic class. The analytic equality with positive finite residues requires the convention used by the packet; equivalently the coefficient of \(S^{-1}\) in \(P/H\) is the negative of the analytic residue at infinity. The parent task verifies the complete coefficient-residue proof and its orientation convention.

If \(R\) is noetherian, the above factorization lies directly within the source's §6 setup. For arbitrary \(R\), the explicit monic construction remains meaningful and finite free, but citing the noetherian source alone does not prove the arbitrary-base assertion. Its direct proof and base-change calculation in the packet supply that extension; no strengthening of SGA's printed hypotheses is asserted here.

## DLMF gamma product

The official [DLMF equation 5.5.7](https://dlmf.nist.gov/5.5.E7), within §5.5(iii), was opened directly. Its TeX endpoint was retrieved to `sga_trace_period_primary_evidence_20260913/dlmf_5_5_E7.tex`. It states

\[
\prod_{k=1}^{n-1}\Gamma(k/n)=(2\pi)^{(n-1)/2}n^{-1/2}.
\]

For the packet set \(n=d=q+1\ge2\). Every gamma argument is positive, so all factors and \(d^{-1/2}\) are positive real values. This is exactly `RESEARCH_NOTE.md` lines 453–458 and `NOTE.tex` line 687. It is also obtained from DLMF (5.5.6) with \(z=1/n\) and \(\Gamma(1)=1\). The generic symbol annotation “nonnegative integer” must not be used to insert \(n=0\), where this formula is undefined; the packet never does so. This real gamma product does not choose the unsquared contour-determinant phase; the ray order, orientation, and argument of \(u\) remain separate retained data.

## Integration disposition

- Accept the SGA residue/conormal citation with printed pages 127–129 added as the independent primary receipt.
- Keep the source's missing-proof qualification and the packet's complete direct one-variable proof.
- Keep the noetherian source scope explicit. Attribute the arbitrary-base extension to the elementary finite-free calculation.
- If adding a literal source transcription, annotate the three printed \(N_{Y/S}\) occurrences on page 128 as a conormal-index typography issue; use \(N_{Y/X}\) in the actual mathematical map.
- Do not claim that this independent review reread the missing exact English master, or that the full étale/correspondence corpus was reaudited.
- Accept DLMF (5.5.7) as cited. No determinant normalization or phase change follows from it.

The companion JSON records source hashes, scope, exact selected primary pages, evidence hashes, and the remaining exact-master provenance limitation.
