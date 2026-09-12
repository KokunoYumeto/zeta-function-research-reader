# Independent all-depth invariant-dimension and degree audit

This audit reads the delivered `Tau_Cyclic_Sum_Control/NOTE.tex`, Sections 2, 7 and 8, and the complete `work/cyclic_sum_depth_independent_audit_20260912.md`. The delivered NOTE has SHA256 `2cdfd5b25631464f9500dc5fd07c4c8f5c927c8877eb1bf076307ec5dcbc2e8c`. The original polynomial, all root orders, every collided occupation, and the literal sum coordinate are retained below. No original source, cumulative TeX or release file was edited. No Lean or numerical claim is made.

Both proposed formulas are correct. The generating-series coefficient must use the total block cost across all coordinates, and the proof of the degree bound must retain the full original monic polynomial through its triangular division basis. Here are complete proofs.

## 1. Objects and local coordinate maps

Let

\[
h(s)=\prod_{i=1}^{a}(s-\rho_i)^{m_i},\qquad
m_i\geq1,\qquad d=\sum_i m_i\geq1,
\]

where the roots \(\rho_i\) are distinct. Let \(k,r\geq1\), and retain

\[
P_k=\mathbb C[s_1,\ldots,s_k],\quad
I_k=(h(s_1),\ldots,h(s_k)),\quad
B_{k,r}=P_k/I_k^r,\quad S=\sum_{j=1}^k s_j.
\]

For an occupation \(\mathbf n=(n_1,\ldots,n_a)\), with \(n_i\geq0\) and \(\sum_i n_i=k\), choose the ordered root tuple in which the first \(n_1\) coordinates have centre \(\rho_1\), the next \(n_2\) have centre \(\rho_2\), and so on. Its translated coordinates are \(z_{i,j}=s_{i,j}-\rho_i\), for \(1\leq j\leq n_i\). Its stabilizer is

\[
H_{\mathbf n}=\prod_i S_{n_i},\qquad
\lambda_{\mathbf n}=\sum_i n_i\rho_i.
\]

The full local factor at this tuple is exactly

\[
L_{\mathbf n,r}
=\mathbb C[z_{i,j}:1\leq i\leq a,1\leq j\leq n_i]
\big/\big(z_{i,j}^{m_i}:i,j\big)^r.
\tag{D.1}
\]

Indeed, in the original local ring
\(h(\rho_i+z_{i,j})=u_i(z_{i,j})z_{i,j}^{m_i}\), where
\(u_i(z)=\prod_{v\ne i}(\rho_i-\rho_v+z)^{m_v}\) and
\(u_i(0)\ne0\). Each displayed unit is invertible. Thus the original local ideal equals the ideal in (D.1), and equality persists for its exact power \(r\). This replaces its generators by the stated invertible multiples; it does not alter \(s_{i,j}\), \(z_{i,j}\), \(S\), or a Taylor unit used in the arithmetic inclusion. The quotient in (D.1) is already local: every \(z_{i,j}^{r m_i}\) vanishes, so a polynomial with nonzero constant term has a finite geometric-series inverse.

To see the global product explicitly, the ideal \((h(s_1)^r,\ldots,h(s_k)^r)\) is contained in \(I_k^r\). Its quotient is the tensor product of the one-variable quotients \(\mathbb C[s_j]/(h^r)\), each of which splits by the Chinese remainder theorem into the original root factors of lengths \(r m_i\). Quotienting their product by the image of \(I_k^r\) gives exactly (D.1) at each ordered tuple. The permutation action sends these local factors to the factors with permuted centres and permutes their displayed translated coordinates.

The invariant part of the product of all factors in one occupation orbit is canonically isomorphic to \(L_{\mathbf n,r}^{H_{\mathbf n}}\). The forward map restricts an invariant family to the chosen factor. For the inverse, given \(v\in L_{\mathbf n,r}^{H_{\mathbf n}}\), put the value \(\sigma v\) in the factor with centre tuple \(\sigma\boldsymbol\rho\). If two permutations give that same tuple, their difference belongs to its stabilizer and fixes \(v\); hence the value is well-defined. These two maps are inverse algebra maps and commute with multiplication by the original \(S\). Therefore

