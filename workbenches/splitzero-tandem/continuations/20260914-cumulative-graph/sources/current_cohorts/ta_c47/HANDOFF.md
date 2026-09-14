# Full TA and C47 source staging

The manifest inventories two exact-byte complete repository snapshots and 12 complete prepared source bodies. Prepared bodies preserve every byte except explicitly mapped TeX label/ref namespace edits. Every inverse is recorded and checked. No original is edited and no PDF is built.

TA and its full independent review come from the sealed Actual Source and Metric Addendum. All eight addendum source bodies remain in the snapshot for provenance; only TA and TAReview are proposed as readable routes here. Existing v22 TA routes should be reused by exact original-body hash when already included.

C47 includes TC followed by WB, WBR, CH, TR, TT, GF, TCReview, RootAcceptance and GFR. Preserve the entire C47 repository, including both inherited dependency levels, exact rational replay, calculation certificates and original conversion records.

The standalone inclusion recipe is INCLUDE_ALL_COMPLETE_BODIES.tex, resolved from this staging root. The global builder should rebase its input paths and apply the listed local macro context; it must not import the old document wrappers or standalone font setup. C47 display tags TR1–TR23 have two source bodies, so cumulative citations need a body name.

| Role | Original SHA-256 | Prepared SHA-256 |
|---|---|---|
| TA | `a0ece9f6049a982e06c28b38c61e39cf7571632432bbb17deb5e73b5ff7736c1` | `4667eef2ac13f9d1057b3960c275de4eb5c1aa056c8156a4c3302bd652465c3b` |
| TAReview | `c22ab8b7f20b5bbbef469bf86e0ec7d0a566f9b3dc2abf9f1721c171e8f8892f` | `c22ab8b7f20b5bbbef469bf86e0ec7d0a566f9b3dc2abf9f1721c171e8f8892f` |
| C47_TC | `3996ab65e1b73d028f72475441f94b98f7508e1d57e4deee6a04d79c23ac826a` | `3996ab65e1b73d028f72475441f94b98f7508e1d57e4deee6a04d79c23ac826a` |
| C47_WB | `fee19447b01eb14e22d164ec18ed105fe052d71fea52f2ad977b16a28370ac85` | `6b876c26704edc8bbf5b18b9852cd12d3d451d95d643f7ee85654be2be17fd6a` |
| C47_WBR | `45236acf7bb0d9192329c506c2233d51a391d851d4e3f5af204d16d3cb5c0aff` | `f3e92fd13c644a9791d0d7be964ff6728d4d598e7fcf404aa051550f055a6b3c` |
| C47_CH | `d86513eedf16004f9261ef79cabc007f57392fd422b10120ee72a17cb431415c` | `98b7b150e7e433072143899e2be70ece95e8debc0152f5ec1bcc665cc28d6034` |
| C47_TR | `5134c15bcc6b0ce840f797c2f3965219546d86f46e0f964132875da4a288e51e` | `cac6c5f735183040f16f8ea91659edcdd04dcc188cdd638fb9951914d6d74e1c` |
| C47_TT | `cb7438d8e400680ab61b2f43fe9de06276d223a54f62b27fc3a6aabe9dd7c2cf` | `9a0b385fb361665ece8707c1f512cdc369850ca4099ffaf47a8d337dbb857c90` |
| C47_GF | `62aa49e0f6dad4e41bd74e04df029763d0a2fb8e82b4e4b13d88279e0859bdca` | `62aa49e0f6dad4e41bd74e04df029763d0a2fb8e82b4e4b13d88279e0859bdca` |
| C47_TCReview | `453249bf3741023de560798b46023776263a8ff67524d8f01d059974b3744374` | `d97be63f233739058a3a4c03f1e6921ebdc8bda4c4885a9128ca80a3e3a39361` |
| C47_RootAcceptance | `3c4f9bca0581d680a4deb2ce202766a96f0aa72ff43dfa224ea3f282e8f01f5d` | `e01630dfd12c6d81c6a77cc8b74a8270c4c6a1ef3f88b77fa626fec93ae0003e` |
| C47_GFR | `5aaf0006058e4e9755a4e38a2769e30aea954e437c9b438b9f79e97545e10483` | `4f1d0c39c36930529d9211e0f7f1f6527dc18fe6e2975cb9d1a963528bf34a6e` |

CF aliases are only proposed below when exact equality was measured:

- C47_TC → CF:TC: exact byte equality = True; candidate SHA `3996ab65e1b73d028f72475441f94b98f7508e1d57e4deee6a04d79c23ac826a`.
- C47_WBR → CF:WBR: exact byte equality = True; candidate SHA `45236acf7bb0d9192329c506c2233d51a391d851d4e3f5af204d16d3cb5c0aff`.
- C47_GF → CF:GF: exact byte equality = True; candidate SHA `62aa49e0f6dad4e41bd74e04df029763d0a2fb8e82b4e4b13d88279e0859bdca`.

Read audit/C47_INCLUSION_AUDIT.md for exact dependency and current-text propagation edges. This package establishes complete staged inputs; root edition work must apply accepted mathematical replacements at their earlier and downstream locations.
