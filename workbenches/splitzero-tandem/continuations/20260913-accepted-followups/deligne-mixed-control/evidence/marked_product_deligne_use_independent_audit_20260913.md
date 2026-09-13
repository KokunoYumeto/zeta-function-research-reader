# Marked external product: actual Deligne use and the next boundary calculation

Date: 2026-09-13. This is an independent bounded mathematical audit and continuation. It does not replace the cumulative programme, integrate into another owner's files, or assert a remote publication.

## Sources read completely and source pins

The new pasted continuation was read completely from `source:received-attachments\ddee9476-d3a1-48a9-a020-d50a036083f5\pasted-text.txt`.

The following package files were read completely: `NOTE.tex` (708 lines), `SOURCE_REVIEW.md`, and `HANDOFF.md`, in `source:marked-product-original`. The independently supplied NOTE pin is SHA256 `40749e2a9d599a322e7b125eb43ad0878a066a51b61da52cc3bb2ffb94cbd841`; the archive pin is `c26683faaa76aeb6c59beabcee0e8d70f5a34d45ff9ec9fd8bccd66ef79b2d73`.

Primary Deligne statements and their surrounding proofs were read in `workspace:math\output\Deligne_Weil_II_S20_LaTeX\typed_latex\S20_EN_article_text.txt`: 1.2.2 and 1.2.5 at lines 414–436; 1.8.4 and 1.8.8 at lines 1101 and 1126; 3.3.1–3.3.6 and the actual boundary dévissage at lines 1985–2043; 3.7.2–3.7.4 at lines 2327–2360; 6.1.13 and 6.2.1–6.2.6 at lines 3211–3261. These statements concern the specified finite-field/étale objects. Their use below does not manufacture an étale structure on the theta Fréchet complex.

## 1. The actual degree of use

The package makes a real application of Weil II 3.7.2.3 to a concrete exponential family. The phase degree is d+1, the number of variables is k, the cohomological degree is k, the rank is d^k, and the weight is k. Those indices match. This is stronger than having an arbitrary rank-q one-variable pure family beside the arithmetic packet.

It also constructs a free polynomial lattice whose marked fibre is the complete tensor packet, with a literal source realization containing the complete Taylor unit. These are substantive maps. The package does not, however, construct the mixed extension of that family through u=0, compute its local monodromy/Stokes data, or transport the resulting control to every original supported source face and its Hermitian relation norms. Its final target at NOTE line 700 is an eventual consequence to pursue; the work needed before it includes the intervening boundary and mixed-support calculations. No failed-program conclusion follows from the absent transfer, and the package itself explicitly disclaims that conclusion.

The following locators make this assessment testable.

| Construction | Package lines | Finding |
| --- | --- | --- |
| Absolute base, semiring sheaf, and scalar observations | 28–94 | The actual single-slot base is retained. These formulas do not by themselves reconstruct all independent mixed coefficient masks. |
| Two-leg theta complex and retained H0 summand | 96–145 | The coordinate isomorphism `(v,w) -> (v-Fourier(w),w)` has the displayed inverse and retains the additional degree-zero cycle. |
| Full packet, Euler inverse, complete Taylor unit, source chain map | 147–183 | Source maps are correctly typed. The H1 map is `sigma_h M_upsilon`, not an unweighted identification. The complementary quotient remains in the cone. |
| Dilation and tensor relation primitives | 185–223, 367–409 | The original action, nilpotent powers, original relation and all cross-pairings remain. |
| Free external family and its marked coefficient specialization | 225–277 | The leading-term splitting is over the parameter ring, so specialization really preserves the full d^k-dimensional tensor fibre. |
| Cyclic relation away from the marked fibre | 279–298 | The correction `sum_i(t_i Q_i-u partial_i Q_i)` is an exact calculated relation defect. It cannot be discarded. |
| Parameter connection and transverse cyclic map | 300–321 | The t-connection and its transverse map are present. The u-connection and its boundary control were not calculated there; section 4 below supplies the u-connection. |
| Finite-field realization | 323–332 | The application of 3.7.2.3 is justified for the stated good specialization and u nonzero. The proof also permits a further genuine application of 3.7.3 and 1.8.4, given in section 3 below. |
| Complex periods | 334–365 | The ordered period comparison is defined on u nonzero. The marked algebraic fibre is not asserted to be the lisse fibre at u=0. The exact determinant is calculated in section 5 below. |
| Signed four-endpoint source/relations calculation | 411–589 | A useful finite analytic calculation is present. It is not the boundary mixed-extension theory. It retains the relation-valued derivative and the signed equal-rank cancellation. |
| Original moment list and first pair | 591–664 | The exact moment formulas are provided. The numerical illustration is expressly not an interval proof or an asymptotic estimate. |

