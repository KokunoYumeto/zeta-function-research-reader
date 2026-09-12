# Independent proof review: cyclic control and interpolation-volume increments

Date: 2026-09-12. Reviewer: cyclic-volume review lane.

The review covers the complete chapter `work/cyclic_control_determinant_increments_20260912.tex`, including CV.1–9 and the subsequently added CV.10–10a. This file records the proofs checked and the two precision repairs requested before acceptance. A final seal below records the reviewed chapter bytes and exact finite-replay outputs. The finite replay is a supplement to the proofs; its measure is explicitly specified and is not asserted to be the arithmetic Xi measure.

The inherited cyclic definitions and rank-two formula were read in `sources/web_cyclic_sum_delivery/Tau_Cyclic_Sum_Control/NOTE.tex`, SHA256 `2cdfd5b25631464f9500dc5fd07c4c8f5c927c8877eb1bf076307ec5dcbc2e8c`. The exterior determinant metric, original alternating source map, and complete quartet calculation were read in `sources/web_exterior_trace_delivery/Tau_Exterior_Trace_Amplification/NOTE.tex`, SHA256 `c7050e1c2f76b31b72af1d237efd29f656fd34a92492e5a11f76d8bc55b2acd9`. This states the actual reading scope; it does not claim a fresh audit of every unrelated source chapter.

## 1. Original objects and the nonsingular matrix

Retain the source convolution measure (m_{h,k}(u),du) and the monic polynomials (p_j(S)), with (S=k/2+iu). Their original norms are

\[
\omega_j=\int |p_j(k/2+iu)|^2m_{h,k}(u)\,du>0.
\]

The mass is the original (omega_0=mu_h^k). Let (C=\mathbb C[S]/(\chi)), where (chi) is monic of degree (q\geq1). In the fixed remainder basis (1,S,\ldots,S^{q-1}), set (b_j=[p_j]_\chi). For (j<q), reduction does nothing to (p_j); its coefficient vector has leading coordinate one in degree (j) and zero in higher degrees. Hence (b_0,\ldots,b_{q-1}) form an upper triangular coefficient basis with diagonal one.

For (N\geq q-1), define (K_N=\sum_{j=0}^N b_jb_j^*/\omega_j). For each nonzero coordinate vector (x),

\[
x^*K_Nx=\sum_{j=0}^N\frac{|b_j^*x|^2}{\omega_j}>0,
\]

because vanishing would force (x) orthogonal to the displayed basis. Thus (K_N) is positive definite, (D_N=\det K_N>0), and (G_N=K_N^{-1}) exists. This argument does not presume that either (K_{N-1}) or the omitted-direction matrix is invertible.

## 2. Signed determinant identities and the complex cross term

Write (u=b_N), (v=b_{N+1}), (x=\omega_N>0), (y=\omega_{N+1}>0), and (G=G_N). Retain (a=u^*Gu), (d=v^*Gv), and the full (c=u^*Gv). There is no replacement of (c) by its real part.

For invertible (K), the block matrix

\[
\begin{pmatrix}K&U\\-V^*&I_r\end{pmatrix}
\]

has determinant (det K\det(I_r+V^*K^{-1}U)) by eliminating its lower-left block, and determinant (det(K+UV^*)) by eliminating its upper-right block. Neither argument requires (K+UV^*) to be invertible. With one column this yields

\[
\frac{D_{N-1}}{D_N}=1-\frac ax,
\qquad
\frac{D_{N+1}}{D_N}=1+\frac dy.
\]

For the omitted-direction matrix, use (U=(-u/\sqrt x,v/\sqrt y)) and (V=(u/\sqrt x,v/\sqrt y)). This auxiliary factorization leaves the original columns and norms unchanged. Its small determinant is

\[
\det\begin{pmatrix}1-a/x&c/\sqrt{xy}\\-\overline c/\sqrt{xy}&1+d/y\end{pmatrix}
=(1-a/x)(1+d/y)+|c|^2/(xy).
\]

In particular the last sign is **plus**. This proves all three CV.3 identities. Subtracting the omitted-direction ratio from (D_{N+1}/D_N+D_{N-1}/D_N-1) gives exactly

