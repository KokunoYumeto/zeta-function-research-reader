# Exact geometric-scale maps to the original-zeta quotient

24 September 2026. Proof labels GI1–GI7. These are actual algebraic intertwiners between the two receivers of FT, followed by a calculation of their graph closures in the specified topologies. No coordinate or arithmetic operation is put on \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). Source labels are carried by the disjoint family in ZR; all vector-space operations here are on coefficient fibers.

Inputs, with complete proofs in the cumulative reader: `INTEGRAL_FROBENIUS_TRANSFER_ALGEBRA.md` FT1–FT10, `ORIGINAL_ZETA_RESOLVENT_AND_PROJECTORS.md` RZ1–RZ12, and `../quantum_tau_programme_bridge_20260924/GLOBAL_MELLIN_SYNTHESIS.md` S1–S7. The finite geometric covering maps were derived in FT6; the complete original-zeta quotient is the proved arithmetic source quotient in S5. No new identification between those original sources is presumed.

## GI1. The two coefficient spaces and all scale factors

Let
\[
 E_0=\bigoplus_{q\in\mathbb Q_{>0}}\mathbb C e_q,
 \qquad \Big\|\sum_q a_qe_q\Big\|^2
       =AB\sum_q q|a_q|^2,
 \qquad A=\log p>0,\ B=2\pi,
\tag{GI1.1}
\]
where \(p\) is the fixed recovered prime specifying the original torus periods in FT6. Sums in \(E_0\) have finite support. Its Hilbert completion is the degree-zero receiver \(H^0_{\mathrm{geom}}\) of FT10. The integral algebra \(\mathcal C\) acts by
\[
 F_ne_q=e_{nq},\qquad V_ne_q=n e_{q/n}\qquad(n\geq1).
\tag{GI1.2}
\]
These are the full covering pullback and transfer actions; neither the factor \(n\) nor the measure weight \(qAB\) is omitted.

On the other side retain
\[
 \mathcal Q=\mathcal B/\mathcal I,
 \qquad T_q[F]=[q^sF(s)],
 \qquad\Psi(F_n)=T_n,\quad\Psi(V_n)=nT_{1/n}.
\tag{GI1.3}
\]
Here \(\mathcal B\) is the entire strip-Schwartz space, with seminorms
\[
 b_{a,M}(F)=\sup_{|\operatorname{Re}s|\leq a}
              (1+|\operatorname{Im}s|)^M|F(s)|,
\tag{GI1.4}
\]
and \(\mathcal I\) consists of the functions vanishing at all actual nontrivial zeros of the original \(\zeta\), to their entire original multiplicities. It is closed because each derivative evaluation is continuous by Cauchy's integral formula on a compact disc. Thus \(\mathcal Q\) has the Hausdorff quotient topology. Its original source comparison retains
\[
 F_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s),
\tag{GI1.5}
\]
including all endpoint and trivial-zero comparisons proved in CD and S. This calculation uses the original \(s\), without moving the spectral line.

## GI2. All algebraic intertwiners are explicitly obtained

For each \(x\in\mathcal Q\), define
\[
 K_x:E_0\longrightarrow\mathcal Q,\qquad
 K_x\left(\sum_q a_qe_q\right)=\sum_q a_qT_qx.
\tag{GI2.1}
\]
This finite sum defines a complex-linear map on the entire stated domain. It intertwines both generators:
\[
 K_x(F_ne_q)=T_{nq}x=T_nK_x(e_q),
\tag{GI2.2}
\]
\[
 K_x(V_ne_q)=nT_{q/n}x=nT_{1/n}K_x(e_q).
\tag{GI2.3}
\]
Integer linearity and multiplication extend these identities to every element of \(\mathcal C\), and complex linearity to its scalar extension.

Conversely, let \(K:E_0\to\mathcal Q\) be a complex-linear intertwiner for this specified algebra. Set \(x=K(e_1)\). For a reduced positive rational \(q=a/b\),
\[
 e_{a/b}=\frac1b F_aV_be_1.
\tag{GI2.4}
\]
Intertwining and complex linearity give
\[
 K(e_{a/b})=\frac1b T_a(bT_{1/b})x=T_{a/b}x.
\tag{GI2.5}
\]
Thus \(K=K_x\). The scalar divisions in GI2.4–GI2.5 occur on the complex coefficient spaces, not inside the integral algebra \(\mathcal C\). This proves a complete classification of the algebraic intertwiners and gives their exact image:
\[
 M_x=\operatorname{span}_{\mathbb C}\{T_qx:q\in\mathbb Q_{>0}\}.
\tag{GI2.6}
\]
In the locally convex direct-sum topology on \(E_0\), every \(K_x\) is continuous: its restriction to every finite-dimensional coordinate subspace is a linear map to \(\mathcal Q\), hence continuous, which is the defining final property of this topology. The Hilbert topology has a different answer, calculated next.

