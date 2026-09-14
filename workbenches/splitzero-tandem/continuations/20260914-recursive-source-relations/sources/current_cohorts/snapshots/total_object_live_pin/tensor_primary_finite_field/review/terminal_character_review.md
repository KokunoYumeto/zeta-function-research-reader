# Terminal-character dictionary: independent exact review

Parent task (verbatim):

> Root adds terminal line label dictionary. Complex form y^b dy has deck pullback δζ^* eigen ζ^(b+1), terminal b=m−1=N−2 gives ζ^m=ζ^-1; ordered terminal tensor character ζ^(km), invariant iff N|k. SPF Dζ e_r=eζr on fibre functions is (δζ^-1)^* (since δζ^*δ_r=δ_{ζ^-1 r}); thus finite χ summand has D eigen λχ^-1 but ordinary deck pullback eigen λχ. My proposed exact character dictionary: fix abstract μ_N identifications/primitive character χ_* with λχ_* the chosen tautological char; then form b maps to χ_b=χ_*^{b+1}, terminal χ_ter=χ_*^m=χ_*^-1 (under pullback-to-pullback comparison), not χ_* from matching pullback directly to D. Need independently check this and compute repeated terminal tuple finite Frobenius/orbit: χ_ter order N, orbit length d, constant aχter^k; invariants if N|k and (c0 orp|k), so c!=0 needs pN|k; originalbase orbit degree d lambda=[−χ_ter(N)G_L(χ_ter,psi)]^k, characteristicT^d−lambda (terminal tuple itself not defined base unless d1). No deRham-etale/Frob claim. Check root fullpacket scalar specialization zero exact; state nonzero only if coeff alpha scalar !=0.

## 1. The inverse is fixed by the actual source operators

Retain \(N=m+1\), \(m\ge1\), and \(q_N:y\mapsto z=y^N\). Its deck map is \(\delta_\zeta(y)=\zeta y\). Literal pullback gives
\[
\delta_\zeta^*(y^b\,dy)
=(\zeta y)^b\,d(\zeta y)
=\zeta^{b+1}y^b\,dy.
\tag{TC.1}
\]
On a geometric fibre, \(e_r\) is the indicator function at the root \(r\). Evaluation at a root \(t\) gives
\[
(\delta_\zeta^*e_r)(t)=e_r(\zeta t)
=\mathbf1_{t=\zeta^{-1}r}.
\]
Consequently the SPF source operator satisfies the exact equality
\[
\delta_\zeta^*e_r=e_{\zeta^{-1}r},
\qquad D_\zeta e_r=e_{\zeta r},
\qquad D_\zeta=(\delta_{\zeta^{-1}})^*.
\tag{TC.2}
\]
The SPF projector
\[
e_\chi=\frac1N\sum_{\zeta\in\mu_N}\lambda_\chi(\zeta)D_\zeta
\]
has image with \(D_\zeta\)-eigenvalue \(\lambda_\chi(\zeta)^{-1}\). Its ordinary pullback eigenvalue is therefore
\[
\delta_\zeta^*|_{\operatorname{im}e_\chi}
=D_{\zeta^{-1}}|_{\operatorname{im}e_\chi}
=\lambda_\chi(\zeta).
\tag{TC.3}
\]
The phase \(y^N/(Nu)+c/u\) is fixed by this deck map. Finite direct image, tensor by that pulled-back phase, and compact-support direct image commute with these source operators, so (TC.3) also describes ordinary source pullback on the resulting Kummer–Gauss summand.

## 2. The exact character-label map

Choose a generator of the abstract cyclic group \(C_N\), and corresponding primitive roots \(\xi_{\mathbf C}\), \(\xi_L\), and \(\xi_\ell\) in \(\mathbf C\), \(L\), and \(\overline{\mathbf Q}_\ell\). These choices identify the three root-of-unity groups. Let \(\chi_*\in X_N\) be the unique character with
\(\lambda_{\chi_*}(\xi_L)=\xi_\ell\).

