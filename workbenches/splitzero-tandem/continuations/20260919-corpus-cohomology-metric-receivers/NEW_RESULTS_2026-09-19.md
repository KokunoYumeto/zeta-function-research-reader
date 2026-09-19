# Mathematical results added on 19 September 2026

The original analytic object is the theta complex
\(V\xrightarrow{\Theta}\mathscr B\), with
\(\Theta\phi(x)=2\sum_{n\ge1}\phi(nx)\), physical measure \(dx\), and
\(D=-x\partial_x\). Here \(V\) consists of even Schwartz functions with zero
value and integral, and \(\mathscr B\) consists of functions rapidly decreasing
at both endpoints with every \(D\)-derivative. Its cohomology is
\(Q=\mathscr B/\Theta V\). The canonical source has Mellin transform \(2\xi\).
These definitions are kept throughout the [complete proof](CORPUS_RECEIVERS_AND_METRIC_CONTROL.pdf)
and [LaTeX](CORPUS_RECEIVERS_AND_METRIC_CONTROL.tex).

The following results are proved in this edition. They connect earlier
Split-Zero constructions to this entire complex and to the original finite
arithmetic metrics. The source register identifies the earlier manuscripts;
the manuscript-reading programme remains ongoing.

1. **SZ-20260919-018 — the theta quotient is actual cohomology on the split support space.**
   On \(X=\operatorname{Spec}G(\mathbb C)=\{\eta,z\}\), the sheaf whose
   restriction is the original \(\Theta:V\to\mathscr B\) satisfies
   \(R\Gamma_{\{z\}}(X,\mathcal F_\Theta)\simeq[V\to\mathscr B]\),
   hence \(H^1_{\{z\}}=Q\). Every finite full-jet map and canonical section
   is an actual sheaf map. The mixed addition on \(V\sqcup\mathscr B\) is
   \(v\oplus b=\Theta v+b\); its Bourne quotient by \(V\) is
   \(Q\sqcup\{\tau\}\). Unsupported and supported-zero fibres are respectively
   \(V\) and \(\Theta V\) in the separate components. This realizes the
   analytic complex over the earlier split support, with the coefficient
   category and all quotient maps specified. **Proof: S1–S5.**

2. **019 — the original endpoints and the global jet tail both have exact receivers.**
   Adding the two endpoint states gives
   \(\mathscr B/\Theta V\cong\mathscr B_{01}/\Theta\mathcal S_{\rm ev}\),
   with boundary map \((\phi(0),\int\phi)\mapsto(-\phi(0),\int\phi)\)
   and endpoint action \(\operatorname{diag}(0,1)\). Compatible canonical
   sections embed \(E_{\rm fin}=\bigoplus_\rho E_\rho\) into \(Q\), and
   \[0\longrightarrow K\longrightarrow Q/\sigma E_{\rm fin}
       \longrightarrow T_{\rm arith}\longrightarrow0,\qquad
       0\ne T_{\rm arith}\subset\prod_\rho E_\rho/\bigoplus_\rho E_\rho.\]
   Here \(K\) is the kernel of all full Mellin jets. This retains the global
   component beyond any finite packet. **Proof: E1–E5 and T1–T3.**

3. **020 — the earlier Beurling approximation route has a full-multiplicity observation bound.**
   In its original space \(L^2((1,\infty),y^{-2}dy)\), the jets at any actual
   finite set of zeros with \(\Re\rho>1/2\) have Gram matrix and target
   \[G_{(\rho,j),(\sigma,k)}=
   \frac{(-1)^{j+k}(j+k)!}{j!k!(\rho+\bar\sigma-1)^{j+k+1}},\qquad
   b_{\rho,j}=\frac{(-1)^j}{\rho^{j+1}}.\]
   Every squared approximation error is at least \(b^*G^{-1}b>0\).
   The actual map into theta cohomology is \(R_ZJ_Z\); the least-common-multiple
   denominator stages receive the Nyman–Beurling/Báez-Duarte criterion.
   An upper estimate for those distances remains an analytic calculation.
   **Proof: B1–B5.**

4. **021 — the finite-prime boundary calculation now has a genuine lift.**
   The proof constructs the quotient projection, its self-adjoint lift and
   the actual crossed-product representation. Its exponential determinant is
   \(e^{2\pi i/(1+e^t)}\) in the original logarithmic coordinate, so its
   boundary index is \(-1\). The explicit semilocal coordinate maps give
   \(\delta_0=-(1,\ldots,1,1,1)\),
   \(K_0(A_S)\cong\mathbb Z^{n+1}\) and \(K_1(A_S)\cong\mathbb Z^n\)
   for the specified finite-unit-quotiented space. Both archimedean sign
   projections are retained. **Proof: K1–K10.**

