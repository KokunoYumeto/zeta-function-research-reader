# Source reading and integration record

## Scope of this turn

This is a selected primary-text reading followed by explicit calculations. It is not a claim to have audited all of Deligne's proof, the entire repository, or any new Lean run. The supplied LaTeX and page-local transcription records were used. No PDF extraction, OCR, or fresh inspection of the printed scan was performed.

## Verified source assembly

The six supplied `DELIGNE_D032_WEIL_II_S20_FULL_STATE_PART_01_OF_06.zip` through `06` packages were opened. Their contained binary chunks were checked against their declared lengths and SHA-256 values and joined in order.

- Joined size: 216,580,466 bytes.
- ZIP members: 312.
- Joined SHA-256: `e2005bf31e1fcf362765f73c315c855e0f504f24f34d3a0ab188049da522b7c8`.
- Exact per-part receipt: `checks/deligne-assembly.json`.

The current `source_language.ndjson` was read alongside the historical LaTeX inside `salvage/30_ZERO_ACCEPTED_DEDUP_PRIOR_WORK_DELIGNE_D032.zip`. The selected working files were `fr_seg2.tex` and `032_Deligne_The_Weil_Conjecture_II_EN_source_checked_corrected.tex`. The delivery retains hashes and reading ranges, not a republished literature corpus.

## Passages actually inspected

1. Historical French second segment, the portions of lines 700–985 displayed in the tool output: exceptional-fibre, constituent, tensor-square, and image arguments. Because one tool output was truncated, this is not claimed as a complete line-by-line audit of that interval.
2. Historical English TeX, lines 2160–2245: specialization, the beginning of the return to §1.8, and the exponential-family argument.
3. Current page-local French records for printed pages 201, 202, 203, 206, and 248, each read in full in the working session.
4. Current page-local French records for printed pages 215 and 216, each read in full, including a second direct read while finishing the new proof. These are the main new passages: §§3.7.2–3.7.4.
5. Historical French second segment around §§3.7.2–3.7.4 was located and compared with the current records. The earlier source-index and record filenames are hash-listed in `checks/source-files.json`.

6. In the final reading pass, current page-local French records 177–181 were read in full. Page 178 gives Corollaries 1.8.10–1.8.12, including propagation of pointwise purity in a connected lisse mixed family. Pages 179–181 retain the relative-monodromy filtration discussion; those results are read for context but not imported into the new algebraic proofs. Historical `fr_seg1.tex` lines 1215–1265 were compared with those records.

Further records 175–176 and 158–159 were extracted for navigation. Their extraction alone is not counted as reading each complete page.

## What the reading contributes

Pages 201–203 retain separate steps: the exceptional-fibre exact sequence, integer weights of nonconstant constituents, a strict bound below two, the vanishing of the specified first cohomology for constant constituents, and only then tensor improvement on the same eigenvalue. Page 206 retains upper and dual lower bounds meeting on the actual comparison image.

Pages 215–216 give a different concrete construction. Deligne attaches an Artin–Schreier eigensheaf to a polynomial Q of degree d prime to p with nonsingular leading projective hypersurface. He proves that its compact-support cohomology is concentrated in degree n, has dimension (d−1)^n, and is pure of weight n. He places these polynomials in a parameter space, proves lissity using local acyclicity on a compactification, and reduces through connectedness and Künneth to monomials. The new note constructs precisely a one-variable polynomial-exponential family from the existing cyclic relation and checks the hypotheses for its finite-field branch.

## Transcription qualifications retained

- In the older French TeX, Lemma 3.2.10 is printed with a non-strict inequality. The current page 203 record has the strict inequality needed by the following integer-weight step. The continuation does not use the erroneous non-strict transcription.
- The historical §3.2.13 loses the square on the tensor eigenvalue in one displayed account. The current source reading retains the eigenvalue-square operation.
- Page 216's current transcription writes `S'_0` in the connectedness sentence while the historical French has `S_0`. The new one-variable family has an explicitly described parameter open and is obtained by pullback of the lisse universal family; no new theorem is based on silently reconciling that transcription. No claim of a fresh visual scan check is made.
- There is also an unresolved internal cross-reference: the supplied §3.7.4 refers the final one-variable monomial case to (1.8.11), whereas its own printed page 178 labels a mixed-sheaf filtration corollary (1.8.11). I have not silently repaired that reference or claimed an independent audit of that final cited case. The finite-field application in the new note uses the displayed exponential-cohomology theorem (3.7.2.3), with all its hypotheses checked; the new characteristic-zero period proof is independent of that cross-reference.
- The current page 216 transcription repeats a pushforward expression. The argument used is the actual compactification/local-acyclicity mechanism and Deligne's stated lissity lemma, not the repeated typography.

## Predecessor and repository

The delivered `Tau_Deligne_Specialization_Curvature_2026-09-13.zip` is preserved. Its 41 manifest entries were verified. Its unchanged 23-method checker was rerun in normal and optimized Python; the resulting JSON records agree. This is distinct from the predecessor's claimed source-reading history.

Current GitHub main was fetched directly and was `1f7e7c02343884a17df9873566e81a9083c70951`, parent `952ef9fee1e1419b6858d920354de8fa99430b7d`, with message “Integrate endpoint and confluent-transfer proofs with the frozen Gamma companion”. The open-PR metadata still reports PR #25 at `66fac5e7885a40cd4873e74b754907320f05b067`. This turn inspected those metadata and the supplied full formalization reports, not the complete CI logs. Its certificate claims are retained as reported scope, not counted as a fresh execution here.

The norm and consecutive-window inputs retain their existing status. In particular the off-line four-volume lower threshold is four, not the earlier weaker threshold two. No upper bound contradicting it is inferred from the new geometry.

## Primary outside references

- Pierre Deligne, *La conjecture de Weil II*, Publications Mathématiques de l'IHÉS 52 (1980), 137–252, DOI 10.1007/BF02684780. Bibliographic record consulted online: https://www.numdam.org/item/PMIHES_1980__52__137_0/ . Mathematical reading used the supplied text as recorded above.
- The Stacks Project, Tag 0FMU, *Log poles along a divisor*, https://stacks.math.columbia.edu/tag/0FMU . The residue exact sequence and its coefficient-linear complexes provide standard background for the explicit logarithmic calculation.
- Marco Hien, *Periods for flat algebraic connections*, Inventiones Mathematicae 178 (2009), 1–22, DOI 10.1007/s00222-009-0185-7. The primary bibliographic abstract was consulted to attribute the established de Rham/rapid-decay framework. No claim to have read or reapplied the entire general proof; the note supplies the elementary contour argument it uses.
- Claude Sabbah and Morihiko Saito, *Kontsevich's conjecture on an algebraic formula for vanishing cycles of local systems*, arXiv:1212.0436. Abstract consulted only as context for twisted de Rham/vanishing-cycle machinery. No theorem from that paper is imported into the claimed results.

## What is not supplied by the sources

Deligne's exponential-sum purity controls Frobenius on finite-field cohomology. It does not identify the polar coefficient of this characteristic-zero connection with Frobenius, supply a uniform period-to-theta norm bound, or impose real part one half on the roots of an arbitrary polynomial. The rank-one calibration in the note retains this distinction through actual equations. The new period isomorphism is proved for u nonzero; its singular u=0 norm comparison remains unestimated.
