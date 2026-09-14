# Source-faithful ledger conversion audit

read-only proposals; no active edits; no PDF build.

build_ledger.py invokes Pandoc --from=markdown+tex_math_single_backslash, retaining default inline_notes and superscript extensions. Pandoc parses bare ^[K:Q] as Note and un-delimited pairs of ^ as Superscript before layout.lua visits Str/Code/Math. It also parses adjacent [1+k(m−1)](k+1) mathematical factors as a hyperlink to k+1. Actual AST probes of all 12 Markdown files reproduce exactly two Notes, fifteen Superscripts and the two formula Links. Every proposed expression parses as a single InlineMath node.

All 24 source files exist and match their manifest hashes and bytes. Exactly two raw `^[K:Q]` occurrences are field-degree exponents; no genuine source footnotes were found.

## SUP01: formation:133

Original path: `work/tau_f1_transcript_audit_20260913/audit_base_formation/AUDIT.md`
Source SHA-256: `829cb91ad8456045812dea3bfc0e47530212286bed20031d5e1bdff8037f3818`

Original: `diag(e^{-aL},e^{aL})`

Old active TeX line 3671: `diag(e\textsuperscript{\{-aL\},e}\{aL\}); hyperbolic anomaly envelope`

Proposed: `\(\operatorname{diag}(e^{-aL},e^{aL})\)`

## SUP02: formation:193

Original path: `work/tau_f1_transcript_audit_20260913/audit_base_formation/AUDIT.md`
Source SHA-256: `829cb91ad8456045812dea3bfc0e47530212286bed20031d5e1bdff8037f3818`

Original: `P_{a,b}(s)=((s−1/2−a)^2+b²)((s−1/2+a)^2+b²)`

Old active TeX line 3802: `P\_\{a,b\}(s)=((s\allowbreak{}\ensuremath{−}\allowbreak{}1/2\allowbreak{}\ensuremath{−}\allowbreak{}a)\textsuperscript{2+b²)((s\allowbreak{}\ensuremath{−}\allowbreak{}1/2+a)}2+b²),`

Proposed: `\(P_{a,b}(s)=((s-1/2-a)^2+b^2)((s-1/2+a)^2+b^2)\)`

## SUP03: formation:377

Original path: `work/tau_f1_transcript_audit_20260913/audit_base_formation/AUDIT.md`
Source SHA-256: `829cb91ad8456045812dea3bfc0e47530212286bed20031d5e1bdff8037f3818`

Original: `c_i:H_c^i→H^i`

Old active TeX line 4214: `c\_i:H\_c\textsuperscript{i\allowbreak{}\ensuremath{→}\allowbreak{}H}i,`

Proposed: `\(c_i:H_c^i\to H^i\)`

## SUP04: formation:479

Original path: `work/tau_f1_transcript_audit_20260913/audit_base_formation/AUDIT.md`
Source SHA-256: `829cb91ad8456045812dea3bfc0e47530212286bed20031d5e1bdff8037f3818`

Original: `FNF^(−1)=q^(−1)N`

Old active TeX line 4456: `FNF\textsuperscript{(\allowbreak{}\ensuremath{−}\allowbreak{}1)=q}(\allowbreak{}\ensuremath{−}\allowbreak{}1)N;`

Proposed: `\(FNF^{(-1)}=q^{(-1)}N\)`

Original parenthesized inverse exponent is retained as {(-1)}; no sign or exponent simplification.

## SUP05: formation:479

Original path: `work/tau_f1_transcript_audit_20260913/audit_base_formation/AUDIT.md`
Source SHA-256: `829cb91ad8456045812dea3bfc0e47530212286bed20031d5e1bdff8037f3818`

Original: `N z^j=z^{j+1}`

Old active TeX line 4459: `instead has N z\textsuperscript{j=z}\{j+1\},`

Proposed: `\(N z^j=z^{j+1}\)`

## SUP06: formation:487

Original path: `work/tau_f1_transcript_audit_20260913/audit_base_formation/AUDIT.md`
Source SHA-256: `829cb91ad8456045812dea3bfc0e47530212286bed20031d5e1bdff8037f3818`

Original: `C_qNC_q^(−1)=q^(−1)N`

Old active TeX line 4488: `C\_qNC\_q\textsuperscript{(\allowbreak{}\ensuremath{−}\allowbreak{}1)=q}(\allowbreak{}\ensuremath{−}\allowbreak{}1)N`

