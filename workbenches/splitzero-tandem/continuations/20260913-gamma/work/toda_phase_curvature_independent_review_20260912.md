# Independent review of the Toda curvature, phase and scalar control identities

Source date: 12 September 2026. Review completed: 13 September 2026.

Source read in full: `sources/web_toda_volume_delivery/Tau_Toda_Volume_Control/NOTE.tex`, SHA256 `027cd27a5fc104c5ebdf0102ee43aafd7b6218da4929ceb1b8913e3448cd2375`. The review is of the delivered source equations (20)–(29), including the definitions and proofs on which they depend. No source, cumulative PDF or frozen release was changed. No Lean execution or numerical calculation was used for the conclusions below.

The source formulas (21), (22), (23), (24), (26), (27), (28) and (29) are correct under the stated nonempty-packet, reflection and real-tilt hypotheses. Two presentation details need explicit repair in the cumulative proof:

1. The trace of the outgoing Gram in (22) is generally **not** the positive source Toda coefficient by itself. The incoming trace is generally **not** the boundary Toda coefficient by itself. Each contains the same term, which cancels in their difference. The exact formulas and their proof appear below.
2. In the prose immediately after (27), the expression `d_N=nu_0-omega_q` uses a previously defined quotient vector as a scalar norm. The correctly typed equality is
   \[
   d_q^*G_{q-1}d_q=\nu_0-\omega_q.
   \]
   This notation defect does not change formula (27).

The description of the first squared loss in (28) as an “imbalance” is best accompanied by its exact equality condition. That loss does not generally vanish when the two contractions are equal. The equality condition is derived below.

## 1. Fixed objects, coordinate map and adjoint conventions

Fix the original nonempty reflection-stable packet, its complete orders, the tensor degree \(k\geq1\), and the monic cyclic annihilator \(\chi(S)\) of degree \(q\geq1\). Put \(c=k/2\). The source measure is
\[
d\mu_\theta(u)=e^{\theta u}m_k(u)\,du,
\qquad m_k=w_h^{*k},
\qquad |\theta|<\pi/2,
\]
with real \(\theta\). Its mass is the original \(M_h(\theta)^k\). Every polynomial moment is finite, the measure is positive on a set of full Lebesgue measure, and every nonzero polynomial has positive squared norm. Differentiation of every finite source Gram is justified by the locally dominated differentiated integrals established in source §3. No division by the mass occurs.

For an explicit real-coordinate calculation define
\[
\widetilde\chi(u)=i^{-q}\chi(c+iu).
\]
Reflection makes this a real monic polynomial. The exact algebra isomorphism is
\[
L:C_S=\mathbb C[S]/(\chi)
 \longrightarrow C_u=\mathbb C[u]/(\widetilde\chi),
\qquad L[P(S)]=[P(c+iu)].
\]
It is well-defined because \(\chi(c+iu)=i^q\widetilde\chi(u)\), with the scalar unit \(i^q\) retained. Its inverse is induced by \(u\mapsto(S-c)/i\). In the respective monomial bases of degree below \(q\), \(L\) is triangular with diagonal \(1,i,\ldots,i^{q-1}\), so
\[
\det L=i^{q(q-1)/2},\qquad |\det L|^2=1.
\]
This proves the equality of determinant volumes in the two presentations; it does not change either source polynomial or its original arithmetic unit.

Work first in \(C_u\). Let \(\mathcal P_N\) denote the space of polynomials in \(u\) of degree at most \(N\), evaluated in \(H_\theta=L^2(d\mu_\theta)\). For \(N\geq q-1\), let
\[
J_N:\mathcal P_N\twoheadrightarrow C_u,
\qquad
\mathcal D_N=\ker J_N
 =\widetilde\chi\mathcal P_{N-q}.
\]
The degree \(-1\) polynomial space is zero. Let
\[
R=R_N(\theta):C_u\longrightarrow\mathcal P_N
\]
be the unique quotient lift with image orthogonal to \(\mathcal D_N\). Thus \(J_NR=1\). Write \(G=R^*R\), where \(R^*\) is the adjoint from \(H_\theta\) to the **fixed Euclidean coefficient coordinates** of \(C_u\). In particular, matrix stars in \(G\), \(O^*O\) and \(I^*I\) use that fixed coefficient pairing. The Hilbert adjoint when the quotient carries the metric \(G\) is \(G^{-1}R^*\), and likewise for \(O\) and \(I\). This explains the factors \(G^{-1}\) in their Hilbert–Schmidt traces.

