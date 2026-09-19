# The original coefficient image, its arithmetic compression, and membership

19 September 2026. New deductions from the exact NCT and COB maps, on their original simple-quartet domain. This is not an evaluation of the native minimum metric D, and it does not change that metric to the arithmetic moment metric.

## 1. The prescribed minor has an explicit value

Use NCT6–7 at degree a. Put q=(a+1)^2, q'=(a-7)^2, m=q-q'-v, c=a/2. The actual conductor has derivatives mu_d, with mu_0=...=mu_{v-1}=0 and mu_v nonzero. The lower roots are beta_(a-8,u,w), and the upper roots are beta_(a,u,w). All root labels and the lexicographic order are retained.

The conductor identity N_(C^T eta)(z)=E_A(z) sum_lambda eta_lambda exp(lambda z) gives

    (V_a C^T)[v+r,lambda]
      = sum_(d=v)^(v+r) binom(v+r,d) mu_d lambda^(v+r-d).

The right side is the evaluation of a polynomial P_r of degree r, with leading coefficient binom(v+r,v) mu_v. Therefore the determinant of the first q' rows of J_(v,a)=P_v^T V_a C^T is exactly

    mu_v^(q') [product_(r=0)^(q'-1) binom(v+r,v)] det V_lower.

It is nonzero. Thus the first ordered nonzero minor prescribed by NCT7 is the first q' rows, and the complementary selector is precisely

    J_a = {q',...,q-v-1}.

Consequently Z_exp,a = V_a^(-1) E_high, where E_high inserts the m coordinate vectors at derivative indices q-m,...,q-1. This is an evaluation of the original selector, not a replacement by a new complement.

## 2. Compute every column of the actual residue injection

Write chi(S)=sum_(t=0)^q c_t S^t, c_q=1. COB4 defines

    L_a z = sum_beta (Z_exp,a z)_beta chi(S)/(S-beta).

For the j-th column, 0<=j<m, let b=Z_exp,a e_j. Its first q moments are

    sum_beta b_beta beta^n = delta_(n,q-m+j),  0<=n<q.

Expanding the exact partial-fraction identity at infinity gives

    (L_a e_j)(S) / chi(S) = sum_beta b_beta/(S-beta).

Taking the polynomial part after multiplying by chi proves

    ell_j(S) := L_a e_j
       = [chi(S)/S^(q-m+j+1)]_+
       = sum_(t=q-m+j+1)^q c_t S^(t-q+m-j-1).             (F1)

Its degree is m-1-j and its leading coefficient is one. Thus, in the reverse degree order, the coefficient matrix of L_a is unit triangular. In particular,

    image L_a = P_(m-1) subset C[S]/chi.                  (F2)

For any P of degree below m, its exact preimage has coordinates

    z_j = coefficient of S^(-(q-m+j+1)) in P(S)/chi(S).

The first q-m Laurent coefficients vanish. These expressions are inverse to (F1). They retain the full chi coefficients and the selected conductor moment chart.

This statement concerns the COB residue map. The native metric on its coefficient domain is still the full DNE/PRD minimum after conductor division. No equality of that native metric with the source moment Gram follows from (F2).

## 3. Exact intersections with arithmetic primary subspaces

For an actual monic divisor g of chi, let J=deg g. Polynomial division gives

    ker g(A) = (chi/g) P_(J-1) in E,

where A is the original multiplication by S. Intersecting literal representatives of degree below q with (F2) gives

    image L_a intersect ker g(A)
       = (chi/g) P_(m-q+J-1),
    dimension = max(0,m+J-q).                           (F3)

A polynomial space of negative degree is zero. This is an equality of subspaces with the displayed multiplication map, not a dimension heuristic.

A terminal eigenvector has J=1, and a reflected pair has J=2. On the original eventual domain m<=q-2, neither nonzero terminal vector nor a nonzero vector in that pair belongs to image L_a. In particular the terminal CRT representative chi/((S-lambda)chi'(lambda)) has degree q-1.

For the positive-real-displacement primary subspace E_+, the actual odd rectangular grid has J=q/2. For a>=29 and v>=0, m<=q/2. Hence

    image L_a intersect E_+ = {0}.                       (F4)

Under the original full-unit theta injection these remain the same statements: apply its injectivity to the displayed intersections. No unit value is set equal to one.

The smallest A-invariant space containing image L_a is all of E, since 1 belongs to image L_a and 1,A1,...,A^(q-1)1 is the original monic basis. More precisely,

    sum_(r=0)^d A^r image L_a = P_(min(q-1,m+d-1)).        (F5)

The rank rises by one at each step until q. Four copies give rank 4 min(q,m+d).

## 4. The actual compression is a finite Jacobi operator

The metric G_(q-1) is exactly the original source moment Gram on P_(q-1), because the remainder map there is the identity. Use the actual even arithmetic measure dmu=w_h^{*a}(y)dy on S=c+iy. Let varphi_0,...,varphi_m be its orthonormal polynomials, with positive leading coefficients, and let omega_r be the squared monic norms. Define

    a_r = sqrt(omega_r/omega_(r-1)), r>=1.

Orthogonality and evenness prove, without a change of measure,

    y varphi_r = a_(r+1) varphi_(r+1) + a_r varphi_(r-1).

Let T be the unique coefficient matrix defined by

    L_a z(c+iy) = sum_(r=0)^(m-1) (Tz)_r varphi_r(y).

It has inverse because of (F2), and T* T = L_a* G_(q-1) L_a. Thus T is the exact isometry from the retained coefficient metric to these orthonormal coordinates.

Let J_m be the real symmetric tridiagonal matrix with off-diagonals a_1,...,a_(m-1). Since m<q, multiplication of P_(m-1) by S has degree at most m and involves no reduction modulo chi. The original COB15 compression and residual therefore satisfy

    T A_H T^(-1) = c I_m + i J_m,                        (F6)
    (A L_a-L_a A_H) T^(-1)
       = i a_m varphi_m e_(m-1)^T.                      (F7)

For four copies replace T and J_m by I_4 tensor T and I_4 tensor J_m. The residual has exactly rank four, and all four nonzero singular values in the specified domain/source norms are a_m.

The characteristic polynomial of J_m is the actual monic orthogonal polynomial pi_m: the determinants of yI-J_r obey its same recurrence and initial values. Its eigenvalues are real and simple; a repeated eigenvalue would have two eigenvectors, while the nonzero off-diagonals make every eigenvector determined by its first coordinate. Thus the compressed spectrum is exactly c+i times the m real zeros of pi_m, each repeated four times in the four-copy space.

Writing G_H=M* G M gives the exact identity

    A_H* G_H + G_H A_H - a G_H = 0.                      (F8)

This is a statement about the compressed action, with its explicit nonzero residual (F7). It is not the corresponding identity for the original operator A on E.

## 5. Return to the boundary forms without replacing their metric

Keep the actual COB forms Gamma_i=M* M_i M. Put Q_i=(I_4 tensor T)^(-*) Gamma_i (I_4 tensor T)^(-1). Then the compressed boundary weight defect is exactly

    (I_4 tensor T)^(-*)
      (A_H* Gamma_i+Gamma_i A_H-a Gamma_i)
      (I_4 tensor T)^(-1)
       = i [Q_i, I_4 tensor J_m].                       (F9)

It has relative trace zero. It vanishes exactly when the displayed matrices commute. This criterion does not assert commutation for the original Gamma_i.

For each original cone subspace X=B,S,W, let P_X^G be its orthogonal projection in G_H. Its actual compressed preservation residual is

    (I-P_X^G) A_H P_X^G.

In the above isometry it is i(I-P_TX)(I_4 tensor J_m)P_TX. The full arithmetic action additionally retains (F7). Thus proving preservation under this critical-line Jacobi compression would still not turn M into an intertwiner of the original arithmetic action.

On the proper-source boundary image, retain both COB tangential and normal terms:

    S beta_i-beta_i A_H
      = boldDelta_i (R+boldC_i M)+boldN_i M.

Equations (F7) and (F9) evaluate the previously unspecified arithmetic compression and its residual in this expression. They do not delete either boundary term or assert that the original cone subspaces are invariant.

## Scope

The original terminal class is excluded from this particular arithmetic image by (F3), and the entire positive-primary space is excluded on (F4)'s stated domain. A recovery claimed through this image must use an actual different preimage or an enlargement, whose minimal invariant enlargement is explicitly (F5). This does not assert that the original observation Lambda, the original proper-source value space Z_R, or every possible geometric comparison has this kernel. Those are different specified maps, and no substitution for them has been made here.

## 6. Full invariant closure in the actual proper-source packet

COB7–9 puts every nonzero one-copy boundary image in the actual module

    E_2=C[S]/chi^(a+1),
    p=Delta_i L_a z=chi R, deg R<=q.

Its cyclic submodule under the original S action has the exact annihilator

    ann(p)=chi^a / gcd(chi^a,R).                         (F10)

Proof: chi^(a+1) divides f chi R exactly when chi^a divides fR. Prime-by-prime valuation gives (F10), with every multiplicity retained. Therefore

    dim C[S]p = a q-deg gcd(chi^a,R) >= (a-1)q.          (F11)

This applies to each nonzero image, not merely to an unspecified ambient module. The original full-unit injection Psi_2 preserves its annihilator because it is injective and intertwines the actual S action.

In particular no nonzero boundary image can lie in an S-invariant subspace of dimension O(a) on this family. An actual invariant enlargement of even one of those image vectors has the lower bound (F11). This is about the specified COB image and original action; no assertion is made about unrelated geometric realizations.

There is also a quantitative spectral return for that enlargement. The cyclic module in (F10) has primary multiplicities a-d_lambda, where d_lambda=min(a,ord_lambda R) and sum d_lambda<=q. The positive weight trace lower bound for every positive metric on that module is

    sum_lambda (a-d_lambda) max(2 Re lambda-a,0)
      >= a L_(h,a)-2a delta q
      = delta a q(a-3)/2,                              (F12)

where L_(h,a)=delta q(a+1)/2 is the original simple-packet exterior benchmark. The inequality uses the explicit maximum positive displacement 2a delta and the complete degree bound on R. It follows by the same triangular-flag trace inequality proved in note 04.

Thus enlarging the small coefficient image to close it under the actual proper arithmetic action carries a large, explicit spectral cost; it does not preserve a small-rank compressed allowance for free. The coefficient-cone preservation calculation under A_H and the true invariant enlargement under S remain related by the displayed residual and the actual cyclic-annihilator map.

## 7. The invariant core of this coefficient image is zero

The degree description above has a further exact consequence. There is no nonzero A-invariant subspace contained in im L_a=P_(m-1). Indeed, choose in such a subspace a nonzero polynomial of maximal occurring degree d<m. Multiplication by S has degree d+1<=m<q, so no reduction by chi occurs. Its image cannot belong to a subspace all of whose elements have degree at most d. The same argument uses the largest degree among the four components to prove the statement for im M=(P_(m-1))^4. Thus the entire A-invariant core of this original coefficient image is zero, not merely its intersection with one selected eigenspace.

The source-metric compression A_H still exists, but its exact spectrum is c+i t_j, with all t_j real (the real Jacobi eigenvalues). The original A has spectrum c+(2a_0-a)delta+i(2b_0-a)gamma; because a is odd, none of its real parts equals c. Consequently the actual Sylvester map

    S(X)=A X-X A_H

has zero kernel and is invertible on Hom(H,E^4). To see this without an abstract spectral identification, use the original root-value CRT coordinates on E and the orthonormal Jacobi eigenvectors on H. It acts on each matrix entry by multiplication by

    (2a_0-a)delta+i[(2b_0-a)gamma-t_j],

whose modulus is at least delta. Its inverse is division by precisely that displayed nonzero number; no root, unit or coefficient direction is omitted.

Since the computed residual is R=A M-M A_H, the unique correction X satisfying

    A(M+X)=(M+X)A_H

is

    X=-M.                                                (K20)

Therefore an exact action-compatible correction within this specified finite source/target problem kills the entire inclusion. This does not rule out another source action, a larger complex with its own defect map, or a different arithmetic realization. It computes the full correction problem for the actual compression in COB.15: its affine solution set is the single point -M. In particular the rank-four residual cannot be erased while retaining a nonzero intertwining map with that compressed action.
