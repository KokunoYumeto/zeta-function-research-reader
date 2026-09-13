# Complete BV, WP and FV chapter transfer

Status: PASS for source transfer. These are three complete LaTeX input chapters, not a PDF or a new mathematical proof. The integrated main build and rendered-page review remain the main integrator's responsibility.

## Immutable inputs and outputs

| Unit | Accepted source SHA-256 | Output SHA-256 |
| --- | --- | --- |
| BV: `29yc_balanced_window_norms.tex` | `a3bb84329d384071b4ac4829731e26dbe2586b719548a660bae6eefb34f5e00c` | `109da810c78ff9848c871f52fcc8d29a88f69e89a1f3caa28fe17bf64ec5799f` |
| WP: `29z_exact_window_product.tex` | `c97c831a5e1c2ef3685910c648bce0f9fbcd54230bc8a1bec7e521bd808a1209` | `4a89134345d654c2966ef122578b6f8bb9a80f135dc14d03b354873844fe9721` |
| FV: `29za_four_volume_threshold.tex` | `9ff55c84d74db85306e7a68c70fe7b08d8e642e8ac1a3e6137649f68e102fc3a` | `27af4a09b264f5f297efce080518ef6374c7169a00f2d8c70459427a95131229` |

The sources are respectively `arithmetic_endpoint_review/BALANCED_WINDOW_PROOF.md`, `window_product_review/WINDOW_PRODUCT_PROOF.md`, and `FOUR_VOLUME_THRESHOLD.md` under the integration cut. Their lengths are 5,891, 13,786 and 7,716 bytes. Output lengths are 8,850, 16,804 and 10,311 bytes.

The complete machine receipt is `WINDOW_THRESHOLD_TRANSFER_RECEIPT.json`, SHA-256 `e6ce7755b4468cbe4eb3297c7f29d3844d7ce8f85ba34ede688f69d94c3acf87`. It records source and output pins, all exact AST transformations, the full ASCII-math map, all final links and tags, the converter hash, and the three observed canonical-file hashes.

## Preservation actually checked

The pinned Markdown sources were read completely and converted with Pandoc 3.9.0.2. All 43 BV, 68 WP and 53 FV source blocks are retained in their original sequence: the sole source title becomes the chapter section, followed by a separate editorial introduction and the entire source body. No proof or source paragraph is summarized or dropped.

For WP and FV, all 131 and 75 original TeX mathematical payloads, respectively, are unchanged except explicit equation-tag prefixes. The converter independently checks their ordered occurrence in the emitted body. For BV, the original source uses plain ASCII equations rather than TeX math: all 15 complete formula blocks were individually transcribed and reviewed, producing 16 displays, and 58 exact inline formula spans were protected and transcribed. The inline preprocessing reverses byte-for-byte to the original source; the 15 display mappings require entire-block exact matches. This is a complete reviewed mathematical transcription, not a claim that the ASCII and TeX formula strings are byte-identical.

The transformed AST reverses exactly to the parsed source AST. The generated source body is included in full, and every math payload appears in order. The transformation log accounts for formula typography, breakable literal code, heading identifiers, presentation-only leading heading ordinals, the relative source link, and equation/reference prefixes. Subordinate TOC-spacing additions also reverse exactly to the full emitted body. All three final TeX sources were read; the final BV output was reread after protecting the source's caret notation against Markdown superscript parsing.

After the main integrator reported an overfull opaque hash in WP, the inline-code adapter was narrowly extended for complete 40/64-character hexadecimal hashes only. Such literals retain monospaced typography and receive zero-width `\allowbreak{}` commands between eight-character chunks. There are no inserted visible characters, spaces or hyphens. Only the one 64-character literal in WP changes; BV and FV remain byte-identical. Removing this adapter restores each entire output byte-for-byte to its pre-repair SHA-256, including WP `7fc25fb07c82ae7793e492e3b2cabb982c5e020804dc78ca8bca07df80bf240e`. The receipt checks this independently of its full AST and math checks. The subsequent PDF rebuild and layout confirmation belong to the main integrator; this source-only repair makes no new visual-pass claim.

Tags are BV.1--BV.7, WP.1--WP.13 and FV.1--FV.9. Auto-label namespaces are `balanced-window-`, `window-product-`, and `four-volume-`; no new labels collide with one another or the 1,589 labels scanned from existing canonical TeX. The chapters reuse the existing packages, with locally grouped emergency stretch and a scoped `tightlist` fallback. They add no document wrapper, package, theorem or axiom.

## Public provenance and editorial boundary

All three introductions point to the public immutable source commit `952ef9fee1e1419b6858d920354de8fa99430b7d`. All source hyperlinks are HTTP(S), and the one local-relative arithmetic-note link is rewritten to that commit's `workbenches/tau-arithmetic-endpoint-bounds/delivery/NOTE.tex`. Its independently recorded public SHA-256 is `f776e7934f026342f48732a74f14d57470b8aae1cef76ebdee5f831bd49dedf8`.

The public BV and WP payloads exactly equal the accepted source bytes. Public FV SHA-256 `50cf16bc0ccd955d2dccac62b7fb8d8f08623cfe6436c4fff7374ac5ea3f3ec2` differs from the accepted local source only by the single relative-link portability adapter to `delivery/NOTE.tex`; this complete-byte equality after that declared adapter is also checked. The chapter retains the requested accepted FV body and publishes its link as the same absolute pinned target.

The added introductions say **this integrated reader**. They explicitly identify the body's frozen-edition, next-cut and GitHub-only boundary statements as historical; the frozen edition is not retroactively changed. WP's added introduction clarifies that only alpha, beta and t are positive contraction parameters at most one, whereas the positive norm factor A need not be at most one. The historical source body is unchanged by that clarification.

The original source's phase, zero-contraction, r=1, determinant and missing-upper-estimate qualifications remain in full. This transfer does not extend the accepted mathematical result or assert an arithmetic upper estimate, an RH proof, a Lean certificate, or a PDF visual-review pass.

No PDF build, second authoring marker, local Lean, remote action or canonical edit was performed. The observed canonical `main.tex`, `main.pdf` and `29x_gamma_convolution_descent.tex` hashes remained unchanged across generation.
