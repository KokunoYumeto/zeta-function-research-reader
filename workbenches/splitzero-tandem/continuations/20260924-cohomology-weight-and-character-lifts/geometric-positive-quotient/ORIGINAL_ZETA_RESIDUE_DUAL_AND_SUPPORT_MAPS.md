# Original-zeta residue duality and the actual support receiver

24 September 2026. Complete derivation RD0–RD9.

## RD0. Prerequisites and the specific comparison

The support remains the user's \(\tau\langle Z_1;\text{no }Z_2\rangle\). The complete arithmetic reconstruction precedes every coefficient, integer, prime, analytic variable and linear operation below. None of these operations is addition at \(\tau\), a coordinate on that point, or a replacement of the user's information layers by cyclic groups. The governing corpus rule, correction chains, latest direct global-quotientability arguments, and the complete source passages for the distance, separate-branch and global-admissibility corrections were read before this calculation.

The current receiving objects are the actual closed summation image of SSI0–SSI10 and ESI0–ESI12 and the sphere sheaf calculated in CSP0–CSP13, `../tau_weight_cohomology_20260924/CC_SPHERE_PULLBACK_AND_NORMAL_DIRECTION.md`. All of CSP was read. The original-zeta projector proof RZ1–RZ2, RZ5 and RZ8–RZ12 was read directly in `../tau_weight_cohomology_20260924/ORIGINAL_ZETA_RESOLVENT_AND_PROJECTORS.md`; its other sections are dependencies with their existing proofs, not newly claimed reading coverage.

Deligne's actual lifting argument is *La conjecture de Weil. II*, §3.6, printed213–214, particularly the support-dual term in the cross on214. The full original article has been read with the separate original-source ledger. That term is \(H^{2N-i-1}(X_s)^\vee(-N)\); identifying a dual coefficient without its support, degree and twist would not reproduce that term. The calculation here constructs a dual receiver for the programme's actual coefficient spaces. It does not identify these infinite-dimensional complex sheaves with Deligne's constructible étale category.

The operations to construct are: continuous linear functionals on the already formed quotient; residues of the original \(\zeta\); their embedding into the continuous dual of actual sheaf cohomology; and their arithmetic action. The degree character used in the comparison is independently constructed by the sphere cover in CSP8, rather than assigned to the supporting point.

## RD1. The complete quotient and its finite-support subspace

Retain the Fréchet space
\[
\mathcal B=\{F\text{ entire}:b_{A,M}(F)=
\sup_{|\Re s|\le A}(1+|\Im s|)^M|F(s)|<\infty
\text{ for all integers }A,M\ge0\}.
\tag{RD1.1}
\]
Let \(\mathscr Z\) denote all distinct nontrivial zeros of the original \(\zeta(s)\), with their full multiplicities \(m_\rho\). Set
\[
\mathcal I=\{F\in\mathcal B:F^{(j)}(\rho)=0
\ (\rho\in\mathscr Z,\ 0\le j<m_\rho)\},\qquad
\mathcal Q=\mathcal B/\mathcal I.
\tag{RD1.2}
\]
This is the actual quotient topology. Cauchy's formula gives
\(|F^{(j)}(\rho)|/j!\le r^{-j}b_{A,0}(F)\) whenever \(A\ge|\Re\rho|+r\). Therefore every required jet is continuous and \(\mathcal I\) is closed. All zero multiplicities are retained in the quotient.

The already proved global isolators can also be constructed explicitly here. Keep the entire source transform with its entire multiplier:
\[
F_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad
A_\rho(s)=\frac{F_0(s)}{(s-\rho)^{m_\rho}}.
\tag{RD1.3}
\]
Division is removable at \(\rho\). It preserves \(\mathcal B\): away from a disk the denominator is bounded below by a polynomial, and on the disk the maximum principle bounds the holomorphic quotient by a larger boundary circle. Put \(a_j=A_\rho^{(j)}(\rho)/j!\), and define
\[
b_0=a_0^{-1},\qquad
b_r=-a_0^{-1}\sum_{h=1}^r a_hb_{r-h},\qquad
e_\rho(s)=A_\rho(s)\sum_{r=0}^{m_\rho-1}b_r(s-\rho)^r.
\tag{RD1.4}
\]
The nonzero number \(a_0\) is determined by the actual multiplicity, not by simplicity. The recursion proves that \(e_\rho=1\) modulo \((s-\rho)^{m_\rho}\) and has every required vanishing jet at every other zero. Thus
\[
e_{\rho,j}=[e_\rho(s)(s-\rho)^j],\quad0\le j<m_\rho,
\qquad
\mathcal Q_{\rm fin}=\bigoplus_{\rho\in\mathscr Z}
\operatorname{span}_{\mathbb C}\{e_{\rho,j}:0\le j<m_\rho\}
\subset\mathcal Q.
\tag{RD1.5}
\]
The sum is direct because evaluation of the full jet at any one zero recovers its coefficients. A member has finitely many nonzero zero blocks, but each block's source representative satisfies the conditions at **all** other zeros simultaneously. This is a subspace of the globally constructed quotient, not a bounded-height replacement for it. No density of \(\mathcal Q_{\rm fin}\) in \(\mathcal Q\) is assumed below.

