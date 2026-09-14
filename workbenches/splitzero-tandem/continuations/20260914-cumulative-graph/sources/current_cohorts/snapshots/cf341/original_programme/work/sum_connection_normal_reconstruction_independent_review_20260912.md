# Independent final audit of finite normal-image reconstruction

Date: 2026-09-12. The complete new subsection FC.28–FC.36, including
FC.29a, of `tex/sum_connection_stieltjes.tex` was read and checked at
whole-file SHA256
`ff30e49f3d33df24fbacbd4504ede5e82bff251d248cccb4d594905e26a97b45`.

The first 26,504 bytes have SHA256
`639fc202b30a5504a6b280f0b8dd155daaa48d12f3e9da80fe9ac30c524c744a`,
exactly the prior complete FC.1–FC.27 file. This byte-prefix equality
was independently recomputed. The earlier strictness review therefore
continues to apply to FC.21–FC.27 without any silent revision.

After that read, the root made the earlier FC.4 typesetting/prose edit
recorded in `logbook/stieltjes_typesetting_repairs.json`, producing
whole-file SHA256
`fb453c93e3a08e3ed2aca04691e9401b13779be137eb07b2de55571df6b888cc`.
The FC.28–FC.36 subsection is byte-for-byte unchanged; its SHA256 is
`03b2f13329d4a18e75d2f7328b072f9faf2f4d698aa991ec3896c6a56e0fceeb`.
To verify the historical/current comparison, the recorded earlier
window was reversed in memory and the recovered whole-file bytes were
checked against the already read `ff30e49...` hash. They matched exactly.
That immutable historical snapshot and the unchanged subsection are
retained beside this review. The prefix statement above is explicitly
about the revision before the root's later FC.4 edit, not a claim that
the current whole-file prefix still has that hash.

**Final result: the reconstruction, its two retained metrics, the full
arithmetic derivative observation, and gauge transport pass. No further
mathematical correction is required.** No TeX file was edited by this
reviewer and no numerical or implementation-mirroring test was used in
place of the proof. The bounded audit ends with this reconstruction.

## 1. The literal finite source and its degree bounds

FC.28 retains the exact index set (alpha,n) with 0<=n<=M-ell_alpha,
the polynomial theta_alpha(z) S^n, and the coefficient matrix
C_M[beta,(alpha,n)]=delta_(alpha,beta)(k/2+iu)^n. Its derivative
is exactly i n(k/2+iu)^(n-1) for n>=1 and zero for n=0.

For completeness, independence over C of the relative polynomials
also gives independence of these source columns over the coefficient
polynomials in S. In any vanishing sum, first collect each power S^n;
its coefficient is a C-linear combination of the independent relative
polynomials, and every scalar coefficient is consequently zero. Thus
p -> P_p is an isomorphism onto precisely the stated finite source.
The independent original coordinates (S,z_1,...,z_(k-1)) justify this
comparison; no relation among the independent relative variables was
silently omitted. When the frame specifies a proper admitted summand,
the text retains that summand rather than claiming the whole numerator.

## 2. Actual Hilbert maps, their domains, and all three computed forms

The ambient space K=L2(du;L2(dy)) uses the original measures. Each
normal column N_u C_M(u)e_j lies in K because orthogonal projection
is a contraction and j_u' C_M(u)e_j is a polynomially weighted
Schwartz function of the full variables. Each tangent column is the
projection by Pi_u of partial_u(j_u C_M(u)e_j), so it is in K as
well. In particular both finite-column maps are bounded from the
literal Euclidean coordinate space C^(q_M) to K.

The positive forms are computed from those actual amplitudes:

\[
 H_M^0=\int C_M^*WC_M,\qquad
 H_M^N=\int C_M^*\mathcal N C_M=\mathbf N_M^*\mathbf N_M,
 \qquad
 H_M^\partial=\mathbf T_M^*\mathbf T_M+H_M^N.
\]