There are small literal corrections to make without changing any mathematical object: NOTE 436 writes `du` after defining the density in the variable y; NOTE 442, 460 and 517 use `c+iu` for the source-frequency argument although that argument was named y. Those must read `dy` and `c+iy`. The analytic deformation parameter u is already in use and must not be silently identified with y. At line 569, `M(0)^(-1)M(1)` is positive self-adjoint in the M(0) metric; `M(0)^(-1)(M(1)-M(0))` is self-adjoint and need not be positive. The norm delta and the ensuing estimate remain valid.

## 2. Audit of the full fibre, cyclic relation, and finite-field application

Fix the original monic packet

    h(s) = product_rho (s-rho)^(m_rho),    d = sum_rho m_rho >= 1,
    Phi_h(s) = s^(d+1)/(d+1) + sum_(b=0)^(d-1) h_b s^(b+1)/(b+1).

Every m_rho is the selected zero's complete order and Phi_h(0)=0. Write `f_t=Phi_h-ts`, `L=u partial_s+h-t`. In the coefficient ring `R=C[u,t]`, the leading term of `LP` is the leading coefficient of P times `s^(deg P+d)`. Consequently L is injective and successive subtraction of terms `L(a s^j)` produces one and only one remainder of degree less than d. If a remainder of degree less than d were in the image of L, the leading-degree identity would make it zero. This proves the direct module decomposition

    R[s] = L(R[s]) direct_sum R[s]_(<d).

The inverse from `L(R[s])` to `R[s]` is R-linear; it is a contracting homotopy on the two-term image summand. Tensoring k such split complexes over `C[u,t_1,...,t_k]` leaves only the ordered top remainder. The other tensor summands contract: on a summand with a contractible factor, use its contracting homotopy with the Koszul sign from preceding degrees; the two cross terms from different factors cancel. Hence the cohomology is concentrated in degree k and its top module is free with the original monomials `product s_i^(a_i) ds_1 wedge ... wedge ds_k`, `0<=a_i<d`. The splitting remains a splitting under the displayed coefficient evaluation, proving the full tensor fibre without dropping any primary nilpotent.

At the marked fibre the chain map is `(alpha_h,T_h)`, where `alpha_h(P)=P(D)phi_*`, `T_h(P)=P(D)F_h`, and `Theta alpha_h(P)=T_h(hP)`. On H1 it is exactly `sigma_h M_upsilon_h`, because `J_h T_h(P)=upsilon_h[P]_h`. Tensoring gives the complete factor `upsilon_h^(tensor k)`. No ring-map assertion is made about the linear source section.

For the cyclic relation, fixed ordered division gives `chi(S)P(S)=sum_i h(s_i)Q_i`. The ordered primitive is `sum_i (-1)^(i-1) Q_i ds_1 wedge ... omit ds_i ... wedge ds_k`. Applying the exterior differential contributes the second `(-1)^(i-1)`, so its top coefficient is `sum_i (h_i Q_i-t_i Q_i+u partial_i Q_i)`. Taking the top cohomology class gives exactly NOTE (34). This proves the parameter correction with its signs, rather than assigning the marked cyclic annihilator to every fibre.

