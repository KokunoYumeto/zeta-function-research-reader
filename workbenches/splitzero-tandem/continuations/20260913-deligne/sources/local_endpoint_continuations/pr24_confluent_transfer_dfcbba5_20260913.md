# Confluent transfer for the original source–relation volume

## Scope and current-main integration

This add-only analytic continuation starts from main `fa4be32f87a9a90f3c02a07f7790dea95a1e7b0f`, after the merge of PR #21 and its workflow-trigger correction. The PR #22 mathematical note was read at `811210d24b80813a08972ca23f919db015383137`; its strict verification was in progress at that reading. This contribution neither modifies that branch nor treats pending checks as a certificate.

The source is the delivered Toda-volume continuation, following the cyclic and exterior-trace notes. Its full LaTeX was read directly. The new result is a fixed-width, full-jet transfer for the SAME canonical source/relation quotient metric. It applies the classical Christoffel transformation; it is not a claim to a new general orthogonal-polynomial theorem or to RH.

Keep G(Z)->Z, with its infinite target, and its coefficient square to G(C)->C. The structural base remains b_tau. Every supported coefficient map below retains e=0^bullet and external tau separately. The original theta complex is C_+=[V --Theta--> B], with D=-x d/dx, Q=B/Theta V and g=2 xi. No scalar, source function or measure is assigned a new normalization.

For a nonempty finite packet h of actual zeros with full orders, retain F_h with Mellin transform g/h. At tensor degree k, keep the actual cyclic sum module

    C=C[S]/(chi),  q=deg chi>=1,  c=k/2,  A=M_S,
    eta[P]=upsilon_h^(tensor k) P(sum_i M_(s_i))1,
    upsilon_h=j_h(g/h),
    Vcal P=P(D_1+...+D_k)(F_h^(tensor k)).

The original equations are

    J^(k) Vcal=eta pi_chi,
    q^(k) Vcal=sigma_h^(tensor k) eta pi_chi.

Its norm is the actual integral against m_k=w_h^{*k}, where

    w_h(t)=|(g/h)(1/2+i t)|^2/(2 pi),  integral m_k=mu_h^k.

The auxiliary measure is dmu_theta(u)=exp(theta u)m_k(u)du, |theta|<pi/2. Its mass is M_h(theta)^k. Theta in this expression is the real tilt parameter, not the theta-summation map. The exponential-moment bound from the source makes all finite derivatives below valid. At tilt zero the metric is the original arithmetic metric.

For h=1 the finite arithmetic quotient is zero. Its determinant is the empty determinant 1; the analytic seed and its mass remain, and G(0) still has e and tau. The positive-dimensional inverses below require q>=1.

## 1. Exact coordinate and raw-jet maps

Use the ring isomorphism

    Psi:C[S]->C[u],  P |-> P(c+i u),  u |-> (S-c)/i.

