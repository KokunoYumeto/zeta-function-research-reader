# Fourier, interpolation, low-rank inverse and probability credit check

Checked 2026-09-17. This is an additive bibliography/provenance report. No mathematical source, frozen bundle, remote publication, or continuation prompt was edited.

## Scope and evidence boundary

The current cumulative TeX inspected is `output/Split_Zero_Web_Continuation_CURRENT/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex`, SHA-256 `9926c5b5670777548f15f3fd626a4237d2c10a26834f51ba2b466a3b3a349656`. Line locators below belong to that exact file. Historical transcript records A1959, A1998 and A2225 are retained in `output/tau_f1_transcript_audit_2026-09-13/sources/turns/`.

Primary-source authentication, exact-result extraction and project application are distinct statuses below. A source cited here as an exposition is not thereby credited with first discovery. The underlying project proofs remain necessary for their arithmetic objects, domains, units, masses and actions.

## 1. Carl de Boor: confluent Newton interpolation and simplex formula

**Verified source:** Carl de Boor, “Divided Differences,” *Surveys in Approximation Theory* **1** (2005), 46–69; published 14 January 2005; paper dated 21 December 2004. [Author/journal record](https://pages.cs.wisc.edu/~deboor/sat/papers/2/); [journal PDF](https://surveys-in-approximation-theory.com/papers/2/2.pdf).

**Exact verified locators:** Proposition 7, p. 48, with condition (8), gives the unique Hermite interpolant in Newton form, including complex repeated nodes. Equation (14), p. 49, gives repeated-node divided differences as derivatives divided by factorials. Section 9, equation (52), p. 64, is the Genocchi–Hermite simplex representation. The historical discussion on pp. 63–65 distinguishes Frobenius, Hermite and Genocchi and warns against an incorrect 1859 Hermite attribution. Cite de Boor as the checked modern treatment; do not call these classical constructions new results of the current programme or discoveries by de Boor.

**Project edge:** AKS20, lines 6636–6668. With de Boor's nodes equal to the original ordered list `omega_1,...,omega_(a+1)`, his Newton factor is precisely `N_a`; the derivative of the project exponential is `v^a exp(v y)`. Its simplex volume is `1/a!`, so the project bound `|v|^a exp(R|v|)/a!` is the stated specialization. Repeated nodes retain their derivative orders. The project also proves this formula directly; a proof does not remove the obligation to credit the classical mechanism.

**Disposition:** add the de Boor citation at AKS20, with these result locators. Earliest historical primary papers were not individually read in this bounded check; do not label their content independently verified here.

## 2. Walter Rudin: authentic edition; exact Plancherel body still unchecked

**Verified source identity:** Walter Rudin, *Fourier Analysis on Groups*, Wiley Classics Library, John Wiley & Sons, 1990; first published 1962; ISBN 0-471-52364-X. [Publisher front matter](https://onlinelibrary.wiley.com/doi/epdf/10.1002/9781118165621.fmatter) explicitly confirms edition, year and ISBN. Its contents identifies Section 1.6, “The Plancherel Theorem,” p. 26. [Publisher book record](https://onlinelibrary.wiley.com/doi/book/10.1002/9781118165621).

**Actual use:** the corpus inventory resolves an existing `rudin1990` entry at `FOUNDATION/tex/satellites/90_references.tex`, lines 188–192, and a declaration of Fourier-analysis use at `FOUNDATION/tex/satellites/10_literature_foundations.tex`, lines 13–17. Current cumulative TeX line 57133 invokes Plancherel for a Gamma-integral mass.

**Status:** edition and section/page verified from the primary publisher; chapter PDF access failed, so theorem number, exact normalization and proof body were **not** verified. Do not convert discovery references to Theorem 1.6.1 into a checked theorem claim. Rudin is a modern exposition, not the originator of Plancherel's theorem. Existing human credit should remain, with this precise verification limit.

## 3. Sherman–Morrison–Woodbury: actual use and historical caution

**Project edges:** OMR18 lines 15830–15858 explicitly invokes a restricted Sherman–Morrison update. IRR27 lines 42086–42101 is an exact rank-four inverse update and expressly disclaims floating-point stability certification.

**Checked treatment:** William W. Hager, “Updating the Inverse of a Matrix,” *SIAM Review* **31**(2) (1989), 221–239, DOI [10.1137/1031049](https://doi.org/10.1137/1031049). [Author-hosted published PDF](https://people.clas.ufl.edu/hager/files/update-1.pdf), p. 221, equations (1)–(2), and pp. 221–223 historical discussion, were read. Hager distinguishes the conventional names from priority: the general inverse modification predates Woodbury's report; the usual rank-one form is associated in this history with Bartlett. Duncan, Guttman and Plackett also appear in that documented history. Cite Hager for the inspected account; do not imply that all these earlier primary papers were inspected.

**Exact project dictionary:** Hager's `A-UV` becomes the original `G_(Y,n-1)+z_(Y,n)^* z_(Y,n)` on setting `A=G_(Y,n-1)`, `U=-z_(Y,n)^*`, `V=z_(Y,n)`. Then `I-VA^(-1)U=I_4+L_(Y,n)`. Thus his formula yields the exact minus correction in IRR27, with unchanged original Gram and rows. Positive definiteness gives the middle inverse; no stability theorem follows.

**Historical bibliographic identities:** Jack Sherman and Winifred J. Morrison, “Adjustment of an Inverse Matrix Corresponding to a Change in One Element of a Given Matrix,” *Annals of Mathematical Statistics* **21**(1) (1950), 124–127, DOI `10.1214/aoms/1177729893`; the [journal's archived issue contents](https://www.jstor.org/stable/i312761) confirms authors/title/pages. Max A. Woodbury, *Inverting Modified Matrices*, Memorandum Report 42, Statistical Research Group, Princeton University, 1950, is reference [52] in Hager. Original Sherman–Morrison article download failed; original Woodbury report was not obtained. Their exact internal equation/page locators remain unverified. The BibTeX retains that distinction.

## 4. Russell Lyons: exterior determinant mechanism actually cited

**Verified source:** Russell Lyons, “Determinantal Probability Measures,” *Publications Mathématiques de l'IHÉS* **98** (2003), 167–212, DOI [10.1007/s10240-003-0016-0](https://doi.org/10.1007/s10240-003-0016-0). [Journal archive metadata](https://www.numdam.org/item/PMIHES_2003__98__167_0/); exact inspected author version [arXiv:math/0204325v4](https://arxiv.org/pdf/math/0204325v4), dated 18 June 2003. Version-specific locators: Section 4, equation (4.1), p. 11 (exterior inner product equals Gram determinant); Section 5, equation (5.1), p. 13 (probabilities on bases from a unit exterior vector).

**Project edge:** A2225, Section 5, lines 404–428, cites the classical exterior determinant mechanism through marker `turn274511view1` (arXiv identity resolved by the parent bibliography audit). This is an inspected modern account of the mechanism, not a claim that Lyons invented exterior algebra or Cauchy–Binet.

**Exact translation:** set `X=B_j O_j^(-1/2)` using the original diagonal masses. Then `XX^*=K_j`. Cauchy–Binet gives `det K_j=sum_(|D|=q) |det X_D|^2`, and each summand is exactly the original `a_D=|det B_D|^2/product_(d in D) omega_d`. If a probability interpretation is stated, its probabilities are `a_D/det K_j`; this auxiliary distribution does not replace the retained determinant or original mass. It is a consequence of the existing metric, not a new choice of metric.

## 5. Oliver Johnson and Andrew Barron: the information projection actually cited

**Verified source:** Oliver Johnson and Andrew Barron, “Fisher information inequalities and the central limit theorem,” *Probability Theory and Related Fields* **129**(3) (2004), 391–409, DOI [10.1007/s00440-004-0344-0](https://doi.org/10.1007/s00440-004-0344-0). [Publisher metadata](https://link.springer.com/article/10.1007/s00440-004-0344-0). Exact inspected version [arXiv:math/0111020v2](https://arxiv.org/pdf/math/0111020v2), dated 4 July 2003: introduction equation (1), p. 2, and Lemma 3.1, pp. 9–10. The latter supplies the conditional score identity and its Pythagorean residual for independent weakly differentiable densities. These version-specific page numbers are not asserted to be journal pagination.

**Credit chain:** the introduction itself credits Stam (1959) and Blachman (1965) for earlier convolution-information methods; it discusses Shimizu (1975), Brown (1982) and Barron (1986) for subsequent information-convergence methods. This is a verified report of Johnson–Barron's attribution, not independent verification of every earlier paper. Do not silently transfer origination to this programme or Johnson–Barron.

**Project edges:** A1959 line 268 (`turn576038view0`) and A1998 line 628 (`turn143300view2`), source identities resolved by the parent audit. A1959 lines 131–266 retain the arithmetic amplitude, its fixed phase, mass `mu_h`, and full relative residual.

**Exact mass dictionary and derivation:** keep `w_h=|a_h|^2`, `m_k=w_h^{*k}` and `mu_h=integral w_h`. To compare with the probability theorem, introduce the explicitly related auxiliary density `p=w_h/mu_h`; this does not change the project objects. For independent `X_i` with density `p`, write `S=sum X_i`, `rho=p'/p`, and `r=(1/k)sum rho(X_i)`. Independence and the vanishing integral of `w_h'` give `E(r^2)=I_h/(k mu_h)`. Differentiating the convolution gives `E(r|S=u)=m_k'(u)/m_k(u)`. In the project's fixed relative coordinates, `2 partial_u Psi_k=Psi_k r` almost everywhere, so `2 n_k=Psi_k(r-E(r|S))`. Consequently `4 integral ||n_k||^2=mu_h^k E[(r-E(r|S))^2]` and `I_(h,k)=mu_h^k E[E(r|S)^2]`. Orthogonal projection therefore gives exactly `I_(h,k)+4 integral ||n_k||^2=mu_h^(k-1) I_h/k`. The zero sets are handled through the smooth amplitude in A1959; this comparison does not add a bounded-score hypothesis. A1998's polynomially weighted extension needs its own displayed calculation and is not supplied by the central limit theorem.

## Status and reproducibility

Only focused primary pages/results above were checked. No global historical priority search, numerical computation, Lean validation, or proof audit of the full research programme is claimed. No remote PDF was retained locally in this subtask; the stable primary links and precise versions identify the inspected sources. Existing source copies were sought through the local corpus inventory and bounded filename searches; none was ingested into a new cache.

Historical transcript hashes: A1959 `e92fb1e61f757edd7fcaf542693e221af4769430320e97c28965a1b472be7f5c`; A1998 `e274ca3b334f39d213a06868c55a5c91e27e01988d0aa78b9f3edf2d2991d715`; A2225 `0b0a38af5d51cbbb70c1535258ffdce5482d56944f610bdf807dfe7934af5751`.
