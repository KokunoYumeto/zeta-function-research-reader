# Independent mathematical review of the original relation-moment construction

Date: 2026-09-13. Scope: complete mathematical reading of every section of the delivered `NOTE.tex` and `RESEARCH_NOTE.md`, followed by independent derivation of the finite identities. This review makes no change to either source, the cumulative paper, a frozen edition, main, or Zenodo. The package's regression programs were not run by this reviewer; the intake owner is executing them separately. Two direct symbolic matrix reconstructions below are independent calculations, not a rerun of that test suite.

Source directory: `workspace:/output/split_zero_rh_tandem_2026-09-12/sources/web_relation_moment_delivery/Tau_Relation_Moment_Control`.

Exact sources read in full:

| File | Bytes | SHA-256 |
|---|---:|---|
| `NOTE.tex` | 30033 | `f3dd07e247d7b3785d15520c4e9e91f0223e19b21ee53ab3279ab97eb6e1df71` |
| `RESEARCH_NOTE.md` | 26244 | `17e14c11ca60906604f66ddf9e6a758412a16143d5742736f3a5708658270795` |

## Findings and exact corrections

The new finite mathematical results pass this independent derivation: the cost endomorphism and its original-metric action defect; the two traces and exterior-area map; the sharp determinant estimate; its complete positive integral remainder; the third-trace improvement; the radical-free area estimate; the error-aware polynomial estimate; coordinate and mass propagation; and both literal Gaussian calibrations. The finite composition with the consecutive-window result is algebraically valid. The inherited PR #25 analytic estimates and its first-degree theorem are assigned to the root's separate source validation; this review does not certify them merely from their statement here.

Two source corrections are required, with two additional precision clarifications:

1. **Zero cost is a zero log-ratio, not a zero volume.** `RESEARCH_NOTE.md:330` and `NOTE.tex:499` say that if `t_1=0`, “the volume is zero.” Replace precisely with: “If \(t_1=0\), positivity gives \(Z=0\), hence \(V_i/V_j=1\), \(V_i=V_j>0\), and \(\log(V_i/V_j)=0\).” For positive dimension, each admitted \(G_N\) is positive definite, so \(V_N\) cannot be zero. For dimension zero the empty determinant is one. This correction does not alter any displayed determinant estimate.

2. **The window estimate needs a nonempty window.** The cost construction correctly permits \(i=j\) in section 3. Section 8, beginning at `RESEARCH_NOTE.md:408` and `NOTE.tex:605`, must explicitly require \(q-1\le i<j\), equivalently \(r=j-i\ge1\), before taking the minimum and the powers \(1/(2r)\) in (26)–(27). At \(i=j\), equations (5)–(25) retain their defined cases, \(F\) has zero-dimensional domain, \(Z=0\), and the volume ratio is one; the empty-window minimum is not defined by this note.

3. In section 5, the **complete remainder** in (21), rather than its bare rational integrand, is strictly positive away from \(x=a,b\). The rational integrand itself is positive also at those endpoints. Replace “the integrand in (21) is strictly positive except at \(x=a,b\)” by “the remainder in (21) is strictly positive for \(x\in[0,a]\setminus\{a,b\}\).” The stated equality characterization is correct.

4. Before (30), make “positive lower budget” literal: \(2q\log(D_hk)>0\), equivalently \(D_hk>1\), implies \(t_1>0\). The number \((D_hk)^{2q}\) in (29) is positive for every \(D_hk>0\); its positivity alone does not imply \(t_1>0\). Equation (30) remains valid whenever the actual \(t_1>0\), even if its right side is negative. The exact finite version with the actual volume cost, proved below, avoids this possible ambiguity.

The raw files should remain intact as delivered. These corrections belong in the integration adapter or a separately identified correction note.

## 1. Source setting, support square, and scope of inherited claims

For a ring inclusion \(j:\mathbb Z\to\mathbb C\), the maps on the source square are explicitly
\[
G(j)(\tau)=\tau,\qquad G(j)(n^\bullet)=j(n)^\bullet,
\quad p_R(\tau)=0_R,\quad p_R(r^\bullet)=r.
\]
On \(\tau\), both composites in (3) give zero; on \(n^\bullet\), both give \(j(n)\). Thus the square commutes without identifying \(\tau\) and \(e_R=0_R^\bullet\). Its represented scalar observation is a map on the split object, not an identification of its two zero-amplitude elements.

