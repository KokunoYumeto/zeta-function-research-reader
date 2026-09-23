# Independent verification of the original-zeta divisor and matrix receivers

Date: 2026-09-23. This is an independent mathematical receiving-map check of the complete current text **ORIGINAL_ZETA_DIVISOR_AND_MATRIX_RECEIVERS.tex**, equations OZ1–23. All paragraphs and proofs were read. The two numerical receiver programs, their receipts, the exact original nineteen coefficients, and the source contraction convention were also read. The full-lattice lifts and the meromorphic-test correction were checked against **COMPLETION_FACTOR_FULL_HEAT_MAP.tex**, CF31–36.

**Result:** no mathematical defect was found in OZ1–23. The sign conventions, multiplicities, original coefficient maps, all four Schur correction blocks, connection difference, whole-window enclosure, and local transport conclusion are correct on their stated domains. The independent exact-rational verifier passes 56 checks. It proves the displayed numerical inequalities using the retained quadrature intervals as inputs; it does not rerun theta quadrature or assert formal verification of the interval library.

## OZV1. Sources actually used and exact scope

The receiving manuscript is **ORIGINAL_ZETA_DIVISOR_AND_MATRIX_RECEIVERS.tex**, OZ1–23, including its explanations of the test domain and full signed divisor. The numerical receiver programs read completely are **evaluate_full_zeta_trace.py** and **propagate_native_original_zeta.py**. Their outputs are **FULL_ZETA_TRACE_RECEIPT.json** and **NATIVE_ORIGINAL_ZETA_RECEIPT.json**.

The retained time-zero source is **inputs/REPRODUCED_WITNESS63.json**, with SHA256

    aa296253ed03decc4bf11da1d2be897ab5eef990c65370c922e1abcc8d4e3b56

The retained native time-window source is **inputs/NATIVE_SCHUR_INTERVALS.json**, with SHA256

    4c528afccdb8a0caaca37e25d716d5933a74ea396f274a30de83a2d8b84b661c

The unchanged rational coefficient source is **inputs/rational_witness.json**, with SHA256

    85314e9fb3115647b7f03a5e00f1b5512c4b23c9280a753f3cf2cababdfed4ac

These hashes were checked against the actual files. The native source's own witness pin equals the third hash. The original contraction implementation in the parent native-Schur directory, **native_schur_moments.py**, coefficient construction and contractions around lines 84–117, agrees with OZ19–20.

The independent arithmetic derivation is implemented in **independent_original_zeta_check.py**; its complete result is **INDEPENDENT_ORIGINAL_ZETA_RATIONAL_CHECK.json**. Relative source names are resolved against the receiver directory, while an absolute source name is retained unchanged. This is a file-location rule, with no alteration of the numerical inputs.

The human source of the original theta coordinate and full multiplier remains Brad Rodgers and Terence Tao, *The de Bruijn–Newman constant is non-negative*, arXiv:1801.05914v5, source labels **hoz**, **sas**, **phidef**, and **htdef**, as cited in OZ1. This independent check uses the local complete derivations CF1–29 and WR1–5 for their proved analytic inputs. Its bounded scope is verification of the receiving maps from those inputs, not a fresh reading of the entire analytic literature or a fresh quadrature computation.

## OZV2. Original coordinate, full multiplier, and test reflection

Keep exactly
\[
 C(s)=s(s-1)\pi^{-s/2}\Gamma(s/2),\qquad
 Z(s)=-2i(s-\tfrac12),\qquad
 z_t(s)=\frac{16H_t(Z(s))}{C(s)}.
\]
The inverse coordinate is
\[
 s=\tfrac12+\frac{iZ}{2}.
\]
In particular neither the factor \(16\) nor any factor of \(C\) is changed. The proved original-source identity is \(z_0=\zeta\). For other real times the function in the argument is exactly the displayed meromorphic \(z_t\).

For \(r(s)=1-\bar s\), direct computation gives
\[
 Z(r(s))
 =-2i(\tfrac12-\bar s)
 =2i(\bar s-\tfrac12)
 =\overline{Z(s)}.
\]
Thus, with \(F_j(s)=Z(s)^{-(2j+1)}\),
\[
 F_j^\#(s)=\overline{F_j(r(s))}=F_j(s).
\]
For complex coefficients \(c_j\),
\[
 F_c^\#=\sum_j\bar c_jF_j.
\]
The involution is therefore exactly conjugation of the coefficient vector on this specified test space. Its only finite pole is \(s=1/2\). These statements verify OZ1–2 without changing the arithmetic coordinate.