In source (15), more explicitly, let \(M_N\) be the Gram matrix in the fixed monomial source coordinates and let \(J_N\) also denote the corresponding rectangular quotient matrix. Its symbol \(J_N^*\) is the Euclidean conjugate transpose. The Hilbert adjoint from the Euclidean target into the source carrying \(M_N\) is exactly \(M_N^{-1}J_N^*\), because
\[
\langle J_Nz,x\rangle_{\mathrm{Euc}}
 =z^*J_N^*x
 =z^*M_N(M_N^{-1}J_N^*x).
\]
After the target is equipped with \(G_N\), that adjoint is \(M_N^{-1}J_N^*G_N=\widehat R_N\). Thus
\[
K_N=J_NM_N^{-1}J_N^*,\qquad
G_N=K_N^{-1},\qquad
\widehat R_N^*M_N\widehat R_N=G_N.
\]
These exact formulas are the intended metric content of the source wording about adjoints. Taking \(J_N^*\) itself to mean the weighted adjoint would apply the source metric twice and would change (15).

Let \(P_N\) and \(P_D\) be the \(H_\theta\)-orthogonal projections onto \(\mathcal P_N\) and \(\mathcal D_N\). Then
\[
P_Q=RG^{-1}R^*
\]
is the orthogonal projection onto \(\mathcal Q_N=R(C_u)\), and
\[
\mathcal P_N=\mathcal D_N\mathbin\perp\mathcal Q_N,
\qquad P_N=P_D+P_Q.
\]
These assertions follow directly from \(R^*R=G\), the injectivity of \(R\), and the dimension of the quotient. The multiplication operator \(Xf=uf\) is used only on the polynomial domain. All products below have finite polynomial degree, hence belong to \(H_\theta\). No boundedness of \(X\) on the entire Hilbert space is assumed.

## 2. Derivative of the least-norm lift and the full matrix curvature

