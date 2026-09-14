# Independent check of the original finite-germ residue identities

This proof uses the original function \(g=2\xi\), original coordinates \(z_\rho=s-\rho\), and original units \(u_\rho\). It does not replace \(g\) by a monomial or change the orientation of its residue pairing. Source: `output/split_zero_rh_tandem_2026-09-12/sources/Tau_Base_Cohomology_2026-09-12/NOTE.md`, read completely, equations \(38\)–\(45\). The source's functional equations are \(g(1-s)=g(s)\) and \(\overline{g(\bar s)}=g(s)\); hence \(g^\dagger=g\). All assertions below concern the actual finite quotients of this \(g\), without a simplicity assertion or an assertion that its zeros lie on the critical line.

## 1. Exact reflected units and the residue form

Let \(Z\) be the specified finite set of actual zeros, stable under \(\iota\rho=1-\bar\rho\). At each point retain

\[
g(\rho+z)=g_\rho(z)=u_\rho(z)z^{m_\rho},\qquad u_\rho(0)\ne0,
\qquad A_\rho=\mathcal O_\rho/(g_\rho)=\mathcal O_\rho/(z^{m_\rho}),
\qquad A=\bigoplus_{\rho\in Z}A_\rho.
\]

The equality of the two ideals identifies quotient rings; it does not remove \(u_\rho\) from the residue denominator or the derivative contraction. Since \(g^\dagger=g\), reflected zeros have equal orders, \(m_{\iota\rho}=m_\rho=:m\), and the exact germ identity is

\[
u_\rho(z)=(-1)^m\overline{u_{\iota\rho}(-\bar z)}.
\tag{G1}
\]

Indeed \(g_\rho(z)=\overline{g_{\iota\rho}(-\bar z)}=(-1)^m\overline{u_{\iota\rho}(-\bar z)}z^m\), and division by \(z^m\) is legitimate as an identity of holomorphic germs. For a tuple of germs define

\[
(f^\dagger)_\rho(z)=\overline{f_{\iota\rho}(-\bar z)}.
\tag{G2}
\]

This is a conjugate-linear involution and preserves the ideal \((g)\), so descends to \(A\). Explicitly, \((c_jz^j)^\dagger=(-1)^j\bar c_jz^j\), with the component reflected. In this notation \(u^\dagger_\rho=(-1)^{m_\rho}u_\rho\), component by component; one must retain this sign even when the orders at distinct reflection orbits differ.

The original pairing is

\[
R(f,h)=\sum_{\rho\in Z}\operatorname{Res}_{z=0}
\frac{(f^\dagger)_\rho(z)h_\rho(z)}{u_\rho(z)z^{m_\rho}}\,dz.
\tag{G3}
\]

It is conjugate-linear in \(f\) and linear in \(h\). Changing \(h\) by a multiple of \(g\) changes the integrand by a holomorphic germ; changing \(f\) by a multiple of \(g\) does the same because \(g^\dagger=g\). Thus it is well-defined on the original quotients.

For a tuple \(b\) of meromorphic germs, reflection of the Laurent coefficient of \(z^{-1}\) gives

\[
\operatorname{Res}_{z=0}(b^\dagger)_\rho(z)\,dz
=-\overline{\operatorname{Res}_{z=0}b_{\iota\rho}(z)\,dz}.
\tag{G4}
\]

Here the minus sign is \((-1)^{-1}\), not a chosen phase. Apply this to \(b=h^\dagger f/g\), use \(b^\dagger=f^\dagger h/g\), and reindex the finite sum by \(\iota\). Then

\[
R(f,h)=-\overline{R(h,f)}.
\tag{G5}
\]

The raw pairing is therefore skew-Hermitian. It is perfect: if \(h\ne0\), choose a nonzero component \(h_\rho\), and let \(k<m_\rho\) be its first nonzero coefficient. Choose \(f\) supported on the reflected component so that \((f^\dagger)_\rho=z^{m_\rho-1-k}\). This is possible by (G2), and (G3) gives \(R(f,h)=h_{\rho,k}/u_\rho(0)\ne0\). Equation (G5) gives nondegeneracy in the other argument too. Finite dimensionality then proves perfectness.

## 2. Dilation, its exact unit, and its residue adjoint

For a positive real number \(q\), set

\[
(C_qf)_\rho(z)=f_\rho(z/q),\qquad
(C_q^{-1}f)_\rho(z)=f_\rho(qz).
\tag{G6}
\]

These are inverse linear maps and algebra automorphisms of every quotient: a multiple of \(z^{m_\rho}\) remains a multiple after either substitution. They are continuous for the canonical finite-dimensional topology. Since \(q\) is real, (G2) directly gives

