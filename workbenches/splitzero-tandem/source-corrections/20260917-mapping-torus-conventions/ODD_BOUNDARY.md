# Mapping-torus odd boundary with the historical suspension convention

This completes the two boundary calculations for explicit maps. The companion DOWNSTREAM_USE_RECONCILIATION.md checks the identified direct uses. The sealed companion and the accepted mathematical bundle remain unchanged.

## Exact historical source

The local first edition of Bruce Blackadar, *K-Theory for Operator Algebras* (1986), is the exact catalogue file: 10,413,048 bytes, 346 PDF pages, SHA256 `dedcbf9363bd8ed23b2767f93c7e6e64b5c6011b3443a3bd25bbcbbd65e73b0b`. The inherited source ID is `LITSRC-20260830-0062`; statement ID `LITSTMT-20260830-0155`. Its DOI is <https://doi.org/10.1007/978-1-4613-9572-0>.

Primary pages inspected: Theorem 8.2.2 and its proof, printed 68–70 (PDF 76–78); Definition 8.3.1, printed 70 (PDF 78);8.3.2, printed 71 (PDF 79); positive Bott Definition 9.1.1, printed 72–73 (PDF 80–81); exponential9.3.2, printed 77 (PDF 85); mapping-torus Definition 10.3.1, printed 85 (PDF 93); Proposition 10.4.1, printed 87 (PDF 95). The historical and author-hosted later editions have matching conventions at these items, despite different pagination. No protected book pages are included in a public deliverable.

Write theta_A:K1(A)->K0(SA) for the exact isomorphism of Theorem 8.2.2: a unitary path Z from1 to diag(u,u*) gives theta_A([u])=[Z E Z*]-[E], where E=diag(I_n,0_n). Scalar parts of u and Z are1. The index boundary of Definition 8.3.1 has the same positive projection-difference order.

## A fully explicit suspension path

For any contraction a in M_n(A^+), set

    D_a=(I-a*a)^(1/2),  D_a_star=(I-aa*)^(1/2),
    V(a) = [[a, -D_a_star], [D_a, a*]],
    Q(a) = V(a) E V(a)*
         = [[aa*, a D_a], [D_a a*, I-a*a]].

The identity a D_a=D_a_star a follows first for polynomials in a*a and aa* by a(a*a)^k=(aa*)^k a, and then for the square root by uniform polynomial approximation on[0,1]. Thus multiplication of the displayed blocks gives V(a)V(a)*=V(a)*V(a)=I. In particular Q(a) is an orthogonal projection. The square-root functional calculus and these operations are norm continuous. For a unitary u, V(u)=diag(u,u*) and Q(u)=E.

For0<=r<=1 set c=(1-r^2)^(1/2) and

    W(r)=V(r I)=[[r I,-c I],[c I,r I]],
    Z_u(r)=W(r)* V(r u),
    F_u(r)=Z_u(r) E Z_u(r)*.

All these matrices are explicit unitaries or projections as indicated. Since u has scalar image I, Z_u has scalar image I. At r=0, V(0)=W(0), hence Z_u(0)=I. At r=1, W(1)=I and Z_u(1)=diag(u,u*). Therefore F_u is a based projection loop with constant scalar image E, and the historical definition gives

    theta_A([u])=[F_u]-[E].

This pins the suspension coordinate without an unrecorded sign choice.

## The exact odd boundary

Retain SA=C_0((0,1),A), M_alpha={f:f(1)=alpha(f(0))}, the increasing-coordinate zero-endpoint inclusion and quotient pi=ev0. For u in U_n(A^+) with scalar image I, put v=alpha(u) and a(t)=(1-t)u+t v. It is a contraction by the triangle inequality. V(a(t)) lies in the matrix unitization of M_alpha: its endpoints are diag(u,u*) and diag(v,v*)=alpha(diag(u,u*)), and its scalar part is I. Consequently Definition 8.3.1 gives

    delta_1([u])=[Q(a)]-[E] in K0(SA).

No partial-isometry lifting hypothesis is used.

Define the broken contraction path

    b(t)=(1-2t)u               for0<=t<=1/2,
    b(t)=(2t-1)v               for1/2<=t<=1,

