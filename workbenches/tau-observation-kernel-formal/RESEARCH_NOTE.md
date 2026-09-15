# Original observation: corrected kernel norms and complete iterated detection

14 September 2026. This is a complementary research/formalization continuation, not a replacement for the concurrent analytic source. The source baseline is main `5a2fa7d6fc2db3133601dccbeed77785792be5d4`; the full OPG1–26 and OPR1–5 addendum and NEXT_RECEIVING_INTERFACE were read at that immutable revision. Their body blobs are respectively `e719d7666011b94eb5b653fd04689c98b6d4cf7e` and `20456dcb5c5a3a0a6cfbdbfd90186bf683ef7726`. The branch also retains the complete PR31 head `b4060b25c21f1a49a5e7730e9aff76d4c93c820d` and its PR30 ancestry. Actual execution is recorded separately in STATUS; writing a proof here does not make it a Lean certificate.

## 1. What the new source supplies

The uploaded check-in report ends before the current Original Volumes source cut. Current main reports the original baseline and quantitative Gamma return completed at their stated scales, including the nonzero m=1 centre and its nonvanishing limsup radius. This note does not independently re-prove that equilibrium/Hankel asymptotic analysis or relabel its written proof as a kernel check. The source-only OPG/OPR addendum is separate from the fixed 75-page PDF. The canonical source orders remain s=1 and s=k.

We use its actual observation

    Lambda:E -> B=im(P_k Pi^(tensor k) U^(tensor k) iota),
    E=C[S]/chi,  A=M_S,  Y=(A-kI/2)/i.

The full unit U=M_(j_h(2xi/h)), all primary jets, original periods and orientations, tensor inclusion and finite cyclic average remain in Lambda. No freely chosen replacement row is used in an arithmetic application. The infinite theta quotient remains upstream of E. An observation kernel inside E is not identified with the original theta boundary.

OPG supplies the normalized polynomial classes e_d, observed columns lambda_d=Lambda e_d, covariance M_D=sum_(d<D)lambda_d lambda_d*, and their complete coupled recurrence with the fixed-section kernel coordinates. OPR supplies the correction from those coordinates to the actual minimum-section residual. These are the two finite interfaces formalized here.

## 2. The minimum observation section and the whole residual Gram

Let G be the original positive Gram on E, K=G^(-1), Lambda:E->B the stated surjection onto its actual image, and

    Q=(Lambda K Lambda*)^(-1),   S_G=K Lambda* Q.

The new Data.sectionMap is exactly the inherited Restriction.representative constructor with source G and observation Lambda. It gives

    Lambda S_G=1,   S_G* G=Q Lambda,   S_G* G S_G=Q.

For any rectangular family X of coefficient vectors, put Z=Lambda X and R=X-S_G Z. Then

    Lambda R=0,
    R* G S_G=0,
    R* G R=X* G X-Z* Q Z.                                  (OK1)

Proof. The first equation uses Lambda S_G=1. The second follows by adjoint from G S_G=Lambda*Q and Lambda R=0. Expanding the full Gram, the two cross terms and the section Gram are each Z*QZ. The expansion leaves exactly the right side of OK1. In particular it is positive semidefinite by congruence of the positive original G. This is a matrix identity, including all off-diagonal mixed entries, not only a list of scalar norms. For any competing lift S_G Z+R' with Lambda R'=0, its Gram is Z*QZ+R'*GR'; positivity also proves the unique minimum property. Empty B gives S_G=0 and R=X.

Retain the source's fixed section S_* and actual kernel maps I:Kern(Lambda)->E, kappa:E->Kern(Lambda), with

    I kappa=1-S_* Lambda.

Then the exact relation to the metric section is

    R=I(kappa X-kappa S_G Lambda X).                        (OK2)

Indeed I kappa S_G=S_G-S_*, and expansion cancels the two occurrences of S_*Lambda X. For D=q+j and X=e_D, this is precisely OPR2, not the generally false formula R=I kappa e_D. If theta=kappa e_D-kappa S_G lambda_D and H^K=I*GI, then

    theta* H^K theta=e_D*G e_D-lambda_D*Q lambda_D=t_j-xi_j.

Consequently OPR's ordered factors are

    1+xi_j,   1+(t_j-xi_j)/(1+xi_j),

and their product is exactly 1+t_j. The denominator, old degree D-1 and elimination order remain. Nothing assigns one factor the asymptotic coefficient of their combined product.

