# Exact comparison of the common and phase generator boundaries

This note completes the assigned comparison inside the actual original arithmetic source. It retains the quotient \(Q=\mathscr B/\Theta V\), \(g=2\xi\), the full unit \(j_h(g/h)\), every selected nilpotent order, the logarithmic coordinates of H9, and the measure \(d\theta/(2\pi)\). Its calculations show that the gluing error and the difference of two generator boundaries can both tend to zero while the full generator boundary has the already proved positive quartet floor. No existence of an off-line zero is asserted.

The parent assignment, verbatim, was:

> Independent bounded read/derivation: read original H NOTE.md complete at output/split_zero_rh_tandem_2026-09-12/sources/web_holonomy_descent_delivery/Tau_Holonomy_Descent_Control/NOTE.md, focus H24-H56. Derive exact generator defect difference between common lift C and phase lift C_theta, and quantify with computed source derivative moments and eta. Show precisely how gluing o(k) can be arranged by L choice yet full generator defect cannot under quartet. Do not redo HT floor; use it if needed. Save complete note in work/rh_counterfactual_20260913/total_object/phase_scaling_audit/comparison_review.md, verify parent dir exists (I'll create now). No global edits. I derive repeated-full-jet spectral generator floors and aggregate scaling.

## 1. Original spaces and the actual source at both degrees

Fix a finite original packet \(h\), a tensor order \(k\geq2\), and the exact original cyclic polynomial \(\chi=\chi_{h,k}\) of degree \(q>0\). Retain

\[
 E=\mathbb C[S]/(\chi),\qquad A=M_S:E\longrightarrow E,
 \qquad P_N=\mathbb C[S]_{\leq N},\quad N\geq q-1,
 \qquad J_N=\pi_\chi|_{P_N}.
 \tag{PC.1}
\]

The source and its half-density version are precisely

\[
 \mathcal VP=P(D_1+\cdots+D_k)F_h^{\otimes k},
 \qquad \mathcal MF_h=g/h,\qquad
 \Psi_N=\mathcal U_k\mathcal V|_{P_N}.
 \tag{PC.2}
\]

Here \(D_i=-x_i\partial_{x_i}\),
\(r=\log x_k\), \(z_i=\log x_i-\log x_k\), and

\[
 (\mathcal U_kF)(r,z)
 =e^{(kr+\sum_{i<k}z_i)/2}
 F(e^{r+z_1},\ldots,e^{r+z_{k-1}},e^r).
\]

The target is \(L^2(\mathbb R,dr;\mathcal K)\), with
\(\mathcal K=L^2(\mathbb R^{k-1},dz)\). Its relative variables are retained. The original full-jet map is the injection

\[
 \eta_{\mathrm{H8}}[P]
 =j_h(g/h)^{\otimes k}P(A_h^{(k)})1,\qquad
 J^{(k)}\mathcal VP=\eta_{\mathrm{H8}}\pi_\chi P.
 \tag{PC.3}
\]

Here \(E_h=\mathbb C[s]/(h)\), \(A_h=M_s:E_h\to E_h\), and \(A_h^{(k)}=\sum_{i=1}^kA_{h,i}\) acts on \(E_h^{\otimes k}\). Its restriction to the displayed cyclic image agrees with the original \(A=M_S\). The subscript merely identifies the original map called \(\eta\) in H8; the scalar source error below is the \(\eta\) of H32. No unit factor is removed from (PC.3).

Write \(\iota_N:P_N\hookrightarrow P_{N+1}\) for inclusion and
\(\mathsf S_N:P_N\to P_{N+1}\), \(P\mapsto SP\), for multiplication before reduction. These have different codomains from \(A\), and satisfy

\[
 J_{N+1}\mathsf S_N=AJ_N,\qquad
 J_{N+1}\iota_N=J_N,\qquad
 \partial_r\Psi_N
 =\Psi_{N+1}\bigl((k/2)\iota_N-\mathsf S_N\bigr).
 \tag{PC.4}
\]

The last formula follows by applying the exact H10 identity
\(\mathcal U_kD^{(k)}=(-\partial_r+k/2)\mathcal U_k\) to each polynomial column. It is why the comparison below uses a source bound at degree \(N+1\).

For \(L>0\) define

\[
 W_{N,\theta}=\mathcal Z_{L,\theta}\Psi_N,\qquad
 M_N=\Psi_N^*\Psi_N,\qquad
 M_{N,\theta}=W_{N,\theta}^*W_{N,\theta}.
 \tag{PC.5}
\]

The phase source is in
\(\mathcal H_{L,\theta}=L^2([0,L],dr;\mathcal K)\).
Its generator is
\[
 D_{L,\theta}=-\partial_r+k/2,\qquad
 \operatorname{Dom}D_{L,\theta}
 =\{f\in H^1([0,L];\mathcal K):f(L)=e^{-i\theta}f(0)\}.
\]
All columns used here belong to this domain. The original weighted source bounds justify the periodization and its \(r\)-derivative. In particular no derivative in \(\theta\) is involved when \(D_{L,\theta}\) is applied to a coefficient map depending on \(\theta\).

The complete phase transform gives
\[
 \int_0^{2\pi}M_{N,\theta}\,\frac{d\theta}{2\pi}=M_N.
 \tag{PC.6}
\]

## 2. The exact relation map between the two sections

Let \(B_N:\mathbb C^{N-q+1}\hookrightarrow P_N\) be the coefficient matrix of literal multiplication by \(\chi\), with zero-dimensional domain if \(N=q-1\). Thus
\(\operatorname{im}B_N=\chi P_{N-q}=\ker J_N\).
Keep the original sections

\[
 \begin{aligned}
 G&=(J_NM_N^{-1}J_N^*)^{-1},
 &C&=M_N^{-1}J_N^*G,\\
 G_\theta&=(J_NM_{N,\theta}^{-1}J_N^*)^{-1},
 &C_\theta&=M_{N,\theta}^{-1}J_N^*G_\theta .
 \end{aligned}
 \tag{PC.7}
\]

Since \(J_NC=J_NC_\theta=I_E\), the difference
\(Z_\theta:=C-C_\theta:E\to P_N\) has image in \(\ker J_N\). Hence there is a unique polynomial coefficient map
\(X_\theta:E\to P_{N-q}\) such that

\[
 Z_\theta=\chi X_\theta=B_NX_\theta,\qquad
 X_\theta=(B_N^*M_{N,\theta}B_N)^{-1}
 B_N^*M_{N,\theta}C
 \tag{PC.8}
\]

in the fixed coefficient bases. An inverse on a zero-dimensional space in this notation is the unique empty map.

Indeed \(B_N^*M_{N,\theta}C_\theta=0\), so multiplying the first identity by \(B_N^*M_{N,\theta}\) proves the second. This is precisely the literal original theta-relation difference from H26.

Define maps \(E\to\mathcal H_{L,\theta}\) by

\[
 R^c_\theta=W_{N,\theta}C,\qquad
 R^p_\theta=W_{N,\theta}C_\theta,\qquad
 L_\theta=W_{N,\theta}Z_\theta
 =R^c_\theta-R^p_\theta .
 \tag{PC.9}
\]

The superscripts label the common section and phase minimum. The orthogonality from (PC.7) is the exact map identity
\((R^p_\theta)^*L_\theta=0\). Therefore

\[
 \begin{aligned}
 \mathscr D
 &:=\int_0^{2\pi}L_\theta^*L_\theta\,\frac{d\theta}{2\pi}
   =\int_0^{2\pi}X_\theta^*B_N^*M_{N,\theta}B_NX_\theta
       \,\frac{d\theta}{2\pi},\\
 G&=\overline G+\mathscr D,\qquad
 \overline G:=\int_0^{2\pi}G_\theta\,\frac{d\theta}{2\pi}.
 \end{aligned}
 \tag{PC.10}
\]

For clarity, the proof is an expansion:
\((R^c_\theta)^*R^c_\theta
=G_\theta+L_\theta^*L_\theta\).
Integration and (PC.6) give \(C^*M_NC=G\), hence (PC.10). No cancellation of the norm of a relation has been made.

## 3. Exact generator difference, with its literal primitive

Define the common and phase generator boundaries by

\[
 \mathscr B^c_\theta
 =D_{L,\theta}R^c_\theta-R^c_\theta A,\qquad
 \mathscr B^p_\theta
 =D_{L,\theta}R^p_\theta-R^p_\theta A.
 \tag{PC.11}
\]

Both are maps on the original \(E\); \(\mathscr B^p_\theta\) is H54. At polynomial level put

\[
 T_c=\mathsf S_NC-\iota_NCA,\qquad
 T_{p,\theta}=\mathsf S_NC_\theta-\iota_NC_\theta A
 \quad:E\longrightarrow P_{N+1}.
\]

Applying \(J_{N+1}\) gives zero, so unique monic division yields
\(T_c=\chi Q_c\) and \(T_{p,\theta}=\chi Q_{p,\theta}\), where both
\(Q_c,Q_{p,\theta}\) map to \(P_{N+1-q}\). Using (PC.8), their exact difference is

\[
 Q_c-Q_{p,\theta}=SX_\theta-X_\theta A.
 \tag{PC.12}
\]

Here \(SX_\theta:E\to P_{N-q+1}\) raises degree before reduction, whereas \(X_\theta A\) is composition on \(E\). The calculation is
\[
 T_c-T_{p,\theta}
 =S(C-C_\theta)-(C-C_\theta)A
 =\chi(SX_\theta-X_\theta A);
\]
injectivity of multiplication by the nonzero polynomial \(\chi\) proves (PC.12).

After applying the same source and phase maps, the full comparison is

\[
 \boxed{
 \begin{aligned}
 \Delta\mathscr B_\theta
 &:=\mathscr B^c_\theta-\mathscr B^p_\theta\\
 &=W_{N+1,\theta}\bigl(\mathsf S_NZ_\theta-\iota_NZ_\theta A\bigr)\\
 &=\mathcal Z_{L,\theta}\mathcal U_k
   \mathcal V\bigl(\chi(SX_\theta-X_\theta A)\bigr)\\
 &=D_{L,\theta}L_\theta-L_\theta A\\
 &=-\partial_rL_\theta-L_\theta\bigl(A-(k/2)I_E\bigr).
 \end{aligned}}
 \tag{PC.13}
\]

The final line expands the stated generator without changing either \(A\) or its marked arithmetic value.

There is an explicit original tensor primitive for every displayed relation. If \(Y(S)\) is any of \(X_\theta\), \(Q_c\), \(Q_{p,\theta}\), or \(SX_\theta-X_\theta A\), tensor monic division gives polynomial coefficient maps \(Y_i\) with
\[
 \chi(S)Y(S)=\sum_{i=1}^k h(s_i)Y_i(s_1,\ldots,s_k).
\]
This holds because the left side has zero image in the full tensor jet algebra, not because the tensor relation ideal was replaced by \((\chi)\). With the original relation
\(h(D)F_h=\Theta\phi_h\), a degree-\((k-1)\) primitive is
\[
 \sum_{i=1}^k(-1)^{i-1}Y_i(D_1,\ldots,D_k)
 \left(F_h^{\otimes(i-1)}\otimes\phi_h
       \otimes F_h^{\otimes(k-i)}\right).
 \tag{PC.14}
\]
The differential crosses \(i-1\) degree-one factors before acting on \(\phi_h\), supplying a second \((-1)^{i-1}\). The two signs multiply to \(+1\), so its differential is exactly
\(\mathcal V(\chi Y)\). Applying \(\mathcal U_k\) and \(\mathcal Z_{L,\theta}\) gives the maps in (PC.9), (PC.11), and (PC.13).

## 4. Exact energy identities before any inequality

Introduce the matrices on the original coefficient space \(E\)
\[
 \mathscr E
 =\int(\partial_rL_\theta)^*(\partial_rL_\theta)
       \,\frac{d\theta}{2\pi},\qquad
 \mathscr K
 =\int(\partial_rL_\theta)^*L_\theta
       \,\frac{d\theta}{2\pi}.
 \tag{PC.15}
\]
All integrals in this note range over \(0\leq\theta<2\pi\).
Expanding the last line of (PC.13), with both signs retained, gives
\[
 \begin{aligned}
 \mathscr E_\Delta
 &:=\int(\Delta\mathscr B_\theta)^*
             \Delta\mathscr B_\theta\,\frac{d\theta}{2\pi}\\
 &=\mathscr E+
   (A^*-(k/2)I_E)\mathscr D(A-(k/2)I_E)\\
 &\quad+\mathscr K(A-(k/2)I_E)
       +(A^*-(k/2)I_E)\mathscr K^* .
 \end{aligned}
 \tag{PC.16}
\]

It also has the original finite-moment formula
\[
 \mathscr E_\Delta
 =\int
  (\mathsf S_NZ_\theta-\iota_NZ_\theta A)^*
  M_{N+1,\theta}
  (\mathsf S_NZ_\theta-\iota_NZ_\theta A)
  \,\frac{d\theta}{2\pi}.
 \tag{PC.17}
\]

For the full boundaries, the exact comparison includes its cross term:
\[
 \begin{aligned}
 T_c^*M_{N+1}T_c
 &=\int(\mathscr B^c_\theta)^*\mathscr B^c_\theta
             \,\frac{d\theta}{2\pi}\\
 &=\int(\mathscr B^p_\theta)^*\mathscr B^p_\theta
             \,\frac{d\theta}{2\pi}
   +\mathscr E_\Delta\\
 &\quad+\int\left[
       (\mathscr B^p_\theta)^*\Delta\mathscr B_\theta
       +(\Delta\mathscr B_\theta)^*\mathscr B^p_\theta
      \right]\frac{d\theta}{2\pi}.
 \end{aligned}
 \tag{PC.18}
\]
The first equality is (PC.6) at degree \(N+1\), because \(T_c\) is independent of phase. The remaining equality is expansion of
\(\mathscr B^c_\theta=\mathscr B^p_\theta+\Delta\mathscr B_\theta\).
Orthogonality of \(R^p_\theta\) and \(L_\theta\) does not delete the last integral in (PC.18).

There is also an exact comparison for the adjoint generator forms. Set
\(\mathfrak H(M)=A^*M+MA-kM\), for a Hermitian form \(M\) on the same \(E\). Then
\[
 \boxed{
 \mathfrak H(G)-\mathfrak H(\overline G)
 =A^*\mathscr D+\mathscr DA-k\mathscr D.}
 \tag{PC.19}
\]
This follows by substituting (PC.10) into the left side. It concerns the difference of the two forms; it does not assert that either full form is small.

## 5. Actual source derivative moments and a uniform comparison

The source Gram for its derivative is the finite, explicitly specified matrix
\[
 \begin{aligned}
 Q_N
 &:=(\partial_r\Psi_N)^*(\partial_r\Psi_N)\\
 &=\bigl((k/2)\iota_N-\mathsf S_N\bigr)^*
       M_{N+1}
       \bigl((k/2)\iota_N-\mathsf S_N\bigr).
 \end{aligned}
 \tag{PC.20}
\]
In the original coefficient basis \(P_a(S)\), its entries are exactly
\[
 \begin{gathered}
 (Q_N)_{ab}
 =\int_{\mathbb R}u^2
       \overline{P_a(k/2+iu)}P_b(k/2+iu)
       m_{h,k}(u)\,du,\\
 m_{h,k}=w_h^{*k},\quad
 w_h(u)=\frac{|(g/h)(1/2+iu)|^2}{2\pi}.
 \end{gathered}
 \tag{PC.21}
\]
Indeed the derivative has Fourier multiplier \(-iu\), while (H17) and the continuous source norm retain precisely \(m_{h,k}\). Its squared absolute value is \(u^2\), proving every entry in (PC.21). The full vector-valued source remains in (PC.20); (PC.21) evaluates its Gram.

Define the exact finite number
\[
 d_N=\sup_{v\ne0}\frac{v^*Q_Nv}{v^*M_Nv}.
 \tag{PC.22}
\]
It exists because \(M_N\succ0\), \(Q_N\) is finite, and the finite-dimensional unit sphere for \(M_N\) is compact. Thus \(Q_N\preceq d_NM_N\) is a proved statement, not an additional arithmetic hypothesis. H50's original derivative matrix satisfies
\[
 Q_N\preceq H_{1,N}
 =\int_{\mathbb R}(1+r^2)(\partial_r\Psi_N)^*
                 (\partial_r\Psi_N)\,dr .
 \tag{PC.23}
\]
Consequently the original \(h_{1,N}\) of H51 can be used in every occurrence of \(d_N\) below if its bound has been supplied. Formula (PC.22), using (PC.20)–(PC.21), is the sharper exact source moment used here.

Choose \(a>0\) and retain the original two weighted source Grams at degree \(N+1\):
\[
 M_{a,\pm,N+1}
 =(e^{\pm ar}\Psi_{N+1})^*(e^{\pm ar}\Psi_{N+1}).
\]
The weighted column maps take the finite coefficient space \(P_{N+1}\) into the same \(L^2(\mathbb R,dr;\mathcal K)\); their squared weights are the original coordinate factors \(x_k^{\pm2a}\). Define their actual finite cost
\[
 \kappa_{a,N+1}
 =\sup_{v\ne0}
 \frac{v^*(M_{a,+,N+1}+M_{a,-,N+1})v}
      {v^*M_{N+1}v},\qquad
 \eta=\frac{\kappa_{a,N+1}}{e^{aL}-1}<1.
 \tag{PC.24}
\]
The original weighted Schwartz estimates make both weighted Grams finite for the chosen finite source. H41 therefore gives, with no new phase hypothesis,
\[
 (1-\eta)M_{N+1}\preceq M_{N+1,\theta}
                  \preceq(1+\eta)M_{N+1}.
 \tag{PC.25}
\]
Restricting gives the same comparison at degree \(N\). H33, whose hypotheses are now supplied by the actual source, gives
\[
 0\preceq\mathscr D\preceq\eta^2G.
 \tag{PC.26}
\]

For each \(x\in E\), apply (PC.25) to
\(\bigl((k/2)\iota_N-\mathsf S_N\bigr)Z_\theta x\), then (PC.22), then the lower degree-\(N\) bound:
\[
 \begin{aligned}
 \|\partial_rL_\theta x\|^2
 &\leq(1+\eta)x^*Z_\theta^*Q_NZ_\theta x\\
 &\leq(1+\eta)d_Nx^*Z_\theta^*M_NZ_\theta x\\
 &\leq\frac{1+\eta}{1-\eta}d_N
          x^*Z_\theta^*M_{N,\theta}Z_\theta x\\
 &=\frac{1+\eta}{1-\eta}d_N\|L_\theta x\|^2.
 \end{aligned}
 \tag{PC.27}
\]
Periodization commutes with the \(r\)-derivative on these source columns, so the first line uses the actual derivative in (PC.15). Integrating (PC.27) and using (PC.26) proves
\[
 0\preceq\mathscr E
 \preceq\frac{1+\eta}{1-\eta}d_N\mathscr D
 \preceq\frac{1+\eta}{1-\eta}d_N\eta^2G.
 \tag{PC.28}
\]

## 6. Generator-difference bounds in the original quotient metric

For a family \(Y_\theta:E\to\mathcal H_{L,\theta}\), define the Hilbert–Schmidt norm using the retained \(G\) by
\[
 \|Y\|_{2,G}^2
 :=\int\operatorname{Tr}(G^{-1}Y_\theta^*Y_\theta)
                  \,\frac{d\theta}{2\pi}.
 \tag{PC.29}
\]
Equivalently this is the sum of \(\|Y_\theta e_j\|^2\) over any \(G\)-orthonormal basis \((e_j)\), integrated in the original phase measure. This definition does not rescale either the source mass or the arithmetic metric.

Keep the exactly computed coefficient quantities
\[
 a_{\mathrm{HS}}^2
 =\operatorname{Tr}\!\left(
       G^{-1}(A^*-(k/2)I_E)G(A-(k/2)I_E)\right),\qquad
 a_{\mathrm{op}}=\|A-(k/2)I_E\|_G.
 \tag{PC.30}
\]
They are computed from the actual multiplication matrix and original minimum metric. In particular no diagonalizability or removal of nilpotent parts is used.

Equations (PC.26), (PC.28), and (PC.13) imply
\[
 \boxed{
 \begin{aligned}
 \|L\|_{2,G}&\leq\eta\sqrt q,\\
 \|\Delta\mathscr B\|_{2,G}
 &\leq\eta\left(
     \sqrt{\frac{1+\eta}{1-\eta}\,d_Nq}
     +a_{\mathrm{HS}}\right).
 \end{aligned}}
 \tag{PC.31}
\]
To prove the second statement, the triangle inequality in the Hilbert space of phase families gives
\[
 \|\Delta\mathscr B\|_{2,G}
 \leq\|\partial_rL\|_{2,G}
      +\|L(A-(k/2)I_E)\|_{2,G}.
 \]
The first squared norm is
\(\operatorname{Tr}(G^{-1}\mathscr E)
\leq\eta^2(1+\eta)(1-\eta)^{-1}d_Nq\).
The second squared norm is
\[
 \operatorname{Tr}\!\left(
 G^{-1}(A^*-(k/2)I_E)\mathscr D(A-(k/2)I_E)\right)
 \leq\eta^2a_{\mathrm{HS}}^2,
 \]
which proves (PC.31). The first statement is
\(\operatorname{Tr}(G^{-1}\mathscr D)\leq\eta^2q\).

For every real \(t>0\), a matrix form of the same estimate is
\[
 \mathscr E_\Delta
 \preceq\eta^2\left[
   (1+t)\frac{1+\eta}{1-\eta}d_NG
   +(1+t^{-1})(A^*-(k/2)I_E)G(A-(k/2)I_E)
 \right].
 \tag{PC.32}
\]
For each vector \(x\), use
\(2\operatorname{Re}\langle u,v\rangle
\leq t\|u\|^2+t^{-1}\|v\|^2\)
in the squared norm of (PC.13), integrate, and then apply (PC.26) and (PC.28). This proves all quadratic forms in (PC.32).

The adjoint-form comparison (PC.19) has a quadratic error:
\[
 \left\|
 G^{-1/2}\bigl(\mathfrak H(G)-\mathfrak H(\overline G)\bigr)
 G^{-1/2}
 \right\|_{\mathrm{op}}
 \leq2\eta^2a_{\mathrm{op}}.
 \tag{PC.33}
\]
Indeed let \(\mathsf D=G^{-1}\mathscr D\); it is positive self-adjoint for \(G\), and \(\|\mathsf D\|_G\leq\eta^2\). Multiplication of (PC.19) by \(G^{-1}\) gives
\[
 (A-(k/2)I_E)^{\dagger_G}\mathsf D
 +\mathsf D(A-(k/2)I_E),
 \]
where \({}^{\dagger_G}\) is the metric adjoint. Submultiplicativity proves (PC.33). The statement is in the original \(G\)-metric; it is not an unqualified Euclidean bound on the coefficient matrix in (PC.19).

## 7. An explicit length choice makes both comparison errors small

Keep a fixed original packet \(h\) and let \(k\) vary, with any finite cutoff \(N_k\geq q_k-1\). In the following formulas all matrices are the actual source matrices for that \(k,N_k\). Set
\[
 \eta_k=
 \frac{1}
 {(k+1)\bigl(1+\sqrt{q_k}
       +\sqrt{3d_{N_k}q_k}+a_{\mathrm{HS},k}\bigr)},
 \qquad
 L_k=\frac1a\log\left(1+\frac{\kappa_{a,N_k+1}}{\eta_k}\right).
 \tag{PC.34}
\]
Every input in these formulas is finite, and the weighted Gram cost is strictly positive. Thus both parameters are finite and positive. Substitution gives
\[
 \frac{\kappa_{a,N_k+1}}{e^{aL_k}-1}=\eta_k.
 \]
Also \(0<\eta_k<1/2\), so
\((1+\eta_k)/(1-\eta_k)\leq3\).
Thus (PC.31) proves the explicit simultaneous estimates
\[
 \boxed{
 \|L\|_{2,G}\leq\frac1{k+1},\qquad
 \|\mathscr B^c-\mathscr B^p\|_{2,G}
          \leq\frac1{k+1}.}
 \tag{PC.35}
\]

For example, the first bound follows by inserting the numerator
\(\sqrt{q_k}\) into the positive denominator in (PC.34); the second follows by inserting
\(\sqrt{3d_{N_k}q_k}+a_{\mathrm{HS},k}\).
Both errors are therefore \(o(k)\), indeed they tend to zero.

No uniform estimate on the growth of \(\kappa_{a,N_k+1}\), \(d_{N_k}\), or \(a_{\mathrm{HS},k}\) was claimed. The length in (PC.34) explicitly pays their full cost. This is an existence and exact-formula comparison at each finite \(k,N_k\), not a certified numerical evaluation of an unevaluated arithmetic Gram.

## 8. The complete quartet boundary cannot satisfy the same estimate

Now remain inside the counterfactual branch of the original program: a root
\(\rho=1/2+\delta+i\gamma\), \(0<\delta<1/2\), \(\gamma>0\), of its full order \(m\), together with its reflected and conjugate roots, is selected. Retain HT1–HT2 exactly:
\[
 \ell_k=1+k(m-1),\qquad q_k=\ell_k(k+1)^2,\qquad
 \mathcal L_{h,k}
 =2\delta\ell_k(k+1)
        \left\lfloor\frac{(k+1)^2}{4}\right\rfloor.
 \tag{PC.36}
\]
The full original cyclic polynomial is
\[
 \chi_{h,k}(S)
 =\prod_{a_0,b_0=0}^k
 \bigl(S-k/2-(2a_0-k)\delta-i(2b_0-k)\gamma\bigr)^{\ell_k}.
 \]
No order in this polynomial is reduced.

The independently proved HT14–HT15 give, for every phase, every length, and every \(N_k\geq q_k-1\),
\[
 \operatorname{Tr}\bigl(
     G_\theta^{-1}(\mathscr B^p_\theta)^*\mathscr B^p_\theta\bigr)
 \geq\frac{\mathcal L_{h,k}^2}{2}
 \geq\frac{\delta^2 k^2q_k^2}{8}.
 \tag{PC.37}
\]
Those arithmetic lower bounds are used here, not reproved.

To place (PC.37) in precisely the same metric as (PC.35), first note that the source bound (PC.25) gives
\[
 (1-\eta_k)G\preceq G_\theta\preceq(1+\eta_k)G.
 \tag{PC.38}
\]
Indeed the minimum over \(J_NP=x\) of each quadratic source form is its quotient form \(x^*G_\theta x\), respectively \(x^*Gx\); minimizing the two inequalities proves both statements. The lower inequality implies
\(G^{-1}\succeq(1-\eta_k)G_\theta^{-1}\).
Taking its trace against the positive matrix
\((\mathscr B^p_\theta)^*\mathscr B^p_\theta\), and then integrating (PC.37), gives
\[
 \|\mathscr B^p\|_{2,G}
 \geq\sqrt{1-\eta_k}\,
       \frac{\mathcal L_{h,k}}{\sqrt2}
 \geq\frac{\sqrt{1-\eta_k}\,\delta kq_k}{2\sqrt2}.
 \tag{PC.39}
\]

The same lower bound reaches the common section with its exact comparison cost. The reverse triangle inequality applied to (PC.13) and (PC.35) gives
\[
 \boxed{
 \begin{aligned}
 \|\mathscr B^c\|_{2,G}
 &=\left(\operatorname{Tr}
      (G^{-1}T_c^*M_{N_k+1}T_c)\right)^{1/2}\\
 &\geq\sqrt{1-\eta_k}\,
       \frac{\mathcal L_{h,k}}{\sqrt2}-\frac1{k+1}.
 \end{aligned}}
 \tag{PC.40}
\]
The equality is the exact all-phase isometry (PC.18), so the common boundary in this formula is the original source boundary.

In particular (PC.34) gives \(\eta_k\to0\), and \(q_k\geq1\), whence
\[
 \liminf_{k\to\infty}
 \frac{\|\mathscr B^c\|_{2,G}}{kq_k}
 \geq\frac{\delta}{2\sqrt2},\qquad
 \liminf_{k\to\infty}
 \frac{\|\mathscr B^p\|_{2,G}}{kq_k}
 \geq\frac{\delta}{2\sqrt2}.
 \tag{PC.41}
\]
Thus neither full generator boundary has \(o(k)\) norm, even after reporting its norm per quotient dimension. The actual phasewise metric version (PC.37) is uniform in \(L\) without any length restriction.

Equations (PC.35), (PC.39), and (PC.40) coexist because (PC.35) makes the two large boundaries close. It does not set either boundary equal to zero. The morphism that relates these statements is the exact original relation map (PC.12)–(PC.14).

## 9. At the minimal cutoff the gluing error is identically zero

There is a useful exact case requiring no length choice or limiting statement. Set \(N=q-1\). Then
\[
 J_{q-1}:P_{q-1}\longrightarrow E
 \]
is an isomorphism: monic division gives a unique remainder of degree at most \(q-1\) for every class, and a nonzero multiple of a degree-\(q\) monic polynomial cannot have degree at most \(q-1\).

Every section in (PC.7) must consequently equal the unique inverse, so
\[
 C=C_\theta=J_{q-1}^{-1},\qquad
 Z_\theta=X_\theta=L_\theta=0,\qquad
 \mathscr D=\mathscr E_\Delta=0
 \tag{PC.42}
\]
for every \(\theta\) and \(L>0\).

Define the original H57 residue coefficient
\[
 \ell:E\longrightarrow\mathbb C,\qquad
 \ell([P])=[S^{q-1}]\operatorname{rem}_\chi P.
 \tag{PC.43}
\]
This is nonzero since \(\ell([S^{q-1}])=1\).
For a remainder \(P\) of degree at most \(q-1\), the polynomial \(SP\) has degree at most \(q\). Its monic division by \(\chi\) has constant quotient exactly \([S^{q-1}]P\). Its remainder is \(C A[P]\). Therefore the complete coefficient identity is
\[
 \mathsf S_{q-1}C-\iota_{q-1}CA=\chi\,\ell.
 \tag{PC.44}
\]

It follows that the persistent boundary is the explicit rank-one map
\[
 \boxed{
 \mathscr B^c_\theta=\mathscr B^p_\theta
 =f_{\chi,\theta}\otimes\ell,\qquad
 f_{\chi,\theta}
 :=\mathcal Z_{L,\theta}\mathcal U_k\mathcal V\chi.}
 \tag{PC.45}
\]
It factors through exactly the same scalar functional as the original residue constituent
\(\mathcal R=1_E\otimes\ell\) in H57. In (PC.45) the receiving vector is the actual source relation \(f_{\chi,\theta}\), and its tensor theta primitive is (PC.14) with \(Y=1\).

This vector is nonzero. Its exact phase norm is
\[
 \|f_{\chi,\theta}\|^2
 =\frac{2\pi}{L}\sum_{n\in\mathbb Z}
   m_{h,k}\!\left(\frac{2\pi n+\theta}{L}\right)
   \left|\chi\!\left(k/2+i\frac{2\pi n+\theta}{L}\right)\right|^2>0.
 \tag{PC.46}
\]
All weights are positive for \(k\geq2\), as proved for the actual source in HT6. The nonzero polynomial \(\chi\) has only finitely many distinct roots; it cannot vanish on every point of the infinite distinct sampled lattice. At least one summand is therefore positive and all are nonnegative. Convergence follows from the original source bounds.

Thus (PC.45) has rank exactly one and the full generator energy is exactly
\[
 \operatorname{Tr}\bigl(
    G_\theta^{-1}(\mathscr B^p_\theta)^*\mathscr B^p_\theta\bigr)
 =\|f_{\chi,\theta}\|^2\,\ell G_\theta^{-1}\ell^*>0.
 \tag{PC.47}
\]
To verify this equation, the Gram of \(f_{\chi,\theta}\otimes\ell\) is
\(\|f_{\chi,\theta}\|^2\ell^*\ell\); cyclicity of the finite matrix trace gives (PC.47). Positive definiteness of \(G_\theta^{-1}\) and \(\ell\ne0\) prove strict positivity. Under the selected quartet, HT14 supplies the quantitative lower bound (PC.37) to this exact expression.

Hence even perfect gluing, \(\mathscr D=0\), is already compatible with the full positive generator defect in the original finite quotient at its first cutoff. This is an exact calculation on the counterfactual packet, not an asserted RH counterexample.

### Exact first-cutoff energy, including the monic residual

In this paragraph fix one phase and \(N=q-1\), and write
\(R=R^p_\theta=R^c_\theta\), \(G_0=G_\theta\),
\(f=f_{\chi,\theta}\). Thus \(G_0\) denotes this phase metric, not the common metric \(G\) in (PC.7). Put
\[
 U=RG_0^{-1/2},\qquad
 r^*=\ell G_0^{-1/2},\qquad
 T=\mathscr B^p_\theta G_0^{-1/2}=fr^*,\qquad
 z=U^*f,\qquad \alpha=r^*z.
 \tag{PC.48}
\]
Here \(U^*U=I_E\). The exact integration-by-parts identity H55 gives
\[
 H_0=G_0^{-1/2}(A^*G_0+G_0A-kG_0)G_0^{-1/2}
 =-(zr^*+rz^*).
 \tag{PC.49}
\]
For the complete quartet, \(\operatorname{Tr}H_0=0\); therefore
\(\operatorname{Re}\alpha=0\). HT9 identifies its two nonzero eigenvalues as \(\varepsilon_\theta,-\varepsilon_\theta\), with \(\varepsilon_\theta\geq\mathcal L_{h,k}\).

Multiplying out the square in (PC.49) and taking its trace gives
\[
 2\varepsilon_\theta^2
 =2\|z\|^2\|r\|^2+2\operatorname{Re}(\alpha^2)
 =2\|z\|^2\|r\|^2-2(\operatorname{Im}\alpha)^2.
 \]
The decomposition \(f=Uz+(I-UU^*)f\) is orthogonal. Since \(T=fr^*\) is rank one, both its squared operator norm and squared Hilbert–Schmidt norm equal \(\|f\|^2\|r\|^2\). Consequently
\[
 \boxed{
 \|T\|_{\mathrm{op}}^2=\|T\|_{\mathrm{HS}}^2
 =\varepsilon_\theta^2+(\operatorname{Im}\alpha)^2
     +\|r\|^2\|(I-UU^*)f\|^2.}
 \tag{PC.50}
\]
In particular the projection term is present.

Let \(p_j\) be the actual monic orthogonal polynomials for the same original phase measure
\[
 d\nu_{L,\theta}(u)
 =\frac{2\pi}{L}\sum_{n\in\mathbb Z}
       m_{h,k}(u_n)\delta_{u_n},\qquad
 u_n=(2\pi n+\theta)/L,\qquad S=k/2+iu,
 \]
and let \(\omega_j=\int|p_j(k/2+iu)|^2\,d\nu_{L,\theta}(u)>0\).
The range of \(U\) is precisely \(W_{q-1,\theta}P_{q-1}\), since \(C=J_{q-1}^{-1}\) is an isomorphism. Both \(\chi\) and \(p_q\) are monic of degree \(q\), so \(\chi-p_q\in P_{q-1}\), while \(W_{q,\theta}p_q\) is orthogonal to that range. It follows that
\[
 (I-UU^*)f=W_{q,\theta}p_q,\qquad
 \|(I-UU^*)f\|^2=\omega_q.
 \tag{PC.51}
\]
On the orthogonal basis \(p_0,\ldots,p_{q-1}\) of \(P_{q-1}\), the functional \(\ell\) is zero on \(p_j\) for \(j<q-1\) and equals one on \(p_{q-1}\). Its squared dual norm is therefore exactly \(1/\omega_{q-1}\). The identification with the phase quotient is the isometry \(C:(E,G_0)\to(P_{q-1},M_{q-1,\theta})\). Thus
\[
 \|r\|^2=\ell G_0^{-1}\ell^*=\frac1{\omega_{q-1}},\qquad
 \boxed{\|T\|_{\mathrm{op}}^2=\|T\|_{\mathrm{HS}}^2
 =\varepsilon_\theta^2+(\operatorname{Im}\alpha)^2
     +\frac{\omega_q}{\omega_{q-1}}
 >\varepsilon_\theta^2\geq\mathcal L_{h,k}^2.}
 \tag{PC.52}
\]
This is a strictly stronger first-cutoff floor, using the original monic source moments and preserving their mass.

### A full-jet eigenvector and its exact arithmetic boundary ratio

Let \(\lambda\) be any root of \(\chi\) of its complete order \(d_\lambda\), and write
\[
 \psi_\lambda(S)=\frac{\chi(S)}{(S-\lambda)^{d_\lambda}},
 \qquad \psi_\lambda(\lambda)\ne0,\qquad
 v_\lambda=
 \left[\frac{\chi(S)}
 {(S-\lambda)\psi_\lambda(\lambda)}\right]\in E.
 \tag{PC.53}
\]
The displayed representative has degree \(q-1\).
It satisfies \((A-\lambda I_E)v_\lambda=0\), since multiplication by \(S-\lambda\) produces the multiple \(\chi/\psi_\lambda(\lambda)\).
At the full local factor
\(\mathbb C[\epsilon]/(\epsilon^{d_\lambda})\), its value is
\[
 \epsilon^{d_\lambda-1}
 \frac{\psi_\lambda(\lambda+\epsilon)}{\psi_\lambda(\lambda)}
 =\epsilon^{d_\lambda-1}.
 \]
At every other full primary factor its value is zero. Thus this is a specified nonzero vector in the full original jet algebra, with every local order retained. Its leading coefficient is
\[
 \ell(v_\lambda)=\frac1{\psi_\lambda(\lambda)}.
 \tag{PC.54}
\]

The exact two squared norms before any cancellation of a coefficient are
\[
 \begin{aligned}
 \|\mathscr B^p_\theta v_\lambda\|^2
 &=\frac1{|\psi_\lambda(\lambda)|^2}
       \int|\chi(k/2+iu)|^2\,d\nu_{L,\theta}(u),\\
 \|R v_\lambda\|^2
 &=\frac1{|\psi_\lambda(\lambda)|^2}
       \int\left|
       \frac{\chi(k/2+iu)}{k/2+iu-\lambda}
       \right|^2\,d\nu_{L,\theta}(u).
 \end{aligned}
 \tag{PC.55}
\]
The quotient inside the second integral is the polynomial
\(\chi(S)/(S-\lambda)\), including at any sampled root. In particular no singular point is omitted. The denominator is strictly positive by the infinite positive lattice argument used in (PC.46).

For the extreme complete primary factor
\(\lambda=k/2+k\delta+ik\gamma\), with \(d_\lambda=\ell_k\), division of the two equations in (PC.55) gives the exact identity
\[
 \boxed{
 \frac{\|\mathscr B^p_\theta v_\lambda\|^2}
      {\|R v_\lambda\|^2}
 =k^2\delta^2+
 \frac{\displaystyle\int (u-k\gamma)^2
       \left|\frac{\chi(k/2+iu)}{k/2+iu-\lambda}\right|^2
           \,d\nu_{L,\theta}(u)}
      {\displaystyle\int
       \left|\frac{\chi(k/2+iu)}{k/2+iu-\lambda}\right|^2
           \,d\nu_{L,\theta}(u)}
 >k^2\delta^2.}
 \tag{PC.56}
\]
Indeed on the original sampled line,
\(|k/2+iu-\lambda|^2=k^2\delta^2+(u-k\gamma)^2\).
Multiplying this equality by
\(|\chi(k/2+iu)/(k/2+iu-\lambda)|^2\), integrating, and using (PC.55) proves the formula. The last numerator is positive: at most one lattice point has \(u=k\gamma\), and the nonzero polynomial in the integrand cannot vanish at all remaining infinitely many points. Both the nonzero factor \(\psi_\lambda(\lambda)\) and the full arithmetic unit in (PC.3) were retained in the actual vector and observation maps before the equality of ratios was calculated.

## 10. Split-base typing, provenance, and independent check

Each displayed linear coefficient map acts on a fixed original support label by
\[
 (\lambda,v)\longmapsto(\lambda,fv),\qquad
 \tau\longmapsto\tau .
 \]
If \(fv=0\), the target is the represented zero at that label. For instance the full-jet observation of \(\mathcal V(\chi Y)\) is zero by (PC.3), although its source representative and norm remain in (PC.14), (PC.18), and (PC.47). This is the original map to the receiving coefficient zero; it does not send represented data to external absence. Arithmetic scalars remain under
\(G(\mathbb Z)\to G(\mathbb C)\), the marked \(a=0\) coefficient remains fixed, and neither the phase \(\theta\) nor the length \(L\) translates \(A\), \(g\), or \(\chi\).

The entire original H note was read. Its path is
workspace:/output/split_zero_rh_tandem_2026-09-12/sources/web_holonomy_descent_delivery/Tau_Holonomy_Descent_Control/NOTE.md
and its SHA-256 is
900E7C16369A58093B16A03DBC449D41A100EE45DBE8515E30BC026E660BA393.
The reused quartet floor was read in HT1–HT15 at
workspace:/output/tau_split_zero_counterfactual_reconstruction_20260913/tex/modules/HT.tex,
whose SHA-256 is
00D276CD5FF7FF111D56D8A7F19039D65AD7DCCCE987C0E524F2B26E46C0CAF8.

An independent child audit checked (PC.27)–(PC.35), including the derivative's degree, the sign in (PC.13), the metric direction in the derivative estimate, every coefficient of the Hilbert–Schmidt bound, and the length substitution. It found no algebraic error and required the explicit metric qualification now included in (PC.33). No original source, global TeX, or published artifact was edited.