Proposed: `\(C_qNC_q^{(-1)}=q^{(-1)}N\)`

Original parenthesized inverse exponent is retained as {(-1)}; no sign or exponent simplification.

## SUP07: formation:487

Original path: `work/tau_f1_transcript_audit_20260913/audit_base_formation/AUDIT.md`
Source SHA-256: `829cb91ad8456045812dea3bfc0e47530212286bed20031d5e1bdff8037f3818`

Original: `C_qU_aC_q^(−1)=a^{ρ(1−1/q)}U_{a^{1/q}}`

Old active TeX line 4490: `C\_qU\_aC\_q\textsuperscript{(\allowbreak{}\ensuremath{−}\allowbreak{}1)=a}\{\allowbreak{}\ensuremath{ρ}\allowbreak{}(1\allowbreak{}\ensuremath{−}\allowbreak{}1/q)\}U\_\{a\textasciicircum{}\{1/q\}\}.`

Proposed: `\(C_qU_aC_q^{(-1)}=a^{\rho(1-1/q)}U_{a^{1/q}}\)`

Original parenthesized inverse exponent is retained as {(-1)}; no sign or exponent simplification.

## SUP08: formation:530

Original path: `work/tau_f1_transcript_audit_20260913/audit_base_formation/AUDIT.md`
Source SHA-256: `829cb91ad8456045812dea3bfc0e47530212286bed20031d5e1bdff8037f3818`

Original: `C_qNC_q^(−1)=q^(−1)N`

Old active TeX line 4638: `C\_qNC\_q\textsuperscript{(\allowbreak{}\ensuremath{−}\allowbreak{}1)=q}(\allowbreak{}\ensuremath{−}\allowbreak{}1)N`

Proposed: `\(C_qNC_q^{(-1)}=q^{(-1)}N\)`

Original parenthesized inverse exponent is retained as {(-1)}; no sign or exponent simplification.

## SUP09: formation:530

Original path: `work/tau_f1_transcript_audit_20260913/audit_base_formation/AUDIT.md`
Source SHA-256: `829cb91ad8456045812dea3bfc0e47530212286bed20031d5e1bdff8037f3818`

Original: `C_qU_aC_q^(−1)=a^{ρ(1−1/q)}U_{a^{1/q}}`

Old active TeX line 4640: `C\_qU\_aC\_q\textsuperscript{(\allowbreak{}\ensuremath{−}\allowbreak{}1)=a}\{\allowbreak{}\ensuremath{ρ}\allowbreak{}(1\allowbreak{}\ensuremath{−}\allowbreak{}1/q)\}U\_\{a\textasciicircum{}\{1/q\}\}.`

Proposed: `\(C_qU_aC_q^{(-1)}=a^{\rho(1-1/q)}U_{a^{1/q}}\)`

Original parenthesized inverse exponent is retained as {(-1)}; no sign or exponent simplification.

## SUP10: typed:241

Original path: `work/tau_f1_transcript_audit_20260913/audit_typed_route/AUDIT_TYPED_ROUTE.md`
Source SHA-256: `e791f7ad7c544235ad5ab2e1ed6fe49b03ae8569a6475fc79c93eb5b94837744`

Original: `H_R=L2((e^−R,e^R),dx)`

Old active TeX line 5218: `H\_R=L2((e\textsuperscript{\allowbreak{}\ensuremath{−}\allowbreak{}R,e}R),dx),`

Proposed: `\(H_R=\mathrm{L2}((e^{-R},e^R),dx)\)`

The ledger source spells the space L2; proposal preserves those literal characters with \mathrm{L2}. Recasting it as L^2 would require an explicitly documented source-typography correction; transcript witness is being checked separately.

## SUP11: late:137

Original path: `work/tau_f1_transcript_audit_20260913/audit_late_control/AUDIT_LATE_CONTROL.md`
Source SHA-256: `2beba5c8289b33aa01d039f3a2ecbb78f13fb2899d7251a498adee329473d87b`

Original: `G_N^ar≤C_h^kG_N^Γ`

Old active TeX line 8417: `G\_N\textsuperscript{ar\allowbreak{}\ensuremath{≤}\allowbreak{}C\_h}kG\_N\textasciicircum{}\allowbreak{}\ensuremath{Γ}\allowbreak{},`