The maps \(\mathcal V,\eta,J^{(k)},q^{(k)},\sigma_h^{\otimes k}\), the original theta complex, and the arithmetic density are cited inherited constructions. For this finite review their use is through the explicitly displayed commuting maps (4), not through an unproved assertion about a new metric. In particular, the polynomial relation calculations below prove membership in \(\ker\pi_\chi\) with the full original \(\chi\); applying each displayed composite therefore gives zero in its stated linear target. Applying the represented-element lift of that zero linear observation gives the receiving \(e\), not \(\tau\). This is the exact map needed to retain the source relation while describing its quotient observation.

The source makes no claim to prove a uniform bound for its original growing-degree traces. Its small-o example in section 8 remains a stated implication with an unproved arithmetic premise; it cannot be imported into the cumulative paper as a proved arithmetic growth estimate. The classical attribution and reported PR status are source attributions; the self-contained finite proof below does not rely on an unread theorem from the cited literature or on CI status.

## 2. Original quotient and least-norm representative

Write \(\mathcal P_N\) for the degree-at-most-\(N\) polynomial coordinate space in the actual monic orthogonal basis, with Gram \(O_N=\operatorname{diag}(\omega_0,\ldots,\omega_N)\), and retain the map
\[
B_N:\mathcal P_N\longrightarrow E=\mathbb C[S]/(\chi),\qquad
(c_n)\longmapsto\sum_{n=0}^N c_n[p_n]_\chi.
\]
If \(N\ge q-1\), the first \(q\) monic polynomials form a triangular basis modulo monic \(\chi\), so \(B_N\) is surjective. Consequently, for every nonzero coefficient vector \(v\),
\[
v^*K_Nv=(B_N^*v)^*O_N^{-1}(B_N^*v)>0.
\]
This proves that \(K_N\), \(G_N=K_N^{-1}\), and \(R_N=O_N^{-1}B_N^*G_N\) exist in the admitted range. Direct multiplication gives
\[
B_NR_N=I_E,\qquad R_N^*O_NR_N=G_N.
\]
For \(z\in\ker B_N\),
\[
z^*O_NR_Nv=z^*B_N^*G_Nv=0.
\]
Every representative of \(v\) is therefore \(R_Nv+z\), with the exact original-norm identity
\[
\|R_Nv+z\|_{O_N}^2=v^*G_Nv+\|z\|_{O_N}^2.
\]
No mass has been divided out; \(\omega_0=\mu_h^k\) remains in these Grams. The fixed realization \(\mathcal V\) sends these polynomial coordinates to the corresponding original test functions.

## 3. Typed inverse restriction, source cost, and arithmetic action

Let \(q-1\le i\le j\). Put \(U=(\mathbb C^{j-i},\Omega)\), \(E_i=(E,G_i)\), and \(E_j=(E,G_j)\). The newly admitted column map is
\[
F:U\to E_i,\qquad F=(b_{i+1},\ldots,b_j),\qquad
D=F\Omega^{-1}F^*=K_j-K_i\succeq0.
\]
The forward coefficient identity \(I:E_i\to E_j\) has adjoint \(T=G_i^{-1}G_j=K_iG_j:E_j\to E_i\), because \(\langle Iv,w\rangle_{G_j}=\langle v,Tw\rangle_{G_i}\). The endomorphism \(Q=TI\) is positive self-adjoint on \(E_i\). Its inverse is \(K_jG_i\), so
\[
Z=Q^{-1}-I_E=(K_j-K_i)G_i=D G_i.
\]
Here \(G_iZ=G_iDG_i\succeq0\); hence \(Z\) is positive self-adjoint in the original \(G_i\) metric. Its eigenvalues \(\lambda_\alpha\) are nonnegative, and the same eigenvectors give
\[
Q=(I_E+Z)^{-1},\qquad g_\alpha=(1+\lambda_\alpha)^{-1}.
\]
The original determinant ratio is exactly
\[
\det(I_E+Z)=\det(K_jG_i)=\frac{\det K_j}{\det K_i}
=\frac{V_i}{V_j}.
\]
The adjoint of \(F\) is \(F^\dagger=\Omega^{-1}F^*G_i\), so \(Z=FF^\dagger\). These statements do not require making the coefficient matrix of \(Z\) Euclidean Hermitian.