\[
B_{k,r}^{S_k}\cong
\prod_{\substack{\mathbf n\in\mathbb N^a\\\sum_i n_i=k}}
L_{\mathbf n,r}^{H_{\mathbf n}}.
\tag{D.2}
\]

No orbit factor or occupation idempotent is identified with another when two sums coincide.

## 2. Exact orbit-sum basis and generating series

A monomial \(z^{\boldsymbol\alpha}\) belongs to the ideal in (D.1) exactly when

\[
\sum_{i,j}\left\lfloor\frac{\alpha_{i,j}}{m_i}\right\rfloor\geq r.
\tag{D.3}
\]

The generators of that ideal power are the products
\(\prod_{i,j} z_{i,j}^{m_i c_{i,j}}\) with \(\sum c_{i,j}=r\). Such a product divides the given monomial exactly when integers \(c_{i,j}\) with that sum can be chosen below their respective capacities \(\lfloor\alpha_{i,j}/m_i\rfloor\). They can be chosen if and only if the sum of capacities is at least \(r\). Since this is a monomial ideal, the complementary monomials are a basis, with no further linear relations.

Write each exponent uniquely as

\[
\alpha_{i,j}=m_i q_{i,j}+b_{i,j},\qquad
q_{i,j}\geq0,\quad 0\leq b_{i,j}<m_i.
\]

A surviving monomial has total block cost \(\sum_{i,j}q_{i,j}<r\). The group \(H_{\mathbf n}\) permutes these monomials. For every orbit \(\mathcal O\) of surviving monomials, retain its unscaled orbit sum

\[
o_{\mathcal O}=\sum_{z^{\boldsymbol\alpha}\in\mathcal O}z^{\boldsymbol\alpha}.
\tag{D.4}
\]

An invariant vector has constant coefficients on each orbit, so these orbit sums span the invariants. Distinct sums have disjoint supports in the monomial basis, so they are independent. Thus (D.4) is an exact invariant basis. In particular no factor \(1/|\mathcal O|\), no quotient by an orbit size, and no rescaling of a coefficient is used.

Its orbits are indexed by nonnegative integers

\[
c_{i,q,b}=\#\{j:(q_{i,j},b_{i,j})=(q,b)\},
\]

with the exact constraints

\[
\sum_{q\geq0}\sum_{b=0}^{m_i-1}c_{i,q,b}=n_i
\quad\hbox{for every }i,
\qquad
\sum_i\sum_{q\geq0}\sum_{b=0}^{m_i-1}q c_{i,q,b}<r.
\tag{D.5}
\]

Indeed the counts are unchanged by permutations; conversely, equal counts permit matching every coordinate type within its root block, giving a stabilizer permutation. A type \((i,q,b)\) used \(c\) times contributes \(x_i^c t^{qc}\). Summing over all \(c\geq0\) gives \((1-x_i t^q)^{-1}\). Taking the product over the literal \(m_i\) residue types proves

\[
\boxed{
d_{\mathbf n,r}:=\dim L_{\mathbf n,r}^{H_{\mathbf n}}
=\sum_{j=0}^{r-1}
[x_1^{n_1}\cdots x_a^{n_a}t^j]
\prod_{i=1}^{a}\prod_{q\geq0}(1-x_i t^q)^{-m_i}.}
\tag{D.6}
\]

This is an identity of formal coefficient counts. For the indicated coefficients, all factors with \(q\geq r\) contribute only their constant term and may be omitted. The remaining product has finitely many factors; its \(q=0\) factors are expanded in the variables \(x_i\), and extracting the prescribed finite occupation makes every coefficient finite. Thus no analytic convergence hypothesis is hidden in (D.6).

## 3. Collisions, nilpotent lengths and exact traces

On the factor (D.1), multiplication by the original sum is

\[
M_S=\lambda_{\mathbf n}I+M_X,\qquad
X=\sum_{i,j}z_{i,j}.
\]

