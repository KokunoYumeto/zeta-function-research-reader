# All-degree angle transport for the original arithmetic four-volume

This folder supplies the full AGT1–AGT19 calculation as a five-page readable PDF and editable LaTeX. It preserves both complete principal-angle lists, the original relation-energy matrices, moment positivity, source masses and signed determinant expression. The nonlinear endpoint calculation applies in every quotient degree, with the original coefficient m=2q−1.

The editable entry point is `Tau_All_Degree_Angle_Transport.tex`. The complete body is `proofs/AGT.tex`; `originals/AGT_original.tex` preserves the corrected original byte-exactly. Its declared cutoff is q−1≤N≤2q in the fixed common source. The only body typography change supplies a plain-text bookmark for an identically displayed mathematical heading. Full inverse records are in `evidence/BODY_EXTRACTION.json` and `evidence/LAYOUT.json`.

The complete independent AA1–AA44 proof and acceptance are retained in `evidence/`, including the explicit original theta primitive and tensor differential signs. The complete supplementary PA1–PA29 proof is retained separately. Its receipt uses a portable source locator; the exact metadata transformation is recorded. These are full written proofs rather than acceptance summaries.

The full sealed 65-file AW package is retained byte-exact under `dependencies/Tau_Relation_Window_Spectral_Transport`. It contains the unchanged 49-file AT package and all 29 complete original proof dependencies. `dependencies/AGT_DEPENDENCY_CROSSWALK.md` locates the inherited proofs and preserves the recorded historical source distinction.

Run `python build.py` with a LaTeX distribution to rebuild the main PDF. All five pages were visually inspected, all 19 equation tags are present, the complete source inverse passed, and the final build has zero warnings. No mathematical checker or Lean process was run for this companion. `SOURCE_GUIDE.json` gives complete proof routes; `MANIFEST.json` pins every delivered payload except itself.