Thus d_u Psi(P)=i Psi(P'), and multiplication by S remains c+i M_u. Define the original norm polynomial

    Pi(u)=conj(chi)(c-i u) chi(c+i u).

Its leading coefficient is literally (-i)^q i^q=1. It is real and nonnegative on R. Reflection gives chi^dagger=(-1)^q chi, hence

    psi(u)=i^(-q) chi(c+i u) is real and monic,
    Pi=psi^2,  Psi(chi)=i^q psi.

The factor i^q remains in the source multiplication map. For distinct roots lambda_a of chi, of complete lengths ell_a, put

    zeta_a=(lambda_a-c)/i,  r_a=2 ell_a,  r=sum r_a=2q.

Define raw, NOT factorial-divided, derivative coordinates

    J_2 f=(f^(d)(zeta_a))_(a,0<=d<r_a).

Their kernel is (Pi). Their product uses the full binomial rule. Multiplication by u has matrix

    (X_Pi v)_(a,d)=zeta_a v_(a,d)+d v_(a,d-1),  v_(a,-1)=0.

All nilpotent orders and the coefficient d are retained.

Let Q_j be the real monic orthogonal source polynomials for dmu_theta, obtained by subtracting lower-degree projections, and write

    omega_j=integral Q_j^2 dmu_theta>0,
    a_j=omega_j/omega_(j-1),  a_0=0,
    b_j=integral u Q_j^2 dmu_theta / omega_j.

The source recurrence is

    u Q_j=Q_(j+1)+b_j Q_j+a_j Q_(j-1),  Q_(-1)=0.

No Q_j is divided by its norm. Set

    v_j=J_2 Q_j,
    F_n=[v_n,...,v_(n+r-1)],
    V=[J_2 1,...,J_2 u^(r-1)].

Both are r by r. The raw confluent determinant is

    det V=(product_a product_(d=0)^(r_a-1) d!)
           product_(a<b)(zeta_b-zeta_a)^(r_a r_b).

The fixed row order is part of this formula. F_0=V times the actual unit-triangular polynomial coefficient matrix; only their determinants are equal.

## 2. Invertibility and the original relation polynomial

**Invertibility proof.** Suppose F lies in span(Q_n,...,Q_(n+r-1)) and J_2 F=0. Then F=Pi H with deg H<n. Orthogonality gives

    0=<H,F>=integral Pi |H|^2 dmu_theta.

The integrand is nonnegative and its weight is positive almost everywhere except finitely many points. Thus H=0, then F=0. For n=0 the degree argument suffices. Hence every F_n is invertible. This does NOT estimate its inverse uniformly.

Solve

    d_n=F_n^(-1)v_(n+r),   vartheta_n=-(d_n)_0.

The polynomial

    Qhat_n=(Q_(n+r)-sum_(j=0)^(r-1)(d_n)_j Q_(n+j))/Pi

exists by exact raw-jet divisibility and is monic of degree n. Pairing its numerator with every polynomial of degree below n proves that Qhat_n is precisely the monic orthogonal polynomial for the ORIGINAL relation weight Pi dmu_theta. Its norm is

    nu_n=integral Qhat_n^2 Pi dmu_theta
        =-(d_n)_0 omega_n=omega_n vartheta_n>0.               (1)

Indeed only the Q_n column pairs with the degree-n quotient; its coefficient is -(d_n)_0. This proves vartheta_n>0 with arbitrary nonreal and repeated nodes.

Let K_n=[e_1,...,e_(r-1),d_n]. Then

    F_(n+1)=F_n K_n,
    det K_n=(-1)^(r-1)(d_n)_0=vartheta_n.                  (2)

The sign uses the displayed even r=2q. On the same jet algebra,

    T_n=F_n^(-1)X_Pi F_n,
    T_(n+1)=K_n^(-1)T_n K_n,
    d_n=(T_n-b_(n+r-1)I)e_(r-1)-a_(n+r-1)e_(r-2).         (3)

Thus the full operator and its jets have an explicit discrete transport, rather than only a determinant observation.

## 3. Fixed-width determinant and quotient-volume formulas

Let D_n be the n by n source Hankel determinant, and B_n the corresponding determinant for Pi dmu_theta. D_0=B_0=1. Orthogonality gives

    D_n=product_(j<n) omega_j,  B_n=product_(j<n) nu_j.

Multiplying (1) and (2) proves the complete confluent Christoffel identity

    B_n/D_n=product_(j<n) vartheta_j=det F_n/det V.          (4)

This is a proof from the source division and norm, not a distinct-root approximation. Raw derivative factorials remain in det V.

For N>=q-1 set n=N-q+1. The source sequence is still

    0 -> P_(N-q) --chi--> P_N -> C[S]/chi -> 0.

Its canonical least-norm quotient Gram G_N satisfies the existing Schur identity det G_N=D_(N+1)/B_n. Consequently

    V_N:=det G_N=(product_(j=n)^(n+q-1) omega_j) det V/det F_n. (5)

The constant coefficient map S=c+i u has determinant of modulus one on each remainder basis, so these are the original quotient determinants, with that coordinate map retained.

For n>=1,

    delta_N=V_N/V_(N-1)=omega_N/nu_(n-1)
           =omega_N/(omega_(n-1) vartheta_(n-1)),          (6)
    R_N:=V_(N-1)/V_(N+1)
       =omega_(n-1)omega_n vartheta_(n-1)vartheta_n
          /(omega_N omega_(N+1)).                         (7)

The transfer width 2q does not grow with N. The source recurrence and high-degree polynomial evaluation are still required; no computational-complexity or conditioning claim is inferred from the width alone.

## 4. One additional solve retains the full phase

Differentiating actual source orthogonality under exp(theta u) gives

    d_theta Q_j=-a_j Q_(j-1),  d_theta log omega_j=b_j.

For the first identity, every coefficient below j-1 vanishes by differentiated orthogonality; pairing with Q_(j-1) gives -omega_j. Let L_n have entries (L_n)_(j-1,j)=-a_(n+j) for 1<=j<r, all other entries zero. Then

    F_n'=F_n L_n-a_n v_(n-1)e_0^T.                        (8)

At n=0 the last term is zero. Trace of L_n is zero. Hence

    (log det F_n)'=-a_n e_0^T F_n^(-1)v_(n-1),
    (log V_N)'=sum_(j=n)^(n+q-1) b_j
                 +a_n e_0^T F_n^(-1)v_(n-1).             (9)

Retain T=(A-cI)/i and sigma=Tr T, which is real. The previous source cross term is exactly

    (b_N^*G_N b_(N+1))/omega_N=i(sigma-(log V_N)').

Here b_N in that formula denotes the remainder vector of the S-monic source polynomial, not the scalar recurrence b_j. The factor i and the distinction of types remain. The phase is phi_N=sigma-(log V_N)'. At zero tilt for a full quartet, evenness gives phi_N=0; it is not set to zero at a general tilt.

## 5. The positive gaps are norms of actual source vectors

Put

    Z_j=psi Qhat_j-Q_(j+q) in P_(j+q-1).

The leading terms cancel. Source orthogonality therefore proves

    Delta_j:=||Z_j||^2=nu_j-omega_(j+q)>=0.                (10)

The first term psi Qhat_j is, through the explicit unit i^(-q), an original chi relation. Its quotient is its supported zero. The difference Z_j instead has class -[Q_(j+q)] in the original quotient. Its norm is not assigned to an absent element.

The SAME canonical rank-two control is W_N=A*G_N+G_N A-kG_N. Combining its previously proved radius identity with (6) gives, for n>=1,

    epsilon_N^2=Delta_(n-1)Delta_n/(nu_(n-1)omega_N)-phi_N^2. (11)

Thus every factor in the upper bound

    epsilon_N <= sqrt(Delta_(n-1)Delta_n/(nu_(n-1)omega_N))

comes from a specified positive source norm. Both gaps are computed by the transfer:

    Delta_(n-1)=omega_(n-1)vartheta_(n-1)-omega_N,
    Delta_n=omega_n vartheta_n-omega_(N+1).

The previous two-step bound is now

    epsilon_N <= sqrt(omega_(N+1)/omega_N)
                      (R_N-1)/(2 sqrt(R_N)),              (12)

with R_N from (7). At the first degree N=q-1, use the separate expression

    epsilon_(q-1)^2=(nu_0-omega_q)/omega_(q-1)-phi_(q-1)^2.

No inverse at the previous rank-deficient degree is introduced.

## 6. Keep the actual conormal quotient, not a repeated first ideal

The helper algebra for the norm computation is C[u]/Pi, isomorphic through S=c+i u to C[S]/chi_1^2. The actual depth-two object is C[S]/chi_2, defined using the literal pullback of the original I^2. The merged conormal work gives chi_2 | chi_1^2. The actual maps are

    C[S]/chi_1^2 ->> C[S]/chi_2 ->> C[S]/chi_1.            (13)

Their kernels are respectively (chi_2)/(chi_1^2) and (chi_1)/(chi_2). In raw jets they truncate at the indicated full orders and intertwine multiplication by S. Differentiation into depth one also commutes, since chi_1 | chi_2'. The coordinate relation d_u Psi=i Psi d_S is retained.

For h=(s-rho)^2 and tensor degree two, X=S-2rho gives

    C[X]/X^6 ->> C[X]/X^5 ->> C[X]/X^3.

The first kernel is the class of X^5. The retained depth-two class X^3 has derivative 3X^2 at depth one. These maps use one original scalar support. Their split lifts send quotient-killed classes to e at the receiving label and fix external tau.

The full multiplier U=product_i(g/h)(s_i) retains the checked equation delta(UP)=U delta(P)+(delta U)P. The second term is not discarded or presumed cyclic. The 2q-jet norm calculation is not counted as construction of new actual spectral multiplicities.

## 7. Residual-controlled numerical interface

For an actual F and a specified candidate inverse Y, suppose a justified bound gives ||I-YF||_infinity<=eta<1. For candidate d_hat and residual r=v-F d_hat, the exact Neumann argument proves

    ||d-d_hat||_infinity <= ||Y||_infinity ||r||_infinity/(1-eta). (14)

This bounds the first coordinates used in (1) and (9). Arithmetic application requires certified input enclosures for the moments, source polynomials and zeros. Floating-point output alone is not a certificate.

Positive enclosures of omega and vartheta bound (7). Since (R-1)^2/(4R) is increasing for R>=1, (12) yields a valid upper enclosure of epsilon^2. The full phase can improve it through (11). Finite positivity/invertibility is not substituted for a uniform estimate of these residuals or inverse norms.

## 8. Exact calibration and analytic target

For a declared Gaussian measure of literal mass seven and variance one, psi=u^2+1, q=2,n=2,N=3, the calculation gives

    (omega_0,...,omega_4)=(7,7,14,42,168),
    vartheta_1=22, vartheta_2=86/3,
    Qhat_1=u, Qhat_2=u^2-11/3,
    Delta_1=112, Delta_2=700/3,
    G_3=diag(7/3,21/11), epsilon_3^2=400/99.

An independent quotient-Gram calculation with A=(1/2)I+i M_u gives the same result. The nonreal u-roots are algebraic fixtures, not zeros of xi; the nonzero allowance explicitly tests that the method does not manufacture purity. Repeated nodes, complex quartets, asymmetric atomic tilt derivatives and mass changes are covered by the expanded checks.

For the actual quartet retain

    q_k=[1+k(m-1)](k+1)^2,
    L_(h,k)=2 delta [1+k(m-1)](k+1) floor((k+1)^2/4).

The source exterior/filtration result gives L_(h,k)<=epsilon_(h,k,N), and L_(h,k)/(k q_k)>=delta/2. Thus epsilon=o(k q_k), with fixed h and admitted N>=q_k, is sufficient for the intended contradiction. The new representation attaches that exact target to TWO consecutive source-to-relation transfer coefficients and ONE phase solve. It has NOT proved that asymptotic bound.

No new Lean execution or arithmetic interval certificate is claimed. All new mathematical claims have the written proofs above at the retained source inputs. The original arithmetic function, unit, action, theta relations, residue pairing and trace remain unchanged.

## References and checks

Classical background: C. Krattenthaler (2021), 'A determinant identity for moments of orthogonal polynomials that implies Uvarov’s formula for the orthogonal polynomials of rationally related densities', arXiv:2103.03969; NIST DLMF Section 18.2. The proofs above supply the particular confluent and arithmetic interfaces rather than attributing them wholesale to those references.

The expanded conversation delivery includes the complete LaTeX/HTML reader and twenty exact finite regression methods; both normal and optimized runs passed with matching records, and both deliberate-failure controls failed. The preceding Toda archive's 35 manifest entries verified and its 24-method checker passed fresh normal and optimized runs. These are stated verification scopes, not new Lean certificates. The public core checker in this directory independently tests the principal raw-jet, transfer, norm, determinant, volume and phase interfaces.