## RD2. The original-zeta local residue dual

Write \(\mathcal Q'\) for the continuous complex-linear dual. On a zero block put
\[
t=s-\rho,\qquad \zeta(\rho+t)=t^m u_\rho(t),\quad
m=m_\rho,\quad u_\rho(0)=\zeta^{(m)}(\rho)/m!\ne0.
\tag{RD2.1}
\]
For a polynomial \(P\) of degree below \(m\), define
\[
\lambda_{\rho,P}([F])
=\operatorname{Res}_{s=\rho}\frac{P(s-\rho)F(s)}{\zeta(s)}\,ds
=\frac1{2\pi i}\int_{|s-\rho|=r}
\frac{P(s-\rho)F(s)}{\zeta(s)}\,ds.
\tag{RD2.2}
\]
The circle is positively oriented and sufficiently small to contain no other zero or pole. No choice of its admissible radius changes the residue. Changing \(F\) by \(\mathcal I\) makes the integrand holomorphic at \(\rho\), so the functional is well defined. It is a finite linear combination of continuous jets and hence is continuous on the quotient.

Every Taylor-coefficient functional
\(\delta_{\rho,j}([F])=F^{(j)}(\rho)/j!\), \(0\le j<m\), is one of these residues. Specifically set
\[
P_{\rho,j}(t)=\bigl[t^{m-1-j}u_\rho(t)\bigr]_{<m}.
\tag{RD2.3}
\]
Here the brackets retain exactly the Taylor terms of degrees below \(m\). The discarded remainder is divisible by \(t^m\), so
\(P_{\rho,j}(t)/(t^m u_\rho(t))=t^{-j-1}+\text{holomorphic germ}\).
Taking the residue after multiplication by \(F(\rho+t)\) proves
\[
\lambda_{\rho,P_{\rho,j}}=\delta_{\rho,j}.
\tag{RD2.4}
\]
Unscaled derivatives are \(j!\lambda_{\rho,P_{\rho,j}}\); the factorial is not suppressed. Conversely (RD2.2) is a linear combination of these \(m\) functionals. Consequently the original local residue, including every derivative of its unit \(u_\rho\), gives the entire dual of the full multiplicity block.

## RD3. A separating pairing using every reflected block

The original functional equation preserves zero multiplicities under \(\rho\mapsto1-\rho\). Define, for \(x=[F]\in\mathcal Q\) and \(g=[G]\in\mathcal Q_{\rm fin}\),
\[
\mathcal R(x,g)=\sum_{\rho\in\mathscr Z}
\operatorname{Res}_{s=\rho}\frac{F(s)G(1-s)}{\zeta(s)}\,ds.
\tag{RD3.1}
\]
This sum has finite support because every zero jet of \(G\) outside its finite support vanishes to the required order. It is independent of both representatives by exactly that order of vanishing. For each fixed \(g\), it is a continuous functional on the **entire** \(\mathcal Q\). It is complex bilinear; no Hermitian or positivity assertion is part of its definition.

For \(\sigma=1-\rho\), take the exact basis classes in (RD1.5) at \(\rho\) and \(\sigma\). Formula (RD2.1) gives the full block matrix
\[
\mathcal R(e_{\rho,i},e_{\sigma,j})
=(-1)^j[t^{m-1-i-j}]\,u_\rho(t)^{-1},\quad
0\le i,j<m,
\tag{RD3.2}
\]
where a coefficient with negative index is zero. Blocks not paired by \(\sigma=1-\rho\) give zero. The entries on \(i+j=m-1\) are \((-1)^j/u_\rho(0)\). Reversing the order of the columns introduces \((-1)^{m(m-1)/2}\); the product of the displayed signs introduces the same sign. Therefore
\[
\det\bigl(\mathcal R(e_{\rho,i},e_{1-\rho,j})\bigr)_{i,j=0}^{m-1}
=u_\rho(0)^{-m}\ne0.
\tag{RD3.3}
\]
All lower coefficients of \(u_\rho^{-1}\) remain in (RD3.2). The determinant does not replace that matrix.

Let
\[
\mathcal D=\operatorname{span}_{\mathbb C}
\{\delta_{\rho,j}:\rho\in\mathscr Z,0\le j<m_\rho\}
\subset\mathcal Q'.
\tag{RD3.4}
\]
Then
\[
\iota:\mathcal Q_{\rm fin}\xrightarrow{\sim}\mathcal D,
\qquad \iota(g)(x)=\mathcal R(x,g)
\tag{RD3.5}
\]
is a linear isomorphism. An explicit inverse on (RD2.2) is the class supported at \(\sigma=1-\rho\) whose local polynomial is \(P(-t)\): its reflected germ is \(P(t)\). Construct it by the finite linear combination of the \(e_{\sigma,j}\). Extend over finite sums. This proves surjectivity; (RD3.3) proves injectivity. It also proves that the pairing separates both arguments: a nonzero class \([F]\) has a nonzero required jet somewhere by (RD1.2), and (RD2.4) detects it.

## RD4. The exact global dual closure, without a topology substitution

Give \(\mathcal Q'\) its weak topology \(\sigma(\mathcal Q',\mathcal Q)\), namely pointwise convergence on all \(x\in\mathcal Q\). Then
\[
\overline{\mathcal D}^{\,\sigma(\mathcal Q',\mathcal Q)}=\mathcal Q'.
\tag{RD4.1}
\]
Here is a proof that also specifies its precise strength. Fix \(\lambda\in\mathcal Q'\) and any finite collection \(x_1,\ldots,x_k\in\mathcal Q\). Let
\(E:\mathcal D\to\mathbb C^k\), \(E(d)=(d(x_1),\ldots,d(x_k))\).
If \((\lambda(x_i))_i\) were not in \(E(\mathcal D)\), finite-dimensional linear algebra would supply \(c_1,\ldots,c_k\) such that
\(\sum_i c_i d(x_i)=0\) for every \(d\in\mathcal D\) but
\(\sum_i c_i\lambda(x_i)\ne0\). The first assertion and separation in RD3 imply \(\sum_i c_ix_i=0\) in \(\mathcal Q\), contradicting the second. Thus some \(d\in\mathcal D\) matches \(\lambda\) exactly on this finite collection. Direct the finite subsets of \(\mathcal Q\) by inclusion and select one such matching functional at each stage. The resulting net converges pointwise to \(\lambda\), proving (RD4.1).

Every element of the full dual is therefore recovered in this weak topology from the full residue system. This statement does not claim convergence in the strong dual topology, equicontinuity of this chosen net, a continuous extension of \(\iota\) to all of \(\mathcal Q\), or replacement of \(\mathcal Q\) by an unrestricted product of jets. Those are different assertions; none is used in this proof.

## RD5. The full arithmetic action and its dual degree factor

On the original quotient let
\[
T_a[F]=[a^sF(s)],\qquad L[F]=[sF(s)],\qquad a>0.
\tag{RD5.1}
\]
The operations are continuous since \(a^{\Re s}\) is bounded on any fixed vertical strip, and \(|s|\) adds at most one polynomial seminorm. They preserve the ideal and every finite block. For a continuous map \(U\), denote its ordinary transpose by \(U'\lambda=\lambda\circ U\); its contragredient action is \((U^{-1})'\) when \(U\) is invertible. Directly in the original residue integrand,
\[
\mathcal R(T_ax,T_ag)=a\,\mathcal R(x,g),\qquad
\mathcal R(Lx,g)+\mathcal R(x,Lg)=\mathcal R(x,g).
\tag{RD5.2}
\]
The first identity uses the complete product \(a^s a^{1-s}=a\), the second \(s+(1-s)=1\), before taking any residue. It follows that
\[
\boxed{\iota T_a=a(T_{a^{-1}})'\iota,\qquad
\iota L=(1-L')\iota.}
\tag{RD5.3}
\]
Thus the same factor \(n\) produced geometrically by the degree of \(z\mapsto z^n\) in CSP8 is present in the exact original-zeta dual receiver. For nonintegral \(a\), (RD5.3) is a coefficient identity, not a claimed single-valued cover \(z\mapsto z^a\).

For the Taylor functionals the entire triangular formulas are
\[
T_a'\delta_{\rho,j}
=a^\rho\sum_{h=0}^j\frac{(\log a)^{j-h}}{(j-h)!}\delta_{\rho,h},
\]
\[
a(T_{a^{-1}})'\delta_{\rho,j}
=a^{1-\rho}\sum_{h=0}^j
\frac{(-\log a)^{j-h}}{(j-h)!}\delta_{\rho,h},
\quad
L'\delta_{\rho,j}=\rho\delta_{\rho,j}+\delta_{\rho,j-1},
\tag{RD5.4}
\]
where \(\delta_{\rho,-1}=0\). They follow by multiplying the original Taylor series, so every factorial and every nilpotent coefficient is accounted for. They are compatible with (RD3.2), including its signs. The ordinary transpose of the actual degree-two action \(aT_a\) is instead \(aT_a'\), and its contragredient is \(a^{-1}(T_{a^{-1}})'\). Neither is silently replaced by the degree-twisted dual \(a(T_{a^{-1}})'\) in (RD5.3).

More generally, for the actual degree-character twists indexed by integers \(k,\ell\), the same integrand proves
\[
\mathcal R(a^kT_ax,a^\ell T_ag)=a^{k+\ell+1}\mathcal R(x,g).
\tag{RD5.5}
\]
In particular two normal-direction inputs carry the full factor \(a^3\), and one normal-direction input together with one unshifted input carries \(a^2\). Equivalently the map \(\iota\) intertwines the unshifted \(T_a\) with \(a^2\) times the contragredient of the normal action \(aT_a\), since that contragredient is \(a^{-1}(T_{a^{-1}})'\). This retains the difference between the coefficient degree-character dual and the dual of an already shifted normal term.

## RD6. Functional equation and the retained symmetry defect

The original functional equation in this local comparison is
\[
\zeta(s)=\chi(s)\zeta(1-s),\qquad
\chi(s)=2^s\pi^{s-1}\sin(\pi s/2)\Gamma(1-s)
=\pi^{s-1/2}\frac{\Gamma((1-s)/2)}{\Gamma(s/2)}.
\tag{RD6.1}
\]
At each nontrivial zero both local multiplier expressions are holomorphic and nonzero. For \(\sigma=1-\rho\), the full local units satisfy
\[
u_\rho(t)=(-1)^m\chi(\rho+t)u_\sigma(-t).
\tag{RD6.2}
\]
This follows by substituting \(s=\rho+t\) into (RD6.1) and retaining the factor \((-t)^m\). For \(F,G\) with finite zero support, substitution \(s=1-z\), including \(ds=-dz\), proves the exact reversal law
\[
\mathcal R([F],[G])
=-\sum_{\sigma\in\mathscr Z}\operatorname{Res}_{z=\sigma}
\frac{\chi(z)G(z)F(1-z)}{\zeta(z)}\,dz.
\tag{RD6.3}
\]
The sum is finite; the formula uses the germs of \(\chi\) there. It does not assert that multiplication by its meromorphic global formula preserves \(\mathcal B\). Derivatives of \(\chi\) in (RD6.2)–(RD6.3) are retained. In particular a symmetric or Hermitian global form has not been obtained by deleting this unit or its differential sign.

The ordinary reflected trace form previously constructed in RZ10 is
\[
W([F],[G])=\sum_{\rho\in\mathscr Z}m_\rho
\overline{F(1-\overline\rho)}G(\rho).
\tag{RD6.4}
\]
Its multiplicity-block trace has no higher-jet entries. The residue pairing (RD3.2) does: its matrix is invertible for every positive multiplicity. This proves an exact additional dual observation of the retained classes. It does not replace (RD6.4) in Weil's positivity criterion, and it makes no sign claim about that form.

## RD7. Passage to the actual sheaf cohomology and support maps

CSP gives \(H^1(Y,\mathscr F)=Q_A=A/J\) with
\[
\kappa:Q_A\xrightarrow{\sim}\mathcal Q,\qquad
\kappa([b])=[\Theta b],\qquad
\Theta b(s)=\frac12\int_0^\infty b(u)u^s\,\frac{du}{u}.
\tag{RD7.1}
\]
This is the CS convention, retaining the factor \(1/2\). The original restriction is still \(\Sigma f=2\sum_{k\ge1}f(ku)\); SSI's raw transform uses \(\mathcal M_0=2\Theta\). The isomorphism in (RD7.1) follows from the proved actual equality \(\Sigma S=J=\Theta^{-1}\mathcal I\). It retains the quotient topology, not a closure surrogate.

Transpose (RD7.1) to get an actual isomorphism of continuous duals
\(\kappa':\mathcal Q'\to Q_A'\). Combining it with (RD3.5) gives
\[
\mathcal Q_{\rm fin}\xrightarrow{\ \kappa'\iota\ }
H^1(Y,\mathscr F)',\qquad
g\longmapsto\left([b]\mapsto
\sum_\rho\operatorname{Res}_{s=\rho}
\frac{\tfrac12\mathcal M_0b(s)\,G(1-s)}{\zeta(s)}\,ds\right).
\tag{RD7.2}
\]
Its image is weakly dense by (RD4.1) and the topological isomorphism. Formula (RD5.3) gives its arithmetic action with the same complete factor. No coefficient arithmetic has been assigned to \(\tau\).

The degree-one support-to-global map from CSP7 is
\[
k^1:Q_A\oplus Q_A\longrightarrow Q_A,\qquad
(x_+,x_-)\longmapsto x_+-x_-.
\tag{RD7.3}
\]
Therefore its exact transpose on these residue functionals is
\[
(k^1)'(\kappa'\iota g)
=(\kappa'\iota g,-\kappa'\iota g).
\tag{RD7.4}
\]
The degree-two support map is instead the sum \(A\oplus A\to A\), whose transpose is \(\lambda\mapsto(\lambda,\lambda)\). The annular boundary \(a\mapsto(-a,a)\) transposes to \((\lambda_+,\lambda_-)\mapsto-\lambda_++\lambda_-\). These three identities follow by evaluating the maps on arbitrary input pairs; they preserve both branches and every orientation sign.

This embeds the residue receiver in the actual dual localization sequence. Its terms are continuous duals of CSP's coefficient complexes. Calling them a Verdier-dual sheaf, or Deligne's étale support-dual cross, would require an additional constructed comparison; that assertion is not used here.

## RD8. Endpoint and original-function data remain in the source

The quotient in RD1 records the nontrivial-zero divisor. Its original source retains the other contributions. In the raw convention SSI proves for every \(F\in\mathcal I\)
\[
f_F(x)=\frac1{2\pi}\int_{\mathbb R}
\frac{F(2+it)}{2\zeta(2+it)}x^{-2-it}\,dt,
\quad
\frac{f_F^{(2r)}(0)}{(2r)!}=\frac{F(-2r)}{2\zeta'(-2r)}\quad(r\ge1),
\tag{RD8.1}
\]
\[
f_F(0)=0,\quad \int_{\mathbb R}f_F=0,\quad
\int_0^\infty f_F(x)\,\frac{dx}{x}=-F(0),\quad
\int_0^\infty f_F(x)\log x\,dx=\frac{F(1)}2.
\tag{RD8.2}
\]
The four independent endpoint lines \(E_+\oplus E_-\) remain in \(H^0(Y,\mathscr F)\) and their full duals remain in the degree-zero transposed cohomology. They have not been folded into (RD7.2) or declared absent.

For the isolator source (RD1.3), the full retained special values are, with \(r\ge1\) in the second formula,
\[
F_0(0)=F_0(1)=\frac18,\qquad
F_0(-2r)=\frac{r(2r+1)(-1)^r\pi^r}{2\,r!}\zeta'(-2r)
=\frac{(1+2r)(2r)}8\pi^{-(1+2r)/2}
\Gamma((1+2r)/2)\zeta(1+2r).
\tag{RD8.3}
\]
Every unit coefficient \(a_j\) in (RD1.4) is obtained from the full derivatives of (RD1.3). At nontrivial \(\rho\), writing its displayed multiplier as \(C(s)\), the exact expression is
\[
a_j=\sum_{h=0}^j\frac{C^{(h)}(\rho)}{h!}
\frac{\zeta^{(m+j-h)}(\rho)}{(m+j-h)!}.
\tag{RD8.4}
\]
In contrast, (RD2.1)–(RD3.3) use the original local unit of \(\zeta\) itself. The comparison has not substituted \(F_0\) for the original arithmetic function.

## RD9. What this calculation establishes for the lifting programme

The proved map (RD7.2) supplies the complete finite-jet residue receiver inside the continuous dual of the actual geometric degree-one cohomology. It sees every nilpotent multiplicity coordinate; (RD4.1) recovers the entire continuous dual in its specified weak topology. Its arithmetic action is the degree-character contragredient (RD5.3), and its support maps have the exact transposed signs (RD7.4). These are full-divisor identities, with no bounded numerical experiment and no assumed purity.

The support-dual target used in Deligne §3.6 additionally has geometrically derived weight bounds and a particular specialization/localization cross. Neither a residue similitude nor the positive degree of a sphere cover proves those bounds for this coefficient sheaf. The current target remains to construct and calculate that comparison. The present calculation contributes its actual dual objects and maps; it does not turn the desired weight separation into an input.