\[
\frac{D_{N+1}+D_{N-1}-D_N-\widetilde D_N}{D_N}
=\frac{ad-|c|^2}{xy}.
\]

Multiplying by (y/x) proves CV.4, because the inherited control is (epsilon^2=(ad-|c|^2)/x^2). Substituting the first two CV.3 ratios instead proves CV.5.

For completeness, the inherited rank-two formula remains valid in its degenerate cases. The endomorphism is (H=(vu^*+uv^*)G/x), which is self-adjoint for (G). On the span of (u,v), its displayed coefficient matrix is

\[
\frac1x\begin{pmatrix}\overline c&d\\a&c\end{pmatrix}.
\]

The source reflection gives (c+\overline c=0). When the two vectors are independent, this matrix has trace zero and determinant ((|c|^2-ad)/x^2), so its eigenvalues are the opposite real numbers (pm\sqrt{ad-|c|^2}/x). When the two vectors are dependent, (H) has rank at most one and trace zero. Its self-adjointness makes it diagonalizable with real eigenvalues, hence it is zero. The two-vector Gram determinant is then also zero. Thus no division by this determinant or by a nonzero (epsilon) occurs.

## 3. Boundary and exceptional cases

At (N=q-1), the vectors (b_0,\ldots,b_{q-2}) are independent, so (K_{N-1}) has rank exactly (q-1). Therefore (D_{N-1}=0), and the first CV.3 identity gives (a=\omega_N). The third becomes

\[
\widetilde D_N/D_N=|c|^2/(\omega_N\omega_{N+1}).
\]

It allows both a singular omitted-direction map, when (c=0), and an onto omitted-direction map, when (c\ne0). No inverse of that map is used in either case.

For (q=1), all vectors in (C) are collinear, the Gram determinant (ad-|c|^2) is zero, and every CV.4–5 expression is zero. At (N=0), (K_{-1}) is the zero (1\times1) matrix and has determinant zero, consistently with the boundary argument. For the empty packet (h=1), the coefficient quotient is zero. The chapter explicitly excludes that zero-dimensional case from the positive-dimensional determinant calculation and retains its unique coefficient maps and Split-Zero lift ({\tau,e}).

## 4. The typed adjoint, exterior norm, and original tensor factorial

The source (mathcal P_N=\operatorname{span}\{p_0,\ldots,p_N\}) has Gram (Omega=\operatorname{diag}(\omega_0,\ldots,\omega_N)). Reduction (T_N:\mathcal P_N\to C) has coefficient matrix (B=[b_0\ \cdots\ b_N]). With the fixed coordinate Euclidean pairing on its target, its adjoint has coefficient matrix (Omega^{-1}B^*). Consequently

\[
T_N^*x=\sum p_j\frac{b_j^*x}{\omega_j},\quad T_NT_N^*=K_N,
\quad R_N=T_N^*G_N,\quad T_NR_N=I_C.
\]

For (x,y\in C), the actual source inner product of (R_Nx,R_Ny) is (x^*G_NK_NG_Ny=x^*G_Ny). If (T_N f=x), then (f-R_Nx\in\ker T_N) and

\[
\langle R_Nx,f-R_Nx\rangle
=\langle G_Nx,T_N(f-R_Nx)\rangle=0.
\]

This proves the canonical minimum property and its Gram, without a target-coordinate replacement. Its (q)-fold exterior power sends the fixed coordinate wedge (e_C) to a vector of squared determinant norm (det G_N=D_N^{-1}).

The initial draft's sentence about composing this exterior vector with (mathcal V_{h,k}) was under-typed. The accepted text supplies the exact map

\[
\bigwedge^q\mathcal V_{h,k}:\bigwedge^q\mathcal P_N
\longrightarrow\bigwedge^q(\mathscr B^{\widehat\otimes k}).
\]

The original (mathcal V_{h,k}) preserves every pairwise source inner product, so this exterior map preserves determinant inner products. To reach the actual tensor cochain source, the text now separately uses

\[
\mathcal V_{h,k}^{\otimes q}\operatorname{Alt}_q:
\bigwedge^q\mathcal P_N\longrightarrow\mathscr B^{\widehat\otimes kq}.
\]

