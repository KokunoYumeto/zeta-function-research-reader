# Finite residue orientation and the exact right-adjoint injection

## Provenance and bounded scope

This is the independent residue calculation requested by the parent proof lane. The parent retains the complete verbatim session inputs in `work/tau_f1_transcript_audit_20260913/USER_INPUTS.md`; its `exact_continuation/LOGBOOK.md` records the surrounding proof workflow.

Delegated instruction (verbatim):

> Bounded independent algebra calculation. Read NOTE.md section 6 completely (already in context) and derive exact finite residue pairing orientation and injection (43), with full nilpotent jets g=u(z)z^m. Check reflection signs for raw R, trace R(f,g'h), equivariance aL1 inverse action, and its placement in H^-1 RHom(T,K). No browser, Lean, root gamma/purity duplication, or source edits. Write only work/tau_f1_transcript_audit_20260913/exact_continuation/residue_sign_check.md if useful; send precise formulas and any genuine sign correction. Parent handles general fibre and tensor proof.

Read the entire retained `output/split_zero_rh_tandem_2026-09-12/sources/Tau_Base_Cohomology_2026-09-12/NOTE.md`, SHA256 `d03e71ad18f187bd89880cb8ca6fc9c5d6f260b3de8e8e5702c27db97e7b63c3`, including equations (38)–(45). Also read lines 490–795 of its dependency `sources/Split_Support_Actual_Comparison__CONTINUATION.tex`, SHA256 `98e8aaa63b1f7ee4661c043cd985ca274646b749f36d23d2ec46cbc4b0737dc5`. That window includes the actual generator, finite interpolation and the original local residue matrix. Neither source was edited. No browser or Lean process was used.

The results below validate the signs in NOTE.md (42)–(45). They also specify the exact radical of the trace contraction and show why the raw pairing still detects every nilpotent jet. They establish a finite, continuous family of functionals inside the source's algebraic right-adjoint dual; they do not identify an algebraic dual with the whole continuous dual.

## 1. Objects, coordinates and symmetry

Retain the original function

\[
g(s)=2\xi(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

Its holomorphic continuation obeys

\[
g(1-s)=g(s),\qquad g(\bar s)=\overline{g(s)},\qquad
g^\dagger(s):=\overline{g(1-\bar s)}=g(s).
\tag{R1}
\]

For completeness, these symmetry signs follow directly from the retained Gaussian Poisson identity. Put \(\psi(t)=\sum_{n\geq1}e^{-\pi n^2t}\). Poisson gives

\[
\psi(t)=t^{-1/2}\psi(1/t)+\tfrac12(t^{-1/2}-1).
\]

For \(\Re s>1\), integration term by term gives

\[
\pi^{-s/2}\Gamma(s/2)\zeta(s)
=\int_0^\infty\psi(t)t^{s/2}\frac{dt}{t}.
\]

Splitting at 1 and substituting \(t=1/v\) in the reflected term yields

\[
g(s)=1+s(s-1)\int_1^\infty\psi(t)
\bigl(t^{s/2}+t^{(1-s)/2}\bigr)\frac{dt}{t}.
\tag{R2}
\]

The constant is exactly 1 because
\(\frac12\int_0^1(t^{(s-1)/2}-t^{s/2})dt/t
=1/(s-1)-1/s=1/[s(s-1)]\).
For \(t\geq1\), \(\psi(t)\leq e^{-\pi t}/(1-e^{-\pi t})\), since \(n^2\geq n\). Thus the integral and all its derivatives in \(s\) converge uniformly on compact subsets of the plane. It is entire. Its expression is invariant under \(s\mapsto1-s\), and its real integrand coefficients give conjugation invariance. This proves (R1), with the original factor 2 in \(g=2\xi\).

Let \(Z\) be a finite set of actual zeros stable under
\(\iota\rho=1-\bar\rho\). Retain each actual order \(m_\rho\), the original coordinate \(z_\rho=s-\rho\), and the actual nonvanishing holomorphic unit

\[
g(\rho+z)=u_\rho(z)z^{m_\rho},\qquad u_\rho(0)\ne0.
\tag{R3}
\]

Equation (R1) implies \(m_{\iota\rho}=m_\rho\) and, with \(m=m_\rho\),

\[
u_\rho(z)=(-1)^m\overline{u_{\iota\rho}(-\bar z)}.
\tag{R4}
\]

Indeed inserting (R3) for \(g\) at \(\iota\rho\) into
\(g(\rho+z)=\overline{g(\iota\rho-\bar z)}\) gives this equation and the equality of vanishing orders.

Write

\[
A_Z=\bigoplus_{\rho\in Z}A_\rho,\qquad
A_\rho=\mathcal O_\rho/(g),\qquad
f_\rho(z)=\sum_{j=0}^{m_\rho-1}f_{\rho,j}z^j.
\]

Using the equality of ideals \((u_\rho z^{m_\rho})=(z^{m_\rho})\) represents classes by these unique polynomials. It does not replace the denominator \(g\) by \(z^{m_\rho}\) in any pairing. Define the conjugate-linear involution by

\[
(f^\dagger)_\rho(z)=\sum_{j=0}^{m_\rho-1}
(-1)^j\overline{f_{\iota\rho,j}}z^j.
\tag{R5}
\]

The equality \(g^\dagger=g\) proves that this is independent of germ representatives. Applying it twice gives \(f\) because \(\iota^2\rho=\rho\) and \((-1)^{2j}=1\). It preserves multiplication.

## 2. The complete residue matrix and perfectness

Retain

\[
R_Z(f,h)=\sum_{\rho\in Z}\operatorname{Res}_{s=\rho}
\frac{f^\dagger(s)h(s)}{g(s)}\,ds.
\tag{R6}
\]

Changing \(h\) by a multiple of \(g\) adds a holomorphic differential; changing \(f\) by a multiple of \(g\) does the same by (R1). Thus (R6) is well-defined on the specified quotient and is conjugate-linear in \(f\), linear in \(h\).

Set \(v_\rho(z)=u_\rho(z)^{-1}=\sum_{\ell\geq0}v_{\rho,\ell}z^\ell\), retaining all its required Taylor coefficients. Direct coefficient extraction gives

\[
R_Z(f,h)=\sum_{\rho\in Z}
\sum_{\substack{0\leq j,k<m_\rho\\j+k\leq m_\rho-1}}
(-1)^j\overline{f_{\iota\rho,j}}\,
h_{\rho,k}\,v_{\rho,m_\rho-1-j-k}.
\tag{R7}
\]

The block pairing the coefficients of \(\overline{f_{\iota\rho}}\) with those of \(h_\rho\) has matrix

\[
B_\rho(j,k)=(-1)^jv_{\rho,m-1-j-k},\quad 0\leq j,k<m,
\]

where a negative coefficient index denotes zero. In the determinant, a nonzero permutation term must satisfy \(j+\pi(j)\leq m-1\) for every \(j\). Summing these inequalities forces equality in each, hence \(\pi(j)=m-1-j\). Consequently

\[
\det B_\rho
=(-1)^{m(m-1)/2}\prod_{j=0}^{m-1}(-1)^jv_{\rho,0}
=u_\rho(0)^{-m}\ne0.
\tag{R8}
\]

The permutation of blocks by \(\iota\) is invertible. Thus (R6) is perfect on the full \(A_Z\). This determinant includes both the reversal sign and every reflection sign; the familiar determinant \((-1)^{m(m-1)/2}u_\rho(0)^{-m}\) without reflection belongs to the bilinear residue matrix, which is a different matrix.

A direct witness also displays the nilpotent information. Suppose \(f_{\iota\rho,j_0}\ne0\) and all coefficients of \(f_{\iota\rho}\) below \(j_0\) vanish. Take \(h\) to be zero on all other summands and take

\[
h_\rho(z)=[u_\rho(z)z^{m-1-j_0}]\in A_\rho.
\]

Then, with the same actual unit,

\[
R_Z(f,h)=(-1)^{j_0}\overline{f_{\iota\rho,j_0}}\ne0.
\tag{R9}
\]

Indeed the unit cancels inside this particular residue expression, leaving the coefficient of \(z^{j_0}\) in \(f^\dagger\); coefficients above \(j_0\) become holomorphic and coefficients below it are zero. A positive-order jet is therefore not in the radical of the raw form.

## 3. Raw orientation and multiplier adjoints

For a meromorphic germ \(k\), a Laurent term \(c_nw^n\) at \(\iota\rho\) becomes \((-1)^n\bar c_nz^n\) under reflection. In particular its residue term changes sign:

\[
\operatorname{Res}_{\rho}k^\dagger(s)\,ds
=-\overline{\operatorname{Res}_{\iota\rho}k(s)\,ds}.
\tag{R10}
\]

Apply (R10) to \(k=h^\dagger f/g\), then sum over the reflection-stable set. Since \(k^\dagger=f^\dagger h/g\),

\[
\boxed{R_Z(f,h)=-\overline{R_Z(h,f)}.}
\tag{R11}
\]

This proves the source's raw skew-Hermitian orientation. No phase has been inserted.

For any multiplier \(b\in A_Z\), multiplication and (R5) give the exact adjoint formula

\[
R_Z(M_bf,h)=R_Z(f,M_{b^\dagger}h).
\tag{R12}
\]

Differentiating \(g^\dagger=g\) in the original coordinate gives

\[
(g')^\dagger=-g'.
\tag{R13}
\]

The minus sign here is essential. It is the sign which changes the orientation after the trace contraction.

## 4. Trace contraction, radicals and exact finite signature

Let \(J_g=M_{g'}:A_Z\to A_Z\), exactly as in the source. From (R3),

\[
g'(\rho+z)=u'_\rho(z)z^m+m u_\rho(z)z^{m-1},
\]

so its class is

\[
[g']_\rho=[m u_\rho(z)z^{m-1}]
=m u_\rho(0)z^{m-1}.
\tag{R14}
\]

Both equalities are in the original quotient; the omitted term in the first equality is explicitly a multiple of \(z^m\). For every \(h_\rho\),

\[
(J_gh)_\rho=m u_\rho(0)h_\rho(0)z^{m-1}.
\tag{R15}
\]

Since \(m\ne0\) in \(\mathbb C\) and \(u_\rho(0)\ne0\),

\[
\ker J_g=\bigoplus_{\rho\in Z}z_\rho A_\rho,
\qquad
\operatorname{im}J_g=\bigoplus_{\rho\in Z}\mathbb C\,u_\rho(0)z_\rho^{m_\rho-1}.
\tag{R16}
\]

This includes \(m_\rho=1\): that kernel summand is zero and that image summand is all \(A_\rho\).

Define the contracted form \(T_Z(f,h)=R_Z(f,J_gh)\). The exact logarithmic derivative is

\[
\frac{g'}{g}=\frac{m}{z}+\frac{u'_\rho}{u_\rho}.
\]

The second term is holomorphic, so

\[
\boxed{T_Z(f,h)=\sum_{\rho\in Z}m_\rho
\overline{f_{\iota\rho}(0)}h_\rho(0).}
\tag{R17}
\]

Multiplication by an element \(b\) in the ordered monomial basis of \(A_\rho\) is triangular with every diagonal entry \(b_\rho(0)\): the coefficient of \(z^j\) in \(bz^j\) is exactly \(b_\rho(0)\), and no term has degree below \(j\). Therefore

\[
T_Z(f,h)=\operatorname{Tr}(M_{f^\dagger h}|A_Z).
\tag{R18}
\]

To verify the orientation without dropping a sign, combine (R11)–(R13):

\[
\overline{T_Z(h,f)}=-R_Z(J_gf,h)
=-R_Z(f,M_{(g')^\dagger}h)=R_Z(f,J_gh)=T_Z(f,h).
\tag{R19}
\]

Thus the trace form is Hermitian. Its left and right radicals are both exactly the ideal in (R16). In the right variable this follows from perfectness of \(R_Z\) and the identity \(T_Z(f,h)=R_Z(f,J_gh)\); Hermitian symmetry gives the left radical. Alternatively (R17) and the independent coordinate values prove both statements directly.

Here “zero value” means \(f_\rho(0)=f(\rho)=0\), not zero residue against every test in (R6). The quotient by the trace radical is the value algebra \(\bigoplus_\rho\mathbb C\); raw duality (R6) precedes this quotient and remains perfect on the full jets.

The finite signature is also completely determined. A fixed point \(\rho=\iota\rho\) has \(\Re\rho=1/2\), and its value form is \(m_\rho\bar f_\rho h_\rho\). A two-element orbit \(\{\rho,\iota\rho\}\), with its common multiplicity \(m\), has value matrix

\[
\begin{pmatrix}0&m\\m&0\end{pmatrix}.
\]

On the unscaled vectors \(e_\rho+e_{\iota\rho}\) and \(e_\rho-e_{\iota\rho}\), the diagonal values are \(2m\) and \(-2m\), and their cross pairing is zero. Thus each fixed orbit contributes one positive direction, each two-element orbit contributes one positive and one negative direction, and the nullity of the full form is exactly \(\sum_\rho(m_\rho-1)\). This is a calculation for the stated finite packet, not an assertion that the actual full divisor has only fixed orbits.

## 5. The original scaling, including its nilpotent part

For \(a>0\), retain \(U_aF(x)=F(x/a)\). Substitution \(x=at\) in the Mellin integral proves

\[
\mathcal M(U_aF)(s)=a^s\mathcal MF(s).
\]

Accordingly on \(A_\rho\),

\[
U_a=M_{a^s}=a^\rho\sum_{j=0}^{m_\rho-1}
\frac{(\log a)^j}{j!}N_\rho^j,
\qquad N_\rho z^k=z^{k+1},\qquad N_\rho^{m_\rho}=0.
\tag{R20}
\]

As \(a\) is positive, \(\log a\) is real and

\[
(a^s)^\dagger=a^{1-s}=a(a^s)^{-1}.
\]

Equation (R12) therefore gives, retaining the complete matrix in (R20),

\[
R_Z(U_af,U_ah)=aR_Z(f,h).
\tag{R21}
\]

All multiplication operators commute, hence \(J_gU_a=U_aJ_g\) and
\(T_Z(U_af,U_ah)=aT_Z(f,h)\). At the generator level \(s^\dagger=1-s\), so

\[
R_Z(M_sf,h)+R_Z(f,M_sh)=R_Z(f,h).
\tag{R22}
\]

In the local cross block the scalar identity is
\(\overline{\iota\rho}=1-\rho\), and the remaining identity is
\(R_Z(N_{\iota\rho}f,h)=-R_Z(f,N_\rho h)\).
This explicitly retains the nilpotent reflection sign.

## 6. Finite Mellin interpolation with the original test topology

The source spaces are

\[
V=\{\phi\in\mathcal S(\mathbb R):\phi\text{ even},\ \phi(0)=0,\ \widehat\phi(0)=0\},
\]

\[
\mathscr B=\{F\in C^\infty(\mathbb R_{>0}):
p_{b,k}(F):=\sup_{x>0}x^b|(-x\partial_x)^kF(x)|<\infty
\text{ for all }b\in\mathbb Z,k\geq0\}.
\]

The finite coefficient functionals are

\[
\ell_{\rho,j}(F)=\frac1{j!}\int_0^\infty
F(x)x^\rho(\log x)^j\frac{dx}{x},\quad0\leq j<m_\rho.
\tag{R23}
\]

If integers \(b_-<\Re\rho<b_+\) are retained, direct absolute integration on \((0,1)\) and \((1,\infty)\) gives

\[
|\ell_{\rho,j}(F)|\leq
\frac{p_{b_-,0}(F)}{(\Re\rho-b_-)^{j+1}}+
\frac{p_{b_+,0}(F)}{(b_+-\Re\rho)^{j+1}}.
\tag{R24}
\]

The same estimates uniformly on any compact \(s\)-set permit differentiation under the integral to every order. Thus \(\mathcal MF\) is entire, and (R23) is its Taylor coefficient with the stated \(1/j!\). In particular each finite jet is continuous for the original seminorms; there has been no replacement of the test topology.

To prove surjectivity constructively, fix any \(R>0\), put

\[
\eta_R(y)=\begin{cases}\exp[-1/(R^2-y^2)]&|y|<R,\\0&|y|\geq R,\end{cases}
\quad
r_{\rho,j}(x)=x^{\bar\rho-1}(\log x)^j/j!,
\]

and index jets by \(\alpha=(\rho,j)\). Retain the exact matrix

\[
B^R_{\alpha\beta}=
\frac1{j!k!}\int_{-R}^R\eta_R(y)
e^{(\rho+\bar\sigma-1)y}y^{j+k}\,dy,
\quad\beta=(\sigma,k).
\tag{R25}
\]

For a coefficient vector \(c\),

\[
c^*B^Rc=\int_{-R}^R\eta_R(y)e^{-y}
\left|\sum_{\alpha=(\rho,j)}\bar c_\alpha e^{\rho y}y^j/j!\right|^2dy.
\]

The exponential polynomials \(e^{\rho y}y^j\) are linearly independent on this interval. Indeed, to isolate an exponent \(\rho\), apply
\(\prod_{\sigma\ne\rho}(\partial_y-\sigma)^{m_\sigma}\).
It kills all other blocks. On the remaining block it is \(e^{\rho y}\) times a product of invertible operators \(\partial_y+\rho-\sigma\) on the polynomials of degree less than \(m_\rho\). For a nonzero constant \(c\), the inverse of \(\partial_y+c\) on that space is the finite sum
\(\sum_{k=0}^{m_\rho-1}(-\partial_y)^k/c^{k+1}\).
The remaining polynomial must therefore be zero. Repeating for each \(\rho\) proves independence. A nonzero such analytic function is nonzero on an open subinterval, so the displayed positive integral is strictly positive. Hence \(B^R\) is invertible.

For every prescribed jet vector \(v\), define the actual function

\[
F_v(x)=\eta_R(\log x)\sum_\beta((B^R)^{-1}v)_\beta r_\beta(x).
\tag{R26}
\]

It is smooth, supported on \([e^{-R},e^R]\), and belongs to \(\mathscr B\). Substitution of (R26) into (R23) gives exactly \(J_ZF_v=B^R(B^R)^{-1}v=v\). If support strictly inside \((e^{-R},e^R)\) is required, retain any explicitly chosen \(0<R'<R\) in (R25)–(R26). Thus this right inverse establishes surjectivity without assuming any zero locations, zero simplicity or vanishing of an uncomputed kernel.

Retain the source identity \(\mathcal M\Theta\phi=gH_\phi\), with \(H_\phi\) entire. It proves that \(J_Z\) annihilates \(\Theta V\). Thus the surjective map just constructed factors as

\[
q_Z:Q=\mathscr B/\Theta V\longrightarrow A_Z.
\tag{R27}
\]

Continuity (R24) also implies annihilation of the closure of \(\Theta V\), without identifying that closure with the original algebraic image. On either specified quotient, the induced finite map is continuous in its quotient topology. The adjunction below uses the algebraic quotient \(Q\) of the retained source.

## 7. The degree, the cochain differential and the actual injection

For the actual sheaf \(\mathcal T\) on \(+, -<\eta<\sigma\), retain

\[
C:=\mathsf A_\tau(\mathcal T)
=[V\oplus V\xrightarrow{d}\mathscr B],\quad
d(\phi,\psi)=\Theta\phi-J\Theta\psi,
\]

in cohomological degrees 0 and 1. Since \(J\Theta\psi=\Theta\widehat\psi\) and the Fourier transform preserves \(V\), its image is precisely \(\Theta V\): inclusion into that subspace follows from the equality, and the first leg already gives every element \(\Theta V\). Thus \(H^1(C)=Q\).

For \(W=\mathcal L_1\), a one-dimensional complex coefficient space with action \(a\), the computed injective complex is

\[
K_\tau(W)=
[I_\eta(W)\xrightarrow{(+\mathrm{res},-\mathrm{res})}I_+(W)\oplus I_-(W)]
\]

in degrees \(-1,0\). Evaluation against the sheaf \(\mathcal T\) gives

\[
R\operatorname{Hom}_{\mathcal A}(\mathcal T,K_\tau(W))
\simeq
[\operatorname{Hom}_{\mathbb C}(\mathscr B,W)
\xrightarrow{\ell\mapsto(\ell\Theta,-\ell J\Theta)}
\operatorname{Hom}_{\mathbb C}(V,W)^{\oplus2}].
\tag{R28}
\]

There is no degree \(-2\) term. The differential in (R28) has a plus in front of precomposition with \(d\). This also follows from the standard Hom rule

\[
d_{\operatorname{Hom}}(\ell)=d_W\ell-(-1)^{|\ell|}\ell d_C:
\quad |\ell|=-1\implies d_{\operatorname{Hom}}\ell=+\ell d_C.
\]

Consequently

\[
H^{-1}R\operatorname{Hom}_{\mathcal A}(\mathcal T,K_\tau(W))
=\{\ell:\mathscr B\to W\mid\ell(\Theta V)=0\}
\cong\operatorname{Hom}_{\mathbb C}(Q,W).
\tag{R29}
\]

Let \(\overline{A_Z}\) denote the conjugate vector space, so
\(\lambda\cdot\bar f=\overline{\bar\lambda f}\). Define

\[
\Phi_Z:\overline{A_Z}\longrightarrow\operatorname{Hom}_{\mathbb C}(Q,\mathcal L_1),
\quad
\Phi_Z(\bar f)([F])=
\sum_{\rho\in Z}\operatorname{Res}_\rho
\frac{f^\dagger(s)\mathcal MF(s)}{g(s)}\,ds.
\tag{R30}
\]

The coefficient line here is exactly the source's moment line; scalars on the right are read in that same line. Formula (R30) is linear in \(\bar f\): replacing \(f\) by \(\bar\lambda f\) multiplies its dagger and hence the functional by \(\lambda\). It is linear in \([F]\). Replacing \(F\) by \(F+\Theta\phi\) adds the residue of the holomorphic germ \(f^\dagger H_\phi\), so it is well-defined. This argument also proves directly that its cochain in (R28) is closed.

The formula factors as the three actual maps

\[
\overline{A_Z}\xrightarrow{\ f\mapsto R_Z(f,-)\ }A_Z^*
\xrightarrow{\ q_Z^*\ }Q^*
\cong H^{-1}R\operatorname{Hom}_{\mathcal A}(\mathcal T,K_\tau(\mathcal L_1)).
\tag{R31}
\]

The first is an isomorphism by (R8), and the second is injective by the surjectivity proved in (R26)–(R27). More explicitly, for nonzero \(f\), choose the actual detecting jet \(h\) in (R9), then choose \(F_h\) in (R26). Formula (R30) takes the nonzero value (R9) on \([F_h]\). This proves injectivity without losing any nilpotent order.

The sheaf map \(\mathcal T\to S_\eta A_Z\) is zero at the other stalks and \(J_Z\) at \(\eta\). Its arrow compatibility is exactly \(J_Z\Theta=J_ZJ\Theta=0\). Global cohomology of \(S_\eta A_Z\) is \(A_Z[-1]\), which has \(A_Z\) in degree 1. Dualizing therefore puts \(A_Z^*\) in degree \(-1\), namely \(A_Z^*[1]\). This verifies the degree in (43) at the sheaf and complex levels, with no unstated shift or extra sign.

By (R24) and the finite formula (R7), each functional (R30) is continuous on the original \(\mathscr B\) and on its indicated quotient. Thus (R31) lands in continuous functionals inside the algebraic Hom space. Nothing in this argument asserts that all elements of the latter space are continuous.

## 8. Equivariance into the second-moment dual

The action on \(Q\) is the action induced by \(U_aF(x)=F(x/a)\); the full two-leg action on the original source is
\((\phi,\psi)\mapsto(U_a\phi,aU_{1/a}\psi)\).
The source identity \(U_aJ=aJU_{1/a}\) makes its differential commute with the action. Also \(q_ZU_a=U_aq_Z\) by (R20).

Give \(\overline{A_Z}\) its conjugate action \(\bar U_a\bar f=\overline{U_af}\), and retain on the target the action induced by the moment line:

\[
(U_a\ell)(q)=a\ell(U_a^{-1}q).
\tag{R32}
\]

Then for every \(q\in Q\), equations (R21) and (R27) give

\[
\begin{aligned}
\Phi_Z(\overline{U_af})(q)
&=R_Z(U_af,q_Zq)\\
&=aR_Z(f,U_a^{-1}q_Zq)\\
&=a\Phi_Z(\bar f)(U_a^{-1}q)\\
&=(U_a\Phi_Z(\bar f))(q).
\end{aligned}
\tag{R33}
\]

This proves equivariance for the original action, the complete nilpotent jets, and the original second-moment factor \(a\). Replacing the factor \(a\) by 1 would change the target representation and would break (R33).

## 9. Exact conclusion for integration

The raw residue form in NOTE.md (42) is correctly skew-Hermitian. The contraction in (45) is correctly Hermitian because \((g')^\dagger=-g'\). The original injection (43) is a linear, injective, equivariant map from the conjugate full finite packet into degree \(-1\) of the computed right-adjoint Hom complex. It has no missing phase or degree sign.

Its finite source retains all actual units and nilpotents. Passing to the trace form is the explicit endomorphism \(J_g=M_{g'}\), with kernel \(\bigoplus z_\rho A_\rho\); this is the precise operation that makes positive-order jets invisible. On any retained support label, a zero value under one of these linear maps is the supported zero of that label, not the external absorbing element. The parent proof handles the complete support-transport diagrams.

The completed finite interpolation also supplies an explicit function detecting any nonzero full jet through (R30). It supplies no uniform estimate as the zero packet, multiplicities or cutoff grow: the exact inverse matrix \((B^R)^{-1}\) remains in (R26), and no bound for it has been assumed. This is the exact extent of the completed calculation relevant to subsequent analytic control.
