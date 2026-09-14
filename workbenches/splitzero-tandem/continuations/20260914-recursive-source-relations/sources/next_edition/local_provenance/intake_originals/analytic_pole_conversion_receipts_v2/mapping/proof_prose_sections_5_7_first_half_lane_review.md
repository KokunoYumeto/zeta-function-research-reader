# Independent prose-typing review of AP Sections 5–7 and provenance

Reviewed source: `ANALYTIC_POLE_RESIDUE_TRANSPORT.md`, 18,433 bytes, SHA-256 `357923aead35c77f2fa98598fbc4ed8bc1f7cd6ebc04760da504a0ded765a652`.

Reviewed map: `proof_prose_sections_5_7.json`, initial 123-span version. This is a contextual mathematical-typing coverage review. It does not re-audit the mathematical proof or claim final PDF acceptance.

I applied every mapping to a private in-memory derivative, then read the entire resulting prose from Section 5 through the final provenance paragraph, including all mapped expressions in context. The following concrete corrections were sent to the mapping owner; I did not change their map.

## False mathematical identifications to remove

All intervals below are zero-based, half-open UTF-8 byte offsets in the exact original source.

| Byte interval | Original character | Actual source context |
|---|---|---|
| [8963,8964) | s | operator's |
| [13990,13991) | A | A formal coefficient sequence |
| [14123,14124) | s | AP3's |
| [15740,15741) | s | UG's |
| [17878,17879) | s | AP3's |
| [17923,17924) | s | AP8--AP13's |
| [18024,18025) | s | AP15--AP18's |
| [18059,18060) | s | AP22's |
| [18090,18091) | s | AP23--AP24's |
| [18277,18278) | s | review's |

The mathematical `A` at [16847,16848), in “It commutes with A”, must remain mapped.

## Mathematical occurrences omitted from the initial map

- `alpha` in “the injected column for alpha” names the same covector as the following displayed column. Type it as `\alpha`.
- `tau` in “previous tau-base dagger” names the original mathematical base. Type it as `\tau`, preserving the remaining compound text.
- `theta` in “uniform theta-norm bound” names the norm's original mathematical parameter. Type it as `\theta`, preserving the remaining compound text.

## Preserve the original derivative symbol

At [15229,15247), the exact source is `u d_t w(p)=-p w(p)`. The initial TeX payload is `u\partial_t w(p)=-p w(p)`. Retain the source's written `d_t` symbol in the typed expression. This avoids an unnecessary notational replacement while preserving the exact derivative identity.

All other mathematical expressions in the initial 123-span map preserve their original algebraic order, factors and content. A corrected map needs a final byte-span and coverage check against these findings.
