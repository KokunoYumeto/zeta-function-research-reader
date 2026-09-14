# Independent review: ordered tensor inertia and arithmetic descent

Review scope supplied by the parent:

> Independent bounded review of tensor-primary finite-field inertia/descent. Base k0=F_Q0, p>N>=2, split constant field L=F_Q Q=Q0^d,d=ord_N(Q0). Original single primary F on same u has after L: AS(c/u) tensor ⊕_{chi∈X_N,chi≠1} A_aχ tensor Kχ(u), aχ=−χ(N)G_L(chi,psi), psi=psi0∘Tr. Ordered degree k>=1 unrestricted. Need independent exact inertia character multiplicities, projector, Swan, Nlog=0 when kc=0 (c0 orp|k) and otherwise; d0=((N−1)^k+(N−1)(−1)^k)/N. Also rigorously derive arithmetic descent permutation under geometric Frob_Q0: how χ-labels permute (Q0 vs inverse) and orbit-cycle invariant Frobenius eigenvalues; avoid presumed diagonal base.

Source read in full: the supplied SPF.1–29 module, including the geometric Frobenius and deck-projector conventions. The formulas below are derived from that actual sheaf and its source power map. No new specialization of the coefficient ring, removal of the coefficient \(N\), change of \(u\), or normalization of a Gauss sum is made.

## 1. The original tensor and its full inertia representation

Write \(F_0\) for the original sheaf over \(k_0=\mathbf F_{Q_0}\), \(F=(F_0)_L\), and
\[
X_N=\{\chi:L^\times\longrightarrow\overline{\mathbf Q}_\ell^\times:
\chi^N=1\},\qquad X_N^\circ=X_N\setminus\{1\}.
\]
For an ordered tuple \(\boldsymbol\chi=(\chi_1,\ldots,\chi_k)\in(X_N^\circ)^k\), put
\[
\tau(\boldsymbol\chi)=\prod_{i=1}^k\chi_i,\qquad
a(\boldsymbol\chi)=\prod_{i=1}^k a_{\chi_i},\qquad
a_\chi=-\chi(N)G_L(\chi,\psi).
\]
The tensor-product laws for the actual Artin–Schreier and Kummer torsors give the sheaf isomorphism on the original \(u\)-line
\[
F^{\otimes k}
=\mathcal L_\psi(kc/u)\otimes
\bigoplus_{\boldsymbol\chi\in(X_N^\circ)^k}
\mathcal A_{a(\boldsymbol\chi)}\otimes
\mathcal K_{\tau(\boldsymbol\chi)}(u).
\tag{TR.1}
\]
Here \(kc\) means multiplication by the image of the integer \(k\) in the original characteristic-\(p\) coefficient field. Thus
\[
kc=0\quad\Longleftrightarrow\quad c=0\ \text{or}\ p\mid k.
\tag{TR.2}
\]
For the fixed nontrivial additive character \(\vartheta\) of \(\mathbf F_p\), write the original character as
\(\psi(x)=\vartheta(\operatorname{Tr}_{L/\mathbf F_p}(bx))\).
The coefficient \(b\) is the image in \(L\) of the coefficient of \(\psi_0\), so it is fixed by \(\operatorname{Fr}_{Q_0}\); \(b\ne0\).
Let \(\epsilon_{kbc}\) denote the geometric inertia character of
\(\mathcal L_\vartheta(kbc/u)\), with \(\epsilon_0=1\).
Let \(\theta_\tau\) be the inertia character of the original Kummer sheaf
\(\mathcal K_\tau(u)\). In the SPF convention it is the
\(\lambda_\tau^{-1}\)-character on the deck group of \(u=v^N\).
The full representation is
\[
(F^{\otimes k})_{\bar\eta}|_{I_0}
\simeq
\bigoplus_{\tau\in X_N}
(\epsilon_{kbc}\theta_\tau)^{\oplus d_\tau(k)}.
\tag{TR.3}
\]
This includes every ordered tuple and every copy of a repeated character.

