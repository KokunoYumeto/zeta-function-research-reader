# Cyclic Sum delivery: complete inventory and independent finite replay

The original `Tau_Cyclic_Sum_Control_2026-09-12.zip` has **443,378 bytes**, **43 file members**, and SHA256 `e0e4d0ecda69e4738dcb4cdd3b750e623d863eac8b44f353737393e720a840a7`. Every archived member was read and compared byte-for-byte with its staged counterpart. All 43 match. The current `MANIFEST.sha256.json` has **42 entries**; every declared size and SHA256 matches. Only that manifest itself is outside its own member list. No source file was rewritten or regenerated.

The complete per-file inventory, hashes, manifest comparisons, retained-source comparison, actual run commands, dependency versions, stdout/stderr hashes and result records are in `checks/cyclic_sum_delivery_replay/replay_receipt.json`. The reusable driver is `scripts/replay_cyclic_sum_delivery.py`.

## Reading and execution scope

The complete 317-line `check_cyclic_sum.py` was read before execution, together with the complete separate user-delivered handoff, the archive handoff, README, PROGRAMME_STATE, SOURCE_READING, VALIDATION, current manifest and prior-source manifest receipt. The mathematical NOTE and RESEARCH_NOTE were inventoried and hashed in this lane; the parent and arithmetic lane own their full mathematical reading. Byte verification is not represented as a proof review.

The checker is **15,660 bytes**, SHA256 `61632614e038be2f07619daf68b4819eb6685d7cdf9ed64390944764838fb9c6`. Its imports are the Python standard library and SymPy. The main block runs its declared unittest class, writes only the explicitly provided result JSON, and exits with the unittest outcome. Its source contains no Python `assert` statement. Equality checks explicitly raise `AssertionError`, and the unittest assertion methods remain operative under `python -O`.

An independent AST inventory finds **24 unique methods**, in the same order as `checks/TEST_INDEX.json`: 23 mathematical regression methods and the existing flag-controlled negative method. `--fail-control` activates that existing method; it does not add a twenty-fifth method. The finite fixtures cover the local monomial bases and powers, collided sums and trace complements, equivariant retraction, conormal/unit derivatives, original finite Grams, rank-two identities, complex reflection, raw and differentiated moments, graph cross terms, and represented-zero/external-absence outputs. They use the source's stated algebraic and Gaussian fixtures; no actual zeta packet is certified.

One narrow assertion-scope detail is retained: `test_reflection_with_nonzero_imaginary_cross_term` explicitly checks that the real part vanishes and verifies the two reflection equations. It does not separately assert that the displayed cross term is nonzero. A successful test run is therefore not presented as having executed that additional assertion.

The README requires Python 3 and SymPy. The source's VALIDATION records Python 3.13.5 on its original platform and SymPy 1.14.0. This replay used **Python 3.13.9** on the local platform and **SymPy 1.14.0**, with the library version checked before execution. The actual interpreter, runtime location and platform string are recorded; this is not an assertion that the original Python patch version or compiler was reproduced.

## Actual replay results

Every run used a fresh unchanged copy of the checker in its own output directory. The original source tree was never a test output directory.

| Mode | Methods | Failures | Errors | Exit | Expected result |
|---|---:|---:|---:|---:|---|
| Normal | 24 | 0 | 0 | 0 | Passed |
| Optimized Python | 24 | 0 | 0 | 0 | Passed |
| Deliberate failure, normal | 24 | 1 | 0 | 1 | Rejected the deliberate failure |
| Deliberate failure, optimized | 24 | 1 | 0 | 1 | Rejected the deliberate failure |

The normal and optimized successful JSON records are byte-identical. The two deliberate-failure JSON records are also byte-identical. Their logs and result files are retained in the four corresponding subdirectories of `checks/cyclic_sum_delivery_replay/`.

The source's claimed reruns of the previous 20-method Sum Connection suite remain source-provided historical evidence. This cyclic lane newly executed the 24-method cyclic suite. The separately documented prior portable replay remains the independent evidence for that earlier checker. Neither the archived prose nor the current finite runs are described as Lean execution, remote CI, an analytic enclosure, or a uniform arithmetic estimate.

