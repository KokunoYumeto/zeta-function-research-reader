# Independent Stieltjes-pair formula audit

Scope: the coefficient change, operator, metric, arithmetic unit, parity kernels, and Gaussian Christoffel formulas requested by `kernel_antidual_check`. This is an algebraic audit. It does not assert that an as-yet-unread implementation or paper fragment has passed.

## 1. Exact coefficient map

Let D >= 1, let H in C[x] be monic of degree D, and put z=s-1/2, x=-z^2 and h(s)=(-1)^D H(-(s-1/2)^2). Then h is monic of degree 2D. Set A=C[x]/(H), E=C[s]/(h). The C-linear bijection

    B: A direct_sum A -> E, (a,b) -> a(x)+z b(x)

uses the ordered bases `(1,x,...,x^(D-1); z,zx,...,zx^(D-1))` and `(1,s,...,s^(2D-1))`. It is an algebra identification with the multiplication `(a,b)(c,d)=(ac-Xbd,ad+bc)`, where X is multiplication by x on A. In particular the pair multiplication, not the direct-product multiplication, is required.

The change s=z+1/2 from increasing powers of z to increasing powers of s is triangular with diagonal 1. The pair basis has leading z degrees `0,2,...,2D-2,1,3,...,2D-1`. This permutation has D(D-1)/2 inversions. The product of leading coefficients of all pair columns is `(-1)^(2 sum_{k=0}^{D-1} k)=1`. Therefore

    det B = det T = (-1)^(D(D-1)/2),    T=B^(-1).

This proof includes every shift coefficient: triangularity, rather than deletion of the shift, explains its determinant contribution.

## 2. Generator and congruences

For original s multiplication A_s, its paired matrix is

    A_pair = T A_s T^(-1) = (1/2) I + [[0,-X],[I,0]].

Indeed z(a+zb)=-xb+za in E. For an original positive metric G, a coefficient column u transforms to u_pair=Tu, so

    G_pair = T^(-*) G T^(-1).

For a positive kernel K:E^* -> E and a commuting arithmetic unit U:E -> E,

    K_pair = T K T*,     U_pair=T U T^(-1),
    G=U* K^(-1) U  implies
    G_pair=U_pair* K_pair^(-1) U_pair.

The congruence directions follow by substitution, with no orthogonality assumption on T. Since |det T|=1, det G_pair=det G and det K_pair=det K.

If G_pair=diag(G_even,G_odd), then direct multiplication gives

    A_pair* G_pair + G_pair A_pair - G_pair
      = [[0,G_odd-G_even X],[G_odd-X* G_even,0]].

The bottom-left block is the adjoint of the top-right block. This uses the original coefficient matrix X, and does not require X to be Hermitian.

## 3. Unit and determinant factors

Suppose g(s)=g(1-s) is entire. Its power series about 1/2 contains only even powers, so there is an entire F with `g(s)=F(-(s-1/2)^2)`. The radius is infinite: the absolute convergence of the even series at every z implies absolute convergence of the x series at every x by taking |z|=sqrt(|x|).

If H divides F with exactly the selected multiplicities, `F/H` is an analytic unit in A. Define `e_H=j_H(H/F)` by its holomorphic germs at the roots of H, retaining all jets. The original unit epsilon=j_h(h/g) then maps to

    epsilon_pair = ((-1)^D e_H, 0),
    U_pair = (-1)^D diag(E_H,E_H),    E_H=M_(e_H).

The sign is present for odd D. It contributes no sign to det U because the matrix has dimension 2D; explicitly

    det U = (det E_H)^2,
    det G = |det E_H|^4 / (det K_even det K_odd)

when K_pair=diag(K_even,K_odd). If the paper instead defines e directly as the image of epsilon, the scalar (-1)^D is already in e and must not be inserted a second time.

## 4. The measures and truncations

Let dnu(t)=w(t) dt/(2 pi) with w(-t)=w(t), and let lambda be its pushforward under t -> x=t^2. If w is a density, then

    dlambda(x)=w(sqrt(x)) dx/(2 pi sqrt(x)),    x>0.