## OZV3. Complete signed divisor and multiplicities

For real \(s\), the coordinate \(Z(s)\) is purely imaginary. The original positive theta kernel gives
\[
 H_t(iy)=\int_0^\infty e^{tu^2}\Phi(u)\cosh(yu)\,du>0
 \qquad (t,y\in\mathbb R).
\]
Consequently the numerator has no real-\(s\) zero. The original multiplier has a simple zero at \(s=1\), a simple pole at every \(s=-2\ell\), \(\ell\ge1\), and a finite nonzero value at \(s=0\). The last statement retains the cancellation between the explicit factor \(s\) and the simple Gamma pole; it is not an omission of those factors. The factor \(\pi^{-s/2}\) is entire and nonzero.

Division by \(C\), with the numerator nonzero at every real point, therefore gives one simple pole at \(1\), one simple zero at each \(-2\ell\), and no zero or pole at \(0\). At a nonreal image of a zero \(\lambda\) of \(H_t\), all factors of \(C\) are holomorphic and nonzero, so the multiplicity remains \(m_\lambda\). The affine coordinate has derivative \(-2i\ne0\), so it does not change this multiplicity.

This proves
\[
 \operatorname{div}z_t
 =\sum_{H_t(\lambda)=0}m_\lambda
       [\tfrac12+i\lambda/2]
   +\sum_{\ell\ge1}[-2\ell]-[1].
\]
Every actual \(H_t\) zero is included, with multiplicity. The first and second sums are disjoint. Since \(H_t(0)>0\), the test pole \(s=1/2\) is absent from the divisor. These observations verify the complete counting convention in OZ3–4.

## OZV4. Absolute convergence and the specified Hermitian form

Each \(F_c\) is a finite sum of inverse odd powers. Hence
\[
 F_c^\#(\tfrac12+i\lambda/2)F_d(\tfrac12+i\lambda/2)
 =O(|\lambda|^{-2})
\]
as \(|\lambda|\to\infty\). The supplied reciprocal-square estimate
\(\sum_\lambda m_\lambda|\lambda|^{-2}<\infty\) proves absolute convergence of the nonreal-\(s\) part. Finitely many small nonzero denominators cause no difficulty because the zero set is discrete and excludes \(\lambda=0\). At \(-2\ell\) the products are \(O((4\ell+1)^{-2})\), so the complete real-zero series also converges absolutely. The pole term is a single finite evaluation.

For real \(t\), \(H_t(\bar Z)=\overline{H_t(Z)}\); its zero multiplicities are invariant under conjugation. Absolute convergence then gives \(S_n(t)\in\mathbb R\), where
\[
 S_n(t)=\sum_\lambda m_\lambda\lambda^{-2n}.
\]
The resulting finite matrices are real symmetric, and
\(B_t^\zeta(F_c,F_d)=c^*K^\zeta d\) is Hermitian on this test space. The argument uses the exact coefficient reflection and real entries. It does not require, or assert, reflection symmetry of the entire original signed divisor for arbitrary meromorphic tests.

## OZV5. Every sign in the completion correction

Let \(n=i+j+1\). At the real divisor points,
\[
 Z(-2\ell)=i(4\ell+1),\qquad Z(1)=-i.
\]
Therefore
\[
 F_i(-2\ell)F_j(-2\ell)
 =i^{-2n}(4\ell+1)^{-2n}
 =(-1)^n(4\ell+1)^{-2n},
\]
and
\[
 F_i(1)F_j(1)=(-i)^{-2n}=(-1)^n.
\]
The pole occurs with multiplicity \(-1\). Writing
\[
 T_n=\sum_{\ell=1}^\infty(4\ell+1)^{-2n},
\]
the complete original-zeta entry is consequently
\[
 K^\zeta_{ij}=S_n+(-1)^n(T_n-1).
\]
The full multiplier has the opposite signed real divisor,
\([1]-\sum_{\ell\ge1}[-2\ell]\), so
\[
 K^C_{ij}=(-1)^n(1-T_n),\qquad
 K^h_{ij}=S_n=K^\zeta_{ij}+K^C_{ij}.
\]
This verifies OZ5–6. There is exactly one copy of every negative even trivial zero; none is doubled by the evenness of \(H_t\), since those zeros belong to the additional real divisor of \(1/C\).

