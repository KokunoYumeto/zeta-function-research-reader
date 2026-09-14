# Concurrent main integration

During this continuation, main advanced to `e4ee97cdce904d4b9bb5697d33095aaa00083f24` and incorporated the PR26 restriction work. That change was observed when draft PR27 was opened. The original comparison against `1f7e7c02343884a17df9873566e81a9083c70951` had 41 additions because it still counted PR26's 26 added files.

The final integration uses the complete tree of main `e4ee97cdce904d4b9bb5697d33095aaa00083f24` as its base and adds only this continuation's 15 files plus this coordination record. It preserves every current-main publication, index, archive and workbench file rather than restoring older versions of those files. The branch merge records both histories without force-updating any ref.

The current-main `formal` tree `766a67b32d629424d7b92aaaeffd20057569f46b` and `.github` tree `a282020549e29342eab88a24f85a6049b70cd0c4` are exactly the already inspected PR26 trees. Its consecutive-window and restriction workbench trees also match the inherited verified snapshots. The newly added specialization workbench did not exist on main. Thus the inherited formal sources and both dependency pins are unchanged by this integration.

All five new Lean blobs, both audit files, both new checkers, and the workflow are the exact bytes from the successful source checkpoint in `STATUS.md`. The verified run remains `34735210715` at source commit `25960903723954d6118b1aa76a817cb6a7f452f0`. This coordination update does not claim that an unobserved later workflow has completed.

PR27 is a draft. This session has not merged it, changed main, or rewritten any earlier PR branch. The resulting diff against the concurrently updated main is intended to contain only the 16 new continuation files; its final GitHub comparison is checked after the branch update. Historical checkpoint references in the other notes remain valid and identify their original verification context.
