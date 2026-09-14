# Independent review of the main single-primary boundary calculation

The entire file single_primary_boundary_control.tex, SP.1–34, was read independently after deriving the full one-factor contour and monodromy calculation from BC.tex.

First reviewed main snapshot SHA256:
832C5DFD08D544C633732E63BA1A4EC83D943EC8C50A41AE08BE5889ED3E1A0C

No proof error found in that snapshot.

The derivation agrees in all constants, signs, monomial and contour orders, and inverse monodromy conventions. In particular, the period action in SP.24 is exact because the lower-shift entries acquire u^(1/n), and conjugation by the cycle monodromy acquires the factor zeta. Its derivative is precisely the transported connection commutator. The same calculation proves every term and coefficient in the full Taylor-unit formula SP.29.

SP.30–31 correctly retain the common irregular scalar and describe the exact holomorphic matrix after factoring that scalar in the period expression. The constant invertible factors identify its image with the sum of the ideals (v), ..., (v^m), whose cokernel has length m(m+1)/2. The image lattice itself has an m-dimensional fibre, and its inclusion into the displayed ambient lattice has zero reduction modulo v. The scalar factor is not claimed to be a meromorphic gauge.

SP.34 correctly identifies the full kernel by the degree-raising property of L_u, and integration of the exact exponential derivative proves its period factorization. The rank is m. Two precision edits were sent to the parent: explicitly fix u≠0 for the period statement, and say that the restriction to the retained remainder frame is positive definite, rather than wording that could claim this frame is the unique positive complement.

The only unit-transport scope issue to guard is identifying the constant finite coordinate matrix with multiplication on arbitrary twisted de Rham representatives. The independent proof gives the exact constant coordinate map and the complete derivative defect:

v_pol Lq = L(v_pol q) − u v_pol′ q.

If deg p<m and v_pol p=hq+r is ordinary monic division, the full differential remainder is r−u q′, because deg q′<m. This correction was subsequently read in the final bounded audit below and is now certified for that recorded core snapshot.

## Final bounded core review

The final SP.25–36 text was read in full, including the complete Taylor coefficient identities, inverse matrix, theta source maps, actual period and connection transport, new representative defect, cover lattice and cokernel, source metric, and enlarged-source kernel. The remaining support/scope ending was also read.

Latest reviewed complex core SHA256, before any SPF append:
B68000AC12F65176F112C42AF282656CEE9640BD472F0705D43613BC053E5F52

The file contained 647 lines and only the SP complex portion at this snapshot. Appending SPF changes the whole-file hash; this receipt certifies the displayed SP core, not an unread appended SPF portion.

No proof error found. SP.30 has the correct minus derivative term for the original plus-sign differential L_u=u∂s+h. SP.31 retains the full r−u q′ remainder; its degree bound follows from deg(v_pol p)≤2m−2, with zero quotient when the degree is below m. The stated constant U_s coefficient extension is now explicitly distinguished from multiplication on arbitrary twisted representatives. SP.36 now fixes u≠0 and states positivity on the retained remainder frame without claiming uniqueness of that complement. Both requested precision edits are complete.

No deduction about tensor invariants, finite-field comparison, or RH is made by this review.

Independent deliverables:

- single_primary_complex_review.tex, SPR.1–36: complete proof and exact contour homotopy.
- matrix_audit.md, MA1–38: a second independent full algebra, source-unit, and representative audit.
- compile_review.tex and compile_review.log: five-page draftmode TeX compilation; no overfull, underfull, undefined, LaTeX warning, or TeX-error entries. The expected pdfdraftmode notice is present; no PDF was generated or visually inspected.

The algebra reviewer read SPR.1–34 in full and found no error. SPR.35–36 state its independently proved coefficient-map and remainder formulas. Main SP.1–34 was subsequently read in full by this reviewing agent.

Independent TeX SHA256:
FFE564712580717BAE698284B205BE90C8734EF205E95C48A0270E8877D7355E

Matrix audit SHA256:
A9B4D6B8A956BCD77E9F330C7E1EFEF06B7B9A4D299022D7CDDDE3C1CD392A61

BC source SHA256:
6575B8E33FF00BEF8B08E214B974B9BD1E966C3BED4B573C5CA274206A69E9FA