A nonzero coefficient vector gives a nonzero vector polynomial C_M p.
At least one of its components is a nonzero polynomial in u; its common
zero set is therefore finite. Positivity of W and the previously proved
almost-everywhere strict positivity of mathcal N imply respectively
H_M^0>0 and H_M^N>0. Every matrix entry is finite by the integrability
just established. The graph form H_M^partial is positive as well.

FC.29a correctly preserves the original source-amplitude form H_M^0
and the distinct form pulled back from the normal observation H_M^N.
The exact matrix between them is

\[
 K_M^{N:0}=(H_M^0)^{-1}H_M^N,\qquad
 (K_M^{N:0})^*H_M^0=H_M^0K_M^{N:0}=H_M^N.
\]

These equalities use the ordinary coordinate adjoint and follow by
direct multiplication of the two Hermitian matrices and their
inverses. They prove self-adjointness and strict positivity in the
H_M^0 inner product. For all p,q,
p*H_M^Nq=p*H_M^0 K_M^(N:0)q. No identity of the source-amplitude,
normal-image, or graph norms is assumed. The Euclidean inner product
is used to specify coefficient adjoints, and is not substituted for
one of these integral forms.

## 3. The integral adjoint, bounded inverse, and actual projection

For r in K, the jth coordinate of the proposed adjoint is the integral
pairing of r with the jth L2 column of N_M. Cauchy–Schwarz gives
absolute integrability and a bound by ||N_M e_j|| ||r||. There are
finitely many coordinates, so the displayed vector integral is also
well-defined and bounded. Pairing it with an arbitrary coordinate
vector verifies exactly

\[
 \mathbf N_M^*r=\int C_M(u)^*N_u^*r(u)\,du.
\]

Since H_M^N>0, L_M^N=(H_M^N)^(-1) N_M^* is a bounded map on all
of K and L_M^N N_M=I. Thus N_M is injective and L_M^N is its
inverse on the specified range R_M^N. The operator
Pi_M^N=N_M(H_M^N)^(-1)N_M^* is self-adjoint and satisfies
(Pi_M^N)^2=Pi_M^N by N_M^*N_M=H_M^N. Its range is R_M^N and
it fixes every vector there. This is the orthogonal projection for
the actual ambient K inner product. The range is finite-dimensional
and closed; no closure is substituted for a different algebraic image.

The ambient formula returns coefficients of the projected finite
normal image. The arithmetic observation below is asserted on that
actual finite image, as specified, rather than interpreted as point
evaluation of an arbitrary ambient measurable function.

## 4. Both graph components and their full metric

For r=N_M p, the reconstruction is exactly

\[
 \mathsf{Rec}_M r=(\mathbf T_Mp,\mathbf N_Mp)
       =(\mathbf T_M L_M^N r,r).
\]

Every member of the original graph has this form, and the inverse
is its second projection. Uniqueness follows from injectivity of N_M.
The two components are pointwise orthogonal because j_u* N_u=0.
Consequently the graph norm and its addition map retain

\[
 \|\mathsf{Rec}_M r\|^2
       =\|r\|^2+\|\mathbf T_M L_M^N r\|^2
       =(L_M^N r)^*H_M^\partial(L_M^N r).
\]

This equality is stated for r in R_M^N, where N_M L_M^N r=r;
it is not imposed on an unrelated ambient r. Graph addition is an
isometry for the sum of the two component norms because the components
are orthogonal. Reconstruction from the normal norm alone has the
additional displayed tangent term, so no unsupported isometry occurs.

## 5. Complete arithmetic derivative columns and their constants

For a nonempty full packet, v_h=g/h is nonzero at every selected
root after its complete order is canceled. Therefore U=product_i v_h(s_i)
has a full invertible Hermite class upsilon^(k) modulo
I=(h(s_1),...,h(s_k)). Its inverse in that finite algebra retains all
nilpotent coefficients. In particular beta_h is the exact full class
(upsilon^(k))^(-1) j_I(partial_S^rel U), with
partial_S^rel=(1/k)sum_i partial_(s_i).

From the original affine coordinates,