Put \(M_{\mathbf n}=\max_{i:n_i>0}m_i\) and

\[
D_{\mathbf n,r}=\sum_i n_i(m_i-1)+(r-1)M_{\mathbf n},
\qquad L_{\mathbf n,r}^{\rm cyc}=D_{\mathbf n,r}+1.
\tag{D.7}
\]

For every surviving monomial,

\[
|\boldsymbol\alpha|
=\sum_{i,j}b_{i,j}+\sum_{i,j}m_iq_{i,j}
\leq D_{\mathbf n,r}.
\]

Equality is achieved by setting every residue \(b_{i,j}=m_i-1\) and placing all \(r-1\) blocks at one coordinate of order \(M_{\mathbf n}\). Hence \(X^{D_{\mathbf n,r}+1}=0\), whereas \(X^{D_{\mathbf n,r}}\) has the specified surviving monomial with nonzero coefficient
\(D_{\mathbf n,r}!/\prod_{i,j}\alpha_{i,j}!\). This proves its exact nilpotence index. The vector \(1\) and all its powers under \(M_X\) are invariant, so the restriction to \(H_{\mathbf n}\)-invariants has the same index. The unscaled orbit sum containing this monomial has that same nonzero coefficient in \(X^{D_{\mathbf n,r}}\), since permuting coordinates preserves the factorial product.

Consequently the generalized \(\lambda\)-space in \(B_{k,r}^{S_k}\) is the product of the exact occupation factors with \(\lambda_{\mathbf n}=\lambda\); as a vector space this finite product is also their direct sum. Its dimension is

\[
\boxed{a_{\lambda,r}
=\sum_{\mathbf n:\lambda_{\mathbf n}=\lambda}d_{\mathbf n,r}.}
\tag{D.8}
\]

Its nilpotence index is
\(\ell_{\lambda,r}=\max_{\mathbf n:\lambda_{\mathbf n}=\lambda}L_{\mathbf n,r}^{\rm cyc}\). Thus its characteristic and minimal polynomials, with a separate polynomial variable \(T\), are respectively

\[
\prod_{\lambda}(T-\lambda)^{a_{\lambda,r}},
\qquad
\chi_{h,k,r}(T)=\prod_{\lambda}(T-\lambda)^{\ell_{\lambda,r}}.
\tag{D.9}
\]

For the minimal polynomial assertion, vanishing of a polynomial in \(S\) is tested in every local factor, where its order at \(\lambda_{\mathbf n}\) must be at least the exact index in (D.7). Distinct factors at the same sum therefore contribute a maximum, while their vector-space dimensions add as in (D.8). The invariant vector \(1\) has precisely this annihilator, proving the assertion also on the invariant algebra.

For an entire function \(f\), its evaluation on a local factor is the finite Taylor polynomial in \(M_X\). Every positive power of a nilpotent operator has trace zero, so

\[
\operatorname{Tr}(f(M_S)|B_{k,r}^{S_k})
=\sum_{\lambda}a_{\lambda,r}f(\lambda).
\tag{D.10}
\]

The algebra map
\(\alpha_r:\mathbb C[S]/(\chi_{h,k,r})\to B_{k,r}^{S_k}\),
\([P]\mapsto[P(S)]\), is injective by the annihilator calculation. With the original full symmetric Taylor unit \(U_{k,r}\), multiplication by \(U_{k,r}\) is invertible and commutes with \(M_S\); hence the weighted map \(\eta_r=M_{U_{k,r}}\alpha_r\) is an injective \(\mathbb C[S]\)-module map. The quotient
\(T_{k,r}=B_{k,r}^{S_k}/\eta_r\mathbb C[S]/(\chi_{h,k,r})\)
therefore has generalized \(\lambda\)-dimension \(a_{\lambda,r}-\ell_{\lambda,r}\), and

\[
\operatorname{Tr}(f(M_S)|T_{k,r})
=\sum_\lambda(a_{\lambda,r}-\ell_{\lambda,r})f(\lambda).
\tag{D.11}
\]

