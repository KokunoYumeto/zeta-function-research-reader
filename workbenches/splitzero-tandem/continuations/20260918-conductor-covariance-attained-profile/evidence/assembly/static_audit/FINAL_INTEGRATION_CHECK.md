# Independent final integration check

Result: **PASS** for the generated source edition at the hashes recorded in `FINAL_INTEGRATION_CHECK.json` and `cumulative_recovery/RECOVERY_AUDIT.json`.

This audit read the acceptance record, insertion manifest, accepted inputs, sealed snapshots, complete common body, standalone supplement, bibliography files, and three cumulative derivatives. It did not import or execute the assembler, edit mathematical sources, or run a TeX compiler.

## Accepted inputs and generated fragments

- The manifest names the actual SHA256 of `MATHEMATICAL_ACCEPTANCE.json`: `a24715564307271dfbf89e83f6cb36682f76bca56586d2d33ad83fe806f4ff2f`.
- Its twelve input paths are precisely the twelve accepted paths. Every source length/hash agrees with the acceptance record, and every sealed snapshot equals its accepted source byte for byte.
- Each of the twelve rendered fragments occurs between exactly one pair of sealed-input markers in the common body. Replaying the recorded presentation changes against the corresponding snapshot reproduces the fragment byte for byte and gives its recorded rendered SHA256. Reversing those changes uniquely restores the source text.
- Every manifest artifact pin inspected matches the current file length and SHA256, including all predecessor and successor source files.
- The common body has SHA256 `eb3ca69c0cda569c8b7017d961295cd09642d5acd8996b856d279d15ea1bc6b4`. Its exact bytes occur once in each of the three cumulative successors and once in the standalone supplement.
- Generated common body, supplement, both bibliography files, and all three cumulative successors contain no forbidden ASCII control byte: no code below 32 other than ordinary tab, LF, or CR, and no DEL. The preserved scalar input snapshot contains the documented original form-feed; its rendered derivative does not.

The machine check is reproducible with `python -B assembly/static_audit/check_final_integration.py` from the intake directory. It writes only its audit JSON.

## Presentation changes and their mathematical content

The manifest records exactly 24 operations. Twenty-one only add or remove the specified `gathered` layout wrappers, spacing macros, line breaks, or whitespace. Removing exactly those layout tokens from each operation's before/after strings gives identical remaining tokens, including every variable, numerical constant, sign, exponent, bound, order of factors, and equation-tag token. This is a lexical preservation check; it does not replace a mathematical expression by a simpler one.

The three other operations are checked individually below. The malformed raw TeX does not have an executable mathematical interpretation merely because its delimiters balance; the rendered repair is justified by the surrounding accepted definitions and identities.

### LT6 indexed diagonal inverse

The raw expression `\operatorname{diag}(\rho_i)_{i=0}^D^{-1}` has two consecutive superscripts. The derivative prints

\[
\bigl[\operatorname{diag}(\rho_i)_{i=0}^{D}\bigr]^{-1}.
\]

This groups precisely the original indexed diagonal matrix; it changes no index, exponent, or factor order. To check the object exactly, LT2 defines

\[
\rho_n=\sqrt{\frac{n!}{(s/2)_n}},\qquad s\in\{1,a\},\qquad s>0.
\]

For every integer \(n\ge0\), the factorial and every factor of \((s/2)_n\) are positive, and the empty product at \(n=0\) is one. Thus \(\rho_n>0\). With the unchanged indices \(0\le i,j\le D\), put

\[
R=\operatorname{diag}(\rho_i)_{i=0}^{D},\qquad
R_v=\operatorname{diag}(\rho_{i+v})_{i=0}^{D}.
\]

The repaired LT6 product has entries

\[
(R^{-1}T_D(g)R_v)_{ij}
=\rho_i^{-1}(T_D(g))_{ij}\rho_{j+v}
=\begin{cases}
g_{j-i}\rho_{j+v}/\rho_i,&i\le j,\\
0,&i>j.
\end{cases}
\]

These are exactly the accepted entry formula also displayed in XIM3 and WCF8. The definition of \(R\) in LT12 is the same indexed diagonal matrix. The inverse is therefore on the original left diagonal factor, with no transpose, reordering, or scalar rescaling.

### Form-feed repair in the scalar endpoint expansion

