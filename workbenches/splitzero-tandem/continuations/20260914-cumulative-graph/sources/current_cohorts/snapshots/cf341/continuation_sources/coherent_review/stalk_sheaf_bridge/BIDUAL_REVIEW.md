# Exact derived bidual and its sign

Continue with the exact original R=O_{C,s}, z=t-s, omega=R dt, F=Frac(R), B=omegahat=C[[z]] dt and C_omega=B/omega. The companion REVIEW.md proves C_omega is a nonzero F-vector space and gives an explicit nonzero class [sum n! z^n dt]. The original nonzero germ g is unchanged.

## Acyclicity of the completed module

For every F-vector space K,

\[
\operatorname{Hom}_R(K,B)=0,\qquad
\operatorname{Ext}^j_R(K,B)=0\quad(j\ge1).
\tag{BD1}
\]

For K=F, apply the explicit telescope from REVIEW.md with B replacing omega. Its Hom differential is (Da)_n=a_n-z a_{n+1}. Its kernel is zero because intersection_n z^n B=0. It is surjective: for b=(b_n), the formal sum a_0=sum z^n b_n lies in B by completeness, and

\[
a_n=z^{-n}\left(a_0-\sum_{j=0}^{n-1}z^j b_j\right)\in B
\]

satisfies Da=b. Higher Ext vanishes because the telescope has length one. For arbitrary K, choose an F-basis, so K is a direct sum of copies of F. The direct sum of the free telescope resolutions is a free resolution of K; after Hom, the differential is a product of the surjective telescope differentials. Products of surjections of modules are surjective, and products of the zero kernels are zero. This proves (BD1) and also shows the result is independent of the chosen basis.

The module C_omega is injective over R. Indeed every nonzero element of R acts invertibly, so it is divisible. Every ideal of the discrete valuation ring R is principal; any map from an ideal (a) to C_omega extends to R by sending 1 to a^{-1} times the given image of a. This verifies the injective extension criterion for modules directly. The same argument makes F omega and F omega/omega injective: the latter is divisible because a lift of a quotient class can be divided by any nonzero a in F omega.

The long exact Ext sequence of

\[
0\to\omega\to B\xrightarrow{\pi}C_\omega\to0
\tag{BD2}
\]

therefore gives its positive Yoneda connecting isomorphism

\[
\delta_K:\operatorname{Hom}_F(K,C_\omega)
\xrightarrow{\sim}\operatorname{Ext}^1_R(K,\omega),
\tag{BD3}
\]

where delta_K(f) is the pullback of (BD2) along f. Hom_R(K,C_omega)=Hom_F(K,C_omega) because both are F-vector spaces and any R-linear map automatically commutes with inverses of nonzero scalars.

## The shifted target and the exact map

Use the cohomological shift convention (A[1])^n=A^{n+1}, with d_{A[1]}=-d_A. Define the unshifted complex T=(B --pi--> C_omega) in degrees 0,1 and define

\[
J=T[1]=(B\xrightarrow{-\pi}C_\omega)
\quad\text{in degrees }-1,0.
\tag{BD4}
\]

The map omega[1]->J is +inclusion omega->B in degree -1, and is a quasi-isomorphism. There is only one shift in (BD4).

For an F-vector space K placed in degree zero, ordinary Hom_R(K,J) has no term in degree -1 by (BD1), and its degree-zero term is

\[
W=\operatorname{Hom}_F(K,C_\omega).
\]

The terms B and C_omega are acyclic for Hom_R(K,-), by (BD1) and injectivity of C_omega. Hence this complex computes

\[
D(K):=R\operatorname{Hom}_R(K,\omega[1])\simeq W[0].
\tag{BD5}
\]

This identification is precisely the positive connecting identification (BD3), not its negative. One direct sign check uses an injective resolution omega->I^0 --d--> I^1 and a map b_0:B->I^0 extending omega->I^0. Its induced b_1:C_omega->I^1 satisfies d b_0=b_1 pi. The maps (b_0,b_1) define a chain map T->I with no negative component. After shifting, the differentials on both sides are negated, while the components remain (b_0,b_1). Thus f:K->C_omega represents the same positive class [b_1 f] in H^0 Hom(K,I[1])=Ext^1_R(K,omega).

Since W is also an F-vector space, exactly the same calculation gives

\[
D^2(K)\simeq\operatorname{Hom}_F(W,C_\omega)[0].
\tag{BD6}
\]

Under (BD5)-(BD6), the canonical derived bidual morphism is exactly

\[
\boxed{\eta_K:K\longrightarrow
\operatorname{Hom}_F\bigl(\operatorname{Hom}_F(K,C_\omega),C_\omega\bigr),
\qquad \eta_K(k)(f)=f(k).}
\tag{BD7}
\]

There is no minus sign. At the level of dg complexes, bidual evaluation is
\(\operatorname{ev}(x)(f)=(-1)^{|x||f|}f(x)\).
Here k and every f in Hom(K,J)=W[0] have degree zero, so that sign is +1. The negative differential -pi in (BD4) is already accounted for by the single target shift and introduces no further evaluation sign.

For completeness, the use of J rather than an everywhere injective complex does not change this canonical morphism. Choose a quasi-isomorphism q:J->I where I is an injective resolution of omega[1]. Such a two-term comparison can be constructed by extending the identity on omega to an R-linear map B->F omega, and passing to quotients; the target is the complex I with F omega in degree -1, F omega/omega in degree 0, and differential minus the quotient map. Both target modules are injective as proved above.

The maps

\[
\alpha=\operatorname{Hom}(K,q):W\to\operatorname{Hom}(K,I),\qquad
q_*:\operatorname{Hom}(W,J)\to\operatorname{Hom}(W,I)
\]

are quasi-isomorphisms by the established acyclicity for the F-vector spaces K and W. Since I is an injective target complex, precomposition with alpha also gives a quasi-isomorphism

\[
\alpha^*:\operatorname{Hom}(\operatorname{Hom}(K,I),I)
\longrightarrow\operatorname{Hom}(W,I).
\]

Naturality of dg evaluation gives the exact chain-map identity

\[
\alpha^*\operatorname{ev}_{I,K}=q_*\operatorname{ev}_{J,K}.
\tag{BD8}
\]

For k and f the two sides both evaluate to q(f(k)). Inverting the displayed quasi-isomorphisms in the derived category proves that the ordinary evaluation in (BD7) is the canonical derived bidual, not an arbitrarily chosen abstract isomorphism.

## Injectivity

Let 0!=k in K, and choose an F-linear functional lambda:K->F with lambda(k)=1 by extending k to a basis. Choose the explicit nonzero c=[sum n! z^n dt] in C_omega and define f(u)=lambda(u)c. Then

\[
\eta_K(k)(f)=f(k)=c\ne0.
\]

Thus eta_K is injective for every F-vector space K. This proves injectivity of the actual natural derived bidual map; no surjectivity or duality equivalence is asserted.

