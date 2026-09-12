# Independent original-source review of DE.28–35

Date: 2026-09-12. Result: **no correction to the displayed formulas, cutoff shift, primitive signs, or numerical factors is needed.** This is a written mathematical review of the actual analytic source and its cochain domains, not a numerical test or a new formal certification. Neither reviewed document was changed.

## Exact sources and scope

Both documents were read in full:

- `DIAGONAL_EXTERIOR_PROOF.md`, 396 lines, SHA256 `492e01238632e646818f9acd7274c0ee7f49805c9a4dfd2197cc702662302d9a`. Reviewed equations DE.28–35 are at lines 268, 276, 290, 298, 313, 330, 345, and 352.
- The frozen PR17 `NOTE.tex` at `private-profile/Documents/math/output/split_zero_rh_tandem_2026-09-12/release_20260912f/sources/web_sum_connection_delivery/Tau_Sum_Connection_Control/sources/Tau_Spectral_Sum_Descent/NOTE.tex`, 839 lines, SHA256 `a3becf8455ddf96e8e382762acbc0e9d0548ea7342c01d70aecdad744ae79552`. Relevant original definitions: section 2, lines 123–172; full tensor unit jet (4.8), line 419; source measure and change of variables (5.1)–(5.4), lines 436–461; full-cutoff minimum metrics, section 6.

The arithmetic application retains the original nonempty full-order zero packet: its monic polynomial is \(h\), its degree is \(d\ge1\), \(g=2\xi\), \(v_h=g/h\), and \(\upsilon=j_h(v_h)\in E_h^\times\). No eigenvalue-only replacement or change of source measure is made.

## 1. Full unit and actual jet intertwining

For the full polynomial-remainder representative of \(v\in E_h^\times\), put \(u=v(s_1)v(s_2)\). The first two identities in DE.28 follow by multiplication of representatives. On the diagonal, \(u(t,t)=v(t)^2\), proving the identity for \(\rho\). For \(\iota(q)=H_1q(S/2)\), the symmetric polynomial

\[
u-v(S/2)^2
\]

is divisible by \(\Delta=(s_1-s_2)^2\). Consequently \(\Delta H_1=0\) gives \(uH_1q(S/2)=H_1v(S/2)^2q(S/2)\). This proves the final identity without specializing \(H_1\) or discarding nilpotent jets. The squared unit is the full class modulo \(h\).

More importantly, original source equations (2.3), (2.4), and (4.8) give

\[
\mathcal T_2(P)=P(D_1,D_2)(F_h\otimes F_h),\qquad
J^{(2)}\mathcal T_2(P)=(\upsilon\otimes\upsilon)[P].
\]

Since \(D=-x\partial_x\) becomes **multiplication** by the Mellin variable, not differentiation of that variable,

\[
J^{(2)}(D_1-D_2)\mathcal T_2(P)
=(\upsilon\otimes\upsilon)[(s_1-s_2)P]
=r_AJ^{(2)}\mathcal T_2(P).
\]

There is no derivative of \(\upsilon\), additional phase, or drift term.

## 2. Actual minimum, parity, cutoff, and boundary energy

The ordinary source swap is unitary for the original product measure \(\nu_h\otimes\nu_h\), preserves the full total-degree space and relation ideal, and commutes with the full jet because the tensor unit is symmetric. Uniqueness of the least-norm lift therefore proves

\[
\operatorname{swap}_{\rm source}R_N
=R_N\operatorname{swap}_{\rm quotient}.
\]

This supplies the source-level parity justification implicit in DE.31. It uses identical tensor factors, not a new reflection hypothesis. The literal orbit insertions retain their original factors, in particular \(I_-^*I_-=2I\) and \(L_-=I_-^*/2\).

The original complete ordered quotient is reached for \(N\ge2(d-1)\). Multiplication of a numerator by \(s_1-s_2\) raises its degree by at most one. Hence the corrected minimum must be taken at **\(N+1\)** as written. Each difference in DE.31 has zero full jet and numerator degree at most \(N+1\). Invertibility of the full tensor unit identifies this zero-jet space with the entire original truncated ideal \((h(s_1),h(s_2))\), not a selected boundary family.

The \(N+1\) least-norm lift is orthogonal to that whole boundary space. The mixed terms thus vanish when expanding, for example,

\[
r_DR_N^-=R_{N+1}^+\mathsf M+E_N^+.
\]

