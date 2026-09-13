# Source review and reconciliation

## GitHub read in this continuation

- Default main was read at `b32ca2128e0deb0eec6eafb860776a5d6a28dcbb`.
  Its metadata records the merge of PR #22. This is a read of the current
  repository and merge description, not a new execution of its Lean audit.
- PR #23 was read at head `c720f40530eed2f5969dbabe94dfd3fddc0f507f`.
  Its body reports a successful strict run. The complete
  `workbenches/tau-toda-volume-formal/ENDPOINT_CRITERION.md` was read through
  the connected repository. Its blob is `aa2f449a8829532672dc308282446ad3b24bb54f`.
  The user-supplied 353-line report was also read. This note uses its endpoint
  selection theorem with its original attribution and proof scope.
- PR #24 was read at head `dfcbba5cbf7fec8c9301fe242c13e741d762013e`.
  The displayed full research note was read, including raw derivative factors,
  source-to-relation positivity, the fixed-width determinant, phase solve,
  and distinction of the norm helper from the actual conormal quotient.
  Its endpoint factors are integrated explicitly in NOTE equation (42).

Retained corrections: the exact quartet count is for that packet, not for a
larger packet containing it; h=1 is a zero finite arithmetic packet; the
second exterior operation has its stated multiplicity cost; a finite Gram or
transfer inverse is not a uniform estimate; the Taylor-unit derivative remains
in the ambient target. The current work performs no remote edits.

## Actual Deligne source access

All six user-supplied S20 part ZIPs were opened locally. Each chunk matched its
PART_INFO checksum. Concatenation produced 216,580,466 bytes, 312 ZIP members,
and SHA-256:

`e2005bf31e1fcf362765f73c315c855e0f504f24f34d3a0ab188049da522b7c8`

The archive's current `edition/source_language.ndjson` and
`edition/english_standalone.ndjson` were read for printed pages 158, 202--204,
and 206 (also p.156 for context). Their text is user-supplied transcription,
not new extraction or OCR by this session.

The nested `salvage/30_ZERO_ACCEPTED_DEDUP_PRIOR_WORK_DELIGNE_D032.zip`
contains the actual prior TeX. The following passages were read directly:

- `zenodo_record_21807212/evidence_members/fr_seg1.tex`, lines 610--637,
  including Definition 1.3.5 and the determinant/rank operation.
- `zenodo_record_21807212/evidence_members/fr_seg2.tex`, lines 840--874,
  including Lemmas 3.2.10--3.2.12 and the tensor-square step 3.2.13.
- The same `fr_seg2.tex`, lines 935--943, Corollary 3.3.6.
- `older_preserved_20260531/members/tex/032_Deligne_The_Weil_Conjecture_II_EN_source_checked_corrected.tex`,
  lines 715--737 and 1988--2028, corresponding determinant and estimate passages.

The nested directory is explicitly a retained prior/salvage source. It is not
silently preferred over the controlling current edition.

### Genuine transcription discrepancies retained

1. The older French TeX states `<=2` in Lemma 3.2.10, and repeats `<=2` before
   inferring `<=1` from integrality in the next proof. The current French
   page-local record at p.203 says `<2` in both places. The strict bound is
   necessary for that implication.
2. The older French last sentence in 3.2.13 substitutes an unsquared eigenvalue
   inequality before the improvement. The current p.203 record explicitly has
   `w_q(alpha^2)<=2+2^(-k)`, then `w_q(alpha)<=1+2^(-(k+1))`.
3. The older English TeX has strict signs in the statements corresponding to
   3.2.11 and 3.2.12 where the current records retain non-strict upper bounds.

No old source file was overwritten. No newly scanned-PDF comparison or full
116-page audit is claimed. Source hashes and read ranges are recorded separately
in `checks/source-reading.json`; the external literature corpus is not republished.

## Preceding analytic package

The delivered Gamma Convolution Descent archive was opened. All 37 entries of
its manifest were checked against actual ZIP bytes. Its 17-method normal run
was executed again; the optimized-run status is recorded in CHECKS.md after
completion. Its math is not reclassified as new Lean verification.

## Outside mathematical inputs

The new proof explicitly uses the classical zeta functional equation and gamma
vertical-strip asymptotic (DLMF 25.4 and 5.11), the maximum-principle proof of the
annulus three-circles inequality, and the monic Legendre extremal formula
(DLMF 18.3/18.5). These were applied to the source's fixed arithmetic measure.
The local-mass argument, lower convolution bound and endpoint estimate are
proved in the new note rather than cited as results of Deligne or of the
formalization session.
