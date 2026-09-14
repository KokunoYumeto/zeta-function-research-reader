# Lossless public representation of the historical page comparison

[Open the complete gzip JSON](CROSS_PAGE_RENDER_TRANSFER.json.gz). Decompression yields **151,964,146 bytes** with SHA-256 `1d9f4c913912676950a4a70eb8ce89bb653f4a81b6619c76b85bbdd6c80e6807`. No JSON field, page measurement, pixel hash or proof expression was removed or reserialized.

The historical output manifests and transfer receipts retain their original source-cut identities. They are not newly issued acceptances of this gzip file. [The current representation map](../../../PUBLIC_REPRESENTATIONS.json) records the stored payload and exact decompression identity; [the full public derivation](../../../PUBLIC_DERIVATION.json) retains the preceding source-locator transformation.

Historical tools that expect a `.json` may consume a decompressed working copy. The current reader build does not depend on this historical QA JSON. Its PDF, 240 compiled inputs and fixed builders are unchanged.