To justify the dimension statement through the exact sequence, take its generalized-sum idempotents: they are polynomials in \(M_S\) supplied by the Chinese remainder identity for the pairwise coprime powers in (D.9), and all arrows commute with them. The sequence therefore restricts to an exact sequence at each sum. For (D.11), choose a basis of the invariant submodule and extend it to a basis of the full space. Every \(f(M_S)\) has a block upper-triangular matrix, whose diagonal blocks are its submodule and quotient maps; their traces add. General multiplication by \(U_{k,r}^{\dagger}U_{k,r}\) has not been assumed to preserve the weighted cyclic image. The compression maps already supplied in the independent depth audit remain necessary for that general multiplier.

## 4. Original monic division and the all-depth degree bound

The following proof applies directly to the original \(h\), including all its lower coefficients. For multi-indices \(\mathbf a\in\mathbb N^k\) and \(\mathbf b\in\{0,\ldots,d-1\}^k\), put

\[
e_{\mathbf a,\mathbf b}(\mathbf s)
=\prod_{i=1}^{k}h(s_i)^{a_i}s_i^{b_i}.
\tag{D.12}
\]

Since the original \(h\) is monic of degree \(d\), this polynomial has leading homogeneous term
\(\mathbf s^{d\mathbf a+\mathbf b}\), and every other term has strictly smaller total degree. Every exponent vector \(\boldsymbol\gamma\in\mathbb N^k\) has one and only one expression \(d\mathbf a+\mathbf b\) with these residue bounds. Induction on total degree therefore expresses every monomial as a finite linear combination of (D.12): subtract the unique (D.12) with its same leading monomial, and expand the remaining lower-degree terms. These polynomials are independent: in a finite nonzero relation, choose the largest total degree present. At that degree, their leading monomials are distinct, so their nonzero coefficients cannot cancel. This proves a basis of the original polynomial ring, without changing \(h\) to a pure power or erasing any of its coefficients.

In this basis, the original ideal power has the exact description

\[
I_k^r
=\operatorname{span}_{\mathbb C}
\{e_{\mathbf a,\mathbf b}:|\mathbf a|\geq r\}.
\tag{D.13}
\]

Indeed, for \(|\mathbf a|\geq r\), choose \(\mathbf c\leq\mathbf a\) with \(|\mathbf c|=r\). Then (D.12) is a multiple of \(\prod_i h(s_i)^{c_i}\), so it lies in \(I_k^r\). Conversely, every element of \(I_k^r\) is a finite sum of those products with \(|\mathbf c|=r\) times arbitrary polynomials. Expanding each multiplying polynomial in (D.12) simply shifts its index \(\mathbf a\) to \(\mathbf a+\mathbf c\), whose total is at least \(r\). This proves both containments.

It follows that the classes of (D.12) with \(|\mathbf a|<r\) form a quotient basis. Let

\[
D=k(d-1)+(r-1)d.
\tag{D.14}
\]

For every integer \(0\leq q\leq D\), there exists an exponent vector \(\boldsymbol\gamma\) with

\[
|\boldsymbol\gamma|=q,\qquad
0\leq\gamma_1\leq(r-1)d+d-1,\qquad
0\leq\gamma_i\leq d-1\ (i>1).
\tag{D.15}
\]

For example, distribute \(q\) units successively up to these displayed capacities; their sum is exactly \(D\), so all \(q\) units can be assigned. For its unique division \(\boldsymbol\gamma=d\mathbf a+\mathbf b\), one has \(|\mathbf a|\leq r-1\): all indices except possibly the first are zero. This is therefore a surviving quotient-basis index in (D.13).

Now take a nonzero one-variable polynomial \(F(T)=c_qT^q+\cdots+c_0\) of degree \(q\leq D\), where \(c_q\ne0\). In the original polynomial \(F(S)\), the coefficient of \(\mathbf s^{\boldsymbol\gamma}\) in its degree-\(q\) homogeneous part is precisely

\[
c_q\frac{q!}{\gamma_1!\cdots\gamma_k!}\ne0.
\tag{D.16}
\]

