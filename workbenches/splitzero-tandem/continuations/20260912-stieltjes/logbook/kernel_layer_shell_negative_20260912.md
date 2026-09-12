# Exact calibration: the actual orthogonal shell cannot be replaced by raw monomials

For the requested fixture, the actual top-jet row and projected derivative both have rank zero, while the raw homogeneous degree-one jet row has rank one. The unprojected derivative has rank one and lies entirely in the old relation space. These are four separately computed maps.

## Original objects and finite inner product

Retain (h(s)=s-\tfrac12), tensor degree (k=2), total-degree level (N=1), and unit (v=1). Each variable takes the original values (s=\tfrac12+it) with (t=-1,0,1), each of weight one. On polynomials in (s_1,s_2), use

\[
\langle f,g\rangle=
\sum_{t_1,t_2\in\{-1,0,1\}}
\overline{f(\tfrac12+it_1,\tfrac12+it_2)}
g(\tfrac12+it_1,\tfrac12+it_2).
\]

The full-jet map is (J(f)=f(\tfrac12,\tfrac12)), with codomain (E=\mathbb C). Write (P_n=\mathbb C[s_1,s_2]_{\leq n}), (L_n=\ker(J|_{P_n})), and (z_i=s_i-\tfrac12) as an explicit polynomial identity. Constants and original (s_i)-coordinates remain in every map below. The shift (s_i\mapsto z_i+\tfrac12) is an invertible polynomial substitution, with inverse (z_i\mapsto s_i-\tfrac12).

The values of the first three monic orthogonal polynomials, in the original order (t=-1,0,1), are

\[
\begin{array}{c|c|c}
p_j(s)&(p_j(\tfrac12-i),p_j(\tfrac12),p_j(\tfrac12+i))&\kappa_j\\\hline
1&(1,1,1)&3\\
s-\tfrac12&(-i,0,i)&2\\
(s-\tfrac12)^2+\tfrac23&(-\tfrac13,\tfrac23,-\tfrac13)&\tfrac23.
\end{array}
\]

The displayed vectors are pairwise orthogonal by direct summation. Their leading coefficients are one, so uniqueness of the monic orthogonal polynomial in each degree identifies them. Product orthogonality gives squared norms (9,6,6,2,4,2) for the ordered product basis indexed by

\[
(0,0),(0,1),(1,0),(0,2),(1,1),(2,0).
\]

## Original right inverse and the two shell maps

In the original monomial basis ((1,s_2,s_1)), the jet and Gram are

\[
J_{\mathrm{raw}}=\begin{pmatrix}1&\tfrac12&\tfrac12\end{pmatrix},
\qquad M_{\mathrm{raw}}=
\begin{pmatrix}
9&\tfrac92&\tfrac92\\
\tfrac92&\tfrac{33}4&\tfrac94\\
\tfrac92&\tfrac94&\tfrac{33}4
\end{pmatrix}.
\]

The checker constructs the constrained minimum directly from these original objects:

\[
\mathcal K_1=J_{\mathrm{raw}}M_{\mathrm{raw}}^{-1}J_{\mathrm{raw}}^*
=\tfrac19,quad G_1=9,quad
M_{\mathrm{raw}}^{-1}J_{\mathrm{raw}}^*G_1
=\begin{pmatrix}1\\0\\0\end{pmatrix}.
\]

Thus (R_1:E\to P_1) is (R_1u=u). An independent proof is that every preimage of (u) is uniquely (u+a z_2+b z_1), whose squared norm is (9|u|^2+6|a|^2+6|b|^2). Its unique minimum is attained at (a=b=0).

The actual top degree-one columns are (p_0(s_1)p_1(s_2)=z_2) and (p_1(s_1)p_0(s_2)=z_1). Their full jets and original Gram are

\[
\mathsf A_1=\begin{pmatrix}0&0\end{pmatrix},\qquad
\mathsf D_1=6I_2.
\]

The raw homogeneous shell (H_{\mathrm{raw}}=\operatorname{span}\{s_2,s_1\}) has jet row ((\tfrac12,\tfrac12)), of rank one. The exact isomorphism relating this shell to the actual orthogonal shell is

\[
T:H_{\mathrm{raw}}\longrightarrow\operatorname{span}\{z_2,z_1\},\qquad
T(a s_2+b s_1)=a z_2+b z_1
=(I-R_1J)(a s_2+b s_1).
\]

Its inverse sends (a z_2+b z_1) to (a s_2+b s_1). It induces the identity on leading classes in (P_1/P_0), but its exact effect on the retained lower term is