\[
 \partial_S^{\rm rel}S=1,\qquad
 \partial_S^{\rm rel}z_i=0.
\]

For the source column theta_alpha(z)S^n, differentiating the entire
product U theta_alpha S^n before taking its full jet therefore gives

\[
 n\upsilon^{(k)}[\theta_\alpha S^{n-1}]_I
       +\beta_h\upsilon^{(k)}[\theta_\alpha S^n]_I.
\]

There is no relative derivative term and no extra factor k multiplying
n. The factor 1/k stays in beta_h and in the defining complex
derivative. The n=0 term is explicitly zero, with no negative power.
The expression beta_h=(1/k)sum_i j_I(v_h'/v_h)(s_i) is only used
in the actual unit neighbourhoods of the finite packet, not as global
division across other zeros of v_h.

The real derivative of C_M has the factor i. Consistently, the source
unitary transform satisfies partial_u U_k=i U_k L_k on the actual
test domain. The arrow -i U_k^(-1) in FC.35 cancels exactly that i
after graph addition. Thus the final arithmetic columns use the complex
derivative above, with its original n and 1/k, and no missing i or
Plancherel factor. Both g=2xi and every derivative of its full local
unit remain in the columns.

It follows on the actual normal image that

\[
 \mathsf{Obs}_M^{\log}(r)
      =\mathsf J_M^{\log}(H_M^N)^{-1}\mathbf N_M^*r
\]

agrees exactly with reconstruction, graph addition, the inverse Mellin
unitary with its -i factor, logarithmic source multiplication, and the
original full arithmetic jet. The recovered source is an actual finite
tensor test function. Logarithmic multiplication preserves that test
space, so the penultimate arrow has its stated domain. No surjectivity
onto the whole packet algebra is claimed for this finite observation.

## 6. Gauge and zero-space scopes

For a specified smooth invertible relative frame C(u), the transported
coefficient matrix is C_M^C=C^(-1)C_M. The identity
(C^(-1))'=-C^(-1)C'C^(-1) cancels exactly against the additional
C^(-1)C' term in Gamma^C. Multiplication then gives both equations

\[
 N^C C_M^C=NC_M,\qquad
 j^C((C_M^C)'+\Gamma^C C_M^C)=j(C_M'+\Gamma C_M).
\]

The actual maps N_M and T_M are unchanged, hence so are H_M^N,
its inverse formula, both images, graph reconstruction and the arithmetic
observation. This argument transports the original admitted coefficient
image; it does not replace it with all functions in the new frame or
assume global growth bounds for C^(-1).

If the degree index set is empty, the finite source and its normal and
graph images are zero. The source-to-image maps and their inverses on
zero images are the unique zero-space maps; the ambient projection and
arithmetic observation have zero image. The nonempty positive matrix
argument is not needed in this case. If h=1, the packet target E is the
zero algebra and the arithmetic observation is the unique zero map;
the nonzero analytic source and its normal reconstruction remain as
already proved. Thus the analytic injectivity statement is not being
used to infer a nonzero arithmetic quotient for the empty packet.

The fixed-support linear lifts have their stated original source and
target modules. All maps preserve supported zero and external absence
according to the already defined lift, including a nonzero source
relation whose arithmetic class is supported zero and whose normal
image nevertheless retains its recoverable source data.

## Review changes and final scope

The initial draft at SHA256
`b86b987de6099f510e58e21a192c21b6e60e1cb6c46ea3af3ac743f052998911`
had three missing TeX escapes and called H_M^N “the actual source
metric,” which could conflate it with the original amplitude Gram.
The author corrected the escapes and added the exact two-form operator
FC.29a. The corrected subsection was then reread completely at the final
hash above. The arithmetic source path was also split across two display
rows without changing any map.

This final review certifies the written finite reconstruction and
observation proofs at the stated source hash. It asserts no uniform
inverse bound as the source degree grows, no arbitrary normal-section
arithmetic interpretation, and no new estimate for the finite Weil
defect. Layout rendering and cumulative publication are separate work.