For the action, retain \(A_i=A_j=M_S\) in the fixed coordinate presentation, and use \(I\) to type its transport. Write
\[
\mathsf H_N=K_NA^*G_N+A-kI_E.
\]
Direct multiplication, rather than an action-invariance assumption, gives
\[
\mathsf H_iQ-Q\widehat{\mathsf H}_j
 =K_iA^*G_j+AK_iG_j-kK_iG_j
  -K_iA^*G_j-K_iG_jA+kK_iG_j
 =[A,Q].
\]
Multiplying the identity \([A,Q^{-1}]=-Q^{-1}[A,Q]Q^{-1}\) yields
\[
[A,Z]=\widehat{\mathsf H}_j(I_E+Z)-(I_E+Z)\mathsf H_i.
\]
This proves (10) with exactly its order and signs. It also describes the action when a cost eigenspace is not invariant under \(A\).

## 4. Relation map, both traces, exterior area, and its precise spectrum bridge

Let \(L:\mathcal P_i\to\mathcal P_j\) pad the old coordinates and \(T_{\rm new}:U\to\mathcal P_j\) insert the new coordinates. Their ranges are orthogonal in \(O_j\), with \(L^*O_jL=O_i\) and \(T_{\rm new}^*O_jT_{\rm new}=\Omega\). Set
\[
\Phi=R_iF:U\to\mathcal P_i,\qquad
\mathfrak b=T_{\rm new}-LR_iF:U\to\mathcal P_j.
\]
Then
\[
B_j\mathfrak b=F-B_iR_iF=0,
\qquad
\mathfrak b^*O_j\mathfrak b=\Omega+F^*G_iF.
\]
The \(n\)-th relation column is exactly the polynomial
\[
P_n(S)=p_n(S)-\sum_{\ell=0}^{i}(R_ib_n)_\ell p_\ell(S)
=\chi(S)U_n(S),\qquad i<n\le j,
\]
where \(U_n\) is the unique monic polynomial of degree \(n-q\). Divisibility follows from its vanishing remainder, retaining every multiplicity in \(\chi\). Thus its actual source image under \(\mathcal V\) is retained, while (4) maps it to zero in the specified arithmetic and coequalizer targets.

The source map \(\mathfrak b\) is injective because its new-coordinate projection is the identity on \(U\). Its range is orthogonal to \(L\ker B_i\): the old representative components are orthogonal to \(\ker B_i\), and the new columns are orthogonal to \(\mathcal P_i\). Dimension counting or polynomial triangularity then proves the exact orthogonal relation decomposition
\[
\ker B_j=L\ker B_i\ \mathbin{\oplus^{\perp}}\ \operatorname{im}\mathfrak b.
\]

The old correction map has
\[
M:=\Phi^\dagger\Phi=F^\dagger F=\Omega^{-1}F^*G_iF:U\to U,
\qquad \mathfrak b^\dagger\mathfrak b=I_U+M.
\]
Thus cyclicity gives
\[
t_1=\operatorname{Tr}(FF^\dagger)=\operatorname{Tr}M
=\sum_n\frac{b_n^*G_ib_n}{\omega_n}=\|\Phi\|_{\rm HS}^2,
\]
\[
t_2=\operatorname{Tr}M^2
=\sum_{n,m}\frac{(b_n^*G_ib_m)(b_m^*G_ib_n)}{\omega_n\omega_m}
=\sum_{n,m}\frac{|b_n^*G_ib_m|^2}{\omega_n\omega_m}.
\]
In particular, \(t_2=\|\Phi^\dagger\Phi\|_{\rm HS}^2\), while the second exterior coefficient is a different, explicitly related expression:
\[
\mathcal A_2=\frac{t_1^2-t_2}{2}
=\sum_{n<m}\frac{\|R_ib_n\|_{O_i}^2\|R_ib_m\|_{O_i}^2
-|\langle R_ib_n,R_ib_m\rangle_{O_i}|^2}{\omega_n\omega_m}.
\]
Equip \(\bigwedge^2U\) and \(\bigwedge^2\mathcal P_i\) with determinant Grams on the unscaled exterior quotient basis. The basis wedge \(e_n\wedge e_m\) has squared norm \(\omega_n\omega_m\), and its image has the numerator just displayed. Summing the quotient of these squared norms proves exactly
\[
\mathcal A_2=\|\bigwedge^2\Phi\|_{\rm HS}^2.
\]
For the unscaled alternating-tensor realization \(u\wedge v\mapsto u\otimes v-v\otimes u\), both domain and codomain wedge Grams acquire the factor \(2!\); its cancellation in this map norm is the stated typed passage, not an omitted factorial.