The exact multiplicities are
\[
d_\tau(k)=
\begin{cases}
\displaystyle\frac{(N-1)^k+(N-1)(-1)^k}{N},&\tau=1,\\[6pt]
\displaystyle\frac{(N-1)^k-(-1)^k}{N},&\tau\ne1.
\end{cases}
\tag{TR.4}
\]
To prove the count without assuming any equidistribution, let
\(r_k(\tau)\) count the tuples with product \(\tau\).
For \(k=1\), \(r_1(1)=0\) and \(r_1(\tau)=1\) for \(\tau\ne1\).
For every \(k\ge1\), choosing the last nontrivial character gives
\[
r_{k+1}(\tau)=
\sum_{\eta\ne1}r_k(\tau\eta^{-1})
=(N-1)^k-r_k(\tau).
\]
The second equality holds because multiplication by \(\tau\) and inversion permute all \(N\) characters; the omitted term is exactly \(\eta=1\).
Both expressions in (TR.4) have the stated initial values and satisfy this recurrence. Induction proves (TR.4), including its integrality and nonnegativity.
Summing gives
\(d_1(k)+(N-1)d_{\tau\ne1}(k)=(N-1)^k\), the unchanged rank.

For \(N=2\), this proof explicitly gives \(d_1(k)=1\) for even \(k\) and \(0\) for odd \(k\); the unique nontrivial character has the complementary multiplicity. In particular, the assertion that the original single-primary sheaf has no inertia invariants cannot be carried into all tensor degrees.

## 2. The actual invariant projector and Swan conductor

Use the deck projectors already defined on the original source power map \(y^N=z\):
\[
e_\chi=\frac1N\sum_{\zeta\in\mu_N}
\lambda_\chi(\zeta)D_\zeta.
\]
Their tensor products are pairwise orthogonal idempotents and sum to the identity on \(F^{\otimes k}\); tuples containing a trivial entry have zero image, by the vanishing of the original trivial source summand.
The simultaneous deck action \(D_\zeta^{\otimes k}\) has eigenvalue
\(\lambda_{\tau(\boldsymbol\chi)}(\zeta)^{-1}\) on a tuple summand.
Consequently the exact tame-trivial projector is
\[
P_{\rm tame}
=\frac1N\sum_{\zeta\in\mu_N}D_\zeta^{\otimes k}
=\sum_{\substack{\boldsymbol\chi\in(X_N^\circ)^k\\
\tau(\boldsymbol\chi)=1}}
e_{\chi_1}\otimes\cdots\otimes e_{\chi_k}.
\tag{TR.5}
\]
Character orthogonality proves the equality on every summand, hence on the sheaf.
Equivalently, (TR.5) is the inertia average on the Kummer factor of (TR.1); the original source decomposition and the parameter Kummer decomposition give the same indicated image.

When \(kc=0\), the Artin–Schreier sheaf in (TR.1) is canonically the constant sheaf with Frobenius eigenvalue \(1\). Hence
\[
P_{I_0}=P_{\rm tame},\qquad
\dim (F^{\otimes k})^{I_0}=d_1(k),\qquad
\operatorname{Swan}_0(F^{\otimes k})=0.
\tag{TR.6}
\]
When \(kc\ne0\), the pole \(kbc/u\) has order one. The original SPF.22–23 valuation calculation applies with precisely this numerator: the nontrivial Artin–Schreier inertia character has unique upper break one. Every Kummer factor is tame. Thus for positive upper ramification indices the restrictions of all summands in (TR.3) are the same nontrivial character until break one and become trivial after break one. Therefore
\[
P_{I_0}=0,\qquad
(F^{\otimes k})^{P_0}=(F^{\otimes k})^{I_0}=0,\qquad
\operatorname{Swan}_0(F^{\otimes k})=(N-1)^k.
\tag{TR.7}
\]
For an explicit finite-group projector in this case, take
\[
u=v^N,\qquad z^p-z=kbc/v^N.
\]
Over the geometric punctured disc the deck transformations are
\((v,z)\mapsto(\zeta v,z+a)\), with
\(\zeta\in\mu_N\), \(a\in\mathbf F_p\). They commute because \(\zeta^N=1\).
Their orders are coprime and the extension has degree \(Np\): the first degree is \(N\), and the second equation has pole order \(N\), not divisible by \(p\), so it is a nontrivial degree-\(p\) Artin–Schreier extension. Averaging over this finite group gives (TR.5) multiplied by the average of a nontrivial character of \(\mathbf F_p\), hence the zero projector, proving (TR.7) directly.