\[
f-Tf=\tfrac{a+b}{2},\qquad J(Tf)=0,\quad J(f)=\tfrac{a+b}{2},
\]
\[
\|f\|^2=6(|a|^2+|b|^2)+\tfrac94|a+b|^2,
\qquad\|Tf\|^2=6(|a|^2+|b|^2).
\]

In full polynomial coordinates the same change is

\[
Q=\begin{pmatrix}1&-\tfrac12&-\tfrac12\\0&1&0\\0&0&1\end{pmatrix},
\quad (1,s_2,s_1)Q=(1,z_2,z_1),
\quad J_{\mathrm{raw}}Q=(1,0,0).
\]

The lower constant columns in (Q) explain the jet-rank difference exactly.

## Original derivative, relation layer, and the false replacement

The summed Mellin-side derivative is the typed multiplication map

\[
\mathcal D:P_1\to P_2,\quad f\mapsto(s_1+s_2)f.
\]

It induces the scalar packet action (A=1). Therefore

\[
B_1=\mathcal D R_1-R_1A,\qquad
B_1u=(s_1+s_2-1)u=(z_1+z_2)u.
\]

The original relation columns are (L_1=\operatorname{span}\{z_2,z_1\}), with Gram (6I_2). Hence (P_{L_1}B_1=B_1), and

\[
\operatorname{rank}B_1=1,\quad B_1^*B_1=12,
\qquad C_1=(I-P_{L_1})B_1=0,
\quad\operatorname{rank}C_1=0=\operatorname{rank}\mathsf A_1.
\]

At the next degree, in the order ((0,2),(1,1),(2,0)), the product-polynomial row has jets

\[
\mathsf U_1=(\tfrac23,0,\tfrac23),\qquad
\mathsf D_2=\operatorname{diag}(2,4,2).
\]

Subtracting the original right inverse gives actual relation columns

\[
\mathscr E_1=(z_2^2,z_1z_2,z_1^2),\quad
H_1^{\mathrm{lay}}=
\begin{pmatrix}6&0&4\\0&4&0\\4&0&6\end{pmatrix}
=\mathsf D_2+\mathsf U_1^*G_1\mathsf U_1.
\]

Each column lies in (L_2\cap L_1^\perp), by evaluation and oddness. Their leading monomials prove independence; (dim L_2-\dim L_1=5-2=3) proves they form the full layer basis. Their Gram has determinant (80), and

\[
x^*H_1^{\mathrm{lay}}x=
2(|x_1|^2+|x_3|^2)+4|x_2|^2+4|x_1+x_3|^2>0
\]

for (x\ne0). The coefficient incidence map is

\[
\mathsf T_1=\begin{pmatrix}1&0\\1&1\\0&1\end{pmatrix}.
\]

Consequently KL.13 gives the actual (C_1=\mathscr E_1\mathsf T_1\mathsf D_1^{-1}\mathsf A_1^*G_1=0). Replacing only its actual top jet row by the raw homogeneous row instead produces the explicit different map

\[
C_{\mathrm{raw}}=
\mathscr E_1\mathsf T_1(6I_2)^{-1}
\begin{pmatrix}\tfrac12\\\tfrac12\end{pmatrix}9
=\tfrac34(z_1+z_2)^2,
\quad C_{\mathrm{raw}}^*C_{\mathrm{raw}}=\tfrac{81}{4},
\quad\operatorname{rank}C_{\mathrm{raw}}=1.
\]

This is an explicit false substitution into the exact map, not just a difference in upper bounds. The false equality (operatorname{rank}C_1=\operatorname{rank}(\tfrac12,\tfrac12)) is (0=1). It also changes the predicted KL.18 quotient dimension from the actual (3) to (2): here (Z_1=\operatorname{im}(\mathsf D_1^{-1}\mathsf A_1^*)=0), so the actual quotient has dimensions (2+1=3). The refined KL.15 weight bound is zero because (C_1=0); the actual form (A^*G_1+G_1A-2G_1) is indeed zero. Replacing that zero bound by a larger bound would merely weaken it; the rank equality and quotient dimension above exhibit the genuinely false conclusions.

## Finite-degree scope and execution

Evaluation on the nine-point grid is injective on (P_2): fix either variable at each grid value and apply the three-root criterion to the other variable, then apply it to each coefficient polynomial. It is not injective on (P_3), since the nonzero polynomial ((s_1-\tfrac12)^3+(s_1-\tfrac12)) vanishes on the entire grid. This fixture thus calibrates the positive polynomial spaces through degree two used above. It supplies no all-degree arithmetic or KL.19–KL.20 analytic certificate.