There is an exact relation between the cost and the relation Gram even when their dimensions differ. For \(\lambda>0\),
\[
F^\dagger:\ker(Z-\lambda I_E)\longrightarrow\ker(M-\lambda I_U),
\quad
\lambda^{-1}F:\ker(M-\lambda I_U)\longrightarrow\ker(Z-\lambda I_E)
\]
are inverse linear maps. The first multiplies squared norms by \(\lambda\); hence \(\lambda^{-1/2}F^\dagger\) is the exact isometry between these original metric eigenspaces, with inverse \(\lambda^{-1/2}F\). At zero,
\[
\ker Z=\ker F^\dagger=(\operatorname{im}F)^{\perp_{G_i}},
\qquad \ker M=\ker F.
\]
These kernels remain present. This proves the nonzero spectral correspondence and, including the unit contributions of both zero eigenspaces,
\[
\det_E(I_E+Z)=\det_U(I_U+M)
=\frac{\det(\mathfrak b^*O_j\mathfrak b)}{\det\Omega}.
\]
In particular, a vanishing exterior image of an admitted pair has a zero numerical area and a represented \(e\)-valued scalar observation; the admitted pair's domain vector is still in \(\bigwedge^2U\). An index pair outside this exterior indexing object is not a domain element. The explicit map \(\bigwedge^2\Phi\), followed by squared norm and represented scalar lift, relates those presentations without collapsing them.

## 5. Spectral cap, optimal determinant estimate, and all equality cases

Assume \(q\ge2\). For the actual nonnegative spectrum,
\[
t_1^2/q\le t_2\le t_1^2,
\qquad d=\sqrt{(qt_2-t_1^2)/(q-1)}\in[0,t_1].
\]
The first inequality is Cauchy–Schwarz; the second follows from \(t_1^2-t_2=2\sum_{\alpha<\beta}\lambda_\alpha\lambda_\beta\ge0\). Consequently
\[
a=(t_1+(q-1)d)/q,\quad b=(t_1-d)/q,
\quad 0\le b\le a,
\]
and direct expansion gives \(a+(q-1)b=t_1\), \(a^2+(q-1)b^2=t_2\). For an actual eigenvalue \(x\), Cauchy–Schwarz on the other \(q-1\) coordinates gives
\[
qx^2-2t_1x+t_1^2-(q-1)t_2\le0.
\]
The upper root is
\[
\frac{t_1+\sqrt{(q-1)(qt_2-t_1^2)}}q=a.
\]
Thus \(0\le x\le a\), and \(Q=(I_E+Z)^{-1}\succeq(1+a)^{-1}I_E\) in \(G_i\). This cap is calculated from these finite traces; it is not an independent uniform arithmetic assertion.

