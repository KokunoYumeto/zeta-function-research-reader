# Current primary-source correction for the Deligne comparison

13 September 2026. This addendum supersedes the earlier claim that the final citation in Weil II §3.7.4 has an unresolved internal numbering mismatch. It also records which displayed typographical features belong to the printed source. The original delivered exponential note, S20 records, historical TeX, 84-file intake manifest and XD1–26 proof remain unchanged.

The Zeta literature task's complete primary review, `DELIGNE_PRIMARY_REVIEW_20260913.md`, is retained byte-for-byte in the accompanying `primary_source_evidence` folder. Its reviewer visually read complete Weil II printed pages 178, 202, 203, 206, 215 and 216 from the official Numdam scan; page 216 received a higher-resolution check. A bounded collaborator checked complete Weil I printed pages 305–306 and the exact cited passage. This addendum records that completed primary review; it does not relabel those inspections as a new full-paper audit performed here.

## Resolved citation and printed typography

The final reference in Weil II §3.7.4 is **(I.8.11), with Roman I**. It refers to **Weil I §8.11, printed page 306**, rather than to Weil II Corollary 1.8.11. Weil I §8.10 reduces the calculation to one variable and the monomial \(Q=x^d\); §8.11 treats that case, and §§8.12–8.13 continue the Euler-characteristic calculation. The previously asserted internal numbering mismatch is therefore resolved. This identification does not assert that §8.11 alone states the entire later general purity theorem. Sources: [Weil II, printed page 216](https://www.numdam.org/item/10.1007/BF02684780.pdf), [Weil I, printed pages 305–306](https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf).

The printed page 216 itself says \(S'_0\) in the connectedness sentence. The parameter sheaves in the preceding construction are on the good open \(S_0\). That open is connected: the affine parameter space is irreducible, its stated open is nonempty, and a nonempty open of an irreducible space is irreducible. Retain the literal printed prime as source typography while using the explicitly specified good parameter open in the mathematical application.

The high-resolution printed display also repeats the final proper direct image: its three terms are

\[
R^if_!\mathcal F_0(\Psi Q_S)
=R^i\bar f_*j_!\mathcal F_0(\Psi Q_S)
=R^i\bar f_*j_!\mathcal F_0(\Psi Q_S).
\]

Both final terms have \(\bar f_*\). The equality \(\bar f_!=\bar f_*\) available for a proper map can explain an intended intermediate step, but replacing one printed star by an exclamation mark would be a reconstruction. It is not a literal correction of what the scan shows. The repeated display and the prime are present in the printed source, rather than established errors first introduced by S20.

## Inequalities, tensor powers and mixedness

The fresh printed-page check confirms **strict weight \(<2\)** in Lemma 3.2.10 on page 203. The strict sign must remain when combined with integer weights. Section 3.2.13 on that page uses **\(w_q(\alpha^2)\)** and then divides the resulting bound by two. It is the tensor square of the same eigenvalue. The older typed witnesses that lost the strict sign or the square remain historical witnesses, and those losses must not enter the current proof. [Weil II, printed page 203](https://www.numdam.org/item/10.1007/BF02684780.pdf).

Corollary 1.8.12 on printed page 178 requires a **lisse \(\iota\)-mixed sheaf on a connected scheme of finite type over the finite field**, pure at one point. It concludes pointwise purity. Normality is not a hypothesis of that corollary; mixedness is. Constant rank alone does not supply its hypotheses. [Weil II, printed page 178](https://www.numdam.org/item/10.1007/BF02684780.pdf).

The verified exponential theorem (3.7.2.3), printed pages 215–216, applies to the actual specialized potential \((\Phi-tS)/u\): its degree is \(d=q+1\), its leading coefficient \(1/(du)\) is a unit on the stated open \(u\ne0\), and the assumed residue characteristic \(p>d\) makes \(d\) prime to \(p\). Its leading projective zero locus in \(\mathbb P^0\) is empty and smooth. Thus the finite-field compact-support cohomology is concentrated in degree one, has rank \(q\), and is pure of weight one. Repeated roots of \(\chi\) do not obstruct these hypotheses. Lemma 3.7.3 supplies lissity on the stated good open through its compactification and local-acyclicity calculation, including infinity. These remain applications of the exact historical theorem, with no identification of its Frobenius with the original arithmetic sum operator and no new theta-norm estimate.

## Retained evidence and scope

The official Weil II scan inspected by the owner has 13,547,082 bytes and SHA-256 `b06eea61bf9cb2b596c162f5befcf85d1be69828910a6107c8aa3a99c4afcc71`. The Weil I scan has 3,582,172 bytes and SHA-256 `8392b345d4854e6dc55fb42cfc0b616d941935983723627237239a87348f42e5`. The publication evidence contains the complete written review, URLs, hashes and exact inspection scope; it contains no scan or rendered-page copy.

The companion `SHARED_PERIOD_MAPS_REVIEW.md`, exact checker and six supplied execution receipts retain the owner's separate complete review of XD1–26 and DT1–13. That review reports twelve independently written finite test methods passing normally and under `-O`, and two false formulas failing in both modes. They are owner-executed evidence; no replay or new execution is claimed in this correction. The general proofs remain the complete written XD and DT sources.

For current reading, apply this correction wherever the earlier intake or delivered source review says that the terminal citation is unresolved. The previously sealed artifacts preserve their historical claims; this dated addendum supplies their explicit current correction.