## 3. A raw observation kernel need not carry the arithmetic action

For a linear observation L:V->W and action A:V->V define

    K_inf=intersection_(n>=0) ker(L A^n),
    O_q(x)=(Lx,LAx,...,LA^(q-1)x).

K_inf is A-stable and lies in ker L. Conversely every A-stable submodule P contained in ker L lies in K_inf: all A^n x remain in P. Thus K_inf is the largest invariant submodule inside the literal one-step kernel, rather than an assumption that the one-step kernel was invariant.

If the original polynomial supplies

    A^q=sum_(j<q)c_j A^j,

strong induction proves that the first q observations determine every later one. For n>=q, multiply this same relation by A^(n-q); all resulting powers j+n-q are strictly smaller than n. Hence

    ker O_q=K_inf.                                         (OK3)

This includes a typed q=0 case: the supplied relation then forces id=0. The arithmetic monic polynomial has q>0. Its original coefficients, not inferred eigenvalues, provide the recurrence. The quotient action on V/K_inf is constructed from proved stability. The standard first-isomorphism map to im O_q is intertwining; its concrete target shift has the original coefficients c_j in its last component. The general quotient action and finite determination are Lean targets here. The explicit companion-shift realization and its inverse are written consequences and exact regression targets, not additional claimed Lean declarations.

In OPG the action Y is an invertible affine transform of A. The spans of 1,A,...,A^(q-1) and 1,Y,...,Y^(q-1) agree by their triangular binomial coefficient change with nonzero diagonal. Therefore both yield the same finite and infinite invisible kernel. This fact retains the centre k/2 and factor i; neither is assigned a different value.

## 4. Additional result: calculate the invisible kernel by the existing residue pairing

This section is an additional deduction joining OPG23 to the previously verified monic residue duality; it is not attributed as a new claim in OPG.

Let chi be monic of degree q>0 over a field and E=K[S]/chi. Retain

    ell(x)=[S^(q-1)] rem_chi(x).

The inherited MonicResidue.residueEquiv proves that x -> (y -> ell(yx)) is an actual linear equivalence E -> E*. It uses the literal AdjoinRoot quotient and the leading-coefficient monomial detection argument, including repeated factors.

Choose the specified coordinate rows lambda_mu of the actual observation Lambda. Define, using that proved inverse,

    a_mu=residueEquiv^(-1)(lambda_mu),
    lambda_mu(x)=ell(x a_mu).                              (OK4)

Then

    K_inf={x : a_mu x=0 for every mu}.                      (OK5)

Proof. If all these products vanish, every lambda_mu(A^n x)=ell(S^n x a_mu) vanishes. Conversely, if one product a_mu x is nonzero, the existing monomial detection theorem supplies n<q with ell(S^n a_mu x) nonzero. The corresponding one of the first q observations is nonzero. This proves both OK5 and concrete finite determination without assuming a separate recurrence or diagonalization.

The implementation constructs a_mu by the actual residue equivalence and proves both implications. It also proves injectivity of O_q from a literal Bezout witness sum b_mu a_mu=1 in E. This witness is a required arithmetic input, not a field set to true by purity terminology.

### Written polynomial and primary calculation

For a finite row family, take its unique monic-remainder representatives a_mu(S), and put

    d=gcd(chi,a_1,...,a_r),  monic.

The ideal generated by the a_mu in E is (d)/(chi). Therefore

    K_inf=(chi/d)/(chi),
    E/K_inf = K[S]/(chi/d),
    dim K_inf=deg d,   rank O_q=q-deg d.                    (OK6)

To verify the annihilator formula directly, write chi=d b. Then d x=0 modulo chi precisely when d b divides d x in the polynomial domain, equivalently b divides x. This proves the stated ideal and the explicit quotient map; its kernel is exactly K_inf. For no observation rows the convention d=chi gives K_inf=E and zero observed quotient. There is no artificial nonempty observation.

At a root alpha of chi with multiplicity m_alpha, let

    nu_alpha=min(m_alpha, min_mu ord_alpha(a_mu)).

Its invisible submodule is the actual ideal (z^(m_alpha-nu_alpha)) inside K[z]/z^m_alpha; it has dimension nu_alpha. Its observed quotient has length m_alpha-nu_alpha. Thus no nilpotent jet is removed without a displayed kernel.