For \(a>b\), put
\[
P_{a,b}(x)=\log(1+b)+\frac{x-b}{1+b}+c_{a,b}(x-b)^2,
\quad c_{a,b}=\frac{\log(1+a)-\log(1+b)-(a-b)/(1+b)}{(a-b)^2}<0.
\]
Strict concavity of \(\log\) gives the indicated sign. To establish the full remainder without an unspecified interpolation point, for fixed \(s\ge1\) define \(f_s(x)=s^{-1}-(s+x)^{-1}\). Its Hermite interpolant at \(b,b,a\) is
\[
H_s(x)=f_s(b)+\frac{x-b}{(s+b)^2}
-\frac{(x-b)^2}{(s+b)^2(s+a)}.
\]
Direct common-denominator multiplication gives
\[
H_s(x)-f_s(x)
=\frac{(a-x)(x-b)^2}{(s+x)(s+b)^2(s+a)}.
\]
The terms are integrable on \([1,\infty)\); in particular the remainder integrand is \(O(s^{-4})\). Integrating \(f_s(x)\) gives \(\log(1+x)\), while integration of its interpolation values and derivative gives \(P_{a,b}(x)\). Therefore
\[
P_{a,b}(x)-\log(1+x)
=(a-x)(x-b)^2\int_1^\infty\frac{ds}{(s+x)(s+b)^2(s+a)}.
\]
This proves (21) with its exact sign. The right side is nonnegative on the proven spectral interval, and is positive away from the two interpolation nodes. Since the trace of a quadratic depends only on \(q,t_1,t_2\),
\[
\operatorname{Tr}P_{a,b}(Z)=P_{a,b}(a)+(q-1)P_{a,b}(b)
=\log(1+a)+(q-1)\log(1+b)=U_2.
\]
Summing the remainder yields \(\log\det(I_E+Z)\le U_2\). If equality holds and \(a>b\), every actual eigenvalue belongs to \(\{a,b\}\). If \(m\) is the multiplicity of \(a\), the trace identity is
\[
ma+(q-m)b=a+(q-1)b,
\]
so \((m-1)(a-b)=0\) and \(m=1\). Conversely that spectrum gives equality. It realizes the two prescribed moments and is positive, so the bound is optimal given only dimension and those two traces. Additional constraints on rank or on arithmetic realizability have not been included in that optimization claim.

If \(a=b\), Cauchy–Schwarz equality forces \(Z=bI_E\) as a self-adjoint endomorphism, and the upper bound is exact without the divided expression for \(c_{a,b}\). If \(t_1=0\), all eigenvalues are zero, \(Z=0\), the ratio is one, and its logarithm is zero. If \(q=1\), the exact ratio is \(1+t_1\); (16) is not formed. If \(q=0\), the empty determinant gives ratio one and log-ratio zero, and no positive-dimensional matrix inverse or division by \(q-1\) is introduced. If \(i=j\), the map \(F\) has zero-dimensional domain and the same zero-cost conclusion applies.

## 6. Exact positive loss and third-trace improvement

All powers and resolvents below are functional calculus of the same original-metric self-adjoint \(Z\). For each spectral coordinate,
\[
(a-x)(x-b)^2=-x^3+(a+2b)x^2-(2ab+b^2)x+ab^2\ge0.
\]
Summing proves
\[
C_3=-t_3+(a+2b)t_2-(2ab+b^2)t_1+qab^2\ge0.
\]
The finite spectral sum may be interchanged with the convergent integral, giving precisely
\[
U_2-\log\det(I_E+Z)
=\int_1^\infty\frac{\operatorname{Tr}((aI_E-Z)(Z-bI_E)^2(sI_E+Z)^{-1})}
{(s+b)^2(s+a)}\,ds.
\]
For \(0\le x,b\le a\), the denominator \((s+x)(s+b)^2(s+a)\) is at most \((s+a)^4\). Consequently
\[
U_2-\log\det(I_E+Z)
\ge C_3\int_1^\infty(s+a)^{-4}\,ds
=\frac{C_3}{3(1+a)^3}.
\]
This proves (23). It extends through the degenerate equal-spectrum case because then \(C_3=0\) and the loss is zero. Strict concavity of \(\log\), applied to \(a,b,\ldots,b\), gives
\[
U_2\le q\log(1+t_1/q),
\]
with equality for \(q\ge2\) precisely when \(a=b\). There is no assumption about commutation with \(A\); that interaction is already computed in (10).

## 7. Exterior-area certificate and the exact finite lower comparison

