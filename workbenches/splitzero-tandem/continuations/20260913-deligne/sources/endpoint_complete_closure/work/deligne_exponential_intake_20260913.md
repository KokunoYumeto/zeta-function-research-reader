# Complete intake and proof audit of the polynomial-exponential comparison

Date: 13 September 2026. Scope: the newly delivered exponential comparison, its exact original-source dependencies, and the additional determinant calculation. Original delivered files are unchanged. No Lean, predecessor-suite replay, remote edit, or claim of an RH conclusion is part of this intake.

## 1. Exact source and reading scope

The archive `Tau_Deligne_Exponential_Comparison_2026-09-13.zip` has 692,455 bytes and SHA-256 `cab9b98618f812f71e2407b26f6c2a48eb65d4fbcbe9b9cfea93ab6547c8d936`. Its 52 files were safely extracted under `output/split_zero_rh_tandem_2026-09-12/sources/web_deligne_exponential_delivery/Tau_Deligne_Exponential_Comparison`. Every path was resolved inside that destination before writing. The extraction receipt is `work/deligne_exponential_extraction_20260913.json`.

The complete 39,393-byte `NOTE.tex`, SHA-256 `919f4036a3b3e10fcef0b5bf1b1aff5c0e4fb4dfa311feea51d61ed7c546e9f2`, was read in disjoint line ranges covering the entire file. The complete `SOURCE_REVIEW.md`, `HANDOFF.md`, `CHECKS.md`, `PROGRAMME_STATE.md`, `check_exponential.py` and manifest were read. The combined user paste also contains the distinct logarithmic-constituent packet; its detailed constituent calculation belongs to the parallel intake and is not claimed here as a fresh full audit.

The actual S20 `edition/source_language.ndjson` was read at complete printed pages 178, 215 and 216. Page 178 supplies Corollary 1.8.12 with both **lisse** and **mixed** hypotheses and a connected finite-type base. Pages 215–216 give the explicit exponential-sheaf theorem (3.7.2.3), the local-acyclicity-at-infinity proof of Lemma 3.7.3, and the connected-family argument. The current record still has the reported internal final cross-reference mismatch and the `S'_0`/`S_0` typography. This intake uses the displayed theorem with its verified hypotheses; it does not silently repair that source or claim a new complete proof of Deligne's theorem.

The original source definitions and theta multiplier were reread in `tex/arithmetic_input.tex`, beginning through (A6). The complete relevant canonical tensor-source construction was reread in `tex/coherent_tensor_integration.tex`, equations (CT.1)–(CT.6) and (CT.11)–(CT.15). The full constructive cyclic retraction proof (CC.12)–(CC.14) was reread in `work/cyclic_conormal_depth_continuation_20260912.tex`. The topology limitation and its exact graph comparison were reread in `tex/jet_topology.tex`, (JT1)–(JT8). These dependencies establish the actual domain of the source observation used below.

## 2. The polynomial complex and arbitrary base change

Keep the original monic polynomial

\[
\chi(S)=S^q+\sum_{a=0}^{q-1}c_aS^a,\qquad q>0,
\]

and the coefficient ring \(R=\mathbb C[u,t]\). Define the coefficient-linear map

\[
L=u\partial_S+\chi(S)-t:R[S]\longrightarrow R[S],
\qquad \mathcal C=[R[S]\xrightarrow{L\,dS}R[S]dS].
\]

For every nonzero \(P=bS^n+\cdots\), the term of degree \(n+q\) in \(LP\) is exactly \(bS^{n+q}\); every other term has lower degree. Thus \(L\) is injective. To divide a polynomial \(F\) of degree \(N\ge q\), subtract \(L(bS^{N-q})\), with its exact current leading coefficient \(b\). This strictly decreases the degree. Iteration gives

\[
F=LQ+R_F,\qquad \deg R_F<q.
\]

If two such expressions existed, their difference would make a nonzero element of \(L(R[S])\) have degree less than \(q\), contradicting the first calculation. This proves

\[
R[S]=L(R[S])\oplus R[S]_{<q},\quad H^0\mathcal C=0,
\quad H^1\mathcal C\cong R^q.
\]

The procedure uses addition, multiplication and the leading coefficient one of \(\chi\); it never divides by a parameter or by a discriminant. The same direct decomposition holds after any coefficient-ring base change. At \(u=t=0\), the differential is the literal multiplication map by \(\chi\), so the specialization is precisely \(E=\mathbb C[S]/(\chi)\). Repeated-root jets survive unchanged.

