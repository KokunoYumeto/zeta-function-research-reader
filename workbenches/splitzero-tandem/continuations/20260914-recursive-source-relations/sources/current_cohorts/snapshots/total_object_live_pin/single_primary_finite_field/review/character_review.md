# Independent review: single-primary characters, Frobenius conventions, and inertia

Date: 2026-09-13.

Assigned scope, verbatim:

> Independent bounded review of finite-field single-primary formula. h=(s−rho)^m, n=m+1≥2, char p>n, Phi=((s−rho)^n−(−rho)^n)/n=(y^n/n)+c, c=−(−rho)^n/n. Let F=R1 pi! Lpsi(Phi/u) on Gm_u, k=F_Q after extension n|Q−1. Define Kchi trace chi(x), Gauss G=sum z≠0 chi(z)psi(z). Claimed exact decomposition F=Lpsi(c/u)⊗⊕_{chi^n=1,chi≠1} A_{−G(chi,psi)}⊗K_{chi^-1}(a), a=1/(nu), equivalently A_{−chi(n)G}⊗Kchi(u). Need independently prove inertia at0 V^I=0 for c=0 and c≠0; explicit finite cover kills inertia so N=0, retaining AS c/u; check signs and field extension trace/norm conventions. Use primarysource web verification if needed. Write review under work/rh_counterfactual_20260913/total_object/single_primary_finite_field/review/character_review.md. I am writing full sheaf proof locally; you independently review conventions and local Artin-Schreier cover/ramification only.

The parent maintains the complete user transcript and cumulative program log. This file records the bounded independent calculations and their provenance.

## 1. Objects and conventions

Let \(k=\mathbf F_Q\), \(Q=p^f\), let \(n=m+1\geq2\), assume \(p>n\) and \(n\mid Q-1\), and let \(\rho\in k\). The coordinate is \(y=s-\rho\); the phase, including its constant, is
\[
\Phi(s)=\frac{(s-\rho)^n-(-\rho)^n}{n}
       =\frac{y^n}{n}+c,\qquad
c=-\frac{(-\rho)^n}{n}.
\]
In particular \(c=0\) if and only if \(\rho=0\). This follows because \(n\) is invertible in the field \(k\), and a field has no nonzero nilpotents. We retain \(c\) throughout.

Fix \(\ell\ne p\), a coefficient field \(E\subset\overline{\mathbf Q}_\ell\) containing the character values, and a nontrivial additive character \(\psi:k\to E^\times\). Every Frobenius in the formulas below is geometric Frobenius. Write \(\mathcal A_\alpha\) for a geometrically constant rank-one sheaf whose geometric Frobenius eigenvalue over \(k\) is \(\alpha\). Define \(\mathcal K_\chi\) by the trace convention
\[
\operatorname{Tr}(\operatorname{Frob}_{x,k_r}\mid\mathcal K_\chi)
=\chi_r(x),\qquad
\chi_r=\chi\circ N_{k_r/k},\qquad k_r=\mathbf F_{Q^r}.
\]
Define the Artin–Schreier trace convention by
\[
\operatorname{Tr}(\operatorname{Frob}_{x,k_r}\mid\mathcal L_\psi(f))
=\psi_r(f(x)),\qquad
\psi_r=\psi\circ\operatorname{Tr}_{k_r/k}.
\]
These conventions fix any possible inverse ambiguity in an associated-torsor description.

Put
\[
G(\chi,\psi)=\sum_{z\in k^\times}\chi(z)\psi(z),\qquad
a=\frac1{nu}.
\]
The morphism \(\pi:\mathbf A^1_y\times\mathbf G_{m,u}\to\mathbf G_{m,u}\) is projection, and the object under review is
\[
\mathcal F=R^1\pi_!\mathcal L_\psi(ay^n+c/u).
\]

## 2. The elementary character calculation fixes both signs and inverses