The quotient equation \(J_NR=1\) has a fixed \(J_N\). Therefore \(R'x\in\mathcal D_N\) for every fixed coefficient vector \(x\). For any fixed polynomial \(d\in\mathcal D_N\), differentiating its orthogonality to \(Rx\), including the differentiated measure, gives
\[
0=\partial_\theta\langle d,Rx\rangle_\theta
 =\langle d,XR x+R'x\rangle_\theta.
\]
Consequently
\[
\boxed{R'=-P_DXR.}
\tag{A1}
\]
Its source and target are \(C_u\to\mathcal D_N\). Monic division gives a unique polynomial coefficient in \(\mathcal P_{N-q}\) for each such boundary. Composing that division with the already constructed theta primitive map gives the original analytic boundary primitive; no quotient derivative is substituted for multiplication by \(\chi\).

Differentiate the actual Gram, again including the measure derivative. The two terms containing \(R'\) vanish by boundary orthogonality. Thus
\[
\boxed{G'=R^*XR.}
\tag{A2}
\]
Differentiating this expression a second time gives
\[
\begin{aligned}
G''
 &=R'^*XR+R^*XR'+R^*X^2R\\
 &=R^*X^2R-2R^*XP_DXR.
\end{aligned}
\tag{A3}
\]
Here the star in each displayed term is evaluated at the given \(\theta\); (A3) explicitly accounts for the variation of the measure, rather than treating the Hilbert adjoint as constant.

Define the actual source maps
\[
O=(1-P_N)XR:
 C_u\longrightarrow\mathcal P_{N+1}\cap\mathcal P_N^\perp,
\qquad
I=P_DXR:C_u\longrightarrow\mathcal D_N.
\]
Now
\[
G'G^{-1}G'=R^*XP_QXR.
\]
Subtraction from (A3), followed by the proved identity \(P_Q+P_D=P_N\), gives
\[
\begin{aligned}
G''-G'G^{-1}G'
 &=R^*X(1-P_Q-2P_D)XR\\
 &=R^*X(1-P_N)XR-R^*XP_DXR\\
 &=\boxed{O^*O-I^*I.}
\end{aligned}
\tag{A4}
\]
All signs in source (22) are therefore correct. The outgoing target is one-dimensional. The incoming map also has rank at most one: for every \(d\in\widetilde\chi\mathcal P_{N-q-1}\), multiplication sends \(Xd\) back into \(\mathcal D_N\), whence \(\langle d,XR x\rangle=\langle Xd,Rx\rangle=0\). Only the final boundary direction can occur. At \(N=q-1\), the boundary space is zero and \(I=0\).

## 3. The two separate map traces and their shared term

Let \(Q_j\) be the real monic source orthogonal polynomials in \(u\), with full norms \(\omega_j\), and put \(d_j=[Q_j]\in C_u\). Orthogonality gives
\[
K_N=G_N^{-1}=\sum_{j=0}^N\frac{d_jd_j^*}{\omega_j},
\qquad
R_Nx=\sum_{j=0}^N Q_j\frac{d_j^*G_Nx}{\omega_j}.
\tag{A5}
\]
Hence
\[
O_Nx=Q_{N+1}\frac{d_N^*G_Nx}{\omega_N},
\]
and therefore
\[
\operatorname{Tr}(G_N^{-1}O_N^*O_N)
 =\frac{\omega_{N+1}}{\omega_N^2}d_N^*G_Nd_N.
\tag{A6}
\]

For \(N\geq q\), put \(m=N-q+1\geq1\), and let \(B_j\) be the real monic orthogonal polynomials for the actual relation weight \(|\widetilde\chi|^2d\mu_\theta\), with full norms \(\nu_j\). Define
\[
a_{N+1}=\frac{\omega_{N+1}}{\omega_N},
\qquad
\beta_m=\frac{\nu_m}{\nu_{m-1}},
\qquad
\delta_N=\frac{V_N}{V_{N-1}}=\frac{\omega_N}{\nu_{m-1}}.
\]
The last equality follows directly from the proved determinant quotient, with all indices retained. The rank-one inverse update proved in §5 below gives
\[
\frac{d_N^*G_Nd_N}{\omega_N}=1-\delta_N.
\]
Thus the first map trace is exactly
\[
\boxed{
\operatorname{Tr}(G_N^{-1}O_N^*O_N)
 =a_{N+1}(1-\delta_N).
}
\tag{A7}
\]

For the incoming trace use the actual unit vector spanning the final boundary direction:
\[
\psi=\frac{\widetilde\chi B_{m-1}}{\sqrt{\nu_{m-1}}}
 \in\mathcal D_N.
\]
The rank-one assertion above implies
\[
I_Nx=\psi\langle X\psi,R_Nx\rangle_\theta.
\]
Taking the trace with the quotient metric consequently gives
\[
\operatorname{Tr}(G_N^{-1}I_N^*I_N)
 =\|P_QX\psi\|_\theta^2.
\tag{A8}
\]
The relation orthogonal-polynomial recurrence gives
\[
(1-P_D)X\psi
 =\frac{\widetilde\chi B_m}{\sqrt{\nu_{m-1}}},
\qquad
\|(1-P_D)X\psi\|_\theta^2=\beta_m.
\]
This vector belongs to \(\mathcal P_{N+1}\). Its component outside \(\mathcal P_N\) is
\[
(1-P_N)X\psi=\frac{Q_{N+1}}{\sqrt{\nu_{m-1}}},
\]
because both numerators are monic of degree \(N+1\). The complement of \(\mathcal D_N\) inside \(\mathcal P_{N+1}\) is the orthogonal sum of \(\mathcal Q_N\) and the span of \(Q_{N+1}\). Thus
\[
\boxed{
\begin{aligned}
\operatorname{Tr}(G_N^{-1}I_N^*I_N)
 &=\beta_m-\frac{\omega_{N+1}}{\nu_{m-1}}\\
 &=\beta_m-a_{N+1}\delta_N.
\end{aligned}
}
\tag{A9}
\]
The equality also proves the nonnegativity of that expression. It does not assign positivity to the difference of the two map Grams.

Taking the trace of (A4), using the derivative formula for \(\log\det G_N\), now yields
\[
\begin{aligned}
(\log V_N)''
 &=\operatorname{Tr}(G_N^{-1}O_N^*O_N)
   -\operatorname{Tr}(G_N^{-1}I_N^*I_N)\\
 &=a_{N+1}(1-\delta_N)
   -(\beta_m-a_{N+1}\delta_N)\\
 &=a_{N+1}-\beta_m.
\end{aligned}
\tag{A10}
\]
This is source (20). The common term is \(a_{N+1}\delta_N=\omega_{N+1}/\nu_{m-1}\); it must be retained in both maps before it is cancelled in their difference.

At \(m=0\), \(N=q-1\), the whole source is the orthogonal quotient space. The last source column has leverage one, so (A6) is \(a_q\), and \(I=0\). Consequently \((\log V_{q-1})''=a_q\), in agreement with the zero curvature of the empty relation determinant. No negative-index relation determinant is used.

## 4. Exact quotient phase identity

Let \(T=M_u\) on \(C_u\), so that the original scaling generator is conjugate through \(L\) to \(c1+iT\). Define
\[
\sigma=\operatorname{Tr}T\in\mathbb R,
\qquad \ell_N=\log\det G_N.
\]
Reality follows from the real coefficients of \(\widetilde\chi\). It does not require evenness of the source measure.

Set
\[
\mathfrak b_N=Q_{N+1}-R_Nd_{N+1}.
\]
This is monic of degree \(N+1\) and belongs to the actual next boundary space \(\widetilde\chi\mathcal P_{N+1-q}\). Orthogonality of \(Q_{N+1}\) to \(\mathcal P_N\) gives
\[
R_N^*\mathfrak b_N=-G_Nd_{N+1}.
\tag{A11}
\]
The row giving the leading coefficient of \(R_Nx\) is \(d_N^*G_N/\omega_N\), by (A5). Furthermore
\[
J_{N+1}(XR_N-R_NT)=T-T=0.
\]
It follows by subtracting the leading term that
\[
XR_N-R_NT
 -\mathfrak b_N\frac{d_N^*G_N}{\omega_N}
 :C_u\longrightarrow\mathcal D_N.
\tag{A12}
\]
This states the precise boundary map suppressed by the source phrase “modulo old boundaries.” Its degree is at most \(N\), and its quotient is zero; monic division supplies its unique coefficient polynomial.

Multiplying (A12) by \(R_N^*\) kills that boundary map and gives
\[
R_N^*XR_N-G_NT
 =-\frac{G_Nd_{N+1}d_N^*G_N}{\omega_N}.
\]
Multiply by \(G_N^{-1}\), take the trace and use (A2). The result is
\[
\boxed{
\frac{d_N^*G_Nd_{N+1}}{\omega_N}
 =\sigma-\ell_N'.
}
\tag{A13}
\]

In original \(S\)-coordinates, the monic orthogonal polynomial satisfies
\[
p_j(c+iu)=i^jQ_j(u).
\]
Indeed the left side has leading coefficient \(i^j\), is orthogonal to all lower degrees under the literal coordinate change, and uniqueness of the monic orthogonal polynomial determines the stated factor. If \(b_j=[p_j]\in C_S\), then \(Lb_j=i^jd_j\). Since \(G_S=L^*G_uL\),
\[
b_N^*G_Sb_{N+1}
 =\overline{i^N}i^{N+1}d_N^*G_ud_{N+1}
 =i\,d_N^*G_ud_{N+1}.
\]
The determinant equality already proved implies that \(\ell_N\) and its derivative are unchanged by this fixed coordinate map. Hence
\[
\boxed{
\frac{b_N^*G_Sb_{N+1}}{\omega_N}
 =i(\sigma-\ell_N').
}
\tag{A14}
\]
The source sign and the factor \(i\) are correct. This calculation transports the full arithmetic coefficient algebra through an isomorphism and transports back; it does not remove the original \(S\)-coordinates or replace the arithmetic unit in \(\eta\).

## 5. Rank-two control and rank-one volume ratios

For completeness, the inherited control can be derived within these same coordinates. The monic recurrence is
\[
uQ_j=Q_{j+1}+\beta_j^{\mathrm{src}}Q_j
       +\frac{\omega_j}{\omega_{j-1}}Q_{j-1},
\]
with real diagonal coefficient and with the final term absent at \(j=0\). Apply the quotient, insert (A5), and subtract the adjoint expression. The off-diagonal terms telescope because
\( (\omega_j/\omega_{j-1})/\omega_j=1/\omega_{j-1}\). This gives
\[
TK_N-K_NT^*
 =\frac{d_{N+1}d_N^*-d_Nd_{N+1}^*}{\omega_N}.
\tag{A15}
\]
For \(A=c1+iT\), define the original Hermitian control form
\[
W_N=A^*G_N+G_NA-2cG_N.
\]
Since \(2c=k\), this is the original scaling-control form. Equation (A15) gives
\[
G_N^{-1/2}W_NG_N^{-1/2}
 =\frac{i(vu^*-uv^*)}{\omega_N},
\quad u=G_N^{1/2}d_N,\quad v=G_N^{1/2}d_{N+1}.
\tag{A16}
\]
The entries of \(d_N,d_{N+1},G_N\) are real in these coordinates, so \(u^*v\) is real and the trace of (A16) is zero. The matrix is Hermitian, has rank at most two, and is supported on the span of \(u,v\). Direct multiplication gives its squared trace
\[
\operatorname{Tr}\bigl((G_N^{-1/2}W_NG_N^{-1/2})^2\bigr)
 =\frac{2(\|u\|^2\|v\|^2-|u^*v|^2)}{\omega_N^2}.
\]
Its nonzero eigenvalues, if any, are therefore \(\epsilon_N,-\epsilon_N\), where
\[
\boxed{
\epsilon_N^2
 =\frac{(d_N^*G_Nd_N)(d_{N+1}^*G_Nd_{N+1})
       -|d_N^*G_Nd_{N+1}|^2}{\omega_N^2}.
}
\tag{A17}
\]
This includes the dependent-vector and one-dimensional cases: the expression is then zero. It is invariant under the proved \(S\)-coordinate transport.

For \(N\geq q\), both \(K_{N-1}\) and \(K_N\) are positive definite. Their exact update is
\[
K_N=K_{N-1}+\frac{d_Nd_N^*}{\omega_N}.
\]
Put \(t=d_N^*G_{N-1}d_N/\omega_N\geq0\). The determinant lemma and rank-one inverse identity imply
\[
\delta_N=\frac{1}{1+t},
\qquad
\frac{d_N^*G_Nd_N}{\omega_N}
 =\frac{t}{1+t}=1-\delta_N.
\tag{A18}
\]
The same determinant update one degree later gives
\[
\frac{d_{N+1}^*G_Nd_{N+1}}{\omega_{N+1}}
 =\delta_{N+1}^{-1}-1.
\tag{A19}
\]
All these formulas permit a zero quotient column; no strict leverage inequality is imposed. Substituting (A13), (A18) and (A19) into (A17) proves
\[
\boxed{
\epsilon_N^2
 =a_{N+1}(1-\delta_N)(\delta_{N+1}^{-1}-1)
  -(\sigma-\ell_N')^2.
}
\tag{A20}
\]
Equivalently, with \(v_j=-\log\delta_j\), this is exactly source (26).

## 6. The endpoint at the first admitted source degree

At \(N=q-1\), the quotient map from \(\mathcal P_{q-1}\) is an isomorphism. Thus its full source basis \(d_0,\ldots,d_{q-1}\) is a basis of \(C_u\), and its last leverage equals one:
\[
d_{q-1}^*G_{q-1}d_{q-1}=\omega_{q-1}.
\tag{A21}
\]
The difference \(Q_q-\widetilde\chi\) has degree at most \(q-1\) and quotient \(d_q\). Since there are no old boundaries, it is the unique lift:
\[
R_{q-1}d_q=Q_q-\widetilde\chi.
\]
Therefore
\[
\widetilde\chi=Q_q-R_{q-1}d_q.
\]
The two terms on the right are orthogonal, because \(Q_q\) is orthogonal to the entire preceding source. Keeping both squared norms yields
\[
\boxed{\nu_0=\omega_q+d_q^*G_{q-1}d_q.}
\tag{A22}
\]
Here \(\nu_0=\|\widetilde\chi\|_\theta^2=\|\chi(c+iu)\|_\theta^2=Z_\chi(\theta)\); the norm equality follows from the retained scalar phase of modulus one.

Insert (A21) and (A22) into (A17), and use the phase identity, which is valid at this degree. This proves
\[
\boxed{
\epsilon_{q-1}^2
 =\frac{\nu_0-\omega_q}{\omega_{q-1}}
   -(\sigma-\ell_{q-1}')^2.
}
\tag{A23}
\]
This establishes source (27) without introducing \(G_{q-2}\), \(K_{q-2}^{-1}\), or a quotient determinant of an unsaturated source. The prose after source (27) should use (A22), rather than equating the vector \(d_N\) with a scalar. Transport back to the original coordinates gives the fully typed scalar identity
\[
d_q^*G_{u,q-1}d_q
 =b_q^*G_{S,q-1}b_q
 =\nu_0-\omega_q,
\]
where the metric subscripts distinguish the coordinate matrices and \(Lb_q=i^qd_q\).

## 7. Exact two-loss identity, bound and equality conditions

For \(N\geq q\), let
\[
x=v_N\geq0,\quad y=v_{N+1}\geq0,
\qquad s=(x+y)/2,\quad t=(y-x)/2.
\]
Direct multiplication, with all factors retained, gives
\[
\begin{aligned}
(1-e^{-x})(e^y-1)
 &=e^y-1-e^{y-x}+e^{-x}\\
 &=2e^t\cosh s-1-e^{2t}\\
 &=\sinh^2s-(e^t-\cosh s)^2.
\end{aligned}
\tag{A24}
\]
Together with (A20), this proves the exact decomposition
\[
\boxed{
\epsilon_N^2
 =a_{N+1}\sinh^2s
  -a_{N+1}(e^t-\cosh s)^2
  -(\sigma-\ell_N')^2.
}
\tag{A25}
\]
The first norm ratio is positive, all displayed quantities are real, and the last two terms are nonnegative squared losses. Moreover
\[
\mathcal R_N=e^{2s}=\frac{V_{N-1}}{V_{N+1}}\geq1,
\qquad
\sinh s=\frac{\mathcal R_N-1}{2\sqrt{\mathcal R_N}}.
\]
Since \(\epsilon_N\geq0\), taking square roots yields
\[
\boxed{
\epsilon_N\leq
\sqrt{a_{N+1}}
\frac{\mathcal R_N-1}{2\sqrt{\mathcal R_N}}.
}
\tag{A26}
\]
This is source (3) and (29), with both discarded quantities explicitly identified by (A25).

Equality in (A26) holds exactly when both
\[
\sigma-\ell_N'=0,
\qquad e^t=\cosh s
\tag{A27}
\]
hold. The second condition is equivalent to
\[
2\delta_N=1+\delta_N\delta_{N+1}.
\tag{A28}
\]
Indeed multiplying \(e^t=\cosh s\) by \(2\sqrt{\delta_N\delta_{N+1}}\) gives precisely (A28). Equal consecutive contractions instead give \(t=0\) and the first squared loss \((1-\cosh s)^2\), which vanishes only at \(s=0\). Thus “imbalance” should not be read as “difference from equal consecutive contractions.” The exact expression (A25) already has the correct behavior.

## 8. Scope and consequence for the live arithmetic estimate

At \(\theta=0\), these are the original arithmetic source and canonical quotient metric. At other real tilts the formulas describe the stated exponential observation of that source. The exact map of Hilbert spaces is \(f\mapsto e^{\theta u/2}f\) from \(H_\theta\) to \(H_0\), with inverse \(f\mapsto e^{-\theta u/2}f\). It changes neither the admitted finite polynomial list nor the original coefficient unit in the arithmetic jet map.

Inserting the already proved exterior result \(L_{h,k}\leq\epsilon_N\) at zero tilt, (A26), monotonicity of \(\operatorname{arsinh}\) and \(s\geq0\) give exactly
\[
\log\frac{V_{N-1}}{V_{N+1}}
 \geq 2\operatorname{arsinh}
       \left(\frac{L_{h,k}}{\sqrt{a_{N+1}}}\right).
\]
Summing the inequalities for \(N=N_0,N_0+2,\ldots,N_0+2r-2\) cancels the consecutive intermediate logarithms and gives source (31), with denominator \(V_{N_0+2r-1}\) and coefficients \(a_{N_0+2j+1}\). This review verifies the new algebraic implication from the exterior bound; it does not substitute for a proof of that inherited exterior theorem.

For \(h=1\), the original positive-depth quotient is zero and \(\chi=1\). The source and relation determinants coincide, their quotient is the empty determinant \(1\), and the above nonzero-dimensional inverse formulas are outside their stated domain. The original analytic mass remains positive and the two distinct split elements remain. This exceptional fibre is retained.

No uniform bound in \(k\), no subcubic limiting estimate, no arithmetic zero exclusion and no formalization certificate follow from this review. The reviewed contribution is the complete exact matrix-to-volume calculation on the stated original finite sources, including the shared curvature term, the endpoint and both scalar losses.