The exact relation to multiplication is

\[
[L,M_S]=uI,\qquad [\chi-t]=0,\qquad [S(\chi-t)]=-u[1].
\]

These equations retain the coefficient-module quotient and exhibit why its general fibre does not acquire the original polynomial multiplication merely by naming it a quotient. The descending parameter connection is the actual bridge.

## 3. Connections, signs and the retained special-fibre operator

After inverting \(u\), the identities

\[
[L,\partial_t]=I,\qquad [L,-M_S/u]=-I
\]

show that \(\partial_t-M_S/u\) commutes with \(L\). It therefore sends its image to itself and descends to \(\nabla_t\). In the exact degree-below-\(q\) frame, only \(S^q\) needs reduction; \(L(1)=\chi-t\). Thus

\[
\nabla_t=\partial_t-A(t)/u,\qquad
A(t)=A+t e_0e_{q-1}^{T},\qquad A=M_S\text{ on }E.
\]

The last column is \((-c_0+t,-c_1,\ldots,-c_{q-1})^T\). In particular

\[
(-u\nabla_t)(fv)=f(-u\nabla_t)v-u(\partial_tf)v.
\]

The operator preserves the ideal \((u,t)H^1\mathcal C\): differentiating a term \(tv\) produces \(-uv\), which is still in that ideal. Its induced endomorphism on the specified special fibre is exactly \(A\). The formula is a connection in the \(t\) direction, not a derivative in \(u\).

With variable original coefficients, put

\[
\nabla_{c_a}=\partial_{c_a}+S^{a+1}/((a+1)u).
\]

The two commutators with \(L\) are \(-S^a\) and \(+S^a\). All these unreduced parameter operators commute with one another; the same flatness holds after passing to the coefficient quotient. The paper's bilinear duality below is specifically horizontal for the displayed \(t\)-connection. It does not claim that its constant residue matrix gives all coefficient-direction dualities without further terms.

## 4. The original theta domain and the full retraction

The source is the original strong Schwartz space

\[
\mathscr B=\{F\in C^\infty(\mathbb R_+):
\sup_{x>0}x^b|D^jF(x)|<\infty\text{ for every }b\in\mathbb Z,j\ge0\},
\quad D=-x\partial_x,
\]

and its stated completed tensor product. Its Mellin transform and all finite derivatives are entire. To see continuity of a Taylor evaluation at \(\rho\), split the integral of \(F(x)x^\rho(\log x)^a/a!\,dx/x\) at one and bound the two halves by seminorms with powers strictly beyond \(\Re\rho\). The integrals of a polynomial in \(|\log x|\) against those strictly decaying powers are finite. Tensoring these finite families gives the continuous full-jet map \(J^{(k)}\). Integration by parts, with both original ends zero, gives

\[
J^{(k)}D^{(k)}=A_kJ^{(k)}.
\]

The original multiplier is \(g=2\xi\), and \(\mathcal M\Theta\phi=gH_\phi\) with \(H_\phi\) holomorphic at every admitted nontrivial zero. Because \(h\) retains complete multiplicities, each theta boundary has zero full \(h\)-jet. In a tensor boundary, one factor has this zero jet; hence the whole tensor jet is zero, with the tensor differential signs unchanged.

For completeness, the equivariant retraction extends directly to the full finite tensor packet, without assuming that its cyclic image is an orthogonal or symmetric direct factor. On its \(\lambda\)-primary part \(M_\lambda\), put \(N=A_k-\lambda I\), let \(\ell\) be its exact nilpotent order and let \(w_\lambda\) be the full arithmetic-unit vector. The earlier local monomial calculation gives \(N^{\ell-1}w_\lambda\ne0\). Choose the specified coefficient functional \(\theta\) detecting that vector and set

\[
\pi^0_\lambda(v)=\sum_{j=0}^{\ell-1}
\theta(N^{\ell-1-j}v)X^j\pmod {X^\ell},\quad
p_\lambda=\pi^0_\lambda(w_\lambda),\quad
\pi_\lambda=p_\lambda^{-1}\pi^0_\lambda.
\]