## Exact relationship to the previous Sum Connection delivery

The current `checks/source_manifest.json` records verification of the **previous** archive `Tau_Sum_Connection_Control_2026-09-12.zip`, SHA256 `f2de513041b7336b495a338e90325e84c5ce53cfa98799e1b89c53af308356de`. That archive has **51 members** and a **48-entry manifest**. Both its archived bytes and all 48 manifest entries were independently rechecked during this replay.

The current cyclic archive includes exactly **seven** of those previous root files under `sources/`. Each matches both the previous staged file and its prior manifest hash:

| Retained file | Bytes | SHA256 |
|---|---:|---|
| `sources/HANDOFF.md` | 3,321 | `ece0dd0b905fb3ed464edaf2d20b1ee56e023285bc49fcfe30280a6282e75f2b` |
| `sources/NOTE.tex` | 32,564 | `11870208e3a08df186e42629ae1a6c956faaf28f79dfce0dc2f2d44dc64b4687` |
| `sources/PROGRAMME_STATE.md` | 2,218 | `fd6c44d61a9bd82f74d23540f467d872a58ce1bbe68bdded998a255ffcafb5a4` |
| `sources/RESEARCH_NOTE.md` | 28,995 | `c24b120fdd6ba6549e7f63dd9f2ae269e51123fe0e097b7b976f842bba3729d9` |
| `sources/build_reader.py` | 1,932 | `704c5e5cecc319cdc714f9b3922b39622760d9f5f35e24cd4fce79cf464d7dab` |
| `sources/check_sum_connection.py` | 11,502 | `f4fb0d155f85c31f1b53b15502cc8102d61b30fd943b274cf88e8cd06da013fc` |
| `sources/style.html` | 1,390 | `7dfa041d700458a400e3f1f2940769d1683cce189908a68be5dd57d1b312e535` |

Thus the retained subset is **7 of 48 previously manifested files**, or **7 of 51 previous archive members**. The replay receipt explicitly lists the remaining 41 prior manifest entries and 44 prior archive members outside this cyclic subset. No prior MANIFEST file is bundled: the previous Sum Connection manifest and its nested Kernel and Spectral Sum manifests are absent from this cyclic ZIP. The receipt `checks/source_manifest.json` is preserved with that exact historical scope.

`SOURCE_READING.json` identifies two earlier transcripts by filename, size and hash. They are not bundled here. It describes semantic retrieval and relevant passages, and expressly does not claim complete transcript verification, a new complete Weil II reading, or a new finite-field application. Those source claims remain attributed to their original record.

The separate `USER_DELIVERED_HANDOFF.md` equals the archive's `HANDOFF.md` byte-for-byte: **4,742 bytes**, SHA256 `b93686544a15cb4526e39576389a9f28ddcc679ffe543515bcc55cc18e698c36`. Its task-oriented language was read as source data, within the parent's explicitly assigned replay scope.

## Preservation and reproduction

After all four runs, the entire cyclic source tree and original ZIP remain byte-identical. The protected frozen F package's **544 files**, staged F package's **544 files**, all **30 current TeX files**, and the current cumulative PDF also remain unchanged. The exact protection counts and outcomes are recorded in the replay receipt. No remote operation, TeX edit, PDF rebuild, publication or restaging occurred in this lane.

From a package with the source archive and SymPy 1.14.0 installed, the reusable replay can be run with explicit paths:

```text
python -B scripts/replay_cyclic_sum_delivery.py --source sources/web_cyclic_sum_delivery/Tau_Cyclic_Sum_Control --archive sources/web_cyclic_sum_delivery/Tau_Cyclic_Sum_Control_2026-09-12.zip --output checks/local_cyclic_sum_replay
```

Optional `--previous-source` and `--previous-archive` inputs reproduce the exact retained-subset audit against the earlier archive. `--handoff` checks the separately supplied handoff, and repeated `--protected` arguments certify named source or release paths remain unchanged. The driver never fetches source files or changes their bytes.