The factor is the sum of both t branches. For polynomials a,b,c,d,

    integral conjugate(a(t^2)+it b(t^2)) (c(t^2)+it d(t^2)) dnu(t)
      = integral conjugate(a)c dlambda + integral x conjugate(b)d dlambda.

The cross terms vanish by oddness, while conjugate(it)*(it)=t^2=x gives the positive odd measure x dlambda. Thus degree-N s polynomials correspond to

    P_floor(N/2)(x) direct_sum z P_floor((N-1)/2)(x).

The pair kernel is the direct sum of the two remainder kernels for H with precisely those cutoffs and measures lambda and x lambda. Both quotient maps are onto when N >= 2D-1. Finite-level kernel changes must use the alternating cutoff order; increasing N does not increase both cutoffs at once.

## 5. Monic Christoffel pair and all signs

Assume lambda is positive on an infinite subset of (0,infinity), with all moments finite. Let P_n and R_n be monic orthogonal polynomials for lambda and x lambda respectively, with squared norms tau_n and sigma_n. Their coefficients are real because the moment matrices and right hand sides determining the monic lower coefficients are real. Also P_n(0) cannot vanish: if P_n=x r with deg r=n-1, then its lambda inner product against r is the strictly positive integral of x|r|^2, contradicting orthogonality. Put c_n=P_(n+1)(0)/P_n(0). Then

    R_n(x) = (P_(n+1)(x)-c_n P_n(x))/x,
    sigma_n = -c_n tau_n.

The numerator vanishes at x=0. Its quotient is monic of degree n. Against any degree <n polynomial r, its x-lambda inner product is the lambda inner product of P_(n+1)-c_n P_n against r, hence zero. The norm identity follows by pairing x R_n with R_n: the P_(n+1) contribution vanishes and the P_n contribution is tau_n because R_n-P_n has degree below n. Positivity of both norms proves c_n<0; induction from P_0(0)=1 gives sign P_n(0)=(-1)^n without a separate root-location assertion.

For the original vertical-line monic orthogonal polynomials q_j(s),

    q_(2n)(s)=(-1)^n P_n(x),
    q_(2n+1)(s)=(-1)^n z R_n(x),
    kappa_(2n)=tau_n,       kappa_(2n+1)=sigma_n.

For a_j=kappa_j/kappa_(j-1), the original vertical recurrence q_(j+1)=z q_j+a_j q_(j-1) gives

    x R_n=P_(n+1)+a_(2n+1) P_n,
    R_n=P_n-a_(2n) R_(n-1),
    a_(2n+1)=sigma_n/tau_n=-c_n,
    a_(2n)=tau_n/sigma_(n-1)   (n>=1).

## 6. Exact Gaussian calibration

For dnu=e^(-t^2)dt/(2 pi), the pushforward is dlambda=x^(-1/2)e^(-x)dx/(2 pi). Using monic Laguerre polynomials,

    P_n=(-1)^n n! L_n^(-1/2)(x),
    R_n=(-1)^n n! L_n^(1/2)(x),
    tau_n=n! Gamma(n+1/2)/(2 pi),
    sigma_n=n! Gamma(n+3/2)/(2 pi),
    c_n=-(n+1/2),   a_(2n)=n,   a_(2n+1)=n+1/2.

These constants refer to the Gaussian exponent exactly as displayed. Scaling the density by a constant scales both norm sequences and preserves the ratios; scaling its exponent changes the recurrence ratios.

## Suggested negative controls

1. Use T^(-*) K T^(-1) for the kernel; it must fail against the original remainder Gram computation for a non-unitary T.
2. Drop the x in the odd measure; the degree-one norm and paired metric must fail.
3. Replace P_(n+1)-c_n P_n by P_(n+1)+c_n P_n; divisibility by x must fail.
4. Drop the (-1)^D unit sign at odd D; the unit identity must fail even though a norm-only test cannot detect it.
5. Increase both parity cutoffs on each source step; the direct original monomial kernel must fail.