Alternatively, the finite cover already trivializing the original single-primary sheaf,
\[
u=v^N,\qquad z^p-z=bc/v^N,
\]
trivializes every tensor degree simultaneously. On its finite-index inertia subgroup all matrices are exactly the identity. Thus the unipotent logarithm is
\[
N_{\log}=0
\tag{TR.8}
\]
in both cases of (TR.2). Formula (TR.8) does not imply vanishing of invariants: (TR.6) gives the exact counterexample when \(d_1(k)>0\).

## 3. The geometric Frobenius permutation has exponent \(Q_0\)

Fix a geometric Frobenius lift \(\Phi=\operatorname{Fr}_{Q_0}\) in the arithmetic fundamental group. Its action on a geometric \(N\)th root of unity is
\(\zeta\mapsto\zeta^{Q_0^{-1}}\), where the inverse is in
\((\mathbf Z/N\mathbf Z)^\times\). Hence, on the original source deck operators,
\[
\Phi D_\zeta\Phi^{-1}=D_{\zeta^{Q_0^{-1}}}.
\tag{TR.9}
\]
The coefficients lie in the fixed coefficient field
\(\overline{\mathbf Q}_\ell\); \(\Phi\) is linear on it.
Changing the summation variable to \(\eta=\zeta^{Q_0^{-1}}\) gives
\[
\begin{split}
\Phi e_\chi\Phi^{-1}
&=\frac1N\sum_\zeta\lambda_\chi(\zeta)D_{\zeta^{Q_0^{-1}}}\\
&=\frac1N\sum_\eta\lambda_\chi(\eta^{Q_0})D_\eta
=e_{\chi^{Q_0}}.
\end{split}
\tag{TR.10}
\]
The last identity follows from
\(\lambda_{\chi^{Q_0}}=\lambda_\chi^{Q_0}\), which can be checked on the surjective map \(L^\times\to\mu_N\) used in SPF.10.
Thus the actual permutation of the character lines is
\[
\boldsymbol\chi\longmapsto
\boldsymbol\chi^{Q_0}:=
(\chi_1^{Q_0},\ldots,\chi_k^{Q_0}).
\tag{TR.11}
\]
It is not exponent \(Q_0^{-1}\) for geometric Frobenius under the supplied convention. The inverse exponent in (TR.9) becomes \(Q_0\) when the idempotent is relabeled in (TR.10).
No tensor factors are interchanged.

Raising all entries to \(Q_0\) preserves the equation
\(\tau(\boldsymbol\chi)=1\). Thus (TR.5) is arithmetic-Frobenius stable and descends to the original base. On inertia invariants the action of \(\Phi\) is independent of its chosen lift, because any two lifts differ by inertia and inertia acts trivially there.

## 4. The cycle scalar is computed over its actual field of definition

Assume \(kc=0\), since otherwise the invariant space is zero.
Let
\[
\mathcal T_k=\{\boldsymbol\chi\in(X_N^\circ)^k:
\tau(\boldsymbol\chi)=1\}.
\]
Let \(O\) be an orbit in \(\mathcal T_k\) under (TR.11), and let its length be \(e\). Then \(e\mid d\).
Write \(k_e=\mathbf F_{Q_0^e}\), \(q_e=Q_0^e\), and
\(\psi_e=\psi_0\circ\operatorname{Tr}_{k_e/k_0}\).
For any representative \(\boldsymbol\chi\in O\), each \(\chi_i\) is fixed by exponent \(q_e\).
There is a unique character
\[
\kappa_i:k_e^\times\to\overline{\mathbf Q}_\ell^\times,
\qquad
\chi_i=\kappa_i\circ\operatorname{N}_{L/k_e}.
\tag{TR.12}
\]
Indeed the character group of \(L^\times\) is cyclic of order \(Q-1\), and its subgroup annihilated by \(q_e-1\) has order \(q_e-1\), because \(q_e-1\mid Q-1\).
The norm is surjective between the cyclic multiplicative groups, so its pullback is injective on character groups and its image has exactly that order. This proves existence and uniqueness. Each \(\kappa_i\ne1\), its order divides \(N\), and injectivity of norm pullback gives
\[
\prod_i\kappa_i=1.
\tag{TR.13}
\]

