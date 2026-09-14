# Independent BF12 exponent and TCL.2 display recovery audit

The two bounded repairs pass. `BF12_TCL2_INDEPENDENT_RECEIPT.json` records the exact source hashes, all replacement byte spans, current active snapshots, parser reproduction, and double-read timestamps. `verify_bf12_tcl.py` replays the checks and writes only within this audit directory.

## BF12 source fidelity and exact replacement maps

The retained `formation.md` line 277 and `ledger.md` line 2452 contain the same proof paragraph byte-for-byte. Their two expressions are exactly `N(2R)=2^[K:Q]>1` and `q=2^[K:Q]q`. The retained A0862 source states `d=[K:\mathbb Q].` at line 136, `N_K(2R)=2^d.` at line 142, and `q=2^dq.` at line 164. It also writes `q=2^{[K:\mathbb Q]}q` explicitly at line 456. Thus the source fixes the degree exponent; no mathematical inference from the malformed TeX is needed.

The exact active-file correction map is:

```text
N(2R)=2\footnote{K:Q}\textgreater1
  -> \(N(2R)=2^{[K:Q]}>1\)
q=2\footnote{K:Q}q
  -> \(q=2^{[K:Q]}q\)
```

For each retained stage and delivery pair, applying exactly those two replacements reproduces the entire after file; applying their inverses reproduces the entire before file. Every byte outside those two expression spans is unchanged, including the rest of the BF12 proof paragraph. The original source spelling `[K:Q]`, `N(2R)`, `q`, the inequality `>1`, and the right-hand multiplication placement are retained.

| Object | Bytes | SHA-256 |
|---|---:|---|
| BF12 before, stage and delivery | 394423 | `514033f1c772997e2b13a1cd095f84a631a92162f0d5711ab3795dcfb97c77c3` |
| BF12-only after, stage and delivery | 394408 | `ede1c650557697a902702947e835e057675f3a2be98cf27a4f085d1216a8ad45` |
| Current ledger, stage and delivery | 393073 | `4110f2c19863a616228ceceaf89215b4887ca656b3c81bb8207c42dc03931cb0` |

Byte spans are zero-based and half-open. In the retained before state, the malformed norm and fixed-point expressions occupy `[148874,148908)` and `[148952,148970)`; in the BF12-only after state they occupy `[148874,148895)` and `[148939,148955)`. In the current stage and delivery files, after later repairs elsewhere, the corrected expressions occupy `[148735,148756)` and `[148800,148816)`. Both remain at lines 3994 and 3995.

The current entire BF12 block is byte-equal to the BF12-only after block, with SHA-256 `6fc641d4b7ca174cd65772281876f529e67a3eaecd9d81ffc08b59423ef27a70`. The BF12-only after file is also byte-equal to the retained before input of the later 17 ledger repairs, and the current active hash equals that later application's after hash. The parent audits the 17 intervening replacements; this audit independently proves the chain endpoint identities and BF12 preservation.

The original Pandoc parser invocation reproduces exactly two `Note` nodes, both containing `K:Q`. The corrected source produces no `Note` nodes and produces the two intended inline math nodes. Fresh full-ledger conversion matches the retained generated files under the original correction script's `text=True` stdout convention. Native Windows stdout uses CRLF; both native output files and the original script's LF text-stream representation are retained, and their exact reversible newline transport is checked. Reversing the two expressions in the fully regenerated output preserves every non-whitespace TeX token; Pandoc's line wrapping differs. This full-conversion token comparison is distinct from the stronger whole-byte equality proved for the two applied active-file repairs.

## TCL.2 exact display map

The only changes are `\begin{split}` to `\begin{aligned}` at line 2072 and `\end{split}` to `\end{aligned}` at line 2080. The complete mapped fragment occupies `[79795,80100)` before and `[79795,80104)` after. The opening environment token occupies `[79796,79809)` before and `[79796,79811)` after; the closing token occupies `[80088,80099)` before and `[80090,80103)` after.

The formula lines 2073–2079 remain byte-exact:

```tex
 K&=k(m-1),\qquad y_i=s_i-\rho,\qquad
 E_S=S[s_1,\ldots,s_k]/((s_i-\rho)^m)_{i=1}^k
       =S[y_1,\ldots,y_k]/(y_i^m)_{i=1}^k,\\
 J&=\sum_{i=1}^k y_i,\qquad
 M=\sum_{i=1}^k s_i=k\rho+J,\qquad
 \mathcal C_S=S[T]/(T^{K+1}),\qquad
 \mathcal C_S^{\rm orig}=S[Z]/((Z-k\rho)^{K+1}).
```

Those seven lines occupy 277 bytes, SHA-256 `85792f9002f0aae7681586db29cca8de0134ea96d01c1555e42f091cbe0cfa36`. The entire environment interior including the newline immediately after the opening token and the space immediately before the closing token occupies 279 bytes, SHA-256 `e00d4467722f9d1f932b522570a3212c78488f742a6c983f9e7b78ed5be10e45`. An additional read-only subagent independently obtained that latter hash and the same token spans.

The before file is 116788 bytes, SHA-256 `ce50669c58c4e023bd0ddd978543f8951a055352b6f42be9a1fb8275a3e30e30`. The repaired file and both current active copies are 116792 bytes, SHA-256 `a81cdbd085184161e59e2ba979d188507420a556f91626698eeb71137c5f94f9`. Exact forward and inverse substitutions reproduce the entire respective files; the TCL.2 tag and label remain untouched at line 2081.

## Scope and concurrent build

Only conversion and display-fidelity evidence is certified here. No active source was edited; no PDF was rendered; no Lean or compiler process was started; no remote action was performed. This audit does not re-prove the entire source ledger, certify the other conversion repairs, or certify PDF visual acceptance. All four active TeX inputs remained byte-identical between this audit's two reads. The parent owns final compiler-input and delivery binding after the concurrent build settles.