For a specified residue-field point `R0 -> kappa=F_Q`, with characteristic p>d+1, the leading phase is `sum_i s_i^(d+1)/((d+1)u)`. Its partial derivatives are `s_i^d/u`; if they all vanish, every projective coordinate vanishes. Thus its projective hypersurface is smooth. Apply Weil II 3.7.2.3 with Deligne's polynomial degree equal to d+1 and his dimension equal to k. It gives precisely degree k, dimension d^k, and purity of weight k. Repeated finite critical roots do not affect this leading-hypersurface check. The finite Taylor unit and its inverse lie in R0 as stipulated, so their matrix identity specializes as well. This last observation supplies an invertible coefficient map; it supplies no identity between a finite-field Frobenius operator and real dilation.

## 3. The next genuine finite-field mixed-boundary use is available now

This section constructs and applies actual objects; it does not assume a theta weight estimate.

For the same specified finite field, let

    S = G_m,u x A^k_(t_1,...,t_k),
    pi: A^k_s x S -> S,
    L = L_psi((sum_i Phi_h(s_i)-sum_i t_i s_i)/u),
    F = R^k pi_! L.

The coefficient map from S to Deligne's good leading-form open is explicit: substitute the displayed polynomial coefficients, including `1/u`. The leading-form check in section 2 shows that its entire image is in that good open. Lemma 3.7.3 proves lissity of every universal `R^j pi_!`; proper-support base change pulls that assertion to S. Statement 3.7.2.3 then gives `R^j pi_! L=0` for j different from k and F lisse pointwise pure of weight k. This is a sheaf-level statement, beyond a collection of pointwise vector-space dimensions.

Fix an actual finite-field parameter value `t=t0`, after a finite residue-field extension if needed. Write `F_t0` for its pullback to G_m and `j:G_m -> A^1_u`. The sheaf `j_! F_t0` is defined and mixed of weight k: it has F_t0 on the open and zero boundary stalk. The ordinary direct image has its exact boundary sequence

    0 -> j_! F_t0 -> j_* F_t0 -> i_* (V^I) -> 0,

where `i:{0}->A^1`, V is the representation at the geometric generic point of the strict local trait at u=0, and I is inertia. Exactness follows on the open, where the first map is the identity, and at the closed stalk, where its cokernel is precisely the invariant stalk `(j_*F_t0)_0=V^I`.

After passing to an open finite-index inertia subgroup with unipotent action, its logarithm N and monodromy filtration M are the actual ones attached to this V. Deligne 1.8.4 applies to the lisse pointwise pure F_t0 and proves `Gr_i^M V` pure of weight `k+i`. His 1.8.8 identifies the invariant stalk as the finite-group invariants of `ker N`; the induced graded pieces vanish for i>0. It follows that `(j_*F_t0)_0` is mixed of weights at most k. These are actual finite-field boundary bounds, with no asserted numerical value of N or each graded rank.

The remaining local calculation in that branch is therefore precise: compute the inertia representation, its filtration and ranks, and the compactification/source comparison for this particular phase. The coefficient lattice at u=0 and the theta image in NOTE (30) are separately explicit. Their relation to this boundary representation has not been furnished by the package. A coefficient-ring specialization zigzag alone does not manufacture a comparison of complex twisted de Rham cohomology, ℓ-adic cohomology, and the theta source. The explicit u-connection below records boundary data on the complex side that such a comparison must retain.

## 4. New calculation: the full u-connection in the unchanged monomial lattice

Keep `f_t(s)=Phi_h(s)-ts`. For `0<=b<d`, perform ordinary monic division, in the original variable and basis:

    f_t(s) s^b = (h(s)-t) q_b(s,t) + r_b(s,t),
    deg_s r_b < d,    deg_s q_b <= b+1 <= d.                 (BC1)

Define d-by-d matrices C_h(t) and B_h(t) by their b-th columns:

    C_h(t)e_b = coefficient_vector(r_b),
    B_h(t)e_b = coefficient_vector(partial_s q_b).          (BC2)

The quotient derivative already has degree below d. Therefore there is exactly one differential-reduction correction, with no omitted series:

    [f_t s^b] = [r_b-u partial_s q_b] in coker L.             (BC3)