From the two exact moments of \(a,b,\ldots,b\),
\[
\mathcal A_2=(q-1)ab+\frac{(q-1)(q-2)}2b^2
=(q-1)b(t_1-qb/2).
\]
For \(q\ge2\), \(t_1>0\), and \(0\le b\le t_1/q\), the last factor belongs to \([t_1/2,t_1]\). Hence
\[
\frac{\mathcal A_2}{(q-1)t_1}\le b\le
\frac{2\mathcal A_2}{(q-1)t_1},\qquad a\le t_1,
\]
which proves (25). Moreover, \(\mathcal A_2=\sum_{\alpha<\beta}\lambda_\alpha\lambda_\beta=0\) and \(t_1>0\) imply exactly one positive eigenvalue. Thus (19) is exact in that case, with ratio \(1+t_1\), independently of the number of retained domain coordinates or support labels.

Let \(\mathcal C_{i,j}=\log(V_i/V_j)\) be the actual finite volume cost. Equation (25) itself proves the completely finite bound
\[
\log\left(1+\frac{2\mathcal A_2}{(q-1)t_1}\right)
\ge\frac{\mathcal C_{i,j}-\log(1+t_1)}{q-1},
\quad q\ge2,\ t_1>0.
\]
Substituting a separately established lower estimate \(\mathcal C_{i,j}\ge2q\log(D_hk)\) gives exactly (30). If \(D_hk>1\), that lower estimate forces \(\mathcal C_{i,j}>0\), so \(Z\ne0\) and \(t_1>0\), justifying its division. A negative right side retains its valid finite meaning.

The claimed example with a small-o upper growth premise follows by taking logs of (30), dividing by \(\log k\), and retaining
\[
\frac{2q}{q-1}\left(1+\frac{\log D_h}{\log k}\right)
-\frac{\log(1+t_1)}{(q-1)\log k}.
\]
For the displayed quartet degree \(q_k\to\infty\), this has lower limit two if the displayed small-o premise is proved. No such arithmetic premise is proved by the present source or by this review; the valid finite inequality above is the unconditional calculation made with its actual matrices.

## 8. Consecutive-window composition and retained analytic scope

For a nonempty admitted window \(q-1\le i<j\), \(r=j-i\ge1\), the source cites its inherited inequality
\[
\min_{i\le N<j}\epsilon_N\le
(\omega_j/\omega_i)^{1/(2r)}(V_i/V_j)^{1/(2r)}.
\]
Since the determinant bound (1) has positive sides, raising it to the positive exponent \(1/(2r)\) preserves its order. Substitution proves (27) without selecting a different representative or metric. For each endpoint block, \(r=q\), and substitution of the inherited original-norm envelope yields (28). A verified off-line lower bound for each selected \(\epsilon_N\) then composes in the stated direction with that upper bound.

The two displayed lower per-block budgets in (2), their first-admissible-degree justification, the existence and exact value of the norm-envelope constants, and the threshold-four conclusion depend on the separately identified PR #25 full source. Their validity is not established solely by this local note's statement. The root owns that full source audit. This review verifies that once the actual cited inequalities are supplied, every exponent and determinant direction in (27)–(30) is correct. No conditional substitute for that missing review has been inserted into the source.

## 9. Enclosure polynomial, moment order, coordinate map, and mass

For nonnegative eigenvalues, every \(\lambda_\alpha\le t_1\le t_1^+\). Therefore any rational \(A_0\ge t_1^+\) is a cap. Choose rational \(0\le B_0<A_0\); if the trace enclosure proves zero cost, use the explicit zero case instead, or choose a strictly positive cap. The scalar Hermite identity applies to \(A_0,B_0\) on \([0,A_0]\) even though these nodes are not fitted to the exact two traces. Summation gives
\[
\log\det(I_E+Z)\le q\log(1+B_0)+\frac{t_1-qB_0}{1+B_0}
+c_{A_0,B_0}(t_2-2B_0t_1+qB_0^2).
\]
This is (31); all coefficients are formed from rational arithmetic and logarithms of positive rationals. Interval evaluation enclosing every addition, multiplication, and signed coefficient therefore yields an upper enclosure, even though repeated appearances of a trace can overestimate the interval width.

