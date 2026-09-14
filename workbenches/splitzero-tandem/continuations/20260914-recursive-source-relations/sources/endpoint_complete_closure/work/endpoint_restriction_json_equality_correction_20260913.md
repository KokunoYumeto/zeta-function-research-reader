# Exact correction to the JSON byte-equality report

The pinned `arithmetic_endpoint_intake_20260913.md` reports the normal run as follows: “the full JSON stdout is byte-identical to the normal run and to the delivered successful payload.” The intended normal/optimized comparison is verified, but the extension of literal byte equality to the delivered file is false. This supplemental correction preserves that pinned audit and its manifest, identifies the exact comparison, and supplies the complete byte-to-text map. No mathematical statement or test outcome changes.

The delivered arithmetic successful JSON is 989 bytes with LF line endings, SHA `a3c19dd9f4b2d3414875fc6134359f6ba78c309d37f63d804114358a8e378331`. The fresh normal stdout is 1016 bytes with 27 CRLF endings. The delivered restriction successful JSON is 164 bytes with LF line endings; its fresh normal file is 171 bytes with seven CRLF endings. The exact paths and all four SHA-256 values are in the accompanying JSON record.

For each pair, the literal byte strings are unequal. Define the explicit map on the fresh byte string by replacing each two-byte sequence CR LF with the single byte LF and retaining every other byte in order. Its output equals the delivered byte string exactly in both cases. Parsing either original string as JSON gives exactly equal objects. The fresh normal and optimized outputs in each lane are also literally byte-identical to one another, as recorded by their separate replay checks.

The corrected statement is: **Fresh normal and optimized results have identical bytes; their parsed JSON payloads equal the delivered payload. The fresh and delivered files differ only by the proven CRLF-to-LF map.** This statement neither overwrites nor reclassifies either original byte sequence. Both remain separately hashed and retained.

No old mathematical source, pinned audit, prior manifest, current Gamma cut, or remote object was edited for this correction.