It is necessary here to compute the source summand over \(k_e\), because \(N\) need not divide \(q_e-1\).
For a given entry let \(r_i=\operatorname{ord}(\chi_i)=\operatorname{ord}(\kappa_i)\).
Then \(r_i\mid N\) and \(r_i\mid q_e-1\). The source power map factors over \(k_e\) as
\[
y\longmapsto w=y^{N/r_i}\longmapsto z=w^{r_i}=y^N.
\tag{TR.14}
\]
On every nonzero geometric fibre, taking the quotient of its \(N\) roots by \(\mu_{N/r_i}\) identifies the quotient with the \(r_i\) roots of \(z\).
The pullback of a function on these quotient roots is the function constant on the corresponding fibres. Thus it identifies the direct image for the second map with the \(\mu_{N/r_i}\)-invariant summand for the original \(N\)-power map. Its inverse is the average over the \(N/r_i\) roots in each fibre; this scalar is invertible in \(\overline{\mathbf Q}_\ell\).
At zero both direct images have a single geometric stalk with trivial deck action and the same assertion holds on that stalk.
The character \(\lambda_{\chi_i}\) factors through
\(\mu_N\to\mu_{r_i}\), \(\zeta\mapsto\zeta^{N/r_i}\), and under (TR.12) the factor is exactly \(\lambda_{\kappa_i}\).
To verify the constants in this assertion, for \(x\in L^\times\) one has
\[
\lambda_{\kappa_i}\bigl(x^{(Q-1)/r_i}\bigr)
=\kappa_i\bigl(x^{(Q-1)/(q_e-1)}\bigr)
=\chi_i(x)
=\lambda_{\chi_i}\bigl(x^{(Q-1)/N}\bigr).
\]
The arguments in the first and last terms are related by exponent \(N/r_i\), and the last map to \(\mu_N\) is surjective.
This gives the actual \(k_e\)-descent of the chosen source line as the standard trace-\(\kappa_i\) Kummer line on \(z\), including its zero stalk, without assuming that all \(N\) characters split over \(k_e\).

The source phase after the original translation is still
\(z/(Nu)+c/u\). Applying the original change of variable
\(w=z/(Nu)\) to this individual line over \(k_e\) gives its exact factor
\[
\mathcal L_{\psi_e}(c/u)\otimes
\mathcal A_{-\kappa_i(N)G_{k_e}(\kappa_i,\psi_e)}
\otimes\mathcal K_{\kappa_i}(u).
\tag{TR.15}
\]
The negative sign follows from the actual one-dimensional
\(H_c^1(\mathbf G_m,\mathcal K_{\kappa_i}\otimes\mathcal L_{\psi_e})\)
and the trace formula, exactly as in SPF.11–19.
This argument uses the denominator \(N\) of the original phase, not the order \(r_i\) of the selected character.

Tensoring (TR.15) over the entries and using (TR.2), (TR.13) proves that the tuple line is geometrically constant over \(k_e\) and that \(\Phi^e\) acts on it by
\[
\boxed{\displaystyle
\beta_O=
\prod_{i=1}^k
\left[-\kappa_i(N)G_{k_e}(\kappa_i,\psi_e)\right].}
\tag{TR.16}
\]
Every factor \(N\) has been retained. The established identity
\(\prod_i\kappa_i=1\) also proves
\(\prod_i\kappa_i(N)=1\), if an equivalent expression is desired.
There is no Artin–Schreier phase left in (TR.16), precisely because its original tensor coefficient is \(kc=0\).