\[
(C_qf)^\dagger=C_q(f^\dagger),\qquad
(C_q^{-1}f)^\dagger=C_q^{-1}(f^\dagger).
\tag{G7}
\]

Define the actual unit, modulo \(z^{m_\rho}\), by

\[
\kappa_{q,\rho}(z)=q^{1-m_\rho}
\frac{u_\rho(z)}{u_\rho(qz)}.
\tag{G8}
\]

The denominator has nonzero constant term, and this unit has constant term \(q^{1-m_\rho}\ne0\). Its reflection is exactly itself. To see every sign, use (G1) in both numerator and denominator:

\[
\begin{aligned}
(\kappa_q^\dagger)_\rho(z)
&=q^{1-m_\rho}
\frac{\overline{u_{\iota\rho}(-\bar z)}}
     {\overline{u_{\iota\rho}(-q\bar z)}}\\
&=q^{1-m_\rho}
\frac{(-1)^{m_\rho}u_\rho(z)}{(-1)^{m_\rho}u_\rho(qz)}
=\kappa_{q,\rho}(z).
\end{aligned}
\tag{G9}
\]

For each residue in \(R(C_qf,C_qh)\), substitute \(z=qw\). The coordinate differential is \(dz=q\,dw\), and \(z^{m_\rho}=q^{m_\rho}w^{m_\rho}\). Because \(q>0\), a positively oriented small circle maps to a positively oriented small circle. The resulting coefficient identity is

\[
\begin{aligned}
\operatorname{Res}_{z=0}
\frac{(f^\dagger)_\rho(z/q)h_\rho(z/q)}{u_\rho(z)z^{m_\rho}}\,dz
&=\operatorname{Res}_{w=0}
\frac{q^{1-m_\rho}(f^\dagger)_\rho(w)h_\rho(w)}{u_\rho(qw)w^{m_\rho}}\,dw\\
&=\operatorname{Res}_{w=0}
\frac{(f^\dagger)_\rho(w)\kappa_{q,\rho}(w)h_\rho(w)}{u_\rho(w)w^{m_\rho}}\,dw.
\end{aligned}
\tag{G10}
\]

Summing proves

\[
R(C_qf,C_qh)=R(f,M_{\kappa_q}h).
\tag{G11}
\]

The factor \(q^{1-m_\rho}\), including its \(q\) from \(dz\), is indispensable. Define the residue adjoint of a linear endomorphism \(B\) by \(R(Bf,h)=R(f,B^*h)\). Perfectness gives uniqueness and existence. In (G11) replace \(h\) by \(C_q^{-1}h\). This gives the exact order of operations

\[
\boxed{C_q^*=D_q=M_{\kappa_q}C_q^{-1}.}
\tag{G12}
\]

In particular \(D_qC_q=M_{\kappa_q}\). The order must not be exchanged: generally \(C_q^{-1}M_{\kappa_q}=M_{\kappa_q(qz)}C_q^{-1}\). Since (G9) holds, multiplication by \(\kappa_q\) is self-adjoint for \(R\): directly \(R(M_{\kappa_q}f,h)=R(f,M_{\kappa_q}h)\).

## 3. The original derivative contraction is exactly preserved