Indeed subtract `Lq_b=(h-t)q_b+u q_b'` from (BC1). This proves (BC3) at the original u, t, coefficients, and basis.

On polynomial coefficients localized at u, define

    nabla_u^1 = partial_u - f_t/u^2,
    nabla_u^0 = partial_u - f_t/u^2 + 1/u.                   (BC4)

These are the degree-one and degree-zero operators respectively. They are a chain connection: direct commutator calculation gives

    [L, partial_u] = -partial_s,
    [L, -f_t/u^2] = -(h-t)/u,
    [L, nabla_u^1] = -L/u,
    nabla_u^1 L = L(nabla_u^1+1/u) = L nabla_u^0.           (BC5)

Thus the top connection really descends. In the retained remainder basis, (BC3) proves its exact matrix:

    nabla_u = partial_u - C_h(t)/u^2 + B_h(t)/u.             (BC6)

For the whole ordered k-factor complex, the degree-j chain operator is

    nabla_u^(j) = partial_u - (sum_i f_(t_i)(s_i))/u^2
                              + (k-j)/u.                  (BC7)

The commutator with each coefficient differential is `-L_i/u`; the scalar difference between adjacent degrees contributes `+L_i/u`. Their cancellation proves compatibility with the full exterior differential and its original signs. The top-cohomology connection is consequently

    nabla_u = partial_u - (sum_i C_(h,i)(t_i))/u^2
                              + (sum_i B_(h,i)(t_i))/u.    (BC8)

The existing `nabla_(t_i)=partial_(t_i)-s_i/u` commutes with (BC7): differentiating `-s_i/u` in u gives `+s_i/u^2`, and the commutator of `-sum f_i/u^2` with `partial_(t_i)` gives `-s_i/u^2`. All other commutators vanish. Hence the displayed connections are flat, including the u direction.

The entries of B_h(t) in fact do not depend on t. To see this without changing basis, compare the coefficients of degrees greater than d in (BC1). The perturbation `-t s^(b+1)` has degree at most d and the term `-t q_b` also has degree at most d. Therefore all coefficients of q_b except possibly its constant coefficient are determined by equations independent of t. Differentiation removes that constant. In addition, q_b has leading term `s^(b+1)/(d+1)`. Thus B_h is upper triangular in the ascending monomial basis, with

    (B_h)_(b,b) = (b+1)/(d+1),
    Tr B_h = sum_(b=0)^(d-1) (b+1)/(d+1) = d/2.             (BC9)

This calculation does not identify B_h alone with the local monodromy: the order-two matrix C_h is present and generally does not commute with B_h.

At the marked fibre t=0, C_h(0) is multiplication by `[Phi_h]_h`. Retain every Chinese-remainder projector of the full jet algebra. On the rho-primary summand `C[s]/(s-rho)^(m_rho)`, write

    h(s) = (s-rho)^(m_rho) a_rho(s),    a_rho(rho) != 0.

Integrating the Taylor series from rho proves

    Phi_h(s)-Phi_h(rho)
      = sum_(j>=0) a_rho^(j)(rho)/j!
                    * (s-rho)^(m_rho+j+1)/(m_rho+j+1).     (BC10)

Every term is divisible by `(s-rho)^(m_rho+1)`. Consequently

    C_h(0)|_(E_rho) = Phi_h(rho) I_(E_rho),
    A_h|_(E_rho) = rho I_(E_rho)+N_rho,
    dim E_rho = m_rho.                                    (BC11)

Both equations matter: the leading u-pole is scalar on a primary jet block, while the original nilpotent remains in the t-connection, the module, and the source map. No jet is discarded by (BC11). For an ordered tensor tuple `(rho_1,...,rho_k)`, the leading coefficient is `sum_i Phi_h(rho_i)` on a block of dimension `product_i m_(rho_i)`. Equal sums retain their separate original projectors and source labels.

