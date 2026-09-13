# Independent proof audit: arithmetic reflection parity and frontier control

Date: 2026-09-12. Reviewer lane: `frontier_parity_review`.

Verdict: the proposed sharpening is proved for the stated actual packet,
canonical total-degree source, and original arithmetic metric. The factor
`2` in the source estimate (4.8) disappears because its two frontier maps
have opposite **linear reflection parity**. The entire cross matrix is
retained below. Its determinant supplies a further upper bound; it does
not replace that matrix. No estimate uniform in tensor degree is asserted.

## 1. Evidence read and precise scope

The source `sources/web_symmetric_frontier_delivery/Tau_Symmetric_Frontier_Control/NOTE.tex`
was read with particular attention to every definition and proof in
sections 1–4, including (2.1)–(2.7), (3.1)–(3.8), (4.1)–(4.8).
Its SHA-256 at this audit is
`734b6c935892ebd9d18b506f6b592f1ca3489afcb95d5c669a489f4ca04656cf`.

The existing cumulative proofs used for the source bridge were also read:

* `tex/coherent_tensor_integration.tex`, reflection and joint source
  (CT.8)–(CT.16b), SHA-256
  `0223362bc1a9dccf31f42e0b59187d9ab63269ab42d2c5dd19613a03d695e1f9`;
* `tex/kernel_terminal_continuation.tex`, full proof of (KT.28), SHA-256
  `6932e3c4d350aece95c003083d8938668d60bd81b2ebceba6eb1b78a510b2e9f`;
* `tex/arithmetic_moments.tex`, original linear Hilbert reflection
  (AM.3)–(AM.4), SHA-256
  `9523452478397aea57c8e0c88ad88c814a0e7c5372b7398111e03eb438720379`.

This is a written proof audit. It is not a Lean receipt or an assertion
that all analytic source statements have been formalized. The source
construction of the actual theta representative is retained, rather
than inferred from a finite Gaussian calibration.

## 2. Original objects and exact reflection maps

Let the actual finite nonempty divisor of zeros of `g=2 xi` be closed,
with all multiplicities, under both `rho -> conjugate(rho)` and
`rho -> 1-conjugate(rho)`. Their composite is `rho -> 1-rho`.
Write

\[
 h(s)=\prod_\rho(s-\rho)^{m_\rho},\qquad d=\deg h,\qquad
 E=\mathbb C[s]/(h),\qquad v_h=g/h,\qquad
 \upsilon=j_h(v_h)\in E^\times.
\]

The functional equation is `g(1-s)=g(s)` in the original variable.
Changing the root index in the displayed product, with every
multiplicity retained, proves

\[
 h(1-s)=(-1)^dh(s),\qquad v_h(1-s)=(-1)^dv_h(s).       \tag{P1}
\]

The quotient operation

\[
 C_1:E\longrightarrow E,\qquad [u(s)]\longmapsto[u(1-s)]
                                                               \tag{P2}
\]

is well-defined because the substitution sends the ideal `(h)` to itself
by (P1). It is linear, invertible, and its square is the identity.
For `E_k=E^{\otimes k}`, let `C=C_1^{\otimes k}`. In the original
power basis it is the unique remainder matrix for substitution of
`1-s_j` in every variable. In full local jet coordinates its formula is

\[
 (C_1u)_{\rho,j}=(-1)^j u_{1-\rho,j},\qquad 0\le j<m_\rho.
                                                               \tag{P3}
\]

Thus (P2) and (P3) give the exact map on every nilpotent coefficient;
no evaluation-only quotient has been introduced.

On the original Hilbert observation `L^2(R_{>0}^k,d^k x)`, define

\[
 (\mathcal T_k f)(x_1,\ldots,x_k)
  =(x_1\cdots x_k)^{-1}f(x_1^{-1},\ldots,x_k^{-1}).     \tag{P4}
\]

Substitution `y_j=1/x_j` proves directly that it preserves the original
`d^k x` norm. Its square is one, so it is a unitary self-adjoint linear
operator. For the Mellin convention of the source, substitution in the
integral gives