5. **022 — earlier phase germs determine every coefficient of the original source unit.**
   The local logarithmic expansion of \(\xi\) gives an explicit finite
   recurrence for all coefficients of \(j_h(h/(2\xi))\), including every
   root-difference factor and phase. With full confluent evaluation \(V_Z\)
   and local multiplication matrix \(T\), the canonical numerator's map is
   \(u\mapsto V_Z^{-1}Tu\) on divided jets. Multiplication on original power
   coefficients is \(a\mapsto V_Z^{-1}TV_Za\). Their connecting map is
   exactly \(u=V_Za\). **Proof: U0–U3.**

6. **023 — denominator inversion reconstructs the source and its endpoint singularities.**
   \[\mathcal I_\mu F(x)=\tfrac12\sum_{n\ge1}\mu(n)F(nx),\qquad
     Q\cong\mathcal I_\mu(\mathscr B)/V.\]
   For the actual canonical section \(R_Zu\), its inverse source has the
   complete expansion \(\sum_\rho x^{-\rho}P_\rho(-\log x)+O(x^2)\).
   The exact threshold is
   \[\mathcal I_\mu R_Zu\in L^2(dx)
       \iff u_\rho=0\text{ for every }\Re\rho\ge\tfrac12,\]
   where each \(u_\rho\) means its whole primary jet. This calculates the
   zero-end source obstruction while keeping the original cohomology.
   **Proof: MI1–MI9.**

7. **024 — the Hurwitz branch receives all original finite jets after bilateral completion.**
   A positive compact Hurwitz shift has the additional residue
   \(\operatorname{Res}_{w=-2}\Lambda_{\mu,t}
      =(2\pi/3)\int ty(ty+1/2)(ty+1)\,d\mu\).
   The full pole train is calculated. The bilateral family
   \[F_a=D(D-1)\left(2\sum_{n\in\mathbb Z}e^{-\pi(n+a)^2x^2}\right)\]
   lies in the original \(\mathscr B\). Its full-jet vectors span every
   actual finite primary packet even when \(a\) is confined to
   \([\epsilon,1-\epsilon]\). Their positive integral Gram gives an explicit
   right inverse of the original jet map. The residual difference from the
   canonical section remains in the stated all-jet kernel. **Proof: HU1–HU10.**

8. **025 — the actual metric determines the necessary heat depth.**
   Original reflection is \(IF(x)=x^{-1}F(1/x)\), with
   \(DI=I(1-D)\), including every primary derivative sign.
   The original theta derivative family is dense in \(L^2(dx)\).
   At fixed full divisor, its attained finite metric therefore decreases
   to zero. If \(A=R_h^*R_h\),
   \[c_N^2=\lambda_{\max}(H_N^{-1/2}AH_N^{-1/2})\longrightarrow\infty.\]
   The full heat comparison has relative largest eigenvalue at least
   \((2^{-(J+1)/2}c_N-1)_+^2\). A fixed upper comparison constant \(B\)
   thus requires
   \(J+1\ge2\log_2c_N-2\log_2(1+\sqrt B)\).
   This evaluates the required dependence on the actual finite metric;
   it assigns no unproved growth rate in \(N\) or a growing packet.
   **Proof: RC1–RC10 and HD1–HD5.**

9. **026 — metric approximation now controls the original complex responses and all three currents.**
   Keep the original observation map \(\Lambda\), boundary columns
   \(a_i\), retained class \(v\), and arithmetic coefficient \(\mathfrak c\).
   Define
   \[L=G-\Lambda^*(\Lambda G^{-1}\Lambda^*)^{-1}\Lambda,
      \quad U=\frac{a_1^*Lv}{a_1^*Gv},\quad
      V=\frac{a_2^*Lv}{a_2^*Gv}.\]
   With source energies \(p_i=|a_i^*Gv|^2/[(a_i^*Ga_i)(v^*Gv)]\),
   the proved heat comparison gives
   \[|U'-U|\le\frac{\eta(2+|U|)}{\sqrt{p_1}-\eta},\qquad
     |V'-V|\le\frac{\eta(2+|V|)}{\sqrt{p_2}-\eta},\quad
     \eta=(1+2^{-(J+1)/2}c_N)^{2k}-1<\min_i\sqrt{p_i}.\]
   HR9–HR11 carry these errors through
   \(\bar UV,(1-\bar U)(1-V),1-\bar UV-(1-\bar U)(1-V)\), including
   the quadratic errors and exact sum cancellation. These estimates
   specify the accuracy needed to use a heat computation for a sign;
   they retain the small denominators and do not assign unevaluated signs.

The complete proofs cite Deligne, Beurling, Báez-Duarte, Connes and Consani,
Green, Apostol, Askey and Roy, Stein and Shakarchi, Boyd and Vandenberghe,
and the Stacks Project at the relevant uses. The earlier phase manuscript's
attribution to Jacolm Tobley is retained. There are 156 passing finite complex
matrix diagnostics for HD and HR; these are examples checking the formulas,
not numerical data for hypothetical zeta zeros.