For \(a\in k^\times\), let
\[
S(a)=\sum_{y\in k}\psi(ay^n).
\]
The group \(k^\times\) is cyclic and \(n\mid Q-1\). Consequently the number of solutions \(y\in k^\times\) to \(y^n=x\) is
\[
\sum_{\chi^n=1}\chi(x).
\]
Indeed, when \(x\) is an \(n\)-th power all \(n\) characters in the sum take the value \(1\); otherwise the sum of the resulting nontrivial character on the cyclic quotient \(k^\times/(k^\times)^n\) is zero. Thus
\[
\begin{aligned}
S(a)
&=1+\sum_{\chi^n=1}\sum_{x\in k^\times}\chi(x)\psi(ax)\\
&=1+\sum_{x\in k^\times}\psi(ax)
 +\sum_{\substack{\chi^n=1\\\chi\ne1}}
   \sum_{x\in k^\times}\chi(x)\psi(ax)\\
&=\sum_{\substack{\chi^n=1\\\chi\ne1}}
  \chi(a^{-1})G(\chi,\psi).
\end{aligned}
\]
Here the first two terms cancel because a nontrivial additive character sums to zero on \(k\), and substitution \(z=ax\) gives
\(\chi(x)=\chi(a^{-1})\chi(z)\).
There is no inverse on \(\chi\) inside \(G\).

For the compactly supported cohomology in degree one, the Lefschetz sign is minus. The resulting trace is therefore
\[
\operatorname{Tr}(\operatorname{Frob}_{u,k}\mid\mathcal F)
=-\psi(c/u)\sum_{\substack{\chi^n=1\\\chi\ne1}}
\chi(a^{-1})G(\chi,\psi).
\]
The proposed factors \(\mathcal A_{-G(\chi,\psi)}\) and
\(\mathcal K_{\chi^{-1}}(a)\) give precisely this trace.

The equivalent expression in the \(u\)-coordinate retains the constant \(n\):
\[
\mathcal K_{\chi^{-1}}\!\left(\frac1{nu}\right)
\simeq
\mathcal A_{\chi(n)}\otimes\mathcal K_\chi(u).
\]
This is an isomorphism of the rank-one character sheaves: inversion changes
\(\chi^{-1}\) to \(\chi\), and multiplicativity of the character sheaf splits
\(\mathcal K_\chi(nu)\) into the constant fiber at \(n\) and
\(\mathcal K_\chi(u)\). In particular the constant Frobenius eigenvalue is
\(-\chi(n)G(\chi,\psi)\), not \(-\chi(n)^{-1}G(\chi,\psi)\).

An actual sheaf decomposition can be obtained without invoking equality of
traces as a substitute for an isomorphism. Under \(y\mapsto x=y^n\), the finite
pushforward decomposes by the idempotents of \(\mu_n\). Its trivial summand
extends across \(x=0\) as the constant sheaf, while the nontrivial summands
are the extensions by zero of \(\mathcal K_\chi(x)\). On each nontrivial
summand the base change \(z=ax\) gives the exact pullback identity
\[
\mathcal K_\chi(x)\otimes\mathcal L_\psi(ax)
\simeq
\mathcal K_{\chi^{-1}}(a)\otimes
\mathcal K_\chi(z)\otimes\mathcal L_\psi(z).
\]
The constant degree-one cohomology factor is
\(H_c^1(\mathbf G_{m,\bar k},\mathcal K_\chi(z)\otimes\mathcal L_\psi(z))\);
its Frobenius is \(-G(\chi,\psi)\). The parent's sheaf argument establishes
the dimension and the vanishing of the other degrees. The local calculations
below concern the exact displayed rank-one factors, so do not depend on a
semisimplification or an inference from a single trace.

## 3. Every extension uses norm and trace; the sign is stable