\[
 \mathcal M(\mathcal T_kf)(s_1,\ldots,s_k)
   =\mathcal M f(1-s_1,\ldots,1-s_k).
\]

With the unchanged source map `mathcal T_h^{(k)}` from the supplied
note, this proves the exact numerator transport

\[
 \mathcal T_k\mathcal T_h^{(k)}P
   =(-1)^{kd}\mathcal T_h^{(k)}
            P(1-s_1,\ldots,1-s_k).                    \tag{P5}
\]

Equality holds in the original source space: both sides have the
displayed equal Mellin transform, and the source Mellin map is
injective. The full jet map therefore obeys

\[
 C\mathcal JP=(-1)^{kd}\mathcal J
              P(1-s_1,\ldots,1-s_k).                  \tag{P6}
\]

In particular `C mathcal J P` is the full jet of the actual function
on the left of (P5). The factor `(-1)^{kd}` has not been dropped from
the numerator or from the arithmetic unit.

Fix `k>=1`, `M>=k(d-1)` and let `R_M` be exactly the source constrained
minimum in the degree-`M` polynomial image. Substitution preserves
total degree and the relation ideal `(h(s_1),...,h(s_k))`; (P5) shows
that `mathcal T_k` preserves that same source image and its relation
subspace. If `R_Mu` is its minimum with jet `u`, `mathcal T_k R_Mu`
has jet `Cu`, lies in the same source image, and has the same norm.
Applying the inverse unitary operation to any other candidate proves
that it too is a minimum. Uniqueness gives

\[
 \mathcal T_kR_M=R_MC,\qquad C^*G_MC=G_M,
 \qquad G_M=R_M^*R_M\succ0.                            \tag{P7}
\]

This establishes (P7) for the **linear** reflection (P2). It should not
be obtained by deleting complex conjugates from the existing
antiunitary identity (CT.16a). Equations (P1)–(P7) are the required
bridge between those two reflection descriptions.

## 3. Parity of the original orthogonal polynomials and frontier jets

The measure remains

\[
 d\nu_h(y)=|v_h(1/2+iy)|^2\,dy/(2\pi).
\]

By (P1), its density is unchanged by `y -> -y`. For the original monic
orthogonal polynomial `p_n`, the polynomial `(-1)^n p_n(1-s)` is
monic of degree `n`. Its inner product with each polynomial of degree
less than `n` vanishes: substitute `y -> -y` in the integral, retain
the real sign `(-1)^n`, and use the original orthogonality of `p_n`.
The difference from `p_n` has degree less than `n` and is orthogonal
to itself. Positivity of the polynomial moment Gram proves

\[
 p_n(1-s)=(-1)^n p_n(s).                               \tag{P8}
\]

This proof keeps the monic polynomials and their actual norms
`omega_n`; it never replaces the measure by a probability measure.
It also implies the original recurrence coefficient `b_n=1/2`:
the numerator of its imaginary part is an odd integrable function
`y|p_n(1/2+iy)|^2` against the even measure. The positive coefficients
`a_n=omega_n/omega_{n-1}`, with `a_0=0`, are unchanged.

Let `N=d^k`, `r=binom(M+k,k-1)`, and retain exactly the columns of the
source:

\[
 z_\alpha=\mathcal Jp_\alpha\in\mathbb C^N,
 \quad F=[z_\beta]_{|\beta|=M+1},
 \quad\Omega=\operatorname{diag}(\omega_\beta)\succ0,
\]
\[
 E_+=[w_\beta]_{|\beta|=M+1},\qquad
 w_\beta=\sum_{j:\beta_j>0}a_{\beta_j}z_{\beta-e_j}.
                                                               \tag{P9}
\]

Here `F,E_+` both have type `C^r -> C^N`, and `Omega` is `r by r`.
Equations (P6) and (P8) prove

\[
 Cz_\alpha=(-1)^{kd+|\alpha|}z_\alpha,
 \quad CF=\eta F,
 \quad CE_+=-\eta E_+,
 \quad\eta=(-1)^{kd+M+1}.                              \tag{P10}
\]

