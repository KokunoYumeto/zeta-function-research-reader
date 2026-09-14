# Bounded source compile check

The complete editable `Original_Observation_Addendum.tex` entry passed two XeLaTeX runs with `-no-pdf -interaction=nonstopmode -halt-on-error -recorder`. Both returned exit code zero. The engine was XeTeX 0.999998, MiKTeX 26.5. All nine relative proof input files were read successfully. The second run produced a 21-page intermediate XDV and completed without missing inputs, undefined commands or unresolved-reference warnings.

The check intentionally produced no addendum PDF. Its XDV and build files stay in the mathematical work folder's `original_observation_20260914/compile_check`; the main Cut 22 PDF and its visually checked layout remain unchanged.

Two layout warnings remain in byte-exact historical proof spans: IGO1–3 line 55 (7.14441 points) and IPM1–7 lines 32–45 (27.74944 points). These are recorded for any later PDF typesetting pass. This source check makes no visual layout approval claim. The complete new OPG and OPR sections produced no overfull-box warning in this run.

The separate `verify_sources.py` check verifies every staged provider hash and byte count, each exact proof slice against the included full original, and every relative entry input. Mathematical proof acceptance is recorded in the independent review and the root's complete proof read.
