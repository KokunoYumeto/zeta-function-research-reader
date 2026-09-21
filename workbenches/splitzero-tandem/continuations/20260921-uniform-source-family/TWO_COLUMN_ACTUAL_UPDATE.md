# The actual activated two-column update

21 September 2026. This is an independent finite derivation of the adjacent update ACC24, retaining its activated baseline, complete physical source, and every value cross term. It also identifies exactly which distinct two-column update admits a product of consecutive monic-norm ratios.

The actual ACC24 update is one scalar outgoing column together with one outgoing column of the full joint source. Its determinant is not the determinant of two consecutive scalar polynomial additions. Nevertheless its logarithm is proved below to be \(O_h(q)\), uniformly over \(0\le\eta\le1\), at each of the four original cutoffs. The joint part has the stronger bound \(O_h(k\log^2(q+2))=o(q)\). Hence the complete angle change is \(o(kq)\) from the actual activated baseline, with no assertion about its unevaluated initial angle.

## Source identities and exact reading coverage

All paths in this paragraph are relative to the `spectral_intake_20260921` directory containing this note's parent directory. The sources read for this calculation were:

- `inverse_sector_reduction_20260921/INVERSE_QUOTIENT_RECEIVERS.tex`, IQR15–23, SHA-256 `251B10623FB60C425775E62B434C744F3C2F14CF00EE2D334B63B0E2D0B85CAC`.
- `inverse_sector_reduction_20260921/COMPLETE_MIXED_SOURCE_PROOFS.tex`, C6–10, lines 523–552, SHA-256 `82CCCE2D56D43C544B1D813BDA27DBE1C20700FAA83BD983E34C3D83315C0C99`. The surrounding current/source discussion was also read. Its actual public locator is [C6–10 in the complete mixed-source proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/78ed538f7c00121ab66e9e8adbefc0612c118db8/workbenches/splitzero-tandem/continuations/20260921-mixed-family-proof-source/COMPLETE_MIXED_SOURCE_PROOFS.tex#L528).
- `ORIGINAL_ADJACENT_CUTOFF_CURRENT.tex`, complete file; especially ACC24 at line 324 and ACC27 at line 360. SHA-256 `786933325827D18FFD924C73C218AA1CED9CB4F0C232830A814488825A5507CB`.
- `activation_intake_20260921/ACTIVATION_ORIGINAL_COMPLETE_PROOFS.md`, opening definitions and A1–19, the finite return proof through A19, and A28–31. Exact locators: A4 line 62, A7 line 108, A9 line 127, A28 line 522, A29 line 532, A30 line 540. SHA-256 `6FC047F2513C6C61E0568E47BDA23CCB5CCC4394E7704BB7F3F4E5AA9D871E29`.
- `../../JOINT_MINIMUM_COMPLETE.tex`, lines 611–683: J3 is proved at lines 634–643, and the complete normal-source maps J5–J8 occur at lines 655–671. SHA-256 `70DC576A470E1FDC15AFE7C7CA49EFCDD569BF1EA2A429094D0E19B97EBCD416`.
- `publication_003/RETAINED_PROFILE_PROOF.tex`, opening source definitions and H1–9; H3 is the exact monic norm calculation and H4 is the retained profile through relation degree \(q+1\). Its public locator is [H3–H4 in the retained original profile](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/0fd693c844aad9117e30ec447c59864a28af10f3/workbenches/splitzero-tandem/continuations/20260921-native-spectral-real-pair/003/RETAINED_PROFILE_PROOF.tex#L19).

The exact public proof sources are [IQR15–23](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/ab120cf974feb26a31d77b07458b6da52f912ea4/workbenches/splitzero-tandem/continuations/20260921-inverse-quotient/INVERSE_QUOTIENT_RECEIVERS.tex), [ACC24–27](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/7230c00b9f07dd222b2aea95427d67918f3a8cac/workbenches/splitzero-tandem/continuations/20260921-local-covariance-activation/010/ORIGINAL_ADJACENT_CUTOFF_CURRENT.tex), [A6–9 and A28–30 in the complete activation reader](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/7230c00b9f07dd222b2aea95427d67918f3a8cac/workbenches/splitzero-tandem/continuations/20260921-local-covariance-activation/010/COMPLETE_ACTIVATION_AND_NATIVE_READER.tex), and the [complete J3 source included in this edition](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-uniform-source-family/JOINT_MINIMUM_COMPLETE.tex#L634).

These are bounded readings of the named original sources, not an exhaustive literature claim. The finite identities below are proved here; the named original coercivity bounds and monic profile are retained with their stated source scope. Their arithmetic source conventions retain T. H. Koornwinder, R. Wong, R. Koekoek, R. F. Swarttouw and W. P. Reinhardt, [NIST DLMF 18.22.E8](https://dlmf.nist.gov/18.22.E8) and [18.23.E7](https://dlmf.nist.gov/18.23.E7). The one-factor analytic bounds retain T. M. Apostol's Chapter25 and R. A. Askey and R. Roy's Chapter5 attributions in the full J3 source and its accompanying original equation TeX.

## 1. Original spaces and the actual two columns

Keep the original physical coordinate \(S=k/2+iy\), full monic relation \(Q_k(y)=i^{-q}\chi_k(k/2+iy)\), and source measure \(d\mu=w_h^{*k}(y)\,dy\). Write \(E=\mathbb C[y]/(Q_k)\) in its unchanged coefficient coordinates. Let \(X_N\) be the original scalar polynomial source through degree \(N\), represented in the original physical Hilbert space. Let \(Y\) be the same fixed tensor-section image at every cutoff, and write \(\mathcal J_N=X_N+Y\).

Every attained metric uses the full prescribed tensor value, including the original unit and the complete relation kernel. Let

\[
C_N=G_N^{-1},\qquad C_N^J=(G_N^J)^{-1},\qquad
C_N(\eta)=(1-\eta)C_N+\eta C_N^J,
\qquad G_N(\eta)=C_N(\eta)^{-1},
\tag{TC1}
\]

for source activation \(0\le\eta\le1\). The tensor-section parameter, when it must be named, will be \(\zeta\); it is fixed and is not the activation \(\eta\).

Set \(n=N+1\), and let \(\phi_n=p_n/\sqrt{\omega_n}\) be the actual orthonormal outgoing scalar polynomial. Define

\[
f_N=\operatorname{value}(\phi_n),\quad
z_N=(I-P_{\mathcal J_N})\phi_n,\quad
g_N=\begin{cases}\operatorname{value}(z_N)/\|z_N\|,&z_N\ne0,\\0,&z_N=0.\end{cases}
\tag{TC2}
\]

The projections here are physical source projections. A nonzero \(z_N\) may still have zero value, in which case \(g_N=0\) as well. The exact orthogonal source decompositions are

\[
X_{N+1}=X_N\mathbin{\perp}\mathbb C\phi_n,
\qquad
\mathcal J_{N+1}=\mathcal J_N\mathbin{\perp}\mathbb Cz_N,
\tag{TC3}
\]

with the last summand absent if \(z_N=0\). Covariances add under these actual orthogonal decompositions, so

\[
\begin{gathered}
C_{N+1}=C_N+f_Nf_N^*,\quad
C_{N+1}^J=C_N^J+g_Ng_N^*,\\
C_{N+1}(\eta)=C_N(\eta)+U_NU_N^*,
\quad U_N=[\sqrt{1-\eta}\,f_N,\sqrt\eta\,g_N].
\end{gathered}
\tag{TC4}
\]

This proves the exact ACC24 update from its source spaces. Zero or dependent value columns remain allowed.

The two coefficient channels in \(U_N\) belong to the two weighted covariance summands in TC1. They are not asserted to be orthogonal vectors in their common physical ambient source. Indeed put \(Z_N=(I-P_{X_N})Y\), so \(\mathcal J_N=X_N\mathbin{\perp}Z_N\), and use \(\phi_n\perp X_N\). Then

\[
z_N=(I-P_{Z_N})\phi_n,\qquad
f_N=h_N+\sqrt{\theta_N}\,g_N,
\quad h_N=\operatorname{value}(P_{Z_N}\phi_n),
\quad \theta_N=\|z_N\|^2\in[0,1].
\tag{TC5}
\]

The formula holds also at \(\theta_N=0\). It is the exact connecting value identity. In particular the second column is a residual of the same degree-\(n\) polynomial against the old full joint source; it is not \([\phi_{n+1}]\).

For completeness, TC1 is the covariance of the value map
\[
(x,j)\mapsto\sqrt{1-\eta}\operatorname{value}(x)+\sqrt\eta\operatorname{value}(j)
\]
on the orthogonal direct sum \(X_N\oplus\mathcal J_N\). After splitting \(\mathcal J_N=X_N\perp Z_N\), rotate the two copies of \(X_N\) by the unitary two-by-two coefficient matrix with rows
\((\sqrt{1-\eta},\sqrt\eta)\) and \((-\sqrt\eta,\sqrt{1-\eta})\). The first copy supplies the unchanged scalar value map and the second has zero value. Removing only that zero-value channel leaves \(X_N\oplus Z_N\) with the prescribed normal-source penalty \(\eta^{-1}\). This proves the exact relation to A11 without deleting a cross term of an unprocessed source Gram.

## 2. The full finite determinant with all cross terms

Fix \(N,\eta\), abbreviate \(G=G_N(\eta)\), \(f=f_N\), \(g=g_N\), and define

\[
a=(1-\eta)f^*Gf,\quad c=\eta g^*Gg,\quad
b=\sqrt{\eta(1-\eta)}f^*Gg.
\tag{TC6}
\]

The determinant identity \(\det(I+AB)=\det(I+BA)\), proved by eliminating either block of \(\begin{psmallmatrix}I&A\\-B&I\end{psmallmatrix}\), gives

\[
e^{D_N(\eta)}
:=\frac{\det C_{N+1}(\eta)}{\det C_N(\eta)}
=\det(I_2+U_N^*GU_N)
=(1+a)(1+c)-|b|^2.
\tag{TC7}
\]

Equivalently, if
\(G_1=(G^{-1}+(1-\eta)ff^*)^{-1}\), then direct multiplication gives

\[
G_1=G-\frac{1-\eta}{1+a}Gff^*G,
\qquad
e^{D_N(\eta)}=(1+a)(1+\eta g^*G_1g),
\tag{TC8}
\]

because \(\eta g^*G_1g=c-|b|^2/(1+a)\). Thus the interference term is retained exactly in the conditional second factor.

For any other independent frame on these same two source channels, write \(F=U_NT\), \(H=T^*T\), with \(T\) invertible. Its complete source covariance satisfies

\[
FH^{-1}F^*=U_NU_N^*,\qquad
\det(I+G^{1/2}FH^{-1}F^*G^{1/2})
=\frac{\det(H+F^*GF)}{\det H}=e^{D_N(\eta)}.
\tag{TC9}
\]

No diagonal replacement of \(H\) occurs. If a redundant source description is used, pass to its positive source range with the original kernel compatibility, or retain its Moore–Penrose inverse; its nonzero covariance eigenvalues and the determinant in TC9 are unchanged.

## 3. A rank-one joint step has no dimension multiplier

The full-source enclosure needed here is the actual J3/A7 enclosure in one common physical value frame:

\[
\mathbf L^{-1}T\preceq G_M^J\preceq\mathbf B T,
\qquad T=G_{k,1},
\tag{TC10}
\]

at both \(M=N\) and \(M=N+1\). It is obtained before minimization on the lower side, and by the retained full tensor section on the upper side. More explicitly, J3 gives
\(\Lambda_{h,n_*}^{-k}T\preceq G_M^J\preceq\tau_\zeta^kG_{k,\zeta}\preceq\tau_\zeta^kT\)
after choosing the common degree allowance to cover both cutoffs and the fixed section. Thus one may take \(\mathbf L=\Lambda_{h,n_*}^k\), \(\mathbf B=\tau_\zeta^k\), or the already retained A7 constants. Here the existing \(n_*=2q+2\) allowance covers every outgoing degree used below; if the fixed section degree is larger, use its maximum with \(2q+2\), as required by J3. In the original eventual domain the fixed section degree is already below this allowance.

TC10 implies \(\mathbf B\mathbf L\ge1\). Inverting its lower bound at \(N+1\), and applying its upper bound at \(N\), yields

\[
\begin{aligned}
I+(G_N^J)^{1/2}g_Ng_N^*(G_N^J)^{1/2}
&=(G_N^J)^{1/2}(G_{N+1}^J)^{-1}(G_N^J)^{1/2}\\
&\preceq\mathbf L(G_N^J)^{1/2}T^{-1}(G_N^J)^{1/2}
\preceq\mathbf B\mathbf L I.
\end{aligned}
\tag{TC11}
\]

For the last order, \(G_N^J\preceq\mathbf B T\) is equivalent to
\(T^{-1/2}G_N^JT^{-1/2}\preceq\mathbf B I\). The positive matrix
\((G_N^J)^{1/2}T^{-1}(G_N^J)^{1/2}\) has the same eigenvalues, hence the same upper scalar bound. This verifies the order without assuming the two metrics commute.

The left side of TC11 is an identity plus one rank-one positive matrix. Its only possibly nonunit eigenvalue is \(1+g_N^*G_N^Jg_N\). Therefore

\[
\boxed{0\le D_N^J
:=\log\frac{\det C_{N+1}^J}{\det C_N^J}
=\log(1+g_N^*G_N^Jg_N)
\le\log(\mathbf B\mathbf L).}
\tag{TC12}
\]

This is the complete rank-one derivation. A factor \(q\) is unnecessary because all other relative eigenvalues equal one. It includes \(g_N=0\).

The original A6–7 bounds give

\[
\log(\mathbf B\mathbf L)=O_h(k\log^2(q+2))=o(q)
\tag{TC13}
\]

at fixed original packet and fixed section data. In the simple-quartet application \(q=(k+1)^2\), so the last equality follows directly from \(\log^2(q+2)/k\to0\). No new lower bound on an individual normal-source Gram eigenvalue is used.

## 4. Evaluated bound for the actual activated determinant

Because \(X_N\subset\mathcal J_N\), the same-fibre minimum gives \(G_N^J\preceq G_N\), hence \(C_N^J\succeq C_N\). Thus

\[
G_N(\eta)\preceq G_N,
\quad a\le\alpha_N:=f_N^*G_Nf_N.
\tag{TC14}
\]

Also \(G_1\preceq G_N(\eta)\). For \(\eta>0\), TC1 gives
\(G_N(\eta)\preceq\eta^{-1}G_N^J\), so
\(\eta g_N^*G_1g_N\le g_N^*G_N^Jg_N\). At \(\eta=0\), the former term is zero. Taking logarithms in TC8 proves the exact refinement of A30

\[
\boxed{
0\le D_N(\eta)-\log(1+(1-\eta)\|f_N\|_{G_N(\eta)}^2)
\le D_N^J\le\log(\mathbf B\mathbf L).
}
\tag{TC15}
\]

The scalar endpoint has an exact monic-norm value. Let \(s=N+1-q\), and let \(\nu_s\) be the squared minimum norm of a monic degree-\(N+1\) polynomial divisible by the complete \(Q_k\). Its unique minimizer \(Q_kv_s\) is orthogonal to all previous relations. The difference \(Q_kv_s-p_{N+1}\) belongs to the old scalar space \(X_N\), has value \(-[p_{N+1}]\), and is orthogonal to every old zero-value relation. It is therefore the exact minimum old-source lift of that value. Since \(p_{N+1}\perp X_N\),

\[
\nu_s=\omega_{N+1}+\|Q_kv_s-p_{N+1}\|_\mu^2,
\quad
1+\alpha_N=R_N:=\frac{\nu_s}{\omega_{N+1}}.
\tag{TC16}
\]

Combining TC12–16 gives the uniform finite estimate

\[
\boxed{0\le D_N(\eta)\le
\log\frac{\nu_{N+1-q}}{\omega_{N+1}}
+\log(\mathbf B\mathbf L),\qquad 0\le\eta\le1.}
\tag{TC17}
\]

Every source cross term remains in the exact TC7–8 identity; TC17 bounds that identity rather than replacing it.

At \(N=q-1,q,2q-1,2q\), H4/IQR22 supplies

\[
\log R_N=2q\psi((N+1-q)/q)
+O_h(k\log^2(q+2))=O_h(q),
\tag{TC18}
\]

including its retained relation degree \(q+1\) at \(N=2q\). Hence TC17 is \(O_h(q)\), uniformly in \(\eta\), at all four actual cutoffs. This evaluates the needed determinant size at the actual activated baseline.

The \(O_h(q)\) bound itself also follows from the complete finite coefficient bounds in TC29 below, so it does not require the sharper H4/EIQ asymptotic. TC18 and the fixed-\(b\) refinement TC19 retain that earlier profile theorem's stated proof status and parameter scope.

The already proved scalar profile A4 also evaluates the leading term when its source activation is \(\eta_k(b)=e^{-2bq\log(q/k)}\), with fixed \(b>0\). Its stated result is
\(\log\|f_N\|_{G_N(\eta_k(b))}=q\Psi_b((N+1-q)/q)+o_h(q)\), uniformly in the original window, with positive profile there. Since \(\eta_k(b)\to0\), TC15 gives

\[
D_N(\eta_k(b))=2q\Psi_b((N+1-q)/q)+o_h(q).
\tag{TC19}
\]

On fixed compact subsets of \(0<b<1\), the retained scalar error and TC13 give the explicit error \(O_h(q/\log(q/k)+k\log^2(q+2))\). At \(\eta=1\), TC12 gives instead \(D_N(1)=D_N^J=o(q)\). No moving-\(b\) conclusion is obtained by substituting into a fixed-\(b\) asymptotic.

## 5. The resulting exact angle receiver

Fix the original disjoint \(K,V_r\) and their original coefficient frames at each cutoff. Let \(\delta_{N,\eta}(t)\) be their concatenated-frame angle loss in
\((C_N(\eta)+tU_NU_N^*)^{-1}\), for \(0\le t\le1\). The previously independently proved IQR17 spectral-sum inequality gives

\[
\begin{aligned}
|\delta_{N,\eta}(t)-\delta_{N,\eta}(0)|
&\le\sum_{j=1}^{\min(m,r,2)}\log(1+t\lambda_j(U_N^*G_N(\eta)U_N))\\
&\le\log\det(I_2+U_N^*G_N(\eta)U_N)
=D_N(\eta).
\end{aligned}
\tag{TC20}
\]

Zero eigenvalues contribute zero. Combining TC17–18 yields

\[
|\delta_{N,\eta}(1)-\delta_{N,\eta}(0)|=O_h(q)=o(kq)
\tag{TC21}
\]

uniformly in the actual activation \(\eta\). For four possibly different activations \(\eta_N\), keeping the four original signs,

\[
\left|\mathcal R_N[\delta_{N,\eta_N}(1)-\delta_{N,\eta_N}(0)]\right|
\le\sum_{N=q-1,q,2q-1,2q}
\left[\log R_N+\log(\mathbf B\mathbf L)\right]
=O_h(q)=o(kq).
\tag{TC22}
\]

The initial angle at \(G_N(\eta_N)\) remains in these equations. Rank has not been used to replace it by the canonical initial angle. Through IQR19, TC22 controls the difference between the actual kernel determinant loss and its quotient loss, with both taken from this same activated baseline.

## 6. What the complete normal source actually evaluates

Let the actual normal source at cutoff \(N\) have its complete original Gram \(H_{Z,N}\) and value map \(F_{Z,N}\), as in J5. With the original positive-range inverse set

\[
\Omega_N=F_{Z,N}H_{Z,N}^+F_{Z,N}^*,\qquad
C_N^J=C_N+\Omega_N,
\quad Z_N(\eta)=\det(I+\eta G_N^{1/2}\Omega_NG_N^{1/2}).
\tag{TC23}
\]

These are the full normal-source covariances of J7–8 and C6–10; they can have rank of order \(q\). They are not the rank-two covariance \(U_NU_N^*\). Subtracting the two exact covariance increments in TC4 proves the connecting identity

\[
\boxed{\Omega_{N+1}-\Omega_N=g_Ng_N^*-f_Nf_N^*.}
\tag{TC24}
\]

In particular the difference of two positive complete normal-source covariances need not be positive. Using \(C_N(\eta)=C_N+\eta\Omega_N\) and the determinant lemma gives the exact factorization

\[
\boxed{
e^{D_N(\eta)}
=R_N\,\frac{Z_{N+1}(\eta)}{Z_N(\eta)}.
}
\tag{TC25}
\]

Thus one canonical monic-norm ratio is present, together with the exact change of the full normal-source determinant. That second quotient contains the fixed tensor section and its complete scalar-section cross Gram. It cannot be replaced by the next canonical monic ratio merely because TC4 has two columns. TC25 is the exact relation to the full mixed-source response C6–10. For example, their logarithmic response identity reads
\(\eta\partial_\eta\log Z_N(\eta)=\operatorname{Tr}[\eta G_N^{1/2}\Omega_NG_N^{1/2}(I+\eta G_N^{1/2}\Omega_NG_N^{1/2})^{-1}]\);
differentiating TC25 connects the difference of those responses to the adjacent determinant, without identifying covariance eigenvalues with arithmetic ones.

TC15–19 evaluate the size, and in the stated fixed-activation regimes the leading term, of the complete left side of TC25. They do so without requiring an independent evaluation of both large normal-source determinants on its right side.

## 7. The different two-polynomial update and its exact monic product

For comparison within the same original polynomial source, adding the two consecutive orthonormal columns \(\phi_{N+1},\phi_{N+2}\) to \(X_N\) gives a different covariance update

\[
C_{N+2}=C_N+F_NF_N^*,\qquad
F_N=[\operatorname{value}(\phi_{N+1}),\operatorname{value}(\phi_{N+2})].
\tag{TC26}
\]

Applying TC16 successively with the actual updated baseline proves

\[
\boxed{
\det(I_2+F_N^*G_NF_N)
=\frac{\det C_{N+2}}{\det C_N}
=\frac{\nu_{N+1-q}\nu_{N+2-q}}{\omega_{N+1}\omega_{N+2}}.
}
\tag{TC27}
\]

The two columns can have a nonzero value cross Gram \(f_{N+1}^*G_Nf_{N+2}\). It is exactly included in the two-by-two determinant on the left. Sequential evaluation accounts for it by measuring the second column in \(G_{N+1}\), not again in \(G_N\). The invariance formula TC9 proves the same identity for every full non-diagonal source Gram obtained by changing the two normal-source coordinates.

At an already activated baseline \(G_N(\eta)\), adding those same two scalar columns yields
\(\det(I_2+F_N^*G_N(\eta)F_N)\), which need not equal TC27. The exact connecting formula is

\[
\det(I_2+F_N^*G_N(\eta)F_N)
=R_NR_{N+1}
\frac{\det(I+\eta G_{N+2}^{1/2}\Omega_NG_{N+2}^{1/2})}
{\det(I+\eta G_N^{1/2}\Omega_NG_N^{1/2})}.
\tag{TC28}
\]

Here \(\Omega_N\) is held fixed because this is the two-scalar-column update, not the next full joint source. TC28 follows directly by evaluating
\(\det(C_{N+2}+\eta\Omega_N)/\det(C_N+\eta\Omega_N)\)
in the two orders. Since \(G_N(\eta)\preceq G_N\), its logarithm is bounded above by \(\log R_N+\log R_{N+1}\).

For a finite \(O_h(q)\) bound that also covers \(N=2q\) in TC27, one must retain the extra degree \(N+2=2q+2\). The quoted H4 profile is stated through relation degree \(q+1\), so it is not used beyond that range. The existing full polynomial coefficient bounds A9, through \(n_*=2q+2\), suffice. If all roots of the full \(Q_k\) have modulus at most \(R\), they give for every \(q\le n\le2q+2\)

\[
1\le\frac{\nu_{n-q}}{\omega_n}
\le\frac{g_+}{g_-}(1+R/q)^{2q}.
\tag{TC29}
\]

Indeed any degree-\(n\) monic polynomial has scaled leading coefficient \(q^n\), so its squared source norm is at least \(g_-q^{2n}\). The complete relation trial \(Q_k(y)y^{n-q}\) is monic and admissible for \(\nu_{n-q}\). Its scaled coefficient one-norm is at most \(q^n(1+R/q)^q\), so its squared source norm is at most \(g_+q^{2n}(1+R/q)^{2q}\). Taking the two minima proves TC29 with all roots and their multiplicities retained. The lower ratio follows because the relation-restricted monic minimum is taken over a subset of all monic polynomials.

Finally A9 gives
\(\log(g_+/g_-)=O_h(q+k\log^2(q+2))=O_h(q)\), while \(R=O_h(k)\). Thus each logarithm in TC29 is \(O_h(q)\), and both TC27 and its activated-baseline upper bound have \(O_h(q)\) logarithm at all four cutoffs. This is a proof for the genuine two-degree polynomial update; it has not been substituted for ACC24.

## Scope of the new conclusion

The finite identities retain the fixed packet, complete arithmetic unit, original physical value map, full relation polynomial, same section \(Y\) at every cutoff, and its entire cross Gram. The \(O_h(q)\) and \(o(kq)\) conclusions use the existing simple-quartet domain \(0<\delta<1/2\), \(\gamma>2\), \(k\equiv1\pmod4\), \(q=(k+1)^2\), the original period and inverse-sector positivity guards, and the fixed-source bounds TC10/TC13 through the outgoing degree. The observation kernel keeps dimension \(8k-16\) on its proved five-orbit domain.

The actual ACC24 determinant is evaluated by TC7–8 and TC25, with the uniform bound TC17 and fixed-activation profile TC19. The corresponding original-metric angle change is TC20–22. The different consecutive-polynomial determinant has the exact monic product TC27. Each statement keeps its actual starting metric and does not evaluate an initial angle from a rank count.