A particularly useful complete criterion is

    O_q is injective
      iff Lambda(e_alpha (S-alpha)^(m_alpha-1)) != 0
          for every primary alpha.                       (OK7)

Indeed the top primary class has nonzero residue. Multiplying it by a_mu leaves precisely a_mu(alpha) times that class. So its observation is nonzero exactly when at least one a_mu is a unit in that primary factor, equivalently nu_alpha=0. Each alpha may use a different detecting row. It is not necessary that one boundary row be faithful on the full packet.

A one-step-zero vector may be seen later; for example ell(1)=0 in K[z]/z^4, but ell(A^3 1)=1. Conversely, when every row kills a primary socle class, all of its iterates remain killed, because A acts scalarly on that class. Delayed observation cannot resurrect that permanently invisible direction.

OK6--7 and their CRT/gcd dimension interpretation are complete written consequences, with exact repeated-root regressions. They are not additional general polynomial-gcd declarations in the present Lean audit. No claim is made that the actual transcendental period/unit rows already satisfy d=1. Their certification needs their actual values or rigorous nonvanishing estimates.

## 5. Explicit reconstruction and the original metric, without selecting a new one

Suppose a literal Bezout identity in E is supplied:

    sum_mu b_mu a_mu=1.

Then for every x,y in E,

    ell(yx)=sum_mu lambda_mu(b_mu y x).                     (OK8)

Reduce b_mu y in the original power basis. Each term on the right becomes an explicit combination of the first q observed iterates of x. Applying the inverse residue equivalence reconstructs x itself. Equation OK8 supplies a written left inverse of the stack O_q, not just a rank count. Its coefficients include the actual row polynomials and Bezout coefficients; no condition-number bound is inferred from existence of that inverse.

For positive W on the original observation image, the finite Gram

    H_obs=sum_(r<q) (A^r)* Lambda* W Lambda A^r

has kernel K_inf: its quadratic form is a sum of nonnegative squared observed norms. It is positive definite on the resulting quotient. This is an additional observation of the original data, not a substitute for G. If O_q is injective with actual left inverse T, transport the specified G through T on im O_q. That is the isometric transported metric. The independently specified product metric W on the observed outputs need not equal it. Estimates comparing these metrics remain explicit quantitative obligations.

The metric residual OK1 and the dynamical kernel OK5 also remain different objects. The former subtracts the current G-minimum section from one source vector; the latter retains vectors undetectable under all operator iterates. Neither construction sets the mixed kernel/boundary pairing to zero except where the displayed canonical orthogonality actually proves it.

## 6. Original SplitZero integration

The original scalar G(R)={tau} disjoint-union R^bullet, e=0^bullet, arithmetic coefficient square and infinite theta quotient remain unchanged. For original coefficient diagrams D,E, a natural observation obs and natural action A, the new invisibleRelations has fibre K_inf,i and uses the old transports. Equivariance transports every observed power, proving stability without assuming injective support maps.

The existing Relations.quotientDiagram constructs D/K_inf. The new actionHom, observationHom and forgetIterates prove the total G(R)-linear squares

    actionHom q_inf = q_inf A,
    observationHom q_inf = obs,
    forgetIterates q_inf = q_raw.

Here q_raw is the separate quotient by ker(obs). The source class of x not in K_inf but with obs(x)=0 remains nonzero in D/K_inf and maps to the zero of its receiving support fibre. At nonbottom support this is not global absence. The existing present-empty-face theorem is reused; it is not replaced by an empty-sum convention.

These quotients are additional observations of the already marked coefficient object. No theorem here says a vector in ker(obs) has an original theta primitive. The original full/restricted boundary comparison of PR31 remains imported and is audited in the combined environment alongside the canonical signed trace and boundary-socle modules.

## 7. Handoff and scope

The concrete next evaluation is on the original OPG lambda_d and their full unit/period data: use OPR's section-corrected vector for the kernel cost, and use OK4--7 to identify exactly which primary jets any proposed observed-iterate realization retains. A simultaneous family of further observations intersects their invisible kernels by adjoining its rows; this does not license deleting the residual intersection.

The independent analytic baseline, Gamma asymptotics, actual period integration, cochain primitives and uniform arithmetic upper estimates retain their own proof scopes. The new result is finite algebra and metric bookkeeping on those actual maps, plus the explicit residue-annihilator criterion. It is neither an RH proof nor a categorical impossibility statement. Current verification, source hashes, negative controls and development failures are reported separately.
