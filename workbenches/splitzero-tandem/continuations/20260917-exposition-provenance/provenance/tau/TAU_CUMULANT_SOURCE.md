# Human source for the tau note's moment–cumulant identity

Checked: 2026-09-17. This additive record resolves one attribution edge in the deposited Secondary Note, DOI [10.5281/zenodo.19120905](https://doi.org/10.5281/zenodo.19120905). It does not change the deposited text or certify unrelated claims in that note.

## Exact dependent passage

The file inspected is `split_zero_secondary_note.tex`. Its SHA-256 is `8e1aa2f934c49fc21e7a3d946ac6a465bc1a68896ec184afcb3d989cc9f8b364`.

The original shifted Dirichlet series is defined at line 1113 (`def:Lt`); the derivative identity is `cor:jets`, line 1180. The relevant definitions begin at line 1258 (`def:cumulants`). The partition theorem begins at line 1270 (`thm:cumulant-partition-formula`). At line 1318 its proof invokes a standard moment–cumulant identity without giving a human source. The first-four-cumulants corollary begins at line 1328.

## Authenticated source and exact locator

**Peter McCullagh, _Tensor Methods in Statistics_, second edition, Dover Publications, 2018, §2.3.4, printed p. 38, equation (2.9).** The immediately preceding §2.3.3, printed pp. 35–37, derives the formal composition identity (2.8); taking the outer series to be the logarithm gives (2.9).

The [author's University of Chicago book page](https://www.stat.uchicago.edu/~pmcc/tensorbook/) identifies the linked [author-hosted PDF](https://www.stat.uchicago.edu/~pmcc/tensorbook/DoverEdition.pdf) as the Dover 2018 edition. Its preface records revision in August 2017. The [publisher's ISBN page](https://store.doverpublications.com/products/9780486823782) identifies ISBN 9780486823782. Do not confuse this with the separately available first edition or the similarly dated Taylor & Francis electronic reissue.

The complete author PDF was fetched successfully and parsed in memory: 1,113,279 bytes, 292 PDF pages, SHA-256 `c91d3731543cbb3fac05541e9d2f45e62fc246536296991b64e7ce8acfe8f1bf`. Printed p. 38 is PDF page 50, zero-based index 49. No copy of the copyrighted book was added to this public-facing work tree. Text extraction through the web PDF reader succeeded; the first-edition chapter PDF's text encoding was defective, so it was not used as the exact formula witness. Local cache lookup found no McCullagh record.

**Status:** bibliographic authentication, exact formula extraction, and application to the project's complex formal series have all been checked. The identity is **known after translation of notation**, not a project novelty.

## Exact translation, including domain and signs

Keep the note's original objects. For

\[
L(s)=\sum_{r\geq1}a_r r^{-s},\qquad
L_t(s)=\sum_{r\geq1}a_r(r+t)^{-s},\qquad
|t|<1,\quad\Re(s)>\sigma_a,
\]

fix an original point \((t,s)\) with \(L_t(s)\ne0\). Use the holomorphic logarithm of \(r+t\) on the right half-plane; this is the branch determined by the positive real value at \(t=0\). For any \(\rho<1\), the functions \((r+t)^{-s-j}\), for \(|t|\leq\rho\) and fixed \(s,j\), satisfy

\[
|(r+t)^{-s-j}|\leq C_{s,j,\rho}r^{-\Re(s)-j}.
\]

Indeed, write \((r+t)^{-s-j}=r^{-s-j}\exp(-(s+j)\log(1+t/r))\). The exponential factor is uniformly bounded because \(|t/r|\leq\rho<1\). Absolute convergence of the original Dirichlet series at \(\Re(s)\), together with this bound, gives locally uniform convergence of each derivative series. Termwise differentiation therefore yields, with the original rising factorial,

\[
(s)_0=1,\qquad(s)_j=s(s+1)\cdots(s+j-1),\qquad
\partial_t^{\,j}L_t(s)=(-1)^j(s)_jL_t(s+j).
\]

The source-to-project dictionary is

| McCullagh's formula | Original project expression |
|---|---|
| index set \([n]\) | \(\{1,\ldots,n\}\) |
| set partitions \(\Upsilon_n\) | \(\Pi_n\) |
| block \(b\), number of blocks \(\#\sigma\) | \(B\), \(|\pi|\) |
| block moment \(\mu(b)\) | \(m_{|B|}(t;s)=\partial_t^{|B|}L_t(s)/L_t(s)\) |
| cumulant \(\kappa([n])\) | \(\kappa_n(t;s)=\partial_t^n\log L_t(s)\) |

Here \(m_0=1\), and the note's exact coefficient is

\[
m_j(t;s)=(-1)^j(s)_j\frac{L_t(s+j)}{L_t(s)}
=(-1)^jA_j(t;s).
\]

These quantities can be complex. No probability distribution, positivity, or real-valuedness is claimed or required. The pertinent source is the formal-series derivation, rather than an unsupported probabilistic interpretation.

For completeness, the exact specialization is the unital algebra homomorphism

\[
\Phi_{t,s}:\mathbb Q[x_1,x_2,\ldots]\longrightarrow\mathbb C,
\qquad
x_j\longmapsto(-1)^j(s)_j\frac{L_t(s+j)}{L_t(s)}.
\]

It exists uniquely because the source is the polynomial algebra on the displayed generators. Every coefficient used below is a polynomial involving only finitely many generators, so \(\Phi_{t,s}\) applies coefficientwise with no exchange of infinite numerical sums.

Set

\[
U(z)=\sum_{j\ge1}x_j\frac{z^j}{j!},\qquad
C_n=n![z^n]\log(1+U(z)).
\]

The formal logarithm is defined in the \(z\)-adic algebra by

\[
\log(1+U)=\sum_{k\ge1}\frac{(-1)^{k-1}}k U^k.
\]

Since \(U\) has zero constant coefficient, only \(1\leq k\leq n\) contribute to \(C_n\). An ordered list of \(k\) nonempty disjoint blocks covering \([n]\), with ordered block sizes \(j_1,\ldots,j_k\), has \(n!/(j_1!\cdots j_k!)\) label assignments. Each unordered partition into \(k\) blocks has exactly \(k!\) orderings. Therefore

\[
n![z^n]U(z)^k
=\sum_{\substack{j_1+\cdots+j_k=n\\j_i\ge1}}
\frac{n!}{j_1!\cdots j_k!}x_{j_1}\cdots x_{j_k}
=k!\sum_{\substack{\pi\in\Pi_n\\|\pi|=k}}
\prod_{B\in\pi}x_{|B|},
\]

and hence, with every coefficient retained,

\[
C_n=\sum_{\pi\in\Pi_n}
(-1)^{|\pi|-1}(|\pi|-1)!
\prod_{B\in\pi}x_{|B|}.
\]

Because \(L_t(s)\ne0\), continuity supplies a disk about the original \(t\), contained in \(|t|<1\), on which \(L\) has no zero as a function of its subscript. On that disk choose a local holomorphic logarithm \(\ell(w)=\log L_w(s)\). Taylor's theorem gives

\[
\Phi_{t,s}(1+U(z))=\frac{L_{t+z}(s)}{L_t(s)},\qquad
\log\!\left(\frac{L_{t+z}(s)}{L_t(s)}\right)
=\ell(t+z)-\ell(t).
\]

The logarithm on the left has value zero at \(z=0\); thus both sides are the same local holomorphic function. Its \(n\)-th Taylor coefficient times \(n!\) is the original \(\kappa_n(t;s)\). Applying \(\Phi_{t,s}\) to \(C_n\) proves

\[
\kappa_n(t;s)=
\sum_{\pi\in\Pi_n}(-1)^{|\pi|-1}(|\pi|-1)!
\prod_{B\in\pi}m_{|B|}(t;s).
\]

Finally \(\sum_{B\in\pi}|B|=n\) for each partition, so the signs multiply to \((-1)^n\), exactly as in the deposited theorem:

\[
\boxed{\displaystyle
\kappa_n(t;s)=(-1)^n
\sum_{\pi\in\Pi_n}(-1)^{|\pi|-1}(|\pi|-1)!
\prod_{B\in\pi}(s)_{|B|}\frac{L_t(s+|B|)}{L_t(s)}.}
\]

This argument proves the stated specialization on the original convergence domain and at its nonzero values. It does not assign a value at a zero or pole of \(L_t(s)\), prove a global logarithm exists, or establish any separate meromorphic-continuation claim. The polynomial identity also applies to any already-established holomorphic germ with nonzero constant value; no such further continuation is assumed here.

## One-hop human attribution trail

1. **The immediate source actually used here is Peter McCullagh.** His p. 37 follows formula (2.8) by directing readers to **Warren P. Johnson (2002), §2**, for another derivation and history of the formula named for **Francesco Faà di Bruno**. The [publisher's record](https://doi.org/10.1080/00029890.2002.11919857) authenticates Johnson's article, _The Curious History of Faà di Bruno's Formula_, _American Mathematical Monthly_ 109(3), 217–234. That backward reference is recorded; this check does not claim to have audited Johnson's complete historical argument or establish first priority for Faà di Bruno.
2. **The partition-lattice route has a separate precise human lineage.** **T. P. Speed**, _Cumulants and partition lattices_, _Australian Journal of Statistics_ 25(2) (1983), 378–388, DOI [10.1111/j.1467-842X.1983.tb00391.x](https://doi.org/10.1111/j.1467-842X.1983.tb00391.x), is authenticated by its publisher. Full original text was not obtained in this pass; no theorem number is invented for it. **Peter McCullagh's author-hosted April 2011 commentary**, [pp. 2 and 4](https://www.stat.uchicago.edu/~pmcc/reports/speed.pdf), gives the partition-lattice coefficient and expressly treats the theory algebraically, without requiring positive or real moments. Its p. 2 attributes the incidence-algebra inversion framework to **Gian-Carlo Rota (1964)**. This commentary is a first-hand exposition, not Speed's original article.
3. **Gian-Carlo Rota**, _On the foundations of combinatorial theory I. Theory of Möbius functions_, _Zeitschrift für Wahrscheinlichkeitstheorie und Verwandte Gebiete_ 2 (1964), 340–368, DOI [10.1007/BF00531932](https://doi.org/10.1007/BF00531932), has authenticated publisher metadata. McCullagh's commentary bibliography transposes the final page to 386; use the publisher's **368**. The Rota paper is recorded as the underlying framework in that attribution trail, not as a paper whose cumulant theorem was directly verified here.

These are attribution edges with different evidence levels. They do not show that the original project's author or model actually consulted these sources while drafting the deposited note. They identify human mathematical antecedents suitable for the additive corrected exposition. They also do not imply that all authors mentioned elsewhere in McCullagh's books contributed specifically to this project.

## Citation text ready for the additive exposition

> The partition coefficients in this calculation are classical. We use Peter McCullagh's formal-series derivation of the moment–cumulant identity, _Tensor Methods in Statistics_, second edition (2018), §2.3.3–2.3.4, especially (2.9), p. 38. The present application substitutes the original shifted Dirichlet-series derivatives into that identity, with the factor \((-1)^n\) retained. For the partition-lattice treatment, see T. P. Speed (1983); its inversion framework is associated with Gian-Carlo Rota (1964). This is a specialization of a classical identity, not a new moment–cumulant formula.

Suggested LaTeX call: `\cite[\S\S 2.3.3--2.3.4, eq.~(2.9), p.~38]{McCullagh2018Tensor}`. The accompanying `TAU_CUMULANT_SOURCE.bib` provides the exact source entry and the distinctly marked historical references.

## Search and verification boundary

Queries included “Speed Cumulants and partition lattices 1983 pdf moment cumulant Mobius,” “McCullagh cumulants partition formula factorial log generating function,” and searches for the author-hosted book, its Dover ISBN, Johnson's article and Rota's DOI. Primary sources used for the mathematical statement were McCullagh's author-hosted book and commentary; publisher pages authenticate bibliographic metadata. Search snippets and third-party summaries were discovery aids only. The formula was checked again against the dependent note and independently derived above. No global-priority or novelty search was conducted. No deposited mathematical source, mathematical continuation prompt, public repository, Zenodo record, or remote metadata was changed.