Proposed: `\(G_N^{\mathrm{ar}}\le C_h^kG_N^\Gamma\)`

## SUP12: late:243

Original path: `work/tau_f1_transcript_audit_20260913/audit_late_control/AUDIT_LATE_CONTROL.md`
Source SHA-256: `2beba5c8289b33aa01d039f3a2ecbb78f13fb2899d7251a498adee329473d87b`

Original: `H^{−1}=E_1,H^0=E_1`

Old active TeX line 8686: `H\textsuperscript{\{\allowbreak{}\ensuremath{−}\allowbreak{}1\}=E\_1,H}0=E\_1,`

Proposed: `\(H^{-1}=E_1,H^0=E_1\)`

## SUP13: late:270

Original path: `work/tau_f1_transcript_audit_20260913/audit_late_control/AUDIT_LATE_CONTROL.md`
Source SHA-256: `2beba5c8289b33aa01d039f3a2ecbb78f13fb2899d7251a498adee329473d87b`

Original: `H^0=F,H^1=0,H^2=E/F`

Old active TeX line 8761: `Auxiliary log de Rham groups are H\textsuperscript{0=F,H}1=0,H\^{}2=E/F.`

Proposed: `\(H^0=F,H^1=0,H^2=E/F\)`

## SUP14: late:324

Original path: `work/tau_f1_transcript_audit_20260913/audit_late_control/AUDIT_LATE_CONTROL.md`
Source SHA-256: `2beba5c8289b33aa01d039f3a2ecbb78f13fb2899d7251a498adee329473d87b`

Original: `Π^{−*}G_NΠ^{−1}`

Old active TeX line 8904: `\allowbreak{}\ensuremath{Π}\allowbreak{}\textsuperscript{\{\allowbreak{}\ensuremath{−}\allowbreak{}*\}G\_N\allowbreak{}\ensuremath{Π}\allowbreak{}}\{\allowbreak{}\ensuremath{−}\allowbreak{}1\}.`

Proposed: `\(\Pi^{-*}G_N\Pi^{-1}\)`

## SUP15: late:376

Original path: `work/tau_f1_transcript_audit_20260913/audit_late_control/AUDIT_LATE_CONTROL.md`
Source SHA-256: `2beba5c8289b33aa01d039f3a2ecbb78f13fb2899d7251a498adee329473d87b`

Original: `B_N^0→B_N^0`

Old active TeX line 9040: `B\_N\textsuperscript{0\allowbreak{}\ensuremath{→}\allowbreak{}B\_N}0`

Proposed: `\(B_N^0\to B_N^0\)`

## LINK01: late:84

Original path: `work/tau_f1_transcript_audit_20260913/audit_late_control/AUDIT_LATE_CONTROL.md`
Source SHA-256: `2beba5c8289b33aa01d039f3a2ecbb78f13fb2899d7251a498adee329473d87b`

Original: `q_k=[1+k(m−1)](k+1)²`

Old TeX: `q\_k=\href{k+1}{1+k(m\allowbreak{}\ensuremath{−}\allowbreak{}1)}²`

Proposed: `\(q_k=[1+k(m-1)](k+1)^2\)`

The mathematical [1+k(m−1)] factor and adjacent (k+1) factor must both remain visible. floor is retained as an operator word with its original parenthesized argument; no evaluation or normalization.

## LINK02: late:84

Original path: `work/tau_f1_transcript_audit_20260913/audit_late_control/AUDIT_LATE_CONTROL.md`
Source SHA-256: `2beba5c8289b33aa01d039f3a2ecbb78f13fb2899d7251a498adee329473d87b`

Original: `L_{h,k}=2δ[1+k(m−1)](k+1)floor((k+1)²/4)`

Old TeX: `L\_\{h,k\}=2\allowbreak{}\ensuremath{δ}\allowbreak{}\href{k+1}{1+k(m\allowbreak{}\ensuremath{−}\allowbreak{}1)}floor((k+1)²/4)`

Proposed: `\(L_{h,k}=2\delta[1+k(m-1)](k+1)\operatorname{floor}((k+1)^2/4)\)`

The mathematical [1+k(m−1)] factor and adjacent (k+1) factor must both remain visible. floor is retained as an operator word with its original parenthesized argument; no evaluation or normalization.