The triangular-basis expansion in (D.12) has no term of degree greater than \(q\), by its degree-induction construction. At degree \(q\), only the unique matching leading term of each basis element contributes to its monomial. Thus the coefficient of the particular \(e_{\mathbf a,\mathbf b}\) indexed by (D.15) is exactly (D.16). Lower powers of \(S\), and the lower terms of the original factors \(h(s_i)^{a_i}\), have smaller total degree and cannot change it. Since this index satisfies \(|\mathbf a|<r\), its nonzero coefficient survives the quotient (D.13). Consequently \(F(S)\notin I_k^r\).

This proves the explicit injection

\[
\mathbb C[T]_{\leq D}\longrightarrow B_{k,r}^{S_k},\qquad
F\longmapsto[F(S)],
\tag{D.17}
\]

and, using the already computed contracted ideal,

\[
\boxed{\deg\chi_{h,k,r}\geq k(d-1)+(r-1)d+1.}
\tag{D.18}
\]

For each nonzero polynomial of degree at most \(D\), the surviving coefficient (D.16) is a concrete witness for its nonzero image. This proof does not presume absent spectral collisions, simple roots, or a generic original packet. It proves the bound even when the maximizing occupation in an individual collided sum changes with depth.

## 5. Endpoints and an exact finite example

At \(r=1\), formula (D.6) retains only block cost zero, giving

\[
d_{\mathbf n,1}=[x^{\mathbf n}]\prod_i(1-x_i)^{-m_i}
=\prod_i\binom{n_i+m_i-1}{m_i-1}.
\]

The last coefficient counts nonnegative counts of the \(m_i\) residue types with sum \(n_i\): insert \(m_i-1\) separators between \(n_i\) indistinguishable selections, obtaining the stated binomial coefficient. Thus the formula reproduces the source's exact equation (2.6), including all collisions after (D.8).

At \(k=1\), each occupation chooses one root \(\rho_i\). The surviving exponents are \(0,\ldots,r m_i-1\), so its dimension is \(r m_i\). Globally \(\chi_{h,1,r}=h^r\), with degree \(rd\), and (D.18) is equality.

For a single root of multiplicity \(d\), formula (D.7) gives
\(\chi_{h,k,r}(S)=(S-k\rho)^{k(d-1)+(r-1)d+1}\). Hence the bound (D.18) is sharp for every \(k,r,d\geq1\). The invariant dimension remains (D.6) and can be larger. For the exact algebraic fixture \(h=(s-\rho)^2\), \(k=2\), \(r=2\), the seven unscaled invariant basis vectors are

\[
1,\ z_1+z_2,\ z_1z_2,\ z_1^2+z_2^2,\
z_1^3+z_2^3,\ z_1^2z_2+z_1z_2^2,\
z_1^3z_2+z_1z_2^3.
\]

Here the ideal is \((z_1^2,z_2^2)^2\), the cyclic length is \(5\), and the complementary generalized-sum dimension is exactly \(7-5=2\). Formula (D.6) gives the same seven vectors by its three block-cost-zero orbits and four block-cost-one orbits. No claim that this is an actual zeta packet is made.

For \(d=1\), there is a single root of order one. Formula (D.6) counts multisets of \(k\) nonnegative exponents of total degree less than \(r\). The local algebra is exactly \(\mathbb C[z_1,\ldots,z_k]/(z_1,\ldots,z_k)^r\), and its cyclic polynomial is \((S-k\rho)^r\), again attaining (D.18).

For the empty packet \(h=1\), the original ideal is \(P_k\), so every \(B_{k,r}\) and its invariant and cyclic modules are zero, and the contracted polynomial is \(1\). All their maps are the unique zero maps. Neither a maximum over empty occupations nor the positive-degree division basis (D.12) is used at that endpoint. The assumptions \(d\geq1\), \(k,r\geq1\) of (D.6) and (D.18) are therefore exact.

The invariant generating series, collision dimensions, nilpotent lengths, quotient traces and degree bound all pass this independent proof audit with their stated types and endpoints.