The map \(\chi\mapsto\lambda_\chi\) is a group isomorphism: the surjective power map \(L^\times\to\mu_N(L)\) in SPF.10 makes its defining equation unique, and its inverse pulls a character of \(\mu_N\) back along that power map. Thus \(\chi_*\) has order \(N\). Matching ordinary pullback on both sides of (TC.1), (TC.3) gives
\[
\mathbf Z/N\mathbf Z\longrightarrow X_N,\quad j\longmapsto\chi_*^j,
\qquad
\chi_b=\chi_*^{b+1}.
\tag{TC.4}
\]
For \(0\le b\le N-2\), these are exactly all nontrivial characters. In particular,
\[
\boxed{\chi_{\rm ter}=\chi_*^{m}=\chi_*^{-1},
\qquad \operatorname{ord}(\chi_{\rm ter})=N.}
\tag{TC.5}
\]
Matching ordinary pullback directly against \(D_\zeta\), instead of its inverse, would give the incorrect inverse label.

There is a concrete common character module for this dictionary. Set
\[
B=\mathbf Z[T,T^{-1},1/N]/(\Phi_N(T)),
\qquad M_j=B e_j,\qquad \sigma e_j=T^j e_j.
\]
The substitutions \(T\mapsto\xi_{\mathbf C},\xi_L,\xi_\ell\) give exactly the three cyclic character representations with exponent \(j\). These are actual scalar-extension maps from the same integral module. They specify character labels; they neither define a differential-to-étale cohomology comparison nor give the complex differential a Frobenius action.

## 3. Ordered terminal tensor and exact inertia

The ordered terminal form is
\[
\omega_{{\rm ter},k}
=y_1^{m-1}\cdots y_k^{m-1}
\,dy_1\wedge\cdots\wedge dy_k.
\]
Simultaneous pullback scales it by \(\zeta^{km}\). No factors are permuted. Because \(m=N-1\) is coprime to \(N\), this character is trivial exactly when \(N\mid k\).

The corresponding ordered label is
\(\boldsymbol\chi_{\rm ter}=(\chi_{\rm ter},\ldots,\chi_{\rm ter})\).
Its actual summand over \(L\) is
\[
\mathcal L_\psi(kc/u)\otimes
\mathcal A_{a_{\chi_{\rm ter}}^k}\otimes
\mathcal K_{\chi_{\rm ter}^k}(u),
\qquad
a_{\chi_{\rm ter}}
=-\chi_{\rm ter}(N)G_L(\chi_{\rm ter},\psi).
\tag{TC.6}
\]
In particular, all \(N\)-factors and \(k\) minus signs are retained.

For \(c\ne0\), the original cover is
\(u=v^N,\ z^p-z=bc/v^N\).
Its exact tuple character is
\[
(\zeta,a)\longmapsto
\lambda_{\chi_{\rm ter}}(\zeta)^{-k}\vartheta(-ka).
\]
The tame factor is trivial exactly when \(N\mid k\); the wild factor exactly when \(p\mid k\). Their orders are coprime. For \(c=0\) the wild factor is already absent. Thus
\[
\boxed{
\boldsymbol\chi_{\rm ter}\text{ contributes to }V_k^{I_0}
\quad\Longleftrightarrow\quad
N\mid k\ \text{and}\ (c=0\ \text{or}\ p\mid k).
}
\tag{TC.7}
\]
When \(c\ne0\), this is precisely \(pN\mid k\). The occurrence of \(p\mid k\) cancels the original characteristic-\(p\) additive character; it does not reduce the integer number of tensor factors.

## 4. The original-base orbit has length \(d\)