This proves the first DE.32 identity with the additional term \((E_N^+)^*E_N^+\); the other identity follows with the opposite parity. DE.30 is only the target-minimum pullback and does not identify two pre-existing source metrics.

There is no hidden unbounded-adjoint assumption: \(r_D\) is applied to the polynomial-source range of a finite-dimensional lift. The star on \(r_DR_N^\pm\) is the adjoint of this everywhere-defined finite-domain map into the source Hilbert space.

## 3. Primitive in the original differential domains

The source complex is \([V\xrightarrow{\Theta}\mathcal B]\), with \(V\) in degree zero and \(\mathcal B\) in degree one. Here \(V\) consists of even Schwartz functions with value and integral zero. The operator \(D\) preserves \(V\): parity and the value at zero are preserved, and integration by parts gives \(\int D\phi=\int\phi=0\). Its preservation of \(\mathcal B\) follows directly from that space's \(x^bD^j\) seminorms. Schwartz convergence also gives \(D\Theta=\Theta D\). The original \(\phi_*\) belongs to \(V\), while \(F_h\in\mathcal B\); it is not necessary or appropriate to put \(\phi_*\) in \(\mathcal B\).

Ordered monic division first by \(h(s_1)\), then by \(h(s_2)\), yields

\[
F=h_1C_1+h_2C_2,\qquad \deg C_i\le N+1-d.
\]

Each subtraction preserves this total-degree bound. The remainder has each variable degree below \(d\) and is zero by the complete quotient basis and the full unit's invertibility. The stated parity averaging preserves both the identity and these bounds.

The resulting primitive

\[
K=C_1^\varepsilon(D)(\phi_*\otimes F_h)
-C_2^\varepsilon(D)(F_h\otimes\phi_*)
\]

lies in \((V\otimes\mathcal B)\oplus(\mathcal B\otimes V)\). The tensor differential has signs \(+\Theta\otimes1\) and \(-1\otimes\Theta\) on these summands. Therefore, using the original \(h(D)F_h=\Theta\phi_*\),

\[
dK=C_1^\varepsilon(D)(\Theta\phi_*\otimes F_h)
+C_2^\varepsilon(D)(F_h\otimes\Theta\phi_*)
=\mathcal T_2(F).
\]

Thus the displayed minus sign is essential and correct. The graded swap has no mixed-degree sign and gives \(TK=-\varepsilon K\): the symmetric correction has its primitive in the original signed projector, and the antisymmetric correction has its primitive in the retained complement. Ordered division specifies a linear choice; it need not give uniqueness among all primitives.

The \(d=1\) edge is consistent. Although the exterior quotient and \(\mathsf P\) vanish, the symmetric minimum can have nonzero antisymmetric source boundary. Writing \(h=s-a\) and \(R_0^+(1)=cF_h\otimes F_h\), its difference numerator is \(c(h_1-h_2)\), with primitive \(c(\phi_*\otimes F_h+F_h\otimes\phi_*)\). Its full energy is precisely the second DE.32 boundary term.

## 4. Original measure and odd coefficient weight

Original source equations (5.1)–(5.4) give \(w_h=|v_h(1/2+it)|^2/(2\pi)\). Under \(u=t_1+t_2\), \(v=t_1-t_2\), the Jacobian is \(1/2\), \(S=1+iu\), \(r=iv\), and \(\Delta=-v^2\). Thus \(|r|^2=v^2\), while the two powers of \(\Delta\) in a Gram coefficient contribute \((-1)^{a+c}\). This gives exactly DE.34 and DE.35, including both original \(1/(2\pi)\) factors and the separate \(1/2\) Jacobian. Original source exponential moments justify the finite polynomial expansions and integrals.

For an odd numerator of total degree at most \(M\), division by \(r\) leaves the precise coefficient cutoff \(\deg_S f_a+2a\le M-1\). This agrees with the stated degree decrease and does not alter the original \(N\mapsto N+1\) boundary comparison.

## Editorial conclusion

No mathematical correction is requested. For a self-contained reader, one sentence proving least-norm swap equivariance and one sentence identifying the primitive's two mixed cochain domains would make the already-valid source argument explicit. An independent second reader checked DE.33's domains, signs, degree bounds, graded parity, and the \(d=1\) case with the same conclusion. No new Lean or finite-check claim is made.