## GI3. Strong continuity of the actual multipliers at scale one

For positive real \(q\), let \(t=\log q\). The identity
\[
 e^{ts}-1=ts\int_0^1e^{uts}\,du
\tag{GI3.1}
\]
gives, when \(|\operatorname{Re}s|\leq a\),
\[
 |q^s-1|\leq |\log q|\,|s|\,e^{a|\log q|}.
\tag{GI3.2}
\]
Since \(|s|\leq(a+1)(1+|\operatorname{Im}s|)\) on this strip, every \(F\in\mathcal B\) satisfies
\[
 b_{a,M}((q^s-1)F)
 \leq |\log q|e^{a|\log q|}(a+1)b_{a,M+1}(F).
\tag{GI3.3}
\]
Thus \(q^sF\to F\) in every original seminorm as \(q\to1\), and passing through the continuous quotient map proves
\[
 T_qx\longrightarrow x\quad\text{in }\mathcal Q.
\tag{GI3.4}
\]
The bound is uniform for \(q\) in an interval shrinking to one. It retains the entire strip and uses only one additional decay seminorm; no analytic continuation or location assumption on zeros has been inserted.

## GI4. An explicit sequence proves nonclosability for every nonzero receiver

For each integer \(N\geq1\), choose the explicit distinct positive rationals
\[
 q_{N,j}=1+\frac{j}{N^2},\qquad 1\leq j\leq N,
 \qquad u_N=\frac1N\sum_{j=1}^Ne_{q_{N,j}}\in E_0.
\tag{GI4.1}
\]
Orthogonality of distinct scale components gives the full norm
\[
 \|u_N\|^2
 =\frac{AB}{N^2}\sum_{j=1}^N\left(1+\frac{j}{N^2}\right)
 =AB\left(\frac1N+\frac{N+1}{2N^3}\right)
 \longrightarrow0.
\tag{GI4.2}
\]
All \(q_{N,j}\) lie in \([1,1+1/N]\). Therefore GI3 gives
\[
 K_xu_N=\frac1N\sum_{j=1}^N T_{q_{N,j}}x
       \longrightarrow x\quad\text{in }\mathcal Q.
\tag{GI4.3}
\]
For an explicit quotient verification choose any representative \(F\) of \(x\); GI3.3 bounds the difference of the average representatives from \(F\) by the supremum of its right side over \([1,1+1/N]\), which tends to zero for every seminorm.

A densely defined linear map from the Hilbert space into this Hausdorff topological vector space is closable only if the closure of its graph contains no pair \((0,y)\) with \(y\ne0\). GI4.2–GI4.3 put \((0,x)\) in that graph closure. Hence
\[
 \boxed{K_x:E_0\subset H^0_{\mathrm{geom}}\to\mathcal Q
            \text{ is closable exactly when }x=0.}
\tag{GI4.4}
\]
For \(x=0\), the map is zero and extends continuously to the Hilbert completion, proving the other direction. In particular no nonzero \(K_x\) is Hilbert-continuous. This conclusion applies to critical-line and off-line blocks alike; it is not a zero-location criterion.

## GI5. The whole graph closure and the retained cyclic image

Let \(\Gamma_x\) denote the graph of \(K_x\), and take its closure in \(H^0_{\mathrm{geom}}\times\mathcal Q\). Then
\[
 \boxed{\overline{\Gamma_x}
          =H^0_{\mathrm{geom}}\times\overline{M_x}.}
\tag{GI5.1}
\]
To prove it, GI4 first gives \((0,x)\in\overline{\Gamma_x}\). For every positive rational \(r=a/b\), the operator sending \(e_q\) to \(e_{rq}\) is \(b^{-1}F_aV_b\) on the complex domain. Its squared norm is exactly \(r\), because
\[
 AB\sum_q rq|a_q|^2=r\,AB\sum_q q|a_q|^2.
\tag{GI5.2}
\]
It extends boundedly to the Hilbert completion, and the target operator is the continuous \(T_r\). Intertwining makes their product action preserve the graph and its closure. Applying it to \((0,x)\) gives \((0,T_rx)\) in the closure. Closed linearity then gives \(\{0\}\times\overline{M_x}\subseteq\overline{\Gamma_x}\).