Equation (BC11) also gives an exact elementary boundary comparison. The moduli of the scalar exponential factors for two tuples have ratio

    exp(Re((sum_i Phi_h(rho_i)-sum_i Phi_h(rho_i'))/u)).    (BC12)

For a nonzero difference, their equal-modulus rays satisfy `arg u=arg(difference)+pi/2 mod pi`. This determines candidate Stokes directions, not their Stokes matrices. The connection (BC8), with its actual coefficients and full primary data, is the object on which those matrices must be calculated.

## 5. New calculation: the complete period determinant, with its phase and constant

Let Pi_h be NOTE (39) in its original ordered rays and monomial columns. Put

    Ctr_h(t) = Tr C_h(t).

Differentiating the convergent period integrals in u and using (BC3) gives `partial_u Pi_h=Pi_h(-C_h/u^2+B_h/u)`. Jacobi's determinant identity and (BC9) imply

    partial_u log det Pi_h = -Ctr_h(t)/u^2 + d/(2u).        (BD1)

Therefore, on an original contour branch,

    det Pi_h(u,t) = K_d u^(d/2) exp(Ctr_h(t)/u).            (BD2)

Here the constant is the following explicit number, including the ordered contour phase. Set `zeta=exp(2 pi i/(d+1))`, `beta_b=(b+1)/(d+1)`, and `W_(j,b)=zeta^(j(b+1))-1`, with `1<=j<=d`, `0<=b<d`. Then

    K_d = (d+1)^(-d/2) exp(pi i d/2)
                 * product_(b=0)^(d-1) Gamma(beta_b) * det W.    (BD3)

No gamma factor or contour sign has been suppressed. The matrix W is invertible: if `sum_(r=1)^d a_r(z^r-1)` vanishes at the d nontrivial `(d+1)`-st roots and at 1, its degree at most d forces it to be zero, and then every a_r is zero.

Here is a proof that K_d is independent of the lower coefficients of h and of t, including repeated critical roots. On the dense open of simple critical roots, differentiation of `Ctr_h(t)=sum_rho f_t(rho)` gives `partial_t Ctr_h=-sum_rho rho=-Tr A_h(t)`, since `f_t'(rho)=0`. Both sides are polynomial coefficient expressions, so the identity extends to all h,t. The t-period equation then cancels the t-derivative of the exponential in (BD2).

For a coefficient h_b, period differentiation inserts `s^(b+1)/((b+1)u)`. Multiplying this by column s^j has degree j+b+1 at most 2d-1. In its division by h-t, the derivative of the quotient has degree at most j+b-d, strictly less than j. Accordingly the differential-reduction correction matrix has zero trace. The logarithmic determinant derivative in h_b is exactly `Tr M_(s^(b+1))/((b+1)u)`. On the same dense simple-root open this equals `(partial_(h_b) Ctr_h)/u`, again because the derivative of f_t at each critical root vanishes; the identity extends polynomially. Thus the remaining factor in (BD2) has zero derivatives in every coefficient and t.

At h=s^d,t=0 the original radial integral is

    (Pi_h)_(j,b) = [(d+1)u]^(beta_b) exp(pi i beta_b)
                        * Gamma(beta_b)/(d+1)
                        * (zeta^(j(b+1))-1).

This follows by the substitution `v=r^(d+1)/((d+1)|u|)` on the stated rays. Its determinant is exactly (BD3) times `u^(d/2)`. Period convergence and coefficient differentiation hold on compact parameter sets by the fixed leading negative radial exponent; the identities extend across critical-root collisions. This proves (BD2) for the entire coefficient family on each retained u/contour branch.

For the ordered k-fold product, the determinant of a Kronecker product gives

    det Pi_k = K_d^(k d^(k-1)) u^(k d^k/2)
                  * exp(d^(k-1) sum_i Ctr_h(t_i)/u).        (BD4)

In particular its exact period Gram determinant is

    det(Pi_k^* Pi_k)
      = |K_d|^(2k d^(k-1)) |u|^(k d^k)
          * exp(2 d^(k-1) Re(sum_i Ctr_h(t_i)/u)).           (BD5)

This is a full-family determinant calculation, not a claim that the period form equals the original theta form. The exact map between the two forms can also be stated without changing either one. On the one-factor retained polynomial basis let

    (G_theta)_(a,b)
      = (1/(2 pi)) integral_R
             conjugate(1/2+iy)^a (1/2+iy)^b
             |v_h(1/2+iy)|^2 dy.

It is the Gram of the original map `T_h(P)=P(D)F_h`, containing the unchanged g/h and all its Taylor-unit information. This Gram is positive definite because T_h is injective. The k-fold source Gram is `G_theta^(tensor k)`. The period comparison is the positive self-adjoint endomorphism

    T_period = (G_theta^(tensor k))^(-1) (Pi_k^* Pi_k),     (BD6)

where self-adjointness and positivity refer to the original source metric. Its determinant is (BD5) divided by `(det G_theta)^(k d^(k-1))`. This proves the precise finite-dimensional metric comparison. Controlling its restriction to the weighted cyclic image requires `eta^* Pi_k^* Pi_k eta` and the retained original cyclic metric; the full determinant does not determine the singular values of that rectangular restriction. Formula (37), the original relation derivatives, and the Stokes/extension data therefore remain relevant even after (BD5).

## 6. Mixed faces must travel through these constructions

For every original coefficient mask A, apply the preceding coefficient complexes and connections to the actual A-indexed family of slots. If `j_A^B` is its specified zero-insertion linear map, it inserts represented zero in added coordinates. The operators (BC7) act with the same parameter coefficients in each retained slot. Since `j_A^B` is constant and linear,

    j_A^B nabla_A = nabla_B j_A^B,
    j_A^B D_A = D_B j_A^B.                                 (MF1)

These identities follow componentwise, including the added zero coordinates: derivative and every matrix coefficient send them to zero. On the disjoint carrier retaining its mask, a killed vector remains the receiving represented zero with that mask. The empty coefficient face maps under zero insertion to the zero vector in the receiving face; it is not a tau-preserving pointed lift. In particular a nonempty outer theta-leg label is not erased by an empty coefficient mask. No colimit over the whole mask poset is taken; its terminal full face would discard the independent face labels.

Equation (MF1) is a compatibility of actual coefficient face maps with the calculated family. It does not supply a weight filtration on the support poset by simply renaming a Boolean mask a weight. To build the requested full control one must calculate the sheaf/connection extensions and the maps induced by these actual face arrows, including their kernels, images, cones and original relation pairings. On the finite-field realization the corresponding weight statements can use the actual exact-sequence and duality machinery of 3.3 and 6. On the complex source realization, (BC1)–(BD6) give explicit boundary coefficients and metric maps rather than an assumed purity assertion.

## 7. Immediate continuation, stated as mathematics to carry out

Continue at u=0 on this original external family. Use (BC8) to calculate the actual local extension and Stokes/nearby-cycle data, beginning with every original primary block and preserving coincident critical-value blocks as labelled summands. On the finite-field branch compute the inertia action and monodromy filtration of the lisse F already constructed in section 3, using the compactified phase and its actual ramification. Form the extension/image/duality maps through all original mixed faces and carry their theta source sections, original units and relation forms along those maps. Compute the induced contribution on the weighted cyclic image, including (34) and (37), then feed those calculated terms into the same signed endpoint correction. This is the next part of the programme; it is not a request to posit the eventual uniform upper estimate as a new theorem hypothesis.

The boundary operator, its determinant, and the finite-field boundary weight statement above are completed work. No Stokes matrix, arithmetic weight-transfer theorem, or uniform signed four-volume estimate is claimed in this audit. Their absence gives specific calculations to continue and provides no theorem that the programme has failed.

## Exact finite verification

`marked_product_boundary_connection_check_20260913.py` checks (BC3), flatness, t-independence of B, its diagonal and trace, the critical-value trace derivative, and complete critical-jet divisibility using four exact polynomial fixtures of degrees 1, 2, 3 and 4, including repeated roots. All passed. The JSON receipt is `marked_product_boundary_connection_check_20260913.json`. The fixtures are explicitly not represented as arithmetic zero packets. The proofs above apply to the actual original h, not only these tests.
