# PR31 and the original joint-Schur return

`JOINT_SCHUR_RESOLVENT_APPLICATION.tex` is the complete new written application, JRA1–29. It constructs the eight original coefficient blocks, their direct-sum metric, the determinant character giving the four-endpoint Gamma return, the simultaneous metric isometry, the centered finite-resolvent interval, the closed integrated finite center, and a finite stopping integer. It retains the raw/divided derivative factorial map, full source masses, original relation correction, cyclic inclusion, and labelled coefficient maps. This application has not been compiled as a Lean declaration.

`SCOPE_REVIEW.md` records a complete independent reading of the five downloaded Lean proof bodies and both complete research/status documents. `APPLICATION_REVIEW.md` records the independent reading of JRA1–29 and the current proof hash. The fetched GitHub sources remain unchanged under their repository paths.

The snapshot is PR31 head `b4060b25c21f1a49a5e7730e9aff76d4c93c820d`. The live PR was open and draft when read on 14 September 2026. Its implementation commit `04ef2f962d69186ef48f07679a339b57486ef471` and successful run 34797644407 match the incoming report. The comparison from that implementation to the final head changes only the workbench README and STATUS.

There is now directly observed successful verification at the final head itself: [signed-resolvent run 34798302998](https://github.com/KokunoYumeto/zeta-function-research-reader/actions/runs/34798302998) concluded successfully. Its finite job 103835635107 completed at 02:13:46 UTC and verify job 103835635284 at 02:17:29 UTC. The API reports 18 final-head runs, all completed successfully; this intake inspected the signed run's actual compiler, audit, test and negative-control records. It does not claim to have reread all setup/cache/post-job lines or all logs of the other 17 workflows.

The signed-run log records 33 distinct local sources checked with `--trust=0 -DwarningAsError=true`, 60 distinct selected axiom reports, finite suites of 9, 8, 10 and 24 methods in both normal and optimized modes, and each of the five named mathematical negative controls rejected in both modes. Those are observed remote records. No local Lean/Lake/Elan process or checker replay was launched for this intake.

`FETCH_RECEIPT.json` pins the eight retrieved source/document files by Git blob and SHA256. `CI_OBSERVATION_RECEIPT.json` pins the decoded final-head signed log and the exact observation scope. Raw API responses and the full decoded log are retained. No remote mutation or new PDF build was performed.

The new integrated radius is for the specified packet and degree. Its positive constants are computed from the actual joint-Schur blocks. The calculation proves a finite stopping rule and a literal return to the original quotient determinant; it does not replace the remaining growing-family estimate by a constant assumed uniform in degree.