Here \(p_\lambda(0)\ne0\); its inverse is the exact finite geometric polynomial
\(p_\lambda(0)^{-1}\sum_{j=0}^{\ell-1}[-(p_\lambda/p_\lambda(0)-1)]^j\).
Coefficient shifting proves \(\pi^0_\lambda N=X\pi^0_\lambda\), and therefore
\(\pi_\lambda(P(N)w_\lambda)=P(X)\). Summing via the actual CRT idempotents gives a full equivariant map \(\pi:M\to E\) with \(\pi\eta=I\); its kernel is retained. This is also obtainable from the invariant-packet version by its specified symmetrization, but no additional symmetrization is needed for the displayed full construction.

Consequently \(j_E=\pi J^{(k)}\) on this source satisfies

\[
j_Er_N=I_E,\qquad j_ED^{(k)}=Aj_E,
\qquad j_Ed=0,
\quad r_N=\mathcal VR_N.
\]

Thus \(D_t^{(k)}=D^{(k)}+t r_Ne_0e_{q-1}^Tj_E\) is a continuous finite-rank perturbation on the stated source topology, with

\[
j_ED_t^{(k)}=A(t)j_E,\qquad
D_t^{(k)}r_N-r_NA(t)=D^{(k)}r_N-r_NA=dK_N.
\]

It leaves the original differential on boundaries unchanged. The same perturbation need not be bounded on the unweighted Hilbert completion: the proved jet-graph calculation (JT2)–(JT4) retains its nonclosability there. No such extension is used by the exponential packet. Its metric statements concern the original finite-dimensional representatives, with \(G_N\) unchanged.

## 5. Nonproper periods: convergence, differentiation and invertibility

Fix \(u\ne0\), a specified argument of \(u\), \(d=q+1\), and

\[
\theta_j=(\arg u+\pi)/d+2\pi j/d,\qquad
\Gamma_j=-\ell_0+\ell_j,\quad 1\le j\le q,
\]

where \(\ell_j\) points from zero to infinity along \(\theta_j\). On a compact set of lower coefficients and \(t\), choose \(C\) bounding the absolute sum of their contributions to \(\Phi_t/u\). For \(r\ge1\), their absolute value is at most \(Cr^{d-1}\), while the leading real part is exactly \(-r^d/(d|u|)\). For \(r\ge \max(1,2d|u|C)\),

\[
\Re(\Phi_t(re^{i\theta_j})/u)\le-r^d/(2d|u|).
\]