For \(r\geq1\), write
\[
G_r=G(\chi_r,\psi_r)
=\sum_{z\in k_r^\times}
\chi(N_{k_r/k}z)\psi(\operatorname{Tr}_{k_r/k}z).
\]
The exact identity is
\[
G_r=(-1)^{r-1}G(\chi,\psi)^r,\qquad
-G_r=(-G(\chi,\psi))^r.
\]
Here is an elementary proof including the sign. For a monic polynomial
\[
P(X)=X^d+a_1X^{d-1}+\cdots+a_d,\qquad a_d\ne0,
\]
define
\[
\lambda(P)=\chi((-1)^d a_d)\psi(-a_1),\qquad\lambda(1)=1.
\]
The product of its roots is \((-1)^d a_d\) and the sum is \(-a_1\), both
counted with multiplicity. Hence \(\lambda(P_1P_2)=\lambda(P_1)\lambda(P_2)\).
Unique factorization gives the formal power-series identity
\[
L(T):=\sum_{\substack{P\ {\rm monic}\\P(0)\ne0}}
\lambda(P)T^{\deg P}
=\prod_{\substack{P\ {\rm monic\ irreducible}\\P\ne X}}
(1-\lambda(P)T^{\deg P})^{-1}.
\]
If \(P\) has degree \(d\) and a root \(\alpha\in k_d\), then
\[
\lambda(P)=
\chi(N_{k_d/k}\alpha)\psi(\operatorname{Tr}_{k_d/k}\alpha).
\]
In \(k_r\) with \(d\mid r\), the contribution of each of the \(d\) roots is
\(\lambda(P)^{r/d}\). Expanding the logarithm of the Euler product therefore
gives
\[
\log L(T)=\sum_{r\geq1}G_r\frac{T^r}{r}.
\]
The coefficient of \(T\) in the polynomial sum is
\[
\sum_{a_1\ne0}\chi(-a_1)\psi(-a_1)=G(\chi,\psi).
\]
For \(d\geq2\), the coefficients \(a_1\in k\) and \(a_d\in k^\times\)
vary independently. Summing first over \(a_1\) gives zero. Thus
\[
L(T)=1+G(\chi,\psi)T
\]
and comparison with
\[
\log(1+GT)=\sum_{r\geq1}(-1)^{r-1}G^r\frac{T^r}{r}
\]
proves the identity.

Since \(\chi_r(n)=\chi(n)^r\), the constant eigenvalue over \(k_r\) is
\[
(-\chi(n)G(\chi,\psi))^r=-\chi_r(n)G(\chi_r,\psi_r).
\]
The norm is surjective, so lifting the \(n\) characters of order dividing
\(n\) gives all \(n\) such characters over \(k_r\). Thus the original
character calculation and the decomposition agree over every \(k_r\).