## 7. Full written-fragment and checker read

Read the complete current `tex/theta_stieltjes_pair.tex` and `scripts/check_theta_stieltjes_pair.py`, including all original monomial source-Gram construction, full quotient reductions, parity kernels, unit factors, metric/weight congruences, mass scaling, repeated-root controls, and zero-frontier cases.

No mathematical correction was found. The fragment chooses the original unit v=g/h, rather than epsilon=h/g used as the temporary convention in section 3 of this audit. It explicitly defines `V=(-1)^D Phi/H`, hence its v is exactly V(x), and its paired unit really is diag(U_V,U_V). The source residue map is U_v j_h; its minimum metric is the inverse of its residue kernel. This agrees with the earlier formula U_epsilon* K^(-1) U_epsilon by explicitly inverting U_v.

The written fragment's formulas SP.25--26 also preserve the multiplication order: for R=G_even^(-1/2)G_odd G_even^(-1/2), L=G_even^(1/2)X G_even^(-1/2), and B=G_even^(-1/2)(G_odd-G_even X)G_odd^(-1/2), one has B=(R-L)G_even^(1/2)G_odd^(-1/2), hence BB*=(R-L)R^(-1)(R-L)*. If the allowance vanishes, R=L, so X is similar to a positive Hermitian matrix; the argument from the minimal polynomial H then excludes repeated roots at exact zero allowance.

The source also gives the correct maximal multiplication domain in the two Hilbert components. The condition f,tf in L2(nu), applied to the even/odd norm identities, is precisely a in L2(lambda) intersect L2(x lambda) and b in L2(x lambda) intersect L2(x^2 lambda). Neither parity integrability condition is omitted.

The checker uses a variance-one Gaussian, not the exponent used in section 6 above. Its exact moments are `M*(2j-1)!!`, with M=1 or 7/3. Accordingly its measures are

    dnu=M exp(-t^2/2)dt/sqrt(2 pi),
    dlambda=M x^(-1/2)exp(-x/2)dx/sqrt(2 pi).

The paired monic polynomials are `(-2)^n n! L_n^(-1/2)(x/2)` and `(-2)^n n! L_n^(1/2)(x/2)`. Thus its asserted norms `M*(2n)!` and `M*(2n+1)!` are correct; the corresponding c_n is -(2n+1), a_(2n)=2n, and a_(2n+1)=2n+1. The file explicitly limits these computations to rational Gaussian calibration, with no arithmetic theta moment enclosure or RH certificate. All check decisions use explicit exceptions rather than Python assert, so the logic is retained under optimized Python. This independent audit read the checker; execution receipts remain the implementing agent's responsibility.

Snapshot hashes observed after the complete read:

- Written fragment SHA-256: `19D46E9436DE4D0236468552C31109A67BB7A759EB264B6937E5DCE45E8C5743`.
- Checker SHA-256: `04AE359AA8A8C5DF6B946976A41F18015E1D6C1C37EC8DB5FB182200A1719434`.

Notation-only suggestion sent to the author: define upsilon=j_h(v_h) explicitly at its first appearance in the fragment, unless inherited notation is deliberately intended. No main source or checker file was edited by this audit.

## 8. Audit of the subsequent exact branch and characteristic-polynomial checks

Read the complete updated checker after the implementing agent added `run_local_branches`, source characteristic-polynomial substitution, the unit-sign controls, every consecutive-stage determinant update, and the complete relative characteristic-polynomial comparison. No mathematical correction was found.

In the local ring B=C[eta]/eta^m, for alpha nonzero, let

    Z=alpha sum_{j=0}^{m-1} binom(1/2,j)(-eta/alpha^2)^j.

