# Independent source-ideal, section and quotient review

25 September 2026. Independent mathematical review, ISQ0–ISQ9, of the frozen source endpoint and residue-section continuation. Complete proofs and precise reading limits are retained below.

## ISQ0. Result and exact review scope

No mathematical error was found in the assigned NCI, NJS, RSS, SSR and receiving RSR statements after checking their native proofs and the explicitly identified dependencies below. In particular, residue-one admissibility and identity-induced quotient compatibility are different conditions: P(0)=1 proves the former, while RSR7 correctly requires every root to be an actual original nontrivial zeta zero, with polynomial order no greater than its actual multiplicity, for the latter. The source topology and the full jet orders are essential in this assertion.

Two stronger results are proved here, rather than left as questions. ISQ6 computes the maximal common identity-induced quotient for every admissible polynomial, including those failing RSR7. ISQ7 computes every single-cover equivariant section of its finite quotient and proves joint uniqueness for two multiplicatively independent covers. ISQ8 proves compatibility of the endpoint quotient maps with their canonical sections. These are consequences of the reviewed source arguments, not claims of historical priority.

The only concrete publication-receipt discrepancy found is that SSR's stated NPE/NER reading hashes are not the hashes of the current assigned candidate files; details are in ISQ9. This need not be a mathematical error, since receipts may refer to earlier versions, but they must not be presented as verification of the present bytes without the distinction.

All coefficient calculations occur after the stated complete-history arithmetic reconstruction. The support remains tau〈Z1;no Z2〉, with its retraction and separate branch histories intact. No primitive addition, parity, coordinate or arithmetic value is supplied. No identification with Deligne's geometric extension, no weight vanishing, no off-line-zero existence and no RH conclusion is inferred.

## ISQ1. Original source, multiplier and all exceptional factors

Let B be the entire functions with all original seminorms
\[
b_{A,N}(F)=\sup_{|\Re s|\le A}(1+|\Im s|)^N|F(s)|<\infty.
\]
Taking positive real A or nonnegative integer A gives the same topology by cofinality. Completeness follows from locally uniform convergence of a source-Cauchy sequence and uniform convergence in each weighted strip seminorm. Cauchy's formula bounds every finite derivative evaluation by a larger strip seminorm. Therefore the ideal
\[
I=\{F\in B:F^{(j)}(\rho)=0\text{ for every actual nontrivial zero }\rho,
\ 0\le j<m_\rho\}
\]
is closed. Q=B/I has its actual source quotient topology.