## OZV6. The time-zero two-term test and supported cancellation

For
\[
 F=F_0+F_1=Z^{-1}+Z^{-3},
\]
the original pole evaluation is
\[
 F_0(1)=i,\qquad F_1(1)=-i,\qquad F(1)=0.
\]
The signed divisor still contains the pole. Its evaluated contribution is zero. In the synchronized \(G_L(\mathbb C)\)-module each displayed nonzero summand has support \(1_L\), and their sum is \((0,1_L)=e\).

At \(r=4\ell+1\),
\[
 F(-2\ell)=-\frac{i}{r}+\frac{i}{r^3}
          =-\frac{i}{r}(1-r^{-2}).
\]
Because \(F^\#=F\), the product used in the form is
\[
 F^\#(-2\ell)F(-2\ell)
 =-r^{-2}(1-r^{-2})^2.
\]
It is not an absolute square. Thus, writing \(a_\ell=r^{-2}\), every trivial-zero contribution is exactly
\(-a_\ell(1-a_\ell)^2<0\). For \(\ell=1\) this is
\[
 -\frac1{25}\left(1-\frac1{25}\right)^2
 =-\frac{576}{15625}.
\]
It follows that
\[
 B_0^\zeta(F,F)=S_1+2S_2+S_3-(T_1-2T_2+T_3),
\]
\[
 B^C(F,F)=T_1-2T_2+T_3
        =\sum_{\ell\ge1}a_\ell(1-a_\ell)^2>0.
\]
The pole's cancellation also follows from the entry formula: the pole coefficients combine as \(1-2+1=0\). Both routes preserve its original occurrence in the divisor. This verifies OZ7–8.

## OZV7. Exact moment receiver and source index

Write the original Taylor expansion
\[
 H_0(Z)=\sum_{n\ge0}a_nZ^{2n},\qquad
 a_n=\frac{(-1)^nM_n}{(2n)!},\qquad a_0=M_0>0.
\]
Pairing the \(\lambda\) and \(-\lambda\) factors in the supplied even Hadamard product, while retaining their multiplicities, gives near \(Z=0\)
\[
 \frac{H_0'(Z)}{H_0(Z)}
 =-\sum_{n\ge1}S_nZ^{2n-1}.
\]
There is no extra factor of two: the definition of \(S_n\) already sums over both members of each pair. Comparing the \(Z^{2n-1}\) coefficient after multiplication by \(H_0\) gives
\[
 2na_n=-\sum_{j=0}^{n-1}a_jS_{n-j},
\]
and hence precisely
\[
 S_n=\frac{-2na_n-\sum_{j=1}^{n-1}a_jS_{n-j}}{M_0}.
\]
The original positive \(M_0\) remains the denominator.

The stored array has a dummy entry \(S_0=0\). The numerical receivers correctly take indices \(1,2,3\), rather than entries \(0,1,2\). The independent checker also applies this recurrence directly to the retained binary \(M_0,\ldots,M_3\) intervals. Its resulting intervals overlap the stored \(S_1,S_2,S_3\) intervals, as recorded. This comparison is reported as overlap, not equality of differently propagated interval endpoints. The actual source root-moment intervals are the input used for reproducing the time-zero receiver.

## OZV8. Complete rational tail and exact time-zero receipt

For \(f_n(x)=(4x+1)^{-2n}\), \(n\ge1\), positivity and monotonic decrease give
\[
 \int_{N+1}^{\infty}f_n(x)\,dx
 \le\sum_{\ell=N+1}^{\infty}f_n(\ell)
 \le\int_N^\infty f_n(x)\,dx.
\]
Direct integration gives
\[
 \int_a^\infty f_n(x)\,dx
 =\frac{1}{4(2n-1)(4a+1)^{2n-1}}.
\]
With \(N=400\), these are exactly the lower and upper tails in OZ12. Every omitted positive term is covered; the tail is not set to zero.

The receiver **evaluate_full_zeta_trace.py** decodes a binary endpoint
\((\epsilon,m,e,b)\) as the rational number
\((-1)^\epsilon m2^e\). It uses rational interval operations for all sums, products, signs, and tails. Its decimal strings are displays; the exact rational endpoint pairs are retained.

The independent checker reproduces all three \(T_n\) intervals exactly, and reproduces the rational endpoints for the four quantities
\[
 B_0^h(F,F),\quad B_0^\zeta(F,F),\quad B^C(F,F),
 \quad\det K^\zeta_2(0)
\]
exactly. The resulting exact interval comparisons prove
\[
 0.0115617942<B_0^h(F,F)<0.0115617943<3/250,
\]
\[
 -0.059716<B_0^\zeta(F,F)<-0.059714,
 \qquad
 0.071276<B^C(F,F)<0.071278,
\]
and
\[
 K^\zeta_{00}(0)>0,\qquad
 -0.059715<\det K^\zeta_2(0)<-0.059713.
\]
Also \(3/250-576/15625<0\) is checked exactly. These prove OZ9–10 and OZ13 from the retained source intervals. A real symmetric \(2\times2\) matrix with strictly negative determinant has two nonzero eigenvalues of opposite signs, proving the displayed inertia \((1,1,0)\).

## OZV9. Time derivatives and every fixed coefficient map

The correction \(K^C\) has no \(t\)-dependence. Therefore on any real interval where the source moments are analytic,
\[
 \partial_t^rK^\zeta=\partial_t^rK^h,\qquad r\ge1.
\]
Near any real \(t_0\), \(H_{t_0}(0)>0\). Holomorphic dependence on \(t\) and continuity provide a complex neighborhood with \(H_t(0)\ne0\); the exact moment recurrence gives the holomorphic entries there. Thus the local analytic assertion used later is justified by the same source data.

For any fixed complex coefficient matrix \(J\),
\[
 G^\zeta=J^*K^\zeta J,\quad
 D_J=J^*K^CJ,\quad
 G^h=G^\zeta+D_J.
\]
No invertibility of \(J\) is required for this identity. The transpose-conjugate is fixed because the coefficients are fixed, and every original conditioning factor in \(J\) remains present. The derivative identity for \(G\) then follows as well. If \(J\) varied with time, extra differentiated-\(J\) terms would occur; OZ14–15 explicitly use fixed \(J\), so they do not omit such terms.

## OZV10. Connection difference, with the multiplication order retained

On the common invertible set,
\[
 (G^\zeta)^{-1}-(G^h)^{-1}
 =(G^\zeta)^{-1}(G^h-G^\zeta)(G^h)^{-1}
 =(G^\zeta)^{-1}D_J(G^h)^{-1}.
\]
Because \((G^h)'=(G^\zeta)'\),
\[
 \Gamma_\zeta-\Gamma_h
 =\frac12(G^\zeta)^{-1}D_J(G^h)^{-1}(G^\zeta)'.
\]
Every factor occurs in the order in OZ16. In general these factors do not commute, so their order is part of the statement. The formula does not extend through a zero determinant merely by notation.

Let \(P_\bullet(t,s)\) satisfy
\(\partial_tP_\bullet(t,s)=-\Gamma_\bullet(t)P_\bullet(t,s)\)
and \(P_\bullet(s,s)=I\). The composition property implies
\(\partial_vP_\zeta(t,v)=P_\zeta(t,v)\Gamma_\zeta(v)\).
Consequently
\[
 \frac{d}{dv}\{P_\zeta(t,v)P_h(v,s)\}
 =P_\zeta(t,v)(\Gamma_\zeta(v)-\Gamma_h(v))P_h(v,s).
\]
At \(v=t\) the product is \(P_h(t,s)\); at \(v=s\) it is \(P_\zeta(t,s)\). Integration therefore gives precisely the minus sign in OZ17:
\[
 P_\zeta(t,s)-P_h(t,s)
 =-\int_s^tP_\zeta(t,v)(\Gamma_\zeta-\Gamma_h)(v)P_h(v,s)\,dv.
\]
For an oriented complex path the same calculation uses its path differential. This proves the full transport receiver on the stated common domain.

## OZV11. Schur inclusion and all four correction blocks

For a Hermitian block matrix
\[
 G=\begin{pmatrix}A&B\\ C&E\end{pmatrix},
 \qquad C=B^*,\ E=E^*,
\]
with \(E\) invertible, put
\[
 J_E=\begin{pmatrix}I\\-E^{-1}C\end{pmatrix}.
\]
Then
\[
 GJ_E=\begin{pmatrix}A-BE^{-1}C\\0\end{pmatrix},
 \qquad
 J_E^*GJ_E=A-BE^{-1}C.
\]
This is an attained restriction to an explicit graph. It does not require \(E\) positive definite and does not assert a minimum when \(E\) is indefinite.

Substitute \(G=G^h-D_J\). Its actual lower block is \(E_h-D_{22}\), its upper-right block is \(B_h-D_{12}\), its lower-left block is \(C_h-D_{21}\), and its upper-left block is \(A_h-D_{11}\). Thus the restriction is exactly
\[
 A_h-D_{11}
 -(B_h-D_{12})(E_h-D_{22})^{-1}(C_h-D_{21}).
\]
The domain is precisely where \(E_h-D_{22}\) is invertible. Multiplication by block triangular matrices of determinant one also gives
\[
 \det G^\zeta
 =\det(E_h-D_{22})
   \det\!\left(
 A_h-D_{11}
 -(B_h-D_{12})(E_h-D_{22})^{-1}(C_h-D_{21})
       \right).
\]
This verifies all of OZ18; no off-diagonal correction is lost.

## OZV12. Full support maps and the contour residue at the test pole

For a complex linear map \(A:V\to W\), the full synchronized carriers
\[
 M_L(V)=(V\times\{1_L\})\cup(\{0\}\times L)
\]
have the map
\[
 \widehat A(v,\lambda)=(Av,\lambda).
\]
It is well-defined: if \(\lambda\ne1_L\), then \(v=0\), so \(Av=0\). Addition gives
\[
 \widehat A(v+w,\lambda\vee\mu)
 =(Av+Aw,\lambda\vee\mu)
 =\widehat A(v,\lambda)+\widehat A(w,\mu).
\]
For an original scalar \((a,\nu)\in G_L(\mathbb C)\), linearity similarly proves
\[
 \widehat A(av,\nu\wedge\lambda)
 =(aAv,\nu\wedge\lambda).
\]
Thus every fixed coefficient map used above has the exact full-\(L\) lift asserted in OZ7 and CF35–36. A zero image retains its incoming support. Infinite amplitudes in the particular form are assigned the specified top support; the proof invokes no arbitrary infinite join in \(L\).

For the contour identity, let \(A(s)=F_c^\#(s)F_d(s)\). The multiplier has no zero or pole at \(s=1/2\), so locally
\[
 A(s)=\sum_{j=-q}^{\infty}A_j(s-\tfrac12)^j,\qquad
 \frac{C'}C(s)=\sum_{j\ge0}b_j(s-\tfrac12)^j.
\]
The coefficient of \((s-\tfrac12)^{-1}\) in their product is
\[
 \sum_{j=1}^q A_{-j}b_{j-1}.
\]
This is precisely the additional test-pole residue stated in OZ7. At an exceptional point with multiplier order \(k_a\), the more general CF34 formula is
\(k_aA_0+\sum_{j=1}^qA_{-j}b_{j-1}\); the current point has \(k_a=0\). The logarithmic derivatives of the numerator and of \(z_t\) are also regular at this test pole, and their product residues with \(A\) are retained in the contour identity.

Accordingly the absolutely convergent divisor sums are not being confused with a contour integral having omitted test-pole residues. CF31–34 verify the finite contour identity directly by multiplication of the original local Laurent expansions.

## OZV13. Unchanged nineteen-coordinate source and corrected contractions

The exact coefficients are
\[
 c_i=\frac{1000^i n_i}{10^{120}},\qquad 0\le i\le18.
\]
The checker verifies the denominator \(10^{120}\), the nineteen entries, and the retained final coefficient \(c_{18}=10^{54}\). Neither source program rounds the input integers. The ordered pair is exactly
\[
 (f_*,F_0),\qquad f_*=\sum_{i=0}^{18}c_iF_i.
\]
The source contraction definitions therefore give
\[
 Q_h=\sum_{i,j}c_ic_jS_{i+j+1},\quad
 B_h=\sum_i c_iS_{i+1},\quad A_h=S_1.
\]
These agree with the original implementation, including the powers of \(1000\).

Put \(E_n=(-1)^n(T_n-1)\). The correction matrix in this unchanged pair is then
\[
 Q_\zeta-Q_h=\sum_{i,j}c_ic_jE_{i+j+1},\quad
 B_\zeta-B_h=\sum_i c_iE_{i+1},\quad
 A_\zeta-A_h=E_1.
\]
The maximum needed index is \(18+18+1=37\). Thus computing every \(T_n\), \(1\le n\le37\), is exactly sufficient, and OZ19–20 contain the original conditioning scale without any missing power.

## OZV14. What the retained whole-window interval proves

The source contains a dedicated **whole_window** record whose binary time interval encloses the exact rational interval
\[
 I=[-2,-2+10^{-20}].
\]
This containment is checked using rational decoding of both binary endpoints. Its three zeroth-derivative entries \(Q[0]\), \(B[0]\), \(A[0]\) are the original three contractions throughout that interval. The endpoint records do not substitute for this whole-window record.

The receiving script uses exactly those zeroth entries, adds the three time-independent corrections, and computes
\[
 \Delta_\zeta=A_\zeta Q_\zeta-B_\zeta^2,\qquad
 \mathcal S_\zeta=Q_\zeta-\frac{B_\zeta^2}{A_\zeta}.
\]
Its directed interval arithmetic encloses each input binary endpoint before using it. Even where an endpoint has more bits than the working precision, this enclosing decode remains valid; the independent checker uses the exact rational endpoints.

For an independent finite proof, each positive rational summand \(u/v\) of every \(T_n\) is enclosed on the denominator \(10^{220}\) grid by integer division:
\[
 \frac{\lfloor 10^{220}u/v\rfloor}{10^{220}}
 \le\frac uv
 \le\frac{\lceil 10^{220}u/v\rceil}{10^{220}}.
\]
The two rational integral tails are enclosed the same way. All subsequent operations use exact rational intervals and the unchanged exact coefficients. The checker proves a strictly positive lower endpoint for \(A_\zeta\), so inversion uses
\([A_-,A_+]^{-1}=[1/A_+,1/A_-]\) without crossing zero.

This independent computation proves, for the whole-window record and also for both endpoint records,
\[
 A_\zeta>0,\qquad Q_\zeta>0,
\]
\[
 -6.41746\,10^{106}
 <\Delta_\zeta
 <-6.41741\,10^{106},
\]
\[
 -6.85437\,10^{106}
 <\mathcal S_\zeta
 <-6.85431\,10^{106}.
\]
These are exactly the paper's OZ21 inequalities. The independently computed native intervals and the stored native receipt intervals overlap; the check records this fact accurately. Equality of native receipt endpoints is not claimed, since the two arithmetic implementations propagate different valid enclosing intervals. The paper's strict rational bounds are nevertheless proved independently from the same source inputs.

## OZV15. Actual negative section, inertia, and local connection

On \(I\), \(G_\zeta\) is real symmetric and has negative determinant. Hence it has inertia \((1,1,0)\), with no singular time in \(I\). Since \(A_\zeta>0\), the original real coefficient section
\[
 f_*-\frac{B_\zeta(t)}{A_\zeta(t)}F_0
\]
is well-defined and has value
\[
 Q_\zeta
 -2\frac{B_\zeta}{A_\zeta}B_\zeta
 +\frac{B_\zeta^2}{A_\zeta^2}A_\zeta
 =Q_\zeta-\frac{B_\zeta^2}{A_\zeta}<0.
\]
The full unaltered \(f_*\) remains in this expression. This proves OZ22.

At each \(t_0\in I\), the local holomorphic continuation of the moment entries exists by OZV9. Its determinant is nonzero at \(t_0\), so by continuity it remains nonzero on a sufficiently small complex disk. The inverse matrix and
\(\Gamma_\zeta=\tfrac12G_\zeta^{-1}G_\zeta'\) are holomorphic there. A holomorphic fundamental matrix for the linear equation on that disk is single-valued and invertible, giving identity transport around a loop within it. This is the local assertion of OZ23.

It does not assert trivial global transport around other singularities. The old auxiliary singular time cannot produce a local singularity of this corrected matrix in \(I\), because the corrected determinant is explicitly bounded away from zero there. On their common invertible domain the exact relation to the old transport is already OZ16–17.

## OZV16. Completed verification and its mathematical interpretation

All current OZ1–23 formulas and proofs, both receiving programs, both receiver receipts, their pinned source inputs, the original coefficient/contraction convention, and CF31–36 were read and checked. The independent script passes 56 checks, comprising source identity, exact coefficient and source-index checks, time-zero rational receipt reproduction, complete trivial-zero tails, the displayed strict numerical bounds, and the original whole-window contraction bounds.

The negative values are values of the full signed original-zeta divisor form defined in OZ4. Its compensating full-multiplier contribution is explicitly present in OZ6 and is positive for the time-zero test in OZ8. Nothing here turns an uncompensated negative value into a negative value of the auxiliary nontrivial-zero form, and no conclusion about a counterexample to RH is drawn. The exact relation between the two forms, their compressions, and their connections is proved rather than assumed.

