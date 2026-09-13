# Source review and access record

## Read directly through the GitHub connector

1. Main branch metadata at `fa4be32f87a9a90f3c02a07f7790dea95a1e7b0f`.
2. Open PR collection and PR #22 metadata, head
   `811210d24b80813a08972ca23f919db015383137`.
3. Full `workbenches/tau-exterior-trace-formal/RESEARCH_NOTE.md` at that head,
   reported blob `3662efb29c4353f6e50b94601a30eeb4c256ec00`.
4. Lines 1--220 of
   `workbenches/splitzero-tandem/continuations/20260912-stieltjes/tex/theta_gamma_reference.tex`
   at main, reported blob `89cee46828a36df716a8f4610098e922bdd055ec`.
   This includes the arithmetic multiplier and complete gamma constants,
   generating integral, polynomial norms and recurrence. It is not a new
   verification of all chapters in the reader.

The connector read succeeded. Separate attempts to save remote raw bytes from
this container failed DNS resolution. Therefore these remote blob identifiers
are reported from the connector, not claimed to be independently verified
against a local raw-file copy. No remote source corpus is bundled here.

## Read locally

The supplied Toda NOTE.tex was read in its sections 2--8, together with its
complete handoff, archive manifest, checker and selected build sources. The
35 manifest entries were checked against the actual extracted bytes. Its
24-method checker passed in both normal and optimized Python. These are the
reproduction scopes, not an independent proof of every analytic sentence in
all preceding packages.

## Outside references

DLMF sections 18.23 and 18.22 were consulted for the classical generating
function and recurrence. Koelink and Van der Jeugt's original convolution
paper (arXiv:q-alg/9607010) was consulted at its abstract/bibliographic entry
to identify the general background, not claimed read in full. The specialized
projection and coefficient identities in this continuation have direct proofs.

## Publication capability

The active GitHub connector exposed read actions. A write-action discovery
returned no creation action; plugin discovery confirmed the installed GitHub
connector but exposed no alternative write tool. This runtime has no GitHub
CLI and its external raw-byte requests failed DNS resolution. No authenticated
remote write, commit or pull request was made. The patch is an explicit
add-only local artifact, not a claimed remote update.
