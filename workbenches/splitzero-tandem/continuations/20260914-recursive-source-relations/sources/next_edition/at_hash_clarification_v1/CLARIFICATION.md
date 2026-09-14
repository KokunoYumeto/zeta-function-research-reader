# Exact identification of the AT extraction hash

This additive record identifies a metadata-frame mismatch in the sealed Arithmetic Determinant Transport artifact. The complete accepted original, accepted reader, proof paragraphs, original preamble and all 23 equation tags remain unchanged.

The value `42b97470bfe0f67e0a0247e5cefcb95609c487b8ff20c275457aeebc02b7b706` in `evidence/BODY_EXTRACTION.json`, under `pre_layout_reader_body_sha256`, is the exact **final post-layout reader body in LF encoding**. Its byte count is 17149. The accepted reader itself has CRLF line endings and 17558 bytes. Replacing each CRLF in that accepted reader by LF gives the identified value exactly. The field name and its `hash_stage_note` therefore name the wrong processing stage. This record leaves that historical metadata untouched and identifies all four actual frames.

| Complete body frame | Bytes | SHA-256 |
|---|---:|---|
| pre layout LF | 17113 | `5ccb346f20b37ea30a40491a9c6ec84e7121869816efbb081007ae8f64cc9116` |
| pre layout CRLF | 17520 | `3ed5d0dbedbcaffdaa8949a4dc6108e99546acd3023c32c4785388860a5d1815` |
| post layout LF | 17149 | `42b97470bfe0f67e0a0247e5cefcb95609c487b8ff20c275457aeebc02b7b706` |
| post layout CRLF | 17558 | `9fa19a509edf91f5aa0a9cb4762485449196d0b1ff521f2445f791fa3290cc75` |

## Fixed sealed inputs

All paths in this section are relative to `Tau_Arithmetic_Determinant_Transport_2026-09-13`. Exact pins are retained in [CLARIFICATION.json](CLARIFICATION.json).

- `originals/AT_original.tex`: 17706 bytes; SHA-256 `24cf7ce5be6a43cc656641b516185df10b2e4d7824600ece657120d1c549deae`.
- `proofs/AT.tex`: 17558 bytes; SHA-256 `9fa19a509edf91f5aa0a9cb4762485449196d0b1ff521f2445f791fa3290cc75`.
- `evidence/BODY_EXTRACTION.json`: 19432 bytes; SHA-256 `b34076921f71b1a1a7d355ae88844b689771783966154eb68bcc7a9cc5a17ffb`.
- `evidence/LAYOUT.json`: 2700 bytes; SHA-256 `9f9cc79a2d6a6f9fb65e3b8d71b8f1e3dc8597ce883db8eecbfc9f2c78386d0f`.
- `MANIFEST.json`: 12833 bytes; SHA-256 `ef9b0517241fc770d22ec399388ba4e381309292067b8b6ae984898f05c1491f`.

## Exact original-file reconstruction

Every interval below uses zero-based byte offsets, with the end excluded. Concatenating the five components in order recovers all 17706 original bytes and the original SHA-256 `24cf7ce5be6a43cc656641b516185df10b2e4d7824600ece657120d1c549deae`. The complete original preamble and postamble are also retained literally in the JSON record; the complete body remains in the pinned original source.

| Component | Original byte interval | Bytes | SHA-256 |
|---|---|---:|---|
| preamble | [0, 549) | 549 | `7e0dfd244177e35a4b381d329b368c433173ddd193969bef8aac17fc419c74f6` |
| begin document boundary | [549, 565) | 16 | `49d34b0366eb0a68eb35c75d6d8aeb1d60be3c49779501a7e1cdf4941acdab46` |
| original body | [565, 17691) | 17126 | `1cdcd3282042d180edd411b32b26c41046b27c4b62520051336274936492435d` |
| end document boundary | [17691, 17705) | 14 | `2dc670e7ffe1f12aa0326631b39a0b6d72da153425c7f5f9aed627a71c1487d6` |
| postamble | [17705, 17706) | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |

The literal prefix removed from the original body is the 13-byte sequence `\n\\maketitle\n\n` (base64 `ClxtYWtldGl0bGUKCg==`). No proof prose is part of that prefix. The retained LF body occupies original bytes [578, 17691). Its exact pin is the pre-layout LF row above. Replacing every LF in that retained body by CRLF gives the pre-layout CRLF row above; no other byte is changed in this step.

## All ten forward and inverse layout transformations

The sealed `evidence/LAYOUT.json` supplies ten ordered pairs of complete strings. Nine pairs move an existing equation tag outside an inner alignment, and the tenth records the determinant-line wrap. For every step, the complete old and new payloads are included as both literal text and base64 in [CLARIFICATION.json](CLARIFICATION.json), together with exact source spans and all before/after pins in both line-ending frames. The transformations are applied in that recorded order, each to its unique exact source occurrence.

| Step | LF source span, end excluded | LF bytes after step | LF SHA-256 after step |
|---:|---|---:|---|
| 1 | 3943–3968 | 17113 | `db4026e2d3fbbe10a9464f0284560c8ddcab3b6e989648ca59ecfa7fc26d75df` |
| 2 | 4895–4920 | 17113 | `4d6a8737b9cf4acc3b37c7d4831b99fdb843daffdd457354decd8a029860b256` |
| 3 | 5211–5236 | 17113 | `6f89b5e56ad727a40a04a09f3734c662af25a8276fcfb1ab3d5e698e1953474b` |
| 4 | 5461–5483 | 17113 | `e43de707123e84c1ae4bf459d62dbea15e8f50e92db714dbd11d7293c25f67b4` |
| 5 | 5754–5776 | 17113 | `4b02463f699bdc41ba7e19afe8b4a5970e7365d19733a7ffec71c7739e71cecb` |
| 6 | 9604–9630 | 17113 | `5076def80daf388f8776225e0d3fad319460b7b048a216457389baacd17cab27` |
| 7 | 10316–10339 | 17113 | `d24961f25a60d2afaaa33d958c016bd5c93c948d50abbee3d526bc4155c3025f` |
| 8 | 10843–10869 | 17113 | `7b32c14b706f658c41cebc3e4f6fdacb8ccdc4ece7423611be86340d0b87d4fb` |
| 9 | 11804–11830 | 17113 | `a1239e1bd9c2f3fe8680147c2580936f6a26fad50ac357271f31f5fb430292fc` |
| 10 | 6750–7028 | 17149 | `42b97470bfe0f67e0a0247e5cefcb95609c487b8ff20c275457aeebc02b7b706` |

Applying all ten transformations to the 17113-byte LF body gives the 17149-byte final LF body. Applying the same transformations to the CRLF body, after converting every LF in each old/new payload to CRLF, gives every byte of the accepted 17558-byte reader. Thus the retained hash `42b97470bfe0f67e0a0247e5cefcb95609c487b8ff20c275457aeebc02b7b706` has an exact identified final-body preimage.

For the inverse, start from the accepted CRLF reader and visit the ten pairs in reverse order. Replace each unique new CRLF payload by its old CRLF payload. This recovers the complete pre-layout CRLF body. Replace its CRLF sequences by LF, restore the exact 13-byte title prefix, then concatenate the original preamble, the literal `\begin{document}` boundary, the restored complete body, the literal `\end{document}` boundary and the original postamble. Exact byte comparison recovers the pinned original. This comparison retains all original definitions, proof prose, constants, signs, macros and equation tags because it recovers the entire source file, including its preamble.

## Reproducible byte verification

The complete standard-library verification program is [verify_reconstruction.py](verify_reconstruction.py). Given the sealed artifact directory, run:

```text
python verify_reconstruction.py --artifact-root PATH_TO_SEALED_AT_ARTIFACT
```

The program checks all five input pins, every intermediate layout pin and source span, both final line-ending frames, all ten inverse substitutions and every original-file component. It writes no source file and executes no mathematical code or document build. The accompanying local audit records successful verification against the pinned staged public artifact. This clarification adds no mathematical theorem or new mathematical execution claim.