Geometric \(\operatorname{Fr}_{Q_0}\) sends each tuple label to its entrywise \(Q_0\)th power, as proved from the original projectors in TPF.27–28 and TR.9–11. Since \(\chi_{\rm ter}\) has exact order \(N\), its repeated tuple is fixed by the \(e\)th iterate exactly when
\[
Q_0^e\equiv1\pmod N.
\]
Its orbit therefore has exact length \(d=\operatorname{ord}_N(Q_0)\), independently of \(k\ge1\). This remains true when its product character is trivial; the distinct ordered tuple lines have not been identified.

When (TC.7) holds, this orbit lies in the original inertia-invariant subspace. Its actual orbit field is \(L=\mathbf F_{Q_0^d}\), and
\[
\boxed{\Lambda_{{\rm ter},k}
=\left[-\chi_{\rm ter}(N)G_L(\chi_{\rm ter},\psi)\right]^k}
\tag{TC.8}
\]
is the exact scalar of
\(\operatorname{Fr}_{Q_0}^d=\operatorname{Fr}_Q\) on the selected tuple line, by (TC.6). Both geometric character factors in (TC.6) are trivial under (TC.7), so this is the scalar at the invariant boundary stalk as well.

Choose \(0\ne v_0\) in that line and let
\(v_j=\operatorname{Fr}_{Q_0}^jv_0\), \(0\le j<d\).
These vectors belong to the \(d\) distinct summands and form a basis of their direct sum. Frobenius sends \(v_j\) to \(v_{j+1}\), except that \(v_{d-1}\) returns to \(\Lambda_{{\rm ter},k}v_0\). It follows directly that
\[
\boxed{
\det(X-\operatorname{Fr}_{Q_0}\mid O_{\rm ter})
=X^d-\Lambda_{{\rm ter},k},\quad
\det(1-T\operatorname{Fr}_{Q_0}\mid O_{\rm ter})
=1-\Lambda_{{\rm ter},k}T^d.
}
\tag{TC.9}
\]
There is no extra cycle sign in (TC.8). The determinant of the cycle block itself is \((-1)^{d-1}\Lambda_{{\rm ter},k}\).
The exact Gauss absolute value gives
\[
|\Lambda_{{\rm ter},k}|=Q_0^{dk/2},
\qquad |\beta|=Q_0^{k/2}
\quad\text{whenever }\beta^d=\Lambda_{{\rm ter},k}.
\]

For \(d>1\), the distinguished terminal tuple line is moved by original-base Frobenius. It is not a descended embedded rank-one summand over \(k_0\); its orbit block does descend. Eigenlines formed by combinations of orbit lines are different subspaces. If (TC.7) fails, the orbit has zero intersection with the original invariant subspace and contributes no invariant-boundary block.

## 5. Specialization of the exact scalar and the full unit

Retain the original coefficient map \(\alpha:R\to k_0\) and the full marked packet
\[
A_{R,k}
=R[y_1,\ldots,y_k]/(y_1^m,\ldots,y_k^m)
\,dy_1\wedge\cdots\wedge dy_k.
\]
Precisely, this is the quotient of the free module of ambient top forms
\(\Omega^k_{R[y_1,\ldots,y_k]/R}\) by the ideal
\((y_1^m,\ldots,y_k^m)\) times that module. It is not the Kähler differential module of the quotient algebra, whose differential relations are different. In particular, the relation obtained by differentiating \(y_i^m=0\) is not imposed on this displayed marked packet.
Here \(y_i=s_i-\rho\), so specialization sends it to \(s_i-\alpha(\rho)\). Repeated division by the monic powers \(y_i^m\) gives the unique remainder basis
\[
y_1^{b_1}\cdots y_k^{b_k}\,dy_1\wedge\cdots\wedge dy_k,
\qquad 0\le b_i<m.
\]
Indeed a supported remainder in the ideal generated by the \(y_i^m\) has every coefficient zero. The same argument proves that this is a basis after scalar extension to \(k_0\) or \(L\).