This sign is also stated in Katz, *G2 and Hypergeometric Sheaves*, printed
page 36, as the lifting identity for \((-g)^{[L:E]}\), with norm-compatible
characters on the preceding page:
[Katz, pp. 35–36](https://web.math.princeton.edu/~nmk/g2hyper62finalcorr.pdf).
The proof above is supplied independently, so no lifting assertion is left
unproved in this review.

For completeness, the absolute value of each Gauss factor follows directly.
After any complex embedding of its cyclotomic field, character values have
absolute value one. For nontrivial \(\chi\),
\[
\begin{aligned}
|G(\chi,\psi)|^2
&=\sum_{x,y\in k^\times}\chi(x/y)\psi(x-y)\\
&=\sum_{t\in k^\times}\chi(t)
  \sum_{y\in k^\times}\psi((t-1)y)\\
&=(Q-1)-\sum_{\substack{t\in k^\times\\t\ne1}}\chi(t)
=Q.
\end{aligned}
\]
The last equality uses \(\sum_{t\in k^\times}\chi(t)=0\).
Consequently the constants \(-\chi(n)G(\chi,\psi)\) have absolute value
\(Q^{1/2}\), with neither \(n\) nor \(c\) discarded.

## 4. The exact Artin–Schreier cover

Choose a nontrivial character \(\psi_0:\mathbf F_p\to E^\times\).
There is a unique \(b\in k^\times\) such that
\[
\psi(x)=\psi_0(\operatorname{Tr}_{k/\mathbf F_p}(b x)).
\]
To see existence and uniqueness, the trace pairing
\((b,x)\mapsto\operatorname{Tr}_{k/\mathbf F_p}(b x)\) is nondegenerate:
the trace map is a nonzero \(\mathbf F_p\)-linear map because the polynomial
\(X+X^p+\cdots+X^{p^{f-1}}\), whose degree is less than \(Q\), cannot vanish
on all of \(k\); multiplying by any nonzero \(b\) is a bijection of \(k\).
Therefore \(b\mapsto\operatorname{Tr}(b\,\cdot)\) is an injective map
between vector spaces of equal dimension \(f\), hence a bijection.
All additive characters arise by composing such a functional with
\(\psi_0\). Nontriviality forces \(b\ne0\).

Work over the geometric complete local field
\[
K=\bar k((u)).
\]
The Artin–Schreier factor \(\mathcal L_\psi(c/u)\) is trivialized by
\[
z^p-z=\frac{bc}{u}.
\]
The choice of associated character, or its inverse, is determined by the
trace convention in Section 1; either has the same kernel and the same
ramification. The equation here therefore fixes the actual trivializing
cover without imposing an incompatible torsor convention.

For \(c\ne0\), this equation has no solution in \(K\). If
\(w\in K\) has a pole of order \(d>0\), then \(w^p-w\) has pole order
\(pd\), because its most negative valuation occurs in \(w^p\) and cannot
cancel against \(w\). If \(w\) has no pole, neither does \(w^p-w\).
The right-hand side \(bc/u\) has pole order one, so both possibilities
exclude a solution.

Its splitting field has degree exactly \(p\): adjoining a root adjoins all
roots \(z+j\), \(j\in\mathbf F_p\); the polynomial is separable since its
derivative is \(-1\). Its Galois group embeds into the additive group
\(\mathbf F_p\) by \(\sigma\mapsto\sigma(z)-z\), and hence has order \(1\)
or \(p\). The absence of a root in \(K\) excludes order \(1\). This is the
elementary Artin–Schreier construction also recorded by the
[Stacks Project, Tag 09I7](https://stacks.math.columbia.edu/tag/09I7).

Let \(M_0=K(z)\) and let \(v_{M_0}\) be its normalized valuation. If its
ramification index is \(e\), the equation implies \(v_{M_0}(z)<0\) and
\[
p\,v_{M_0}(z)=-e.
\]
Thus \(p\mid e\). Since \(e\leq[M_0:K]=p\), it follows that
\(e=p\) and \(v_{M_0}(z)=-1\): the extension is totally ramified.
The uniformizer \(\varpi=z^{-1}\) satisfies, for \(j\ne0\),
\[
\sigma_j(\varpi)-\varpi
=\frac1{z+j}-\frac1z
=-\frac{j}{z(z+j)},\qquad
v_{M_0}(\sigma_j(\varpi)-\varpi)=2.
\]
By the definition
\(G_i=\{\sigma:v(\sigma(\varpi)-\varpi)\geq i+1\}\), the lower
ramification groups are \(G_0=G_1=\mathbf F_p\) and \(G_2=1\).
A nontrivial character therefore has Swan conductor one.

## 5. The combined finite cover and its ramification, with \(c\) retained

The single cover
\[
u=t^n,\qquad z^p-z=\frac{bc}{t^n}
\tag{COV}
\]
trivializes all geometric inertia factors simultaneously.

First, every \(\mathcal K_\chi(u)\), \(\chi^n=1\), pulls back to the
trivial Kummer sheaf, since
\(\mathcal K_\chi(t^n)=\mathcal K_{\chi^n}(t)=\mathcal K_1(t)\).
Second, the Artin–Schreier factor pulls back to the factor defined by
\(bc/t^n=z^p-z\), so its pullback is trivial on the displayed torsor.
The geometrically constant Gauss factors need no extension of local
geometric inertia. Arithmetic Frobenius on those factors has not been
removed by this observation.

For \(c=0\), the Kummer extension \(\bar k((t))/K\) suffices. It has
degree \(n\), is totally and tamely ramified, and has Galois group
\(\mu_n\). Indeed \(t^n-u\) is Eisenstein, and its \(n\) roots are
\(\zeta t\), \(\zeta\in\mu_n\subset\bar k\); \(n\) is prime to \(p\).

For \(c\ne0\), the equation after Kummer pullback still has no solution:
its pole order is \(n\), and \(p\nmid n\). The same pole-order proof as
above applies. The field
\[
M=\bar k((t))(z),\qquad z^p-z=bc/t^n,
\]
has degree \(np\) over \(K\). It is Galois, with commuting automorphisms
\[
(\zeta,j):(t,z)\longmapsto(\zeta t,z+j),
\qquad (\zeta,j)\in\mu_n\times\mathbf F_p.
\]
These \(np\) distinct automorphisms exhaust its degree. The group is
therefore exactly \(\mu_n\times\mathbf F_p\).

The ramification index of \(M/\bar k((t))\) is \(p\). If it were \(e\),
the valuation equation would give \(p\,v_M(z)=-ne\); \(p\nmid n\) forces
\(p\mid e\), and \(e\leq p\). With normalized valuation on \(M\),
\[
v_M(t)=p,\qquad v_M(z)=-n.
\]
Choose the unique integer \(d\in\{1,\ldots,p-1\}\) with
\(-nd\equiv1\pmod p\), and put \(a_0=(1+nd)/p\). Then
\[
\varpi=t^{a_0}z^d,\qquad v_M(\varpi)=a_0p-nd=1
\]
is a uniformizer. For \(j\ne0\),
\[
\sigma_j(\varpi)-\varpi
=t^{a_0}\bigl((z+j)^d-z^d\bigr).
\]
Since \(1\leq d<p\), the term \(d j z^{d-1}\) has nonzero coefficient.
It has strictly smaller valuation than all the lower powers of \(z\).
Consequently
\[
v_M(\sigma_j(\varpi)-\varpi)
=a_0p-(d-1)n=n+1.
\]
For a general \((\zeta,j)\) with \(\zeta\ne1\), the coefficient of \(z^d\)
in \(\zeta^{a_0}(z+j)^d-z^d\) is \(\zeta^{a_0}-1\).
The relation \(a_0p-nd=1\) gives \(\gcd(a_0,n)=1\), so this coefficient
is nonzero. Its valuation is exactly \(1\) after multiplying by
\(t^{a_0}\), and every other term has larger valuation. Thus
\[
G_0=\mu_n\times\mathbf F_p,\qquad
G_i=\mathbf F_p\ (1\leq i\leq n),\qquad
G_{n+1}=1.
\]
These are the full lower ramification groups of (COV). In particular the
original Artin–Schreier factor has upper break one over \(K\); the
degree-\(n\) tame pullback has lower and upper break \(n\).

## 6. Invariants, Swan conductor, and the nilpotent operator

Let \(V=\mathcal F_{\bar\eta}\), of dimension \(n-1\), and let \(I\) be
the geometric inertia group at \(u=0\).

If \(c=0\), the decomposition restricts to the direct sum of every
nontrivial character of the quotient \(\mu_n\). Each character has zero
fixed space: for a nontrivial character \(\theta\), select \(g\) with
\(\theta(g)\ne1\), and an invariant vector \(v\) would satisfy
\((\theta(g)-1)v=0\), hence \(v=0\). Taking the direct sum gives
\[
V^I=0,\qquad\operatorname{Swan}_0(V)=0.
\]
The full list includes a character of exact order \(n\), so the tame
inertia image has order \(n\).

If \(c\ne0\), wild inertia acts on every summand through the same
nontrivial rank-one Artin–Schreier character. The faithful nontrivial
character of \(\mathbf F_p\) has no fixed vector by the preceding scalar
argument. Kummer factors are trivial on wild inertia. Therefore
\[
V^{P}=0,\qquad V^I=0,
\]
where \(P\subset I\) denotes wild inertia.

The Swan conductor follows directly from the computed lower groups:
\[
\begin{aligned}
\operatorname{Swan}_0(V)
&=\sum_{i\geq1}\frac{|G_i|}{|G_0|}
  \operatorname{codim}V^{G_i}\\
&=\sum_{i=1}^{n}\frac{p}{np}(n-1)=n-1.
\end{aligned}
\]
Thus the Artin conductors are \(n-1\) when \(c=0\) and \(2(n-1)\) when
\(c\ne0\), using \(a(V)=\operatorname{Swan}(V)+\dim V-\dim V^I\).

The inertia image when \(c\ne0\) is the full finite group of order \(np\).
To check faithfulness, if \((\zeta,j)\) acts trivially on every summand,
the tame scalar in any summand (of order dividing \(n\)) is the inverse
of the wild scalar (of order dividing \(p\)). Coprimality forces both
scalars to equal \(1\). A primitive Kummer character then gives
\(\zeta=1\), and faithfulness of the nontrivial additive character gives
\(j=0\).

In both cases the finite cover explicitly makes the geometric inertia
action trivial, so the nilpotent monodromy operator is
\[
N=0.
\]
One can also see this without a logarithm convention: a finite-order
matrix over a characteristic-zero coefficient field is semisimple,
because its minimal polynomial divides the separable polynomial
\(X^r-1\). Its unipotent part is therefore the identity, whose nilpotent
logarithm is zero.

The exact statements are consequently
\[
\boxed{
\dim V=n-1,\quad V^I=0,\quad N=0,\quad
\operatorname{Swan}_0(V)=
\begin{cases}
0,&c=0,\\
n-1,&c\ne0.
\end{cases}}
\]
The assertions \(N=0\) and \(V^I=0\) are compatible. The first concerns
the unipotent factor after finite inertia is accounted for; the second
concerns the nontrivial finite characters before passing to a cover.
For \(j:\mathbf G_m\hookrightarrow\mathbf A^1\), the ordinary invariant
stalk \((j_*\mathcal F)_{\bar0}=V^I\) is zero. The geometric generic fiber
still has dimension \(n-1\), and becomes an unramified representation
after (COV). Therefore zero invariant stalk is not a calculation that
the entire generic fiber is zero.

## 7. Review result and exact integration cautions

The displayed decomposition has the correct minus sign, inverse
character, factor \(\chi(n)\), and field-extension convention. The local
invariant and nilpotent claims are correct with the original constant
\(c=-(-\rho)^n/n\) retained. The equations in Sections 4–6 prove them
directly, including the cover and its entire lower ramification
filtration.

For integration, keep the following precise choices explicit:

1. Every stated Frobenius eigenvalue uses geometric Frobenius.
2. Extend multiplicative characters by norm and additive characters by trace.
3. Keep the minus sign because the cohomology is \(R^1\pi_!\).
4. Keep \(\mathcal L_\psi(c/u)\); the \(c=0\) and \(c\ne0\) cases have
   different wild ramification and conductors.
5. Claim \(N=0\) together with finite nontrivial inertia, not with
   trivial inertia on the original base.
6. Prove the sheaf decomposition by the finite power-map idempotents and
   the coordinate isomorphism, as above and in the parent's full proof;
   traces alone would establish less.

No assertion about existence or nonexistence of a Riemann zeta zero is
made by this local calculation.

## 8. Cross-check of the parent's SPF.1–29 source

The complete source
../single_primary_finite_field.tex was read after the preceding independent
calculation was written. Its initial field is \(k_0=\mathbf F_{Q_0}\);
its split field is \(k=\mathbf F_{Q_0^d}\), where
\(d=\operatorname{ord}_{(\mathbf Z/n\mathbf Z)^\times}(Q_0)\).
Since \(p>n\), the residue class of \(Q_0\) is a unit modulo \(n\),
so this order exists and \(n\mid Q_0^d-1\). Its additive character
\(\psi_0\circ\operatorname{Tr}_{k/k_0}\) is nontrivial: the trace map
is surjective because it is a nonzero \(k_0\)-linear functional, as
proved by the trace-polynomial argument in Section 4 with \(Q_0\)
in place of \(p\). Composition of a surjection with a nontrivial
character cannot be trivial. Transitivity of field trace gives the
same character over each further extension. These choices agree
exactly with Sections 1–3.

The explicit projector in SPF.10 is
\[
e_\chi=\frac1n\sum_{\zeta\in\mu_n(k)}
\lambda_\chi(\zeta)D_\zeta,\qquad D_\zeta e_w=e_{\zeta w},
\qquad
\lambda_\chi(x^{(Q-1)/n})=\chi(x).
\]
Direct reindexing gives
\[
D_\eta e_\chi
=\frac1n\sum_{\zeta}\lambda_\chi(\zeta)D_{\eta\zeta}
=\lambda_\chi(\eta)^{-1}e_\chi.
\]
For a point \(x\in k_r^\times\) and \(w^n=x\), arithmetic Frobenius
sends \(w\) to
\[
w^{Q^r}=x^{(Q^r-1)/n}w.
\]
Because \(\mu_n\subset k\), geometric Frobenius acts by the inverse
deck transformation. Its action on the projector image is
\[
\lambda_\chi(x^{(Q^r-1)/n})
=\lambda_\chi((N_{k_r/k}x)^{(Q-1)/n})
=\chi(N_{k_r/k}x)=\chi_r(x).
\]
Thus the positive coefficient \(\lambda_\chi(\zeta)\) in the
projector, its inverse deck eigencharacter, and geometric Frobenius
give precisely the claimed convention. Replacing the coefficient
by its inverse without changing the other conventions would
reverse the Kummer trace character.

The original unit has a precise transport at the primary algebra
level. With the parent's specified ring map \(\alpha:R\to k_0\),
the maps of algebras are
\[
\begin{aligned}
R[s]/((s-\rho)^m)&\longrightarrow R[y]/(y^m),
&[f(s)]&\longmapsto[f(y+\rho)],\\
R[y]/(y^m)&\longrightarrow R[s]/((s-\rho)^m),
&[P(y)]&\longmapsto[P(s-\rho)].
\end{aligned}
\]
The first sends the defining relation to \(y^m\), the second sends
\(y^m\) to the defining relation, and the two substitutions are
mutual inverses. They therefore preserve the entire length-\(m\)
algebra. Coefficient specialization extends these maps by
\[
\sum_{j=0}^{m-1}a_jy^j\longmapsto
\sum_{j=0}^{m-1}\alpha(a_j)y^j.
\]
If \(v\) and its specified inverse \(w\) represent the original
unit and inverse in this algebra, their images satisfy
\(\alpha(v)\alpha(w)=\alpha(vw)=\alpha(1)=1\). Translation satisfies
the same identity. Thus both operations preserve the actual unit
and its inverse as algebra elements, with every nilpotent
coefficient retained. This calculation does not assert a map
from arbitrary complex analytic functions to finite-field
functions; it is the exact algebra map for the specified
coefficient specialization and primary classes.

The phase in SPF.5 is explicitly the primitive of \(h\), and the
sheaf calculation concerns that stated phase. No factor of the
original unit is present in that phase and no unit factor is
silently canceled in the sheaf computation. The preceding
algebra map identifies exactly what retaining the original
unit in the coefficient data establishes.

All convention, invariant-space, and nilpotent claims in
SPF.18–29 pass this review. One proof precision repair was sent
to the parent: in the total ramification proof, the equation
\(p\,v_E(z)=-e\) immediately forces \(e=p\), as in Section 4;
including it avoids leaving a defectlessness theorem implicit
in the phrase that the residue field is algebraically closed.

The parent adopted this repair and reported the final SPF source
SHA256 07c12cb103535255a194275944e7b3cb3c0ce43b3e65c06633038be3e1e6577d.
The bounded independent review is complete; no remaining convention
or inertia correction was identified.
