# Independent body-preservation receipt

Status: PASS. This is an independent packaging comparison with the displayed AW/SP correspondence checked below; it makes no PDF-rendering claim.

Reader SHA256: `78f16ab6df3629232e143aa6e7caf40cd3fb88a16ed040f1f3947fc3bd0b20c4`.

Manifest SHA256: `e4d065dd58f19b3d875681737577b04e86bf8a12285e1f4d799fc9f8734e84a1`.

- All 22 manifest entries have the stated SHA256 and byte count and are byte-identical to their current original files.
- MCF.tex: the entire decoded source body is identical between its unique reader markers; only universal newline decoding is applied.
- MW.tex: the entire decoded source body is identical between its unique reader markers; only universal newline decoding is applied.
- MRE.tex: the entire decoded source body is identical between its unique reader markers; only universal newline decoding is applied.
- SP.tex: the entire decoded source body is identical between its unique reader markers; only universal newline decoding is applied.
- BC.tex: the entire original document body survives after removal of its one maketitle and prefixing label/ref/eqref targets with BC:. Every one of its 11 source macro declarations survives in the common preamble. The additional enclosing group, section title and equation-number prefix agree with BUILD_READER.py; no proof prose or display is dropped.
- AW.tex: the entire original document body is exact after removing its single maketitle. The original C macro is identical; Tr remains the same non-limits math operator via DeclareMathOperator; cP is imported with its original definition. AW1–AW23, including the full-spectrum AW13, commutator AW11, observation defect AW12 and q=1 refinements, remain intact.
- Original marked-product note: the entire original document body, including its abstract, is exact after removing only its single maketitle and tableofcontents controls. Errata are external reader prose and do not silently edit the original body.

The reader has exactly one document boundary pair and no input/include dependencies. No missing body, unexpected body alteration, missing source macro, or manifest mismatch was found. BUILD_READER.py was read and its body transformations were checked without executing the builder or changing any source.

## Added attribution and exact operator correspondence

The complete AW source and the new correspondence paragraph were read. The paragraph correctly identifies the earlier AW7 spectra and AW14 bound as reproduced in SP, while preserving AW13 and attributing the additional overlap calculation to SP8–SP10. AW uses frequency u_AW and interpolation t; assigning y=u_AW and x=t leaves the independent BC deformation variable unchanged. The literal convolution formula gives c_(1/4)=sqrt(2pi), so the two reference densities, including their mass factors, are equal; the arithmetic densities are both w_h^{*k}. Integrating the same monomials gives identical top Grams and M_N=I_N* M I_N. The relation map in SP has target H, whereas AW first targets P_N; the actual equality B_SP=I_N B_AW makes both projection formulas identical. With Q_(q−1)=0 this proves R_SP=U_AW and P_SP=W_AW, and their common relative derivative is T_SP=C_AW. AW10 independently supplies its isometry T_iso; substituting U=T_iso W T_iso^(-1) and using trace cyclicity gives Tr((U−W)C)=Tr(W T_iso^(-1)[C,T_iso]), with the stated commutator order and signs. Thus the preface does not confuse that isometry with the metric derivative. Finally MW9 says Psi_q commutes with A_a; A_a acts on each graded rho-piece by a^rho. Consequently the explicitly named combined operator T_(a,q)=A_a Psi_q acts there by omega a^rho, as the clarification states. These are exact identities on the displayed original objects; no new uniform estimate follows from their attribution.