One raw byte sequence is U+000C followed by `rac{m^2}{8n^2}`. The derivative changes exactly that sequence to `\frac{m^2}{8n^2}`. The numerator \(m^2\), denominator \(8n^2\), following logarithm, and positive sign are untouched.

Its required coefficient also follows directly from the accepted preceding identities. LRS14 gives, for positive \(t\) tending to zero,

\[
\psi(t)=a_0+\frac t4\log t+(a_0-\tfrac14)t+O(t^{3/2}),
\]

and LRS15 gives \(\mathfrak F(0)=0\) and \(\mathfrak F'=\psi\). For positive \(t\), the exact antiderivative and its zero endpoint are

\[
\int_0^t x\log x\,dx
=\frac{t^2}{2}\log t-\frac{t^2}{4},
\qquad \lim_{x\downarrow0}x^2\log x=0.
\]

If the remainder in LRS14 is bounded by \(C x^{3/2}\) on the relevant interval, its integral has absolute value at most \((2C/5)t^{5/2}\). Integrating the unchanged terms therefore gives

\[
\mathfrak F(t)
=a_0t+\frac{t^2}{8}\log t
 +\left(\frac{a_0}{2}-\frac{3}{16}\right)t^2
 +O(t^{5/2}).
\]

Substituting exactly the original positive value \(t=m/n\) yields

\[
\mathfrak F(m/n)
=a_0m/n+\frac{m^2}{8n^2}\log(m/n)
 +\left(\frac{a_0}{2}-\frac{3}{16}\right)m^2/n^2
 +O((m/n)^{5/2}).
\]

Thus the repaired fraction is the exact coefficient already required by the preceding accepted calculation; it is not a replacement parameter or new estimate.

### Inline quotient displayed as a fraction

The equilibrium operation replaces the inline quotient

\[
\sin\theta\cos\theta/\sqrt{\cos^2\theta+s^2\sin^2\theta}
\]

by the displayed expression

\[
\frac{\sin\theta\cos\theta}{\sqrt{\cos^2\theta+s^2\sin^2\theta}}.
\]

The numerator and denominator token sequences are exactly identical. The source has \(s=u/v_*>0\). For every real \(\theta\),

\[
\cos^2\theta+s^2\sin^2\theta
\ge \min\{1,s^2\}(\cos^2\theta+\sin^2\theta)
=\min\{1,s^2\}>0.
\]

Hence both notations express the same well-defined quotient throughout the original integration interval, with the same \(s\) and \(\theta\). No derivative, integration bound, or parameter is altered.

## Cumulative byte recovery and bibliography

The separate recovery audit independently checked 233 conditions with zero failures. For each of the three cumulative files it verified the recorded insertion offsets and hashes, removed the exact 208-byte DLMF18 locator append, 206-byte DLMF5 locator append, and 218,930-byte continuation insertion, and recovered the predecessor byte for byte. Recovered SHA256 values are:

| Predecessor | Recovered SHA256 |
|---|---|
| 09 | `d0fbf7da7af46177628e09d3288f0253e36e6baf7b5d2bc6ecc69e8e3904d301` |
| 10 | `64c17d9ddf373462810515cb97621de8703c8d9e5dcf1cece5cce089159feaa2` |
| 14 | `50e5071b8bc1e1325f401764e7fdd3cda50994601b6f2e1bf00627864d665571` |

All 29, 29, and 27 inherited bibliography entries, respectively, retain their original bytes after reversing just the two targeted locator appends. The supplied locator spans appear exactly once and inside the correct existing entries. The only added key is `human:dlmf1`, appearing exactly once as H25. The common continuation and new bibliography appear exactly once. The raw accepted source and snapshot files are not edited by these insertions.

## Scope and limitations

This is an independent source/insertion/presentation check. The assembling agent reports a separate 68-page additive-supplement compilation with zero overfull, reference, citation, glyph, or warning diagnostics; this auditor did not rerun that compilation or inspect all PDF pages. The three cumulative sources are verified by structural inspection and exact byte recovery, and were not recompiled by this edition workflow. Historical duplicate GEL display tags in predecessors 09 and 10 remain byte-exact as explicitly required. These inherited ambiguities and the preserved raw TeX faults do not change the PASS result for the documented generated derivatives.