The independent checker is [kernel_layer_shell_negative_20260912.py](workspace:/work/kernel_layer_shell_negative_20260912.py). Its SHA256 is `6426f7106fcb09f835e1453adda13eaf417bc6fd67018ab58c42637525e3d342`. The four-mode runner is [kernel_layer_shell_negative_replay_20260912.py](workspace:/work/kernel_layer_shell_negative_replay_20260912.py).

All 16 test methods pass normally and under optimized Python. Adding `--self-test-failure` runs the same methods plus the exact false rank equality: both modes report seventeen methods, one deliberate failure, no errors, and exit status one. The checks use `unittest` operations, which remain active under `-O`; there are no Python `assert` statements. All exact mathematical records agree between the paired modes. The recorded runtime is SymPy **1.13.1**, distinct from the parent's separate pinned 1.14.0 source-suite replay.

The [receipt](workspace:/work/kernel_layer_shell_negative_20260912_receipt.json) retains commands, exit codes, all matrices, result hashes, and log hashes. An independent subagent derived the same values without executing this checker. The original stage, cumulative TeX, and parent's checker were not edited.

## Read-only review of the parent's quotient and consecutive-layer calibrations

The complete parent checker `output/split_zero_rh_tandem_2026-09-12/checks/kernel_layer_continuation.py` was read, with particular attention to `quotient_coordinates` at line 85, `test_02_actual_rank_kernel_and_whole_quotient` at line 176, and `test_03_derivative_on_original_relation_columns_two_levels` at line 220. The reviewed file's SHA256 is `6eefa4866fa21367b8c5791184459b89b8e4de632754e681c9640e0695e398a8`. No source error or incorrect mathematical calibration claim was found in the requested functions. The parent checker was not run or edited by this reviewer.

For the quotient calculation, its matrix (Z=\mathsf D_N^{-1}\mathsf A_N^*) has domain (E) and codomain (\mathsf H_N). Taking the ordinary transpose nullspace of (Z^T), then transposing its basis columns into rows, correctly constructs a **complex-linear** annihilator (Q_Z\) satisfying (Q_ZZ=0). The checked rank (\operatorname{rank}Q_Z=\dim\mathsf H_N-\operatorname{rank}Z) proves that its full kernel is (operatorname{im}Z). The selected pivot columns give an embedding (I_P) with (Q_ZI_P) invertible; consequently (S_Z=I_P(Q_ZI_P)^{-1}) has the verified right-inverse identity (Q_ZS_Z=I).

If (q,r,\iota) are the ordered polynomial division matrices, the checker constructs precisely

\[
Q=\begin{pmatrix}Q_Zq\\r\end{pmatrix},\qquad
S=\begin{pmatrix}\mathsf T_NS_Z&\iota\end{pmatrix}.
\]

Its exact tests (QS=I), (Q\mathsf T_NZ=0), and the quotient dimension verify the quotient map and section. The additional rank test on the concatenated matrix ([\mathsf T_NZ\mid SQ-I]) establishes that the entire inverse error has image in (operatorname{im}(\mathsf T_NZ)). The source-space test on ([C_N\mid\mathscr E_N(SQ-I)]) verifies the same statement after the actual layer embedding. This explicitly checks both quotient inverse identities in the retained source coordinates.

The consecutive-layer test reconstructs the original numerator rows of (mathscr E_N) and (mathscr E_{N+1}) from the source product polynomials, original constrained coefficients, and original next-jet columns. It retains the complete polynomial difference

\[
\Delta=(s_1+\cdots+s_k)e^{(N)}
             -e^{(N+1)}\mathsf T_{N+1}.
\]

Evaluation includes the original product multiplier (\prod_i v_h(s_i)), and is compared to the actual difference (D^{(k)}\mathscr E_N-\mathscr E_{N+1}\mathsf T_{N+1}). The projector test places that full difference in (\mathcal L_{N+1}); the subsequent projection identity proves the induced quotient map. Ordered division verifies each complete ideal remainder and reconstructs every retained relation. Both Koszul signs are present. The difference's total degree bound (N+1) and its primitive degree bound (N+1-d) are checked separately.

The fixtures used there have at most degree four in either variable and five distinct nodes in each variable; their positive source multiplier is nonzero at the grid nodes. Thus these particular evaluation comparisons preserve the complete polynomial identities through the required degrees. The parent's general all-degree claims remain supported by the written mathematics, rather than inferred from these finite grids.

One optional direct strengthening was communicated: alongside the checked incidence rank (operatorname{rank}\mathsf T_{N+1}=\dim\mathcal E_N), test the actual matrix rank (operatorname{rank}(\mathscr E_{N+1}\mathsf T_{N+1})=\dim\mathcal E_N). The existing source construction and positive Gram already imply this equality; the added check would make the source-image injection count explicit. It is not an outstanding correction.