Retain the full original source multiplier, not a replacement zeta function:
\[
F_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s),
\quad F_0(0)=F_0(1)=\frac18,
\quad F_0(-1)=F_0(2)=\frac\pi{24},
\]
\[
F_0(-2k)=\frac{k(2k+1)(-1)^k\pi^k}{2k!}\zeta'(-2k)\ne0
\quad(k\ge1).
\tag{ISQ1.1}
\]
The last coefficient follows directly from the Gamma residue
\(\Gamma(-k+\varepsilon/2)=2(-1)^k/(k!\varepsilon)+O(1)\),
the original zeta expansion \(\zeta(-2k+\varepsilon)=\varepsilon\zeta'(-2k)+O(\varepsilon^2)\), and the retained endpoint factor \(s(s-1)/8\). At a nontrivial zero, all derivatives belong to the full product
\[
F_0(\rho+z)=z^{m_\rho}\frac{(\rho+z)(\rho+z-1)}8
\pi^{-(\rho+z)/2}\Gamma((\rho+z)/2)
\frac{\zeta(\rho+z)}{z^{m_\rho}}.
\tag{ISQ1.2}
\]
The last factor is a nonzero local holomorphic unit at z=0. Thus the exact zero orders are m_rho; no other point is silently made a zero of F0.

The inspected [GLOBAL_MELLIN_SYNTHESIS.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/96b02efaf4511d07f33de5ea4cfb10058e905d7e/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/proofs/GLOBAL_MELLIN_SYNTHESIS.md) S1–S7 constructs F0 from
\[
f_0(v)=\frac\pi2v^2(2\pi v^2-3)e^{-\pi v^2},\quad
k_0(u)=u^{1/2}\sum_{n\ge1}f_0(nu),
\]
and the centered Mellin transform \(\int k_0(u)u^{s-1/2}du/u\). In the raw half-Mellin convention used here the corresponding source is exactly
\(a_0(u)=2u^{-1/2}k_0(u)=2\sum_{n\ge1}f_0(nu)\), with
\(\Theta a(s)=\frac12\int a(u)u^sdu/u\). This explicitly recovers the factor two between conventions. Its Gaussian moments give f0(0)=0 and integral f0=0, and the Fourier identities in S2 give its reflection and rapid decay at both endpoints. S2 therefore proves F0 belongs to B, not only to entire functions.

The same native proof gives
\[
|F_0(s)|\le \exp(C(R+2)\log(R+2))\quad(|s|\le R),
\quad n(R)\le C(R+2)^{3/2},
\]
\[
F_0(s)=e^{a+bs}\prod_\rho(1-s/\rho)e^{s/\rho},
\qquad e^a=1/8,\quad b=F_0'(0)/F_0(0),
\tag{ISQ1.3}
\]
counting each zero through its full order. The analytic factorization theorem is the standard Hadamard input explicitly cited in that native proof; this review checked its receiving calculation, not a new proof of the general theorem. The original-zeta pole and trivial zeros remain represented by ISQ1.1 and are not deleted from the original function. No current identity differentiates a truncated or substituted multiplier.

## ISQ2. Independent check of the full-ideal closure

For F in I, Taylor division by ISQ1.2 makes H=F/F0 entire. At scale R take the union of open radius R^-2 disks about every zero with modulus at most 8R. Their total radii are O(R^-1/2), and every connected component has diameter at most twice that sum: a simple chain of intersecting disks joins any two of its points. Hence every component has diameter less than one for large R, without a zero-spacing assumption.

When R/2≤|s|≤3R outside this union, each retained finite factor obeys
\(|1-s/\rho|\ge1/(8R^3)\). The sum of their logarithmic contributions is at least −CR^(3/2)log R. The finite exponential terms contribute at least
\(-3R\sum_{|\rho|\le8R}m_\rho/|\rho|\ge-CR^{3/2}\).
Dyadic summation of the count in ISQ1.3 proves this reciprocal sum bound and
\(\sum_{|\rho|>8R}m_\rho/|\rho|^2\le CR^{-1/2}\).
For the tail, |s/rho|≤3/8 and
\[
\log|(1-w)e^w|=\Re\left(-\sum_{j\ge2}\frac{w^j}{j}\right)
\ge-\frac85|w|^2.
\]
The tail consequently contributes at least −CR^(3/2). The leading exponential contributes at least −|a|−3|b|R. Keeping each contribution proves
\[
|F_0(s)|^{-1}\le\exp(CR^{3/2}\log R).
\tag{ISQ2.1}
\]
For a point inside a disk component in |Re s|≤A, R≤|s|≤2R, the whole component lies in the strip enlarged by one and in the larger annulus above. Its boundary lies outside the open union. H is entire even at all enclosed zeros, so maximum modulus on the compact closure carries the boundary bound through the component. Smoothness and simple connectivity of that boundary are unnecessary. Dyadic scales and a compact-region bound give
\[
\sup_{|x|\le A}|H(x+iy)|
\le C_{A,F}\exp\{C(|y|+2)^{3/2}\log(|y|+2)\}.
\tag{ISQ2.2}
\]
The supremum is at fixed y, as required in the corrected source.

For every epsilon>0, \(H_\varepsilon=e^{\varepsilon s^2}H\) belongs to B because its factor \(e^{\varepsilon A^2-\varepsilon y^2}\) dominates that subquadratic bound and every vertical polynomial. Its actual image is
\(F_0H_\varepsilon=e^{\varepsilon s^2}F\). For 0<epsilon≤1 the integral remainder, with |s|²≤(A²+1)(1+|y|)², gives
\[
b_{A,N}((e^{\varepsilon s^2}-1)F)
\le\varepsilon e^{A^2}(A^2+1)b_{A,N+2}(F).
\tag{ISQ2.3}
\]
Thus the image converges to F in the full source topology. Since every product F0G has all the original zero orders,
\[
\overline{F_0B}^{\,B}=I.
\tag{ISQ2.4}
\]
This cannot be upgraded to algebraic equality: F0 lies in I, but F0=F0G for G in B forces G=1 by the identity theorem, while 1 is not in B. This confirms the closure qualification in NCI2 and RSS5 exactly.

## ISQ3. Independent density, covariance and domain calculation

Fix the original positive real t and write g_t(s)=e^(ts²). The actual Gaussian discrepancy and original discrepancy are
\[
\eta_{n,t}(s)=g_t(s)\frac{n-n^{1-s}}s,
\qquad\delta_{n,t}(s)=8F_0(s)\eta_{n,t}(s).
\tag{ISQ3.1}
\]
Both are entire source elements with value n log n at s=0, since 8F0(0)=1. To check density independently let Lambda annihilate every eta and set
\[
K_w(s)=g_t(s)\frac{e^w-e^{(1-s)w}}s
=we^wg_t(s)\int_0^1e^{-\theta sw}\,d\theta,
\quad L(w)=\Lambda(K_w).
\]
For s=x+iy, w=a+ib, completing the quadratic gives
\[
b_{A,N}(K_w)\le C_{A,N,t}|w|(1+|b|)^N
e^{(1+A)|a|+b^2/(4t)}.
\tag{ISQ3.2}
\]
The bound follows by writing y=(y−theta b/(2t))+theta b/(2t) in the vertical weight. Parameter derivatives introduce finite powers of s and w, controlled on compact parameter sets by the same negative vertical quadratic. Taylor integral remainders satisfy these estimates too. Hence K_w is source-valued entire and L is entire of growth at most Ce^(C(1+|w|²)). Its exact zeros are L(log n)=0 for all n≥1. For nonzero L, Jensen about any w0 with L(w0)≠0 bounds the number of zeros in |w−w0|≤R by O(R²); a boundary-zero radius can be enlarged within [2R,3R]. The exponentially many integer logarithms with n≤e^(R/2) contradict this. Therefore L=0.

The derivative sign is positive:
\[
(\partial_w-1)K_w=g_t e^{(1-s)w},
\quad\Lambda(g_t e^{vs})=0\quad(v\in\mathbb C).
\tag{ISQ3.3}
\]
To pass to all B, take F in B and real u>t. With H=e^((u−t)s²)F, the exact raw inverse and forward integrals are
\[
a_H(x)=\frac{x^{-1/2}}\pi\int_\mathbb R H(1/2+iy)x^{-iy}dy,
\quad H(s)=\frac12\int_\mathbb R a_H(e^v)e^{sv}dv.
\tag{ISQ3.4}
\]
Cauchy derivative estimates and rapid strip decay justify Fourier inversion; shifting to any fixed real c gives \(a_H(e^v)=e^{-cv}\pi^{-1}\int H(c+iy)e^{-iyv}dy\). Taking c with either arbitrarily large sign proves faster-than-every-exponential decay in |v|. Therefore
\[
e^{us^2}F=\frac12\int_\mathbb R a_H(e^v)g_t e^{sv}dv
\tag{ISQ3.5}
\]
converges in every B seminorm, since b_(A,N)(g_t e^(sv))≤C e^(A|v|) for real v. Passing Lambda through convergent Riemann sums and tails yields Lambda(e^(us²)F)=0. For complex u=p+iq with p>0, the exponent p(x²−y²)−2qxy has a uniform negative vertical quadratic on compact u-sets, controlling derivatives and remainders. The scalar identity theorem extends the zero to Re u>0. Let positive real u decrease to zero using ISQ2.3. Then Lambda(F)=0. Hahn–Banach now proves
\[
\overline{\operatorname{span}\{\eta_{n,t}:n\ge2\}}^B=B.
\tag{ISQ3.6}
\]
Multiplication by the retained 8F0 is continuous. Approximating each source vector by the dense eta span shows that its image span has the same closure as 8F0B. Multiplication of coefficients by the nonzero scalar eight is bijective, so ISQ2.4 yields
\[
\overline{\operatorname{span}\{\delta_{n,t}:n\ge2\}}^B
=\overline{8F_0B}^{\,B}=I.
\tag{ISQ3.7}
\]
No factor is removed from the actual discrepancy map. The same proof works for any degree set whose number of logarithms up to R has limsup divided by R² infinite; hence the square-degree refinement in NCI8/NJS4 is valid.

For the actual corrected tests
\(F^h_m=g_t\phi_m+h_t\),
\(h_t=8g_tF_0/s\),
\(\phi_0=-1/s\),
\(\phi_m=(m^{1-s}-(m+1)^{1-s})/s\),
finite telescoping, including m=0, gives
\[
\sum_{a=0}^{n-1}F^h_{nm+a}-U_nF^h_m=\delta_{n,t},
\quad U_nF=n^{1-s}F.
\]
Applying a continuous source functional and retaining the receiver's conjugation gives
\[
\mathscr W_n^*H_h\Lambda-H_hU_n'\Lambda
=\frac{\overline{\Lambda(\delta_{n,t})}}{1-z}.
\tag{ISQ3.8}
\]
The scalar right side vanishes for all covers exactly when Lambda annihilates I, by ISQ3.7. Such a functional descends uniquely and continuously to Q by its quotient topology. No inverse strong-topology assertion is needed for this criterion.

If H_h Lambda belongs to H², boundedness of W_n^* and the fact that a nonzero constant coefficient sequence is not square summable show
\[
H_hU_n'\Lambda\in H^2\iff\Lambda(\delta_{n,t})=0.
\]
The intersection over all covers is precisely the actual Hardy domain intersected with I-perp. It is invariant since U_n preserves every full zero order. The retained raw identities are W_n^*W_n=nI and W_nW_n^*=nP_n, with P_n block averaging, so the nonnegative degree defect is n times the squared norm of the complementary projection. Neither that term nor its factor n is erased by the ideal theorem. These facts check NCI6–7; receiver injectivity and graph prerequisites were also read in NHJ0–9, but they are not needed to replace any step of this direct criterion proof.

## ISQ4. Sections, shears and receiver prerequisites

In the actual meromorphic space E=B+C h_t, residue at zero is the coefficient c of h_t. Put j_t=g_t/s and k=j_t−h_t=g_t(1−8F0)/s. The numerator is a source function vanishing at zero. For any K in B with K(0)=0, division outside |s|<1 and maximum modulus on |s|=2 give
\[
b_{A,N}(K/s)\le b_{A,N}(K)+2^{N-1}b_{2,0}(K).
\]
Thus k belongs to B, with k(0)=−8F0'(0). Both sections give precisely the same product topology on the same meromorphic functions.

More generally take any polynomial P with P(0)=1 and hP=g_tP/s. Then bP=hP−h_t=g_t(P−8F0)/s belongs to B. The exact primal and strong-dual changes are
\[
(F,c)_h\mapsto(F-cb_P,c)_P,
\qquad(\Lambda,\alpha_h)_h\mapsto
(\Lambda,\alpha_h+\Lambda(b_P))_P.
\tag{ISQ4.1}
\]
The inverse has opposite signs. Evaluation on the fixed bP is continuous in the strong dual because its singleton is bounded; product bounded sets and their bounded projections justify the strong-dual product coordinates. These formulas therefore prove a topological isomorphism, not only a formal relabeling.

The actual cocycle is deltaP=n hP−U_n hP=P eta_n, and
\[
\delta^P_n=\delta_n+(n-U_n)b_P,
\quad (U_n^E)'(\Lambda,\alpha_P)
=(U_n'\Lambda,n\alpha_P-\Lambda(\delta^P_n)).
\tag{ISQ4.2}
\]
This is a complex-linear transpose, so no conjugation belongs in its last term. The receiver uses conjugation separately:
\[
H_P\Lambda=H_h\Lambda+\frac{\overline{\Lambda(b_P)}}{1-z},
\quad M\widetilde\Lambda
=H_h\Lambda-\frac{\overline{\alpha_h}}{1-z}
=H_P\Lambda-\frac{\overline{\alpha_P}}{1-z}.
\tag{ISQ4.3}
\]
Indeed its unchanged meromorphic tests are G_m=g_t phi_m, each with residue −1; adding the chosen section makes them entire, and the two corrected sequences differ by bP in every coefficient. Their source seminorms have polynomial growth in m by the finite-difference formula and Gaussian decay, so all series converge on compact subdisks. The same actual function in ISQ4.3 has the same Hardy norm whenever defined. No Hardy membership of either separately divergent boundary term is inferred.

The old invariant lift (Lambda,0)_h for Lambda in I-perp becomes the graph alphaP=Lambda(bP). Its exact invariance follows from
\(n\Lambda(b_P)-\Lambda(\delta^P_n)=\Lambda(U_nb_P)\).
For the Gaussian section, the zeroth corrected test is zero; hence beta=−conjugate(M Lambda-tilde(0)), retaining rather than deleting the residue coordinate.

Modulo I the old cocycle vanishes, so [h_t] defines an equivariant residue section. Uniqueness holds already for any fixed n>1: at every actual nontrivial zero rho, |n^(1−rho)|<n, so n^(1−s)−n is a local holomorphic unit; if its product with F has all the zero jets then F has all of them. By contrast no equivariant section exists in E: the correction equation (U_n−n)F=delta_n has left value zero at s=0 and right value n log n. All multiplicities in these arguments are full local orders.

## ISQ5. Exact polynomial quotient criterion

For nonzero P with P(0)=1 write d_a for its root orders. Every root a is nonzero. Polynomial multiplication maps B continuously into B; its image is exactly
\[
PB=\{F\in B:F^{(j)}(a)=0\ (0\le j<d_a)\}.
\tag{ISQ5.1}
\]
To verify the reverse inclusion, F/P is entire. Outside small fixed disjoint root disks, 1/P is bounded by its polynomial behavior at infinity and a compact-set bound. Inside the disks use maximum modulus on the entire quotient. Their vertical weights are bounded and a single enlarged strip contains them. Thus
\[
b_{A,N}(F/P)\le C_Pb_{A,N}(F)+C_{P,A,N}b_{A_0,0}(F).
\tag{ISQ5.2}
\]
This proves continuous division on the image, and ISQ5.1 proves closedness. Since eta is dense, the closed span of deltaP is exactly PB.

The finite full jet map
\(F\mapsto(F^{(j)}(a))_{a,j<d_a}\)
is onto: multiplication of a polynomial p by e^(s²) is an invertible triangular map on each finite jet space, with diagonal e^(a²). Prescribe the inverse jets of p using polynomial Chinese remainders modulo (s−a)^d, retaining each Taylor coefficient p^(j)(a)/j!. This produces a source function e^(s²)p with any requested finite jets. Choosing those representatives linearly gives a continuous finite-dimensional right inverse. Hence
\[
B/PB\simeq\bigoplus_a\mathbb C^{d_a}
\tag{ISQ5.3}
\]
with its actual quotient topology. In derivative coordinates the action retains the full formula
\[
U_n'\operatorname{ev}_a^{(j)}
=n^{1-a}\sum_{b=0}^j\binom jb(-\log n)^{j-b}
\operatorname{ev}_a^{(b)}.
\tag{ISQ5.4}
\]
Consequently the largest invariant zero-P-coordinate slice is exactly (PB)-perp with scalar coordinate zero, not an arbitrary selected spectral subspace.

The identity on B induces a map Q→B/PB exactly when I⊂PB, since changing a representative changes it by an arbitrary element of I. Necessity of the root condition follows from F0∈I: the inclusion forces F0 to vanish at a to order at least d_a. ISQ1.1–2 says precisely that a must be an actual nontrivial zero and d_a≤m_a. Conversely every F∈I has those orders, so ISQ5.1 proves inclusion. This proves the full equivalence and an explicit failure witness: if the criterion fails, F0 represents zero in Q but a nonzero class in B/PB.

When the criterion holds, the induced surjection is continuous and open. For an open V⊂Q, its inverse image in B is open and its image under the open quotient B→B/PB is exactly the image of V. Its kernel is PB/I. The map is cover-equivariant by the same source multiplier; its transpose includes precisely the selected full derivative functionals. The condition P(0)=1 does not imply this root compatibility; it only ensures the stipulated residue-one section.

## ISQ6. Stronger result: the exact common quotient even for incompatible P

For every root a of P define \(m_a=\operatorname{ord}_aF_0\); it equals the actual nontrivial-zero multiplicity on that divisor and is zero elsewhere. Put
\[
r_a=\min(d_a,m_a),\qquad
R(s)=\prod_{a:\,r_a>0}(1-s/a)^{r_a},
\tag{ISQ6.1}
\]
with empty product R=1. This retains the exact constant R(0)=1 and every common multiplicity. The stronger algebraic equality is
\[
\boxed{I+PB=F_0B+PB=RB.}
\tag{ISQ6.2}
\]
In particular the sum is already closed; a closure need not be added.

Here is a complete proof. Both I and PB vanish to orders at least r_a at every indicated point, so their sum lies in RB by polynomial division. For H∈RB, work at each root a in its finite Taylor algebra C[z]/(z^d_a), z=s−a. The full original multiplier is F0(a+z)=z^m_a u_a(z), with u_a(0)≠0. Multiplication by that element has image precisely the ideal generated by z^r_a. Indeed if m_a≥d_a its image is zero; otherwise u_a is invertible in the finite algebra and multiplication by z^m_a has that exact image. Because H vanishes to order r_a, there is a Taylor class B_a such that F0 B_a agrees with H modulo z^d_a. If m_a<d_a, B_a is obtained by the Taylor expansion of z^(-m_a)H/u_a through order d_a−m_a−1 and arbitrary higher coefficients; if m_a≥d_a, choose B_a=0.

Finite jet surjectivity from ISQ5 gives B0∈B realizing all these classes simultaneously. Therefore H−F0B0 has all P-jets zero and lies in PB. Hence H belongs to F0B+PB⊂I+PB. This proves every equality in ISQ6.2, without replacing F0B by I algebraically and without an infinite interpolation assertion.

Let d=deg P and r=deg R=Σr_a. In the d-dimensional quotient B/PB the exact image of I, already attained by F0B, is the direct sum of the ideals z^r_a inside C[z]/z^d_a. Its dimension is d−r. These are precisely the surviving representative-dependence directions, and the quotient by them has dimension r. Thus the complete common-quotient diagram is
\[
\begin{array}{ccc}
Q=B/I&\longrightarrow&B/RB\\
&&\uparrow\\[-2pt]
&&B/PB.
\end{array}
\tag{ISQ6.3}
\]
Both arrows are continuous open cover-equivariant surjections induced by the identity on B. The first has kernel RB/I, the second RB/PB. Every other quotient B/J receiving both through that same identity must satisfy I⊂J and PB⊂J, hence RB=I+PB⊂J. Consequently its map factors uniquely through B/RB. This proves maximality among common identity-induced source quotients, with the usual reverse ordering of kernels. It is not a claim about arbitrary abstract quotient isomorphisms.

All retained derivative functionals are exactly those with j<r_a and have ISQ5.4's unchanged action. If P shares no original zero, R=1 and the common quotient is zero; if P meets the original divisor with excess orders, exactly the smaller original orders survive. If P satisfies RSR7, R=P and ISQ6.3 reduces to the already proved Q→B/PB. This calculates the strongest common identity comparison even when the requested direct map fails.

## ISQ7. Stronger result: every finite quotient's equivariant sections

The actual endpoint quotient E/PB is topologically (B/PB)⊕C in hP coordinates and the cover action is diagonal because deltaP∈PB. Its residue character is n. Every continuous linear residue section is therefore
\[
\sigma_v(c)=c([h_{P,t}]+v),\qquad v\in B/PB.
\tag{ISQ7.1}
\]
It is n-equivariant precisely when (U_n−n)v=0.

Fix n>1. In the a-primary finite Taylor algebra, the multiplier is
\(q_n(a+z)=n^{1-a}e^{-z\log n}-n\).
If n^(-a)≠1 then its constant term is nonzero, so it is a unit and the kernel is zero. If n^(-a)=1, its exact first term is −n log n·z, whose coefficient is nonzero. Thus q_n=z times a holomorphic unit. In C[z]/z^d_a its kernel is exactly C z^(d_a−1). Therefore the affine space of n-equivariant residue sections is based at [hP] and has one complex parameter for each distinct root a with n^(-a)=1, regardless of its multiplicity. In undivided derivative coordinates that parameter affects the top derivative by the retained factor (d_a−1)!; it is not a deletion of the lower jet action.

For two multiplicatively independent positive integers n,l>1, no nonzero a can satisfy n^(-a)=l^(-a)=1. Those equations imply Re a=0 and
\(\Im a\log n\in2\pi\mathbb Z\),
\(\Im a\log l\in2\pi\mathbb Z\).
If Im a≠0 the ratio log n/log l is rational, which would imply n^q=l^p for positive integers p,q, contradicting the stipulated independence. If Im a=0 then a=0, excluded by P(0)=1. Hence the two kernels have zero common intersection in every primary block. It follows that
\[
\boxed{[h_{P,t}]\text{ is the unique residue section equivariant jointly under }U_2,U_3,}
\tag{ISQ7.2}
\]
and in particular the unique all-cover-equivariant section, for every admissible P, including arbitrary non-zeta roots. The positive integers 2 and 3 are used only after the complete-history arithmetic construction; this is not an initialization of that arithmetic or a primitive operation on tau.

This uniqueness is not the RSR7 compatibility criterion: even a polynomial with roots unrelated to the original divisor has that unique joint section in its own finite endpoint quotient. To receive the original quotient through the identity it must still satisfy ISQ5, or pass through the smaller common quotient ISQ6.

## ISQ8. Endpoint quotient maps retain the canonical sections

If P satisfies the exact root criterion, the identity of E induces a continuous open cover-equivariant surjection
\[
E/I\longrightarrow E/PB.
\tag{ISQ8.1}
\]
Its kernel is PB/I and it is identity on the residue character. Furthermore
\[
h_{P,t}-h_t=\frac{g_t(P-8F_0)}s\in PB.
\tag{ISQ8.2}
\]
To prove the stronger inclusion, at every P-root a the numerator vanishes to order at least d_a because both P and F0 do; a≠0 and g_t is a unit there. The difference is in B by removable division at zero, so ISQ5.1 proves PB membership. Therefore (ISQ8.1) sends [h_t] to exactly [hP], not to an unspecified section. In the diagonal coordinates on both quotients it is ([F],c)↦([F],c), with the first quotient-map component from ISQ5.

For an arbitrary P the same proof with R of ISQ6 shows hP−h_t∈RB, since both P and F0 vanish to at least r_a there. Thus the two identity-induced endpoint maps
\[
E/I\longrightarrow E/RB\longleftarrow E/PB
\tag{ISQ8.3}
\]
carry their canonical residue sections to the same actual class. The finite source kernels and all residual multiplicities remain those already calculated in ISQ6. This is the complete endpoint comparison supplied by the common-quotient result; it does not claim the unquotiented E has an equivariant section.

## ISQ9. Source locators, receipts and bounded human-source coverage

Final supplementary check: this main reviewer also read the completed D8 addition to the child note and the complete `NJS_DENSITY_RECEIVER_INDEPENDENT_CHECK_20260925.md`, SHA256 `ed842cc788667619db829062579865f0896defb31a79d25398508cdebb7d7fc6`. It independently confirms the source-density mechanism used in ISQ3 and the full meromorphic receiver injection. Its precise formula caution is that the general first-n receiver coefficient sum equals minus the conjugate of tildeLambda(V_log n). NPE6/NER7 omit that written conjugation in the zero-receiver sentence; the zero inference remains correct, but the shorthand must not be exported as a general nonzero-data identity. The final child note D1–D8 has SHA256 `fd2bef7a5a84ff0f38a9c2d119959ecaf949955f7e5f85dcbf390c8df0d177be`.

The following assigned candidate native Markdown files were read completely. All paths in this list are relative to `the frozen incoming source directory`:

| Source | Exact proof locators | SHA256 |
|---|---|---|
| READ_THIS_CONTINUATION.md | all 11 lines | 974bf5af25587b22fb145fa2ae17ce2c9c5c978e48c53145f74e1f9400cb7a15 |
| NOOR_COVER_DISCREPANCIES_GENERATE_ORIGINAL_IDEAL.md | NCI0–8; division lines 80–153, density 155–281, covariance/domain 283–364 | eb6163cc6fa78c8c84d2f87e44a36cfa653d4e3d2bf768e056ab62e7c8d2d16c |
| NOOR_RESIDUE_SECTION_DEPENDENCE.md | NJS0–10, including square-cover refinement and both Hardy domains | bb26684d6aae262e72ded39dec138c6bc2fc46a0f5f52e419b95c5831cd757f3 |
| RESIDUE_SECTION_SELECTION_AND_ORIGINAL_IDEAL.md | RSS0–6; polynomial image lines 80–110; quotient map 169–191 | ac69b79cac80878918e8a482f26d2bed7d7d69fd8ce3267ba3bee751f5ac61a7 |
| SECTION_SHEAR_AND_QUOTIENT_REVIEW.md | SSR0–7; shear 36–128, unique quotient section 130–169, complete receiver 202–290 | 8ed654893bf227e51625279801a55c52c00013c59f44b0d7e28f7e11752ecfd5 |
| RESIDUE_SECTION_SELECTION_INDEPENDENT_REVIEW.md | RSR0–8; full quotient criterion lines 431–441 | ab4d1e0a218813a6c552707d673977e00cf9cb3ef3a28a8570925a2b4b8ba45b |
| NOOR_ORIGINAL_ZETA_JET_RECEIVER.md | NHR0–9, receiving context and original coefficient/degree formulas | 64e5452900292ba9431ba8c16e42921da364fa74a24153408ff360fc6ae40d65 |

Also read the complete [NOOR_FULL_DUAL_INJECTIVITY_AND_HILBERT_DOMAIN.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-source-endpoint-and-section/NOOR_FULL_DUAL_INJECTIVITY_AND_HILBERT_DOMAIN.md), NHJ0–9, especially NHJ1–4 source estimates and injection, NHJ6 graph and NHJ7 prequotient formula, SHA256 `2757e36087a631983cc84b2f919138b864a594d0492155b26c513e85a0ade8e7`. The NHJ8 use of Noor's adjoint-domain theorem was read for dependency scope but is not independently attributed to a fresh author-source reading in this bounded review.

The complete native [GLOBAL_MELLIN_SYNTHESIS.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/96b02efaf4511d07f33de5ea4cfb10058e905d7e/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/proofs/GLOBAL_MELLIN_SYNTHESIS.md) S1–S7 and later exact-image notice were read at the parent programme directory, SHA256 `71376fe8074ca8a20623e4e829be5bce74455a447bbdb677156f28e561553e9f`. Its complete independent review R1–R5 was read there, SHA256 `21e991e1e2f793a98d80f7a6a92d7d488fc7e50e4527b92f5704171dfd244dfb`. This review independently checked their receiving product/division estimates in ISQ1–2. The cumulative TeX retains the Hadamard source passage around lines 5211–5229 and the formula around 5371; the standalone GLOBAL files are not top-level files of this candidate directory. A public point-use link should target the retained cumulative proof or an actually published native file, not an absent relative path.

Human-source provenance retained, not falsely expanded: S. Waleed Noor, *A Hardy space analysis of the Báez-Duarte criterion for the RH*, [arXiv:1809.09577v4](https://arxiv.org/abs/1809.09577v4), §§1–5, canonical `PUBUNIT-803463A3EF787AE3E69C519B`, author-TeX hash `bc3075483547782dce36bf55a6349899a26766fcfc8ae9f265079ec74601f2d3`. NHR records exact author-source reading through line 387, including cover lines 262–288. This bounded reviewer read the native programme source and directly verified the block operator and coefficient calculations; it did not claim another full Noor author-source reading. Likewise GLOBAL S2 cites Alain Connes, *The Riemann Hypothesis: Past, Present and a Letter Through Time*, [arXiv:2602.04022v1](https://arxiv.org/abs/2602.04022v1), `rhready.tex` lines 526–535 for Hadamard factorization, author-TeX hash `7f1888d82b42263faca4264f3f9fc77e5750c348640f85db0ac4569fe88ebab2`. Its historical Hadamard 1892 attribution is mediated there; that original historical article was not newly read here. No literature discovery or PDF reading was performed.

Receipt issue: SSR lines 31–32 identify NPE and NER hashes `da8a4d25c22391e32fddc44fac98d12de515679f2d5b013ee33639c6200134ed` and `c05f47854508143b2aeb3ea42a7e0dbd74fe5c3da9b00923dd0bacc6ad44442e`. The current assigned [NOOR_MEROMORPHIC_ENDPOINT_EXTENSION.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-source-endpoint-and-section/NOOR_MEROMORPHIC_ENDPOINT_EXTENSION.md) hashes to `100d5fa09ed7cc778e1993de9fb164ba9e1a7e525e9d99b6f8367cf441aee926`; the current [NOOR_ENDPOINT_EXTENSION_INDEPENDENT_REVIEW.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-source-endpoint-and-section/NOOR_ENDPOINT_EXTENSION_INDEPENDENT_REVIEW.md) hashes to `49c9d21a63e75ef23b082bbdc2f01dd576d6397a3029c1ca7428ceb2ecf887b9`. The older hashes should be labeled as historical reading witnesses, while the new review receipt pins the current candidate. The mathematical child check read those current endpoint dependencies independently and records its full coverage separately. This main-agent review does not convert a child reading into its own claimed reading.

The source uses standard Jensen, maximum-modulus, Fourier inversion, identity theorem, Hahn–Banach and finite polynomial Chinese remainders. Their particular applications and constants were derived in ISQ2–5. A human point-use bibliography may credit general theorem treatments, but none of those general classical theorems is being claimed as original programme mathematics. The genuinely further calculations preserved here are ISQ6–8, and the source's source-topological restrictions remain part of their statements.

The independent mathematical child supplied `SECTION_SHEAR_INDEPENDENT_CALCULATION_20260925.md`, D1–D7, which this main reviewer read completely. D1–D4 independently check the same source shears and receiving maps; D6 independently confirms ISQ6–7. Its additional D5 calculation gives unconditional strict incomparability of the two corrected Hardy domains using only actual evaluations at s=1 and s=2, rather than assuming an off-line zero. In detail, with c=e^(4t)(3−pi)/6≠0, the full functionals Xi_h=ev_2−(pi/6)e^(3t)ev_1 and Xi_j=ev_2−(1/2)e^(3t)ev_1 have respective (alpha,beta)=(0,c) and (−c,0). Their full receiver images are e^(4t)(g_2+pi/6) and e^(4t)(g_2+1/2), where g_2=−1/2+sum_{m≥1}z^m/[2m(m+1)] belongs to H². The shear therefore puts their restrictions in D_h minus D_j and D_j minus D_h respectively. The nonzero term c/(1−z) proves each failure. This verifies the child's stronger consequence directly, with all original endpoint values retained; its supplementary derivation is retained privately in D5 of that check. The explicit witnesses and their receiving calculation are given here. The supplementary private files mentioned in this reading record are not distributed as part of this edition.