Then Z^2=alpha^2-eta and Z has inverse because its constant term is alpha. For branch sign e=+1 or -1, put a=e alpha. The original branch coordinate w=s-(1/2+a) has eta=-2a w-w^2, and its inverse is w=e Z-a. Substitution gives the stated inverse identities modulo eta^m and w^m. In particular the leading coefficient of w(eta) is -1/(2a), so all jet powers through order m-1 are retained. This also proves that the wrong sign used in the negative control fails already in the linear coefficient for m>1. At m=1 the checker correctly uses remainders, where eta and w themselves are zero, and does not require that negative control.

The coefficient matrix from a+zb to its two branch values is

    C=[[I,M_Z],[I,-M_Z]],
    C^(-1)=(1/2)[[I,I],[M_Z^(-1),-M_Z^(-1)]].

Subtracting the first block row from the second shows `det C=det(-2M_Z)=(-2alpha)^m`; multiplication by Z is triangular with diagonal alpha in the full eta basis. In the pair multiplication, z^2=alpha^2-eta, so `(1/2, +/- Z^(-1)/2)` squares to itself, their product is zero, and their sum is `(1,0)`. These are the exact tested idempotents. The test values alpha=1, i/2, and 3/5+4i/5 are all nonzero and are carried out at all local lengths m=1,2,3,4. The complex examples retain their actual complex coefficients.

The source characteristic polynomial test first obtains the actual symbol `cp.gen` returned by SymPy, then substitutes that symbol by s. Thus it compares the complete degree-2D companion characteristic polynomial with h, rather than accidentally comparing a polynomial in a different free variable or evaluating at a matrix.

For a source step N to N+1, the orthogonal polynomial expansion gives the complete residue-kernel update

    K_next=K_prev+v v*/kappa_(N+1),
    det K_prev / det K_next
      =1/(1+v* K_prev^(-1) v/kappa_(N+1)).

Both sides are defined because K_prev is positive definite and kappa_(N+1)>0. The ratio equals the new source-metric determinant divided by the previous one, since that metric is the inverse kernel. Under T the new column occupies the even block when N is odd and the odd block when N is even. The checker tests the unchanged block and the exact changing block separately. It retains the v=0 case, in which the determinant ratio is exactly one.

Write O=G_odd-G_even X. In paired coordinates the relative operator G^(-1)W is similar to

    L=[[0,G_even^(-1) O],[G_odd^(-1) O*,0]].

For lambda nonzero, block elimination yields

    det(lambda I_(2D)-L)
      =det(lambda^2 I_D-G_even^(-1)O G_odd^(-1)O*).

Both expressions are polynomials in lambda, so the identity holds at lambda=0 as well. This proves that the check includes every eigenvalue and its full algebraic multiplicity, including zero. Squaring L gives the two products of its opposite off-diagonal blocks; cyclicity of trace gives the asserted factor two in the squared trace. The D-by-D product is similar to

    G_even^(-1/2) O G_odd^(-1) O* G_even^(-1/2),

which is positive semidefinite, so the characteristic-polynomial relation agrees with the positive/negative singular-value pairing in the written fragment.

The audited updated checker SHA-256 is `355C96048F84413FB310E513F61063C72E92B12E485C104091F4F274CB6B87F3`. This supersedes the checker snapshot in section 7. The source file changed separately after the earlier complete source read; this checker follow-up does not silently extend the earlier source-hash claim. No re-execution was needed for this independent read: the implementing agent is producing the ordinary, optimized, and harness-negative execution receipts for the final checker.

## 9. Full rank-one discrepancy and the independently projected source derivative

Read the new source subsection SP.32--35 and the corresponding new checker block. No mathematical correction was found. Also inspected the checker's updated metadata: it now explicitly states that the Gaussian Gram measure and residue unit are separately prescribed finite inputs. The formal polynomial g_model=h*v checks unit/sign algebra and does not generate the Gaussian measure. The scope statement correctly avoids claiming a calibrated analytic coupling between the actual theta measure and its unit.

For the original source section r_N:E -> P_N, let z_j=J(q_j), G_N=r_N* r_N, and let K_N=ker(J:P_N -> E). Because the monic orthogonal q_j have norms kappa_j, the section is

    r_N u = sum_{j=0}^N q_j (z_j* G_N u)/kappa_j.