For any \(u\in E_0\), subtracting \((0,K_xu)\) from its graph point \((u,K_xu)\) gives \((u,0)\) in the closed graph. Density of \(E_0\) gives \(H^0_{\mathrm{geom}}\times\{0\}\) in that closure, and adding the two subspaces proves one inclusion in GI5.1. The reverse inclusion follows because every original graph value lies in \(M_x\) and \(H^0_{\mathrm{geom}}\times\overline{M_x}\) is closed. This proves the whole formula rather than only the failure of boundedness.

## GI6. Every multiplicity jet in a local cyclic image

For an actual nontrivial zero \(\rho\) with multiplicity \(m\), retain its actual continuous projector \(P_\rho\) from RZ and its full block \(\mathcal Q_\rho\). If \(x\in\mathcal Q_\rho\), then
\[
 K_x(e_q)=q^\rho\sum_{j=0}^{m-1}
                    \frac{(\log q)^j}{j!}N_\rho^j x.
\tag{GI6.1}
\]
No jet has been projected away. For nonzero \(x\), let \(d\) be the least positive integer with \(N_\rho^d x=0\). The vectors
\[
 x,N_\rho x,\ldots,N_\rho^{d-1}x
\tag{GI6.2}
\]
are independent: in a nontrivial relation choose the first nonzero coefficient at index \(j_0\) and apply \(N_\rho^{d-1-j_0}\); only that coefficient times \(N_\rho^{d-1}x\ne0\) survives.

Every vector in GI6.1 belongs to their span. Conversely choose \(q=2^k\), \(0\leq k<d\). The coefficient matrix in this ordered list is
\[
 \left[2^{k\rho}\frac{(k\log2)^j}{j!}\right]_{0\leq k,j<d}.
\tag{GI6.3}
\]
Its determinant retains every factor:
\[
 \left(\prod_{k=0}^{d-1}2^{k\rho}\right)
 \left(\prod_{j=0}^{d-1}\frac{(\log2)^j}{j!}\right)
 \prod_{0\leq k<\ell<d}(\ell-k)\ne0.
\tag{GI6.4}
\]
Thus these images span every vector in GI6.2, proving
\[
 M_x=\operatorname{span}_{\mathbb C}
                 \{x,N_\rho x,\ldots,N_\rho^{d-1}x\},
 \qquad\dim M_x=d.
\tag{GI6.5}
\]
It is closed in the Hausdorff locally convex space \(\mathcal Q\), since it is finite dimensional. In particular, use the quotient class of RZ's zero-isolating function, \(x=[E_{\rho,0}]=[e_\rho]\in\mathcal Q\). For this actual cyclic vector, \(d=m\), \(M_x=\mathcal Q_\rho\), and GI5 becomes
\[
 \overline{\Gamma_{[E_{\rho,0}]}}
       =H^0_{\mathrm{geom}}\times\mathcal Q_\rho.
\tag{GI6.6}
\]
This gives a surjective algebraic map to each complete actual zero block, including all multiplicities, with its entire graph closure explicitly calculated.

## GI7. Consequence for the geometric purity comparison

FT10 proves the exact circle spectrum \(|\lambda|=\sqrt n\) and empty point spectrum for the geometric Hilbert shift of degree \(n\geq2\). GI2 constructs the algebraic maps to every actual original-zeta coefficient vector, and GI6 proves surjectivity onto every actual finite zero block when its cyclic vector is chosen. GI4–GI5 show exactly why these particular maps do not transport that Hilbert spectral statement: every nonzero map is nonclosable in that Hilbert topology, although it is continuous for the original direct-sum topology of the algebraic domain.

This is an actual morphism and its complete topological defect, not an assertion that the two constructions are unrelated. The same defect occurs for a hypothetical off-line block and for every critical-line block. It neither assumes nor disproves RH. The source's complete zero detector and its reflected Weil pairing remain unchanged. The support-record version sends \((\ell,u)\) to \((\ell,K_xu)\), retaining \((\ell,0)\) when its coefficient is zero, exactly as ZR2–ZR4 prove.