Every predecessor in the sum (P9) has degree `M`, which is why all its
terms have the same opposite sign. No condition on cancellation
between individual columns is needed.

## 4. Full relative spectrum and its exact cross-matrix

For this section put `G=G_M`. The coordinate isometry

\[
 G^{1/2}:(\mathbb C^N,\langle u,v\rangle_G=u^*Gv)
          \longrightarrow(\mathbb C^N,\langle u,v\rangle=u^*v)
\]

has inverse `G^{-1/2}`. Its use retains the original metric explicitly;
it is not a choice of a replacement metric. Define the matrices with
their original domains and codomains by

\[
 P=G^{1/2}CG^{-1/2}\in\operatorname{End}(\mathbb C^N),
 \quad U=G^{1/2}F\Omega^{-1/2}:\mathbb C^r\to\mathbb C^N,
 \quad V=G^{1/2}E_+\Omega^{-1/2}:\mathbb C^r\to\mathbb C^N.
                                                               \tag{P11}
\]

From (P7) and `C^2=I` it follows that `C^*G=GC`. Consequently
`P^*=P` and `P^2=I`. Let `H_eta` and `H_-eta` be its orthogonal
eigenspaces. Equation (P10) gives `ran U subset H_eta` and
`ran V subset H_-eta`. In particular

\[
 U^*V=0=V^*U.                                         \tag{P12}
\]

The exact source displacement (4.2) and (4.4) yield

\[
 S:=G^{-1/2}W_MG^{-1/2}
   =UV^*+VU^*,\qquad
 W_M=A_k^*G+GA_k-kG.                                  \tag{P13}
\]

In the orthogonal decomposition `H_eta direct-sum H_-eta`, put
`T=UV^*|_{H_-eta}:H_-eta -> H_eta`. Then (P12) proves the full block
identity

\[
 S=\begin{pmatrix}0&T\\T^*&0\end{pmatrix}.             \tag{P14}
\]

If `sigma>0` is a singular value of `T`, choose unit singular vectors
`Tx=sigma y` and `T^*y=sigma x`. The vectors `(y,x)` and `(y,-x)`
are eigenvectors of (P14) with eigenvalues `sigma` and `-sigma`.
The singular value decomposition, completed with the kernels, shows
that these give every nonzero eigenvalue, with its full multiplicity.
All other eigenvalues are zero. It follows in particular that

\[
 \epsilon_{k,M}:=\|G^{-1/2}W_MG^{-1/2}\|
   =\|UV^*\|.                                        \tag{P15}
\]

This equals the least nonnegative two-sided allowance for the original
pencil `-epsilon G <= W_M <= epsilon G`; it is also its least upper
allowance because (P14) pairs the spectrum.

Retain both `r by r` positive semidefinite matrices

\[
 A_F=U^*U=\Omega^{-1/2}F^*GF\Omega^{-1/2},\qquad
 B_F=V^*V=\Omega^{-1/2}E_+^*GE_+\Omega^{-1/2}.           \tag{P16}
\]

The subscript avoids confusing this `A_F` with the original generator
`A_k`. The polar factorizations `U=Q_U A_F^{1/2}` and
`V=Q_V B_F^{1/2}` have partial isometries that preserve the norm on
the respective positive supports. Thus

\[
 UV^*=Q_U A_F^{1/2}B_F^{1/2}Q_V^*.
\]

The range of the middle product is in the initial support of `Q_U`,
and its domain is supported on the final domain reached by `Q_V^*`.
The nonzero singular values, their multiplicities, and the rank
therefore equal those of `A_F^{1/2}B_F^{1/2}`. Hence the complete
finite certificate is

\[
 \boxed{\epsilon_{k,M}^2
  =\lambda_{\max}(A_F^{1/2}B_FA_F^{1/2}),\qquad
  p=\operatorname{rank}(A_F^{1/2}B_F^{1/2}).}            \tag{P17}
\]