This scalar is independent of the orbit representative. Under (TR.11), \(\kappa_i\) changes to \(\kappa_i^{Q_0}\), whereas
\[
\psi_e(x^{Q_0})=\psi_e(x),\qquad N^{Q_0}=N.
\]
The first equality follows by cyclically permuting the terms of
\(\operatorname{Tr}_{k_e/k_0}\). Substituting \(w=x^{Q_0}\) in the finite Gauss sum gives
\[
G_{k_e}(\kappa_i^{Q_0},\psi_e)
=G_{k_e}(\kappa_i,\psi_e),\qquad
\kappa_i^{Q_0}(N)=\kappa_i(N).
\tag{TR.17}
\]
Thus every factor in (TR.16) is unchanged.

Base change of the same one-dimensional compact-support group, rather than the choice of a root, gives
\[
\left[-\kappa_i(N)G_{k_e}(\kappa_i,\psi_e)\right]^{d/e}
=-\chi_i(N)G_L(\chi_i,\psi).
\]
Multiplying yields the useful consistency identity
\[
\beta_O^{d/e}=a(\boldsymbol\chi).
\tag{TR.18}
\]
Formula (TR.18) alone would leave a root-of-unity ambiguity; the calculation (TR.12)–(TR.16) removes it.

## 5. Exact Frobenius block and purity of the invariant space

Choose \(0\ne v_0\) in the tuple line at a representative of \(O\), and put
\(v_j=\Phi^jv_0\) for \(0\le j<e\).
These vectors lie in the \(e\) distinct tuple lines, so they form a basis of the orbit summand of the invariant space. By (TR.16),
\[
\Phi v_j=v_{j+1}\ (j<e-1),\qquad
\Phi v_{e-1}=\beta_Ov_0.
\tag{TR.19}
\]
Consequently
\[
\det(X-\Phi\mid O)=X^e-\beta_O,\qquad
\det(1-T\Phi\mid O)=1-\beta_OT^e.
\tag{TR.20}
\]
The \(e\) eigenvalues are exactly the roots of \(X^e-\beta_O\).
They are distinct because \(\beta_O\ne0\) and the coefficient field has characteristic zero; hence this block is semisimple.
The determinant of the block is \((-1)^{e-1}\beta_O\). That sign belongs to the determinant of a cycle matrix; it is not an extra sign in the Gauss product.
No factors are permuted in the ordered tensor, so there is no Koszul sign. The only cohomological signs in (TR.16) are its \(k\) explicit minus signs.

Over the original base field the complete invariant-space formula is
\[
\det(1-T\operatorname{Fr}_{Q_0}\mid(F_0^{\otimes k})^{I_0})
=
\begin{cases}
\displaystyle\prod_{O\subset\mathcal T_k}
(1-\beta_OT^{|O|}),&kc=0,\\
1,&kc\ne0.
\end{cases}
\tag{TR.21}
\]
Here the product is over the actual arithmetic-Frobenius orbits of the ordered tuples, rather than the characters individually over \(L\).

The exact unscaled Gauss calculation in SPF.28 applies over \(k_e\):
\[
\left|G_{k_e}(\kappa_i,\psi_e)\right|^2=q_e
\]
for every complex embedding. All multiplicative-character values have absolute value one. Hence
\[
|\beta_O|=q_e^{k/2}=Q_0^{ek/2}.
\]
Every eigenvalue \(\alpha\) in (TR.20) therefore has
\[
|\alpha|^e=|\beta_O|,\qquad
|\alpha|=Q_0^{k/2}.
\tag{TR.22}
\]
Thus the nonzero inertia-invariant space in the \(kc=0\) case has exact weight \(k\) under the original geometric \(\operatorname{Fr}_{Q_0}\).
It is neither forced to weight zero nor made zero by \(N_{\log}=0\).

