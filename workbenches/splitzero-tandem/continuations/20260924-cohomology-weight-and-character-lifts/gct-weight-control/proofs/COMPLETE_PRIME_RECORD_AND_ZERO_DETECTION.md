# What the complete prime record detects, and the resulting arithmetic weight

24 September 2026. Proof locators CD1–CD7. This calculation receives the user's integrality and completeness argument in WU037. It retains the common supporting point \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\), the full signed stalk of CG2–CG3, and the original Riemann zeta function. No operation, coordinate, or distance is introduced on the supporting point.

The completed source reconstruction in CG0–CG8 is an input: its uniqueness is uniqueness of the specified complete Connes–Consani chart diagram and its universal localization, with all chart maps retained. Neither the existence of a cyclic stalk nor a spectral weight is deduced merely from the duration of an observation. The analytic quotient used below is the proved quotient in GLOBAL_MELLIN_SYNTHESIS.md, S1–S7; its complete proof is included in the cumulative reader. This note proves the next receiving calculation, rather than assuming that a zero outside the critical line is an omitted arithmetic event.

## CD1. The full return record determines the original logarithmic derivative

Write \(R=\operatorname{End}_{\mathrm{Ab}}(L)\), with its orientation-independent identity \(\mathbf1_R=\operatorname{id}_L\), as constructed in CG4. For each nonzero prime ideal \(\mathfrak p\), its residue norm is
\[
N(\mathfrak p)=|R/\mathfrak p|.
\tag{CD1.1}
\]
CG5 identifies these norms with every positive prime integer, including two. Retain the three complete measures
\[
\mathcal D=\delta_0+\sum_{n\ge2}\delta_{\log n},\qquad
\mathcal R=\sum_p\sum_{k\ge1}\frac1k\delta_{k\log p},\qquad
\mathcal W=\sum_p\sum_{k\ge1}(\log p)\delta_{k\log p}.
\tag{CD1.2}
\]
The proof of \(\mathcal D=\exp_*\mathcal R\), including each coefficient and the unit atom, is TP9–TP13. For \(\operatorname{Re}s>1\) it gives
\[
\zeta(s)=\int e^{-st}\,d\mathcal D(t)
=1+\sum_{n\ge2}n^{-s}
=\prod_p(1-p^{-s})^{-1},
\tag{CD1.3}
\]
\[
H(s):=\int e^{-st}\,d\mathcal W(t)
=\sum_p\sum_{k\ge1}(\log p)p^{-ks}
=-\frac{\zeta'(s)}{\zeta(s)}.
\tag{CD1.4}
\]
Every displayed identity is on its convergence domain. In particular the prime sum is not asserted to converge at a nontrivial zero. To justify the derivative and all local termwise operations, on a compact set in \(\operatorname{Re}s>1\), choose \(\sigma_0>1\) below all its real parts. The sum with an additional fixed power of \(k\log p\) is bounded by a constant times
\(\sum_{n\ge2}(\log n)^j n^{-\sigma_0}\), with a possibly larger nonnegative integer \(j\). This converges by the integral test. The exponential of the absolutely convergent prime logarithm is nonzero on this half-plane, so logarithmic differentiation is justified there.

The complete record therefore determines one holomorphic germ \(H\) on that half-plane. Its meromorphic continuation is the indicated logarithmic derivative of the original meromorphic \(\zeta\). Two continuations on a connected domain agree by the identity theorem. This is analytic uniqueness from the full record, without a finite-prefix inference.

## CD2. Every zero is detected, with its original multiplicity

Let \(\rho\) be any actual nontrivial zero of the original \(\zeta\), of multiplicity \(m_\rho\). Holomorphic Taylor division gives, on a sufficiently small disk,
\[
\zeta(s)=(s-\rho)^{m_\rho}g_\rho(s),\qquad g_\rho(\rho)\ne0.
\tag{CD2.1}
\]
Shrinking the disk ensures \(g_\rho\) has no zero there. Direct differentiation of this original function gives
\[
H(s)=-\frac{m_\rho}{s-\rho}
-\frac{g_\rho'(s)}{g_\rho(s)}.
\tag{CD2.2}
\]
Consequently the positive counterclockwise boundary \(\gamma_\rho\) of that disk detects exactly
\[
-\frac1{2\pi i}\int_{\gamma_\rho}H(s)\,ds=m_\rho.
\tag{CD2.3}
\]
The second term in (CD2.2) is holomorphic, so its integral is zero; the first term has residue \(-m_\rho\). This proves (CD2.3). No step uses \(\operatorname{Re}\rho=1/2\).

The original pole at \(s=1\) is retained too. Writing \(\zeta(s)=(s-1)^{-1}g_1(s)\), with \(g_1(1)=1\), gives
\[
H(s)=\frac1{s-1}-\frac{g_1'(s)}{g_1(s)}.
\tag{CD2.4}
\]
Every original trivial zero \(-2r\), \(r\ge1\), gives residue \(-1\) in \(H\). Thus this scalar detector contains the pole and both types of zero, with their signs.

An off-line zero, if there is one, is consequently a zero detected by the same uniquely reconstructed record. It is not an extra prime, a fractional prime norm, or a prime-power event omitted from (CD1.2). The assertion follows from the actual detector (CD2.3), not from substituting another zeta function. Completeness determines all zero locations; it does not restrict the definition of detection to locations on the critical line.

## CD3. The full auxiliary multiplier and its contribution to the detector

The exact Mellin transform used for the source realization is
\[
F_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s).
\tag{CD3.1}
\]
It is the Mellin transform of the explicit original kernel
\[
k_0(u)=u^{1/2}\sum_{n\ge1}f_0(nu),\qquad
f_0(v)=\frac\pi2v^2(2\pi v^2-3)e^{-\pi v^2},
\]
under \(\mathcal Mk(s)=\int_0^\infty k(u)u^{s-1/2}\,du/u\). S2 proves this identity, entire continuation, and every exceptional value. In particular
\[
F_0(0)=F_0(1)=\frac18,
\]
\[
F_0(-2r)=\frac{r(2r+1)(-1)^r\pi^r}{2\,r!}\zeta'(-2r)
=\frac{(1+2r)(2r)}8\pi^{-(1+2r)/2}
\Gamma((1+2r)/2)\zeta(1+2r)\ne0.
\tag{CD3.2}
\]
This is an auxiliary source transform with an explicit comparison, not a replacement for the original function.

Let \(\psi=\Gamma'/\Gamma\). Logarithmic differentiation of the complete product, on the open set where its factors are nonsingular and nonzero, gives
\[
\boxed{
-\frac{\zeta'(s)}{\zeta(s)}
=-\frac{F_0'(s)}{F_0(s)}
+\frac1s+\frac1{s-1}
-\frac{\log\pi}{2}+\frac12\psi(s/2).}
\tag{CD3.3}
\]
Both sides are meromorphic, so the identity extends meromorphically. The constant \(1/8\) has derivative zero and remains in (CD3.1), (CD3.2), and every source projector below. At \(s=0\), the residues of \(1/s\) and \(\psi(s/2)/2\) cancel. At \(s=1\), the retained endpoint term has residue \(+1\). At \(s=-2r\), the Gamma logarithmic derivative has residue \(-1\), while (CD3.2) makes \(F_0'/F_0\) regular. At a nontrivial zero, the elementary and Gamma terms are regular and \(-F_0'/F_0\) has residue \(-m_\rho\). Thus the quotient detector and the full original detector agree on nontrivial zeros with every discarded-looking term accounted for explicitly.

## CD4. Detection inside the actual whole source quotient

For the following stronger detection statement, retain the exact function spaces
\[
\mathcal B=\{F\text{ entire}:b_{A,M}(F)=
\sup_{|\operatorname{Re}s|\le A}(1+|\operatorname{Im}s|)^M|F(s)|<\infty
\text{ for all integers }A,M\ge0\},
\]
\[
\mathcal I=\{F\in\mathcal B:F^{(j)}(\rho)=0
\text{ for every actual nontrivial zero }\rho,\ 0\le j<m_\rho\},
\qquad \mathcal Q=\mathcal B/\mathcal I.
\tag{CD4.1}
\]
The synthesis proof S5 identifies \(\mathcal I\) with the closed original source image; zeros have not been freely appended as extra states. The physical source space and full proof of this equality are included in the cumulative reader.

For a particular actual zero, put \(m=m_\rho\) and
\[
A_\rho(s)=\frac{F_0(s)}{(s-\rho)^m},\qquad
B_\rho(s)=\operatorname{Tay}_{\rho,<m}(1/A_\rho)(s),\qquad
e_\rho=A_\rho B_\rho.
\tag{CD4.2}
\]
Taylor division gives \(A_\rho(\rho)\ne0\). At \(\rho\) the product is \(1\) modulo \((s-\rho)^m\); at every other zero it has the full required vanishing order because its denominator is nonzero there. Division by a fixed linear factor of a vanishing entire strip-Schwartz function stays in \(\mathcal B\): outside a unit disk this follows by division, and inside it follows by Cauchy's maximum principle on a radius-two disk. Multiplication by a polynomial also preserves \(\mathcal B\). These facts establish \(e_\rho\in\mathcal B\) on the whole plane, not only on a finite test window.

The exact projector lift is
\[
\mathscr P_\rho F(s)=A_\rho(s)
\operatorname{Tay}_{\rho,<m}(F/A_\rho)(s).
\tag{CD4.3}
\]
Its output has all of the first \(m\) jets of \(F\) at \(\rho\) and all zero jets at every other zero. Taylor coefficients are continuous on \(\mathcal B\); hence this is a continuous finite-rank operator. A second application does not change its polynomial, so it is idempotent. It kills \(\mathcal I\) and defines \(P_\rho\) on \(\mathcal Q\). The vectors
\[
[e_\rho(s)(s-\rho)^j],\qquad 0\le j<m,
\tag{CD4.4}
\]
are independent because their derivative jets at \(\rho\) are respectively \(j!\) in position \(j\) and zero in the other positions. Their quotient classes span \(\operatorname{im}P_\rho\), since
\[
P_\rho[F]=\sum_{j=0}^{m-1}\frac{F^{(j)}(\rho)}{j!}
[e_\rho(s)(s-\rho)^j].
\]
At the representative level, the range of (CD4.3) is \(A_\rho\operatorname{Pol}_{<m}\); the displayed representatives agree with their projected representatives modulo \(\mathcal I\). Consequently \(\operatorname{rank}P_\rho=m\), and
\[
\bigcap_{\rho}\ker P_\rho=\{0\}.
\tag{CD4.5}
\]
Indeed the intersection forces all required jets to vanish, exactly the definition of \(\mathcal I\), which the synthesis theorem identifies with the original closed source image. No convergence of an infinite sum of projectors is asserted or needed. The complete resolvent and every source-level correction are proved in RZ3–RZ7.

Thus completeness of the quotient makes every actual zero detectable, including its multiplicity, independently of its location. An off-line zero would not fail (CD4.5); its own nonzero projector would be among the detectors proving that equality.

## CD5. The exact arithmetic weight seen by those detectors

Use a different symbol \(L_\zeta\) for the spectral operator to avoid confusing it with the winding group \(L\). It is induced by \(F(s)\mapsto sF(s)\). For every positive real \(a\), the actual action is
\[
T_a[F]=[a^sF(s)],\qquad
\mathcal M^{-1}T_a\mathcal Mk(u)=a^{1/2}k(u/a).
\tag{CD5.1}
\]
The multiplier preserves \(\mathcal B\), with seminorm factor \(\max(a^A,a^{-A})\), and preserves \(\mathcal I\), with every order unchanged. Substitution \(u=av\) in the Mellin integral proves the second identity including its factor. Composition gives \(T_aT_b=T_{ab}\) and \(T_1=I\).

On the range of \(P_\rho\), let \(N_\rho=L_\zeta-\rho I\). Multiplication by \(s-\rho\) shifts the vectors (CD4.4) to the next one, and kills the final one modulo \(\mathcal I\). Thus \(N_\rho^m=0\), \(N_\rho^{m-1}\ne0\), and Taylor expansion gives the full operator
\[
T_p|_{\operatorname{im}P_\rho}
=p^\rho\sum_{j=0}^{m-1}\frac{(\log p)^j}{j!}N_\rho^j,
\qquad |p^\rho|=p^{\operatorname{Re}\rho}.
\tag{CD5.2}
\]
Every logarithmic jet term remains present. The weight-one modulus is precisely the further assertion \(|p^\rho|=p^{1/2}\) for these actual blocks. Equation (CD5.2) proves that assertion is equivalent to \(\operatorname{Re}\rho=1/2\), for any one prime \(p>1\); it does not assume it from the source's unique supporting point.

## CD6. The retained reflection gives an exact degree factor, and exposes the sign

The original functional equation, with all factors retained in (CD3.1), gives the involution \(\rho^\#=1-\overline\rho\) with \(m_{\rho^\#}=m_\rho\). On \(\mathcal B\), \(F^\#(s)=\overline{F(1-\overline s)}\). The actual reflected form is
\[
W([F],[G])=\sum_{\rho}m_\rho\overline{F(\rho^\#)}G(\rho).
\tag{CD6.1}
\]
The sum is over distinct zeros, with multiplicity supplied by \(m_\rho\), and is absolutely convergent and continuous. For example strip decay of order two bounds the summand by a constant times \((1+|\operatorname{Im}\rho|)^{-4}\); the zero count from S2 is \(O((R+2)^{3/2})\). A dyadic decomposition makes the sum finite. RZ10 also gives the quotient seminorm bound and its exact radical. Direct substitution yields
\[
W(T_p x,T_p y)=pW(x,y),
\tag{CD6.2}
\]
because \(\overline{\rho^\#}+\rho=1\). Thus the similitude factor is already derived on the actual whole arithmetic quotient. It equals the prime norm \(p=|L/[p]L|\); no finite geometric morphism with degree \(p\) on this quotient is asserted by that equality.

Its sign is not supplied by that factor. The globally constructed vectors \(e_\rho\) have value one at \(\rho\) and zero at all other zeros. On a distinct reflected pair their actual form is
\[
\left.W\right|_{\langle[e_\rho],[e_{\rho^\#}]\rangle}
=\begin{pmatrix}0&m_\rho\\m_\rho&0\end{pmatrix},
\tag{CD6.3}
\]
as follows by inserting those two exact value functions in (CD6.1). In particular their difference has value \(-2m_\rho\). If a zero is fixed by reflection, its corresponding value vector instead has squared value \(m_\rho\). All higher multiplicity jets lie in the radical of this value form and remain nonzero elements of \(\mathcal Q\); no simplicity assertion is implicit.

The two eigenvalue moduli on a distinct reflected pair are exactly \(p^{\operatorname{Re}\rho}\) and \(p^{1-\operatorname{Re}\rho}\). Their product is \(p\), and (CD6.2) holds on that pair. The calculated negative direction and the calculated unequal moduli are two descriptions of the same potential obstruction in this particular quotient. The unique complete counting record has supplied the quotient, all these projectors, and this pairing. Its uniqueness has not changed (CD6.3) into a positive matrix.

## CD7. What follows for the proposed contradiction

The calculation establishes three connected facts. First, the complete reconstructed prime record determines the original zeta and hence every actual zero and multiplicity. Second, each such zero has an explicit nonzero projector in the source quotient; the joint kernel of all these projectors is zero. Third, the arithmetic action on those projectors has modulus \(p^{\operatorname{Re}\rho}\) and satisfies the reflected degree identity (CD6.2), with its sign fully calculated.

The detector identities prove that every actual zero has residue count \(m_\rho>0\) and a nonzero projector, with no restriction on its real part. Thus the proposed contradiction has not been derived: off-line location has not been shown to imply a failure of detection. This identifies the exact inference not established by the reconstruction; it does not discard the supporting geometry or the programme of deriving a weight theorem over it.

The integrality comparison is given in INTEGRAL_COUNTING_AND_WEIGHT_COMPARISON.md. Its exact connecting object is the integral group algebra of the multiplicative positive rationals, acting through (CD5.1). This retains integer arithmetic and the full prime scaling representation without falsely treating that representation as additive. No theorem of positivity or purity is introduced as a missing hypothesis.

## Sources and proof provenance

- Alain Connes and Caterina Consani, *The Absolute Twistor Line and the Geometry of* \(\overline{\operatorname{Spec}\mathbb Z}\), arXiv:2609.00299v1, original CC.tex, especially lines 494–615 and 772–904. The common generic support and actual signed stalk are inputs from this source, with the comparison proved in CG1–CG3. Public source: <https://arxiv.org/html/2609.00299v1#S3>.
- Alain Connes, *The Riemann Hypothesis: Past, Present and a Letter Through Time*, arXiv:2602.04022v1, original rhready.tex, lines 526–545. The source's complete multiplier is compared in S2 and (CD3.1); its factorization theorem is used with all genus-one factors in the full synthesis proof. Public source: <https://arxiv.org/abs/2602.04022>.
- Local complete derivations: CG0–CG8 and TP0–TP14; GLOBAL_MELLIN_SYNTHESIS.md S1–S7; GLOBAL_CANONICAL_MELLIN_INVOLUTION.md G1–G5; ORIGINAL_ZETA_RESOLVENT_AND_PROJECTORS.md RZ1–RZ12. These are programme derivations, not quotations or novelty claims. Their complete sources are retained in the cumulative local reader.

The disk index routes Deligne's original Weil I and Weil II to PDF-only records. They were not newly read as TeX in this calculation; no claim of reconstructing Deligne's proof is made here. The elementary integral comparison in the companion note is proved directly. A complete derivation of Deligne's machinery over the present source remains a different mathematical task from the detection result proved above.