For \(y\in[1,2)\), \(z=(y-1)/(y+1)\in[0,1/3)\), and integer \(M\ge0\), the retained tail is
\[
R_M=2\sum_{n=M}^{\infty}\frac{z^{2n+1}}{2n+1}
\le\frac{2z^{2M+1}}{2M+1}\sum_{r=0}^{\infty}z^{2r}
=\frac{2z^{2M+1}}{(2M+1)(1-z^2)}.
\]
It is nonnegative. The same convergent expression applies to \(\log2\) at \(z=1/3\). For rational \(x\ge1\), retaining \(x=2^ey\) gives \(\log x=e\log2+\log y\); for \(0<x<1\), \(\log x=-\log(1/x)\) reverses the enclosing interval endpoints. Thus the analytic enclosure formula is correct without treating the source's printed decimals as certificates. This review does not claim that the source checker has executed; intake owns that execution.

Orthogonalization of monomials through degree \(j\) uses Gram entries from moments of degree at most \(2j\), retaining the line coordinate \(S=k/2+iu\), its conjugation, and all binomial factors. Thus its norm and monic coefficient claims have the stated moment cutoff. The endpoint block reaching \(j=2q\) can require moments through \(4q\); this construction does not itself replace them by lower moments.

For an invertible fixed quotient-coordinate map \(C:E\to E'\), direct substitution yields
\[
B_N'=CB_N,\quad K_N'=CK_NC^*,\quad
G_N'=C^{-*}G_NC^{-1},\quad R_N'=R_NC^{-1},\quad F'=CF.
\]
Hence \(Z'=CZC^{-1}\), while \(F'^*G_i'F'=F^*G_iF\). This proves trace and exterior-area invariance through the specified coordinate map, including any raw-derivative factorials in \(C\). The coordinate volumes themselves obey \(V_N'=|\det C|^{-2}V_N\); the original ratio cancels this identical factor at its two endpoints. A rectangular injection \(\eta\) is not used as this invertible square map.

If the original measure is multiplied by a literal \(c>0\), the monic orthogonal polynomials remain the same: the defining orthogonality equations acquire the common nonzero multiplier \(c\). Their norms become \(c\omega_n\). Thus
\[
O_N'=cO_N,\quad\Omega'=c\Omega,\quad
K_N'=c^{-1}K_N,\quad G_N'=cG_N,\quad R_N'=R_N.
\]
Consequently \(Z'=Z\), \(t_1,t_2,\mathcal A_2\) remain exactly the same, while \(V_N'=c^qV_N\). The ratio cancels the explicit \(c^q\) factors. This is the proved mass transport, not a choice to reset the arithmetic mass.

## 10. Literal Gaussian fixtures, including the complete q=3 matrices

Keep \(S=1+ix\), variance one, Gaussian mass seven, and original quotient basis \(1,S,\ldots,S^{q-1}\). For the probabilists' Gaussian polynomials \(H_n\), the original monic source polynomials obey \(p_n(1+ix)=i^nH_n(x)\); the displayed recurrence follows with its plus sign, and the norm is \(7n!\). In particular the phase \(i^n\) has not changed the original mass or recurrence.

For \(q=2\), direct remainder construction gives
\[
K_1=\begin{pmatrix}2/7&-1/7\\-1/7&1/7\end{pmatrix},\quad
K_3=\begin{pmatrix}4/7&-5/14\\-5/14&5/14\end{pmatrix},
\]
\[
K_2=\begin{pmatrix}5/14&-1/7\\-1/7&1/7\end{pmatrix},\quad
K_4=\begin{pmatrix}5/8&-5/14\\-5/14&5/14\end{pmatrix}.
\]
The actual cost matrices are
\[
Z_{1,3}=\begin{pmatrix}1/2&-1\\0&3/2\end{pmatrix},\qquad
Z_{2,4}=\begin{pmatrix}1/4&-5/4\\0&3/2\end{pmatrix}.
\]
Their first two traces are respectively \((2,5/2)\) and \((7/4,37/16)\), and their exact determinant ratios are \(15/4\) and \(25/8\). The total ratio is \(375/32\). Their coefficient matrices display why original-metric self-adjointness does not mean Euclidean self-adjointness in this fixed basis.

For \(q=3\), reduction modulo \((S-1)^3\) of the retained recurrence gives columns
\[
b_0=(1,0,0)^T,\ b_1=(-1,1,0)^T,\ b_2=(2,-2,1)^T,
\ b_3=(-3,3,0)^T,
\]
\[
b_4=(9,-12,6)^T,\quad b_5=(-15,15,0)^T,\quad b_6=(60,-90,45)^T.
\]
Using the literal norms \(7n!\),
\[
K_3=\begin{pmatrix}11/14&-9/14&1/7\\-9/14&9/14&-1/7\\1/7&-1/7&1/14\end{pmatrix},
\quad
G_3=\begin{pmatrix}7&7&0\\7&49/5&28/5\\0&28/5&126/5\end{pmatrix},
\]
\[
K_6=\begin{pmatrix}9/4&-21/8&1\\-21/8&27/8&-11/8\\1&-11/8&11/16\end{pmatrix},
\quad
F=\begin{pmatrix}9&-15&60\\-12&15&-90\\6&0&45\end{pmatrix},
\quad \Omega=\operatorname{diag}(168,840,5040).
\]
Thus
\[
F^*G_3F=\begin{pmatrix}567&0&4410\\0&630&0\\4410&0&34650\end{pmatrix},
\quad
M=\Omega^{-1}F^*G_3F=
\begin{pmatrix}27/8&0&105/4\\0&3/4&0\\7/8&0&55/8\end{pmatrix},
\]
\[
Z=(K_6-K_3)G_3=
\begin{pmatrix}-29/8&-35/8&21/2\\21/4&6&-63/4\\-21/8&-21/8&69/8\end{pmatrix}.
\]
The positive spectrum, common to \(Z\) and \(M\), is
\[
\frac34,\qquad \frac{41-7\sqrt{34}}8,\qquad \frac{41+7\sqrt{34}}8.
\]
Positivity of the smaller radical eigenvalue follows from \(41^2-49\cdot34=15>0\). The last two sum to \(41/4\) and have product \(15/64\). Therefore direct rational evaluation gives
\[
t_1=11,\quad t_2=3365/32,\quad t_3=273947/256,
\quad \mathcal A_2=(121-3365/32)/2=507/64,
\]
\[
\det(I_E+Z)=\frac74\cdot
\frac{49^2-49\cdot34}{64}=\frac{5145}{256}.
\]
Substitution in (16) yields exactly
\[
a=\frac{11}{3}+\frac{7\sqrt{127}}{12},\qquad
b=\frac{11}{3}-\frac{7\sqrt{127}}{24}.
\]
The actual three eigenvalues are distinct. Thus this fixture has strictly positive Hermite loss, rather than accidental equality in a two-valued optimization. It also has strictly positive \(C_3\), because equality would force its spectrum into \(\{a,b\}\). The source's exact two-trace and determinant values pass; its decimal values are explanatory output, not the proof used here. The quotient still carries the full nonzero nilpotent part of \(M_S\) modulo \((S-1)^3\); nothing in the cost calculation removes it or identifies a cost eigenvalue with an arithmetic zero.

## 11. Coverage and integration disposition

Every section of both complete source presentations was read: the result and inherited reports; arithmetic source/support and empty packet; fixed polynomial coordinates; positive cost and action; both source traces and the exterior map; cap and sharp optimization; full remainder and third trace; radical-free area estimate; consecutive-window composition; robust enclosures and input size; coordinate and mass propagation; both Gaussian calibrations; final status and references.

The complete new finite argument is suitable for integration after the two required boundary corrections and the two precision clarifications above. Preserve the delivered source files verbatim and carry the corrected mathematical reading in a visibly identified integration layer. Retain the original degree indexing, the original arithmetic norm and mass, all quotient multiplicities, the actual source relation map and its kernel, and the exact action defect. The source's inherited analytic prerequisites and its unproved uniform trace growth are not converted into new proved assertions by this review.

A second independent read-only scalar review of sections 5–7 and 9 returned the same positive remainder, spectral cap, equality multiplicities, third-trace correction, and boundary findings. It also supplied the exact coefficient signs in (31): after collecting terms, the coefficient of \(t_1\) is \((1+B_0)^{-1}-2B_0c_{A_0,B_0}>0\), while that of \(t_2\) is \(c_{A_0,B_0}<0\). With exact coefficients, the rectangular trace-enclosure maximum is therefore attained at \((t_1^+,t_2^-)\); enclosing the coefficients themselves by rational intervals retains validity. No extra arithmetic hypothesis is required for this finite enclosure fact.
