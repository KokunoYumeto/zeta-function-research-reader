# Deligne's final amplification: the exact contradiction

The particular argument requested here is in Pierre Deligne, *La conjecture de Weil I* (1974), Lemma 7.1 and paragraph 7.3, printed pages 298 and 301. It is not a quotation from *Weil II* (1980). The [original paper](https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf) is the primary source; the [English translation](https://arxiv.org/abs/1807.10810) was checked against it. The source input is the proved estimate below and the Frobenius-equivariant Künneth isomorphism. The subsequent calculation spells out their contradiction mechanism.

## The proved bound being reused

Let $q>1$ be the cardinality of the finite base field and let $\ell$ be a prime different from its characteristic. For a smooth, projective, geometrically irreducible variety $Y_0/\mathbb F_q$ of **even** dimension $D$, put $Y=Y_0\times_{\mathbb F_q}\overline{\mathbb F}_q$. Deligne's Lemma 7.1 establishes that each eigenvalue $\beta$ of geometric Frobenius on $H^D(Y,\mathbb Q_\ell)$ is algebraic and that every complex conjugate satisfies

$$q^{D/2-1/2}\le |\beta|\le q^{D/2+1/2}.\tag{DA1}$$

This already excludes everything outside a band of width one in the exponent. The additive error $1/2$ is the same for every such variety and every even dimension. There is no unrecorded constant depending on its Betti numbers in (DA1).

## Constructing the object to which the earlier exclusion applies

Take a smooth, projective, geometrically irreducible $X_0/\mathbb F_q$ of dimension $d$. Let $X$ be its geometric base change and $F_X^*$ its geometric Frobenius action. Take an eigenvalue $\alpha$ in the middle group $H^d(X,\mathbb Q_\ell)$, and an eigenvector $v\ne0$ after extending coefficients to $\overline{\mathbb Q}_\ell$.

For every positive even integer $k$, form the actual product variety

$$X_0^k=\underbrace{X_0\times_{\mathbb F_q}\cdots\times_{\mathbb F_q}X_0}_{k\text{ factors}}.$$

It is again smooth, projective and geometrically irreducible. Its dimension is $kd$, which is even. The field cardinality stays **$q$**. The Frobenius-equivariant Künneth map has the precise form

$$\bigoplus_{i_1+\cdots+i_k=kd}\bigotimes_{j=1}^kH^{i_j}(X,\overline{\mathbb Q}_\ell)
\xrightarrow{\sim}H^{kd}(X^k,\overline{\mathbb Q}_\ell),$$

$$x_1\otimes\cdots\otimes x_k\longmapsto
\operatorname{pr}_1^*x_1\smile\cdots\smile\operatorname{pr}_k^*x_k.\tag{DA2}$$

In particular, the summand with $i_1=\cdots=i_k=d$ injects into the middle cohomology of the product. The tensor $v^{\otimes k}$ is nonzero: choose a linear functional $\lambda$ with $\lambda(v)=1$; then $\lambda^{\otimes k}(v^{\otimes k})=1$. It stays nonzero under the isomorphism (DA2). Frobenius acts on it by

$$(F_X^*)^{\otimes k}v^{\otimes k}
=(\alpha v)\otimes\cdots\otimes(\alpha v)
=\alpha^k v^{\otimes k}.\tag{DA3}$$

Thus the construction retains the offending eigenvalue as $\alpha^k$ in exactly the cohomological degree covered by (DA1). No semisimplicity assertion is needed. Nor is a symmetric or exterior quotient taken: even when $d$ is odd, the external tensor of $v$ with itself in different factors survives.

Algebraicity is not an extra assumption: applying (DA1) to $X_0^2$ shows $\alpha^2$ is algebraic; then $\alpha$ is algebraic over the algebraic extension containing $\alpha^2$. Every complex embedding of $\mathbb Q(\alpha)$ restricts to one on $\mathbb Q(\alpha^k)$, so the following inequalities hold for each fixed complex conjugate of $\alpha$.

## Apply the earlier bound to the newly constructed product

Substitute $Y_0=X_0^k$, $D=kd$ and $\beta=\alpha^k$ into (DA1):

$$q^{kd/2-1/2}\le |\alpha^k|\le q^{kd/2+1/2}.\tag{DA4}$$

Taking positive real $k$th roots, and using $|\alpha^k|=|\alpha|^k$, gives

$$q^{d/2-1/(2k)}\le |\alpha|\le q^{d/2+1/(2k)}
\qquad(k=2,4,6,\ldots).\tag{DA5}$$

The expected exponent $kd/2$ and the actual exponent of $|\alpha|^k$ both scale by $k$. The already-proved error remains $1/2$. This is precisely why its contribution after taking the root is $1/(2k)$.

## The finite contradiction, without relying on informal limiting language

For a fixed complex conjugate define

$$\varepsilon=\log_q|\alpha|-\frac d2.$$

Suppose $\varepsilon\ne0$. Choose the explicit even positive integer

$$k=2\left(\left\lfloor\frac{1}{4|\varepsilon|}\right\rfloor+1\right).
\tag{DA6}$$

Then $k>1/(2|\varepsilon|)$, hence $k|\varepsilon|>1/2$.

If $\varepsilon>0$, (DA3) supplies an actual eigenvalue with

$$|\alpha^k|=q^{kd/2+k\varepsilon}>q^{kd/2+1/2},$$

contradicting the upper bound in (DA4). If $\varepsilon<0$, it supplies

$$|\alpha^k|=q^{kd/2-k|\varepsilon|}<q^{kd/2-1/2},$$

contradicting the lower bound in (DA4). Thus $\varepsilon=0$ and

$$\boxed{|\alpha|=q^{d/2}.}\tag{DA7}$$

An arbitrarily small fixed deviation is enough. A smaller deviation merely requires a larger finite product. The exact boundary $\varepsilon=0$ is retained and satisfies every bound. This closes the middle-degree argument; the cited paper's paragraph 7.2 then uses weak Lefschetz, Poincaré duality, components and finite field extensions to cover the other degrees.

## Why repeating a bound is not sufficient by itself

In exponent coordinates the entire product family is the intersection

$$\bigcap_{k\in2\mathbb N_{>0}}
\left[-\frac1{2k},\frac1{2k}\right]=\{0\}.\tag{DA8}$$

To prove the equality, zero belongs to every interval; a nonzero real number is excluded by the explicit $k$ in (DA6). This is an exhaustive exclusion, not a computation for finitely many chosen dimensions.

Both quantitative and geometric ingredients are essential to the calculation. The same eigenclass maps to a nonzero tensor class; here the exclusion for the resulting class has error exactly $1/2$. With a nonnegative error $e_k$, the corresponding calculation would produce $|\varepsilon|\le e_k/k$. The resulting intersection is the singleton zero exactly when $\inf_{k\in2\mathbb N_{>0}}e_k/k=0$. Sublinear error $e_k=o(k)$ is sufficient; convergence along every even integer is not necessary. If $e_k$ were a fixed positive multiple of $k$, that calculation would leave a positive-width band. No such proportional error is present in (DA4).

Extending the base field alone gives a different calculation. Take $d$ even so that (DA1) applies directly. Replacing $\mathbb F_q$ by $\mathbb F_{q^r}$ replaces $\alpha$ by $\alpha^r$ but leaves dimension $d$ unchanged. The same weak bound would read

$$(q^r)^{d/2-1/2}\le|\alpha|^r\le(q^r)^{d/2+1/2}.$$

Its $r$th root is the original weak bound; the error does not shrink. The product construction keeps $q$ fixed while increasing dimension and tensor exponent together.

## The logical pattern recorded for the actual Split-Zero object

The pattern is: an offending class survives an exact amplification map; the amplified class belongs to a previously bounded object; its fixed nonzero displacement grows linearly with tensor degree; a proved exclusion has smaller growth; a finite tensor degree contradicts that exclusion.

In the actual programme the additive tensor generator is $A_h^{(k)}=\sum_j A_{h,j}$. A nonzero eigenvector with eigenvalue $\rho=1/2+\delta+i\gamma$ has nonzero tensor power with eigenvalue $k\rho$. Its real displacement from $k/2$ is exactly $k\delta$. This statement follows by applying each summand to the original tensor and by the same linear-functional test proving nonvanishing. The complete local nilpotent sum remains $\sum_jN_j$; on a full order-$m$ block its top nonzero power is $k(m-1)$ with coefficient $(k(m-1))!/((m-1)!)^k$ on $\prod_jN_j^{m-1}$. Consequently no multiplicity is discarded in making this comparison.

Deligne's numerical bound is a theorem about his finite-field cohomology. It is not inserted into the Split-Zero tensor source as an assumption. The present construction keeps every already-calculated original arithmetic bound and its actual error term on the same amplified source. Their compatibility or contradiction must be calculated there. The finite contradiction (DA6) records exactly what a successful amplification/exclusion calculation accomplishes.