Thus its leading coefficient row is L_N=z_N* G_N/kappa_N. Define the actual degree-N+1 relation

    w_N=q_(N+1)-r_N z_(N+1).

Its full J image is zero. It is orthogonal to K_N because q_(N+1) is orthogonal to all P_N and the section image is orthogonal to K_N. Its squared norm is

    ||w_N||^2=kappa_(N+1)+z_(N+1)* G_N z_(N+1),

because its two displayed summands are orthogonal. The original derivative b_N=s r_N-r_N A has full zero J image. Its leading coefficient row is L_N. Therefore b_N-w_N L_N lies in P_N and has full zero J image, hence belongs to K_N. Projection away from K_N consequently gives exactly w_N L_N. This is the projection computed in the checker using the direct original monomial Gram matrix M_(N+1), the actual coefficient shift by s, the padded old section, and an explicit basis of ker J_N.

The relative Hilbert--Schmidt cost is therefore

    chi_N = Tr(G_N^(-1) (w_N L_N)* (w_N L_N))
      = (kappa_(N+1)+z_(N+1)*G_N z_(N+1))
        (z_N*G_N z_N)/kappa_N^2.

All spaces and inner products here are the original source ones. The derivative cost is not inferred solely from the target weight identity.

The inverse-metric identity is obtained by summing the full residue recurrence, with all interior adjacent terms canceling by a_(j+1)/kappa_(j+1)=1/kappa_j. Its last pair is

    A C_N+C_N A*-C_N
      = (z_(N+1)z_N*+z_N z_(N+1)*)/kappa_N.

In the two parity coordinates its upper-right block is K_even-X K_odd. At N=2n its two endpoint columns give `f_n e_n*/p_n`; at N=2n+1 they give `-f_(n+1)e_n*/u_n`. This proves both signs in SP.32, with the different parity truncations retained. Multiplication on the left by G_even and on the right by G_odd gives the metric discrepancy O=G_odd-G_even X. Its relative form is one outer product, so the squared allowance is exactly the product of the two contracted column norms divided by p_n^2 or u_n^2, respectively. The full original relative characteristic polynomial is lambda^(2D-2)(lambda^2-epsilon^2), including every zero multiplicity.

Writing B=z_(N+1)*G_N z_(N+1), the determinant update gives pi_N=kappa_(N+1)/(kappa_(N+1)+B). Hence

    (1-pi_N)chi_N = B(z_N*G_N z_N)/kappa_N^2 = epsilon_(N-d)^2.

Neither the source proof nor the checker divides by a residue column or its norm. The zero-frontier controls compare pi_N with the next kernel constructed directly from J_(N+1) and M_(N+1); they are therefore independent of substituting the right-hand side of the desired identity.

### A strict strengthening of the two zero cases

The two consecutive residue columns can never both vanish. Indeed the unit U_v is invertible, so z_N=z_(N+1)=0 would imply h divides both q_N and q_(N+1). The three-term recurrence and a_N>0 then imply h divides q_(N-1). Repeating the argument reaches q_0=1, contradicting deg h>=1. Thus:

- If the new column z_(N+1) vanishes, then z_N is nonzero, pi_N=1, and chi_N is strictly positive.
- If the predecessor z_N vanishes, then z_(N+1) is nonzero, chi_N=0, and pi_N is strictly below one.

This is a general exact argument within the stated source hypotheses, not a consequence drawn from the finite examples. Sent to the source author as an optional strengthening of the written endpoint wording.

Snapshot hashes observed for this follow-up:

- Source containing the audited SP.32--35 subsection: `15B2B20E2DA43826024585431754047548237CCA0BA4B495FFC156ECD62FA21B`.
- Checker containing the audited new direct derivative block: `A8CA05D60FEA7097602A62CDF8EFF722799F567D7D8E7C4C300FB9846C5D3ED6`.

These record the files at this read; any subsequent source edits require their own recorded verification. No main proof source or checker was edited by this auditor, and execution receipts are produced separately by the implementing agent.