There are exactly `p` positive and `p` negative eigenvalues in (P13).
The zero multiplicity is `N-2p`. In particular
`p<=min(r,dim H_eta,dim H_-eta)` and `p<=floor(N/2)`.
Every one of these formulas includes `p=0`: the middle product and
the displacement then vanish, and `epsilon=0`. No inverse of `A_F`
or `B_F` is required anywhere.

## 5. Source incidence bound with the improved constant

Here is a direct check of the source estimate needed for the new bound.
Let the rows of `L` be indexed by `|alpha|=M` and its columns by
`|beta|=M+1`, with `L_{alpha,beta}=a_{beta_j}` for
`alpha=beta-e_j`, and zero otherwise. Retain
`Omega_M=diag(omega_alpha)` and the source columns `Z_M=[z_alpha]`.
Then `E_+=Z_ML` exactly.

The matrix

\[
 R=\Omega_M L\Omega^{-1}L^*
\]

has nonnegative real entries and is similar, by `Omega_M^{1/2}`,
to the positive semidefinite Hermitian matrix
`Omega_M^{1/2}L Omega^{-1}L^*Omega_M^{1/2}`. At a fixed row `alpha`,
write `beta=alpha+e_j`. The first weight in a nonzero summand is

\[
 \frac{\omega_\alpha a_{\alpha_j+1}}
       {\omega_{\alpha+e_j}}=1.
\]

The other predecessor for this `beta` has index `beta-e_l`.
For `l=j` its coefficient is `a_{alpha_j+1}`; for `l!=j` it is
`a_{alpha_l}`, interpreted as zero when `alpha_l=0`. Summing first
over `l` and then over `j` gives the exact row sum

\[
 \sum_j\bigl(a_{\alpha_j+1}+(k-1)a_{\alpha_j}\bigr).
\]

It is bounded by the original number

\[
 \Gamma_{k,M}=\max_{|\alpha|=M}
      \sum_j\bigl(a_{\alpha_j+1}+(k-1)a_{\alpha_j}\bigr).
                                                               \tag{P18}
\]

The maximum row-sum matrix norm bounds the spectral radius. Similarity
to the stated positive matrix then proves the Loewner inequality
`L Omega^{-1}L^* <= Gamma Omega_M^{-1}`. Multiplication by `Z_M`
and its adjoint, followed by the exact inverse-metric sum (2.6), gives

\[
 E_+\Omega^{-1}E_+^*
  \preceq\Gamma_{k,M}Z_M\Omega_M^{-1}Z_M^*
  \preceq\Gamma_{k,M}G^{-1},\qquad
 VV^*\preceq\Gamma_{k,M}I.                             \tag{P19}
\]

There is no change to the source row sum. Since the original frontier
ratio is

\[
 \lambda_{k,M}=
 \max_{v\ne0}\frac{v^*F\Omega^{-1}F^*v}{v^*G^{-1}v}
 =\|U\|^2,
\]

the exact cross formula (P15) proves

\[
 \boxed{\epsilon_{k,M}^2
     \le\Gamma_{k,M}\lambda_{k,M},\qquad
 \epsilon_{k,M}\le\sqrt{\Gamma_{k,M}\lambda_{k,M}}.}     \tag{P20}
\]

Indeed `||UV^*||<=||U|| ||V||`, and (P19) bounds `||V||^2`.
The former general estimate `2 sqrt(Gamma lambda)` used a triangle or
scalar cross-pairing bound before exploiting (P12). The exact maps
(P11)–(P14) explain why that extra factor is absent here.

## 6. Exact volume identity and the further upper bound

Use the actual next metric, rather than a hypothetical comparison
metric. The supplied kernel update (3.7) is

\[
 G_{M+1}^{-1}=G^{-1}+F\Omega^{-1}F^*
             =G^{-1/2}(I+UU^*)G^{-1/2}.
\]

Taking determinants with all factors retained proves

\[
 \pi_M:=\frac{\det G_{M+1}}{\det G_M}
  =\det(I+UU^*)^{-1}=\det(I+A_F)^{-1},\qquad
 0<\pi_M\le1.                                         \tag{P21}
\]