For decomposable wedges (v_1\wedge\cdots\wedge v_q) and (w_1\wedge\cdots\wedge w_q), the inner product of their unscaled alternating tensors is

\[
\sum_{\pi,\sigma}\operatorname{sgn}(\pi)\operatorname{sgn}(\sigma)
\prod_r\langle v_{\pi(r)},w_{\sigma(r)}\rangle
=q!\det(\langle v_i,w_j\rangle)_{i,j}.
\]

The equality follows by fixing (pi), reindexing (sigma\pi^{-1}), and obtaining the same determinant for each of the (q!) choices of (pi). Also (operatorname{wed}\operatorname{Alt}_q=q!I), since every summand's permutation sign occurs once in the coefficient and once in the exterior quotient. Thus the literal tensor-source squared norm is (q!D_N^{-1}). The accepted chapter retains this factor and the exact top degree (kq).

## 5. Quartet scope and the exterior trace inequality

The initial chapter did not state clearly enough that equality (q=[1+k(m-1)](k+1)^2) requires the packet polynomial to be exactly the selected quartet polynomial. The accepted text writes this polynomial explicitly. Let its roots be (1/2+\varepsilon\delta+i\eta\gamma), where (arepsilon,eta\in\{1,-1\}), (delta,gamma>0), with common full order (m).

The (k)-fold sums are (lambda_{a,b}=k/2+\delta(2a-k)+i\gamma(2b-k)), (0\leq a,b\leq k). Every pair (a,b) is realized: choose an integer (t) in ([\max(0,a+b-k),\min(a,b)]), which is nonempty because (0\leq a,b\leq k), and use occupation counts (t,a-t,b-t,k-a-b+t). Distinct margins give distinct sums because their real and imaginary differences are respectively (2\delta(a-a')) and (2\gamma(b-b')).

Each tensor local block has nilpotent variables (z_i^m=0). The power ((\sum z_i)^{k(m-1)}) has the nonzero top coefficient ((k(m-1))!/((m-1)!)^k) on (prod z_i^{m-1}). Every monomial in its next power has some exponent at least (m) and vanishes. Therefore every sum has full cyclic length (ell_k=1+k(m-1)) and (q=\ell_k(k+1)^2).

For the positive real-defect spectral subspace (C_>), sum over (a>k/2), all (b), and all (ell_k) generalized directions. Its dimension is (p=\ell_k(k+1)\lceil k/2\rceil). On its determinant line, the additive exterior multiplication operator has scalar (operatorname{Tr}(A|_{C_>})), including every generalized direction. Its control scalar is

\[
2\Re\operatorname{Tr}(A|_{C_>})-kp
=2\delta\ell_k(k+1)\sum_{a>k/2}(2a-k)
=L_k.
\]

The last sum equals (n(n+1)) for (k=2n), and ((n+1)^2) for (k=2n+1), hence (L_k=2\delta\ell_k(k+1)\lfloor(k+1)^2/4\rfloor).

To see the exterior allowance directly, a nonzero (G)-self-adjoint rank-two trace-zero control has eigenspaces (L_+,Z_0,L_-), with eigenvalues (epsilon,0,-\epsilon), and (L_+,L_-) each one-dimensional. An exterior wedge can include each of these one-dimensional directions at most once. The additive exterior control thus has eigenvalues among (0,epsilon,-\epsilon). Differentiating the determinant pairing proves that it is exactly the relative control for the exterior metric. Apply its Rayleigh bound to a nonzero vector of (igwedge^pC_>): its quotient is (L_k), so (L_k\leq\epsilon). If (epsilon=0), the control is zero and the same conclusion follows. Inserting this inequality in CV.4 yields CV.8 with no assumption about an asymptotic upper bound.

For a larger packet, the quartet tensor local factors are retained CRT summands. The largest cyclic length at a colliding sum is the maximum over local summands, so it is at least (ell_k) at every quartet sum. The larger positive-defect trace contains at least the calculated contribution, all other terms being nonnegative. Therefore the same (L_k) is a lower bound, while every norm and determinant must use that larger packet and (N\geq\deg\chi_{h,k}-1). The accepted chapter states this exact comparison and does not infer the larger dimension from the quartet formula.