Every fixed finite parameter derivative only inserts a polynomial factor in \(S\), so an integrable majorant \(C'(1+r)^M e^{-r^d/(2d|u|)}\) controls that derivative uniformly on the compact parameter set. This proves absolute convergence, holomorphic dependence on all lower coefficients and \(t\), and differentiation under the integral. It explicitly treats the infinite tails; finite-dimensional rank constancy by itself is not used as a nonproper base-change theorem.

Truncate both rays at radius \(R\). Integration of the exact derivative \(u\,d(e^{\Phi_t/u}P)\) has two origin contributions with opposite signs and two outer contributions. The origin values cancel exactly; the outer values tend to zero by the bound above. Hence each integral vanishes on \(L(R[S])\), and defines the claimed period map on the same quotient.

At the monomial parameter, radial substitution gives the complete entries

\[
\Pi_{jb}^{\mathrm{mon}}=
\frac{(d|u|)^{(b+1)/d}}d\Gamma((b+1)/d)
e^{i(b+1)\theta_0}(e^{2\pi ij(b+1)/d}-1).
\]

A column dependence produces a degree-at-most-\(q\) polynomial
\(\sum_{l=1}^q a_l(z^l-1)\) vanishing at all \(d=q+1\) distinct roots of unity, including one. It is zero, and comparison of its coefficients gives all \(a_l=0\). The initial determinant is nonzero, including every Gamma factor and phase.

The coefficient connection formulas give \(\partial_{c_a}\Pi=\Pi B_a\) and \(\partial_t\Pi=-\Pi A(t)/u\). Along any fixed straight coefficient path the matrix \(B\) is continuous. The adjugate determinant formula gives \(y'=(\operatorname{Tr}B)y\) even at a hypothetical singular point; its solution is \(y(0)\exp\int\operatorname{Tr}B\). It never vanishes. This proves the isomorphism at every lower coefficient and every \(t\), including every repeated critical root. No assumption of independent vanishing cycles is hidden in the argument.

For varying \(u\), these statements are understood on a local argument sector; fixed nearby decay rays give the same local holomorphic comparison by entire contour deformation. A single global holomorphic choice of \(\arg u\) is not asserted.

On the source, \(\Pi j_E:r_N(E)\to\mathbb C^q\) has inverse \(r_N\Pi^{-1}\). Its observation on all admitted source vectors has exact kernel \(\ker j_E\). For a \(t\)-independent source vector \(F\),

\[
-u\partial_t(\Pi j_EF)=\Pi A(t)j_EF=\Pi j_ED_t^{(k)}F.
\]

The existing original theta primitive vanishes under \(j_E\); it is not inferred to be zero as a source function.

## 6. Bilinear residue duality and the retained metric

For degree-below-\(q\) representatives, the form is the coefficient of \(S^{-1}\) in \(PQ/(\chi-t)\), equal to the sum of finite residues with that sign. The difference between the denominators at \(t\) and zero is \(t/(\chi(\chi-t))\). Multiplying by \(PQ\) gives order at most \(S^{-2}\), so this coefficient is unchanged. The residue Gram \(\mathsf S\) therefore is independent of \(t\). Its entries for \(a+b<q-1\) vanish and those for \(a+b=q-1\) equal one, giving determinant \((-1)^{q(q-1)/2}\).

Ordinary multiplication by \(S\) on \(\mathbb C[S]/(\chi-t)\), whose matrix is exactly \(A(t)\), is self-adjoint for this bilinear form. Hence \(A(t)^T\mathsf S=\mathsf S A(t)\). Expanding the derivative proves the horizontal pairing between the \(u\) and \(-u\) \(t\)-connections. This gives the exact linear-dual map, without substituting Hermitian conjugation. On the original fibre the separately retained dagger map may be composed with it.

For a root of multiplicity \(\ell_\lambda\), \(\chi'/\chi=\ell_\lambda/(S-\lambda)+\) a holomorphic function. The corresponding residue of \(f^{\dagger_k}v\chi'/\chi\) is \(\ell_\lambda f^{\dagger_k}(\lambda)v(\lambda)\), equal to the local multiplication trace because the remaining Taylor terms act nilpotently. This proves the Jacobian contraction with every multiplicity retained. The full tensor trace still includes the complementary module of \(\eta\).

The chosen coordinate Gram on periods is explicitly \(I_q\); thus \(H_\Pi=\Pi^*\Pi\) and \(B_N^{\rm per}=G_N^{-1}H_\Pi\). Direct multiplication gives \((B_N^{\rm per})^*G_N=G_NB_N^{\rm per}=H_\Pi\), so it is positive self-adjoint in the original \(G_N\). At the same \((u,t)\),

\[
\frac{\det B_j^{\rm per}}{\det B_i^{\rm per}}
=\frac{\det G_i}{\det G_j}=\frac{V_i}{V_j}.
\]

The auxiliary period Gram cancels exactly from this ratio. The new determinant evaluation in the separate full extension makes that cancellation explicit even before taking the ratio; it supplies an exact scalar formula, not an unproved estimate of the original changing metrics.

## 7. Infinity and the finite-field application

Use the actual finitely generated coefficient ring \(R_0\subset\mathbb C\) containing all \(c_a\) and \(1/(q+1)!\). Every specified specialization to \(\mathbb F_Q\) of characteristic \(p>q+1\), together with \(u\ne0\), gives

\[
Y^p-Y=(\Phi(S)-tS)/u.
\]

At \(w=1/S\), the right side is \(w^{-d}b\), where

\[
b=\frac1u\left(\frac1d+
\sum_{a=0}^{q-1}\frac{c_a}{a+1}w^{q-a}-tw^q\right),
\qquad b(0)=1/(du).
\]

Restrict to the neighborhood where \(b\) is a unit. The algebra defined by \(bv^d=1\) is finite free of rank \(d\), since its equivalent equation is the monic \(v^d-b^{-1}=0\). Its derivative \(dbv^{d-1}\) has inverse \(v/d\), so the cover is finite étale. The function \(x_\infty=wv\) has invertible relative derivative at the boundary and is an étale coordinate after a further neighborhood restriction. Precisely,

\[
x_\infty^{-d}=w^{-d}v^{-d}=w^{-d}b=(\Phi-tS)/u.
\]

The retained cover action is \(v\mapsto\zeta v\), \(\zeta^d=1\). On the affine part the Artin–Schreier cover is finite étale and its eigensheaf lisse. At infinity the displayed relative coordinate pulls it back from the fixed pole model \(x_\infty^{-d}\). This is the explicit local-acyclicity mechanism of Lemma 3.7.3, including the nonproper boundary before compactification and proper pushforward. Its domain remains \(u\ne0\).

The leading degree is \(d=q+1\), prime to \(p\); its nonzero leading homogeneous form in one variable has empty projective zero locus in \(\mathbb P^0\), which is smooth. The displayed Deligne theorem (3.7.2.3) therefore gives concentration in degree one, rank \(q\), and pure weight one for the finite-field cohomology. The parameter map into the universal polynomial space lands in that stated open, so its lisse higher compact-support sheaf pulls back to the family here. These are applications of the precise historical theorem, not finite-checker consequences.

The two realizations are the specified maps from \(R_0\) to \(\mathbb C\) and to \(\mathbb F_Q\). Their operators are retained separately with those base maps. The additional translation calculation described below gives a further exact comparison rather than stopping at nonidentity.

## 8. Check of the parallel translation bridge

For a fixed auxiliary \(a\), put \(\chi_a(S)=\chi(S-a)\),
\(\Phi_a(S)=\Phi(S-a)-\Phi(-a)\), and \(T_aP(X)=P(X+a)\).
Direct substitution gives \(T_aL_a=LT_a\) and the special-fibre relation
\(T_aA_aT_a^{-1}=A+aI\). The exact zero constant of the primitive is retained.

At \(u\ne0\), define

\[
f_a=\exp((-\Phi(-a)-ta)/u).
\]

Then \(T_a\nabla_t^aT_a^{-1}=\nabla_t-a/u\), and the correctly directed horizontal map is **\(f_aT_a\) from the translated connection to the original one**:

\[
\nabla_t(f_aT_aP)=f_aT_a(\nabla_t^aP),
\]

because \(\partial_tf_a=-af_a/u\). The Pascal coefficient matrix of \(T_a\) has determinant one. In the periods, translate the original rays by \(-a\); the origin cancellation becomes a cancellation at \(-a\). The remaining rays can be moved to the original rays by the integral of an entire form. At radius \(R\), the connecting pieces have angular deviation \(O(1/R)\), so their leading exponent remains at most \(-cR^d\) for some fixed \(c>0\), while the lower-degree terms are \(O(R^{d-1})\). Their polynomial factors and at most polynomial lengths are dominated by that exponential decay. The connecting integrals vanish. Consequently the retained orientations give

\[
\Pi_a=f_a\Pi C_a,\qquad \det C_a=1.
\]

In a finite-field specialization that also contains \(a\), the substitution is the affine automorphism \(S=X+a\). The new potential differs by the constant \(\kappa_a/u\), \(\kappa_a=-\Phi(-a)-ta\). Addition of Artin–Schreier potentials gives the precise eigensheaf tensor factor \(\mathcal L_\psi(\kappa_a/u)\). With Deligne's convention that its trace function is \(\psi(\operatorname{Tr}Q)\), the constant Frobenius scalar is \(\psi(\operatorname{Tr}(\kappa_a/u))\), a root of unity. Its absolute value is one while the special coefficient shifts by \(aI\). This exact family of comparisons preserves the original \(a=0\) source and explains which additional original-source information the RH estimate must use.

## 9. Actual finite verification and limits

Every one of the 51 entries in the delivered manifest was verified by length and SHA-256. The unchanged new checker, SHA-256 `3a4ecfe77cca69404d08fe95de02887bd7128355be18f1f54cf2b7eb32267d0b`, was executed under Python 3.13.9 and SymPy 1.13.1 normally and with `-O`. Each run passed 22 named finite methods, with zero errors and failures. All three specified false controls were rejected with exit one in both modes. These are eight actual jobs with full argv, runtime, source pin, exit and raw output in `work/deligne_exponential_replay_20260913`. The delivered predecessor's 23-method logs remain historical supplied evidence; that predecessor was not rerun in this intake.

The 43-file add-only patch was applied in an isolated local repository and all resulting files compared with the original delivered bytes. A first attempt used the machine's default worktree line-ending conversion and therefore changed LF to CRLF. That attempt is preserved separately. The successful byte-exact application used `git -c core.autocrlf=false apply` only for that command; all 43 files agree exactly. There are no source formula edits or remote changes.

The finite suite supplements the written proofs. It does not certify the improper integrals, Deligne's theorem, an RH conclusion, or a uniform arithmetic endpoint estimate. The explicit convergence proof, exact source maps, and deterministic determinant extension are the mathematical evidence for their own stated claims.