For the nonnegative eigenvalues `lambda_i` of `A_F`,
`prod_i(1+lambda_i) >= 1+max_i lambda_i`, including zero eigenvalues.
Consequently

\[
 \lambda_{k,M}\le\pi_M^{-1}-1,
 \qquad
 \boxed{\epsilon_{k,M}^2
      \le\Gamma_{k,M}(\pi_M^{-1}-1).}                   \tag{P22}
\]

If `pi_M=1`, each `lambda_i=0`, so `U=0`, `F=0`, `S=0`, and both
bounds give zero exactly. If `p=0` while `pi_M<1`, (P17) still gives
`epsilon=0`; a nonzero frontier kernel update is compatible with a
zero cross matrix. If one reflection eigenspace is zero, the map into
that eigenspace vanishes, and the same formulas apply. No division by
`epsilon`, `lambda`, a matrix rank, or a possibly zero column is used.

Equality in the scalar inequality for `lambda` holds when at most one
`lambda_i` is nonzero. The general cross-matrix formula (P17), and
the exact update (P21), remain available when the scalar bound is
strict.

## 7. Exact relation to the existing one-variable volume formula

Set `k=1`; then `r=1`, `F=z_{M+1}`, `E_+=a_{M+1}z_M`, and
`Omega=omega_{M+1}`. Formula (P17), which now involves scalar
`A_F` and `B_F`, gives

\[
 \epsilon_{1,M}^2=
 \left(\frac{z_{M+1}^*G_Mz_{M+1}}{\omega_{M+1}}\right)
 a_{M+1}\left(\frac{z_M^*G_Mz_M}{\omega_M}\right).      \tag{P23}
\]

For `M>=d` the previous source minimum is also defined. Write
`r_-=det G_M/det G_{M-1}` and `r_+=det G_{M+1}/det G_M`.
The rank-one determinant and inverse update give, respectively,

\[
 \frac{z_{M+1}^*G_Mz_{M+1}}{\omega_{M+1}}=r_+^{-1}-1,
 \qquad
 \frac{z_M^*G_Mz_M}{\omega_M}=1-r_-.
\]

For the second formula one may put
`x=z_M^*G_{M-1}z_M/omega_M>=0`; the exact inverse update gives
`r_-=(1+x)^{-1}` and the displayed quadratic form is `x/(1+x)`.
Thus (P23) proves

\[
 \epsilon_{1,M}^2
    =a_{M+1}(1-r_-)(r_+^{-1}-1).                       \tag{P24}
\]

With the existing source indexing `M=d+m`, `r_-=r_m`,
`r_+=r_{m+1}`, and `a_{M+1}=kappa_{d+m+1}/kappa_{d+m}`,
(P24) is exactly (KT.28), including every zero-column case.
The initial degree `M=d-1` remains covered by (P17)–(P22) without
introducing an undefined earlier metric. The factor `1-r_-` in the
stronger one-variable equality is retained in (P24); it is bounded
by one only when deriving (P22).

## 8. Symmetric restriction, source layers, and completion scope

The same proof applies to the supplied symmetric cohomology summand.
The linear reflection commutes with all factor permutations. In the
original unscaled orbit basis, retain exactly `I_k`,
`D_k=I_k^*I_k`, and `L_k=D_k^{-1}I_k^*` from source (6.2).
The induced reflection is `C_sym=L_k C I_k`, and its metric identity
is `C_sym^*G_sym C_sym=G_sym`, where
`G_sym=I_k^*G I_k`. The grouped frontier columns and norms are those
of source (6.1)–(6.4), with the full orbit cardinalities. Their total
degrees are still `M+1` and `M`, so (P10) has exactly the same signs.
Applying the proved argument to these declared matrices gives
(P17)–(P22) with symmetric metrics and their actual determinant ratio.
The original `Gamma_{k,M}` remains a valid bound through the source
grouped-incidence inequality. No unweighted compression or interchange
of matrix inversion with arbitrary compression is used.

The original relation layer remains explicitly identified with the
frontier coordinates by

