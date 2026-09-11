# Split-support Rees trace workbench

This is an isolated research continuation for the Zeta workbench. It adds no claim to the existing reader and does not change the frozen editions. Begin with [RESEARCH_NOTE.md](RESEARCH_NOTE.md).

## Results added here

- Functorial comparison defects over the existing support diagram, with strictness of actual mixed-support synchronization.
- Exact composition and Ext-dual residue pairing for a Rees defect.
- Tensor, symmetric, and exterior-power defect lengths for every degree; a proved sublinear-bound vanishing criterion.
- A graded determinant which equals one after forgetting the grading, while its first grading derivative recovers the defect trace.
- Coupling of that grading to the actual prime norm, including ramification, followed by all archimedean/discriminant factors and the completed zeta test-function trace.
- A supported-null first jet which retains the logarithmic derivative instead of replacing a supported cancellation by external absence.

The uniform-shift arithmetic family is constructed in the note. It is not asserted to be the unidentified global compact-support/ordinary-cohomology comparison, nor is an RH-relevant sign or sublinear bound asserted. Novelty and independent review have not been established.

## Run the exact checks

From this directory:

```bash
python checks/check_rees_trace.py --output checks/local-results.json
python -O checks/check_rees_trace.py --output checks/local-results-optimized.json
```

Python 3.13.5 and SymPy 1.14.0 were used. The recorded run has 2,085 exact finite assertions in nine suites. There are no floating-point zero-location tests. Normal and optimized outputs were identical. Failure conditions use explicit exceptions, not assert statements. General theorems have written proofs; these finite instances are not formal verification of those proofs or of RH.

## Integration map and source basis

Inspected base: `42d00e359b16d52ca71568ce5e3db5341949d929` in `KokunoYumeto/zeta-function-research-reader`.

- `satellites/14_globalization_cue_split_zero_and_shifted_sheets.tex`, Git blob `49318a578b96462384000afa16794cfd5fe492c1`: the support character and the equivalence between split-zero semimodules and linear join diagrams. Relevant lines 135-374 were read directly.
- `satellites/15_divisor_sheaves_artin_chains_and_packet_descent.tex`, blob `46cfffde09bb0e2b21458590d1a199f8eb19625c`: the beginning fixed-pair and sheaf construction, and its interfaces with retained jets. This continuation does not replace its higher origin data by repeated scalar adjunctions.
- `satellites/17_centered_packet_products_and_global_zeta_factorization.tex`, blob `31d3bbce031bfc7d9aaf16b47c1533211cee6009`: lines 764-922 give the compact-uniform logarithmic derivative and multiplicity residues. Section 8 of this continuation connects its first variation to those existing packet coordinates.
- `satellites/19_primitive_defect_source_audit.tex`, blob `6531b5b35225acfcb6c4dd112f4e08ee43974084`: selected final interface statements were inspected, not the entire chapter independently audited.
- The corresponding uploaded source-archive copies of all four chapters match those Git blob identities.
- Conversation predecessor: *Split support, adelic filtrations, and the comparison image*, 11 September 2026. Complete TeX read; SHA-256 `a5060dc4ed7581ec6e58aa28b642c448142c9f948d764645dee91417410df77f`.
- Chen--Moriwaki, *Positivity in Arakelov Geometry over Adelic Curves*, 2024, particularly the HN and spectral-norm formulas already cited in the predecessor. The attached corrected book gives the arithmetic input; its full contents were not reread for this note. DOI `10.1007/978-3-031-61668-6`; related preprint `arXiv:2207.02033`.
- The supplied Weil II TeX excerpts for sections 3.3.4-3.3.6 and 6.2.4-6.2.6 were reread. Their historical-transcription status is retained. No new PDF extraction or OCR was used.
- Cogdell's *On Artin L-functions* and Connes--Consani--Moscovici's *Zeta Spectral Triples*, section 3, supply the established arithmetic completion/explicit-formula inputs, with their displayed factors retained.

The attached predecessor has fuller adelic estimates. This addition includes the definitions needed for its new proofs; it does not bundle protected literature.

## Contribution and publication boundaries

Research direction and split-support framework: KokunoYumeto. Derivations, exposition and executable finite checks in this addition were developed in the present ChatGPT session. This is tool-assisted mathematical work, not an independent external review. Existing source attribution and repository rights remain intact.

No primary-literature PDFs, raw conversations, private paths, credentials, or unrelated project data are included. No blanket license is asserted over third-party material. The parent reader, accepted claim ledgers, schedules, other branches, and existing pull requests are untouched. This contribution is for a draft pull request, not an automatic merge.