For additional exact orbit counts, if \(f\mid d\) put
\[
g_f=\gcd(N,Q_0^f-1),\qquad
D(f)=\frac{(g_f-1)^k+(g_f-1)(-1)^k}{g_f}.
\tag{TR.23}
\]
The characters fixed by exponent \(Q_0^f\) form the cyclic subgroup of \(X_N\) of order \(g_f\); a tuple fixed by this exponent must have every entry in this subgroup. Applying the proven recurrence (TR.4) inside that subgroup gives exactly \(D(f)\) fixed tuples with product one.
The formula also covers \(g_f=1\), when \(D(f)=0\) because \(k\ge1\).
If \(C(e)\) is the number of orbits of exact length \(e\), then
\[
D(f)=\sum_{e\mid f}eC(e),\qquad
C(e)=\frac1e\sum_{f\mid e}\mu(e/f)D(f).
\tag{TR.24}
\]
The first equality counts each fixed orbit by its number of elements. For the second, multiply the first equality for \(D(f)\) by \(\mu(e/f)\) and sum over \(f\mid e\). For a given divisor \(r\mid e\), the coefficient of \(rC(r)\) is
\(\sum_{r\mid f\mid e}\mu(e/f)\), equal to \(1\) if \(r=e\) and \(0\) otherwise: the sum of the Möbius function over divisors of a nontrivial integer is \(\prod_{p\mid(e/r)}(1-1)=0\).
This proves the exact orbit-count formula.

## Review conclusion

The expected invariant multiplicity is correct. It applies precisely when \(kc=0\), which includes all positive tensor degrees divisible by \(p\) even if \(c\ne0\). The complementary case has full Swan conductor \((N-1)^k\) and zero invariants. In all cases the unipotent logarithm is zero.

The geometric Frobenius label permutation is exponent \(Q_0\). The original-base invariant Frobenius is generally a collection of cycle blocks (TR.19), not a diagonal collection of the \(L\)-scalars. The exact cycle scalars are (TR.16); they require the actual smaller-field source descent (TR.14)–(TR.15), retaining the original denominator \(N\). Formula (TR.21) and weight (TR.22) follow without any unproved root choice.

## Complete read of the resulting TPF.1–33 manuscript

After completing the independent derivation above, I read the entire parent's TPF.1–33 manuscript. No mathematical error was found. The particular checks requested by the parent have the following exact outcomes.

1. **TPF.15:** the action
   \(\lambda_\eta(\zeta)^{-1}\vartheta(-ka)\)
   is correct on the original cover \(z^p-z=bc/v^N\).
   The original trace-\(\vartheta\) sheaf is the
   \(\vartheta^{-1}\)-eigenspace of translation of the torsor coordinate.
   Geometric Frobenius translates the coordinate by the negative of the finite-field trace of its right side, so the two inverses produce the specified positive trace function. Taking the ordered \(k\)th tensor power gives exactly \(\vartheta(-ka)\), with no change of its original numerator.

2. **TPF.20:** the exceptional tame image order \(1\) for \(N=2\), even \(k\), is correct; all other tame image orders are \(N\). For \(N\ge3\), \(k=1\) contains a primitive character, and \(k\ge2\) contains every product character by the positive multiplicities in TPF.18. If the wild character remains nontrivial, equality of a tame scalar and the inverse wild scalar would make that scalar have order dividing both \(N\) and \(p\), hence order one. Thus the product image order is exactly \(h_kp\) in the nonzero-\(kc\) case.

3. **TPF.29–31:** the norm kernel, geometric Frobenius exponent \(Q_0\), original-\(N\) Gauss constant, and cycle determinant signs all agree with the independent derivation above. In particular, for a generator \(g\) of \(L^\times\), the norm kernel is generated by \(g^{Q_0^e-1}\); no exponent has been inverted there.

4. **Requested proof-strengthening:** the pre-TPF.30 paragraph should include the explicit power-map quotient (TR.14) and the character-factor identity following it. This proves the exact source descent morphism instead of stopping at the observation that the idempotent is Galois stable. It leaves all formulas unchanged and retains the original denominator \(N\).

The independent secondary reviewer separately verified all multiplicity, projector, Swan, logarithm, and characteristic-\(p\) cancellation cases. That reviewer also emphasized the correct qualification already present in TPF.16–17: averaging the Kummer subgroup alone does not compute full inertia invariants when the Artin–Schreier factor is nontrivial.
