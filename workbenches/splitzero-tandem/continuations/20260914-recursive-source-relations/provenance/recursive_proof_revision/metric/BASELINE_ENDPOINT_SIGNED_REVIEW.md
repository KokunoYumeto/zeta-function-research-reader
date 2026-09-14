# Independent final review of signed endpoint propagation

Date: 2026-09-13. Verdict: **PASS on the final pinned mathematical sources below.**

This is a bounded independent review of the new FV.M16a–c construction, the signed entries of FV.M17, and the signed R44 replacement. It supplements the earlier accepted five-entry endpoint review; it does not replace that review or claim a fresh audit of the entire cumulative manuscript. No shared mathematical source was edited by this reviewer. A primitive-orientation clarification was sent to the author, incorporated by the author, and reread before this verdict.

## Exact reviewed sources

All paths below are relative to workspace:/work/backpropagation_20260913/.

| Source | SHA-256 |
|---|---|
| incoming_pr29_metric/incoming_source_metric_control.tex | ce4b0968607fd06d7203ca498e66ce3dbe78e93e8eb3fe9079a106fa188ae0d8 |
| recursive_metric_transport.tex | 8110fbb1c5796ad36a75cf364b7744d5852419608b9e890d83b5fde5c0a9844f |
| metric/recursive_endpoint_specialization.tex | 8e65e4a3a7531bb5111ae867dc50624420c1bdf52897d5c9476c2dc81d2f63d8 |
| metric/ENDPOINT_CONCLUSION_REPLACEMENTS.json | 79d300216798edc4f42985ab73a4e9696c3639b648531938fe6cef68c3aa2f0d |
| metric/ENDPOINT_CONCLUSION_REPLACEMENTS.md | 12182df5e9f97a5d755efb0b103cccdb9d8c90959aeabe1e00789f3035428cd9 |

The assignment mentioned an earlier ISM hash beginning c1586e0c. The actual file read was the ce4b0968 version above. The complete ISM31–37 text was read, together with ISM1–3, 13–20, 28–30 and the relevant source/primitive/support definitions in ISM38–43. RMT19–22 and the full current endpoint-specialization file were read. The original FV.M1–6, FV.M11–14 and R44 endpoint-loss identities were checked at their actual use sites.

## Original forms, typed maps and sign

The common coefficient space is H=P_(2q), with dimension n=2q+1. Both sources use the original ascending monomials at S=k/2+iu. Under the frequency identification y=u, the reference measure is literally r_(1/4)^{*k}(u)du, with its retained mass (sqrt(2 pi))^k; the arithmetic measure is w_h^{*k}(u)du. Thus the two moment matrices M_0 and M_1, and every M_x=(1-x)M_0+xM_1, are equal coefficient by coefficient across ISM, RMT and FV.

ISM's included multiplication map B_N:P_(N-q) -> H equals FV's I_N B_N, where FV's unpadded B_N has codomain P_N. ISM's canonical section rho_N:E -> H equals I_N R_N(x). To verify the latter equality, both sections have remainder identity, both take values in P_N, and both are M_x-orthogonal to the same relation range. Their difference therefore lies both in that range and its orthogonal complement. Its squared M_x norm is zero, so the difference vanishes. The quotient Gram matrices and all four determinants consequently agree individually.

It follows that X_x in ISM equals C_x=M_x^{-1}(M_1-M_0) in FV, while Pi_N=P_N-Q_N and A_ISM=U_x-W_x=A_x. The symbol C:E -> H in ISM is the literal remainder lift, whose role and type are distinct from the endomorphism C_x and are explicitly stated in the new text. No identity between those differently typed symbols is used.

The scalar correction in ISM is B(M_1)-B(M_0), hence equals Delta_(h,k)=F(1)-F(0). Its base endpoint is B^Gamma_(h,k). The truncation order is exactly L_ISM=L_RMT=p_N, with p_N an integer at least zero; it changes neither the polynomial cutoff N nor L_(h,k), q, k, u or x.

## Finite construction and error calculation

Let D=M_0^{-1}M_1. Positivity makes D self-adjoint in M_0 with positive eigenvalues b_1,...,b_n. On each eigenline M_x multiplies M_0 by lambda_j(x)=1-x+xb_j>0. Therefore every real function of D used here is also self-adjoint in M_x. The endpoint metrics themselves are unchanged.

Write B_x^circ=(1-x)I+xD, alpha_x=(lambda_1+lambda_n)/2 and H_x^circ=I-B_x^circ/alpha_x. Then C_x=(B_x^circ)^{-1}(D-I). Multiplication of the finite sum by I-H_x^circ gives exactly

    (I-H_x^circ) sum_(r=0)^p (H_x^circ)^r
       = I-(H_x^circ)^(p+1).

Since all factors commute, the FV.M16a operator satisfies

    C_x-C_x^[p]=(H_x^circ)^(p+1) C_x=R_x^[p].

Centering this exact residual gives E_x^[p]=R_x^[p]-Tr(R_x^[p])I/n. Trace zero of A_x then proves

    F'(x)=Tr(C_x^[p] A_x)+Tr(E_x^[p] A_x).