\[
 b_M=T_+-R_MF:\mathbb C^r\xrightarrow{\sim}\mathcal E_M,
 \qquad b_M^*b_M=\Omega+F^*GF.
\]

Its inverse extracts the highest orthogonal polynomial component.
The same source numerator `p_beta-c_M(z_beta)` and fixed-order
division by all `h(s_j)` give its original theta primitive with the
specified tensor signs. Its representative update is
`R_{M+1}=R_M+b_M(Omega+F^*GF)^{-1}F^*G`; therefore (P21) is a volume
identity for these actual theta representatives. At a fixed support,
each finite linear map is lifted by `(label,x)->(label,Tx)`.
The relation quotient maps its vanishing amplitude to the next
supported zero, while external absence remains external absence.

The proved new statement is a finite arithmetic parity identity and
its consequent upper bounds. None of (P17), (P20), or (P22) proves
sublinear growth in `k`: the original recurrence norms and actual
volume ratio still occur in the proved formulas. Every generator,
root, multiplicity, unit, and original source metric is retained.

## 9. Audit of the root's exact cumulative TeX, AP.1–AP.23

After completing the independent derivation above, the full file
`tex/arithmetic_frontier_parity.tex` was read from beginning to end.
Its reviewed SHA-256 is
`b93922a11dd9658183a59eabc9cc2d0a7fa214895af23f4ad3d38a686b0a9987`.
No mathematical correction was needed and no source fragment was
edited by this lane. The root's manuscript is ready for integration
at that exact hash.

The AP.2 identification `q_j=p_j`, `kappa_j=omega_j` is proved by
monic uniqueness and uses the same measure, so all signs and constants
in AP.4–AP.6 are those audited above. The original source row sum in
AP.19 is exactly correct, including `a_0=0`. The square-root
isometries, positive and negative ranks, spectral zero cases, and
determinant directions in AP.12–AP.21 all agree with this independent
proof. The equality `Tr(S_M^2)=2 Tr(mathsf A mathsf B)` follows by
expanding the square and applying the proved `U^*V=0`; it retains
both cross products rather than treating them as separate bounds.

For AP.22 I also read the complete CT.20–CT.25 proof. Its original
identity is

\[
 \operatorname{Tr}(S_M^2)
   =4\sum_{i_1,\ldots,i_k}
       (\delta_{i_1}+\cdots+\delta_{i_k})^2
       +2\mathfrak d_M^{(k)}.
\]

Combining it with the just-verified trace in AP.15 gives exactly
AP.22, including the coefficient `2` in front of the displacement
sum. The nilpotent contribution remains in the full matrix definition
CT.20 of `mathfrak d_M^{(k)}`; it is not replaced by the diagonal sum.

For AP.23 I read the full proof of R8–R9 and its typed supported
character map. The original character is
`c_{-+}(rho)=4(Re rho-1/2)`. A four-distinct-point orbit of common
order `mu` contributes `4 mu |Re rho-1/2|` to the full ordered
absolute displacement sum. At `k=1`, the frontier has `r=1`,
so the aggregate bound is `epsilon>=sum_i |delta_i|`; it gives
`epsilon>=mu |c_{-+}|` and hence exactly the first squared
inequality in AP.23. This proves it both when the retained packet is
exactly that orbit (the literal R9 setting, `d=4 mu`) and when that
orbit is contained in a larger fully retained packet. In the latter
case the other terms in the sum are nonnegative and remain present.
The subsequent equality and upper estimate are AP.15 and AP.17
on the same `G_M`. For the original one-variable source indexing,
`M=d+m` with `m>=0`, as used in KT.28, so no `M=d-1` antecedent
is silently required for this chain. At the critical supported value
the quartet has the stated two-point divisor and vanishing
`c_{-+}`; R9's following paragraph supplies that exact change of
orbit size and the unchanged phase coordinate.

Readiness statement: AP.1–AP.23 is a complete written proof of its
finite arithmetic claims with the cited cumulative source proofs.
This audit supplies no new formalization claim and does not extend
the scope to a uniform RH estimate.