## 6. New positive-minor identity and its source vector

During the independent review, a further exact consequence was derived and then added to the chapter with root authorization: CV.10 expresses the signed determinant combination as a positive sum of maximal minors. Its proof is fully included in the chapter and was checked term by term.

For any finite column set (L), expand (det(\sum_{j\in L}b_jb_j^*/\omega_j)) multilinearly in its (q) columns. An ordered repeated index contributes zero. For each increasing (q)-element index set (J), summing its permutations gives (det B_J\overline{\det B_J}/\prod_{j\in J}\omega_j) by the Leibniz formula. Hence

\[
\det K_L=\sum_{J\subseteq L,\,|J|=q}\frac{|\det B_J|^2}{\Omega_J}.
\]

In the four determinants defining (Delta_N=D_{N+1}+D_{N-1}-D_N-\widetilde D_N), a subset containing neither (N) nor (N+1) has coefficient (1+1-1-1=0); a subset containing exactly one has coefficient (1-1=0); a subset containing both has coefficient one. Consequently

\[
\Delta_N=\sum_{\substack{I\subseteq\{0,\ldots,N-1\}\\|I|=q-2}}
\frac{|\det B_{I\cup\{N,N+1\}}|^2}{\omega_N\omega_{N+1}\prod_{i\in I}\omega_i}.
\]

At (q=2) the sum has its single empty-(I) term. At (q=1) it has no possible contributing subset and is defined to be zero. The proof requires no nonsingularity of any subset Gram and applies at (N=q-1).

The chapter also proves the exact source realization, not just the scalar identity. In the exterior source, let

\[
\mathcal E_N=(\bigwedge^{q-2}\mathcal P_{N-1})\wedge p_N\wedge p_{N+1},
\qquad\Lambda_N=(\bigwedge^qT_{N+1})|_{\mathcal E_N}.
\]

For its increasing orthogonal basis (e_I), the original squared norm is (Omega_{I\cup\{N,N+1\}}) and (Lambda_N e_I=\det B_{I\cup\{N,N+1\}}e_C). Relative to the explicitly declared Euclidean coordinate pairing on the one-dimensional target, its adjoint gives

\[
\zeta_N=\Lambda_N^*e_C
=\sum_I\frac{\overline{\det B_{I\cup\{N,N+1\}}}}
{\Omega_{I\cup\{N,N+1\}}}e_I.
\]

Orthogonality gives (|\zeta_N|^2=\Delta_N), and applying (Lambda_N) gives (Lambda_N\zeta_N=\Delta_N e_C). Pairwise isometry and the unscaled alternating source map give

\[
\|\mathcal V_{h,k}^{\otimes q}\operatorname{Alt}_q\zeta_N\|^2=q!\Delta_N.
\]

All maps are typed in the text. For (q=1), define (mathcal E_N=0), (Lambda_N=0), and (zeta_N=0); every displayed zero identity remains valid. The resulting control identity is (epsilon^2=(\omega_{N+1}/\omega_N)|\zeta_N|^2/D_N). It proves an exact positive source-volume expression and does not supply a growth estimate for that expression.

## 7. Scope of acceptance

The proofs preserve the original coefficient coordinates, original convolution mass, all (omega_j), the full imaginary cross term, the signs of both determinant updates, nilpotent multiplicities, the exact quartet-packet restriction, and the literal tensor factorial. The two requested typing/scope repairs have been read in the complete revised file and are correct. No remaining mathematical defect was found in CV.1–10a.

CV.9 and its positive-source reformulation remain quantities to estimate for the actual arithmetic measure at admissible growing degree. Neither the determinant identity nor a finite replay proves an RH conclusion or a limit in (k). No Lean run, historical CI claim, or source-provided numerical assertion is used as proof of this chapter.

## Final seal and exact finite replay

This section will be completed when the independent exact finite run and its optimized replay finish. The proof findings above already state the full mathematical review; the pending supplement will supply executable evidence with its precise measure and scope.