Let \(J_g=M_{g'}\) on \(A\), retaining the actual derivative with respect to \(s\), equivalently \(z_\rho\) on the \(\rho\)-germ. The exact derivative and its reduction are

\[
g'_\rho(z)=z^{m_\rho}u'_\rho(z)+m_\rho u_\rho(z)z^{m_\rho-1},
\qquad
g'_\rho(z)\equiv m_\rho u_\rho(z)z^{m_\rho-1}\pmod {z^{m_\rho}}.
\tag{G13}
\]

For any germ \(t\), direct evaluation gives

\[
C_q^{-1}M_tC_q=M_{t(qz)}.
\tag{G14}
\]

Combining (G8), (G12), and (G14), the multiplier of \(C_q^*M_{g'}C_q\) on the \(\rho\)-component is \(\kappa_{q,\rho}(z)g'_\rho(qz)\). Before taking the quotient, its exact difference from \(g'_\rho(z)\) is

\[
\kappa_{q,\rho}(z)g'_\rho(qz)-g'_\rho(z)
=z^{m_\rho}\left(
q\,\frac{u_\rho(z)u'_\rho(qz)}{u_\rho(qz)}-u'_\rho(z)
\right).
\tag{G15}
\]

The expression in parentheses is holomorphic. The right side therefore vanishes in the original \(A_\rho\), proving, on the whole finite packet,

\[
\boxed{C_q^*M_{g'}C_q=M_{g'}.}
\tag{G16}
\]

No unrecorded monomial replacement of \(g\) is used in this proof.

For completeness the contracted pairing is

\[
S(f,h):=R(f,M_{g'}h)
=\sum_{\rho\in Z}m_\rho\overline{f_{\iota\rho}(0)}h_\rho(0).
\tag{G17}
\]

Indeed \(g'/g=m_\rho/z+u'_\rho/u_\rho\), whose second term is holomorphic. Multiplication by \(f^\dagger h\) leaves just the displayed constant term as residue. Multiplication by \(f^\dagger h\) on \(A_\rho\), in the basis \(1,z,\ldots,z^{m_\rho-1}\), is triangular with that same constant term on all \(m_\rho\) diagonal entries. Thus (G17) is also exactly the source trace \(\operatorname{Tr}(M_{f^\dagger h}|A)\), including every original multiplicity.

Unlike \(R\), \(S\) is Hermitian. One proof is to conjugate (G17) and reindex by \(\iota\), using equal reflected multiplicities. A second proof records the derivative sign: differentiation of \(g^\dagger=g\) gives \((g')^\dagger=-g'\). Consequently \(M_{g'}^*=-M_{g'}\); combining this with the skew-Hermitian sign of \(R\) gives the Hermitian sign of \(S\). Neither step multiplies a form by a phase. Equation (G16) says exactly

\[
S(C_qf,C_qh)=S(f,h).
\tag{G18}
\]

Let \(N\) be componentwise multiplication by \(z_\rho\). Then the two radicals of \(S\) are both

\[
\operatorname{rad}S=NA=\bigoplus_{\rho\in Z}z_\rho A_\rho.
\tag{G19}
\]

Every element of this subspace has zero residue values and annihilates (G17). Conversely, any nonzero residue value of \(h\) can be paired with a tuple having only the corresponding reflected residue value nonzero, and the nonzero integer \(m_\rho\) makes the result nonzero. This proves the converse without a simplicity assumption. The quotient is \(A/NA=\bigoplus_\rho\mathbb C\) with its exact multiplicity-weighted reflection pairing. At a reflection-fixed zero its contribution is \(m_\rho\bar f_\rho h_\rho\). A two-point reflection orbit contributes \(m_\rho(\bar f_{\iota\rho}h_\rho+\bar f_\rho h_{\iota\rho})\), whose matrix has eigenvalues \(m_\rho,-m_\rho\). This describes the form's exact signature from the actual chosen packet; it makes no assertion about which such orbits occur among all zeros.

Equations (G11) and (G18) are different conclusions. If some actual \(m_\rho>1\) and \(q\ne1\), the constant term \(q^{1-m_\rho}\ne1\) in (G8) shows \(M_{\kappa_q}\ne1\). Perfectness of \(R\) then shows \(C_q\) does not preserve \(R\). If every chosen zero is simple, all local algebras are constants, \(C_q=1\), and \(\kappa_q=1\) in their quotients. The preserved trace form does not assert preservation of the full jet pairing at a multiple zero.

## 4. Actual scaling and the scope of the simultaneous-intertwiner obstruction

Retain the original positive-real action

\[
U_a|_{A_\rho}=a^\rho\exp((\log a)N_\rho),
\qquad a>0,\qquad a^\rho=\exp(\rho\log a),
\tag{G20}
\]

Here the logarithm is real and the nilpotent exponential retains every term up to its actual nilpotency order. Multiplication by the germ \(a^{\rho+z}\) is exactly this action. Reflection changes this germ on the paired component to \(a^{1-\rho-z}\). Thus, before passing to the quotient, the two multipliers in the residue integrand have product \(a\):

\[
(U_af)^\dagger_\rho(z)=a^{1-\rho-z}(f^\dagger)_\rho(z),
\qquad
R(U_af,U_ah)=aR(f,h),
\qquad
U_a^*=aU_a^{-1}.
\tag{G20a}
\]

The last identity follows from perfectness, by replacing \(h\) by \(U_a^{-1}h\). Likewise the reflected coordinate is \(-z_\rho\), so \(N^*=-N\). These formulas retain the original target line of weight \(a\), rather than changing it to the trivial line. Directly from (G6),

\[
C_qN=q^{-1}NC_q,\qquad
C_qNC_q^{-1}=q^{-1}N,
\tag{G21}
\]

and hence

\[
\begin{aligned}
F_{q,a}|_{A_\rho}
:=(C_qU_aC_q^{-1})|_{A_\rho}
&=a^\rho\exp((\log a)N_\rho/q)\\
&=a^{\rho(1-1/q)}U_{a^{1/q}}|_{A_\rho}.
\end{aligned}
\tag{G22}
\]

The factor \(a^{\rho(1-1/q)}\) depends on the original zero. The dilation fixes each zero's centre and scales only its local coordinate; discarding this scalar would change the original action. Both \(U_a\) and \(F_{q,a}\) commute with \(N\), since they are polynomials in \(N\) times a scalar on each component. In particular

\[
F_{q,a}NF_{q,a}^{-1}=N,
\tag{G23}
\]

whereas \(C_qNC_q^{-1}=q^{-1}N\). Thus the coordinate dilation itself and its conjugate of the arithmetic action have different, now explicitly calculated, relations to \(N\).

Here is the exact obstruction for the stricter proposed morphism. Let \(D\) be a complex vector space, \(N_D\in\operatorname{End}_{\mathbb C}(D)\), and \(F\in\operatorname{Aut}_{\mathbb C}(D)\) with

\[
FN_DF^{-1}=q^{-1}N_D,\qquad q>0,\quad q\ne1.
\tag{G24}
\]

Fix any positive \(a\). A linear map \(T:A\to D\) that is simultaneously an ordinary intertwiner for the two displayed operators means precisely

\[
TU_a=FT,\qquad TN=N_DT.
\tag{G25}
\]

The full source operators commute: \(U_aN=NU_a\), directly from (G20). Therefore

\[
FN_DT=FTN=TU_aN=TNU_a=N_DTU_a=N_DFT.
\tag{G26}
\]

On the other hand, (G24) gives \(FN_DT=q^{-1}N_DFT\). Subtracting from (G26) proves \((1-q^{-1})N_DFT=0\), so \(N_DFT=0\). Substituting \(FT=TU_a\) and composing with the actual inverse \(U_a^{-1}=U_{1/a}\) proves

\[
\boxed{N_DT=TN=0.}
\tag{G27}
\]

Consequently \(T\) has the unique exact factorization

\[
A\xrightarrow{\pi}A/NA
\xrightarrow{\overline T}\ker N_D
\hookrightarrow D,\qquad
\overline T([x])=Tx.
\tag{G28}
\]

Well-definedness follows from \(T(NA)=0\); the image lies in the indicated kernel by (G27); uniqueness follows from surjectivity of \(\pi\). The operator \(U_a\) descends to \(\overline U_a|_\rho=a^\rho\) on \(A/NA\). The subspace \(\ker N_D\) is stable under \(F\), since \(N_DF=qFN_D\). Equations (G25) give \(\overline T\,\overline U_a=F|_{\ker N_D}\,\overline T\). Conversely, every map \(\overline T:A/NA\to\ker N_D\) satisfying this last equality produces a simultaneous intertwiner (G25) by (G28), because both sides of its nilpotent intertwining equality then vanish. Thus this is a complete description of those maps, not only a necessary obstruction.

The conclusion does not set \(NA=0\) in the source. It states that these particular simultaneous maps kill it. If an actual zero has multiplicity greater than one, \(N\ne0\) on that component, so such a \(T\) cannot be injective there. If all chosen zeros are simple, this nilpotent obstruction is empty. It neither removes the original quotient \(A\) nor removes the source's \(Q\to A\) or residue-induced injection into its computed \(K_\tau\)-dual.

The stronger surviving exact map on all original jets is the invertible \(C_q\) already constructed: it satisfies

\[
C_qU_a=F_{q,a}C_q,
\qquad C_qN=(q^{-1}N)C_q,
\tag{G29}
\]

so is a genuine isomorphism from the commuting representation \((A,U_a,N)\) to the commuting representation \((A,F_{q,a},q^{-1}N)\). It has the residue adjoint (G12), preserves the actual derivative contraction by (G16), and preserves every original zero, multiplicity, and jet. Equation (G23) proves that its target pair does not acquire relation (G24) merely by conjugation. These formulas give the exact surviving correspondence and the exact scope of the failed literal intertwiner.

## Verification record

The proof above is an independent direct algebra check, using the complete primary note rather than a successor's interpretation. Its chain of equalities supplies all signs, residue Jacobians, quotient remainders, maps, inverses, and radical calculations. No Lean, Lake, or Elan process was started.

The accompanying verify_germ_pairing.py passed eight exact symbolic fixtures: orders \(m=1,2,3,4\) and dilation factors \(q=2,3/2\), each with paired nonconstant complex units satisfying (G1). It checks the skew residue sign, perfectness, Hermitian trace sign, trace rank and radical, full Jacobian, adjoint, derivative contraction, nilpotent conjugation, trace invariance, and dagger compatibility. Mutation controls reject omission of the residue Jacobian, reversal of adjoint factors, and a false full-residue isometry. GERM_PAIRING_CHECK_RECEIPT.json records the result. These fixtures are formal local regression examples; they assert no actual zero multiplicity and do not replace the proofs above.