For the exact original scalar \(q\in R\), specialization therefore gives
\[
q\omega_{{\rm ter},k}
\longmapsto
\alpha(q)\overline\omega_{{\rm ter},k},
\qquad
\boxed{
\alpha(q)\overline\omega_{{\rm ter},k}=0
\Longleftrightarrow\alpha(q)=0.
}
\tag{TC.10}
\]
Taking the terminal basis coefficient proves the reverse implication; the forward construction proves the other. A nonzero complex value of \(q\) does not establish that its image under this specified map is nonzero.

Retain the full original unit
\(v(y)=\sum_{j=0}^{m-1}a_jy^j\) and its inverse in the original remainder ring. Its complete multiplication on the terminal packet is
\[
\left(\prod_{i=1}^k v(y_i)\right)\omega_{{\rm ter},k}
=a_0^k\omega_{{\rm ter},k}.
\tag{TC.11}
\]
Every term containing a positive power of any \(y_i\) becomes divisible by \(y_i^m\) and vanishes in the actual retained quotient. Taking constant coefficients in \(v(y)v(y)^{-1}=1\) proves that \(a_0\) is a unit, so \(\alpha(a_0)\ne0\). Thus this full unit contributes the proved nonzero factor \(\alpha(a_0)^k\); any further factors in the actual scalar \(q\) still require their exact images under the same \(\alpha\). No unprovided invertibility is inferred.

The scalar \(\alpha(q)\) is in characteristic \(p\). It is not a scalar in the characteristic-zero coefficient field \(\overline{\mathbf Q}_\ell\) of the Gauss line: a unital field map \(k_0\to\overline{\mathbf Q}_\ell\) would send \(p\cdot1=0\) to \(p\cdot1\ne0\), which is impossible. Therefore (TC.10) is the precise specialization statement for the algebraic marked packet. Equations (TC.4), (TC.6), and (TC.9) give its character label and the independently constructed finite-field sheaf's orbit. They do not turn a base-field scalar into an étale-cohomology scalar or imply an unconstructed cohomological comparison.

All proposed signs and orbit formulas are correct with these explicit conventions and the scalar qualification (TC.10).

## 6. Review of the actual full-packet scalar in TPF.41–43

I subsequently read the full new terminal section TPF.36–43. It specifies the original scalar
\[
K=k(m-1),\qquad
u_0=(g/h_0)(\rho),\qquad
C_{h_0,k}=\frac{K!}{((m-1)!)^k}u_0^k.
\]
This is the \(q\) to use in (TC.10). Its exact image is
\[
\alpha(C_{h_0,k})
=\overline{K!}\,
\bigl(\overline{(m-1)!}\bigr)^{-k}
\alpha(u_0)^k.
\]
Because \(m-1=N-2<p\), the denominator is nonzero in the specified characteristic-\(p\) field. The numerator is nonzero exactly when \(K<p\): for \(K<p\) every integer factor from \(1\) through \(K\) is nonzero, while \(K\ge p\) includes the zero factor \(p\). Therefore
\[
\boxed{\alpha(C_{h_0,k})\ne0
\quad\Longleftrightarrow\quad
k(m-1)<p\ \text{and}\ \alpha(u_0)\ne0.}
\tag{TC.12}
\]
For \(m\ge2\) and \(p\mid k\), one has \(K\ge p\); hence the original marked scalar specializes to zero. In particular all terminal-invariant degrees \(pN\mid k\) in the \(c\ne0\) case have zero specialized marked scalar when \(m\ge2\). The independently constructed sheaf and its invariant orbit block remain nonzero. For \(m=1\), \(K=0\) and \(C_{h_0,k}=u_0^k\).

If the original full unit and its inverse are retained at this marked point, evaluation and the same coefficient map send their product to one; this proves \(\alpha(u_0)\ne0\) in that specified coefficient model. It does not remove the factorial zero in (TC.12).

All formulas TPF.36–43 agree with this independent calculation. TPF.43 uses the coefficient quotient without a Kähler differential construction, so its nonzero terminal basis vector has the correct module target.