and r(t)=|2t-1|. The two formulas meet at0. Let a_s(t)=(1-s)a(t)+s b(t), and r_s(t)=1-s+s r(t), for0<=s<=1. Each a_s is a contraction, its scalar image is r_s I, and its endpoints remain u,v. Define

    P_s(t)=W(r_s(t))* Q(a_s(t)) W(r_s(t)).

This is a norm-continuous homotopy of projections. Its scalar image is E because Q(r_s I)=W(r_s) E W(r_s)*. Its endpoint values are E since r_s(0)=r_s(1)=1 and u,v are unitary. Hence it is a homotopy in the projection matrices over(SA)^+, with fixed scalar projection. At s=0, W(1)=I and P_0=Q(a). At s=1,

    P_1(t)=F_u(1-2t)          for0<=t<=1/2,
    P_1(t)=F_v(2t-1)          for1/2<=t<=1.

This is the reversed F_u followed by F_v.

For completeness its K0 class can be identified directly from unitary transport. Write D_u=diag(u,u*). A unitary transport of P_1 starting at I is

    T(t)=Z_u(1-2t) D_u*       for0<=t<=1/2,
    T(t)=Z_v(2t-1) D_u*       for1/2<=t<=1.

The values agree at1/2, and D_u commutes with E, so T E T*=P_1. Its endpoint is

    T(1)=diag(vu*,v*u).

After stabilization the lower block v*u can be connected to uv* explicitly. For arbitrary unitaries x,y, let R(theta) be the scalar2x2 block rotation with entries cos(theta)I,-sin(theta)I,sin(theta)I,cos(theta)I. The path

    diag(x,I) R(theta) diag(y,I) R(theta)*,
       0<=theta<=pi/2,

joins diag(xy,I) to diag(x,y). Conjugating diag(x,y) by R(theta) joins it to diag(y,x); reversing the first construction with y,x joins that to diag(yx,I). With x=v*,y=u, this gives the required path from diag(v*u,I) to diag(uv*,I).

Stabilize the top block by I as well, and append this lower-block path to T while holding the top block diag(vu*,I) fixed. This appended segment commutes with the stabilized E, so the projection remains constant there. The endpoint is now diag(w,w*) with w=diag(vu*,I). The source's definition of theta therefore identifies the same projection-loop class as theta_A([vu*]). Since Proposition 8.1.3 identifies multiplication and addition in K1,

    delta_1([u])=theta_A([v]-[u])
               =theta_A((alpha_*-id)[u]).

Unitary classes generate K1(A); thus the exact odd-boundary identity is

    theta_A^(-1) o delta_1 = alpha_*-id.

Together with `CONVENTION_CHECK.md`, both boundaries have alpha_*-id under the stated forward maps, the source's positive Bott map beta, and the source's suspension map theta.

## Time reversal and the kernel/cokernel consequence

For projection loops, time reversal changes theta_A to its negative. Indeed the reversed F_u has transport Z_u(1-t)D_u*, starting at I and ending at D_u*=diag(u*,u); Theorem 8.2.2 identifies its class with theta_A([u*])=-theta_A([u]). The exact same time-reversal *-isomorphism rho used in `CONVENTION_CHECK.md` therefore gives

    theta_A^(-1) o delta_1,rev = id-alpha_*.

Let G be either K-group and T=alpha_*-id. Then ker(T)=ker(-T) as subsets: Tx=0 iff -Tx=0. Also im(T)=im(-T), because -Tx=T(-x) and Tx=(-T)(-x). Accordingly the identity of G descends to the identity isomorphism between the two cokernel presentations. This proves that the sign correction alone leaves the abstract kernel/cokernel groups unchanged. It does not determine signs in additional chosen coordinate maps or in another extension's connecting morphism. Those exact use maps must be compared separately.

## Audit conclusion

The two boundary calculations are now proved with explicit homotopies and the exact historical source convention, rather than left as an undecided universal sign. The historical catalogue combined a forward endpoint definition/evaluation0 with a reversed affine lift. Correct that record by stating the maps above and preserving the original record as history. Before modifying other mathematical files, identify where their suspension inclusion, evaluation, or profinite coordinate map uses a different orientation. The proof establishes no failure of the abstract Pimsner–Voiculescu sequence and changes no accepted zeta continuation claim.