This also proves equality of the displayed signed center with ISM's centered-Y version: subtracting Tr(C_x^[p])I/n contributes zero to its pairing with A_x.

In an M_x-orthonormal basis the two operators in the last trace are Hermitian. Cauchy–Schwarz for their matrix entries bounds the absolute residual pairing by sqrt(Tr((E_x^[p])^2) Tr(A_x^2)). Integrating over the original oriented interval [0,1] therefore yields exactly

    j_p-e_p <= Delta_(h,k) <= j_p+e_p.

The eigenvalues of H_x^circ are 1-lambda_j/alpha_x. Their largest absolute value is x(b_n-b_1)/(2(1-x)+x(b_1+b_n)), which increases from zero to theta=(b_n-b_1)/(b_n+b_1)<1. The eigenvalues of C_x are (b_j-1)/(1-x+xb_j), whose absolute values are at most |b_j-1|/min(1,b_j). Thus

    Tr((E_x^[p])^2)
      = sum_j delta_j(x)^2 - (sum_j delta_j(x))^2/n
      <= theta^(2p+2) K_D,

with the full K_D in FV.M16b and delta_j the exact residual eigenvalues. The centering term has its required negative sign.

The nested flags give U_x and W_x the full spectra 0^[q],1^[2],2^[q-1]. Each therefore has rank q+1 and dominates its range projection. Their ranges in dimension 2q+1 intersect in dimension at least one. The product trace of their range projections is at least this intersection dimension; positivity of trace products under increasing either positive factor gives Tr(U_x W_x)>=1. Hence

    Tr(A_x^2)=8q-4-2 Tr(U_x W_x) <= 8q-6.

This proves the retained constant, including q=1. Integration over an interval of length one gives

    0 <= e_p <= theta^(p+1) sqrt(K_D(8q-6)) -> 0.

If all b_j coincide, then H_x^circ=0 and the exact trace pairing with the scalar C_x vanishes, so j_p=e_p=Delta_(h,k)=0. The formulas include this case without an indeterminate zero power because p+1>=1. All integrands are continuous finite matrix expressions. The convergence is for the fixed actual pair of source forms. Numerical evaluation still requires its own integration error, as both FV and R44 explicitly retain; no uniform assertion in k has been inserted.

## Endpoint intersection and preservation

Adding B^Gamma_(h,k) to the signed interval gives the lower endpoint B^Gamma+j_p-e_p and upper endpoint B^Gamma+j_p+e_p. FV.M17 and R44 put these in the lower maximum and upper minimum respectively. Every earlier linear/nonlinear bound remains present. Intersecting intervals each proved to contain the same actual B_(h,k) preserves a nonempty enclosure of that endpoint.

An independent preservation reader compared the current JSON against metric/historical_seals/five_entry_20260913/ENDPOINT_CONCLUSION_REPLACEMENTS.json, SHA-256 0284d3ab60aed50ace4b1985c662cc6ad817aca22ed510181a7d49ce6452d3d3. All four metadata records, old source blocks and baseline hashes are unchanged. The R45 body and both R47 bodies are identical after JSON decoding. Only R44's new body gains the signed construction paragraph and the two signed endpoint entries.

The original definitions E_0=log(V_(q-1)/V_q), E_1=log(V_(2q-1)/V_(2q)) and B=2C_k+E_0+E_1 remain literal. The whole existing R44 downstream tail beginning “Monotonicity of the exact inverse coordinate” is unchanged, including

    4(q-1) log(L_(h,k)/(C_h^bal q))+E_0+E_1 <= B_hi,
    C_k <= (B_hi-E_0-E_1)/2.

Thus the sharper B_hi propagates through the original identities without deleting either endpoint loss. The Markdown rendering has the definitions at lines 26–27, signed interval at line 55, endpoint signs at lines 65 and 69, and retained losses at lines 78 and 80. The baseline research_conclusion.tex still hashes to cec03014398811e5fa4788cb7b6f4816123c026d673a1a9a0398b7fded360e3b.

## Exact primitive orientation repair

ISM38 uses rho_1-rho_0, whereas FV.M12 uses I_N(R_N(x)-R_N(1)). The final source now explicitly instantiates only the primitive construction with ordered pair (M_1,M_x). Its section difference then equals FV's difference exactly. At x=0, relative to the original ordered pair (M_0,M_1), the section difference, its linear primitive and its proper-source residual are each multiplied by -1. This is an exact linear map on the original source and quotient; it leaves the Gamma-to-arithmetic definition of Delta and every signed estimate above unchanged.

The proper-support residual remains the kernel quotient

    (d C_full^(k-1) intersect C_lambda^k) / d C_lambda^(k-1),

with the same representative map and the original one-leg map [v] -> [Theta v] from V/W. The new matrix construction changes no source representative, face, outer label, full unit or theta primitive. The explicit orientation paragraph was reread at lines 167–178 of the final endpoint-specialization source.

## Review boundary

No mathematical defect remains in the signed additions reviewed here. Compilation was performed by the owning agent; this receipt certifies the bounded mathematical and preservation checks above and does not independently claim compilation or visual inspection. Earlier proof modules and the broader research programme retain their previous review scope.
