# Origin-jet ladder from actual restricted theta relations

Companion to ORIGINAL_QUOTIENT_PROPAGATION.md. This calculation starts with explicit source test functions and propagates the original support-preserving quotient. It does not postulate an additional zero of the actual zeta function.

## 1. Actual source operators produce the relation ideals

Retain

\[
D=-x\partial_x,\qquad
\phi_*(x)=(4\pi^2x^4-6\pi x^2)e^{-\pi x^2},\qquad g(s)=2\xi(s).
\]

The existing source identity is M Theta phi_*=g. For every j>=0 define phi_j=D^j phi_*. Each belongs to the actual source V: it is even and Schwartz, has value zero at the real origin, and integration by parts gives integral D phi = integral phi = 0. Differentiating the theta sum and integrating the Mellin integral by parts gives

\[
\boxed{\mathcal M\Theta\phi_j(s)=s^jg(s).}
\tag{1}
\]

The identity first holds in an absolute-convergence half-plane and then extends by the source's entire continuation. All coefficients and signs are retained.

For 0<=m<=N put

\[
W_{m,N}=\operatorname{span}_{\mathbb C}\{\phi_m,\ldots,\phi_N\}.
\]

These are actual finite labels in the existing source diagram. Their image ideals are exactly

\[
\boxed{\mathcal I_{W_{m,N}}=(g(s)s^m).}
\tag{2}
\]

Containment follows from (1), and the generator at j=m gives equality. The ideal is independent of N once N>=m. For fixed N and 0<=m<N, the source inclusion W_{m+1,N} -> W_{m,N} gives the quotient map

\[
\mathcal D_{m+1}=\mathcal O/(gs^{m+1})\longrightarrow
\mathcal D_m=\mathcal O/(gs^m),\qquad[f]\mapsto[f].
\tag{3}
\]

Every finite segment of this inverse system therefore comes from actual source inclusions, not repeated bottom-support adjunction. The inputs are independent: writing phi_j=P_j exp(-pi x^2) gives P_{j+1}=2 pi x^2 P_j-x P_j', with nonzero leading term of degree 4+2(j+1).

## 2. The comparison kernel is exactly the origin jet

At m=0, D_0=O/(g) is the actual completed arithmetic divisor module. The exact sequence is

\[
\boxed{0\to\mathcal O/(s^m)\xrightarrow{k_m}\mathcal D_m
\longrightarrow\mathcal D_0\to0,\qquad k_m([a])=[ga].}
\tag{4}
\]

The kernel is (g)/(gs^m). Multiplication by the nonzero entire g identifies it with O/(s^m), retaining g in the actual map.

The same theta source computes g(0)=1. Let theta(x)=sum_{n!=0} exp(-pi n^2 x^2). Poisson gives theta(x)=x^{-1}-1 plus a term whose derivatives vanish faster than any power at zero. Also Theta phi_*=D(D-1)theta. Hence

\[
\mathcal M\Theta\phi_*(0)=-[(D-1)\theta]_0^\infty=1.
\]

The functional equation gives g(1)=1.

For m>=1, an explicit Chinese-remainder inverse is obtained by letting a_m(s) be the Taylor polynomial of 1/g at zero of degree less than m and putting

\[
b_m(s)=\frac{1-a_m(s)g(s)}{s^m}.
\]

This is entire and a_m g+b_m s^m=1. The inverse of D_m -> D_0 direct-sum O/(s^m) is

\[
([u],[v])\longmapsto[b_m s^m u+a_m g v].
\tag{5}
\]

For m=0, O/(s^0)=0 and the comparison is the identity D_0 -> D_0 direct-sum 0; no Taylor polynomial is needed. Thus the m-step origin module is an exactly computed kernel of the restricted-presentation comparison. It is not being described as an extra nontrivial zero of the unchanged xi function.

## 3. Apply the original split congruence at every stage

At any analytic stalk R use exactly

\[
x\sim_I^{\mathrm{sp}}y\iff(x=y=\tau)
\text{ or }(x,y\in R\text{ and }x-y\in I).
\]

The supported system is

\[
\boxed{G(R/(gs^{m+1}))\longrightarrow G(R/(gs^m))
\longrightarrow G(R/(g)).}
\tag{6}
\]

Every arrow fixes external absence. Its preimage over external absence contains only external absence. The preimage of the supported zero under the last arrow is the supported copy of (g)/(gs^m).

The class of g s^m is nonzero in the origin stalk at level m+1 and becomes the supported zero at level m. It never becomes tau.

Applying G to the actual Chinese-remainder map gives, stalkwise and then with sheafification,

\[
\boxed{G(\mathcal D_m)\cong
G(\mathcal D_0)\times_{\mathbb B}G(\mathcal O/(s^m)).}
\tag{7}
\]

The fibre product uses the same Boolean support character. It does not add a new external scalar zero for the origin factor.

## 4. The Fourier-compatible version retains both endpoints

On the even Schwartz source,

\[
\widehat{D\phi}=(1-D)\widehat\phi.
\]

Therefore Delta=D(1-D) commutes with Fourier transform. Since hat phi_*=phi_*, the tests psi_j=Delta^j phi_* are Fourier-fixed and satisfy

\[
\boxed{\mathcal M\Theta\psi_j(s)=[s(1-s)]^j g(s).}
\tag{8}
\]

For the source label spanned by psi_m,...,psi_N, the ideal is g[s(1-s)]^m. The comparison kernel is

\[
\boxed{\mathcal O/([s(1-s)]^m)
\cong\mathcal O/(s^m)\oplus\mathcal O/((1-s)^m),}
\tag{9}
\]

embedded into O/(g[s(1-s)]^m) by multiplication by the actual g. The endpoint ideals are comaximal and g is a unit at both endpoints. The full split decomposition is the common-support fibre product of these endpoint factors and the actual arithmetic divisor factor.

For the source involution f^dagger(s)=overline(f(1-bar s)), coordinates z_0=s and z_1=s-1 give the endpoint map

\[
\sum_j a_jz_1^j\longmapsto\sum_j(-1)^j\bar a_jz_0^j.
\tag{10}
\]

The factor s(1-s) has not been replaced by s(s-1); such a replacement would introduce (-1)^m into (8).

This calculates the one-endpoint ladder and its symmetry-preserving two-endpoint counterpart inside the actual source test space. It does not equate a jet order with a Krull dimension or supply a spectral positivity bound. Omitted lower source relations produce a supported origin-jet module; reintroducing those relations removes it by the specified quotient map without erasing the common support.

## Source and check boundary

The source theta multiplier and phi_* are read from ACTUAL_ADELIC_COMPARISON.md at blob c23656c2a43e0041d6f7aeb0b80d6e12a6b468d9. The original quotient is the congruence of the globalization note and the general quotient theorem in ORIGINAL_QUOTIENT_PROPAGATION.md. The recursive Gaussian calculation, exact sequence, and explicit CRT maps above are derived in this continuation.

The local companion checker executes 101 exact symbolic comparisons: the Gaussian Mellin-polynomial recursions, the involution, and universal polynomial CRT identities. The polynomial CRT test examples are not claimed to be the Riemann xi function. The general analytic claims are proved above. No RH claim, independent novelty assessment or automatic merge is made.
