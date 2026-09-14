# Independent review of the final Deligne amplification

Reviewed 2026-09-13: all 102 lines of `DELIGNE_AMPLIFICATION.md`, followed by rereading both corrected explanatory paragraphs. Current reviewed source SHA-256: `C988FD8A4A571ADC59E401045CC9A5BCC4C735FAECEDFDD90CD4D1AFFB8F0C96`. This audit treats DA1 and the Frobenius-equivariant Künneth isomorphism as the supplied, primary-verified inputs; it does not reprove étale foundations or repeat the primary-source audit. The reviewer did not edit the amplification source; the root agent made the two corrections documented below.

## Verdict

The finite contradiction DA2–DA7 is correct on the stated objects. The original additive tensor calculation and the full local nilpotent exponent are also correct. The root agent applied both minor qualifications identified during review, and the reviewer verified them in the current source at the hash above. No corrections remain in this bounded mathematical review. The checked artifact is the Markdown source; this receipt does not claim verification of a generated TeX copy.

## Exact checks

**Product and cohomological degree — lines 15–35.** For positive even \(k\), the product remains smooth, projective and geometrically irreducible over the same \(\mathbb F_q\); its dimension is \(kd\), which is even. The all-\(d\) Künneth summand has total degree \(kd\), so it lies in precisely the middle cohomology to which DA1 applies. The external tensor is retained as a tensor in the direct sum; no permutation quotient is taken. In particular odd \(d\) does not make it vanish by graded antisymmetry.

**Eigenvector survival — lines 29–35.** A functional \(\lambda(v)=1\) proves \(v^{\otimes k}\ne0\). Injectivity of the Künneth summand proves that its cup-product image is nonzero. Equivariance gives eigenvalue \(\alpha^k\). This proof uses one actual eigenvector and never requires a semisimple Frobenius action.

**Algebraicity, including odd dimension — line 37.** Applying the supplied bound to \(X_0^2\) makes \(\alpha^2\) algebraic over \(\mathbb Q\). The element \(\alpha\) satisfies \(T^2-\alpha^2=0\) over \(\mathbb Q(\alpha^2)\); hence
\[
[\mathbb Q(\alpha):\mathbb Q]
\le2[\mathbb Q(\alpha^2):\mathbb Q]<\infty.
\]
This establishes algebraicity without first applying an even-dimension lemma to an odd-dimensional variety. The positive lower bound on \(|\alpha^2|\) also gives \(\alpha\ne0\), justifying the later logarithm.

**Every complex conjugate — lines 37–56.** For every embedding \(\sigma:\mathbb Q(\alpha)\hookrightarrow\mathbb C\), its restriction to \(\mathbb Q(\alpha^k)\) is an embedding and
\[
\sigma(\alpha^k)=\sigma(\alpha)^k.
\]
DA1 bounds every conjugate of the actual product eigenvalue \(\alpha^k\), so it bounds this image for every positive even \(k\). A single embedding can therefore be fixed throughout DA4–DA7. This reasoning does not require every complex conjugate itself to occur as a separately chosen \(\ell\)-adic eigenvalue.

**Explicit integer and strict inequalities — lines 58–75.** For \(\varepsilon\ne0\), let \(x=1/(4|\varepsilon|)>0\). Then \(\lfloor x\rfloor+1>x\), including integral \(x\), so the displayed
\[
k=2(\lfloor x\rfloor+1)
\]
is positive and even, and \(k>1/(2|\varepsilon|)\). Thus \(k|\varepsilon|>1/2\). Since \(q>1\), exponentiation preserves the strict order: the positive-displacement case violates the upper DA4 inequality and the negative case violates its lower inequality. The case \(\varepsilon=0\) is separately retained. There is no endpoint equality gap.

**Products versus base-field extensions — lines 90–94.** The formulas correctly distinguish fixed \(q\), growing dimension \(kd\) from growing field size \(q^r\), fixed dimension \(d\). In the base-extension formula, division of the exponents by \(r\) leaves the error \(1/2\); in the product formula, division by \(k\) gives \(1/(2k)\). The corrected paragraph explicitly takes \(d\) even, as required for a direct application of DA1.

**Original additive tensor — line 100.** If \(Av=\rho v\) and \(A_j\) acts on factor \(j\), then
\[
\Bigl(\sum_{j=1}^kA_j\Bigr)v^{\otimes k}
=\sum_{j=1}^k\rho v^{\otimes k}=k\rho v^{\otimes k}.
\]
The same functional test proves nonvanishing. For \(\rho=1/2+\delta+i\gamma\), the real displacement from \(k/2\) is exactly \(k\delta\); neither \(\alpha^k\) nor a multiplicative Frobenius formula is substituted for this additive operator.

For a full local block with \(N^m=0\), \(N^{m-1}\ne0\), let \(N_j\) be its operator on tensor factor \(j\), and put \(K=k(m-1)\). The \(N_j\) commute. Every nonzero term in the multinomial expansion has each exponent at most \(m-1\). At total degree \(K\), the unique possible exponent list is \((m-1,\ldots,m-1)\), giving the exact identity
\[
\Bigl(\sum_jN_j\Bigr)^K
=\frac{K!}{((m-1)!)^k}\prod_jN_j^{m-1}.
\]
Choose \(w\) with \(N^{m-1}w\ne0\); applying the product to \(w^{\otimes k}\) gives the nonzero tensor \((N^{m-1}w)^{\otimes k}\). The coefficient is nonzero in characteristic zero. At degree \(K+1\), every exponent list has an entry at least \(m\), so the power is zero. Thus the top nonzero power is exactly \(K\), and the nilpotency index is \(K+1\). When \(m=1\), this reads power zero equal to the identity and power one equal to zero, as required. This verifies the retained local multiplicity calculation.

**Arithmetic scope — line 102.** The source explicitly keeps Deligne's numerical theorem on its finite-field cohomology and does not insert it as a bound on the Split-Zero tensor source. The analogy records the amplification calculation and the needed comparison of actual errors; it does not claim a new arithmetic exclusion from DA1.

## Minor qualifications resolved and verified

1. **Line 90, direct application domain — resolved.** DA1 is stated only for even dimension, whereas \(d\) in the running argument is arbitrary. The current source now explicitly says “Take \(d\) even so that (DA1) applies directly.” This resolves the domain issue. The numerical cancellation is correct.

2. **Line 88, general error-family wording — resolved.** The current source replaces the former necessity claim with the exact condition for a family of bounds \(|\varepsilon|\le e_k/k\), with nonnegative \(e_k\). Their intersection is \(\{0\}\) precisely when
   \[
   \inf_{k\in2\mathbb N_{>0}}e_k/k=0.
   \]
   Indeed a zero infimum excludes each positive \(|\varepsilon|\); a positive infimum retains the interval with that radius. The condition \(e_k=o(k)\) is sufficient. It is not necessary: take \(e_k=1/2\) when \(k\) is a power of two and \(e_k=k\) for all other positive even \(k\). The ratios have infimum zero but do not tend to zero. The current source states precisely the infimum condition and the sufficient sublinear condition. For its actual \(e_k=1/2\), DA6 and the contradiction remain unaffected.
